import paramiko

def backup_router(ip, username, password):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(ip, username=username, password=password)

    command = "/export"

    stdin, stdout, stderr = ssh.exec_command(command)

    config = stdout.read().decode()

    file_name = f"backup_{ip}.rsc"

    with open(file_name, "w") as file:
        file.write(config)

    ssh.close()

    print("Backup selesai:", file_name)