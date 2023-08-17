""" 
fizz_buzz Exercise

if divisible by 3, print Fizz (i.e. 3)
if divisible by 5, print Buzz (i.e. 5)
if divisible by 3 and 5, print FizzBuzz (i.e. 15)
esle return the same input (i.e. 7 returns 7)

"""


def fizz_buzz(input):
    """fizz-buzz determination method"""
    if (input % 3 == 0 and input % 5 == 0):
        return "FizzBuzz"
    if (input % 3 == 0):
        return "Fizz"
    if (input % 5 == 0):
        return "Buzz"
    return input


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
