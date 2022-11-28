from work.computeEngine import BackendCompute
import requests
"""
This script will call the load balancer 100 times calling the same shit.
"""
if __name__ == "__main__":
    for i in range(100):
        url = "http://localhost:8080/compute"
        try:
            x = requests.post(url, data={"heads": str(i)})
            print(x.text)
        except Exception:
            print("error")
            pass
