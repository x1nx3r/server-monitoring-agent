import psutil
import time

def monitor_cpu():
    print("CPU Monitoring:")

    # CPU usage percentage (system-wide)
    cpu_percent = psutil.cpu_percent(interval=1)  # 1-second interval
    print(f"CPU Usage: {cpu_percent}%")

    # CPU times (system-wide)
    cpu_times = psutil.cpu_times()
    print(f"CPU Times: user={cpu_times.user}s, system={cpu_times.system}s, idle={cpu_times.idle}s")

    # CPU frequency (current frequency in MHz)
    cpu_freq = psutil.cpu_freq()
    print(f"CPU Frequency: {cpu_freq.current} MHz (min: {cpu_freq.min} MHz, max: {cpu_freq.max} MHz)")

def monitor_memory():
    print("\nMemory Monitoring:")

    # Virtual memory usage
    virtual_memory = psutil.virtual_memory()
    print(f"Total Memory: {virtual_memory.total / (1024**3):.2f} GB")
    print(f"Used Memory: {virtual_memory.used / (1024**3):.2f} GB")
    print(f"Available Memory: {virtual_memory.available / (1024**3):.2f} GB")
    print(f"Memory Usage: {virtual_memory.percent}%")

    # Swap memory usage
    swap_memory = psutil.swap_memory()
    print(f"Total Swap: {swap_memory.total / (1024**3):.2f} GB")
    print(f"Used Swap: {swap_memory.used / (1024**3):.2f} GB")
    print(f"Free Swap: {swap_memory.free / (1024**3):.2f} GB")
    print(f"Swap Usage: {swap_memory.percent}%")

if __name__ == "__main__":
    monitor_cpu()
    monitor_memory()
