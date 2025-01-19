# QR Code Web Application

This project is a simple web application that generates QR codes from user-provided URLs. It is built using Flask and utilizes the `qrcode` library for QR code generation.

## Project Structure

```
qr-web-app
├── src
│   ├── app.py               # Main application file
│   ├── templates
│   │   └── index.html       # HTML template for user input and QR code display
│   └── static
│       └── qrcode.png       # Placeholder for the generated QR code image
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd qr-web-app
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   Start the Flask server by running:
   ```
   python src/app.py
   ```

4. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000` to access the QR code generator.

## Usage

- Enter a URL in the input field and submit the form.
- The application will generate a QR code for the provided URL and display it on the page.

## License

This project is licensed under the MIT License.