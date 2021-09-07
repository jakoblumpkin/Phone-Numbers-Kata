"""
Use this script to generate a file of names and phone numbers suitable for load testing the Phone Numbers code kata.
"""

import csv
import os
from random import choice, sample, randrange

phone_number_digits = ["", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
phone_number_partitions = ["", "-", " "]

def random_phonenumber():
    number = "0{0}{1}{2}{3}{4}{5}{6}".format("".join(sample(phone_number_digits, randrange(2,6))), 
                                    "".join(sample(phone_number_partitions, 1)), 
                                    "".join(sample(phone_number_digits, 3)),
                                    "".join(sample(phone_number_partitions, 1)),
                                    "".join(sample(phone_number_digits, 2)),
                                    "".join(sample(phone_number_partitions, 1)),
                                    "".join(sample(phone_number_digits, 2)),
                                    )
    return number


print(len(random_phonenumber()))