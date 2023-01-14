import requests
import json

def back_translate(text, source_language, target_language):
    # Set the API endpoint and parameters
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": source_language,
        "tl": target_language,
        "dt": "t",
        "q": text
    }
    # Make the API request
    response = requests.get(url, params=params)
    # Get the translated text from the response
    translated_text = json.loads(response.text)[0][0][0]
    # Translate the text back to the original language
    params["tl"] = source_language
    params["q"] = translated_text
    response = requests.get(url, params=params)
    original_text = json.loads(response.text)[0][0][0]
    return original_text

# Example usage
original_text = "The quick brown fox jumps over the lazy dog."
source_language = "en"
target_language = "fr"
back_translated_text = back_translate(original_text, source_language, target_language)
print(back_translated_text)
