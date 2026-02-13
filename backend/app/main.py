from fastapi import FastAPI
from app.routes import auth
from app.routes import users





app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "IDP Platform Running 🚀"}
