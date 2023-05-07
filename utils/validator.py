import os.path
import re

from PIL import Image
from rest_framework.exceptions import ValidationError

from .constants import IMAGE_MIMETYPES, IMAGE_EXTENSIONS, MAX_AVATAR_WIDTH, MAX_AVATAR_HEIGHT, MAX_IMAGE_HEIGHT, \
    MAX_IMAGE_WIDTH, MINIMUM_USERNAME_LENGTH, MINIMUM_PASSWORD_LENGTH


def check_phone_number(phone_number):
    # ^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$
    if not bool(re.match("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", phone_number)):
        raise ValidationError({'phone_number_problem': "Some message"})


def check_avatar(avatar):
    width, height = get_image_dimensions(avatar)
    name, extension = os.path.splitext(avatar.name)
    if extension not in IMAGE_EXTENSIONS:
        raise ValidationError({'extension': 'Extension not ok'})
    if avatar.content_type not in IMAGE_MIMETYPES:
        raise ValidationError({'extension': 'Mimetype not ok'})
    if width > MAX_AVATAR_WIDTH or height > MAX_AVATAR_HEIGHT:
        raise ValidationError({'size': 'invalid size of avatar'})


def check_car_image(car_image):
    width, height = get_image_dimensions(car_image)
    name, extension = os.path.splitext(car_image.name)
    if extension not in IMAGE_EXTENSIONS:
        raise ValidationError({'extension': 'Extension not ok'})
    if car_image.content_type not in IMAGE_MIMETYPES:
        raise ValidationError({'Mimetype': 'Mimetype not ok'})
    if width > MAX_IMAGE_WIDTH or height > MAX_IMAGE_HEIGHT:
        raise ValidationError({'image_problem': 'invalid size of image'})


def get_image_dimensions(avatar):
    avatar = Image.open(avatar)
    width, height = avatar.size
    return width, height


def username_is_valid(username):
    if username is None or len(username) < MINIMUM_USERNAME_LENGTH:
        return False
    return True


def password_is_valid(password):
    if password is None or len(password) < MINIMUM_PASSWORD_LENGTH:
        return False
    return True
