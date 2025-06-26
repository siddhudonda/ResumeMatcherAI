import os
from pyresparser import ResumeParser

def extract_resume_data(file_path):
    if not os.path.exists(file_path):
        return {"error": "File does not exist."}
    try:
        data = ResumeParser(file_path).get_extracted_data()
        return data
    except Exception as e:
        return {"error": str(e)}