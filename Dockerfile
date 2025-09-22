# 1. Usar una imagen base oficial de Python
FROM python:3.13-slim

# 2. Establecer variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Establecer el directorio de trabajo
WORKDIR /app

# 4. Instalar uv
RUN pip install uv

# 5. Copiar los archivos de dependencias
COPY pyproject.toml uv.lock ./

# 6. Instalar dependencias con uv
RUN uv sync --no-dev

# 7. Copiar el código de la aplicación
COPY ./app ./app

# 8. Exponer el puerto en el que corre la aplicación
EXPOSE 8000

# 9. Comando para ejecutar la aplicación
CMD ["uv", "run", "uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
