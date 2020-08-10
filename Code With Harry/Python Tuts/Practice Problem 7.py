# SEARCH ENGINE
# Given few sentences as a list (list of sentences).
# Pull out the sentes matching the query inputtted by the user in decresing order of relevance..
# Most relevent sentence is with maximum number of matching words with the query.
# Convert everything to lower case.

# Input:
# Input the query string.

# Output:
# Print the number of results.
# Print out the sentences matching the query.

                    # SOLUTION

'''
Author: Jay Patil
Date: 9 August 2020
Purpose: Practice Problem
'''

# Return the number of matching words.


def matchingWords(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == "__main__":
    # matchingWords("This is good", "Python is good")
    sentences = ["Python is a good", "This is a snake",
                 "Jay is a good boy", "Subscribe Code With Harry"]

    query = input("Please enter the query string:\n")
    scores = [matchingWords(query, sentence) for sentence in sentences]
    # print(scores)
    sortedSentScore = [sentScore for sentScore in sorted(
        zip(scores, sentences), reverse=True) if sentScore[0] !=0]
    # print(sortedSentScore)
    print(f"{len(sortedSentScore)} results found!")
    for score, item in sortedSentScore:
        print(f"\"{item}\": with a score of {score}")
