from flask import Flask,render_template,url_for,flash
from forms import decryptForm,encryptForm
from cryption import encryptMessage,generateKey,decryptMessage
app = Flask(__name__)
app.config['SECRET_KEY'] = '7908e7a467af3317a4e7f2b4324fdc03'

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html') # Choose Encrypt or Decrypt.

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    form = encryptForm()
    if form.validate_on_submit():
        key = generateKey()
        encryptedMessage = encryptMessage(form.normalText.data,key)

        flash(f"{encryptedMessage}\n\n",'content')
        flash(f"{key}", 'key')
    return render_template('encrypt.html', form=form)
# Encrypt the given text.

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    form = decryptForm()
    if form.validate_on_submit():
       decryptedMessage = decryptMessage(form.normalText.data.encode(),form.key)
       flash(f"Given text: {decryptedMessage}",'success')
    return render_template('decrypt.html', form=form)
# Decrypt the given text.

if __name__ == '__main__':
    app.run(debug=True)


