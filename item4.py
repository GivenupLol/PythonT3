# DIGITECH Year 9 Term 3 Python Item 4

# Import the 'random' module
from random import *

# Define a function to simulate scanning of machines
def simulate_scan(num_machines):
    # List of Windows versions
    windows_versions = ["Windows 7", "Windows 8", "Windows 10", "Windows 11"]
    
    # Initialize data storage variables
    output = []  # Store detailed scan results
    windows_count = {version: 0 for version in windows_versions}  # Count of each Windows version
    malware_attempts = 0  # Count of malware installation attempts
    malware_successes = 0  # Count of successful malware installations
    
    # Loop through each machine
    for _ in range(num_machines):
        version = random.choice(windows_versions)  # Select a random Windows version
        ip_address = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        
        # Check the Windows version and perform actions accordingly
        if version == "Windows 7":
            malware_attempts += 1
            output.append(f"{ip_address} - {version} detected. Testing malware.")
            # Simulate malware installation success with a 50% chance
            if random.random() < 0.5:
                output.append("-- Malware installation successful.")
                malware_successes += 1
            else:
                output.append("-- Malware installation failed.")
        else:
            output.append(f"{ip_address} - {version} detected. Skipping malware test.")
        
        windows_count[version] += 1  # Update the count for the detected Windows version
    
    # Create a summary of the scan results
    summary = [
        f"Windows 7: {windows_count['Windows 7']} machines.",
        f"Windows 8: {windows_count['Windows 8']} machines.",
        f"Windows 10: {windows_count['Windows 10']} machines.",
        f"Windows 11: {windows_count['Windows 11']} machines.",
        f"Malware attempts: {malware_attempts}",
        f"Malware successes: {malware_successes}",
        f"Malware failed: {malware_attempts - malware_successes}"
    ]
    
    return output, summary

# Define the number of machines to simulate
num_machines = 100

# Simulate the scan and get results and summary
scan_results, scan_summary = simulate_scan(num_machines)

# Print detailed scan results
for result in scan_results:
    print(result)

# Print summary of findings
print("\nSummary of Findings:")
for summary_item in scan_summary:
    print(summary_item)
