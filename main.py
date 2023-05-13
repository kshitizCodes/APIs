import mysql.connector
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
conn = mysql.connector.connect(
    host="localhost", port=3307, user="root", password="alpine", database="mobile_programming"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


class User(BaseModel):
    email: str
    password: str


@app.post("/signup")
async def signup(user: User):
    with conn.cursor() as cursor:
        try:
            cursor.execute(
                f"INSERT INTO login_info(email,password) VALUES('{user.email}','{user.password}')"
            )
            conn.commit()
            return {
                "error": False,
                "message": "Inserted into database successfully"
            }
        except Exception as e:
            return {
                "error": True,
                "message": f"Couldn't insert into database",
                "long_message": e
            }


@app.get("/login_info")
async def show():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM login_info")
        info = []
        for data in cursor.fetchall():
            info.append({
                "email": data[1],
                "password": data[2]
            })
    return info


@app.get("/login")
async def login():
    return
