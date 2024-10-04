import subprocess
import re
from collections import defaultdict
from datetime import datetime
from firewall import Firewall

# Threshold for blocking the IP
BLOCK_THRESHOLD = 5

# Dictionary to store the count of occurrences for each IP address
ip_count = defaultdict(int)

# Regular expression to extract IP from log line
ip_regex = re.compile(r'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)')

command = ['logread', '-e', "Bad password", '-S', '100']
# Continuously read the log lines from the logread command
process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)

for line in process.stdout:
    # Check if the line contains an IP address matching the pattern
    match = ip_regex.search(line)
    if match:
        ip = match.group(1)

        # Increment the count for this IP
        ip_count[ip] += 1

# After processing all lines, check counts and block IPs as needed
for ip, count in ip_count.items():
    if count > BLOCK_THRESHOLD:
        block_ip(ip)
