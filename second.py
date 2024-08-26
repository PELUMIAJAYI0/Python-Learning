'''
print("before")
if 0>1:
    thif
print("after")

a = """i am fine
        how are you
        thank you"""
print(a)


cgpa = float(input("What is your CGPA---> "))

if cgpa >= 0 and cgpa <= 5:
    if cgpa >=4.5:
        print("You are on first class")
    elif cgpa>=3.5:
        print("You are on second class upper")
    elif cgpa>=2.5:
        print("You are on second class lower")
    elif cgpa>=1.5:
        print("You are on a Pass")
    else:
        print("you are a graduate")
else:
    print("Your CGPA is out of range...")

'''

workHour = int(input("Input the number of hours you worked today---> "))

if workHour >6:
    print("You have a reward of 12,000 Naira")
elif workHour >5:
    print("You have a reward of 10,000 Naira")
elif workHour >4:
    print("You have a reward of 8,000 Naira")
elif workHour >3:
    print("You have a reward of 5,000 Naira")
elif workHour >2:
    print("You have a reward of 4,000 Naira")
