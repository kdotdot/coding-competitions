fi=open("submitInput.txt", "r")
fo=open("output.txt","w+")
c = int(fi.readline())
for case in range(c):
    n = int(fi.readline())
    best = set() #Un array que mantiene los mejores jugadores. Al final solo debe quedar 1
    nonValid = set()
    for match in range(n):
        l = fi.readline()
        l = l.split()
        l = [int(i) for i in l]
        a,b,r = l
        g = a if r==1 else b
        p = b if r==1 else a

        if g not in nonValid:
            best.add(g)
        best.discard(p)
        nonValid.add(p)

    print(best)
    fo.write("Case #{}: {}\n".format(case+1,best.pop()))
