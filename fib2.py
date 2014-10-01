def fib(n,m):
   if n <= 2:
      return 1
   else:
      return fib(n-1, m) + fib(n-2, m)  - (fib(n-m,m)-fib(n-m-1,m) )

print fib(6,3)



