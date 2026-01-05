def reverse_string(str):
	reversed = ''
	for char in str:
		reversed = char + reversed
	print(reversed)

reverse_string('Hello')
