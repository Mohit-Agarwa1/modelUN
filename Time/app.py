from flask import Flask, render_template, request
import webbrowser
import time

app = Flask(__name__)



@app.route("/")
def home():
    return render_template('RLEAPP.html')

@app.route("/display_input")
def display_input():
    return render_template('open_file.html')

@app.route('/display_input', methods=['POST'])
def my_form_post():
    text = request.form['text']
    text = open(text, 'r')
    text = text.read()
    text = text.replace('\n','<br>')
    return text




if __name__ == "__main__":
    app.run(debug=True)
