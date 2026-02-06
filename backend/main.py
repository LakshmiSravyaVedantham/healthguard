from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from config import FRONTEND_URL

Base.metadata.create_all(bind=engine)

app = FastAPI(title="HealthGuard", description="Health Awareness System for 50+ Indians")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        FRONTEND_URL,
        "http://localhost:3000", "http://127.0.0.1:3000",
        "http://localhost:5500", "http://127.0.0.1:5500",
        "https://lakshmisravya123.github.io",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routers
from routers import whatsapp, parents, medicines, checkins, dashboard, alerts, auth

app.include_router(whatsapp.router)
app.include_router(parents.router)
app.include_router(medicines.router)
app.include_router(checkins.router)
app.include_router(dashboard.router)
app.include_router(alerts.router)
app.include_router(auth.router)


@app.get("/health")
def health_check():
    return {"status": "healthy", "app": "HealthGuard"}


@app.on_event("startup")
def startup_event():
    from services.reminder_scheduler import start_scheduler
    start_scheduler()
