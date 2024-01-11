"""
SNORT 2 Synthetic rule generator
AUTHOR: frbello at cisco dot com
REV: JAN-2024
USAGE: 
"""


def generate_snort_rules(num_rules):
    protocols = ['ip','tcp', 'udp', 'icmp']
    src_ip = '16.0.0.0/8'
    dst_ip = '48.0.0.0/8'
    rules = []

    for i in range(num_rules):
        protocol = protocols[i % len(protocols)]
        classtype = generate_class_type(i)
        src_port = str(1000 + (i % 1000))  # Example port range
        dst_port = str(2000 + (i % 1000))  # Example port range
        rule = f"alert {protocol} {src_ip} any <> {dst_ip} any (msg:PoV Custom Rule {i+1}; classtype:{classtype}; rev:2; gid:1; sid:{1000000+i};)"
        rules.append(rule)
        rule = f"alert {protocol} {dst_ip} any <> {src_ip} any (msg:PoV Custom Rule {i+2500}; classtype:{classtype}; rev:2; gid:1; sid:{1002500+i};)"
        rules.append(rule)



    return rules


def generate_class_type(index):
    classlist = [
        'attempted-admin',
'attempted-dos',
'attempted-recon',
'attempted-user',
'bad-unknown',
'client-side-exploit',
'default-login-attempt',
'denial-of-service',
'file-format',
'icmp-event',
'inappropriate-content',
'malware-cnc',
'misc-activity',
'misc-attack',
'network-scan',
'non-standard-protocol',
'not-suspicious',
'policy-violation',
'protocol-command-decode',
'rpc-portmap-decode',
'sdf',
'shellcode-detect',
'string-detect',
'successful-admin',
'successful-dos',
'successful-recon-largescale',
'successful-recon-limited',
'successful-user',
'suspicious-filename-detect',
'suspicious-login',
'system-call-detect',
'tcp-connection',
'trojan-activity',
'unknown',
'unsuccessful-user',
'unusual-client-port-connection',
'web-application-activity',
'web-application-attack'
    ]

    return classlist[index % len(classlist)]




def main():
    # Generate 10 example rules
    example_rules = generate_snort_rules(2500)
    for rule in example_rules:
        print(rule)


if __name__=="__main__":
    main()
