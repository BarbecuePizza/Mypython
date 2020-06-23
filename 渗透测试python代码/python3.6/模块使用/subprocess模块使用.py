import subprocess

def run_command():
    while True:
        try:
            command = input("shell_>")
            out = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
            print(out.decode())
        except:
            print("Failse to execute the command")

run_command()