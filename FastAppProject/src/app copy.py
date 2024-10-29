#in vscode create file app.py
#pip install sqlalchemy, #pip install SQLAlchemy, #pip install jinja2

from fastapi import FastAPI, Response, Depends
from schemas import ToDoSchemaIn, ToDoSchemaOut
from typing import List
from sqlalchemy import create_engine, Column, String, Boolean, Integer
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base


app= FastAPI()


#sqlite 
DATABASE_URL="sqlite:///todo.db"  
engine=create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autoflush=False, autocommit=False,bind=engine)
Base = declarative_base()

#design dB Tables
class ToDoModel(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)


# function to create db session
def get_db():
    db = SessionLocal()
    return db


@app.get("/todos", response_model= List[ToDoSchemaOut]) # api 01  von mir
def todo_list(db:Session = Depends(get_db)):
    return db.query(ToDoModel).all()  # return all todos from db : select & from ToDo
    

@app.post("/todos",response_model= ToDoSchemaOut)   #u  api 03
def create_todo(todo:ToDoSchemaIn, db:Session = Depends(get_db)):
    new_todo = ToDoModel(**todo.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo



@app.get("/todos/{todo_id}",response_model= ToDoSchemaOut)   #  api 02
def todo_detail(todo_id:int, db:Session = Depends(get_db)):
    single_todo = db.query(ToDoModel).filter(ToDoModel.id == todo_id).first()
    return  single_todo #{"id":todo_id, **all_todos[todo_id]}


@app.put("/todos/{todo_id}")   #  api 04
def edit_todo(todo_id:int, todo:ToDoSchemaIn, db:Session = Depends(get_db)):
    single_todo = db.query(ToDoModel).filter(ToDoModel.id == todo_id).first()
    for key, value in todo.dict().items():
        setattr(single_todo, key, value)
    db.commit()
    db.refresh(single_todo)
    return single_todo

# @app.put("/todos/{todo_id}")   # API 04
# def edit_todo(todo_id: int, todo: ToDoSchemaIn, db: Session = Depends(get_db)):
#     single_todo = db.query(ToDoModel).filter(ToDoModel.id == todo_id).first()
#     if not single_todo:
#         return {"error": "Todo not found"}  # Optionally handle a case where the todo doesn't exist
    
#     for key, value in todo.dict().items():
#         setattr(single_todo, key, value)
    
#     db.commit()
#     db.refresh(single_todo)  # Corrected typo here
#     return single_todo



@app.delete("/todos/{todo_id}",response_model= ToDoSchemaOut)   #  api 05
def delete_todo(todo_id:int, db:Session = Depends(get_db)):
    single_todo = db.query(ToDoModel).filter(ToDoModel.id == todo_id).first()
    db.delet(single_todo)
    db.commit()
    return single_todo   # return json


# uvicorn app:app --reload        # run in Trminal 
# uvicorn test02:app --reload --port 9001
# Get-Process uvicorn
# Stop-Process -Id <ProcessId>
# uvicorn app02:app --reload
# Start-Process -NoNewWindow -FilePath "uvicorn" -ArgumentList "app:app", "--reload"
# ps uvicorn                     # to get id 
# kill id
