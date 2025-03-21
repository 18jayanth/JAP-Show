from fastapi import APIRouter, Query
from app.models.movies import MovieUpdateModel, MovieCreateModel
from app.services.movies_service import MovieService
from typing import List, Optional

router = APIRouter()

@router.get("/{movie_id}")
async def GetOne(movie_id: str):
    movie = await MovieService.GetMovie(movie_id)
    return movie

@router.post("/", status_code=201)
async def Insert(movie: MovieCreateModel):
    movie_id = await MovieService.CreateMovie(movie)
    return {
        "message": "Movie Inserted Successfully",
        "movie_id": movie_id
    }

@router.put("/{movie_id}")
async def Update(movie_id: str, movie: MovieUpdateModel):
    await MovieService.UpdateMovie(movie_id, movie)
    return {
        "message": "Movie Updated Successfully",
        "movie_id": movie_id
    }

@router.delete("/{movie_id}")
async def Delete(movie_id: str):
    await MovieService.DeleteMovie(movie_id)
    return {
        "message": "Movie Deleted Successfully",
        "movie_id": movie_id
    }

@router.get("/")
async def GetMovies(
    genre: Optional[List[str]] = Query(None),
    languages: Optional[List[str]] = Query(None),
    formats: Optional[List[str]] = Query(None),
    certificate: Optional[str] = Query(None)
):
    movies = await MovieService.GetMoviesByFilters(
        genre=genre,
        languages=languages,
        formats=formats,
        certificate=certificate
    )
    return movies