import grpc
from concurrent import futures
import time

import system_metrics_pb2
import system_metrics_pb2_grpc

class SystemMetricsServicer(system_metrics_pb2_grpc.SystemMetricsServicer):
    def SendMetrics(self, request, context):
        print(f"Received metrics: {request}")
        return system_metrics_pb2.MetricsResponse(message="Metrics received successfully")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    system_metrics_pb2_grpc.add_SystemMetricsServicer_to_server(SystemMetricsServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
