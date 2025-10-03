# Food Ordering System
from pyscript import display, document # pyright: ignore[reportMissingImports]

# Menu List
products_prices = {"Fondant Cake": 349.0, "Sweet Cupcakes": 70.0, "Chocolate Cookies": 60.0, "Vanila Sundae": 75.0, "Flavored Bread": 80.0, "Chois Special": 456.0} # Dictionary
tax_rate = 7.5 # Float

# Order Selection and Calculations
def order(e):
    document.getElementById('output').innerHTML = "" # Clear Output

    total = 0.0 # Float

    # Checkbox Selection With Tax Calculations
    if document.getElementById("FondantCake").checked:
        total += products_prices["Fondant Cake"] * (1 + tax_rate / 100)
    if document.getElementById("SweetCupcakes").checked:
        total += products_prices["Sweet Cupcakes"] * (1 + tax_rate / 100)
    if document.getElementById("ChocolateCookies").checked:
        total += products_prices["Chocolate Cookies"] * (1 + tax_rate / 100)
    if document.getElementById("VanilaSundae").checked:
        total += products_prices["Vanila Sundae"] * (1 + tax_rate / 100)
    if document.getElementById("FlavoredBread").checked:
        total += products_prices["Flavored Bread"] * (1 + tax_rate / 100)
    if document.getElementById("ChoisSpecial").checked:
        total += products_prices["Chois Special"] * (1 + tax_rate / 100)

    # Customer Details
    customer_name = document.getElementById("customerName").value.strip() # String
    customer_address = document.getElementById("customerAddress").value.strip() # String
    customer_number = document.getElementById("customerNumber").value.strip() # Integer

    if not customer_name or not customer_address or not customer_number:
        display("Please enter all required fields before checkout.", target="output")
        return

    # Display Order Summary and Total Order
    display(f"Order for: {customer_name}", target="output")
    display(f"Address: {customer_address}", target="output")
    display(f"Contact Number: {customer_number}", target="output")
    display(f"Total: ₱{total:.1f}", target="output")