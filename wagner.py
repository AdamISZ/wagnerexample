#! /usr/bin/env python
import math
import hashlib
import sys
import binascii

def chunks(l, n=2):
    return [l[i:i + n] for i in range(0, len(l), n)]

hashmem = {}

def nhash(data):
    if data in hashmem:
        return hashmem[data]
    hashmem[data] = hashlib.sha256(data).digest()[:ntrunc]
    return hashmem[data]

def xor(a, b):
    return bytes(x^y for x, y in zip(a, b))

def xormulti(*vals):
    first = vals[:2]
    xorout = xor(*first)
    for val in vals[2:]:
        xorout = xor(xorout, val)
    return xorout

def nbitsmatch(n, l):
    return n & (2**l-1) == 0

def get_join(left, right, l):
    # given a list of 3-tuples left and right,
    # and a number of bits l,
    # return the list of (xor(str0, str1), el1, el2)
    # for which the lowest l bits in str0 and str1 match.
    x = []

    # for byte-aligned checking we have a quick way:
    if l % 8 == 0:
        bytesl = l // 8
        for a in left:
            al = a[0][-bytesl:]
            for b in right:
                if al == b[0][-bytesl:]:
                    x.append((xor(a[0], b[0]), a, b))
        return x
    # TODO: I presume this slower way can be much quicker:
    for a in left:
        for b in right:
            if nbitsmatch(int.from_bytes(xor(a[0], b[0]), byteorder="big"), l):
                x.append((xor(a[0], b[0]), a, b))
    return x

class Node(object):
    v = None
    def __init__(self, left, right, l):
        self.l = l
        self.left = left
        self.right = right
        self.v = get_join(self.left, self.right, self.l)

    def getv(self):
        """ For display purposes.
        """
        return [binascii.hexlify(x[0]).decode() for x in self.v]

def main(n, k, seed):
    l = n // int(math.log(k, 2)+1)
    print("calculated l: ", l)
    # need pairs of 2**l length lists for each base node
    def getlist(length, seed):
        x = []
        h = nhash(seed)
        for i in range(length):
            x.append((h, None, None))
            h = nhash(h)
        return x
    startlists = []
    for i in range(k):
        startlists.append(getlist(2**l, seed=seed + str(i).encode()))
    tree_depth = int(math.log(k, 2))
    basenodes = []
    for i in range(k//2):
        basenodes.append(Node(startlists[i*2], startlists[i*2+1], l))
    tree = []
    tree.append(basenodes)
    for height in range(1, tree_depth):
        tree.append([])
        for a, b in chunks(tree[height-1]):
            tree[height].append(Node(a.v, b.v, (height+1)*l))
    root = tree[height][0]
    # final step is to do an *in-list* (not cross-list) match
    # on the root node's value (.v) list; we expect about 1 match;
    # since we need only 1, we grab the first.
    for a in root.left:
        for b in root.right:
            if a[0] == b[0]:
                founda = a
                foundb = b
                break
    print("Got a match on: {} with {}, now finding preimages.".format(founda[0], foundb[0]))
    # now we traverse *down* the tree from the root to the basenodes, and find the basenode preimages
    matchvals = [founda, foundb]
    for i in range(1, tree_depth):
        newmatchvals = []
        for m in matchvals:
            newmatchvals.extend([m[1], m[2]])
        matchvals = newmatchvals
    print("We print out the calculation in detail:")
    hashes = []
    preimages = []
    for i in range(k):
        # to save space in earlier stages, we here retrieve
        # the preimage by iterating over the startlist:
        for p in startlists[i]:
            if nhash(p[0]) == matchvals[i][0]:
                preimages.append(p[0])
                hashes.append(matchvals[i][0])
                print("H({}) = {}".format(binascii.hexlify(p[0]).decode(),
            binascii.hexlify(hashes[-1]).decode()))
                break
    # now verify that these hashes xor to the correct value:
    print("Now we calculate the value of *all* those hashes xor-red together:")
    testval = xormulti(*hashes)
    print("resulting xor is: {}".format(testval))

if __name__ == "__main__":
    global ntrunc
    # how many bits in the hash function we're using:
    n = int(sys.argv[1])
    # how many bytes to truncate our base hash function to, to get
    # our test hash function:
    ntrunc = n // 8
    # how many values input to the k-sum problem:
    k = int(sys.argv[2])
    # some random data to start off our lists of hashes;
    # by using H(H(H(...H(seed)))..) iteratively, we can
    # keep using the same data set if we want:
    seed = sys.argv[3].encode("utf-8")
    main(n, k, seed)
