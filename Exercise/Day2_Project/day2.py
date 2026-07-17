'''
def process_order(customer_name, email, cart, is_premium=False):
    total = 0

    if customer_name == "":
        print("Invalid customer name")
        return

    if "@" not in email:
        print("Invalid email")
        return

    if len(cart) == 0:
        print("Cart is empty")
        return

    print(f"Processing order for {customer_name}")

    for item in cart:
        if item["price"] < 0:
            print("Invalid product price")
            return

        total += item["price"] * item["quantity"]

    if is_premium:
        total *= 0.90

    if total > 5000:
        shipping = 0
    else:
        shipping = 150

    total += shipping

    tax = total * 0.18
    total += tax

    print("-------------------")
    print("Order Summary")
    print("-------------------")

    for item in cart:
        print(
            item["name"],
            item["quantity"],
            item["price"],
            item["price"] * item["quantity"]
        )

    print("-------------------")
    print(f"Subtotal : {total - tax}")
    print(f"Tax : {tax}")
    print(f"Shipping : {shipping}")
    print(f"Grand Total : {total}")

    print("-------------------")

    print("Sending confirmation email...")

    print(f"Email sent to {email}")

    print("Updating inventory...")

    for item in cart:
        print(f"Reduced stock of {item['name']}")

    print("Saving order to database...")

    print("Order completed successfully")
'''

TAX_AMOUNT=0.18
def validate_user(customer_name:str, email:str)->bool:
    """to check whether the customer name is empty or the email is invalid without the character @"""
    if not customer_name:
        #print("Invalid customer name")
        return False
    
    if "@" not in email:
        #print("Invalid email")
        return False
    return True

def valid_cart(cart:list[dict])->bool:
    if not cart:
        return False
    return True


def calculate(cart:list[dict])->int:
    """to calculate the total price of all the items in the cart"""
    if not valid_cart(cart):
        return 0
    
    #if not cart:
     #   print("Cart is empty")
      #  return 0
    tot=0
    for item in cart:
        if item["price"]<0:
            print("Invalid product price")
            return 0
            
        tot += item["price"] * item["quantity"]
        
    return tot
        
def find_shipping(total:int)->int:
    """to find the shipping cost"""
    if total>5000:
        shipping=0
    else:
        shipping=150
    return shipping

def calculate_tax(total:int)->float:
    """to calculate the tax for the cart"""
    return total * TAX_AMOUNT

def print_summary(cart:list[dict], total:float|int, shipping:int, tax:float)->None:
    """to print the summary about the order"""
    print("----------------")
    print("Order Summary")
    print("----------------")
    for item in cart:
        print(item["name"], item["quantity"], item["price"], item["price"]*item["quantity"])
    print("-----------------")
    print(f"Subtotal : {total-tax}")
    print(f"Tax : {tax}")
    print(f"Shipping : {shipping}")
    print(f"Grand Total : {total}")
    print("-----------------")

def confirm_mail(email:str)->None:
    """to send confirmation email to the customer who ordered items"""
    print("Sending confirmation email...")
    print(f"Email sent to {email}")
    
def update_inventory(cart:list[dict])->None:
    """to update the inventory"""
    print("Updating inventory...")
    for item in cart:
        print(f"Reduced stock of {item['name']}")

def save_to_database():
    """saving the date to the database"""
    print("Saving order to databse...")

def process_order(customer_name:str, email:str, cart:list[dict], is_premium=False):
    """to process the order of a customer"""

    total=0
    if not validate_user(customer_name,email):
        print("Invalid customer name or email")
        return
    
    total=calculate(cart)
    if is_premium:
        total *= 0.90

    shipping=find_shipping(total)
    total+=shipping
    tax=calculate_tax(total)
    total+=tax

    print_summary(cart,total, shipping, tax)
    confirm_mail(email)
    update_inventory(cart)
    save_to_database()
    print("Order completed successfully")



