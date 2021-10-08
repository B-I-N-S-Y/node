[req]
prompt = no
default_md = sha256
default_bits = 2048
distinguished_name = dn
x509_extensions = v3_req

[dn]
C = TW
ST = Taiwan
L = Taipei
O = Binsy Inc.
OU = IT Department
emailAddress = admin@example.com
CN = Binsy.eth

[v3_req]
subjectAltName = @alt_names

[alt_names]
DNS.1 = binsy.eth
DNS.2 = binsy.bnb
