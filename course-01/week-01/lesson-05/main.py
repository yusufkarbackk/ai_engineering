import requests
import json
import logging
from pydantic import BaseModel, PositiveInt

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Todo(BaseModel):
    id: int
    userId: int
    title: str
    completed: bool
    
def fetch_todo(todo_id):
    url = "https://jsonplaceholder.typicode.com/todos/" + str(todo_id)
    
    
    data = requests.get(url, timeout=5)
    
    if data.status_code != 200:
        data.raise_for_status()

    
    try:
        parsed_data = data.json()
    except:
        logger.warning("json decode error")
    
    #final_data = Todo(**parsed_data)
    
    print(parsed_data)
    
fetch_todo(1)