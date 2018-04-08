# Stephen Hammel
# A program that displays the smallest number divisible by 1-20 without leving a remainder (Euler Project Problem 5)

rangemax = 20
def div_check(n):
    for i in xrange(1,rangemax+1):
        if n % i == 0:
            continue
        else:
            return False
    return True

if __name__ == '__main__':
   num = 2
   while not div_check(num):
       print num
       num += 2
   print num
   
  #Answer= 232792560 
