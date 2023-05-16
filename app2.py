import grpc
from flask import Flask, render_template, jsonify
from flask_grpc import grpcify
from grpc import ssl_channel_credentials
import requests
import currency_converter_pb2
import currency_converter_pb2_grpc

app = Flask(__name__)

# Create the gRPC channel using SSL credentials
channel = grpc.insecure_channel('localhost:50051')
stub = currency_converter_pb2_grpc.CurrencyConverterStub(channel)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']

    request = currency_converter_pb2.CurrencyConversionRequest(
        amount=amount, from_currency=from_currency, to_currency=to_currency
    )
    response = stub.ConvertCurrency(request)

    return jsonify({'result': response.result})

if __name__ == '__main__':
    grpcify(app, [channel], ssl=False)
    app.run()
