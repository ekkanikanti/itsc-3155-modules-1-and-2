string = input('Enter a string: ')
lowerFirst = ""

for x in string:
    if (x.islower() == True):
        lowerFirst += x

for y in string:
    if (y.islower() == False and y.isspace() == False):
        lowerFirst += y

print(lowerFirst.strip())