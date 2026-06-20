import subprocess

try:
    # check_output raises an exception if the return code is non-zero
    output = subprocess.check_output(["python3", "--version"], text=True)
    print(output)
except subprocess.CalledProcessError:
    print("Command failed (returned non-zero exit code)")


try:
    # except scenario
    output = subprocess.check_output(["python3", "--versions"], text=True)
    print(output)
except subprocess.CalledProcessError:
    print("Command failed (returned non-zero exit code)")
