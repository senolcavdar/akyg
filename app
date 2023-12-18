server {
listen 82;

location / {
  include proxy_params;
  proxy_pass http://unix:opt/akyg/app.sock;
    }


location /static  {
    include  /etc/nginx/mime.types;
    root /opt/akyg/;
  }
}
