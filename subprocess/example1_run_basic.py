import subprocess

# Run a command and capture the output
res = subprocess.run(["python3", "--version"], capture_output=True, text=True)
print(res.stdout)
