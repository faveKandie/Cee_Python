def menus():
	import prettytable
	from prettytable import PrettyTable
	sar = PrettyTable()
	sar.add_column("s/n", ["1", "2", "3", "4"])
	sar.add_column("Diet Drinks", ["Fanta", "Coke", "Sprite", "water"])
	sar.add_column("Price per 25ml", ["$11", "$16", "$6", "free"])
	print(sar)
	
menus()
