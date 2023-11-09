#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Nov. 8th, 2023
# This program asks the user to enter a whole number
# then tells the user the factorial of that number


def main():
    # Get the number
    user_num_string = input("Enter a whole number: ")

    # Initialize the counter
    counter = 0

    # Initialize the factorial
    factorial = 1

    # Making sure the number is an integer
    try:
        user_num_int = int(user_num_string)

        # Check if the number is negative
        if user_num_int < 0:
            print("{} is not a whole number.".format(user_num_int))
        else:
            # Do While loop to find the factorial
            while True:
                counter = counter + 1
                factorial = factorial * counter
                print("Tracking {} times through the loop.".format(counter))
                if counter >= user_num_int:
                    break

            print("The factorial of {} is {}".format(user_num_int, factorial))
    except:
        print("{} is not an integer!".format(user_num_string))
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
