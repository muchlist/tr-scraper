"""

1. a setidaknya 1 kali
2. b persis 5 kali
3. c beberapa kali pasang
4. d atau e pada akhir kata

ex : aaaabbbbbccccd, aabbbbbcce

rgex = aa*bbbbb(cc)*(d|e)

aa*  :
    a setidaknya 1 kali dilanjut dengan a* yang artinya beberapa huruf a termasuk 0 a . dengan begitu
    digaransi bahwa setidaknya ada a 1 kali
bbbbb :
    5 b persis
(cc)* :
    dapat mempunyai sejumlah pasangan c atau 0 c
(d|e) :
    d atau e
"""