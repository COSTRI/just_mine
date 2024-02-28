
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == cars:
       print(car.upper())
    else:
        print(car.title())


#Checking for inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
    print(requested_topping)


#Numerical comparisons
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

#checking whether a value is not in a list
banned_users = ['moi', 'lina', 'tina']
user = 'lila'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")

#simple if statements
age = 19
if age >= 18:
    print("You are old enough to vote!")


#if-else statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as you turn 18!")


#if-elif-else chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40.")

age = 12
if age < 4:
    price = 0#lif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

#using multiple elif blocks
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}")

#omitting the else block
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 3
elif age < 65: #to omit the 'else' you bring 'elif' then '>='
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost price is ${price}")

#Testing muliple conditions
requested_music = ['k-pop', 'pop']
if 'k-pop' in requested_music:
    print("Playing k-pop.")
if 'mandopop' in requested_music:
    print("Playing mandopop.")
if 'pop' in requested_music:
    print("Playing pop .")
print("\nFinished playing music")

#the code above wont work if 'elif' was used
requested_music = ['k-pop', 'pop']
if 'k-pop' in requested_music:
    print("Playing k-pop.")
elif 'mandopop' in requested_music:#elif
    print("Playing mandopop.")
elif 'pop' in requested_music:#elif
    print("Playing pop .")
print("\nFinished playing music")