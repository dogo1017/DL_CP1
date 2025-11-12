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

valid_inps = [1,2,3,4]

orders = {}

while True:
    action = int(input("1) Menu\n2) Select Item\n3) Remove Item\n4) View Order\n5) Finalize Order\n"))
    if action not in valid_inps:
        print(f"please input a number from 1-4")
        continue
    elif action == 1:
        print("\n---MAIN DISHES---\n")
        for main in mains:
            print(f"{main}: {mains[main]}")
        print("\n---SIDES---\n")
        for side in sides:
            print(f"{side}: {sides[side]}")
        print("\n---DRINKS---")
        for drink in drinks:
            print(f"{drink}: {drinks[drink]}")
        break
    elif action == 2:
        current_cat = 4
        while current_cat not in range(3):
            current_cat = int(input("\nWhat type of item would you like to add:\n1) Main dish\n2) Sides\n3) Drinks\n"))
        if current_cat == 1:
            cur_it = 0
            for main in mains:
                cur_it +=1
                print(f"{cur_it}){main}: {mains[main]}")
            while True:
                new_item = int(input("\nWhich item would you like add to order: "))
                if new_item in range(cur_it):
                    break
                else:
                    print(f"please type a valid input (1-{cur_it})")
            new_key = mains[new_item]
            orders[new_key] = mains[new_item]
        if current_cat == 2:
            cur_it = 0
            for side in sides:
                cur_it +=1
                print(f"{cur_it}){side}: {sides[side]}")
            while True:
                new_item = int(input("\nWhich item would you like add to order: "))
                if new_item in range(cur_it):
                    break
                else:
                    print(f"please type a valid input (1-{cur_it})")
            new_key = sides[new_item]
            orders[new_key] = sides[new_item]
        if current_cat == 3:
            cur_it = 0
            for drink in drinks:
                cur_it +=1
                print(f"{cur_it}){drink}: {drinks[drink]}")
            while True:
                new_item = int(input("\nWhich item would you like add to order: "))
                if new_item in range(cur_it):
                    break
                else:
                    print(f"please type a valid input (1-{cur_it})")
            new_key = drinks[new_item]
            orders[new_key] = drinks[new_item]

        elif action == 3:
            while True:
                cur_it = 0
                for order in orders:
                    cur_it +=1
                    print(f"{cur_it}){order}: {orders[order]}")
                item_remove = int(input("Which item would you like to remove: "))
                if item_remove in range(cur_it):
                    break
                else:
                    print("Please type a valid input")
            del orders[item_remove]
    elif action == 4:
        for order in orders:
                    cur_it +=1
                    print(f"{cur_it}){order}: {orders[order]}")
    
    elif action == 5:
        sum = 0
        for order in orders:
                    sum += 1
                    cur_it +=1
                    print(f"{cur_it}){order}: {orders[order]}")

        print(f"Total sum: {sum}")