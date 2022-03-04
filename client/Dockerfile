FROM node:16

WORKDIR /usr/src/app

ENV NODE_PATH=/node_modules
ENV PATH=$PATH:/node_modules/.bin

COPY package.json ./

COPY yarn.lock ./

RUN yarn install

RUN yarn global add serve

COPY . ./

EXPOSE 3000

CMD yarn start