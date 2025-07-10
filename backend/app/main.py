from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from app.routes.user_routes import router

app = FastAPI()

# CORS (por si usas frontend en otro puerto)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción deberías especificar origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

# ✅ Personalizar Swagger para que use solo Bearer Token
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="SaaS SOC API",
        version="1.0.0",
        description="Documentación de autenticación con JWT",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    # Aplica el esquema a todas las rutas
    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

# 🔁 Cambiar el openapi por defecto
app.openapi = custom_openapi
