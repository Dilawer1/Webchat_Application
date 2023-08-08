# Stage 1: build
FROM node:16.14 AS development

WORKDIR /webchat/frontend/src/app

COPY package*.json ./

RUN npm install
RUN npm install -g @angular/cli@16.1.0

COPY . .

RUN npm run build

EXPOSE 4200