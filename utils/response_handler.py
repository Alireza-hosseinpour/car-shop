from typing import Any

from pydantic import BaseModel
from rest_framework.response import Response


class MetaResponseModel(BaseModel):
    message: str = None
    errors: dict = {}


class ResponseModel(BaseModel):
    meta: MetaResponseModel = MetaResponseModel()
    body: Any


class ResponseHandler(object):

    def __init__(self):
        pass

    @staticmethod
    def build_http_response_body(meta, body: Any):
        return ResponseModel(meta=meta, body=body)

    def make_response(self, **kwargs):
        meta_response_model = MetaResponseModel(
            message=kwargs.get('message', None),
            errors=kwargs.get('errors', dict())
        )
        res = self.build_http_response_body(meta=meta_response_model, body=kwargs.get('body', dict())).dict()
        return Response(res, status=kwargs.get('status', 200))
