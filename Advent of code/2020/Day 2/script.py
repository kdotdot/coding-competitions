f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]
tot = 0
for line in lines:
    o = 0
    numbers, letter, password = line.split(' ')
    numbers = numbers.split('-')
    from_n = int(numbers[0])
    to_n = int(numbers[-1])
    letter = letter[0]
    for p in password:
        if p == letter:
            o += 1
    if o >= from_n and o <= to_n:
        tot +=1
        print(line,o,from_n,to_n)
print(tot)

