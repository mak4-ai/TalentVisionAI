import os
import pdfplumber
import docx
from PyPDF2 import PdfReader
import shutil
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load AI model (semantic embeddings)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Read PDF
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# Read DOCX
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

# Read any resume
def read_resume(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    elif ext == ".txt":
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    else:
        return ""

# Core function to filter resumes
def filter_resumes(resume_folder, jd_file, output_folder, threshold=0.75):
    # Read Job Description
    with open(jd_file, 'r', encoding='utf-8') as f:
        jd_text = f.read()

    jd_embedding = model.encode([jd_text])

    results = []

    for filename in os.listdir(resume_folder):
        file_path = os.path.join(resume_folder, filename)
        resume_text = read_resume(file_path)

        if not resume_text.strip():
            continue

        resume_embedding = model.encode([resume_text])
        score = cosine_similarity(jd_embedding, resume_embedding)[0][0]

        results.append({"Resume": filename, "Score": score})

        if score >= threshold:
            shutil.copy(file_path, output_folder)

    # Save CSV report
    df = pd.DataFrame(results)
    df.to_csv(os.path.join(output_folder, "shortlist_report.csv"), index=False)
    print("Filtering complete! Check output folder.")
