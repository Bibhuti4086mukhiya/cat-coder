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
    highest_price=int(price)
    open_bid=int(price)
    highest_bid=0
    highest_bidder=''
    bidder=''
    buyer=[]
    result=[]
    if len(bid_list)==2:
        if bidder=='':
            result+=['-']
            result+=[str(bid)]
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
            result+=[str(bid)]
            result+=[buyer[0]]
            result+=[open_bid]
        return result
    
    for i in range((len(bid_list))-1):
        if len(bid_list) != 0:
            if bidder=='':
                result+=['-']
                result+=[str(bid)]

            bidder1,bid1 = bidderAndBid(bid_list)
            if len(bid_list) != 0:
                bidder2,bid2 = bidderAndBidReadOnly(bid_list)

            if highest_bid<bid1:
                highest_bid=bid1

            if bid1>bid and first_bid==1:
                first_bid=0
                price=price.replace(price,str(int(bid)))
                bidder=bidder.replace(bidder,bidder1)
                result+=[bidder]
                result+=[price]

            if bid1<bid2 and highest_bid<bid2:
                price=price.replace(price,str(int(highest_bid)+int(bid)))
                bidder=bidder.replace(bidder,bidder2)
                result+=[bidder]
                result+=[price]

            if highest_bid<bid2:
                highest_bid1=highest_bid
                highest_bid=bid2
            
            if highest_bid1<bid2 and bidder1==bidder2 and bidder1!=bidder:
                highest_bid=highest_bid1
                price=price.replace(price,str(int(highest_bid)+int(bid)))
                bidder=bidder.replace(bidder,bidder2)
                result+=[bidder]
                result+=[price]
            
            if bid1<bid2 and bid2!=highest_bid:
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

inputValue='''1,A,5,B,10,A,8,A,14,A,17,B,17'''
result=main(inputValue)
for i in result:
    print(i,end=',')