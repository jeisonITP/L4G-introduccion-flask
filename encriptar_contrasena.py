import hashlib

message = hashlib.sha256()
message.update(b"Itp2022")

print(message.hexdigest())

# Salt
salt = bcrypt.gensalt()
password = bcrypt.hashpw('12345678', salt)

brypt.compare(password_guardada, password) #True o False