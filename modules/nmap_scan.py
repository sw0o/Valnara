import nmap

def syn_scan():
    # Get target and ports from the user
    target = input("Enter the target IP or hostname: ")
    ports = input("Enter the ports to scan (comma-separated, e.g., 22,80,443): ")

    try:
        # Initialize the PortScanner
        nm = nmap.PortScanner()

        # Perform a SYN scan using Nmap
        print(f"Performing SYN scan on {target} for ports {ports}...")
        nm.scan(hosts=target, ports=ports, arguments='-sS', timeout=1)

        # Display scan results
        if target in nm.all_hosts():
            print(f"Scan results for {target}:")
            for port in nm[target]['tcp']:
                state = nm[target]['tcp'][port]['state']
                print(f"Port {port}: {state.capitalize()}")
        else:
            print("No response from target or target is unreachable.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    syn_scan()
