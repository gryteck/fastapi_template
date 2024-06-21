import logging

from fastapi import APIRouter, status

router = APIRouter()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@router.get(
    "/",
    response_description="Проверка работоспособности сервиса",
    status_code=status.HTTP_200_OK,
    summary="Проверка доступности сервиса",
)
async def protected():
    return {"detail":"App is alive"}
