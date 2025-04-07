import random  # Random module to generate number

secret_number = random.randint(1, 100)  # Secret number between 1 to 100
attempts = 5  # Total chances to guess

print("🎮 Welcome to the Guess The Number Game!")
print("🧡 You have 5 chances to guess the number between 1 and 100!\n")

while attempts > 0:
    try:
        guess = int(input("👉 Enter your guess: "))
        
        if guess == secret_number:
            print("🎉 Wah Prachi! You guessed it right!")
            break
        elif guess < secret_number:
            print("📉 Too low baby, try higher!")
        else:
            print("📈 Too high baby, try lower!")

        attempts -= 1
        print(f"💡 You have {attempts} attempt(s) left.\n")

    except ValueError:
        print("🚫 Oops! Please enter a valid number.\n")

if attempts == 0:
    print(f"😢 Sorry baby! The correct number was {secret_number} 💔")
