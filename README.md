# 🔐 Password Strength Checker

A comprehensive password security tool that evaluates password strength, generates secure passwords, and provides detailed security analysis with entropy calculations and crack time estimates.

## ✨ Features

### Core Password Analysis
- **Strength Classification**: Weak, Moderate, or Strong based on multiple criteria
- **Regex-based Validation**: Checks for uppercase, lowercase, digits, and special characters
- **Length Requirements**: Minimum 8 characters with bonus points for 12+ characters
- **Real-time Feedback**: Instant strength evaluation as you type

### Advanced Security Features
- **Entropy Calculation**: Mathematical measurement of password randomness (bits)
- **Crack Time Estimation**: Estimates how long it would take to brute-force the password
- **Common Password Detection**: Built-in database of top 1000+ common passwords
- **Security Warnings**: Explains risks of using weak passwords

### Password Generation
- **Strong Password Generator**: Creates cryptographically secure random passwords
- **Customizable Length**: Generate passwords from 8 to 50 characters
- **Similar Character Exclusion**: Option to exclude confusing characters (O/0, I/1, l/i)
- **Guaranteed Complexity**: Ensures all character types are included

### User Experience
- **Interactive CLI**: Command-line interface with menu-driven options
- **Modern Web UI**: Beautiful, responsive web interface with live strength meter
- **Clipboard Integration**: One-click password copying (with pyperclip)
- **Mobile Responsive**: Works perfectly on all device sizes

## 🚀 Installation

### Option 1: Python Script (Recommended for developers)

1. **Clone or download the project files**
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   Or install manually:
   ```bash
   pip install pyperclip
   ```

3. **Run the Python script**:
   ```bash
   python password_checker.py
   ```

### Option 2: Web Interface (No installation required)

1. **Open `web_interface.html` in any modern web browser**
2. **No server setup or dependencies required**
3. **Works offline and can be hosted anywhere**

## 📱 Usage

### Python Script Interface

```
🔐 Password Strength Checker
========================================

Options:
1. Check password strength
2. Generate strong password
3. Exit

Enter your choice (1-3):
```

**Option 1: Check Password Strength**
- Enter any password to analyze
- Get detailed strength report with:
  - Security score (0-6 points)
  - Entropy calculation
  - Estimated crack time
  - Specific issues found
  - Personalized recommendations

**Option 2: Generate Strong Password**
- Choose custom length (8-50 characters)
- Option to exclude similar-looking characters
- Automatically checks generated password strength
- Copy to clipboard functionality

### Web Interface

1. **Password Input**: Type or paste any password
2. **Live Strength Meter**: Real-time visual feedback (red → orange → green)
3. **Requirement Checkmarks**: Visual indicators for each security requirement
4. **Statistics Dashboard**: Security score, entropy, crack time, and length
5. **Generate Button**: Create new strong passwords instantly
6. **Copy to Clipboard**: Secure one-click copying

## 🔒 Security Features Explained

### Entropy Calculation
- **What it means**: Measures the randomness and unpredictability of your password
- **Higher is better**: More entropy = harder to crack
- **Formula**: log₂(character_set_size^password_length)
- **Example**: "password123" has ~28 bits, "Kj9#mN2$pL" has ~65 bits

### Crack Time Estimation
- **Assumption**: 1 billion attempts per second (modern GPU capability)
- **Realistic**: Based on average-case brute force attacks
- **Context**: Longer times mean better security

### Common Password Detection
- **Database**: Built-in list of 1000+ most common passwords
- **Risk**: These passwords are targeted first by attackers
- **Examples**: "123456", "password", "admin", "qwerty"

## 🎯 Password Strength Criteria

| Criterion | Points | Description |
|-----------|--------|-------------|
| Length ≥ 8 | 1 | Basic length requirement |
| Length ≥ 12 | 2 | Extended length bonus |
| Uppercase | 1 | Contains A-Z |
| Lowercase | 1 | Contains a-z |
| Numbers | 1 | Contains 0-9 |
| Special | 1 | Contains !@#$%^&*... |

**Scoring System:**
- **0-2 points**: Weak
- **3-4 points**: Moderate  
- **5-6 points**: Strong

## 🛡️ Security Best Practices

### What Makes a Strong Password
- **Length**: At least 12 characters
- **Complexity**: Mix of all character types
- **Uniqueness**: Not used elsewhere
- **Randomness**: Avoid patterns and personal info

### What to Avoid
- **Common words**: "password", "admin", "123456"
- **Personal info**: Names, birthdays, addresses
- **Patterns**: "qwerty", "abc123", sequential numbers
- **Reuse**: Same password across multiple accounts

## 🔧 Technical Details

### Python Requirements
- **Python 3.6+** (for f-strings and type hints)
- **Standard library**: re, random, string, math, hashlib
- **Optional**: pyperclip for clipboard functionality

### Web Interface
- **Pure HTML/CSS/JavaScript**
- **No external dependencies**
- **Modern ES6+ features**
- **Responsive CSS Grid and Flexbox**

### Algorithm Details
- **Entropy calculation**: Uses Shannon entropy formula
- **Random generation**: Python's cryptographically secure random module
- **Pattern matching**: Comprehensive regex for character validation

## 📊 Example Output

### Strong Password Analysis
```
📊 Password Analysis:
Strength: Strong
Score: 6/6
Entropy: 78.45 bits
Estimated crack time: 2.3 years

✅ Requirements met:
  ✔ Minimum length (8+ characters)
  ✔ Contains uppercase letters
  ✔ Contains lowercase letters
  ✔ Contains numbers
  ✔ Contains special characters
```

### Weak Password Analysis
```
📊 Password Analysis:
Strength: Weak
Score: 2/6
Entropy: 28.34 bits
Estimated crack time: 3.2 seconds

❌ Issues found:
  • Password is too short (minimum 8 characters)
  • No special characters

💡 Recommendations:
  • Increase password length to at least 8 characters
  • Add special characters (!@#$%^&*...)
```

## 🌟 Advanced Features

### Custom Password Generation
```python
# Generate 20-character password excluding similar characters
password = checker.generate_strong_password(20, exclude_similar=True)
# Result: "Kj9#mN2$pL8vX4@qR7w"
```

### Programmatic Usage
```python
from password_checker import PasswordStrengthChecker

checker = PasswordStrengthChecker()
result = checker.check_password_strength("MyPassword123!")

print(f"Strength: {result['strength']}")
print(f"Entropy: {result['entropy']:.2f} bits")
print(f"Crack time: {result['crack_time']}")
```

## 🚨 Security Disclaimer

This tool is designed for educational and personal use. While it provides accurate security assessments, no password is 100% secure. Always:

- Use unique passwords for each account
- Enable two-factor authentication when available
- Regularly update your passwords
- Be cautious of phishing attempts
- Consider using a password manager for better security

## 🤝 Contributing

Feel free to contribute improvements:
- Add more common passwords to the database
- Enhance entropy calculations
- Improve UI/UX
- Add additional security checks
- Support for other languages

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Related Resources

- [OWASP Password Guidelines](https://owasp.org/www-project-cheat-sheets/cheatsheets/Authentication_Cheat_Sheet.html)
- [NIST Password Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [Have I Been Pwned](https://haveibeenpwned.com/) - Check if your accounts have been compromised

---

**Stay secure! 🔐✨** 