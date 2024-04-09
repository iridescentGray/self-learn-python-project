import time

from demo_job import long_time_get_str
from redis import Redis
from rq import Queue

# 运行前，请确保local host redis已经开启
q = Queue(connection=Redis())

if __name__ == "__main__":
    jobs = []
    for i in range(10):
        job = q.enqueue(long_time_get_str, i)
        jobs.append(job)

    for job_in_list in jobs:
        print(job_in_list.return_value())
    # wait for execute complete
    time.sleep(3)
    for job_in_list in jobs:
        print(job_in_list.return_value())
