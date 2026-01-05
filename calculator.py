def program():
	print("Simple calculator")
	print("Choose a operation:")
	print("1. Addition")
	print("2. Subraction")
	print("3. Multiply")
	print("4. Divide")
	print("5. Exit")
	
	selected = input("Enter your choice:")
	
	if selected == "5":
		print("Goodbye")
		exit()

	try:
		num1 = float(input("First number:"))
		num2 = float(input("Second number: "))
	except:
		print("Invalid data")
		exit

	if selected == "1":
		print(f"Result: {num1+num2}")
	elif selected == "2":
		print(f"Result: {num1 - num2}")
	elif selected == "3":
		print(f"Result: {num1 * num2}")
	elif selected == "4":
		print(f"Result: {num1/num2}")
	else:
		print("Invalid response")

program()
