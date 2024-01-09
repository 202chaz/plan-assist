FROM node:18

# set working directory

WORKDIR /ui

COPY package.json ./
RUN npm install

# add app
COPY . .

EXPOSE 3000

CMD ["npm", "run", "start"]