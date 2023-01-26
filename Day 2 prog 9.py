month = input("enter the month : ")
day = int(input("enter the day: "))

if month in ('January', 'February', 'March'):
	season = 'winter'
elif month in ('April', 'May', 'June'):
	season = 'summer'
elif month in ('July', 'August', 'September'):
	season = 'spring'
else:
	season = 'fall'

if (month == 'March') and (day > 1):
	season = 'summer'
elif (month == 'June') and (day > 1):
	season = 'spring'
elif (month == 'September') and (day > 1):
	season = 'fall'
elif (month == 'December') and (day > 1):
	season = 'winter'

print("Season is",season)
