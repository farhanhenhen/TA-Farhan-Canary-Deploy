from flask import Flask, jsonify, request

app = Flask(__name__)

def generate_complex_data(n):
    complex_data = []

    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    for m in range(n):
                        complex_data.append({
                            'index_i': i,
                            'index_j': j,
                            'index_k': k,
                            'index_l': l,
                            'index_m': m,
                            'result': i * j * k * l * m  # Sesuaikan 
                        })

    return complex_data

@app.route('/', methods=['GET'])
def test_api():
    n = 3  # Ganti nilai n sesuai kebutuhan Anda
    complex_data = generate_complex_data(n)

    return jsonify({
        'source': request.url_root,
        'complex_data': complex_data,
        'message': 'success'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
