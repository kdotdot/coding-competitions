fi=open("submitInput.txt", "r")
fo=open("output.txt","w+")

f1 = fi.readlines()

f1.pop(0)
for i,l in enumerate(f1):
    l = int(l)
    d = l // 20
    r = l % 20
    res = 'IMPOSSIBLE' if r-(d*9) > 0 else str(d)
    fo.write('Case #{}: {}\n'.format(i+1,res))
