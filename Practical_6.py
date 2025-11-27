import os

source = "/home/hrishit/myproject/source_file.txt"
destination = "/home/hrishit/myproject/destination_file.txt"

src = os.open(source, os.O_RDONLY)
dst = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)

while True:
    data = os.read(src, 1024)
    if not data:
        break
    os.write(dst, data)

os.close(src)
os.close(dst)

print("File copied from " + source + " to " + destination)
