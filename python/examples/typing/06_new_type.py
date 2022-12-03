# python -m mypy .\06_new_type.py
from typing import NewType

# defining a new 'type':
JobName = NewType("JobName", str)


def job_handler(jobname: JobName) -> None:
    print(f"handling job {jobname.upper()}")


job_name_1 = "carry eggs"
job_name_2: JobName = JobName("install server")

job_handler(jobname=job_name_1)
job_handler(jobname=job_name_2)

# why???

# We can have additional precision, since we do not just want to handle 'any' string.
# We do not want to re-invent the wheel and come up with a new version of string.


# note, even though mypy complains, the interpretor will still run this without
# any errors.
