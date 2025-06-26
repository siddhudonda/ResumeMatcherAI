from resume_parser import extract_resume_data
from job_parser import parse_job_description
from matcher import match_resume_to_job
from utils import format_resume_data


def run_pipeline(resume_path, job_path):
    resume_data = extract_resume_data(resume_path)
    job_description = parse_job_description(job_path)
    resume_text = format_resume_data(resume_data)
    score = match_resume_to_job(resume_text, job_description)
    return resume_text, job_description, score