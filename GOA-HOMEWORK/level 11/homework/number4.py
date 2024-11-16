price = int(input("Enter price: "))

if price > 50:
    discount = price / 100 * 10
    newPrice = price - discount
    print(newPrice)

if price >= 20 and price <= 50:
    discount = price / 100 * 5
    newPrice = price - discount
    print(newPrice)

if price < 20:
    print(price)