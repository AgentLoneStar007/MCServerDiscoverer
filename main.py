## Imports
import os
# Tests to see if user has MCStatus installed.
try:
    from mcstatus import JavaServer
except:
    print("You don't have MCStatus installed. Do you want to autoinstall it now?")
    autoinstall = input("<Y/n> ")
    if autoinstall.lower() == 'y':
        os.system("pip install mcstatus")
    else:
        exit()

# Main program loop
# For in range loops through all possible IPs.
for a in range(256):
    for g in range(256):
        for e in range(256):
            for n in range(256):
                # Define current IP
                ip = "%d.%d.%d.%d" % (a, g, e, n)
                # Open log file
                logIPs = open("log.txt", "a")

                # Program output
                print(f"Now testing {ip}:25565.")

                # Tests IP. If MCStatus finds a valid response, it's logged as a hit.
                # Otherwise, it's logged as a miss.
                try:
                    server = JavaServer.lookup(ip + "25565")
                    status = server.status()
                    print(f'Server {ip} currently has {status.players.online} players. It is online.')
                    logIPs.write(f"Hit: {ip}:25565\n")
                    logIPs.close()

                except:
                    print(f'IP {ip} either is down or does not have a Minecraft server on it, or it uses a port '
                          f'besides 25565.')
                    logIPs.write(f"Miss: {ip}:25565\n")
                    logIPs.close()
