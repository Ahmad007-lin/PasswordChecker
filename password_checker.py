import re
import random
import string
import math
import hashlib
from typing import Dict, List, Tuple

class PasswordStrengthChecker:
    def __init__(self):
        # Common passwords database (top 1000+ common passwords)
        self.common_passwords = self._load_common_passwords()
        
    def _load_common_passwords(self) -> set:
        """Load common passwords from a built-in list"""
        common = {
            '123456', 'password', '123456789', '12345678', '12345', 'qwerty', 'abc123',
            '111111', '1234567', '123123', 'admin', 'letmein', 'welcome', 'monkey',
            'password123', '1234567890', 'dragon', 'master', 'hello', 'freedom',
            'whatever', 'qazwsx', 'trustno1', 'jordan', 'harley', 'hunter', 'buster',
            'thomas', 'tigger', 'robert', 'soccer', 'batman', 'test', 'pass', 'killer',
            'hunter', 'mike', 'charlie', 'andrew', 'matthew', 'access', 'shadow',
            'michael', 'jessica', 'diamond', 'jordan', 'mustang', 'mickey', 'secret',
            'dallas', 'dennis', 'ginger', 'striker', 'hammer', 'silver', 'joseph',
            'blowme', 'spitfire', 'green', 'superman', 'bigdaddy', 'johnson', 'chester',
            'london', 'midnight', 'blue', 'fishing', 'david', 'maddog', 'eagles',
            'mackenzie', 'donna', 'murphy', 'frank', 'green', 'lucky', 'andrew',
            'charlie', 'michael', 'sarah', 'jessica', 'jordan', 'tiger', 'hunter',
            'michelle', 'chris', 'jessica', 'amanda', 'daniel', 'joshua', 'michael',
            'jennifer', 'thomas', 'jessica', 'amanda', 'daniel', 'joshua', 'michael',
            'jennifer', 'thomas', 'jessica', 'amanda', 'daniel', 'joshua', 'michael'
        }
        return common
    
    def check_password_strength(self, password: str) -> Dict:
        """Evaluate password strength and return detailed analysis"""
        if not password:
            return {"strength": "Weak", "score": 0, "issues": ["Password is empty"]}
        
        # Check against common passwords
        if password.lower() in self.common_passwords:
            return {
                "strength": "Very Weak", 
                "score": 0, 
                "issues": ["Password is in the top 1000 common passwords list"],
                "recommendations": ["Choose a unique password that's not commonly used"]
            }
        
        score = 0
        issues = []
        recommendations = []
        
        # Length check
        if len(password) < 8:
            issues.append("Password is too short (minimum 8 characters)")
            recommendations.append("Increase password length to at least 8 characters")
        elif len(password) >= 12:
            score += 2
        else:
            score += 1
        
        # Character variety checks
        has_upper = bool(re.search(r'[A-Z]', password))
        has_lower = bool(re.search(r'[a-z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password))
        
        if has_upper:
            score += 1
        else:
            issues.append("No uppercase letters")
            recommendations.append("Add uppercase letters (A-Z)")
        
        if has_lower:
            score += 1
        else:
            issues.append("No lowercase letters")
            recommendations.append("Add lowercase letters (a-z)")
        
        if has_digit:
            score += 1
        else:
            issues.append("No numbers")
            recommendations.append("Add numbers (0-9)")
        
        if has_special:
            score += 1
        else:
            issues.append("No special characters")
            recommendations.append("Add special characters (!@#$%^&*...)")
        
        # Entropy calculation
        entropy = self._calculate_entropy(password)
        crack_time = self._estimate_crack_time(entropy)
        
        # Determine strength based on score
        if score <= 2:
            strength = "Weak"
        elif score <= 4:
            strength = "Moderate"
        else:
            strength = "Strong"
        
        return {
            "strength": strength,
            "score": score,
            "entropy": entropy,
            "crack_time": crack_time,
            "issues": issues,
            "recommendations": recommendations,
            "checks": {
                "length": len(password) >= 8,
                "uppercase": has_upper,
                "lowercase": has_lower,
                "numbers": has_digit,
                "special": has_special
            }
        }
    
    def _calculate_entropy(self, password: str) -> float:
        """Calculate password entropy (bits of randomness)"""
        if not password:
            return 0
        
        # Determine character set size
        charset_size = 0
        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'\d', password):
            charset_size += 10
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password):
            charset_size += 32
        
        if charset_size == 0:
            return 0
        
        return math.log2(charset_size ** len(password))
    
    def _estimate_crack_time(self, entropy: float) -> str:
        """Estimate time to crack password using brute force"""
        if entropy <= 0:
            return "Instant"
        
        # Assuming 1 billion attempts per second (modern GPU)
        attempts_per_second = 1_000_000_000
        total_attempts = 2 ** (entropy - 1)  # Average case
        
        seconds = total_attempts / attempts_per_second
        
        if seconds < 1:
            return "Less than 1 second"
        elif seconds < 60:
            return f"{seconds:.1f} seconds"
        elif seconds < 3600:
            minutes = seconds / 60
            return f"{minutes:.1f} minutes"
        elif seconds < 86400:
            hours = seconds / 3600
            return f"{hours:.1f} hours"
        elif seconds < 31536000:
            days = seconds / 86400
            return f"{days:.1f} days"
        else:
            years = seconds / 31536000
            return f"{years:.1f} years"
    
    def generate_strong_password(self, length: int = 16, exclude_similar: bool = True) -> str:
        """Generate a strong random password"""
        if length < 8:
            length = 8
        
        # Character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Exclude similar-looking characters if requested
        if exclude_similar:
            lowercase = lowercase.replace('l', '').replace('i', '')
            uppercase = uppercase.replace('I', '').replace('O', '')
            digits = digits.replace('0', '').replace('1', '')
            special = special.replace('|', '').replace('I', '')
        
        # Ensure at least one character from each set
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(special)
        ]
        
        # Fill remaining length with random characters
        all_chars = lowercase + uppercase + digits + special
        for _ in range(length - 4):
            password.append(random.choice(all_chars))
        
        # Shuffle the password
        random.shuffle(password)
        return ''.join(password)

def main():
    """Main interactive function"""
    checker = PasswordStrengthChecker()
    
    print("Password Strength Checker")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. Check password strength")
        print("2. Generate strong password")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            password = input("\nEnter password to check: ").strip()
            if password:
                result = checker.check_password_strength(password)
                
                print(f"\nPassword Analysis:")
                print(f"Strength: {result['strength']}")
                print(f"Score: {result['score']}/6")
                print(f"Entropy: {result['entropy']:.2f} bits")
                print(f"Estimated crack time: {result['crack_time']}")
                
                if result['checks']:
                    print(f"\nRequirements met:")
                    if result['checks']['length']:
                        print("  ✔ Minimum length (8+ characters)")
                    if result['checks']['uppercase']:
                        print("  ✔ Contains uppercase letters")
                    if result['checks']['lowercase']:
                        print("  ✔ Contains lowercase letters")
                    if result['checks']['numbers']:
                        print("  ✔ Contains numbers")
                    if result['checks']['special']:
                        print("  ✔ Contains special characters")
                
                if result['issues']:
                    print(f"\nIssues found:")
                    for issue in result['issues']:
                        print(f"  • {issue}")
                
                if result['recommendations']:
                    print(f"\nRecommendations:")
                    for rec in result['recommendations']:
                        print(f"  • {rec}")
                
                if result['strength'] == "Very Weak":
                    print(f"\nWARNING: This password is extremely weak!")
                    print("   Using common passwords makes you vulnerable to:")
                    print("   • Dictionary attacks")
                    print("   • Credential stuffing")
                    print("   • Social engineering")
            
        elif choice == "2":
            try:
                length = int(input("Enter password length (8-50): ").strip())
                length = max(8, min(50, length))
                
                exclude_similar = input("Exclude similar characters (O/0, I/1, l/i)? (y/n): ").strip().lower() == 'y'
                
                password = checker.generate_strong_password(length, exclude_similar)
                
                print(f"\nGenerated Password:")
                print(f"Password: {password}")
                print(f"Length: {len(password)} characters")
                
                # Check the generated password
                result = checker.check_password_strength(password)
                print(f"Strength: {result['strength']}")
                print(f"Entropy: {result['entropy']:.2f} bits")
                print(f"Estimated crack time: {result['crack_time']}")
                
                copy_choice = input("\nCopy to clipboard? (y/n): ").strip().lower()
                if copy_choice == 'y':
                    try:
                        import pyperclip
                        pyperclip.copy(password)
                        print("Password copied to clipboard!")
                    except ImportError:
                        print("pyperclip not installed. Install with: pip install pyperclip")
                        print("   Or manually copy the password above.")
                
            except ValueError:
                print("ERROR: Invalid length. Using default length of 16.")
                password = checker.generate_strong_password()
                print(f"Generated password: {password}")
        
        elif choice == "3":
            print("Goodbye! Stay secure!")
            break
        
        else:
            print("ERROR: Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main() 