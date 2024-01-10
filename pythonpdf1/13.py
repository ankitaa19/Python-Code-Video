def word_frequency(input_text):
    word_count = {}

    # Split the input text into words
    words = input_text.split()

    # Count the frequency of each word
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Sort the keys alphanumerically
    sorted_word_count = dict(sorted(word_count.items()))

    return sorted_word_count


input_text = "Hello My name is Ankita. I Study at ITM skill University."

result = word_frequency(input_text)

for word, frequency in result.items():
    print(f"{word}: {frequency}")