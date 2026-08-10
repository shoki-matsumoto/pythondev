def fibonacci(n):
    fibli = [1,1] 
    while i < 100:
        fibli.append(fibli[i]+fibli[i+1])
        i += 1
    return fibli[n-1]