# DL class Shopping List Manager

shop_list = []
finished_tasks = []

while True:
    action = int(input("\n1. Add item\n2. Remove task\n3. Show list\n4. Mark completed item\n5. Quit\nChose an option (1-5): "))
    
    if action == 1:
        item = input("\nEnter item: ")
        shop_list.append(item)
        print(f"\n'{item}' added to list")
    elif action == 2:
        item = input("\nEnter the number of the task to remove: ")
        item = shop_list[item]
        if item in shop_list:
            shop_list.remove(item)
            print(f"\n'{item}' removed from list")
        else:
            print("\nItem not found")
    elif action == 3:
        item_num = 1
        if not shop_list:
            print("\nList is empty")
        else:
            print("\n1---Shopping list---")
            for i in shop_list:
                list_item = shop_list[(item_num-1)]
                if (item_num-1) in finished_tasks:
                    print(f"{item_num}) {list_item} ✅")
                    item_num += 1  
                else:
                    print(f"{item_num}) {list_item}")
                    item_num += 1
    elif action == 4:
        item = int(input("\nEnter the number of the task to mark as completed: "))
        finished_tasks.append(item-1)
        print(f"\n'{shop_list[item-1]}' has been completed")
    elif action == 5:
        break
    else:
        print("That is not a valid action")
