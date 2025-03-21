from app.db.mongo import mongo
from app.models.movies import MovieSerializer, MoviesSerializer


class MovieRepository:
    @staticmethod
    async def CreateMovie(movie_data: dict) -> str:
        new_movie = await mongo.db["movies"].insert_one(movie_data)
        return new_movie.inserted_id

    @staticmethod
    async def GetMoviesByFilters(filter_: dict) -> list:
        cursor = mongo.db["movies"].find(filter_).sort([("created_at", -1)]).limit(20)
        movies = await cursor.to_list()
        return MoviesSerializer(movies)

    @staticmethod
    async def GetMovie(movie_id: str) -> dict:
        movie =  await mongo.db["movies"].find_one({"_id": movie_id})
        return MovieSerializer(movie)

    @staticmethod
    async def UpdateMovie(movie_id: str, movie_data: dict) -> bool:
        await mongo.db["movies"].update_one({"_id": movie_id}, {"$set": movie_data})
        return True

    @staticmethod
    async def DeleteMovie(movie_id: str) -> bool:
        await mongo.db["movies"].delete_one({"_id": movie_id})
        return True
