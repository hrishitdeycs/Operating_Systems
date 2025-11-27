meminfo = {}

# Read /proc/meminfo
for line in open("/proc/meminfo", "r"):
    parts = line.split(":")
    key = parts[0].strip()
    value = parts[1].strip()
    meminfo[key] = value

# Extract needed fields
total = int(meminfo["MemTotal"].split()[0]) // 1024
free = int(meminfo["MemFree"].split()[0]) // 1024
available = int(meminfo["MemAvailable"].split()[0]) // 1024
buffers = int(meminfo["Buffers"].split()[0]) // 1024
cached = int(meminfo["Cached"].split()[0]) // 1024

used = total - available
print("\n====== Linux Memory Report ======\n")
print("Total Memory     : " + str(total) + " MB")
print("Used Memory      : " + str(used) + " MB")
print("Free Memory      : " + str(free) + " MB")
print("Available Memory : " + str(available) + " MB")
print("Buffers          : " + str(buffers) + " MB")
print("Cached           : " + str(cached) + " MB")
print("\n=================================\n")
