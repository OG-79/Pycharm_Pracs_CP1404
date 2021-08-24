# a program to quickly work out the total price for a number of items, each with different prices. If the total price
# if the cost is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
total = 0
number = int(input("How many items are there? "))
for i in range(number):
    price = int(input("Enter the price of the item: "))
    total += price   # determines total items then calculates total cost
if total > 100:
    total *= 0.9  # apply ten percent discount
print("Total price for ", number, " items is $", total, sep='')
