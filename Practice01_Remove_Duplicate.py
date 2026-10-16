#Approch: Using set to remove duplicates from a list
#This code removes duplicate items from a shopping cart list by converting it to a set and then back to a list.
cart = ["Laptop", "Mouse", "Keyboard", "Mouse", "Laptop", "Monitor"]
unique_cart = list(set(cart))
print(unique_cart)

#Approach: Using a loop to remove duplicates while preserving order
#This code removes duplicate items from a shopping cart list while preserving the original order of items.
#Complexity O(n)^2
cart = ["Laptop", "Mouse", "Keyboard", "Mouse", "Laptop", "Monitor"]
unique_cart = []
for item in cart:
    if item not in unique_cart:
       unique_cart.append(item)
print(unique_cart)

#Approch: Using set + loop
#This code removes duplicate items from a shopping cart list while preserving the original order of items.
#Complexity O(n)
cart = ["Laptop", "Mouse", "Keyboard", "Mouse", "Laptop", "Monitor"]
unique_cart = []
seen=set()
for item in cart:
    if item not in seen:
       seen.add(item)
       unique_cart.append(item)
print(unique_cart)

#Approch: Take the value from User and then make a unique list:

unique_cart =[]

while True:
    product = input("Enter the items, Once you done just Type (done)")

    if product.lower() == 'done':
       break

    if product not in unique_cart:
       unique_cart.append(product)

print("Cart:", unique_cart)


#Approch: In this we are also calculating to no of product count

cart = []

while True:
    product = input("Enter your product name once done then type 'done'")

    if product.lower() == 'done':
     break
    else:
        if product not in cart:
           cart.append(product)

print(cart)

