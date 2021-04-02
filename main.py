print('Welcome to the Food App')
name = input("Please enter your name: ")
print('Hello ' + name)
products = {
    "French Fries": 10.5,
    "Big Mac": 15,
    "Happy Meal": 13.4,
    "Chicken": 11,
    "Burger": 7
}
print(products)
product_name = input("Please select a product: ")
prodQ = input("quantity: ")
x = (products[product_name] * int(prodQ))
print(str(x) + '$')

