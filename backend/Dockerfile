# Node Version and Image
# Name Image development
FROM node:16.14 AS development

# Working directory inside container
WORKDIR /webchat/src/app

# Copy package-lock.json & package.json from host to inside container working directory
COPY package*.json ./

# Install deps inside container
RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

# Another image named production
FROM node:16.14 AS production

ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

#  work dir
WORKDIR /webchat/src/app

COPY --from=development /webchat/src/app/ .

EXPOSE 3000

# run app
CMD [ "node", "dist/main"]