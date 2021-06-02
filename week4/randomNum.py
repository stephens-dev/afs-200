import random

num = random.randint(1,9)

count = 0

while True:
    count +=1
    # try:
    #     check = int(input('Guess the number'))
    #     if check == num:
    #         break
    #     print('HA HA try again')
    # except Exception as e:
    #     print('Congratulations you guessed my number')
    print('Guress my number from 1-9')
    check = int(input('Guess the number '))
    if check == 0:
        break
    elif int(num) == int(check):
        print('Congratulations you guessed my number in',count,'trys press 0 to exit')
    else:
        print('HA HA try again')