#!/usr/bin/env python3
"""
Demo script for Password Strength Checker
Shows various password examples and their security analysis
"""

from password_checker import PasswordStrengthChecker

def demo_password_analysis():
    """Demonstrate password strength analysis with various examples"""
    checker = PasswordStrengthChecker()
    
    print("🔐 Password Strength Checker - Demo")
    print("=" * 50)
    
    # Example passwords to test
    test_passwords = [
        "123456",                    # Very weak - common password
        "password",                  # Very weak - common password
        "abc123",                    # Weak - too short, no special chars
        "MyPassword",               # Weak - no numbers or special chars
        "MyPassword123",            # Moderate - missing special chars
        "MyPassword123!",           # Strong - all requirements met
        "Kj9#mN2$pL8vX4@qR7w",     # Very strong - random and long
        "P@ssw0rd!",                # Strong - meets all criteria
        "qwertyuiop",               # Weak - keyboard pattern
        "admin123",                 # Weak - common combination
        "SecurePass2024!",          # Strong - good complexity
        "a",                        # Very weak - too short
        "",                         # Very weak - empty
    ]
    
    for i, password in enumerate(test_passwords, 1):
        print(f"\n{i:2d}. Testing: '{password}'")
        print("-" * 40)
        
        result = checker.check_password_strength(password)
        
        print(f"Strength: {result['strength']}")
        print(f"Score: {result['score']}/6")
        print(f"Entropy: {result['entropy']:.2f} bits")
        print(f"Crack Time: {result['crack_time']}")
        
        if result['checks']:
            print("Requirements:")
            checks = result['checks']
            print(f"  Length (8+): {'✅' if checks['length'] else '❌'}")
            print(f"  Uppercase: {'✅' if checks['uppercase'] else '❌'}")
            print(f"  Lowercase: {'✅' if checks['lowercase'] else '❌'}")
            print(f"  Numbers: {'✅' if checks['numbers'] else '❌'}")
            print(f"  Special: {'✅' if checks['special'] else '❌'}")
        
        if result['issues']:
            print("Issues:")
            for issue in result['issues']:
                print(f"  • {issue}")
        
        if result['recommendations']:
            print("Recommendations:")
            for rec in result['recommendations']:
                print(f"  • {rec}")
        
        if result['strength'] == 'Very Weak':
            print("⚠️  WARNING: This password is extremely weak!")

def demo_password_generation():
    """Demonstrate password generation capabilities"""
    checker = PasswordStrengthChecker()
    
    print("\n\n🔑 Password Generation Demo")
    print("=" * 50)
    
    # Generate different types of passwords
    lengths = [8, 12, 16, 20, 32]
    
    for length in lengths:
        print(f"\nGenerating {length}-character password:")
        password = checker.generate_strong_password(length, exclude_similar=True)
        print(f"Password: {password}")
        
        # Analyze the generated password
        result = checker.check_password_strength(password)
        print(f"Strength: {result['strength']} | Entropy: {result['entropy']:.2f} bits")
        print(f"Crack Time: {result['crack_time']}")
    
    # Test with similar characters included
    print(f"\nGenerating 16-character password (including similar chars):")
    password = checker.generate_strong_password(16, exclude_similar=False)
    print(f"Password: {password}")
    
    result = checker.check_password_strength(password)
    print(f"Strength: {result['strength']} | Entropy: {result['entropy']:.2f} bits")

def demo_entropy_calculation():
    """Demonstrate entropy calculation with examples"""
    checker = PasswordStrengthChecker()
    
    print("\n\n🧮 Entropy Calculation Demo")
    print("=" * 50)
    
    # Show how different character sets affect entropy
    examples = [
        ("1234567890", "Only digits"),
        ("abcdefghij", "Only lowercase"),
        ("ABCDEFGHIJ", "Only uppercase"),
        ("!@#$%^&*()", "Only special chars"),
        ("abc123", "Lowercase + digits"),
        ("ABC123", "Uppercase + digits"),
        ("abcABC", "Lowercase + uppercase"),
        ("abcABC123", "Lowercase + uppercase + digits"),
        ("abcABC123!", "All character types"),
        ("abcABC123!@#", "All types, longer"),
    ]
    
    print(f"{'Password':<20} {'Charset':<25} {'Entropy':<10} {'Crack Time':<15}")
    print("-" * 80)
    
    for password, description in examples:
        entropy = checker.calculate_entropy(password)
        crack_time = checker.estimate_crack_time(entropy)
        
        # Determine charset
        charset = []
        if any(c.islower() for c in password):
            charset.append("a-z")
        if any(c.isupper() for c in password):
            charset.append("A-Z")
        if any(c.isdigit() for c in password):
            charset.append("0-9")
        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            charset.append("!@#$%...")
        
        charset_str = "+".join(charset)
        
        print(f"{password:<20} {charset_str:<25} {entropy:<10.1f} {crack_time:<15}")

def main():
    """Run all demo functions"""
    try:
        demo_password_analysis()
        demo_password_generation()
        demo_entropy_calculation()
        
        print("\n\n🎉 Demo completed!")
        print("\nTo run the interactive version:")
        print("python password_checker.py")
        print("\nTo open the web interface:")
        print("Open web_interface.html in your browser")
        
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Error during demo: {e}")

if __name__ == "__main__":
    main() 