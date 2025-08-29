# Password Strength Checker

A comprehensive tool for analyzing password security and providing improvement recommendations.

## Purpose

This tool evaluates password strength using multiple security criteria and provides detailed feedback to help users create more secure passwords. It's designed for educational purposes and security awareness.

## Features

- **Comprehensive Analysis**: Checks length, character variety, common patterns, and dictionary words
- **Strength Rating**: Provides Weak/Medium/Strong ratings with detailed scoring
- **Entropy Calculation**: Measures password randomness in bits
- **Detailed Feedback**: Specific recommendations for improvement
- **Batch Processing**: Analyze multiple passwords at once
- **Password Suggestions**: Generate examples of strong passwords

## How to Run

1. Navigate to the PasswordChecker directory
2. Run the script:
   ```bash
   python password_checker.py
   ```

## Dependencies

No external libraries required - uses only Python standard library.

## Analysis Criteria

### Length Check
- **Strong**: 12+ characters
- **Medium**: 8-11 characters  
- **Weak**: Less than 8 characters

### Character Variety
- Uppercase letters (A-Z)
- Lowercase letters (a-z)
- Numbers (0-9)
- Special characters (!@#$%^&*)

### Pattern Detection
- Sequential numbers (123, 456)
- Sequential letters (abc, xyz)
- Keyboard patterns (qwerty, asdf)
- Repeated characters (aaa, 111)

### Dictionary Words
- Common passwords (password, admin)
- Dictionary words in various languages
- Personal information patterns

## Example Usage

### Test Cases

**Weak Password**: `password123`
- Issues: Contains dictionary word, predictable pattern
- Rating: Weak (4/12)

**Medium Password**: `MyPass123!`
- Issues: Contains dictionary word, but good variety
- Rating: Medium (8/12)

**Strong Password**: `Tr@v3l!ng*Ar0und&W0rld`
- Excellent length, variety, no common patterns
- Rating: Strong (12/12)

## Security Tips

1. **Use 12+ characters** for better security
2. **Mix character types** (upper, lower, numbers, symbols)
3. **Avoid dictionary words** and personal information
4. **Use passphrases** with special characters
5. **Don't reuse passwords** across different accounts
6. **Consider password managers** for unique passwords

## Educational Note

This tool is for educational purposes to understand password security principles. Always use unique, strong passwords for real accounts and consider using a reputable password manager.
