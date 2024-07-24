
from flask import Flask,request,jsonify
import products_doa
from sqlconnection import get_sql_connection
import uom_dao
import orders_doa
import json
# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)
connection=get_sql_connection()

# The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.
@app.route('/getProducts',methods=['GET'])
# ‘/’ URL is bound with hello_world() function.
def get_products():
    products=products_doa.get_all_products(connection)
    response=jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/deleteProduct',methods=['POST'])

def delete_products():
    return_id=products_doa.delete_product(connection,request.form['product_id'])
    response=jsonify({
        'product_id': return_id
                   })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_doa.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_doa.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/getOrderDetails', methods=['GET'])
def get_order_details():
    response=orders_doa.get_order_details(connection,request.form['order_id'])
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_doa.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    print("Starting python flask server for Grocery Store Management System")
    app.run(port=5000)