## Challenge-2 Extract EC2 instance metadata

## What it does
- Query the metadata of an ec2 instance within AWS and provide a json formatted output.
- Retrieve the value of a particular data key.


## How to run
- login into EC2 instance and place the python script
- Run whichever script you need:
    - `python get_metadata.py`
    - `python get_key.py`

## Please refer evidence of get_metadata.py and get_key.py
- Output 
   - `get_key_output.png`
   - `get_metadata_output.png`
## How it works
- It makes use of the http://169.254.169.254/latest/meta-data link-local address. Instance metatada is provided at this link, but only when you visit it from a running instance.
- A few simple Python scripts are used to extract the required information using the above API.
- See [AWS user guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) for more info on the instance metadata API.