from basic_transactions_gp import blockchain

from flask import Flask

FLASK_APP = "basic_transactions_gp/blockchain.py"

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# # Load ID
# f = open("my_id.txt", "r")
# id = f.read()
# print("ID is", id)
# f.close()

# Instantiate our app
app = Flask(__name__)

# Run the program on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
