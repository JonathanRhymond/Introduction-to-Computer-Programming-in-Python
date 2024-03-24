#1
def foo_1(n):
  if n > 0:
    return "Positive"
  if n < 0:
    return "Negative"
  if n == 0:
    return "Zero"

#2
def fizz_buzz(n):
  if n % 3 == 0 and n % 5 == 0:
    return "FizzBuzz"
  if n % 3 == 0 and n % 5 != 0:
    return "Fizz"
  if n % 3 != 0 and n % 5 == 0:
    return "Buzz"
  if n % 3 != 0 and n % 5 != 0:
    return n