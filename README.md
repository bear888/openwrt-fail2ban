# OpenWRT SSH Protection with Python Script

This project provides a simple Python script designed for OpenWRT users who want to block repeated failed SSH password attempts. OpenWRT lacks the traditional auth.log file, which Fail2Ban typically uses to monitor and block malicious login attempts. This script solves that problem by reading directly from the system logs, detecting bad password attempts, and blocking IP addresses with multiple failed login attempts.

## Features

* Blocks IPs that repeatedly fail to log in via SSH.
* Designed specifically for OpenWRT, which doesn’t provide an auth.log file by default.
* Can be run periodically (e.g., every 15 minutes) using a cron job.
* Lightweight and easy to configure.

## Prerequisites

* OpenWRT installed on your router.
* Python installed on OpenWRT (use opkg install python to install it).
* Firewall enabled (using iptables or nftables).

## How It Works

1. The script reads from the system log (logread) to detect failed password attempts for SSH.
2. It counts how many times an IP address fails to log in.
3. If an IP address exceeds a certain threshold of failed attempts (configurable in the script), the script blocks that IP using iptables.

## License

This project is licensed under the MIT License.

Let me know if you’d like any changes!
