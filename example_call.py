import subprocess

def notify_user(message):
    subprocess.run(["python", "notify.py", message])

if __name__ == "__main__":
    notify_user("This is a test notification")
