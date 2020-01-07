nu= int(input ("Enter N :"))
for i in range(0,nu):
    num=i
    result= 0
    n=len(str(i))
    while(i>0):
        digit=i%10
        result=result+digit**n
        i=i//10
    if num==result:
        print(num)