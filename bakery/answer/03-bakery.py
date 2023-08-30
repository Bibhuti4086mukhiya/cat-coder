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

list_of_input=""" F 1 200 F 2 170 B 1 100 B 2 80 B 2 15 B 2 100 B 3 70"""
sales_payment=dayAndPayment(list_of_input)
sal=sales_payment[0]
pay=sales_payment[1]
print(sal,pay)
for i in pay:
    if i in sal:
        print(i)



for i in range(1,len(pay)):
    two_sum=int(pay[0])+int(pay[i])
    for k in range(len(sal)):
        if int(sal[k])==two_sum:
            del sal[k]

print(sal,pay)
for i in range(2,len(pay)):
    three_sum=int(pay[0])+int(pay[1])+int(pay[i])
    if str(three_sum) in sal:
        print(three_sum)

