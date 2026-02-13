from auth import hash_password, verify_password

password = "mypassword123"

hashed = hash_password(password)

print("Hashed:", hashed)

print("Verify correct:", verify_password("mypassword123", hashed))
print("Verify wrong:", verify_password("wrongpass", hashed))
