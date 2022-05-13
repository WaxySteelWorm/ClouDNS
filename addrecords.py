# https://pypi.org/project/cloudns-api/ 

import cloudns_api
#Input variables

ip = input('Enter IPv4 Address: ')
hostname = input('Enter Hostname: ')
ipv6_ptr = input('Enter IPv6 Record| eg 109 = 9.0.1: ')

response = cloudns_api.record.create(domain_name='stormycloud.org', host=(f"{hostname}"), record_type='A', record=(f"23.128.248.{ip}"), ttl=3600)

response = cloudns_api.record.create(domain_name='stormycloud.org', host=(f"{hostname}"), record_type='AAAA', record=(f"2602:FC05:0000:0000:0000:0000:0000:0{ip}"), ttl=3600)

response = cloudns_api.record.create(domain_name='248.128.23.in-addr.arpa', host=(f"{ip}"), record_type='PTR', record=(f"{hostname}.stormycloud.org"), ttl=3600)

response = cloudns_api.record.create(domain_name='0.0.5.0.c.f.2.0.6.2.ip6.arpa', host=(f"{ipv6_ptr}.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0"), record_type='PTR', record=(f"{hostname}.stormyc>

print(response.json())
