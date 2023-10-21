from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/bot-chat/')
def chat():
    return render_template('chat.html')
@app.route('/dodge-game/')
def dodge():
    return render_template('dodge.html')
if __name__ == '__main__':
    app.run(debug=True)
