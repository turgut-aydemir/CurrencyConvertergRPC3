import grpc
import currency_converter_pb2
import currency_converter_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = currency_converter_pb2_grpc.CurrencyConverterStub(channel)

    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the source currency: ")
    to_currency = input("Enter the target currency: ")

    request = currency_converter_pb2.CurrencyConversionRequest(amount=amount, from_currency=from_currency, to_currency=to_currency)
    response = stub.ConvertCurrency(request)

    print(f"Amount: {amount}")
    print(f"From Currency: {from_currency}")
    print(f"To Currency: {to_currency}")
    print(f"Result: {response.result}")

if __name__ == '__main__':
    run()