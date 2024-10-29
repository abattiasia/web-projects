#in vscode create file app.py
from fastapi import FastAPI, Response
from schemas import ToDoSchemaIn, ToDoSchemaOut
from sqlalchemy import create_engine, Column, String, Boolean, Integer
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base


app= FastAPI()


#sqlite 
DATABASE_URL="sqlite://todo.db"  
engine=create_engine(DATABASE_URL, connect_args={"check_samo_thread":False})
SessionLocal = sessionmaker(autoflush=False, autocommit=False,bind=engine)
Base = declarative_base()

#design dB Tables
class ToDo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primery_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)


Base.metada.create_all(bind=engine)


# function to create db session
def get_db():
    db = SessionLocal()
    return db


@app.get("/todos") # api 01  von mir
def todo_list():
    return [{"id": id, **todo} for id, todo in all_todos.items()]
    

@app.post("/todos")   #u  api 03
def create_todo(todo:ToDoSchema):
    todo_id = random.randint(1,100)  # generate unique id
    all_todos[todo_id] = todo.model_dump()
    return {"id":todo_id, **all_todos[todo_id]}


# @app.get("/todos/{todo_id}")   #  api 02
# def todo_detail(todo_id:int):
#     return {"id":todo_id, **all_todos[todo_id]}


# @app.put("/todos/{todo_id}")   #  api 04
# def edit_todo(todo_id:int, todo:ToDoSchema):
#     all_todos[todo_id].update(todo.model_dump())
#     return {"id":todo_id, **all_todos[todo_id]}

# @app.delete("/todos/{todo_id}")   #  api 05
# def delete_todo(todo_id:int):
#     del all_todo[todo_id]
#     return {"message":"todo was deleted"}  # return json






# uvicorn app:app --reload        # run in Trminal 
# uvicorn test02:app --reload --port 9001
# Get-Process uvicorn
# Stop-Process -Id <ProcessId>
# uvicorn app02:app --reload
# Start-Process -NoNewWindow -FilePath "uvicorn" -ArgumentList "app:app", "--reload"
# ps uvicorn                     # to get id 
# kill id