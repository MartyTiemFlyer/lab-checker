"""
routes.py
Здесь описываются API-эндпоинты сервиса.
"""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class LabRequest(BaseModel):
    bash_code: str
    systemd_config: str


@router.post("/check")
async def check_lab(data: LabRequest):
    return {
        "status": "received",
        "bash_length": len(data.bash_code),
        "systemd_length": len(data.systemd_config),
    }
