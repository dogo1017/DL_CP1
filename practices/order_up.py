#DL 1st, order up practice

#dictionary for main dishes
mains = {
    "Grilled Salmon": 18.99,
    "BBQ Ribs": 22.50,
    "Margherita Pizza": 14.25,
    "Beef Lasagna": 16.75,
    "Chicken Alfredo": 15.50,
    "Vegetable Stir Fry": 13.00,
    "Lamb Chops": 24.99,
    "Stuffed Peppers": 12.95,
    "Seafood Paella": 21.50,
    "Mushroom Risotto": 14.75,
    "Teriyaki Chicken": 15.25,
    "Pork Schnitzel": 17.40
}

# Dictionary for drinks
drinks = {
    "Sparkling Water": 2.50,
    "Lemonade": 3.25,
    "Iced Tea": 3.50,
    "Cola": 2.95,
    "Orange Juice": 3.75,
    "Mango Smoothie": 4.50,
    "Cappuccino": 4.25,
    "Latte": 4.50,
    "Hot Chocolate": 3.95,
    "Green Tea": 2.75,
    "Craft Beer": 6.50,
    "House Red Wine": 7.25
}

# Dictionary for side dishes
sides = {
    "French Fries": 3.99,
    "Garlic Bread": 4.25,
    "Caesar Salad": 5.50,
    "Mashed Potatoes": 4.75,
    "Steamed Vegetables": 4.50,
    "Onion Rings": 4.25,
    "Coleslaw": 3.75,
    "Sweet Potato Fries": 4.95,
    "Baked Beans": 3.50,
    "Mac and Cheese": 5.25,
    "Corn on the Cob": 3.95,
    "Side Rice": 3.25
}

# Function to display all menu items
def display_menu():
    # Print main dishes header
    print("\n---MAIN DISHES---\n")
    # Loop through each main dish
    for main in mains:
        # Print dish name and price
        print(f"{main}: {mains[main]}")
    # Print sides header
    print("\n---SIDES---\n")
    # Loop through each side
    for side in sides:
        # Print side name and price
        print(f"{side}: {sides[side]}")
    # Print drinks header
    print("\n---DRINKS---")
    # Loop through each drink
    for drink in drinks:
        # Print drink name and price
        print(f"{drink}: {drinks[drink]}")

# Function to display items from a dictionary with numbers
def display_numbered_items(item_dict):
    # Initialize counter
    cur_it = 0
    # Convert dictionary keys to list
    item_list = list(item_dict.keys())
    # Loop through each item
    for item in item_list:
        # Increment counter
        cur_it += 1
        # Print number, name, and price
        print(f"{cur_it}) {item}: {item_dict[item]}")
    # Return list of items and count
    return item_list, cur_it

# Function to display order items (can have duplicates)
def display_order_items(orders):
    # Initialize counter
    cur_it = 0
    # Loop through each order item
    for i in range(len(orders)):
        # Increment counter
        cur_it += 1
        # Get item name and price
        item_name = orders[i]["name"]
        item_price = orders[i]["price"]
        # Print number, name, and price
        print(f"{cur_it}) {item_name}: {item_price}")
    # Return count
    return cur_it

# Function to get valid number input from user
def get_valid_input(max_num):
    # Keep looping until valid input
    while True:
        # Get user input
        choice = int(input(f"\nWhich item would you like add to order: "))
        # Check if input is in valid range
        if choice in range(1, max_num + 1):
            # Return valid choice
            return choice
        else:
            # Print error message
            print(f"please type a valid input (1-{max_num})")

# Function to add item to order
def add_item_to_order(orders):
    # Initialize category variable
    current_cat = 4
    # Loop until valid category chosen
    while current_cat not in range(1, 4):
        # Ask user for category
        current_cat = int(input("\nWhat type of item would you like to add:\n1) Main dish\n2) Sides\n3) Drinks\n"))
    
    # If main dish selected
    if current_cat == 1:
        # Display mains with numbers
        item_list, count = display_numbered_items(mains)
        # Get valid selection
        choice = get_valid_input(count)
        # Get item name from list
        item_name = item_list[choice - 1]
        # Add to orders as new entry
        orders.append({"name": item_name, "price": mains[item_name]})
    # If side selected
    elif current_cat == 2:
        # Display sides with numbers
        item_list, count = display_numbered_items(sides)
        # Get valid selection
        choice = get_valid_input(count)
        # Get item name from list
        item_name = item_list[choice - 1]
        # Add to orders as new entry
        orders.append({"name": item_name, "price": sides[item_name]})
    # If drink selected
    elif current_cat == 3:
        # Display drinks with numbers
        item_list, count = display_numbered_items(drinks)
        # Get valid selection
        choice = get_valid_input(count)
        # Get item name from list
        item_name = item_list[choice - 1]
        # Add to orders as new entry
        orders.append({"name": item_name, "price": drinks[item_name]})

# Function to remove item from order
def remove_item_from_order(orders):
    # Check if order is empty
    if len(orders) == 0:
        # Print error message
        print("No items in order to remove!")
    else:
        # Display orders with numbers
        count = display_order_items(orders)
        # Keep looping for valid input
        while True:
            # Ask which item to remove
            item_remove = int(input("Which item would you like to remove: "))
            # Check if valid number
            if item_remove in range(1, count + 1):
                # Exit loop
                break
            else:
                # Print error message
                print("Please type a valid input")
        # Remove item at that position (adjust for 0-index)
        orders.pop(item_remove - 1)

# Function to view current order
def view_order(orders):
    # Print blank line
    print("\n")
    # Check if order is empty
    if len(orders) == 0:
        # Print no items message
        print("No items in order yet!")
    else:
        # Display all order items
        display_order_items(orders)
        # Print blank line
        print("\n")

# Function to finalize order and calculate total
def finalize_order(orders):
    # Initialize total to zero
    sum_total = 0
    # Loop through all orders
    for i in range(len(orders)):
        # Get item name and price
        item_name = orders[i]["name"]
        item_price = orders[i]["price"]
        # Print item details
        print(f"{i + 1}) {item_name}: {item_price}")
        # Add price to total
        sum_total += item_price
    # Print formatted total
    print(f"Total sum: ${sum_total:.2f}")
    # Ask for final decision
    end = int(input("1) finalize order\n2) return\n3) you're too broke and changed your mind\n"))
    # Return user choice
    return end

# Function to print angry leave message
def print_leave_message():
    # Print first rant
    print("Listen here, I don't get paid enough for this. Minimum wage, minimum effort, that's my motto. I spent the last five minutes of my life, minutes I will never get back, helping you navigate a menu that a five-year-old could figure out, only for you to bail at the last second. Do you have any idea how many times I've done this today? Do you? My feet hurt, my soul is crushed, and you just waltz in, select 'leave', and think that's acceptable behavior? It's not. I had hopes. I had dreams of actually getting this order done, maybe getting a five-minute break to cry in the walk-in fridge, but no, you had to come along and ruin that small beacon of hope.")
    # Print second rant
    print("\nAnd for what? To save yourself what, 15 bucks on a Margherita Pizza? You think you're smart? You're not smart, you're a time-waster, a soul-sucker, the reason I'm going bald at 24. I hope the next place you go to has slow service, warm beer, and runs out of French Fries right as you order them. This isn't just about the food anymore; it's about the principle. The principle of not wasting people's time in a service industry job where they are already hanging on by a thread. Get out of my face. Go on, get!")
    # Print third rant
    print("\nBut wait, there's more. You think this is a game? A hilarious little interaction for your day? This is my life, pal. This is where my dreams come to die, one 'leave' option at a time. I'm starting to think the universe is actively conspiring against me, using you as its main agent of chaos. Did you even consider the emotional toll? The sheer, crushing weight of having to smile and say 'Have a nice day!' to someone who just ripped the last shred of joy from your miserable existence?")
    # Print fourth rant
    print("\nI bet you leave a 5% tip in real life, too, thinking you're a big shot for gracing a business with your presence. You're the human equivalent of a dial-up modem in a broadband world – slow, annoying, and makes everyone want to scream. You probably put your shopping cart back with only one wheel going the right way. You're the kind of person who uses 'their,' 'there,' and 'they\'re' interchangeably, and feels no shame!")
    # Print fifth rant
    print("\nI was supposed to be a marine biologist! I was meant to be swimming with dolphins, not trying to explain the difference between a calzone and a stromboli to someone who looks like they've never seen the sun. Instead, here I am, trapped in this purgatory of minimum wage and maximum existential dread, all because you had a momentary lapse in judgement and selected 'leave'.")
    # Print sixth rant
    print("\nThe audacity! The sheer, unmitigated gall! I'm going to tell my grandkids about you. The one that got away. The customer who didn't even order anything, but left a psychological scar that will last for generations. I hope you get a paper cut on your tongue from a really important document. I hope your charger only works if it's bent at a 45-degree angle. I hope every traffic light you encounter for the rest of the week is red. Now, seriously, scram.")
    # Print final message
    print("\nTHANKS FOR WASTING MY TIME (:")

# Main program starts here
# Create list of valid menu options
valid_inps = [1,2,3,4,5,6]
# Create empty orders list (changed from dictionary to list)
orders = []

# Main loop - runs forever until break
while True:
    # Display main menu and get choice
    action = int(input("1) Menu\n2) Select Item\n3) Remove Item\n4) View Order\n5) Finalize Order\n6) leave\n"))
    # Check if input is valid
    if action not in valid_inps:
        # Print error message
        print(f"please input a number from 1-6")
        # Skip to next loop iteration
        continue
    # If menu option selected
    elif action == 1:
        # Call display menu function
        display_menu()
    # If select item chosen
    elif action == 2:
        # Call add item function
        add_item_to_order(orders)
    # If remove item chosen
    elif action == 3:
        # Call remove item function
        remove_item_from_order(orders)
    # If view order chosen
    elif action == 4:
        # Call view order function
        view_order(orders)
    # If finalize order chosen
    elif action == 5:
        # Call finalize function, get result
        end = finalize_order(orders)
        # If return to menu
        if end == 2:
            # Go back to start of loop
            continue
        # If confirm order
        elif end == 1:
            # Print thank you message
            print("Thank you for ordering food with us. Please wait while we make your food.")
            # Exit program
            break
        # If broke option chosen
        elif end == 3:
            # Print insult message
            print("Listen here, I don't get paid enough for this. Minimum wage, minimum effort, that's my motto. I spent the last five minutes of my life, minutes I will never get back, helping you navigate a menu that a five-year-old could figure out, only for you to bail at the last second. Do you have any idea how many times I've done this today? Do you? My feet hurt, my soul is crushed, and you just waltz in, select 'leave', and think that's acceptable behavior? It's not. I had hopes. I had dreams of actually getting this order done, maybe getting a five-minute break to cry in the walk-in fridge, but no, you had to come along and ruin that small beacon of hope.")
            print("\nAnd for what? To save yourself what, 15 bucks on a Margherita Pizza? You think you're smart? You're not smart, you're a time-waster, a soul-sucker, the reason I'm going bald at 24. I hope the next place you go to has slow service, warm beer, and runs out of French Fries right as you order them. This isn't just about the food anymore; it's about the principle. The principle of not wasting people's time in a service industry job where they are already hanging on by a thread. Get out of my face. Go on, get!")
            print("\nBut wait, there's more. You think this is a game? A hilarious little interaction for your day? This is my life, pal. This is where my dreams come to die, one 'leave' option at a time. I'm starting to think the universe is actively conspiring against me, using you as its main agent of chaos. Did you even consider the emotional toll? The sheer, crushing weight of having to smile and say 'Have a nice day!'' to someone who just ripped the last shred of joy from your miserable existence?")
            print("\nI bet you leave a 5% tip in real life, too, thinking you're a big shot for gracing a business with your presence. You're the human equivalent of a dial-up modem in a broadband world – slow, annoying, and makes everyone want to scream. You probably put your shopping cart back with only one wheel going the right way. You're the kind of person who uses 'their,' 'there,' and 'they\'re' interchangeably, and feels no shame!")
            print("\nI was supposed to be a marine biologist! I was meant to be swimming with dolphins, not trying to explain the difference between a calzone and a stromboli to someone who looks like they've never seen the sun. Instead, here I am, trapped in this purgatory of minimum wage and maximum existential dread, all because you had a momentary lapse in judgement and selected 'leave'.")
            print("\nThe audacity! The sheer, unmitigated gall! I'm going to tell my grandkids about you. The one that got away. The customer who didn't even order anything, but left a psychological scar that will last for generations. I hope you get a paper cut on your tongue from a really important document. I hope your charger only works if it's bent at a 45-degree angle. I hope every traffic light you encounter for the rest of the week is red. Now, seriously, scram.")
            print("\nTHANKS FOR WASTING MY TIME (:")
    # Exit program
            break
    # If leave chosen
    elif action == 6:
        # Call angry message function
        print_leave_message()
        # Exit program
        break