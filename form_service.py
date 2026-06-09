from fastapi import APIRouter ,HTTPException 
from backend .models import FormUpdateRequest 
from backend import database as db 
from backend .agent .insurance_agent import agent 
from backend .services .form_service import compute_progress 

router =APIRouter ()

@router .get ("/form/{session_id}")
async def get_form (session_id :str ):
    db .create_session (session_id )
    state =agent .get_form_state (session_id )
    return {
    "session_id":session_id ,
    "fields":state ["fields"],
    "progress":state ["progress"]
    }

@router .post ("/form/update")
async def update_form (request :FormUpdateRequest ):
    
    if not request .session_id :
        raise HTTPException (status_code =400 ,detail ="session_id is required.")

    db .create_session (request .session_id )
    db .upsert_many_fields (request .session_id ,request .fields ,source ="manual")

    form_data =db .get_form_data (request .session_id )
    progress =compute_progress (form_data )

    return {
    "session_id":request .session_id ,
    "message":f"Updated {len (request .fields )} field(s) successfully.",
    "progress":progress 
    }

@router .get ("/progress/{session_id}")
async def get_progress (session_id :str ):
    db .create_session (session_id )
    form_data =db .get_form_data (session_id )
    progress =compute_progress (form_data )
    return {"session_id":session_id ,**progress }
