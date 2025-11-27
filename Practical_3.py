'''import os

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
'''
'''
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
'''
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


