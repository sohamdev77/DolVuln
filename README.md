# DolVuln - Web Vulnerability Scanner

## Overview
DolVuln is a simple, yet effective, web vulnerability scanner that helps identify common vulnerabilities like open ports and server information leaks. Built using Python, it is designed to work in the Windows terminal or Kali terminal.

## Features
- Scans common ports (80, 443, 8080, etc.)
- Detects server info leaks in HTTP headers
- Works on Windows, Termux, Kali Linux

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DolVuln.git
   cd DolVuln
Install required dependencies:

pip install -r requirements.txt

Usage
Run the scanner:

python dolvuln.py

Enter the target website or IP address, and the tool will check for common vulnerabilities.