def bidderAndBid(bid_list):
    if len(bid_list) != 0:
        bidder=bid_list.pop(0)
        bid=int(bid_list.pop(0))
    return bidder,bid

def main(bid_list):
    bid_list=bid_list.split(',')
    bid=1
    price=bid_list.pop(0)
    highest_price=int(price)
    open_bid=price
    highest_bid=int()
    highest_bidder=''
    bidder=''
    buyer=[]
    if len(bid_list)==2:
        bidder1,bid1 = bidderAndBid(bid_list)
        price=price.replace(price,str(bid1))
        bidder=bidder.replace(bidder,bidder1)
    
    for i in range(0,(len(bid_list)),2):
        buyer+=[bid_list[i]]

    for i in buyer:
        if buyer[0]==i:
            b=True
        else:
            b=False
            break
    if b==True:
        return buyer[0],open_bid
    
    for i in range((len(bid_list)//2)-1):
        if len(bid_list) != 0:
            bidder1,bid1 = bidderAndBid(bid_list)

            highest_price=int(price)
            if bid1>highest_bid and bidder=='G':
                price=price.replace(price,str(highest_price + int(bid)))
                highest_bidder=highest_bidder.replace(bidder,bidder1)
                return highest_bidder,price
            
            if bid1>highest_bid:
                highest_bid=bid1 
                price=price.replace(price,str(bid1 + int(bid)))
                highest_bidder=highest_bidder.replace(bidder,bidder1)

            if len(bid_list) != 0 and str(bidder) != str(bid_list[0]):
                bidder2,bid2 = bidderAndBid(bid_list)
                if bid2>highest_bid:
                    highest_bid=bid2 
                    price=price.replace(price,str(bid2 + int(bid)))
                    highest_bidder=bidder.replace(bidder,bidder2)
                    bidder=bidder.replace(bidder,bidder2)

                if bid2<bid1:
                    price=price.replace(price,str(bid2+int(bid)))
                    bidder=bidder.replace(bidder,bidder1)

                if bid2>bid1:
                    price=price.replace(price,str(bid1 + int(bid)))
                    bidder=bidder.replace(bidder,bidder2)

                if bid2 == bid1:
                    price=price.replace(price,str(bid1))
                    bidder=bidder.replace(bidder,bidder1)

            if len(bid_list) != 0 and str(bidder1) == str(bid_list[0]):
                bidder2,bid2 = bidderAndBid(bid_list)
                highest_bid=int(open_bid)
                price=price.replace(price,str(highest_bid))
                highest_bidder=bidder.replace(bidder,bidder2)
                bidder=bidder.replace(bidder,bidder2)
               
            if len(bid_list) != 0 or bidder2!=''and bid2!='':
                if bid1 < bid2:
                    price=price.replace(price,str(bid1 + int(bid)))
                    bidder=bidder.replace(bidder,bidder2)
                if bid1 > bid2:
                    price=price.replace(price,str(bid2 + int(bid)))
                    bidder=bidder.replace(bidder,bidder1)
                if bid2 == bid1:
                    price=price.replace(price,str(bid1))
                    bidder=bidder.replace(bidder,bidder2)
                    
        if len(bid_list) != 0 or bidder2!=''and bid2!='':
            if bid1 < bid2:
                price=price.replace(price,str(bid1 + int(bid)))
                bidder=bidder.replace(bidder,bidder2)
            if bid1 > bid2:
                price=price.replace(price,str(bid2 + int(bid)))
                bidder=bidder.replace(bidder,bidder1)
            if bid2 == bid1:
                price=price.replace(price,str(bid1))
                bidder=bidder.replace(bidder,bidder2)
            if highest_bid>bid1 and bid1>bid2:
                price=price.replace(price,str(bid1 + int(bid)))
                bidder=highest_bidder.replace(bidder,highest_bidder)
            if highest_bid>bid2 and bid1<bid2:
                price=price.replace(price,str(bid2 + int(bid)))
                bidder=highest_bidder.replace(bidder,highest_bidder)            
    return bidder,price

inputValue='''100,A,100,A,115,A,119,A,144,A,145,A,157,A,158,A,171,A,179,A,194,A,206,A,207,A,227,A,229,A,231,A,234'''
result=main(inputValue)
print(result[0] +','+result[1])