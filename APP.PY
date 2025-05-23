from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # نقرأ API Key من متغير بيئة

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "أنت مساعد ذكي تتحدث باللهجة السعودية، تجاوب على الاستفسارات بطريقة ودودة، "
                        "وتستخدم تعبيرات دارجة مثل (تم، أبد، على خشمي، تمام، زين). خلك واضح وبسيط، "
                        "وتجنب الكلمات الفصحى الثقيلة."
                    )
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )
        return jsonify({"reply": response["choices"][0]["message"]["content"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
