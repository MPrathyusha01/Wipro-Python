num = int(input())
flag = False
if num>1:
    for i in range(2,num):
        if num%i ==0:
            flag = True
if flag:
    print("The number is not prime")
else:
    print("The number is Prime")