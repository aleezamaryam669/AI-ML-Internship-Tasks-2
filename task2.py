#Part 1 – Collect Patient Information 
name = input("Enter Patient name :")
age = input("Enter patient age :")
weight = input("Enter patient weight (kg):")
height = input ("Enter patient height  (meters) :")
#Part 2 – Calculate Body Mass Index (BMI) 
new_weight = float(weight)
new_height = float(height)
BMI = new_weight/(new_height*new_height)
print(f"{BMI:.2F}")
if BMI < 18.5:
    category= "underweight"
    print(category)
elif BMI >= 18.5 and BMI <= 24.9:
    category="normalweight"
    print(category)
elif BMI >= 25.0 and BMI <= 29.9:
    category="overweight"
    print(category)
elif BMI >= 30.0:
    category= "obese"
    print(category)
new_age = int(age)
if BMI > 30 and new_age > 40:
    risk="Health risk: High Health Risk "
    print(risk)
else:
    risk ="Health Risk : Normal Risk" 
    print(risk)

    # Part 5 – Generate Health Report

print("\n===================================")
print("        HEALTH REPORT")
print("===================================")

print("Patient Name :", name)
print("Age :", new_age)
print("Weight (kg) :", new_weight)
print("Height (m) :", new_height)
print(f"BMI : {BMI:.2f}")
print("BMI Category :", category)
print("Health Risk :", risk)

print("\nHealth Advice :")

if category == "underweight":
    print("Increase calorie intake and consult a nutritionist.")
elif category == "normalweight":
    print("Maintain your current healthy lifestyle.")
elif category == "overweight":
    print("Increase physical activity and improve diet.")
elif category == "obese":
    print("Consult a healthcare professional and follow a weight management plan.")