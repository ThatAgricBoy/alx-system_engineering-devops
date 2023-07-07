# HTTPS SSL

HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP, the protocol used for transmitting data over the internet. It incorporates SSL (Secure Sockets Layer) or its successor, TLS (Transport Layer Security), to provide encryption and authentication for secure communication between a client (usually a web browser) and a server.

The two main roles of HTTPS and SSL/TLS are as follows:

* Encryption: The primary role of HTTPS and SSL/TLS is to ensure secure communication by encrypting the data transmitted between the client and the server. Encryption transforms the data into a format that can only be read by authorized parties, preventing unauthorized access or eavesdropping.
When a client establishes a connection with an HTTPS-enabled website, SSL/TLS initiates a handshake process, during which the client and server agree on encryption algorithms and exchange cryptographic keys. These keys are then used to encrypt and decrypt data during the session, protecting it from interception or tampering.

Encryption ensures the confidentiality and integrity of the transmitted data, making it extremely difficult for malicious actors to intercept and decipher sensitive information, such as passwords, financial details, or personal data.
* Authentication: The second important role of SSL/TLS is to provide authentication. SSL/TLS allows the client to verify the identity of the server it is communicating with, ensuring that it is connecting to the intended and trusted website.
Authentication is achieved through the use of digital certificates, which are issued by trusted Certificate Authorities (CAs). These certificates contain the website's public key and are signed by the CA, serving as a digital credential that verifies the authenticity of the website.
## Learning Objectives
* What is HTTPS SSL 2 main roles
* What is the purpose encrypting traffic
* What SSL termination means
