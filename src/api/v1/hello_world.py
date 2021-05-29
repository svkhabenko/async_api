from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi import HTTPException

from src.api.v1.api_models import HelloWorldResponse
from src.services.hello_world import get_hello_world_service, HelloWorldService

router = APIRouter()


@router.get(
    '/hello/',
    response_model=list[HelloWorldResponse],
    summary="Привет Мир!",
    description="Внутри ничего не происходит, просто возвращаем ответ",
    response_description="Описание ответа",
    tags=["Привет Мир"]
)
# @cache(expire=CACHE_EXPIRE_IN_SECONDS, coder=OrJsonCoder)
async def hello(
        hello_world_service: HelloWorldService = Depends(get_hello_world_service)
) -> list[HelloWorldResponse]:
    data = await hello_world_service.get_some_data()

    if not data:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='no data')

    return [
        HelloWorldResponse(uuid=data.uuid, hello=data.hello, world=data.world)
    ]
