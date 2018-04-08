#Stephen Hammel
#Collatz Conjecture assignment that displays the while loop results until it reaches 1

seq = []
x = (int(input("Add number:")))

while x > 1:
    if x % 2 == 0:
        x=x/2
    else:
        x = 3 * x + 1
    seq.append (x)
print seq
