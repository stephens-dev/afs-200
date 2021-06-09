import random

num = random.randint(1,20)

count = 0

while True:
    count +=1
  
    print('Guess my number from 1-20')
    check = int(input('Guess the number '))
    if check == 0:
        break
    elif int(num) == int(check):
        print('Congratulations you guessed my number in',count,'trys press 0 to exit')
    elif int(num) <= int(check) -5:
        print('Your are way to high')
    elif int(num) >= int(check) + 5:
        print('You are way to low')
    elif int(num) < int(check):
        print('You are a little high')
    elif int(num) > int(check):
        print('You are a little low')
    else:
        print('HA HA try again')