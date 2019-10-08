FROM python:2.7

WORKDIR /project

ADD . /project

RUN pip install -r requirements.txt

CMD ["/bin/bash", "-c", "sleep 120 && python single.py"]
