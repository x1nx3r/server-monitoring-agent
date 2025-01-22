import time
import grpc
from concurrent import futures

import psutil
from handlers.cpuMonitorHandler import getCpuPercentage, getCpuTimes, getCpuFreq
from handlers.memoryMonitorHandler import getTotalRam, getUsedRam, getAvailableRam, getRamUsage

import system_metrics_pb2
import system_metrics_pb2_grpc

# Define the gRPC client
class SystemMetricsClient:
    def __init__(self, channel):
        self.stub = system_metrics_pb2_grpc.SystemMetricsStub(channel)

    def send_metrics(self, metrics):
        request = system_metrics_pb2.MetricsRequest(
            cpu_usage=metrics['cpu_usage'],
            cpu_times=metrics['cpu_times'],
            cpu_frequency=metrics['cpu_frequency'],
            total_ram=metrics['total_ram'],
            used_ram=metrics['used_ram'],
            available_ram=metrics['available_ram'],
            ram_usage=metrics['ram_usage']
        )
        response = self.stub.SendMetrics(request)
        return response

def collect_metrics():
    metrics = {
        'cpu_usage': getCpuPercentage(),
        'cpu_times': getCpuTimes(),
        'cpu_frequency': getCpuFreq(),
        'total_ram': getTotalRam(),
        'used_ram': getUsedRam(),
        'available_ram': getAvailableRam(),
        'ram_usage': getRamUsage()
    }
    return metrics

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        client = SystemMetricsClient(channel)
        while True:
            metrics = collect_metrics()
            response = client.send_metrics(metrics)
            print(f"Server response: {response.message}")
            time.sleep(5)

if __name__ == '__main__':
    run()
