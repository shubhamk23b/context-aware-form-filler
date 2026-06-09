from pydantic import BaseModel 
from typing import Optional ,Dict ,Any 

class ChatRequest (BaseModel ):
    session_id :str 
    message :str 

class FormUpdateRequest (BaseModel ):
    session_id :str 
    fields :Dict [str ,Any ]

class SessionResponse (BaseModel ):
    session_id :str 
    message :str 

class ProgressResponse (BaseModel ):
    session_id :str 
    total_fields :int 
    required_fields :int 
    filled_fields :int 
    filled_required :int 
    percent_total :float 
    percent_required :float 
    missing_required :list 
    missing_optional :list
