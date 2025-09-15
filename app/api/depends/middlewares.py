from fastapi import Request


async def get_main_container_middleware(request: Request, call_next):
    request.state.container = request.app.state.container
    response = await call_next(request)
    return response
