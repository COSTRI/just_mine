#lists
names = ['ama', 'trish', 'gau', 'talk']
print(names)
print(names[0])
print(names[2].title())
message = (f"I wouldnt mind if you {names[-1]} to me")
print(message)

#modify
names[1] = 'trishelle'
print(names)

#add
names.append('akosah')
print(names)

#creating from emptiness
you = []
you.append('nana')
you.append('moku')
you.append('karen')
print(you)

#inserting
names.insert(2, 'pokuaah')
print(names)

#removing
del names[-3]
print(names)

popped_name = names.pop(-2)
print(popped_name)
print(names)
new = (f"I dont want to {popped_name} to you")
print(new)

#names.remove('ama')
#print(names)

name = 'ama'
names.remove(name)
print(f"{name} is my first name")

#sort
#permanently
names.sort()
print(names)

#reverse-alpha
names.sort(reverse=True)
print(names)

#temporary
print(f"Here is the original list:\n {names} ")
print(f"Here is a sorted list:\n {sorted(names)}")
print(f"the old list:\n{names}")

#reverse-non_alpha
names.reverse()
print(names)

#for number of elements in a set use len()

#LOOPING
friends = ['nana yaa', 'deborah', 'richel', 'maaaa']
for friend in friends:
    print(friend)
    print(f"{friend.title()}, I will cherish you.")
    print(f"\t{friend.upper()}! Dont leave myside")

print(f"Thank you, everyone, \n For coming into my life")

#range
for value in range(1, 5):
    print(value)

numbers = list(range(2, 11, 2))
print(numbers)

squares = []
for value in range(1, 11):
    squares.append(value**2)
    #square = value **2
    #squares.append(square)
    print(squares)

#comprehension in range
squares = [value**2 for value in range(1, 11)]
print(f"\n{squares}")

#slicing a list
print(names[0:3])
print(friends[0:3])#basically means from the beginning to the 3rd elements

#looping through a slice
print(f"Hi, i am {names[-1].title()}, here are a list of my friends:")
for friend in friends[0:2]:
    print(friend.title())

#copying a list, use [:]
foods = ['waakye', 'rice', 'milk', 'fufuo']
friend_food = foods[:]
print(f"My foods are:\n {foods}")
print(f"My friend's foods are:\n {friend_food}")
#to show to that are diff but same append
foods.append('fried rice')
friend_food.append('ice cream')
print(f"My foods are:\n {foods}")
print(f"My friend's foods are:\n {friend_food}")

#TUPLE, instead of [] you use (), to define it
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#or
for dimension in dimensions:
    print(dimension)

#writing over a tuple
print(f"\nHere is the original dimension:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified lists:")
for dimension in dimensions:
    print(dimension)


#IF STATEMENTS
for name in names:
    if name == 'akosah':
        print(name.upper())
    else:
        print(f"not found")
    
#>>>name = 'Akosah'
#>>>name == 'akosah'
#False
#>>>name = 'Akosah'
#>>>name.lower() == 'audi'
#True
        
#checking for inequality
wanted = 'you'
if wanted != 'maaaa':
    print("Hold the maaaa!")

answer = 17
if answer != 42:
    print("That is not it")
 #if 151=150 then nothing will be printed. if not vice versa
    
#check whether a value is not in list
you = 'perverted angel'
if you not in friends:
    print(f"{you.title()}, \n I want you.")

#conditional
# press ctrl question mark to make a comment
age = 17
if age >= 18:
    print("You are old enough to fuck.\n Have you?")
else:
     print("Are you a virgin?\n Sorry, Dont fuck")

# if-elif-else
age = 12
if age < 4:
    print("You are too young")
elif age <= 18:
    print("You pay $100 to enter")
else:
    print("Too old to enter")


score = 65
if score < 40:
    grade = 'F'
elif score < 50:
    grade = 'E'
elif score < 60:
    grade = 'D'
elif score < 65:
    grade = 'C'
elif score < 70:
    grade = 'B'
else:
    grade = 'A'

print(f"Your grade is {grade}")#

wanted = ['you', 'perveted angel', ' maaaa']
for want in wanted:
    print(f"add {want}")
print("\n Here it is")

wanted = ['you', 'perveted angel', ' maaaa']
for want in wanted:
    if want == 'love':
        print("But you already have it.")
    else:
        print(f"add {want}")
    #print("\nFinished with your order")
        


#dictionary
alien = {'color': 'green', 'points': 5}
print(alien['color'])
print(alien['points'])

#adding new key value
alien['x_position'] = 0
alien['y_position'] = 25
print(alien)

#modifying
alien['color'] = 'red'
print(f"alien is now {alien['color']}")

#deleting
del alien['points']
print(alien)

#loop thru keys
fav_lang = {
    'prince': 'french',
    'maaaa': 'inimaticy',
    'kershia': 'german',
}
lang = fav_lang['maaaa'].title()
print(f"why do you like {lang}")