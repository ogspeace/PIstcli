import os, platform, re, subprocess, time

# executes speedtest-cli command
command = ""
if platform.system().lower() in ('windows','win32'):
    command = "speedtest-cli --simple"
else:
    osdeets = {}
    with open('/etc/os-release','r') as fin:
        for line in fin.readlines():
            key, val = line.split('=')
            osdeets[key] = val
    if osdeets['NAME'] == 'Raspbian GNU/Linux':
        command = "/usr/local/bin/speedtest-cli --simple"
    else:
        command = "speedtest-cli --simple"

response = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

# extracts and stores ping, download, and upload values to respective variables

ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)
ping = ping[0].replace(',', '.')
download = download[0].replace(',', '.')
upload = upload[0].replace(',', '.') 

print(f"Pg: {ping} ms\nDL: {download} Megabits per second\nUL: {upload} Megabits per second")
