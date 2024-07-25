print("Hello, World")
print("My name is Pelumi")

#ask user for their name
name = input("What is your name ").strip().title()

#remove white space from str
#name = name.strip().title()

#split user first name and last name
first, last = name.split(" ")

#Capitalise user's name
#name = name.capitalize()

#Capitalise user's name
#name = name.title()
print(name)

#Different ways to print
print(f"Hello",name)
print("Hello "+ name)
print("Hello", name)
print(f"Hello {last}")
print(f"Hello {first}")
