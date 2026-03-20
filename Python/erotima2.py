import os
import sys
import logging
from erotima1 import Factory

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class Solution:
    def __init__(self, factory):
        self.factory = factory
        self.schedule = {}
        self.current_time = 0

    def eet(self):
        jobs_ops_remaining = []

        for job in self.factory.jobs:
            job_operations = list(job.operations)
            jobs_ops_remaining.append((job.job_id, job_operations))

        while any(ops for _, ops in jobs_ops_remaining):
            next_job = None
            next_duration = None
            next_machine = None
            job_idx = None

            for idx, (job_id, operations) in enumerate(jobs_ops_remaining):
                if not operations:
                    continue
                op = operations[0]
                if next_duration is None or op.duration < next_duration:
                    next_duration = op.duration
                    next_machine = op.machine
                    next_job = job_id
                    job_idx = idx

            operation = jobs_ops_remaining[job_idx][1].pop(0)
            start_time = self.current_time
            end_time = start_time + operation.duration

            op_index = len(self.factory.jobs[next_job].operations) - len(jobs_ops_remaining[job_idx][1]) - 1
            self.schedule[(next_job, op_index)] = (start_time, end_time, operation.machine)

            logger.debug(
                f"Scheduled Job {next_job} Op {op_index} on Machine {operation.machine}: Start={start_time}, End={end_time}"
            )

            self.current_time = end_time

    def makespan(self):
        return self.current_time

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python erotima2.py <job_shop_problem_file>")
        sys.exit(1)

    filename = sys.argv[1]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, filename)

    factory = Factory.from_file(full_path)

    solution = Solution(factory)
    solution.eet()
