# Keyword arguments - arguments preceded by identifiers
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello(first="Boby",title="Mr.",last="Lee",greeting="Hello")

print("1","2","3","4","5",sep = "-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country="91", area="464", first="312", last="3424")
print(phone_num)