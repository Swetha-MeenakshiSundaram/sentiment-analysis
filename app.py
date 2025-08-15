from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load model & vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form["Review"]
        data = vectorizer.transform([message])
        prediction = model.predict(data)[0]
        result = "Positive" if prediction == 1 else "Negative"
        return render_template("index.html", prediction=result, message=message)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)