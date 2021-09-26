 docker run -d \
  --restart=always \
  --name registry \
  -v /root/certs:/certs \
  -e REGISTRY_HTTP_ADDR=0.0.0.0:443 \
  -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/MyCertificate.crt \
  -e REGISTRY_HTTP_TLS_KEY=/certs/MyKey.key \
  -p 443:443 \
  registry:2
