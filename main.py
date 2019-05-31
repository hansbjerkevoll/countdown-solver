
def match_words(word1, word2):
    word1_list = list(word1.lower())
    word2_list = list(word2.lower())

    for char in word1_list:
        if char in word2_list:
            word2_list.remove(char)
        else:
            return False

    return True


def main():

    input_letters = input("Input letters: ")
    print()
    output_length = len(input_letters)

    # Fetch all english words, remove all larger than input and sort
    with open('words.txt', "r") as f:
        words = [word.strip() for word in f.readlines()]
    words = [w for w in words if len(w) <= len(input_letters)]
    words.sort(key=lambda s: len(s))
    words.reverse()

    matching_words = []

    for word in words:

        if len(word) < output_length:
            print("Number of " + str(output_length) + "-letter words: " + str(len(matching_words)))
            if len(matching_words) != 0:
                print(matching_words)
            print()
            if len(word) < 5 and len(matching_words) != 0:
                break
            matching_words.clear()
            output_length -= 1

        if match_words(word, input_letters) and (word not in matching_words):
            matching_words.append(word)


if __name__ == "__main__":
    main()
