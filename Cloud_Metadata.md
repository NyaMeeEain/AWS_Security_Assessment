## AWS 

The metadata API that allows processes in a VM instance to learn the information specific to that VM. Metadata service gives applications an easy way to know the environments they are running in and adjust the configurations accordingly. The metadata API provides information such as instance ID, image ID, private/public IP, and network configuration.
Any user or process, by default, has full access to the metadata API.

```
http://x.x.x.x/latest/user-data
http://x.x.x.x/latest/user-data/iam/security-credentials/[ROLE NAME]
http://x.x.x.x/latest/meta-data/iam/security-credentials/[ROLE NAME]
http://x.x.x.x/latest/meta-data/ami-id
http://x.x.x.x/latest/meta-data/reservation-id
http://x.x.x.x/latest/meta-data/hostname
http://x.x.x.x/latest/meta-data/public-keys/0/openssh-key
http://x.x.x.x/latest/meta-data/public-keys/[ID]/openssh-key
```

## Google Cloud
```
http://x.x.x.x/computeMetadata/v1/
http://metadata.google.internal/computeMetadata/v1/
http://metadata/computeMetadata/v1/
http://metadata.google.internal/computeMetadata/v1/instance/hostname
http://metadata.google.internal/computeMetadata/v1/instance/id
http://metadata.google.internal/computeMetadata/v1/project/project-id
```
## Digital Ocean
```
http://x.x.x.x/metadata/v1.json
http://x.x.x.x/metadata/v1/ 
http://x.x.x.x/metadata/v1/id
http://x.x.x.x/metadata/v1/user-data
http://x.x.x.x/metadata/v1/hostname
http://x.x.x.x/metadata/v1/region
http://x.x.x.x/metadata/v1/interfaces/public/0/ipv6/address
```
## Oracle Cloud
```
http://x.x.x.x/latest/
http://x.x.x.x/latest/user-data/
http://x.x.x.x/latest/meta-data/
http://x.x.x.x/latest/attributes/
```

## Alibaba
```
http://x.x.x.x/latest/meta-data/
http://x.x.x.x/latest/meta-data/instance-id
http://x.x.x.x/latest/meta-data/image-id
```


