def getYear () :
    year = input
    year = int (year)
    return year
    
def age (yearOfBirth) :
    today = dat.today()
    thisYear = today . year
    age = thisYear - yearOfBirth
    return age
