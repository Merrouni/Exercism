def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lower_sentence = sentence.lower()
    for letter in alphabet:
        if letter not in lower_sentence:
            return False
    return True
