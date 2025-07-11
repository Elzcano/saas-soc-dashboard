from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from app.auth.oauth2 import get_current_user
from app.reports.pdf_generator import generar_pdf
from fastapi.security import OAuth2PasswordBearer
import os

router = APIRouter(prefix="/reportes", tags=["Reportes"])

@router.get("/generar", response_class=FileResponse)
def generar_reporte(current_user=Depends(get_current_user)):
    """
    Genera un reporte PDF para el usuario autenticado y lo retorna como descarga.
    """

    try:
        # Datos simulados (más adelante, vendrán de la base de datos)
        eventos = [
            "Alerta: intento de acceso no autorizado",
            "Evento: archivo malicioso detectado",
            "Conexión sospechosa desde IP 123.123.123.123",
        ]

        ruta_pdf = generar_pdf(usuario=current_user.username, eventos=eventos)

        if not os.path.exists(ruta_pdf):
            raise HTTPException(status_code=404, detail="No se pudo generar el PDF")

        return FileResponse(
            path=ruta_pdf,
            filename=os.path.basename(ruta_pdf),
            media_type='application/pdf'
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar el reporte: {str(e)}")
