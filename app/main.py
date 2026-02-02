from fastapi import FastAPI
from app.routes import users
from app.database import engine
from app.models.users import Base
#from app.models import User  # just to register models

app = FastAPI(
    title="Library System API",
    description="API for managing a library system including books and members.",
    version="1.0.0"
)

# create tables
Base.metadata.create_all(bind=engine)

# include routers
app.include_router(users.router)





app.include_router(users.router)