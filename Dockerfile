FROM python:3.9


# --------------------------------------
# ------------- Set labels -------------

# See https://github.com/opencontainers/image-spec/blob/master/annotations.md
LABEL name="akulai"
LABEL version="2.0.0"
LABEL vendor="akulai"
LABEL org.opencontainers.image.title="akulai"
LABEL org.opencontainers.image.version="2.0.0"
LABEL org.opencontainers.image.url="https://github.com/AkulAI/akulai"
LABEL org.opencontainers.image.documentation="https://github.com/Akul-AI/akulai"

# Install system deps
RUN pip install -r requirements.txt

