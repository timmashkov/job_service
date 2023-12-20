import jwt

from settings.config import config


async def encode_jwt(payload: dict,
                     private_key: str = config.auth.private_key.read_text(),
                     algorythm: str = config.auth.algorythm):
    encoded = jwt.encode(payload, private_key, algorythm)
    return encoded


async def decode_jwt(jwt_token: str | bytes,
                     public_key: str = config.auth.public_key.read_text(),
                     algorythm: str = config.auth.algorythm):
    decoded = jwt.decode(jwt_token, public_key, algorythm)
    return decoded

