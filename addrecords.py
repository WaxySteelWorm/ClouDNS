# https://pypi.org/project/cloudns-api/  

import cloudns_api
import argparse

# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-i", "--ip", help = "Enter last octet (eg 250)")
parser.add_argument("-n", "--hostname", help = "Enter hostname (eg tor-exit101")
parser.add_argument("-p", "--ipv6_ptr", help = "Enter IPv6 PTR entry (eg 9.0.1")

# Read arguments from command line
args = parser.parse_args()

response = cloudns_api.record.create(domain_name='stormycloud.org', host=(f"{args.hostname}"), record_type='A', record=(f"23.128.248.{args.ip}"), ttl=3600)

response = cloudns_api.record.create(domain_name='stormycloud.org', host=(f"{args.hostname}"), record_type='AAAA', record=(f"2602:FC05:0000:0000:0000:0000:0000:0{args.ip}"), ttl=3600)

response = cloudns_api.record.create(domain_name='248.128.23.in-addr.arpa', host=(f"{args.ip}"), record_type='PTR', record=(f"{args.hostname}.stormycloud.org"), ttl=3600)

response = cloudns_api.record.create(domain_name='0.0.5.0.c.f.2.0.6.2.ip6.arpa', host=(f"{args.ipv6_ptr}.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0"), record_type='PTR', record=(f"{args.hostname}.stormycloud.org"), ttl=3600)
print(response.json())
