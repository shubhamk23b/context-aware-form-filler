from backend .services .extraction_service import extract_text 
from backend .services .llm_service import extract_fields_from_text ,chat_with_agent 
from backend .services .form_service import (
compute_progress ,get_missing_fields ,
get_form_with_schema ,get_next_question ,FIELD_EXPLANATIONS 
)
from backend import database as db 

class InsuranceAgent :

    def process_document (self ,session_id :str ,file_path :str )->dict :
        

        raw_text =extract_text (file_path )
        if not raw_text .strip ():
            return {
            "success":False ,
            "message":"Could not extract any text from the document. "
            "Please ensure the document is readable.",
            "extracted":{},
            "progress":None 
            }

        extracted_fields =extract_fields_from_text (raw_text )

        db .upsert_many_fields (session_id ,extracted_fields ,source ="extracted")

        form_data =db .get_form_data (session_id )
        progress =compute_progress (form_data )
        missing =get_missing_fields (form_data )
        next_q =get_next_question (missing ["missing_required"])

        count =len (extracted_fields )
        if count >0 :
            names =", ".join (extracted_fields .keys ())
            summary =f"I found {count } field(s) in your document: {names }."
        else :
            summary ="I couldn't identify any specific fields in this document."

        if next_q :
            summary +=f"\n\n{next_q ['question']}"
        else :
            summary +="\n\nAll required fields are now filled! You can review and submit."

        db .save_message (session_id ,"assistant",summary )

        return {
        "success":True ,
        "message":summary ,
        "extracted":extracted_fields ,
        "progress":progress ,
        "next_question":next_q 
        }

    def handle_chat (self ,session_id :str ,user_message :str )->dict :
        

        db .save_message (session_id ,"user",user_message )

        form_data =db .get_form_data (session_id )
        missing =get_missing_fields (form_data )
        history =db .get_chat_history (session_id )

        reply ,extracted =chat_with_agent (
        conversation_history =history [:-1 ],
        user_message =user_message ,
        missing_fields =missing ["missing_required"],
        field_explanations =FIELD_EXPLANATIONS 
        )

        if extracted :
            db .upsert_many_fields (session_id ,extracted ,source ="manual")

        db .save_message (session_id ,"assistant",reply )

        form_data =db .get_form_data (session_id )
        progress =compute_progress (form_data )

        return {
        "reply":reply ,
        "extracted":extracted ,
        "progress":progress 
        }

    def get_form_state (self ,session_id :str )->dict :
        """Return the full form with current values and progress."""
        form_data =db .get_form_data (session_id )
        form_fields =get_form_with_schema (form_data )
        progress =compute_progress (form_data )
        return {
        "fields":form_fields ,
        "progress":progress 
        }

agent =InsuranceAgent ()
