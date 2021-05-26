robert = ('robert','smith',1776,'patriot','farmer','west virgina')
nums = (1,2,3,4,5,3,5,3,2,5,6,7)

print(robert[0],nums[1:4])

csv = 'Eric,John,Michael,Terry,Grahm,TerryG,Brian'

friendsList = []

splitList=csv.split(',')

for i in range (len(splitList)):
    friendsList.append(splitList[i])

print(splitList)