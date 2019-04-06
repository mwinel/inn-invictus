from .serializer import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    """ JWT_RESPONSE_PAYLOAD_HANDLER """
    return {
        "token": token,
        "user": UserSerializer(user, context={"request": request}).data,
    }
