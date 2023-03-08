def koffee():
	import prettytable
	from prettytable import PrettyTable
	kar = PrettyTable()
	kar.add_column("s/n", ["1", "2", "3"])
	kar.add_column("Diet Drinks", ["Cappucino", "Latte", "Expresso"])
	kar.add_column("Price per 25ml", ["$15", "$10", "$10"])
	print(kar)
	
koffee()