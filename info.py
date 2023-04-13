import psutil
import platform
import socket
import datetime

hostname = socket.gethostname()

os_info = platform.uname()

cpu_info = platform.processor()
cpu_usage = psutil.cpu_percent()

print(cpu_info)
print(cpu_usage)

memory = psutil.virtual_memory()
disk_info = psutil.disk_usage('/')
print(memory)
print(disk_info)

now = datetime.datetime.now()

file_name = f"{now.strftime('%d_%Y_%m_%H_%M_%S')}.txt"

with open(file_name, 'w') as f:
    f.write(f'Hostname: {hostname}\n')
    f.write(f'OsInfo: {os_info}\n')
    f.write(f'CpuInfo: {cpu_info}\n')
    f.write(f'CpuUsage: {cpu_usage}\n')
    f.write(f'Memory: {memory}\n')
