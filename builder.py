from protobufs.error_pb2 import ErrorResponse
from google.protobuf.json_format import MessageToDict

def build_error_proto(code: str, message: str, status: int = 400, details: dict = None, trace_id: str = None) -> ErrorResponse:
    error = ErrorResponse()
    error.code = code
    error.message = message
    error.status = status

    if details:
        error.details.update(details)

    if trace_id:
        error.trace_id = trace_id

    return error

def to_dict(err_proto, preserving_proto_field_name=True):
    return MessageToDict(err_proto, preserving_proto_field_name=preserving_proto_field_name)
