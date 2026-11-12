import product_backend
import backend_invantory
def main():
    to_exit = False
    while not to_exit:
        client_choise = input("""
    =================================
        COMPUTER STORE SYSTEM
    =================================

    1. Products Management
    2. Inventory Management
    3. Sales Management
    4. Reports
    5. Exit

    Choose an option: 
        """)
        if client_choise == "5":
            to_exit = True
        elif client_choise == "1":
            product_backend.product_manegment()
        elif client_choise == "2":
            backend_invantory.invantory_manegment()
        else:
            print("wrong choise, chuse only from the opshen in the manu ")







if __name__ == ("__main__"):
    main()