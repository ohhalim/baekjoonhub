def solution(order):
    menu_prices = {
        "americano": 4500,  # cold americano
        "cafelatte": 5000,  # cold cafelatte
        "anything": 4500,   # cold americano
        "americanoice": 4500,
        "iceamericano": 4500,
        "americanohot": 4500,
        "hotamericano": 4500,
        "cafelatteice": 5000,
        "icecafelatte": 5000,
        "cafelattehot": 5000,
        "hotcafelatte": 5000
    }
    total_price = 0
    
    for item in order:
        total_price += menu_prices[item]
    
    return total_price  