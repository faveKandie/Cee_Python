pimu = ormu = stmu = pemu = lemu = grmu = nomu = 500
vamu = dimu = limu = ramu = chmu = cimu = 500
svamu = llimu = strmu = gimu = gramu = sdimu = 500

def act():
	import prettytable
	from prettytable import PrettyTable
	print("Welcome, it takes 75ml to fill a cee_soda cup")

	global svamu
	global llimu
	global strmu
	global gimu
	global gramu
	global sdimu
	global pimu
	global ormu
	global stmu
	global pemu
	global lemu
	global grmu
	global nomu
	global vamu
	global ramu
	global chmu
	global cimu
	global limu
	global dimu
	cup = 75
	price = 0

	do = input("Do you want to continue in this display screen? Yes or no: ").lower()
	if do == "no":
		import KfShop
	elif do == "yes":
		order = input("Select your order:\n").lower()
		if order == "fanta":
			base = PrettyTable()
			base.add_column("s/n", ["1", "2", "3", "4", "5", "6", "7"])
			base.add_column("Fanta Flavours", ["pineapple", "orange", "strawberry", "peach", "lemon", "grape", "diet"])
			print(base)
			pick = input("Pick a flavour:\n").lower()
			if pick == "pineapple":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 14), 2)
				pimu -= want
				base.add_column("Current Quantity Available", [pimu, ormu, stmu, pemu, lemu, grmu, nomu])
				print(f"\n{base}")
			elif pick == "orange":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 12), 2)
				ormu -= want
				base.add_column("Current Quantity Available", [pimu, ormu, stmu, pemu, lemu, grmu, nomu])
				print(f"\n{base}")
			elif pick == "strawberry":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 15), 2)
				stmu -= want
				base.add_column("Current Quantity Available", [pimu, ormu, stmu, pemu, lemu, grmu, nomu])
				print(f"\n{base}")
			elif pick == "peach":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 13), 2)
				pemu -= want
				base.add_column("Current Quantity Available", [pimu, ormu, stmu, pemu, lemu, grmu, nomu])
				print(f"\n{base}")
			elif pick == "lemon":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 11), 2)
				lemu -= want
				base.add_column("Current Quantity Available", [pimu, ormu, stmu, pemu, lemu, grmu, nomu])
				print(f"\n{base}")
			elif pick == "grape":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 15), 2)
				grmu -= want
				base.add_column("Current Quantity Available", [pimu, ormu, stmu, pemu, lemu, grmu, nomu])
				print(f"\n{base}")
			elif pick == "diet":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 11), 2)
				nomu -= want
				base.add_column("Current Quantity Available", [pimu, ormu, stmu, pemu, lemu, grmu, nomu])
				print(f"\n{base}")
		elif order == "coke":
			base = PrettyTable()
			base.add_column("s/n", ["1", "2", "3", "4", "5", "6"])
			base.add_column("Coke Flavours", ["vanilla", "lime", "raspberry", "cherry", "citra", "diet"])
			print(base)
			pick = input("Pick a flavour:\n").lower()
			if pick == "vanilla":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 19), 2)
				vamu -= want
				base.add_column("Current Quantity Available", [vamu, limu, ramu, chmu, cimu, dimu])
				print(f"\n{base}")
			elif pick == "lime":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 16), 2)
				limu -= want
				base.add_column("Current Quantity Available", [vamu, limu, ramu, chmu, cimu, dimu])
				print(f"\n{base}")
			elif pick == "raspberry":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 17), 2)
				ramu -= want
				base.add_column("Current Quantity Available", [vamu, limu, ramu, chmu, cimu, dimu])
				print(f"\n{base}")
			elif pick == "cherry":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 18), 2)
				chmu -= want
				base.add_column("Current Quantity Available", [vamu, limu, ramu, chmu, cimu, dimu])
				print(f"\n{base}")
			elif pick == "diet":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 16), 2)
				dimu -= want
				base.add_column("Current Quantity Available", [vamu, limu, ramu, chmu, cimu, dimu])
				print(f"\n{base}")
			elif pick == "citra":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 20), 2)
				cimu -= want
				base.add_column("Current Quantity Available", [vamu, limu, ramu, chmu, cimu, dimu])
				print(f"\n{base}")
		elif order == "sprite":
			base = PrettyTable()
			base.add_column("s/n", ["1", "2", "3", "4", "5", "6"])
			base.add_column("Sprite Flavours", ["vanilla", "lemlime", "strawberry", "ginger", "grape", "diet"])
			print(base)
			pick = input("Pick a flavour:\n").lower()
			if pick == "vanilla":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 10), 2)
				svamu -= want
				base.add_column("Current Quantity Available", [svamu, llimu, strmu, gimu, gramu, sdimu])
				print(f"\n{base}")
			elif pick == "lemlime":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 7), 2)
				llimu -= want
				base.add_column("Current Quantity Available", [svamu, llimu, strmu, gimu, gramu, sdimu])
				print(f"\n{base}")
			elif pick == "strawberry":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 9), 2)
				strmu -= want
				base.add_column("Current Quantity Available", [svamu, llimu, strmu, gimu, gramu, sdimu])
				print(f"\n{base}")
			elif pick == "ginger":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 7), 2)
				gimu -= want
				base.add_column("Current Quantity Available", [svamu, llimu, strmu, gimu, gramu, sdimu])
				print(f"\n{base}")
			elif pick == "grape":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 8), 2)
				gramu -= want
				base.add_column("Current Quantity Available", [svamu, llimu, strmu, gimu, gramu, sdimu])
				print(f"\n{base}")
			elif pick == "diet":
				want = int(input("How many ml do you want dispensed: "))
				cup -= want
				price += round(((want / 25) * 6), 2)
				sdimu -= want
				base.add_column("Current Quantity Available", [svamu, llimu, strmu, gimu, gramu, sdimu])
				print(f"\n{base}")

		rate = False
		while not rate:
				print(f"{cup}ml is left for your cee_soda cup to be full.\nYour current price is: ${price}")
				if cup > 0:
					print("\n")
					asks = input("Do you want to include another order to fill your cup? Yes of No: ").lower()
					if asks == "yes":
						import ceeMenu
						from ceeMenu import menu
						calm = menu()
						print(calm)
						orderr = input("Pick an order: ").lower()
						if orderr == "fanta":
							base = PrettyTable()
							base.add_column("s/n", ["1", "2", "3", "4", "5", "6", "7"])
							base.add_column("Fanta Flavours", ["pineapple", "orange", "strawberry", "peach", "lemon", "grape", "diet"])
							print(f"\n{base}")
							read = input("Pick a flavour again: \n")
							if read == "pineapple":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								pimu -= want
								if pimu > 0 and cup >= 0:
									price += round(((want / 25) * 14), 2)
									base.add_column("Current Quantity Available", [pimu, ormu, stmu, pemu, lemu, grmu, nomu])
									print(f"\n{base}")
								else:
									pimu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
							if read == "orange":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								ormu -= want
								if ormu > 0 and cup >= 0:
									price += round(((want / 25) * 14), 2)
									base.add_column("Current Quantity Available", [pimu, ormu, stmu, pemu, lemu, grmu, nomu])
									print(f"\n{base}")
								else:
									ormu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
							if read == "strawberry":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								stmu -= want
								if stmu > 0 and cup >= 0:
									price += round(((want / 25) * 14), 2)
									base.add_column("Current Quantity Available", [pimu, ormu, stmu, pemu, lemu, grmu, nomu])
									print(f"\n{base}")
								else:
									stmu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
									ask = input("\nDo you want to add ice? yes or no: ").lower()
							if read == "peach":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								pemu -= want
								if pemu > 0 and cup >= 0:
									price += round(((want / 25) * 14), 2)
									base.add_column("Current Quantity Available", [pimu, ormu, stmu, pemu, lemu, grmu, nomu])
									print(f"\n{base}")
								else:
									pemu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
							if read == "lemon":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								lemu -= want
								if lemu > 0 and cup >= 0:
									price += round(((want / 25) * 14), 2)
									base.add_column("Current Quantity Available", [pimu, ormu, stmu, pemu, lemu, grmu, nomu])
									print(f"\n{base}")
								else:
									lemu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
							if read == "grape":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								grmu -= want
								if grmu > 0 and cup >= 0:
									price += round(((want / 25) * 14), 2)
									base.add_column("Current Quantity Available", [pimu, ormu, stmu, pemu, lemu, grmu, nomu])
									print(f"\n{base}")
								else:
									grmu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
							if read == "diet":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								nomu -= want
								if nomu > 0 and cup >= 0:
									price += round(((want / 25) * 14), 2)
									base.add_column("Current Quantity Available", [pimu, ormu, stmu, pemu, lemu, grmu, nomu])
									print(f"\n{base}")
								else:
									nomu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
						elif orderr == "coke":
							base = PrettyTable()
							base.add_column("s/n", ["1", "2", "3", "4", "5", "6"])
							base.add_column("Coke Flavours", ["vanilla", "lime", "raspberry", "cherry", "citra", "diet"])
							print(f"\n{base}")
							read = input("Pick a flavour:\n").lower()
							if read == "vanilla":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								vamu -= want
								if vamu > 0 and cup >= 0:
									price += round(((want / 25) * 19), 2)
									base.add_column("Current Quantity Available", [vamu, limu, ramu, chmu, cimu, dimu])
									print(f"\n{base}")
								else:
									vamu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
							if read == "lime":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								limu -= want
								if limu> 0 and cup >= 0:
									price += round(((want / 25) * 19), 2)
									base.add_column("Current Quantity Available", [vamu, limu, ramu, chmu, cimu, dimu])
									print(f"\n{base}")
								else:
									limu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
							if read == "raspberry":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								ramu -= want
								if ramu > 0 and cup >= 0:
									price += round(((want / 25) * 19), 2)
									base.add_column("Current Quantity Available", [vamu, limu, ramu, chmu, cimu, dimu])
									print(f"\n{base}")
								else:
									ramu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
							if read == "cherry":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								chmu -= want
								if chmu > 0 and cup >= 0:
									price += round(((want / 25) * 19), 2)
									base.add_column("Current Quantity Available", [vamu, limu, ramu, chmu, cimu, dimu])
									print(f"\n{base}")
								else:
									chmu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
							if read == "citra":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								cimu -= want
								if cimu > 0 and cup >= 0:
									price += round(((want / 25) * 19), 2)
									base.add_column("Current Quantity Available", [vamu, limu, ramu, chmu, cimu, dimu])
									print(f"\n{base}")
								else:
									cimu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
							if read == "diet":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								dimu -= want
								if dimu > 0 and cup >= 0:
									price += round(((want / 25) * 19), 2)
									base.add_column("Current Quantity Available", [vamu, limu, ramu, chmu, cimu, dimu])
									print(f"\n{base}")
								else:
									dimu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
						elif orderr == "sprite":
							base = PrettyTable()
							base.add_column("s/n", ["1", "2", "3", "4", "5", "6"])
							base.add_column("Sprite Flavours", ["vanilla", "lemlime", "strawberry", "ginger", "grape", "diet"])
							print(f"{base}")
							read = input("Pick a flavour:\n").lower()
							if read == "vanilla":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								svamu -= want
								if svamu > 0 and cup >= 0:
									price += round(((want / 25) * 19), 2)
									base.add_column("Current Quantity Available", [svamu, llimu, strmu, gimu, gramu, sdimu])
									print(f"\n{base}")
								else:
									svamu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
							if read == "lemlime":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								llimu -= want
								if llimu > 0 and cup >= 0:
									price += round(((want / 25) * 19), 2)
									base.add_column("Current Quantity Available", [svamu, llimu, strmu, gimu, gramu, sdimu])
									print(f"\n{base}")
								else:
									llimu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
							if read == "strawberry":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								strmu -= want
								if strmu > 0 and cup >= 0:
									price += round(((want / 25) * 19), 2)
									base.add_column("Current Quantity Available", [svamu, llimu, strmu, gimu, gramu, sdimu])
									print(f"\n{base}")
								else:
									strmu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
							if read == "ginger":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								gimu -= want
								if gimu > 0 and cup >= 0:
									price += round(((want / 25) * 19), 2)
									base.add_column("Current Quantity Available", [svamu, llimu, strmu, gimu, gramu, sdimu])
									print(f"\n{base}")
								else:
									gimu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
							if read == "grape":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								gramu -= want
								if gramu > 0 and cup >= 0:
									price += round(((want / 25) * 19), 2)
									base.add_column("Current Quantity Available", [svamu, llimu, strmu, gimu, gramu, sdimu])
									print(f"\n{base}")
								else:
									gramu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
							if read == "diet":
								want = int(input("How many ml do you want dispensed: "))
								cup -= want
								sdimu -= want
								if sdimu > 0 and cup >= 0:
									price += round(((want / 25) * 19), 2)
									base.add_column("Current Quantity Available", [svamu, llimu,strmu, gimu, gramu, sdimu])
									print(f"\n{base}")
								else:
									sdimu += want
									print("\nIt's either your cup is full or the machine is empty")
									print(f"Your current charge is $ {price}")
									print("order terminated")
					elif asks == "no":
						ask = input("\nDo you want to add ice? yes or no: ").lower()
						if ask == "yes":
							price += 1
							total = round(price, 2)
							print(f"Your order is ready.\nYour total cost is now ${total}")
							rate =  True
						elif ask == "no":
							print(f"Your order is ready.\nYour total cost is now ${price}")
							rate = True
				elif cup == 0:
					ask = input("\nDo you want to add ice? yes or no: ").lower()
					if ask == "yes":
						price += 1
						total = round(price, 2)
						print(f"Your order is ready.\nYour total cost is now ${total}")
						rate =  True
					elif ask == "no":
						print(f"Your order is ready.\nYour total cost is now ${price}")
						rate = True
act()