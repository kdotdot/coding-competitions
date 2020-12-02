f = open("input.txt", "r")
lines = f.readlines()
lines = [line.rstrip() for line in lines]
tot = 0
for line in lines:
    o = 0
    numbers, letter, password = line.split(' ')
    numbers = numbers.split('-')
    valid = int(numbers[0])
    invalid = int(numbers[-1])
    letter = letter[0]
    if (password[valid-1] == letter and not password[invalid-1] == letter) or (not password[valid-1] == letter and password[invalid-1] == letter):
        print(line)
        tot+=1
print(tot)

