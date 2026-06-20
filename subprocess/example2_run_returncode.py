import subprocess

# Run a command and capture output and return code
res = subprocess.run(["python3", "--version"], capture_output=True, text=True)
print("Output:", res.stdout)
print("Return Code:", res.returncode)
