import uuid
from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict, field_validator
from app.utils.helpers import GetCurrentUTCTime


class MovieCreateModel(BaseModel):
    title: str
    sub_title: str
    duration: int
    release_date: str
    genre: List[str]
    language: List[str]
    formats: List[str]
    certificate: str
    poster: str
    banner: str
    about: str

    @field_validator('genre', 'language', 'formats')
    def validate_list_not_empty(cls, value: List[str], info) -> List[str]:
        if not value:
            raise ValueError(f"{info.field_name.capitalize()} list cannot be empty")
        return value

    @field_validator('title', 'sub_title', 'release_date', 'certificate', 'poster', 'banner', 'about')
    def validate_string_not_empty(cls, value: str, info) -> str:
        if not value.strip():
            raise ValueError(f"{info.field_name.replace('_', ' ').capitalize()} cannot be empty")
        return value

    @field_validator('duration')
    def validate_duration(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("Duration must be greater than 0")
        return value


class MovieUpdateModel(BaseModel):
    title: Optional[str] = None
    sub_title: Optional[str] = None
    duration: Optional[int] = None
    release_date: Optional[str] = None
    genre: Optional[List[str]] = None
    language: Optional[List[str]] = None
    formats: Optional[List[str]] = None
    certificate: Optional[str] = None
    poster: Optional[str] = None
    banner: Optional[str] = None
    about: Optional[str] = None

    def model_dump(self, **kwargs):
        kwargs.setdefault("exclude_none", True)
        return super().model_dump(**kwargs)


class MovieModel(BaseModel):
    movie_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    title: str
    sub_title: str
    duration: int
    release_date: str
    genre: List[str]
    language: List[str]
    formats: List[str]
    certificate: str
    poster: str
    banner: str
    about: str
    created_at: str = Field(default_factory=lambda: GetCurrentUTCTime())

    model_config = ConfigDict(populate_by_name=True)

    @classmethod
    def from_create_model(cls, create_model: "MovieCreateModel") -> "MovieModel":
        return cls(
            title=create_model.title,
            sub_title=create_model.sub_title,
            duration=create_model.duration,
            release_date=create_model.release_date,
            genre=create_model.genre,
            language=create_model.language,
            formats=create_model.formats,
            certificate=create_model.certificate,
            poster=create_model.poster,
            banner=create_model.banner,
            about=create_model.about,
        )


def MovieSerializer(movie) -> dict:
    return {
        "movie_id": movie["_id"],
        "title": movie["title"],
        "sub_title": movie.get("sub_title", ""),
        "duration": movie.get("duration", ""),
        "release_date": movie.get("release_date", ""),
        "genre": movie["genre"],
        "language": movie.get("language", []),
        "formats": movie.get("formats", []),
        "certificate": movie.get("certificate", ""),
        "poster": movie.get("poster", ""),
        "banner": movie.get("banner", ""),
        "about": movie.get("about", ""),
    }


def MoviesSerializer(movies) -> list:
    return [MovieSerializer(movie) for movie in movies]