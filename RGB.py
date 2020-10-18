#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on October 2020
# This program states all valid RGD values


def main():
    # This function states all valid RGD values

    # Input
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0

    # Process & Output
    print("Here are all the valid RGB values:")
    print("")

    for counter_1 in range(255):
        for counter_2 in range(255):
            for counter_3 in range(255):
                print("RGB({0},{1},{2})"
                      .format(counter_1, counter_2, counter_3))


if __name__ == "__main__":
    main()
