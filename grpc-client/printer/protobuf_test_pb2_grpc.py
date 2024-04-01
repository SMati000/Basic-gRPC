# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from printer import protobuf_test_pb2 as printer_dot_protobuf__test__pb2


class PrinterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PrintThis = channel.unary_unary(
                '/printer.Printer/PrintThis',
                request_serializer=printer_dot_protobuf__test__pb2.Mensaje.SerializeToString,
                response_deserializer=printer_dot_protobuf__test__pb2.Mensaje.FromString,
                )


class PrinterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PrintThis(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PrinterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PrintThis': grpc.unary_unary_rpc_method_handler(
                    servicer.PrintThis,
                    request_deserializer=printer_dot_protobuf__test__pb2.Mensaje.FromString,
                    response_serializer=printer_dot_protobuf__test__pb2.Mensaje.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'printer.Printer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Printer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PrintThis(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/printer.Printer/PrintThis',
            printer_dot_protobuf__test__pb2.Mensaje.SerializeToString,
            printer_dot_protobuf__test__pb2.Mensaje.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)