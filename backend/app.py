from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# ------------------- CONTACT -------------------
@app.route("/contact", methods=["POST"])
def contact_form():
    data = request.form

    name = data.get("nom")
    email = data.get("email")
    subject = data.get("sujet")
    message = data.get("message")

    print("\n===== 📩 NOUVEAU MESSAGE CONTACT =====")
    print("Nom :", name)
    print("Email :", email)
    print("Sujet :", subject)
    print("Message :", message)

    return jsonify({"status": "success"})


# ------------------- NOUS REJOINDRE -------------------
@app.route("/join", methods=["POST"])
def join_form():
    data = request.form

    name = data.get("nom")
    email = data.get("email")
    role = data.get("poste")
    message = data.get("message")

    print("\n===== 🧑‍💼 NOUVELLE CANDIDATURE =====")
    print("Nom :", name)
    print("Email :", email)
    print("Poste :", role)
    print("Message :", message)

    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(debug=True)
