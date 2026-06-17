from passlib.context import CryptContext

# 1. Create a CryptContext instance specifying "argon2" as the algorithm
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# 2. Function to hash a plaintext password before saving to the database
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# 3. Function to verify a password during login
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

