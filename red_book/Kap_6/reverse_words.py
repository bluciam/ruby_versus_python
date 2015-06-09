def reverse_words(sentence):
    separated = sentence.split()
    reversing = []
    print separated
    for i in reversed(range(0, len(separated))):
        reversing.append(separated[i])
    print reversing
    return ' '.join(reversing)



sentence1 = "Return a copy of the string with trailing  characters removed."
print reverse_words(sentence1)
print reverse_words("")

