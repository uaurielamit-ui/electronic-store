import val
import data
def invantory_manegment():
    to_exit = False
    while not to_exit:
        client_choice = input ("""
    --------- INVANTORY MANAGEMENT ---------

        1. show foll stock
        2.find 1 product
        3.add unit to stock
        4.sub unit to stok
        5.show items whitout stock
        6.show items on low
        7.exit
        """)
        if client_choice == "7":
            to_exit = True 
        elif client_choice =="1":
            show_all(data.products)

def show_all(products):
    for p in products:
        print(p)