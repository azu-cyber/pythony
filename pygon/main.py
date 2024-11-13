def romanToInt(romanInput):
    roman = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    resultInteger = 0
    for i in range(0, len(romanInput) - 1):
        if roman[romanInput[i]] < roman[romanInput[i+1]]:
            resultInteger -= roman[romanInput[i]]
        else:
            resultInteger += roman[romanInput[i]]
    return resultInteger + roman[romanInput[-1]]
roman = input("Input roman numeral : ")
print ("Integer equivalent : ",romanToInt(roman))
#binary to decimal
n=10
bin=n
dec=0
base=1
while n>0:
    rem=n%10
    dec=dec+rem*base
    base=base*2
print("The decimal value is ",dec)