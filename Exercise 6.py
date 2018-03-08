# Pyhton programme that defines function 'factorial' which takes a positive input and gives its factorial as its output

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

print("The factorial of 5 is: ", factorial(5))
print("The factorial of 7 is: ", factorial(7))
print("The factorial of 10 is: ", factorial(10))