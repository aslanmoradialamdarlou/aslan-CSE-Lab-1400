n = int(input())
a = n//2
flag = True
for i in range(2,a+1):
    if n % i == 0 :
        flag = False
	break
if flag :
    print('Yes')
else:
    print('No')
