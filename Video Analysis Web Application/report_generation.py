from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(objects_count):
    # Generate PDF report with object counts
    doc = SimpleDocTemplate("report.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    report_title = "Object Detection Report"
    report_content = [
        f"Number of Potholes: {objects_count['potholes']}",
        f"Number of Lane Markings: {objects_count['lane_markings']}",
        f"Number of Traffic Lights: {objects_count['traffic_lights']}",
        f"Number of Signages: {objects_count['signages']}"
    ]

    content = [Paragraph(report_title, styles['Title'])]
    for line in report_content:
        content.append(Paragraph(line, styles['Normal']))
        content.append(Spacer(1, 12))

    doc.build(content)
    return "report.pdf"
