# TalentVisionAI
AI-powered resume filtering software with GUI and installer


**TalentVisionAI** is an AI-powered resume filtering software designed to help companies automatically screen resumes and match them with job descriptions. It saves HR teams hours of manual work and ensures the best candidates are shortlisted quickly.

---

## **Features**

- Automatically reads resumes in PDF, DOCX, and TXT formats
- Matches resumes with job descriptions using advanced AI algorithms
- Scores and ranks candidates based on relevance
- User-friendly GUI for easy use
- Generates filtered resume lists automatically
- Supports exporting results in multiple formats

---

## **Installation**

1. **Download the installer** from the [GitHub Release](https://github.com/mak4-ai/TalentVisionAI/releases/tag/v1.0)  
2. Run the `.exe` file and follow the installation instructions
3. Once installed, launch **TalentVisionAI** from your desktop or start menu

---

## **Usage**

1. Open TalentVisionAI  
2. Select the **folder containing resumes**  
3. Select the **job description file**  
4. Click **Run**  
5. The software will process all resumes and generate a **filtered output file** with top candidates

---

## **Project Structure**

TalentVisionAI/
│
├─ src/ 
│ ├─ gui.py
│ ├─ ai_engine.py
│ ├─ run_ai.py
│ └─ (other helper .py files)
├─ README.md
└─ icon.ico 



---

## **Technologies Used**

- Python 3.10+
- PyPDF2 & pdfplumber for resume parsing
- Sentence-Transformers (HuggingFace) for semantic matching
- Tkinter for GUI
- PyInstaller for creating installer `.exe`

---

## **Contributing**

Contributions are welcome! Please fork the repo and submit pull requests with improvements or bug fixes.

---

## **License**

This project is open-source and free to use under the MIT License.


