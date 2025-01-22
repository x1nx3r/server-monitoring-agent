# memoryMonitorHandler.py
#
# This module provides functions to monitor and report on system memory usage.
#

import psutil
import time

def getTotalRam():
    """
    Returns the total amount of RAM in the system.

    Sample Output:
    "Total Memory: 16.00 GB"
    """
    virtual_memory = psutil.virtual_memory()
    return f"Total Memory: {virtual_memory.total / (1024**3):.2f} GB"

def getUsedRam():
    """
    Returns the amount of used RAM in the system.

    Sample Output:
    "Used Memory: 8.00 GB"
    """
    virtual_memory = psutil.virtual_memory()
    return f"Used Memory: {virtual_memory.used / (1024**3):.2f} GB"

def getAvailableRam():
    """
    Returns the amount of available RAM in the system.

    Sample Output:
    "Available Memory: 7.50 GB"
    """
    virtual_memory = psutil.virtual_memory()
    return f"Available Memory: {virtual_memory.available / (1024**3):.2f} GB"

def getRamUsage():
    """
    Returns the percentage of RAM usage in the system.

    Sample Output:
    "Memory Usage: 50.0%"
    """
    virtual_memory = psutil.virtual_memory()
    return f"Memory Usage: {virtual_memory.percent}%"
