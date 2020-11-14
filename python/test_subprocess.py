import subprocess

process = subprocess.Popen('ls')
print('Durante el proceso')
stdout, stderr = process.communicate()
print('Fin del proceso')
