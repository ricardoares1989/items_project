from fastapi import Request


def get_container(request: Request):
    return request.state.container
