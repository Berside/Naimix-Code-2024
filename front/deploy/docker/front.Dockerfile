FROM node:20.17.0-alpine

WORKDIR /app
COPY package.json /app
RUN npm install
COPY . /app
RUN npm run build
RUN npm install -g serve

EXPOSE 3000

CMD serve -s build -l 3000
