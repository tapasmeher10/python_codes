def findgcd(a, b):
    if (b == 0):
        return a;
    else:
        return findgcd(b, a % b)


num1 = float(input(" Please Enter the First Value  Num1 : "))
num2 = float(input(" Please Enter the Second Value Num2 : "))

gcd = findgcd(num1, num2)
print("\n GCD of {0} and {1} = {2}".format(num1, num2, gcd))