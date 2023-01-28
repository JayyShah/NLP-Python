from flask import Flask, request
app = Flask(__name__)

@app.route('/name_entity', methods=['POST'])
def name_entity():
    name = request.json["Name"]
    doc = nlp(name)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return {"Name": name, "Entity": "Person"}
        elif ent.label_ == "GPE":
            return {"Name": name, "Entity": "City"}

if __name__ == '__main__':
    app.run()