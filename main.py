import sys
import socket
from datetime import datetime
import threading

# Define the function to scan ports
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()
    except Exception as e:
        print("Exception occurred:", e)

def main():
    target_input = input("Enter IP address or domain name: ")
    try:
        target = socket.gethostbyname(target_input)
    except socket.gaierror:
        print("Invalid domain or IP address.")
        sys.exit()

    # Banner
    print("*" * 50)
    print("Scanning Target: " + target)
    print("Started at: " + str(datetime.now()))
    print("*" * 50)

    # Create and start threads for scanning ports
    threads = []
    for port in range(1, 65536):  # Adjust range as per your requirement
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
