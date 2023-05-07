from django.utils import timezone


def get_user_if_exist(phone_number):
    from user.models import User
    try:
        return User.objects.get(phone_number=phone_number)
    except Exception as e:
        print(e)
        return None


def is_otp_code_still_valid(otp_expire_at): 
    now = timezone.now()
    if now < otp_expire_at:
        return True
    else:
        return False


def update_user(data, user):
    user.first_name = data.validated_data.get("first_name", None)
    user.last_name = data.validated_data.get("last_name", None)
    user.email = data.validated_data.get("email", None)
    user.avatar = data.validated_data.get("avatar", None)
    user.save()


def set_user_otp(user, otp, otp_expire_at):
    user.otp = otp
    user.otp_expire_at = otp_expire_at
    user.save()


def activate_user_login(user):
    user.is_active = True
    user.save()
