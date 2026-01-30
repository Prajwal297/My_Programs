def is_leap(year):
    leap = False
    # Write your logic here
    if(1900<=year>=10**5 and year%4==0 or year%400==0):
        return True
    elif(1900<=year>=10**5 and year%100==0 and (year/100)%2==0):
        return leap
    else:
        return leap
year = int(input("enter the year :"))

