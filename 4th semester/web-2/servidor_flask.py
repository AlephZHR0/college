from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/user_mock", methods=["GET"])
def get_mock_user():
    #dados ficticios do usuario
    user = {
        "id": 1,
        "name": "Ophelia Watkins",
        "city": "São Paulo",
        "state": "SP",
        "address": "Paulista, 1234",
    }
    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)