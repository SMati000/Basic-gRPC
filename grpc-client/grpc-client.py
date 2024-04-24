import grpc

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from printer import protobuf_test_pb2 as pb2
from printer import protobuf_test_pb2_grpc as pb2_grpc

def main():
    run()

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.PrinterStub(channel)
        response = stub.PrintThis(pb2.Mensaje(printThis='you'))
        print("Printer client received: " + response.printThis)
        print("Printer client received: sadsadasd")

if __name__ == '__main__':
    main()
