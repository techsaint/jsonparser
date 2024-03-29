## Quick Description
This is a system built in AWS Cloudformation. 
It creates the following AWS Resources:
- EC2 instance (default is t2.micro)
- ALB / ALB Listener / LB Target Group 
- Security Group for EC2 instance 
- Security Group for ALB

## Prereqs for running 
- AWS CLI
- AWS Configure (or equiv) set up with Secrets


### Files Included
1. deploy-system.sh   
2. destroy-system.sh 
3. goodrx.cf.json

deploy-system.sh will stand up the environment and deploy the Cloudformation Stack

destroy-system.sh will delete the stack


### How to Run
The application is build in Python and is located here: https://github.com/techsaint/jsonparser
It is deployed onto the EC2 instance using git and Docker. 

running deploy-system.sh should produce this output: 
it will produce this output:
"Exports": [
        {
            "ExportingStackId": "arn:aws:cloudformation:us-west-2:418829585411:stack/techsaint-test-stack/c1092700-132d-11ea-aa4b-06c69e594abe",
            "Name": "techsaint-test-stack-ALBDNS",
            "Value": "BuildAppalb-933841391.us-west-2.elb.amazonaws.com"
        }
    ]
}

Take the ALB DNS value and test the application:  http://BuildAppalb-933841391.us-west-2.elb.amazonaws.com/build

destory the application when complete to free up resources.

