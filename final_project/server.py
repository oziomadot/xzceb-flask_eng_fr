from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    frenchText = language_translator.translate(
    textToTranslate, model_id='fr-en').get_result()
    return "Translated text to French" +frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    englishText = language_translator.translate(
    textToTranslate, model_id='fr-en').get_result()
    return "Translated text to English" +englishText

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    render_template('index.py')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
