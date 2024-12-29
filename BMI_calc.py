que = input("do you want to calculate BMI in metric system??")
yes=True
if que==yes:
   h = float(input("enter your height( in meters)"))
   w = float(input("enter your weight (in kilograms)"))
   BMI= w/(h**2)
   print("BMI = ",BMI)
else :
   h = float(input("enter you height(in inches)"))
   w = float(input("enter your weight (in pounds)"))
   BMI= (w/(h**2))*703
   print("your body mass index(BMI) is : ",BMI)