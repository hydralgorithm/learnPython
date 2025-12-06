# KWARGS AND ARGS SHIPPING LABEL

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(f"{value}")

shipping_label("Dr.","Spongebob","Squarepants","III",
               street = "MG Road",
               city = "Bengaluru",
               state = "Karnataka",
               zip = "560071")