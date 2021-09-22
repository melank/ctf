# https://play.picoctf.org/practice/challenge/144

q = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}"
lcs = 'abcdefghijklmnopqrstuvwxyz'
ucs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''

for c in q:
    i = 0
    t = ''
    if c in lcs:
        i = lcs.index(c)
        t = lcs[(i + 13) % 26]
    elif c in ucs:
        i = ucs.index(c)
        t = ucs[(i + 13) % 26]
    else:
        t = c

    result += t

print(result)