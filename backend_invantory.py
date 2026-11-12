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
        elif client_choice =="2":
            print(find_1_product(data.products))
        elif client_choice == "3":
            print(add_unit_to_stock(data.products))
        elif client_choice == "4":
            print(sub_unit_to_stok(data.products))
        elif client_choice == "5":
            print(show_items_whitout_stock(data.products))
        elif client_choice == "6":
            print(show_items_on_low(data.products))



def show_all(products):
    for p in products:
        print(p)


def find_1_product(products):
    item = val.val_int("whats the product id: ")
    for p in products:
        if p["id"] == item:
            return p
    return "did not faund"


def add_unit_to_stock(products):
    item = val.val_int("whats the product id: ")
    for p in products:
        if p["id"] == item:
            unit = val.val_int("how moch yunits you ont to add: ")
            p["stock"] += unit
            return "adding secsis"
    return "item not find" 


def sub_unit_to_stok(products):    
    item = val.val_int("whats the product id: ")
    for p in products:
        if p["id"] == item:
            unit = val.val_int("how moch yunits you ont to sub: ")
            if p["stock"] >= unit:
                p["stock"] -= unit
                return "subing secsis"
            else:
                return "not inaf units"
    return "item not find"    


def show_items_whitout_stock(products):
    no_stok=[]
    for p in products:
        if p["stock"] == 0:
            no_stok.append(p)
    if no_stok == []:
        return "all items have units "
    else:
        return no_stok


def show_items_on_low(products):
    low_stok=[]
    for p in products:
        if p["stock"] > 0 and p["stock"] < 5:
            low_stok.append(p)
    if low_stok == []:
        return "no unit on low stock "
    else:
        return low_stok