# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import currency_converter_pb2 as currency__converter__pb2


class CurrencyConverterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ConvertCurrency = channel.unary_unary(
            '/currency_converter.CurrencyConverter/ConvertCurrency',
            request_serializer=currency__converter__pb2.CurrencyConversionRequest.SerializeToString,
            response_deserializer=currency__converter__pb2.CurrencyConversionResponse.FromString,
        )


class CurrencyConverterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ConvertCurrency(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CurrencyConverterServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'ConvertCurrency': grpc.unary_unary_rpc_method_handler(
            servicer.ConvertCurrency,
            request_deserializer=currency__converter__pb2.CurrencyConversionRequest.FromString,
            response_serializer=currency__converter__pb2.CurrencyConversionResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'currency_converter.CurrencyConverter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))