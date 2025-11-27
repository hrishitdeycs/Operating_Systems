import os

# Print initial process info before fork
print("Before fork: PID =", os.getpid(), "PPID =", os.getppid())

# Create a child process
pid = os.fork()

# After fork, both parent and child continue executing the same code from here
# They both execute the same instructions below, but have different PIDs

print("After fork: PID =", os.getpid(), "PPID =", os.getppid())

if pid > 0:
    # This branch is only executed by the parent
    print("This is the parent process (PID =", os.getpid(), ")")
elif pid == 0:
    # This branch is only executed by the child
    print("This is the child process (PID =", os.getpid(), ")")
else:
    # Fork failed
    print("Fork failed!")

# Both parent and child continue executing the same program here
print("Both parent and child are executing the same code: PID =", os.getpid())
