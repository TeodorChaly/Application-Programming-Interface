import uvicorn
from fastapi import FastAPI
from databases import SessionLocal, Base, engine
from routers import user as user_router
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router.router, prefix="/user")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port = 80, reload=True, workers=2)