nums = []

while len(nums) < 3:
    temp = int(input('please give a number'))
    nums.append(temp)


def maxing():
    print('The largest number is', max(nums))
    nums.remove(max(nums))
    print('The smallest number is', min(nums))
    nums.remove(min(nums))
    print('And the middle number is', nums[-1])
maxing()
