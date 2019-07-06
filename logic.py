def length(b, g):
    for i in b:
        if i in g:
            b.remove(i)
            g.remove(i)
            return length(b, g)
    le = len(g) + len(b)
    return le
# -------------------------------------------
def remspc(s):
    lis = []
    for i in s.lower():
        if i.isalpha():
            lis.append(i)
    return lis
# --------------------------------------------

def rem(v,f):
    f.remove(f[v-1])
    f = f[v-1:] + f[:v-1]
    return f
#-----------------------------------
def final(n,f):
    if len(f)==1:
        return f
    else:
        v=n%len(f)
        if v==0:
            f.remove(f[-1])
            return final(n,f)
        elif v==1:
            f.remove(f[0])
            return final(n,f)
        elif v==2:
            f=rem(v,f)
            return final(n,f)
        elif v==3:
            f = rem(v, f)
            return final(n, f)
        elif v==4:
            f = rem(v, f)
            return final(n, f)
        else:
            f = rem(v, f)
            return final(n, f)
#------------------------------------