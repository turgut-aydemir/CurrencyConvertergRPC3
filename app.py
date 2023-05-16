from flask import Flask, render_template
import requests
import grpc
import currency_converter_pb2
import currency_converter_pb2_grpc

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']

        channel = grpc.insecure_channel('localhost:50051')
        stub = currency_converter_pb2_grpc.CurrencyConverterStub(channel)

        request = currency_converter_pb2.CurrencyConversionRequest(amount=amount, from_currency=from_currency, to_currency=to_currency)
        response = stub.ConvertCurrency(request)

        result = response.result
        return render_template('index.html', result=result, amount=amount, from_currency=from_currency, to_currency=to_currency)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
