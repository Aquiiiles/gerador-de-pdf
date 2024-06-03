from reportlab.pdfgen import canvas

pdf = canvas.Canvas('./exemplo.pdf')

pdf.drawString(0, 0, 'Hello world')

pdf.save()

