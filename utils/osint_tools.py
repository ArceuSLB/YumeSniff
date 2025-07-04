import socket
import dns.resolver
import whois

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except Exception as e:
        return f"[ERROR get_ip] {e}"

def dig_lookup(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return [answer.to_text() for answer in answers]
    except Exception as e:
        return f"[ERROR dig_lookup] {e}"

def get_whois(domain):
    try:
        w = whois.whois(domain)
        return str(w)
    except Exception as e:
        return f"[ERROR whois] {e}"
