# Custom wordlist generator based on user details

def wordlist_from_inputs(inputs):
    variants = set()
    common_years = ['2023', '2024', '2025']
    leet_map = {'a':'@', 'e':'3', 'i':'1', 'o':'0', 's':'$'}
    
    for word in inputs:
        if not word:
            continue
        word = word.strip()
        variants.add(word)
        variants.add(word.lower())
        variants.add(word.capitalize())
        variants.add(word[::-1])  # reversed word
        
        # Leetspeak substitution
        leet_word = ''.join(leet_map.get(c, c) for c in word.lower())
        variants.add(leet_word)
        
        # Append common years
        for year in common_years:
            variants.add(word + year)
            variants.add(leet_word + year)
        
        # Simple symbol endings
        for symbol in ['!', '@', '#', '123']:
            variants.add(word + symbol)
            variants.add(leet_word + symbol)
            
    return list(variants)

# Example usage: manually set inputs below to test, or import from collect_inputs.py
inputs = ['Sharanya', '2007', 'Rio', 'Paris']

wordlist = wordlist_from_inputs(inputs)

print("\nGenerated wordlist:")
for word in wordlist:
    print(word)
# Export wordlist to a file
with open("custom_wordlist.txt", "w") as f:
    for word in wordlist:
        f.write(word + "\n")

print("\nWordlist successfully saved to custom_wordlist.txt")
