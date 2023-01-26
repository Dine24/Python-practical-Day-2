y=float(input("enter a year:"))
if(y==19.47):
        print("enter a valid year")
elif(y==0):
    print("enter a valid year")
elif(y%400==0)&(y%100!=0):
    print("the given year is leap year")
elif(y%4==0):
    print("the given year is leap year")
else:
    print("the given year is not leap year")
