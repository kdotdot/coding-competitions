fi=open("submitInput.txt", "r")
fo=open("output.txt","w+")
f1 = fi.readlines()
n = f1.pop(0)
for n,x in enumerate(f1):
    c = x.split()
    res = "-"
    if c[0] != c[1]:
        if (c[0]=='R' and c[1]=='S') or (c[0]=='P' and c[1]=='R') or  (c[0]=='S' and c[1]=='P') :
            res = c[0]
        else:
            res = c[1]
    fo.write("Case #{}: {}\n".format(n+1,res))
