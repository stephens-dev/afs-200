num=input('What is your number')


if int(num) % 4 == 0 :
    print("And a multible of four")
elif int(num) % 2 == 0 :
    print("Your number is even")
else :
    print("Your number is odd")
# num='What is your first number'
check=input('What is your second number')

if int(num) % int(check) == 0 :
    print('These numbers divide evenly')
else : 
    print('The numbers do not divide evenly')
