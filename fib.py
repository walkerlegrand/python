#this algorithm asks how many numbers of the Fibonacci sequence you would like
#generated and then it prints them out to the console

#Inspiration for idea came from www.practicepython.org
fibCnt = int(input("How many number of Fibonacci sequence?"))
a = 1
b = 1
temp = 0
fib = []
if(fibCnt >= 1):
    fib.append(1)
if(fibCnt >= 2):
    fib.append(1)
if(fibCnt >= 3):
    for x in range(2,fibCnt):
        fib.append(fib[x-1] + fib[x-2])
print(fib)
