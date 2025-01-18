from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()

# Inclusion des routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Système de gestion sécurisé avec HSM"}
