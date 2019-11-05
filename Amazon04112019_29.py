"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. 
You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""

# Solution Oscar

def encode(string) :
	new_string = ""
	while string :
		char = string[0]
		i = 0
		while string and string[0] == char :
			i += 1
			string = string[1:]
		new_string += str(i)+char
	return new_string

encoded = encode("AAAAAAAAAABBBCCDAA")
print(encoded)

def decode(string) :
	chiffres = [str(i) for i in range(10)]
	new_string = ""
	while string :
		numero = ""
		while string and string[0] in chiffres :
			numero += string[0]
			string = string[1:]
		new_string += string[0] * int(numero)
		string = string[1:]
	return new_string

print(decode(encoded))