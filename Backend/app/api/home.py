from fastapi import APIRouter
from app.services.home_service import HomePageService

router = APIRouter()

@router.get("/recommended-movies")
async def GetRecommendedMovies():
    movies = await HomePageService.GetRecommendedMovies()
    return movies

@router.get("/banners")
async def GetBanners():
    banners = await HomePageService.GetBanners()
    return banners