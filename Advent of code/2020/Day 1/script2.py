f = open("input.txt", "r")
lines = f.readlines()
lines = [int(line.rstrip()) for line in lines]
for linei in lines:
    for linej in lines:
        for linek in lines:
            if(linei+linej+linek == 2020):
                print(linei, linej, linek)
                print(linei*linej*linek)
