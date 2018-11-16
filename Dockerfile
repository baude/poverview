#FROM docker.io/library/alpine:latest
#FROM registry.fedoraproject.org/fedora-minimal:29
FROM registry.fedoraproject.org/fedora:29
RUN dnf install -y python3-podman python3-flask python3-pyroute2
LABEL RUN="podman run -it --rm -v /run/podman/io.podman:/run/podman/io.podman:Z -p 5000:5000 IMAGE python3 pman.py"
WORKDIR /root/code
COPY pman.py /root/code/pman.py
COPY containers.py /root/code/containers.py
COPY socketfinder.py /root/code/socketfinder.py
COPY static /root/code/static


