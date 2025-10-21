FROM python:3.11.13-slim
WORKDIR /app
RUN pip install "fastapi[standard]"
COPY task1.py .
CMD [ "fastapi","dev","task1.py","--host","0.0.0.0","--port","8000" ]
