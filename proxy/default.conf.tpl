server {
    listen ${LISTEN_PORT};
    server_name tatillikya.com.tr;

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name tatillikya.com.tr;

    ssl_certificate /etc/ssl/certs/tatillikya_com_tr.crt;
    ssl_certificate_key /etc/ssl/certs/tatillikya.com.tr.key;
    ssl_trusted_certificate /etc/ssl/certs/USERTrustRSAAAACA.crt;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass ${APP_HOST}:${APP_PORT};
        include /etc/nginx/uwsgi_params;
        client_max_body_size 10M;
    }
}

