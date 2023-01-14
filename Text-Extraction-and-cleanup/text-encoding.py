import chardet

def detect_encoding(text):
    text = text.encode()
    result = chardet.detect(text)
    return result['encoding']

text = "This is a sample text to be encoded"
encoding = detect_encoding(text)
encoded_text = text.encode(encoding)
print(encoded_text)
