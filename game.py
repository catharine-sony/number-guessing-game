import random
import time

def play_game():
    print("\n🎮 Welcome to the Advanced Number Guessing Game!")
    print("👉 I will think of a number between 1 and 50")
    print("👉 You have to guess it correctly\n")

    number = random.randint(1, 50)
    attempts = 0
    max_attempts = 7

    start_time = time.time()

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except:
            print("❌ Please enter a valid number!")
            continue

        attempts += 1

        if guess == number:
            end_time = time.time()
            time_taken = round(end_time - start_time, 2)

            print("\n🎉 Congratulations! You guessed it right!")
            print("🏆 Attempts used:", attempts)
            print("⏱️ Time taken:", time_taken, "seconds")
            print("⭐ Score:", (max_attempts - attempts + 1) * 10)
            return

        elif guess < number:
            print("⬆️ Try a higher number")
        else:
            print("⬇️ Try a lower number")

        print(f"⚠️ Remaining attempts: {max_attempts - attempts}\n")

    print("\n😢 Game Over!")
    print("The correct number was:", number)


while True:
    play_game()
    again = input("\n🔁 Do you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("🙏 Thanks for playing! See you again!")
        break