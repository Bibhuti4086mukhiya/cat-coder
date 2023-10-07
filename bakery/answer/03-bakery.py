def dayAndPayment(list_of_input):
    list_of_input=list_of_input.split()
    sales=[]
    payment=[]
    for i in range(0,len(list_of_input)):
        if list_of_input[i]=='F':
            sales+=[list_of_input[2+i]]
        if list_of_input[i]=='B':
            payment+=[list_of_input[2+i]] 
    return sales,payment

list_of_input="""F 1 995 F 2 884 F 3 749 F 4 866 
B 1 497 B 2 442 B 3 319 B 3 374 B 4 239 B 4 433 B 5 375 B 6 177"""
sales_payment=dayAndPayment(list_of_input)
sal=sales_payment[0]
pay=sales_payment[1]
both_sales_payment=list_of_input.split()
print(sal,pay)

remove_sal=[]
remove_pay=[]

p=None
for i in range(0,len(pay)):
    if p==None:
        single=int(pay[i])
    if p=='hi':
        single=int(pay[i-1])
    for k in range(len(sal)):
        if int(sal[k])==single:
            remove_sal+=[sal[k]]
            print(sal[k])
            print(pay[i])
            del pay[i]
            p='hi'

p=None
for i in range(1,len(pay)):
    if p==None:
        two_sum=int(pay[0])+int(pay[i])
    if p=='hi':
        two_sum=int(pay[0])+int(pay[i-2])
    for k in range(len(sal)):
        if int(sal[k])==two_sum:
            remove_sal+=[sal[k]]
            print(sal[k])
            print(pay[0],pay[i-1])
            del pay[0],pay[i-1]
            p='hi'

p=None
for i in range(2,len(pay)):
    if p==None:
        three_sum=int(pay[0])+int(pay[1])+int(pay[i])
    if p=='hi':
        three_sum=int(pay[0])+int(pay[1])+int(pay[i-3])
    for k in range(len(sal)):
        if int(sal[k])==three_sum:
            remove_sal+=[sal[k]]
            print(sal[k])
            print(pay[0],pay[1],pay[i-2])
            del pay[0],pay[1],pay[i-2]
            p='hi'

p=None
for i in range(3,len(pay)):
    if p==None:
        fourth_sum=int(pay[0])+int(pay[1])+int(pay[2])+int(pay[i])
    if p=='hi':
        fourth_sum=int(pay[0])+int(pay[1])+int(pay[2])+int(pay[i-4])
    for k in range(len(sal)):
        if int(sal[k])==fourth_sum:
            remove_sal+=[sal[k]]
            print(sal[k])
            print(pay[0],pay[1],pay[3],pay[i-3])
            del pay[0],pay[1],pay[3],pay[i-3]
            p='hi'

ans=set(sal).difference(set(remove_sal))
ans=list(ans)
result=[]
for i in range(len(ans)):
    for j in range(len(both_sales_payment)):
        if ans[i]==both_sales_payment[j]:
            result+=[both_sales_payment[j-1]]
result.sort()
print(result)