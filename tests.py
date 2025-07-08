from builder import build_error_proto, to_dict

err_proto = build_error_proto(
    code="USER_NOT_FOUND",
    message="User with ID abc123 not found.",
    status=404,
    details={"user_id": "abc123"},
    trace_id="req-001"
)
print(err_proto)
print(to_dict(err_proto))