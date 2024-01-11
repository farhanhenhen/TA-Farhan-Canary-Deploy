from flask import Flask, jsonify, request

app= Flask(_name_)

@app.route('/', methods=['GET'])
def test_api():
    return jsonify(
        {
            'source': request.url_root,
            'message': 'success'
        }
    )

if _name_ == '_main_':
     app.run(host='10.0.1.2', port=5000, debug=False)