r'''
# CloudFront Origins for the CDK CloudFront Library

This library contains convenience methods for defining origins for a CloudFront distribution. You can use this library to create origins from
S3 buckets, Elastic Load Balancing v2 load balancers, or any other domain name.

## S3 Bucket

An S3 bucket can be used as an origin. An S3 bucket origin can either be configured using a standard S3 bucket or using a S3 bucket that's configured as a website endpoint (see AWS docs for [Using an S3 Bucket](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistS3AndCustomOrigins.html#using-s3-as-origin)).

> Note: `S3Origin` has been deprecated. Use `S3BucketOrigin` for standard S3 origins and `S3StaticWebsiteOrigin` for static website S3 origins.

### Standard S3 Bucket

To set up an origin using a standard S3 bucket, use the `S3BucketOrigin` class. The bucket
is handled as a bucket origin and
CloudFront's redirect and error handling will be used. It is recommended to use `S3BucketOrigin.withOriginAccessControl()` to configure OAC for your origin.

```python
my_bucket = s3.Bucket(self, "myBucket")
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.S3BucketOrigin.with_origin_access_control(my_bucket))
)
```

> Note: When you use CloudFront OAC with Amazon S3 bucket origins, you must set Amazon S3 Object Ownership to Bucket owner enforced (the default for new Amazon S3 buckets). If you require ACLs, use the Bucket owner preferred setting to maintain control over objects uploaded via CloudFront.

### S3 Bucket Configured as a Website Endpoint

To set up an origin using an S3 bucket configured as a website endpoint, use the `S3StaticWebsiteOrigin` class. When the bucket is configured as a
website endpoint, the bucket is treated as an HTTP origin,
and the distribution can use built-in S3 redirects and S3 custom error pages.

```python
my_bucket = s3.Bucket(self, "myBucket")
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.S3StaticWebsiteOrigin(my_bucket))
)
```

### Restricting access to a standard S3 Origin

CloudFront provides two ways to send authenticated requests to a standard Amazon S3 origin:

* origin access control (OAC) and
* origin access identity (OAI)

OAI is considered legacy due to limited functionality and regional
limitations, whereas OAC is recommended because it supports all Amazon S3
buckets in all AWS Regions, Amazon S3 server-side encryption with AWS KMS (SSE-KMS), and dynamic requests (PUT and DELETE) to Amazon S3. Additionally,
OAC provides stronger security posture with short term credentials,
and more frequent credential rotations as compared to OAI. OAI and OAC can be used in conjunction with a bucket that is not public to
require that your users access your content using CloudFront URLs and not S3 URLs directly.

See AWS docs on [Restricting access to an Amazon S3 Origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) for more details.

> Note: OAC and OAI can only be used with an regular S3 bucket origin (not a bucket configured as a website endpoint).

The `S3BucketOrigin` class supports creating a standard S3 origin with OAC, OAI, and no access control (using your bucket access settings) via
the `withOriginAccessControl()`, `withOriginAccessIdentity()`, and `withBucketDefaults()` methods respectively.

#### Setting up a new origin access control (OAC)

Setup a standard S3 origin with origin access control as follows:

```python
my_bucket = s3.Bucket(self, "myBucket")
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(
        origin=origins.S3BucketOrigin.with_origin_access_control(my_bucket)
    )
)
```

When creating a standard S3 origin using `origins.S3BucketOrigin.withOriginAccessControl()`, an [Origin Access Control resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-originaccesscontrol-originaccesscontrolconfig.html) is automatically created with the origin type set to `s3` and signing behavior set to `always`.

You can grant read, read versioned, list, write or delete access to the OAC using the `originAccessLevels` property:

```python
my_bucket = s3.Bucket(self, "myBucket")
s3_origin = origins.S3BucketOrigin.with_origin_access_control(my_bucket, origin_access_levels=[cloudfront.AccessLevel.READ, cloudfront.AccessLevel.READ_VERSIONED, cloudfront.AccessLevel.WRITE, cloudfront.AccessLevel.DELETE])
```

The read versioned permission does contain the read permission, so it's required to set both `AccessLevel.READ` and
`AccessLevel.READ_VERSIONED`.

For details of list permission, see [Setting up OAC with LIST permission](#setting-up-oac-with-list-permission).

You can also pass in a custom S3 origin access control:

```python
my_bucket = s3.Bucket(self, "myBucket")
oac = cloudfront.S3OriginAccessControl(self, "MyOAC",
    signing=cloudfront.Signing.SIGV4_NO_OVERRIDE
)
s3_origin = origins.S3BucketOrigin.with_origin_access_control(my_bucket,
    origin_access_control=oac
)
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(
        origin=s3_origin
    )
)
```

An existing S3 origin access control can be imported using the `fromOriginAccessControlId` method:

```python
imported_oAC = cloudfront.S3OriginAccessControl.from_origin_access_control_id(self, "myImportedOAC", "ABC123ABC123AB")
```

> [Note](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html): When you use OAC with S3
> bucket origins, the bucket's object ownership must be either set to Bucket owner enforced (default for new S3 buckets) or Bucket owner preferred (only if you require ACLs).

#### Setting up OAC with a SSE-KMS encrypted S3 origin

If the objects in the S3 bucket origin are encrypted using server-side encryption with
AWS Key Management Service (SSE-KMS), the OAC must have permission to use the KMS key.

Setting up a standard S3 origin using `S3BucketOrigin.withOriginAccessControl()` will automatically add the statement to the KMS key policy
to give the OAC permission to use the KMS key.

```python
import aws_cdk.aws_kms as kms


my_kms_key = kms.Key(self, "myKMSKey")
my_bucket = s3.Bucket(self, "mySSEKMSEncryptedBucket",
    encryption=s3.BucketEncryption.KMS,
    encryption_key=my_kms_key,
    object_ownership=s3.ObjectOwnership.BUCKET_OWNER_ENFORCED
)
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(
        origin=origins.S3BucketOrigin.with_origin_access_control(my_bucket)
    )
)
```

##### Scoping down the key policy

I saw this warning message during synth time. What do I do?

```text
To avoid a circular dependency between the KMS key, Bucket, and Distribution during the initial deployment, a wildcard is used in the Key policy condition to match all Distribution IDs.
After deploying once, it is strongly recommended to further scope down the policy for best security practices by following the guidance in the "Using OAC for a SSE-KMS encrypted S3 origin" section in the module README.
```

If the S3 bucket has an `encryptionKey` defined, `S3BucketOrigin.withOriginAccessControl()`
will automatically add the following policy statement to the KMS key policy to allow CloudFront read-only access (unless otherwise specified in the `originAccessLevels` property).

```json
{
    "Statement": {
        "Effect": "Allow",
        "Principal": {
            "Service": "cloudfront.amazonaws.com"
        },
        "Action": "kms:Decrypt",
        "Resource": "*",
        "Condition": {
            "ArnLike": {
                "AWS:SourceArn": "arn:aws:cloudfront::<account ID>:distribution/*"
            }
        }
    }
}
```

This policy uses a wildcard to match all distribution IDs in the account instead of referencing the specific distribution ID to resolve the circular dependency. The policy statement is not as scoped down as the example in the AWS CloudFront docs (see [SSE-KMS section](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#create-oac-overview-s3)).

After you have deployed the Distribution, you should follow these steps to only grant permissions to the specific distribution according to AWS best practices:

**Step 1.** Copy the key policy

**Step 2.** Use an escape hatch to update the policy statement condition so that

```json
  "Condition": {
      "ArnLike": {
          "AWS:SourceArn": "arn:aws:cloudfront::<account ID>:distribution/*"
      }
  }
```

...becomes...

```json
  "Condition": {
      "StringEquals": {
          "AWS:SourceArn": "arn:aws:cloudfront::111122223333:distribution/<CloudFront distribution ID>"
      }
  }
```

> Note the change of condition operator from `ArnLike` to `StringEquals` in addition to replacing the wildcard (`*`) with the distribution ID.

To set the key policy using an escape hatch:

```python
import aws_cdk.aws_kms as kms


kms_key = kms.Key(self, "myKMSKey")
my_bucket = s3.Bucket(self, "mySSEKMSEncryptedBucket",
    encryption=s3.BucketEncryption.KMS,
    encryption_key=kms_key,
    object_ownership=s3.ObjectOwnership.BUCKET_OWNER_ENFORCED
)
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(
        origin=origins.S3BucketOrigin.with_origin_access_control(my_bucket)
    )
)

# Add the following to scope down the key policy
scoped_down_key_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": {
            "AWS": "arn:aws:iam::111122223333:root"
        },
        "Action": "kms:*",
        "Resource": "*"
    }, {
        "Effect": "Allow",
        "Principal": {
            "Service": "cloudfront.amazonaws.com"
        },
        "Action": ["kms:Decrypt", "kms:Encrypt", "kms:GenerateDataKey*"
        ],
        "Resource": "*",
        "Condition": {
            "StringEquals": {
                "AWS:SourceArn": "arn:aws:cloudfront::111122223333:distribution/<CloudFront distribution ID>"
            }
        }
    }
    ]
}
cfn_key = (kms_key.node.default_child)
cfn_key.key_policy = scoped_down_key_policy
```

**Step 3.** Deploy the stack

> Tip: Run `cdk diff` before deploying to verify the
> changes to your stack.

**Step 4.** Verify your final key policy includes the following statement after deploying:

```json
{
    "Effect": "Allow",
    "Principal": {
        "Service": [
            "cloudfront.amazonaws.com"
        ]
     },
    "Action": [
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:GenerateDataKey*"
    ],
    "Resource": "*",
    "Condition": {
            "StringEquals": {
                "AWS:SourceArn": "arn:aws:cloudfront::111122223333:distribution/<CloudFront distribution ID>"
            }
        }
}
```

##### Updating imported key policies

If you are using an imported KMS key to encrypt your S3 bucket and want to use OAC, you will need to update the
key policy manually to allow CloudFront to use the key. Like most imported resources, CDK apps cannot modify the configuration of imported keys.

After deploying the distribution, add the following policy statement to your key policy to allow CloudFront OAC to access your KMS key for SSE-KMS:

```json
{
    "Sid": "AllowCloudFrontServicePrincipalSSE-KMS",
    "Effect": "Allow",
    "Principal": {
        "Service": [
            "cloudfront.amazonaws.com"
        ]
     },
    "Action": [
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:GenerateDataKey*"
    ],
    "Resource": "*",
    "Condition": {
            "StringEquals": {
                "AWS:SourceArn": "arn:aws:cloudfront::111122223333:distribution/<CloudFront distribution ID>"
            }
        }
}
```

See CloudFront docs on [SSE-KMS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#create-oac-overview-s3) for more details.

#### Setting up OAC with imported S3 buckets

If you are using an imported bucket for your S3 Origin and want to use OAC,
you will need to update
the S3 bucket policy manually to allow the OAC to access the S3 origin. Like most imported resources, CDK apps cannot modify the configuration of imported buckets.

After deploying the distribution, add the following
policy statement to your
S3 bucket to allow CloudFront read-only access
(or additional S3 permissions as required):

```json
{
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Principal": {
            "Service": "cloudfront.amazonaws.com"
        },
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::<S3 bucket name>/*",
        "Condition": {
            "StringEquals": {
                "AWS:SourceArn": "arn:aws:cloudfront::111122223333:distribution/<CloudFront distribution ID>"
            }
        }
    }
}
```

See CloudFront docs on [Giving the origin access control permission to access the S3 bucket](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#create-oac-overview-s3) for more details.

> Note: If your bucket previously used OAI, you will need to manually remove the policy statement
> that gives the OAI access to your bucket after setting up OAC.

#### Setting up OAC with LIST permission

By default, S3 origin returns 403 Forbidden HTTP response when the requested object does not exist.
When you want to receive 404 Not Found, specify `AccessLevel.LIST` in `originAccessLevels` to add `s3:ListBucket` permission in the bucket policy.

This is useful to distinguish between responses blocked by WAF (403) and responses where the file does not exist (404).

```python
my_bucket = s3.Bucket(self, "myBucket")
s3_origin = origins.S3BucketOrigin.with_origin_access_control(my_bucket,
    origin_access_levels=[cloudfront.AccessLevel.READ, cloudfront.AccessLevel.LIST]
)
cloudfront.Distribution(self, "distribution",
    default_behavior=cloudfront.BehaviorOptions(
        origin=s3_origin
    ),
    default_root_object="index.html"
)
```

When the origin is associated to the default behavior, it is highly recommended to specify `defaultRootObject` distribution property.
Without it, the root path `https://xxxx.cloudfront.net/` will return the list of the S3 object keys.

#### Setting up an OAI (legacy)

Setup an S3 origin with origin access identity (legacy) as follows:

```python
my_bucket = s3.Bucket(self, "myBucket")
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(
        origin=origins.S3BucketOrigin.with_origin_access_identity(my_bucket)
    )
)
```

You can also pass in a custom S3 origin access identity:

```python
my_bucket = s3.Bucket(self, "myBucket")
my_oai = cloudfront.OriginAccessIdentity(self, "myOAI",
    comment="My custom OAI"
)
s3_origin = origins.S3BucketOrigin.with_origin_access_identity(my_bucket,
    origin_access_identity=my_oai
)
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(
        origin=s3_origin
    )
)
```

#### Setting up OAI with imported S3 buckets (legacy)

If you are using an imported bucket for your S3 Origin and want to use OAI,
you will need to update
the S3 bucket policy manually to allow the OAI to access the S3 origin. Like most imported resources, CDK apps cannot modify the configuration of imported buckets.

Add the following
policy statement to your
S3 bucket to allow the OAI read access:

```json
{
    "Version": "2012-10-17",
    "Id": "PolicyForCloudFrontPrivateContent",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity <origin access identity ID>"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<S3 bucket name>/*"
        }
    ]
}
```

See AWS docs on [Giving an origin access identity permission to read files in the Amazon S3 bucket](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#private-content-restricting-access-to-s3-oai) for more details.

### Setting up a S3 origin with no origin access control

To setup a standard S3 origin with no access control (no OAI nor OAC), use `origins.S3BucketOrigin.withBucketDefaults()`:

```python
my_bucket = s3.Bucket(self, "myBucket")
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(
        origin=origins.S3BucketOrigin.with_bucket_defaults(my_bucket)
    )
)
```

### Migrating from OAI to OAC

If you are currently using OAI for your S3 origin and wish to migrate to OAC,
replace the `S3Origin` construct (deprecated) with `S3BucketOrigin.withOriginAccessControl()` which automatically
creates and sets up an OAC for you.

Existing setup using OAI and `S3Origin`:

```python
my_bucket = s3.Bucket(self, "myBucket")
s3_origin = origins.S3Origin(my_bucket)
distribution = cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=s3_origin)
)
```

**Step 1:**

To ensure CloudFront doesn't lose access to the bucket during the transition, add a statement to bucket policy to grant OAC access to the S3 origin. Deploy the stack. If you are okay with downtime during the transition, you can skip this step.

> Tip: Run `cdk diff` before deploying to verify the
> changes to your stack.

```python
import aws_cdk as cdk
import aws_cdk.aws_iam as iam


stack = Stack()
my_bucket = s3.Bucket(self, "myBucket")
s3_origin = origins.S3Origin(my_bucket)
distribution = cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=s3_origin)
)

# Construct the bucket policy statement
distribution_arn = stack.format_arn(
    service="cloudfront",
    region="",
    resource="distribution",
    resource_name=distribution.distribution_id,
    arn_format=cdk.ArnFormat.SLASH_RESOURCE_NAME
)

cloudfront_sP = iam.ServicePrincipal("cloudfront.amazonaws.com")

oac_bucket_policy_statement = iam.PolicyStatement(
    effect=iam.Effect.ALLOW,
    principals=[cloudfront_sP],
    actions=["s3:GetObject"],
    resources=[my_bucket.arn_for_objects("*")],
    conditions={
        "StringEquals": {
            "AWS:SourceArn": distribution_arn
        }
    }
)

# Add statement to bucket policy
my_bucket.add_to_resource_policy(oac_bucket_policy_statement)
```

The following changes will take place:

1. The bucket policy will be modified to grant the CloudFront distribution access. At this point the bucket policy allows both an OAI and an OAC to access the S3 origin.

**Step 2:**

Replace `S3Origin` with `S3BucketOrigin.withOriginAccessControl()`, which creates an OAC and attaches it to the distribution. You can remove the code from Step 1 which updated the bucket policy, as `S3BucketOrigin.withOriginAccessControl()` updates the bucket policy automatically with the same statement when defined in the `Distribution` (no net difference).

Run `cdk diff` before deploying to verify the changes to your stack.

```python
bucket = s3.Bucket(self, "Bucket")
s3_origin = origins.S3BucketOrigin.with_origin_access_control(bucket)
distribution = cloudfront.Distribution(self, "Distribution",
    default_behavior=cloudfront.BehaviorOptions(origin=s3_origin)
)
```

The following changes will take place:

1. A `AWS::CloudFront::OriginAccessControl` resource will be created.
2. The `Origin` property of the `AWS::CloudFront::Distribution` will set [`OriginAccessControlId`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-origin.html#cfn-cloudfront-distribution-origin-originaccesscontrolid) to the OAC ID after it is created. It will also set [`S3OriginConfig`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-s3originconfig.html#aws-properties-cloudfront-distribution-s3originconfig-properties) to `{"OriginAccessIdentity": ""}`, which deletes the origin access identity from the existing distribution.
3. The `AWS::CloudFront::CloudFrontOriginAccessIdentity` resource will be deleted.

**Will migrating from OAI to OAC cause any resource replacement?**

No, following the migration steps does not cause any replacement of the existing `AWS::CloudFront::Distribution`, `AWS::S3::Bucket` nor `AWS::S3::BucketPolicy` resources. It will modify the bucket policy, create a `AWS::CloudFront::OriginAccessControl` resource, and delete the existing `AWS::CloudFront::CloudFrontOriginAccessIdentity`.

**Will migrating from OAI to OAC have any availability implications for my application?**

Updates to bucket policies are eventually consistent. Therefore, removing OAI permissions and setting up OAC in the same CloudFormation stack deployment is not recommended as it may cause downtime where CloudFront loses access to the bucket. Following the steps outlined above lowers the risk of downtime as the bucket policy is updated to have both OAI and OAC permissions, then in a subsequent deployment, the OAI permissions are removed.

For more information, see [Migrating from origin access identity (OAI) to origin access control (OAC)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#migrate-from-oai-to-oac).

### Adding Custom Headers

You can configure CloudFront to add custom headers to the requests that it sends to your origin. These custom headers enable you to send and gather information from your origin that you don’t get with typical viewer requests. These headers can even be customized for each origin. CloudFront supports custom headers for both for custom and Amazon S3 origins.

```python
my_bucket = s3.Bucket(self, "myBucket")
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.S3BucketOrigin.with_origin_access_control(my_bucket,
        custom_headers={
            "Foo": "bar"
        }
    ))
)
```

## ELBv2 Load Balancer

An Elastic Load Balancing (ELB) v2 load balancer may be used as an origin. In order for a load balancer to serve as an origin, it must be publicly
accessible (`internetFacing` is true). Both Application and Network load balancers are supported.

```python
# vpc: ec2.Vpc

# Create an application load balancer in a VPC. 'internetFacing' must be 'true'
# for CloudFront to access the load balancer and use it as an origin.
lb = elbv2.ApplicationLoadBalancer(self, "LB",
    vpc=vpc,
    internet_facing=True
)
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.LoadBalancerV2Origin(lb))
)
```

The origin can also be customized to respond on different ports, have different connection properties, etc.

```python
# load_balancer: elbv2.ApplicationLoadBalancer

origin = origins.LoadBalancerV2Origin(load_balancer,
    connection_attempts=3,
    connection_timeout=Duration.seconds(5),
    read_timeout=Duration.seconds(45),
    keepalive_timeout=Duration.seconds(45),
    protocol_policy=cloudfront.OriginProtocolPolicy.MATCH_VIEWER
)
```

Note that the `readTimeout` and `keepaliveTimeout` properties can extend their values over 60 seconds only if a limit increase request for CloudFront origin response timeout
quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Consider that this value is
still limited to a maximum value of 180 seconds, which is a hard limit for that quota.

## From an HTTP endpoint

Origins can also be created from any other HTTP endpoint, given the domain name, and optionally, other origin properties.

```python
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.HttpOrigin("www.example.com"))
)
```

See the documentation of `aws-cdk-lib/aws-cloudfront` for more information.

## VPC origins

You can use CloudFront to deliver content from applications that are hosted in your virtual private cloud (VPC) private subnets.
You can use Application Load Balancers (ALBs), Network Load Balancers (NLBs), and EC2 instances in private subnets as VPC origins.

Learn more about [Restrict access with VPC origins](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-vpc-origins.html).

### From an Application Load Balancer

An Application Load Balancer (ALB) can be used as a VPC origin.
It is not needed to be publicly accessible.

```python
# Creates a distribution from an Application Load Balancer
# vpc: ec2.Vpc

# Create an application load balancer in a VPC. 'internetFacing' can be 'false'.
alb = elbv2.ApplicationLoadBalancer(self, "ALB",
    vpc=vpc,
    internet_facing=False,
    vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED)
)
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.VpcOrigin.with_application_load_balancer(alb))
)
```

### From a Network Load Balancer

A Network Load Balancer (NLB) can also be use as a VPC origin.
It is not needed to be publicly accessible.

* A Network Load Balancer must have a security group attached to it.
* Dual-stack Network Load Balancers and Network Load Balancers with TLS listeners can't be added as origins.

```python
# Creates a distribution from a Network Load Balancer
# vpc: ec2.Vpc

# Create a network load balancer in a VPC. 'internetFacing' can be 'false'.
nlb = elbv2.NetworkLoadBalancer(self, "NLB",
    vpc=vpc,
    internet_facing=False,
    vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
    security_groups=[ec2.SecurityGroup(self, "NLB-SG", vpc=vpc)]
)
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.VpcOrigin.with_network_load_balancer(nlb))
)
```

### From an EC2 instance

An EC2 instance can also be used directly as a VPC origin.
It can be in a private subnet.

```python
# Creates a distribution from an EC2 instance
# vpc: ec2.Vpc

# Create an EC2 instance in a VPC. 'subnetType' can be private.
instance = ec2.Instance(self, "Instance",
    vpc=vpc,
    instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
    machine_image=ec2.MachineImage.latest_amazon_linux2023(),
    vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)
)
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.VpcOrigin.with_ec2_instance(instance))
)
```

### Restrict traffic coming to the VPC origin

You may need to update the security group for your VPC private origin (Application Load Balancer, Network Load Balancer, or EC2 instance) to explicitly allow the traffic from your VPC origins.

#### The CloudFront managed prefix list

You can allow the traffic from the CloudFront managed prefix list named **com.amazonaws.global.cloudfront.origin-facing**. For more information, see [Use an AWS-managed prefix list](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-aws-managed-prefix-lists.html#use-aws-managed-prefix-list).

```python
# alb: elbv2.ApplicationLoadBalancer


cf_origin_facing = ec2.PrefixList.from_lookup(self, "CloudFrontOriginFacing",
    prefix_list_name="com.amazonaws.global.cloudfront.origin-facing"
)
alb.connections.allow_from(cf_origin_facing, ec2.Port.HTTP)
```

#### The VPC origin service security group

VPC origin will create a security group named `CloudFront-VPCOrigins-Service-SG`.
It can be further restricted to allow only traffic from your VPC origins.

The id of the security group is not provided by CloudFormation currently.
You can retrieve it dynamically using a custom resource.

```python
import aws_cdk.custom_resources as cr

# vpc: ec2.Vpc
# distribution: cloudfront.Distribution
# alb: elbv2.ApplicationLoadBalancer


# Call ec2:DescribeSecurityGroups API to retrieve the VPC origins security group.
get_sg = cr.AwsCustomResource(self, "GetSecurityGroup",
    on_create=cr.AwsSdkCall(
        service="ec2",
        action="describeSecurityGroups",
        parameters={
            "Filters": [{"Name": "vpc-id", "Values": [vpc.vpc_id]}, {"Name": "group-name", "Values": ["CloudFront-VPCOrigins-Service-SG"]}
            ]
        },
        physical_resource_id=cr.PhysicalResourceId.of("CloudFront-VPCOrigins-Service-SG")
    ),
    policy=cr.AwsCustomResourcePolicy.from_sdk_calls(resources=["*"])
)
# The security group may be available after the distributon is deployed
get_sg.node.add_dependency(distribution)
sg_vpc_origins = ec2.SecurityGroup.from_security_group_id(self, "VpcOriginsSecurityGroup",
    get_sg.get_response_field("SecurityGroups.0.GroupId"))
# Allow connections from the security group
alb.connections.allow_from(sg_vpc_origins, ec2.Port.HTTP)
```

## Failover Origins (Origin Groups)

You can set up CloudFront with origin failover for scenarios that require high availability.
To get started, you create an origin group with two origins: a primary and a secondary.
If the primary origin is unavailable, or returns specific HTTP response status codes that indicate a failure,
CloudFront automatically switches to the secondary origin.
You achieve that behavior in the CDK using the `OriginGroup` class:

```python
my_bucket = s3.Bucket(self, "myBucket")
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(
        origin=origins.OriginGroup(
            primary_origin=origins.S3BucketOrigin.with_origin_access_control(my_bucket),
            fallback_origin=origins.HttpOrigin("www.example.com"),
            # optional, defaults to: 500, 502, 503 and 504
            fallback_status_codes=[404]
        )
    )
)
```

### Selection Criteria: Media Quality Based with AWS Elemental MediaPackageV2

You can setup your origin group to be configured for media quality based failover with your AWS Elemental MediaPackageV2 endpoints.
You can achieve this behavior in the CDK, again using the `OriginGroup` class:

```python
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(
        origin=origins.OriginGroup(
            primary_origin=origins.HttpOrigin("<AWS Elemental MediaPackageV2 origin 1>"),
            fallback_origin=origins.HttpOrigin("<AWS Elemental MediaPackageV2 origin 2>"),
            fallback_status_codes=[404],
            selection_criteria=cloudfront.OriginSelectionCriteria.MEDIA_QUALITY_BASED
        )
    )
)
```

## From an API Gateway REST API

Origins can be created from an API Gateway REST API. It is recommended to use a
[regional API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html) in this case. The origin path will automatically be set as the stage name.

```python
# api: apigateway.RestApi

cloudfront.Distribution(self, "Distribution",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.RestApiOrigin(api))
)
```

If you want to use a different origin path, you can specify it in the `originPath` property.

```python
# api: apigateway.RestApi

cloudfront.Distribution(self, "Distribution",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.RestApiOrigin(api, origin_path="/custom-origin-path"))
)
```

## From a Lambda Function URL

Lambda Function URLs enable direct invocation of Lambda functions via HTTP(S), without intermediaries. They can be set as CloudFront origins for streamlined function execution behind a CDN, leveraging caching and custom domains.

```python
import aws_cdk.aws_lambda as lambda_

# fn: lambda.Function

fn_url = fn.add_function_url(auth_type=lambda_.FunctionUrlAuthType.NONE)

cloudfront.Distribution(self, "Distribution",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.FunctionUrlOrigin(fn_url))
)
```

### Lambda Function URL with Origin Access Control (OAC)

You can configure the Lambda Function URL with Origin Access Control (OAC) for enhanced security. When using OAC with Signing SIGV4_ALWAYS, it is recommended to set the Lambda Function URL authType to AWS_IAM to ensure proper authorization.

```python
import aws_cdk.aws_lambda as lambda_
# fn: lambda.Function


fn_url = fn.add_function_url(
    auth_type=lambda_.FunctionUrlAuthType.AWS_IAM
)

cloudfront.Distribution(self, "MyDistribution",
    default_behavior=cloudfront.BehaviorOptions(
        origin=origins.FunctionUrlOrigin.with_origin_access_control(fn_url)
    )
)
```

If you want to explicitly add OAC for more customized access control, you can use the originAccessControl option as shown below.

```python
import aws_cdk.aws_lambda as lambda_
# fn: lambda.Function


fn_url = fn.add_function_url(
    auth_type=lambda_.FunctionUrlAuthType.AWS_IAM
)

# Define a custom OAC
oac = cloudfront.FunctionUrlOriginAccessControl(self, "MyOAC",
    origin_access_control_name="CustomLambdaOAC",
    signing=cloudfront.Signing.SIGV4_ALWAYS
)

# Set up Lambda Function URL with OAC in CloudFront Distribution
cloudfront.Distribution(self, "MyDistribution",
    default_behavior=cloudfront.BehaviorOptions(
        origin=origins.FunctionUrlOrigin.with_origin_access_control(fn_url,
            origin_access_control=oac
        )
    )
)
```
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import Duration as _Duration_4839e8c3
from ..aws_apigateway import RestApiBase as _RestApiBase_0431da32
from ..aws_cloudfront import (
    AccessLevel as _AccessLevel_315d9a76,
    CfnDistribution as _CfnDistribution_d9ad3595,
    IOrigin as _IOrigin_83d4c1fa,
    IOriginAccessControl as _IOriginAccessControl_82a6fe5a,
    IOriginAccessIdentity as _IOriginAccessIdentity_a922494c,
    IVpcOrigin as _IVpcOrigin_6f584d50,
    OriginBase as _OriginBase_b8fe5bcc,
    OriginBindConfig as _OriginBindConfig_25a57096,
    OriginBindOptions as _OriginBindOptions_088c2b51,
    OriginProps as _OriginProps_0675928d,
    OriginProtocolPolicy as _OriginProtocolPolicy_967ed73c,
    OriginSelectionCriteria as _OriginSelectionCriteria_ba6d3e21,
    OriginSslPolicy as _OriginSslPolicy_d65cede2,
    VpcOriginOptions as _VpcOriginOptions_f9e74bd8,
)
from ..aws_ec2 import IInstance as _IInstance_ab239e7c
from ..aws_elasticloadbalancingv2 import (
    IApplicationLoadBalancer as _IApplicationLoadBalancer_4cbd50ab,
    ILoadBalancerV2 as _ILoadBalancerV2_4c5c0fbb,
    INetworkLoadBalancer as _INetworkLoadBalancer_96e17101,
)
from ..aws_lambda import IFunctionUrl as _IFunctionUrl_1a74cd94
from ..aws_s3 import IBucket as _IBucket_42e086fd


class FunctionUrlOrigin(
    _OriginBase_b8fe5bcc,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.FunctionUrlOrigin",
):
    '''An Origin for a Lambda Function URL.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_lambda as lambda_
        # fn: lambda.Function
        
        
        fn_url = fn.add_function_url(
            auth_type=lambda_.FunctionUrlAuthType.AWS_IAM
        )
        
        cloudfront.Distribution(self, "MyDistribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.FunctionUrlOrigin.with_origin_access_control(fn_url)
            )
        )
    '''

    def __init__(
        self,
        lambda_function_url: _IFunctionUrl_1a74cd94,
        *,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param lambda_function_url: -
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcda903697b26acfe2149a285d5a64619682b675affb52f4ae2d1aca46c8f1c3)
            check_type(argname="argument lambda_function_url", value=lambda_function_url, expected_type=type_hints["lambda_function_url"])
        props = FunctionUrlOriginProps(
            keepalive_timeout=keepalive_timeout,
            read_timeout=read_timeout,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [lambda_function_url, props])

    @jsii.member(jsii_name="withOriginAccessControl")
    @builtins.classmethod
    def with_origin_access_control(
        cls,
        lambda_function_url: _IFunctionUrl_1a74cd94,
        *,
        origin_access_control: typing.Optional[_IOriginAccessControl_82a6fe5a] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> _IOrigin_83d4c1fa:
        '''Create a Lambda Function URL Origin with Origin Access Control (OAC) configured.

        :param lambda_function_url: -
        :param origin_access_control: An optional Origin Access Control. Default: - an Origin Access Control will be created.
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4d59b7721f41be7903dbcffeddd34d596392d2c8d2a4110f31a4dacdb532727)
            check_type(argname="argument lambda_function_url", value=lambda_function_url, expected_type=type_hints["lambda_function_url"])
        props = FunctionUrlOriginWithOACProps(
            origin_access_control=origin_access_control,
            keepalive_timeout=keepalive_timeout,
            read_timeout=read_timeout,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        return typing.cast(_IOrigin_83d4c1fa, jsii.sinvoke(cls, "withOriginAccessControl", [lambda_function_url, props]))

    @jsii.member(jsii_name="renderCustomOriginConfig")
    def _render_custom_origin_config(
        self,
    ) -> typing.Optional[_CfnDistribution_d9ad3595.CustomOriginConfigProperty]:
        return typing.cast(typing.Optional[_CfnDistribution_d9ad3595.CustomOriginConfigProperty], jsii.invoke(self, "renderCustomOriginConfig", []))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.FunctionUrlOriginBaseProps",
    jsii_struct_bases=[_OriginProps_0675928d],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_access_control_id": "originAccessControlId",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
    },
)
class FunctionUrlOriginBaseProps(_OriginProps_0675928d):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for configuring a origin using a standard Lambda Functions URLs.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_cloudfront_origins as cloudfront_origins
            
            function_url_origin_base_props = cloudfront_origins.FunctionUrlOriginBaseProps(
                connection_attempts=123,
                connection_timeout=cdk.Duration.minutes(30),
                custom_headers={
                    "custom_headers_key": "customHeaders"
                },
                origin_access_control_id="originAccessControlId",
                origin_id="originId",
                origin_path="originPath",
                origin_shield_enabled=False,
                origin_shield_region="originShieldRegion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__610b4764a440619f38a9adeb3e13225e58180ee2ee316abd994579fdcdb84c12)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_access_control_id", value=origin_access_control_id, expected_type=type_hints["origin_access_control_id"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_access_control_id is not None:
            self._values["origin_access_control_id"] = origin_access_control_id
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_access_control_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an origin access control for this origin.

        :default: - no origin access control
        '''
        result = self._values.get("origin_access_control_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionUrlOriginBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.FunctionUrlOriginProps",
    jsii_struct_bases=[_OriginProps_0675928d],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_access_control_id": "originAccessControlId",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "keepalive_timeout": "keepaliveTimeout",
        "read_timeout": "readTimeout",
    },
)
class FunctionUrlOriginProps(_OriginProps_0675928d):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Properties for a Lambda Function URL Origin.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_cloudfront_origins as cloudfront_origins
            
            function_url_origin_props = cloudfront_origins.FunctionUrlOriginProps(
                connection_attempts=123,
                connection_timeout=cdk.Duration.minutes(30),
                custom_headers={
                    "custom_headers_key": "customHeaders"
                },
                keepalive_timeout=cdk.Duration.minutes(30),
                origin_access_control_id="originAccessControlId",
                origin_id="originId",
                origin_path="originPath",
                origin_shield_enabled=False,
                origin_shield_region="originShieldRegion",
                read_timeout=cdk.Duration.minutes(30)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56d340a9ac5dd93c6aa22cb98bcbc860fb23f8d247b53c2cd1a51ecd8406909a)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_access_control_id", value=origin_access_control_id, expected_type=type_hints["origin_access_control_id"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument keepalive_timeout", value=keepalive_timeout, expected_type=type_hints["keepalive_timeout"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_access_control_id is not None:
            self._values["origin_access_control_id"] = origin_access_control_id
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if keepalive_timeout is not None:
            self._values["keepalive_timeout"] = keepalive_timeout
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_access_control_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an origin access control for this origin.

        :default: - no origin access control
        '''
        result = self._values.get("origin_access_control_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keepalive_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront persists its connection to the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("keepalive_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront waits for a response from the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionUrlOriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.FunctionUrlOriginWithOACProps",
    jsii_struct_bases=[FunctionUrlOriginProps],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_access_control_id": "originAccessControlId",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "keepalive_timeout": "keepaliveTimeout",
        "read_timeout": "readTimeout",
        "origin_access_control": "originAccessControl",
    },
)
class FunctionUrlOriginWithOACProps(FunctionUrlOriginProps):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_access_control: typing.Optional[_IOriginAccessControl_82a6fe5a] = None,
    ) -> None:
        '''Properties for configuring a Lambda Functions URLs with OAC.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param origin_access_control: An optional Origin Access Control. Default: - an Origin Access Control will be created.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_lambda as lambda_
            # fn: lambda.Function
            
            
            fn_url = fn.add_function_url(
                auth_type=lambda_.FunctionUrlAuthType.AWS_IAM
            )
            
            # Define a custom OAC
            oac = cloudfront.FunctionUrlOriginAccessControl(self, "MyOAC",
                origin_access_control_name="CustomLambdaOAC",
                signing=cloudfront.Signing.SIGV4_ALWAYS
            )
            
            # Set up Lambda Function URL with OAC in CloudFront Distribution
            cloudfront.Distribution(self, "MyDistribution",
                default_behavior=cloudfront.BehaviorOptions(
                    origin=origins.FunctionUrlOrigin.with_origin_access_control(fn_url,
                        origin_access_control=oac
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56968af993436ccfcac0aa6a57169f1a033078c10740d435d086816ad0336a75)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_access_control_id", value=origin_access_control_id, expected_type=type_hints["origin_access_control_id"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument keepalive_timeout", value=keepalive_timeout, expected_type=type_hints["keepalive_timeout"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
            check_type(argname="argument origin_access_control", value=origin_access_control, expected_type=type_hints["origin_access_control"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_access_control_id is not None:
            self._values["origin_access_control_id"] = origin_access_control_id
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if keepalive_timeout is not None:
            self._values["keepalive_timeout"] = keepalive_timeout
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout
        if origin_access_control is not None:
            self._values["origin_access_control"] = origin_access_control

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_access_control_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an origin access control for this origin.

        :default: - no origin access control
        '''
        result = self._values.get("origin_access_control_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keepalive_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront persists its connection to the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("keepalive_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront waits for a response from the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def origin_access_control(self) -> typing.Optional[_IOriginAccessControl_82a6fe5a]:
        '''An optional Origin Access Control.

        :default: - an Origin Access Control will be created.
        '''
        result = self._values.get("origin_access_control")
        return typing.cast(typing.Optional[_IOriginAccessControl_82a6fe5a], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionUrlOriginWithOACProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HttpOrigin(
    _OriginBase_b8fe5bcc,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.HttpOrigin",
):
    '''An Origin for an HTTP server or S3 bucket configured for website hosting.

    :exampleMetadata: infused

    Example::

        my_bucket = s3.Bucket(self, "myBucket")
        cloudfront.Distribution(self, "myDist",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.OriginGroup(
                    primary_origin=origins.S3BucketOrigin.with_origin_access_control(my_bucket),
                    fallback_origin=origins.HttpOrigin("www.example.com"),
                    # optional, defaults to: 500, 502, 503 and 504
                    fallback_status_codes=[404]
                )
            )
        )
    '''

    def __init__(
        self,
        domain_name: builtins.str,
        *,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
        protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param domain_name: -
        :param http_port: The HTTP port that CloudFront uses to connect to the origin. Default: 80
        :param https_port: The HTTPS port that CloudFront uses to connect to the origin. Default: 443
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param origin_ssl_protocols: The SSL versions to use when interacting with the origin. Default: OriginSslPolicy.TLS_V1_2
        :param protocol_policy: Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Default: OriginProtocolPolicy.HTTPS_ONLY
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57d13f69f251622e0723aa73c3eb93e482e0deb7a7b1e8439c7d7ad35cfc0cc5)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        props = HttpOriginProps(
            http_port=http_port,
            https_port=https_port,
            keepalive_timeout=keepalive_timeout,
            origin_ssl_protocols=origin_ssl_protocols,
            protocol_policy=protocol_policy,
            read_timeout=read_timeout,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [domain_name, props])

    @jsii.member(jsii_name="renderCustomOriginConfig")
    def _render_custom_origin_config(
        self,
    ) -> typing.Optional[_CfnDistribution_d9ad3595.CustomOriginConfigProperty]:
        return typing.cast(typing.Optional[_CfnDistribution_d9ad3595.CustomOriginConfigProperty], jsii.invoke(self, "renderCustomOriginConfig", []))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.HttpOriginProps",
    jsii_struct_bases=[_OriginProps_0675928d],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_access_control_id": "originAccessControlId",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "http_port": "httpPort",
        "https_port": "httpsPort",
        "keepalive_timeout": "keepaliveTimeout",
        "origin_ssl_protocols": "originSslProtocols",
        "protocol_policy": "protocolPolicy",
        "read_timeout": "readTimeout",
    },
)
class HttpOriginProps(_OriginProps_0675928d):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
        protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Properties for an Origin backed by an S3 website-configured bucket, load balancer, or custom HTTP server.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param http_port: The HTTP port that CloudFront uses to connect to the origin. Default: 80
        :param https_port: The HTTPS port that CloudFront uses to connect to the origin. Default: 443
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param origin_ssl_protocols: The SSL versions to use when interacting with the origin. Default: OriginSslPolicy.TLS_V1_2
        :param protocol_policy: Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Default: OriginProtocolPolicy.HTTPS_ONLY
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_cloudfront as cloudfront
            from aws_cdk import aws_cloudfront_origins as cloudfront_origins
            
            http_origin_props = cloudfront_origins.HttpOriginProps(
                connection_attempts=123,
                connection_timeout=cdk.Duration.minutes(30),
                custom_headers={
                    "custom_headers_key": "customHeaders"
                },
                http_port=123,
                https_port=123,
                keepalive_timeout=cdk.Duration.minutes(30),
                origin_access_control_id="originAccessControlId",
                origin_id="originId",
                origin_path="originPath",
                origin_shield_enabled=False,
                origin_shield_region="originShieldRegion",
                origin_ssl_protocols=[cloudfront.OriginSslPolicy.SSL_V3],
                protocol_policy=cloudfront.OriginProtocolPolicy.HTTP_ONLY,
                read_timeout=cdk.Duration.minutes(30)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13f43bf70f0a97ee8ca0e4f7aca38d43089ed2bc254d5c2b57c73b51c1c2b9df)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_access_control_id", value=origin_access_control_id, expected_type=type_hints["origin_access_control_id"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument http_port", value=http_port, expected_type=type_hints["http_port"])
            check_type(argname="argument https_port", value=https_port, expected_type=type_hints["https_port"])
            check_type(argname="argument keepalive_timeout", value=keepalive_timeout, expected_type=type_hints["keepalive_timeout"])
            check_type(argname="argument origin_ssl_protocols", value=origin_ssl_protocols, expected_type=type_hints["origin_ssl_protocols"])
            check_type(argname="argument protocol_policy", value=protocol_policy, expected_type=type_hints["protocol_policy"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_access_control_id is not None:
            self._values["origin_access_control_id"] = origin_access_control_id
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if http_port is not None:
            self._values["http_port"] = http_port
        if https_port is not None:
            self._values["https_port"] = https_port
        if keepalive_timeout is not None:
            self._values["keepalive_timeout"] = keepalive_timeout
        if origin_ssl_protocols is not None:
            self._values["origin_ssl_protocols"] = origin_ssl_protocols
        if protocol_policy is not None:
            self._values["protocol_policy"] = protocol_policy
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_access_control_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an origin access control for this origin.

        :default: - no origin access control
        '''
        result = self._values.get("origin_access_control_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTP port that CloudFront uses to connect to the origin.

        :default: 80
        '''
        result = self._values.get("http_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def https_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTPS port that CloudFront uses to connect to the origin.

        :default: 443
        '''
        result = self._values.get("https_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def keepalive_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront persists its connection to the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("keepalive_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def origin_ssl_protocols(
        self,
    ) -> typing.Optional[typing.List[_OriginSslPolicy_d65cede2]]:
        '''The SSL versions to use when interacting with the origin.

        :default: OriginSslPolicy.TLS_V1_2
        '''
        result = self._values.get("origin_ssl_protocols")
        return typing.cast(typing.Optional[typing.List[_OriginSslPolicy_d65cede2]], result)

    @builtins.property
    def protocol_policy(self) -> typing.Optional[_OriginProtocolPolicy_967ed73c]:
        '''Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin.

        :default: OriginProtocolPolicy.HTTPS_ONLY
        '''
        result = self._values.get("protocol_policy")
        return typing.cast(typing.Optional[_OriginProtocolPolicy_967ed73c], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpOriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerV2Origin(
    HttpOrigin,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.LoadBalancerV2Origin",
):
    '''An Origin for a v2 load balancer.

    :exampleMetadata: infused

    Example::

        # Creates a distribution from an ELBv2 load balancer
        # vpc: ec2.Vpc
        
        # Create an application load balancer in a VPC. 'internetFacing' must be 'true'
        # for CloudFront to access the load balancer and use it as an origin.
        lb = elbv2.ApplicationLoadBalancer(self, "LB",
            vpc=vpc,
            internet_facing=True
        )
        cloudfront.Distribution(self, "myDist",
            default_behavior=cloudfront.BehaviorOptions(origin=origins.LoadBalancerV2Origin(lb))
        )
    '''

    def __init__(
        self,
        load_balancer: _ILoadBalancerV2_4c5c0fbb,
        *,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
        protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param load_balancer: -
        :param http_port: The HTTP port that CloudFront uses to connect to the origin. Default: 80
        :param https_port: The HTTPS port that CloudFront uses to connect to the origin. Default: 443
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param origin_ssl_protocols: The SSL versions to use when interacting with the origin. Default: OriginSslPolicy.TLS_V1_2
        :param protocol_policy: Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Default: OriginProtocolPolicy.HTTPS_ONLY
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e5124d4f469d6539077a529c09cfba685fe4a7037b9417216b18f6ccdba96c0)
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
        props = LoadBalancerV2OriginProps(
            http_port=http_port,
            https_port=https_port,
            keepalive_timeout=keepalive_timeout,
            origin_ssl_protocols=origin_ssl_protocols,
            protocol_policy=protocol_policy,
            read_timeout=read_timeout,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [load_balancer, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.LoadBalancerV2OriginProps",
    jsii_struct_bases=[HttpOriginProps],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_access_control_id": "originAccessControlId",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "http_port": "httpPort",
        "https_port": "httpsPort",
        "keepalive_timeout": "keepaliveTimeout",
        "origin_ssl_protocols": "originSslProtocols",
        "protocol_policy": "protocolPolicy",
        "read_timeout": "readTimeout",
    },
)
class LoadBalancerV2OriginProps(HttpOriginProps):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
        protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Properties for an Origin backed by a v2 load balancer.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param http_port: The HTTP port that CloudFront uses to connect to the origin. Default: 80
        :param https_port: The HTTPS port that CloudFront uses to connect to the origin. Default: 443
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param origin_ssl_protocols: The SSL versions to use when interacting with the origin. Default: OriginSslPolicy.TLS_V1_2
        :param protocol_policy: Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Default: OriginProtocolPolicy.HTTPS_ONLY
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)

        :exampleMetadata: infused

        Example::

            # load_balancer: elbv2.ApplicationLoadBalancer
            
            origin = origins.LoadBalancerV2Origin(load_balancer,
                connection_attempts=3,
                connection_timeout=Duration.seconds(5),
                read_timeout=Duration.seconds(45),
                keepalive_timeout=Duration.seconds(45),
                protocol_policy=cloudfront.OriginProtocolPolicy.MATCH_VIEWER
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c72b63200b184ae3f51c9b6a19be2eef9bddae313ee00c7378396c0dcf586887)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_access_control_id", value=origin_access_control_id, expected_type=type_hints["origin_access_control_id"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument http_port", value=http_port, expected_type=type_hints["http_port"])
            check_type(argname="argument https_port", value=https_port, expected_type=type_hints["https_port"])
            check_type(argname="argument keepalive_timeout", value=keepalive_timeout, expected_type=type_hints["keepalive_timeout"])
            check_type(argname="argument origin_ssl_protocols", value=origin_ssl_protocols, expected_type=type_hints["origin_ssl_protocols"])
            check_type(argname="argument protocol_policy", value=protocol_policy, expected_type=type_hints["protocol_policy"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_access_control_id is not None:
            self._values["origin_access_control_id"] = origin_access_control_id
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if http_port is not None:
            self._values["http_port"] = http_port
        if https_port is not None:
            self._values["https_port"] = https_port
        if keepalive_timeout is not None:
            self._values["keepalive_timeout"] = keepalive_timeout
        if origin_ssl_protocols is not None:
            self._values["origin_ssl_protocols"] = origin_ssl_protocols
        if protocol_policy is not None:
            self._values["protocol_policy"] = protocol_policy
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_access_control_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an origin access control for this origin.

        :default: - no origin access control
        '''
        result = self._values.get("origin_access_control_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTP port that CloudFront uses to connect to the origin.

        :default: 80
        '''
        result = self._values.get("http_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def https_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTPS port that CloudFront uses to connect to the origin.

        :default: 443
        '''
        result = self._values.get("https_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def keepalive_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront persists its connection to the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("keepalive_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def origin_ssl_protocols(
        self,
    ) -> typing.Optional[typing.List[_OriginSslPolicy_d65cede2]]:
        '''The SSL versions to use when interacting with the origin.

        :default: OriginSslPolicy.TLS_V1_2
        '''
        result = self._values.get("origin_ssl_protocols")
        return typing.cast(typing.Optional[typing.List[_OriginSslPolicy_d65cede2]], result)

    @builtins.property
    def protocol_policy(self) -> typing.Optional[_OriginProtocolPolicy_967ed73c]:
        '''Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin.

        :default: OriginProtocolPolicy.HTTPS_ONLY
        '''
        result = self._values.get("protocol_policy")
        return typing.cast(typing.Optional[_OriginProtocolPolicy_967ed73c], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerV2OriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IOrigin_83d4c1fa)
class OriginGroup(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.OriginGroup",
):
    '''An Origin that represents a group.

    Consists of a primary Origin,
    and a fallback Origin called when the primary returns one of the provided HTTP status codes.

    :exampleMetadata: infused

    Example::

        my_bucket = s3.Bucket(self, "myBucket")
        cloudfront.Distribution(self, "myDist",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.OriginGroup(
                    primary_origin=origins.S3BucketOrigin.with_origin_access_control(my_bucket),
                    fallback_origin=origins.HttpOrigin("www.example.com"),
                    # optional, defaults to: 500, 502, 503 and 504
                    fallback_status_codes=[404]
                )
            )
        )
    '''

    def __init__(
        self,
        *,
        fallback_origin: _IOrigin_83d4c1fa,
        primary_origin: _IOrigin_83d4c1fa,
        fallback_status_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        selection_criteria: typing.Optional[_OriginSelectionCriteria_ba6d3e21] = None,
    ) -> None:
        '''
        :param fallback_origin: The fallback origin that should serve requests when the primary fails.
        :param primary_origin: The primary origin that should serve requests for this group.
        :param fallback_status_codes: The list of HTTP status codes that, when returned from the primary origin, would cause querying the fallback origin. Default: - 500, 502, 503 and 504
        :param selection_criteria: The selection criteria for the origin group. Default: - OriginSelectionCriteria.DEFAULT
        '''
        props = OriginGroupProps(
            fallback_origin=fallback_origin,
            primary_origin=primary_origin,
            fallback_status_codes=fallback_status_codes,
            selection_criteria=selection_criteria,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        *,
        origin_id: builtins.str,
        distribution_id: typing.Optional[builtins.str] = None,
    ) -> _OriginBindConfig_25a57096:
        '''The method called when a given Origin is added (for the first time) to a Distribution.

        :param scope: -
        :param origin_id: The identifier of this Origin, as assigned by the Distribution this Origin has been used added to.
        :param distribution_id: The identifier of the Distribution this Origin is used for. This is used to grant origin access permissions to the distribution for origin access control. Default: - no distribution id
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__428f309ea8c48c002d77db24802c77164c9607d40492e08c4b243080f941ff61)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        options = _OriginBindOptions_088c2b51(
            origin_id=origin_id, distribution_id=distribution_id
        )

        return typing.cast(_OriginBindConfig_25a57096, jsii.invoke(self, "bind", [scope, options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.OriginGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "fallback_origin": "fallbackOrigin",
        "primary_origin": "primaryOrigin",
        "fallback_status_codes": "fallbackStatusCodes",
        "selection_criteria": "selectionCriteria",
    },
)
class OriginGroupProps:
    def __init__(
        self,
        *,
        fallback_origin: _IOrigin_83d4c1fa,
        primary_origin: _IOrigin_83d4c1fa,
        fallback_status_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
        selection_criteria: typing.Optional[_OriginSelectionCriteria_ba6d3e21] = None,
    ) -> None:
        '''Construction properties for ``OriginGroup``.

        :param fallback_origin: The fallback origin that should serve requests when the primary fails.
        :param primary_origin: The primary origin that should serve requests for this group.
        :param fallback_status_codes: The list of HTTP status codes that, when returned from the primary origin, would cause querying the fallback origin. Default: - 500, 502, 503 and 504
        :param selection_criteria: The selection criteria for the origin group. Default: - OriginSelectionCriteria.DEFAULT

        :exampleMetadata: infused

        Example::

            my_bucket = s3.Bucket(self, "myBucket")
            cloudfront.Distribution(self, "myDist",
                default_behavior=cloudfront.BehaviorOptions(
                    origin=origins.OriginGroup(
                        primary_origin=origins.S3BucketOrigin.with_origin_access_control(my_bucket),
                        fallback_origin=origins.HttpOrigin("www.example.com"),
                        # optional, defaults to: 500, 502, 503 and 504
                        fallback_status_codes=[404]
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d6baf80fcac5a22fc2c985c83f9022e23b11075b338c076ac86172fff7d7e8b)
            check_type(argname="argument fallback_origin", value=fallback_origin, expected_type=type_hints["fallback_origin"])
            check_type(argname="argument primary_origin", value=primary_origin, expected_type=type_hints["primary_origin"])
            check_type(argname="argument fallback_status_codes", value=fallback_status_codes, expected_type=type_hints["fallback_status_codes"])
            check_type(argname="argument selection_criteria", value=selection_criteria, expected_type=type_hints["selection_criteria"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fallback_origin": fallback_origin,
            "primary_origin": primary_origin,
        }
        if fallback_status_codes is not None:
            self._values["fallback_status_codes"] = fallback_status_codes
        if selection_criteria is not None:
            self._values["selection_criteria"] = selection_criteria

    @builtins.property
    def fallback_origin(self) -> _IOrigin_83d4c1fa:
        '''The fallback origin that should serve requests when the primary fails.'''
        result = self._values.get("fallback_origin")
        assert result is not None, "Required property 'fallback_origin' is missing"
        return typing.cast(_IOrigin_83d4c1fa, result)

    @builtins.property
    def primary_origin(self) -> _IOrigin_83d4c1fa:
        '''The primary origin that should serve requests for this group.'''
        result = self._values.get("primary_origin")
        assert result is not None, "Required property 'primary_origin' is missing"
        return typing.cast(_IOrigin_83d4c1fa, result)

    @builtins.property
    def fallback_status_codes(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''The list of HTTP status codes that, when returned from the primary origin, would cause querying the fallback origin.

        :default: - 500, 502, 503 and 504
        '''
        result = self._values.get("fallback_status_codes")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def selection_criteria(self) -> typing.Optional[_OriginSelectionCriteria_ba6d3e21]:
        '''The selection criteria for the origin group.

        :default: - OriginSelectionCriteria.DEFAULT

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html#concept_origin_groups.creating
        '''
        result = self._values.get("selection_criteria")
        return typing.cast(typing.Optional[_OriginSelectionCriteria_ba6d3e21], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OriginGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RestApiOrigin(
    _OriginBase_b8fe5bcc,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.RestApiOrigin",
):
    '''An Origin for an API Gateway REST API.

    :exampleMetadata: infused

    Example::

        # api: apigateway.RestApi
        
        cloudfront.Distribution(self, "Distribution",
            default_behavior=cloudfront.BehaviorOptions(origin=origins.RestApiOrigin(api))
        )
    '''

    def __init__(
        self,
        rest_api: _RestApiBase_0431da32,
        *,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param rest_api: -
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56b6a9ee9b4e8ac821a25cc86fc2ff9f7490081ff9a35a5c551216af6a6ab722)
            check_type(argname="argument rest_api", value=rest_api, expected_type=type_hints["rest_api"])
        props = RestApiOriginProps(
            keepalive_timeout=keepalive_timeout,
            read_timeout=read_timeout,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [rest_api, props])

    @jsii.member(jsii_name="renderCustomOriginConfig")
    def _render_custom_origin_config(
        self,
    ) -> typing.Optional[_CfnDistribution_d9ad3595.CustomOriginConfigProperty]:
        return typing.cast(typing.Optional[_CfnDistribution_d9ad3595.CustomOriginConfigProperty], jsii.invoke(self, "renderCustomOriginConfig", []))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.RestApiOriginProps",
    jsii_struct_bases=[_OriginProps_0675928d],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_access_control_id": "originAccessControlId",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "keepalive_timeout": "keepaliveTimeout",
        "read_timeout": "readTimeout",
    },
)
class RestApiOriginProps(_OriginProps_0675928d):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Properties for an Origin for an API Gateway REST API.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)

        :exampleMetadata: infused

        Example::

            # api: apigateway.RestApi
            
            cloudfront.Distribution(self, "Distribution",
                default_behavior=cloudfront.BehaviorOptions(origin=origins.RestApiOrigin(api, origin_path="/custom-origin-path"))
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eca8c8f76c90eb80c45563b1a8eb9b9f1868ad621b45412a4cb935297b4d303)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_access_control_id", value=origin_access_control_id, expected_type=type_hints["origin_access_control_id"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument keepalive_timeout", value=keepalive_timeout, expected_type=type_hints["keepalive_timeout"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_access_control_id is not None:
            self._values["origin_access_control_id"] = origin_access_control_id
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if keepalive_timeout is not None:
            self._values["keepalive_timeout"] = keepalive_timeout
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_access_control_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an origin access control for this origin.

        :default: - no origin access control
        '''
        result = self._values.get("origin_access_control_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keepalive_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront persists its connection to the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("keepalive_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RestApiOriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3BucketOrigin(
    _OriginBase_b8fe5bcc,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.S3BucketOrigin",
):
    '''A S3 Bucket Origin.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_kms as kms
        
        
        my_kms_key = kms.Key(self, "myKMSKey")
        my_bucket = s3.Bucket(self, "mySSEKMSEncryptedBucket",
            encryption=s3.BucketEncryption.KMS,
            encryption_key=my_kms_key,
            object_ownership=s3.ObjectOwnership.BUCKET_OWNER_ENFORCED
        )
        cloudfront.Distribution(self, "myDist",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3BucketOrigin.with_origin_access_control(my_bucket)
            )
        )
    '''

    def __init__(
        self,
        bucket: _IBucket_42e086fd,
        *,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: -
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cb1f0b82603224c7fbeb25b954355d9b19c8971c1f19cce6cc99b4579024f0f)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        props = S3BucketOriginBaseProps(
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [bucket, props])

    @jsii.member(jsii_name="withBucketDefaults")
    @builtins.classmethod
    def with_bucket_defaults(
        cls,
        bucket: _IBucket_42e086fd,
        *,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> _IOrigin_83d4c1fa:
        '''Create a S3 Origin with default S3 bucket settings (no origin access control).

        :param bucket: -
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f676436dc530972f0e77d574f148913989a94d38c9af09bff28450e29ace8acb)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        props = _OriginProps_0675928d(
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        return typing.cast(_IOrigin_83d4c1fa, jsii.sinvoke(cls, "withBucketDefaults", [bucket, props]))

    @jsii.member(jsii_name="withOriginAccessControl")
    @builtins.classmethod
    def with_origin_access_control(
        cls,
        bucket: _IBucket_42e086fd,
        *,
        origin_access_control: typing.Optional[_IOriginAccessControl_82a6fe5a] = None,
        origin_access_levels: typing.Optional[typing.Sequence[_AccessLevel_315d9a76]] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> _IOrigin_83d4c1fa:
        '''Create a S3 Origin with Origin Access Control (OAC) configured.

        :param bucket: -
        :param origin_access_control: An optional Origin Access Control. Default: - an Origin Access Control will be created.
        :param origin_access_levels: The level of permissions granted in the bucket policy and key policy (if applicable) to the CloudFront distribution. Default: [AccessLevel.READ]
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23afb965139dc34be23cec3ad5506b4c5de509db9c0d653bed7877f463b7a9db)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        props = S3BucketOriginWithOACProps(
            origin_access_control=origin_access_control,
            origin_access_levels=origin_access_levels,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        return typing.cast(_IOrigin_83d4c1fa, jsii.sinvoke(cls, "withOriginAccessControl", [bucket, props]))

    @jsii.member(jsii_name="withOriginAccessIdentity")
    @builtins.classmethod
    def with_origin_access_identity(
        cls,
        bucket: _IBucket_42e086fd,
        *,
        origin_access_identity: typing.Optional[_IOriginAccessIdentity_a922494c] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> _IOrigin_83d4c1fa:
        '''Create a S3 Origin with Origin Access Identity (OAI) configured OAI is a legacy feature and we **strongly** recommend you to use OAC via ``withOriginAccessControl()`` unless it is not supported in your required region (e.g. China regions).

        :param bucket: -
        :param origin_access_identity: An optional Origin Access Identity. Default: - an Origin Access Identity will be created.
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13e7421c65d5fbb92fc686fa854daca3e90dc002f3e99da4b4757e32e3c4105d)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        props = S3BucketOriginWithOAIProps(
            origin_access_identity=origin_access_identity,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        return typing.cast(_IOrigin_83d4c1fa, jsii.sinvoke(cls, "withOriginAccessIdentity", [bucket, props]))

    @jsii.member(jsii_name="renderS3OriginConfig")
    def _render_s3_origin_config(
        self,
    ) -> typing.Optional[_CfnDistribution_d9ad3595.S3OriginConfigProperty]:
        return typing.cast(typing.Optional[_CfnDistribution_d9ad3595.S3OriginConfigProperty], jsii.invoke(self, "renderS3OriginConfig", []))


class _S3BucketOriginProxy(
    S3BucketOrigin,
    jsii.proxy_for(_OriginBase_b8fe5bcc), # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, S3BucketOrigin).__jsii_proxy_class__ = lambda : _S3BucketOriginProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.S3BucketOriginBaseProps",
    jsii_struct_bases=[_OriginProps_0675928d],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_access_control_id": "originAccessControlId",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
    },
)
class S3BucketOriginBaseProps(_OriginProps_0675928d):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for configuring a origin using a standard S3 bucket.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_cloudfront_origins as cloudfront_origins
            
            s3_bucket_origin_base_props = cloudfront_origins.S3BucketOriginBaseProps(
                connection_attempts=123,
                connection_timeout=cdk.Duration.minutes(30),
                custom_headers={
                    "custom_headers_key": "customHeaders"
                },
                origin_access_control_id="originAccessControlId",
                origin_id="originId",
                origin_path="originPath",
                origin_shield_enabled=False,
                origin_shield_region="originShieldRegion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5e580c31fe629b713e1ecbf9905ebb4220e152805ab34129f693f2c4d4db098)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_access_control_id", value=origin_access_control_id, expected_type=type_hints["origin_access_control_id"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_access_control_id is not None:
            self._values["origin_access_control_id"] = origin_access_control_id
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_access_control_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an origin access control for this origin.

        :default: - no origin access control
        '''
        result = self._values.get("origin_access_control_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketOriginBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.S3BucketOriginWithOACProps",
    jsii_struct_bases=[S3BucketOriginBaseProps],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_access_control_id": "originAccessControlId",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "origin_access_control": "originAccessControl",
        "origin_access_levels": "originAccessLevels",
    },
)
class S3BucketOriginWithOACProps(S3BucketOriginBaseProps):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        origin_access_control: typing.Optional[_IOriginAccessControl_82a6fe5a] = None,
        origin_access_levels: typing.Optional[typing.Sequence[_AccessLevel_315d9a76]] = None,
    ) -> None:
        '''Properties for configuring a S3 origin with OAC.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param origin_access_control: An optional Origin Access Control. Default: - an Origin Access Control will be created.
        :param origin_access_levels: The level of permissions granted in the bucket policy and key policy (if applicable) to the CloudFront distribution. Default: [AccessLevel.READ]

        :exampleMetadata: infused

        Example::

            my_bucket = s3.Bucket(self, "myBucket")
            oac = cloudfront.S3OriginAccessControl(self, "MyOAC",
                signing=cloudfront.Signing.SIGV4_NO_OVERRIDE
            )
            s3_origin = origins.S3BucketOrigin.with_origin_access_control(my_bucket,
                origin_access_control=oac
            )
            cloudfront.Distribution(self, "myDist",
                default_behavior=cloudfront.BehaviorOptions(
                    origin=s3_origin
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1af53a7ded1427e29cc874af45efdfe026a0004a1f2782a5bc936dbfcb4fe7a4)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_access_control_id", value=origin_access_control_id, expected_type=type_hints["origin_access_control_id"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument origin_access_control", value=origin_access_control, expected_type=type_hints["origin_access_control"])
            check_type(argname="argument origin_access_levels", value=origin_access_levels, expected_type=type_hints["origin_access_levels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_access_control_id is not None:
            self._values["origin_access_control_id"] = origin_access_control_id
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if origin_access_control is not None:
            self._values["origin_access_control"] = origin_access_control
        if origin_access_levels is not None:
            self._values["origin_access_levels"] = origin_access_levels

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_access_control_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an origin access control for this origin.

        :default: - no origin access control
        '''
        result = self._values.get("origin_access_control_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_access_control(self) -> typing.Optional[_IOriginAccessControl_82a6fe5a]:
        '''An optional Origin Access Control.

        :default: - an Origin Access Control will be created.
        '''
        result = self._values.get("origin_access_control")
        return typing.cast(typing.Optional[_IOriginAccessControl_82a6fe5a], result)

    @builtins.property
    def origin_access_levels(
        self,
    ) -> typing.Optional[typing.List[_AccessLevel_315d9a76]]:
        '''The level of permissions granted in the bucket policy and key policy (if applicable) to the CloudFront distribution.

        :default: [AccessLevel.READ]
        '''
        result = self._values.get("origin_access_levels")
        return typing.cast(typing.Optional[typing.List[_AccessLevel_315d9a76]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketOriginWithOACProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.S3BucketOriginWithOAIProps",
    jsii_struct_bases=[S3BucketOriginBaseProps],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_access_control_id": "originAccessControlId",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "origin_access_identity": "originAccessIdentity",
    },
)
class S3BucketOriginWithOAIProps(S3BucketOriginBaseProps):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        origin_access_identity: typing.Optional[_IOriginAccessIdentity_a922494c] = None,
    ) -> None:
        '''Properties for configuring a S3 origin with OAI.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param origin_access_identity: An optional Origin Access Identity. Default: - an Origin Access Identity will be created.

        :exampleMetadata: infused

        Example::

            my_bucket = s3.Bucket(self, "myBucket")
            my_oai = cloudfront.OriginAccessIdentity(self, "myOAI",
                comment="My custom OAI"
            )
            s3_origin = origins.S3BucketOrigin.with_origin_access_identity(my_bucket,
                origin_access_identity=my_oai
            )
            cloudfront.Distribution(self, "myDist",
                default_behavior=cloudfront.BehaviorOptions(
                    origin=s3_origin
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b64c18ef31b660c450eee84b6738d7bbd960797e1788e068be9663127832c26)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_access_control_id", value=origin_access_control_id, expected_type=type_hints["origin_access_control_id"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument origin_access_identity", value=origin_access_identity, expected_type=type_hints["origin_access_identity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_access_control_id is not None:
            self._values["origin_access_control_id"] = origin_access_control_id
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if origin_access_identity is not None:
            self._values["origin_access_identity"] = origin_access_identity

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_access_control_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an origin access control for this origin.

        :default: - no origin access control
        '''
        result = self._values.get("origin_access_control_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_access_identity(
        self,
    ) -> typing.Optional[_IOriginAccessIdentity_a922494c]:
        '''An optional Origin Access Identity.

        :default: - an Origin Access Identity will be created.
        '''
        result = self._values.get("origin_access_identity")
        return typing.cast(typing.Optional[_IOriginAccessIdentity_a922494c], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketOriginWithOAIProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IOrigin_83d4c1fa)
class S3Origin(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.S3Origin",
):
    '''(deprecated) An Origin that is backed by an S3 bucket.

    If the bucket is configured for website hosting, this origin will be configured to use the bucket as an
    HTTP server origin and will use the bucket's configured website redirects and error handling. Otherwise,
    the origin is created as a bucket origin and will use CloudFront's redirect and error handling.

    :deprecated: Use ``S3BucketOrigin`` or ``S3StaticWebsiteOrigin`` instead.

    :stability: deprecated
    :exampleMetadata: infused

    Example::

        # s3_bucket: s3.Bucket
        # Add a cloudfront Function to a Distribution
        cf_function = cloudfront.Function(self, "Function",
            code=cloudfront.FunctionCode.from_inline("function handler(event) { return event.request }"),
            runtime=cloudfront.FunctionRuntime.JS_2_0
        )
        cloudfront.Distribution(self, "distro",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(s3_bucket),
                function_associations=[cloudfront.FunctionAssociation(
                    function=cf_function,
                    event_type=cloudfront.FunctionEventType.VIEWER_REQUEST
                )]
            )
        )
    '''

    def __init__(
        self,
        bucket: _IBucket_42e086fd,
        *,
        origin_access_identity: typing.Optional[_IOriginAccessIdentity_a922494c] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: -
        :param origin_access_identity: An optional Origin Access Identity of the origin identity cloudfront will use when calling your s3 bucket. Default: - An Origin Access Identity will be created.
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ba8623373b0faa9ac55c816167da21a58e0753e0dd032b1f3e6ccd0bd977994)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        props = S3OriginProps(
            origin_access_identity=origin_access_identity,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [bucket, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        *,
        origin_id: builtins.str,
        distribution_id: typing.Optional[builtins.str] = None,
    ) -> _OriginBindConfig_25a57096:
        '''(deprecated) The method called when a given Origin is added (for the first time) to a Distribution.

        :param scope: -
        :param origin_id: The identifier of this Origin, as assigned by the Distribution this Origin has been used added to.
        :param distribution_id: The identifier of the Distribution this Origin is used for. This is used to grant origin access permissions to the distribution for origin access control. Default: - no distribution id

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1731b0d7a385b196730b287be11e2cb13fa03d064ae3ffbfd55c5422a8f2c430)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        options = _OriginBindOptions_088c2b51(
            origin_id=origin_id, distribution_id=distribution_id
        )

        return typing.cast(_OriginBindConfig_25a57096, jsii.invoke(self, "bind", [scope, options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.S3OriginProps",
    jsii_struct_bases=[_OriginProps_0675928d],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_access_control_id": "originAccessControlId",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "origin_access_identity": "originAccessIdentity",
    },
)
class S3OriginProps(_OriginProps_0675928d):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        origin_access_identity: typing.Optional[_IOriginAccessIdentity_a922494c] = None,
    ) -> None:
        '''Properties to use to customize an S3 Origin.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param origin_access_identity: An optional Origin Access Identity of the origin identity cloudfront will use when calling your s3 bucket. Default: - An Origin Access Identity will be created.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_cloudfront as cloudfront
            from aws_cdk import aws_cloudfront_origins as cloudfront_origins
            
            # origin_access_identity: cloudfront.OriginAccessIdentity
            
            s3_origin_props = cloudfront_origins.S3OriginProps(
                connection_attempts=123,
                connection_timeout=cdk.Duration.minutes(30),
                custom_headers={
                    "custom_headers_key": "customHeaders"
                },
                origin_access_control_id="originAccessControlId",
                origin_access_identity=origin_access_identity,
                origin_id="originId",
                origin_path="originPath",
                origin_shield_enabled=False,
                origin_shield_region="originShieldRegion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbd2a0ca1bf4d32899d90ea633e3ac416a6fa29972ee055a5866ec269b24307e)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_access_control_id", value=origin_access_control_id, expected_type=type_hints["origin_access_control_id"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument origin_access_identity", value=origin_access_identity, expected_type=type_hints["origin_access_identity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_access_control_id is not None:
            self._values["origin_access_control_id"] = origin_access_control_id
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if origin_access_identity is not None:
            self._values["origin_access_identity"] = origin_access_identity

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_access_control_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an origin access control for this origin.

        :default: - no origin access control
        '''
        result = self._values.get("origin_access_control_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_access_identity(
        self,
    ) -> typing.Optional[_IOriginAccessIdentity_a922494c]:
        '''An optional Origin Access Identity of the origin identity cloudfront will use when calling your s3 bucket.

        :default: - An Origin Access Identity will be created.
        '''
        result = self._values.get("origin_access_identity")
        return typing.cast(typing.Optional[_IOriginAccessIdentity_a922494c], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3OriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3StaticWebsiteOrigin(
    HttpOrigin,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.S3StaticWebsiteOrigin",
):
    '''An Origin for a S3 bucket configured as a website endpoint.

    :exampleMetadata: infused

    Example::

        my_bucket = s3.Bucket(self, "myBucket")
        cloudfront.Distribution(self, "myDist",
            default_behavior=cloudfront.BehaviorOptions(origin=origins.S3StaticWebsiteOrigin(my_bucket))
        )
    '''

    def __init__(
        self,
        bucket: _IBucket_42e086fd,
        *,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
        protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: -
        :param http_port: The HTTP port that CloudFront uses to connect to the origin. Default: 80
        :param https_port: The HTTPS port that CloudFront uses to connect to the origin. Default: 443
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param origin_ssl_protocols: The SSL versions to use when interacting with the origin. Default: OriginSslPolicy.TLS_V1_2
        :param protocol_policy: Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Default: OriginProtocolPolicy.HTTPS_ONLY
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0edd2083352b96faf3ea9eb05136629dff841fa272ecdb6dfb52772a77b9b22)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        props = S3StaticWebsiteOriginProps(
            http_port=http_port,
            https_port=https_port,
            keepalive_timeout=keepalive_timeout,
            origin_ssl_protocols=origin_ssl_protocols,
            protocol_policy=protocol_policy,
            read_timeout=read_timeout,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [bucket, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.S3StaticWebsiteOriginProps",
    jsii_struct_bases=[HttpOriginProps],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_access_control_id": "originAccessControlId",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "http_port": "httpPort",
        "https_port": "httpsPort",
        "keepalive_timeout": "keepaliveTimeout",
        "origin_ssl_protocols": "originSslProtocols",
        "protocol_policy": "protocolPolicy",
        "read_timeout": "readTimeout",
    },
)
class S3StaticWebsiteOriginProps(HttpOriginProps):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
        protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Properties for configuring a origin using a S3 bucket configured as a website endpoint.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param http_port: The HTTP port that CloudFront uses to connect to the origin. Default: 80
        :param https_port: The HTTPS port that CloudFront uses to connect to the origin. Default: 443
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param origin_ssl_protocols: The SSL versions to use when interacting with the origin. Default: OriginSslPolicy.TLS_V1_2
        :param protocol_policy: Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Default: OriginProtocolPolicy.HTTPS_ONLY
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_cloudfront as cloudfront
            from aws_cdk import aws_cloudfront_origins as cloudfront_origins
            
            s3_static_website_origin_props = cloudfront_origins.S3StaticWebsiteOriginProps(
                connection_attempts=123,
                connection_timeout=cdk.Duration.minutes(30),
                custom_headers={
                    "custom_headers_key": "customHeaders"
                },
                http_port=123,
                https_port=123,
                keepalive_timeout=cdk.Duration.minutes(30),
                origin_access_control_id="originAccessControlId",
                origin_id="originId",
                origin_path="originPath",
                origin_shield_enabled=False,
                origin_shield_region="originShieldRegion",
                origin_ssl_protocols=[cloudfront.OriginSslPolicy.SSL_V3],
                protocol_policy=cloudfront.OriginProtocolPolicy.HTTP_ONLY,
                read_timeout=cdk.Duration.minutes(30)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bc18cdba7c0e6d7d0a68d2a1cf3c3f91f50a7e3e7384f5f62ebee6006adbb85)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_access_control_id", value=origin_access_control_id, expected_type=type_hints["origin_access_control_id"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument http_port", value=http_port, expected_type=type_hints["http_port"])
            check_type(argname="argument https_port", value=https_port, expected_type=type_hints["https_port"])
            check_type(argname="argument keepalive_timeout", value=keepalive_timeout, expected_type=type_hints["keepalive_timeout"])
            check_type(argname="argument origin_ssl_protocols", value=origin_ssl_protocols, expected_type=type_hints["origin_ssl_protocols"])
            check_type(argname="argument protocol_policy", value=protocol_policy, expected_type=type_hints["protocol_policy"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_access_control_id is not None:
            self._values["origin_access_control_id"] = origin_access_control_id
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if http_port is not None:
            self._values["http_port"] = http_port
        if https_port is not None:
            self._values["https_port"] = https_port
        if keepalive_timeout is not None:
            self._values["keepalive_timeout"] = keepalive_timeout
        if origin_ssl_protocols is not None:
            self._values["origin_ssl_protocols"] = origin_ssl_protocols
        if protocol_policy is not None:
            self._values["protocol_policy"] = protocol_policy
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_access_control_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an origin access control for this origin.

        :default: - no origin access control
        '''
        result = self._values.get("origin_access_control_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTP port that CloudFront uses to connect to the origin.

        :default: 80
        '''
        result = self._values.get("http_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def https_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTPS port that CloudFront uses to connect to the origin.

        :default: 443
        '''
        result = self._values.get("https_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def keepalive_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront persists its connection to the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("keepalive_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def origin_ssl_protocols(
        self,
    ) -> typing.Optional[typing.List[_OriginSslPolicy_d65cede2]]:
        '''The SSL versions to use when interacting with the origin.

        :default: OriginSslPolicy.TLS_V1_2
        '''
        result = self._values.get("origin_ssl_protocols")
        return typing.cast(typing.Optional[typing.List[_OriginSslPolicy_d65cede2]], result)

    @builtins.property
    def protocol_policy(self) -> typing.Optional[_OriginProtocolPolicy_967ed73c]:
        '''Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin.

        :default: OriginProtocolPolicy.HTTPS_ONLY
        '''
        result = self._values.get("protocol_policy")
        return typing.cast(typing.Optional[_OriginProtocolPolicy_967ed73c], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3StaticWebsiteOriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpcOrigin(
    _OriginBase_b8fe5bcc,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.VpcOrigin",
):
    '''Represents a distribution's VPC origin.

    :exampleMetadata: infused

    Example::

        # Creates a distribution from a Network Load Balancer
        # vpc: ec2.Vpc
        
        # Create a network load balancer in a VPC. 'internetFacing' can be 'false'.
        nlb = elbv2.NetworkLoadBalancer(self, "NLB",
            vpc=vpc,
            internet_facing=False,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            security_groups=[ec2.SecurityGroup(self, "NLB-SG", vpc=vpc)]
        )
        cloudfront.Distribution(self, "myDist",
            default_behavior=cloudfront.BehaviorOptions(origin=origins.VpcOrigin.with_network_load_balancer(nlb))
        )
    '''

    def __init__(
        self,
        domain_name_: builtins.str,
        *,
        domain_name: typing.Optional[builtins.str] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param domain_name_: -
        :param domain_name: The domain name associated with your VPC origin. Default: - The default domain name of the endpoint.
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27d66442a972110883cdde622df199c2db6a7264e19031f1118d7aa01681cef6)
            check_type(argname="argument domain_name_", value=domain_name_, expected_type=type_hints["domain_name_"])
        props = VpcOriginProps(
            domain_name=domain_name,
            keepalive_timeout=keepalive_timeout,
            read_timeout=read_timeout,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [domain_name_, props])

    @jsii.member(jsii_name="withApplicationLoadBalancer")
    @builtins.classmethod
    def with_application_load_balancer(
        cls,
        alb: _IApplicationLoadBalancer_4cbd50ab,
        *,
        domain_name: typing.Optional[builtins.str] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
        protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
        vpc_origin_name: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> "VpcOrigin":
        '''Create a VPC origin with an Application Load Balancer.

        :param alb: -
        :param domain_name: The domain name associated with your VPC origin. Default: - The default domain name of the endpoint.
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param http_port: The HTTP port for the CloudFront VPC origin endpoint configuration. Default: 80
        :param https_port: The HTTPS port of the CloudFront VPC origin endpoint configuration. Default: 443
        :param origin_ssl_protocols: A list that contains allowed SSL/TLS protocols for this distribution. Default: - TLSv1.2
        :param protocol_policy: The origin protocol policy for the CloudFront VPC origin endpoint configuration. Default: OriginProtocolPolicy.MATCH_VIEWER
        :param vpc_origin_name: The name of the CloudFront VPC origin endpoint configuration. Default: - generated from the ``id``
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8615ead9bb90a8fd2c91dc07371d03b8f4b4192a1500a449646bd8a7be95fa6c)
            check_type(argname="argument alb", value=alb, expected_type=type_hints["alb"])
        props = VpcOriginWithEndpointProps(
            domain_name=domain_name,
            keepalive_timeout=keepalive_timeout,
            read_timeout=read_timeout,
            http_port=http_port,
            https_port=https_port,
            origin_ssl_protocols=origin_ssl_protocols,
            protocol_policy=protocol_policy,
            vpc_origin_name=vpc_origin_name,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        return typing.cast("VpcOrigin", jsii.sinvoke(cls, "withApplicationLoadBalancer", [alb, props]))

    @jsii.member(jsii_name="withEc2Instance")
    @builtins.classmethod
    def with_ec2_instance(
        cls,
        instance: _IInstance_ab239e7c,
        *,
        domain_name: typing.Optional[builtins.str] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
        protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
        vpc_origin_name: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> "VpcOrigin":
        '''Create a VPC origin with an EC2 instance.

        :param instance: -
        :param domain_name: The domain name associated with your VPC origin. Default: - The default domain name of the endpoint.
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param http_port: The HTTP port for the CloudFront VPC origin endpoint configuration. Default: 80
        :param https_port: The HTTPS port of the CloudFront VPC origin endpoint configuration. Default: 443
        :param origin_ssl_protocols: A list that contains allowed SSL/TLS protocols for this distribution. Default: - TLSv1.2
        :param protocol_policy: The origin protocol policy for the CloudFront VPC origin endpoint configuration. Default: OriginProtocolPolicy.MATCH_VIEWER
        :param vpc_origin_name: The name of the CloudFront VPC origin endpoint configuration. Default: - generated from the ``id``
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fc3f8db0baa99548845b1733d31d8271fbe2c934c89a6c44958edcb38b35a13)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
        props = VpcOriginWithEndpointProps(
            domain_name=domain_name,
            keepalive_timeout=keepalive_timeout,
            read_timeout=read_timeout,
            http_port=http_port,
            https_port=https_port,
            origin_ssl_protocols=origin_ssl_protocols,
            protocol_policy=protocol_policy,
            vpc_origin_name=vpc_origin_name,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        return typing.cast("VpcOrigin", jsii.sinvoke(cls, "withEc2Instance", [instance, props]))

    @jsii.member(jsii_name="withNetworkLoadBalancer")
    @builtins.classmethod
    def with_network_load_balancer(
        cls,
        nlb: _INetworkLoadBalancer_96e17101,
        *,
        domain_name: typing.Optional[builtins.str] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
        protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
        vpc_origin_name: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> "VpcOrigin":
        '''Create a VPC origin with a Network Load Balancer.

        :param nlb: -
        :param domain_name: The domain name associated with your VPC origin. Default: - The default domain name of the endpoint.
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param http_port: The HTTP port for the CloudFront VPC origin endpoint configuration. Default: 80
        :param https_port: The HTTPS port of the CloudFront VPC origin endpoint configuration. Default: 443
        :param origin_ssl_protocols: A list that contains allowed SSL/TLS protocols for this distribution. Default: - TLSv1.2
        :param protocol_policy: The origin protocol policy for the CloudFront VPC origin endpoint configuration. Default: OriginProtocolPolicy.MATCH_VIEWER
        :param vpc_origin_name: The name of the CloudFront VPC origin endpoint configuration. Default: - generated from the ``id``
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83c5561f2747600ee99b6ee41190dcba45f2a24cc1c9500759e9c382320b83d6)
            check_type(argname="argument nlb", value=nlb, expected_type=type_hints["nlb"])
        props = VpcOriginWithEndpointProps(
            domain_name=domain_name,
            keepalive_timeout=keepalive_timeout,
            read_timeout=read_timeout,
            http_port=http_port,
            https_port=https_port,
            origin_ssl_protocols=origin_ssl_protocols,
            protocol_policy=protocol_policy,
            vpc_origin_name=vpc_origin_name,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        return typing.cast("VpcOrigin", jsii.sinvoke(cls, "withNetworkLoadBalancer", [nlb, props]))

    @jsii.member(jsii_name="withVpcOrigin")
    @builtins.classmethod
    def with_vpc_origin(
        cls,
        origin: _IVpcOrigin_6f584d50,
        *,
        domain_name: typing.Optional[builtins.str] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> "VpcOrigin":
        '''Create a VPC origin with an existing VPC origin resource.

        :param origin: -
        :param domain_name: The domain name associated with your VPC origin. Default: - The default domain name of the endpoint.
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7ed2e0f746eab77b2774c1adb0f114f10e786a05b531cd1218f93ad3770e5af)
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
        props = VpcOriginProps(
            domain_name=domain_name,
            keepalive_timeout=keepalive_timeout,
            read_timeout=read_timeout,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_access_control_id=origin_access_control_id,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        return typing.cast("VpcOrigin", jsii.sinvoke(cls, "withVpcOrigin", [origin, props]))

    @jsii.member(jsii_name="renderVpcOriginConfig")
    def _render_vpc_origin_config(
        self,
    ) -> typing.Optional[_CfnDistribution_d9ad3595.VpcOriginConfigProperty]:
        return typing.cast(typing.Optional[_CfnDistribution_d9ad3595.VpcOriginConfigProperty], jsii.invoke(self, "renderVpcOriginConfig", []))

    @builtins.property
    @jsii.member(jsii_name="props")
    def _props(self) -> "VpcOriginProps":
        return typing.cast("VpcOriginProps", jsii.get(self, "props"))

    @builtins.property
    @jsii.member(jsii_name="vpcOrigin")
    def _vpc_origin(self) -> typing.Optional[_IVpcOrigin_6f584d50]:
        return typing.cast(typing.Optional[_IVpcOrigin_6f584d50], jsii.get(self, "vpcOrigin"))

    @_vpc_origin.setter
    def _vpc_origin(self, value: typing.Optional[_IVpcOrigin_6f584d50]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d0218fc5ea8fbca94cbaeda39ab353fe5c35e197d6d8d60852fb576332785ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcOrigin", value) # pyright: ignore[reportArgumentType]


class _VpcOriginProxy(
    VpcOrigin,
    jsii.proxy_for(_OriginBase_b8fe5bcc), # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, VpcOrigin).__jsii_proxy_class__ = lambda : _VpcOriginProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.VpcOriginProps",
    jsii_struct_bases=[_OriginProps_0675928d],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_access_control_id": "originAccessControlId",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "domain_name": "domainName",
        "keepalive_timeout": "keepaliveTimeout",
        "read_timeout": "readTimeout",
    },
)
class VpcOriginProps(_OriginProps_0675928d):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        domain_name: typing.Optional[builtins.str] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Properties to define a VPC origin.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param domain_name: The domain name associated with your VPC origin. Default: - The default domain name of the endpoint.
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_cloudfront_origins as cloudfront_origins
            
            vpc_origin_props = cloudfront_origins.VpcOriginProps(
                connection_attempts=123,
                connection_timeout=cdk.Duration.minutes(30),
                custom_headers={
                    "custom_headers_key": "customHeaders"
                },
                domain_name="domainName",
                keepalive_timeout=cdk.Duration.minutes(30),
                origin_access_control_id="originAccessControlId",
                origin_id="originId",
                origin_path="originPath",
                origin_shield_enabled=False,
                origin_shield_region="originShieldRegion",
                read_timeout=cdk.Duration.minutes(30)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6605ea586b09bdf0ddb88a83b7c4e00626fe891625563cb019777b1480340f14)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_access_control_id", value=origin_access_control_id, expected_type=type_hints["origin_access_control_id"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument keepalive_timeout", value=keepalive_timeout, expected_type=type_hints["keepalive_timeout"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_access_control_id is not None:
            self._values["origin_access_control_id"] = origin_access_control_id
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if domain_name is not None:
            self._values["domain_name"] = domain_name
        if keepalive_timeout is not None:
            self._values["keepalive_timeout"] = keepalive_timeout
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_access_control_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an origin access control for this origin.

        :default: - no origin access control
        '''
        result = self._values.get("origin_access_control_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''The domain name associated with your VPC origin.

        :default: - The default domain name of the endpoint.
        '''
        result = self._values.get("domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keepalive_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront persists its connection to the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("keepalive_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcOriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.VpcOriginWithEndpointProps",
    jsii_struct_bases=[VpcOriginProps, _VpcOriginOptions_f9e74bd8],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_access_control_id": "originAccessControlId",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "domain_name": "domainName",
        "keepalive_timeout": "keepaliveTimeout",
        "read_timeout": "readTimeout",
        "http_port": "httpPort",
        "https_port": "httpsPort",
        "origin_ssl_protocols": "originSslProtocols",
        "protocol_policy": "protocolPolicy",
        "vpc_origin_name": "vpcOriginName",
    },
)
class VpcOriginWithEndpointProps(VpcOriginProps, _VpcOriginOptions_f9e74bd8):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_access_control_id: typing.Optional[builtins.str] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        domain_name: typing.Optional[builtins.str] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
        protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
        vpc_origin_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties to define a VPC origin with endpoint.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_access_control_id: The unique identifier of an origin access control for this origin. Default: - no origin access control
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param domain_name: The domain name associated with your VPC origin. Default: - The default domain name of the endpoint.
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param http_port: The HTTP port for the CloudFront VPC origin endpoint configuration. Default: 80
        :param https_port: The HTTPS port of the CloudFront VPC origin endpoint configuration. Default: 443
        :param origin_ssl_protocols: A list that contains allowed SSL/TLS protocols for this distribution. Default: - TLSv1.2
        :param protocol_policy: The origin protocol policy for the CloudFront VPC origin endpoint configuration. Default: OriginProtocolPolicy.MATCH_VIEWER
        :param vpc_origin_name: The name of the CloudFront VPC origin endpoint configuration. Default: - generated from the ``id``

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_cloudfront as cloudfront
            from aws_cdk import aws_cloudfront_origins as cloudfront_origins
            
            vpc_origin_with_endpoint_props = cloudfront_origins.VpcOriginWithEndpointProps(
                connection_attempts=123,
                connection_timeout=cdk.Duration.minutes(30),
                custom_headers={
                    "custom_headers_key": "customHeaders"
                },
                domain_name="domainName",
                http_port=123,
                https_port=123,
                keepalive_timeout=cdk.Duration.minutes(30),
                origin_access_control_id="originAccessControlId",
                origin_id="originId",
                origin_path="originPath",
                origin_shield_enabled=False,
                origin_shield_region="originShieldRegion",
                origin_ssl_protocols=[cloudfront.OriginSslPolicy.SSL_V3],
                protocol_policy=cloudfront.OriginProtocolPolicy.HTTP_ONLY,
                read_timeout=cdk.Duration.minutes(30),
                vpc_origin_name="vpcOriginName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e581b80df977101d74a87a861c6ddf752f3dc8bcbd114f5e12bc33daa6879040)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_access_control_id", value=origin_access_control_id, expected_type=type_hints["origin_access_control_id"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument keepalive_timeout", value=keepalive_timeout, expected_type=type_hints["keepalive_timeout"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
            check_type(argname="argument http_port", value=http_port, expected_type=type_hints["http_port"])
            check_type(argname="argument https_port", value=https_port, expected_type=type_hints["https_port"])
            check_type(argname="argument origin_ssl_protocols", value=origin_ssl_protocols, expected_type=type_hints["origin_ssl_protocols"])
            check_type(argname="argument protocol_policy", value=protocol_policy, expected_type=type_hints["protocol_policy"])
            check_type(argname="argument vpc_origin_name", value=vpc_origin_name, expected_type=type_hints["vpc_origin_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_access_control_id is not None:
            self._values["origin_access_control_id"] = origin_access_control_id
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if domain_name is not None:
            self._values["domain_name"] = domain_name
        if keepalive_timeout is not None:
            self._values["keepalive_timeout"] = keepalive_timeout
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout
        if http_port is not None:
            self._values["http_port"] = http_port
        if https_port is not None:
            self._values["https_port"] = https_port
        if origin_ssl_protocols is not None:
            self._values["origin_ssl_protocols"] = origin_ssl_protocols
        if protocol_policy is not None:
            self._values["protocol_policy"] = protocol_policy
        if vpc_origin_name is not None:
            self._values["vpc_origin_name"] = vpc_origin_name

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_access_control_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of an origin access control for this origin.

        :default: - no origin access control
        '''
        result = self._values.get("origin_access_control_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''The domain name associated with your VPC origin.

        :default: - The default domain name of the endpoint.
        '''
        result = self._values.get("domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keepalive_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront persists its connection to the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("keepalive_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def http_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTP port for the CloudFront VPC origin endpoint configuration.

        :default: 80
        '''
        result = self._values.get("http_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def https_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTPS port of the CloudFront VPC origin endpoint configuration.

        :default: 443
        '''
        result = self._values.get("https_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def origin_ssl_protocols(
        self,
    ) -> typing.Optional[typing.List[_OriginSslPolicy_d65cede2]]:
        '''A list that contains allowed SSL/TLS protocols for this distribution.

        :default: - TLSv1.2
        '''
        result = self._values.get("origin_ssl_protocols")
        return typing.cast(typing.Optional[typing.List[_OriginSslPolicy_d65cede2]], result)

    @builtins.property
    def protocol_policy(self) -> typing.Optional[_OriginProtocolPolicy_967ed73c]:
        '''The origin protocol policy for the CloudFront VPC origin endpoint configuration.

        :default: OriginProtocolPolicy.MATCH_VIEWER
        '''
        result = self._values.get("protocol_policy")
        return typing.cast(typing.Optional[_OriginProtocolPolicy_967ed73c], result)

    @builtins.property
    def vpc_origin_name(self) -> typing.Optional[builtins.str]:
        '''The name of the CloudFront VPC origin endpoint configuration.

        :default: - generated from the ``id``
        '''
        result = self._values.get("vpc_origin_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcOriginWithEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "FunctionUrlOrigin",
    "FunctionUrlOriginBaseProps",
    "FunctionUrlOriginProps",
    "FunctionUrlOriginWithOACProps",
    "HttpOrigin",
    "HttpOriginProps",
    "LoadBalancerV2Origin",
    "LoadBalancerV2OriginProps",
    "OriginGroup",
    "OriginGroupProps",
    "RestApiOrigin",
    "RestApiOriginProps",
    "S3BucketOrigin",
    "S3BucketOriginBaseProps",
    "S3BucketOriginWithOACProps",
    "S3BucketOriginWithOAIProps",
    "S3Origin",
    "S3OriginProps",
    "S3StaticWebsiteOrigin",
    "S3StaticWebsiteOriginProps",
    "VpcOrigin",
    "VpcOriginProps",
    "VpcOriginWithEndpointProps",
]

publication.publish()

def _typecheckingstub__fcda903697b26acfe2149a285d5a64619682b675affb52f4ae2d1aca46c8f1c3(
    lambda_function_url: _IFunctionUrl_1a74cd94,
    *,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4d59b7721f41be7903dbcffeddd34d596392d2c8d2a4110f31a4dacdb532727(
    lambda_function_url: _IFunctionUrl_1a74cd94,
    *,
    origin_access_control: typing.Optional[_IOriginAccessControl_82a6fe5a] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__610b4764a440619f38a9adeb3e13225e58180ee2ee316abd994579fdcdb84c12(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56d340a9ac5dd93c6aa22cb98bcbc860fb23f8d247b53c2cd1a51ecd8406909a(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56968af993436ccfcac0aa6a57169f1a033078c10740d435d086816ad0336a75(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_access_control: typing.Optional[_IOriginAccessControl_82a6fe5a] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57d13f69f251622e0723aa73c3eb93e482e0deb7a7b1e8439c7d7ad35cfc0cc5(
    domain_name: builtins.str,
    *,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
    protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13f43bf70f0a97ee8ca0e4f7aca38d43089ed2bc254d5c2b57c73b51c1c2b9df(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
    protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e5124d4f469d6539077a529c09cfba685fe4a7037b9417216b18f6ccdba96c0(
    load_balancer: _ILoadBalancerV2_4c5c0fbb,
    *,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
    protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c72b63200b184ae3f51c9b6a19be2eef9bddae313ee00c7378396c0dcf586887(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
    protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__428f309ea8c48c002d77db24802c77164c9607d40492e08c4b243080f941ff61(
    scope: _constructs_77d1e7e8.Construct,
    *,
    origin_id: builtins.str,
    distribution_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d6baf80fcac5a22fc2c985c83f9022e23b11075b338c076ac86172fff7d7e8b(
    *,
    fallback_origin: _IOrigin_83d4c1fa,
    primary_origin: _IOrigin_83d4c1fa,
    fallback_status_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
    selection_criteria: typing.Optional[_OriginSelectionCriteria_ba6d3e21] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56b6a9ee9b4e8ac821a25cc86fc2ff9f7490081ff9a35a5c551216af6a6ab722(
    rest_api: _RestApiBase_0431da32,
    *,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eca8c8f76c90eb80c45563b1a8eb9b9f1868ad621b45412a4cb935297b4d303(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cb1f0b82603224c7fbeb25b954355d9b19c8971c1f19cce6cc99b4579024f0f(
    bucket: _IBucket_42e086fd,
    *,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f676436dc530972f0e77d574f148913989a94d38c9af09bff28450e29ace8acb(
    bucket: _IBucket_42e086fd,
    *,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23afb965139dc34be23cec3ad5506b4c5de509db9c0d653bed7877f463b7a9db(
    bucket: _IBucket_42e086fd,
    *,
    origin_access_control: typing.Optional[_IOriginAccessControl_82a6fe5a] = None,
    origin_access_levels: typing.Optional[typing.Sequence[_AccessLevel_315d9a76]] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13e7421c65d5fbb92fc686fa854daca3e90dc002f3e99da4b4757e32e3c4105d(
    bucket: _IBucket_42e086fd,
    *,
    origin_access_identity: typing.Optional[_IOriginAccessIdentity_a922494c] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5e580c31fe629b713e1ecbf9905ebb4220e152805ab34129f693f2c4d4db098(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1af53a7ded1427e29cc874af45efdfe026a0004a1f2782a5bc936dbfcb4fe7a4(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    origin_access_control: typing.Optional[_IOriginAccessControl_82a6fe5a] = None,
    origin_access_levels: typing.Optional[typing.Sequence[_AccessLevel_315d9a76]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b64c18ef31b660c450eee84b6738d7bbd960797e1788e068be9663127832c26(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    origin_access_identity: typing.Optional[_IOriginAccessIdentity_a922494c] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ba8623373b0faa9ac55c816167da21a58e0753e0dd032b1f3e6ccd0bd977994(
    bucket: _IBucket_42e086fd,
    *,
    origin_access_identity: typing.Optional[_IOriginAccessIdentity_a922494c] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1731b0d7a385b196730b287be11e2cb13fa03d064ae3ffbfd55c5422a8f2c430(
    scope: _constructs_77d1e7e8.Construct,
    *,
    origin_id: builtins.str,
    distribution_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbd2a0ca1bf4d32899d90ea633e3ac416a6fa29972ee055a5866ec269b24307e(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    origin_access_identity: typing.Optional[_IOriginAccessIdentity_a922494c] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0edd2083352b96faf3ea9eb05136629dff841fa272ecdb6dfb52772a77b9b22(
    bucket: _IBucket_42e086fd,
    *,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
    protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bc18cdba7c0e6d7d0a68d2a1cf3c3f91f50a7e3e7384f5f62ebee6006adbb85(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
    protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27d66442a972110883cdde622df199c2db6a7264e19031f1118d7aa01681cef6(
    domain_name_: builtins.str,
    *,
    domain_name: typing.Optional[builtins.str] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8615ead9bb90a8fd2c91dc07371d03b8f4b4192a1500a449646bd8a7be95fa6c(
    alb: _IApplicationLoadBalancer_4cbd50ab,
    *,
    domain_name: typing.Optional[builtins.str] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
    protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
    vpc_origin_name: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fc3f8db0baa99548845b1733d31d8271fbe2c934c89a6c44958edcb38b35a13(
    instance: _IInstance_ab239e7c,
    *,
    domain_name: typing.Optional[builtins.str] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
    protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
    vpc_origin_name: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83c5561f2747600ee99b6ee41190dcba45f2a24cc1c9500759e9c382320b83d6(
    nlb: _INetworkLoadBalancer_96e17101,
    *,
    domain_name: typing.Optional[builtins.str] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
    protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
    vpc_origin_name: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7ed2e0f746eab77b2774c1adb0f114f10e786a05b531cd1218f93ad3770e5af(
    origin: _IVpcOrigin_6f584d50,
    *,
    domain_name: typing.Optional[builtins.str] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d0218fc5ea8fbca94cbaeda39ab353fe5c35e197d6d8d60852fb576332785ce(
    value: typing.Optional[_IVpcOrigin_6f584d50],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6605ea586b09bdf0ddb88a83b7c4e00626fe891625563cb019777b1480340f14(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    domain_name: typing.Optional[builtins.str] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e581b80df977101d74a87a861c6ddf752f3dc8bcbd114f5e12bc33daa6879040(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_access_control_id: typing.Optional[builtins.str] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    domain_name: typing.Optional[builtins.str] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
    protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
    vpc_origin_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
