import os
try:
    from mcstatus import JavaServer
except:
    print("You don't have MCStatus installed. Do you want to autoinstall it now?")
    autoinstall = input("<Y/n> ")
    if autoinstall.lower() == 'y':
        os.system("pip install mcstatus")
    else:
        exit()

while True:
    for k in range(256):
        for l in range(256):
            for m in range(256):
                for n in range(256):
                    ip = "%d.%d.%d.%d" % (k, l, m, n)
                    log = open("log.txt", "a")
                    print(f"Now testing {ip}:25565.")
                    try:
                        server = JavaServer.lookup(ip + "25565")
                        status = server.status()
                        print(f'Server {ip} currently has {status.players.online} players. It is online.')
                        log.write(f"Hit: {ip}:25565\n")
                        log.close()
                    except:
                        print(f'IP {ip} either is down or does not have a Minecraft server on it, or it uses a port besides 25565.')
                        log.write(f"Miss: {ip}:25565\n")
                        log.close()
