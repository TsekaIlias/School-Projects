import os
import sys


class Operation:
    def __init__(self, machine, duration):
        self.machine = machine
        self.duration = duration

    def __repr__(self):
        return (
            f"Operation(machine={self.machine},"
            f" duration={self.duration}, "
        )


class Job:
    def __init__(self, job_id, operations):
        self.job_id = job_id
        self.operations = operations

    def __repr__(self):
        return (
             f"Job(job_id={self.job_id},"
            f"operations={self.operations})"
        )
    
    def total_net_execution_time(self):
        return sum(operation.duration for operation in self.operations)


class Factory:
    def __init__(self, problem_name, jobs, num_machines):
        self.problem_name = problem_name
        self.jobs = jobs
        self.num_machines = num_machines

    @classmethod
    def from_file(cls, fn):
        with open(fn, "r") as f:
            lines = [line.strip() for line in f if line.strip()]

        num_jobs, num_machines = map(int, lines[0].split())

        jobs = []
        for job_id, line in enumerate(lines[1 : num_jobs + 1]):
            parts = list(map(int, line.split()))
            operations = [
                Operation(parts[i], parts[i + 1]) for i in range(0, len(parts), 2)
            ]
            jobs.append(Job(job_id, operations))

        return cls(os.path.basename(fn), jobs, num_machines)

    def __str__(self):
        return (
            f"Job Shop Problem Instance: {self.problem_name}\n"
            f"# jobs: {len(self.jobs)}\n"
            f"# machines : {self.num_machines}"
        )

    def jobs_by_net_execution_time(self):
        sorted_jobs = sorted(self.jobs, key=lambda job: job.total_net_execution_time())   
        sorted_jobs.reverse()
        return sorted_jobs


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python erotima1.py <job_shop_problem_file_name>")
        sys.exit(-1)

    script_directory = os.path.dirname(os.path.abspath(__file__))
    fn = sys.argv[1]
    factory = Factory.from_file(os.path.join(script_directory, fn))
    print(factory)
    jobs = factory.jobs_by_net_execution_time()
    print("Jobs sorted by total execution time")
    for job in jobs:
        print(
            f"Job = {job.job_id}, net total duration = {job.total_net_execution_time()}"
        )