from rest_framework import status
from .modules import get_message
from utils.response_handler import ResponseHandler


def invalid_response(error):
    response = ResponseHandler()
    return response.make_response(
        message=get_message('DATA_NOT_VALID'),
        errors=error,
        status=status.HTTP_400_BAD_REQUEST)


def user_not_found_response():
    response = ResponseHandler()
    return response.make_response(
        message=get_message('USER_NOT_FOUND'),
        status=status.HTTP_400_BAD_REQUEST)


def successful_response(data):
    response = ResponseHandler()
    return response.make_response(
        message=get_message('SUCCESSFUL'),
        body={f'{data}'},
        status=status.HTTP_200_OK)


def car_created_response():
    response = ResponseHandler()
    return response.make_response(
        message=get_message('CAR_ADDED_SUCCESSFULLY'),
        status=status.HTTP_201_CREATED)


def user_created_response(data):
    response = ResponseHandler()
    return response.make_response(
        message=get_message('SUCCESSFUL'),
        body={"result": data},
        status=status.HTTP_201_CREATED
    )


def invalid_code_response():
    response = ResponseHandler()
    return response.make_response(
        message=get_message('INVALID_CODE'),
        status=status.HTTP_400_BAD_REQUEST)


def car_not_found_response():
    response = ResponseHandler()
    return response.make_response(
        message=get_message('CAR_NOT_FOUND'),
        status=status.HTTP_400_BAD_REQUEST)
