from flask import Flask, render_template, render_template_string
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def render_with_back_button(title):
    return render_template_string(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{title}</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
        </head>
        <body class="d-flex justify-content-center align-items-center" style="height: 100vh; background-color: #f8f9fa;">
            <div class="text-center">
                <h3>{title} đã được mở!</h3>
                <a href="/" class="btn btn-primary mt-3">Quay về trang chủ</a>
            </div>
        </body>
        </html>
    """)

@app.route("/caesar")
def run_caesar():
    subprocess.Popen(["python", "caesar_cipher.py"])
    return render_with_back_button("Caesar Cipher")

@app.route("/vigenere")
def run_vigenere():
    subprocess.Popen(["python", "vigenere_cipher.py"])
    return render_with_back_button("Vigenere Cipher")

@app.route("/playfair")
def run_playfair():
    subprocess.Popen(["python", "playfair_cipher.py"])
    return render_with_back_button("Playfair Cipher")

@app.route("/railfence")
def run_railfence():
    subprocess.Popen(["python", "railfence_cipher.py"])
    return render_with_back_button("Railfence Cipher")

if __name__ == "__main__":
    app.run(debug=True)
