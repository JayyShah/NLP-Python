import gensim
from gensim.models import KeyedVectors

# Load pre-trained word2vec model
model = KeyedVectors.load_word2vec_format('path_to_word2vec.bin', binary=True)

def find_similar_word(text, word, k):
    # tokenize the text
    words = text.split()
    similar_words = model.most_similar(positive=[word], topn=k+1)
    similar_words = [w for w, s in similar_words if w in words]
    return similar_words

# Example usage
text = "The quick brown fox jumps over the lazy dog."
word = "fox"
k = 2
similar_words = find_similar_word(text, word, k)
print(similar_words)



"""

Use the Following link to Get the Bin Model
https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit

"""