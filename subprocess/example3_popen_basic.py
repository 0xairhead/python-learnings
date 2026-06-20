import subprocess

# 1. Start python3 interpreter and redirect stdin/stdout pipes
process = subprocess.Popen(
    ["python3"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

# 2. Send code ("print(5 + 5)") into the python process and read the response
# output captures the first element (the standard output of the process, which is 10).
# _ captures the second element (the standard error output, which in this case is empty/None or an empty string "" because there were no errors).
output, _ = process.communicate("print(5 + 5)")
print(output)  # Outputs: 10
