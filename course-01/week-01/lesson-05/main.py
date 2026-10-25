import requests
import json
import logging
from pydantic import BaseModel

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
    
    try: 
        data.raise_for_status()
    except requests.exceptions.HTTPError: 
        logger.warning("error HTTP ")
    
    try:
        parsed_data = data.json()
    except json.JSONDecodeError:
        logger.warning("json decode error")
    
    final_data = Todo(**parsed_data)
    
    return final_data
    
print(fetch_todo(-1))