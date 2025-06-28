import gradio as gr
from backend.app import run_pipeline

def process_inputs(resume_file, job_file):
    resume_path = resume_file.name
    job_path = job_file.name
    resume_text, job_text, score = run_pipeline(resume_path, job_path)
    return resume_text, job_text, f"Match Score: {score*100:.2f}%"
                                                                            
demo = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.File(label="Upload Resume (PDF or DOCX)"),
        gr.File(label="Upload Job Description (TXT)")
    ],
    outputs=[
        gr.Textbox(label="Resume Details"),
        gr.Textbox(label="Job Description"),
        gr.Textbox(label="Match Score")
    ],
    title="AI Resume to Job Matcher",
    description="Upload your resume and a job description. The system will analyze and give you a match score."
)

if __name__ == "__main__":
    demo.launch()
