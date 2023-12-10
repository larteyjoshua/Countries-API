from fastapi import APIRouter
from typing import List
from app.services import countries
from app.models import schema


router = APIRouter(prefix="/v1")

@router.get('/countries', response_model=List[schema.ShowCountries], tags=['User'])
async def list_country():
    return countries.get_countries()