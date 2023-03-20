from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()

    @app.get("/")
    def hello_world() -> str:
        return "Hello, World!"

    @app.get("/health-check")
    async def health_check() -> str:
        return "OK"

    return app
