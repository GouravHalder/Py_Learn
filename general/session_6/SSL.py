import ssl
import socket
import pprint

def get_certificate(hostname, port=8443):
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            return cert

def main():
    print ("Here I am")
    #hostname = 'APP4549.frca.kfplc.com'
    hostname = 'APP3619.uk.b-and-q.com'
    port = 8443
    cert = get_certificate(hostname, port)
    pprint.pprint(cert)

if __name__ == "__main__":
    main()
