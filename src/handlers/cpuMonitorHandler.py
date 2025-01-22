# cpuMonitorHandler.py
#
# This module provides functions to monitor and report on CPU usage and statistics.
#

import psutil
import time

# CPU usage percentage (system-wide)
def getCpuPercentage():
    """
    Returns the CPU usage percentage system-wide over a 1-second interval.

    Sample Output:
    "CPU Usage: 15.0%"
    """
    cpu_percent = psutil.cpu_percent(interval=1)  # 1-second interval
    return f"CPU Usage: {cpu_percent}%"

# CPU times (system-wide)
def getCpuTimes():
    """
    Returns the CPU times for user, system, and idle states.

    Sample Output:
    "CPU Times: user=12345.67s, system=2345.67s, idle=34567.89s"
    """
    cpu_times = psutil.cpu_times()
    return f"CPU Times: user={cpu_times.user}s, system={cpu_times.system}s, idle={cpu_times.idle}s"

# CPU frequency (current frequency in MHz)
def getCpuFreq():
    """
    Returns the current CPU frequency in MHz, along with the minimum and maximum frequencies.

    Sample Output:
    "CPU Frequency: 2400.0 MHz (min: 800.0 MHz, max: 3500.0 MHz)"
    """
    cpu_freq = psutil.cpu_freq()
    return f"CPU Frequency: {cpu_freq.current} MHz (min: {cpu_freq.min} MHz, max: {cpu_freq.max} MHz)"
