import subprocess
import argparse
import datetime
parser = argparse.ArgumentParser(description='Read input')
year = datetime.date.today().year
day = datetime.date.today().day
SESSION = "53616c7465645f5fcd66d3270fb20f01c551a7329da18b998b6b7a569ae620d56fca563b6e75d680b4347b879093e5fcdbc3b2ef630dfe54c72b7ff541c4013b"
cmd = f'curl https://adventofcode.com/{year}/day/{day}/input --cookie "session={SESSION}"'
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')
with open("input.in", "w") as f:
    f.write(output)

