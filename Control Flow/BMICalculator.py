
def bmi_calculator(weight_kg, height_cm):
    # Convert CM to Meter
    height_m = height_cm / 100

    print(f"Height Value of (M): {height_m:.2f}")

    # BMI Formula
    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        status = "Under Weight"
    
    elif 18.5 <= bmi < 24.9:
        status = "Normal Weight"

    elif 25 <= bmi < 29.9:
        status = "Over Weight"
    # elif bmi>= 30:
    #     status = "Obese"
    else:
        status = "Obese"
    
    return bmi, status
    # return bmi, status, height_m


weight_kg = float(input("Please Enter the Weight Value of (KG): "))
height_cm = float(input("Please Enter the Height Value of (CM): "))


bmi, status = bmi_calculator(weight_kg, height_cm)
# bmi, status, height_m = bmi_calculator(weight_kg, height_cm)

# print(f"Height Value of (M): {height_m:.2f}")
print(f"BMI Result: {bmi:.2f}")
print(f"BMI Status: {status}")
