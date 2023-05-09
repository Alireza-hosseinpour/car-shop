import datetime
import jwt

from user.models import User


class Authenticate(object):

    @staticmethod
    def get_user_with_token(request):
        token = request.headers['Authorization']
        token = token.replace("Bearer ", "")
        try:
            payload = jwt.decode(token, key='secret', algorithms='HS256')
            user = User.objects.get(id=payload['id'])
            if not user:
                return None
            return user
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def create_access_token(user_id):
        payload = {
            "id": user_id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, key="secret", algorithm="HS256")
        return token
