def disp():
	import prettytable
	from prettytable import PrettyTable
	display = PrettyTable()
	display.add_column("All Drinks", [])
	display.add_column("Zero Sugar", [])
	display.add_column("Coffee", [])
	
	print(display)
disp()