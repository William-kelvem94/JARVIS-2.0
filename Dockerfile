# Base
FROM node:20-bullseye-slim

# Atualizações básicas
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    make \
    build-essential \
    python3 \
    python3-pip \
    procps \
    && apt-get clean

# Cria o usuário padrão
RUN groupadd -r docker && useradd -r -g docker docker

# Diretórios
WORKDIR /home/docker/jarvis

# Copia apenas package.json para cache mais eficiente
COPY --chown=docker:docker package*.json ./

# Instala apenas o npm primeiro
RUN npm install

# Agora copia o restante do projeto
COPY --chown=docker:docker . .

# Garantir permissões
RUN mkdir -p /home/docker/.npm && chown -R docker:docker /home/docker/.npm

# Instala as dependências Python
RUN pip3 install -r requirements.txt

# User
USER docker

# Porta de comunicação
EXPOSE 1337

# Comando padrão
CMD ["npm", "start"]
