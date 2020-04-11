from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '7908e7a467af3317a4e7f2b4324fdc03'

@app.route('/')
@app.route('/index')
def index():
    pass
# Choose Encrypt or Decrypt.

@app.route('/encrypt')
def encrypt():
    pass
# Encrypt the given text.

@app.route('/decrypt')
def decrypt():
    pass
# Decrypt the given text.

if __name__ == '__main__':
    app.run(debug=True)

