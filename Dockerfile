FROM node:22-bullseye-slim
ENV IS_DOCKER=true

USER root
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      git \
      make \
      build-essential \
      python3 \
      python3-pip \
      procps              # ← adicionamos aqui, para que 'ps' exista no container \
 && rm -rf /var/lib/apt/lists/*

# resto igual...
RUN npm install -g npm@10.9.2
RUN groupadd -r docker && useradd -r -g docker docker
WORKDIR /home/docker/jarvis
RUN chown -R docker:docker /home/docker
RUN mkdir -p /home/docker/.npm && chown -R docker:docker /home/docker/.npm
USER docker

COPY --chown=docker:docker . .
RUN npm install
RUN npm run build

EXPOSE 1337
CMD ["npm","start"]
