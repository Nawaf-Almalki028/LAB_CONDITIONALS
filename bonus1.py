weight = input("How much do you weigh (kg): ")
heigh = input("How tall are you (cm): ")

weight = float(weight)
heigh = float(heigh) / 100

BMI = weight / (heigh ** 2)

print(f"Your BMI is: {round(BMI,2)}")
if BMI >=30:
    print("You are overwieght you need to work out more and watch your diet.")
elif BMI >=23:
    print("You are fit & healthy.")
elif BMI <23:
    print("You are underweight. Watch your health.")
else:
    print("Your are not a human anymore! sorry for that")