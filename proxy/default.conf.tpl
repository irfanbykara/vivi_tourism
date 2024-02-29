server {
    listen ${LISTEN_PORT} ssl;
    ssl_certificate     /etc/ssl/certs/tatillikya.com.tr.crt;
    ssl_certificate_key /etc/ssl/certs/tatillikya.com.tr.key;


    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}
