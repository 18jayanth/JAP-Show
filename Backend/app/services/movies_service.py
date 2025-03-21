from app.models.movies import MovieModel, MovieUpdateModel, MovieCreateModel
from app.repositories.movies_repo import MovieRepository


class MovieService:
    @staticmethod
    async def CreateMovie(movie: MovieCreateModel) -> str:
        movie_model = MovieModel.from_create_model(movie)
        movie_dict = movie_model.model_dump(by_alias=True)
        return await MovieRepository.CreateMovie(movie_dict)

    @staticmethod
    async def GetMovie(movie_id: str) -> dict:
        movie = await MovieRepository.GetMovie(movie_id)
        return movie

    @staticmethod
    async def UpdateMovie(movie_id: str, movie: MovieUpdateModel) -> bool:
        movie_dict = movie.model_dump(exclude_none=True)
        return await MovieRepository.UpdateMovie(movie_id, movie_dict)

    @staticmethod
    async def DeleteMovie(movie_id: str) -> bool:
        return await MovieRepository.DeleteMovie(movie_id)

    @staticmethod
    async def GetMoviesByFilters(genre=None, languages=None, formats=None, certificate=None):
        query = {}
        if genre: query["genre"] = {"$in": genre}
        if languages: query["language"] = {"$in": languages}
        if formats: query["formats"] = {"$in": formats}
        if certificate: query["certificate"] = certificate
        movies = await MovieRepository.GetMoviesByFilters(query)
        return movies