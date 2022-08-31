FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install -i https://test.pypi.org/simple/ deep-profane==0.0.6
RUN pip install -q -U "tensorflow-text==2.8.*"
COPY . .
EXPOSE 80
CMD ["python", "./app.py"]