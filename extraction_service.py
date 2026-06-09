from fastapi import APIRouter ,HTTPException 
from backend .models import ChatRequest 
from backend import database as db 
from backend .agent .insurance_agent import agent 

router =APIRouter ()

@router .post ("/chat")
async def chat (request :ChatRequest ):
    
    if not request .session_id or not request .message .strip ():
        raise HTTPException (status_code =400 ,detail ="session_id and message are required.")

    db .create_session (request .session_id )

    result =agent .handle_chat (request .session_id ,request .message )

    return {
    "session_id":request .session_id ,
    "reply":result ["reply"],
    "extracted":result ["extracted"],
    "progress":result ["progress"]
    }

@router .get ("/chat/history/{session_id}")
async def get_history (session_id :str ):
    """Return full chat history for a session."""
    history =db .get_chat_history (session_id )
    return {"session_id":session_id ,"history":history }
