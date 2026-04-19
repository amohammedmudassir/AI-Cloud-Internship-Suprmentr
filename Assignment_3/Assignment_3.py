#Assignment 3 (12/02/2026) 
#Smart Input Program Description : Build a Python program that takes name, age, hobby and prints a personalized message while categorizing age using conditionals

Name=input("Hello, what's your good name? ")
Age=int(input(" Let me know your age and i'll let you know few intresting facts!"))
Hobby=input("Whats your favourite hobby? ")
print(f"Yaay!! Nice to meet you {Name}! My name is Mudassir and am 21 years old.")
if Age < 18:
    print("You are a minor! Did you know that the legal drinking age in most countries is 18 or 21? Doesn't mean you can drink after all!") 
elif Age >=18 and Age < 30:
    print("You are a young adult! Did you know that the human brain continues to develop until around age 25?")
else:
    print("You are an adult! Hey Youngster, Did you know that the average life expectancy worldwide is around 72 years? So you got One Life Baby and less time to make it count!!")
print(f"That's great that you enjoy {Hobby}! Did you know that engaging in hobbies can reduce stress and improve mental health?")
