# MINI PROJECT #1
# Library manager.
# Create a library class.
# Display all the books.
# Lend Books. (Who owns the book if not present)
# Add Books.
# Return books.
# HarryLibrary = Library(Listof books, library_name.)


# Dictionary. (Book, Person)
# Lend book will take the name and and add to dictionary.
# Create a main function and run a infinite while loop asking user for the input.

                    # SOLUTION

'''
Author: Jay Patil
Purpose: Learning Python
'''

import pandas
class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.bookslist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Lender Book database has been updated. You can take the book now.")
        else:
            print(f"This book is already been used by {self.lendDict[book]}")

    def addBook(self, book):
        self.bookslist.append(book)
        print("The book has been added to the book list.")

    def returnBook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    harry = Library(["Python", "Rich Dad Poor Dad", "Harry Potter", "c++ Basics"
                     "Algorithms by CLRS"], "CodeWithHarry")

    while(True):
        print(f"Welcome to the{harry.name} library. Enter your choice to continue.")
        print("1] Display Books")
        print("2] Lend a Books")
        print("3] Add a Books")
        print("4] Return a Books")
        user_choice = input()
        if user_choice not in ["1", "2", "3", "4"]:
            print("Please enter a valid option.")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            harry.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            harry.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            harry.addBook(book)


        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            harry.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2 != "q" and user_choice2 != "c"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
