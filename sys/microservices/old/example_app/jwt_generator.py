# file: jwt_generator.py
from datetime import datetime, timedelta
from pathlib import Path
import jwt
from cryptography.hazmat.primitives import serialization


def generate_jwt():
    now = datetime.utcnow()
    payload = {
        "iss": "https://auth.coffeemesh.io/",
        "sub": "ec7bbccf-ca89-4af3-82ac-b41e4831a962",
        "aud": "http://127.0.0.1:8000/orders",
        "iat": now.timestamp(),
        "exp": (now + timedelta(hours=24)).timestamp(),
        "scope": "openid",
    }
    private_key_text = Path("private_key.pem").read_text()
    private_key = serialization.load_pem_private_key(
        private_key_text.encode(),
        password=None,
    )
    return jwt.encode(payload=payload, key=private_key, algorithm="RS256")


token = generate_jwt()
print("generated a token:\n", token)


# load the pu key
from cryptography.x509 import load_pem_x509_certificate
from pathlib import Path

public_key_text = Path("public_key.pem").read_text()
public_key = load_pem_x509_certificate(public_key_text.encode("utf-8")).public_key()
print("loaded public key:\n", public_key)

# use the key to validate a token:
import jwt


result = jwt.decode(
    token,
    key=public_key,
    algorithms=["RS256"],
    audience=["http://127.0.0.1:8000/orders"],
)
print("decoded the token:\n", result)
# {
#    "iss": "https://auth.coffeemesh.io/",
#    "sub": "ec7bbccf-ca89-4af3-82ac-b41e4831a962",
#    "aud": "http://127.0.0.1:8000/orders",
#    "iat": 1663259111.119025,
#    "exp": 1663345511.119025,
#    "scope": "openid",
# }
