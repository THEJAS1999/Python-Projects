from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form["url"]  # Get the URL from the form
        if url:
            # Generate QR Code for the URL
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(url)
            qr.make(fit=True)

            # Create an image of the QR Code
            img = qr.make_image(fill="black", back_color="white")
            
            # Save the image to a BytesIO object
            img_io = BytesIO()
            img.save(img_io, 'PNG')
            img_io.seek(0)

            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name="qr_code.png")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
