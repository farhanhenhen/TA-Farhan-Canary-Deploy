from flask import Flask, jsonify, request

app= Flask(__name__)

@app.route('/', methods=['GET'])
def test_api():
  if request.headers.getlist("X-Forwarded-For"):
   ip = request.headers.getlist("X-Forwarded-For")[0]
  else:
   ip = request.remote_addr
  return jsonify(
    {
      'source': request.host_url,
      'message': 'success'
    }
  )

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=False)