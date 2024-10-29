
#in vscode create file app.py
from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse  # von mir
from schemas import ToDoSchema
import random


app= FastAPI()


all_todos = {
    random.randint(1, 100): {"title": "ANN", "description": "DL ANN Classification", "completed": False},
    random.randint(1, 100): {"title": "CNN", "description": "FDL, CNN Classification'", "completed": True},
    random.randint(1, 100): {"title": "GEN", "description": Chatgpt, Ollma", "completed": False},
}  # von mir

@app.get("/todos", response_class=HTMLResponse) # api 01  von mir
def todo_list():
    todos = [{"id": id, **todo} for id, todo in all_todos.items()]
    formatted_todos = "<br>".join(f"<p>{todo}</p>" for todo in todos)
    return formatted_todos
    
@app.get("/todos/{todo_id}")   #  api 02
def todo_detail():
    pass

@app.post("/todos")   #u  api 03
def create_todo(todo:ToDoSchema):
    todo_id = random.randint(1,100)  # generate unique id
    all_todos[todo_id] = todo.model_dump()
    return {"id":todo_id, **all_todos[todo_id]}

@app.put("/todos/{todo_id}")   #  api 04
def edit_todo():
    pass

@app.delete("/todos/{todo_id}")   #  api 05
def delete_todo():
    pass


runapp(1)
