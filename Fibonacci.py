print("Fibonacci series code")
print("________________________")
fibo = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if fibo <= 0:
   print("Please enter a positive integer")
elif fibo == 1:
   print("Fibonacci sequence upto",fibo,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < fibo:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1