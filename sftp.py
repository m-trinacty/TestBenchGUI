import os
import paramiko
class SFTPClient:
    def __init__(self):
        self.IP = "192.168.151.1"
        self.PORT = 22
        self.USERNAME= "root"
        self.password=""
        self.remotePath= "/var/log/tevogs/testbench.log"
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #self.ssh.connect(hostname=self.IP, port=self.PORT, username=self.USERNAME)
        self.ssh.connect(hostname = self.IP,username = self.USERNAME,password = self.password,port = self.PORT,look_for_keys=False,allow_agent=False)
        self.sftp = self.ssh.open_sftp()

    def getFile(self,path):
        self.sftp.get(self.remotePath,path)
        
    def close(self):
        self.sftp.close()
        self.ssh.close()