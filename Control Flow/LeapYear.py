
# def LeapYear(year):
    
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print(f"This {year} is Leap Year.")
#             else:
#                 print(f"This {year} is not Leap Year.")
#         else:
#             print(f"This {year} is Leap Year.")
#     else:
#         print(f"This {year} is not Leap Year.")

year = int(input("Enter the Year Value: "))
# LeapYear(year)


if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"This {year} is Leap Year.")

else:
    print(f"This {year} is not Leap Year.")