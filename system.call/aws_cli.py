# does not run
# FileNotFoundError: [Errno 2] No such file or directory: 'aws s3 --profile cis-dev ls cisint-nb-staging --recursive --summarize | tail -1'

import os
import subprocess

cmd = "aws s3 --profile cis-dev ls cisint-nb-staging --recursive --summarize | tail -1"

# return exit code
exit_code = os.system(cmd)
print ('exit_code:', exit_code)

# return byte string of output
byte_string = subprocess.check_output(cmd)

# decode byte_string
print('output:', byte_string.decode("utf-8"))
