import platform
import os
# Linux Kernel Information
print("=== Linux Kernel Information ===")
print("Kernel Version:", platform.release())
print("Kernel Name:", platform.system())
print("Kernel Architecture:", platform.machine())
print()
# CPU Information
print("=== CPU Information ===")
print("Processor:", platform.processor())
if os.path.exists("/proc/cpuinfo"):
    with open("/proc/cpuinfo") as f:
        lines = f.read().splitlines()
    
    # Get first model name
    model_lines = [line for line in lines if "model name" in line]
    if model_lines:
        print("CPU Model:", model_lines[0].split(":")[1].strip())
    
    # Count number of cores
    cpu_cores = sum(1 for line in lines if line.startswith("processor"))
    print("Number of CPU Cores:", cpu_cores)
else:
    print("Cannot read /proc/cpuinfo. Not running on Linux?")

