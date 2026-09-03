from fastapi import APIRouter
from app.core.logging import get_logger

logger = get_logger()

router = APIRouter(
    prefix="/home",
)

@router.get("/")
def home():
    logger.info("Home endpoint accessed")
    logger.debug("Home endpoint accessed")
    logger.error("Home endpoint accessed")
    logger.warning("Home endpoint accessed")
    logger.critical("Home endpoint accessed")
    return {"message": "Welcome to the Modern Fraud Detection API!"}