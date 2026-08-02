"""
MAITRI Sequential DOCX Progress Report Generator
Generates formal, formatted Microsoft Word (.docx) progress reports for each Phase of the MAITRI project.
Saved in series as: docs/update_01.docx, docs/update_02.docx, etc.
"""

import os
import sys
from datetime import datetime
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    """Sets background shading of a docx table cell."""
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tc_pr.append(shd)

def create_update_report(phase_num=1, target_folder=None):
    if target_folder is None:
        target_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    docs_dir = os.path.join(target_folder, "docs")
    os.makedirs(docs_dir, exist_ok=True)
    
    filename = f"update_{phase_num:02d}.docx"
    filepath = os.path.join(docs_dir, filename)

    doc = Document()

    # Configure Margins (0.75 in)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)

    # Document Header Title
    title = doc.add_paragraph()
    title_run = title.add_run(f"MAITRI OFFLINE AI ASSISTANT — PHASE {phase_num} REPORT")
    title_run.font.name = 'Arial'
    title_run.font.size = Pt(22)
    title_run.font.bold = True
    title_run.font.color.rgb = RGBColor(15, 32, 67) # Deep Space Navy
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    sub_title = doc.add_paragraph()
    sub_run = sub_title.add_run("Multimodal AI for Total Resilience & Intelligence | NASA/ISRO Mission Architecture")
    sub_run.font.size = Pt(11)
    sub_run.font.italic = True
    sub_run.font.color.rgb = RGBColor(100, 110, 120)
    sub_title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # Metadata Table
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False

    metadata = [
        ("Project Name", "MAITRI (Multimodal AI for Total Resilience & Intelligence)"),
        ("Date & Time", datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")),
        ("Target Repository", "https://github.com/Shalokexe/MAITRI-Dashboard"),
        ("Lead Engineer", "Cmdr. Shalok Dadhwal (Shalokexe)")
    ]

    for idx, (label, val) in enumerate(metadata):
        row = meta_table.rows[idx]
        cell_lbl, cell_val = row.cells[0], row.cells[1]
        
        cell_lbl.text = label
        cell_lbl.paragraphs[0].runs[0].font.bold = True
        cell_lbl.paragraphs[0].runs[0].font.size = Pt(10)
        set_cell_background(cell_lbl, "EBF3FA")
        
        cell_val.text = val
        cell_val.paragraphs[0].runs[0].font.size = Pt(10)

    doc.add_paragraph().paragraph_format.space_after = Pt(16)

    # Content per phase
    if phase_num == 1:
        add_phase_1_content(doc)
    elif phase_num == 2:
        add_phase_2_content(doc)
    else:
        add_generic_phase_content(doc, phase_num)

    doc.save(filepath)
    print(f"[MAITRI DOCX Report] Phase {phase_num} report created successfully at: {filepath}")
    return filepath

def add_heading_styled(doc, text):
    h = doc.add_paragraph()
    run = h.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(14, 116, 144) # Cyber Cyan / Teal
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(6)

def add_phase_1_content(doc):
    add_heading_styled(doc, "1. Executive Overview")
    p = doc.add_paragraph(
        "Phase 1 establishes the complete production-grade foundation for MAITRI, an offline multimodal AI assistant "
        "designed for long-duration space missions (Moon/Mars Artemis habitat). Phase 1 introduces the project directory "
        "architecture, zero-internet SQLite database engine, futuristic mission control web interface skeleton, "
        "and automated Microsoft Word progress reporting pipeline."
    )
    p.paragraph_format.line_spacing = 1.15

    add_heading_styled(doc, "2. Key Components Built")
    components = [
        ("Modular Project Architecture", "Established clean separation between backend AI logic, SQLite DB, frontend UI, media storage, and automated doc generation."),
        ("SQLite Offline Storage Layer", "Built backend/db/schema.sql and backend/db/database.py with 8 core telemetry tables: astronaut profile, facial/voice emotion logs, heart rate/SpO2 vitals history, sleep tracking, mission alerts, content recommendations, chatbot conversation logs, and system updates."),
        ("Mission Control Dashboard Skeleton", "Designed responsive futuristic UI featuring glassmorphism cards, telemetry status bars, real-time vitals graphs using Chart.js, and offline assistant conversation panel."),
        ("DOCX Report Automation", "Developed scripts/generate_docx_report.py using python-docx to generate sequential status updates (update_01.docx through update_07.docx) to satisfy mission logging criteria."),
        ("GitHub Repository & Streak Integration", "Configured clean git repo structure, .gitignore rules, README.md, and CHANGELOG.md ready for GitHub remote deployment.")
    ]

    for comp_name, comp_desc in components:
        bp = doc.add_paragraph(style='List Bullet')
        r1 = bp.add_run(f"{comp_name}: ")
        r1.bold = True
        r2 = bp.add_run(comp_desc)

    add_heading_styled(doc, "3. Files Created & Modified")
    files_table = doc.add_table(rows=1, cols=3)
    files_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = files_table.rows[0].cells
    hdr_cells[0].text = "File Path"
    hdr_cells[1].text = "Status"
    hdr_cells[2].text = "Description"

    for cell in hdr_cells:
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
        set_cell_background(cell, "0F2043")

    files_list = [
        ("backend/db/schema.sql", "NEW", "SQLite DDL schema for offline telemetry and astronaut records"),
        ("backend/db/database.py", "NEW", "Python database manager with row factory, CRUD operations, and seeding"),
        ("frontend/index.html", "NEW/UPDATED", "Sci-Fi futuristic mission control dashboard layout"),
        ("frontend/style.css", "NEW/UPDATED", "Space-themed glassmorphism visual styling & CSS variables"),
        ("frontend/app.js", "NEW/UPDATED", "Frontend logic controller & Chart.js graph initialization"),
        ("scripts/generate_docx_report.py", "NEW", "Automated python-docx sequential status report generator"),
        ("requirements.txt", "NEW", "Python package dependencies (100% offline verified)"),
        ("README.md", "NEW", "Production GitHub documentation & deployment guide"),
        ("CHANGELOG.md", "NEW", "Project milestone & version update history log")
    ]

    for path, status, desc in files_list:
        row_cells = files_table.add_row().cells
        row_cells[0].text = path
        row_cells[1].text = status
        row_cells[2].text = desc
        for c in row_cells:
            c.paragraphs[0].runs[0].font.size = Pt(9.5)

    add_heading_styled(doc, "4. How to Run & Verify Phase 1")
    doc.add_paragraph("1. Initialize and seed local database: python backend/db/database.py")
    doc.add_paragraph("2. Launch Dashboard UI: Open frontend/index.html in any modern browser.")
    doc.add_paragraph("3. Generate Phase 1 Report: python scripts/generate_docx_report.py 1")

    add_heading_styled(doc, "5. Known Issues & Next Steps")
    doc.add_paragraph("Known Issues: WebCam feed currently uses canvas mock stream prior to Phase 2 OpenCV integration.")
    doc.add_paragraph("Next Step (Phase 2): Build OpenCV facial emotion detection pipeline & voice tone stress analyzer.")

def add_generic_phase_content(doc, phase_num):
    add_heading_styled(doc, f"1. Phase {phase_num} Summary")
    doc.add_paragraph(f"Phase {phase_num} implementation details for MAITRI offline astronaut assistant.")

if __name__ == "__main__":
    phase = 1
    if len(sys.argv) > 1:
        phase = int(sys.argv[1])
    create_update_report(phase)
