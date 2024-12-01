def start_game():
    print("You have reached a crucial junction in your life.")
    choice = input("Will you do what it takes to prevail? (yes/no): ")

    if choice =="yes":
        print ("You are a based person. Good luck!")
    elif choice =="no":
        print("Cringe. You deserve whatever chaos begets you...")
    else:
        print("invalid choice. Please type'yes' or 'no'.")

start_game()