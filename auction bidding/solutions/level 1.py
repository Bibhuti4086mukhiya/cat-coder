def bidderAndBid(bid_list):
    if len(bid_list) != 0:
        bidder=bid_list.pop(0)
        bid=int(bid_list.pop(0))
    return bidder,bid

def main(bid_list):
    bid_list=bid_list.split(',')
    bid=1
    highest_bid=int()
    highest_bidder=''
    price=bid_list.pop(0)
    bidder=''
    if len(bid_list)==2:
        bidder1,bid1 = bidderAndBid(bid_list)
        price=price.replace(price,str(bid1))
        bidder=bidder.replace(bidder,bidder1)
    for i in range((len(bid_list)//2)-1):
        if len(bid_list) != 0:
            bidder1,bid1 = bidderAndBid(bid_list)
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
                if bid2>bid1:
                    price=price.replace(price,str(bid1 + int(bid)))
                    bidder=bidder.replace(bidder,bidder2)
                elif bid2 == bid1:
                    price=price.replace(price,str(bid1))
                    bidder=bidder.replace(bidder,bidder1)
                else:
                    price=price.replace(price,str(bid2+int(bid)))
                    bidder=bidder.replace(bidder,bidder1)
            elif len(bid_list) != 0 or bidder2!=''and bid2!='':
                if bid1 < bid2:
                    price=price.replace(price,str(bid1 + int(bid)))
                    bidder=bidder.replace(bidder,bidder2)
                if bid1 > bid2:
                    price=price.replace(price,str(bid2 + int(bid)))
                    bidder=bidder.replace(bidder,bidder1)
                if bid2 == bid1:
                    price=price.replace(price,str(bid1))
                    bidder=bidder.replace(bidder,bidder2)

        elif len(bid_list) != 0 or bidder2!=''and bid2!='':
            if bid1 < bid2:
                price=price.replace(price,str(bid1 + int(bid)))
                bidder=bidder.replace(bidder,bidder2)
            if bid1 > bid2:
                price=price.replace(price,str(bid2 + int(bid)))
                bidder=bidder.replace(bidder,bidder1)
            if bid2 == bid1:
                price=price.replace(price,str(bid1))
                bidder=bidder.replace(bidder,bidder2)
            if highest_bid>bid1 and highest_bid>bid2:
                price=price.replace(price,str(bid1 + int(bid)))
                bidder=highest_bidder.replace(bidder,highest_bidder)
    return bidder,price
inputValue='''15,urtyp,15'''
result=main(inputValue)
print(result[0] +','+result[1])