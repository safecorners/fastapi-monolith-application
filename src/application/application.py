from fastapi import FastAPI

from application.containers import Container
from application.endpoints import router


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()

    app.container = container  # type: ignore[attr-defined]
    app.include_router(router)

    @app.get("/health-check")
    async def health_check() -> str:
        return "OK"

    return app
