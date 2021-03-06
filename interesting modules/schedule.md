
The [schedule](https://github.com/dbader/schedule) module prides itself for the following:
- A simple to use API for scheduling jobs.
- Very lightweight and no external dependencies.
- Excellent test coverage.
- Tested on Python 3.6, 3.7, 3.8, 3.9



```python
import schedule
import time
from datetime import datetime

def collect_device_backup():
    now = datetime.now().strftime("%H:%M:%S")
    print(f"Collecting device backup at {now}.")


def collect_device_facts():
    now = datetime.now().strftime("%H:%M:%S")
    print(f"Collecting device facts at {now}.")    
 

def data_harvester():    
    schedule.every(10).to(20).seconds.do(collect_device_backup)
    schedule.every(10).to(20).seconds.do(collect_device_facts)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    data_harvester()

```

