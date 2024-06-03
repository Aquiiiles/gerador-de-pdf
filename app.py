from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def mm_to_p(mm):
    return mm/ 0.352777

pdf = canvas.Canvas('./exemplo.pdf', pagesize=A4)

pdf.setFont('Helvetica-Oblique',14)
pdf.drawString(mm_to_p(20), mm_to_p(50), 'Hello world, welcome to my new project')

pdf.save()