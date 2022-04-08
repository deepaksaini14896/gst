import bcrypt
import jwt
import datetime

# Secret Key
secret = "123"
# Algorithm
algorithm="HS256"

def create_password(password):
	hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
	return hashed

def check_password(password, hashed):
	hashed = hashed.encode('utf-8')
	password = password.encode('utf-8')

	if bcrypt.checkpw(password, hashed):
		return True
	
	return False

def create_token(pan_number):
	token = jwt.encode( {
							'pan_number': pan_number,
							'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=(60 * 3))
						},
						secret, algorithm)
	return token