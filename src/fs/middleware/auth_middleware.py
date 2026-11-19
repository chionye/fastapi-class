import jwt
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

PUBLIC_PATHS = {
    "/",
    "/docs",
    "/openapi.json",
    "/auth/signup",
    "/auth/login"
}

class JWTAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path in PUBLIC_PATHS or request.method == "OPTIONS":
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer ")
            return JSONResponse(status_code=401, content={"detail": "Missing Token"})

        token = auth_header.split(" ", 1)[1]

        try:
            payload = decode_access_token(token)
        except jwt.ExpiredSignatureError:
           return JSONResponse(status_code=401, content={"detail": "Token Expired"})
        except jwt.InvalidTokenError:
            return JSONResponse(status_code=401, content={"detail": "Invalid Token"})

        request.state.user_id = int(payload["sub"])

        return await call_next(request)