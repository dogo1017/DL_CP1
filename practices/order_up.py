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

valid_inps = [1,2,3,4,5,6]

orders = {}

while True:
    action = int(input("1) Menu\n2) Select Item\n3) Remove Item\n4) View Order\n5) Finalize Order\n6) leave\n"))
    if action not in valid_inps:
        print(f"please input a number from 1-6")
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
        end = int(input("1) finalize order\n2) return\n3) you're to broke and changed your mind"))
        if end == 2:
             break
        elif end == 1:
             print("Thank you for ordering food with us. Please wait while we make your food.")
             break
        elif end == 3:
            print("Go get a job you miserable brokie, even me, a minimum wage worker, have more money than you. You probably went into debt just from the cost of gas that drove you here in your cheap metal tin can")
            break
    
    elif action == 6:
        print("Listen here, I don't get paid enough for this. Minimum wage, minimum effort, that's my motto. I spent the last five minutes of my life, minutes I will never get back, helping you navigate a menu that a five-year-old could figure out, only for you to bail at the last second. Do you have any idea how many times I've done this today? Do you? My feet hurt, my soul is crushed, and you just waltz in, select 'leave', and think that's acceptable behavior? It's not. I had hopes. I had dreams of actually getting this order done, maybe getting a five-minute break to cry in the walk-in fridge, but no, you had to come along and ruin that small beacon of hope.")
    print("\nAnd for what? To save yourself what, 15 bucks on a Margherita Pizza? You think you're smart? You're not smart, you're a time-waster, a soul-sucker, the reason I'm going bald at 24. I hope the next place you go to has slow service, warm beer, and runs out of French Fries right as you order them. This isn't just about the food anymore; it's about the principle. The principle of not wasting people's time in a service industry job where they are already hanging on by a thread. Get out of my face. Go on, get!")
    print("\nBut wait, there's more. You think this is a game? A hilarious little interaction for your day? This is my life, pal. This is where my dreams come to die, one 'leave' option at a time. I'm starting to think the universe is actively conspiring against me, using you as its main agent of chaos. Did you even consider the emotional toll? The sheer, crushing weight of having to smile and say 'Have a nice day!'' to someone who just ripped the last shred of joy from your miserable existence?")
    print("\nI bet you leave a 5% tip in real life, too, thinking you're a big shot for gracing a business with your presence. You're the human equivalent of a dial-up modem in a broadband world – slow, annoying, and makes everyone want to scream. You probably put your shopping cart back with only one wheel going the right way. You're the kind of person who uses 'their,' 'there,' and 'they\'re' interchangeably, and feels no shame!")
    print("\nI was supposed to be a marine biologist! I was meant to be swimming with dolphins, not trying to explain the difference between a calzone and a stromboli to someone who looks like they've never seen the sun. Instead, here I am, trapped in this purgatory of minimum wage and maximum existential dread, all because you had a momentary lapse in judgement and selected 'leave'.")
    print("\nThe audacity! The sheer, unmitigated gall! I'm going to tell my grandkids about you. The one that got away. The customer who didn't even order anything, but left a psychological scar that will last for generations. I hope you get a paper cut on your tongue from a really important document. I hope your charger only works if it's bent at a 45-degree angle. I hope every traffic light you encounter for the rest of the week is red. Now, seriously, scram.")
    print("\nTHANKS FOR WASTING MY TIME (:")
    break