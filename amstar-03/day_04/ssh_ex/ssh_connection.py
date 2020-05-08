# ------------------------------------------------------------------------------------------------------- #
# Architect: Purushotham
# Email: purushotham.s82@gmail.com
# Company: Mindful Learning India, Bangalore
# Code: This code demonstrates the use of paramiko module for openssh connection
# ------------------------------------------------------------------------------------------------------- #


import puttykeys # pip install puttykeys
import paramiko  # pip install paramiko

ppkfile = r"newmigdb.ppk" # PuTTY ppk file
pemfile = r"newmigdb.pem" # OpenSSH file

def genOpenSSHKey(ppkfile, pemfile):
    ppkkey = open(ppkfile,"r").read()
    opensshkey = puttykeys.ppkraw_to_openssh(ppkkey)
    open(pemfile, "w").write(opensshkey)


def main():
    genOpenSSHKey(ppkfile, pemfile)

    key = paramiko.RSAKey.from_private_key_file(pemfile)
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print ("Connecting....")
    c.connect( hostname = "", username = "", pkey = key )
    print ("connected")

    commands = [ "ls -l" ]

    for command in commands:

    	print ("Executing {}".format( command ))
    	stdin , stdout, stderr = c.exec_command(command)
    	print (stdout.read())

    	print( "Errors")
    	print (stderr.read())

    c.close()

if __name__ == "__main__":

    main()
