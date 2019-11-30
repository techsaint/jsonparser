CFTemplate=goodrx.cf.json
STACKNAME="goodrx-jsonparser-docker-stack"

aws cloudformation deploy --template-file $CFTemplate --stack-name $STACKNAME
aws cloudformation list-exports 

