# !/usr/bin/env python3
# Created by: Sereke Asfeday
# Created on: 29, October, 2026
# This program asks user for the year and then tells them whether it is has leap 
# 1 additional day (366) or No (365)


def main():

# This is a welcoming message and it tells the user what the program does.
    print("Welcome\n This program ask for year ex: (2024 or 2026) and tells if it is a leap.")
    
    
    try:
        # Here we get the user input as string and then we cast it into an integer.
        user_input_as_string = input("Enter the year: ")
        year = int(user_input_as_string)

        # here we make the calculation to determine if the year/ user input is a leap year.
        if year % 4 == 0: 
            if year % 100 == 0:
                if year % 400 == 0:
                    print("{year} is a leap year".format(year=year)) # Here we tell the computer
                    # display 
                else:
                    print("{year} is not a leap year".format(year=year))
            else:
                print("{year} is a leap year".format(year=year))
        else:
            print("{year} is not a leap year".format(year=year))

    except ValueError:
        print("Invalid input. Please enter a valid year.")

    finally:
            print("Thank you for using this program.")

if __name__ == "__main__":
    main()