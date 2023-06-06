import bcrypt

password=b"secretpass555"

hashed= bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

if bcrypt.checkpw(password, hashed):
    print("it matches!")
else:
    print("Didn't match")