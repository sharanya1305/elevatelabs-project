from zxcvbn import zxcvbn

# Ask the user to enter a password
password = input("Enter a password to analyze: ")

# Analyze the password
result = zxcvbn(password)

# Print results
print("Score:", result['score'])          # 0 = weak, 4 = strong
print("Feedback:", result['feedback'])    # Suggestions to improve
print("Guesses:", result['guesses'])      # Estimated number of guesses
print("Crack time (offline, fast):", result['crack_times_display']['offline_fast_hashing_1e10_per_second'])

