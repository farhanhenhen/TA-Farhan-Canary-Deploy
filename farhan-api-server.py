from flask import Flask, jsonify, request

app= Flask(__name__)

@app.route('/', methods=['GET'])
def test_api():
    return jsonify(
        {
            'source': request.url_root,
            'message': 'success'
        }
    )

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=False)