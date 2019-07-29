import dns.resolver
import socket

def run(domain):
    ips = []
    print("yay we're here\n")
    try:
        answers = dns.resolver.query(domain, "A")
        for a in answers:
            ips.append(a.address)
        return ips
    except Exception:
        print("Regular DNS Not Resolved\n")
        pass
    try:
       ips = [ str(i[4][0]) for i in socket.getaddrinfo(domain, 443) ] 
       return ips
    except Exception:
       print("No host resolved!\n")
       return ips
