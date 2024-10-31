from datetime import timezone, datetime
import jwt


class AuthenticateService:

    def __init__(self, secret):
        self.secret = secret

    def issue_token(self, profile, expire_time=7200):
        now = int(datetime.now(tz=timezone.utc).timestamp())
        payload = {
            "iat": now,
            "exp": now + expire_time,
        }
        payload.update(profile)
        token = jwt.encode(payload, self.secret, algorithm="HS256")
        return token

    def authenticate_token(self, payload):
        if not payload:
            raise ValueError("Token is empty")
        try:
            payload = jwt.decode(payload, self.secret, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

        return payload
