from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# 加载模型（第一次运行会下载）
classifier = pipeline("sentiment-analysis")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.json.get("text")
    result = classifier(text)[0]
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)