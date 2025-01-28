def generate_wordlist():
    base_words = ["password", "123456", "letmein", "welcome", "qwerty", "admin", "abc123", "sunshine", "iloveyou", "password1"]
    
    wordlist = set(base_words)

    for word in base_words:
        for i in range(1, 6):
            wordlist.add(f"{word}{i}")

    substitutions = ['@', '!', '#', '$', '%', '&']
    for word in base_words:
        for sub in substitutions:
            wordlist.add(word.replace('a', sub))
            wordlist.add(word.replace('s', sub))

    with open("wordlist.txt", "w") as file:
        for word in wordlist:
            file.write(word + "\n")
    
    print("Wordlist generated and saved to 'wordlist.txt'")

generate_wordlist()
