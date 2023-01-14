import random
from nltk.corpus import stopwords
from nltk.corpus import wordnet

def replace_synonyms(sentence, k):
    # Split the sentence into words
    words = sentence.split()
    # Get the list of stop words
    stop_words = set(stopwords.words('english'))
    # Initialize an empty list to store the words that are not stop words
    not_stop_words = []
    # Iterate through the words in the sentence
    for word in words:
        # If the word is not a stop word, add it to the list
        if word.lower() not in stop_words:
            not_stop_words.append(word)
    # If there are less than k words that are not stop words, return the original sentence
    if len(not_stop_words) < k:
        return sentence
    # If there are at least k words that are not stop words, choose k random words to replace
    else:
        # Initialize a list to store the indices of the chosen words
        chosen_indices = random.sample(range(len(not_stop_words)), k)
        # Iterate through the words in the sentence
        for i in range(len(words)):
            # If the word is not a stop word and its index is in the list of chosen indices
            if words[i].lower() not in stop_words and i in chosen_indices:
                # Get synonyms for the word
                synonyms = wordnet.synsets(words[i])
                # If there are synonyms
                if synonyms:
                    # Get the lemmas (base form) of the synonyms
                    lemmas = synonyms[0].lemmas()
                    # If there are lemmas
                    if lemmas:
                        # Replace the word with a randomly chosen lemma
                        words[i] = random.choice(lemmas).name()
        # Join the words back into a sentence
        return ' '.join(words)

# Example usage
sentence = "The computer is a powerful tool for work and play."
k = 2
print(replace_synonyms(sentence, k))
