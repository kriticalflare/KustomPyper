import sys
import subprocess
import os

if __name__ == "__main__":
    print("hello tasks")
    python_path = sys.executable
    
    file_path = os.getcwd() + "\\cmd_bing.py"
    if not os.path.exists('Venv'):
        subprocess.call(f"""{python_path} -m venv Venv""")
    subprocess.call(f"""Venv\\Scripts\\activate.bat""")
    subprocess.call(f"""pip install -r requirements.txt""")
    subprocess.call(
        f"""{python_path} {file_path} India"""
    )
    # subprocess.call(f'''schtasks /create /tn kustompyper /tr "{python_path} {file_path}\\task.py" /sc minute  /mo 2 /ru "USERNAME" ''')
