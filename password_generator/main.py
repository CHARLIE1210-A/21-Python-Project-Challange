import string; import secrets;

# ================= CONFIGURATION ================= 
MIN_LENGTH = 4
MAX_LENGTH = 64


# ================= CORE LOGIC =================
def generate_password(
  length: int = 12,
  use_uppercase: bool = True,
  use_lowercase: bool = True,
  use_digits: bool = True,
  use_symbols: bool = True
):
    if length < MIN_LENGTH or length > MAX_LENGTH:
        raise ValueError(f"Password length must be between {MIN_LENGTH} and {MAX_LENGTH}")
    
    characters = ""
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
        
    if not characters:
        raise ValueError("At least one character type must be selected")
    
    passwords = ''.join(secrets.choice(characters) for _ in range(length))
    
    return passwords

def password_strength(password):
    score = 0
    length = len(password)
    
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    
    if length >= 12:
        score += 1
        
    levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong",
        5: "Excellent"
    }
    
    return levels.get(score, "Very Weak")

# ================= USER INPUT =================
def get_user_preferences():
    length = int(input("Password length: "))
    
    use_uppercase = input("Include upercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits letters? (y/n): ").lower() == 'y'
    use_symbol = input("Include symbols letters? (y/n): ").lower() == 'y'
    
    return length, use_uppercase, use_lower, use_digits, use_symbol

# ================= MAIN APP =================
def main():
    print("=== Password Generator ===")
    
    try:
        count = int(input("How many passwords to generate? "))
        prefs = get_user_preferences()
        
        for i in range(count):
            password = generate_password(*prefs)
            strength = password_strength(password)
            
            print(f"Password {i+1}: {password} | Strength: {strength}")
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()