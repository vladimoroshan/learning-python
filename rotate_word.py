def rotate_word(word, n):
	"""A Caesar cypher 
	A weak form of encryption that involves “rotating” each letter by
	a fixed number of places. To rotate a letter means to shift it 
	through the alphabet, wrapping around to the beginning if necessary, 
	so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.
	
    word: string
    n: integer. Positive or negative. Zero just return the word without change

    Returns: string
	"""
	letters = list(word)	
	result = []

	for i in range(len(letters)):
		num_code = ord(letters[i]) # func ord(c) converts a char to a numeric code
		result.append(chr(num_code + n)) # func chr() converts num code to characters  

	return ''.join(result)

print(rotate_word('IBM', -1))
