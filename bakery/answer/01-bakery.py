
def dayAndPayment(list_of_input):
    list_of_input=list_of_input.split()
    sales=[]
    for i in list_of_input:
        sales+=[list_of_input.pop(0)] 
    payment=list_of_input
    result=[]
    for i in range(2,len(sales),3):
        if int(sales[i])>int(payment[i]):
            result+=[payment[i-1]]
    return result

list_of_input="""F 1 739 F 2 164 F 3 227 F 4 778 F 5 423 F 6 538 F 7 155 F 8 425 F 9 878 B 1 739 B 2 164 B 3 227 B 4 778 B 5 423 B 6 538 B 7 155 B 8 425 B 9 878"""

x=dayAndPayment(list_of_input)
for i in range(len(x)):
    print(x[i],end=' ')