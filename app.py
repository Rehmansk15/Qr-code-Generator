from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate_qr_code", methods=["POST"])
def generate_qr_code():
    text = request.form.get("text")
    file_name = "qrcode.png"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

    return file_name

