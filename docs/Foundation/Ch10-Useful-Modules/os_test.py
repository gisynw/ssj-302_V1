import os
print('Name of operation system', os.name)
print(os.getenv('PYTHONPATH'))
print('User name',os.getlogin())
print('Current ID',os.getpgid())
print('Parent ID',os.getppid())
print('Cpu Number',os.cpu_count())
print('Line space Symbol',os.linesep)