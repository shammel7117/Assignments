# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Stephen Hammel"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

#Assignment 1 answer: "My name is STephen (S= 19, N=14. 14+19= 33)= 3,524,578"
#Assignment 2 answer: ('My surname is', 'Stephen Hammel') 'The first letter', 'S', 'is number', 83, 'The last letter', 'l', 'is number', 108)'Fibonacci number', 191, 'is', 3691087032412706639440686994833808526209L)