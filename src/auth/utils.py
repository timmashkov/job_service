import jwt
import bcrypt

from settings.config import config


async def encode_jwt(payload: dict,
                     private_key: str = config.auth.private_key.read_text(),
                     algorythm: str = config.auth.algorythm):
    """
    Кодирование токена
    :param payload:
    :param private_key:
    :param algorythm:
    :return:
    """
    encoded = jwt.encode(payload, private_key, algorythm)
    return encoded


async def decode_jwt(jwt_token: str | bytes,
                     public_key: str = config.auth.public_key.read_text(),
                     algorythm: str = config.auth.algorythm):
    """
    Декодирование токена
    :param jwt_token:
    :param public_key:
    :param algorythm:
    :return:
    """
    decoded = jwt.decode(jwt_token, public_key, algorythm)
    return decoded


async def hash_password(password: str) -> bytes:
    """
    Хэширование пароля
    :param password:
    :return:
    """
    salt = bcrypt.gensalt()
    pwd_bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


async def validate_password(password: str,
                            hashed_password: bytes) -> bool:
    """
    Валидация пароля
    :param password:
    :param hashed_password:
    :return:
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
