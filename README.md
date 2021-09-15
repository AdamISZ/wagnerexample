### wagnerexample
Mock up of executing Wagner's attack in Python, for education.

### Arguments
* `n` is the number of bits in the hash (just made by truncating SHA256). It must be a whole number of bytes.
* `k` is the k as per the "k-sum problem" (generalized birthday problem). This must be such that `n/(lg(k)+1`, the parameter called `l` in the paper, is integer (it's the size of all the sample lists under examination, in pairs, at each height in the binary tree).
* `seed` is just some data to start a deterministic hash sequence.

### References

Blog post accompanying: https://reyify.com/blog/avoiding-wagnerian-tragedies

Original (full) paper of David Wagner: http://people.eecs.berkeley.edu/~daw/papers/genbday.html

### Usage example

This very quick to run example is: 8 byte hashes, xor-ing 128 preimages to
get a zero output.

```bash
me@here~$ python wagner.py 64 128 hello
calculated l:  8
Got a match on: 8dd2000000000000 with 8dd2000000000000, now finding preimages.
We print out the calculation in detail:
H(2b00a490e2208fd5) = 8a4fcc3356e3a454
H(76020db833d4d0ff) = 60f50931c34a3654
H(be91fe2d696f57fa) = 5516f25d356036c8
H(55272fa52341d8b6) = bdd6eed0da72a4c8
H(9e78cc9fd6af3bfa) = 9536af9589d41efe
H(b155dbd3908da70e) = c947e1723a18cefe
H(a167c059b0581ed2) = 362e32a07306f876
H(cd0f77fd95c30d65) = a6ff935f05712876
H(5965362acf096920) = ab65ef1fab778dfa
H(e696fa3179b0e462) = dc70474154a395fa
H(6c72107ec3f6709c) = 818ad9f6f795f4d6
H(727646f7e65d092e) = 5e304c26cfd5ecd6
H(d69cca8a84d1e250) = d2ec345a817ae999
H(dd8b24264668538a) = a7bc51097349ad99
H(cd2fe0b82b0aaa48) = 72ff26e756ba320a
H(439f99039dd82532) = 4caf38cadc1d760a
H(c15da927aadea0f4) = 470950b55a3c26f0
H(6aa6c864732859cd) = 5786bce602365cf0
H(363eb2eddc01b3a9) = 8c6f87dd6593db60
H(289c7ba5d02c7c96) = 68a4d0fd4b15a160
H(a5e47639bfaca046) = 250bc92548821595
H(05c27c76b720f70c) = d9584218ed2f2695
H(ddcd4667fc6c44f8) = 4b9175284bc26b69
H(c4a3f4ee9ee99a4d) = b6d6afcf8ae35869
H(4285decdb3ca22e3) = 86b92b1308320a8d
H(d6d6047abdb6301c) = 5194f15485a6698d
H(8cca7540a6a0d768) = 5c8e9aa6a46686b3
H(684b77922399eca3) = 2e45e6dec8c3e5b3
H(06d651adc1143a98) = 74499f0cd959ff24
H(4ed86baf0e530583) = 07d4df8175817024
H(bd5673c0174b7df9) = 901a75a2a007323e
H(57f3b9a496e8a14a) = c1c77cdeffeebd3e
H(9a2d587d8fa5965b) = 436be9cd9c185c7b
H(5cafacd7fb98a291) = 8a8417b64a744c7b
H(57e811f502817833) = da4fe9d0eee602af
H(f17128f2aed07ee1) = a9f4ba47d1aa12af
H(48854b9c6d4131ee) = eae0607242298249
H(5b8e747bd2594b8a) = cfd39a07bfa83349
H(d064a139bf05e1d9) = c2111ac4f6d5a41c
H(48c92f76dc7b5972) = 197caae77574151c
H(28b17277a3fb7dd3) = e861bdea2962458d
H(b8d990eb1246aef3) = d0efcdd7a7aded8d
H(e18ccbb2a1adfd13) = 1f83d0a6cd617c93
H(2f2c6a756e333c77) = 6109e5830813d493
H(8227e26ffdc6f4a3) = 74738e5da9a96432
H(0cc4516d2a7df78b) = 4d5560cdd2840d32
H(d0c9b88962f3c916) = c056e11285dc21de
H(3ed14fef9b54a42b) = 6cdf1da8224c48de
H(134ee8b70b02722f) = d179f96fb3238bcb
H(99a67efcc4c67a98) = ec47aac9be6ccfcb
H(36995c55c4b59da3) = 01347b0684a94ca3
H(24ef68e0abc48fae) = b58162a4fdc808a3
H(afbdb0bf0f5b82ad) = 17fbbfdeb7711261
H(9601ca37d82b172e) = 3ee461cb4e81e561
H(d77a5bd2fc428eb9) = 570967eea4a60f3b
H(bc7bb95d120904f3) = de808645e278f83b
H(2e6ee30ab7ec354a) = 811c8b71f402df0b
H(9799a1a40d312962) = 84b566dafbca5a0b
H(dd2f80397ecc1b8b) = 96fe348cddf27dac
H(de92236b47017bab) = ecc5e92ae0d9f8ac
H(447a137125bc2c74) = e4d70e278b16472d
H(2f107207d7061e63) = fcde51ca5421892d
H(93e0521467691f45) = 09e24c8da2a690af
H(28689cab5725758e) = 0294935f84725eaf
H(9942ef3e38fee3e7) = bcfeb6a64f37c56f
H(90e1c1166d00ff17) = e3dc2d50e695736f
H(8a8d41ed58d442b6) = dcd0c89961ab7ccb
H(3907cc2de83dad73) = 1534c7ae1f78cacb
H(02aa60f3308f1c0c) = 4b63952b83eed6c0
H(87147fd94978ee02) = c7c18b3791147fc0
H(11d7ed6b33633bc0) = 22c43486297517a5
H(0381da8a28768e75) = c2daefb0eefebea5
H(c48e8da752e3a1eb) = 03ce917f3d9c5570
H(1b276056100fa441) = 4747334ca64f3670
H(ed1f4e215ddb8921) = 7455fccd2ce5cdaa
H(3f4aa4870a457692) = 7ef8b78e36c7aeaa
H(f50f0c77f4cad283) = 84cb625b14562444
H(f2c2903cdf69ea4d) = 4fd10abf9c44e644
H(beb72e746d22f61c) = 5bde37289fe53704
H(7ad4ec4ab5d67537) = 35b6dfd49406f504
H(3db2be58c831b857) = 7e28f97491ec2536
H(8bf13bf1323d676c) = 8d9a1040593c3536
H(2d1b8613e58127be) = 1fbdaba38c03b5ca
H(1591e9c2ef2b5f94) = 2b45ee4a0e4ba5ca
H(b4a895c9a6892a1a) = 0d8b7595314f5962
H(290f7a204cb76e9b) = f733b613f8f37162
H(f44280bc4440448d) = a80bca5f198825c8
H(d56cd0cd84f9e864) = b7719d19b1ac0dc8
H(a33484822ffdccc7) = 153963d96d013b7e
H(f21f8ebe53f66606) = 19746826390d9c7e
H(bf73bc74e0096417) = bd2b5aad5568288a
H(12ddb41fdadb928a) = 3b2c2787ced78f8a
H(ac4057132042316f) = 233b1f7d5f209e6e
H(fa46b242ef29b97c) = 9e1737eaf272fb6e
H(45c4a2ac6820ef78) = 49df04adea1691d3
H(6133376050503b18) = 2fa70a71a3f7f4d3
H(77228112402a4d93) = 5cf6a83febff61da
H(0370caa5df43e1e0) = 61133829b0fdceda
H(3245f42f7caa444f) = c422c81cf590cf42
H(1739db0e8b0b5482) = 3621a23836656042
H(8c439470a15e2042) = 5a7240803a523687
H(13b94f176d0ae13e) = 1a01dcacbdd81987
H(dc7c87f0690a3c71) = f7938815b7a37d1a
H(5b5bea42ed487ed3) = 75b78e710fde521a
H(0bdb214f398b6ed7) = 6a803848fafa87a3
H(39a7ff463f4e1d4c) = 58469b2e215866a3
H(b334b88aa3e10f79) = 8b23f95872de6521
H(47a126231666e2dd) = a96b3c21df048421
H(fd4d19eaa3f88f8a) = ef46bc9912390d74
H(56fe9958cea5494c) = 8bc0e5a703acd674
H(7aaebcfdfd6ea6a7) = 85a38780e47efb6d
H(72592553ca7215c4) = d2b0dedd2493206d
H(7a6ea552c69b77b5) = 03e2d542a430a03c
H(4fe369ead4b6fb9a) = 842e337f820d743c
H(5f60050574b35ee1) = 5cfad8a91b7cac04
H(56b1f48e2e28fb79) = 0ede8c25b4b67804
H(220f72938e5c1355) = 193c3552b8561f88
H(0a3e90459cb1014f) = 52d0084d3c6ee688
H(675fc28b8f19949f) = a5806266d6e919a5
H(6bf0e689d242a45e) = 78734bba6626e0a5
H(d6e1db8f5972a1f6) = b38a0093099bf485
H(8d249659aaf6ee3e) = e2ffe811ab83e685
H(a5b6626234a56c84) = 1371027912799859
H(e4e3a948634579e4) = c7e72c9d67548a59
H(e6f5b33c2c92ad7f) = 74953455b29f8e76
H(dface84304900306) = 1b226521af47d076
H(d000729f16c98d76) = dc01560cce3c962c
H(3c1854bc0368313d) = b460316ab9d1c82c
Now we calculate the value of *all* those hashes xor-red together:
resulting xor is: 0000000000000000
```
