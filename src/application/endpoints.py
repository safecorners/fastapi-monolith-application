from typing import List, Union

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Response, status

from application.containers import Container
from application.models import User
from application.repositories import NotFoundError
from application.services import UserService

router = APIRouter()


@router.get(
    "/users",
    response_model=None,
)
@inject
def get_list(
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> List[User]:
    return user_service.get_users()


@router.get(
    "/users/{user_id}",
    response_model=None,
)
@inject
def get_by_id(
    user_id: int,
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> Union[User, Response]:
    try:
        return user_service.get_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post(
    "/users",
    status_code=status.HTTP_201_CREATED,
    response_model=None,
)
@inject
def add(
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> User:
    return user_service.create_user()


@router.delete(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
)
@inject
def remove(
    user_id: int,
    user_service: UserService = Depends(Provide[Container.user_service]),
) -> Response:
    try:
        user_service.delete_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/status")
def get_status() -> dict[str, str]:
    return {"status": "OK"}
