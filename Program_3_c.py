import os

# Print initial process info before fork
print("Before fork: PID =", os.getpid(), "PPID =", os.getppid())

# Create a child process
pid = os.fork()
# After fork, both parent and child continue executing from here
print("After fork: PID =", os.getpid(), "PPID =", os.getppid())
if pid > 0:
    # Parent process branch
    print("This is the parent process (PID =", os.getpid(), ")")
    # Parent waits for the child to finish before terminating
    os.waitpid(pid, 0)  # Wait for specific child PID
    print("Child has finished. Parent terminating now.")    
elif pid == 0:
    # Child process branch
    print("This is the child process (PID =", os.getpid(), ")")    
else:
    # Fork failed
    print("Fork failed!")
# Both parent and child continue executing from here
# This line runs in both processes, but in the parent it runs after child finishes
print("Both parent and child are executing the same code: PID =", os.getpid())


