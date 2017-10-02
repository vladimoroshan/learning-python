def scan(raw_sentence):
	lexicon = {
		'north': 'direction', 
		'south': 'direction', 
		'east': 'direction', 
		'west': 'direction', 
		'down': 'direction', 
		'up': 'direction', 
		'left': 'direction', 
		'right': 'direction', 
		'back': 'direction',
		'go': 'verb', 
		'stop': 'verb',
		'kill': 'verb',
		'eat': 'verb',
		'the': 'stop',
		'in': 'stop',
		'of': 'stop', 
		'from': 'stop',
		'at': 'stop',
		'it': 'stop',
		'door': 'noun',
		'bear': 'noun',
		'princess': 'noun',
		'cabinet': 'noun'
	}

	words = raw_sentence.lower().split()
	list_of_tuples = []

	for word in words:
		if word.isdigit():
			list_of_tuples.append(('number', int(word)))
		else:
			corresponding_word = lexicon.get(word, 'error')
			list_of_tuples.append((corresponding_word, word))

	return list_of_tuples
