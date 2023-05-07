import math
import random
from config import settings
from django.utils.deconstruct import deconstructible
from uuid import uuid4
import os
from datetime import datetime, timedelta

from utils import user_handler
from utils.constants import OTP_TIMER

import hashlib

from utils.constants import PASSWORD_SALT


@deconstructible
class path_and_rename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)


def generate_otp():
    digits = "0123456789"
    otp = ""
    for i in range(6):
        otp += digits[math.floor(random.random() * 10)]
    return otp


def get_otp_expire_at():
    datetime_now = datetime.now()
    otp_expire_at = datetime_now + timedelta(minutes=OTP_TIMER)
    return otp_expire_at


def verify_otp(user, otp):
    if user.otp != otp:
        return False
    if not user_handler.is_otp_code_still_valid(user.otp_expire_at):
        return False
    return True


def get_message(message_key):
    if message_key is not None and message_key != "":
        if message_key in settings.MESSAGES_FILE:
            if settings.DEFAULT_LOCALE in settings.MESSAGES_FILE[message_key]:
                return settings.MESSAGES_FILE[message_key][settings.DEFAULT_LOCALE]
    return ""


def hash_password(password: str) -> str:
    hashed_password = hashlib.md5(f"{password}{PASSWORD_SALT}".encode('utf-8')).hexdigest()
    return hashed_password
