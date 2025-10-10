from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys, os

# 🔹 Desarrollo local: agrega la carpeta raíz al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 🔹 Routers por entidad
from controllers.sucursales_controller import router as sucursales_router

# Opcional: agrega más routers si ya existen
# from Apis.Apis1.controllers.servicios_controller import router as servicios_router
# from Apis.Apis1.controllers.costos_controller import router as costos_router
# from Apis.Apis1.controllers.promociones_controller import router as promociones_router

# 🔹 Crear app FastAPI
app = FastAPI(title="API Multi-Entidad")

# 🔹 Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Registrar routers
app.include_router(sucursales_router)

# app.include_router(servicios_router)
# app.include_router(costos_router)
# app.include_router(promociones_router)

# 🔹 Mensaje opcional en la raíz
@app.get("/")
def root():
    return {"message": "API Multi-Entidad funcionando correctamente",
    "rutas": {
        "sucursales": "/sucursales",
    }
    }
