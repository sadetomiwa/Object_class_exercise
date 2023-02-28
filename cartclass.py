
# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.cart = []

    def add_to_cart(self, new_item):
        self.cart.append(new_item)

    def remove_from_cart(self):
        for item in self.cart:
            del self.cart[self.cart.index(item)]
            print(f"{item} removed from cart.")
        
       

    

    def show_cart(self):
        print(f"Your cart is: {self.cart}")

    



class Product():

    def __init__(self, name, quanity, price):
        self.name = name
        self.quantity = quanity
        self.price = price

    def get_product_total(self):
        for item in self.cart:
            print(f"{item.name}: {item.quantity} x {item.price}")
            total = total + (item.quantity * item.price)
        print(f"Your total is: ${total}")
        print("Thank you for shopping with us!")
        print("Here is your receipt:")
        return total
        
        
        


product1 = Product('Yeezy', 1, 220)
product2 = Product('Nike', 1, 159)
product3 = Product('New Balance', 1, 200)
product4 = Product('Astroworld', 1, 40)
product5 = Product('V-Lone', 1, 100)
product6 = Product('Doritoes', 1, 10)
product7 = Product('Bluevine', 1, 100)
product8 = Product('Oreos', 1, 10)

inventory = [product1.name, product2.name, product3.name, product4.name, product5.name, product6.name, product7.name, product8.name]


def run():
    cust_name = input('Welcome. What is your name? ')
    my_cart = Cart(cust_name)
    print(f"Welcone {cust_name},This is our current inventory: {inventory}")

    while True:
        print("""
    Shopping Cart Options
    ------------------------
    1: Add item
    2: Remove item
    3: View cart
    0: Quit program
    """)
        ask_in = input("Enter your choice: ").lower()
        if ask_in == "0":
            product1.get_product_total()
            
            
            
            break

        elif ask_in == "1":
            item = input('What would you like to add? ').lower()
            my_cart.add_to_cart(item)
            print(f"{item} added to cart.")

        elif ask_in == "2":
            item = input('What would you like to remove? ').lower()
            my_cart.remove_from_cart()
            
        
        elif ask_in == "3":
            my_cart.show_cart()
            
            

        
        

run()
