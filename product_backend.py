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
        if client_choice == "1":
            data.add_product(*add_product_data(data.products))
        if client_choice == "2":
            display_all_products(data.products)

        else:
            print("enter only on the legal options")


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
