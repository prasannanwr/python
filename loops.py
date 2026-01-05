def main():
	for i in range(1,6):
		print(i)

def fruits():
	fruits = ['appple', 'orange']
	for fruit in fruits:
		print(fruit)
def do_while():
	count = 1
	while count <=5:
		print(count)
		count +=1

def break_continue():
	for i in range(1,6):
		if i == 3:
			continue
		if i == 5:
			break
		print(i)
#main()
#fruits()
#do_while()
break_continue()
