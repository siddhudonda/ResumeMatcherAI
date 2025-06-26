# ResumeMatcherAI

AI-powered resume and job description matcher using NLP.

## Features
- Resume parsing (PDF/DOCX)
- Job description parsing
- Match score using TF-IDF + Cosine Similarity
- Deployed with Gradio

## How to Run
```bash
pip install -r requirements.txt
python -m nltk.downloader all
python -m spacy download en_core_web_sm
python frontend/app_gradio.py
```

## Future Improvements
- Use Sentence-BERT for deeper matching
- Add keyword suggestion
- Deploy on Hugging Face Spaces
