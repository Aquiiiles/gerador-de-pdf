from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def mm_to_p(mm):
    return mm/ 0.352777

pdf = canvas.Canvas('./exemplo.pdf', pagesize=A4)

pdf.setFont('Helvetica-Bold',18)
pdf.drawString(mm_to_p(20), mm_to_p(50), 'Hello world, welcome to my new project')

pdf.setFont('Helvetica-Oblique', 14)
pdf.drawString(mm_to_p(20), mm_to_p(40), 'this is my first project in python')

pdf.circle(mm_to_p(50), mm_to_p(80), mm_to_p(20))
pdf.rect(mm_to_p(100), mm_to_p(100), mm_to_p(70), mm_to_p(40))

pdf.save()