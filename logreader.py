import subprocess
import re
from collections import defaultdict
import configparser

class logreader:
    def __init__(self) -> None:
        self.ip_regex = re.compile(r'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)')
        self.read_config()

    def read_config(self) -> None:
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.BLOCK_THRESHOLD = config["DEFAULT"].get("BLOCK_THRESHOLD", 5)

    def read_log(self) -> None:
        ip_count = defaultdict(int)
        command = ['logread', '-e', "Bad password", '-S', '100']
        # Continuously read the log lines from the logread command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
        for line in process.stdout:
            # Check if the line contains an IP address matching the pattern
            match = self.ip_regex.search(line)
            if match:
                ip = match.group(1)
                ip_count[ip] += 1