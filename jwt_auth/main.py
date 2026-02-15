import logging
from datetime import datetime, timedelta

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext

# ================= Logging Config =================
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ================= App Init =================
app = FastAPI()

# ================= CONFIG =================
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30

# Use Argon2 instead of bcrypt
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ================= In-Memory User Store =================
fake_users_db = {}

# ================= HELPERS =================
def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)


def create_token(username: str):
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)

    payload = {
        "sub": username,
        "exp": expire
    }

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username not in fake_users_db:
            raise HTTPException(401, "Invalid token")

        return username

    except:
        raise HTTPException(401, "Invalid token")


# ================= ROUTES =================
@app.post("/register")
def register(username: str, password: str):

    if username in fake_users_db:
        raise HTTPException(400, "User already exists")

    if len(password) < 6:
        raise HTTPException(400, "Password too short")

    fake_users_db[username] = hash_password(password)

    logger.info(f"User registered: {username}")

    return {"message": "User registered successfully"}


@app.post("/login")
def login(username: str, password: str):

    stored_hash = fake_users_db.get(username)

    if not stored_hash or not verify_password(password, stored_hash):
        raise HTTPException(401, "Invalid credentials")

    token = create_token(username)

    logger.info(f"User logged in: {username}")

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@app.get("/protected")
def protected(user: str = Depends(get_current_user)):

    logger.info(f"Protected route accessed by {user}")

    return {
        "message": f"Hello {user}, you accessed protected data."
    }
