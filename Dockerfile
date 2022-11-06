FROM --platform=arm64 python:3
WORKDIR /app
COPY requeriments.txt requeriments.txt
RUN pip install -r requeriments.txt
COPY . .
EXPOSE 8080
CMD [ "flask", "run" , "--host=0.0.0.0"]