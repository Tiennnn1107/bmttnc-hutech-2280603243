from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayFairCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
app = Flask(__name__)

#router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

#router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
# #play fair
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')
@app.route("/PF/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Playfair = PlayFairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    playfair_encrypted = Playfair.playfair_encrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {playfair_encrypted}"

@app.route("/PF/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Playfair = PlayFairCipher()
    matrix = Playfair.create_playfair_matrix(key)
    playfair_decrypted = Playfair.playfair_decrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {playfair_decrypted}"
            #   Vinegere
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')
@app.route("/VGNR/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    vigenere_encrypted = Vigenere.vigenere_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {vigenere_encrypted}"

@app.route("/VGNR/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    vigenere_decrypted = Vigenere.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {vigenere_decrypted}"
                    #   RailFence
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')
@app.route("/RF/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Railfencee = RailFenceCipher()
    rail_fence_encrypted = Railfencee.rail_fence_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {rail_fence_encrypted}"

@app.route("/RF/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Railfencee = RailFenceCipher()
    rail_fence_decrypted = Railfencee.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {rail_fence_decrypted}"
# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)