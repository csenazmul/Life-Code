
# Variable Declaration 
name = "Raju"           # String Type Variable
age = 32                # Integer Type Variable
height = 5.8            # Float Type Variable
is_student = True       # Boolean Type Variable (True or False)


# Type Conversion
x = 5
y = 3.8
z = "20"

a = float(x) # 5.0
b = int(y) # 3
c = int(z) # 20
print(a)
print(b)
print(c)



# Challenge: Write a program to swap two variables

p = 10
q = 20
# Before Change Variable
# print(f"Before Swap: p = {p}, q = {q}")
print("Before Swap: p =", p, ", q=", q)

# Swap Two Variable
temp = p        # p value in now temp
p = q           # q value in now p
y = temp
print(f"After Swap: p = {p}, q = {q}")
print("==========================End")

#  Create a temperature converter (Celsius to Fahrenheit)
# formula:  F = C * (9/5) + 32
# Create a temperature converter (Fahrenheit to Celsius)
# formula:  C = (F-32) * (5 / 9)

# c = int(input("Please Input Celsius value: "))
# f = c * (9/5) + 32
# print(f"Celsius: {c}°C Equal Fahrenheit: {f}°F")

f = int(input("Please Input Fahrenheit value: "))
c = (f - 32) * (5/9)
print(f"Fahrenheit: {f}°F Equal Celsius: {c}°C")


# x = "Bangladesh is a beautiful country. Bangla is our mother tongue."
# a = x.replace("Bangladesh", "USA", 1).replace("Bangla", "English")

# print(a)

# 1: এটি একটি ঐচ্ছিক আর্গুমেন্ট যা প্রতিস্থাপনের সংখ্যা নির্দেশ করে। এখানে 1 মানে হলো প্রথমবার "Bangla" দেখা গেলে সেটি "USA" দিয়ে প্রতিস্থাপন করা হবে।
# x = "Bangla is a beautiful country. Bangla is our mother tongue."
# a = x.replace("Bangla", "USA", 1)

# print(a)

# 2: এটি প্রতিস্থাপনের সংখ্যা নির্দেশ করে। এখানে 2 মানে হচ্ছে সর্বাধিক দুইবার "Bangla" প্রতিস্থাপিত করার চেষ্টা করবে।
# x = "Bangla is a beautiful country. Bangla is our mother tongue."
# a = x.replace("Bangla", "USA", 2)

# print(a)