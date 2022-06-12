def f(a, i):
      sb_lf = 0
      sb_rg = len(a) -1
      sb_m = sb_lf + (int( (sb_rg - sb_lf ) /2)
      while True:
            lf = sb_lf
            rg = sb_rg
            m = sb_m 
            if i < a[sb_m]:
                  sb_rg = sb_m -1
                  sb_m = lf + ( int( (m - lf ) /2)
            elif i > a[sb_m]:
                  sb_rg = sb_m -1
                  sb_m = rg - ( int( (rg - lf ) /2)
            else:
                  print(f"found it {i}, index {m}") 
            if lf >= rg :
                  print(f"DID NOT FIND IT {i}")
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(f"available numbers: {a}")
i = input()
f(a,i) 

#eror message:
#  File "d.py", line 5
#    while True:
#    ^
#SyntaxError: invalid syntax

