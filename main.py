from pizzapy import Customer, Order, StoreLocator, CreditCard


# Functions
def searchMenu(menuItem):
    while True:
        print("You are now searching the menu...")
        searchedItem = input("Type an item to look for: ").strip().lower()  # strip the whitespace

        if searchedItem != "" and len(searchedItem) > 1:
            searchedItem = searchedItem[0].upper() + searchedItem[1:]
        else:
            if searchedItem == "":
                break
            print("Invalid Search")

        print(f"Results for: {searchedItem}")
        menuItem.search(Name=searchedItem)


def addItemToOrder(pizzaOrder):
    while True:
        print("Please enter the item code you would like to add to your order...")
        print("Press Enter to stop ordering")
        itemID = input("Code: ").upper()
        try:
            pizzaOrder.add_item(itemID, 1)
        except:
            if itemID == "":
                break
            print("Invalid Code...")
            break


# Initialize Necessary Values
customer = Customer(
    'Pranav',
    'Chati',
    'pchati2003@gmail.com',
    '5133109580',
    '6562 Glenstone Way, Mason, OH, 45040'
)

my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
menu = my_local_dominos.get_menu()
order = Order.begin_customer_order(customer, my_local_dominos)
savedOrder = Order.begin_customer_order(customer, my_local_dominos)
# TODO add savedOrder

while True:
    searchedSavedOrder = input("Enter Saved Order: ").strip().lower()
    if searchedSavedOrder == "me":
        # TODO add only a pizza for myself
        break
    elif searchedSavedOrder == "family":
        # TODO add family pizza order
        break

    searchMenu(menu)
    addItemToOrder(order)
    answer = input("Would you like to add more items(yes/no)? ")
    if answer[0].lower() == 'n':
        break

# Order Finishing Up
# TODO Add something to differentiate between savedOrder and order
total = 0
print("Your order is as follows:")
for item in order.data["Products"]:
    total += float(item["Price"])
    print(f'Item Name: {item["Name"]}, Item Code: {item["Code"]}, Item Price: ${item["Price"]}')

print(f'Order Total: ${total}')
pay = input("Pay for order(yes/no)?")
if pay[0].lower() == 'y':
    # TODO Add environment variable for credit card info
    credit = CreditCard()
