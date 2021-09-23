print("Welcome to the BMI Calculator.")

bmi = 0

a = input("Please choose one of the following options:\n1. Metric\n2. Imperial\nEnter your option here: ")

if a == "Metric" or "metric":
    b = int(input("You have chosen the metric system. If this is correct, please enter 1. Otherwise, enter 0. "))
    if b == 1:
        cm = float(input("Please enter your height in centimeters: "))
        m = cm/100
        kg = float(input("Please enter your weight in kilograms: "))
        bmi = float((kg/m**2))
        print("Your BMI is {:.2f}".format(bmi))
        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 < bmi < 24.9:
            print("You are normal weight.")
        elif 25 < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")
    print("Thank you for using this BMI Calculator.")

elif a == "Imperial" or "imperial":
    c = int(input("You have chosen the imperial system. If this is correct, please enter 1. Otherwise, enter 0. "))
    if c == 1:
        lbs = float(input("Please enter your weight in pounds: "))
        ft = float(input("Please enter your height in feet and inches, starting with feet: "))
        ftin = (ft*12)
        inch = float(input("Please enter your height in feet and inches, continuing with inches: "))
        tot = (ftin + inch)
        bmi = float((lbs/tot**2)*703)
        print("Your BMI is {:.2f}".format(bmi))
        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 < bmi < 24.9:
            print("You are normal weight.")
        elif 25 < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")
    print("Thank you for using this BMI Calculator.")

else:
    print("You have entered an invalid option. Please try again.")
