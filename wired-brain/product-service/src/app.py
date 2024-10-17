from flask import Flask, jsonify, request

products = [
    {'id': 1, 'name': 'Product 1'},
    {'id': 2, 'name': 'Product 2'}
]

app = Flask(__name__)

# curl -v http://localhost:5001/products
@app.route('/products')
def get_products():
    return jsonify(products)

# curl -v http://localhost:5001/product/1
@app.route('/product/<int:id>')
def get_product(id):
    product_list = [product for product in products if product['id'] == id]
    if len(product_list) == 0:
        return f'Producrt with id {id} not found', 404
    return jsonify(product_list[0])

# curl --header "Content-Type: application/json" --request POST --data '{"name": "Product 3"}' -v http://localhost:5001/product/3
@app.route('/product', methods=['POST'])
def post_product():
    #retrieve the product from the request body
    request_product = request.json
    new_id = max([product['id'] for product in products]) +1
    new_product = {
        'id': new_id,
        'name': request_product['name']
    }
    products.append(new_product)
    return jsonify(new_product), 201

app.route('/product/<int:id', methods=['PUT'])
def put_product(id):
    updated_product = request.json
    
    for product in products:
        if product['id'] == id:
            product['name'] = updated_product['name']
            return jsonify(product), 200
    return f'Product with id {id} not found', 404

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product_list = [product for product in products if product['id'] == id]
    if len(product_list) == 1:
        products.remove(product_list[0])
        return f'Product with id {id} deleted', 200
    return f'Poroduct with id {id} not found', 404

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5001)