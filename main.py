from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
jaga = FastAPI()

Movies = [
    {
        "title" : "Inception",
        "director" : "Christopher Nolan",
        "release_year" : 2010,
        "rating" : 8.8,
        "watched" : True
    },
    {
        "title" : "The Dark Knight",
        "director" : "Christopher Nolan",
        "release_year" : 2008,
        "rating" : 8.7,
        "watched" : False
    },
    {
        "title" : "Interstellar",
        "director" : "Christopher Nolan",
        "release_year" : 2014,
        "rating" : 9.0,
        "watched" : True
    },
    {
        "title" : "Baahubali",
        "director" : "SS Rajamouli",
        "release_year" : 2015,
        "rating" : 8.9,
        "watched" : False
    },
     {
        "title" : "Vikram",
        "director" : "Lokesh Kanagaraj",
        "release_year" : 2022,
        "rating" : 9.2,
        "watched" : True
    }
]

# Creating a pydantic model for movie

class MovieSchema(BaseModel):
    title : str = Field(min_length = 1, max_length = 70)
    director : str
    release_year : int = Field(ge = 1900, le = 2030)
    watched : bool = False


# Creating a GET endpoint to retrieve entire movieslist

@jaga.get("/movies")
async def show_watchlist():
    return Movies


# Creating a GET endpoint to retrieve only desired movie

@jaga.get("/movies/{title}")
async def desire_movie(title : str):
    for movie in Movies:
        if movie["title"].lower() == title.lower():
            return movie
    raise HTTPException(status_code = 404, detail = "Movie not found")


# Creating a POST endpoint to add a new movie

@jaga.post("/create_movie",status_code = 201)
async def add_movie(movie : BaseModel):
    new_movie = movie.dump_model()
    Movies.append(new_movie)
    return new_movie


# Creating a PUT endpoint to update the watchlist

@jaga.put("/update_movie/{title}")
async def movie_update(title : str, movie : BaseModel):
    for movies in Movies:
        if movies["title"].lower() == title.lower():
            updated_movie = movie.model_dump()
            movies["watched"] = updated_movie["watched"]
            return {
                "message" : "Movie updated successfully",
                "movie" : movies,
            }
    raise HTTPException(status_code = 404, detail = "Movie not found")


# Creating a DELETE endpoint to remove a movie

jaga.delete("/remove_movie/{title}")
async def movie_removed(title : str):
    for movie in Movies:
        if movie["title"].lower() == title.lower():
            Movies.remove(movie)
            return {"message" : "Movie removed successfully"}
    raise HTTPException(status_code = 404, detail = "Movie not found")