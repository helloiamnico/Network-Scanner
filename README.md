# 🔍 Python Network Scanner

A professional network scanning tool built with Python, Gradio, and Nmap. This project was developed as part of a red teaming assignment to assist in identifying devices, scanning ports, detecting running services, and optionally running vulnerability detection scripts — all through a clean, user-friendly web interface.

---

## ✅ Features

- 🌐 Scan individual IPs or full subnets (e.g., `192.168.1.0` or `192.168.1.0/24`)
- 🔓 Detect open ports and service versions
- 📄 Save results to `scan_information.txt`
- 📂 View all past scans within the interface
- 💡 Optional vulnerability detection via Nmap's `--script vuln`
- 🎯 Real-time progress and status updates
- 💾 Downloadable scan reports
- 🎨 Styled like a security dashboard (Gradio + theme)
- 🔁 “Clear” button resets the interface for new scans

---

## 🖥️ Requirements

- Python 3.10+
- [Nmap](https://nmap.org/download.html) (must be added to your system PATH)
- Dependencies (install via pip):
  pip install gradio nmap
🚀 How to Run
Clone this repository or download the script directly.

Open a terminal in the project folder.

Run:


python network_scanner.py
The tool will open a local Gradio interface (e.g., http://127.0.0.0:)

Enter a target IP or subnet and click 🚀 Generate Scan

Use 📂 Scan Results to view previous logs

Click the download icon to save the results file

🔍 Example Output

===== Scan Run (2025-05-01 00:40:00 =====
Target: 192.168.0.0
Starting Nmap 7.X( https://nmap.org )
Nmap scan report for 192.168.0.0
Host is up (0.19s latency).

PORT    STATE  SERVICE
22/tcp  closed ssh
80/tcp  closed http
443/tcp closed https
MAC Address: xx:xx:xx:xx:xx:xx
⚠️ Notes
Nmap must be correctly installed and available in your system PATH.

Scans can take time depending on network size and scan mode.

This tool is designed for ethical, legal testing only.

Use responsibly and only on networks you have permission to scan.

