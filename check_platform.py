import platform

def check_platform():
    return 'clear' if platform.system() == 'Darwin' else 'cls' if platform.system() == 'Windows' else None
clear_command = check_platform()