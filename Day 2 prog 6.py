def findCombinations(keypad, keys, combinations, index, result=''):
	if index == -1:
		combinations.add(result)
		return
	digit = keys[index]
	length = len(keypad[digit])

	for i in range(length):
		findCombinations(keypad, keys, combinations, index - 1, keypad[digit][i] + result)


def findAllCombinations(keypad, keys):
	if not keypad or not keys:
		return set()
	combinations = set()
	findCombinations(keypad, keys, combinations, len(keys) - 1)
	return combinations


if __name__ == '__main__':

	keypad = {
		2: ['A', 'B', 'C'],
		3: ['D', 'E', 'F'],
		4: ['G', 'H', 'I'],
		5: ['J', 'K', 'L'],
		6: ['M', 'N', 'O'],
		7: ['P', 'Q', 'R', 'S'],
		8: ['T', 'U', 'V'],
		9: ['W', 'X', 'Y', 'Z'],
                                0:[' '],
                
	}
	keys = [8,7]
combinations = findAllCombinations(keypad, keys)
print(combinations)
