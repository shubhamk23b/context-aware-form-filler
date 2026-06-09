import os 
import uuid 
from fastapi import APIRouter ,UploadFile ,File ,Form ,HTTPException 
import aiofiles 

from backend import database as db 
from backend .agent .insurance_agent import agent 

router =APIRouter ()

UPLOAD_DIR ="uploads"
ALLOWED_EXTS ={".pdf",".jpg",".jpeg",".png",".bmp",".tiff",".tif",".webp"}
MAX_FILE_SIZE =10 *1024 *1024 

os .makedirs (UPLOAD_DIR ,exist_ok =True )

@router .post ("/upload")
async def upload_document (
file :UploadFile =File (...),
session_id :str =Form (None )
):
  ext =os .path .splitext (file .filename or "")[1 ].lower ()
    if ext not in ALLOWED_EXTS :
        raise HTTPException (
        status_code =400 ,
        detail =f"Unsupported file type '{ext }'. Allowed: {', '.join (ALLOWED_EXTS )}"
        )

    content =await file .read ()
    if len (content )>MAX_FILE_SIZE :
        raise HTTPException (status_code =413 ,detail ="File too large. Maximum size is 10 MB.")

    if not session_id :
        session_id =str (uuid .uuid4 ())
    db .create_session (session_id )

    safe_name =f"{session_id }_{uuid .uuid4 ().hex }{ext }"
    file_path =os .path .join (UPLOAD_DIR ,safe_name )
    async with aiofiles .open (file_path ,"wb")as f :
        await f .write (content )

    try :
        result =agent .process_document (session_id ,file_path )
    except Exception as e :
        raise HTTPException (status_code =500 ,detail =f"Processing failed: {str (e )}")

    return {
    "session_id":session_id ,
    "filename":file .filename ,
    "success":result ["success"],
    "message":result ["message"],
    "extracted":result ["extracted"],
    "progress":result ["progress"],
    "next_question":result .get ("next_question")
    }
