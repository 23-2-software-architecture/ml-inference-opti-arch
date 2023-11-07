import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from concurrent import futures
import grpc
import numpy as np
from tensorflow import make_ndarray
from tensorflow import make_tensor_proto
from tensorflow.keras.models import load_model
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc

class PredictionServiceServicer(prediction_service_pb2_grpc.PredictionServiceServicer):
    def __init__(self):
        self.model = load_model('./mobilenet_v1')

    def Predict(self, request, context):
        model_input = make_ndarray(request.inputs["input_1"])
        model_output = self.model.predict([model_input])
        response = predict_pb2.PredictResponse()
        response.outputs["output"].CopyFrom(make_tensor_proto(model_output, shape=list(model_output.shape)))
        return response

def serve():
    print("Starting grpc server...")
    server_options = [
        ('grpc.max_send_message_length', 50*1024*1024),
        ('grpc.max_receive_message_length', 50*1024*1024)
    ]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1000), options=server_options)
    prediction_service_pb2_grpc.add_PredictionServiceServicer_to_server(PredictionServiceServicer(), server)
    server.add_insecure_port('[::]:8500')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
