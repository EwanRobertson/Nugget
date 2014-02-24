from datetime import date as dat

def getYear():
    year = input("Please enter the year that you were born. ")
    year = int (year)
    return age
    
def age(yearOfBirth):
    today = dat.today()
    thisYear = today.year
    age = thisYear - yearOfBirth
    return age
    
year = getYear()
print("you will be %s years old this year on your birthday" %age(year))
