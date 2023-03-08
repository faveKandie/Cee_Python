def menu():
	import prettytable
	from prettytable import PrettyTable
	var = PrettyTable()
	var.add_column("s/n", ["1", "2", "3"])
	var.add_column("Resources", ["Fanta", "Coke", "Sprite"])
	var.add_column("Price per 25ml", ["$11 - $15", "$16 - $20", "$5 - $10"])
	print(var)
menu()

