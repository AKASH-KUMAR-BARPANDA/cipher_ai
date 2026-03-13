import subprocess

def open_youtube():
    """this will open YouTube"""
    try:
        command = "open https://www.youtube.com"
        result = subprocess.run(command,shell=True,text=True)

        if result.returncode == 0:
            print("YouTube Opened Successfully")
        else:
            print(f"Error ->\n",result.stderr)

    except Exception as e:
        print(f"ERROR OCCUR {e}")


def open_instagram():
    """this will open Instagram"""
    try:
        command = "open https://www.instagram.com"
        result = subprocess.run(command,shell=True,text=True)

        if result.returncode == 0:
            print("Instagram Opened Successfully")
        else:
            print(f"Error ->\n",result.stderr)

    except Exception as e:
        print(f"ERROR OCCUR {e}")

def open_github():
    """this will open GitHub"""
    try:
        command = "open https://github.com"
        result = subprocess.run(command,shell=True,text=True)

        if result.returncode == 0:
            print("Github Opened Successfully")
        else:
            print(f"Error ->\n",result.stderr)

    except Exception as e:
        print(f"ERROR OCCUR {e}")