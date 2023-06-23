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

            if bidder1==bidder2 and bidder1==bidder and bidder2==bidder and once=='once':
                once='zero'
                continue


            if bidder1==bidder2 and bidder1==bidder and bidder2==bidder:
                price=price.replace(price,str(int(bid1)+int(bid)))
                bidder=bidder.replace(bidder,bidder1)
                once=once.replace(once,once)
                result+=[bidder]
                result+=[price]


            if bid1<bid2 and highest_bid<bid2 and bidder1!=bidder2:
                price=price.replace(price,str(int(highest_bid)+int(bid)))
                bidder=bidder.replace(bidder,bidder2)
                result+=[bidder]
                result+=[price]
                once='once'

            if highest_bid>bid2:
                price=price.replace(price,str(int(bid2)+int(bid)))
                bidder=bidder.replace(bidder,highest_bidder)
                result+=[bidder]
                result+=[price]
                continue
                
            if highest_bid<bid2:
                highest_bid1=highest_bid
                highest_bid=bid2
                highest_bidder=bidder.replace(bidder,bidder2)



            if bid1<bid2 and bid2!=highest_bid and bidder1!=bidder2:
                price=price.replace(price,str(int(bid1)+int(bid)))
                bidder=bidder.replace(bidder,bidder2)
                result+=[bidder]
                result+=[price]


            if highest_bid1<bid2 and bidder1==bidder2 and bidder1!=bidder:
                highest_bid=highest_bid1
                price=price.replace(price,str(int(highest_bid)+int(bid)))
                bidder=bidder.replace(bidder,bidder2)
                result+=[bidder]
                result+=[price]
            
            if bid1==bid2:
                highest_bid=highest_bid
                price=price.replace(price,str(int(highest_bid)))
                bidder=bidder.replace(bidder,bidder1)
                result+=[bidder]
                result+=[price]
            
            if bid1>bid2:
                price=price.replace(price,str(int(bid2)+int(bid)))
                bidder=bidder.replace(bidder,bidder1)
                result+=[bidder]
                result+=[price]
                
    return result

inputValue='''1,rx,50,aa,2000,de,3558,einseins,3999,ek,4999,yd,8332,lb,5000,lb,6000,lb,7000,lb,8000,lb,8999,yd,9999,zn,11000,ir,11110,nr,12999,kt,12567,kt,12667,kt,13000,go,14000,ym,14999,hm,15400,nr,15690,nr,17000,td,18500,kt,18750,uy,18850,hr,18999,td,19049,st,19200'''
result=main(inputValue)
for i in result:
    print(i,end=',')