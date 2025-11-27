
import os

# Print initial process info before fork
print("Before fork: PID =", os.getpid(), "PPID =", os.getppid())

# Create a child process
pid = os.fork()
# After fork, both parent and child continue executing from here
print("After fork: PID =", os.getpid(), "PPID =", os.getppid())
# Branching based on PID to execute different code in parent and child
if pid > 0:
    # Parent process branch
    # Even though it's the same program file, the parent executes this part
    print("This is the parent process (PID =", os.getpid(), ")")
elif pid == 0:
    # Child process branch
    # The child executes this part of the code
    print("This is the child process (PID =", os.getpid(), ")")
else:
    # Fork failed
    print("Fork failed!")
# Both parent and child continue executing from here
# This line is common and runs in both processes
# It's part of the same program, but each process has already executed different code above
print("Both parent and child are executing the same code: PID =", os.getpid())

