def main():
    running = True
    while running:
        print("\n1. select name: ")
        print("2. selcet language: ")
        print("3. select customer_service")
        print("0. exit")

        option = input("choose an option: ")
        if option == "1":
            print("my name is Jacob")
        elif option == "2":
            print("Iam Tiv by tribe")
        elif option == "3":
            print("upcoming developer")
        else:
            print("go to menu")


result = main()