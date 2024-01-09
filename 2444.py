#2444
n = int(input())

for i in range(n):
    result = " "*(n-i)+ "*"(i+1) +" "*(n-i)
    print(result)

