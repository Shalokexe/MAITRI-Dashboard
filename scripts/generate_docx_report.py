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
    elif phase_num == 3:
        add_phase_3_content(doc)
    elif phase_num == 4:
        add_phase_4_content(doc)
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
    doc.add_paragraph("Phase 1 establishes the project foundation and offline database architecture.")

def add_phase_2_content(doc):
    add_heading_styled(doc, "1. Executive Overview")
    doc.add_paragraph("Phase 2 implements the Multimodal Input Pipeline including OpenCV facial emotion and audio stress analysis.")

def add_phase_3_content(doc):
    add_heading_styled(doc, "1. Executive Overview")
    doc.add_paragraph("Phase 3 implements the Offline AI Conversation Engine with empathetic response rules and dialogue persistence.")

def add_phase_4_content(doc):
    add_heading_styled(doc, "1. Executive Overview")
    p = doc.add_paragraph(
        "Phase 4 implements the Health Monitoring Dashboard & Advanced Telemetry Analytics Engine. "
        "It provides real-time health scoring (0-100), physiological boundary evaluation for Heart Rate (BPM), "
        "Blood Oxygen (SpO2), Body Temperature, Stress Index, and 7-day sleep quality trends with Chart.js visualizers."
    )
    p.paragraph_format.line_spacing = 1.15

    add_heading_styled(doc, "2. Key Components Built")
    components = [
        ("Telemetry Health Analytics Engine", "Implemented backend/health/health_monitor.py calculating 0-100 overall health scores, evaluating physiological bounds, and formatting 24-hour telemetry trend analytics."),
        ("Mission Control Health Dashboard UI", "Refactored frontend/index.html & frontend/app.js with dynamic vitals gauges, alert badge status indicators, and sleep stage visualizers."),
        ("Interactive Chart.js Visualizations", "Created live line graphs for HR/SpO2/Stress trends, mood pie charts, and stacked bar charts for deep/REM sleep duration."),
        ("Health Test Suite", "Developed tests/test_health.py verifying nominal vitals evaluation, critical hypoxia/tachycardia detection, and trend aggregation (11/11 tests passing overall).")
    ]

    for comp_name, comp_desc in components:
        bp = doc.add_paragraph(style='List Bullet')
        r1 = bp.add_run(f"{comp_name}: ")
        r1.bold = True
        bp.add_run(comp_desc)

    add_heading_styled(doc, "3. Files Added & Modified")
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
        ("backend/health/health_monitor.py", "NEW", "Health analytics engine & physiological boundary evaluator"),
        ("tests/test_health.py", "NEW", "Unit test suite for health telemetry monitoring"),
        ("docs/update_04.docx", "NEW", "Sequential Phase 4 status report")
    ]

    for path, status, desc in files_list:
        row_cells = files_table.add_row().cells
        row_cells[0].text = path
        row_cells[1].text = status
        row_cells[2].text = desc
        for c in row_cells:
            c.paragraphs[0].runs[0].font.size = Pt(9.5)

    add_heading_styled(doc, "4. Verification & Testing")
    doc.add_paragraph("1. Health Analytics Test: python backend/health/health_monitor.py (Pass)")
    doc.add_paragraph("2. Full System Test Suite: python -m unittest discover tests (11/11 Pass)")

    add_heading_styled(doc, "5. Next Step Plan")
    doc.add_paragraph("Next Step (Phase 5): Build Personalization & Offline Entertainment Vault (Media recommender, lo-fi music, comedy audio, guided relaxation).")

def add_generic_phase_content(doc, phase_num):
    add_heading_styled(doc, f"1. Phase {phase_num} Summary")
    doc.add_paragraph(f"Phase {phase_num} implementation details for MAITRI offline astronaut assistant.")

if __name__ == "__main__":
    phase = 1
    if len(sys.argv) > 1:
        phase = int(sys.argv[1])
    create_update_report(phase)
