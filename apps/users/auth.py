from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils import timezone


def is_token_expired(token):
        time_elapsed = timezone.now() - token.created
        expiring_time_seconds = 1200
        if time_elapsed.total_seconds() > expiring_time_seconds:
            return True
        return False


class ExpiringTokenAuthentication(TokenAuthentication):
    """
    If token is expired then it will be removed
    and new one with different key will be created
    """

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related("user").get(key=key)
        except model.DoesNotExist:
            raise AuthenticationFailed("Invalid token.")

        if not token.user.is_active:
            raise AuthenticationFailed("User inactive or deleted.")

        is_expired = is_token_expired(token)
        if is_expired:
            raise AuthenticationFailed("This Token has expired")

        return (token.user, token)
