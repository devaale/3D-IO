FROM node:17

WORKDIR /usr/src/app

ENV NODE_PATH=/node_modules
ENV PATH=$PATH:/node_modules/.bin

COPY package.json ./
COPY package-lock.json ./

RUN npm install

COPY . ./

EXPOSE 4000

CMD npm start