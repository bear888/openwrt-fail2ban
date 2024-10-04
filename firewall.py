import subprocess
from datetime import datetime
import configparser

class Firewall:
    def __init__(self) -> None:
        self.read_config()

    def read_config(self) -> None:
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.LOG_FILE = config["DEFAULT"].get("LOG_FILE", "/var/log/ip_block.log")

    def log(self, msg: str) -> None:
        with open(self.LOG_FILE, "a") as log_file:
            log_file.write(f"{datetime.now()} - {msg}")

    def clear_all_input_rule(self) -> None:
        clear_iptable_rule = ['iptables', '-F' , 'INPUT']
        subprocess.run(clear_iptable_rule, check=True)
        self.log("Clear all input rule\n")

    def block_ip(self, ip: str) -> None:
        # Command to block the IP using iptables (you can modify for nftables if needed)
        print(f"Blocking IP: {ip}")
        subprocess.run(["iptables", "-I", "INPUT", "-s", ip, "-j", "DROP"], check=True)
        self.log(f"Blocked IP {ip} due to > 5 attempts\n")
    