import os
import time

pid = os.fork()

if pid == 0:
    # Child process
    print("Child process. My PID is:", os.getpid(), " My parent PID is:", os.getppid())
    time.sleep(5)  # just to keep child alive a little
else:
    # Parent process
    print("Parent process. My PID is:", os.getpid(), " I created a child with PID:", pid)
    os.wait()
