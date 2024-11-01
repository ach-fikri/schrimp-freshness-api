from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hasher:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_ctx.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_ctx.hash(password)