
# The body mass index (BMI) is calculated as a person's weight (in pounds) times 720 divided
# by the square of the person's height (in inches).  A BMI in the range 19 to 25, inclusive,
# is considered healthy.


import matplotlib.pyplot as plt
while True:
    print("\n\nThis Program will calculate your BMI\n")
    W = input(("Enter your weight in (Pounds): \n"))
    H = input(("Enter your height in (Inches): \n"))
    if (type(W) != int):
        print("\n\nSomething went WRONG with your input\nPlease, make sure you enter numbers!\n\n")
        continue
    else:
        break

X = 720 * W // (H ** 2)

if (X >= 19 and X < 25):
    print("\n\nYour BMI is: " , int(X) , "\nYou are considered healthy!")

elif(X >= 25 and X < 30):
    print("\n\nYour BMI is: " , int(X) , "\nYou are considered overweight.")

elif(X >= 30 and X < 40):
    print("\n\nYour BMI is: " , int(X) , "\nYour BMI is in the Obesity BMI range\nYou should consider seeing a doctor.")

elif(X >= 40):
    print("\n\n\nYour BMI is: " , int(X) , "\nYour BMI is in the EXTREM Obesity BMI range\nYou need to visit a doctor ASAP.")

else:
    print("\n\nYour BMI is: " , int(X) , "\nYour BMI is lower than the healthy BMI range\nYou should consider seeing a doctor.")
