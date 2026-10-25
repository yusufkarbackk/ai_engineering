import requests
import json
import logging
from pydantic import BaseModel, ValidationError

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Todo(BaseModel):
    id: int
    userId: int
    title: str
    completed: bool
    
def fetch_todo(todo_id):
    url = "https://jsonplaceholder.typicode.com/todos/" + str(todo_id)
    
    
    try:
        data = requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        logger.warning("request timeout")
        raise
    except requests.exceptions.ConnectionError:
        logger.warning("connection error")
        raise
    
    try: 
        data.raise_for_status()
    except requests.exceptions.HTTPError: 
        logger.warning("error HTTP ")
        raise
    
    try:
        parsed_data = data.json()
    except json.JSONDecodeError:
        logger.warning("json decode error")
        raise
    
    try:
        final_data = Todo(**parsed_data)
    except ValidationError:
        logger.error("validasi pydantic error")
        raise
    
    return final_data

print(fetch_todo(-1))