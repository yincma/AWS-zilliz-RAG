r'''
# Amazon Data Firehose Construct Library

[Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html), [formerly known as Amazon Kinesis Data Firehose](https://aws.amazon.com/about-aws/whats-new/2024/02/amazon-data-firehose-formerly-kinesis-data-firehose/),
is a service for fully-managed delivery of real-time streaming data to storage services
such as Amazon S3, Amazon Redshift, Amazon Elasticsearch, Splunk, or any custom HTTP
endpoint or third-party services such as Datadog, Dynatrace, LogicMonitor, MongoDB, New
Relic, and Sumo Logic.

Amazon Data Firehose delivery streams are distinguished from Kinesis data streams in
their models of consumption. Whereas consumers read from a data stream by actively pulling
data from the stream, a delivery stream pushes data to its destination on a regular
cadence. This means that data streams are intended to have consumers that do on-demand
processing, like AWS Lambda or Amazon EC2. On the other hand, delivery streams are
intended to have destinations that are sources for offline processing and analytics, such
as Amazon S3 and Amazon Redshift.

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk)
project. It allows you to define Amazon Data Firehose delivery streams.

## Defining a Delivery Stream

In order to define a Delivery Stream, you must specify a destination. An S3 bucket can be
used as a destination. Currently the CDK supports only S3 as a destination which is covered [below](#destinations).

```python
bucket = s3.Bucket(self, "Bucket")
firehose.DeliveryStream(self, "Delivery Stream",
    destination=firehose.S3Bucket(bucket)
)
```

The above example defines the following resources:

* An S3 bucket
* An Amazon Data Firehose delivery stream with Direct PUT as the source and CloudWatch
  error logging turned on.
* An IAM role which gives the delivery stream permission to write to the S3 bucket.

## Sources

An Amazon Data Firehose delivery stream can accept data from three main sources: Kinesis Data Streams, Managed Streaming for Apache Kafka (MSK), or via a "direct put" (API calls). Currently only Kinesis Data Streams and direct put are supported in the CDK.

See: [Sending Data to a Delivery Stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-write.html)
in the *Amazon Data Firehose Developer Guide*.

### Kinesis Data Stream

A delivery stream can read directly from a Kinesis data stream as a consumer of the data
stream. Configure this behaviour by passing in a data stream in the `source`
property via the `KinesisStreamSource` class when constructing a delivery stream:

```python
# destination: firehose.IDestination

source_stream = kinesis.Stream(self, "Source Stream")

firehose.DeliveryStream(self, "Delivery Stream",
    source=firehose.KinesisStreamSource(source_stream),
    destination=destination
)
```

### Direct Put

Data must be provided via "direct put", ie., by using a `PutRecord` or
`PutRecordBatch` API call. There are a number of ways of doing so, such as:

* Kinesis Agent: a standalone Java application that monitors and delivers files while
  handling file rotation, checkpointing, and retries. See: [Writing to Amazon Data Firehose Using Kinesis Agent](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-agents.html)
  in the *Amazon Data Firehose Developer Guide*.
* AWS SDK: a general purpose solution that allows you to deliver data to a delivery stream
  from anywhere using Java, .NET, Node.js, Python, or Ruby. See: [Writing to Amazon Data Firehose Using the AWS SDK](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-sdk.html)
  in the *Amazon Data Firehose Developer Guide*.
* CloudWatch Logs: subscribe to a log group and receive filtered log events directly into
  a delivery stream. See: [logs-destinations](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-logs-destinations-readme.html).
* Eventbridge: add an event rule target to send events to a delivery stream based on the
  rule filtering. See: [events-targets](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-events-targets-readme.html).
* SNS: add a subscription to send all notifications from the topic to a delivery
  stream. See: [sns-subscriptions](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-sns-subscriptions-readme.html).
* IoT: add an action to an IoT rule to send various IoT information to a delivery stream

## Destinations

Amazon Data Firehose supports multiple AWS and third-party services as destinations, including Amazon S3, Amazon Redshift, and more. You can find the full list of supported destination [here](https://docs.aws.amazon.com/firehose/latest/dev/create-destination.html).

Currently in the AWS CDK, only S3 is implemented as an L2 construct destination. Other destinations can still be configured using L1 constructs.

### S3

Defining a delivery stream with an S3 bucket destination:

```python
# bucket: s3.Bucket

s3_destination = firehose.S3Bucket(bucket)

firehose.DeliveryStream(self, "Delivery Stream",
    destination=s3_destination
)
```

The S3 destination also supports custom dynamic prefixes. `dataOutputPrefix`
will be used for files successfully delivered to S3. `errorOutputPrefix` will be added to
failed records before writing them to S3.

```python
from aws_cdk import TimeZone
# bucket: s3.Bucket

s3_destination = firehose.S3Bucket(bucket,
    data_output_prefix="myFirehose/DeliveredYear=!{timestamp:yyyy}/anyMonth/rand=!{firehose:random-string}",
    error_output_prefix="myFirehoseFailures/!{firehose:error-output-type}/!{timestamp:yyyy}/anyMonth/!{timestamp:dd}",
    # The time zone of timestamps (default UTC)
    time_zone=TimeZone.ASIA_TOKYO
)
```

See: [Custom S3 Prefixes](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html)
in the *Amazon Data Firehose Developer Guide*.

To override default file extension appended by Data Format Conversion or S3 compression features, specify `fileExtension`.

```python
# bucket: s3.Bucket

s3_destination = firehose.S3Bucket(bucket,
    compression=firehose.Compression.GZIP,
    file_extension=".json.gz"
)
```

## Server-side Encryption

Enabling server-side encryption (SSE) requires Amazon Data Firehose to encrypt all data
sent to delivery stream when it is stored at rest. This means that data is encrypted
before being written to the service's internal storage layer and decrypted after it is
received from the internal storage layer. The service manages keys and cryptographic
operations so that sources and destinations do not need to, as the data is encrypted and
decrypted at the boundaries of the service (i.e., before the data is delivered to a
destination). By default, delivery streams do not have SSE enabled.

The Key Management Service keys (KMS keys) used for SSE can either be AWS-owned or
customer-managed. AWS-owned KMS keys are created, owned and managed by AWS for use in
multiple AWS accounts. As a customer, you cannot view, use, track, or manage these keys,
and you are not charged for their use. On the other hand, customer-managed KMS keys are
created and owned within your account and managed entirely by you. As a customer, you are
responsible for managing access, rotation, aliases, and deletion for these keys, and you
are changed for their use.

See: [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys)
in the *KMS Developer Guide*.

```python
# destination: firehose.IDestination
# SSE with an customer-managed key that is explicitly specified
# key: kms.Key


# SSE with an AWS-owned key
firehose.DeliveryStream(self, "Delivery Stream with AWS Owned Key",
    encryption=firehose.StreamEncryption.aws_owned_key(),
    destination=destination
)
# SSE with an customer-managed key that is created automatically by the CDK
firehose.DeliveryStream(self, "Delivery Stream with Customer Managed Key",
    encryption=firehose.StreamEncryption.customer_managed_key(),
    destination=destination
)
firehose.DeliveryStream(self, "Delivery Stream with Customer Managed and Provided Key",
    encryption=firehose.StreamEncryption.customer_managed_key(key),
    destination=destination
)
```

See: [Data Protection](https://docs.aws.amazon.com/firehose/latest/dev/encryption.html)
in the *Amazon Data Firehose Developer Guide*.

## Monitoring

Amazon Data Firehose is integrated with CloudWatch, so you can monitor the performance of
your delivery streams via logs and metrics.

### Logs

Amazon Data Firehose will send logs to CloudWatch when data transformation or data
delivery fails. The CDK will enable logging by default and create a CloudWatch LogGroup
and LogStream with default settings for your Delivery Stream.

When creating a destination, you can provide an `ILoggingConfig`, which can either be an `EnableLogging` or `DisableLogging` instance.
If you use `EnableLogging`, the CDK will create a CloudWatch LogGroup and LogStream with all CloudFormation default settings for you, or you can optionally
specify your own log group to be used for capturing and storing log events. For example:

```python
import aws_cdk.aws_logs as logs
# bucket: s3.Bucket


log_group = logs.LogGroup(self, "Log Group")
destination = firehose.S3Bucket(bucket,
    logging_config=firehose.EnableLogging(log_group)
)

firehose.DeliveryStream(self, "Delivery Stream",
    destination=destination
)
```

Logging can also be disabled:

```python
# bucket: s3.Bucket

destination = firehose.S3Bucket(bucket,
    logging_config=firehose.DisableLogging()
)
firehose.DeliveryStream(self, "Delivery Stream",
    destination=destination
)
```

See: [Monitoring using CloudWatch Logs](https://docs.aws.amazon.com/firehose/latest/dev/monitoring-with-cloudwatch-logs.html)
in the *Amazon Data Firehose Developer Guide*.

### Metrics

Amazon Data Firehose sends metrics to CloudWatch so that you can collect and analyze the
performance of the delivery stream, including data delivery, data ingestion, data
transformation, format conversion, API usage, encryption, and resource usage. You can then
use CloudWatch alarms to alert you, for example, when data freshness (the age of the
oldest record in the delivery stream) exceeds the buffering limit (indicating that data is
not being delivered to your destination), or when the rate of incoming records exceeds the
limit of records per second (indicating data is flowing into your delivery stream faster
than it is configured to process).

CDK provides methods for accessing delivery stream metrics with default configuration,
such as `metricIncomingBytes`, and `metricIncomingRecords` (see [`IDeliveryStream`](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-cdk-lib.aws_kinesisfirehose.IDeliveryStream.html)
for a full list). CDK also provides a generic `metric` method that can be used to produce
metric configurations for any metric provided by Amazon Data Firehose; the configurations
are pre-populated with the correct dimensions for the delivery stream.

```python
import aws_cdk.aws_cloudwatch as cloudwatch

# delivery_stream: firehose.DeliveryStream


# Alarm that triggers when the per-second average of incoming bytes exceeds 90% of the current service limit
incoming_bytes_percent_of_limit = cloudwatch.MathExpression(
    expression="incomingBytes / 300 / bytePerSecLimit",
    using_metrics={
        "incoming_bytes": delivery_stream.metric_incoming_bytes(statistic=cloudwatch.Statistic.SUM),
        "byte_per_sec_limit": delivery_stream.metric("BytesPerSecondLimit")
    }
)

cloudwatch.Alarm(self, "Alarm",
    metric=incoming_bytes_percent_of_limit,
    threshold=0.9,
    evaluation_periods=3
)
```

See: [Monitoring Using CloudWatch Metrics](https://docs.aws.amazon.com/firehose/latest/dev/monitoring-with-cloudwatch-metrics.html)
in the *Amazon Data Firehose Developer Guide*.

## Compression

Your data can automatically be compressed when it is delivered to S3 as either a final or
an intermediary/backup destination. Supported compression formats are: gzip, Snappy,
Hadoop-compatible Snappy, and ZIP, except for Redshift destinations, where Snappy
(regardless of Hadoop-compatibility) and ZIP are not supported. By default, data is
delivered to S3 without compression.

```python
# Compress data delivered to S3 using Snappy
# bucket: s3.Bucket

s3_destination = firehose.S3Bucket(bucket,
    compression=firehose.Compression.SNAPPY
)
firehose.DeliveryStream(self, "Delivery Stream",
    destination=s3_destination
)
```

## Buffering

Incoming data is buffered before it is delivered to the specified destination. The
delivery stream will wait until the amount of incoming data has exceeded some threshold
(the "buffer size") or until the time since the last data delivery occurred exceeds some
threshold (the "buffer interval"), whichever happens first. You can configure these
thresholds based on the capabilities of the destination and your use-case. By default, the
buffer size is 5 MiB and the buffer interval is 5 minutes.

```python
# Increase the buffer interval and size to 10 minutes and 8 MiB, respectively
# bucket: s3.Bucket

destination = firehose.S3Bucket(bucket,
    buffering_interval=Duration.minutes(10),
    buffering_size=Size.mebibytes(8)
)
firehose.DeliveryStream(self, "Delivery Stream",
    destination=destination
)
```

See: [Data Delivery Frequency](https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#frequency)
in the *Amazon Data Firehose Developer Guide*.

Zero buffering, where Amazon Data Firehose stream can be configured to not buffer data before delivery, is supported by
setting the "buffer interval" to 0.

```python
# Setup zero buffering
# bucket: s3.Bucket

destination = firehose.S3Bucket(bucket,
    buffering_interval=Duration.seconds(0)
)
firehose.DeliveryStream(self, "ZeroBufferDeliveryStream",
    destination=destination
)
```

See: [Buffering Hints](https://docs.aws.amazon.com/firehose/latest/dev/buffering-hints.html).

## Destination Encryption

Your data can be automatically encrypted when it is delivered to S3 as a final or an
intermediary/backup destination. Amazon Data Firehose supports Amazon S3 server-side
encryption with AWS Key Management Service (AWS KMS) for encrypting delivered data in
Amazon S3. You can choose to not encrypt the data or to encrypt with a key from the list
of AWS KMS keys that you own. For more information,
see [Protecting Data Using Server-Side Encryption with AWS KMS–Managed Keys (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html).
By default, encryption isn’t directly enabled on the delivery stream; instead, it uses the default encryption settings of the destination S3 bucket.

```python
# bucket: s3.Bucket
# key: kms.Key

destination = firehose.S3Bucket(bucket,
    encryption_key=key
)
firehose.DeliveryStream(self, "Delivery Stream",
    destination=destination
)
```

## Backup

A delivery stream can be configured to back up data to S3 that it attempted to deliver to
the configured destination. Backed up data can be all the data that the delivery stream
attempted to deliver or just data that it failed to deliver (Redshift and S3 destinations
can only back up all data). CDK can create a new S3 bucket where it will back up data, or
you can provide a bucket where data will be backed up. You can also provide a prefix under
which your backed-up data will be placed within the bucket. By default, source data is not
backed up to S3.

```python
# Enable backup of all source records (to an S3 bucket created by CDK).
# bucket: s3.Bucket
# Explicitly provide an S3 bucket to which all source records will be backed up.
# backup_bucket: s3.Bucket

firehose.DeliveryStream(self, "Delivery Stream Backup All",
    destination=
    firehose.S3Bucket(bucket,
        s3_backup=firehose.DestinationS3BackupProps(
            mode=firehose.BackupMode.ALL
        )
    )
)
firehose.DeliveryStream(self, "Delivery Stream Backup All Explicit Bucket",
    destination=
    firehose.S3Bucket(bucket,
        s3_backup=firehose.DestinationS3BackupProps(
            bucket=backup_bucket
        )
    )
)
# Explicitly provide an S3 prefix under which all source records will be backed up.
firehose.DeliveryStream(self, "Delivery Stream Backup All Explicit Prefix",
    destination=
    firehose.S3Bucket(bucket,
        s3_backup=firehose.DestinationS3BackupProps(
            mode=firehose.BackupMode.ALL,
            data_output_prefix="mybackup"
        )
    )
)
```

If any Data Processing or Transformation is configured on your Delivery Stream, the source
records will be backed up in their original format.

## Data Processing/Transformation

Data can be transformed before being delivered to destinations. There are two types of
data processing for delivery streams: record transformation with AWS Lambda, and record
format conversion using a schema stored in an AWS Glue table. If both types of data
processing are configured, then the Lambda transformation is performed first. By default,
no data processing occurs. This construct library currently only supports data
transformation with AWS Lambda. See [#15501](https://github.com/aws/aws-cdk/issues/15501)
to track the status of adding support for record format conversion.

### Data transformation with AWS Lambda

To transform the data, Amazon Data Firehose will call a Lambda function that you provide
and deliver the data returned in place of the source record. The function must return a
result that contains records in a specific format, including the following fields:

* `recordId` -- the ID of the input record that corresponds the results.
* `result` -- the status of the transformation of the record: "Ok" (success), "Dropped"
  (not processed intentionally), or "ProcessingFailed" (not processed due to an error).
* `data` -- the transformed data, Base64-encoded.

The data is buffered up to 1 minute and up to 3 MiB by default before being sent to the
function, but can be configured using `bufferInterval` and `bufferSize`
in the processor configuration (see: [Buffering](#buffering)). If the function invocation
fails due to a network timeout or because of hitting an invocation limit, the invocation
is retried 3 times by default, but can be configured using `retries` in the processor
configuration.

```python
# bucket: s3.Bucket
# Provide a Lambda function that will transform records before delivery, with custom
# buffering and retry configuration
lambda_function = lambda_.Function(self, "Processor",
    runtime=lambda_.Runtime.NODEJS_LATEST,
    handler="index.handler",
    code=lambda_.Code.from_asset(path.join(__dirname, "process-records"))
)
lambda_processor = firehose.LambdaFunctionProcessor(lambda_function,
    buffer_interval=Duration.minutes(5),
    buffer_size=Size.mebibytes(5),
    retries=5
)
s3_destination = firehose.S3Bucket(bucket,
    processor=lambda_processor
)
firehose.DeliveryStream(self, "Delivery Stream",
    destination=s3_destination
)
```

```python
import path as path
import aws_cdk.aws_kinesisfirehose as firehose
import aws_cdk.aws_kms as kms
import aws_cdk.aws_lambda_nodejs as lambdanodejs
import aws_cdk.aws_logs as logs
import aws_cdk.aws_s3 as s3
import aws_cdk as cdk
from aws_cdk.integ_tests_alpha import AwsApiCall, ExpectedResult, IntegTest

app = cdk.App(
    post_cli_context={
        "@aws-cdk/aws-lambda:useCdkManagedLogGroup": False
    }
)

stack = cdk.Stack(app, "aws-cdk-firehose-delivery-stream-s3-all-properties")

bucket = s3.Bucket(stack, "FirehoseDeliveryStreamS3AllPropertiesBucket",
    removal_policy=cdk.RemovalPolicy.DESTROY,
    auto_delete_objects=True
)

backup_bucket = s3.Bucket(stack, "FirehoseDeliveryStreamS3AllPropertiesBackupBucket",
    removal_policy=cdk.RemovalPolicy.DESTROY,
    auto_delete_objects=True
)
log_group = logs.LogGroup(stack, "LogGroup",
    removal_policy=cdk.RemovalPolicy.DESTROY
)

data_processor_function = lambdanodejs.NodejsFunction(stack, "DataProcessorFunction",
    entry=path.join(__dirname, "lambda-data-processor.js"),
    timeout=cdk.Duration.minutes(1)
)

processor = firehose.LambdaFunctionProcessor(data_processor_function,
    buffer_interval=cdk.Duration.seconds(60),
    buffer_size=cdk.Size.mebibytes(1),
    retries=1
)

key = kms.Key(stack, "Key",
    removal_policy=cdk.RemovalPolicy.DESTROY
)

backup_key = kms.Key(stack, "BackupKey",
    removal_policy=cdk.RemovalPolicy.DESTROY
)

delivery_stream = firehose.DeliveryStream(stack, "DeliveryStream",
    destination=firehose.S3Bucket(bucket,
        logging_config=firehose.EnableLogging(log_group),
        processor=processor,
        compression=firehose.Compression.GZIP,
        data_output_prefix="regularPrefix",
        error_output_prefix="errorPrefix",
        file_extension=".log.gz",
        time_zone=cdk.TimeZone.ASIA_TOKYO,
        buffering_interval=cdk.Duration.seconds(60),
        buffering_size=cdk.Size.mebibytes(1),
        encryption_key=key,
        s3_backup=firehose.DestinationS3BackupProps(
            mode=firehose.BackupMode.ALL,
            bucket=backup_bucket,
            compression=firehose.Compression.ZIP,
            data_output_prefix="backupPrefix",
            error_output_prefix="backupErrorPrefix",
            buffering_interval=cdk.Duration.seconds(60),
            buffering_size=cdk.Size.mebibytes(1),
            encryption_key=backup_key
        )
    )
)

firehose.DeliveryStream(stack, "ZeroBufferingDeliveryStream",
    destination=firehose.S3Bucket(bucket,
        compression=firehose.Compression.GZIP,
        data_output_prefix="regularPrefix",
        error_output_prefix="errorPrefix",
        buffering_interval=cdk.Duration.seconds(0)
    )
)

test_case = IntegTest(app, "integ-tests",
    test_cases=[stack],
    regions=["us-east-1"]
)

test_case.assertions.aws_api_call("Firehose", "putRecord", {
    "DeliveryStreamName": delivery_stream.delivery_stream_name,
    "Record": {
        "Data": "testData123"
    }
})

s3_api_call = test_case.assertions.aws_api_call("S3", "listObjectsV2", {
    "Bucket": bucket.bucket_name,
    "MaxKeys": 1
}).expect(ExpectedResult.object_like({
    "KeyCount": 1
})).wait_for_assertions(
    interval=cdk.Duration.seconds(30),
    total_timeout=cdk.Duration.minutes(10)
)

if s3_api_call instanceof AwsApiCall && s3_api_call.waiter_provider:
    s3_api_call.waiter_provider.add_to_role_policy({
        "Effect": "Allow",
        "Action": ["s3:GetObject", "s3:ListBucket"],
        "Resource": ["*"]
    })
```

See: [Data Transformation](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html)
in the *Amazon Data Firehose Developer Guide*.

## Specifying an IAM role

The DeliveryStream class automatically creates IAM service roles with all the minimum
necessary permissions for Amazon Data Firehose to access the resources referenced by your
delivery stream. One service role is created for the delivery stream that allows Amazon
Data Firehose to read from a Kinesis data stream (if one is configured as the delivery
stream source) and for server-side encryption. Note that if the DeliveryStream is created
without specifying a `source` or `encryptionKey`, this role is not created as it is not needed.

Another service role is created for each destination, which gives Amazon Data Firehose write
access to the destination resource, as well as the ability to invoke data transformers and
read schemas for record format conversion. If you wish, you may specify your own IAM role for
either the delivery stream or the destination service role, or both. It must have the correct
trust policy (it must allow Amazon Data Firehose to assume it) or delivery stream creation or
data delivery will fail. Other required permissions to destination resources, encryption keys, etc.,
will be provided automatically.

```python
# Specify the roles created above when defining the destination and delivery stream.
# bucket: s3.Bucket
# Create service roles for the delivery stream and destination.
# These can be used for other purposes and granted access to different resources.
# They must include the Amazon Data Firehose service principal in their trust policies.
# Two separate roles are shown below, but the same role can be used for both purposes.
delivery_stream_role = iam.Role(self, "Delivery Stream Role",
    assumed_by=iam.ServicePrincipal("firehose.amazonaws.com")
)
destination_role = iam.Role(self, "Destination Role",
    assumed_by=iam.ServicePrincipal("firehose.amazonaws.com")
)
destination = firehose.S3Bucket(bucket, role=destination_role)
firehose.DeliveryStream(self, "Delivery Stream",
    destination=destination,
    role=delivery_stream_role
)
```

See [Controlling Access](https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html)
in the *Amazon Data Firehose Developer Guide*.

## Granting application access to a delivery stream

IAM roles, users or groups which need to be able to work with delivery streams should be
granted IAM permissions.

Any object that implements the `IGrantable` interface (i.e., has an associated principal)
can be granted permissions to a delivery stream by calling:

* `grantPutRecords(principal)` - grants the principal the ability to put records onto the
  delivery stream
* `grant(principal, ...actions)` - grants the principal permission to a custom set of
  actions

```python
# Give the role permissions to write data to the delivery stream
# delivery_stream: firehose.DeliveryStream
lambda_role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
)
delivery_stream.grant_put_records(lambda_role)
```

The following write permissions are provided to a service principal by the
`grantPutRecords()` method:

* `firehose:PutRecord`
* `firehose:PutRecordBatch`

## Granting a delivery stream access to a resource

Conversely to the above, Amazon Data Firehose requires permissions in order for delivery
streams to interact with resources that you own. For example, if an S3 bucket is specified
as a destination of a delivery stream, the delivery stream must be granted permissions to
put and get objects from the bucket. When using the built-in AWS service destinations, the CDK grants the
permissions automatically. However, custom or third-party destinations may require custom
permissions. In this case, use the delivery stream as an `IGrantable`, as follows:

```python
# delivery_stream: firehose.DeliveryStream
fn = lambda_.Function(self, "Function",
    code=lambda_.Code.from_inline("exports.handler = (event) => {}"),
    runtime=lambda_.Runtime.NODEJS_LATEST,
    handler="index.handler"
)
fn.grant_invoke(delivery_stream)
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
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    Duration as _Duration_4839e8c3,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    Resource as _Resource_45bc6135,
    Size as _Size_7b441c34,
    TagManager as _TagManager_0a598cb3,
    TimeZone as _TimeZone_cdd72ac9,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_cloudwatch import (
    Metric as _Metric_e396a4dc,
    MetricOptions as _MetricOptions_1788b62f,
    Unit as _Unit_61bc6f70,
)
from ..aws_ec2 import (
    Connections as _Connections_0f31fce8, IConnectable as _IConnectable_10015a05
)
from ..aws_iam import (
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IPrincipal as _IPrincipal_539bb2fd,
    IRole as _IRole_235f5d8e,
)
from ..aws_kinesis import IStream as _IStream_4e2457d2
from ..aws_kms import IKey as _IKey_5f11635f
from ..aws_lambda import IFunction as _IFunction_6adb0ab8
from ..aws_logs import ILogGroup as _ILogGroup_3c4fa718
from ..aws_s3 import IBucket as _IBucket_42e086fd


@jsii.enum(jsii_type="aws-cdk-lib.aws_kinesisfirehose.BackupMode")
class BackupMode(enum.Enum):
    '''Options for S3 record backup of a delivery stream.

    :exampleMetadata: infused

    Example::

        # Enable backup of all source records (to an S3 bucket created by CDK).
        # bucket: s3.Bucket
        # Explicitly provide an S3 bucket to which all source records will be backed up.
        # backup_bucket: s3.Bucket
        
        firehose.DeliveryStream(self, "Delivery Stream Backup All",
            destination=
            firehose.S3Bucket(bucket,
                s3_backup=firehose.DestinationS3BackupProps(
                    mode=firehose.BackupMode.ALL
                )
            )
        )
        firehose.DeliveryStream(self, "Delivery Stream Backup All Explicit Bucket",
            destination=
            firehose.S3Bucket(bucket,
                s3_backup=firehose.DestinationS3BackupProps(
                    bucket=backup_bucket
                )
            )
        )
        # Explicitly provide an S3 prefix under which all source records will be backed up.
        firehose.DeliveryStream(self, "Delivery Stream Backup All Explicit Prefix",
            destination=
            firehose.S3Bucket(bucket,
                s3_backup=firehose.DestinationS3BackupProps(
                    mode=firehose.BackupMode.ALL,
                    data_output_prefix="mybackup"
                )
            )
        )
    '''

    ALL = "ALL"
    '''All records are backed up.'''
    FAILED = "FAILED"
    '''Only records that failed to deliver or transform are backed up.'''


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDeliveryStream(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream",
):
    '''The ``AWS::KinesisFirehose::DeliveryStream`` resource specifies an Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivery stream that delivers real-time streaming data to an Amazon Simple Storage Service (Amazon S3), Amazon Redshift, or Amazon Elasticsearch Service (Amazon ES) destination.

    For more information, see `Creating an Amazon Kinesis Data Firehose Delivery Stream <https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html>`_ in the *Amazon Kinesis Data Firehose Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html
    :cloudformationResource: AWS::KinesisFirehose::DeliveryStream
    :exampleMetadata: infused

    Example::

        destination_bucket = s3.Bucket(self, "Bucket")
        delivery_stream_role = iam.Role(self, "Role",
            assumed_by=iam.ServicePrincipal("firehose.amazonaws.com")
        )
        
        stream = firehose.CfnDeliveryStream(self, "MyStream",
            delivery_stream_name="amazon-apigateway-delivery-stream",
            s3_destination_configuration=firehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                bucket_arn=destination_bucket.bucket_arn,
                role_arn=delivery_stream_role.role_arn
            )
        )
        
        api = apigateway.RestApi(self, "books",
            deploy_options=apigateway.StageOptions(
                access_log_destination=apigateway.FirehoseLogDestination(stream),
                access_log_format=apigateway.AccessLogFormat.json_with_standard_fields()
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        amazon_open_search_serverless_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        amazonopensearchservice_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        database_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DatabaseSourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        delivery_stream_encryption_configuration_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        delivery_stream_name: typing.Optional[builtins.str] = None,
        delivery_stream_type: typing.Optional[builtins.str] = None,
        direct_put_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DirectPutSourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        elasticsearch_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        extended_s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        http_endpoint_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        iceberg_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.IcebergDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kinesis_stream_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.KinesisStreamSourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        msk_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.MSKSourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        redshift_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.RedshiftDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        snowflake_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SnowflakeDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        splunk_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SplunkDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param amazon_open_search_serverless_destination_configuration: Describes the configuration of a destination in the Serverless offering for Amazon OpenSearch Service.
        :param amazonopensearchservice_destination_configuration: The destination in Amazon OpenSearch Service. You can specify only one destination.
        :param database_source_configuration: The top level object for configuring streams with database as a source. Amazon Data Firehose is in preview release and is subject to change.
        :param delivery_stream_encryption_configuration_input: Specifies the type and Amazon Resource Name (ARN) of the CMK to use for Server-Side Encryption (SSE).
        :param delivery_stream_name: The name of the Firehose stream.
        :param delivery_stream_type: The Firehose stream type. This can be one of the following values:. - ``DirectPut`` : Provider applications access the Firehose stream directly. - ``KinesisStreamAsSource`` : The Firehose stream uses a Kinesis data stream as a source.
        :param direct_put_source_configuration: The structure that configures parameters such as ``ThroughputHintInMBs`` for a stream configured with Direct PUT as a source.
        :param elasticsearch_destination_configuration: An Amazon ES destination for the delivery stream. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon ES destination to an Amazon S3 or Amazon Redshift destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param extended_s3_destination_configuration: An Amazon S3 destination for the delivery stream. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon Extended S3 destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param http_endpoint_destination_configuration: Enables configuring Kinesis Firehose to deliver data to any HTTP endpoint destination. You can specify only one destination.
        :param iceberg_destination_configuration: Specifies the destination configure settings for Apache Iceberg Table.
        :param kinesis_stream_source_configuration: When a Kinesis stream is used as the source for the delivery stream, a `KinesisStreamSourceConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html>`_ containing the Kinesis stream ARN and the role ARN for the source stream.
        :param msk_source_configuration: The configuration for the Amazon MSK cluster to be used as the source for a delivery stream.
        :param redshift_destination_configuration: An Amazon Redshift destination for the delivery stream. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon Redshift destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param s3_destination_configuration: The ``S3DestinationConfiguration`` property type specifies an Amazon Simple Storage Service (Amazon S3) destination to which Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivers data. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon S3 destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param snowflake_destination_configuration: Configure Snowflake destination.
        :param splunk_destination_configuration: The configuration of a destination in Splunk for the delivery stream.
        :param tags: A set of tags to assign to the Firehose stream. A tag is a key-value pair that you can define and assign to AWS resources. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the Firehose stream. For more information about tags, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_ in the AWS Billing and Cost Management User Guide. You can specify up to 50 tags when creating a Firehose stream. If you specify tags in the ``CreateDeliveryStream`` action, Amazon Data Firehose performs an additional authorization on the ``firehose:TagDeliveryStream`` action to verify if users have permissions to create tags. If you do not provide this permission, requests to create new Firehose streams with IAM resource tags will fail with an ``AccessDeniedException`` such as following. *AccessDeniedException* User: arn:aws:sts::x:assumed-role/x/x is not authorized to perform: firehose:TagDeliveryStream on resource: arn:aws:firehose:us-east-1:x:deliverystream/x with an explicit deny in an identity-based policy. For an example IAM policy, see `Tag example. <https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html#API_CreateDeliveryStream_Examples>`_
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3cd824a2680c7d043cac684bd1be9ca77e94201f1ba00785d60a50ff43c2288)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeliveryStreamProps(
            amazon_open_search_serverless_destination_configuration=amazon_open_search_serverless_destination_configuration,
            amazonopensearchservice_destination_configuration=amazonopensearchservice_destination_configuration,
            database_source_configuration=database_source_configuration,
            delivery_stream_encryption_configuration_input=delivery_stream_encryption_configuration_input,
            delivery_stream_name=delivery_stream_name,
            delivery_stream_type=delivery_stream_type,
            direct_put_source_configuration=direct_put_source_configuration,
            elasticsearch_destination_configuration=elasticsearch_destination_configuration,
            extended_s3_destination_configuration=extended_s3_destination_configuration,
            http_endpoint_destination_configuration=http_endpoint_destination_configuration,
            iceberg_destination_configuration=iceberg_destination_configuration,
            kinesis_stream_source_configuration=kinesis_stream_source_configuration,
            msk_source_configuration=msk_source_configuration,
            redshift_destination_configuration=redshift_destination_configuration,
            s3_destination_configuration=s3_destination_configuration,
            snowflake_destination_configuration=snowflake_destination_configuration,
            splunk_destination_configuration=splunk_destination_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f6206943f45cc34824996fe47b775be3c1a09cb74450254dfa716bc71a96a69)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__822762453b1edc05d278fe4b56cb34de36a63cda89772b6624160f6ac406e7e7)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the delivery stream, such as ``arn:aws:firehose:us-east-2:123456789012:deliverystream/delivery-stream-name`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="amazonOpenSearchServerlessDestinationConfiguration")
    def amazon_open_search_serverless_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty"]]:
        '''Describes the configuration of a destination in the Serverless offering for Amazon OpenSearch Service.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty"]], jsii.get(self, "amazonOpenSearchServerlessDestinationConfiguration"))

    @amazon_open_search_serverless_destination_configuration.setter
    def amazon_open_search_serverless_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9361f4405d0a8e9a0285d4b343c6420073eedc822c339d1a147f151a3b03f641)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amazonOpenSearchServerlessDestinationConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="amazonopensearchserviceDestinationConfiguration")
    def amazonopensearchservice_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty"]]:
        '''The destination in Amazon OpenSearch Service.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty"]], jsii.get(self, "amazonopensearchserviceDestinationConfiguration"))

    @amazonopensearchservice_destination_configuration.setter
    def amazonopensearchservice_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58964b8831d37cbba22a48328508a0d1fc866bb6da992a0c3f544fc6649acc5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amazonopensearchserviceDestinationConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="databaseSourceConfiguration")
    def database_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DatabaseSourceConfigurationProperty"]]:
        '''The top level object for configuring streams with database as a source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DatabaseSourceConfigurationProperty"]], jsii.get(self, "databaseSourceConfiguration"))

    @database_source_configuration.setter
    def database_source_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DatabaseSourceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__671f3a3eb25ab7249d3b64fb9d1c6865a8a68b8a7b92841ab6890851853da1f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseSourceConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamEncryptionConfigurationInput")
    def delivery_stream_encryption_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty"]]:
        '''Specifies the type and Amazon Resource Name (ARN) of the CMK to use for Server-Side Encryption (SSE).'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty"]], jsii.get(self, "deliveryStreamEncryptionConfigurationInput"))

    @delivery_stream_encryption_configuration_input.setter
    def delivery_stream_encryption_configuration_input(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b541613844a306d329ee6aaf12a513672a01cea651f015810fd2ab896394415)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStreamEncryptionConfigurationInput", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamName")
    def delivery_stream_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Firehose stream.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStreamName"))

    @delivery_stream_name.setter
    def delivery_stream_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d90731f57c337a34bb7290e3bb4239e949b5caeea354433c46c25998a03b39f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStreamName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamType")
    def delivery_stream_type(self) -> typing.Optional[builtins.str]:
        '''The Firehose stream type.

        This can be one of the following values:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStreamType"))

    @delivery_stream_type.setter
    def delivery_stream_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0749b7e1cb2e266044df272e646eba4d2505c56ccb68f4ce96de186aeb83ba9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStreamType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="directPutSourceConfiguration")
    def direct_put_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DirectPutSourceConfigurationProperty"]]:
        '''The structure that configures parameters such as ``ThroughputHintInMBs`` for a stream configured with Direct PUT as a source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DirectPutSourceConfigurationProperty"]], jsii.get(self, "directPutSourceConfiguration"))

    @direct_put_source_configuration.setter
    def direct_put_source_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DirectPutSourceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c2e3d41bd399b2de627c15c37d5d5a53d60ea55a256dc5f1b73146429dd1f24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directPutSourceConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="elasticsearchDestinationConfiguration")
    def elasticsearch_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty"]]:
        '''An Amazon ES destination for the delivery stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty"]], jsii.get(self, "elasticsearchDestinationConfiguration"))

    @elasticsearch_destination_configuration.setter
    def elasticsearch_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2485fd6e8467da83435abf801383e98fea4d4ae9797551e1774f2327e1b069c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticsearchDestinationConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="extendedS3DestinationConfiguration")
    def extended_s3_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty"]]:
        '''An Amazon S3 destination for the delivery stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty"]], jsii.get(self, "extendedS3DestinationConfiguration"))

    @extended_s3_destination_configuration.setter
    def extended_s3_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b3827d67811452e6783eeef4d719d420c5534229b93597dbfafa7256a89932e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extendedS3DestinationConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="httpEndpointDestinationConfiguration")
    def http_endpoint_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty"]]:
        '''Enables configuring Kinesis Firehose to deliver data to any HTTP endpoint destination.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty"]], jsii.get(self, "httpEndpointDestinationConfiguration"))

    @http_endpoint_destination_configuration.setter
    def http_endpoint_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c45396814a2f1f16d85b99c121f14ab851eda0a9f84038025d5ae44a858837a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpEndpointDestinationConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="icebergDestinationConfiguration")
    def iceberg_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.IcebergDestinationConfigurationProperty"]]:
        '''Specifies the destination configure settings for Apache Iceberg Table.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.IcebergDestinationConfigurationProperty"]], jsii.get(self, "icebergDestinationConfiguration"))

    @iceberg_destination_configuration.setter
    def iceberg_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.IcebergDestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94c8f409ef0a75500e50bbf49d47688097508bd257b3ce092b027c552453cd59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icebergDestinationConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamSourceConfiguration")
    def kinesis_stream_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.KinesisStreamSourceConfigurationProperty"]]:
        '''When a Kinesis stream is used as the source for the delivery stream, a `KinesisStreamSourceConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html>`_ containing the Kinesis stream ARN and the role ARN for the source stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.KinesisStreamSourceConfigurationProperty"]], jsii.get(self, "kinesisStreamSourceConfiguration"))

    @kinesis_stream_source_configuration.setter
    def kinesis_stream_source_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.KinesisStreamSourceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__025f54a26e52ce42f679eff3aa8b95a5fee2e0e5b3aba7c4320f9900690e60b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kinesisStreamSourceConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mskSourceConfiguration")
    def msk_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.MSKSourceConfigurationProperty"]]:
        '''The configuration for the Amazon MSK cluster to be used as the source for a delivery stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.MSKSourceConfigurationProperty"]], jsii.get(self, "mskSourceConfiguration"))

    @msk_source_configuration.setter
    def msk_source_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.MSKSourceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d05261de796c66b290d3bf9493dedca3a4f904726566b1e0d28cd6f7e525757)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mskSourceConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftDestinationConfiguration")
    def redshift_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RedshiftDestinationConfigurationProperty"]]:
        '''An Amazon Redshift destination for the delivery stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RedshiftDestinationConfigurationProperty"]], jsii.get(self, "redshiftDestinationConfiguration"))

    @redshift_destination_configuration.setter
    def redshift_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RedshiftDestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9283febc90a4404b9eb41b227b6baf567d66cf4929f4f56dc67252a81e997f1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftDestinationConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="s3DestinationConfiguration")
    def s3_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]]:
        '''The ``S3DestinationConfiguration`` property type specifies an Amazon Simple Storage Service (Amazon S3) destination to which Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivers data.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]], jsii.get(self, "s3DestinationConfiguration"))

    @s3_destination_configuration.setter
    def s3_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb8b949ac7c9700a5ef03cddf3b3be451041166fe7583faee720a903b17ffd7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3DestinationConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="snowflakeDestinationConfiguration")
    def snowflake_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeDestinationConfigurationProperty"]]:
        '''Configure Snowflake destination.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeDestinationConfigurationProperty"]], jsii.get(self, "snowflakeDestinationConfiguration"))

    @snowflake_destination_configuration.setter
    def snowflake_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeDestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4334e067c783ee048616b856f03ad5fb828c1a4c18bbdce130d9850ac2ce4034)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snowflakeDestinationConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="splunkDestinationConfiguration")
    def splunk_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SplunkDestinationConfigurationProperty"]]:
        '''The configuration of a destination in Splunk for the delivery stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SplunkDestinationConfigurationProperty"]], jsii.get(self, "splunkDestinationConfiguration"))

    @splunk_destination_configuration.setter
    def splunk_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SplunkDestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1143a0f5e018d10fdc1fff0bbcada0e3653e2264078be8b5a6441f6918b95c91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "splunkDestinationConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A set of tags to assign to the Firehose stream.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b611aca673873100e4f1f1366dada7f80beaecdafd39582bd00fb48881dca276)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessBufferingHintsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interval_in_seconds": "intervalInSeconds",
            "size_in_m_bs": "sizeInMBs",
        },
    )
    class AmazonOpenSearchServerlessBufferingHintsProperty:
        def __init__(
            self,
            *,
            interval_in_seconds: typing.Optional[jsii.Number] = None,
            size_in_m_bs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes the buffering to perform before delivering data to the Serverless offering for Amazon OpenSearch Service destination.

            :param interval_in_seconds: Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).
            :param size_in_m_bs: Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                amazon_open_search_serverless_buffering_hints_property = kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessBufferingHintsProperty(
                    interval_in_seconds=123,
                    size_in_mBs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__73b3806edee327ffa718f826cdd3f2971c613586675003f856582bd7f9f0990b)
                check_type(argname="argument interval_in_seconds", value=interval_in_seconds, expected_type=type_hints["interval_in_seconds"])
                check_type(argname="argument size_in_m_bs", value=size_in_m_bs, expected_type=type_hints["size_in_m_bs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if interval_in_seconds is not None:
                self._values["interval_in_seconds"] = interval_in_seconds
            if size_in_m_bs is not None:
                self._values["size_in_m_bs"] = size_in_m_bs

        @builtins.property
        def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination.

            The default value is 300 (5 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints-intervalinseconds
            '''
            result = self._values.get("interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size_in_m_bs(self) -> typing.Optional[jsii.Number]:
            '''Buffer incoming data to the specified size, in MBs, before delivering it to the destination.

            The default value is 5.

            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints-sizeinmbs
            '''
            result = self._values.get("size_in_m_bs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonOpenSearchServerlessBufferingHintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "index_name": "indexName",
            "role_arn": "roleArn",
            "s3_configuration": "s3Configuration",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "collection_endpoint": "collectionEndpoint",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_mode": "s3BackupMode",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class AmazonOpenSearchServerlessDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            index_name: builtins.str,
            role_arn: builtins.str,
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.AmazonOpenSearchServerlessBufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            collection_endpoint: typing.Optional[builtins.str] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.AmazonOpenSearchServerlessRetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
            vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.VpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes the configuration of a destination in the Serverless offering for Amazon OpenSearch Service.

            :param index_name: The Serverless offering for Amazon OpenSearch Service index name.
            :param role_arn: The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Serverless offering for Amazon OpenSearch Service Configuration API and for indexing documents.
            :param s3_configuration: 
            :param buffering_hints: The buffering options. If no value is specified, the default values for AmazonopensearchserviceBufferingHints are used.
            :param cloud_watch_logging_options: 
            :param collection_endpoint: The endpoint to use when communicating with the collection in the Serverless offering for Amazon OpenSearch Service.
            :param processing_configuration: 
            :param retry_options: The retry behavior in case Firehose is unable to deliver documents to the Serverless offering for Amazon OpenSearch Service. The default value is 300 (5 minutes).
            :param s3_backup_mode: Defines how documents should be delivered to Amazon S3. When it is set to FailedDocumentsOnly, Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with AmazonOpenSearchService-failed/ appended to the key prefix. When set to AllDocuments, Firehose delivers all incoming records to Amazon S3, and also writes failed documents with AmazonOpenSearchService-failed/ appended to the prefix.
            :param vpc_configuration: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                amazon_open_search_serverless_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty(
                    index_name="indexName",
                    role_arn="roleArn",
                    s3_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessBufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    collection_endpoint="collectionEndpoint",
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    retry_options=kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessRetryOptionsProperty(
                        duration_in_seconds=123
                    ),
                    s3_backup_mode="s3BackupMode",
                    vpc_configuration=kinesisfirehose.CfnDeliveryStream.VpcConfigurationProperty(
                        role_arn="roleArn",
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c09d95c569c785593bec028509479a3c62ff0333544fe7fb6ea165082930dcf0)
                check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument collection_endpoint", value=collection_endpoint, expected_type=type_hints["collection_endpoint"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
                check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "index_name": index_name,
                "role_arn": role_arn,
                "s3_configuration": s3_configuration,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if collection_endpoint is not None:
                self._values["collection_endpoint"] = collection_endpoint
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode
            if vpc_configuration is not None:
                self._values["vpc_configuration"] = vpc_configuration

        @builtins.property
        def index_name(self) -> builtins.str:
            '''The Serverless offering for Amazon OpenSearch Service index name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-indexname
            '''
            result = self._values.get("index_name")
            assert result is not None, "Required property 'index_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Serverless offering for Amazon OpenSearch Service Configuration API and for indexing documents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonOpenSearchServerlessBufferingHintsProperty"]]:
            '''The buffering options.

            If no value is specified, the default values for AmazonopensearchserviceBufferingHints are used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonOpenSearchServerlessBufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def collection_endpoint(self) -> typing.Optional[builtins.str]:
            '''The endpoint to use when communicating with the collection in the Serverless offering for Amazon OpenSearch Service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-collectionendpoint
            '''
            result = self._values.get("collection_endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonOpenSearchServerlessRetryOptionsProperty"]]:
            '''The retry behavior in case Firehose is unable to deliver documents to the Serverless offering for Amazon OpenSearch Service.

            The default value is 300 (5 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonOpenSearchServerlessRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''Defines how documents should be delivered to Amazon S3.

            When it is set to FailedDocumentsOnly, Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with AmazonOpenSearchService-failed/ appended to the key prefix. When set to AllDocuments, Firehose delivers all incoming records to Amazon S3, and also writes failed documents with AmazonOpenSearchService-failed/ appended to the prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.VpcConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.VpcConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonOpenSearchServerlessDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class AmazonOpenSearchServerlessRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configures retry behavior in case Firehose is unable to deliver documents to the Serverless offering for Amazon OpenSearch Service.

            :param duration_in_seconds: After an initial failure to deliver to the Serverless offering for Amazon OpenSearch Service, the total amount of time during which Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessretryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                amazon_open_search_serverless_retry_options_property = kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessRetryOptionsProperty(
                    duration_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__753f83f6d86f1797776bc00b3eb90cc19e80bd47ed33370727e5209255714a3b)
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''After an initial failure to deliver to the Serverless offering for Amazon OpenSearch Service, the total amount of time during which Firehose retries delivery (including the first attempt).

            After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessretryoptions.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonOpenSearchServerlessRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interval_in_seconds": "intervalInSeconds",
            "size_in_m_bs": "sizeInMBs",
        },
    )
    class AmazonopensearchserviceBufferingHintsProperty:
        def __init__(
            self,
            *,
            interval_in_seconds: typing.Optional[jsii.Number] = None,
            size_in_m_bs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes the buffering to perform before delivering data to the Amazon OpenSearch Service destination.

            :param interval_in_seconds: Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).
            :param size_in_m_bs: Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                amazonopensearchservice_buffering_hints_property = kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty(
                    interval_in_seconds=123,
                    size_in_mBs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4bc008db5e34e3ef0ac28740f5aa52a90ec2c2ec0ebeb06a2e361e737f34b840)
                check_type(argname="argument interval_in_seconds", value=interval_in_seconds, expected_type=type_hints["interval_in_seconds"])
                check_type(argname="argument size_in_m_bs", value=size_in_m_bs, expected_type=type_hints["size_in_m_bs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if interval_in_seconds is not None:
                self._values["interval_in_seconds"] = interval_in_seconds
            if size_in_m_bs is not None:
                self._values["size_in_m_bs"] = size_in_m_bs

        @builtins.property
        def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination.

            The default value is 300 (5 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints-intervalinseconds
            '''
            result = self._values.get("interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size_in_m_bs(self) -> typing.Optional[jsii.Number]:
            '''Buffer incoming data to the specified size, in MBs, before delivering it to the destination.

            The default value is 5. We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints-sizeinmbs
            '''
            result = self._values.get("size_in_m_bs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonopensearchserviceBufferingHintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "index_name": "indexName",
            "role_arn": "roleArn",
            "s3_configuration": "s3Configuration",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "cluster_endpoint": "clusterEndpoint",
            "document_id_options": "documentIdOptions",
            "domain_arn": "domainArn",
            "index_rotation_period": "indexRotationPeriod",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_mode": "s3BackupMode",
            "type_name": "typeName",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class AmazonopensearchserviceDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            index_name: builtins.str,
            role_arn: builtins.str,
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cluster_endpoint: typing.Optional[builtins.str] = None,
            document_id_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DocumentIdOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            domain_arn: typing.Optional[builtins.str] = None,
            index_rotation_period: typing.Optional[builtins.str] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
            type_name: typing.Optional[builtins.str] = None,
            vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.VpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes the configuration of a destination in Amazon OpenSearch Service.

            :param index_name: The Amazon OpenSearch Service index name.
            :param role_arn: The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for calling the Amazon OpenSearch Service Configuration API and for indexing documents.
            :param s3_configuration: Describes the configuration of a destination in Amazon S3.
            :param buffering_hints: The buffering options. If no value is specified, the default values for AmazonopensearchserviceBufferingHints are used.
            :param cloud_watch_logging_options: Describes the Amazon CloudWatch logging options for your delivery stream.
            :param cluster_endpoint: The endpoint to use when communicating with the cluster. Specify either this ClusterEndpoint or the DomainARN field.
            :param document_id_options: Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.
            :param domain_arn: The ARN of the Amazon OpenSearch Service domain.
            :param index_rotation_period: The Amazon OpenSearch Service index rotation period. Index rotation appends a timestamp to the IndexName to facilitate the expiration of old data.
            :param processing_configuration: Describes a data processing configuration.
            :param retry_options: The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon OpenSearch Service. The default value is 300 (5 minutes).
            :param s3_backup_mode: Defines how documents should be delivered to Amazon S3.
            :param type_name: The Amazon OpenSearch Service type name.
            :param vpc_configuration: The details of the VPC of the Amazon OpenSearch Service destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                amazonopensearchservice_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty(
                    index_name="indexName",
                    role_arn="roleArn",
                    s3_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    cluster_endpoint="clusterEndpoint",
                    document_id_options=kinesisfirehose.CfnDeliveryStream.DocumentIdOptionsProperty(
                        default_document_id_format="defaultDocumentIdFormat"
                    ),
                    domain_arn="domainArn",
                    index_rotation_period="indexRotationPeriod",
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    retry_options=kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty(
                        duration_in_seconds=123
                    ),
                    s3_backup_mode="s3BackupMode",
                    type_name="typeName",
                    vpc_configuration=kinesisfirehose.CfnDeliveryStream.VpcConfigurationProperty(
                        role_arn="roleArn",
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fd4e3bfe32a6bde0a79abfda5de58ef25a59c29217c39eadcd363cb781608bca)
                check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument cluster_endpoint", value=cluster_endpoint, expected_type=type_hints["cluster_endpoint"])
                check_type(argname="argument document_id_options", value=document_id_options, expected_type=type_hints["document_id_options"])
                check_type(argname="argument domain_arn", value=domain_arn, expected_type=type_hints["domain_arn"])
                check_type(argname="argument index_rotation_period", value=index_rotation_period, expected_type=type_hints["index_rotation_period"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
                check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
                check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "index_name": index_name,
                "role_arn": role_arn,
                "s3_configuration": s3_configuration,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if cluster_endpoint is not None:
                self._values["cluster_endpoint"] = cluster_endpoint
            if document_id_options is not None:
                self._values["document_id_options"] = document_id_options
            if domain_arn is not None:
                self._values["domain_arn"] = domain_arn
            if index_rotation_period is not None:
                self._values["index_rotation_period"] = index_rotation_period
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode
            if type_name is not None:
                self._values["type_name"] = type_name
            if vpc_configuration is not None:
                self._values["vpc_configuration"] = vpc_configuration

        @builtins.property
        def index_name(self) -> builtins.str:
            '''The Amazon OpenSearch Service index name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-indexname
            '''
            result = self._values.get("index_name")
            assert result is not None, "Required property 'index_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for calling the Amazon OpenSearch Service Configuration API and for indexing documents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''Describes the configuration of a destination in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty"]]:
            '''The buffering options.

            If no value is specified, the default values for AmazonopensearchserviceBufferingHints are used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''Describes the Amazon CloudWatch logging options for your delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def cluster_endpoint(self) -> typing.Optional[builtins.str]:
            '''The endpoint to use when communicating with the cluster.

            Specify either this ClusterEndpoint or the DomainARN field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-clusterendpoint
            '''
            result = self._values.get("cluster_endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def document_id_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DocumentIdOptionsProperty"]]:
            '''Indicates the method for setting up document ID.

            The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-documentidoptions
            '''
            result = self._values.get("document_id_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DocumentIdOptionsProperty"]], result)

        @builtins.property
        def domain_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Amazon OpenSearch Service domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-domainarn
            '''
            result = self._values.get("domain_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def index_rotation_period(self) -> typing.Optional[builtins.str]:
            '''The Amazon OpenSearch Service index rotation period.

            Index rotation appends a timestamp to the IndexName to facilitate the expiration of old data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-indexrotationperiod
            '''
            result = self._values.get("index_rotation_period")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''Describes a data processing configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty"]]:
            '''The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon OpenSearch Service.

            The default value is 300 (5 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''Defines how documents should be delivered to Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type_name(self) -> typing.Optional[builtins.str]:
            '''The Amazon OpenSearch Service type name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-typename
            '''
            result = self._values.get("type_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.VpcConfigurationProperty"]]:
            '''The details of the VPC of the Amazon OpenSearch Service destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.VpcConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonopensearchserviceDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class AmazonopensearchserviceRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configures retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon OpenSearch Service.

            :param duration_in_seconds: After an initial failure to deliver to Amazon OpenSearch Service, the total amount of time during which Kinesis Data Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                amazonopensearchservice_retry_options_property = kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty(
                    duration_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3a6adce37d15471d3dfb2f014a8d32c640e5a4f535c6da724e3b743675a04cb)
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''After an initial failure to deliver to Amazon OpenSearch Service, the total amount of time during which Kinesis Data Firehose retries delivery (including the first attempt).

            After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonopensearchserviceRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.AuthenticationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"connectivity": "connectivity", "role_arn": "roleArn"},
    )
    class AuthenticationConfigurationProperty:
        def __init__(
            self,
            *,
            connectivity: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''The authentication configuration of the Amazon MSK cluster.

            :param connectivity: The type of connectivity used to access the Amazon MSK cluster.
            :param role_arn: The ARN of the role used to access the Amazon MSK cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                authentication_configuration_property = kinesisfirehose.CfnDeliveryStream.AuthenticationConfigurationProperty(
                    connectivity="connectivity",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__68e16a68225e493cf684cc2bfb151ded05293f2e7b47087f4a97398a1bfeaeb0)
                check_type(argname="argument connectivity", value=connectivity, expected_type=type_hints["connectivity"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connectivity": connectivity,
                "role_arn": role_arn,
            }

        @builtins.property
        def connectivity(self) -> builtins.str:
            '''The type of connectivity used to access the Amazon MSK cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration.html#cfn-kinesisfirehose-deliverystream-authenticationconfiguration-connectivity
            '''
            result = self._values.get("connectivity")
            assert result is not None, "Required property 'connectivity' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role used to access the Amazon MSK cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration.html#cfn-kinesisfirehose-deliverystream-authenticationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthenticationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interval_in_seconds": "intervalInSeconds",
            "size_in_m_bs": "sizeInMBs",
        },
    )
    class BufferingHintsProperty:
        def __init__(
            self,
            *,
            interval_in_seconds: typing.Optional[jsii.Number] = None,
            size_in_m_bs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ``BufferingHints`` property type specifies how Amazon Kinesis Data Firehose (Kinesis Data Firehose) buffers incoming data before delivering it to the destination.

            The first buffer condition that is satisfied triggers Kinesis Data Firehose to deliver the data.

            :param interval_in_seconds: The length of time, in seconds, that Kinesis Data Firehose buffers incoming data before delivering it to the destination. For valid values, see the ``IntervalInSeconds`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .
            :param size_in_m_bs: The size of the buffer, in MBs, that Kinesis Data Firehose uses for incoming data before delivering it to the destination. For valid values, see the ``SizeInMBs`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                buffering_hints_property = kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                    interval_in_seconds=123,
                    size_in_mBs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c672d0753e4b959e46f98cc809bc2380cd7be551cc9bab6f1b7baa1d203a6f7d)
                check_type(argname="argument interval_in_seconds", value=interval_in_seconds, expected_type=type_hints["interval_in_seconds"])
                check_type(argname="argument size_in_m_bs", value=size_in_m_bs, expected_type=type_hints["size_in_m_bs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if interval_in_seconds is not None:
                self._values["interval_in_seconds"] = interval_in_seconds
            if size_in_m_bs is not None:
                self._values["size_in_m_bs"] = size_in_m_bs

        @builtins.property
        def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The length of time, in seconds, that Kinesis Data Firehose buffers incoming data before delivering it to the destination.

            For valid values, see the ``IntervalInSeconds`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html#cfn-kinesisfirehose-deliverystream-bufferinghints-intervalinseconds
            '''
            result = self._values.get("interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size_in_m_bs(self) -> typing.Optional[jsii.Number]:
            '''The size of the buffer, in MBs, that Kinesis Data Firehose uses for incoming data before delivering it to the destination.

            For valid values, see the ``SizeInMBs`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html#cfn-kinesisfirehose-deliverystream-bufferinghints-sizeinmbs
            '''
            result = self._values.get("size_in_m_bs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BufferingHintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.CatalogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_arn": "catalogArn",
            "warehouse_location": "warehouseLocation",
        },
    )
    class CatalogConfigurationProperty:
        def __init__(
            self,
            *,
            catalog_arn: typing.Optional[builtins.str] = None,
            warehouse_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the containers where the destination Apache Iceberg Tables are persisted.

            :param catalog_arn: Specifies the Glue catalog ARN identifier of the destination Apache Iceberg Tables. You must specify the ARN in the format ``arn:aws:glue:region:account-id:catalog`` .
            :param warehouse_location: The warehouse location for Apache Iceberg tables. You must configure this when schema evolution and table creation is enabled. Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-catalogconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                catalog_configuration_property = kinesisfirehose.CfnDeliveryStream.CatalogConfigurationProperty(
                    catalog_arn="catalogArn",
                    warehouse_location="warehouseLocation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__92b3c1717fb66856049eddd62f0c12dbf945ae8d9450b716e7d065a04359aee0)
                check_type(argname="argument catalog_arn", value=catalog_arn, expected_type=type_hints["catalog_arn"])
                check_type(argname="argument warehouse_location", value=warehouse_location, expected_type=type_hints["warehouse_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if catalog_arn is not None:
                self._values["catalog_arn"] = catalog_arn
            if warehouse_location is not None:
                self._values["warehouse_location"] = warehouse_location

        @builtins.property
        def catalog_arn(self) -> typing.Optional[builtins.str]:
            '''Specifies the Glue catalog ARN identifier of the destination Apache Iceberg Tables.

            You must specify the ARN in the format ``arn:aws:glue:region:account-id:catalog`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-catalogconfiguration.html#cfn-kinesisfirehose-deliverystream-catalogconfiguration-catalogarn
            '''
            result = self._values.get("catalog_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def warehouse_location(self) -> typing.Optional[builtins.str]:
            '''The warehouse location for Apache Iceberg tables. You must configure this when schema evolution and table creation is enabled.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-catalogconfiguration.html#cfn-kinesisfirehose-deliverystream-catalogconfiguration-warehouselocation
            '''
            result = self._values.get("warehouse_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CatalogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "log_group_name": "logGroupName",
            "log_stream_name": "logStreamName",
        },
    )
    class CloudWatchLoggingOptionsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            log_group_name: typing.Optional[builtins.str] = None,
            log_stream_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``CloudWatchLoggingOptions`` property type specifies Amazon CloudWatch Logs (CloudWatch Logs) logging options that Amazon Kinesis Data Firehose (Kinesis Data Firehose) uses for the delivery stream.

            :param enabled: Indicates whether CloudWatch Logs logging is enabled.
            :param log_group_name: The name of the CloudWatch Logs log group that contains the log stream that Kinesis Data Firehose will use. Conditional. If you enable logging, you must specify this property.
            :param log_stream_name: The name of the CloudWatch Logs log stream that Kinesis Data Firehose uses to send logs about data delivery. Conditional. If you enable logging, you must specify this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                cloud_watch_logging_options_property = kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                    enabled=False,
                    log_group_name="logGroupName",
                    log_stream_name="logStreamName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0992b1c8af7fd8e057904e94d1f683be6233929613125517587cd51de86aa4b5)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
                check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name
            if log_stream_name is not None:
                self._values["log_stream_name"] = log_stream_name

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether CloudWatch Logs logging is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''The name of the CloudWatch Logs log group that contains the log stream that Kinesis Data Firehose will use.

            Conditional. If you enable logging, you must specify this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_stream_name(self) -> typing.Optional[builtins.str]:
            '''The name of the CloudWatch Logs log stream that Kinesis Data Firehose uses to send logs about data delivery.

            Conditional. If you enable logging, you must specify this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-logstreamname
            '''
            result = self._values.get("log_stream_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLoggingOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.CopyCommandProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_table_name": "dataTableName",
            "copy_options": "copyOptions",
            "data_table_columns": "dataTableColumns",
        },
    )
    class CopyCommandProperty:
        def __init__(
            self,
            *,
            data_table_name: builtins.str,
            copy_options: typing.Optional[builtins.str] = None,
            data_table_columns: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``CopyCommand`` property type configures the Amazon Redshift ``COPY`` command that Amazon Kinesis Data Firehose (Kinesis Data Firehose) uses to load data into an Amazon Redshift cluster from an Amazon S3 bucket.

            :param data_table_name: The name of the target table. The table must already exist in the database.
            :param copy_options: Parameters to use with the Amazon Redshift ``COPY`` command. For examples, see the ``CopyOptions`` content for the `CopyCommand <https://docs.aws.amazon.com/firehose/latest/APIReference/API_CopyCommand.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .
            :param data_table_columns: A comma-separated list of column names.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                copy_command_property = kinesisfirehose.CfnDeliveryStream.CopyCommandProperty(
                    data_table_name="dataTableName",
                
                    # the properties below are optional
                    copy_options="copyOptions",
                    data_table_columns="dataTableColumns"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ed6eb88a63ca5e75a449863a292b3dcd0cbfcd3127e73f575819aaf579cc41f)
                check_type(argname="argument data_table_name", value=data_table_name, expected_type=type_hints["data_table_name"])
                check_type(argname="argument copy_options", value=copy_options, expected_type=type_hints["copy_options"])
                check_type(argname="argument data_table_columns", value=data_table_columns, expected_type=type_hints["data_table_columns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_table_name": data_table_name,
            }
            if copy_options is not None:
                self._values["copy_options"] = copy_options
            if data_table_columns is not None:
                self._values["data_table_columns"] = data_table_columns

        @builtins.property
        def data_table_name(self) -> builtins.str:
            '''The name of the target table.

            The table must already exist in the database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-datatablename
            '''
            result = self._values.get("data_table_name")
            assert result is not None, "Required property 'data_table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def copy_options(self) -> typing.Optional[builtins.str]:
            '''Parameters to use with the Amazon Redshift ``COPY`` command.

            For examples, see the ``CopyOptions`` content for the `CopyCommand <https://docs.aws.amazon.com/firehose/latest/APIReference/API_CopyCommand.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-copyoptions
            '''
            result = self._values.get("copy_options")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_table_columns(self) -> typing.Optional[builtins.str]:
            '''A comma-separated list of column names.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-datatablecolumns
            '''
            result = self._values.get("data_table_columns")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CopyCommandProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DataFormatConversionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "input_format_configuration": "inputFormatConfiguration",
            "output_format_configuration": "outputFormatConfiguration",
            "schema_configuration": "schemaConfiguration",
        },
    )
    class DataFormatConversionConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            input_format_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.InputFormatConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            output_format_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.OutputFormatConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            schema_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SchemaConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies that you want Kinesis Data Firehose to convert data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.

            Kinesis Data Firehose uses the serializer and deserializer that you specify, in addition to the column information from the AWS Glue table, to deserialize your input data from JSON and then serialize it to the Parquet or ORC format. For more information, see `Kinesis Data Firehose Record Format Conversion <https://docs.aws.amazon.com/firehose/latest/dev/record-format-conversion.html>`_ .

            :param enabled: Defaults to ``true`` . Set it to ``false`` if you want to disable format conversion while preserving the configuration details.
            :param input_format_configuration: Specifies the deserializer that you want Firehose to use to convert the format of your data from JSON. This parameter is required if ``Enabled`` is set to true.
            :param output_format_configuration: Specifies the serializer that you want Firehose to use to convert the format of your data to the Parquet or ORC format. This parameter is required if ``Enabled`` is set to true.
            :param schema_configuration: Specifies the AWS Glue Data Catalog table that contains the column information. This parameter is required if ``Enabled`` is set to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                data_format_conversion_configuration_property = kinesisfirehose.CfnDeliveryStream.DataFormatConversionConfigurationProperty(
                    enabled=False,
                    input_format_configuration=kinesisfirehose.CfnDeliveryStream.InputFormatConfigurationProperty(
                        deserializer=kinesisfirehose.CfnDeliveryStream.DeserializerProperty(
                            hive_json_ser_de=kinesisfirehose.CfnDeliveryStream.HiveJsonSerDeProperty(
                                timestamp_formats=["timestampFormats"]
                            ),
                            open_xJson_ser_de=kinesisfirehose.CfnDeliveryStream.OpenXJsonSerDeProperty(
                                case_insensitive=False,
                                column_to_json_key_mappings={
                                    "column_to_json_key_mappings_key": "columnToJsonKeyMappings"
                                },
                                convert_dots_in_json_keys_to_underscores=False
                            )
                        )
                    ),
                    output_format_configuration=kinesisfirehose.CfnDeliveryStream.OutputFormatConfigurationProperty(
                        serializer=kinesisfirehose.CfnDeliveryStream.SerializerProperty(
                            orc_ser_de=kinesisfirehose.CfnDeliveryStream.OrcSerDeProperty(
                                block_size_bytes=123,
                                bloom_filter_columns=["bloomFilterColumns"],
                                bloom_filter_false_positive_probability=123,
                                compression="compression",
                                dictionary_key_threshold=123,
                                enable_padding=False,
                                format_version="formatVersion",
                                padding_tolerance=123,
                                row_index_stride=123,
                                stripe_size_bytes=123
                            ),
                            parquet_ser_de=kinesisfirehose.CfnDeliveryStream.ParquetSerDeProperty(
                                block_size_bytes=123,
                                compression="compression",
                                enable_dictionary_compression=False,
                                max_padding_bytes=123,
                                page_size_bytes=123,
                                writer_version="writerVersion"
                            )
                        )
                    ),
                    schema_configuration=kinesisfirehose.CfnDeliveryStream.SchemaConfigurationProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        region="region",
                        role_arn="roleArn",
                        table_name="tableName",
                        version_id="versionId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d2fd0a4fb437e036bd2436bcfd397fa35f08aba48c5a25c4aac36dedb0d37e42)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument input_format_configuration", value=input_format_configuration, expected_type=type_hints["input_format_configuration"])
                check_type(argname="argument output_format_configuration", value=output_format_configuration, expected_type=type_hints["output_format_configuration"])
                check_type(argname="argument schema_configuration", value=schema_configuration, expected_type=type_hints["schema_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if input_format_configuration is not None:
                self._values["input_format_configuration"] = input_format_configuration
            if output_format_configuration is not None:
                self._values["output_format_configuration"] = output_format_configuration
            if schema_configuration is not None:
                self._values["schema_configuration"] = schema_configuration

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Defaults to ``true`` .

            Set it to ``false`` if you want to disable format conversion while preserving the configuration details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def input_format_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.InputFormatConfigurationProperty"]]:
            '''Specifies the deserializer that you want Firehose to use to convert the format of your data from JSON.

            This parameter is required if ``Enabled`` is set to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-inputformatconfiguration
            '''
            result = self._values.get("input_format_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.InputFormatConfigurationProperty"]], result)

        @builtins.property
        def output_format_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.OutputFormatConfigurationProperty"]]:
            '''Specifies the serializer that you want Firehose to use to convert the format of your data to the Parquet or ORC format.

            This parameter is required if ``Enabled`` is set to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-outputformatconfiguration
            '''
            result = self._values.get("output_format_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.OutputFormatConfigurationProperty"]], result)

        @builtins.property
        def schema_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SchemaConfigurationProperty"]]:
            '''Specifies the AWS Glue Data Catalog table that contains the column information.

            This parameter is required if ``Enabled`` is set to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-schemaconfiguration
            '''
            result = self._values.get("schema_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SchemaConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataFormatConversionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DatabaseColumnsProperty",
        jsii_struct_bases=[],
        name_mapping={"exclude": "exclude", "include": "include"},
    )
    class DatabaseColumnsProperty:
        def __init__(
            self,
            *,
            exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
            include: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param exclude: 
            :param include: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasecolumns.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                database_columns_property = kinesisfirehose.CfnDeliveryStream.DatabaseColumnsProperty(
                    exclude=["exclude"],
                    include=["include"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__111648b092f5dd75408d33db5fb1adea30dc7a8b58549cef95459f9224ccb26a)
                check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
                check_type(argname="argument include", value=include, expected_type=type_hints["include"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if exclude is not None:
                self._values["exclude"] = exclude
            if include is not None:
                self._values["include"] = include

        @builtins.property
        def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasecolumns.html#cfn-kinesisfirehose-deliverystream-databasecolumns-exclude
            '''
            result = self._values.get("exclude")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def include(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasecolumns.html#cfn-kinesisfirehose-deliverystream-databasecolumns-include
            '''
            result = self._values.get("include")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseColumnsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DatabaseSourceAuthenticationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"secrets_manager_configuration": "secretsManagerConfiguration"},
    )
    class DatabaseSourceAuthenticationConfigurationProperty:
        def __init__(
            self,
            *,
            secrets_manager_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SecretsManagerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The structure to configure the authentication methods for Firehose to connect to source database endpoint.

            Amazon Data Firehose is in preview release and is subject to change.

            :param secrets_manager_configuration: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceauthenticationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                database_source_authentication_configuration_property = kinesisfirehose.CfnDeliveryStream.DatabaseSourceAuthenticationConfigurationProperty(
                    secrets_manager_configuration=kinesisfirehose.CfnDeliveryStream.SecretsManagerConfigurationProperty(
                        enabled=False,
                
                        # the properties below are optional
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cecf7807b45586be03c0bc76f8fcdf6ad93c6bd34a795d26aeaf365dd3d297c4)
                check_type(argname="argument secrets_manager_configuration", value=secrets_manager_configuration, expected_type=type_hints["secrets_manager_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "secrets_manager_configuration": secrets_manager_configuration,
            }

        @builtins.property
        def secrets_manager_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SecretsManagerConfigurationProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceauthenticationconfiguration.html#cfn-kinesisfirehose-deliverystream-databasesourceauthenticationconfiguration-secretsmanagerconfiguration
            '''
            result = self._values.get("secrets_manager_configuration")
            assert result is not None, "Required property 'secrets_manager_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SecretsManagerConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseSourceAuthenticationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DatabaseSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "databases": "databases",
            "database_source_authentication_configuration": "databaseSourceAuthenticationConfiguration",
            "database_source_vpc_configuration": "databaseSourceVpcConfiguration",
            "endpoint": "endpoint",
            "port": "port",
            "snapshot_watermark_table": "snapshotWatermarkTable",
            "tables": "tables",
            "type": "type",
            "columns": "columns",
            "digest": "digest",
            "public_certificate": "publicCertificate",
            "ssl_mode": "sslMode",
            "surrogate_keys": "surrogateKeys",
        },
    )
    class DatabaseSourceConfigurationProperty:
        def __init__(
            self,
            *,
            databases: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DatabasesProperty", typing.Dict[builtins.str, typing.Any]]],
            database_source_authentication_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DatabaseSourceAuthenticationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            database_source_vpc_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DatabaseSourceVPCConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            endpoint: builtins.str,
            port: jsii.Number,
            snapshot_watermark_table: builtins.str,
            tables: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DatabaseTablesProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
            columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DatabaseColumnsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            digest: typing.Optional[builtins.str] = None,
            public_certificate: typing.Optional[builtins.str] = None,
            ssl_mode: typing.Optional[builtins.str] = None,
            surrogate_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The top level object for configuring streams with database as a source.

            Amazon Data Firehose is in preview release and is subject to change.

            :param databases: The list of database patterns in source database endpoint for Firehose to read from. Amazon Data Firehose is in preview release and is subject to change.
            :param database_source_authentication_configuration: The structure to configure the authentication methods for Firehose to connect to source database endpoint. Amazon Data Firehose is in preview release and is subject to change.
            :param database_source_vpc_configuration: The details of the VPC Endpoint Service which Firehose uses to create a PrivateLink to the database. Amazon Data Firehose is in preview release and is subject to change.
            :param endpoint: The endpoint of the database server. Amazon Data Firehose is in preview release and is subject to change.
            :param port: The port of the database. This can be one of the following values. - 3306 for MySQL database type - 5432 for PostgreSQL database type Amazon Data Firehose is in preview release and is subject to change.
            :param snapshot_watermark_table: The fully qualified name of the table in source database endpoint that Firehose uses to track snapshot progress. Amazon Data Firehose is in preview release and is subject to change.
            :param tables: The list of table patterns in source database endpoint for Firehose to read from. Amazon Data Firehose is in preview release and is subject to change.
            :param type: The type of database engine. This can be one of the following values. - MySQL - PostgreSQL Amazon Data Firehose is in preview release and is subject to change.
            :param columns: The list of column patterns in source database endpoint for Firehose to read from. Amazon Data Firehose is in preview release and is subject to change.
            :param digest: 
            :param public_certificate: 
            :param ssl_mode: The mode to enable or disable SSL when Firehose connects to the database endpoint. Amazon Data Firehose is in preview release and is subject to change.
            :param surrogate_keys: The optional list of table and column names used as unique key columns when taking snapshot if the tables don’t have primary keys configured. Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                database_source_configuration_property = kinesisfirehose.CfnDeliveryStream.DatabaseSourceConfigurationProperty(
                    databases=kinesisfirehose.CfnDeliveryStream.DatabasesProperty(
                        exclude=["exclude"],
                        include=["include"]
                    ),
                    database_source_authentication_configuration=kinesisfirehose.CfnDeliveryStream.DatabaseSourceAuthenticationConfigurationProperty(
                        secrets_manager_configuration=kinesisfirehose.CfnDeliveryStream.SecretsManagerConfigurationProperty(
                            enabled=False,
                
                            # the properties below are optional
                            role_arn="roleArn",
                            secret_arn="secretArn"
                        )
                    ),
                    database_source_vpc_configuration=kinesisfirehose.CfnDeliveryStream.DatabaseSourceVPCConfigurationProperty(
                        vpc_endpoint_service_name="vpcEndpointServiceName"
                    ),
                    endpoint="endpoint",
                    port=123,
                    snapshot_watermark_table="snapshotWatermarkTable",
                    tables=kinesisfirehose.CfnDeliveryStream.DatabaseTablesProperty(
                        exclude=["exclude"],
                        include=["include"]
                    ),
                    type="type",
                
                    # the properties below are optional
                    columns=kinesisfirehose.CfnDeliveryStream.DatabaseColumnsProperty(
                        exclude=["exclude"],
                        include=["include"]
                    ),
                    digest="digest",
                    public_certificate="publicCertificate",
                    ssl_mode="sslMode",
                    surrogate_keys=["surrogateKeys"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dfa32769046e99e73e35a8b5e878b72f25abcaa661bf955ff25e794601e2126d)
                check_type(argname="argument databases", value=databases, expected_type=type_hints["databases"])
                check_type(argname="argument database_source_authentication_configuration", value=database_source_authentication_configuration, expected_type=type_hints["database_source_authentication_configuration"])
                check_type(argname="argument database_source_vpc_configuration", value=database_source_vpc_configuration, expected_type=type_hints["database_source_vpc_configuration"])
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument snapshot_watermark_table", value=snapshot_watermark_table, expected_type=type_hints["snapshot_watermark_table"])
                check_type(argname="argument tables", value=tables, expected_type=type_hints["tables"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
                check_type(argname="argument digest", value=digest, expected_type=type_hints["digest"])
                check_type(argname="argument public_certificate", value=public_certificate, expected_type=type_hints["public_certificate"])
                check_type(argname="argument ssl_mode", value=ssl_mode, expected_type=type_hints["ssl_mode"])
                check_type(argname="argument surrogate_keys", value=surrogate_keys, expected_type=type_hints["surrogate_keys"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "databases": databases,
                "database_source_authentication_configuration": database_source_authentication_configuration,
                "database_source_vpc_configuration": database_source_vpc_configuration,
                "endpoint": endpoint,
                "port": port,
                "snapshot_watermark_table": snapshot_watermark_table,
                "tables": tables,
                "type": type,
            }
            if columns is not None:
                self._values["columns"] = columns
            if digest is not None:
                self._values["digest"] = digest
            if public_certificate is not None:
                self._values["public_certificate"] = public_certificate
            if ssl_mode is not None:
                self._values["ssl_mode"] = ssl_mode
            if surrogate_keys is not None:
                self._values["surrogate_keys"] = surrogate_keys

        @builtins.property
        def databases(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DatabasesProperty"]:
            '''The list of database patterns in source database endpoint for Firehose to read from.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.html#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-databases
            '''
            result = self._values.get("databases")
            assert result is not None, "Required property 'databases' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DatabasesProperty"], result)

        @builtins.property
        def database_source_authentication_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DatabaseSourceAuthenticationConfigurationProperty"]:
            '''The structure to configure the authentication methods for Firehose to connect to source database endpoint.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.html#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-databasesourceauthenticationconfiguration
            '''
            result = self._values.get("database_source_authentication_configuration")
            assert result is not None, "Required property 'database_source_authentication_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DatabaseSourceAuthenticationConfigurationProperty"], result)

        @builtins.property
        def database_source_vpc_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DatabaseSourceVPCConfigurationProperty"]:
            '''The details of the VPC Endpoint Service which Firehose uses to create a PrivateLink to the database.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.html#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-databasesourcevpcconfiguration
            '''
            result = self._values.get("database_source_vpc_configuration")
            assert result is not None, "Required property 'database_source_vpc_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DatabaseSourceVPCConfigurationProperty"], result)

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''The endpoint of the database server.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.html#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''The port of the database. This can be one of the following values.

            - 3306 for MySQL database type
            - 5432 for PostgreSQL database type

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.html#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def snapshot_watermark_table(self) -> builtins.str:
            '''The fully qualified name of the table in source database endpoint that Firehose uses to track snapshot progress.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.html#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-snapshotwatermarktable
            '''
            result = self._values.get("snapshot_watermark_table")
            assert result is not None, "Required property 'snapshot_watermark_table' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tables(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DatabaseTablesProperty"]:
            '''The list of table patterns in source database endpoint for Firehose to read from.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.html#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-tables
            '''
            result = self._values.get("tables")
            assert result is not None, "Required property 'tables' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DatabaseTablesProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of database engine. This can be one of the following values.

            - MySQL
            - PostgreSQL

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.html#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def columns(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DatabaseColumnsProperty"]]:
            '''The list of column patterns in source database endpoint for Firehose to read from.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.html#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-columns
            '''
            result = self._values.get("columns")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DatabaseColumnsProperty"]], result)

        @builtins.property
        def digest(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.html#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-digest
            '''
            result = self._values.get("digest")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def public_certificate(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.html#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-publiccertificate
            '''
            result = self._values.get("public_certificate")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssl_mode(self) -> typing.Optional[builtins.str]:
            '''The mode to enable or disable SSL when Firehose connects to the database endpoint.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.html#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-sslmode
            '''
            result = self._values.get("ssl_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def surrogate_keys(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The optional list of table and column names used as unique key columns when taking snapshot if the tables don’t have primary keys configured.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourceconfiguration.html#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration-surrogatekeys
            '''
            result = self._values.get("surrogate_keys")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DatabaseSourceVPCConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_endpoint_service_name": "vpcEndpointServiceName"},
    )
    class DatabaseSourceVPCConfigurationProperty:
        def __init__(self, *, vpc_endpoint_service_name: builtins.str) -> None:
            '''The structure for details of the VPC Endpoint Service which Firehose uses to create a PrivateLink to the database.

            Amazon Data Firehose is in preview release and is subject to change.

            :param vpc_endpoint_service_name: The VPC endpoint service name which Firehose uses to create a PrivateLink to the database. The endpoint service must have the Firehose service principle ``firehose.amazonaws.com`` as an allowed principal on the VPC endpoint service. The VPC endpoint service name is a string that looks like ``com.amazonaws.vpce.<region>.<vpc-endpoint-service-id>`` . Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourcevpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                database_source_vPCConfiguration_property = kinesisfirehose.CfnDeliveryStream.DatabaseSourceVPCConfigurationProperty(
                    vpc_endpoint_service_name="vpcEndpointServiceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4616b4a1f40a4e175751eda3777e82055e2397fd9dad0a6cd009c18c89e97cd3)
                check_type(argname="argument vpc_endpoint_service_name", value=vpc_endpoint_service_name, expected_type=type_hints["vpc_endpoint_service_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "vpc_endpoint_service_name": vpc_endpoint_service_name,
            }

        @builtins.property
        def vpc_endpoint_service_name(self) -> builtins.str:
            '''The VPC endpoint service name which Firehose uses to create a PrivateLink to the database.

            The endpoint service must have the Firehose service principle ``firehose.amazonaws.com`` as an allowed principal on the VPC endpoint service. The VPC endpoint service name is a string that looks like ``com.amazonaws.vpce.<region>.<vpc-endpoint-service-id>`` .

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasesourcevpcconfiguration.html#cfn-kinesisfirehose-deliverystream-databasesourcevpcconfiguration-vpcendpointservicename
            '''
            result = self._values.get("vpc_endpoint_service_name")
            assert result is not None, "Required property 'vpc_endpoint_service_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseSourceVPCConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DatabaseTablesProperty",
        jsii_struct_bases=[],
        name_mapping={"exclude": "exclude", "include": "include"},
    )
    class DatabaseTablesProperty:
        def __init__(
            self,
            *,
            exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
            include: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param exclude: 
            :param include: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasetables.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                database_tables_property = kinesisfirehose.CfnDeliveryStream.DatabaseTablesProperty(
                    exclude=["exclude"],
                    include=["include"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b669ca3e532e36dd3f6bf714eda78c90c8c90c4c1bc6dbebfab5c56e74950ddb)
                check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
                check_type(argname="argument include", value=include, expected_type=type_hints["include"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if exclude is not None:
                self._values["exclude"] = exclude
            if include is not None:
                self._values["include"] = include

        @builtins.property
        def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasetables.html#cfn-kinesisfirehose-deliverystream-databasetables-exclude
            '''
            result = self._values.get("exclude")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def include(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databasetables.html#cfn-kinesisfirehose-deliverystream-databasetables-include
            '''
            result = self._values.get("include")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseTablesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DatabasesProperty",
        jsii_struct_bases=[],
        name_mapping={"exclude": "exclude", "include": "include"},
    )
    class DatabasesProperty:
        def __init__(
            self,
            *,
            exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
            include: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param exclude: 
            :param include: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databases.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                databases_property = kinesisfirehose.CfnDeliveryStream.DatabasesProperty(
                    exclude=["exclude"],
                    include=["include"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b6aa9553c52b253113ab9a3fd740ae3235a38fc2d9a582fa85db01832e154931)
                check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
                check_type(argname="argument include", value=include, expected_type=type_hints["include"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if exclude is not None:
                self._values["exclude"] = exclude
            if include is not None:
                self._values["include"] = include

        @builtins.property
        def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databases.html#cfn-kinesisfirehose-deliverystream-databases-exclude
            '''
            result = self._values.get("exclude")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def include(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-databases.html#cfn-kinesisfirehose-deliverystream-databases-include
            '''
            result = self._values.get("include")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabasesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"key_type": "keyType", "key_arn": "keyArn"},
    )
    class DeliveryStreamEncryptionConfigurationInputProperty:
        def __init__(
            self,
            *,
            key_type: builtins.str,
            key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the type and Amazon Resource Name (ARN) of the CMK to use for Server-Side Encryption (SSE).

            :param key_type: Indicates the type of customer master key (CMK) to use for encryption. The default setting is ``AWS_OWNED_CMK`` . For more information about CMKs, see `Customer Master Keys (CMKs) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`_ . You can use a CMK of type CUSTOMER_MANAGED_CMK to encrypt up to 500 delivery streams. .. epigraph:: To encrypt your delivery stream, use symmetric CMKs. Kinesis Data Firehose doesn't support asymmetric CMKs. For information about symmetric and asymmetric CMKs, see `About Symmetric and Asymmetric CMKs <https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-concepts.html>`_ in the AWS Key Management Service developer guide.
            :param key_arn: If you set ``KeyType`` to ``CUSTOMER_MANAGED_CMK`` , you must specify the Amazon Resource Name (ARN) of the CMK. If you set ``KeyType`` to ``AWS _OWNED_CMK`` , Firehose uses a service-account CMK.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                delivery_stream_encryption_configuration_input_property = kinesisfirehose.CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty(
                    key_type="keyType",
                
                    # the properties below are optional
                    key_arn="keyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a51e3602fa39b19119cb43ff1945ccb136f7909bb7d76a42abc9195cb0d725a3)
                check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
                check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key_type": key_type,
            }
            if key_arn is not None:
                self._values["key_arn"] = key_arn

        @builtins.property
        def key_type(self) -> builtins.str:
            '''Indicates the type of customer master key (CMK) to use for encryption.

            The default setting is ``AWS_OWNED_CMK`` . For more information about CMKs, see `Customer Master Keys (CMKs) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`_ .

            You can use a CMK of type CUSTOMER_MANAGED_CMK to encrypt up to 500 delivery streams.
            .. epigraph::

               To encrypt your delivery stream, use symmetric CMKs. Kinesis Data Firehose doesn't support asymmetric CMKs. For information about symmetric and asymmetric CMKs, see `About Symmetric and Asymmetric CMKs <https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-concepts.html>`_ in the AWS Key Management Service developer guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keytype
            '''
            result = self._values.get("key_type")
            assert result is not None, "Required property 'key_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_arn(self) -> typing.Optional[builtins.str]:
            '''If you set ``KeyType`` to ``CUSTOMER_MANAGED_CMK`` , you must specify the Amazon Resource Name (ARN) of the CMK.

            If you set ``KeyType`` to ``AWS _OWNED_CMK`` , Firehose uses a service-account CMK.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keyarn
            '''
            result = self._values.get("key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeliveryStreamEncryptionConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DeserializerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hive_json_ser_de": "hiveJsonSerDe",
            "open_x_json_ser_de": "openXJsonSerDe",
        },
    )
    class DeserializerProperty:
        def __init__(
            self,
            *,
            hive_json_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.HiveJsonSerDeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            open_x_json_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.OpenXJsonSerDeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The deserializer you want Kinesis Data Firehose to use for converting the input data from JSON.

            Kinesis Data Firehose then serializes the data to its final format using the ``Serializer`` . Kinesis Data Firehose supports two types of deserializers: the `Apache Hive JSON SerDe <https://docs.aws.amazon.com/https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-JSON>`_ and the `OpenX JSON SerDe <https://docs.aws.amazon.com/https://github.com/rcongiu/Hive-JSON-Serde>`_ .

            :param hive_json_ser_de: The native Hive / HCatalog JsonSerDe. Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.
            :param open_x_json_ser_de: The OpenX SerDe. Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                deserializer_property = kinesisfirehose.CfnDeliveryStream.DeserializerProperty(
                    hive_json_ser_de=kinesisfirehose.CfnDeliveryStream.HiveJsonSerDeProperty(
                        timestamp_formats=["timestampFormats"]
                    ),
                    open_xJson_ser_de=kinesisfirehose.CfnDeliveryStream.OpenXJsonSerDeProperty(
                        case_insensitive=False,
                        column_to_json_key_mappings={
                            "column_to_json_key_mappings_key": "columnToJsonKeyMappings"
                        },
                        convert_dots_in_json_keys_to_underscores=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__42c1d0a7a47a7fb87bd171a324b5d6ec1a60f675aa066d295f3a321445b0d566)
                check_type(argname="argument hive_json_ser_de", value=hive_json_ser_de, expected_type=type_hints["hive_json_ser_de"])
                check_type(argname="argument open_x_json_ser_de", value=open_x_json_ser_de, expected_type=type_hints["open_x_json_ser_de"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if hive_json_ser_de is not None:
                self._values["hive_json_ser_de"] = hive_json_ser_de
            if open_x_json_ser_de is not None:
                self._values["open_x_json_ser_de"] = open_x_json_ser_de

        @builtins.property
        def hive_json_ser_de(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HiveJsonSerDeProperty"]]:
            '''The native Hive / HCatalog JsonSerDe.

            Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html#cfn-kinesisfirehose-deliverystream-deserializer-hivejsonserde
            '''
            result = self._values.get("hive_json_ser_de")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HiveJsonSerDeProperty"]], result)

        @builtins.property
        def open_x_json_ser_de(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.OpenXJsonSerDeProperty"]]:
            '''The OpenX SerDe.

            Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html#cfn-kinesisfirehose-deliverystream-deserializer-openxjsonserde
            '''
            result = self._values.get("open_x_json_ser_de")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.OpenXJsonSerDeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeserializerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DestinationTableConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_database_name": "destinationDatabaseName",
            "destination_table_name": "destinationTableName",
            "partition_spec": "partitionSpec",
            "s3_error_output_prefix": "s3ErrorOutputPrefix",
            "unique_keys": "uniqueKeys",
        },
    )
    class DestinationTableConfigurationProperty:
        def __init__(
            self,
            *,
            destination_database_name: builtins.str,
            destination_table_name: builtins.str,
            partition_spec: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.PartitionSpecProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_error_output_prefix: typing.Optional[builtins.str] = None,
            unique_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Describes the configuration of a destination in Apache Iceberg Tables.

            This section is only needed for tables where you want to update or delete data.

            :param destination_database_name: The name of the Apache Iceberg database.
            :param destination_table_name: Specifies the name of the Apache Iceberg Table.
            :param partition_spec: The partition spec configuration for a table that is used by automatic table creation. Amazon Data Firehose is in preview release and is subject to change.
            :param s3_error_output_prefix: The table specific S3 error output prefix. All the errors that occurred while delivering to this table will be prefixed with this value in S3 destination.
            :param unique_keys: A list of unique keys for a given Apache Iceberg table. Firehose will use these for running Create, Update, or Delete operations on the given Iceberg table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-destinationtableconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                destination_table_configuration_property = kinesisfirehose.CfnDeliveryStream.DestinationTableConfigurationProperty(
                    destination_database_name="destinationDatabaseName",
                    destination_table_name="destinationTableName",
                
                    # the properties below are optional
                    partition_spec=kinesisfirehose.CfnDeliveryStream.PartitionSpecProperty(
                        identity=[kinesisfirehose.CfnDeliveryStream.PartitionFieldProperty(
                            source_name="sourceName"
                        )]
                    ),
                    s3_error_output_prefix="s3ErrorOutputPrefix",
                    unique_keys=["uniqueKeys"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d9e156eb7fa7ea4dde332f5d2ef91909983b4fa7a5b5133510252f637465ea6c)
                check_type(argname="argument destination_database_name", value=destination_database_name, expected_type=type_hints["destination_database_name"])
                check_type(argname="argument destination_table_name", value=destination_table_name, expected_type=type_hints["destination_table_name"])
                check_type(argname="argument partition_spec", value=partition_spec, expected_type=type_hints["partition_spec"])
                check_type(argname="argument s3_error_output_prefix", value=s3_error_output_prefix, expected_type=type_hints["s3_error_output_prefix"])
                check_type(argname="argument unique_keys", value=unique_keys, expected_type=type_hints["unique_keys"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_database_name": destination_database_name,
                "destination_table_name": destination_table_name,
            }
            if partition_spec is not None:
                self._values["partition_spec"] = partition_spec
            if s3_error_output_prefix is not None:
                self._values["s3_error_output_prefix"] = s3_error_output_prefix
            if unique_keys is not None:
                self._values["unique_keys"] = unique_keys

        @builtins.property
        def destination_database_name(self) -> builtins.str:
            '''The name of the Apache Iceberg database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-destinationtableconfiguration.html#cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-destinationdatabasename
            '''
            result = self._values.get("destination_database_name")
            assert result is not None, "Required property 'destination_database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_table_name(self) -> builtins.str:
            '''Specifies the name of the Apache Iceberg Table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-destinationtableconfiguration.html#cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-destinationtablename
            '''
            result = self._values.get("destination_table_name")
            assert result is not None, "Required property 'destination_table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def partition_spec(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.PartitionSpecProperty"]]:
            '''The partition spec configuration for a table that is used by automatic table creation.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-destinationtableconfiguration.html#cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-partitionspec
            '''
            result = self._values.get("partition_spec")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.PartitionSpecProperty"]], result)

        @builtins.property
        def s3_error_output_prefix(self) -> typing.Optional[builtins.str]:
            '''The table specific S3 error output prefix.

            All the errors that occurred while delivering to this table will be prefixed with this value in S3 destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-destinationtableconfiguration.html#cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-s3erroroutputprefix
            '''
            result = self._values.get("s3_error_output_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unique_keys(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of unique keys for a given Apache Iceberg table.

            Firehose will use these for running Create, Update, or Delete operations on the given Iceberg table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-destinationtableconfiguration.html#cfn-kinesisfirehose-deliverystream-destinationtableconfiguration-uniquekeys
            '''
            result = self._values.get("unique_keys")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationTableConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DirectPutSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"throughput_hint_in_m_bs": "throughputHintInMBs"},
    )
    class DirectPutSourceConfigurationProperty:
        def __init__(
            self,
            *,
            throughput_hint_in_m_bs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The structure that configures parameters such as ``ThroughputHintInMBs`` for a stream configured with Direct PUT as a source.

            :param throughput_hint_in_m_bs: The value that you configure for this parameter is for information purpose only and does not affect Firehose delivery throughput limit. You can use the `Firehose Limits form <https://docs.aws.amazon.com/https://support.console.aws.amazon.com/support/home#/case/create%3FissueType=service-limit-increase%26limitType=kinesis-firehose-limits>`_ to request a throughput limit increase.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-directputsourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                direct_put_source_configuration_property = kinesisfirehose.CfnDeliveryStream.DirectPutSourceConfigurationProperty(
                    throughput_hint_in_mBs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bb3b40e967adc088820cc6b98c8d06f49a47427fba6a11c4cfd878f0aa87017f)
                check_type(argname="argument throughput_hint_in_m_bs", value=throughput_hint_in_m_bs, expected_type=type_hints["throughput_hint_in_m_bs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if throughput_hint_in_m_bs is not None:
                self._values["throughput_hint_in_m_bs"] = throughput_hint_in_m_bs

        @builtins.property
        def throughput_hint_in_m_bs(self) -> typing.Optional[jsii.Number]:
            '''The value that you configure for this parameter is for information purpose only and does not affect Firehose delivery throughput limit.

            You can use the `Firehose Limits form <https://docs.aws.amazon.com/https://support.console.aws.amazon.com/support/home#/case/create%3FissueType=service-limit-increase%26limitType=kinesis-firehose-limits>`_ to request a throughput limit increase.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-directputsourceconfiguration.html#cfn-kinesisfirehose-deliverystream-directputsourceconfiguration-throughputhintinmbs
            '''
            result = self._values.get("throughput_hint_in_m_bs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DirectPutSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DocumentIdOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"default_document_id_format": "defaultDocumentIdFormat"},
    )
    class DocumentIdOptionsProperty:
        def __init__(self, *, default_document_id_format: builtins.str) -> None:
            '''Indicates the method for setting up document ID.

            The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.

            :param default_document_id_format: When the ``FIREHOSE_DEFAULT`` option is chosen, Firehose generates a unique document ID for each record based on a unique internal identifier. The generated document ID is stable across multiple delivery attempts, which helps prevent the same record from being indexed multiple times with different document IDs. When the ``NO_DOCUMENT_ID`` option is chosen, Firehose does not include any document IDs in the requests it sends to the Amazon OpenSearch Service. This causes the Amazon OpenSearch Service domain to generate document IDs. In case of multiple delivery attempts, this may cause the same record to be indexed more than once with different document IDs. This option enables write-heavy operations, such as the ingestion of logs and observability data, to consume less resources in the Amazon OpenSearch Service domain, resulting in improved performance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-documentidoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                document_id_options_property = kinesisfirehose.CfnDeliveryStream.DocumentIdOptionsProperty(
                    default_document_id_format="defaultDocumentIdFormat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d76edd5ad2b58b9b0bbc3359143f6d89ce784d7ac50b34881cf657d8016bcec4)
                check_type(argname="argument default_document_id_format", value=default_document_id_format, expected_type=type_hints["default_document_id_format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "default_document_id_format": default_document_id_format,
            }

        @builtins.property
        def default_document_id_format(self) -> builtins.str:
            '''When the ``FIREHOSE_DEFAULT`` option is chosen, Firehose generates a unique document ID for each record based on a unique internal identifier.

            The generated document ID is stable across multiple delivery attempts, which helps prevent the same record from being indexed multiple times with different document IDs.

            When the ``NO_DOCUMENT_ID`` option is chosen, Firehose does not include any document IDs in the requests it sends to the Amazon OpenSearch Service. This causes the Amazon OpenSearch Service domain to generate document IDs. In case of multiple delivery attempts, this may cause the same record to be indexed more than once with different document IDs. This option enables write-heavy operations, such as the ingestion of logs and observability data, to consume less resources in the Amazon OpenSearch Service domain, resulting in improved performance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-documentidoptions.html#cfn-kinesisfirehose-deliverystream-documentidoptions-defaultdocumentidformat
            '''
            result = self._values.get("default_document_id_format")
            assert result is not None, "Required property 'default_document_id_format' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentIdOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DynamicPartitioningConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "retry_options": "retryOptions"},
    )
    class DynamicPartitioningConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.RetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The ``DynamicPartitioningConfiguration`` property type specifies the configuration of the dynamic partitioning mechanism that creates targeted data sets from the streaming data by partitioning it based on partition keys.

            :param enabled: Specifies whether dynamic partitioning is enabled for this Kinesis Data Firehose delivery stream.
            :param retry_options: Specifies the retry behavior in case Kinesis Data Firehose is unable to deliver data to an Amazon S3 prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                dynamic_partitioning_configuration_property = kinesisfirehose.CfnDeliveryStream.DynamicPartitioningConfigurationProperty(
                    enabled=False,
                    retry_options=kinesisfirehose.CfnDeliveryStream.RetryOptionsProperty(
                        duration_in_seconds=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9cc891db4fb4eb3331e62299f82fedd4776288b7686ae851e51bfb6e44e55a52)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if retry_options is not None:
                self._values["retry_options"] = retry_options

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether dynamic partitioning is enabled for this Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html#cfn-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RetryOptionsProperty"]]:
            '''Specifies the retry behavior in case Kinesis Data Firehose is unable to deliver data to an Amazon S3 prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html#cfn-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RetryOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamicPartitioningConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ElasticsearchBufferingHintsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interval_in_seconds": "intervalInSeconds",
            "size_in_m_bs": "sizeInMBs",
        },
    )
    class ElasticsearchBufferingHintsProperty:
        def __init__(
            self,
            *,
            interval_in_seconds: typing.Optional[jsii.Number] = None,
            size_in_m_bs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ``ElasticsearchBufferingHints`` property type specifies how Amazon Kinesis Data Firehose (Kinesis Data Firehose) buffers incoming data while delivering it to the destination.

            The first buffer condition that is satisfied triggers Kinesis Data Firehose to deliver the data.

            ElasticsearchBufferingHints is the property type for the ``BufferingHints`` property of the `Amazon Kinesis Data Firehose DeliveryStream ElasticsearchDestinationConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html>`_ property type.

            :param interval_in_seconds: The length of time, in seconds, that Kinesis Data Firehose buffers incoming data before delivering it to the destination. For valid values, see the ``IntervalInSeconds`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .
            :param size_in_m_bs: The size of the buffer, in MBs, that Kinesis Data Firehose uses for incoming data before delivering it to the destination. For valid values, see the ``SizeInMBs`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                elasticsearch_buffering_hints_property = kinesisfirehose.CfnDeliveryStream.ElasticsearchBufferingHintsProperty(
                    interval_in_seconds=123,
                    size_in_mBs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__081c1ee4107d2560ed72dcc369fb8bd5cb51575be94b287e3e1d199e78950677)
                check_type(argname="argument interval_in_seconds", value=interval_in_seconds, expected_type=type_hints["interval_in_seconds"])
                check_type(argname="argument size_in_m_bs", value=size_in_m_bs, expected_type=type_hints["size_in_m_bs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if interval_in_seconds is not None:
                self._values["interval_in_seconds"] = interval_in_seconds
            if size_in_m_bs is not None:
                self._values["size_in_m_bs"] = size_in_m_bs

        @builtins.property
        def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The length of time, in seconds, that Kinesis Data Firehose buffers incoming data before delivering it to the destination.

            For valid values, see the ``IntervalInSeconds`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html#cfn-kinesisfirehose-deliverystream-elasticsearchbufferinghints-intervalinseconds
            '''
            result = self._values.get("interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size_in_m_bs(self) -> typing.Optional[jsii.Number]:
            '''The size of the buffer, in MBs, that Kinesis Data Firehose uses for incoming data before delivering it to the destination.

            For valid values, see the ``SizeInMBs`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html#cfn-kinesisfirehose-deliverystream-elasticsearchbufferinghints-sizeinmbs
            '''
            result = self._values.get("size_in_m_bs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchBufferingHintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "index_name": "indexName",
            "role_arn": "roleArn",
            "s3_configuration": "s3Configuration",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "cluster_endpoint": "clusterEndpoint",
            "document_id_options": "documentIdOptions",
            "domain_arn": "domainArn",
            "index_rotation_period": "indexRotationPeriod",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_mode": "s3BackupMode",
            "type_name": "typeName",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class ElasticsearchDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            index_name: builtins.str,
            role_arn: builtins.str,
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ElasticsearchBufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cluster_endpoint: typing.Optional[builtins.str] = None,
            document_id_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DocumentIdOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            domain_arn: typing.Optional[builtins.str] = None,
            index_rotation_period: typing.Optional[builtins.str] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ElasticsearchRetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
            type_name: typing.Optional[builtins.str] = None,
            vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.VpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The ``ElasticsearchDestinationConfiguration`` property type specifies an Amazon Elasticsearch Service (Amazon ES) domain that Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivers data to.

            :param index_name: The name of the Elasticsearch index to which Kinesis Data Firehose adds data for indexing.
            :param role_arn: The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for calling the Amazon ES Configuration API and for indexing documents. For more information, see `Controlling Access with Amazon Kinesis Data Firehose <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html>`_ .
            :param s3_configuration: The S3 bucket where Kinesis Data Firehose backs up incoming data.
            :param buffering_hints: Configures how Kinesis Data Firehose buffers incoming data while delivering it to the Amazon ES domain.
            :param cloud_watch_logging_options: The Amazon CloudWatch Logs logging options for the delivery stream.
            :param cluster_endpoint: The endpoint to use when communicating with the cluster. Specify either this ``ClusterEndpoint`` or the ``DomainARN`` field.
            :param document_id_options: Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.
            :param domain_arn: The ARN of the Amazon ES domain. The IAM role must have permissions for ``DescribeElasticsearchDomain`` , ``DescribeElasticsearchDomains`` , and ``DescribeElasticsearchDomainConfig`` after assuming the role specified in *RoleARN* . Specify either ``ClusterEndpoint`` or ``DomainARN`` .
            :param index_rotation_period: The frequency of Elasticsearch index rotation. If you enable index rotation, Kinesis Data Firehose appends a portion of the UTC arrival timestamp to the specified index name, and rotates the appended timestamp accordingly. For more information, see `Index Rotation for the Amazon ES Destination <https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-index-rotation>`_ in the *Amazon Kinesis Data Firehose Developer Guide* .
            :param processing_configuration: The data processing configuration for the Kinesis Data Firehose delivery stream.
            :param retry_options: The retry behavior when Kinesis Data Firehose is unable to deliver data to Amazon ES.
            :param s3_backup_mode: The condition under which Kinesis Data Firehose delivers data to Amazon Simple Storage Service (Amazon S3). You can send Amazon S3 all documents (all data) or only the documents that Kinesis Data Firehose could not deliver to the Amazon ES destination. For more information and valid values, see the ``S3BackupMode`` content for the `ElasticsearchDestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchDestinationConfiguration.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .
            :param type_name: The Elasticsearch type name that Amazon ES adds to documents when indexing data.
            :param vpc_configuration: The details of the VPC of the Amazon ES destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                elasticsearch_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty(
                    index_name="indexName",
                    role_arn="roleArn",
                    s3_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.ElasticsearchBufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    cluster_endpoint="clusterEndpoint",
                    document_id_options=kinesisfirehose.CfnDeliveryStream.DocumentIdOptionsProperty(
                        default_document_id_format="defaultDocumentIdFormat"
                    ),
                    domain_arn="domainArn",
                    index_rotation_period="indexRotationPeriod",
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    retry_options=kinesisfirehose.CfnDeliveryStream.ElasticsearchRetryOptionsProperty(
                        duration_in_seconds=123
                    ),
                    s3_backup_mode="s3BackupMode",
                    type_name="typeName",
                    vpc_configuration=kinesisfirehose.CfnDeliveryStream.VpcConfigurationProperty(
                        role_arn="roleArn",
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__029a33c003279860929256e859d4ba1b8707f3f6569f11613c5f08ef467fe6d6)
                check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument cluster_endpoint", value=cluster_endpoint, expected_type=type_hints["cluster_endpoint"])
                check_type(argname="argument document_id_options", value=document_id_options, expected_type=type_hints["document_id_options"])
                check_type(argname="argument domain_arn", value=domain_arn, expected_type=type_hints["domain_arn"])
                check_type(argname="argument index_rotation_period", value=index_rotation_period, expected_type=type_hints["index_rotation_period"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
                check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
                check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "index_name": index_name,
                "role_arn": role_arn,
                "s3_configuration": s3_configuration,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if cluster_endpoint is not None:
                self._values["cluster_endpoint"] = cluster_endpoint
            if document_id_options is not None:
                self._values["document_id_options"] = document_id_options
            if domain_arn is not None:
                self._values["domain_arn"] = domain_arn
            if index_rotation_period is not None:
                self._values["index_rotation_period"] = index_rotation_period
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode
            if type_name is not None:
                self._values["type_name"] = type_name
            if vpc_configuration is not None:
                self._values["vpc_configuration"] = vpc_configuration

        @builtins.property
        def index_name(self) -> builtins.str:
            '''The name of the Elasticsearch index to which Kinesis Data Firehose adds data for indexing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-indexname
            '''
            result = self._values.get("index_name")
            assert result is not None, "Required property 'index_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for calling the Amazon ES Configuration API and for indexing documents.

            For more information, see `Controlling Access with Amazon Kinesis Data Firehose <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''The S3 bucket where Kinesis Data Firehose backs up incoming data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ElasticsearchBufferingHintsProperty"]]:
            '''Configures how Kinesis Data Firehose buffers incoming data while delivering it to the Amazon ES domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ElasticsearchBufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''The Amazon CloudWatch Logs logging options for the delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def cluster_endpoint(self) -> typing.Optional[builtins.str]:
            '''The endpoint to use when communicating with the cluster.

            Specify either this ``ClusterEndpoint`` or the ``DomainARN`` field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-clusterendpoint
            '''
            result = self._values.get("cluster_endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def document_id_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DocumentIdOptionsProperty"]]:
            '''Indicates the method for setting up document ID.

            The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-documentidoptions
            '''
            result = self._values.get("document_id_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DocumentIdOptionsProperty"]], result)

        @builtins.property
        def domain_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Amazon ES domain.

            The IAM role must have permissions for ``DescribeElasticsearchDomain`` , ``DescribeElasticsearchDomains`` , and ``DescribeElasticsearchDomainConfig`` after assuming the role specified in *RoleARN* .

            Specify either ``ClusterEndpoint`` or ``DomainARN`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-domainarn
            '''
            result = self._values.get("domain_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def index_rotation_period(self) -> typing.Optional[builtins.str]:
            '''The frequency of Elasticsearch index rotation.

            If you enable index rotation, Kinesis Data Firehose appends a portion of the UTC arrival timestamp to the specified index name, and rotates the appended timestamp accordingly. For more information, see `Index Rotation for the Amazon ES Destination <https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-index-rotation>`_ in the *Amazon Kinesis Data Firehose Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-indexrotationperiod
            '''
            result = self._values.get("index_rotation_period")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''The data processing configuration for the Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ElasticsearchRetryOptionsProperty"]]:
            '''The retry behavior when Kinesis Data Firehose is unable to deliver data to Amazon ES.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ElasticsearchRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''The condition under which Kinesis Data Firehose delivers data to Amazon Simple Storage Service (Amazon S3).

            You can send Amazon S3 all documents (all data) or only the documents that Kinesis Data Firehose could not deliver to the Amazon ES destination. For more information and valid values, see the ``S3BackupMode`` content for the `ElasticsearchDestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchDestinationConfiguration.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type_name(self) -> typing.Optional[builtins.str]:
            '''The Elasticsearch type name that Amazon ES adds to documents when indexing data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-typename
            '''
            result = self._values.get("type_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.VpcConfigurationProperty"]]:
            '''The details of the VPC of the Amazon ES destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.VpcConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ElasticsearchRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class ElasticsearchRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ``ElasticsearchRetryOptions`` property type configures the retry behavior for when Amazon Kinesis Data Firehose (Kinesis Data Firehose) can't deliver data to Amazon Elasticsearch Service (Amazon ES).

            :param duration_in_seconds: After an initial failure to deliver to Amazon ES, the total amount of time during which Kinesis Data Firehose re-attempts delivery (including the first attempt). If Kinesis Data Firehose can't deliver the data within the specified time, it writes the data to the backup S3 bucket. For valid values, see the ``DurationInSeconds`` content for the `ElasticsearchRetryOptions <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchRetryOptions.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchretryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                elasticsearch_retry_options_property = kinesisfirehose.CfnDeliveryStream.ElasticsearchRetryOptionsProperty(
                    duration_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2556301b4eb1fbc8924ad4d41633add09219c34215bad4251ecd9506fbd5f4f1)
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''After an initial failure to deliver to Amazon ES, the total amount of time during which Kinesis Data Firehose re-attempts delivery (including the first attempt).

            If Kinesis Data Firehose can't deliver the data within the specified time, it writes the data to the backup S3 bucket. For valid values, see the ``DurationInSeconds`` content for the `ElasticsearchRetryOptions <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchRetryOptions.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchretryoptions.html#cfn-kinesisfirehose-deliverystream-elasticsearchretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kms_encryption_config": "kmsEncryptionConfig",
            "no_encryption_config": "noEncryptionConfig",
        },
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            kms_encryption_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.KMSEncryptionConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            no_encryption_config: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``EncryptionConfiguration`` property type specifies the encryption settings that Amazon Kinesis Data Firehose (Kinesis Data Firehose) uses when delivering data to Amazon Simple Storage Service (Amazon S3).

            :param kms_encryption_config: The AWS Key Management Service ( AWS KMS) encryption key that Amazon S3 uses to encrypt your data.
            :param no_encryption_config: Disables encryption. For valid values, see the ``NoEncryptionConfig`` content for the `EncryptionConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_EncryptionConfiguration.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                encryption_configuration_property = kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                    kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                        awskms_key_arn="awskmsKeyArn"
                    ),
                    no_encryption_config="noEncryptionConfig"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4416718c6f0bcd460ac15d8467b60189a1b6ff006003483c5095802962acb534)
                check_type(argname="argument kms_encryption_config", value=kms_encryption_config, expected_type=type_hints["kms_encryption_config"])
                check_type(argname="argument no_encryption_config", value=no_encryption_config, expected_type=type_hints["no_encryption_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_encryption_config is not None:
                self._values["kms_encryption_config"] = kms_encryption_config
            if no_encryption_config is not None:
                self._values["no_encryption_config"] = no_encryption_config

        @builtins.property
        def kms_encryption_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.KMSEncryptionConfigProperty"]]:
            '''The AWS Key Management Service ( AWS KMS) encryption key that Amazon S3 uses to encrypt your data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html#cfn-kinesisfirehose-deliverystream-encryptionconfiguration-kmsencryptionconfig
            '''
            result = self._values.get("kms_encryption_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.KMSEncryptionConfigProperty"]], result)

        @builtins.property
        def no_encryption_config(self) -> typing.Optional[builtins.str]:
            '''Disables encryption.

            For valid values, see the ``NoEncryptionConfig`` content for the `EncryptionConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_EncryptionConfiguration.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html#cfn-kinesisfirehose-deliverystream-encryptionconfiguration-noencryptionconfig
            '''
            result = self._values.get("no_encryption_config")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_arn": "bucketArn",
            "role_arn": "roleArn",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "compression_format": "compressionFormat",
            "custom_time_zone": "customTimeZone",
            "data_format_conversion_configuration": "dataFormatConversionConfiguration",
            "dynamic_partitioning_configuration": "dynamicPartitioningConfiguration",
            "encryption_configuration": "encryptionConfiguration",
            "error_output_prefix": "errorOutputPrefix",
            "file_extension": "fileExtension",
            "prefix": "prefix",
            "processing_configuration": "processingConfiguration",
            "s3_backup_configuration": "s3BackupConfiguration",
            "s3_backup_mode": "s3BackupMode",
        },
    )
    class ExtendedS3DestinationConfigurationProperty:
        def __init__(
            self,
            *,
            bucket_arn: builtins.str,
            role_arn: builtins.str,
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.BufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            compression_format: typing.Optional[builtins.str] = None,
            custom_time_zone: typing.Optional[builtins.str] = None,
            data_format_conversion_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DataFormatConversionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dynamic_partitioning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DynamicPartitioningConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            error_output_prefix: typing.Optional[builtins.str] = None,
            file_extension: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``ExtendedS3DestinationConfiguration`` property type configures an Amazon S3 destination for an Amazon Kinesis Data Firehose delivery stream.

            :param bucket_arn: The Amazon Resource Name (ARN) of the Amazon S3 bucket. For constraints, see `ExtendedS3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationConfiguration.html>`_ in the *Amazon Kinesis Data Firehose API Reference* .
            :param role_arn: The Amazon Resource Name (ARN) of the AWS credentials. For constraints, see `ExtendedS3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationConfiguration.html>`_ in the *Amazon Kinesis Data Firehose API Reference* .
            :param buffering_hints: The buffering option.
            :param cloud_watch_logging_options: The Amazon CloudWatch logging options for your Firehose stream.
            :param compression_format: The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
            :param custom_time_zone: The time zone you prefer. UTC is the default.
            :param data_format_conversion_configuration: The serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.
            :param dynamic_partitioning_configuration: The configuration of the dynamic partitioning mechanism that creates targeted data sets from the streaming data by partitioning it based on partition keys.
            :param encryption_configuration: The encryption configuration for the Kinesis Data Firehose delivery stream. The default value is ``NoEncryption`` .
            :param error_output_prefix: A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see `Custom Prefixes for Amazon S3 Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`_ .
            :param file_extension: Specify a file extension. It will override the default file extension
            :param prefix: The ``YYYY/MM/DD/HH`` time format prefix is automatically used for delivered Amazon S3 files. For more information, see `ExtendedS3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationConfiguration.html>`_ in the *Amazon Kinesis Data Firehose API Reference* .
            :param processing_configuration: The data processing configuration for the Kinesis Data Firehose delivery stream.
            :param s3_backup_configuration: The configuration for backup in Amazon S3.
            :param s3_backup_mode: The Amazon S3 backup mode. After you create a Firehose stream, you can update it to enable Amazon S3 backup if it is disabled. If backup is enabled, you can't update the Firehose stream to disable it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                extended_s3_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty(
                    bucket_arn="bucketArn",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    compression_format="compressionFormat",
                    custom_time_zone="customTimeZone",
                    data_format_conversion_configuration=kinesisfirehose.CfnDeliveryStream.DataFormatConversionConfigurationProperty(
                        enabled=False,
                        input_format_configuration=kinesisfirehose.CfnDeliveryStream.InputFormatConfigurationProperty(
                            deserializer=kinesisfirehose.CfnDeliveryStream.DeserializerProperty(
                                hive_json_ser_de=kinesisfirehose.CfnDeliveryStream.HiveJsonSerDeProperty(
                                    timestamp_formats=["timestampFormats"]
                                ),
                                open_xJson_ser_de=kinesisfirehose.CfnDeliveryStream.OpenXJsonSerDeProperty(
                                    case_insensitive=False,
                                    column_to_json_key_mappings={
                                        "column_to_json_key_mappings_key": "columnToJsonKeyMappings"
                                    },
                                    convert_dots_in_json_keys_to_underscores=False
                                )
                            )
                        ),
                        output_format_configuration=kinesisfirehose.CfnDeliveryStream.OutputFormatConfigurationProperty(
                            serializer=kinesisfirehose.CfnDeliveryStream.SerializerProperty(
                                orc_ser_de=kinesisfirehose.CfnDeliveryStream.OrcSerDeProperty(
                                    block_size_bytes=123,
                                    bloom_filter_columns=["bloomFilterColumns"],
                                    bloom_filter_false_positive_probability=123,
                                    compression="compression",
                                    dictionary_key_threshold=123,
                                    enable_padding=False,
                                    format_version="formatVersion",
                                    padding_tolerance=123,
                                    row_index_stride=123,
                                    stripe_size_bytes=123
                                ),
                                parquet_ser_de=kinesisfirehose.CfnDeliveryStream.ParquetSerDeProperty(
                                    block_size_bytes=123,
                                    compression="compression",
                                    enable_dictionary_compression=False,
                                    max_padding_bytes=123,
                                    page_size_bytes=123,
                                    writer_version="writerVersion"
                                )
                            )
                        ),
                        schema_configuration=kinesisfirehose.CfnDeliveryStream.SchemaConfigurationProperty(
                            catalog_id="catalogId",
                            database_name="databaseName",
                            region="region",
                            role_arn="roleArn",
                            table_name="tableName",
                            version_id="versionId"
                        )
                    ),
                    dynamic_partitioning_configuration=kinesisfirehose.CfnDeliveryStream.DynamicPartitioningConfigurationProperty(
                        enabled=False,
                        retry_options=kinesisfirehose.CfnDeliveryStream.RetryOptionsProperty(
                            duration_in_seconds=123
                        )
                    ),
                    encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                        kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                            awskms_key_arn="awskmsKeyArn"
                        ),
                        no_encryption_config="noEncryptionConfig"
                    ),
                    error_output_prefix="errorOutputPrefix",
                    file_extension="fileExtension",
                    prefix="prefix",
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    s3_backup_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                    s3_backup_mode="s3BackupMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7faa411782bea929613482f29819c6479d5ad2f4416ea558d510fb9fd71eaa95)
                check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument compression_format", value=compression_format, expected_type=type_hints["compression_format"])
                check_type(argname="argument custom_time_zone", value=custom_time_zone, expected_type=type_hints["custom_time_zone"])
                check_type(argname="argument data_format_conversion_configuration", value=data_format_conversion_configuration, expected_type=type_hints["data_format_conversion_configuration"])
                check_type(argname="argument dynamic_partitioning_configuration", value=dynamic_partitioning_configuration, expected_type=type_hints["dynamic_partitioning_configuration"])
                check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
                check_type(argname="argument error_output_prefix", value=error_output_prefix, expected_type=type_hints["error_output_prefix"])
                check_type(argname="argument file_extension", value=file_extension, expected_type=type_hints["file_extension"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument s3_backup_configuration", value=s3_backup_configuration, expected_type=type_hints["s3_backup_configuration"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_arn": bucket_arn,
                "role_arn": role_arn,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if compression_format is not None:
                self._values["compression_format"] = compression_format
            if custom_time_zone is not None:
                self._values["custom_time_zone"] = custom_time_zone
            if data_format_conversion_configuration is not None:
                self._values["data_format_conversion_configuration"] = data_format_conversion_configuration
            if dynamic_partitioning_configuration is not None:
                self._values["dynamic_partitioning_configuration"] = dynamic_partitioning_configuration
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration
            if error_output_prefix is not None:
                self._values["error_output_prefix"] = error_output_prefix
            if file_extension is not None:
                self._values["file_extension"] = file_extension
            if prefix is not None:
                self._values["prefix"] = prefix
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if s3_backup_configuration is not None:
                self._values["s3_backup_configuration"] = s3_backup_configuration
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode

        @builtins.property
        def bucket_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon S3 bucket.

            For constraints, see `ExtendedS3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationConfiguration.html>`_ in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-bucketarn
            '''
            result = self._values.get("bucket_arn")
            assert result is not None, "Required property 'bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AWS credentials.

            For constraints, see `ExtendedS3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationConfiguration.html>`_ in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.BufferingHintsProperty"]]:
            '''The buffering option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.BufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''The Amazon CloudWatch logging options for your Firehose stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def compression_format(self) -> typing.Optional[builtins.str]:
            '''The compression format.

            If no value is specified, the default is ``UNCOMPRESSED`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-compressionformat
            '''
            result = self._values.get("compression_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_time_zone(self) -> typing.Optional[builtins.str]:
            '''The time zone you prefer.

            UTC is the default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-customtimezone
            '''
            result = self._values.get("custom_time_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_format_conversion_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DataFormatConversionConfigurationProperty"]]:
            '''The serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-dataformatconversionconfiguration
            '''
            result = self._values.get("data_format_conversion_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DataFormatConversionConfigurationProperty"]], result)

        @builtins.property
        def dynamic_partitioning_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DynamicPartitioningConfigurationProperty"]]:
            '''The configuration of the dynamic partitioning mechanism that creates targeted data sets from the streaming data by partitioning it based on partition keys.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-dynamicpartitioningconfiguration
            '''
            result = self._values.get("dynamic_partitioning_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DynamicPartitioningConfigurationProperty"]], result)

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.EncryptionConfigurationProperty"]]:
            '''The encryption configuration for the Kinesis Data Firehose delivery stream.

            The default value is ``NoEncryption`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.EncryptionConfigurationProperty"]], result)

        @builtins.property
        def error_output_prefix(self) -> typing.Optional[builtins.str]:
            '''A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3.

            This prefix appears immediately following the bucket name. For information about how to specify this prefix, see `Custom Prefixes for Amazon S3 Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-erroroutputprefix
            '''
            result = self._values.get("error_output_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def file_extension(self) -> typing.Optional[builtins.str]:
            '''Specify a file extension.

            It will override the default file extension

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-fileextension
            '''
            result = self._values.get("file_extension")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''The ``YYYY/MM/DD/HH`` time format prefix is automatically used for delivered Amazon S3 files.

            For more information, see `ExtendedS3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationConfiguration.html>`_ in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''The data processing configuration for the Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def s3_backup_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]]:
            '''The configuration for backup in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-s3backupconfiguration
            '''
            result = self._values.get("s3_backup_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''The Amazon S3 backup mode.

            After you create a Firehose stream, you can update it to enable Amazon S3 backup if it is disabled. If backup is enabled, you can't update the Firehose stream to disable it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExtendedS3DestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.HiveJsonSerDeProperty",
        jsii_struct_bases=[],
        name_mapping={"timestamp_formats": "timestampFormats"},
    )
    class HiveJsonSerDeProperty:
        def __init__(
            self,
            *,
            timestamp_formats: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The native Hive / HCatalog JsonSerDe.

            Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.

            :param timestamp_formats: Indicates how you want Firehose to parse the date and timestamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime's DateTimeFormat format strings. For more information, see `Class DateTimeFormat <https://docs.aws.amazon.com/https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`_ . You can also use the special value ``millis`` to parse timestamps in epoch milliseconds. If you don't specify a format, Firehose uses ``java.sql.Timestamp::valueOf`` by default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-hivejsonserde.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                hive_json_ser_de_property = kinesisfirehose.CfnDeliveryStream.HiveJsonSerDeProperty(
                    timestamp_formats=["timestampFormats"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f8aed0e38a71aaf287d17202c1a15e108a76c336307d62f78aaec9e6482a117f)
                check_type(argname="argument timestamp_formats", value=timestamp_formats, expected_type=type_hints["timestamp_formats"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if timestamp_formats is not None:
                self._values["timestamp_formats"] = timestamp_formats

        @builtins.property
        def timestamp_formats(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Indicates how you want Firehose to parse the date and timestamps that may be present in your input data JSON.

            To specify these format strings, follow the pattern syntax of JodaTime's DateTimeFormat format strings. For more information, see `Class DateTimeFormat <https://docs.aws.amazon.com/https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`_ . You can also use the special value ``millis`` to parse timestamps in epoch milliseconds. If you don't specify a format, Firehose uses ``java.sql.Timestamp::valueOf`` by default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-hivejsonserde.html#cfn-kinesisfirehose-deliverystream-hivejsonserde-timestampformats
            '''
            result = self._values.get("timestamp_formats")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HiveJsonSerDeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.HttpEndpointCommonAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute_name": "attributeName",
            "attribute_value": "attributeValue",
        },
    )
    class HttpEndpointCommonAttributeProperty:
        def __init__(
            self,
            *,
            attribute_name: builtins.str,
            attribute_value: builtins.str,
        ) -> None:
            '''Describes the metadata that's delivered to the specified HTTP endpoint destination.

            Kinesis Firehose supports any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, MongoDB, and New Relic.

            :param attribute_name: The name of the HTTP endpoint common attribute.
            :param attribute_value: The value of the HTTP endpoint common attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                http_endpoint_common_attribute_property = kinesisfirehose.CfnDeliveryStream.HttpEndpointCommonAttributeProperty(
                    attribute_name="attributeName",
                    attribute_value="attributeValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d04b9e64bbadb832ca77b64870e79e2910eb18ecbaf3d42b7d1c1b17fb3c160)
                check_type(argname="argument attribute_name", value=attribute_name, expected_type=type_hints["attribute_name"])
                check_type(argname="argument attribute_value", value=attribute_value, expected_type=type_hints["attribute_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attribute_name": attribute_name,
                "attribute_value": attribute_value,
            }

        @builtins.property
        def attribute_name(self) -> builtins.str:
            '''The name of the HTTP endpoint common attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html#cfn-kinesisfirehose-deliverystream-httpendpointcommonattribute-attributename
            '''
            result = self._values.get("attribute_name")
            assert result is not None, "Required property 'attribute_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attribute_value(self) -> builtins.str:
            '''The value of the HTTP endpoint common attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html#cfn-kinesisfirehose-deliverystream-httpendpointcommonattribute-attributevalue
            '''
            result = self._values.get("attribute_value")
            assert result is not None, "Required property 'attribute_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpEndpointCommonAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.HttpEndpointConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"url": "url", "access_key": "accessKey", "name": "name"},
    )
    class HttpEndpointConfigurationProperty:
        def __init__(
            self,
            *,
            url: builtins.str,
            access_key: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the configuration of the HTTP endpoint to which Kinesis Firehose delivers data.

            Kinesis Firehose supports any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, MongoDB, and New Relic.

            :param url: The URL of the HTTP endpoint selected as the destination.
            :param access_key: The access key required for Kinesis Firehose to authenticate with the HTTP endpoint selected as the destination.
            :param name: The name of the HTTP endpoint selected as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                http_endpoint_configuration_property = kinesisfirehose.CfnDeliveryStream.HttpEndpointConfigurationProperty(
                    url="url",
                
                    # the properties below are optional
                    access_key="accessKey",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b0aeaa2e754e3362456fea60de1849d85d4913483f2324b0f89480dc7822dd8c)
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "url": url,
            }
            if access_key is not None:
                self._values["access_key"] = access_key
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def url(self) -> builtins.str:
            '''The URL of the HTTP endpoint selected as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def access_key(self) -> typing.Optional[builtins.str]:
            '''The access key required for Kinesis Firehose to authenticate with the HTTP endpoint selected as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-accesskey
            '''
            result = self._values.get("access_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the HTTP endpoint selected as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpEndpointConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_configuration": "endpointConfiguration",
            "s3_configuration": "s3Configuration",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "processing_configuration": "processingConfiguration",
            "request_configuration": "requestConfiguration",
            "retry_options": "retryOptions",
            "role_arn": "roleArn",
            "s3_backup_mode": "s3BackupMode",
            "secrets_manager_configuration": "secretsManagerConfiguration",
        },
    )
    class HttpEndpointDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            endpoint_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.HttpEndpointConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.BufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            request_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.HttpEndpointRequestConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.RetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            role_arn: typing.Optional[builtins.str] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
            secrets_manager_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SecretsManagerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes the configuration of the HTTP endpoint destination.

            Kinesis Firehose supports any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, MongoDB, and New Relic.

            :param endpoint_configuration: The configuration of the HTTP endpoint selected as the destination.
            :param s3_configuration: Describes the configuration of a destination in Amazon S3.
            :param buffering_hints: The buffering options that can be used before data is delivered to the specified destination. Kinesis Data Firehose treats these options as hints, and it might choose to use more optimal values. The SizeInMBs and IntervalInSeconds parameters are optional. However, if you specify a value for one of them, you must also provide a value for the other.
            :param cloud_watch_logging_options: Describes the Amazon CloudWatch logging options for your delivery stream.
            :param processing_configuration: Describes the data processing configuration.
            :param request_configuration: The configuration of the request sent to the HTTP endpoint specified as the destination.
            :param retry_options: Describes the retry behavior in case Kinesis Data Firehose is unable to deliver data to the specified HTTP endpoint destination, or if it doesn't receive a valid acknowledgment of receipt from the specified HTTP endpoint destination.
            :param role_arn: Kinesis Data Firehose uses this IAM role for all the permissions that the delivery stream needs.
            :param s3_backup_mode: Describes the S3 bucket backup options for the data that Kinesis Data Firehose delivers to the HTTP endpoint destination. You can back up all documents (AllData) or only the documents that Kinesis Data Firehose could not deliver to the specified HTTP endpoint destination (FailedDataOnly).
            :param secrets_manager_configuration: The configuration that defines how you access secrets for HTTP Endpoint destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                http_endpoint_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty(
                    endpoint_configuration=kinesisfirehose.CfnDeliveryStream.HttpEndpointConfigurationProperty(
                        url="url",
                
                        # the properties below are optional
                        access_key="accessKey",
                        name="name"
                    ),
                    s3_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    request_configuration=kinesisfirehose.CfnDeliveryStream.HttpEndpointRequestConfigurationProperty(
                        common_attributes=[kinesisfirehose.CfnDeliveryStream.HttpEndpointCommonAttributeProperty(
                            attribute_name="attributeName",
                            attribute_value="attributeValue"
                        )],
                        content_encoding="contentEncoding"
                    ),
                    retry_options=kinesisfirehose.CfnDeliveryStream.RetryOptionsProperty(
                        duration_in_seconds=123
                    ),
                    role_arn="roleArn",
                    s3_backup_mode="s3BackupMode",
                    secrets_manager_configuration=kinesisfirehose.CfnDeliveryStream.SecretsManagerConfigurationProperty(
                        enabled=False,
                
                        # the properties below are optional
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6e8b3a25c8aa6cb1c905473fb8dd18a708e794918ae12a9a622993603b96ab8a)
                check_type(argname="argument endpoint_configuration", value=endpoint_configuration, expected_type=type_hints["endpoint_configuration"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument request_configuration", value=request_configuration, expected_type=type_hints["request_configuration"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
                check_type(argname="argument secrets_manager_configuration", value=secrets_manager_configuration, expected_type=type_hints["secrets_manager_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "endpoint_configuration": endpoint_configuration,
                "s3_configuration": s3_configuration,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if request_configuration is not None:
                self._values["request_configuration"] = request_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode
            if secrets_manager_configuration is not None:
                self._values["secrets_manager_configuration"] = secrets_manager_configuration

        @builtins.property
        def endpoint_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointConfigurationProperty"]:
            '''The configuration of the HTTP endpoint selected as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-endpointconfiguration
            '''
            result = self._values.get("endpoint_configuration")
            assert result is not None, "Required property 'endpoint_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointConfigurationProperty"], result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''Describes the configuration of a destination in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.BufferingHintsProperty"]]:
            '''The buffering options that can be used before data is delivered to the specified destination.

            Kinesis Data Firehose treats these options as hints, and it might choose to use more optimal values. The SizeInMBs and IntervalInSeconds parameters are optional. However, if you specify a value for one of them, you must also provide a value for the other.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.BufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''Describes the Amazon CloudWatch logging options for your delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''Describes the data processing configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def request_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointRequestConfigurationProperty"]]:
            '''The configuration of the request sent to the HTTP endpoint specified as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-requestconfiguration
            '''
            result = self._values.get("request_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointRequestConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RetryOptionsProperty"]]:
            '''Describes the retry behavior in case Kinesis Data Firehose is unable to deliver data to the specified HTTP endpoint destination, or if it doesn't receive a valid acknowledgment of receipt from the specified HTTP endpoint destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RetryOptionsProperty"]], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''Kinesis Data Firehose uses this IAM role for all the permissions that the delivery stream needs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''Describes the S3 bucket backup options for the data that Kinesis Data Firehose delivers to the HTTP endpoint destination.

            You can back up all documents (AllData) or only the documents that Kinesis Data Firehose could not deliver to the specified HTTP endpoint destination (FailedDataOnly).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SecretsManagerConfigurationProperty"]]:
            '''The configuration that defines how you access secrets for HTTP Endpoint destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-secretsmanagerconfiguration
            '''
            result = self._values.get("secrets_manager_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SecretsManagerConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpEndpointDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.HttpEndpointRequestConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "common_attributes": "commonAttributes",
            "content_encoding": "contentEncoding",
        },
    )
    class HttpEndpointRequestConfigurationProperty:
        def __init__(
            self,
            *,
            common_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.HttpEndpointCommonAttributeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            content_encoding: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration of the HTTP endpoint request.

            Kinesis Firehose supports any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, MongoDB, and New Relic.

            :param common_attributes: Describes the metadata sent to the HTTP endpoint destination.
            :param content_encoding: Kinesis Data Firehose uses the content encoding to compress the body of a request before sending the request to the destination. For more information, see Content-Encoding in MDN Web Docs, the official Mozilla documentation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                http_endpoint_request_configuration_property = kinesisfirehose.CfnDeliveryStream.HttpEndpointRequestConfigurationProperty(
                    common_attributes=[kinesisfirehose.CfnDeliveryStream.HttpEndpointCommonAttributeProperty(
                        attribute_name="attributeName",
                        attribute_value="attributeValue"
                    )],
                    content_encoding="contentEncoding"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4a9efa4d9f485d918f70adc5823c0a1caf4894264ec785a00d5ef0879e3c1177)
                check_type(argname="argument common_attributes", value=common_attributes, expected_type=type_hints["common_attributes"])
                check_type(argname="argument content_encoding", value=content_encoding, expected_type=type_hints["content_encoding"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if common_attributes is not None:
                self._values["common_attributes"] = common_attributes
            if content_encoding is not None:
                self._values["content_encoding"] = content_encoding

        @builtins.property
        def common_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointCommonAttributeProperty"]]]]:
            '''Describes the metadata sent to the HTTP endpoint destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointrequestconfiguration-commonattributes
            '''
            result = self._values.get("common_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointCommonAttributeProperty"]]]], result)

        @builtins.property
        def content_encoding(self) -> typing.Optional[builtins.str]:
            '''Kinesis Data Firehose uses the content encoding to compress the body of a request before sending the request to the destination.

            For more information, see Content-Encoding in MDN Web Docs, the official Mozilla documentation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointrequestconfiguration-contentencoding
            '''
            result = self._values.get("content_encoding")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpEndpointRequestConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.IcebergDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_configuration": "catalogConfiguration",
            "role_arn": "roleArn",
            "s3_configuration": "s3Configuration",
            "append_only": "appendOnly",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "destination_table_configuration_list": "destinationTableConfigurationList",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_mode": "s3BackupMode",
            "schema_evolution_configuration": "schemaEvolutionConfiguration",
            "table_creation_configuration": "tableCreationConfiguration",
        },
    )
    class IcebergDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            catalog_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CatalogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            role_arn: builtins.str,
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            append_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.BufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            destination_table_configuration_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DestinationTableConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.RetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
            schema_evolution_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SchemaEvolutionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            table_creation_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.TableCreationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the destination configure settings for Apache Iceberg Table.

            :param catalog_configuration: Configuration describing where the destination Apache Iceberg Tables are persisted.
            :param role_arn: The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling Apache Iceberg Tables.
            :param s3_configuration: 
            :param append_only: Describes whether all incoming data for this delivery stream will be append only (inserts only and not for updates and deletes) for Iceberg delivery. This feature is only applicable for Apache Iceberg Tables. The default value is false. If you set this value to true, Firehose automatically increases the throughput limit of a stream based on the throttling levels of the stream. If you set this parameter to true for a stream with updates and deletes, you will see out of order delivery.
            :param buffering_hints: 
            :param cloud_watch_logging_options: 
            :param destination_table_configuration_list: Provides a list of ``DestinationTableConfigurations`` which Firehose uses to deliver data to Apache Iceberg Tables. Firehose will write data with insert if table specific configuration is not provided here.
            :param processing_configuration: 
            :param retry_options: 
            :param s3_backup_mode: Describes how Firehose will backup records. Currently,S3 backup only supports ``FailedDataOnly`` .
            :param schema_evolution_configuration: The configuration to enable automatic schema evolution. Amazon Data Firehose is in preview release and is subject to change.
            :param table_creation_configuration: The configuration to enable automatic table creation. Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                iceberg_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.IcebergDestinationConfigurationProperty(
                    catalog_configuration=kinesisfirehose.CfnDeliveryStream.CatalogConfigurationProperty(
                        catalog_arn="catalogArn",
                        warehouse_location="warehouseLocation"
                    ),
                    role_arn="roleArn",
                    s3_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                
                    # the properties below are optional
                    append_only=False,
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    destination_table_configuration_list=[kinesisfirehose.CfnDeliveryStream.DestinationTableConfigurationProperty(
                        destination_database_name="destinationDatabaseName",
                        destination_table_name="destinationTableName",
                
                        # the properties below are optional
                        partition_spec=kinesisfirehose.CfnDeliveryStream.PartitionSpecProperty(
                            identity=[kinesisfirehose.CfnDeliveryStream.PartitionFieldProperty(
                                source_name="sourceName"
                            )]
                        ),
                        s3_error_output_prefix="s3ErrorOutputPrefix",
                        unique_keys=["uniqueKeys"]
                    )],
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    retry_options=kinesisfirehose.CfnDeliveryStream.RetryOptionsProperty(
                        duration_in_seconds=123
                    ),
                    s3_backup_mode="s3BackupMode",
                    schema_evolution_configuration=kinesisfirehose.CfnDeliveryStream.SchemaEvolutionConfigurationProperty(
                        enabled=False
                    ),
                    table_creation_configuration=kinesisfirehose.CfnDeliveryStream.TableCreationConfigurationProperty(
                        enabled=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7cc5b65e233b52b72b153275ce8ced9f593e3385051386bed6920a574cf9f53d)
                check_type(argname="argument catalog_configuration", value=catalog_configuration, expected_type=type_hints["catalog_configuration"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument append_only", value=append_only, expected_type=type_hints["append_only"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument destination_table_configuration_list", value=destination_table_configuration_list, expected_type=type_hints["destination_table_configuration_list"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
                check_type(argname="argument schema_evolution_configuration", value=schema_evolution_configuration, expected_type=type_hints["schema_evolution_configuration"])
                check_type(argname="argument table_creation_configuration", value=table_creation_configuration, expected_type=type_hints["table_creation_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "catalog_configuration": catalog_configuration,
                "role_arn": role_arn,
                "s3_configuration": s3_configuration,
            }
            if append_only is not None:
                self._values["append_only"] = append_only
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if destination_table_configuration_list is not None:
                self._values["destination_table_configuration_list"] = destination_table_configuration_list
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode
            if schema_evolution_configuration is not None:
                self._values["schema_evolution_configuration"] = schema_evolution_configuration
            if table_creation_configuration is not None:
                self._values["table_creation_configuration"] = table_creation_configuration

        @builtins.property
        def catalog_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CatalogConfigurationProperty"]:
            '''Configuration describing where the destination Apache Iceberg Tables are persisted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-catalogconfiguration
            '''
            result = self._values.get("catalog_configuration")
            assert result is not None, "Required property 'catalog_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CatalogConfigurationProperty"], result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling Apache Iceberg Tables.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def append_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Describes whether all incoming data for this delivery stream will be append only (inserts only and not for updates and deletes) for Iceberg delivery.

            This feature is only applicable for Apache Iceberg Tables.

            The default value is false. If you set this value to true, Firehose automatically increases the throughput limit of a stream based on the throttling levels of the stream. If you set this parameter to true for a stream with updates and deletes, you will see out of order delivery.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-appendonly
            '''
            result = self._values.get("append_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.BufferingHintsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.BufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def destination_table_configuration_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DestinationTableConfigurationProperty"]]]]:
            '''Provides a list of ``DestinationTableConfigurations`` which Firehose uses to deliver data to Apache Iceberg Tables.

            Firehose will write data with insert if table specific configuration is not provided here.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-destinationtableconfigurationlist
            '''
            result = self._values.get("destination_table_configuration_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DestinationTableConfigurationProperty"]]]], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RetryOptionsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''Describes how Firehose will backup records.

            Currently,S3 backup only supports ``FailedDataOnly`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schema_evolution_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SchemaEvolutionConfigurationProperty"]]:
            '''The configuration to enable automatic schema evolution.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-schemaevolutionconfiguration
            '''
            result = self._values.get("schema_evolution_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SchemaEvolutionConfigurationProperty"]], result)

        @builtins.property
        def table_creation_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.TableCreationConfigurationProperty"]]:
            '''The configuration to enable automatic table creation.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-icebergdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration-tablecreationconfiguration
            '''
            result = self._values.get("table_creation_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.TableCreationConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IcebergDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.InputFormatConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"deserializer": "deserializer"},
    )
    class InputFormatConfigurationProperty:
        def __init__(
            self,
            *,
            deserializer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DeserializerProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the deserializer you want to use to convert the format of the input data.

            This parameter is required if ``Enabled`` is set to true.

            :param deserializer: Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                input_format_configuration_property = kinesisfirehose.CfnDeliveryStream.InputFormatConfigurationProperty(
                    deserializer=kinesisfirehose.CfnDeliveryStream.DeserializerProperty(
                        hive_json_ser_de=kinesisfirehose.CfnDeliveryStream.HiveJsonSerDeProperty(
                            timestamp_formats=["timestampFormats"]
                        ),
                        open_xJson_ser_de=kinesisfirehose.CfnDeliveryStream.OpenXJsonSerDeProperty(
                            case_insensitive=False,
                            column_to_json_key_mappings={
                                "column_to_json_key_mappings_key": "columnToJsonKeyMappings"
                            },
                            convert_dots_in_json_keys_to_underscores=False
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dce5223aa97132391790e172c7c143f8a4c8df67b3b09df48eb0b1dff486468b)
                check_type(argname="argument deserializer", value=deserializer, expected_type=type_hints["deserializer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if deserializer is not None:
                self._values["deserializer"] = deserializer

        @builtins.property
        def deserializer(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DeserializerProperty"]]:
            '''Specifies which deserializer to use.

            You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration.html#cfn-kinesisfirehose-deliverystream-inputformatconfiguration-deserializer
            '''
            result = self._values.get("deserializer")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DeserializerProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputFormatConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"awskms_key_arn": "awskmsKeyArn"},
    )
    class KMSEncryptionConfigProperty:
        def __init__(self, *, awskms_key_arn: builtins.str) -> None:
            '''The ``KMSEncryptionConfig`` property type specifies the AWS Key Management Service ( AWS KMS) encryption key that Amazon Simple Storage Service (Amazon S3) uses to encrypt data delivered by the Amazon Kinesis Data Firehose (Kinesis Data Firehose) stream.

            :param awskms_key_arn: The Amazon Resource Name (ARN) of the AWS KMS encryption key that Amazon S3 uses to encrypt data delivered by the Kinesis Data Firehose stream. The key must belong to the same region as the destination S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                k_mSEncryption_config_property = kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                    awskms_key_arn="awskmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ca085a464bc9440602c605444adda1cec3d2059da145bca43dd610fba2e9a8be)
                check_type(argname="argument awskms_key_arn", value=awskms_key_arn, expected_type=type_hints["awskms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "awskms_key_arn": awskms_key_arn,
            }

        @builtins.property
        def awskms_key_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AWS KMS encryption key that Amazon S3 uses to encrypt data delivered by the Kinesis Data Firehose stream.

            The key must belong to the same region as the destination S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig.html#cfn-kinesisfirehose-deliverystream-kmsencryptionconfig-awskmskeyarn
            '''
            result = self._values.get("awskms_key_arn")
            assert result is not None, "Required property 'awskms_key_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KMSEncryptionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.KinesisStreamSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kinesis_stream_arn": "kinesisStreamArn", "role_arn": "roleArn"},
    )
    class KinesisStreamSourceConfigurationProperty:
        def __init__(
            self,
            *,
            kinesis_stream_arn: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''The ``KinesisStreamSourceConfiguration`` property type specifies the stream and role Amazon Resource Names (ARNs) for a Kinesis stream used as the source for a delivery stream.

            :param kinesis_stream_arn: The ARN of the source Kinesis data stream.
            :param role_arn: The ARN of the role that provides access to the source Kinesis data stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                kinesis_stream_source_configuration_property = kinesisfirehose.CfnDeliveryStream.KinesisStreamSourceConfigurationProperty(
                    kinesis_stream_arn="kinesisStreamArn",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7ae1be427fa992bcfd551dc79aa5bba9af3c552f1661c763a814eb22ecd5dff7)
                check_type(argname="argument kinesis_stream_arn", value=kinesis_stream_arn, expected_type=type_hints["kinesis_stream_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "kinesis_stream_arn": kinesis_stream_arn,
                "role_arn": role_arn,
            }

        @builtins.property
        def kinesis_stream_arn(self) -> builtins.str:
            '''The ARN of the source Kinesis data stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-kinesisstreamarn
            '''
            result = self._values.get("kinesis_stream_arn")
            assert result is not None, "Required property 'kinesis_stream_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that provides access to the source Kinesis data stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisStreamSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.MSKSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_configuration": "authenticationConfiguration",
            "msk_cluster_arn": "mskClusterArn",
            "topic_name": "topicName",
            "read_from_timestamp": "readFromTimestamp",
        },
    )
    class MSKSourceConfigurationProperty:
        def __init__(
            self,
            *,
            authentication_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.AuthenticationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            msk_cluster_arn: builtins.str,
            topic_name: builtins.str,
            read_from_timestamp: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for the Amazon MSK cluster to be used as the source for a delivery stream.

            :param authentication_configuration: The authentication configuration of the Amazon MSK cluster.
            :param msk_cluster_arn: The ARN of the Amazon MSK cluster.
            :param topic_name: The topic name within the Amazon MSK cluster.
            :param read_from_timestamp: The start date and time in UTC for the offset position within your MSK topic from where Firehose begins to read. By default, this is set to timestamp when Firehose becomes Active. If you want to create a Firehose stream with Earliest start position from SDK or CLI, you need to set the ``ReadFromTimestamp`` parameter to Epoch (1970-01-01T00:00:00Z).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                m_sKSource_configuration_property = kinesisfirehose.CfnDeliveryStream.MSKSourceConfigurationProperty(
                    authentication_configuration=kinesisfirehose.CfnDeliveryStream.AuthenticationConfigurationProperty(
                        connectivity="connectivity",
                        role_arn="roleArn"
                    ),
                    msk_cluster_arn="mskClusterArn",
                    topic_name="topicName",
                
                    # the properties below are optional
                    read_from_timestamp="readFromTimestamp"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7b2563c2a3f195e01ffbb501ca4b7d501c1fb934c35f08b019e248300a348473)
                check_type(argname="argument authentication_configuration", value=authentication_configuration, expected_type=type_hints["authentication_configuration"])
                check_type(argname="argument msk_cluster_arn", value=msk_cluster_arn, expected_type=type_hints["msk_cluster_arn"])
                check_type(argname="argument topic_name", value=topic_name, expected_type=type_hints["topic_name"])
                check_type(argname="argument read_from_timestamp", value=read_from_timestamp, expected_type=type_hints["read_from_timestamp"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authentication_configuration": authentication_configuration,
                "msk_cluster_arn": msk_cluster_arn,
                "topic_name": topic_name,
            }
            if read_from_timestamp is not None:
                self._values["read_from_timestamp"] = read_from_timestamp

        @builtins.property
        def authentication_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AuthenticationConfigurationProperty"]:
            '''The authentication configuration of the Amazon MSK cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration.html#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-authenticationconfiguration
            '''
            result = self._values.get("authentication_configuration")
            assert result is not None, "Required property 'authentication_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AuthenticationConfigurationProperty"], result)

        @builtins.property
        def msk_cluster_arn(self) -> builtins.str:
            '''The ARN of the Amazon MSK cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration.html#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-mskclusterarn
            '''
            result = self._values.get("msk_cluster_arn")
            assert result is not None, "Required property 'msk_cluster_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def topic_name(self) -> builtins.str:
            '''The topic name within the Amazon MSK cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration.html#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-topicname
            '''
            result = self._values.get("topic_name")
            assert result is not None, "Required property 'topic_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def read_from_timestamp(self) -> typing.Optional[builtins.str]:
            '''The start date and time in UTC for the offset position within your MSK topic from where Firehose begins to read.

            By default, this is set to timestamp when Firehose becomes Active.

            If you want to create a Firehose stream with Earliest start position from SDK or CLI, you need to set the ``ReadFromTimestamp`` parameter to Epoch (1970-01-01T00:00:00Z).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration.html#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-readfromtimestamp
            '''
            result = self._values.get("read_from_timestamp")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MSKSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.OpenXJsonSerDeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "case_insensitive": "caseInsensitive",
            "column_to_json_key_mappings": "columnToJsonKeyMappings",
            "convert_dots_in_json_keys_to_underscores": "convertDotsInJsonKeysToUnderscores",
        },
    )
    class OpenXJsonSerDeProperty:
        def __init__(
            self,
            *,
            case_insensitive: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            column_to_json_key_mappings: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            convert_dots_in_json_keys_to_underscores: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The OpenX SerDe.

            Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.

            :param case_insensitive: When set to ``true`` , which is the default, Firehose converts JSON keys to lowercase before deserializing them.
            :param column_to_json_key_mappings: Maps column names to JSON keys that aren't identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, ``timestamp`` is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to ``{"ts": "timestamp"}`` to map this key to a column named ``ts`` .
            :param convert_dots_in_json_keys_to_underscores: When set to ``true`` , specifies that the names of the keys include dots and that you want Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is "a.b", you can define the column name to be "a_b" when using this option. The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                open_xJson_ser_de_property = kinesisfirehose.CfnDeliveryStream.OpenXJsonSerDeProperty(
                    case_insensitive=False,
                    column_to_json_key_mappings={
                        "column_to_json_key_mappings_key": "columnToJsonKeyMappings"
                    },
                    convert_dots_in_json_keys_to_underscores=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__65dc173b1d3e5c449c2f9ee9f1727428f35f33407e71da72ecdc48c19f3fb78c)
                check_type(argname="argument case_insensitive", value=case_insensitive, expected_type=type_hints["case_insensitive"])
                check_type(argname="argument column_to_json_key_mappings", value=column_to_json_key_mappings, expected_type=type_hints["column_to_json_key_mappings"])
                check_type(argname="argument convert_dots_in_json_keys_to_underscores", value=convert_dots_in_json_keys_to_underscores, expected_type=type_hints["convert_dots_in_json_keys_to_underscores"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if case_insensitive is not None:
                self._values["case_insensitive"] = case_insensitive
            if column_to_json_key_mappings is not None:
                self._values["column_to_json_key_mappings"] = column_to_json_key_mappings
            if convert_dots_in_json_keys_to_underscores is not None:
                self._values["convert_dots_in_json_keys_to_underscores"] = convert_dots_in_json_keys_to_underscores

        @builtins.property
        def case_insensitive(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When set to ``true`` , which is the default, Firehose converts JSON keys to lowercase before deserializing them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-caseinsensitive
            '''
            result = self._values.get("case_insensitive")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def column_to_json_key_mappings(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''Maps column names to JSON keys that aren't identical to the column names.

            This is useful when the JSON contains keys that are Hive keywords. For example, ``timestamp`` is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to ``{"ts": "timestamp"}`` to map this key to a column named ``ts`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-columntojsonkeymappings
            '''
            result = self._values.get("column_to_json_key_mappings")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def convert_dots_in_json_keys_to_underscores(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When set to ``true`` , specifies that the names of the keys include dots and that you want Firehose to replace them with underscores.

            This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is "a.b", you can define the column name to be "a_b" when using this option.

            The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-convertdotsinjsonkeystounderscores
            '''
            result = self._values.get("convert_dots_in_json_keys_to_underscores")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenXJsonSerDeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.OrcSerDeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "block_size_bytes": "blockSizeBytes",
            "bloom_filter_columns": "bloomFilterColumns",
            "bloom_filter_false_positive_probability": "bloomFilterFalsePositiveProbability",
            "compression": "compression",
            "dictionary_key_threshold": "dictionaryKeyThreshold",
            "enable_padding": "enablePadding",
            "format_version": "formatVersion",
            "padding_tolerance": "paddingTolerance",
            "row_index_stride": "rowIndexStride",
            "stripe_size_bytes": "stripeSizeBytes",
        },
    )
    class OrcSerDeProperty:
        def __init__(
            self,
            *,
            block_size_bytes: typing.Optional[jsii.Number] = None,
            bloom_filter_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
            bloom_filter_false_positive_probability: typing.Optional[jsii.Number] = None,
            compression: typing.Optional[builtins.str] = None,
            dictionary_key_threshold: typing.Optional[jsii.Number] = None,
            enable_padding: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            format_version: typing.Optional[builtins.str] = None,
            padding_tolerance: typing.Optional[jsii.Number] = None,
            row_index_stride: typing.Optional[jsii.Number] = None,
            stripe_size_bytes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''A serializer to use for converting data to the ORC format before storing it in Amazon S3.

            For more information, see `Apache ORC <https://docs.aws.amazon.com/https://orc.apache.org/docs/>`_ .

            :param block_size_bytes: The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Firehose uses this value for padding calculations.
            :param bloom_filter_columns: The column names for which you want Firehose to create bloom filters. The default is ``null`` .
            :param bloom_filter_false_positive_probability: The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.
            :param compression: The compression code to use over data blocks. The default is ``SNAPPY`` .
            :param dictionary_key_threshold: Represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1.
            :param enable_padding: Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is ``false`` .
            :param format_version: The version of the file to write. The possible values are ``V0_11`` and ``V0_12`` . The default is ``V0_12`` .
            :param padding_tolerance: A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is 0.05, which means 5 percent of stripe size. For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task. Kinesis Data Firehose ignores this parameter when ``EnablePadding`` is ``false`` .
            :param row_index_stride: The number of rows between index entries. The default is 10,000 and the minimum is 1,000.
            :param stripe_size_bytes: The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                orc_ser_de_property = kinesisfirehose.CfnDeliveryStream.OrcSerDeProperty(
                    block_size_bytes=123,
                    bloom_filter_columns=["bloomFilterColumns"],
                    bloom_filter_false_positive_probability=123,
                    compression="compression",
                    dictionary_key_threshold=123,
                    enable_padding=False,
                    format_version="formatVersion",
                    padding_tolerance=123,
                    row_index_stride=123,
                    stripe_size_bytes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8a6f3732f1d1f7da40207abc3f87e65bccadac8f31c2f54e16aa9b9d2132fd6e)
                check_type(argname="argument block_size_bytes", value=block_size_bytes, expected_type=type_hints["block_size_bytes"])
                check_type(argname="argument bloom_filter_columns", value=bloom_filter_columns, expected_type=type_hints["bloom_filter_columns"])
                check_type(argname="argument bloom_filter_false_positive_probability", value=bloom_filter_false_positive_probability, expected_type=type_hints["bloom_filter_false_positive_probability"])
                check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
                check_type(argname="argument dictionary_key_threshold", value=dictionary_key_threshold, expected_type=type_hints["dictionary_key_threshold"])
                check_type(argname="argument enable_padding", value=enable_padding, expected_type=type_hints["enable_padding"])
                check_type(argname="argument format_version", value=format_version, expected_type=type_hints["format_version"])
                check_type(argname="argument padding_tolerance", value=padding_tolerance, expected_type=type_hints["padding_tolerance"])
                check_type(argname="argument row_index_stride", value=row_index_stride, expected_type=type_hints["row_index_stride"])
                check_type(argname="argument stripe_size_bytes", value=stripe_size_bytes, expected_type=type_hints["stripe_size_bytes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if block_size_bytes is not None:
                self._values["block_size_bytes"] = block_size_bytes
            if bloom_filter_columns is not None:
                self._values["bloom_filter_columns"] = bloom_filter_columns
            if bloom_filter_false_positive_probability is not None:
                self._values["bloom_filter_false_positive_probability"] = bloom_filter_false_positive_probability
            if compression is not None:
                self._values["compression"] = compression
            if dictionary_key_threshold is not None:
                self._values["dictionary_key_threshold"] = dictionary_key_threshold
            if enable_padding is not None:
                self._values["enable_padding"] = enable_padding
            if format_version is not None:
                self._values["format_version"] = format_version
            if padding_tolerance is not None:
                self._values["padding_tolerance"] = padding_tolerance
            if row_index_stride is not None:
                self._values["row_index_stride"] = row_index_stride
            if stripe_size_bytes is not None:
                self._values["stripe_size_bytes"] = stripe_size_bytes

        @builtins.property
        def block_size_bytes(self) -> typing.Optional[jsii.Number]:
            '''The Hadoop Distributed File System (HDFS) block size.

            This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Firehose uses this value for padding calculations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-blocksizebytes
            '''
            result = self._values.get("block_size_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def bloom_filter_columns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The column names for which you want Firehose to create bloom filters.

            The default is ``null`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-bloomfiltercolumns
            '''
            result = self._values.get("bloom_filter_columns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def bloom_filter_false_positive_probability(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The Bloom filter false positive probability (FPP).

            The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-bloomfilterfalsepositiveprobability
            '''
            result = self._values.get("bloom_filter_false_positive_probability")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def compression(self) -> typing.Optional[builtins.str]:
            '''The compression code to use over data blocks.

            The default is ``SNAPPY`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-compression
            '''
            result = self._values.get("compression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dictionary_key_threshold(self) -> typing.Optional[jsii.Number]:
            '''Represents the fraction of the total number of non-null rows.

            To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-dictionarykeythreshold
            '''
            result = self._values.get("dictionary_key_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def enable_padding(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block boundaries.

            This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-enablepadding
            '''
            result = self._values.get("enable_padding")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def format_version(self) -> typing.Optional[builtins.str]:
            '''The version of the file to write.

            The possible values are ``V0_11`` and ``V0_12`` . The default is ``V0_12`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-formatversion
            '''
            result = self._values.get("format_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def padding_tolerance(self) -> typing.Optional[jsii.Number]:
            '''A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size.

            The default value is 0.05, which means 5 percent of stripe size.

            For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task.

            Kinesis Data Firehose ignores this parameter when ``EnablePadding`` is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-paddingtolerance
            '''
            result = self._values.get("padding_tolerance")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def row_index_stride(self) -> typing.Optional[jsii.Number]:
            '''The number of rows between index entries.

            The default is 10,000 and the minimum is 1,000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-rowindexstride
            '''
            result = self._values.get("row_index_stride")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stripe_size_bytes(self) -> typing.Optional[jsii.Number]:
            '''The number of bytes in each stripe.

            The default is 64 MiB and the minimum is 8 MiB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-stripesizebytes
            '''
            result = self._values.get("stripe_size_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrcSerDeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.OutputFormatConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"serializer": "serializer"},
    )
    class OutputFormatConfigurationProperty:
        def __init__(
            self,
            *,
            serializer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SerializerProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the serializer that you want Firehose to use to convert the format of your data before it writes it to Amazon S3.

            This parameter is required if ``Enabled`` is set to true.

            :param serializer: Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. If both are non-null, the server rejects the request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-outputformatconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                output_format_configuration_property = kinesisfirehose.CfnDeliveryStream.OutputFormatConfigurationProperty(
                    serializer=kinesisfirehose.CfnDeliveryStream.SerializerProperty(
                        orc_ser_de=kinesisfirehose.CfnDeliveryStream.OrcSerDeProperty(
                            block_size_bytes=123,
                            bloom_filter_columns=["bloomFilterColumns"],
                            bloom_filter_false_positive_probability=123,
                            compression="compression",
                            dictionary_key_threshold=123,
                            enable_padding=False,
                            format_version="formatVersion",
                            padding_tolerance=123,
                            row_index_stride=123,
                            stripe_size_bytes=123
                        ),
                        parquet_ser_de=kinesisfirehose.CfnDeliveryStream.ParquetSerDeProperty(
                            block_size_bytes=123,
                            compression="compression",
                            enable_dictionary_compression=False,
                            max_padding_bytes=123,
                            page_size_bytes=123,
                            writer_version="writerVersion"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3fcba637de22c6790633f7c4fdbfafe0f3cf2fcd07e8753fb333222a3b7916c2)
                check_type(argname="argument serializer", value=serializer, expected_type=type_hints["serializer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if serializer is not None:
                self._values["serializer"] = serializer

        @builtins.property
        def serializer(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SerializerProperty"]]:
            '''Specifies which serializer to use.

            You can choose either the ORC SerDe or the Parquet SerDe. If both are non-null, the server rejects the request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-outputformatconfiguration.html#cfn-kinesisfirehose-deliverystream-outputformatconfiguration-serializer
            '''
            result = self._values.get("serializer")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SerializerProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputFormatConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ParquetSerDeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "block_size_bytes": "blockSizeBytes",
            "compression": "compression",
            "enable_dictionary_compression": "enableDictionaryCompression",
            "max_padding_bytes": "maxPaddingBytes",
            "page_size_bytes": "pageSizeBytes",
            "writer_version": "writerVersion",
        },
    )
    class ParquetSerDeProperty:
        def __init__(
            self,
            *,
            block_size_bytes: typing.Optional[jsii.Number] = None,
            compression: typing.Optional[builtins.str] = None,
            enable_dictionary_compression: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            max_padding_bytes: typing.Optional[jsii.Number] = None,
            page_size_bytes: typing.Optional[jsii.Number] = None,
            writer_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A serializer to use for converting data to the Parquet format before storing it in Amazon S3.

            For more information, see `Apache Parquet <https://docs.aws.amazon.com/https://parquet.apache.org/docs/>`_ .

            :param block_size_bytes: The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Firehose uses this value for padding calculations.
            :param compression: The compression code to use over data blocks. The possible values are ``UNCOMPRESSED`` , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for higher decompression speed. Use ``GZIP`` if the compression ratio is more important than speed.
            :param enable_dictionary_compression: Indicates whether to enable dictionary compression.
            :param max_padding_bytes: The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.
            :param page_size_bytes: The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.
            :param writer_version: Indicates the version of row format to output. The possible values are ``V1`` and ``V2`` . The default is ``V1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                parquet_ser_de_property = kinesisfirehose.CfnDeliveryStream.ParquetSerDeProperty(
                    block_size_bytes=123,
                    compression="compression",
                    enable_dictionary_compression=False,
                    max_padding_bytes=123,
                    page_size_bytes=123,
                    writer_version="writerVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d5e42046b59e857630ade1e52237b3f99ec5d3fcea0cff6ee85255354c8bc1a9)
                check_type(argname="argument block_size_bytes", value=block_size_bytes, expected_type=type_hints["block_size_bytes"])
                check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
                check_type(argname="argument enable_dictionary_compression", value=enable_dictionary_compression, expected_type=type_hints["enable_dictionary_compression"])
                check_type(argname="argument max_padding_bytes", value=max_padding_bytes, expected_type=type_hints["max_padding_bytes"])
                check_type(argname="argument page_size_bytes", value=page_size_bytes, expected_type=type_hints["page_size_bytes"])
                check_type(argname="argument writer_version", value=writer_version, expected_type=type_hints["writer_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if block_size_bytes is not None:
                self._values["block_size_bytes"] = block_size_bytes
            if compression is not None:
                self._values["compression"] = compression
            if enable_dictionary_compression is not None:
                self._values["enable_dictionary_compression"] = enable_dictionary_compression
            if max_padding_bytes is not None:
                self._values["max_padding_bytes"] = max_padding_bytes
            if page_size_bytes is not None:
                self._values["page_size_bytes"] = page_size_bytes
            if writer_version is not None:
                self._values["writer_version"] = writer_version

        @builtins.property
        def block_size_bytes(self) -> typing.Optional[jsii.Number]:
            '''The Hadoop Distributed File System (HDFS) block size.

            This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Firehose uses this value for padding calculations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-blocksizebytes
            '''
            result = self._values.get("block_size_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def compression(self) -> typing.Optional[builtins.str]:
            '''The compression code to use over data blocks.

            The possible values are ``UNCOMPRESSED`` , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for higher decompression speed. Use ``GZIP`` if the compression ratio is more important than speed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-compression
            '''
            result = self._values.get("compression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enable_dictionary_compression(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether to enable dictionary compression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-enabledictionarycompression
            '''
            result = self._values.get("enable_dictionary_compression")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def max_padding_bytes(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of padding to apply.

            This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-maxpaddingbytes
            '''
            result = self._values.get("max_padding_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def page_size_bytes(self) -> typing.Optional[jsii.Number]:
            '''The Parquet page size.

            Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-pagesizebytes
            '''
            result = self._values.get("page_size_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def writer_version(self) -> typing.Optional[builtins.str]:
            '''Indicates the version of row format to output.

            The possible values are ``V1`` and ``V2`` . The default is ``V1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-writerversion
            '''
            result = self._values.get("writer_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParquetSerDeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.PartitionFieldProperty",
        jsii_struct_bases=[],
        name_mapping={"source_name": "sourceName"},
    )
    class PartitionFieldProperty:
        def __init__(self, *, source_name: builtins.str) -> None:
            '''Represents a single field in a ``PartitionSpec`` .

            Amazon Data Firehose is in preview release and is subject to change.

            :param source_name: The column name to be configured in partition spec. Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-partitionfield.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                partition_field_property = kinesisfirehose.CfnDeliveryStream.PartitionFieldProperty(
                    source_name="sourceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a839897ef0a46c7170de280f66ed4688ca42be1fcb75c29fba57bc1f602931c1)
                check_type(argname="argument source_name", value=source_name, expected_type=type_hints["source_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source_name": source_name,
            }

        @builtins.property
        def source_name(self) -> builtins.str:
            '''The column name to be configured in partition spec.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-partitionfield.html#cfn-kinesisfirehose-deliverystream-partitionfield-sourcename
            '''
            result = self._values.get("source_name")
            assert result is not None, "Required property 'source_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PartitionFieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.PartitionSpecProperty",
        jsii_struct_bases=[],
        name_mapping={"identity": "identity"},
    )
    class PartitionSpecProperty:
        def __init__(
            self,
            *,
            identity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.PartitionFieldProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Represents how to produce partition data for a table.

            Partition data is produced by transforming columns in a table. Each column transform is represented by a named ``PartitionField`` .

            Here is an example of the schema in JSON.

            ``"partitionSpec": { "identity": [ {"sourceName": "column1"}, {"sourceName": "column2"}, {"sourceName": "column3"} ] }``

            Amazon Data Firehose is in preview release and is subject to change.

            :param identity: List of identity `transforms <https://docs.aws.amazon.com/https://iceberg.apache.org/spec/#partition-transforms>`_ that performs an identity transformation. The transform takes the source value, and does not modify it. Result type is the source type. Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-partitionspec.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                partition_spec_property = kinesisfirehose.CfnDeliveryStream.PartitionSpecProperty(
                    identity=[kinesisfirehose.CfnDeliveryStream.PartitionFieldProperty(
                        source_name="sourceName"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__605b75f57047594e41cbdfa3a36b644835c149c59b7bc3649d482257f34c89b4)
                check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if identity is not None:
                self._values["identity"] = identity

        @builtins.property
        def identity(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.PartitionFieldProperty"]]]]:
            '''List of identity `transforms <https://docs.aws.amazon.com/https://iceberg.apache.org/spec/#partition-transforms>`_ that performs an identity transformation. The transform takes the source value, and does not modify it. Result type is the source type.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-partitionspec.html#cfn-kinesisfirehose-deliverystream-partitionspec-identity
            '''
            result = self._values.get("identity")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.PartitionFieldProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PartitionSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "processors": "processors"},
    )
    class ProcessingConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            processors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessorProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``ProcessingConfiguration`` property configures data processing for an Amazon Kinesis Data Firehose delivery stream.

            :param enabled: Indicates whether data processing is enabled (true) or disabled (false).
            :param processors: The data processors.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                processing_configuration_property = kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                    enabled=False,
                    processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                        type="type",
                
                        # the properties below are optional
                        parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                            parameter_name="parameterName",
                            parameter_value="parameterValue"
                        )]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__47d08fb3fe02427fce54795dba1288ad02d1fec20884867948eae460f986d43d)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument processors", value=processors, expected_type=type_hints["processors"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if processors is not None:
                self._values["processors"] = processors

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether data processing is enabled (true) or disabled (false).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html#cfn-kinesisfirehose-deliverystream-processingconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def processors(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessorProperty"]]]]:
            '''The data processors.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html#cfn-kinesisfirehose-deliverystream-processingconfiguration-processors
            '''
            result = self._values.get("processors")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessorProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProcessingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class ProcessorParameterProperty:
        def __init__(
            self,
            *,
            parameter_name: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''The ``ProcessorParameter`` property specifies a processor parameter in a data processor for an Amazon Kinesis Data Firehose delivery stream.

            :param parameter_name: The name of the parameter. Currently the following default values are supported: 3 for ``NumberOfRetries`` and 60 for the ``BufferIntervalInSeconds`` . The ``BufferSizeInMBs`` ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB.
            :param parameter_value: The parameter value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                processor_parameter_property = kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__29244e412176b0b05c7328e22087c12ec9670a06bdeda2a69994a31022941e39)
                check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parameter_name": parameter_name,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_name(self) -> builtins.str:
            '''The name of the parameter.

            Currently the following default values are supported: 3 for ``NumberOfRetries`` and 60 for the ``BufferIntervalInSeconds`` . The ``BufferSizeInMBs`` ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html#cfn-kinesisfirehose-deliverystream-processorparameter-parametername
            '''
            result = self._values.get("parameter_name")
            assert result is not None, "Required property 'parameter_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''The parameter value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html#cfn-kinesisfirehose-deliverystream-processorparameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProcessorParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ProcessorProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "parameters": "parameters"},
    )
    class ProcessorProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessorParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``Processor`` property specifies a data processor for an Amazon Kinesis Data Firehose delivery stream.

            :param type: The type of processor. Valid values: ``Lambda`` .
            :param parameters: The processor parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                processor_property = kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                    type="type",
                
                    # the properties below are optional
                    parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                        parameter_name="parameterName",
                        parameter_value="parameterValue"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__69c6d7cb07c53f27959cf35e3f4436c85b60c102a9d091138cad44aec29a7fc3)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of processor.

            Valid values: ``Lambda`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html#cfn-kinesisfirehose-deliverystream-processor-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessorParameterProperty"]]]]:
            '''The processor parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html#cfn-kinesisfirehose-deliverystream-processor-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessorParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProcessorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.RedshiftDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cluster_jdbcurl": "clusterJdbcurl",
            "copy_command": "copyCommand",
            "role_arn": "roleArn",
            "s3_configuration": "s3Configuration",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "password": "password",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_configuration": "s3BackupConfiguration",
            "s3_backup_mode": "s3BackupMode",
            "secrets_manager_configuration": "secretsManagerConfiguration",
            "username": "username",
        },
    )
    class RedshiftDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            cluster_jdbcurl: builtins.str,
            copy_command: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CopyCommandProperty", typing.Dict[builtins.str, typing.Any]]],
            role_arn: builtins.str,
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            password: typing.Optional[builtins.str] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.RedshiftRetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
            secrets_manager_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SecretsManagerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``RedshiftDestinationConfiguration`` property type specifies an Amazon Redshift cluster to which Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivers data.

            :param cluster_jdbcurl: The connection string that Kinesis Data Firehose uses to connect to the Amazon Redshift cluster.
            :param copy_command: Configures the Amazon Redshift ``COPY`` command that Kinesis Data Firehose uses to load data into the cluster from the Amazon S3 bucket.
            :param role_arn: The ARN of the AWS Identity and Access Management (IAM) role that grants Kinesis Data Firehose access to your Amazon S3 bucket and AWS KMS (if you enable data encryption). For more information, see `Grant Kinesis Data Firehose Access to an Amazon Redshift Destination <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-rs>`_ in the *Amazon Kinesis Data Firehose Developer Guide* .
            :param s3_configuration: The S3 bucket where Kinesis Data Firehose first delivers data. After the data is in the bucket, Kinesis Data Firehose uses the ``COPY`` command to load the data into the Amazon Redshift cluster. For the Amazon S3 bucket's compression format, don't specify ``SNAPPY`` or ``ZIP`` because the Amazon Redshift ``COPY`` command doesn't support them.
            :param cloud_watch_logging_options: The CloudWatch logging options for your Firehose stream.
            :param password: The password for the Amazon Redshift user that you specified in the ``Username`` property.
            :param processing_configuration: The data processing configuration for the Kinesis Data Firehose delivery stream.
            :param retry_options: The retry behavior in case Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).
            :param s3_backup_configuration: The configuration for backup in Amazon S3.
            :param s3_backup_mode: The Amazon S3 backup mode. After you create a Firehose stream, you can update it to enable Amazon S3 backup if it is disabled. If backup is enabled, you can't update the Firehose stream to disable it.
            :param secrets_manager_configuration: The configuration that defines how you access secrets for Amazon Redshift.
            :param username: The Amazon Redshift user that has permission to access the Amazon Redshift cluster. This user must have ``INSERT`` privileges for copying data from the Amazon S3 bucket to the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                redshift_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.RedshiftDestinationConfigurationProperty(
                    cluster_jdbcurl="clusterJdbcurl",
                    copy_command=kinesisfirehose.CfnDeliveryStream.CopyCommandProperty(
                        data_table_name="dataTableName",
                
                        # the properties below are optional
                        copy_options="copyOptions",
                        data_table_columns="dataTableColumns"
                    ),
                    role_arn="roleArn",
                    s3_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                
                    # the properties below are optional
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    password="password",
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    retry_options=kinesisfirehose.CfnDeliveryStream.RedshiftRetryOptionsProperty(
                        duration_in_seconds=123
                    ),
                    s3_backup_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                    s3_backup_mode="s3BackupMode",
                    secrets_manager_configuration=kinesisfirehose.CfnDeliveryStream.SecretsManagerConfigurationProperty(
                        enabled=False,
                
                        # the properties below are optional
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    ),
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a05dc5298788a3b9496bc2e383242a0570183c6703c04af2c5e991292f2c58fa)
                check_type(argname="argument cluster_jdbcurl", value=cluster_jdbcurl, expected_type=type_hints["cluster_jdbcurl"])
                check_type(argname="argument copy_command", value=copy_command, expected_type=type_hints["copy_command"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
                check_type(argname="argument s3_backup_configuration", value=s3_backup_configuration, expected_type=type_hints["s3_backup_configuration"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
                check_type(argname="argument secrets_manager_configuration", value=secrets_manager_configuration, expected_type=type_hints["secrets_manager_configuration"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cluster_jdbcurl": cluster_jdbcurl,
                "copy_command": copy_command,
                "role_arn": role_arn,
                "s3_configuration": s3_configuration,
            }
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if password is not None:
                self._values["password"] = password
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_configuration is not None:
                self._values["s3_backup_configuration"] = s3_backup_configuration
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode
            if secrets_manager_configuration is not None:
                self._values["secrets_manager_configuration"] = secrets_manager_configuration
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def cluster_jdbcurl(self) -> builtins.str:
            '''The connection string that Kinesis Data Firehose uses to connect to the Amazon Redshift cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-clusterjdbcurl
            '''
            result = self._values.get("cluster_jdbcurl")
            assert result is not None, "Required property 'cluster_jdbcurl' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def copy_command(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CopyCommandProperty"]:
            '''Configures the Amazon Redshift ``COPY`` command that Kinesis Data Firehose uses to load data into the cluster from the Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-copycommand
            '''
            result = self._values.get("copy_command")
            assert result is not None, "Required property 'copy_command' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CopyCommandProperty"], result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the AWS Identity and Access Management (IAM) role that grants Kinesis Data Firehose access to your Amazon S3 bucket and AWS KMS (if you enable data encryption).

            For more information, see `Grant Kinesis Data Firehose Access to an Amazon Redshift Destination <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-rs>`_ in the *Amazon Kinesis Data Firehose Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''The S3 bucket where Kinesis Data Firehose first delivers data.

            After the data is in the bucket, Kinesis Data Firehose uses the ``COPY`` command to load the data into the Amazon Redshift cluster. For the Amazon S3 bucket's compression format, don't specify ``SNAPPY`` or ``ZIP`` because the Amazon Redshift ``COPY`` command doesn't support them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''The CloudWatch logging options for your Firehose stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''The password for the Amazon Redshift user that you specified in the ``Username`` property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-password
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''The data processing configuration for the Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RedshiftRetryOptionsProperty"]]:
            '''The retry behavior in case Firehose is unable to deliver documents to Amazon Redshift.

            Default value is 3600 (60 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RedshiftRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]]:
            '''The configuration for backup in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3backupconfiguration
            '''
            result = self._values.get("s3_backup_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''The Amazon S3 backup mode.

            After you create a Firehose stream, you can update it to enable Amazon S3 backup if it is disabled. If backup is enabled, you can't update the Firehose stream to disable it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SecretsManagerConfigurationProperty"]]:
            '''The configuration that defines how you access secrets for Amazon Redshift.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-secretsmanagerconfiguration
            '''
            result = self._values.get("secrets_manager_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SecretsManagerConfigurationProperty"]], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''The Amazon Redshift user that has permission to access the Amazon Redshift cluster.

            This user must have ``INSERT`` privileges for copying data from the Amazon S3 bucket to the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.RedshiftRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class RedshiftRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configures retry behavior in case Firehose is unable to deliver documents to Amazon Redshift.

            :param duration_in_seconds: The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt takes longer than the current value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                redshift_retry_options_property = kinesisfirehose.CfnDeliveryStream.RedshiftRetryOptionsProperty(
                    duration_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d0656ad0d58c235ec01fb44e9e595a95164029cf26c86a1e17d49b3de0807568)
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt.

            The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt takes longer than the current value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions.html#cfn-kinesisfirehose-deliverystream-redshiftretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.RetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class RetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes the retry behavior in case Kinesis Data Firehose is unable to deliver data to the specified HTTP endpoint destination, or if it doesn't receive a valid acknowledgment of receipt from the specified HTTP endpoint destination.

            Kinesis Firehose supports any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, MongoDB, and New Relic.

            :param duration_in_seconds: The total amount of time that Kinesis Data Firehose spends on retries. This duration starts after the initial attempt to send data to the custom destination via HTTPS endpoint fails. It doesn't include the periods during which Kinesis Data Firehose waits for acknowledgment from the specified destination after each attempt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-retryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                retry_options_property = kinesisfirehose.CfnDeliveryStream.RetryOptionsProperty(
                    duration_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9f65ebaf68fad95eebbec4bb62ddc86711c9f922e5243b0ef218440713a1dbf3)
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The total amount of time that Kinesis Data Firehose spends on retries.

            This duration starts after the initial attempt to send data to the custom destination via HTTPS endpoint fails. It doesn't include the periods during which Kinesis Data Firehose waits for acknowledgment from the specified destination after each attempt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-retryoptions.html#cfn-kinesisfirehose-deliverystream-retryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_arn": "bucketArn",
            "role_arn": "roleArn",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "compression_format": "compressionFormat",
            "encryption_configuration": "encryptionConfiguration",
            "error_output_prefix": "errorOutputPrefix",
            "prefix": "prefix",
        },
    )
    class S3DestinationConfigurationProperty:
        def __init__(
            self,
            *,
            bucket_arn: builtins.str,
            role_arn: builtins.str,
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.BufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            compression_format: typing.Optional[builtins.str] = None,
            encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            error_output_prefix: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``S3DestinationConfiguration`` property type specifies an Amazon Simple Storage Service (Amazon S3) destination to which Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivers data.

            :param bucket_arn: The Amazon Resource Name (ARN) of the Amazon S3 bucket to send data to.
            :param role_arn: The ARN of an AWS Identity and Access Management (IAM) role that grants Kinesis Data Firehose access to your Amazon S3 bucket and AWS KMS (if you enable data encryption). For more information, see `Grant Kinesis Data Firehose Access to an Amazon S3 Destination <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3>`_ in the *Amazon Kinesis Data Firehose Developer Guide* .
            :param buffering_hints: Configures how Kinesis Data Firehose buffers incoming data while delivering it to the Amazon S3 bucket.
            :param cloud_watch_logging_options: The CloudWatch logging options for your Firehose stream.
            :param compression_format: The type of compression that Kinesis Data Firehose uses to compress the data that it delivers to the Amazon S3 bucket. For valid values, see the ``CompressionFormat`` content for the `S3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_S3DestinationConfiguration.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .
            :param encryption_configuration: Configures Amazon Simple Storage Service (Amazon S3) server-side encryption. Kinesis Data Firehose uses AWS Key Management Service ( AWS KMS) to encrypt the data that it delivers to your Amazon S3 bucket.
            :param error_output_prefix: A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see `Custom Prefixes for Amazon S3 Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`_ .
            :param prefix: A prefix that Kinesis Data Firehose adds to the files that it delivers to the Amazon S3 bucket. The prefix helps you identify the files that Kinesis Data Firehose delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                s3_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                    bucket_arn="bucketArn",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    compression_format="compressionFormat",
                    encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                        kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                            awskms_key_arn="awskmsKeyArn"
                        ),
                        no_encryption_config="noEncryptionConfig"
                    ),
                    error_output_prefix="errorOutputPrefix",
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8569fcc15b3b4467365ecb9c23c43fe8704a4b9efea3337dfd60994daf97d928)
                check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument compression_format", value=compression_format, expected_type=type_hints["compression_format"])
                check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
                check_type(argname="argument error_output_prefix", value=error_output_prefix, expected_type=type_hints["error_output_prefix"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_arn": bucket_arn,
                "role_arn": role_arn,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if compression_format is not None:
                self._values["compression_format"] = compression_format
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration
            if error_output_prefix is not None:
                self._values["error_output_prefix"] = error_output_prefix
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def bucket_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon S3 bucket to send data to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-bucketarn
            '''
            result = self._values.get("bucket_arn")
            assert result is not None, "Required property 'bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of an AWS Identity and Access Management (IAM) role that grants Kinesis Data Firehose access to your Amazon S3 bucket and AWS KMS (if you enable data encryption).

            For more information, see `Grant Kinesis Data Firehose Access to an Amazon S3 Destination <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3>`_ in the *Amazon Kinesis Data Firehose Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.BufferingHintsProperty"]]:
            '''Configures how Kinesis Data Firehose buffers incoming data while delivering it to the Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.BufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''The CloudWatch logging options for your Firehose stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def compression_format(self) -> typing.Optional[builtins.str]:
            '''The type of compression that Kinesis Data Firehose uses to compress the data that it delivers to the Amazon S3 bucket.

            For valid values, see the ``CompressionFormat`` content for the `S3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_S3DestinationConfiguration.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-compressionformat
            '''
            result = self._values.get("compression_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.EncryptionConfigurationProperty"]]:
            '''Configures Amazon Simple Storage Service (Amazon S3) server-side encryption.

            Kinesis Data Firehose uses AWS Key Management Service ( AWS KMS) to encrypt the data that it delivers to your Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.EncryptionConfigurationProperty"]], result)

        @builtins.property
        def error_output_prefix(self) -> typing.Optional[builtins.str]:
            '''A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3.

            This prefix appears immediately following the bucket name. For information about how to specify this prefix, see `Custom Prefixes for Amazon S3 Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-erroroutputprefix
            '''
            result = self._values.get("error_output_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''A prefix that Kinesis Data Firehose adds to the files that it delivers to the Amazon S3 bucket.

            The prefix helps you identify the files that Kinesis Data Firehose delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SchemaConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "region": "region",
            "role_arn": "roleArn",
            "table_name": "tableName",
            "version_id": "versionId",
        },
    )
    class SchemaConfigurationProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
            role_arn: typing.Optional[builtins.str] = None,
            table_name: typing.Optional[builtins.str] = None,
            version_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the schema to which you want Firehose to configure your data before it writes it to Amazon S3.

            This parameter is required if ``Enabled`` is set to true.

            :param catalog_id: The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID is used by default.
            :param database_name: Specifies the name of the AWS Glue database that contains the schema for the output data. .. epigraph:: If the ``SchemaConfiguration`` request parameter is used as part of invoking the ``CreateDeliveryStream`` API, then the ``DatabaseName`` property is required and its value must be specified.
            :param region: If you don't specify an AWS Region, the default is the current Region.
            :param role_arn: The role that Firehose can use to access AWS Glue. This role must be in the same account you use for Firehose. Cross-account roles aren't allowed. .. epigraph:: If the ``SchemaConfiguration`` request parameter is used as part of invoking the ``CreateDeliveryStream`` API, then the ``RoleARN`` property is required and its value must be specified.
            :param table_name: Specifies the AWS Glue table that contains the column information that constitutes your data schema. .. epigraph:: If the ``SchemaConfiguration`` request parameter is used as part of invoking the ``CreateDeliveryStream`` API, then the ``TableName`` property is required and its value must be specified.
            :param version_id: Specifies the table version for the output data schema. If you don't specify this version ID, or if you set it to ``LATEST`` , Firehose uses the most recent version. This means that any updates to the table are automatically picked up.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                schema_configuration_property = kinesisfirehose.CfnDeliveryStream.SchemaConfigurationProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    region="region",
                    role_arn="roleArn",
                    table_name="tableName",
                    version_id="versionId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c1389c57283b687c62069951b51187332947eeb24f5fcb8781af71c2b3e5d657)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if database_name is not None:
                self._values["database_name"] = database_name
            if region is not None:
                self._values["region"] = region
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if table_name is not None:
                self._values["table_name"] = table_name
            if version_id is not None:
                self._values["version_id"] = version_id

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the AWS Glue Data Catalog.

            If you don't supply this, the AWS account ID is used by default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''Specifies the name of the AWS Glue database that contains the schema for the output data.

            .. epigraph::

               If the ``SchemaConfiguration`` request parameter is used as part of invoking the ``CreateDeliveryStream`` API, then the ``DatabaseName`` property is required and its value must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''If you don't specify an AWS Region, the default is the current Region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The role that Firehose can use to access AWS Glue.

            This role must be in the same account you use for Firehose. Cross-account roles aren't allowed.
            .. epigraph::

               If the ``SchemaConfiguration`` request parameter is used as part of invoking the ``CreateDeliveryStream`` API, then the ``RoleARN`` property is required and its value must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_name(self) -> typing.Optional[builtins.str]:
            '''Specifies the AWS Glue table that contains the column information that constitutes your data schema.

            .. epigraph::

               If the ``SchemaConfiguration`` request parameter is used as part of invoking the ``CreateDeliveryStream`` API, then the ``TableName`` property is required and its value must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-tablename
            '''
            result = self._values.get("table_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version_id(self) -> typing.Optional[builtins.str]:
            '''Specifies the table version for the output data schema.

            If you don't specify this version ID, or if you set it to ``LATEST`` , Firehose uses the most recent version. This means that any updates to the table are automatically picked up.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-versionid
            '''
            result = self._values.get("version_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SchemaEvolutionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class SchemaEvolutionConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The configuration to enable schema evolution.

            Amazon Data Firehose is in preview release and is subject to change.

            :param enabled: Specify whether you want to enable schema evolution. Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaevolutionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                schema_evolution_configuration_property = kinesisfirehose.CfnDeliveryStream.SchemaEvolutionConfigurationProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__42267f168762343c22cce7785e160c133f9c7e7a8f4cb3e0888c940a1c3cb61d)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specify whether you want to enable schema evolution.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaevolutionconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaevolutionconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaEvolutionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SecretsManagerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "role_arn": "roleArn",
            "secret_arn": "secretArn",
        },
    )
    class SecretsManagerConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            role_arn: typing.Optional[builtins.str] = None,
            secret_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The structure that defines how Firehose accesses the secret.

            :param enabled: Specifies whether you want to use the secrets manager feature. When set as ``True`` the secrets manager configuration overwrites the existing secrets in the destination configuration. When it's set to ``False`` Firehose falls back to the credentials in the destination configuration.
            :param role_arn: Specifies the role that Firehose assumes when calling the Secrets Manager API operation. When you provide the role, it overrides any destination specific role defined in the destination configuration. If you do not provide the then we use the destination specific role. This parameter is required for Splunk.
            :param secret_arn: The ARN of the secret that stores your credentials. It must be in the same region as the Firehose stream and the role. The secret ARN can reside in a different account than the Firehose stream and role as Firehose supports cross-account secret access. This parameter is required when *Enabled* is set to ``True`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-secretsmanagerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                secrets_manager_configuration_property = kinesisfirehose.CfnDeliveryStream.SecretsManagerConfigurationProperty(
                    enabled=False,
                
                    # the properties below are optional
                    role_arn="roleArn",
                    secret_arn="secretArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b935af4b7f540cbb6b063a9c37a906eaf8c3ed8781b19ea32e1836ca909b3dac)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Specifies whether you want to use the secrets manager feature.

            When set as ``True`` the secrets manager configuration overwrites the existing secrets in the destination configuration. When it's set to ``False`` Firehose falls back to the credentials in the destination configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-secretsmanagerconfiguration.html#cfn-kinesisfirehose-deliverystream-secretsmanagerconfiguration-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''Specifies the role that Firehose assumes when calling the Secrets Manager API operation.

            When you provide the role, it overrides any destination specific role defined in the destination configuration. If you do not provide the then we use the destination specific role. This parameter is required for Splunk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-secretsmanagerconfiguration.html#cfn-kinesisfirehose-deliverystream-secretsmanagerconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the secret that stores your credentials.

            It must be in the same region as the Firehose stream and the role. The secret ARN can reside in a different account than the Firehose stream and role as Firehose supports cross-account secret access. This parameter is required when *Enabled* is set to ``True`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-secretsmanagerconfiguration.html#cfn-kinesisfirehose-deliverystream-secretsmanagerconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecretsManagerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SerializerProperty",
        jsii_struct_bases=[],
        name_mapping={"orc_ser_de": "orcSerDe", "parquet_ser_de": "parquetSerDe"},
    )
    class SerializerProperty:
        def __init__(
            self,
            *,
            orc_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.OrcSerDeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            parquet_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ParquetSerDeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The serializer that you want Firehose to use to convert data to the target format before writing it to Amazon S3.

            Firehose supports two types of serializers: the ORC SerDe and the Parquet SerDe.

            :param orc_ser_de: A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see `Apache ORC <https://docs.aws.amazon.com/https://orc.apache.org/docs/>`_ .
            :param parquet_ser_de: A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see `Apache Parquet <https://docs.aws.amazon.com/https://parquet.apache.org/docs/contribution-guidelines/>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                serializer_property = kinesisfirehose.CfnDeliveryStream.SerializerProperty(
                    orc_ser_de=kinesisfirehose.CfnDeliveryStream.OrcSerDeProperty(
                        block_size_bytes=123,
                        bloom_filter_columns=["bloomFilterColumns"],
                        bloom_filter_false_positive_probability=123,
                        compression="compression",
                        dictionary_key_threshold=123,
                        enable_padding=False,
                        format_version="formatVersion",
                        padding_tolerance=123,
                        row_index_stride=123,
                        stripe_size_bytes=123
                    ),
                    parquet_ser_de=kinesisfirehose.CfnDeliveryStream.ParquetSerDeProperty(
                        block_size_bytes=123,
                        compression="compression",
                        enable_dictionary_compression=False,
                        max_padding_bytes=123,
                        page_size_bytes=123,
                        writer_version="writerVersion"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__706925197a1b663cd9be8234e85ce2780b58d7bf71737c801e0c393104407464)
                check_type(argname="argument orc_ser_de", value=orc_ser_de, expected_type=type_hints["orc_ser_de"])
                check_type(argname="argument parquet_ser_de", value=parquet_ser_de, expected_type=type_hints["parquet_ser_de"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if orc_ser_de is not None:
                self._values["orc_ser_de"] = orc_ser_de
            if parquet_ser_de is not None:
                self._values["parquet_ser_de"] = parquet_ser_de

        @builtins.property
        def orc_ser_de(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.OrcSerDeProperty"]]:
            '''A serializer to use for converting data to the ORC format before storing it in Amazon S3.

            For more information, see `Apache ORC <https://docs.aws.amazon.com/https://orc.apache.org/docs/>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html#cfn-kinesisfirehose-deliverystream-serializer-orcserde
            '''
            result = self._values.get("orc_ser_de")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.OrcSerDeProperty"]], result)

        @builtins.property
        def parquet_ser_de(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ParquetSerDeProperty"]]:
            '''A serializer to use for converting data to the Parquet format before storing it in Amazon S3.

            For more information, see `Apache Parquet <https://docs.aws.amazon.com/https://parquet.apache.org/docs/contribution-guidelines/>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html#cfn-kinesisfirehose-deliverystream-serializer-parquetserde
            '''
            result = self._values.get("parquet_ser_de")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ParquetSerDeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SerializerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SnowflakeBufferingHintsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interval_in_seconds": "intervalInSeconds",
            "size_in_m_bs": "sizeInMBs",
        },
    )
    class SnowflakeBufferingHintsProperty:
        def __init__(
            self,
            *,
            interval_in_seconds: typing.Optional[jsii.Number] = None,
            size_in_m_bs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes the buffering to perform before delivering data to the Snowflake destination.

            If you do not specify any value, Firehose uses the default values.

            :param interval_in_seconds: Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 0.
            :param size_in_m_bs: Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 128.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakebufferinghints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                snowflake_buffering_hints_property = kinesisfirehose.CfnDeliveryStream.SnowflakeBufferingHintsProperty(
                    interval_in_seconds=123,
                    size_in_mBs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c4d37eb171641c85a4fd06dfff9a42a4ac04df542059c602ae6c3ce07e369214)
                check_type(argname="argument interval_in_seconds", value=interval_in_seconds, expected_type=type_hints["interval_in_seconds"])
                check_type(argname="argument size_in_m_bs", value=size_in_m_bs, expected_type=type_hints["size_in_m_bs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if interval_in_seconds is not None:
                self._values["interval_in_seconds"] = interval_in_seconds
            if size_in_m_bs is not None:
                self._values["size_in_m_bs"] = size_in_m_bs

        @builtins.property
        def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination.

            The default value is 0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakebufferinghints.html#cfn-kinesisfirehose-deliverystream-snowflakebufferinghints-intervalinseconds
            '''
            result = self._values.get("interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size_in_m_bs(self) -> typing.Optional[jsii.Number]:
            '''Buffer incoming data to the specified size, in MBs, before delivering it to the destination.

            The default value is 128.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakebufferinghints.html#cfn-kinesisfirehose-deliverystream-snowflakebufferinghints-sizeinmbs
            '''
            result = self._values.get("size_in_m_bs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeBufferingHintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SnowflakeDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_url": "accountUrl",
            "database": "database",
            "role_arn": "roleArn",
            "s3_configuration": "s3Configuration",
            "schema": "schema",
            "table": "table",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "content_column_name": "contentColumnName",
            "data_loading_option": "dataLoadingOption",
            "key_passphrase": "keyPassphrase",
            "meta_data_column_name": "metaDataColumnName",
            "private_key": "privateKey",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_mode": "s3BackupMode",
            "secrets_manager_configuration": "secretsManagerConfiguration",
            "snowflake_role_configuration": "snowflakeRoleConfiguration",
            "snowflake_vpc_configuration": "snowflakeVpcConfiguration",
            "user": "user",
        },
    )
    class SnowflakeDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            account_url: builtins.str,
            database: builtins.str,
            role_arn: builtins.str,
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            schema: builtins.str,
            table: builtins.str,
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SnowflakeBufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            content_column_name: typing.Optional[builtins.str] = None,
            data_loading_option: typing.Optional[builtins.str] = None,
            key_passphrase: typing.Optional[builtins.str] = None,
            meta_data_column_name: typing.Optional[builtins.str] = None,
            private_key: typing.Optional[builtins.str] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SnowflakeRetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
            secrets_manager_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SecretsManagerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            snowflake_role_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SnowflakeRoleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            snowflake_vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SnowflakeVpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            user: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configure Snowflake destination.

            :param account_url: URL for accessing your Snowflake account. This URL must include your `account identifier <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/admin-account-identifier>`_ . Note that the protocol (https://) and port number are optional.
            :param database: All data in Snowflake is maintained in databases.
            :param role_arn: The Amazon Resource Name (ARN) of the Snowflake role.
            :param s3_configuration: 
            :param schema: Each database consists of one or more schemas, which are logical groupings of database objects, such as tables and views.
            :param table: All data in Snowflake is stored in database tables, logically structured as collections of columns and rows.
            :param buffering_hints: Describes the buffering to perform before delivering data to the Snowflake destination. If you do not specify any value, Firehose uses the default values.
            :param cloud_watch_logging_options: 
            :param content_column_name: The name of the record content column.
            :param data_loading_option: Choose to load JSON keys mapped to table column names or choose to split the JSON payload where content is mapped to a record content column and source metadata is mapped to a record metadata column.
            :param key_passphrase: Passphrase to decrypt the private key when the key is encrypted. For information, see `Using Key Pair Authentication & Key Rotation <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation>`_ .
            :param meta_data_column_name: Specify a column name in the table, where the metadata information has to be loaded. When you enable this field, you will see the following column in the snowflake table, which differs based on the source type. For Direct PUT as source ``{ "firehoseDeliveryStreamName" : "streamname", "IngestionTime" : "timestamp" }`` For Kinesis Data Stream as source ``"kinesisStreamName" : "streamname", "kinesisShardId" : "Id", "kinesisPartitionKey" : "key", "kinesisSequenceNumber" : "1234", "subsequenceNumber" : "2334", "IngestionTime" : "timestamp" }``
            :param private_key: The private key used to encrypt your Snowflake client. For information, see `Using Key Pair Authentication & Key Rotation <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation>`_ .
            :param processing_configuration: 
            :param retry_options: The time period where Firehose will retry sending data to the chosen HTTP endpoint.
            :param s3_backup_mode: Choose an S3 backup mode.
            :param secrets_manager_configuration: The configuration that defines how you access secrets for Snowflake.
            :param snowflake_role_configuration: Optionally configure a Snowflake role. Otherwise the default user role will be used.
            :param snowflake_vpc_configuration: The VPCE ID for Firehose to privately connect with Snowflake. The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see `Amazon PrivateLink & Snowflake <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/admin-security-privatelink>`_
            :param user: User login name for the Snowflake account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                snowflake_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.SnowflakeDestinationConfigurationProperty(
                    account_url="accountUrl",
                    database="database",
                    role_arn="roleArn",
                    s3_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                    schema="schema",
                    table="table",
                
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.SnowflakeBufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    content_column_name="contentColumnName",
                    data_loading_option="dataLoadingOption",
                    key_passphrase="keyPassphrase",
                    meta_data_column_name="metaDataColumnName",
                    private_key="privateKey",
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    retry_options=kinesisfirehose.CfnDeliveryStream.SnowflakeRetryOptionsProperty(
                        duration_in_seconds=123
                    ),
                    s3_backup_mode="s3BackupMode",
                    secrets_manager_configuration=kinesisfirehose.CfnDeliveryStream.SecretsManagerConfigurationProperty(
                        enabled=False,
                
                        # the properties below are optional
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    ),
                    snowflake_role_configuration=kinesisfirehose.CfnDeliveryStream.SnowflakeRoleConfigurationProperty(
                        enabled=False,
                        snowflake_role="snowflakeRole"
                    ),
                    snowflake_vpc_configuration=kinesisfirehose.CfnDeliveryStream.SnowflakeVpcConfigurationProperty(
                        private_link_vpce_id="privateLinkVpceId"
                    ),
                    user="user"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9743b3910a7f4b6edd05f7d4a76aa45c5a9f674a473fcf4c8c046e1d8d64cb53)
                check_type(argname="argument account_url", value=account_url, expected_type=type_hints["account_url"])
                check_type(argname="argument database", value=database, expected_type=type_hints["database"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
                check_type(argname="argument table", value=table, expected_type=type_hints["table"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument content_column_name", value=content_column_name, expected_type=type_hints["content_column_name"])
                check_type(argname="argument data_loading_option", value=data_loading_option, expected_type=type_hints["data_loading_option"])
                check_type(argname="argument key_passphrase", value=key_passphrase, expected_type=type_hints["key_passphrase"])
                check_type(argname="argument meta_data_column_name", value=meta_data_column_name, expected_type=type_hints["meta_data_column_name"])
                check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
                check_type(argname="argument secrets_manager_configuration", value=secrets_manager_configuration, expected_type=type_hints["secrets_manager_configuration"])
                check_type(argname="argument snowflake_role_configuration", value=snowflake_role_configuration, expected_type=type_hints["snowflake_role_configuration"])
                check_type(argname="argument snowflake_vpc_configuration", value=snowflake_vpc_configuration, expected_type=type_hints["snowflake_vpc_configuration"])
                check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_url": account_url,
                "database": database,
                "role_arn": role_arn,
                "s3_configuration": s3_configuration,
                "schema": schema,
                "table": table,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if content_column_name is not None:
                self._values["content_column_name"] = content_column_name
            if data_loading_option is not None:
                self._values["data_loading_option"] = data_loading_option
            if key_passphrase is not None:
                self._values["key_passphrase"] = key_passphrase
            if meta_data_column_name is not None:
                self._values["meta_data_column_name"] = meta_data_column_name
            if private_key is not None:
                self._values["private_key"] = private_key
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode
            if secrets_manager_configuration is not None:
                self._values["secrets_manager_configuration"] = secrets_manager_configuration
            if snowflake_role_configuration is not None:
                self._values["snowflake_role_configuration"] = snowflake_role_configuration
            if snowflake_vpc_configuration is not None:
                self._values["snowflake_vpc_configuration"] = snowflake_vpc_configuration
            if user is not None:
                self._values["user"] = user

        @builtins.property
        def account_url(self) -> builtins.str:
            '''URL for accessing your Snowflake account.

            This URL must include your `account identifier <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/admin-account-identifier>`_ . Note that the protocol (https://) and port number are optional.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-accounturl
            '''
            result = self._values.get("account_url")
            assert result is not None, "Required property 'account_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database(self) -> builtins.str:
            '''All data in Snowflake is maintained in databases.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-database
            '''
            result = self._values.get("database")
            assert result is not None, "Required property 'database' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Snowflake role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def schema(self) -> builtins.str:
            '''Each database consists of one or more schemas, which are logical groupings of database objects, such as tables and views.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-schema
            '''
            result = self._values.get("schema")
            assert result is not None, "Required property 'schema' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table(self) -> builtins.str:
            '''All data in Snowflake is stored in database tables, logically structured as collections of columns and rows.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-table
            '''
            result = self._values.get("table")
            assert result is not None, "Required property 'table' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeBufferingHintsProperty"]]:
            '''Describes the buffering to perform before delivering data to the Snowflake destination.

            If you do not specify any value, Firehose uses the default values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeBufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def content_column_name(self) -> typing.Optional[builtins.str]:
            '''The name of the record content column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-contentcolumnname
            '''
            result = self._values.get("content_column_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_loading_option(self) -> typing.Optional[builtins.str]:
            '''Choose to load JSON keys mapped to table column names or choose to split the JSON payload where content is mapped to a record content column and source metadata is mapped to a record metadata column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-dataloadingoption
            '''
            result = self._values.get("data_loading_option")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_passphrase(self) -> typing.Optional[builtins.str]:
            '''Passphrase to decrypt the private key when the key is encrypted.

            For information, see `Using Key Pair Authentication & Key Rotation <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-keypassphrase
            '''
            result = self._values.get("key_passphrase")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def meta_data_column_name(self) -> typing.Optional[builtins.str]:
            '''Specify a column name in the table, where the metadata information has to be loaded.

            When you enable this field, you will see the following column in the snowflake table, which differs based on the source type.

            For Direct PUT as source

            ``{ "firehoseDeliveryStreamName" : "streamname", "IngestionTime" : "timestamp" }``

            For Kinesis Data Stream as source

            ``"kinesisStreamName" : "streamname", "kinesisShardId" : "Id", "kinesisPartitionKey" : "key", "kinesisSequenceNumber" : "1234", "subsequenceNumber" : "2334", "IngestionTime" : "timestamp" }``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-metadatacolumnname
            '''
            result = self._values.get("meta_data_column_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def private_key(self) -> typing.Optional[builtins.str]:
            '''The private key used to encrypt your Snowflake client.

            For information, see `Using Key Pair Authentication & Key Rotation <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-privatekey
            '''
            result = self._values.get("private_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeRetryOptionsProperty"]]:
            '''The time period where Firehose will retry sending data to the chosen HTTP endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''Choose an S3 backup mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SecretsManagerConfigurationProperty"]]:
            '''The configuration that defines how you access secrets for Snowflake.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-secretsmanagerconfiguration
            '''
            result = self._values.get("secrets_manager_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SecretsManagerConfigurationProperty"]], result)

        @builtins.property
        def snowflake_role_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeRoleConfigurationProperty"]]:
            '''Optionally configure a Snowflake role.

            Otherwise the default user role will be used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-snowflakeroleconfiguration
            '''
            result = self._values.get("snowflake_role_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeRoleConfigurationProperty"]], result)

        @builtins.property
        def snowflake_vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeVpcConfigurationProperty"]]:
            '''The VPCE ID for Firehose to privately connect with Snowflake.

            The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see `Amazon PrivateLink & Snowflake <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/admin-security-privatelink>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-snowflakevpcconfiguration
            '''
            result = self._values.get("snowflake_vpc_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeVpcConfigurationProperty"]], result)

        @builtins.property
        def user(self) -> typing.Optional[builtins.str]:
            '''User login name for the Snowflake account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-user
            '''
            result = self._values.get("user")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SnowflakeRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class SnowflakeRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specify how long Firehose retries sending data to the New Relic HTTP endpoint.

            After sending data, Firehose first waits for an acknowledgment from the HTTP endpoint. If an error occurs or the acknowledgment doesn’t arrive within the acknowledgment timeout period, Firehose starts the retry duration counter. It keeps retrying until the retry duration expires. After that, Firehose considers it a data delivery failure and backs up the data to your Amazon S3 bucket. Every time that Firehose sends data to the HTTP endpoint (either the initial attempt or a retry), it restarts the acknowledgement timeout counter and waits for an acknowledgement from the HTTP endpoint. Even if the retry duration expires, Firehose still waits for the acknowledgment until it receives it or the acknowledgement timeout period is reached. If the acknowledgment times out, Firehose determines whether there's time left in the retry counter. If there is time left, it retries again and repeats the logic until it receives an acknowledgment or determines that the retry time has expired. If you don't want Firehose to retry sending data, set this value to 0.

            :param duration_in_seconds: the time period where Firehose will retry sending data to the chosen HTTP endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakeretryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                snowflake_retry_options_property = kinesisfirehose.CfnDeliveryStream.SnowflakeRetryOptionsProperty(
                    duration_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b7d919c23da3109305810f31f91a7020b20f997fbd66a87a4b4dfe122efff981)
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''the time period where Firehose will retry sending data to the chosen HTTP endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakeretryoptions.html#cfn-kinesisfirehose-deliverystream-snowflakeretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SnowflakeRoleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "snowflake_role": "snowflakeRole"},
    )
    class SnowflakeRoleConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            snowflake_role: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Optionally configure a Snowflake role.

            Otherwise the default user role will be used.

            :param enabled: Enable Snowflake role.
            :param snowflake_role: The Snowflake role you wish to configure.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakeroleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                snowflake_role_configuration_property = kinesisfirehose.CfnDeliveryStream.SnowflakeRoleConfigurationProperty(
                    enabled=False,
                    snowflake_role="snowflakeRole"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__867673ab46f448fd1867f3b74172d4939969188f736abc7f1c5c26682419368b)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument snowflake_role", value=snowflake_role, expected_type=type_hints["snowflake_role"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if snowflake_role is not None:
                self._values["snowflake_role"] = snowflake_role

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enable Snowflake role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakeroleconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakeroleconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def snowflake_role(self) -> typing.Optional[builtins.str]:
            '''The Snowflake role you wish to configure.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakeroleconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakeroleconfiguration-snowflakerole
            '''
            result = self._values.get("snowflake_role")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeRoleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SnowflakeVpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"private_link_vpce_id": "privateLinkVpceId"},
    )
    class SnowflakeVpcConfigurationProperty:
        def __init__(self, *, private_link_vpce_id: builtins.str) -> None:
            '''Configure a Snowflake VPC.

            :param private_link_vpce_id: The VPCE ID for Firehose to privately connect with Snowflake. The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see `Amazon PrivateLink & Snowflake <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/admin-security-privatelink>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakevpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                snowflake_vpc_configuration_property = kinesisfirehose.CfnDeliveryStream.SnowflakeVpcConfigurationProperty(
                    private_link_vpce_id="privateLinkVpceId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5715c831de8e3fe729e9e76213a2b933810f642d09eb653534a3d23054acf0d)
                check_type(argname="argument private_link_vpce_id", value=private_link_vpce_id, expected_type=type_hints["private_link_vpce_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "private_link_vpce_id": private_link_vpce_id,
            }

        @builtins.property
        def private_link_vpce_id(self) -> builtins.str:
            '''The VPCE ID for Firehose to privately connect with Snowflake.

            The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see `Amazon PrivateLink & Snowflake <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/admin-security-privatelink>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakevpcconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakevpcconfiguration-privatelinkvpceid
            '''
            result = self._values.get("private_link_vpce_id")
            assert result is not None, "Required property 'private_link_vpce_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeVpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SplunkBufferingHintsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interval_in_seconds": "intervalInSeconds",
            "size_in_m_bs": "sizeInMBs",
        },
    )
    class SplunkBufferingHintsProperty:
        def __init__(
            self,
            *,
            interval_in_seconds: typing.Optional[jsii.Number] = None,
            size_in_m_bs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The buffering options.

            If no value is specified, the default values for Splunk are used.

            :param interval_in_seconds: Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 60 (1 minute).
            :param size_in_m_bs: Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkbufferinghints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                splunk_buffering_hints_property = kinesisfirehose.CfnDeliveryStream.SplunkBufferingHintsProperty(
                    interval_in_seconds=123,
                    size_in_mBs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__60823c61f8aea3242c07551788af8f338bff46b6299ee9aa1d0ff6112c454ecc)
                check_type(argname="argument interval_in_seconds", value=interval_in_seconds, expected_type=type_hints["interval_in_seconds"])
                check_type(argname="argument size_in_m_bs", value=size_in_m_bs, expected_type=type_hints["size_in_m_bs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if interval_in_seconds is not None:
                self._values["interval_in_seconds"] = interval_in_seconds
            if size_in_m_bs is not None:
                self._values["size_in_m_bs"] = size_in_m_bs

        @builtins.property
        def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination.

            The default value is 60 (1 minute).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkbufferinghints.html#cfn-kinesisfirehose-deliverystream-splunkbufferinghints-intervalinseconds
            '''
            result = self._values.get("interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size_in_m_bs(self) -> typing.Optional[jsii.Number]:
            '''Buffer incoming data to the specified size, in MBs, before delivering it to the destination.

            The default value is 5.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkbufferinghints.html#cfn-kinesisfirehose-deliverystream-splunkbufferinghints-sizeinmbs
            '''
            result = self._values.get("size_in_m_bs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SplunkBufferingHintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SplunkDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hec_endpoint": "hecEndpoint",
            "hec_endpoint_type": "hecEndpointType",
            "s3_configuration": "s3Configuration",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "hec_acknowledgment_timeout_in_seconds": "hecAcknowledgmentTimeoutInSeconds",
            "hec_token": "hecToken",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_mode": "s3BackupMode",
            "secrets_manager_configuration": "secretsManagerConfiguration",
        },
    )
    class SplunkDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            hec_endpoint: builtins.str,
            hec_endpoint_type: builtins.str,
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SplunkBufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            hec_acknowledgment_timeout_in_seconds: typing.Optional[jsii.Number] = None,
            hec_token: typing.Optional[builtins.str] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SplunkRetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
            secrets_manager_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SecretsManagerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The ``SplunkDestinationConfiguration`` property type specifies the configuration of a destination in Splunk for a Kinesis Data Firehose delivery stream.

            :param hec_endpoint: The HTTP Event Collector (HEC) endpoint to which Firehose sends your data.
            :param hec_endpoint_type: This type can be either ``Raw`` or ``Event`` .
            :param s3_configuration: The configuration for the backup Amazon S3 location.
            :param buffering_hints: The buffering options. If no value is specified, the default values for Splunk are used.
            :param cloud_watch_logging_options: The Amazon CloudWatch logging options for your Firehose stream.
            :param hec_acknowledgment_timeout_in_seconds: The amount of time that Firehose waits to receive an acknowledgment from Splunk after it sends it data. At the end of the timeout period, Firehose either tries to send the data again or considers it an error, based on your retry settings.
            :param hec_token: This is a GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.
            :param processing_configuration: The data processing configuration.
            :param retry_options: The retry behavior in case Firehose is unable to deliver data to Splunk, or if it doesn't receive an acknowledgment of receipt from Splunk.
            :param s3_backup_mode: Defines how documents should be delivered to Amazon S3. When set to ``FailedEventsOnly`` , Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to ``AllEvents`` , Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. The default value is ``FailedEventsOnly`` . You can update this backup mode from ``FailedEventsOnly`` to ``AllEvents`` . You can't update it from ``AllEvents`` to ``FailedEventsOnly`` .
            :param secrets_manager_configuration: The configuration that defines how you access secrets for Splunk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                splunk_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.SplunkDestinationConfigurationProperty(
                    hec_endpoint="hecEndpoint",
                    hec_endpoint_type="hecEndpointType",
                    s3_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.SplunkBufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    hec_acknowledgment_timeout_in_seconds=123,
                    hec_token="hecToken",
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    retry_options=kinesisfirehose.CfnDeliveryStream.SplunkRetryOptionsProperty(
                        duration_in_seconds=123
                    ),
                    s3_backup_mode="s3BackupMode",
                    secrets_manager_configuration=kinesisfirehose.CfnDeliveryStream.SecretsManagerConfigurationProperty(
                        enabled=False,
                
                        # the properties below are optional
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be9923ea7818bcdc567ae6e06b529c44c6a3c42b59af06768977f4c55fdd20a6)
                check_type(argname="argument hec_endpoint", value=hec_endpoint, expected_type=type_hints["hec_endpoint"])
                check_type(argname="argument hec_endpoint_type", value=hec_endpoint_type, expected_type=type_hints["hec_endpoint_type"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument hec_acknowledgment_timeout_in_seconds", value=hec_acknowledgment_timeout_in_seconds, expected_type=type_hints["hec_acknowledgment_timeout_in_seconds"])
                check_type(argname="argument hec_token", value=hec_token, expected_type=type_hints["hec_token"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
                check_type(argname="argument secrets_manager_configuration", value=secrets_manager_configuration, expected_type=type_hints["secrets_manager_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "hec_endpoint": hec_endpoint,
                "hec_endpoint_type": hec_endpoint_type,
                "s3_configuration": s3_configuration,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if hec_acknowledgment_timeout_in_seconds is not None:
                self._values["hec_acknowledgment_timeout_in_seconds"] = hec_acknowledgment_timeout_in_seconds
            if hec_token is not None:
                self._values["hec_token"] = hec_token
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode
            if secrets_manager_configuration is not None:
                self._values["secrets_manager_configuration"] = secrets_manager_configuration

        @builtins.property
        def hec_endpoint(self) -> builtins.str:
            '''The HTTP Event Collector (HEC) endpoint to which Firehose sends your data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecendpoint
            '''
            result = self._values.get("hec_endpoint")
            assert result is not None, "Required property 'hec_endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hec_endpoint_type(self) -> builtins.str:
            '''This type can be either ``Raw`` or ``Event`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecendpointtype
            '''
            result = self._values.get("hec_endpoint_type")
            assert result is not None, "Required property 'hec_endpoint_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''The configuration for the backup Amazon S3 location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SplunkBufferingHintsProperty"]]:
            '''The buffering options.

            If no value is specified, the default values for Splunk are used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SplunkBufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''The Amazon CloudWatch logging options for your Firehose stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def hec_acknowledgment_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The amount of time that Firehose waits to receive an acknowledgment from Splunk after it sends it data.

            At the end of the timeout period, Firehose either tries to send the data again or considers it an error, based on your retry settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecacknowledgmenttimeoutinseconds
            '''
            result = self._values.get("hec_acknowledgment_timeout_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def hec_token(self) -> typing.Optional[builtins.str]:
            '''This is a GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hectoken
            '''
            result = self._values.get("hec_token")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''The data processing configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SplunkRetryOptionsProperty"]]:
            '''The retry behavior in case Firehose is unable to deliver data to Splunk, or if it doesn't receive an acknowledgment of receipt from Splunk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SplunkRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''Defines how documents should be delivered to Amazon S3.

            When set to ``FailedEventsOnly`` , Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to ``AllEvents`` , Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. The default value is ``FailedEventsOnly`` .

            You can update this backup mode from ``FailedEventsOnly`` to ``AllEvents`` . You can't update it from ``AllEvents`` to ``FailedEventsOnly`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SecretsManagerConfigurationProperty"]]:
            '''The configuration that defines how you access secrets for Splunk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-secretsmanagerconfiguration
            '''
            result = self._values.get("secrets_manager_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SecretsManagerConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SplunkDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SplunkRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class SplunkRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ``SplunkRetryOptions`` property type specifies retry behavior in case Kinesis Data Firehose is unable to deliver documents to Splunk or if it doesn't receive an acknowledgment from Splunk.

            :param duration_in_seconds: The total amount of time that Firehose spends on retries. This duration starts after the initial attempt to send data to Splunk fails. It doesn't include the periods during which Firehose waits for acknowledgment from Splunk after each attempt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkretryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                splunk_retry_options_property = kinesisfirehose.CfnDeliveryStream.SplunkRetryOptionsProperty(
                    duration_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5c5cbe7244c68f12454d07974a4cae50f1d208afdbc3a96f1e2ada11e37fc412)
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The total amount of time that Firehose spends on retries.

            This duration starts after the initial attempt to send data to Splunk fails. It doesn't include the periods during which Firehose waits for acknowledgment from Splunk after each attempt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkretryoptions.html#cfn-kinesisfirehose-deliverystream-splunkretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SplunkRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.TableCreationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class TableCreationConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The configuration to enable automatic table creation.

            Amazon Data Firehose is in preview release and is subject to change.

            :param enabled: Specify whether you want to enable automatic table creation. Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-tablecreationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                table_creation_configuration_property = kinesisfirehose.CfnDeliveryStream.TableCreationConfigurationProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ac9314efc3754736d60b5e8780b56333aa2816ec35cd3e5ede526a3656454369)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specify whether you want to enable automatic table creation.

            Amazon Data Firehose is in preview release and is subject to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-tablecreationconfiguration.html#cfn-kinesisfirehose-deliverystream-tablecreationconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableCreationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.VpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class VpcConfigurationProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_ids: typing.Sequence[builtins.str],
        ) -> None:
            '''The details of the VPC of the Amazon ES destination.

            :param role_arn: The ARN of the IAM role that you want the delivery stream to use to create endpoints in the destination VPC. You can use your existing Kinesis Data Firehose delivery role or you can specify a new role. In either case, make sure that the role trusts the Kinesis Data Firehose service principal and that it grants the following permissions: - ``ec2:DescribeVpcs`` - ``ec2:DescribeVpcAttribute`` - ``ec2:DescribeSubnets`` - ``ec2:DescribeSecurityGroups`` - ``ec2:DescribeNetworkInterfaces`` - ``ec2:CreateNetworkInterface`` - ``ec2:CreateNetworkInterfacePermission`` - ``ec2:DeleteNetworkInterface`` If you revoke these permissions after you create the delivery stream, Kinesis Data Firehose can't scale out by creating more ENIs when necessary. You might therefore see a degradation in performance.
            :param security_group_ids: The IDs of the security groups that you want Kinesis Data Firehose to use when it creates ENIs in the VPC of the Amazon ES destination. You can use the same security group that the Amazon ES domain uses or different ones. If you specify different security groups here, ensure that they allow outbound HTTPS traffic to the Amazon ES domain's security group. Also ensure that the Amazon ES domain's security group allows HTTPS traffic from the security groups specified here. If you use the same security group for both your delivery stream and the Amazon ES domain, make sure the security group inbound rule allows HTTPS traffic.
            :param subnet_ids: The IDs of the subnets that Kinesis Data Firehose uses to create ENIs in the VPC of the Amazon ES destination. Make sure that the routing tables and inbound and outbound rules allow traffic to flow from the subnets whose IDs are specified here to the subnets that have the destination Amazon ES endpoints. Kinesis Data Firehose creates at least one ENI in each of the subnets that are specified here. Do not delete or modify these ENIs. The number of ENIs that Kinesis Data Firehose creates in the subnets specified here scales up and down automatically based on throughput. To enable Kinesis Data Firehose to scale up the number of ENIs to match throughput, ensure that you have sufficient quota. To help you calculate the quota you need, assume that Kinesis Data Firehose can create up to three ENIs for this delivery stream for each of the subnets specified here.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                vpc_configuration_property = kinesisfirehose.CfnDeliveryStream.VpcConfigurationProperty(
                    role_arn="roleArn",
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ecd7f59955db0312a31e14fafedff3746c1d169b6a24f2985f6a096a09db25a)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "security_group_ids": security_group_ids,
                "subnet_ids": subnet_ids,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that you want the delivery stream to use to create endpoints in the destination VPC.

            You can use your existing Kinesis Data Firehose delivery role or you can specify a new role. In either case, make sure that the role trusts the Kinesis Data Firehose service principal and that it grants the following permissions:

            - ``ec2:DescribeVpcs``
            - ``ec2:DescribeVpcAttribute``
            - ``ec2:DescribeSubnets``
            - ``ec2:DescribeSecurityGroups``
            - ``ec2:DescribeNetworkInterfaces``
            - ``ec2:CreateNetworkInterface``
            - ``ec2:CreateNetworkInterfacePermission``
            - ``ec2:DeleteNetworkInterface``

            If you revoke these permissions after you create the delivery stream, Kinesis Data Firehose can't scale out by creating more ENIs when necessary. You might therefore see a degradation in performance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''The IDs of the security groups that you want Kinesis Data Firehose to use when it creates ENIs in the VPC of the Amazon ES destination.

            You can use the same security group that the Amazon ES domain uses or different ones. If you specify different security groups here, ensure that they allow outbound HTTPS traffic to the Amazon ES domain's security group. Also ensure that the Amazon ES domain's security group allows HTTPS traffic from the security groups specified here. If you use the same security group for both your delivery stream and the Amazon ES domain, make sure the security group inbound rule allows HTTPS traffic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''The IDs of the subnets that Kinesis Data Firehose uses to create ENIs in the VPC of the Amazon ES destination.

            Make sure that the routing tables and inbound and outbound rules allow traffic to flow from the subnets whose IDs are specified here to the subnets that have the destination Amazon ES endpoints. Kinesis Data Firehose creates at least one ENI in each of the subnets that are specified here. Do not delete or modify these ENIs.

            The number of ENIs that Kinesis Data Firehose creates in the subnets specified here scales up and down automatically based on throughput. To enable Kinesis Data Firehose to scale up the number of ENIs to match throughput, ensure that you have sufficient quota. To help you calculate the quota you need, assume that Kinesis Data Firehose can create up to three ENIs for this delivery stream for each of the subnets specified here.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "amazon_open_search_serverless_destination_configuration": "amazonOpenSearchServerlessDestinationConfiguration",
        "amazonopensearchservice_destination_configuration": "amazonopensearchserviceDestinationConfiguration",
        "database_source_configuration": "databaseSourceConfiguration",
        "delivery_stream_encryption_configuration_input": "deliveryStreamEncryptionConfigurationInput",
        "delivery_stream_name": "deliveryStreamName",
        "delivery_stream_type": "deliveryStreamType",
        "direct_put_source_configuration": "directPutSourceConfiguration",
        "elasticsearch_destination_configuration": "elasticsearchDestinationConfiguration",
        "extended_s3_destination_configuration": "extendedS3DestinationConfiguration",
        "http_endpoint_destination_configuration": "httpEndpointDestinationConfiguration",
        "iceberg_destination_configuration": "icebergDestinationConfiguration",
        "kinesis_stream_source_configuration": "kinesisStreamSourceConfiguration",
        "msk_source_configuration": "mskSourceConfiguration",
        "redshift_destination_configuration": "redshiftDestinationConfiguration",
        "s3_destination_configuration": "s3DestinationConfiguration",
        "snowflake_destination_configuration": "snowflakeDestinationConfiguration",
        "splunk_destination_configuration": "splunkDestinationConfiguration",
        "tags": "tags",
    },
)
class CfnDeliveryStreamProps:
    def __init__(
        self,
        *,
        amazon_open_search_serverless_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        amazonopensearchservice_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        database_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DatabaseSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        delivery_stream_encryption_configuration_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        delivery_stream_name: typing.Optional[builtins.str] = None,
        delivery_stream_type: typing.Optional[builtins.str] = None,
        direct_put_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DirectPutSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        elasticsearch_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        extended_s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        http_endpoint_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        iceberg_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.IcebergDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kinesis_stream_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.KinesisStreamSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        msk_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.MSKSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        redshift_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.RedshiftDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        snowflake_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SnowflakeDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        splunk_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SplunkDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeliveryStream``.

        :param amazon_open_search_serverless_destination_configuration: Describes the configuration of a destination in the Serverless offering for Amazon OpenSearch Service.
        :param amazonopensearchservice_destination_configuration: The destination in Amazon OpenSearch Service. You can specify only one destination.
        :param database_source_configuration: The top level object for configuring streams with database as a source. Amazon Data Firehose is in preview release and is subject to change.
        :param delivery_stream_encryption_configuration_input: Specifies the type and Amazon Resource Name (ARN) of the CMK to use for Server-Side Encryption (SSE).
        :param delivery_stream_name: The name of the Firehose stream.
        :param delivery_stream_type: The Firehose stream type. This can be one of the following values:. - ``DirectPut`` : Provider applications access the Firehose stream directly. - ``KinesisStreamAsSource`` : The Firehose stream uses a Kinesis data stream as a source.
        :param direct_put_source_configuration: The structure that configures parameters such as ``ThroughputHintInMBs`` for a stream configured with Direct PUT as a source.
        :param elasticsearch_destination_configuration: An Amazon ES destination for the delivery stream. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon ES destination to an Amazon S3 or Amazon Redshift destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param extended_s3_destination_configuration: An Amazon S3 destination for the delivery stream. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon Extended S3 destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param http_endpoint_destination_configuration: Enables configuring Kinesis Firehose to deliver data to any HTTP endpoint destination. You can specify only one destination.
        :param iceberg_destination_configuration: Specifies the destination configure settings for Apache Iceberg Table.
        :param kinesis_stream_source_configuration: When a Kinesis stream is used as the source for the delivery stream, a `KinesisStreamSourceConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html>`_ containing the Kinesis stream ARN and the role ARN for the source stream.
        :param msk_source_configuration: The configuration for the Amazon MSK cluster to be used as the source for a delivery stream.
        :param redshift_destination_configuration: An Amazon Redshift destination for the delivery stream. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon Redshift destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param s3_destination_configuration: The ``S3DestinationConfiguration`` property type specifies an Amazon Simple Storage Service (Amazon S3) destination to which Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivers data. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon S3 destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param snowflake_destination_configuration: Configure Snowflake destination.
        :param splunk_destination_configuration: The configuration of a destination in Splunk for the delivery stream.
        :param tags: A set of tags to assign to the Firehose stream. A tag is a key-value pair that you can define and assign to AWS resources. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the Firehose stream. For more information about tags, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_ in the AWS Billing and Cost Management User Guide. You can specify up to 50 tags when creating a Firehose stream. If you specify tags in the ``CreateDeliveryStream`` action, Amazon Data Firehose performs an additional authorization on the ``firehose:TagDeliveryStream`` action to verify if users have permissions to create tags. If you do not provide this permission, requests to create new Firehose streams with IAM resource tags will fail with an ``AccessDeniedException`` such as following. *AccessDeniedException* User: arn:aws:sts::x:assumed-role/x/x is not authorized to perform: firehose:TagDeliveryStream on resource: arn:aws:firehose:us-east-1:x:deliverystream/x with an explicit deny in an identity-based policy. For an example IAM policy, see `Tag example. <https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html#API_CreateDeliveryStream_Examples>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html
        :exampleMetadata: infused

        Example::

            destination_bucket = s3.Bucket(self, "Bucket")
            delivery_stream_role = iam.Role(self, "Role",
                assumed_by=iam.ServicePrincipal("firehose.amazonaws.com")
            )
            
            stream = firehose.CfnDeliveryStream(self, "MyStream",
                delivery_stream_name="amazon-apigateway-delivery-stream",
                s3_destination_configuration=firehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                    bucket_arn=destination_bucket.bucket_arn,
                    role_arn=delivery_stream_role.role_arn
                )
            )
            
            api = apigateway.RestApi(self, "books",
                deploy_options=apigateway.StageOptions(
                    access_log_destination=apigateway.FirehoseLogDestination(stream),
                    access_log_format=apigateway.AccessLogFormat.json_with_standard_fields()
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f4e310bf0ff2c76f9c126ea4431fb25b9b53c8ba7e0c0eacc1c934debd05a95)
            check_type(argname="argument amazon_open_search_serverless_destination_configuration", value=amazon_open_search_serverless_destination_configuration, expected_type=type_hints["amazon_open_search_serverless_destination_configuration"])
            check_type(argname="argument amazonopensearchservice_destination_configuration", value=amazonopensearchservice_destination_configuration, expected_type=type_hints["amazonopensearchservice_destination_configuration"])
            check_type(argname="argument database_source_configuration", value=database_source_configuration, expected_type=type_hints["database_source_configuration"])
            check_type(argname="argument delivery_stream_encryption_configuration_input", value=delivery_stream_encryption_configuration_input, expected_type=type_hints["delivery_stream_encryption_configuration_input"])
            check_type(argname="argument delivery_stream_name", value=delivery_stream_name, expected_type=type_hints["delivery_stream_name"])
            check_type(argname="argument delivery_stream_type", value=delivery_stream_type, expected_type=type_hints["delivery_stream_type"])
            check_type(argname="argument direct_put_source_configuration", value=direct_put_source_configuration, expected_type=type_hints["direct_put_source_configuration"])
            check_type(argname="argument elasticsearch_destination_configuration", value=elasticsearch_destination_configuration, expected_type=type_hints["elasticsearch_destination_configuration"])
            check_type(argname="argument extended_s3_destination_configuration", value=extended_s3_destination_configuration, expected_type=type_hints["extended_s3_destination_configuration"])
            check_type(argname="argument http_endpoint_destination_configuration", value=http_endpoint_destination_configuration, expected_type=type_hints["http_endpoint_destination_configuration"])
            check_type(argname="argument iceberg_destination_configuration", value=iceberg_destination_configuration, expected_type=type_hints["iceberg_destination_configuration"])
            check_type(argname="argument kinesis_stream_source_configuration", value=kinesis_stream_source_configuration, expected_type=type_hints["kinesis_stream_source_configuration"])
            check_type(argname="argument msk_source_configuration", value=msk_source_configuration, expected_type=type_hints["msk_source_configuration"])
            check_type(argname="argument redshift_destination_configuration", value=redshift_destination_configuration, expected_type=type_hints["redshift_destination_configuration"])
            check_type(argname="argument s3_destination_configuration", value=s3_destination_configuration, expected_type=type_hints["s3_destination_configuration"])
            check_type(argname="argument snowflake_destination_configuration", value=snowflake_destination_configuration, expected_type=type_hints["snowflake_destination_configuration"])
            check_type(argname="argument splunk_destination_configuration", value=splunk_destination_configuration, expected_type=type_hints["splunk_destination_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if amazon_open_search_serverless_destination_configuration is not None:
            self._values["amazon_open_search_serverless_destination_configuration"] = amazon_open_search_serverless_destination_configuration
        if amazonopensearchservice_destination_configuration is not None:
            self._values["amazonopensearchservice_destination_configuration"] = amazonopensearchservice_destination_configuration
        if database_source_configuration is not None:
            self._values["database_source_configuration"] = database_source_configuration
        if delivery_stream_encryption_configuration_input is not None:
            self._values["delivery_stream_encryption_configuration_input"] = delivery_stream_encryption_configuration_input
        if delivery_stream_name is not None:
            self._values["delivery_stream_name"] = delivery_stream_name
        if delivery_stream_type is not None:
            self._values["delivery_stream_type"] = delivery_stream_type
        if direct_put_source_configuration is not None:
            self._values["direct_put_source_configuration"] = direct_put_source_configuration
        if elasticsearch_destination_configuration is not None:
            self._values["elasticsearch_destination_configuration"] = elasticsearch_destination_configuration
        if extended_s3_destination_configuration is not None:
            self._values["extended_s3_destination_configuration"] = extended_s3_destination_configuration
        if http_endpoint_destination_configuration is not None:
            self._values["http_endpoint_destination_configuration"] = http_endpoint_destination_configuration
        if iceberg_destination_configuration is not None:
            self._values["iceberg_destination_configuration"] = iceberg_destination_configuration
        if kinesis_stream_source_configuration is not None:
            self._values["kinesis_stream_source_configuration"] = kinesis_stream_source_configuration
        if msk_source_configuration is not None:
            self._values["msk_source_configuration"] = msk_source_configuration
        if redshift_destination_configuration is not None:
            self._values["redshift_destination_configuration"] = redshift_destination_configuration
        if s3_destination_configuration is not None:
            self._values["s3_destination_configuration"] = s3_destination_configuration
        if snowflake_destination_configuration is not None:
            self._values["snowflake_destination_configuration"] = snowflake_destination_configuration
        if splunk_destination_configuration is not None:
            self._values["splunk_destination_configuration"] = splunk_destination_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def amazon_open_search_serverless_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty]]:
        '''Describes the configuration of a destination in the Serverless offering for Amazon OpenSearch Service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration
        '''
        result = self._values.get("amazon_open_search_serverless_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty]], result)

    @builtins.property
    def amazonopensearchservice_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty]]:
        '''The destination in Amazon OpenSearch Service.

        You can specify only one destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration
        '''
        result = self._values.get("amazonopensearchservice_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty]], result)

    @builtins.property
    def database_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.DatabaseSourceConfigurationProperty]]:
        '''The top level object for configuring streams with database as a source.

        Amazon Data Firehose is in preview release and is subject to change.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-databasesourceconfiguration
        '''
        result = self._values.get("database_source_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.DatabaseSourceConfigurationProperty]], result)

    @builtins.property
    def delivery_stream_encryption_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty]]:
        '''Specifies the type and Amazon Resource Name (ARN) of the CMK to use for Server-Side Encryption (SSE).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput
        '''
        result = self._values.get("delivery_stream_encryption_configuration_input")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty]], result)

    @builtins.property
    def delivery_stream_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Firehose stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamname
        '''
        result = self._values.get("delivery_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delivery_stream_type(self) -> typing.Optional[builtins.str]:
        '''The Firehose stream type. This can be one of the following values:.

        - ``DirectPut`` : Provider applications access the Firehose stream directly.
        - ``KinesisStreamAsSource`` : The Firehose stream uses a Kinesis data stream as a source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamtype
        '''
        result = self._values.get("delivery_stream_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def direct_put_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.DirectPutSourceConfigurationProperty]]:
        '''The structure that configures parameters such as ``ThroughputHintInMBs`` for a stream configured with Direct PUT as a source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-directputsourceconfiguration
        '''
        result = self._values.get("direct_put_source_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.DirectPutSourceConfigurationProperty]], result)

    @builtins.property
    def elasticsearch_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty]]:
        '''An Amazon ES destination for the delivery stream.

        Conditional. You must specify only one destination configuration.

        If you change the delivery stream destination from an Amazon ES destination to an Amazon S3 or Amazon Redshift destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration
        '''
        result = self._values.get("elasticsearch_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty]], result)

    @builtins.property
    def extended_s3_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty]]:
        '''An Amazon S3 destination for the delivery stream.

        Conditional. You must specify only one destination configuration.

        If you change the delivery stream destination from an Amazon Extended S3 destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration
        '''
        result = self._values.get("extended_s3_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty]], result)

    @builtins.property
    def http_endpoint_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty]]:
        '''Enables configuring Kinesis Firehose to deliver data to any HTTP endpoint destination.

        You can specify only one destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration
        '''
        result = self._values.get("http_endpoint_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty]], result)

    @builtins.property
    def iceberg_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.IcebergDestinationConfigurationProperty]]:
        '''Specifies the destination configure settings for Apache Iceberg Table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-icebergdestinationconfiguration
        '''
        result = self._values.get("iceberg_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.IcebergDestinationConfigurationProperty]], result)

    @builtins.property
    def kinesis_stream_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.KinesisStreamSourceConfigurationProperty]]:
        '''When a Kinesis stream is used as the source for the delivery stream, a `KinesisStreamSourceConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html>`_ containing the Kinesis stream ARN and the role ARN for the source stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration
        '''
        result = self._values.get("kinesis_stream_source_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.KinesisStreamSourceConfigurationProperty]], result)

    @builtins.property
    def msk_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.MSKSourceConfigurationProperty]]:
        '''The configuration for the Amazon MSK cluster to be used as the source for a delivery stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-msksourceconfiguration
        '''
        result = self._values.get("msk_source_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.MSKSourceConfigurationProperty]], result)

    @builtins.property
    def redshift_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.RedshiftDestinationConfigurationProperty]]:
        '''An Amazon Redshift destination for the delivery stream.

        Conditional. You must specify only one destination configuration.

        If you change the delivery stream destination from an Amazon Redshift destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration
        '''
        result = self._values.get("redshift_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.RedshiftDestinationConfigurationProperty]], result)

    @builtins.property
    def s3_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.S3DestinationConfigurationProperty]]:
        '''The ``S3DestinationConfiguration`` property type specifies an Amazon Simple Storage Service (Amazon S3) destination to which Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivers data.

        Conditional. You must specify only one destination configuration.

        If you change the delivery stream destination from an Amazon S3 destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration
        '''
        result = self._values.get("s3_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.S3DestinationConfigurationProperty]], result)

    @builtins.property
    def snowflake_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.SnowflakeDestinationConfigurationProperty]]:
        '''Configure Snowflake destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration
        '''
        result = self._values.get("snowflake_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.SnowflakeDestinationConfigurationProperty]], result)

    @builtins.property
    def splunk_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.SplunkDestinationConfigurationProperty]]:
        '''The configuration of a destination in Splunk for the delivery stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration
        '''
        result = self._values.get("splunk_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.SplunkDestinationConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A set of tags to assign to the Firehose stream.

        A tag is a key-value pair that you can define and assign to AWS resources. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the Firehose stream. For more information about tags, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_ in the AWS Billing and Cost Management User Guide.

        You can specify up to 50 tags when creating a Firehose stream.

        If you specify tags in the ``CreateDeliveryStream`` action, Amazon Data Firehose performs an additional authorization on the ``firehose:TagDeliveryStream`` action to verify if users have permissions to create tags. If you do not provide this permission, requests to create new Firehose streams with IAM resource tags will fail with an ``AccessDeniedException`` such as following.

        *AccessDeniedException*

        User: arn:aws:sts::x:assumed-role/x/x is not authorized to perform: firehose:TagDeliveryStream on resource: arn:aws:firehose:us-east-1:x:deliverystream/x with an explicit deny in an identity-based policy.

        For an example IAM policy, see `Tag example. <https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html#API_CreateDeliveryStream_Examples>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeliveryStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.CommonDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "logging_config": "loggingConfig",
        "processor": "processor",
        "role": "role",
        "s3_backup": "s3Backup",
    },
)
class CommonDestinationProps:
    def __init__(
        self,
        *,
        logging_config: typing.Optional["ILoggingConfig"] = None,
        processor: typing.Optional["IDataProcessor"] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        s3_backup: typing.Optional[typing.Union["DestinationS3BackupProps", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Generic properties for defining a delivery stream destination.

        :param logging_config: Configuration that determines whether to log errors during data transformation or delivery failures, and specifies the CloudWatch log group for storing error logs. Default: - errors will be logged and a log group will be created for you.
        :param processor: The data transformation that should be performed on the data before writing to the destination. Default: - no data transformation will occur.
        :param role: The IAM role associated with this destination. Assumed by Amazon Data Firehose to invoke processors and write to destinations Default: - a role will be created with default permissions.
        :param s3_backup: The configuration for backing up source records to S3. Default: - source records will not be backed up to S3.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_kinesisfirehose as kinesisfirehose
            from aws_cdk import aws_kms as kms
            from aws_cdk import aws_s3 as s3
            
            # bucket: s3.Bucket
            # compression: kinesisfirehose.Compression
            # data_processor: kinesisfirehose.IDataProcessor
            # key: kms.Key
            # logging_config: kinesisfirehose.ILoggingConfig
            # role: iam.Role
            # size: cdk.Size
            
            common_destination_props = kinesisfirehose.CommonDestinationProps(
                logging_config=logging_config,
                processor=data_processor,
                role=role,
                s3_backup=kinesisfirehose.DestinationS3BackupProps(
                    bucket=bucket,
                    buffering_interval=cdk.Duration.minutes(30),
                    buffering_size=size,
                    compression=compression,
                    data_output_prefix="dataOutputPrefix",
                    encryption_key=key,
                    error_output_prefix="errorOutputPrefix",
                    logging_config=logging_config,
                    mode=kinesisfirehose.BackupMode.ALL
                )
            )
        '''
        if isinstance(s3_backup, dict):
            s3_backup = DestinationS3BackupProps(**s3_backup)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c67ac54054be7496dcf923fd4756691ef492acee6f8731020e20179b0e257c8)
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument s3_backup", value=s3_backup, expected_type=type_hints["s3_backup"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if processor is not None:
            self._values["processor"] = processor
        if role is not None:
            self._values["role"] = role
        if s3_backup is not None:
            self._values["s3_backup"] = s3_backup

    @builtins.property
    def logging_config(self) -> typing.Optional["ILoggingConfig"]:
        '''Configuration that determines whether to log errors during data transformation or delivery failures, and specifies the CloudWatch log group for storing error logs.

        :default: - errors will be logged and a log group will be created for you.
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["ILoggingConfig"], result)

    @builtins.property
    def processor(self) -> typing.Optional["IDataProcessor"]:
        '''The data transformation that should be performed on the data before writing to the destination.

        :default: - no data transformation will occur.
        '''
        result = self._values.get("processor")
        return typing.cast(typing.Optional["IDataProcessor"], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role associated with this destination.

        Assumed by Amazon Data Firehose to invoke processors and write to destinations

        :default: - a role will be created with default permissions.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def s3_backup(self) -> typing.Optional["DestinationS3BackupProps"]:
        '''The configuration for backing up source records to S3.

        :default: - source records will not be backed up to S3.
        '''
        result = self._values.get("s3_backup")
        return typing.cast(typing.Optional["DestinationS3BackupProps"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.CommonDestinationS3Props",
    jsii_struct_bases=[],
    name_mapping={
        "buffering_interval": "bufferingInterval",
        "buffering_size": "bufferingSize",
        "compression": "compression",
        "data_output_prefix": "dataOutputPrefix",
        "encryption_key": "encryptionKey",
        "error_output_prefix": "errorOutputPrefix",
    },
)
class CommonDestinationS3Props:
    def __init__(
        self,
        *,
        buffering_interval: typing.Optional[_Duration_4839e8c3] = None,
        buffering_size: typing.Optional[_Size_7b441c34] = None,
        compression: typing.Optional["Compression"] = None,
        data_output_prefix: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Common properties for defining a backup, intermediary, or final S3 destination for a Amazon Data Firehose delivery stream.

        :param buffering_interval: The length of time that Firehose buffers incoming data before delivering it to the S3 bucket. Minimum: Duration.seconds(0) Maximum: Duration.seconds(900) Default: Duration.seconds(300)
        :param buffering_size: The size of the buffer that Amazon Data Firehose uses for incoming data before delivering it to the S3 bucket. Minimum: Size.mebibytes(1) Maximum: Size.mebibytes(128) Default: Size.mebibytes(5)
        :param compression: The type of compression that Amazon Data Firehose uses to compress the data that it delivers to the Amazon S3 bucket. The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket. Default: - UNCOMPRESSED
        :param data_output_prefix: A prefix that Amazon Data Firehose evaluates and adds to records before writing them to S3. This prefix appears immediately following the bucket name. Default: "YYYY/MM/DD/HH"
        :param encryption_key: The AWS KMS key used to encrypt the data that it delivers to your Amazon S3 bucket. Default: - Data is not encrypted.
        :param error_output_prefix: A prefix that Amazon Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. Default: "YYYY/MM/DD/HH"

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_kinesisfirehose as kinesisfirehose
            from aws_cdk import aws_kms as kms
            
            # compression: kinesisfirehose.Compression
            # key: kms.Key
            # size: cdk.Size
            
            common_destination_s3_props = kinesisfirehose.CommonDestinationS3Props(
                buffering_interval=cdk.Duration.minutes(30),
                buffering_size=size,
                compression=compression,
                data_output_prefix="dataOutputPrefix",
                encryption_key=key,
                error_output_prefix="errorOutputPrefix"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e31b00e38ca06327867ea44e0a0f3d63eb65aaa770f96419cf713c515c231922)
            check_type(argname="argument buffering_interval", value=buffering_interval, expected_type=type_hints["buffering_interval"])
            check_type(argname="argument buffering_size", value=buffering_size, expected_type=type_hints["buffering_size"])
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument data_output_prefix", value=data_output_prefix, expected_type=type_hints["data_output_prefix"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument error_output_prefix", value=error_output_prefix, expected_type=type_hints["error_output_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if buffering_interval is not None:
            self._values["buffering_interval"] = buffering_interval
        if buffering_size is not None:
            self._values["buffering_size"] = buffering_size
        if compression is not None:
            self._values["compression"] = compression
        if data_output_prefix is not None:
            self._values["data_output_prefix"] = data_output_prefix
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if error_output_prefix is not None:
            self._values["error_output_prefix"] = error_output_prefix

    @builtins.property
    def buffering_interval(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The length of time that Firehose buffers incoming data before delivering it to the S3 bucket.

        Minimum: Duration.seconds(0)
        Maximum: Duration.seconds(900)

        :default: Duration.seconds(300)
        '''
        result = self._values.get("buffering_interval")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def buffering_size(self) -> typing.Optional[_Size_7b441c34]:
        '''The size of the buffer that Amazon Data Firehose uses for incoming data before delivering it to the S3 bucket.

        Minimum: Size.mebibytes(1)
        Maximum: Size.mebibytes(128)

        :default: Size.mebibytes(5)
        '''
        result = self._values.get("buffering_size")
        return typing.cast(typing.Optional[_Size_7b441c34], result)

    @builtins.property
    def compression(self) -> typing.Optional["Compression"]:
        '''The type of compression that Amazon Data Firehose uses to compress the data that it delivers to the Amazon S3 bucket.

        The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift
        destinations because they are not supported by the Amazon Redshift COPY operation
        that reads from the S3 bucket.

        :default: - UNCOMPRESSED
        '''
        result = self._values.get("compression")
        return typing.cast(typing.Optional["Compression"], result)

    @builtins.property
    def data_output_prefix(self) -> typing.Optional[builtins.str]:
        '''A prefix that Amazon Data Firehose evaluates and adds to records before writing them to S3.

        This prefix appears immediately following the bucket name.

        :default: "YYYY/MM/DD/HH"

        :see: https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html
        '''
        result = self._values.get("data_output_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The AWS KMS key used to encrypt the data that it delivers to your Amazon S3 bucket.

        :default: - Data is not encrypted.
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def error_output_prefix(self) -> typing.Optional[builtins.str]:
        '''A prefix that Amazon Data Firehose evaluates and adds to failed records before writing them to S3.

        This prefix appears immediately following the bucket name.

        :default: "YYYY/MM/DD/HH"

        :see: https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html
        '''
        result = self._values.get("error_output_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonDestinationS3Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Compression(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.Compression",
):
    '''Possible compression options Amazon Data Firehose can use to compress data on delivery.

    :exampleMetadata: infused

    Example::

        # Compress data delivered to S3 using Snappy
        # bucket: s3.Bucket
        
        s3_destination = firehose.S3Bucket(bucket,
            compression=firehose.Compression.SNAPPY
        )
        firehose.DeliveryStream(self, "Delivery Stream",
            destination=s3_destination
        )
    '''

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, value: builtins.str) -> "Compression":
        '''Creates a new Compression instance with a custom value.

        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e41ad5beb7c57e7d6a51a6e7b54af84f87429433140b71bcff2768d479fc24c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("Compression", jsii.sinvoke(cls, "of", [value]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GZIP")
    def GZIP(cls) -> "Compression":
        '''gzip.'''
        return typing.cast("Compression", jsii.sget(cls, "GZIP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="HADOOP_SNAPPY")
    def HADOOP_SNAPPY(cls) -> "Compression":
        '''Hadoop-compatible Snappy.'''
        return typing.cast("Compression", jsii.sget(cls, "HADOOP_SNAPPY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SNAPPY")
    def SNAPPY(cls) -> "Compression":
        '''Snappy.'''
        return typing.cast("Compression", jsii.sget(cls, "SNAPPY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="UNCOMPRESSED")
    def UNCOMPRESSED(cls) -> "Compression":
        '''Uncompressed.'''
        return typing.cast("Compression", jsii.sget(cls, "UNCOMPRESSED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ZIP")
    def ZIP(cls) -> "Compression":
        '''ZIP.'''
        return typing.cast("Compression", jsii.sget(cls, "ZIP"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        '''the string value of the Compression.'''
        return typing.cast(builtins.str, jsii.get(self, "value"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.DataProcessorBindOptions",
    jsii_struct_bases=[],
    name_mapping={"role": "role"},
)
class DataProcessorBindOptions:
    def __init__(self, *, role: _IRole_235f5d8e) -> None:
        '''Options when binding a DataProcessor to a delivery stream destination.

        :param role: The IAM role assumed by Amazon Data Firehose to write to the destination that this DataProcessor will bind to.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_kinesisfirehose as kinesisfirehose
            
            # role: iam.Role
            
            data_processor_bind_options = kinesisfirehose.DataProcessorBindOptions(
                role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19eda2faa3921fd664688bb9d58a7766cede4c60f2944654651ac8a298dad52e)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role": role,
        }

    @builtins.property
    def role(self) -> _IRole_235f5d8e:
        '''The IAM role assumed by Amazon Data Firehose to write to the destination that this DataProcessor will bind to.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(_IRole_235f5d8e, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataProcessorBindOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.DataProcessorConfig",
    jsii_struct_bases=[],
    name_mapping={
        "processor_identifier": "processorIdentifier",
        "processor_type": "processorType",
    },
)
class DataProcessorConfig:
    def __init__(
        self,
        *,
        processor_identifier: typing.Union["DataProcessorIdentifier", typing.Dict[builtins.str, typing.Any]],
        processor_type: builtins.str,
    ) -> None:
        '''The full configuration of a data processor.

        :param processor_identifier: The key-value pair that identifies the underlying processor resource.
        :param processor_type: The type of the underlying processor resource. Must be an accepted value in ``CfnDeliveryStream.ProcessorProperty.Type``.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kinesisfirehose as kinesisfirehose
            
            data_processor_config = kinesisfirehose.DataProcessorConfig(
                processor_identifier=kinesisfirehose.DataProcessorIdentifier(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                ),
                processor_type="processorType"
            )
        '''
        if isinstance(processor_identifier, dict):
            processor_identifier = DataProcessorIdentifier(**processor_identifier)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d0329dec95ad7ff26b8989814c21e55edb2fa91a61a992ced2d01569d06f530)
            check_type(argname="argument processor_identifier", value=processor_identifier, expected_type=type_hints["processor_identifier"])
            check_type(argname="argument processor_type", value=processor_type, expected_type=type_hints["processor_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "processor_identifier": processor_identifier,
            "processor_type": processor_type,
        }

    @builtins.property
    def processor_identifier(self) -> "DataProcessorIdentifier":
        '''The key-value pair that identifies the underlying processor resource.'''
        result = self._values.get("processor_identifier")
        assert result is not None, "Required property 'processor_identifier' is missing"
        return typing.cast("DataProcessorIdentifier", result)

    @builtins.property
    def processor_type(self) -> builtins.str:
        '''The type of the underlying processor resource.

        Must be an accepted value in ``CfnDeliveryStream.ProcessorProperty.Type``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html#cfn-kinesisfirehose-deliverystream-processor-type

        Example::

            "Lambda"
        '''
        result = self._values.get("processor_type")
        assert result is not None, "Required property 'processor_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataProcessorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.DataProcessorIdentifier",
    jsii_struct_bases=[],
    name_mapping={
        "parameter_name": "parameterName",
        "parameter_value": "parameterValue",
    },
)
class DataProcessorIdentifier:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        parameter_value: builtins.str,
    ) -> None:
        '''The key-value pair that identifies the underlying processor resource.

        :param parameter_name: The parameter name that corresponds to the processor resource's identifier. Must be an accepted value in ``CfnDeliveryStream.ProcessoryParameterProperty.ParameterName``.
        :param parameter_value: The identifier of the underlying processor resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kinesisfirehose as kinesisfirehose
            
            data_processor_identifier = kinesisfirehose.DataProcessorIdentifier(
                parameter_name="parameterName",
                parameter_value="parameterValue"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46d7f3bad270e22195a118b290c387efb2ff5c34792622c7ab288bdc3709ce43)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameter_name": parameter_name,
            "parameter_value": parameter_value,
        }

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''The parameter name that corresponds to the processor resource's identifier.

        Must be an accepted value in ``CfnDeliveryStream.ProcessoryParameterProperty.ParameterName``.
        '''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_value(self) -> builtins.str:
        '''The identifier of the underlying processor resource.'''
        result = self._values.get("parameter_value")
        assert result is not None, "Required property 'parameter_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataProcessorIdentifier(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.DataProcessorProps",
    jsii_struct_bases=[],
    name_mapping={
        "buffer_interval": "bufferInterval",
        "buffer_size": "bufferSize",
        "retries": "retries",
    },
)
class DataProcessorProps:
    def __init__(
        self,
        *,
        buffer_interval: typing.Optional[_Duration_4839e8c3] = None,
        buffer_size: typing.Optional[_Size_7b441c34] = None,
        retries: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Configure the data processor.

        :param buffer_interval: The length of time Amazon Data Firehose will buffer incoming data before calling the processor. s Default: Duration.minutes(1)
        :param buffer_size: The amount of incoming data Amazon Data Firehose will buffer before calling the processor. Default: Size.mebibytes(3)
        :param retries: The number of times Amazon Data Firehose will retry the processor invocation after a failure due to network timeout or invocation limits. Default: 3

        :exampleMetadata: infused

        Example::

            # bucket: s3.Bucket
            # Provide a Lambda function that will transform records before delivery, with custom
            # buffering and retry configuration
            lambda_function = lambda_.Function(self, "Processor",
                runtime=lambda_.Runtime.NODEJS_LATEST,
                handler="index.handler",
                code=lambda_.Code.from_asset(path.join(__dirname, "process-records"))
            )
            lambda_processor = firehose.LambdaFunctionProcessor(lambda_function,
                buffer_interval=Duration.minutes(5),
                buffer_size=Size.mebibytes(5),
                retries=5
            )
            s3_destination = firehose.S3Bucket(bucket,
                processor=lambda_processor
            )
            firehose.DeliveryStream(self, "Delivery Stream",
                destination=s3_destination
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__824567e49e82c5e0ed6a55fe92d29f1a69f55d0bfe50df023c1b00b9faeb44b3)
            check_type(argname="argument buffer_interval", value=buffer_interval, expected_type=type_hints["buffer_interval"])
            check_type(argname="argument buffer_size", value=buffer_size, expected_type=type_hints["buffer_size"])
            check_type(argname="argument retries", value=retries, expected_type=type_hints["retries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if buffer_interval is not None:
            self._values["buffer_interval"] = buffer_interval
        if buffer_size is not None:
            self._values["buffer_size"] = buffer_size
        if retries is not None:
            self._values["retries"] = retries

    @builtins.property
    def buffer_interval(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The length of time Amazon Data Firehose will buffer incoming data before calling the processor.

        s

        :default: Duration.minutes(1)
        '''
        result = self._values.get("buffer_interval")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def buffer_size(self) -> typing.Optional[_Size_7b441c34]:
        '''The amount of incoming data Amazon Data Firehose will buffer before calling the processor.

        :default: Size.mebibytes(3)
        '''
        result = self._values.get("buffer_size")
        return typing.cast(typing.Optional[_Size_7b441c34], result)

    @builtins.property
    def retries(self) -> typing.Optional[jsii.Number]:
        '''The number of times Amazon Data Firehose will retry the processor invocation after a failure due to network timeout or invocation limits.

        :default: 3
        '''
        result = self._values.get("retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataProcessorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.DeliveryStreamAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "delivery_stream_arn": "deliveryStreamArn",
        "delivery_stream_name": "deliveryStreamName",
        "role": "role",
    },
)
class DeliveryStreamAttributes:
    def __init__(
        self,
        *,
        delivery_stream_arn: typing.Optional[builtins.str] = None,
        delivery_stream_name: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''A full specification of a delivery stream that can be used to import it fluently into the CDK application.

        :param delivery_stream_arn: The ARN of the delivery stream. At least one of deliveryStreamArn and deliveryStreamName must be provided. Default: - derived from ``deliveryStreamName``.
        :param delivery_stream_name: The name of the delivery stream. At least one of deliveryStreamName and deliveryStreamArn must be provided. Default: - derived from ``deliveryStreamArn``.
        :param role: The IAM role associated with this delivery stream. Assumed by Amazon Data Firehose to read from sources and encrypt data server-side. Default: - the imported stream cannot be granted access to other resources as an ``iam.IGrantable``.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_kinesisfirehose as kinesisfirehose
            
            # role: iam.Role
            
            delivery_stream_attributes = kinesisfirehose.DeliveryStreamAttributes(
                delivery_stream_arn="deliveryStreamArn",
                delivery_stream_name="deliveryStreamName",
                role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__045ad458e5c2129dfab9cbc14581304a5f9f38f34ef8d143791a7e6ee60d651e)
            check_type(argname="argument delivery_stream_arn", value=delivery_stream_arn, expected_type=type_hints["delivery_stream_arn"])
            check_type(argname="argument delivery_stream_name", value=delivery_stream_name, expected_type=type_hints["delivery_stream_name"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if delivery_stream_arn is not None:
            self._values["delivery_stream_arn"] = delivery_stream_arn
        if delivery_stream_name is not None:
            self._values["delivery_stream_name"] = delivery_stream_name
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def delivery_stream_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the delivery stream.

        At least one of deliveryStreamArn and deliveryStreamName must be provided.

        :default: - derived from ``deliveryStreamName``.
        '''
        result = self._values.get("delivery_stream_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delivery_stream_name(self) -> typing.Optional[builtins.str]:
        '''The name of the delivery stream.

        At least one of deliveryStreamName and deliveryStreamArn  must be provided.

        :default: - derived from ``deliveryStreamArn``.
        '''
        result = self._values.get("delivery_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role associated with this delivery stream.

        Assumed by Amazon Data Firehose to read from sources and encrypt data server-side.

        :default: - the imported stream cannot be granted access to other resources as an ``iam.IGrantable``.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeliveryStreamAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.DeliveryStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "delivery_stream_name": "deliveryStreamName",
        "encryption": "encryption",
        "role": "role",
        "source": "source",
    },
)
class DeliveryStreamProps:
    def __init__(
        self,
        *,
        destination: "IDestination",
        delivery_stream_name: typing.Optional[builtins.str] = None,
        encryption: typing.Optional["StreamEncryption"] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        source: typing.Optional["ISource"] = None,
    ) -> None:
        '''Properties for a new delivery stream.

        :param destination: The destination that this delivery stream will deliver data to.
        :param delivery_stream_name: A name for the delivery stream. Default: - a name is generated by CloudFormation.
        :param encryption: Indicates the type of customer master key (CMK) to use for server-side encryption, if any. Default: StreamEncryption.unencrypted()
        :param role: The IAM role associated with this delivery stream. Assumed by Amazon Data Firehose to read from sources and encrypt data server-side. Default: - a role will be created with default permissions.
        :param source: The Kinesis data stream to use as a source for this delivery stream. Default: - data must be written to the delivery stream via a direct put.

        :exampleMetadata: infused

        Example::

            # bucket: s3.Bucket
            # Provide a Lambda function that will transform records before delivery, with custom
            # buffering and retry configuration
            lambda_function = lambda_.Function(self, "Processor",
                runtime=lambda_.Runtime.NODEJS_LATEST,
                handler="index.handler",
                code=lambda_.Code.from_asset(path.join(__dirname, "process-records"))
            )
            lambda_processor = firehose.LambdaFunctionProcessor(lambda_function,
                buffer_interval=Duration.minutes(5),
                buffer_size=Size.mebibytes(5),
                retries=5
            )
            s3_destination = firehose.S3Bucket(bucket,
                processor=lambda_processor
            )
            firehose.DeliveryStream(self, "Delivery Stream",
                destination=s3_destination
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acb39dfe9c8b47016ad51340ebf8bd9df44f24a25df01acaec0605788a0a5b85)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument delivery_stream_name", value=delivery_stream_name, expected_type=type_hints["delivery_stream_name"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }
        if delivery_stream_name is not None:
            self._values["delivery_stream_name"] = delivery_stream_name
        if encryption is not None:
            self._values["encryption"] = encryption
        if role is not None:
            self._values["role"] = role
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def destination(self) -> "IDestination":
        '''The destination that this delivery stream will deliver data to.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast("IDestination", result)

    @builtins.property
    def delivery_stream_name(self) -> typing.Optional[builtins.str]:
        '''A name for the delivery stream.

        :default: - a name is generated by CloudFormation.
        '''
        result = self._values.get("delivery_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption(self) -> typing.Optional["StreamEncryption"]:
        '''Indicates the type of customer master key (CMK) to use for server-side encryption, if any.

        :default: StreamEncryption.unencrypted()
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional["StreamEncryption"], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role associated with this delivery stream.

        Assumed by Amazon Data Firehose to read from sources and encrypt data server-side.

        :default: - a role will be created with default permissions.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def source(self) -> typing.Optional["ISource"]:
        '''The Kinesis data stream to use as a source for this delivery stream.

        :default: - data must be written to the delivery stream via a direct put.
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional["ISource"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeliveryStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.DestinationBindOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class DestinationBindOptions:
    def __init__(self) -> None:
        '''Options when binding a destination to a delivery stream.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kinesisfirehose as kinesisfirehose
            
            destination_bind_options = kinesisfirehose.DestinationBindOptions()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationBindOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.DestinationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "dependables": "dependables",
        "extended_s3_destination_configuration": "extendedS3DestinationConfiguration",
    },
)
class DestinationConfig:
    def __init__(
        self,
        *,
        dependables: typing.Optional[typing.Sequence[_constructs_77d1e7e8.IDependable]] = None,
        extended_s3_destination_configuration: typing.Optional[typing.Union[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''An Amazon Data Firehose delivery stream destination configuration.

        :param dependables: Any resources that were created by the destination when binding it to the stack that must be deployed before the delivery stream is deployed. Default: []
        :param extended_s3_destination_configuration: S3 destination configuration properties. Default: - S3 destination is not used.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kinesisfirehose as kinesisfirehose
            import constructs as constructs
            
            # dependable: constructs.IDependable
            
            destination_config = kinesisfirehose.DestinationConfig(
                dependables=[dependable],
                extended_s3_destination_configuration=kinesisfirehose.CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty(
                    bucket_arn="bucketArn",
                    role_arn="roleArn",
            
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    compression_format="compressionFormat",
                    custom_time_zone="customTimeZone",
                    data_format_conversion_configuration=kinesisfirehose.CfnDeliveryStream.DataFormatConversionConfigurationProperty(
                        enabled=False,
                        input_format_configuration=kinesisfirehose.CfnDeliveryStream.InputFormatConfigurationProperty(
                            deserializer=kinesisfirehose.CfnDeliveryStream.DeserializerProperty(
                                hive_json_ser_de=kinesisfirehose.CfnDeliveryStream.HiveJsonSerDeProperty(
                                    timestamp_formats=["timestampFormats"]
                                ),
                                open_xJson_ser_de=kinesisfirehose.CfnDeliveryStream.OpenXJsonSerDeProperty(
                                    case_insensitive=False,
                                    column_to_json_key_mappings={
                                        "column_to_json_key_mappings_key": "columnToJsonKeyMappings"
                                    },
                                    convert_dots_in_json_keys_to_underscores=False
                                )
                            )
                        ),
                        output_format_configuration=kinesisfirehose.CfnDeliveryStream.OutputFormatConfigurationProperty(
                            serializer=kinesisfirehose.CfnDeliveryStream.SerializerProperty(
                                orc_ser_de=kinesisfirehose.CfnDeliveryStream.OrcSerDeProperty(
                                    block_size_bytes=123,
                                    bloom_filter_columns=["bloomFilterColumns"],
                                    bloom_filter_false_positive_probability=123,
                                    compression="compression",
                                    dictionary_key_threshold=123,
                                    enable_padding=False,
                                    format_version="formatVersion",
                                    padding_tolerance=123,
                                    row_index_stride=123,
                                    stripe_size_bytes=123
                                ),
                                parquet_ser_de=kinesisfirehose.CfnDeliveryStream.ParquetSerDeProperty(
                                    block_size_bytes=123,
                                    compression="compression",
                                    enable_dictionary_compression=False,
                                    max_padding_bytes=123,
                                    page_size_bytes=123,
                                    writer_version="writerVersion"
                                )
                            )
                        ),
                        schema_configuration=kinesisfirehose.CfnDeliveryStream.SchemaConfigurationProperty(
                            catalog_id="catalogId",
                            database_name="databaseName",
                            region="region",
                            role_arn="roleArn",
                            table_name="tableName",
                            version_id="versionId"
                        )
                    ),
                    dynamic_partitioning_configuration=kinesisfirehose.CfnDeliveryStream.DynamicPartitioningConfigurationProperty(
                        enabled=False,
                        retry_options=kinesisfirehose.CfnDeliveryStream.RetryOptionsProperty(
                            duration_in_seconds=123
                        )
                    ),
                    encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                        kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                            awskms_key_arn="awskmsKeyArn"
                        ),
                        no_encryption_config="noEncryptionConfig"
                    ),
                    error_output_prefix="errorOutputPrefix",
                    file_extension="fileExtension",
                    prefix="prefix",
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
            
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    s3_backup_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
            
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                    s3_backup_mode="s3BackupMode"
                )
            )
        '''
        if isinstance(extended_s3_destination_configuration, dict):
            extended_s3_destination_configuration = CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty(**extended_s3_destination_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4dd310df912fa42818751c79c7d5fea4583bec8e28275de2a13e058f30cb19b)
            check_type(argname="argument dependables", value=dependables, expected_type=type_hints["dependables"])
            check_type(argname="argument extended_s3_destination_configuration", value=extended_s3_destination_configuration, expected_type=type_hints["extended_s3_destination_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dependables is not None:
            self._values["dependables"] = dependables
        if extended_s3_destination_configuration is not None:
            self._values["extended_s3_destination_configuration"] = extended_s3_destination_configuration

    @builtins.property
    def dependables(
        self,
    ) -> typing.Optional[typing.List[_constructs_77d1e7e8.IDependable]]:
        '''Any resources that were created by the destination when binding it to the stack that must be deployed before the delivery stream is deployed.

        :default: []
        '''
        result = self._values.get("dependables")
        return typing.cast(typing.Optional[typing.List[_constructs_77d1e7e8.IDependable]], result)

    @builtins.property
    def extended_s3_destination_configuration(
        self,
    ) -> typing.Optional[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty]:
        '''S3 destination configuration properties.

        :default: - S3 destination is not used.
        '''
        result = self._values.get("extended_s3_destination_configuration")
        return typing.cast(typing.Optional[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.DestinationS3BackupProps",
    jsii_struct_bases=[CommonDestinationS3Props],
    name_mapping={
        "buffering_interval": "bufferingInterval",
        "buffering_size": "bufferingSize",
        "compression": "compression",
        "data_output_prefix": "dataOutputPrefix",
        "encryption_key": "encryptionKey",
        "error_output_prefix": "errorOutputPrefix",
        "bucket": "bucket",
        "logging_config": "loggingConfig",
        "mode": "mode",
    },
)
class DestinationS3BackupProps(CommonDestinationS3Props):
    def __init__(
        self,
        *,
        buffering_interval: typing.Optional[_Duration_4839e8c3] = None,
        buffering_size: typing.Optional[_Size_7b441c34] = None,
        compression: typing.Optional[Compression] = None,
        data_output_prefix: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        bucket: typing.Optional[_IBucket_42e086fd] = None,
        logging_config: typing.Optional["ILoggingConfig"] = None,
        mode: typing.Optional[BackupMode] = None,
    ) -> None:
        '''Properties for defining an S3 backup destination.

        S3 backup is available for all destinations, regardless of whether the final destination is S3 or not.

        :param buffering_interval: The length of time that Firehose buffers incoming data before delivering it to the S3 bucket. Minimum: Duration.seconds(0) Maximum: Duration.seconds(900) Default: Duration.seconds(300)
        :param buffering_size: The size of the buffer that Amazon Data Firehose uses for incoming data before delivering it to the S3 bucket. Minimum: Size.mebibytes(1) Maximum: Size.mebibytes(128) Default: Size.mebibytes(5)
        :param compression: The type of compression that Amazon Data Firehose uses to compress the data that it delivers to the Amazon S3 bucket. The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket. Default: - UNCOMPRESSED
        :param data_output_prefix: A prefix that Amazon Data Firehose evaluates and adds to records before writing them to S3. This prefix appears immediately following the bucket name. Default: "YYYY/MM/DD/HH"
        :param encryption_key: The AWS KMS key used to encrypt the data that it delivers to your Amazon S3 bucket. Default: - Data is not encrypted.
        :param error_output_prefix: A prefix that Amazon Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. Default: "YYYY/MM/DD/HH"
        :param bucket: The S3 bucket that will store data and failed records. Default: - If ``mode`` is set to ``BackupMode.ALL`` or ``BackupMode.FAILED``, a bucket will be created for you.
        :param logging_config: Configuration that determines whether to log errors during data transformation or delivery failures, and specifies the CloudWatch log group for storing error logs. Default: - errors will be logged and a log group will be created for you.
        :param mode: Indicates the mode by which incoming records should be backed up to S3, if any. If ``bucket`` is provided, this will be implicitly set to ``BackupMode.ALL``. Default: - If ``bucket`` is provided, the default will be ``BackupMode.ALL``. Otherwise, source records are not backed up to S3.

        :exampleMetadata: infused

        Example::

            # Enable backup of all source records (to an S3 bucket created by CDK).
            # bucket: s3.Bucket
            # Explicitly provide an S3 bucket to which all source records will be backed up.
            # backup_bucket: s3.Bucket
            
            firehose.DeliveryStream(self, "Delivery Stream Backup All",
                destination=
                firehose.S3Bucket(bucket,
                    s3_backup=firehose.DestinationS3BackupProps(
                        mode=firehose.BackupMode.ALL
                    )
                )
            )
            firehose.DeliveryStream(self, "Delivery Stream Backup All Explicit Bucket",
                destination=
                firehose.S3Bucket(bucket,
                    s3_backup=firehose.DestinationS3BackupProps(
                        bucket=backup_bucket
                    )
                )
            )
            # Explicitly provide an S3 prefix under which all source records will be backed up.
            firehose.DeliveryStream(self, "Delivery Stream Backup All Explicit Prefix",
                destination=
                firehose.S3Bucket(bucket,
                    s3_backup=firehose.DestinationS3BackupProps(
                        mode=firehose.BackupMode.ALL,
                        data_output_prefix="mybackup"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14700eb876e8e0f20f42a3b1362e4b8cd4eb596f1fbaecf0e207a387e8e2247d)
            check_type(argname="argument buffering_interval", value=buffering_interval, expected_type=type_hints["buffering_interval"])
            check_type(argname="argument buffering_size", value=buffering_size, expected_type=type_hints["buffering_size"])
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument data_output_prefix", value=data_output_prefix, expected_type=type_hints["data_output_prefix"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument error_output_prefix", value=error_output_prefix, expected_type=type_hints["error_output_prefix"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if buffering_interval is not None:
            self._values["buffering_interval"] = buffering_interval
        if buffering_size is not None:
            self._values["buffering_size"] = buffering_size
        if compression is not None:
            self._values["compression"] = compression
        if data_output_prefix is not None:
            self._values["data_output_prefix"] = data_output_prefix
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if error_output_prefix is not None:
            self._values["error_output_prefix"] = error_output_prefix
        if bucket is not None:
            self._values["bucket"] = bucket
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if mode is not None:
            self._values["mode"] = mode

    @builtins.property
    def buffering_interval(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The length of time that Firehose buffers incoming data before delivering it to the S3 bucket.

        Minimum: Duration.seconds(0)
        Maximum: Duration.seconds(900)

        :default: Duration.seconds(300)
        '''
        result = self._values.get("buffering_interval")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def buffering_size(self) -> typing.Optional[_Size_7b441c34]:
        '''The size of the buffer that Amazon Data Firehose uses for incoming data before delivering it to the S3 bucket.

        Minimum: Size.mebibytes(1)
        Maximum: Size.mebibytes(128)

        :default: Size.mebibytes(5)
        '''
        result = self._values.get("buffering_size")
        return typing.cast(typing.Optional[_Size_7b441c34], result)

    @builtins.property
    def compression(self) -> typing.Optional[Compression]:
        '''The type of compression that Amazon Data Firehose uses to compress the data that it delivers to the Amazon S3 bucket.

        The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift
        destinations because they are not supported by the Amazon Redshift COPY operation
        that reads from the S3 bucket.

        :default: - UNCOMPRESSED
        '''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[Compression], result)

    @builtins.property
    def data_output_prefix(self) -> typing.Optional[builtins.str]:
        '''A prefix that Amazon Data Firehose evaluates and adds to records before writing them to S3.

        This prefix appears immediately following the bucket name.

        :default: "YYYY/MM/DD/HH"

        :see: https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html
        '''
        result = self._values.get("data_output_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The AWS KMS key used to encrypt the data that it delivers to your Amazon S3 bucket.

        :default: - Data is not encrypted.
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def error_output_prefix(self) -> typing.Optional[builtins.str]:
        '''A prefix that Amazon Data Firehose evaluates and adds to failed records before writing them to S3.

        This prefix appears immediately following the bucket name.

        :default: "YYYY/MM/DD/HH"

        :see: https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html
        '''
        result = self._values.get("error_output_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket(self) -> typing.Optional[_IBucket_42e086fd]:
        '''The S3 bucket that will store data and failed records.

        :default: - If ``mode`` is set to ``BackupMode.ALL`` or ``BackupMode.FAILED``, a bucket will be created for you.
        '''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[_IBucket_42e086fd], result)

    @builtins.property
    def logging_config(self) -> typing.Optional["ILoggingConfig"]:
        '''Configuration that determines whether to log errors during data transformation or delivery failures, and specifies the CloudWatch log group for storing error logs.

        :default: - errors will be logged and a log group will be created for you.
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["ILoggingConfig"], result)

    @builtins.property
    def mode(self) -> typing.Optional[BackupMode]:
        '''Indicates the mode by which incoming records should be backed up to S3, if any.

        If ``bucket`` is provided, this will be implicitly set to ``BackupMode.ALL``.

        :default:

        - If ``bucket`` is provided, the default will be ``BackupMode.ALL``. Otherwise,
        source records are not backed up to S3.
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[BackupMode], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationS3BackupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_kinesisfirehose.IDataProcessor")
class IDataProcessor(typing_extensions.Protocol):
    '''A data processor that Amazon Data Firehose will call to transform records before delivering data.'''

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> DataProcessorProps:
        '''The constructor props of the DataProcessor.'''
        ...

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        *,
        role: _IRole_235f5d8e,
    ) -> DataProcessorConfig:
        '''Binds this processor to a destination of a delivery stream.

        Implementers should use this method to grant processor invocation permissions to the provided stream and return the
        necessary configuration to register as a processor.

        :param scope: -
        :param role: The IAM role assumed by Amazon Data Firehose to write to the destination that this DataProcessor will bind to.
        '''
        ...


class _IDataProcessorProxy:
    '''A data processor that Amazon Data Firehose will call to transform records before delivering data.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_kinesisfirehose.IDataProcessor"

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> DataProcessorProps:
        '''The constructor props of the DataProcessor.'''
        return typing.cast(DataProcessorProps, jsii.get(self, "props"))

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        *,
        role: _IRole_235f5d8e,
    ) -> DataProcessorConfig:
        '''Binds this processor to a destination of a delivery stream.

        Implementers should use this method to grant processor invocation permissions to the provided stream and return the
        necessary configuration to register as a processor.

        :param scope: -
        :param role: The IAM role assumed by Amazon Data Firehose to write to the destination that this DataProcessor will bind to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4720a6b97c475eae9ec0d65aca8250b00f57d45f0efb2368b8df6d486162c508)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        options = DataProcessorBindOptions(role=role)

        return typing.cast(DataProcessorConfig, jsii.invoke(self, "bind", [scope, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataProcessor).__jsii_proxy_class__ = lambda : _IDataProcessorProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_kinesisfirehose.IDeliveryStream")
class IDeliveryStream(
    _IResource_c80c4260,
    _IGrantable_71c4f5de,
    _IConnectable_10015a05,
    typing_extensions.Protocol,
):
    '''Represents an Amazon Data Firehose delivery stream.'''

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamArn")
    def delivery_stream_arn(self) -> builtins.str:
        '''The ARN of the delivery stream.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamName")
    def delivery_stream_name(self) -> builtins.str:
        '''The name of the delivery stream.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the ``grantee`` identity permissions to perform ``actions``.

        :param grantee: -
        :param actions: -
        '''
        ...

    @jsii.member(jsii_name="grantPutRecords")
    def grant_put_records(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the ``grantee`` identity permissions to perform ``firehose:PutRecord`` and ``firehose:PutRecordBatch`` actions on this delivery stream.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Return the given named metric for this delivery stream.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        ...

    @jsii.member(jsii_name="metricBackupToS3Bytes")
    def metric_backup_to_s3_bytes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the number of bytes delivered to Amazon S3 for backup over the specified time period.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        ...

    @jsii.member(jsii_name="metricBackupToS3DataFreshness")
    def metric_backup_to_s3_data_freshness(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the age (from getting into Amazon Data Firehose to now) of the oldest record in Amazon Data Firehose.

        Any record older than this age has been delivered to the Amazon S3 bucket for backup.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        ...

    @jsii.member(jsii_name="metricBackupToS3Records")
    def metric_backup_to_s3_records(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the number of records delivered to Amazon S3 for backup over the specified time period.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        ...

    @jsii.member(jsii_name="metricIncomingBytes")
    def metric_incoming_bytes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the number of bytes ingested successfully into the delivery stream over the specified time period after throttling.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        ...

    @jsii.member(jsii_name="metricIncomingRecords")
    def metric_incoming_records(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the number of records ingested successfully into the delivery stream over the specified time period after throttling.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        ...


class _IDeliveryStreamProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
    jsii.proxy_for(_IGrantable_71c4f5de), # type: ignore[misc]
    jsii.proxy_for(_IConnectable_10015a05), # type: ignore[misc]
):
    '''Represents an Amazon Data Firehose delivery stream.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_kinesisfirehose.IDeliveryStream"

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamArn")
    def delivery_stream_arn(self) -> builtins.str:
        '''The ARN of the delivery stream.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deliveryStreamArn"))

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamName")
    def delivery_stream_name(self) -> builtins.str:
        '''The name of the delivery stream.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deliveryStreamName"))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the ``grantee`` identity permissions to perform ``actions``.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2734269481cf10b40e22df40c033138f0b366868257b0867e62eb92924e9f879)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantPutRecords")
    def grant_put_records(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the ``grantee`` identity permissions to perform ``firehose:PutRecord`` and ``firehose:PutRecordBatch`` actions on this delivery stream.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__430b83a9ce03b133eb0ca75afb61f22cb3d6eac65aafcc08346ba35beea872c2)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPutRecords", [grantee]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Return the given named metric for this delivery stream.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25d98802194f172640833e51b398adf85ca294da7e2a4a6dfb45bfe99dfdb071)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metric", [metric_name, props]))

    @jsii.member(jsii_name="metricBackupToS3Bytes")
    def metric_backup_to_s3_bytes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the number of bytes delivered to Amazon S3 for backup over the specified time period.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricBackupToS3Bytes", [props]))

    @jsii.member(jsii_name="metricBackupToS3DataFreshness")
    def metric_backup_to_s3_data_freshness(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the age (from getting into Amazon Data Firehose to now) of the oldest record in Amazon Data Firehose.

        Any record older than this age has been delivered to the Amazon S3 bucket for backup.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricBackupToS3DataFreshness", [props]))

    @jsii.member(jsii_name="metricBackupToS3Records")
    def metric_backup_to_s3_records(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the number of records delivered to Amazon S3 for backup over the specified time period.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricBackupToS3Records", [props]))

    @jsii.member(jsii_name="metricIncomingBytes")
    def metric_incoming_bytes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the number of bytes ingested successfully into the delivery stream over the specified time period after throttling.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricIncomingBytes", [props]))

    @jsii.member(jsii_name="metricIncomingRecords")
    def metric_incoming_records(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the number of records ingested successfully into the delivery stream over the specified time period after throttling.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricIncomingRecords", [props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeliveryStream).__jsii_proxy_class__ = lambda : _IDeliveryStreamProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_kinesisfirehose.IDestination")
class IDestination(typing_extensions.Protocol):
    '''An Amazon Data Firehose delivery stream destination.'''

    @jsii.member(jsii_name="bind")
    def bind(self, scope: _constructs_77d1e7e8.Construct) -> DestinationConfig:
        '''Binds this destination to the Amazon Data Firehose delivery stream.

        Implementers should use this method to bind resources to the stack and initialize values using the provided stream.

        :param scope: -
        '''
        ...


class _IDestinationProxy:
    '''An Amazon Data Firehose delivery stream destination.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_kinesisfirehose.IDestination"

    @jsii.member(jsii_name="bind")
    def bind(self, scope: _constructs_77d1e7e8.Construct) -> DestinationConfig:
        '''Binds this destination to the Amazon Data Firehose delivery stream.

        Implementers should use this method to bind resources to the stack and initialize values using the provided stream.

        :param scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4557c076602017c3ae1d9a7de086acd858753a2681320e75c1151baf3ad8a77)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        options = DestinationBindOptions()

        return typing.cast(DestinationConfig, jsii.invoke(self, "bind", [scope, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDestination).__jsii_proxy_class__ = lambda : _IDestinationProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_kinesisfirehose.ILoggingConfig")
class ILoggingConfig(typing_extensions.Protocol):
    '''Configuration interface for logging errors when data transformation or delivery fails.

    This interface defines whether logging is enabled and optionally allows specifying a
    CloudWatch Log Group for storing error logs.
    '''

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> builtins.bool:
        '''If true, log errors when data transformation or data delivery fails.

        ``true`` when using ``EnableLogging``, ``false`` when using ``DisableLogging``.
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="logGroup")
    def log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''The CloudWatch log group where log streams will be created to hold error logs.

        :default: - if ``logging`` is set to ``true``, a log group will be created for you.
        '''
        ...


class _ILoggingConfigProxy:
    '''Configuration interface for logging errors when data transformation or delivery fails.

    This interface defines whether logging is enabled and optionally allows specifying a
    CloudWatch Log Group for storing error logs.
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_kinesisfirehose.ILoggingConfig"

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> builtins.bool:
        '''If true, log errors when data transformation or data delivery fails.

        ``true`` when using ``EnableLogging``, ``false`` when using ``DisableLogging``.
        '''
        return typing.cast(builtins.bool, jsii.get(self, "logging"))

    @builtins.property
    @jsii.member(jsii_name="logGroup")
    def log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''The CloudWatch log group where log streams will be created to hold error logs.

        :default: - if ``logging`` is set to ``true``, a log group will be created for you.
        '''
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], jsii.get(self, "logGroup"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILoggingConfig).__jsii_proxy_class__ = lambda : _ILoggingConfigProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_kinesisfirehose.ISource")
class ISource(typing_extensions.Protocol):
    '''An interface for defining a source that can be used in an Amazon Data Firehose delivery stream.'''

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant read permissions for this source resource and its contents to an IAM principal (the delivery stream).

        If an encryption key is used, permission to use the key to decrypt the
        contents of the stream will also be granted.

        :param grantee: -
        '''
        ...


class _ISourceProxy:
    '''An interface for defining a source that can be used in an Amazon Data Firehose delivery stream.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_kinesisfirehose.ISource"

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant read permissions for this source resource and its contents to an IAM principal (the delivery stream).

        If an encryption key is used, permission to use the key to decrypt the
        contents of the stream will also be granted.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d31d061482330f398322aedbe7845244fe1c55607a37db88ea3629f702ba69b0)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISource).__jsii_proxy_class__ = lambda : _ISourceProxy


@jsii.implements(ISource)
class KinesisStreamSource(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.KinesisStreamSource",
):
    '''An Amazon Data Firehose delivery stream source.

    :exampleMetadata: infused

    Example::

        # destination: firehose.IDestination
        
        source_stream = kinesis.Stream(self, "Source Stream")
        
        firehose.DeliveryStream(self, "Delivery Stream",
            source=firehose.KinesisStreamSource(source_stream),
            destination=destination
        )
    '''

    def __init__(self, stream: _IStream_4e2457d2) -> None:
        '''Creates a new KinesisStreamSource.

        :param stream: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc95432da9a8005268f62059d26c76ff3244e1763c675e2cf288a4edbb0235a3)
            check_type(argname="argument stream", value=stream, expected_type=type_hints["stream"])
        jsii.create(self.__class__, self, [stream])

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant read permissions for this source resource and its contents to an IAM principal (the delivery stream).

        If an encryption key is used, permission to use the key to decrypt the
        contents of the stream will also be granted.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0139dd9374d65b09aeb2cc12f10df74ef6fb54d32d3dbfc129f0e7ca2d14423)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))


@jsii.implements(IDataProcessor)
class LambdaFunctionProcessor(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.LambdaFunctionProcessor",
):
    '''Use an AWS Lambda function to transform records.

    :exampleMetadata: infused

    Example::

        # bucket: s3.Bucket
        # Provide a Lambda function that will transform records before delivery, with custom
        # buffering and retry configuration
        lambda_function = lambda_.Function(self, "Processor",
            runtime=lambda_.Runtime.NODEJS_LATEST,
            handler="index.handler",
            code=lambda_.Code.from_asset(path.join(__dirname, "process-records"))
        )
        lambda_processor = firehose.LambdaFunctionProcessor(lambda_function,
            buffer_interval=Duration.minutes(5),
            buffer_size=Size.mebibytes(5),
            retries=5
        )
        s3_destination = firehose.S3Bucket(bucket,
            processor=lambda_processor
        )
        firehose.DeliveryStream(self, "Delivery Stream",
            destination=s3_destination
        )
    '''

    def __init__(
        self,
        lambda_function: _IFunction_6adb0ab8,
        *,
        buffer_interval: typing.Optional[_Duration_4839e8c3] = None,
        buffer_size: typing.Optional[_Size_7b441c34] = None,
        retries: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param lambda_function: -
        :param buffer_interval: The length of time Amazon Data Firehose will buffer incoming data before calling the processor. s Default: Duration.minutes(1)
        :param buffer_size: The amount of incoming data Amazon Data Firehose will buffer before calling the processor. Default: Size.mebibytes(3)
        :param retries: The number of times Amazon Data Firehose will retry the processor invocation after a failure due to network timeout or invocation limits. Default: 3
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9ef06af75a5f9424b9a83d955544e1a8c769bb828e54b77e5dcec4ddd0f9154)
            check_type(argname="argument lambda_function", value=lambda_function, expected_type=type_hints["lambda_function"])
        props = DataProcessorProps(
            buffer_interval=buffer_interval, buffer_size=buffer_size, retries=retries
        )

        jsii.create(self.__class__, self, [lambda_function, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        *,
        role: _IRole_235f5d8e,
    ) -> DataProcessorConfig:
        '''Binds this processor to a destination of a delivery stream.

        Implementers should use this method to grant processor invocation permissions to the provided stream and return the
        necessary configuration to register as a processor.

        :param _scope: -
        :param role: The IAM role assumed by Amazon Data Firehose to write to the destination that this DataProcessor will bind to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__393c41d8ae2fe5acab13fd70fff9f4778e727adfd78b86d20820f067071490de)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
        options = DataProcessorBindOptions(role=role)

        return typing.cast(DataProcessorConfig, jsii.invoke(self, "bind", [_scope, options]))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> DataProcessorProps:
        '''The constructor props of the LambdaFunctionProcessor.'''
        return typing.cast(DataProcessorProps, jsii.get(self, "props"))


@jsii.implements(IDestination)
class S3Bucket(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.S3Bucket",
):
    '''An S3 bucket destination for data from an Amazon Data Firehose delivery stream.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_kinesisfirehose as firehose
        
        
        bucket = s3.Bucket(self, "MyBucket")
        stream = firehose.DeliveryStream(self, "MyStream",
            destination=firehose.S3Bucket(bucket)
        )
        
        topic_rule = iot.TopicRule(self, "TopicRule",
            sql=iot.IotSql.from_string_as_ver20160323("SELECT * FROM 'device/+/data'"),
            actions=[
                actions.FirehosePutRecordAction(stream,
                    batch_mode=True,
                    record_separator=actions.FirehoseRecordSeparator.NEWLINE
                )
            ]
        )
    '''

    def __init__(
        self,
        bucket: _IBucket_42e086fd,
        *,
        file_extension: typing.Optional[builtins.str] = None,
        time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
        buffering_interval: typing.Optional[_Duration_4839e8c3] = None,
        buffering_size: typing.Optional[_Size_7b441c34] = None,
        compression: typing.Optional[Compression] = None,
        data_output_prefix: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[ILoggingConfig] = None,
        processor: typing.Optional[IDataProcessor] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        s3_backup: typing.Optional[typing.Union[DestinationS3BackupProps, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket: -
        :param file_extension: Specify a file extension. It will override the default file extension appended by Data Format Conversion or S3 compression features such as ``.parquet`` or ``.gz``. File extension must start with a period (``.``) and can contain allowed characters: ``0-9a-z!-_.*'()``. Default: - The default file extension appended by Data Format Conversion or S3 compression features
        :param time_zone: The time zone you prefer. Default: - UTC
        :param buffering_interval: The length of time that Firehose buffers incoming data before delivering it to the S3 bucket. Minimum: Duration.seconds(0) Maximum: Duration.seconds(900) Default: Duration.seconds(300)
        :param buffering_size: The size of the buffer that Amazon Data Firehose uses for incoming data before delivering it to the S3 bucket. Minimum: Size.mebibytes(1) Maximum: Size.mebibytes(128) Default: Size.mebibytes(5)
        :param compression: The type of compression that Amazon Data Firehose uses to compress the data that it delivers to the Amazon S3 bucket. The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket. Default: - UNCOMPRESSED
        :param data_output_prefix: A prefix that Amazon Data Firehose evaluates and adds to records before writing them to S3. This prefix appears immediately following the bucket name. Default: "YYYY/MM/DD/HH"
        :param encryption_key: The AWS KMS key used to encrypt the data that it delivers to your Amazon S3 bucket. Default: - Data is not encrypted.
        :param error_output_prefix: A prefix that Amazon Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. Default: "YYYY/MM/DD/HH"
        :param logging_config: Configuration that determines whether to log errors during data transformation or delivery failures, and specifies the CloudWatch log group for storing error logs. Default: - errors will be logged and a log group will be created for you.
        :param processor: The data transformation that should be performed on the data before writing to the destination. Default: - no data transformation will occur.
        :param role: The IAM role associated with this destination. Assumed by Amazon Data Firehose to invoke processors and write to destinations Default: - a role will be created with default permissions.
        :param s3_backup: The configuration for backing up source records to S3. Default: - source records will not be backed up to S3.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2eaf455255fc260033aa24d456779f4b21172e8b4cf2c51f6355f415c9f3ccd)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        props = S3BucketProps(
            file_extension=file_extension,
            time_zone=time_zone,
            buffering_interval=buffering_interval,
            buffering_size=buffering_size,
            compression=compression,
            data_output_prefix=data_output_prefix,
            encryption_key=encryption_key,
            error_output_prefix=error_output_prefix,
            logging_config=logging_config,
            processor=processor,
            role=role,
            s3_backup=s3_backup,
        )

        jsii.create(self.__class__, self, [bucket, props])

    @jsii.member(jsii_name="bind")
    def bind(self, scope: _constructs_77d1e7e8.Construct) -> DestinationConfig:
        '''Binds this destination to the Amazon Data Firehose delivery stream.

        Implementers should use this method to bind resources to the stack and initialize values using the provided stream.

        :param scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3fdb21f9fe6d8dcaca6f65ba8cd1a376d43176607319802bd013001c8c5e9fd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        _options = DestinationBindOptions()

        return typing.cast(DestinationConfig, jsii.invoke(self, "bind", [scope, _options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.S3BucketProps",
    jsii_struct_bases=[CommonDestinationS3Props, CommonDestinationProps],
    name_mapping={
        "buffering_interval": "bufferingInterval",
        "buffering_size": "bufferingSize",
        "compression": "compression",
        "data_output_prefix": "dataOutputPrefix",
        "encryption_key": "encryptionKey",
        "error_output_prefix": "errorOutputPrefix",
        "logging_config": "loggingConfig",
        "processor": "processor",
        "role": "role",
        "s3_backup": "s3Backup",
        "file_extension": "fileExtension",
        "time_zone": "timeZone",
    },
)
class S3BucketProps(CommonDestinationS3Props, CommonDestinationProps):
    def __init__(
        self,
        *,
        buffering_interval: typing.Optional[_Duration_4839e8c3] = None,
        buffering_size: typing.Optional[_Size_7b441c34] = None,
        compression: typing.Optional[Compression] = None,
        data_output_prefix: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        error_output_prefix: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[ILoggingConfig] = None,
        processor: typing.Optional[IDataProcessor] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        s3_backup: typing.Optional[typing.Union[DestinationS3BackupProps, typing.Dict[builtins.str, typing.Any]]] = None,
        file_extension: typing.Optional[builtins.str] = None,
        time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
    ) -> None:
        '''Props for defining an S3 destination of an Amazon Data Firehose delivery stream.

        :param buffering_interval: The length of time that Firehose buffers incoming data before delivering it to the S3 bucket. Minimum: Duration.seconds(0) Maximum: Duration.seconds(900) Default: Duration.seconds(300)
        :param buffering_size: The size of the buffer that Amazon Data Firehose uses for incoming data before delivering it to the S3 bucket. Minimum: Size.mebibytes(1) Maximum: Size.mebibytes(128) Default: Size.mebibytes(5)
        :param compression: The type of compression that Amazon Data Firehose uses to compress the data that it delivers to the Amazon S3 bucket. The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift COPY operation that reads from the S3 bucket. Default: - UNCOMPRESSED
        :param data_output_prefix: A prefix that Amazon Data Firehose evaluates and adds to records before writing them to S3. This prefix appears immediately following the bucket name. Default: "YYYY/MM/DD/HH"
        :param encryption_key: The AWS KMS key used to encrypt the data that it delivers to your Amazon S3 bucket. Default: - Data is not encrypted.
        :param error_output_prefix: A prefix that Amazon Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. Default: "YYYY/MM/DD/HH"
        :param logging_config: Configuration that determines whether to log errors during data transformation or delivery failures, and specifies the CloudWatch log group for storing error logs. Default: - errors will be logged and a log group will be created for you.
        :param processor: The data transformation that should be performed on the data before writing to the destination. Default: - no data transformation will occur.
        :param role: The IAM role associated with this destination. Assumed by Amazon Data Firehose to invoke processors and write to destinations Default: - a role will be created with default permissions.
        :param s3_backup: The configuration for backing up source records to S3. Default: - source records will not be backed up to S3.
        :param file_extension: Specify a file extension. It will override the default file extension appended by Data Format Conversion or S3 compression features such as ``.parquet`` or ``.gz``. File extension must start with a period (``.``) and can contain allowed characters: ``0-9a-z!-_.*'()``. Default: - The default file extension appended by Data Format Conversion or S3 compression features
        :param time_zone: The time zone you prefer. Default: - UTC

        :exampleMetadata: infused

        Example::

            # bucket: s3.Bucket
            # Provide a Lambda function that will transform records before delivery, with custom
            # buffering and retry configuration
            lambda_function = lambda_.Function(self, "Processor",
                runtime=lambda_.Runtime.NODEJS_LATEST,
                handler="index.handler",
                code=lambda_.Code.from_asset(path.join(__dirname, "process-records"))
            )
            lambda_processor = firehose.LambdaFunctionProcessor(lambda_function,
                buffer_interval=Duration.minutes(5),
                buffer_size=Size.mebibytes(5),
                retries=5
            )
            s3_destination = firehose.S3Bucket(bucket,
                processor=lambda_processor
            )
            firehose.DeliveryStream(self, "Delivery Stream",
                destination=s3_destination
            )
        '''
        if isinstance(s3_backup, dict):
            s3_backup = DestinationS3BackupProps(**s3_backup)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04b12dc503479d22af2396c4df8d38c37536719187eef6ddd01c18b529dcbfc9)
            check_type(argname="argument buffering_interval", value=buffering_interval, expected_type=type_hints["buffering_interval"])
            check_type(argname="argument buffering_size", value=buffering_size, expected_type=type_hints["buffering_size"])
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument data_output_prefix", value=data_output_prefix, expected_type=type_hints["data_output_prefix"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument error_output_prefix", value=error_output_prefix, expected_type=type_hints["error_output_prefix"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument processor", value=processor, expected_type=type_hints["processor"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument s3_backup", value=s3_backup, expected_type=type_hints["s3_backup"])
            check_type(argname="argument file_extension", value=file_extension, expected_type=type_hints["file_extension"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if buffering_interval is not None:
            self._values["buffering_interval"] = buffering_interval
        if buffering_size is not None:
            self._values["buffering_size"] = buffering_size
        if compression is not None:
            self._values["compression"] = compression
        if data_output_prefix is not None:
            self._values["data_output_prefix"] = data_output_prefix
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if error_output_prefix is not None:
            self._values["error_output_prefix"] = error_output_prefix
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if processor is not None:
            self._values["processor"] = processor
        if role is not None:
            self._values["role"] = role
        if s3_backup is not None:
            self._values["s3_backup"] = s3_backup
        if file_extension is not None:
            self._values["file_extension"] = file_extension
        if time_zone is not None:
            self._values["time_zone"] = time_zone

    @builtins.property
    def buffering_interval(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The length of time that Firehose buffers incoming data before delivering it to the S3 bucket.

        Minimum: Duration.seconds(0)
        Maximum: Duration.seconds(900)

        :default: Duration.seconds(300)
        '''
        result = self._values.get("buffering_interval")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def buffering_size(self) -> typing.Optional[_Size_7b441c34]:
        '''The size of the buffer that Amazon Data Firehose uses for incoming data before delivering it to the S3 bucket.

        Minimum: Size.mebibytes(1)
        Maximum: Size.mebibytes(128)

        :default: Size.mebibytes(5)
        '''
        result = self._values.get("buffering_size")
        return typing.cast(typing.Optional[_Size_7b441c34], result)

    @builtins.property
    def compression(self) -> typing.Optional[Compression]:
        '''The type of compression that Amazon Data Firehose uses to compress the data that it delivers to the Amazon S3 bucket.

        The compression formats SNAPPY or ZIP cannot be specified for Amazon Redshift
        destinations because they are not supported by the Amazon Redshift COPY operation
        that reads from the S3 bucket.

        :default: - UNCOMPRESSED
        '''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[Compression], result)

    @builtins.property
    def data_output_prefix(self) -> typing.Optional[builtins.str]:
        '''A prefix that Amazon Data Firehose evaluates and adds to records before writing them to S3.

        This prefix appears immediately following the bucket name.

        :default: "YYYY/MM/DD/HH"

        :see: https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html
        '''
        result = self._values.get("data_output_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The AWS KMS key used to encrypt the data that it delivers to your Amazon S3 bucket.

        :default: - Data is not encrypted.
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def error_output_prefix(self) -> typing.Optional[builtins.str]:
        '''A prefix that Amazon Data Firehose evaluates and adds to failed records before writing them to S3.

        This prefix appears immediately following the bucket name.

        :default: "YYYY/MM/DD/HH"

        :see: https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html
        '''
        result = self._values.get("error_output_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_config(self) -> typing.Optional[ILoggingConfig]:
        '''Configuration that determines whether to log errors during data transformation or delivery failures, and specifies the CloudWatch log group for storing error logs.

        :default: - errors will be logged and a log group will be created for you.
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional[ILoggingConfig], result)

    @builtins.property
    def processor(self) -> typing.Optional[IDataProcessor]:
        '''The data transformation that should be performed on the data before writing to the destination.

        :default: - no data transformation will occur.
        '''
        result = self._values.get("processor")
        return typing.cast(typing.Optional[IDataProcessor], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role associated with this destination.

        Assumed by Amazon Data Firehose to invoke processors and write to destinations

        :default: - a role will be created with default permissions.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def s3_backup(self) -> typing.Optional[DestinationS3BackupProps]:
        '''The configuration for backing up source records to S3.

        :default: - source records will not be backed up to S3.
        '''
        result = self._values.get("s3_backup")
        return typing.cast(typing.Optional[DestinationS3BackupProps], result)

    @builtins.property
    def file_extension(self) -> typing.Optional[builtins.str]:
        '''Specify a file extension.

        It will override the default file extension appended by Data Format Conversion or S3 compression features such as ``.parquet`` or ``.gz``.

        File extension must start with a period (``.``) and can contain allowed characters: ``0-9a-z!-_.*'()``.

        :default: - The default file extension appended by Data Format Conversion or S3 compression features

        :see: https://docs.aws.amazon.com/firehose/latest/dev/create-destination.html#create-destination-s3
        '''
        result = self._values.get("file_extension")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[_TimeZone_cdd72ac9]:
        '''The time zone you prefer.

        :default: - UTC

        :see: https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html#timestamp-namespace
        '''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[_TimeZone_cdd72ac9], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3BucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StreamEncryption(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.StreamEncryption",
):
    '''Represents server-side encryption for an Amazon Firehose Delivery Stream.

    :exampleMetadata: infused

    Example::

        # destination: firehose.IDestination
        # SSE with an customer-managed key that is explicitly specified
        # key: kms.Key
        
        
        # SSE with an AWS-owned key
        firehose.DeliveryStream(self, "Delivery Stream with AWS Owned Key",
            encryption=firehose.StreamEncryption.aws_owned_key(),
            destination=destination
        )
        # SSE with an customer-managed key that is created automatically by the CDK
        firehose.DeliveryStream(self, "Delivery Stream with Customer Managed Key",
            encryption=firehose.StreamEncryption.customer_managed_key(),
            destination=destination
        )
        firehose.DeliveryStream(self, "Delivery Stream with Customer Managed and Provided Key",
            encryption=firehose.StreamEncryption.customer_managed_key(key),
            destination=destination
        )
    '''

    @jsii.member(jsii_name="awsOwnedKey")
    @builtins.classmethod
    def aws_owned_key(cls) -> "StreamEncryption":
        '''Configure server-side encryption using an AWS owned key.'''
        return typing.cast("StreamEncryption", jsii.sinvoke(cls, "awsOwnedKey", []))

    @jsii.member(jsii_name="customerManagedKey")
    @builtins.classmethod
    def customer_managed_key(
        cls,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
    ) -> "StreamEncryption":
        '''Configure server-side encryption using customer managed keys.

        :param encryption_key: the KMS key for the delivery stream.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efb44f4c68ce5ed338b1cadc1095db8f6b1ea6c2478ee68c07bb0fa95cecdf47)
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
        return typing.cast("StreamEncryption", jsii.sinvoke(cls, "customerManagedKey", [encryption_key]))

    @jsii.member(jsii_name="unencrypted")
    @builtins.classmethod
    def unencrypted(cls) -> "StreamEncryption":
        '''No server-side encryption is configured.'''
        return typing.cast("StreamEncryption", jsii.sinvoke(cls, "unencrypted", []))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "StreamEncryptionType":
        '''The type of server-side encryption for the Amazon Firehose delivery stream.'''
        return typing.cast("StreamEncryptionType", jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''Optional KMS key used for customer managed encryption.'''
        return typing.cast(typing.Optional[_IKey_5f11635f], jsii.get(self, "encryptionKey"))


class _StreamEncryptionProxy(StreamEncryption):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, StreamEncryption).__jsii_proxy_class__ = lambda : _StreamEncryptionProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_kinesisfirehose.StreamEncryptionType")
class StreamEncryptionType(enum.Enum):
    '''Options for server-side encryption of a delivery stream.'''

    UNENCRYPTED = "UNENCRYPTED"
    '''Data in the stream is stored unencrypted.'''
    CUSTOMER_MANAGED = "CUSTOMER_MANAGED"
    '''Data in the stream is stored encrypted by a KMS key managed by the customer.'''
    AWS_OWNED = "AWS_OWNED"
    '''Data in the stream is stored encrypted by a KMS key owned by AWS and managed for use in multiple AWS accounts.'''


@jsii.implements(IDeliveryStream)
class DeliveryStream(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.DeliveryStream",
):
    '''Create a Amazon Data Firehose delivery stream.

    :resource: AWS::KinesisFirehose::DeliveryStream
    :exampleMetadata: infused

    Example::

        # bucket: s3.Bucket
        # Provide a Lambda function that will transform records before delivery, with custom
        # buffering and retry configuration
        lambda_function = lambda_.Function(self, "Processor",
            runtime=lambda_.Runtime.NODEJS_LATEST,
            handler="index.handler",
            code=lambda_.Code.from_asset(path.join(__dirname, "process-records"))
        )
        lambda_processor = firehose.LambdaFunctionProcessor(lambda_function,
            buffer_interval=Duration.minutes(5),
            buffer_size=Size.mebibytes(5),
            retries=5
        )
        s3_destination = firehose.S3Bucket(bucket,
            processor=lambda_processor
        )
        firehose.DeliveryStream(self, "Delivery Stream",
            destination=s3_destination
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        destination: IDestination,
        delivery_stream_name: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[StreamEncryption] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        source: typing.Optional[ISource] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param destination: The destination that this delivery stream will deliver data to.
        :param delivery_stream_name: A name for the delivery stream. Default: - a name is generated by CloudFormation.
        :param encryption: Indicates the type of customer master key (CMK) to use for server-side encryption, if any. Default: StreamEncryption.unencrypted()
        :param role: The IAM role associated with this delivery stream. Assumed by Amazon Data Firehose to read from sources and encrypt data server-side. Default: - a role will be created with default permissions.
        :param source: The Kinesis data stream to use as a source for this delivery stream. Default: - data must be written to the delivery stream via a direct put.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c5be371024241f9b37d47dc30b79a0d54ad9453eb90d21cc0f6c880f2e4fb91)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DeliveryStreamProps(
            destination=destination,
            delivery_stream_name=delivery_stream_name,
            encryption=encryption,
            role=role,
            source=source,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromDeliveryStreamArn")
    @builtins.classmethod
    def from_delivery_stream_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        delivery_stream_arn: builtins.str,
    ) -> IDeliveryStream:
        '''Import an existing delivery stream from its ARN.

        :param scope: -
        :param id: -
        :param delivery_stream_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1ce0063f18826b4ee51e0d895cc5452b1439ff1e769a5b248178badffad6011)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument delivery_stream_arn", value=delivery_stream_arn, expected_type=type_hints["delivery_stream_arn"])
        return typing.cast(IDeliveryStream, jsii.sinvoke(cls, "fromDeliveryStreamArn", [scope, id, delivery_stream_arn]))

    @jsii.member(jsii_name="fromDeliveryStreamAttributes")
    @builtins.classmethod
    def from_delivery_stream_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        delivery_stream_arn: typing.Optional[builtins.str] = None,
        delivery_stream_name: typing.Optional[builtins.str] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> IDeliveryStream:
        '''Import an existing delivery stream from its attributes.

        :param scope: -
        :param id: -
        :param delivery_stream_arn: The ARN of the delivery stream. At least one of deliveryStreamArn and deliveryStreamName must be provided. Default: - derived from ``deliveryStreamName``.
        :param delivery_stream_name: The name of the delivery stream. At least one of deliveryStreamName and deliveryStreamArn must be provided. Default: - derived from ``deliveryStreamArn``.
        :param role: The IAM role associated with this delivery stream. Assumed by Amazon Data Firehose to read from sources and encrypt data server-side. Default: - the imported stream cannot be granted access to other resources as an ``iam.IGrantable``.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60d49cb1de4cae1a83d89ae7d419d2e7a17f1c8a25478897973ca006cf1f5066)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = DeliveryStreamAttributes(
            delivery_stream_arn=delivery_stream_arn,
            delivery_stream_name=delivery_stream_name,
            role=role,
        )

        return typing.cast(IDeliveryStream, jsii.sinvoke(cls, "fromDeliveryStreamAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromDeliveryStreamName")
    @builtins.classmethod
    def from_delivery_stream_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        delivery_stream_name: builtins.str,
    ) -> IDeliveryStream:
        '''Import an existing delivery stream from its name.

        :param scope: -
        :param id: -
        :param delivery_stream_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__457e8328a163250ba61b71d2ce676a68d801ac8467c715e8ba511357cb60c507)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument delivery_stream_name", value=delivery_stream_name, expected_type=type_hints["delivery_stream_name"])
        return typing.cast(IDeliveryStream, jsii.sinvoke(cls, "fromDeliveryStreamName", [scope, id, delivery_stream_name]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the ``grantee`` identity permissions to perform ``actions``.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d29967317f0315691f87af41c6bab889af970cdd0860933427170179ccabb1b)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantPutRecords")
    def grant_put_records(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant the ``grantee`` identity permissions to perform ``firehose:PutRecord`` and ``firehose:PutRecordBatch`` actions on this delivery stream.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31fc61b3576a2a9576300f38d0cde9d0c42fcad47d437aa8ef160d5016007243)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPutRecords", [grantee]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Return the given named metric for this delivery stream.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86f3b1e63c4046b14a20d8f095529962a56cb82f03a0f9a310b5c1b707bc0f5f)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metric", [metric_name, props]))

    @jsii.member(jsii_name="metricBackupToS3Bytes")
    def metric_backup_to_s3_bytes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the number of bytes delivered to Amazon S3 for backup over the specified time period.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricBackupToS3Bytes", [props]))

    @jsii.member(jsii_name="metricBackupToS3DataFreshness")
    def metric_backup_to_s3_data_freshness(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the age (from getting into Amazon Data Firehose to now) of the oldest record in Amazon Data Firehose.

        Any record older than this age has been delivered to the Amazon S3 bucket for backup.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricBackupToS3DataFreshness", [props]))

    @jsii.member(jsii_name="metricBackupToS3Records")
    def metric_backup_to_s3_records(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the number of records delivered to Amazon S3 for backup over the specified time period.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricBackupToS3Records", [props]))

    @jsii.member(jsii_name="metricIncomingBytes")
    def metric_incoming_bytes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the number of bytes ingested successfully into the delivery stream over the specified time period after throttling.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricIncomingBytes", [props]))

    @jsii.member(jsii_name="metricIncomingRecords")
    def metric_incoming_records(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        stack_account: typing.Optional[builtins.str] = None,
        stack_region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        visible: typing.Optional[builtins.bool] = None,
    ) -> _Metric_e396a4dc:
        '''Metric for the number of records ingested successfully into the delivery stream over the specified time period after throttling.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param id: Unique identifier for this metric when used in dashboard widgets. The id can be used as a variable to represent this metric in math expressions. Valid characters are letters, numbers, and underscore. The first character must be a lowercase letter. Default: - No ID
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param stack_account: Account of the stack this metric is attached to. Default: - Deployment account.
        :param stack_region: Region of the stack this metric is attached to. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        :param visible: Whether this metric should be visible in dashboard graphs. Setting this to false is useful when you want to hide raw metrics that are used in math expressions, and show only the expression results. Default: true
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            id=id,
            label=label,
            period=period,
            region=region,
            stack_account=stack_account,
            stack_region=stack_region,
            statistic=statistic,
            unit=unit,
            visible=visible,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricIncomingRecords", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> _Connections_0f31fce8:
        '''Network connections between Amazon Data Firehose and other resources, i.e. Redshift cluster.'''
        return typing.cast(_Connections_0f31fce8, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamArn")
    def delivery_stream_arn(self) -> builtins.str:
        '''The ARN of the delivery stream.'''
        return typing.cast(builtins.str, jsii.get(self, "deliveryStreamArn"))

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamName")
    def delivery_stream_name(self) -> builtins.str:
        '''The name of the delivery stream.'''
        return typing.cast(builtins.str, jsii.get(self, "deliveryStreamName"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_539bb2fd:
        '''The principal to grant permissions to.'''
        return typing.cast(_IPrincipal_539bb2fd, jsii.get(self, "grantPrincipal"))


@jsii.implements(ILoggingConfig)
class DisableLogging(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.DisableLogging",
):
    '''Disables logging for error logs.

    When this class is used, logging is disabled (``logging: false``)
    and no CloudWatch log group can be specified.

    :exampleMetadata: infused

    Example::

        # bucket: s3.Bucket
        
        destination = firehose.S3Bucket(bucket,
            logging_config=firehose.DisableLogging()
        )
        firehose.DeliveryStream(self, "Delivery Stream",
            destination=destination
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> builtins.bool:
        '''If true, log errors when data transformation or data delivery fails.

        ``true`` when using ``EnableLogging``, ``false`` when using ``DisableLogging``.
        '''
        return typing.cast(builtins.bool, jsii.get(self, "logging"))


@jsii.implements(ILoggingConfig)
class EnableLogging(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.EnableLogging",
):
    '''Enables logging for error logs with an optional custom CloudWatch log group.

    When this class is used, logging is enabled (``logging: true``) and
    you can optionally provide a CloudWatch log group for storing the error logs.

    If no log group is provided, a default one will be created automatically.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_logs as logs
        # bucket: s3.Bucket
        
        
        log_group = logs.LogGroup(self, "Log Group")
        destination = firehose.S3Bucket(bucket,
            logging_config=firehose.EnableLogging(log_group)
        )
        
        firehose.DeliveryStream(self, "Delivery Stream",
            destination=destination
        )
    '''

    def __init__(self, log_group: typing.Optional[_ILogGroup_3c4fa718] = None) -> None:
        '''
        :param log_group: The CloudWatch log group where log streams will be created to hold error logs.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba11d69a3d91c8a6ba63c6ed55a7bbd149c317325863da3c41ebf373cf256b7c)
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
        jsii.create(self.__class__, self, [log_group])

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> builtins.bool:
        '''If true, log errors when data transformation or data delivery fails.

        ``true`` when using ``EnableLogging``, ``false`` when using ``DisableLogging``.
        '''
        return typing.cast(builtins.bool, jsii.get(self, "logging"))

    @builtins.property
    @jsii.member(jsii_name="logGroup")
    def log_group(self) -> typing.Optional[_ILogGroup_3c4fa718]:
        '''The CloudWatch log group where log streams will be created to hold error logs.'''
        return typing.cast(typing.Optional[_ILogGroup_3c4fa718], jsii.get(self, "logGroup"))


__all__ = [
    "BackupMode",
    "CfnDeliveryStream",
    "CfnDeliveryStreamProps",
    "CommonDestinationProps",
    "CommonDestinationS3Props",
    "Compression",
    "DataProcessorBindOptions",
    "DataProcessorConfig",
    "DataProcessorIdentifier",
    "DataProcessorProps",
    "DeliveryStream",
    "DeliveryStreamAttributes",
    "DeliveryStreamProps",
    "DestinationBindOptions",
    "DestinationConfig",
    "DestinationS3BackupProps",
    "DisableLogging",
    "EnableLogging",
    "IDataProcessor",
    "IDeliveryStream",
    "IDestination",
    "ILoggingConfig",
    "ISource",
    "KinesisStreamSource",
    "LambdaFunctionProcessor",
    "S3Bucket",
    "S3BucketProps",
    "StreamEncryption",
    "StreamEncryptionType",
]

publication.publish()

def _typecheckingstub__b3cd824a2680c7d043cac684bd1be9ca77e94201f1ba00785d60a50ff43c2288(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    amazon_open_search_serverless_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    amazonopensearchservice_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    database_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DatabaseSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delivery_stream_encryption_configuration_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delivery_stream_name: typing.Optional[builtins.str] = None,
    delivery_stream_type: typing.Optional[builtins.str] = None,
    direct_put_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DirectPutSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elasticsearch_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    extended_s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    http_endpoint_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iceberg_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.IcebergDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_stream_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.KinesisStreamSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    msk_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.MSKSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.RedshiftDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snowflake_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SnowflakeDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    splunk_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SplunkDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f6206943f45cc34824996fe47b775be3c1a09cb74450254dfa716bc71a96a69(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__822762453b1edc05d278fe4b56cb34de36a63cda89772b6624160f6ac406e7e7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9361f4405d0a8e9a0285d4b343c6420073eedc822c339d1a147f151a3b03f641(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58964b8831d37cbba22a48328508a0d1fc866bb6da992a0c3f544fc6649acc5a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__671f3a3eb25ab7249d3b64fb9d1c6865a8a68b8a7b92841ab6890851853da1f5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.DatabaseSourceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b541613844a306d329ee6aaf12a513672a01cea651f015810fd2ab896394415(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d90731f57c337a34bb7290e3bb4239e949b5caeea354433c46c25998a03b39f6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0749b7e1cb2e266044df272e646eba4d2505c56ccb68f4ce96de186aeb83ba9b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c2e3d41bd399b2de627c15c37d5d5a53d60ea55a256dc5f1b73146429dd1f24(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.DirectPutSourceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2485fd6e8467da83435abf801383e98fea4d4ae9797551e1774f2327e1b069c5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b3827d67811452e6783eeef4d719d420c5534229b93597dbfafa7256a89932e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c45396814a2f1f16d85b99c121f14ab851eda0a9f84038025d5ae44a858837a1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94c8f409ef0a75500e50bbf49d47688097508bd257b3ce092b027c552453cd59(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.IcebergDestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__025f54a26e52ce42f679eff3aa8b95a5fee2e0e5b3aba7c4320f9900690e60b9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.KinesisStreamSourceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d05261de796c66b290d3bf9493dedca3a4f904726566b1e0d28cd6f7e525757(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.MSKSourceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9283febc90a4404b9eb41b227b6baf567d66cf4929f4f56dc67252a81e997f1f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.RedshiftDestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb8b949ac7c9700a5ef03cddf3b3be451041166fe7583faee720a903b17ffd7c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.S3DestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4334e067c783ee048616b856f03ad5fb828c1a4c18bbdce130d9850ac2ce4034(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.SnowflakeDestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1143a0f5e018d10fdc1fff0bbcada0e3653e2264078be8b5a6441f6918b95c91(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.SplunkDestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b611aca673873100e4f1f1366dada7f80beaecdafd39582bd00fb48881dca276(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73b3806edee327ffa718f826cdd3f2971c613586675003f856582bd7f9f0990b(
    *,
    interval_in_seconds: typing.Optional[jsii.Number] = None,
    size_in_m_bs: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c09d95c569c785593bec028509479a3c62ff0333544fe7fb6ea165082930dcf0(
    *,
    index_name: builtins.str,
    role_arn: builtins.str,
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonOpenSearchServerlessBufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    collection_endpoint: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonOpenSearchServerlessRetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
    vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__753f83f6d86f1797776bc00b3eb90cc19e80bd47ed33370727e5209255714a3b(
    *,
    duration_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bc008db5e34e3ef0ac28740f5aa52a90ec2c2ec0ebeb06a2e361e737f34b840(
    *,
    interval_in_seconds: typing.Optional[jsii.Number] = None,
    size_in_m_bs: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd4e3bfe32a6bde0a79abfda5de58ef25a59c29217c39eadcd363cb781608bca(
    *,
    index_name: builtins.str,
    role_arn: builtins.str,
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cluster_endpoint: typing.Optional[builtins.str] = None,
    document_id_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DocumentIdOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    domain_arn: typing.Optional[builtins.str] = None,
    index_rotation_period: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
    type_name: typing.Optional[builtins.str] = None,
    vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a6adce37d15471d3dfb2f014a8d32c640e5a4f535c6da724e3b743675a04cb(
    *,
    duration_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68e16a68225e493cf684cc2bfb151ded05293f2e7b47087f4a97398a1bfeaeb0(
    *,
    connectivity: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c672d0753e4b959e46f98cc809bc2380cd7be551cc9bab6f1b7baa1d203a6f7d(
    *,
    interval_in_seconds: typing.Optional[jsii.Number] = None,
    size_in_m_bs: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92b3c1717fb66856049eddd62f0c12dbf945ae8d9450b716e7d065a04359aee0(
    *,
    catalog_arn: typing.Optional[builtins.str] = None,
    warehouse_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0992b1c8af7fd8e057904e94d1f683be6233929613125517587cd51de86aa4b5(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ed6eb88a63ca5e75a449863a292b3dcd0cbfcd3127e73f575819aaf579cc41f(
    *,
    data_table_name: builtins.str,
    copy_options: typing.Optional[builtins.str] = None,
    data_table_columns: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2fd0a4fb437e036bd2436bcfd397fa35f08aba48c5a25c4aac36dedb0d37e42(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    input_format_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.InputFormatConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    output_format_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.OutputFormatConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schema_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SchemaConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__111648b092f5dd75408d33db5fb1adea30dc7a8b58549cef95459f9224ccb26a(
    *,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    include: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cecf7807b45586be03c0bc76f8fcdf6ad93c6bd34a795d26aeaf365dd3d297c4(
    *,
    secrets_manager_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SecretsManagerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfa32769046e99e73e35a8b5e878b72f25abcaa661bf955ff25e794601e2126d(
    *,
    databases: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DatabasesProperty, typing.Dict[builtins.str, typing.Any]]],
    database_source_authentication_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DatabaseSourceAuthenticationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    database_source_vpc_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DatabaseSourceVPCConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    endpoint: builtins.str,
    port: jsii.Number,
    snapshot_watermark_table: builtins.str,
    tables: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DatabaseTablesProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
    columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DatabaseColumnsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    digest: typing.Optional[builtins.str] = None,
    public_certificate: typing.Optional[builtins.str] = None,
    ssl_mode: typing.Optional[builtins.str] = None,
    surrogate_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4616b4a1f40a4e175751eda3777e82055e2397fd9dad0a6cd009c18c89e97cd3(
    *,
    vpc_endpoint_service_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b669ca3e532e36dd3f6bf714eda78c90c8c90c4c1bc6dbebfab5c56e74950ddb(
    *,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    include: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6aa9553c52b253113ab9a3fd740ae3235a38fc2d9a582fa85db01832e154931(
    *,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    include: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a51e3602fa39b19119cb43ff1945ccb136f7909bb7d76a42abc9195cb0d725a3(
    *,
    key_type: builtins.str,
    key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42c1d0a7a47a7fb87bd171a324b5d6ec1a60f675aa066d295f3a321445b0d566(
    *,
    hive_json_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.HiveJsonSerDeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    open_x_json_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.OpenXJsonSerDeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9e156eb7fa7ea4dde332f5d2ef91909983b4fa7a5b5133510252f637465ea6c(
    *,
    destination_database_name: builtins.str,
    destination_table_name: builtins.str,
    partition_spec: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.PartitionSpecProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_error_output_prefix: typing.Optional[builtins.str] = None,
    unique_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb3b40e967adc088820cc6b98c8d06f49a47427fba6a11c4cfd878f0aa87017f(
    *,
    throughput_hint_in_m_bs: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d76edd5ad2b58b9b0bbc3359143f6d89ce784d7ac50b34881cf657d8016bcec4(
    *,
    default_document_id_format: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cc891db4fb4eb3331e62299f82fedd4776288b7686ae851e51bfb6e44e55a52(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.RetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__081c1ee4107d2560ed72dcc369fb8bd5cb51575be94b287e3e1d199e78950677(
    *,
    interval_in_seconds: typing.Optional[jsii.Number] = None,
    size_in_m_bs: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__029a33c003279860929256e859d4ba1b8707f3f6569f11613c5f08ef467fe6d6(
    *,
    index_name: builtins.str,
    role_arn: builtins.str,
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ElasticsearchBufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cluster_endpoint: typing.Optional[builtins.str] = None,
    document_id_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DocumentIdOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    domain_arn: typing.Optional[builtins.str] = None,
    index_rotation_period: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ElasticsearchRetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
    type_name: typing.Optional[builtins.str] = None,
    vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2556301b4eb1fbc8924ad4d41633add09219c34215bad4251ecd9506fbd5f4f1(
    *,
    duration_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4416718c6f0bcd460ac15d8467b60189a1b6ff006003483c5095802962acb534(
    *,
    kms_encryption_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.KMSEncryptionConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    no_encryption_config: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7faa411782bea929613482f29819c6479d5ad2f4416ea558d510fb9fd71eaa95(
    *,
    bucket_arn: builtins.str,
    role_arn: builtins.str,
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.BufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    compression_format: typing.Optional[builtins.str] = None,
    custom_time_zone: typing.Optional[builtins.str] = None,
    data_format_conversion_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DataFormatConversionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynamic_partitioning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DynamicPartitioningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    error_output_prefix: typing.Optional[builtins.str] = None,
    file_extension: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8aed0e38a71aaf287d17202c1a15e108a76c336307d62f78aaec9e6482a117f(
    *,
    timestamp_formats: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d04b9e64bbadb832ca77b64870e79e2910eb18ecbaf3d42b7d1c1b17fb3c160(
    *,
    attribute_name: builtins.str,
    attribute_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0aeaa2e754e3362456fea60de1849d85d4913483f2324b0f89480dc7822dd8c(
    *,
    url: builtins.str,
    access_key: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e8b3a25c8aa6cb1c905473fb8dd18a708e794918ae12a9a622993603b96ab8a(
    *,
    endpoint_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.HttpEndpointConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.BufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    request_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.HttpEndpointRequestConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.RetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
    secrets_manager_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SecretsManagerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9efa4d9f485d918f70adc5823c0a1caf4894264ec785a00d5ef0879e3c1177(
    *,
    common_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.HttpEndpointCommonAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    content_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cc5b65e233b52b72b153275ce8ced9f593e3385051386bed6920a574cf9f53d(
    *,
    catalog_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CatalogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    append_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.BufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    destination_table_configuration_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DestinationTableConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.RetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
    schema_evolution_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SchemaEvolutionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    table_creation_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.TableCreationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dce5223aa97132391790e172c7c143f8a4c8df67b3b09df48eb0b1dff486468b(
    *,
    deserializer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DeserializerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca085a464bc9440602c605444adda1cec3d2059da145bca43dd610fba2e9a8be(
    *,
    awskms_key_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ae1be427fa992bcfd551dc79aa5bba9af3c552f1661c763a814eb22ecd5dff7(
    *,
    kinesis_stream_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b2563c2a3f195e01ffbb501ca4b7d501c1fb934c35f08b019e248300a348473(
    *,
    authentication_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AuthenticationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    msk_cluster_arn: builtins.str,
    topic_name: builtins.str,
    read_from_timestamp: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65dc173b1d3e5c449c2f9ee9f1727428f35f33407e71da72ecdc48c19f3fb78c(
    *,
    case_insensitive: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    column_to_json_key_mappings: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    convert_dots_in_json_keys_to_underscores: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a6f3732f1d1f7da40207abc3f87e65bccadac8f31c2f54e16aa9b9d2132fd6e(
    *,
    block_size_bytes: typing.Optional[jsii.Number] = None,
    bloom_filter_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
    bloom_filter_false_positive_probability: typing.Optional[jsii.Number] = None,
    compression: typing.Optional[builtins.str] = None,
    dictionary_key_threshold: typing.Optional[jsii.Number] = None,
    enable_padding: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    format_version: typing.Optional[builtins.str] = None,
    padding_tolerance: typing.Optional[jsii.Number] = None,
    row_index_stride: typing.Optional[jsii.Number] = None,
    stripe_size_bytes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fcba637de22c6790633f7c4fdbfafe0f3cf2fcd07e8753fb333222a3b7916c2(
    *,
    serializer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SerializerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5e42046b59e857630ade1e52237b3f99ec5d3fcea0cff6ee85255354c8bc1a9(
    *,
    block_size_bytes: typing.Optional[jsii.Number] = None,
    compression: typing.Optional[builtins.str] = None,
    enable_dictionary_compression: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    max_padding_bytes: typing.Optional[jsii.Number] = None,
    page_size_bytes: typing.Optional[jsii.Number] = None,
    writer_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a839897ef0a46c7170de280f66ed4688ca42be1fcb75c29fba57bc1f602931c1(
    *,
    source_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__605b75f57047594e41cbdfa3a36b644835c149c59b7bc3649d482257f34c89b4(
    *,
    identity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.PartitionFieldProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47d08fb3fe02427fce54795dba1288ad02d1fec20884867948eae460f986d43d(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    processors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29244e412176b0b05c7328e22087c12ec9670a06bdeda2a69994a31022941e39(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69c6d7cb07c53f27959cf35e3f4436c85b60c102a9d091138cad44aec29a7fc3(
    *,
    type: builtins.str,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessorParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a05dc5298788a3b9496bc2e383242a0570183c6703c04af2c5e991292f2c58fa(
    *,
    cluster_jdbcurl: builtins.str,
    copy_command: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CopyCommandProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    password: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.RedshiftRetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
    secrets_manager_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SecretsManagerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0656ad0d58c235ec01fb44e9e595a95164029cf26c86a1e17d49b3de0807568(
    *,
    duration_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f65ebaf68fad95eebbec4bb62ddc86711c9f922e5243b0ef218440713a1dbf3(
    *,
    duration_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8569fcc15b3b4467365ecb9c23c43fe8704a4b9efea3337dfd60994daf97d928(
    *,
    bucket_arn: builtins.str,
    role_arn: builtins.str,
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.BufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    compression_format: typing.Optional[builtins.str] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    error_output_prefix: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1389c57283b687c62069951b51187332947eeb24f5fcb8781af71c2b3e5d657(
    *,
    catalog_id: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    table_name: typing.Optional[builtins.str] = None,
    version_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42267f168762343c22cce7785e160c133f9c7e7a8f4cb3e0888c940a1c3cb61d(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b935af4b7f540cbb6b063a9c37a906eaf8c3ed8781b19ea32e1836ca909b3dac(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    role_arn: typing.Optional[builtins.str] = None,
    secret_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__706925197a1b663cd9be8234e85ce2780b58d7bf71737c801e0c393104407464(
    *,
    orc_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.OrcSerDeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parquet_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ParquetSerDeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4d37eb171641c85a4fd06dfff9a42a4ac04df542059c602ae6c3ce07e369214(
    *,
    interval_in_seconds: typing.Optional[jsii.Number] = None,
    size_in_m_bs: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9743b3910a7f4b6edd05f7d4a76aa45c5a9f674a473fcf4c8c046e1d8d64cb53(
    *,
    account_url: builtins.str,
    database: builtins.str,
    role_arn: builtins.str,
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    schema: builtins.str,
    table: builtins.str,
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SnowflakeBufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    content_column_name: typing.Optional[builtins.str] = None,
    data_loading_option: typing.Optional[builtins.str] = None,
    key_passphrase: typing.Optional[builtins.str] = None,
    meta_data_column_name: typing.Optional[builtins.str] = None,
    private_key: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SnowflakeRetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
    secrets_manager_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SecretsManagerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snowflake_role_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SnowflakeRoleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snowflake_vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SnowflakeVpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7d919c23da3109305810f31f91a7020b20f997fbd66a87a4b4dfe122efff981(
    *,
    duration_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__867673ab46f448fd1867f3b74172d4939969188f736abc7f1c5c26682419368b(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    snowflake_role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5715c831de8e3fe729e9e76213a2b933810f642d09eb653534a3d23054acf0d(
    *,
    private_link_vpce_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60823c61f8aea3242c07551788af8f338bff46b6299ee9aa1d0ff6112c454ecc(
    *,
    interval_in_seconds: typing.Optional[jsii.Number] = None,
    size_in_m_bs: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be9923ea7818bcdc567ae6e06b529c44c6a3c42b59af06768977f4c55fdd20a6(
    *,
    hec_endpoint: builtins.str,
    hec_endpoint_type: builtins.str,
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SplunkBufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hec_acknowledgment_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    hec_token: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SplunkRetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
    secrets_manager_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SecretsManagerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c5cbe7244c68f12454d07974a4cae50f1d208afdbc3a96f1e2ada11e37fc412(
    *,
    duration_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac9314efc3754736d60b5e8780b56333aa2816ec35cd3e5ede526a3656454369(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ecd7f59955db0312a31e14fafedff3746c1d169b6a24f2985f6a096a09db25a(
    *,
    role_arn: builtins.str,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f4e310bf0ff2c76f9c126ea4431fb25b9b53c8ba7e0c0eacc1c934debd05a95(
    *,
    amazon_open_search_serverless_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    amazonopensearchservice_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    database_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DatabaseSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delivery_stream_encryption_configuration_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delivery_stream_name: typing.Optional[builtins.str] = None,
    delivery_stream_type: typing.Optional[builtins.str] = None,
    direct_put_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DirectPutSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elasticsearch_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    extended_s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    http_endpoint_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iceberg_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.IcebergDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_stream_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.KinesisStreamSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    msk_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.MSKSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.RedshiftDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snowflake_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SnowflakeDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    splunk_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SplunkDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c67ac54054be7496dcf923fd4756691ef492acee6f8731020e20179b0e257c8(
    *,
    logging_config: typing.Optional[ILoggingConfig] = None,
    processor: typing.Optional[IDataProcessor] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    s3_backup: typing.Optional[typing.Union[DestinationS3BackupProps, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e31b00e38ca06327867ea44e0a0f3d63eb65aaa770f96419cf713c515c231922(
    *,
    buffering_interval: typing.Optional[_Duration_4839e8c3] = None,
    buffering_size: typing.Optional[_Size_7b441c34] = None,
    compression: typing.Optional[Compression] = None,
    data_output_prefix: typing.Optional[builtins.str] = None,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    error_output_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e41ad5beb7c57e7d6a51a6e7b54af84f87429433140b71bcff2768d479fc24c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19eda2faa3921fd664688bb9d58a7766cede4c60f2944654651ac8a298dad52e(
    *,
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d0329dec95ad7ff26b8989814c21e55edb2fa91a61a992ced2d01569d06f530(
    *,
    processor_identifier: typing.Union[DataProcessorIdentifier, typing.Dict[builtins.str, typing.Any]],
    processor_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46d7f3bad270e22195a118b290c387efb2ff5c34792622c7ab288bdc3709ce43(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__824567e49e82c5e0ed6a55fe92d29f1a69f55d0bfe50df023c1b00b9faeb44b3(
    *,
    buffer_interval: typing.Optional[_Duration_4839e8c3] = None,
    buffer_size: typing.Optional[_Size_7b441c34] = None,
    retries: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__045ad458e5c2129dfab9cbc14581304a5f9f38f34ef8d143791a7e6ee60d651e(
    *,
    delivery_stream_arn: typing.Optional[builtins.str] = None,
    delivery_stream_name: typing.Optional[builtins.str] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acb39dfe9c8b47016ad51340ebf8bd9df44f24a25df01acaec0605788a0a5b85(
    *,
    destination: IDestination,
    delivery_stream_name: typing.Optional[builtins.str] = None,
    encryption: typing.Optional[StreamEncryption] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    source: typing.Optional[ISource] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4dd310df912fa42818751c79c7d5fea4583bec8e28275de2a13e058f30cb19b(
    *,
    dependables: typing.Optional[typing.Sequence[_constructs_77d1e7e8.IDependable]] = None,
    extended_s3_destination_configuration: typing.Optional[typing.Union[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14700eb876e8e0f20f42a3b1362e4b8cd4eb596f1fbaecf0e207a387e8e2247d(
    *,
    buffering_interval: typing.Optional[_Duration_4839e8c3] = None,
    buffering_size: typing.Optional[_Size_7b441c34] = None,
    compression: typing.Optional[Compression] = None,
    data_output_prefix: typing.Optional[builtins.str] = None,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    error_output_prefix: typing.Optional[builtins.str] = None,
    bucket: typing.Optional[_IBucket_42e086fd] = None,
    logging_config: typing.Optional[ILoggingConfig] = None,
    mode: typing.Optional[BackupMode] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4720a6b97c475eae9ec0d65aca8250b00f57d45f0efb2368b8df6d486162c508(
    scope: _constructs_77d1e7e8.Construct,
    *,
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2734269481cf10b40e22df40c033138f0b366868257b0867e62eb92924e9f879(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__430b83a9ce03b133eb0ca75afb61f22cb3d6eac65aafcc08346ba35beea872c2(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d98802194f172640833e51b398adf85ca294da7e2a4a6dfb45bfe99dfdb071(
    metric_name: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    color: typing.Optional[builtins.str] = None,
    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    label: typing.Optional[builtins.str] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    region: typing.Optional[builtins.str] = None,
    stack_account: typing.Optional[builtins.str] = None,
    stack_region: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
    visible: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4557c076602017c3ae1d9a7de086acd858753a2681320e75c1151baf3ad8a77(
    scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d31d061482330f398322aedbe7845244fe1c55607a37db88ea3629f702ba69b0(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc95432da9a8005268f62059d26c76ff3244e1763c675e2cf288a4edbb0235a3(
    stream: _IStream_4e2457d2,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0139dd9374d65b09aeb2cc12f10df74ef6fb54d32d3dbfc129f0e7ca2d14423(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9ef06af75a5f9424b9a83d955544e1a8c769bb828e54b77e5dcec4ddd0f9154(
    lambda_function: _IFunction_6adb0ab8,
    *,
    buffer_interval: typing.Optional[_Duration_4839e8c3] = None,
    buffer_size: typing.Optional[_Size_7b441c34] = None,
    retries: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__393c41d8ae2fe5acab13fd70fff9f4778e727adfd78b86d20820f067071490de(
    _scope: _constructs_77d1e7e8.Construct,
    *,
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2eaf455255fc260033aa24d456779f4b21172e8b4cf2c51f6355f415c9f3ccd(
    bucket: _IBucket_42e086fd,
    *,
    file_extension: typing.Optional[builtins.str] = None,
    time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
    buffering_interval: typing.Optional[_Duration_4839e8c3] = None,
    buffering_size: typing.Optional[_Size_7b441c34] = None,
    compression: typing.Optional[Compression] = None,
    data_output_prefix: typing.Optional[builtins.str] = None,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    error_output_prefix: typing.Optional[builtins.str] = None,
    logging_config: typing.Optional[ILoggingConfig] = None,
    processor: typing.Optional[IDataProcessor] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    s3_backup: typing.Optional[typing.Union[DestinationS3BackupProps, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3fdb21f9fe6d8dcaca6f65ba8cd1a376d43176607319802bd013001c8c5e9fd(
    scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04b12dc503479d22af2396c4df8d38c37536719187eef6ddd01c18b529dcbfc9(
    *,
    buffering_interval: typing.Optional[_Duration_4839e8c3] = None,
    buffering_size: typing.Optional[_Size_7b441c34] = None,
    compression: typing.Optional[Compression] = None,
    data_output_prefix: typing.Optional[builtins.str] = None,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    error_output_prefix: typing.Optional[builtins.str] = None,
    logging_config: typing.Optional[ILoggingConfig] = None,
    processor: typing.Optional[IDataProcessor] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    s3_backup: typing.Optional[typing.Union[DestinationS3BackupProps, typing.Dict[builtins.str, typing.Any]]] = None,
    file_extension: typing.Optional[builtins.str] = None,
    time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efb44f4c68ce5ed338b1cadc1095db8f6b1ea6c2478ee68c07bb0fa95cecdf47(
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c5be371024241f9b37d47dc30b79a0d54ad9453eb90d21cc0f6c880f2e4fb91(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination: IDestination,
    delivery_stream_name: typing.Optional[builtins.str] = None,
    encryption: typing.Optional[StreamEncryption] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    source: typing.Optional[ISource] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1ce0063f18826b4ee51e0d895cc5452b1439ff1e769a5b248178badffad6011(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    delivery_stream_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60d49cb1de4cae1a83d89ae7d419d2e7a17f1c8a25478897973ca006cf1f5066(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    delivery_stream_arn: typing.Optional[builtins.str] = None,
    delivery_stream_name: typing.Optional[builtins.str] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__457e8328a163250ba61b71d2ce676a68d801ac8467c715e8ba511357cb60c507(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    delivery_stream_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d29967317f0315691f87af41c6bab889af970cdd0860933427170179ccabb1b(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31fc61b3576a2a9576300f38d0cde9d0c42fcad47d437aa8ef160d5016007243(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86f3b1e63c4046b14a20d8f095529962a56cb82f03a0f9a310b5c1b707bc0f5f(
    metric_name: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    color: typing.Optional[builtins.str] = None,
    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    label: typing.Optional[builtins.str] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    region: typing.Optional[builtins.str] = None,
    stack_account: typing.Optional[builtins.str] = None,
    stack_region: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
    visible: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba11d69a3d91c8a6ba63c6ed55a7bbd149c317325863da3c41ebf373cf256b7c(
    log_group: typing.Optional[_ILogGroup_3c4fa718] = None,
) -> None:
    """Type checking stubs"""
    pass
