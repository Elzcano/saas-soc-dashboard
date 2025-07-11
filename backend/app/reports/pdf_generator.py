from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generar_pdf(usuario: str, eventos: list, filename: str = "reporte.pdf") -> str:
    ruta = os.path.join("app", "reports", filename)
    c = canvas.Canvas(ruta, pagesize=letter)
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Reporte de Seguridad - SOC")
    
    c.setFont("Helvetica", 12)
    c.drawString(100, 720, f"Generado por: {usuario}")
    
    y = 700
    for evento in eventos:
        if y < 100:
            c.showPage()
            y = 750
        c.drawString(100, y, f"- {evento}")
        y -= 20

    c.save()
    return ruta
