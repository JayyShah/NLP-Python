import spacy
import warnings 
warnings.filterwarnings("ignore")

def replace_entities(text, replacement):
    # Load the spaCy model
    nlp = spacy.load("en_core_web_sm")
    # Process the text
    doc = nlp(text)
    # Replace the entities with the specified replacement
    for ent in doc.ents:
        text = text.replace(ent.text, replacement)
    return text

# Example usage
text = "The quick brown fox jumps over the lazy dog."
replacement = "*"
replaced_text = replace_entities(text, replacement)
print(replaced_text)


"""

Use "python -m spacy download en_core_web_sm" 
To download spacy and en_core_web_sm module

"""