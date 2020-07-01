# DEVOPS TIMESERVICES CODING CHALLENGE
This is my implementation of the challenge

# DEPLOYMENT OF SERVICE
The CloudFormation template timeservice.yml will deploy the following AWS infrastructure
- VPC
- Public/Private Subnets
- Routing tables
- Elastic load balancer
- S3 VPC endpoint
- Autoscaling Group
- EC2 instances

To deploy the service ensure your AWS_PROFILE is set correctly and run the following command
in the root of the respository
```
aws cloudformation create-stack --stack-name timeservice --template-body file://timeservice.yaml --capabilities CAPABILITY_NAMED_IAM
```

# HEALTHCHECK SCRIPT
To configure your environment for running the health check script
* Install [python 3.7.5](https://www.python.org/downloads/)
* Install [pip3](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-pip)
* Configure your environmemnt
```
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```
* Run the health check script
```
./health_check.py
```
