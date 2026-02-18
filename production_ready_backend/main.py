from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from datetime import datetime, timedelta

# ================= CONFIG =================
DATABASE_URL = "sqlite:///./app.db"
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

pwd_context = CryptContext(schemes=["argon2"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

app = FastAPI()

# ================= DATABASE MODELS =================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    completed = Column(Boolean, default=False)
    owner = Column(String)


Base.metadata.create_all(bind=engine)

# ================= HELPERS =================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)


def create_token(username):
    expire = datetime.utcnow() + timedelta(minutes=30)
    return jwt.encode({"sub": username, "exp": expire},
                      SECRET_KEY,
                      algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")

    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(401, "Invalid user")

    return username

# ================= AUTH ROUTES =================
@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(400, "User exists")

    user = User(username=username,
                password=hash_password(password))

    db.add(user)
    db.commit()

    return {"message": "User registered"}


@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException(401, "Invalid credentials")

    token = create_token(username)
    return {"access_token": token}

# ================= TASK ROUTES =================
@app.post("/tasks")
def create_task(title: str,
                user: str = Depends(get_current_user),
                db: Session = Depends(get_db)):
    task = Task(title=title, owner=user)
    db.add(task)
    db.commit()

    return {"message": "Task created"}


@app.get("/tasks")
def list_tasks(user: str = Depends(get_current_user),
               db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.owner == user).all()
    return tasks
