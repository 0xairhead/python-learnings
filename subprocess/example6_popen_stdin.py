import subprocess

# Open Python in interactive mode, send a print command, and capture the stdout output
process = subprocess.Popen(
    ["python3"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

output, _ = process.communicate("print(5 + 5)")
print(output)
