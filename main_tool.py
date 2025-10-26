from zxcvbn import zxcvbn

def analyze_password():
    password = input("Enter a password to analyze: ")
    result = zxcvbn(password)
    print("\nAnalysis Results:")
    print("Score:", result['score'])
    print("Feedback:", result['feedback'])
    print("Guesses:", result['guesses'])
    print("Crack time (offline, fast):", result['crack_times_display']['offline_fast_hashing_1e10_per_second'])

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
        variants.add(word[::-1])

        leet_word = ''.join(leet_map.get(c, c) for c in word.lower())
        variants.add(leet_word)

        for year in common_years:
            variants.add(word + year)
            variants.add(leet_word + year)
        for symbol in ['!', '@', '#', '123']:
            variants.add(word + symbol)
            variants.add(leet_word + symbol)
    return list(variants)

def generate_and_export_wordlist():
    print("\nEnter personal details for custom wordlist generation")
    name = input("Your name: ")
    dob = input("Year of birth: ")
    pet = input("Pet's name: ")
    place = input("Favorite place: ")
    inputs = [name, dob, pet, place]
    wordlist = wordlist_from_inputs(inputs)
    print("\nSample wordlist (first 20 entries):")
    for word in wordlist[:20]:
        print(word)
    with open("custom_wordlist.txt", "w") as f:
        for word in wordlist:
            f.write(word + "\n")
    print("\nWordlist successfully saved to custom_wordlist.txt")

def main():
    print("\nPassword Strength Analyzer & Custom Wordlist Tool")
    print("1. Analyze a password")
    print("2. Generate a custom wordlist")
    choice = input("Select an option (1 or 2): ")
    if choice == "1":
        analyze_password()
    elif choice == "2":
        generate_and_export_wordlist()
    else:
        print("Invalid choice. Please run again.")

if __name__ == "__main__":
    main()
