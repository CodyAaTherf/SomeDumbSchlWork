num = int(input("Enter a number: "))

if ((num % 5 == 0) and (num % 11 == 0)):
    print("{0} is divisible by 5 and 11".format(num))
else:
    print("{0} is not divisible by 5 and 11".format(num))