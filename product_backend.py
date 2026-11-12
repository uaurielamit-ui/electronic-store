import val
import data
def product_manegment():
    to_exit = False
    while not to_exit:
        client_choice = input ("""
    --------- PRODUCTS MANAGEMENT ---------

    1. Add Product
    2. Display All Products
    3. Search Product
    4. Update Product
    5. Delete Product
    6. Back to Main Menu
        """)
        if client_choice == "6":
            to_exit = True 
        elif client_choice == "1":
            data.add_product(*add_product_data(data.products))
        elif client_choice == "2":
            display_all_products(data.products)
        elif client_choice == "3":
            resolt = search_setting(data.products)
        elif client_choice =="4":
            make_cange(data.products,*update_product(data.products))
        elif client_choice =="5":
            delete_product(data.products)


def add_product_data(products):
    max_id = 0
    for p in products:
        if p["id"] >= max_id:
            max_id = p["id"]+1
    name = val.val_str("enter the product name: ")
    real_category = False
    while not real_category:
        category = val.val_str("enter the product category: ") 
        for p in products:
           # print (p["category"],category)
            if p["category"] == category:
                real_category = True,
                break
        if real_category ==False:
            print("this category is not exist ")
    price = val.val_int("enter the product price: ") 
    stock = val.val_int("enter how many yunit are avalable: ")
    active = True
    return max_id, name, category, price, stock, active


def display_all_products(products):
    for p in products:
        print(p)


def search_product():
    legal = False
    while not legal:
        client_choice = input("""
        to serch by id: press 1 
        to serch by name: press 2 
        to serch by category: press 3
        to exit prres 4   
        """)
        if client_choice in ("1", "2", "3", "4"):
            legal = True
        else:
            print("not such a option ")
    return client_choice



def search_setting(products):
    resolt = []
    method = search_product()
    if method == "4":
        return
    if method == "1":
        method ="id"
        search = val.val_int("enter your serch: ")
        for p in products:
            if search == p[method] :
                resolt.append (p)
        return resolt
    search = val.val_str("enter your serch: ").lower()
    if method == "2":
        method ="name"
    if method == "3":
        method = "category"
    for p in products:
        if search in p[method].lower() :
            resolt.append (p)
    return resolt


def update_product(products):
    product = val.val_int("enter the product id: ")
    what_ap = input("""
    to chang the name press 1: 
    to chang the category press 2: 
    to chang the price press 3: 
    to chang the status press 4: 
    """)
    if what_ap == "1":
        key_n ="name"
        new = val.val_str("what the new valeu")
    if what_ap == "2":
        key_n ="category"
        new = val.val_str("what the new valeu")
    if what_ap == "3":
        key_n = "price"
        new = val.val_int("enter the nuw price: ")
    return product, what_ap, new , key_n

def make_cange(Products, product, what_ap, new, key_n):
    if what_ap =="1" or what_ap == "2" or what_ap =="3":
        found =False
        for p in Products:
            if p["id"] == product:
                p[key_n] = new
                return print("valeu_change")
        if found == False:
            return print("not exist ")    
    if what_ap == "4":
        found =False
        for p in Products:
            if p["id"] == product:
                if p["active"] == True:
                    p["active"] = False
                else:
                    p["active"] = True
                return print("valeu_change")
        if found == False:
            return print("not exist ")
    else:
        return print("wrong choice ")

 
def delete_product(products):
    what_to_d = val.val_int("chose the product to delete: ")
    for p in products:
        if p["id"] == what_to_d:
            input("pres enter to delete: ")
            products.remove(p)
            return print("delete sucses")
    return print("item not found")        