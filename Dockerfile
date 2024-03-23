
FROM python:3.9

WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt ./

# Instala as dependências
RUN sh -c "pip install --upgrade pip && pip install -r requirements.txt "

# Copia o restante dos arquivos para o contêiner
COPY . .

EXPOSE 80
        