words = ["level", "python", "radar", "java", "civic", "kotlin", "refer"]
palindromes = []

for word in words:
    backward = ""   
    for letter in word:  
        backward = letter + backward

    if word == backward:   
        palindromes.append(word)

print(palindromes)
