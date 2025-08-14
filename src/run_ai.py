from ai_engine import filter_resumes
import os

resumes_path = "../../data/resumes"
jd_path = "../../data/job_description.txt"
output_path = "../../output"

os.makedirs(output_path, exist_ok=True)

filter_resumes(resumes_path, jd_path, output_path)
