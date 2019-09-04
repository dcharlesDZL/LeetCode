def romanToInt(roman):
    sum = 0
    # romanNumber = 'mcm'
    romanDict = {'' : 0, 
                'I' : 1, 'i' : 1, 
                'V' : 5, 'v' : 5, 
                'X' : 10, 'x' : 10, 
                'L' : 50, 'l' : 50,
                'C' : 100, 'c' : 100,
                'D' : 500, 'd': 500,
                'M' : 1000, 'm' : 1000,}
    for i in range(len(roman)-2, -1, -1):
        if romanDict[roman[i]] < romanDict[roman[i+1]]:
            sum = sum + (-1)*romanDict[roman[i]]
        else:
            sum = sum + romanDict[roman[i]]
    return sum + romanDict[roman[len(roman)-1]]
    

print(romanToInt('CMXCIX'))
