FROM python:3.8.2
USER root

RUN apt-get update && apt-get -y install locales && \
    localedef -f UTF-8 -i C C.UTF-8
#ENV LANG C.UTF-8
#ENV TZ UTC
#ENV TERM xterm

#RUN apt-get install -y vim less
#RUN pip install --upgrade pip setuptools
COPY ./opt/server.py /app/
#ENTRYPOINT ["bash"]
WORKDIR /app
CMD ["python3", "server.py"]
