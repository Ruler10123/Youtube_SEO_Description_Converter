import subprocess

process1 = subprocess.Popen(['python', 'extract_audio.py'])
process1.wait()
process2 = subprocess.Popen(['python', 'transcribe.py'])
process2.wait()