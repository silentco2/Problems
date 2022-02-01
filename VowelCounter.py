def get_count(sentence):
    sentence = sentence.lower()
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for letter in sentence:
        if letter in vowels:
            count+=1
    return count
