from flask import Flask
from controllers.home_controller import index, calculate

app = Flask(__name__)

# Rutas
app.add_url_rule("/", view_func=index, methods=["GET"])
app.add_url_rule("/calculate", view_func=calculate, methods=["POST"])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
