from fastapi import FastAPI, HTTPException
from .models import CourseCreate, CourseOut
from .db import database, courses
import asyncio

app = FastAPI(title='CONOCER Training API')

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

@app.post('/courses', response_model=CourseOut)
async def create_course(c: CourseCreate):
    query = courses.insert().values(title=c.title, description=c.description)
    r = await database.execute(query)
    return { 'id': r, 'title': c.title, 'description': c.description }

@app.get('/courses')
async def list_courses():
    query = courses.select()
    rows = await database.fetch_all(query)
    return rows
