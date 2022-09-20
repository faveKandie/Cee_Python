import prettytable

from prettytable import PrettyTable

var = PrettyTable()
var.add_column("Resources", ["Cappucino", "Latte", "Expresso"])
var.add_column("Price per 25ml", ["$40", "$30", "$35"])
var.add_column("Quantity Available", ["500ml", "500ml", "500ml"])

print(var)

