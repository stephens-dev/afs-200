item = input('Enter a string')

count = 0
count2= 0

for i in item:
    if i.isupper():
        count = count+1
    elif i.islower():
        count2 = count2+1

print('The number of uppercase is', count)
print('The lowercase number is ', count2)