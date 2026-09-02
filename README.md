# 🎬 CineTrack: Movie Watchlist API

A production-grade, lightweight CRUD API built with **FastAPI** and **Pydantic v2**, designed to manage and track movie watchlists with strict validation and clean exception handling.

## 🚀 Features
* **Full CRUD Operations**: Create, Read, Update, and Delete movie records seamlessly.
* **Pydantic v2 Validation**: Strict schema enforcement for titles, director names, release years, and watch statuses.
* **Case-Insensitive Routing**: Smart query handling for fetching and updating specific movies.
* **Robust Error Handling**: Custom `404 HTTPException` responses for missing resources.
* **Interactive Docs**: Built-in Swagger UI (`/docs`) for real-time API testing.

## 🛠️ Tech Stack
* **Python**
* **FastAPI**
* **Pydantic v2**
* **Uvicorn** (ASGI Server)
