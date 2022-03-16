FROM python:3
RUN mkdir WORK_REPO
RUN cd WORK_REPO
WORKDIR /WORK_REPO
ADD requirement.txt .
ADD hello-world.py .
ADD server.py .
RUN pip install -r requirement.txt
CMD ["python", "-u", "server.py"]