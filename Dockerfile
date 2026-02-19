# Run `docker build -t my-command .` then `docker run my-command` from this
# directory.
# Info: https://docs.docker.com/reference/dockerfile/

FROM python:3.14-slim
ENV VIRTUAL_ENV=/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY . .
RUN pip install .
ENTRYPOINT ["python", "my_package/scripts/my_script.py"]
