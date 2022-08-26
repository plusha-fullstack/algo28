def MaximumDiscount(N, price):
    discount = 0
    price.sort(reverse = True)
    for i in range(len(price)):
        if (i % 3) == 2:
            discount += price[i]
            
    return discount
