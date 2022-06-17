#permutation

def fF(lf, rg):
      print(f"L10 lf {lf}, rg {rg}, a {a}\n")
      input()
      if lf>=rg:
            print(a)
            return
      i= lf
      while i <= rg:
            print(f"L11 lf {lf}, rg {rg}, i {i}, a {a}\>
            a[i], a[lf] = fSw( a[i], a[lf])
            fF(lf+1 , rg)
            a[i], a[lf] =  fSw( a[i], a[lf])
            i+=1
def fSw(d_1, d_2):
      return d_2, d_1
a= ["a","b","c"]
fF(0, len(a)-1)
