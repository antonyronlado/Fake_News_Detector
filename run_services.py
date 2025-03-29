import subprocess

flask_process = subprocess.Popen(["python", "app.py"])

fastapi_process = subprocess.Popen(["python", "backend_real_time.py"])

flask_process.wait()
fastapi_process.wait()
