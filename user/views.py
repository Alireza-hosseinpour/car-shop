from rest_framework.views import APIView
from utils.authenticate import Authenticate
from utils.custom_response import invalid_code_response, user_created_response, invalid_response, \
    user_not_found_response, successful_response
from utils.modules import generate_otp, get_otp_expire_at, verify_otp
from utils.user_handler import get_user_if_exist, is_otp_code_still_valid, update_user, set_user_otp, \
    activate_user_login
from .models import User
from .serializers import GetOtpDeserializer, VerifyDeserializer, UpdateProfileDeserializer


class GetOtp(APIView):

    def post(self, request, *args, **kwargs):
        data = GetOtpDeserializer(data=request.data)
        if not data.is_valid():
            return invalid_response(data.errors)
        phone_number = data.validated_data.get("phone_number", None)
        otp = generate_otp()
        otp_expire_at = get_otp_expire_at()

        result = {
            "otp": otp,
            "phone_number": phone_number
        }
        user = get_user_if_exist(phone_number=phone_number)
        if user:
            if not is_otp_code_still_valid(user.otp_expire_at):
                set_user_otp(user, otp, otp_expire_at)

            else:
                result['otp'] = user.otp
        else:
            User.objects.create(
                phone_number=phone_number,
                otp=otp,
                otp_expire_at=otp_expire_at
            )

        return user_created_response(result)


class VerifyOtp(APIView):

    def post(self, request, *args, **kwargs):
        data = VerifyDeserializer(data=request.data)
        if not data.is_valid():
            return invalid_response(data.errors)

        user = get_user_if_exist(phone_number=data.validated_data.get("phone_number"))
        if not user:
            return user_not_found_response()

        otp = data.validated_data.get("otp")
        if not verify_otp(user, otp):
            return invalid_code_response()
        token = Authenticate.create_access_token(user_id=user.id)
        activate_user_login(user)
        return successful_response(token)


class UpdateProfile(APIView):
    def post(self, request, *args, **kwargs):
        user = Authenticate.get_user_with_token(request)
        if not user:
            return user_not_found_response()
        data = UpdateProfileDeserializer(data=request.data)
        if not data.is_valid():
            return invalid_response(data.errors)
        update_user(data, user)
        return successful_response(user)
