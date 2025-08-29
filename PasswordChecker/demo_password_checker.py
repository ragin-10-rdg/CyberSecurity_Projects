#!/usr/bin/env python3
"""
Password Checker Demo Script
Automated demonstration of password strength analysis with test cases.
"""

from password_checker import analyze_password

def run_demo():
    """Run automated demo of password checker functionality."""
    print("=" * 60)
    print("       PASSWORD STRENGTH DEMONSTRATION")
    print("=" * 60)
    
    # Test password categories
    test_cases = {
        "WEAK PASSWORDS": [
            "password",
            "123456", 
            "admin",
            "qwerty",
            "abc123"
        ],
        "MEDIUM PASSWORDS": [
            "Password1",
            "MyPass123",
            "Welcome2024",
            "Admin@123",
            "Hello123!"
        ],
        "STRONG PASSWORDS": [
            "MyD0g&Cat!Love2Play",
            "Tr@v3l!ng*Ar0und&W0rld", 
            "C0ff33&C00k!es#2024",
            "Cyb3r$3cur!ty&Educat!0n",
            "N3tw0rk$3cur!ty&Analys!s"
        ]
    }
    
    for category, passwords in test_cases.items():
        print(f"\n{category}")
        print("-" * 50)
        
        for password in passwords:
            result = analyze_password(password)
            strength_color = {
                'Weak': '🔴',
                'Medium': '🟡', 
                'Strong': '🟢'
            }.get(result['overall_strength'], '⚪')
            
            print(f"{strength_color} {password:<25} | {result['overall_strength']:<8} | Score: {result['score']}/{result['max_score']} | Entropy: {result['entropy']:.1f} bits")
    
    print(f"\n\nDETAILED ANALYSIS EXAMPLES")
    print("-" * 50)
    
    # Detailed analysis for specific examples
    examples = [
        ("password123", "Common weak password"),
        ("MyPass123!", "Medium strength example"),
        ("Tr@v3l!ng*Ar0und&W0rld", "Strong password example")
    ]
    
    for password, description in examples:
        print(f"\n{description.upper()}: '{password}'")
        result = analyze_password(password)
        
        print(f"Overall Strength: {result['overall_strength']} ({result['score']}/{result['max_score']})")
        print(f"Entropy: {result['entropy']} bits")
        print("Issues found:")
        for i, feedback in enumerate(result['feedback'][:3], 1):
            print(f"  {i}. {feedback}")

if __name__ == "__main__":
    run_demo()
