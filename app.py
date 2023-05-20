from flask import Flask, render_template, request
import grpc
import currency_converter_pb2
import currency_converter_pb2_grpc

app = Flask(__name__)

# Initialize the gRPC channel and stub
creds = grpc.ssl_channel_credentials()
channel = grpc.secure_channel('currencyconvertergrpc-server.azurewebsites.net', creds)
stub = currency_converter_pb2_grpc.CurrencyConverterStub(channel)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert_currency():
    amount = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']

    request_message = currency_converter_pb2.CurrencyConversionRequest(
        amount=amount, from_currency=from_currency, to_currency=to_currency
    )

    response = stub.ConvertCurrency(request_message)
    result = response.result

    return f"Result: {result}"


if __name__ == '__main__':
    app.run()
