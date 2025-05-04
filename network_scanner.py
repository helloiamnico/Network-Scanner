import gradio as gr
import subprocess
from datetime import datetime
import os

# === Configuration ===
NMAP_PATH = r"C:\Program Files (x86)\Nmap\nmap.exe"  # Adjust if needed
OUTPUT_FILE = "scan_information.txt"

# === Scan Function ===
def scan_network(target_ip, enable_vuln):
    if not target_ip.strip():
        return "[!] Please enter a valid IP or subnet.", gr.update(visible=False)

    try:
        # Determine arguments based on toggle
        args = "-p 22,80,443"
        if enable_vuln:
            args += " --script vuln"

        command = f'"{NMAP_PATH}" {args} {target_ip}'
        result = subprocess.check_output(command, shell=True, text=True)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output = f"===== Scan Run ({timestamp}) =====\nTarget: {target_ip}\n{result}\n"

        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(output)

        return output, gr.update(visible=True, value=OUTPUT_FILE)

    except subprocess.CalledProcessError as e:
        return f"[!] Scan failed: {e}", gr.update(visible=False)

# === Show Saved Logs ===
def show_logs():
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            return f.read()
    return "[!] No past scans found."

# === Clear Inputs ===
def clear_all():
    return "", "", gr.update(visible=False)

# === Gradio Interface ===
with gr.Blocks(title="🛡️ Python Network Scanner", theme=gr.themes.Soft()) as app:
    gr.Markdown("## 🛡️ <span style='color:#00aaff;'>Python Network Scanner</span>")
    gr.Markdown("Scan for open ports, services, and optional vulnerabilities with Nmap. Logs are saved to `scan_information.txt`.")

    with gr.Row():
        ip_input = gr.Textbox(label="🎯 Target IP or Subnet", placeholder="e.g., 192.168.1.5 or 192.168.1.0/24")
        vuln_toggle = gr.Checkbox(label="🧪 Enable Vulnerability Scripts (--script vuln)", value=False)

    with gr.Row():
        generate_btn = gr.Button("🚀 Generate Scan")
        clear_btn = gr.Button("🧹 Clear")
        logs_btn = gr.Button("📂 Scan Results")

    with gr.Row():
        scan_output = gr.Textbox(label="📊 Scan Output", lines=20, show_copy_button=True)
        download_btn = gr.File(label="⬇️ Download Results", visible=False)

    # === Button Actions ===
    generate_btn.click(fn=scan_network, inputs=[ip_input, vuln_toggle], outputs=[scan_output, download_btn])
    clear_btn.click(fn=clear_all, outputs=[ip_input, scan_output, download_btn])
    logs_btn.click(fn=show_logs, outputs=scan_output)

# === Run App ===
app.launch(share=True)