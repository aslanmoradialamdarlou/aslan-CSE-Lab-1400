n = int(input())
a = n//2
if n > 2:
    flag = True
    for i in range(2,a+1):
        if n % i == 0 :
            flag = False
	    break
    if flag :
        print('Yes')
    else:
        print('No')
elif n == 2:
    print('Yes')
elif n == 1:
    print('we have no answer to this input')
