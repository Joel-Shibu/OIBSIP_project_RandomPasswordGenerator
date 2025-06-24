import secrets
import string
from typing import List

def generate_password(
    length: int = 12,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True
) -> str:
    """
    Generate a secure random password with the specified criteria.
    
    Args:
        length: Length of the password (default: 12)
        use_uppercase: Include uppercase letters (A-Z)
        use_lowercase: Include lowercase letters (a-z)
        use_digits: Include digits (0-9)
        use_symbols: Include symbols (!@#$%^&*()_+-=[]{}|;:,.<>?)
        
    Returns:
        str: Generated password
        
    Raises:
        ValueError: If no character set is selected or length is invalid
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
        
    if length > 64:
        raise ValueError("Password length cannot exceed 64 characters")
    
    # Define character sets
    char_sets = []
    if use_uppercase:
        char_sets.append(string.ascii_uppercase)
    if use_lowercase:
        char_sets.append(string.ascii_lowercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_symbols:
        char_sets.append('!@#$%^&*()_+-=[]{}|;:,.<>?')
    
    if not char_sets:
        raise ValueError("At least one character set must be selected")
    
    # Ensure at least one character from each selected set
    password = []
    for char_set in char_sets:
        password.append(secrets.choice(char_set))
    
    # Fill the rest of the password
    all_chars = ''.join(char_sets)
    password.extend(secrets.choice(all_chars) for _ in range(length - len(password)))
    
    # Shuffle the password to mix the required characters
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def get_password_strength(password: str) -> str:
    """
    Evaluate the strength of a password.
    
    Args:
        password: Password to evaluate
        
    Returns:
        str: Strength rating ('Weak', 'Medium', 'Strong', 'Very Strong')
    """
    if not password:
        return 'Very Weak'
        
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    
    # Calculate strength score
    score = 0
    if length >= 8: score += 1
    if length >= 12: score += 1
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_symbol: score += 1
    
    # Determine strength level
    if length < 4 or score < 2:
        return 'Very Weak'
    elif score < 4:
        return 'Weak'
    elif score < 5:
        return 'Medium'
    elif score < 7:
        return 'Strong'
    return 'Very Strong'
