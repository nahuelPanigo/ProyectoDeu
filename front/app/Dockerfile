# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /app/package.json
RUN npm install
RUN npm install @vue/cli@3.7.0 -g
RUN vue 
RUN npm install vue-router@3
RUN npm install vue2-leaflet leaflet --save
RUN npm install geojson
RUN npm install vue-tour
RUN npm install vue-hotkeys-rt -S
RUN npm install axios
RUN npm install point-in-polygon

# start app
CMD ["npm", "run", "serve"]
