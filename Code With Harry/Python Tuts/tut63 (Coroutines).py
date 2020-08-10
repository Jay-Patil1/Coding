# COROUTINES
def searcher():
    import time
    book = "This is a book on Jay and Code With Harry and good."
    time.sleep(4)  # Some task taking the time().

    while True:
        text = (yield)  # This states that the function is used as a coroutine.
        if text in book:
            print("Your text is in the book.")
        else:
            print("Text is not in the book.")

search = searcher()
print("Search Started.")
next(search)
search.send("Jay")  # The coroutine is used.

search.close()  # The coroutine is closed.
search.send("Jay")  # This is not run as the coroutine is closed. It can be started again.
# print("Next method run.")
# input("Press any key")
# search.send("Jay and")
# input("Press any key")
# search.send("Joker")
# input("Press any key")
# search.send("Like this Video")

# QUESTION
# 15 letters in a file.
# Coroutine reads the the letters.
# Tells if the name is in the letter or not.
