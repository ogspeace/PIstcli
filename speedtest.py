import os, re, subprocess, time

# executes speedtest-cli command
response = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

# extracts and stores ping, download, and upload values to respective variables
ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

ping = ping[0].replace(',', '.')
download = download[0].replace(',', '.')
upload = upload[0].replace(',', '.') 

print(f"Pg: {ping} ms\nDL: {download} Megabits per second\nUL: {upload} Megabits per second")
