

def dayAndPayment(list_of_input):
    list_of_input=list_of_input.split()
    sales=[]
    for i in list_of_input:
        sales+=[list_of_input.pop(0)] 
    payment=list_of_input
    result=[]
    for i in range(2,len(sales),3):
        if sales[i]>payment[i]:
            print(payment[i-1])
            result+=[payment[i-1]]
    return result

list_of_input="""F 1 200 F 2 170 B 1 200 B 2 100"""


x=dayAndPayment(list_of_input)
for i in range(len(x)):
    print(x[i],end=' ')