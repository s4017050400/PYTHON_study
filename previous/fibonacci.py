# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) , (n => 2)
#


def fibonacci(n):
    if n == 0 or n ==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        
        
#result

for i in range(20):
    print(fibonacci(i))
    
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
