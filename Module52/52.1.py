import hashlib

correct_passwd = 'qwerty123'

passwd = input("Enter password: ")

passwd_hash = hashlib.sha256(passwd.encode()).hexdigest()

correct_hash = hashlib.sha256(correct_passwd.encode()).hexdigest()

if passwd_hash == correct_hash:
    print("Access granted")
else:
    print("Access denied")