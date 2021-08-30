FROM nginx:alpine
COPY /build/html/index.html /build/html/ /usr/share/nginx/html/
