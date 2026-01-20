import os
from fastapi import APIRouter, Depends
from sqlmodel import Session

from api.db.session import get_session

from .models import (
EventModel, 
EventListSchema, 
EventCreateSchema,
EventUpdateSchema,
 )

router = APIRouter()
from api.db.config import DATABASE_URL

# LIST VIEW
# GET /api/events
@router.get("/")
def read_events() -> EventListSchema:
    #a bunch of items in a table
    print(os.environ.get("DATABASE_URL"), DATABASE_URL)
    return {
        "results": [
            {"id":1},{"id":2},{"id":3}
            ],
            "count":3
    }

# SEND DATA HERE
# Create View
# POST /api/events/
@router.post("/", response_model=EventModel)
def create_event(
    payload:EventCreateSchema,
    session: Session = Depends(get_session)) :
    # a bunch of items in a table
    
    data = payload.model_dump() # payload -> dict -> pydamtic
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
 
# GET /api/events/12
@router.get("/{event_id}")
def get_event(event_id: int) -> EventModel:
    # a single row
    return {
       "id": event_id
    }

# PUT /api/events/12
@router.put("/{event_id}")
def update_event(event_id: int, payload: EventUpdateSchema) -> EventModel:
    # a single row
   
    data = payload.model_dump()
    return {
       "id": event_id, **data
    }