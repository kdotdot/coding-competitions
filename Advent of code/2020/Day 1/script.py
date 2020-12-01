f = open("input.txt", "r")
lines = f.readlines()
lines = [int(line.rstrip()) for line in lines]
for linei in lines:
    for linej in lines:
        if(linei+linej == 2020):
            print(linei, linej)
            print(linei*linej)
