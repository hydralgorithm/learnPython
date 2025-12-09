# Decorator

# Creating decorator
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🎊*")
        func(*args,**kwargs)
    return wrapper
# Creating decorator
def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("*You add fudge 🥮*")
        func(*args,**kwargs)
    return wrapper

# Declaring decorator
@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} icecream 🍦")

get_ice_cream("vanilla")

 