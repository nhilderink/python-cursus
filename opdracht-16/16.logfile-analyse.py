logfile = open("access_log.txt", "r")
output_file = open("output.txt", "w")
visitors = {}
tellertje = 0

def get_ip(line):
    ip = line.split(" ")[0]
    return ip

def get_ua(line):
    ua = line.split('"')[5]
    return ua

for line in logfile.readlines():
    ip = get_ip(line)
    ua = get_ua(line)

    if ip in visitors:
        visitors[ip]['count'] += 1
    else:
        visitors[ip] = {}
        visitors[ip]['ua'] = ua
        visitors[ip]['count'] = 1

logfile.close()

for ip in visitors:
    tellertje += 1
    count = visitors[ip]['count']
    ua = visitors[ip]['ua']
    output_regel = "{},{},{}\n".format(ip, count, ua)
    output_file.write(output_regel)
    print("{} verwerkt".format(ip))

output_file.close()
print("Klaar - {} ip adressen geteld".format(tellertje))
