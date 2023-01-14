import requests
from bs4 import BeautifulSoup

def get_question_answer(question_url):
    # Send a GET request to the URL
    response = requests.get(question_url)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract the question
    question_header = soup.find(class_='question-header')
    if question_header:
        question = question_header.find('h1').get_text()
    else:
        question = None
    # Extract the best answer
    best_answer = soup.find(class_='answer accepted-answer')
    if best_answer:
        best_answer_text = best_answer.find(class_='post-text').get_text()
    else:
        best_answer_text = None
    return question, best_answer_text

# Example usage
question_url = 'https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time'
question, best_answer = get_question_answer(question_url)
print(question)
print(best_answer)
