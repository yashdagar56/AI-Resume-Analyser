from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import tempfile
import os

def generate_pdf_report(result: dict) -> str:
    """
    Generate a branded PDF report using ReportLab.
    Returns the file path to the generated PDF.
    """
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf_path = temp_file.name
    temp_file.close()

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=40, leftMargin=40,
        topMargin=40, bottomMargin=40
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor("#1A202C"),
        spaceAfter=20,
        alignment=1 # Center
    )
    
    h2_style = ParagraphStyle(
        'CustomH2',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.HexColor("#2D3748"),
        spaceBefore=15,
        spaceAfter=10
    )

    normal_style = styles["Normal"]
    normal_style.fontSize = 11
    normal_style.textColor = colors.HexColor("#4A5568")
    
    bold_style = ParagraphStyle(
        'BoldText',
        parent=normal_style,
        fontName='Helvetica-Bold'
    )

    story = []
    
    story.append(Paragraph("AI Resume Analyser Report", title_style))
    
    story.append(Paragraph(f"Score: {result.get('score', 'N/A')}/100", h2_style))
    story.append(Paragraph(f"ATS Verdict: {result.get('ats_verdict', 'N/A')}", normal_style))
    
    story.append(Paragraph("Keyword Match Analysis", h2_style))
    story.append(Paragraph("Matched Keywords:", bold_style))
    matched_items = [ListItem(Paragraph(k, normal_style)) for k in result.get('matched_keywords', [])]
    story.append(ListFlowable(matched_items, bulletType='bullet'))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("Missing Keywords:", bold_style))
    missing_items = [ListItem(Paragraph(k, normal_style)) for k in result.get('missing_keywords', [])]
    if missing_items:
        story.append(ListFlowable(missing_items, bulletType='bullet'))
    
    story.append(Paragraph("Strengths", h2_style))
    strengths_items = [ListItem(Paragraph(s, normal_style)) for s in result.get('strengths', [])]
    if strengths_items:
        story.append(ListFlowable(strengths_items, bulletType='bullet'))
    
    story.append(Paragraph("Weaknesses", h2_style))
    weaknesses_items = [ListItem(Paragraph(w, normal_style)) for w in result.get('weaknesses', [])]
    if weaknesses_items:
        story.append(ListFlowable(weaknesses_items, bulletType='bullet'))
    
    story.append(Paragraph("Improvement Suggestions", h2_style))
    suggestions_items = [ListItem(Paragraph(s, normal_style)) for s in result.get('suggestions', [])]
    if suggestions_items:
        story.append(ListFlowable(suggestions_items, bulletType='1'))
    
    story.append(Paragraph("Rewritten Bullet Points", h2_style))
    rewritten_items = [ListItem(Paragraph(r, normal_style)) for r in result.get('rewritten_bullets', [])]
    if rewritten_items:
        story.append(ListFlowable(rewritten_items, bulletType='bullet'))
    
    doc.build(story)
    
    return pdf_path
