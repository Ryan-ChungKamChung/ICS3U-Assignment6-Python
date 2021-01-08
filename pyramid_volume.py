#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in January 2021
# Program finds volume of a right rectangular pyramid


import math


def volume(length, width, height):
    # Function calculates volume and returns it

    # Process
    volume = (length * width * height) / 3

    return volume


def main():
    # Takes user input, passes it to functions and calls them

    print("Enter measurements and I will give you the volume of "
          "a right rectangular pyramid")

    # Input
    while True:
        length_string = input("Enter length (cm): ")
        try:
            length = int(length_string)
            assert length > 0
            break
        except AssertionError:
            print("This isn't a valid input")
        except Exception:
            print("This isn't a valid input")

    while True:
        width_string = input("Enter width (cm): ")
        try:
            width = int(width_string)
            assert width > 0
            break
        except AssertionError:
            print("This isn't a valid input")
        except Exception:
            print("This isn't a valid input")

    while True:
        height_string = input("Enter height (cm): ")
        try:
            height = int(height_string)
            assert height > 0
            break
        except AssertionError:
            print("This isn't a valid input")
        except Exception:
            print("This isn't a valid input")

    # Calls functions
    calculated_volume = volume(length, width, height)

    # Output
    print("The volume of the cylinder is: {:.2f}cm³".
          format(calculated_volume))


if __name__ == "__main__":
    main()
