def cd_cmd(directory, cmd):
    cwd = os.getcwd()

    os.chdir(directory)
    raw = subprocess.check_output(cmd)

    os.chdir(cwd)
    return raw
