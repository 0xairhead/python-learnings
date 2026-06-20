import subprocess

# Call a command and get the exit code
code = subprocess.call(["python3", "--version"])

if code == 0:
    print("Success")
else:
    print("Failed")
