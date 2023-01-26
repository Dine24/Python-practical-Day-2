def commonWords(sent1, sent2):
	sen1 = set(sent1)
	sen2 = set(sent2)
	common = list(sen1.intersection(sen2))
	
	
	return common
def removeCommonWords(sent1, sent2):
	sentence1 = list(sent1.split())
	sentence2 = list(sent2.split())
	commonlist = commonWords(sentence1,sentence2)

	word = 0
	for i in range(len(sentence1)):
	
		
		if sentence1[word] in commonlist:
		
			
			sentence1.pop(word)
			
			
			word = word - 1
		word += 1

	word = 0
	for i in range(len(sentence2)):
	
		
		if sentence2[word] in commonlist:
		
			
			sentence2.pop(word)
			
			
			word = word-1
		word += 1
		
	
	print(*sentence1)
	print(*sentence2)
S1 = input("enter a string")
S2 = input("enter a string")

removeCommonWords(S1, S2)
