height = float(input("Enter your height in meter"))
weight = int(input("Enter your weight in kg"))

bmi = weight / (height * height)

if bmi <18.5:
    print(f"Your weight is {bmi}, and you a under weight.")

elif bmi <25:
    print(f"Your weight is {bmi}, and you have a normal weight.")

elif bmi < 30:
    print(f"Your weight is {bmi}, and you are slightly overweight.")

elif bmi <35:
    print(f"Your weight is {bmi}, and you are obese.")

else: 
    print(f"Your weight is {bmi}, and you are clinically obese.")