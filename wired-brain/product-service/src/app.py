from flask import Flask, jsonify, request
from db import db
from Product import Product

products = [
    {'id': 1, 'name': 'Product 1'},
    {'id': 2, 'name': 'Product 2'}
]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@db/products'
db.init_app(app)

# curl -v http://localhost:5001/products
@app.route('/products')
def get_products():
    products = [product.json for product in Product.find_all()]
    return jsonify(products)

# curl -v http://localhost:5001/product/1
@app.route('/product/<int:id>')
def get_product(id):
    product = Product.find_by_id()
    if product:
        return jsonify(product.json)
    return f'Producrt with id {id} not found', 404
    

# curl --header "Content-Type: application/json" --request POST --data '{"name": "Product 3"}' -v http://localhost:5001/product/3
@app.route('/product', methods=['POST'])
def post_product():
    #retrieve the product from the request body
    print('POST /product')
    
    request_product = request.json

    product = Product(None, request_product['name'])
    
    product.save_to_db()
    
    return jsonify(product.json), 201

app.route('/product/<int:id', methods=['PUT'])
def put_product(id):
    existing_product = Product.find_by_id(id)
    
    if existing_product:
        updated_product = request.json
        
        existing_product.name = updated_product['name']
        existing_product.save_to_db()
        
        return jsonify(existing_product.json), 200

    return f'Product with id {id} not found', 404
        

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    existing_product = Product.find_by_id(id)
    if existing_product:
        existing_product.delete_from_db()
        
        return jsonify({'message':f'Product with id {id} deleted'}), 200
    return f'Poroduct with id {id} not found', 404

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5001)