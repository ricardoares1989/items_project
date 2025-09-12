from fastapi import Request


def def get_container(request: Request):
    return request.state.container
