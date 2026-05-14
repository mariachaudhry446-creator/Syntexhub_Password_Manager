from cryptography.fernet import Fernet
import json
import os

KEY_FILE = "secret.key"
DATA_FILE = "vault.json"

def load_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as file:
            return file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)
        return key

key = load_or_create_key()
cipher = Fernet(key)

def load_vault():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    return json.loads(decrypted_data)

def save_vault(vault):
    json_text = json.dumps(vault)
    encrypted_text = cipher.encrypt(json_text.encode())
    with open(DATA_FILE, "wb") as file:
        file.write(encrypted_text)

def check_master_password():
    MASTER_PASSWORD = "admin123"
    password = input("🔒 Enter Master Password: ")
    if password == MASTER_PASSWORD:
        print("✅ Access granted!\n")
        return True
    else:
        print("❌ Wrong password!\n")
        return False

def main():
    print("=" * 40)
    print("   🔐 PASSWORD MANAGER 🔐")
    print("=" * 40)
    
    if not check_master_password():
        return
    
    vault = load_vault()
    
    while True:
        print("\n1️⃣ Add | 2️⃣ Retrieve | 3️⃣ Delete | 4️⃣ Search | 5️⃣ List All | 6️⃣ Exit")
        choice = input("Choose (1-6): ")
        
        if choice == "1":
            site = input("Website: ").lower()
            username = input("Username: ")
            password = input("Password: ")
            vault[site] = {"username": username, "password": password}
            save_vault(vault)
            print("✅ Added!")
            
        elif choice == "2":
            site = input("Website: ").lower()
            if site in vault:
                print(f"Username: {vault[site]['username']}")
                print(f"Password: {vault[site]['password']}")
            else:
                print("❌ Not found")
                
        elif choice == "3":
            site = input("Website: ").lower()
            if site in vault:
                del vault[site]
                save_vault(vault)
                print("✅ Deleted!")
            else:
                print("❌ Not found")
                
        elif choice == "4":
            term = input("Search: ").lower()
            found = [s for s in vault if term in s]
            print(f"Found: {', '.join(found) if found else 'Nothing found'}")
            
        elif choice == "5":
            if vault:
                print("Saved websites:", ", ".join(vault.keys()))
            else:
                print("Nothing saved yet")
                
        elif choice == "6":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()