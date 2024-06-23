import random  # Import the random module to generate random numbers

# Define the main function for the guessing game
def guess_the_number():
    while True:  # Start an infinite loop to allow multiple rounds of the game
        set_number_to_guess = random.randint(1, 50)  # Generate a random number between 1 and 50
        attempts = 0  # Initialize the number of attempts to zero
        has_guessed = False  # Initialize the guessing status to False

        print("\nGuessing game")  # Print the title of the game
        print("Guess a number from 1 - 50")  # Provide instructions to the user

        # Start a loop that continues until the user guesses the correct number
        while not has_guessed:
            try:  # Try block to handle potential errors
                guess_input = int(input("Enter your guess from 1 - 50: "))  # Get user input and convert to integer
                attempts += 1  # Increment the attempt count by one

                # Check if the guess is less than the generated number
                if guess_input < set_number_to_guess:
                    print("Too low of a guess!")  # Inform the user that the guess is too low
                # Check if the guess is greater than the generated number
                elif guess_input > set_number_to_guess:
                    print("Too high of a guess!")  # Inform the user that the guess is too high
                else:
                    # Inform the user that they guessed correctly and display the number of attempts
                    print("You guessed the number right in", attempts, "attempts!")
                    has_guessed = True  # Set the guessing status to True to exit the loop

            except ValueError:  # Handle the case where the input is not an integer
                print("Invalid! Enter an integer")  # Inform the user about the invalid input

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':  # Check if the user input is not 'yes'
            print("Thank you for playing!")  # Thank the user for playing
            break  # Exit the outer loop to end the game

# Call the function to start the game
guess_the_number()

#ChatGPT changelog; Looped the function and enhanced the comments for learning!
