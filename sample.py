import yaml
import time
import requests

if __name__ == "__main__":

     # Initialize variables

    
    domains = []
    avail = 0

    # Read input file path from user
    filePath = input("Enter the input file path: ")
    try:
        # Read and parse YAML data from the input file
        with open(filePath,"r") as input:
            data = input.read()
            yaml_data = yaml.safe_load(data)
            for item in yaml_data:
                url = item['url'].split('/')
                if url[2] not in domains:
                    domains.append(url[2])

    except FileNotFoundError:
        print("File open error")
    
    domainavail = [0]*len(domains)
    totalRequests = [0]*len(domains)
    avialPercentage = [0]*len(domains)
    try:

        # Monitor domains' availability
        while(True):
            
            for items in yaml_data:
                url = items['url']
                for i, data in enumerate(domains):
                    if data in url:
                        totalRequests[i] += 1
                        break
                result = requests.get(url)
                latency = result.elapsed.total_seconds()*1000
                status = result.status_code
                 # Check availability and latency of domain
                if (status >= 200 & status <= 299) & (latency < 500):
                    for i, data in enumerate(domains):
                        if data in url:
                            domainavail[i] += 1
                            break

            # Calculate and print availability percentages
            for i in range(0, len(domains)):
                avialPercentage[i] = int(100 * (domainavail[i] / totalRequests[i]))
                print(f"{domains[i]} has {avialPercentage[i]}% availability percentage" )
            
            # Wait for 15 seconds before next iteration
            time.sleep(15)
            
    except KeyboardInterrupt:
        exit(0)
        
