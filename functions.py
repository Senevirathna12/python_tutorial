def invoice(name , amount , offer):
    final_value = final_price(amount , offer)
    print(f"hy {name}, your {amount}$ invoice is here with {offer}% offer .And this is your final value {final_value}")

def final_price(amount,offer):
    return amount - (amount*(offer/100))

invoice("Amith", 100, 40)