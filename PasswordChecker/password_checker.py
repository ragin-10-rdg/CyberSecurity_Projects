#!/usr/bin/env python3
"""
Password Strength Checker Tool
Analyze password strength and provide feedback for improvement.
"""

import re
import string
from collections import Counter

def check_length(password):
    """Check if password meets length requirements."""
    length = len(password)
    if length >= 12:
        return "Strong", "Password length is excellent (12+ characters)"
    elif length >= 8:
        return "Medium", "Password length is good (8+ characters)"
    else:
        return "Weak", f"Password is too short ({length} characters). Use at least 8 characters"

def check_character_variety(password):
    """Check for variety of character types in password."""
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    variety_count = sum([has_upper, has_lower, has_digit, has_special])
    
    feedback = []
    if not has_upper:
        feedback.append("Add uppercase letters (A-Z)")
    if not has_lower:
        feedback.append("Add lowercase letters (a-z)")
    if not has_digit:
        feedback.append("Add numbers (0-9)")
    if not has_special:
        feedback.append("Add special characters (!@#$%^&*)")
    
    if variety_count >= 4:
        return "Strong", "Excellent character variety"
    elif variety_count >= 3:
        return "Medium", "Good character variety. Consider: " + ", ".join(feedback)
    else:
        return "Weak", "Poor character variety. Add: " + ", ".join(feedback)

def check_common_patterns(password):
    """Check for common weak patterns."""
    weak_patterns = [
        (r'123', "Contains sequential numbers (123)"),
        (r'abc', "Contains sequential letters (abc)"),
        (r'qwerty', "Contains keyboard pattern (qwerty)"),
        (r'password', "Contains the word 'password'"),
        (r'admin', "Contains the word 'admin'"),
        (r'login', "Contains the word 'login'"),
        (r'(.)\1{2,}', "Contains repeated characters (aaa, 111)"),
    ]
    
    issues = []
    for pattern, message in weak_patterns:
        if re.search(pattern, password.lower()):
            issues.append(message)
    
    if not issues:
        return "Strong", "No common weak patterns detected"
    else:
        return "Weak", "Avoid these patterns: " + "; ".join(issues)

def check_dictionary_words(password):
    """Check for common dictionary words."""
    common_words = [
        'password', 'admin', 'login', 'user', 'root', 'guest', 'test',
        'welcome', 'hello', 'world', 'computer', 'internet', 'security',
        'system', 'master', 'super', 'secret', 'private', 'public'
    ]
    
    password_lower = password.lower()
    found_words = [word for word in common_words if word in password_lower]
    
    if not found_words:
        return "Strong", "No common dictionary words found"
    else:
        return "Weak", f"Contains common words: {', '.join(found_words)}"

def calculate_entropy(password):
    """Calculate password entropy (bits)."""
    charset_size = 0
    
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'\d', password):
        charset_size += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset_size += 32
    
    if charset_size == 0:
        return 0
    
    import math
    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)

def analyze_password(password):
    """Comprehensive password analysis."""
    if not password:
        return {
            'overall_strength': 'Invalid',
            'score': 0,
            'feedback': ['Password cannot be empty'],
            'entropy': 0
        }
    
    # Run all checks
    length_strength, length_feedback = check_length(password)
    variety_strength, variety_feedback = check_character_variety(password)
    pattern_strength, pattern_feedback = check_common_patterns(password)
    dictionary_strength, dictionary_feedback = check_dictionary_words(password)
    
    # Calculate entropy
    entropy = calculate_entropy(password)
    
    # Scoring system
    strength_scores = {'Strong': 3, 'Medium': 2, 'Weak': 1}
    total_score = (
        strength_scores[length_strength] +
        strength_scores[variety_strength] +
        strength_scores[pattern_strength] +
        strength_scores[dictionary_strength]
    )
    
    # Determine overall strength
    if total_score >= 11:
        overall_strength = 'Strong'
    elif total_score >= 8:
        overall_strength = 'Medium'
    else:
        overall_strength = 'Weak'
    
    # Compile feedback
    feedback = []
    if length_strength != 'Strong':
        feedback.append(length_feedback)
    if variety_strength != 'Strong':
        feedback.append(variety_feedback)
    if pattern_strength != 'Strong':
        feedback.append(pattern_feedback)
    if dictionary_strength != 'Strong':
        feedback.append(dictionary_feedback)
    
    if not feedback:
        feedback.append("Excellent password! All security criteria met.")
    
    return {
        'overall_strength': overall_strength,
        'score': total_score,
        'max_score': 12,
        'feedback': feedback,
        'entropy': entropy,
        'details': {
            'length': (length_strength, length_feedback),
            'variety': (variety_strength, variety_feedback),
            'patterns': (pattern_strength, pattern_feedback),
            'dictionary': (dictionary_strength, dictionary_feedback)
        }
    }

def generate_password_suggestions():
    """Generate example strong passwords."""
    suggestions = [
        "MyD0g&Cat!Love2Play",
        "C0ff33&C00k!es#2024",
        "Tr@v3l!ng*Ar0und&W0rld",
        "B00ks&M0v!es#MyL!fe",
        "Sp0rts&Gam3s*Fun!2024"
    ]
    return suggestions

def main():
    """Main function to run the password checker tool."""
    print("=" * 60)
    print("         PASSWORD STRENGTH CHECKER")
    print("=" * 60)
    
    while True:
        print("\nChoose an option:")
        print("1. Check password strength")
        print("2. Get password suggestions")
        print("3. Batch check multiple passwords")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            password = input("Enter password to check: ")
            result = analyze_password(password)
            
            print(f"\n{'='*50}")
            print(f"PASSWORD ANALYSIS RESULTS")
            print(f"{'='*50}")
            print(f"Overall Strength: {result['overall_strength']}")
            print(f"Score: {result['score']}/{result['max_score']}")
            print(f"Entropy: {result['entropy']} bits")
            
            print(f"\nDetailed Analysis:")
            for category, (strength, feedback) in result['details'].items():
                print(f"  {category.title()}: {strength} - {feedback}")
            
            print(f"\nRecommendations:")
            for i, feedback in enumerate(result['feedback'], 1):
                print(f"  {i}. {feedback}")
        
        elif choice == '2':
            suggestions = generate_password_suggestions()
            print(f"\nStrong Password Suggestions:")
            print("-" * 30)
            for i, suggestion in enumerate(suggestions, 1):
                print(f"{i}. {suggestion}")
            
            print(f"\nTips for creating strong passwords:")
            print("• Use 12+ characters")
            print("• Mix uppercase, lowercase, numbers, and symbols")
            print("• Avoid dictionary words and personal information")
            print("• Use passphrases with special characters")
            print("• Don't reuse passwords across accounts")
        
        elif choice == '3':
            print("Enter passwords to check (one per line, empty line to finish):")
            passwords = []
            while True:
                pwd = input()
                if not pwd:
                    break
                passwords.append(pwd)
            
            if passwords:
                print(f"\n{'='*60}")
                print(f"BATCH PASSWORD ANALYSIS")
                print(f"{'='*60}")
                
                for i, password in enumerate(passwords, 1):
                    result = analyze_password(password)
                    print(f"\nPassword {i}: {'*' * len(password)}")
                    print(f"Strength: {result['overall_strength']} ({result['score']}/{result['max_score']})")
                    print(f"Entropy: {result['entropy']} bits")
                    if result['feedback']:
                        print(f"Issues: {'; '.join(result['feedback'][:2])}")
        
        elif choice == '4':
            print("Thank you for using Password Strength Checker!")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
