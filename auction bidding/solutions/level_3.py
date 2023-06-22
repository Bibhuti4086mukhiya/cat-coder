def bidderAndBid(bid_list):
    if len(bid_list) != 0:
        bidder=bid_list.pop(0)
        bid=int(bid_list.pop(0))
    return bidder,bid

def bidderAndBidReadOnly(bid_list):
    if len(bid_list) != 0:
        bidder=bid_list[0]
        bid=int(bid_list[1])
        return bidder,bid

def main(bid_list):
    bid_list=bid_list.split(',')
    bid=1
    first_bid=bid
    price=bid_list.pop(0)
    open_bid=int(price)
    highest_bid=0
    bidder=''
    buyer=[]
    result=[]
    once='zero'
    if len(bid_list)==2:
        if bidder=='':
            result+=['-']
            result+=[str(open_bid)]
        bidder1,bid1 = bidderAndBid(bid_list)
        price=price.replace(price,str(bid1))
        bidder=bidder.replace(bidder,bidder1)
        result+=[bidder]
        result+=[str(price)]
        return result

    for i in range(0,(len(bid_list)),2):
        buyer+=[bid_list[i]]

    for i in buyer:
        if buyer[0]==i:
            b=True
        else:
            b=False
            break
    if b==True:
        if bidder=='':
            result+=['-']
            result+=[str(open_bid)]
            result+=[buyer[0]]
            result+=[open_bid]
        return result
    
    for i in range((len(bid_list)//2)-1):
        if len(bid_list) != 0:
            if bidder=='':
                result+=['-']
                result+=[str(open_bid)]

            bidder1,bid1 = bidderAndBid(bid_list)
            if len(bid_list) != 0:
                bidder2,bid2 = bidderAndBidReadOnly(bid_list)

            if highest_bid<bid1:
                highest_bid=bid1
                highest_bidder=bidder.replace(bidder,bidder1)


            if bid1>bid and first_bid==1:
                first_bid=0
                price=price.replace(price,str(int(open_bid)))
                bidder=bidder.replace(bidder,bidder1)
                result+=[bidder]
                result+=[price]

            if bid1<bid2 and highest_bid<bid2 and bidder1!=bidder2:
                price=price.replace(price,str(int(highest_bid)+int(bid)))
                bidder=bidder.replace(bidder,bidder2)
                result+=[bidder]
                result+=[price]

            if highest_bid<bid2:
                highest_bid1=highest_bid
                highest_bid=bid2
                highest_bidder=bidder.replace(bidder,bidder2)
            
            if highest_bid1<bid2 and bidder1==bidder2 and bidder1!=bidder:
                highest_bid=highest_bid1
                price=price.replace(price,str(int(highest_bid)+int(bid)))
                bidder=bidder.replace(bidder,bidder2)
                result+=[bidder]
                result+=[price]

            
            if bidder1==bidder2 and bidder1==bidder and bidder2==bidder and once=='once':
                continue

            elif bidder1==bidder2 and bidder1==bidder and bidder2==bidder:
                price=price.replace(price,str(int(bid1)+int(bid)))
                bidder=bidder.replace(bidder,bidder1)
                once='once'
                once=once.replace(once,once)
                result+=[bidder]
                result+=[price]

            
            if bid1==bid2:
                highest_bid=highest_bid
                price=price.replace(price,str(int(highest_bid)))
                bidder=bidder.replace(bidder,bidder1)
                result+=[bidder]
                result+=[price]
            
            if bid1<bid2 and bid2!=highest_bid and bidder1!=bidder2:
                price=price.replace(price,str(int(bid1)+int(bid)))
                bidder=bidder.replace(bidder,bidder2)
                result+=[bidder]
                result+=[price]

            if bid1>bid2:
                price=price.replace(price,str(int(bid2)+int(bid)))
                bidder=bidder.replace(bidder,bidder1)
                result+=[bidder]
                result+=[price]
                

    return result

inputValue='''1,nepper,15,hamster,24,philipp,30,mmautne,31,hamster,49,hamster,55,thebenil,57,fliegimandi,59,ev,61,philipp,64,philipp,65,ev,74,philipp,69,philipp,71,fliegimandi,78,hamster,78,mio,95,hamster,103,macquereauxpl,135'''
result=main(inputValue)
for i in result:
    print(i,end=',')