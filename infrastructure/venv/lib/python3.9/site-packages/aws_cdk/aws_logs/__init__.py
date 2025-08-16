r'''
# Amazon CloudWatch Logs Construct Library

This library supplies constructs for working with CloudWatch Logs.

## Log Groups/Streams

The basic unit of CloudWatch is a *Log Group*. Every log group typically has the
same kind of data logged to it, in the same format. If there are multiple
applications or services logging into the Log Group, each of them creates a new
*Log Stream*.

Every log operation creates a "log event", which can consist of a simple string
or a single-line JSON object. JSON objects have the advantage that they afford
more filtering abilities (see below).

The only configurable attribute for log streams is the retention period, which
configures after how much time the events in the log stream expire and are
deleted.

The default retention period if not supplied is 2 years, but it can be set to
one of the values in the `RetentionDays` enum to configure a different
retention period (including infinite retention).

```python
# Configure log group for short retention
log_group = LogGroup(stack, "LogGroup",
    retention=RetentionDays.ONE_WEEK
)# Configure log group for infinite retention
log_group = LogGroup(stack, "LogGroup",
    retention=Infinity
)
```

## LogRetention

The `LogRetention` construct is a way to control the retention period of log groups that are created outside of the CDK. The construct is usually
used on log groups that are auto created by AWS services, such as [AWS
lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html).

This is implemented using a [CloudFormation custom
resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html)
which pre-creates the log group if it doesn't exist, and sets the specified log retention period (never expire, by default).

By default, the log group will be created in the same region as the stack. The `logGroupRegion` property can be used to configure
log groups in other regions. This is typically useful when controlling retention for log groups auto-created by global services that
publish their log group to a specific region, such as AWS Chatbot creating a log group in `us-east-1`.

By default, the log group created by LogRetention will be retained after the stack is deleted. If the RemovalPolicy is set to DESTROY, then the log group will be deleted when the stack is deleted.

## Log Group Class

CloudWatch Logs offers two classes of log groups:

1. The CloudWatch Logs Standard log class is a full-featured option for logs that require real-time monitoring or logs that you access frequently.
2. The CloudWatch Logs Infrequent Access log class is a new log class that you can use to cost-effectively consolidate your logs. This log class offers a subset of CloudWatch Logs capabilities including managed ingestion, storage, cross-account log analytics, and encryption with a lower ingestion price per GB. The Infrequent Access log class is ideal for ad-hoc querying and after-the-fact forensic analysis on infrequently accessed logs.

For more details please check: [log group class documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html)

## Resource Policy

CloudWatch Resource Policies allow other AWS services or IAM Principals to put log events into the log groups.
A resource policy is automatically created when `addToResourcePolicy` is called on the LogGroup for the first time:

```python
log_group = logs.LogGroup(self, "LogGroup")
log_group.add_to_resource_policy(iam.PolicyStatement(
    actions=["logs:CreateLogStream", "logs:PutLogEvents"],
    principals=[iam.ServicePrincipal("es.amazonaws.com")],
    resources=[log_group.log_group_arn]
))
```

Or more conveniently, write permissions to the log group can be granted as follows which gives same result as in the above example.

```python
log_group = logs.LogGroup(self, "LogGroup")
log_group.grant_write(iam.ServicePrincipal("es.amazonaws.com"))
```

Similarly, read permissions can be granted to the log group as follows.

```python
log_group = logs.LogGroup(self, "LogGroup")
log_group.grant_read(iam.ServicePrincipal("es.amazonaws.com"))
```

Be aware that any ARNs or tokenized values passed to the resource policy will be converted into AWS Account IDs.
This is because CloudWatch Logs Resource Policies do not accept ARNs as principals, but they do accept
Account ID strings. Non-ARN principals, like Service principals or Any principals, are accepted by CloudWatch.

## Encrypting Log Groups

By default, log group data is always encrypted in CloudWatch Logs. You have the
option to encrypt log group data using a AWS KMS customer master key (CMK) should
you not wish to use the default AWS encryption. Keep in mind that if you decide to
encrypt a log group, any service or IAM identity that needs to read the encrypted
log streams in the future will require the same CMK to decrypt the data.

Here's a simple example of creating an encrypted Log Group using a KMS CMK.

```python
import aws_cdk.aws_kms as kms


logs.LogGroup(self, "LogGroup",
    encryption_key=kms.Key(self, "Key")
)
```

See the AWS documentation for more detailed information about [encrypting CloudWatch
Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html).

## Subscriptions and Destinations

Log events matching a particular filter can be sent to either a Lambda function
or a Kinesis stream.

If the Kinesis stream lives in a different account, a `CrossAccountDestination`
object needs to be added in the destination account which will act as a proxy
for the remote Kinesis stream. This object is automatically created for you
if you use the CDK Kinesis library.

Create a `SubscriptionFilter`, initialize it with an appropriate `Pattern` (see
below) and supply the intended destination:

```python
import aws_cdk.aws_logs_destinations as destinations

# fn: lambda.Function
# log_group: logs.LogGroup


logs.SubscriptionFilter(self, "Subscription",
    log_group=log_group,
    destination=destinations.LambdaDestination(fn),
    filter_pattern=logs.FilterPattern.all_terms("ERROR", "MainThread"),
    filter_name="ErrorInMainThread"
)
```

When you use `KinesisDestination`, you can choose the method used to
distribute log data to the destination by setting the `distribution` property.

```python
import aws_cdk.aws_logs_destinations as destinations
import aws_cdk.aws_kinesis as kinesis

# stream: kinesis.Stream
# log_group: logs.LogGroup


logs.SubscriptionFilter(self, "Subscription",
    log_group=log_group,
    destination=destinations.KinesisDestination(stream),
    filter_pattern=logs.FilterPattern.all_terms("ERROR", "MainThread"),
    filter_name="ErrorInMainThread",
    distribution=logs.Distribution.RANDOM
)
```

When you use `FirehoseDestination`, you can choose the method used to
distribute log data to the destination by setting the `distribution` property.

```python
import aws_cdk.aws_logs_destinations as destinations
import aws_cdk.aws_kinesisfirehose as firehose

# delivery_stream: firehose.IDeliveryStream
# log_group: logs.LogGroup


logs.SubscriptionFilter(self, "Subscription",
    log_group=log_group,
    destination=destinations.FirehoseDestination(delivery_stream),
    filter_pattern=logs.FilterPattern.all_events()
)
```

## Metric Filters

CloudWatch Logs can extract and emit metrics based on a textual log stream.
Depending on your needs, this may be a more convenient way of generating metrics
for you application than making calls to CloudWatch Metrics yourself.

A `MetricFilter` either emits a fixed number every time it sees a log event
matching a particular pattern (see below), or extracts a number from the log
event and uses that as the metric value.

Example:

```python
MetricFilter(self, "MetricFilter",
    log_group=log_group,
    metric_namespace="MyApp",
    metric_name="Latency",
    filter_pattern=FilterPattern.all(
        FilterPattern.exists("$.latency"),
        FilterPattern.regex_value("$.message", "=", "bind: address already in use")),
    metric_value="$.latency"
)
```

Remember that if you want to use a value from the log event as the metric value,
you must mention it in your pattern somewhere.

A very simple MetricFilter can be created by using the `logGroup.extractMetric()`
helper function:

```python
# log_group: logs.LogGroup

log_group.extract_metric("$.jsonField", "Namespace", "MetricName")
```

Will extract the value of `jsonField` wherever it occurs in JSON-structured
log records in the LogGroup, and emit them to CloudWatch Metrics under
the name `Namespace/MetricName`.

### Exposing Metric on a Metric Filter

You can expose a metric on a metric filter by calling the `MetricFilter.metric()` API.
This has a default of `statistic = 'avg'` if the statistic is not set in the `props`.

```python
# log_group: logs.LogGroup

mf = logs.MetricFilter(self, "MetricFilter",
    log_group=log_group,
    metric_namespace="MyApp",
    metric_name="Latency",
    filter_pattern=logs.FilterPattern.exists("$.latency"),
    metric_value="$.latency",
    dimensions={
        "ErrorCode": "$.errorCode"
    },
    unit=cloudwatch.Unit.MILLISECONDS
)

# expose a metric from the metric filter
metric = mf.metric()

# you can use the metric to create a new alarm
cloudwatch.Alarm(self, "alarm from metric filter",
    metric=metric,
    threshold=100,
    evaluation_periods=2
)
```

### Metrics for IncomingLogs and IncomingBytes

Metric methods have been defined for IncomingLogs and IncomingBytes within LogGroups. These metrics allow for the creation of alarms on log ingestion, ensuring that the log ingestion process is functioning correctly.

To define an alarm based on these metrics, you can use the following template:

```python
log_group = logs.LogGroup(self, "MyLogGroup")
incoming_events_metric = log_group.metric_incoming_log_events()
cloudwatch.Alarm(self, "HighLogVolumeAlarm",
    metric=incoming_events_metric,
    threshold=1000,
    evaluation_periods=1
)
```

```python
log_group = logs.LogGroup(self, "MyLogGroup")
incoming_bytes_metric = log_group.metric_incoming_bytes()
cloudwatch.Alarm(self, "HighDataVolumeAlarm",
    metric=incoming_bytes_metric,
    threshold=5000000,  # 5 MB
    evaluation_periods=1
)
```

## Patterns

Patterns describe which log events match a subscription or metric filter. There
are three types of patterns:

* Text patterns
* JSON patterns
* Space-delimited table patterns

All patterns are constructed by using static functions on the `FilterPattern`
class.

In addition to the patterns above, the following special patterns exist:

* `FilterPattern.allEvents()`: matches all log events.
* `FilterPattern.literal(string)`: if you already know what pattern expression to
  use, this function takes a string and will use that as the log pattern. For
  more information, see the [Filter and Pattern
  Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).

### Text Patterns

Text patterns match if the literal strings appear in the text form of the log
line.

* `FilterPattern.allTerms(term, term, ...)`: matches if all of the given terms
  (substrings) appear in the log event.
* `FilterPattern.anyTerm(term, term, ...)`: matches if all of the given terms
  (substrings) appear in the log event.
* `FilterPattern.anyTermGroup([term, term, ...], [term, term, ...], ...)`: matches if
  all of the terms in any of the groups (specified as arrays) matches. This is
  an OR match.

Examples:

```python
# Search for lines that contain both "ERROR" and "MainThread"
pattern1 = logs.FilterPattern.all_terms("ERROR", "MainThread")

# Search for lines that either contain both "ERROR" and "MainThread", or
# both "WARN" and "Deadlock".
pattern2 = logs.FilterPattern.any_term_group(["ERROR", "MainThread"], ["WARN", "Deadlock"])
```

## JSON Patterns

JSON patterns apply if the log event is the JSON representation of an object
(without any other characters, so it cannot include a prefix such as timestamp
or log level). JSON patterns can make comparisons on the values inside the
fields.

* **Strings**: the comparison operators allowed for strings are `=` and `!=`.
  String values can start or end with a `*` wildcard.
* **Numbers**: the comparison operators allowed for numbers are `=`, `!=`,
  `<`, `<=`, `>`, `>=`.

Fields in the JSON structure are identified by identifier the complete object as `$`
and then descending into it, such as `$.field` or `$.list[0].field`.

* `FilterPattern.stringValue(field, comparison, string)`: matches if the given
  field compares as indicated with the given string value.
* `FilterPattern.regexValue(field, comparison, string)`: matches if the given
  field compares as indicated with the given regex pattern.
* `FilterPattern.numberValue(field, comparison, number)`: matches if the given
  field compares as indicated with the given numerical value.
* `FilterPattern.isNull(field)`: matches if the given field exists and has the
  value `null`.
* `FilterPattern.notExists(field)`: matches if the given field is not in the JSON
  structure.
* `FilterPattern.exists(field)`: matches if the given field is in the JSON
  structure.
* `FilterPattern.booleanValue(field, boolean)`: matches if the given field
  is exactly the given boolean value.
* `FilterPattern.all(jsonPattern, jsonPattern, ...)`: matches if all of the
  given JSON patterns match. This makes an AND combination of the given
  patterns.
* `FilterPattern.any(jsonPattern, jsonPattern, ...)`: matches if any of the
  given JSON patterns match. This makes an OR combination of the given
  patterns.

Example:

```python
# Search for all events where the component field is equal to
# "HttpServer" and either error is true or the latency is higher
# than 1000.
pattern = logs.FilterPattern.all(
    logs.FilterPattern.string_value("$.component", "=", "HttpServer"),
    logs.FilterPattern.any(
        logs.FilterPattern.boolean_value("$.error", True),
        logs.FilterPattern.number_value("$.latency", ">", 1000)),
    logs.FilterPattern.regex_value("$.message", "=", "bind address already in use"))
```

## Space-delimited table patterns

If the log events are rows of a space-delimited table, this pattern can be used
to identify the columns in that structure and add conditions on any of them. The
canonical example where you would apply this type of pattern is Apache server
logs.

Text that is surrounded by `"..."` quotes or `[...]` square brackets will
be treated as one column.

* `FilterPattern.spaceDelimited(column, column, ...)`: construct a
  `SpaceDelimitedTextPattern` object with the indicated columns. The columns
  map one-by-one the columns found in the log event. The string `"..."` may
  be used to specify an arbitrary number of unnamed columns anywhere in the
  name list (but may only be specified once).

After constructing a `SpaceDelimitedTextPattern`, you can use the following
two members to add restrictions:

* `pattern.whereString(field, comparison, string)`: add a string condition.
  The rules are the same as for JSON patterns.
* `pattern.whereNumber(field, comparison, number)`: add a numerical condition.
  The rules are the same as for JSON patterns.

Multiple restrictions can be added on the same column; they must all apply.

Example:

```python
# Search for all events where the component is "HttpServer" and the
# result code is not equal to 200.
pattern = logs.FilterPattern.space_delimited("time", "component", "...", "result_code", "latency").where_string("component", "=", "HttpServer").where_number("result_code", "!=", 200)
```

## Logs Insights Query Definition

Creates a query definition for CloudWatch Logs Insights.

Example:

```python
logs.QueryDefinition(self, "QueryDefinition",
    query_definition_name="MyQuery",
    query_string=logs.QueryString(
        fields=["@timestamp", "@message"],
        parse_statements=["@message \"[*] *\" as loggingType, loggingMessage", "@message \"<*>: *\" as differentLoggingType, differentLoggingMessage"
        ],
        filter_statements=["loggingType = \"ERROR\"", "loggingMessage = \"A very strange error occurred!\""
        ],
        stats_statements=["count(loggingMessage) as loggingErrors", "count(differentLoggingMessage) as differentLoggingErrors"
        ],
        sort="@timestamp desc",
        limit=20
    )
)
```

## Data Protection Policy

Creates a data protection policy and assigns it to the log group. A data protection policy can help safeguard sensitive data that's ingested by the log group by auditing and masking the sensitive log data. When a user who does not have permission to view masked data views a log event that includes masked data, the sensitive data is replaced by asterisks.

For more information, see [Protect sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html).

For a list of types of managed identifiers that can be audited and masked, see [Types of data that you can protect](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/protect-sensitive-log-data-types.html).

If a new identifier is supported but not yet in the `DataIdentifiers` enum, the name of the identifier can be supplied as `name` in the constructor instead.

To add a custom data identifier, supply a custom `name` and `regex` to the `CustomDataIdentifiers` constructor.
For more information on custom data identifiers, see [Custom data identifiers](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL-custom-data-identifiers.html).

Each policy may consist of a log group, S3 bucket, and/or Firehose delivery stream audit destination.

Example:

```python
import aws_cdk.aws_kinesisfirehose as firehose


log_group_destination = logs.LogGroup(self, "LogGroupLambdaAudit",
    log_group_name="auditDestinationForCDK"
)

bucket = s3.Bucket(self, "audit-bucket")
s3_destination = firehose.S3Bucket(bucket)

delivery_stream = firehose.DeliveryStream(self, "Delivery Stream",
    destination=s3_destination
)

data_protection_policy = logs.DataProtectionPolicy(
    name="data protection policy",
    description="policy description",
    identifiers=[logs.DataIdentifier.DRIVERSLICENSE_US,  # managed data identifier
        logs.DataIdentifier("EmailAddress"),  # forward compatibility for new managed data identifiers
        logs.CustomDataIdentifier("EmployeeId", "EmployeeId-\\d{9}")
    ],  # custom data identifier
    log_group_audit_destination=log_group_destination,
    s3_bucket_audit_destination=bucket,
    delivery_stream_name_audit_destination=delivery_stream.delivery_stream_name
)

logs.LogGroup(self, "LogGroupLambda",
    log_group_name="cdkIntegLogGroup",
    data_protection_policy=data_protection_policy
)
```

## Field Index Policies

Creates or updates a field index policy for the specified log group. You can use field index policies to create field indexes on fields found in log events in the log group. Creating field indexes lowers the costs for CloudWatch Logs Insights queries that reference those field indexes, because these queries attempt to skip the processing of log events that are known to not match the indexed field. Good fields to index are fields that you often need to query for and fields that have high cardinality of values.

For more information, see [Create field indexes to improve query performance and reduce costs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html).

Only log groups in the Standard log class support field index policies.
Currently, this array supports only one field index policy object.

Example:

```python
field_index_policy = logs.FieldIndexPolicy(
    fields=["Operation", "RequestId"]
)

logs.LogGroup(self, "LogGroup",
    log_group_name="cdkIntegLogGroup",
    field_index_policies=[field_index_policy]
)
```

## Transformer

A log transformer enables transforming log events into a different format, making them easier
to process and analyze. You can transform logs from different sources into standardized formats
that contain relevant, source-specific information. Transformations are performed at the time of log ingestion.
Transformers support several types of processors which can be chained into a processing pipeline (subject to some restrictions, see [Usage Limits](#usage-limits)).

### Processor Types

1. **Parser Processors**: Parse string log events into structured log events. These are configurable parsers created using `ParserProcessor`, and support conversion to a format like Json, extracting fields from CSV input, converting vended sources to [OCSF](https://schema.ocsf.io/1.1.0/) format, regex parsing using Grok patterns or key-value parsing. Refer [configurable parsers](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-Configurable) for more examples.
2. **Vended Log Parsers**: Parse log events from vended sources into structured log events. These are created using `VendedLogParser`, and support conversion from sources such as AWS WAF, PostGres, Route53, CloudFront and VPC. These parsers are not configurable, meaning these can be added to the pipeline but do not accept any properties or configurations. Refer [vended log parsers](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-BuiltIn) for more examples.
3. **String Mutators**: Perform operations on string values in a field of a log event and are created using `StringMutatorProcessor`. These can be used to format string values in the log event such as changing case, removing trailing whitespaces or extracting values from a string field by splitting the string or regex backreferences. Refer [string mutators](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-StringMutate) for more examples.
4. **JSON Mutators**: Perform operation on JSON log events and are created using `JsonMutatorProcessor`. These processors can be used to enrich log events by adding new fields, deleting, moving, renaming fields, copying values to other fields or converting a list of key-value pairs to a map. Refer [JSON mutators](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-JSONMutate) for more examples.
5. **Data Converters**: Convert the data into different formats and are created using `DataConverterProcessor`. These can be used to convert values in a field to datatypes such as integers, string, double and boolean or to convert dates and times to different formats. Refer [datatype processors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-Datatype) for more examples.

### Usage Limits

* A transformer can have a maximum of 20 processors
* At least one parser-type processor is required
* Maximum of 5 parser-type processors allowed
* AWS vended log parser (if used) must be the first processor
* Only one parseToOcsf processor, one grok processor, one addKeys processor, and one copyValue processor allowed per transformer
* Transformers can only be used with log groups in the Standard log class

Example:

```python
# Create a log group
log_group = logs.LogGroup(self, "MyLogGroup")

# Create a JSON parser processor
json_parser = logs.ParserProcessor(
    type=logs.ParserProcessorType.JSON
)

# Create a processor to add keys
add_keys_processor = logs.JsonMutatorProcessor(
    type=logs.JsonMutatorType.ADD_KEYS,
    add_keys_options=logs.AddKeysProperty(
        entries=[logs.AddKeyEntryProperty(
            key="metadata.transformed_in",
            value="CloudWatchLogs"
        )]
    )
)

# Create a transformer with these processors
logs.Transformer(self, "Transformer",
    transformer_name="MyTransformer",
    log_group=log_group,
    transformer_config=[json_parser, add_keys_processor]
)
```

For more details on CloudWatch Logs transformation processors, refer to the [AWS documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html).

## Notes

Be aware that Log Group ARNs will always have the string `:*` appended to
them, to match the behavior of [the CloudFormation `AWS::Logs::LogGroup`
resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#aws-resource-logs-loggroup-return-values).
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
    ITaggableV2 as _ITaggableV2_4e6798f8,
    RemovalPolicy as _RemovalPolicy_9f93c814,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_cloudwatch import (
    Metric as _Metric_e396a4dc,
    MetricOptions as _MetricOptions_1788b62f,
    Unit as _Unit_61bc6f70,
)
from ..aws_iam import (
    AddToResourcePolicyResult as _AddToResourcePolicyResult_1d0a53ad,
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IResourceWithPolicy as _IResourceWithPolicy_720d64fc,
    IRole as _IRole_235f5d8e,
    PolicyDocument as _PolicyDocument_3ac34393,
    PolicyStatement as _PolicyStatement_0fe33853,
)
from ..aws_kms import IKey as _IKey_5f11635f
from ..aws_s3 import IBucket as _IBucket_42e086fd


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.AddKeyEntryProperty",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "value": "value",
        "overwrite_if_exists": "overwriteIfExists",
    },
)
class AddKeyEntryProperty:
    def __init__(
        self,
        *,
        key: builtins.str,
        value: builtins.str,
        overwrite_if_exists: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''This object defines one key that will be added with the addKeys processor.

        :param key: The key of the new entry to be added to the log event.
        :param value: The value of the new entry to be added to the log event.
        :param overwrite_if_exists: Specifies whether to overwrite the value if the key already exists. Default: false

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            add_key_entry_property = logs.AddKeyEntryProperty(
                key="key",
                value="value",
            
                # the properties below are optional
                overwrite_if_exists=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8699e0d43c18a23430a2882c1d81b6da80014a083961d49ed805738cd51f592a)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument overwrite_if_exists", value=overwrite_if_exists, expected_type=type_hints["overwrite_if_exists"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }
        if overwrite_if_exists is not None:
            self._values["overwrite_if_exists"] = overwrite_if_exists

    @builtins.property
    def key(self) -> builtins.str:
        '''The key of the new entry to be added to the log event.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of the new entry to be added to the log event.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def overwrite_if_exists(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether to overwrite the value if the key already exists.

        :default: false
        '''
        result = self._values.get("overwrite_if_exists")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddKeyEntryProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.AddKeysProperty",
    jsii_struct_bases=[],
    name_mapping={"entries": "entries"},
)
class AddKeysProperty:
    def __init__(
        self,
        *,
        entries: typing.Sequence[typing.Union[AddKeyEntryProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''This processor adds new key-value pairs to the log event.

        For more information about this processor including examples, see addKeys in the CloudWatch Logs User Guide.

        :param entries: An array of objects, where each object contains information about one key to add to the log event.

        :exampleMetadata: infused

        Example::

            # Create a log group
            log_group = logs.LogGroup(self, "MyLogGroup")
            
            # Create a JSON parser processor
            json_parser = logs.ParserProcessor(
                type=logs.ParserProcessorType.JSON
            )
            
            # Create a processor to add keys
            add_keys_processor = logs.JsonMutatorProcessor(
                type=logs.JsonMutatorType.ADD_KEYS,
                add_keys_options=logs.AddKeysProperty(
                    entries=[logs.AddKeyEntryProperty(
                        key="metadata.transformed_in",
                        value="CloudWatchLogs"
                    )]
                )
            )
            
            # Create a transformer with these processors
            logs.Transformer(self, "Transformer",
                transformer_name="MyTransformer",
                log_group=log_group,
                transformer_config=[json_parser, add_keys_processor]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1836386a927cf6c05c8ee3f32e141f2a818ce87d4aba162406325e50620c0c9b)
            check_type(argname="argument entries", value=entries, expected_type=type_hints["entries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entries": entries,
        }

    @builtins.property
    def entries(self) -> typing.List[AddKeyEntryProperty]:
        '''An array of objects, where each object contains information about one key to add to the log event.'''
        result = self._values.get("entries")
        assert result is not None, "Required property 'entries' is missing"
        return typing.cast(typing.List[AddKeyEntryProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddKeysProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.BaseProcessorProps",
    jsii_struct_bases=[],
    name_mapping={},
)
class BaseProcessorProps:
    def __init__(self) -> None:
        '''Base properties for all processor types.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            base_processor_props = logs.BaseProcessorProps()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseProcessorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAccountPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnAccountPolicy",
):
    '''Creates or updates an account-level data protection policy or subscription filter policy that applies to all log groups or a subset of log groups in the account.

    *Data protection policy*

    A data protection policy can help safeguard sensitive data that's ingested by your log groups by auditing and masking the sensitive log data. Each account can have only one account-level data protection policy.
    .. epigraph::

       Sensitive data is detected and masked when it is ingested into a log group. When you set a data protection policy, log events ingested into the log groups before that time are not masked.

    If you create a data protection policy for your whole account, it applies to both existing log groups and all log groups that are created later in this account. The account policy is applied to existing log groups with eventual consistency. It might take up to 5 minutes before sensitive data in existing log groups begins to be masked.

    By default, when a user views a log event that includes masked data, the sensitive data is replaced by asterisks. A user who has the ``logs:Unmask`` permission can use a `GetLogEvents <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.html>`_ or `FilterLogEvents <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.html>`_ operation with the ``unmask`` parameter set to ``true`` to view the unmasked log events. Users with the ``logs:Unmask`` can also view unmasked data in the CloudWatch Logs console by running a CloudWatch Logs Insights query with the ``unmask`` query command.

    For more information, including a list of types of data that can be audited and masked, see `Protect sensitive log data with masking <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html>`_ .

    To create an account-level policy, you must be signed on with the ``logs:PutDataProtectionPolicy`` and ``logs:PutAccountPolicy`` permissions.

    An account-level policy applies to all log groups in the account. You can also create a data protection policy that applies to just one log group. If a log group has its own data protection policy and the account also has an account-level data protection policy, then the two policies are cumulative. Any sensitive term specified in either policy is masked.

    *Subscription filter policy*

    A subscription filter policy sets up a real-time feed of log events from CloudWatch Logs to other AWS services. Account-level subscription filter policies apply to both existing log groups and log groups that are created later in this account. Supported destinations are Kinesis Data Streams , Firehose , and Lambda . When log events are sent to the receiving service, they are Base64 encoded and compressed with the GZIP format.

    The following destinations are supported for subscription filters:

    - An Kinesis Data Streams data stream in the same account as the subscription policy, for same-account delivery.
    - An Firehose data stream in the same account as the subscription policy, for same-account delivery.
    - A Lambda function in the same account as the subscription policy, for same-account delivery.
    - A logical destination in a different account created with `PutDestination <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.html>`_ , for cross-account delivery. Kinesis Data Streams and Firehose are supported as logical destinations.

    Each account can have one account-level subscription filter policy. If you are updating an existing filter, you must specify the correct name in ``PolicyName`` . To perform a ``PutAccountPolicy`` subscription filter operation for any destination except a Lambda function, you must also have the ``iam:PassRole`` permission.

    *Field index policy*

    You can use field index policies to create indexes on fields found in log events in the log group. Creating field indexes lowers the scan volume for CloudWatch Logs Insights queries that reference those fields, because these queries attempt to skip the processing of log events that are known to not match the indexed field. Good fields to index are fields that you often need to query for. Common examples of indexes include request ID, session ID, user IDs, or instance IDs. For more information, see `Create field indexes to improve query performance and reduce costs <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html>`_

    For example, suppose you have created a field index for ``requestId`` . Then, any CloudWatch Logs Insights query on that log group that includes ``requestId = *value*`` or ``requestId IN [ *value* , *value* , ...]`` will attempt to process only the log events where the indexed field matches the specified value.

    Matches of log events to the names of indexed fields are case-sensitive. For example, an indexed field of ``RequestId`` won't match a log event containing ``requestId`` .

    You can have one account-level field index policy that applies to all log groups in the account. Or you can create as many as 20 account-level field index policies that are each scoped to a subset of log groups with the ``SelectionCriteria`` parameter. If you have multiple account-level index policies with selection criteria, no two of them can use the same or overlapping log group name prefixes. For example, if you have one policy filtered to log groups that start with ``my-log`` , you can't have another field index policy filtered to ``my-logpprod`` or ``my-logging`` .

    *Transformer policy*

    A *log transformer policy* transforms ingested log events into a different format, making them easier for you to process and analyze. You can also transform logs from different sources into standardized formats that contain relevant, source-specific information. After you have created a transformer, CloudWatch Logs performs this transformation at the time of log ingestion. You can then refer to the transformed versions of the logs during operations such as querying with CloudWatch Logs Insights or creating metric filters or subscription filters.

    You can also use a transformer to copy metadata from metadata keys into the log events themselves. This metadata can include log group name, log stream name, account ID and Region.

    A transformer for a log group is a series of processors, where each processor applies one type of transformation to the log events ingested into this log group. For more information about the available processors to use in a transformer, see `Processors that you can use <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-Processors>`_ .

    Having log events in standardized format enables visibility across your applications for your log analysis, reporting, and alarming needs. CloudWatch Logs provides transformation for common log types with out-of-the-box transformation templates for major AWS log sources such as VPC flow logs, Lambda , and Amazon RDS . You can use pre-built transformation templates or create custom transformation policies.

    You can create transformers only for the log groups in the Standard log class.

    You can have one account-level transformer policy that applies to all log groups in the account. Or you can create as many as 20 account-level transformer policies that are each scoped to a subset of log groups with the ``selectionCriteria`` parameter. If you have multiple account-level transformer policies with selection criteria, no two of them can use the same or overlapping log group name prefixes. For example, if you have one policy filtered to log groups that start with ``my-log`` , you can't have another field index policy filtered to ``my-logpprod`` or ``my-logging`` .

    You can also set up a transformer at the log-group level. For more information, see `AWS::Logs::Transformer <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-transformer.html>`_ . If there is both a log-group level transformer created with ``PutTransformer`` and an account-level transformer that could apply to the same log group, the log group uses only the log-group level transformer. It ignores the account-level transformer.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html
    :cloudformationResource: AWS::Logs::AccountPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_account_policy = logs.CfnAccountPolicy(self, "MyCfnAccountPolicy",
            policy_document="policyDocument",
            policy_name="policyName",
            policy_type="policyType",
        
            # the properties below are optional
            scope="scope",
            selection_criteria="selectionCriteria"
        )
    '''

    def __init__(
        self,
        scope_: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_document: builtins.str,
        policy_name: builtins.str,
        policy_type: builtins.str,
        scope: typing.Optional[builtins.str] = None,
        selection_criteria: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope_: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy_document: Specify the policy, in JSON. *Data protection policy* A data protection policy must include two JSON blocks: - The first block must include both a ``DataIdentifer`` array and an ``Operation`` property with an ``Audit`` action. The ``DataIdentifer`` array lists the types of sensitive data that you want to mask. For more information about the available options, see `Types of data that you can mask <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-types.html>`_ . The ``Operation`` property with an ``Audit`` action is required to find the sensitive data terms. This ``Audit`` action must contain a ``FindingsDestination`` object. You can optionally use that ``FindingsDestination`` object to list one or more destinations to send audit findings to. If you specify destinations such as log groups, Firehose streams, and S3 buckets, they must already exist. - The second block must include both a ``DataIdentifer`` array and an ``Operation`` property with an ``Deidentify`` action. The ``DataIdentifer`` array must exactly match the ``DataIdentifer`` array in the first block of the policy. The ``Operation`` property with the ``Deidentify`` action is what actually masks the data, and it must contain the ``"MaskConfig": {}`` object. The ``"MaskConfig": {}`` object must be empty. .. epigraph:: The contents of the two ``DataIdentifer`` arrays must match exactly. In addition to the two JSON blocks, the ``policyDocument`` can also include ``Name`` , ``Description`` , and ``Version`` fields. The ``Name`` is different than the operation's ``policyName`` parameter, and is used as a dimension when CloudWatch Logs reports audit findings metrics to CloudWatch . The JSON specified in ``policyDocument`` can be up to 30,720 characters long. *Subscription filter policy* A subscription filter policy can include the following attributes in a JSON block: - *DestinationArn* The ARN of the destination to deliver log events to. Supported destinations are: - An Kinesis Data Streams data stream in the same account as the subscription policy, for same-account delivery. - An Firehose data stream in the same account as the subscription policy, for same-account delivery. - A Lambda function in the same account as the subscription policy, for same-account delivery. - A logical destination in a different account created with `PutDestination <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.html>`_ , for cross-account delivery. Kinesis Data Streams and Firehose are supported as logical destinations. - *RoleArn* The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery. - *FilterPattern* A filter pattern for subscribing to a filtered stream of log events. - *Distribution* The method used to distribute log data to the destination. By default, log data is grouped by log stream, but the grouping can be set to ``Random`` for a more even distribution. This property is only applicable when the destination is an Kinesis Data Streams data stream. *Field index policy* A field index filter policy can include the following attribute in a JSON block: - *Fields* The array of field indexes to create. The following is an example of an index policy document that creates two indexes, ``RequestId`` and ``TransactionId`` . ``"policyDocument": "{ \\"Fields\\": [ \\"RequestId\\", \\"TransactionId\\" ] }"`` *Transformer policy* A transformer policy must include one JSON block with the array of processors and their configurations. For more information about available processors, see `Processors that you can use <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-Processors>`_ .
        :param policy_name: A name for the policy. This must be unique within the account.
        :param policy_type: The type of policy that you're creating or updating.
        :param scope: Currently the only valid value for this parameter is ``ALL`` , which specifies that the policy applies to all log groups in the account. If you omit this parameter, the default of ``ALL`` is used. To scope down a subscription filter policy to a subset of log groups, use the ``SelectionCriteria`` parameter.
        :param selection_criteria: Use this parameter to apply the new policy to a subset of log groups in the account. You need to specify ``SelectionCriteria`` only when you specify ``SUBSCRIPTION_FILTER_POLICY`` , ``FIELD_INDEX_POLICY`` or ``TRANSFORMER_POLICY`` for ``PolicyType`` . If ``PolicyType`` is ``SUBSCRIPTION_FILTER_POLICY`` , the only supported ``SelectionCriteria`` filter is ``LogGroupName NOT IN []`` If ``PolicyType`` is ``FIELD_INDEX_POLICY`` or ``TRANSFORMER_POLICY`` , the only supported ``SelectionCriteria`` filter is ``LogGroupNamePrefix`` The ``SelectionCriteria`` string can be up to 25KB in length. The length is determined by using its UTF-8 bytes. Using the ``SelectionCriteria`` parameter with ``SUBSCRIPTION_FILTER_POLICY`` is useful to help prevent infinite loops. For more information, see `Log recursion prevention <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions-recursion-prevention.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__125a77dd271c26d92d39f5fc5e47e588668423ade67a45afc5817e4df1ee8dd0)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccountPolicyProps(
            policy_document=policy_document,
            policy_name=policy_name,
            policy_type=policy_type,
            scope=scope,
            selection_criteria=selection_criteria,
        )

        jsii.create(self.__class__, self, [scope_, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebfd4fb8cf24056dd4dacb27f135740e6f55ee47d01767451cebf21c25f0837a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9fa52c452e9fe5605a874b3dd89e31ad16dc4f246300b4319af792307b4ae876)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAccountId")
    def attr_account_id(self) -> builtins.str:
        '''The account ID of the account where this policy was created.

        For example, ``123456789012`` .

        :cloudformationAttribute: AccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccountId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> builtins.str:
        '''Specify the policy, in JSON.'''
        return typing.cast(builtins.str, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c653a261ed47c5ebab7b21521ba00f1e039f43a3aee30163835cda4b9b741be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''A name for the policy.'''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a3c39fb59cb9806cbee8cf38c347eab7bc33fee8e2148f96faae887592ab14c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policyType")
    def policy_type(self) -> builtins.str:
        '''The type of policy that you're creating or updating.'''
        return typing.cast(builtins.str, jsii.get(self, "policyType"))

    @policy_type.setter
    def policy_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6152ad747f0f8c8124fd42f55dd6679b842c8faa8ef76cc08b3c59d43df9e9c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> typing.Optional[builtins.str]:
        '''Currently the only valid value for this parameter is ``ALL`` , which specifies that the policy applies to all log groups in the account.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a2b34c27c4f47efc3559774d8625b4374c145ac113ac7b65b32dbafd795a627)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="selectionCriteria")
    def selection_criteria(self) -> typing.Optional[builtins.str]:
        '''Use this parameter to apply the new policy to a subset of log groups in the account.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectionCriteria"))

    @selection_criteria.setter
    def selection_criteria(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a0aa0c45a0d208ef1b05bb6d298b1a3b8a6a93293ddc0c629f797b5ea4fb8a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectionCriteria", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnAccountPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy_document": "policyDocument",
        "policy_name": "policyName",
        "policy_type": "policyType",
        "scope": "scope",
        "selection_criteria": "selectionCriteria",
    },
)
class CfnAccountPolicyProps:
    def __init__(
        self,
        *,
        policy_document: builtins.str,
        policy_name: builtins.str,
        policy_type: builtins.str,
        scope: typing.Optional[builtins.str] = None,
        selection_criteria: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccountPolicy``.

        :param policy_document: Specify the policy, in JSON. *Data protection policy* A data protection policy must include two JSON blocks: - The first block must include both a ``DataIdentifer`` array and an ``Operation`` property with an ``Audit`` action. The ``DataIdentifer`` array lists the types of sensitive data that you want to mask. For more information about the available options, see `Types of data that you can mask <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-types.html>`_ . The ``Operation`` property with an ``Audit`` action is required to find the sensitive data terms. This ``Audit`` action must contain a ``FindingsDestination`` object. You can optionally use that ``FindingsDestination`` object to list one or more destinations to send audit findings to. If you specify destinations such as log groups, Firehose streams, and S3 buckets, they must already exist. - The second block must include both a ``DataIdentifer`` array and an ``Operation`` property with an ``Deidentify`` action. The ``DataIdentifer`` array must exactly match the ``DataIdentifer`` array in the first block of the policy. The ``Operation`` property with the ``Deidentify`` action is what actually masks the data, and it must contain the ``"MaskConfig": {}`` object. The ``"MaskConfig": {}`` object must be empty. .. epigraph:: The contents of the two ``DataIdentifer`` arrays must match exactly. In addition to the two JSON blocks, the ``policyDocument`` can also include ``Name`` , ``Description`` , and ``Version`` fields. The ``Name`` is different than the operation's ``policyName`` parameter, and is used as a dimension when CloudWatch Logs reports audit findings metrics to CloudWatch . The JSON specified in ``policyDocument`` can be up to 30,720 characters long. *Subscription filter policy* A subscription filter policy can include the following attributes in a JSON block: - *DestinationArn* The ARN of the destination to deliver log events to. Supported destinations are: - An Kinesis Data Streams data stream in the same account as the subscription policy, for same-account delivery. - An Firehose data stream in the same account as the subscription policy, for same-account delivery. - A Lambda function in the same account as the subscription policy, for same-account delivery. - A logical destination in a different account created with `PutDestination <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.html>`_ , for cross-account delivery. Kinesis Data Streams and Firehose are supported as logical destinations. - *RoleArn* The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery. - *FilterPattern* A filter pattern for subscribing to a filtered stream of log events. - *Distribution* The method used to distribute log data to the destination. By default, log data is grouped by log stream, but the grouping can be set to ``Random`` for a more even distribution. This property is only applicable when the destination is an Kinesis Data Streams data stream. *Field index policy* A field index filter policy can include the following attribute in a JSON block: - *Fields* The array of field indexes to create. The following is an example of an index policy document that creates two indexes, ``RequestId`` and ``TransactionId`` . ``"policyDocument": "{ \\"Fields\\": [ \\"RequestId\\", \\"TransactionId\\" ] }"`` *Transformer policy* A transformer policy must include one JSON block with the array of processors and their configurations. For more information about available processors, see `Processors that you can use <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-Processors>`_ .
        :param policy_name: A name for the policy. This must be unique within the account.
        :param policy_type: The type of policy that you're creating or updating.
        :param scope: Currently the only valid value for this parameter is ``ALL`` , which specifies that the policy applies to all log groups in the account. If you omit this parameter, the default of ``ALL`` is used. To scope down a subscription filter policy to a subset of log groups, use the ``SelectionCriteria`` parameter.
        :param selection_criteria: Use this parameter to apply the new policy to a subset of log groups in the account. You need to specify ``SelectionCriteria`` only when you specify ``SUBSCRIPTION_FILTER_POLICY`` , ``FIELD_INDEX_POLICY`` or ``TRANSFORMER_POLICY`` for ``PolicyType`` . If ``PolicyType`` is ``SUBSCRIPTION_FILTER_POLICY`` , the only supported ``SelectionCriteria`` filter is ``LogGroupName NOT IN []`` If ``PolicyType`` is ``FIELD_INDEX_POLICY`` or ``TRANSFORMER_POLICY`` , the only supported ``SelectionCriteria`` filter is ``LogGroupNamePrefix`` The ``SelectionCriteria`` string can be up to 25KB in length. The length is determined by using its UTF-8 bytes. Using the ``SelectionCriteria`` parameter with ``SUBSCRIPTION_FILTER_POLICY`` is useful to help prevent infinite loops. For more information, see `Log recursion prevention <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions-recursion-prevention.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_account_policy_props = logs.CfnAccountPolicyProps(
                policy_document="policyDocument",
                policy_name="policyName",
                policy_type="policyType",
            
                # the properties below are optional
                scope="scope",
                selection_criteria="selectionCriteria"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e40dcebab5dfdd5fd816fda98a9c4e710aa8bc28c8bbd574a9451defb6d0d66)
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument selection_criteria", value=selection_criteria, expected_type=type_hints["selection_criteria"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_document": policy_document,
            "policy_name": policy_name,
            "policy_type": policy_type,
        }
        if scope is not None:
            self._values["scope"] = scope
        if selection_criteria is not None:
            self._values["selection_criteria"] = selection_criteria

    @builtins.property
    def policy_document(self) -> builtins.str:
        '''Specify the policy, in JSON.

        *Data protection policy*

        A data protection policy must include two JSON blocks:

        - The first block must include both a ``DataIdentifer`` array and an ``Operation`` property with an ``Audit`` action. The ``DataIdentifer`` array lists the types of sensitive data that you want to mask. For more information about the available options, see `Types of data that you can mask <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-types.html>`_ .

        The ``Operation`` property with an ``Audit`` action is required to find the sensitive data terms. This ``Audit`` action must contain a ``FindingsDestination`` object. You can optionally use that ``FindingsDestination`` object to list one or more destinations to send audit findings to. If you specify destinations such as log groups, Firehose streams, and S3 buckets, they must already exist.

        - The second block must include both a ``DataIdentifer`` array and an ``Operation`` property with an ``Deidentify`` action. The ``DataIdentifer`` array must exactly match the ``DataIdentifer`` array in the first block of the policy.

        The ``Operation`` property with the ``Deidentify`` action is what actually masks the data, and it must contain the ``"MaskConfig": {}`` object. The ``"MaskConfig": {}`` object must be empty.
        .. epigraph::

           The contents of the two ``DataIdentifer`` arrays must match exactly.

        In addition to the two JSON blocks, the ``policyDocument`` can also include ``Name`` , ``Description`` , and ``Version`` fields. The ``Name`` is different than the operation's ``policyName`` parameter, and is used as a dimension when CloudWatch Logs reports audit findings metrics to CloudWatch .

        The JSON specified in ``policyDocument`` can be up to 30,720 characters long.

        *Subscription filter policy*

        A subscription filter policy can include the following attributes in a JSON block:

        - *DestinationArn* The ARN of the destination to deliver log events to. Supported destinations are:
        - An Kinesis Data Streams data stream in the same account as the subscription policy, for same-account delivery.
        - An Firehose data stream in the same account as the subscription policy, for same-account delivery.
        - A Lambda function in the same account as the subscription policy, for same-account delivery.
        - A logical destination in a different account created with `PutDestination <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.html>`_ , for cross-account delivery. Kinesis Data Streams and Firehose are supported as logical destinations.
        - *RoleArn* The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.
        - *FilterPattern* A filter pattern for subscribing to a filtered stream of log events.
        - *Distribution* The method used to distribute log data to the destination. By default, log data is grouped by log stream, but the grouping can be set to ``Random`` for a more even distribution. This property is only applicable when the destination is an Kinesis Data Streams data stream.

        *Field index policy*

        A field index filter policy can include the following attribute in a JSON block:

        - *Fields* The array of field indexes to create.

        The following is an example of an index policy document that creates two indexes, ``RequestId`` and ``TransactionId`` .

        ``"policyDocument": "{ \\"Fields\\": [ \\"RequestId\\", \\"TransactionId\\" ] }"``

        *Transformer policy*

        A transformer policy must include one JSON block with the array of processors and their configurations. For more information about available processors, see `Processors that you can use <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-Processors>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html#cfn-logs-accountpolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''A name for the policy.

        This must be unique within the account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html#cfn-logs-accountpolicy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_type(self) -> builtins.str:
        '''The type of policy that you're creating or updating.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html#cfn-logs-accountpolicy-policytype
        '''
        result = self._values.get("policy_type")
        assert result is not None, "Required property 'policy_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Currently the only valid value for this parameter is ``ALL`` , which specifies that the policy applies to all log groups in the account.

        If you omit this parameter, the default of ``ALL`` is used. To scope down a subscription filter policy to a subset of log groups, use the ``SelectionCriteria`` parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html#cfn-logs-accountpolicy-scope
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def selection_criteria(self) -> typing.Optional[builtins.str]:
        '''Use this parameter to apply the new policy to a subset of log groups in the account.

        You need to specify ``SelectionCriteria`` only when you specify ``SUBSCRIPTION_FILTER_POLICY`` , ``FIELD_INDEX_POLICY`` or ``TRANSFORMER_POLICY`` for ``PolicyType`` .

        If ``PolicyType`` is ``SUBSCRIPTION_FILTER_POLICY`` , the only supported ``SelectionCriteria`` filter is ``LogGroupName NOT IN []``

        If ``PolicyType`` is ``FIELD_INDEX_POLICY`` or ``TRANSFORMER_POLICY`` , the only supported ``SelectionCriteria`` filter is ``LogGroupNamePrefix``

        The ``SelectionCriteria`` string can be up to 25KB in length. The length is determined by using its UTF-8 bytes.

        Using the ``SelectionCriteria`` parameter with ``SUBSCRIPTION_FILTER_POLICY`` is useful to help prevent infinite loops. For more information, see `Log recursion prevention <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions-recursion-prevention.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-accountpolicy.html#cfn-logs-accountpolicy-selectioncriteria
        '''
        result = self._values.get("selection_criteria")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccountPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnDelivery(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnDelivery",
):
    '''This structure contains information about one *delivery* in your account.

    A delivery is a connection between a logical *delivery source* and a logical *delivery destination* .

    For more information, see `CreateDelivery <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html>`_ .

    To update an existing delivery configuration, use `UpdateDeliveryConfiguration <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html
    :cloudformationResource: AWS::Logs::Delivery
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_delivery = logs.CfnDelivery(self, "MyCfnDelivery",
            delivery_destination_arn="deliveryDestinationArn",
            delivery_source_name="deliverySourceName",
        
            # the properties below are optional
            field_delimiter="fieldDelimiter",
            record_fields=["recordFields"],
            s3_enable_hive_compatible_path=False,
            s3_suffix_path="s3SuffixPath",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        delivery_destination_arn: builtins.str,
        delivery_source_name: builtins.str,
        field_delimiter: typing.Optional[builtins.str] = None,
        record_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        s3_enable_hive_compatible_path: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        s3_suffix_path: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param delivery_destination_arn: The ARN of the delivery destination that is associated with this delivery.
        :param delivery_source_name: The name of the delivery source that is associated with this delivery.
        :param field_delimiter: The field delimiter that is used between record fields when the final output format of a delivery is in ``Plain`` , ``W3C`` , or ``Raw`` format.
        :param record_fields: The list of record fields to be delivered to the destination, in order. If the delivery's log source has mandatory fields, they must be included in this list.
        :param s3_enable_hive_compatible_path: Use this parameter to cause the S3 objects that contain delivered logs to use a prefix structure that allows for integration with Apache Hive.
        :param s3_suffix_path: Use this to reconfigure the S3 object prefix to contain either static or variable sections. The valid variables to use in the suffix path will vary by each log source. To find the values supported for the suffix path for each log source, use the `DescribeConfigurationTemplates <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeConfigurationTemplates.html>`_ operation and check the ``allowedSuffixPathFields`` field in the response.
        :param tags: An array of key-value pairs to apply to the delivery. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9ab4424636fed5b3c6cadfbae9a75acc19c7a49cc86eb71fbcb77cb343b3f59)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeliveryProps(
            delivery_destination_arn=delivery_destination_arn,
            delivery_source_name=delivery_source_name,
            field_delimiter=field_delimiter,
            record_fields=record_fields,
            s3_enable_hive_compatible_path=s3_enable_hive_compatible_path,
            s3_suffix_path=s3_suffix_path,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99f7221e967e1cfd1a9552bf514bfffa267c72d3a082920609edd6fcf762914f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__62e336df1727ca28efe4ebc70d80806e2800addcc81668613e49206280c6b492)
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
        '''The Amazon Resource Name (ARN) that uniquely identifies this delivery.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDeliveryDestinationType")
    def attr_delivery_destination_type(self) -> builtins.str:
        '''Displays whether the delivery destination associated with this delivery is CloudWatch Logs , Amazon S3 , or Firehose .

        :cloudformationAttribute: DeliveryDestinationType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeliveryDestinationType"))

    @builtins.property
    @jsii.member(jsii_name="attrDeliveryId")
    def attr_delivery_id(self) -> builtins.str:
        '''The unique ID that identifies this delivery in your account.

        :cloudformationAttribute: DeliveryId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeliveryId"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="deliveryDestinationArn")
    def delivery_destination_arn(self) -> builtins.str:
        '''The ARN of the delivery destination that is associated with this delivery.'''
        return typing.cast(builtins.str, jsii.get(self, "deliveryDestinationArn"))

    @delivery_destination_arn.setter
    def delivery_destination_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a50c8581f8db077c41c10f79c036d162827109bb24b65891dfc33cf502c6e78b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryDestinationArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deliverySourceName")
    def delivery_source_name(self) -> builtins.str:
        '''The name of the delivery source that is associated with this delivery.'''
        return typing.cast(builtins.str, jsii.get(self, "deliverySourceName"))

    @delivery_source_name.setter
    def delivery_source_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4ec9d68f7c2d7007a4afa644bcc4bc69a917cf74e5a3f6a6be17358ae262e09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliverySourceName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fieldDelimiter")
    def field_delimiter(self) -> typing.Optional[builtins.str]:
        '''The field delimiter that is used between record fields when the final output format of a delivery is in ``Plain`` , ``W3C`` , or ``Raw`` format.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldDelimiter"))

    @field_delimiter.setter
    def field_delimiter(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bd08694e6454ec1e8a7caa24ed3783c9708c421fe32b6506c73b7844a9734e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldDelimiter", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="recordFields")
    def record_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of record fields to be delivered to the destination, in order.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "recordFields"))

    @record_fields.setter
    def record_fields(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c57c7d1aa190b754df4f2f3cfe02326fa2d33aa925f4476a48f1ad8480bd7c58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordFields", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="s3EnableHiveCompatiblePath")
    def s3_enable_hive_compatible_path(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Use this parameter to cause the S3 objects that contain delivered logs to use a prefix structure that allows for integration with Apache Hive.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "s3EnableHiveCompatiblePath"))

    @s3_enable_hive_compatible_path.setter
    def s3_enable_hive_compatible_path(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__883ead422cb217bb6d7d85bba609b57a45ff8726f927790c48273417346f9faa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3EnableHiveCompatiblePath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="s3SuffixPath")
    def s3_suffix_path(self) -> typing.Optional[builtins.str]:
        '''Use this to reconfigure the S3 object prefix to contain either static or variable sections.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3SuffixPath"))

    @s3_suffix_path.setter
    def s3_suffix_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb1b6261fa6fe536f7b593af4c257808a0259533f08f144df15cc67bd0293e52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3SuffixPath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the delivery.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__000a573f2c99f6b1460750af0c01cc2fc0278bcaf6f21b31ed533ebcf516c233)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnDeliveryDestination(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnDeliveryDestination",
):
    '''This structure contains information about one *delivery destination* in your account.

    A delivery destination is an AWS resource that represents an AWS service that logs can be sent to. CloudWatch Logs, Amazon S3, Firehose, and X-Ray are supported as delivery destinations.

    To configure logs delivery between a supported AWS service and a destination, you must do the following:

    - Create a delivery source, which is a logical object that represents the resource that is actually sending the logs. For more information, see `PutDeliverySource <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html>`_ .
    - Create a *delivery destination* , which is a logical object that represents the actual delivery destination.
    - If you are delivering logs cross-account, you must use `PutDeliveryDestinationPolicy <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html>`_ in the destination account to assign an IAM policy to the destination. This policy allows delivery to that destination.
    - Create a *delivery* by pairing exactly one delivery source and one delivery destination. For more information, see `CreateDelivery <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html>`_ .

    You can configure a single delivery source to send logs to multiple destinations by creating multiple deliveries. You can also create multiple deliveries to configure multiple delivery sources to send logs to the same delivery destination.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.html
    :cloudformationResource: AWS::Logs::DeliveryDestination
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        # delivery_destination_policy: Any
        
        cfn_delivery_destination = logs.CfnDeliveryDestination(self, "MyCfnDeliveryDestination",
            name="name",
        
            # the properties below are optional
            delivery_destination_policy=logs.CfnDeliveryDestination.DestinationPolicyProperty(
                delivery_destination_name="deliveryDestinationName",
                delivery_destination_policy=delivery_destination_policy
            ),
            destination_resource_arn="destinationResourceArn",
            output_format="outputFormat",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        delivery_destination_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryDestination.DestinationPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        destination_resource_arn: typing.Optional[builtins.str] = None,
        output_format: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of this delivery destination.
        :param delivery_destination_policy: An IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account. For examples of this policy, see `Examples <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html#API_PutDeliveryDestinationPolicy_Examples>`_ in the CloudWatch Logs API Reference.
        :param destination_resource_arn: The ARN of the AWS destination that this delivery destination represents. That AWS destination can be a log group in CloudWatch Logs , an Amazon S3 bucket, or a Firehose stream.
        :param output_format: The format of the logs that are sent to this delivery destination.
        :param tags: An array of key-value pairs to apply to the delivery destination. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b48efa0b7b05ab2d9f1417a0b1e0cd7f28039825d1520fe16f6f8dca79d8d4fc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeliveryDestinationProps(
            name=name,
            delivery_destination_policy=delivery_destination_policy,
            destination_resource_arn=destination_resource_arn,
            output_format=output_format,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2db73754a49fde6308de1010ac96a197f9965c58bd5d9e7fc31cc846e853ab8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5af9dd3e40ccb4916d015c0cc40c6ae0c7210e9132f0dbf357f2e527552a5fa8)
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
        '''The Amazon Resource Name (ARN) that uniquely identifies this delivery destination.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDeliveryDestinationType")
    def attr_delivery_destination_type(self) -> builtins.str:
        '''Displays whether this delivery destination is CloudWatch Logs, Amazon S3, Firehose, or X-Ray.

        :cloudformationAttribute: DeliveryDestinationType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeliveryDestinationType"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of this delivery destination.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fdc8a995b69cc816b4deffcde2adde43de71476430695742e74896d1e844841)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deliveryDestinationPolicy")
    def delivery_destination_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryDestination.DestinationPolicyProperty"]]:
        '''An IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryDestination.DestinationPolicyProperty"]], jsii.get(self, "deliveryDestinationPolicy"))

    @delivery_destination_policy.setter
    def delivery_destination_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryDestination.DestinationPolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__318bc8d97cf7e7f129b83631444b5c478bd65a7e80725c9b3be7e3cc4a600b05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryDestinationPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="destinationResourceArn")
    def destination_resource_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the AWS destination that this delivery destination represents.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationResourceArn"))

    @destination_resource_arn.setter
    def destination_resource_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__831ddd5c5bd5a90cbf966f9a711dcab92a21ca60debf21106dbe34c3b30fce44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationResourceArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outputFormat")
    def output_format(self) -> typing.Optional[builtins.str]:
        '''The format of the logs that are sent to this delivery destination.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputFormat"))

    @output_format.setter
    def output_format(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72800638f30c315cbdfab3a9dcdd94e12b62e350f96e85c9fbc816f012ede070)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputFormat", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the delivery destination.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4f5227f043e0a8609b64c4a174886ba54b2825ada7e9a1dffe8fd35487fa5af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnDeliveryDestination.DestinationPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delivery_destination_name": "deliveryDestinationName",
            "delivery_destination_policy": "deliveryDestinationPolicy",
        },
    )
    class DestinationPolicyProperty:
        def __init__(
            self,
            *,
            delivery_destination_name: typing.Optional[builtins.str] = None,
            delivery_destination_policy: typing.Any = None,
        ) -> None:
            '''
            :param delivery_destination_name: The name of the delivery destination to assign this policy to.
            :param delivery_destination_policy: The contents of the policy attached to the delivery destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-deliverydestination-destinationpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                # delivery_destination_policy: Any
                
                destination_policy_property = logs.CfnDeliveryDestination.DestinationPolicyProperty(
                    delivery_destination_name="deliveryDestinationName",
                    delivery_destination_policy=delivery_destination_policy
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__476eb70b6b82939807d3600d63a802f799886d0c7cc23550944471a71b16233e)
                check_type(argname="argument delivery_destination_name", value=delivery_destination_name, expected_type=type_hints["delivery_destination_name"])
                check_type(argname="argument delivery_destination_policy", value=delivery_destination_policy, expected_type=type_hints["delivery_destination_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delivery_destination_name is not None:
                self._values["delivery_destination_name"] = delivery_destination_name
            if delivery_destination_policy is not None:
                self._values["delivery_destination_policy"] = delivery_destination_policy

        @builtins.property
        def delivery_destination_name(self) -> typing.Optional[builtins.str]:
            '''The name of the delivery destination to assign this policy to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-deliverydestination-destinationpolicy.html#cfn-logs-deliverydestination-destinationpolicy-deliverydestinationname
            '''
            result = self._values.get("delivery_destination_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def delivery_destination_policy(self) -> typing.Any:
            '''The contents of the policy attached to the delivery destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-deliverydestination-destinationpolicy.html#cfn-logs-deliverydestination-destinationpolicy-deliverydestinationpolicy
            '''
            result = self._values.get("delivery_destination_policy")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnDeliveryDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "delivery_destination_policy": "deliveryDestinationPolicy",
        "destination_resource_arn": "destinationResourceArn",
        "output_format": "outputFormat",
        "tags": "tags",
    },
)
class CfnDeliveryDestinationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        delivery_destination_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryDestination.DestinationPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        destination_resource_arn: typing.Optional[builtins.str] = None,
        output_format: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeliveryDestination``.

        :param name: The name of this delivery destination.
        :param delivery_destination_policy: An IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account. For examples of this policy, see `Examples <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html#API_PutDeliveryDestinationPolicy_Examples>`_ in the CloudWatch Logs API Reference.
        :param destination_resource_arn: The ARN of the AWS destination that this delivery destination represents. That AWS destination can be a log group in CloudWatch Logs , an Amazon S3 bucket, or a Firehose stream.
        :param output_format: The format of the logs that are sent to this delivery destination.
        :param tags: An array of key-value pairs to apply to the delivery destination. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            # delivery_destination_policy: Any
            
            cfn_delivery_destination_props = logs.CfnDeliveryDestinationProps(
                name="name",
            
                # the properties below are optional
                delivery_destination_policy=logs.CfnDeliveryDestination.DestinationPolicyProperty(
                    delivery_destination_name="deliveryDestinationName",
                    delivery_destination_policy=delivery_destination_policy
                ),
                destination_resource_arn="destinationResourceArn",
                output_format="outputFormat",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53bbf04ee2b4b7e83a98258d41a973972fae20f7537731a0fbcda3e7c5f46c1c)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument delivery_destination_policy", value=delivery_destination_policy, expected_type=type_hints["delivery_destination_policy"])
            check_type(argname="argument destination_resource_arn", value=destination_resource_arn, expected_type=type_hints["destination_resource_arn"])
            check_type(argname="argument output_format", value=output_format, expected_type=type_hints["output_format"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if delivery_destination_policy is not None:
            self._values["delivery_destination_policy"] = delivery_destination_policy
        if destination_resource_arn is not None:
            self._values["destination_resource_arn"] = destination_resource_arn
        if output_format is not None:
            self._values["output_format"] = output_format
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of this delivery destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.html#cfn-logs-deliverydestination-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delivery_destination_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryDestination.DestinationPolicyProperty]]:
        '''An IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account.

        For examples of this policy, see `Examples <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html#API_PutDeliveryDestinationPolicy_Examples>`_ in the CloudWatch Logs API Reference.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.html#cfn-logs-deliverydestination-deliverydestinationpolicy
        '''
        result = self._values.get("delivery_destination_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryDestination.DestinationPolicyProperty]], result)

    @builtins.property
    def destination_resource_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the AWS destination that this delivery destination represents.

        That AWS destination can be a log group in CloudWatch Logs , an Amazon S3 bucket, or a Firehose stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.html#cfn-logs-deliverydestination-destinationresourcearn
        '''
        result = self._values.get("destination_resource_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_format(self) -> typing.Optional[builtins.str]:
        '''The format of the logs that are sent to this delivery destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.html#cfn-logs-deliverydestination-outputformat
        '''
        result = self._values.get("output_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the delivery destination.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.html#cfn-logs-deliverydestination-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeliveryDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnDeliveryProps",
    jsii_struct_bases=[],
    name_mapping={
        "delivery_destination_arn": "deliveryDestinationArn",
        "delivery_source_name": "deliverySourceName",
        "field_delimiter": "fieldDelimiter",
        "record_fields": "recordFields",
        "s3_enable_hive_compatible_path": "s3EnableHiveCompatiblePath",
        "s3_suffix_path": "s3SuffixPath",
        "tags": "tags",
    },
)
class CfnDeliveryProps:
    def __init__(
        self,
        *,
        delivery_destination_arn: builtins.str,
        delivery_source_name: builtins.str,
        field_delimiter: typing.Optional[builtins.str] = None,
        record_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        s3_enable_hive_compatible_path: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        s3_suffix_path: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDelivery``.

        :param delivery_destination_arn: The ARN of the delivery destination that is associated with this delivery.
        :param delivery_source_name: The name of the delivery source that is associated with this delivery.
        :param field_delimiter: The field delimiter that is used between record fields when the final output format of a delivery is in ``Plain`` , ``W3C`` , or ``Raw`` format.
        :param record_fields: The list of record fields to be delivered to the destination, in order. If the delivery's log source has mandatory fields, they must be included in this list.
        :param s3_enable_hive_compatible_path: Use this parameter to cause the S3 objects that contain delivered logs to use a prefix structure that allows for integration with Apache Hive.
        :param s3_suffix_path: Use this to reconfigure the S3 object prefix to contain either static or variable sections. The valid variables to use in the suffix path will vary by each log source. To find the values supported for the suffix path for each log source, use the `DescribeConfigurationTemplates <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeConfigurationTemplates.html>`_ operation and check the ``allowedSuffixPathFields`` field in the response.
        :param tags: An array of key-value pairs to apply to the delivery. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_delivery_props = logs.CfnDeliveryProps(
                delivery_destination_arn="deliveryDestinationArn",
                delivery_source_name="deliverySourceName",
            
                # the properties below are optional
                field_delimiter="fieldDelimiter",
                record_fields=["recordFields"],
                s3_enable_hive_compatible_path=False,
                s3_suffix_path="s3SuffixPath",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b538310aec1f59690c78c4bf171f8ecae0a76d174388a130cf6154213614117c)
            check_type(argname="argument delivery_destination_arn", value=delivery_destination_arn, expected_type=type_hints["delivery_destination_arn"])
            check_type(argname="argument delivery_source_name", value=delivery_source_name, expected_type=type_hints["delivery_source_name"])
            check_type(argname="argument field_delimiter", value=field_delimiter, expected_type=type_hints["field_delimiter"])
            check_type(argname="argument record_fields", value=record_fields, expected_type=type_hints["record_fields"])
            check_type(argname="argument s3_enable_hive_compatible_path", value=s3_enable_hive_compatible_path, expected_type=type_hints["s3_enable_hive_compatible_path"])
            check_type(argname="argument s3_suffix_path", value=s3_suffix_path, expected_type=type_hints["s3_suffix_path"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delivery_destination_arn": delivery_destination_arn,
            "delivery_source_name": delivery_source_name,
        }
        if field_delimiter is not None:
            self._values["field_delimiter"] = field_delimiter
        if record_fields is not None:
            self._values["record_fields"] = record_fields
        if s3_enable_hive_compatible_path is not None:
            self._values["s3_enable_hive_compatible_path"] = s3_enable_hive_compatible_path
        if s3_suffix_path is not None:
            self._values["s3_suffix_path"] = s3_suffix_path
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def delivery_destination_arn(self) -> builtins.str:
        '''The ARN of the delivery destination that is associated with this delivery.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html#cfn-logs-delivery-deliverydestinationarn
        '''
        result = self._values.get("delivery_destination_arn")
        assert result is not None, "Required property 'delivery_destination_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delivery_source_name(self) -> builtins.str:
        '''The name of the delivery source that is associated with this delivery.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html#cfn-logs-delivery-deliverysourcename
        '''
        result = self._values.get("delivery_source_name")
        assert result is not None, "Required property 'delivery_source_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field_delimiter(self) -> typing.Optional[builtins.str]:
        '''The field delimiter that is used between record fields when the final output format of a delivery is in ``Plain`` , ``W3C`` , or ``Raw`` format.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html#cfn-logs-delivery-fielddelimiter
        '''
        result = self._values.get("field_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def record_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of record fields to be delivered to the destination, in order.

        If the delivery's log source has mandatory fields, they must be included in this list.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html#cfn-logs-delivery-recordfields
        '''
        result = self._values.get("record_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def s3_enable_hive_compatible_path(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Use this parameter to cause the S3 objects that contain delivered logs to use a prefix structure that allows for integration with Apache Hive.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html#cfn-logs-delivery-s3enablehivecompatiblepath
        '''
        result = self._values.get("s3_enable_hive_compatible_path")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def s3_suffix_path(self) -> typing.Optional[builtins.str]:
        '''Use this to reconfigure the S3 object prefix to contain either static or variable sections.

        The valid variables to use in the suffix path will vary by each log source. To find the values supported for the suffix path for each log source, use the `DescribeConfigurationTemplates <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeConfigurationTemplates.html>`_ operation and check the ``allowedSuffixPathFields`` field in the response.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html#cfn-logs-delivery-s3suffixpath
        '''
        result = self._values.get("s3_suffix_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the delivery.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html#cfn-logs-delivery-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeliveryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnDeliverySource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnDeliverySource",
):
    '''Creates or updates one *delivery source* in your account.

    A delivery source is an AWS resource that sends logs to an AWS destination. The destination can be CloudWatch Logs , Amazon S3 , or Firehose .

    Only some AWS services support being configured as a delivery source. These services are listed as *Supported [V2 Permissions]* in the table at `Enabling logging from AWS services. <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html>`_

    To configure logs delivery between a supported AWS service and a destination, you must do the following:

    - Create a delivery source, which is a logical object that represents the resource that is actually sending the logs.
    - Create a *delivery destination* , which is a logical object that represents the actual delivery destination. For more information, see `AWS::Logs::DeliveryDestination <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.html>`_ or `PutDeliveryDestination <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html>`_ .
    - Create a *delivery* by pairing exactly one delivery source and one delivery destination. For more information, see `AWS::Logs::Delivery <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.html>`_ or `CreateDelivery <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html>`_ .

    You can configure a single delivery source to send logs to multiple destinations by creating multiple deliveries. You can also create multiple deliveries to configure multiple delivery sources to send logs to the same delivery destination.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.html
    :cloudformationResource: AWS::Logs::DeliverySource
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_delivery_source = logs.CfnDeliverySource(self, "MyCfnDeliverySource",
            name="name",
        
            # the properties below are optional
            log_type="logType",
            resource_arn="resourceArn",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        log_type: typing.Optional[builtins.str] = None,
        resource_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The unique name of the delivery source.
        :param log_type: The type of log that the source is sending. For valid values for this parameter, see the documentation for the source service.
        :param resource_arn: The ARN of the AWS resource that is generating and sending logs. For example, ``arn:aws:workmail:us-east-1:123456789012:organization/m-1234EXAMPLEabcd1234abcd1234abcd1234``
        :param tags: An array of key-value pairs to apply to the delivery source. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ab0297a02d5ec18fef514a89fa2743d7fb62f4e7b1fd892c1bd7ee901ef99c4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeliverySourceProps(
            name=name, log_type=log_type, resource_arn=resource_arn, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7c152d845b9eb6bc70785b4e0e32dec0dce7f287b55eaf85acdcea613be11d3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c67b6491f677638c6c1cb36e66c12c782c6221d3f036515d784e31181d6603e)
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
        '''The Amazon Resource Name (ARN) that uniquely identifies this delivery source.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceArns")
    def attr_resource_arns(self) -> typing.List[builtins.str]:
        '''This array contains the ARN of the AWS resource that sends logs and is represented by this delivery source.

        Currently, only one ARN can be in the array.

        :cloudformationAttribute: ResourceArns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrResourceArns"))

    @builtins.property
    @jsii.member(jsii_name="attrService")
    def attr_service(self) -> builtins.str:
        '''The AWS service that is sending logs.

        :cloudformationAttribute: Service
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrService"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The unique name of the delivery source.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46ee2cc4bb6930c90c749220d8d5170a97f90cc490afa3d4564c90e7f6d9a79a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logType")
    def log_type(self) -> typing.Optional[builtins.str]:
        '''The type of log that the source is sending.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logType"))

    @log_type.setter
    def log_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fafd9abe15a418ef0eafe4df0701cb0c5bd2181041f5fd30e006939ddedc10d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the AWS resource that is generating and sending logs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd0e55d64bccd98b6356d6f16e4ae7dc18393fe37b5ae94cd2dde9e7ecd15097)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the delivery source.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c56ccd3093218052492eee7c66b0cf9e8156a37606a1c8a35551c977444ed97e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnDeliverySourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "log_type": "logType",
        "resource_arn": "resourceArn",
        "tags": "tags",
    },
)
class CfnDeliverySourceProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        log_type: typing.Optional[builtins.str] = None,
        resource_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeliverySource``.

        :param name: The unique name of the delivery source.
        :param log_type: The type of log that the source is sending. For valid values for this parameter, see the documentation for the source service.
        :param resource_arn: The ARN of the AWS resource that is generating and sending logs. For example, ``arn:aws:workmail:us-east-1:123456789012:organization/m-1234EXAMPLEabcd1234abcd1234abcd1234``
        :param tags: An array of key-value pairs to apply to the delivery source. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_delivery_source_props = logs.CfnDeliverySourceProps(
                name="name",
            
                # the properties below are optional
                log_type="logType",
                resource_arn="resourceArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bd979785c6ee68de5cc10f2dec7ca694c3327ec47aa59e93668d849404cd7df)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if log_type is not None:
            self._values["log_type"] = log_type
        if resource_arn is not None:
            self._values["resource_arn"] = resource_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The unique name of the delivery source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.html#cfn-logs-deliverysource-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_type(self) -> typing.Optional[builtins.str]:
        '''The type of log that the source is sending.

        For valid values for this parameter, see the documentation for the source service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.html#cfn-logs-deliverysource-logtype
        '''
        result = self._values.get("log_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the AWS resource that is generating and sending logs.

        For example, ``arn:aws:workmail:us-east-1:123456789012:organization/m-1234EXAMPLEabcd1234abcd1234abcd1234``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.html#cfn-logs-deliverysource-resourcearn
        '''
        result = self._values.get("resource_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the delivery source.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.html#cfn-logs-deliverysource-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeliverySourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnDestination(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnDestination",
):
    '''The AWS::Logs::Destination resource specifies a CloudWatch Logs destination.

    A destination encapsulates a physical resource (such as an Amazon Kinesis data stream) and enables you to subscribe that resource to a stream of log events.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html
    :cloudformationResource: AWS::Logs::Destination
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_destination = logs.CfnDestination(self, "MyCfnDestination",
            destination_name="destinationName",
            role_arn="roleArn",
            target_arn="targetArn",
        
            # the properties below are optional
            destination_policy="destinationPolicy",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        destination_name: builtins.str,
        role_arn: builtins.str,
        target_arn: builtins.str,
        destination_policy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination_name: The name of the destination.
        :param role_arn: The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource.
        :param target_arn: The Amazon Resource Name (ARN) of the physical target where the log events are delivered (for example, a Kinesis stream).
        :param destination_policy: An IAM policy document that governs which AWS accounts can create subscription filters against this destination.
        :param tags: The tags that have been assigned to this delivery destination.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44e37c6c2772abdacfbcd01df5c5418fca8937b435df3890a5a5cb3437b9bab5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDestinationProps(
            destination_name=destination_name,
            role_arn=role_arn,
            target_arn=target_arn,
            destination_policy=destination_policy,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96cb24255178be4bad07466bab77f2ccec3a7bf2f35acfe8bf018152eb28bb7e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f9dedbbaf433f224026d220b3fb36706410370925367aeada047e8858f484ac)
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
        '''The ARN of the CloudWatch Logs destination, such as ``arn:aws:logs:us-west-1:123456789012:destination:MyDestination`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="destinationName")
    def destination_name(self) -> builtins.str:
        '''The name of the destination.'''
        return typing.cast(builtins.str, jsii.get(self, "destinationName"))

    @destination_name.setter
    def destination_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5158605e72fe974296ad671ff50605f46d8a94d78d818e766756296254fa5758)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__908d4772c2472f7ef1a59ee7f794734117f87a8908ceda3def1feff5578217c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetArn")
    def target_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the physical target where the log events are delivered (for example, a Kinesis stream).'''
        return typing.cast(builtins.str, jsii.get(self, "targetArn"))

    @target_arn.setter
    def target_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90e291c0d065725c0ff62d5808258937a46aa7e3d79209721b2ffdb32fc0db6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="destinationPolicy")
    def destination_policy(self) -> typing.Optional[builtins.str]:
        '''An IAM policy document that governs which AWS accounts can create subscription filters against this destination.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationPolicy"))

    @destination_policy.setter
    def destination_policy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b0569830af0faea41307b4fd071b0ef86a0b49f3514f3050bfa53cc72d3ddee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags that have been assigned to this delivery destination.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e2da427145601b64454ab268bb3be33f3c089ff53e25e2b9a66fd51a6d385db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_name": "destinationName",
        "role_arn": "roleArn",
        "target_arn": "targetArn",
        "destination_policy": "destinationPolicy",
        "tags": "tags",
    },
)
class CfnDestinationProps:
    def __init__(
        self,
        *,
        destination_name: builtins.str,
        role_arn: builtins.str,
        target_arn: builtins.str,
        destination_policy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDestination``.

        :param destination_name: The name of the destination.
        :param role_arn: The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource.
        :param target_arn: The Amazon Resource Name (ARN) of the physical target where the log events are delivered (for example, a Kinesis stream).
        :param destination_policy: An IAM policy document that governs which AWS accounts can create subscription filters against this destination.
        :param tags: The tags that have been assigned to this delivery destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_destination_props = logs.CfnDestinationProps(
                destination_name="destinationName",
                role_arn="roleArn",
                target_arn="targetArn",
            
                # the properties below are optional
                destination_policy="destinationPolicy",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faf2f9f88fd096e79a2445aab3efdc3a85509df7ba06ffc305c9faf39fa77a56)
            check_type(argname="argument destination_name", value=destination_name, expected_type=type_hints["destination_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            check_type(argname="argument destination_policy", value=destination_policy, expected_type=type_hints["destination_policy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_name": destination_name,
            "role_arn": role_arn,
            "target_arn": target_arn,
        }
        if destination_policy is not None:
            self._values["destination_policy"] = destination_policy
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def destination_name(self) -> builtins.str:
        '''The name of the destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-destinationname
        '''
        result = self._values.get("destination_name")
        assert result is not None, "Required property 'destination_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the physical target where the log events are delivered (for example, a Kinesis stream).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-targetarn
        '''
        result = self._values.get("target_arn")
        assert result is not None, "Required property 'target_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_policy(self) -> typing.Optional[builtins.str]:
        '''An IAM policy document that governs which AWS accounts can create subscription filters against this destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-destinationpolicy
        '''
        result = self._values.get("destination_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags that have been assigned to this delivery destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnIntegration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnIntegration",
):
    '''Creates an integration between CloudWatch Logs and another service in this account.

    Currently, only integrations with OpenSearch Service are supported, and currently you can have only one integration in your account.

    Integrating with OpenSearch Service makes it possible for you to create curated vended logs dashboards, powered by OpenSearch Service analytics. For more information, see `Vended log dashboards powered by Amazon OpenSearch Service <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-OpenSearch-Dashboards.html>`_ .

    You can use this operation only to create a new integration. You can't modify an existing integration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-integration.html
    :cloudformationResource: AWS::Logs::Integration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_integration = logs.CfnIntegration(self, "MyCfnIntegration",
            integration_name="integrationName",
            integration_type="integrationType",
            resource_config=logs.CfnIntegration.ResourceConfigProperty(
                open_search_resource_config=logs.CfnIntegration.OpenSearchResourceConfigProperty(
                    dashboard_viewer_principals=["dashboardViewerPrincipals"],
                    data_source_role_arn="dataSourceRoleArn",
        
                    # the properties below are optional
                    application_arn="applicationArn",
                    kms_key_arn="kmsKeyArn",
                    retention_days=123
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        integration_name: builtins.str,
        integration_type: builtins.str,
        resource_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.ResourceConfigProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param integration_name: The name of this integration.
        :param integration_type: The type of integration. Integrations with OpenSearch Service have the type ``OPENSEARCH`` .
        :param resource_config: This structure contains configuration details about an integration between CloudWatch Logs and another entity.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d25ae5aedb6cfa0b6f3765f329d81581fbcd3ff378cc552133e5d0fdd6d99ff)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIntegrationProps(
            integration_name=integration_name,
            integration_type=integration_type,
            resource_config=resource_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4444f0ef7fd9d069bfce488a66baa068bb1b87a18239a8510d4cfa183a652a0b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed5813f598ecc3cd5a557ae647d3d2e9b8b9b4d638ea5a9a5ac68d4ef1281007)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIntegrationStatus")
    def attr_integration_status(self) -> builtins.str:
        '''The current status of this integration.

        :cloudformationAttribute: IntegrationStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIntegrationStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="integrationName")
    def integration_name(self) -> builtins.str:
        '''The name of this integration.'''
        return typing.cast(builtins.str, jsii.get(self, "integrationName"))

    @integration_name.setter
    def integration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c789029fae3c40d804160d555fcd880577fad4f74f1191f7b52562964594751e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="integrationType")
    def integration_type(self) -> builtins.str:
        '''The type of integration.'''
        return typing.cast(builtins.str, jsii.get(self, "integrationType"))

    @integration_type.setter
    def integration_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e7ea06be2423b6609ab61f003f306246fb58e590842d8ee6d0b889e4e4d1bce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceConfig")
    def resource_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnIntegration.ResourceConfigProperty"]:
        '''This structure contains configuration details about an integration between CloudWatch Logs and another entity.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnIntegration.ResourceConfigProperty"], jsii.get(self, "resourceConfig"))

    @resource_config.setter
    def resource_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnIntegration.ResourceConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e70a870af94762893ff1564b472074d1ad1ea7d25c502af37606c4cce91a529a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceConfig", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnIntegration.OpenSearchResourceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dashboard_viewer_principals": "dashboardViewerPrincipals",
            "data_source_role_arn": "dataSourceRoleArn",
            "application_arn": "applicationArn",
            "kms_key_arn": "kmsKeyArn",
            "retention_days": "retentionDays",
        },
    )
    class OpenSearchResourceConfigProperty:
        def __init__(
            self,
            *,
            dashboard_viewer_principals: typing.Sequence[builtins.str],
            data_source_role_arn: builtins.str,
            application_arn: typing.Optional[builtins.str] = None,
            kms_key_arn: typing.Optional[builtins.str] = None,
            retention_days: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''This structure contains configuration details about an integration between CloudWatch Logs and OpenSearch Service.

            :param dashboard_viewer_principals: Specify the ARNs of IAM roles and IAM users who you want to grant permission to for viewing the dashboards. .. epigraph:: In addition to specifying these users here, you must also grant them the *CloudWatchOpenSearchDashboardAccess* IAM policy. For more information, see `IAM policies for users <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/OpenSearch-Dashboards-UserRoles.html>`_ .
            :param data_source_role_arn: Specify the ARN of an IAM role that CloudWatch Logs will use to create the integration. This role must have the permissions necessary to access the OpenSearch Service collection to be able to create the dashboards. For more information about the permissions needed, see `Permissions that the integration needs <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/OpenSearch-Dashboards-CreateRole.html>`_ in the CloudWatch Logs User Guide.
            :param application_arn: If you want to use an existing OpenSearch Service application for your integration with OpenSearch Service, specify it here. If you omit this, a new application will be created.
            :param kms_key_arn: To have the vended dashboard data encrypted with AWS KMS instead of the CloudWatch Logs default encryption method, specify the ARN of the AWS KMS key that you want to use.
            :param retention_days: Specify how many days that you want the data derived by OpenSearch Service to be retained in the index that the dashboard refers to. This also sets the maximum time period that you can choose when viewing data in the dashboard. Choosing a longer time frame will incur additional costs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-integration-opensearchresourceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                open_search_resource_config_property = logs.CfnIntegration.OpenSearchResourceConfigProperty(
                    dashboard_viewer_principals=["dashboardViewerPrincipals"],
                    data_source_role_arn="dataSourceRoleArn",
                
                    # the properties below are optional
                    application_arn="applicationArn",
                    kms_key_arn="kmsKeyArn",
                    retention_days=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c674a258b3e224416fabb1fbddb9ff6620ca73f500c2c766f439b1ff2d42221)
                check_type(argname="argument dashboard_viewer_principals", value=dashboard_viewer_principals, expected_type=type_hints["dashboard_viewer_principals"])
                check_type(argname="argument data_source_role_arn", value=data_source_role_arn, expected_type=type_hints["data_source_role_arn"])
                check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
                check_type(argname="argument retention_days", value=retention_days, expected_type=type_hints["retention_days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dashboard_viewer_principals": dashboard_viewer_principals,
                "data_source_role_arn": data_source_role_arn,
            }
            if application_arn is not None:
                self._values["application_arn"] = application_arn
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn
            if retention_days is not None:
                self._values["retention_days"] = retention_days

        @builtins.property
        def dashboard_viewer_principals(self) -> typing.List[builtins.str]:
            '''Specify the ARNs of IAM roles and IAM users who you want to grant permission to for viewing the dashboards.

            .. epigraph::

               In addition to specifying these users here, you must also grant them the *CloudWatchOpenSearchDashboardAccess* IAM policy. For more information, see `IAM policies for users <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/OpenSearch-Dashboards-UserRoles.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-integration-opensearchresourceconfig.html#cfn-logs-integration-opensearchresourceconfig-dashboardviewerprincipals
            '''
            result = self._values.get("dashboard_viewer_principals")
            assert result is not None, "Required property 'dashboard_viewer_principals' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def data_source_role_arn(self) -> builtins.str:
            '''Specify the ARN of an IAM role that CloudWatch Logs will use to create the integration.

            This role must have the permissions necessary to access the OpenSearch Service collection to be able to create the dashboards. For more information about the permissions needed, see `Permissions that the integration needs <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/OpenSearch-Dashboards-CreateRole.html>`_ in the CloudWatch Logs User Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-integration-opensearchresourceconfig.html#cfn-logs-integration-opensearchresourceconfig-datasourcerolearn
            '''
            result = self._values.get("data_source_role_arn")
            assert result is not None, "Required property 'data_source_role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def application_arn(self) -> typing.Optional[builtins.str]:
            '''If you want to use an existing OpenSearch Service application for your integration with OpenSearch Service, specify it here.

            If you omit this, a new application will be created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-integration-opensearchresourceconfig.html#cfn-logs-integration-opensearchresourceconfig-applicationarn
            '''
            result = self._values.get("application_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''To have the vended dashboard data encrypted with AWS KMS instead of the CloudWatch Logs default encryption method, specify the ARN of the AWS KMS key that you want to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-integration-opensearchresourceconfig.html#cfn-logs-integration-opensearchresourceconfig-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def retention_days(self) -> typing.Optional[jsii.Number]:
            '''Specify how many days that you want the data derived by OpenSearch Service to be retained in the index that the dashboard refers to.

            This also sets the maximum time period that you can choose when viewing data in the dashboard. Choosing a longer time frame will incur additional costs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-integration-opensearchresourceconfig.html#cfn-logs-integration-opensearchresourceconfig-retentiondays
            '''
            result = self._values.get("retention_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenSearchResourceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnIntegration.ResourceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"open_search_resource_config": "openSearchResourceConfig"},
    )
    class ResourceConfigProperty:
        def __init__(
            self,
            *,
            open_search_resource_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.OpenSearchResourceConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''This structure contains configuration details about an integration between CloudWatch Logs and another entity.

            :param open_search_resource_config: This structure contains configuration details about an integration between CloudWatch Logs and OpenSearch Service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-integration-resourceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                resource_config_property = logs.CfnIntegration.ResourceConfigProperty(
                    open_search_resource_config=logs.CfnIntegration.OpenSearchResourceConfigProperty(
                        dashboard_viewer_principals=["dashboardViewerPrincipals"],
                        data_source_role_arn="dataSourceRoleArn",
                
                        # the properties below are optional
                        application_arn="applicationArn",
                        kms_key_arn="kmsKeyArn",
                        retention_days=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d0dad8c7beab9d66f0a9d16731a931e58e75731a8cb6142e5ecd221eea5f4bab)
                check_type(argname="argument open_search_resource_config", value=open_search_resource_config, expected_type=type_hints["open_search_resource_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if open_search_resource_config is not None:
                self._values["open_search_resource_config"] = open_search_resource_config

        @builtins.property
        def open_search_resource_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.OpenSearchResourceConfigProperty"]]:
            '''This structure contains configuration details about an integration between CloudWatch Logs and OpenSearch Service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-integration-resourceconfig.html#cfn-logs-integration-resourceconfig-opensearchresourceconfig
            '''
            result = self._values.get("open_search_resource_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.OpenSearchResourceConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "integration_name": "integrationName",
        "integration_type": "integrationType",
        "resource_config": "resourceConfig",
    },
)
class CfnIntegrationProps:
    def __init__(
        self,
        *,
        integration_name: builtins.str,
        integration_type: builtins.str,
        resource_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ResourceConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnIntegration``.

        :param integration_name: The name of this integration.
        :param integration_type: The type of integration. Integrations with OpenSearch Service have the type ``OPENSEARCH`` .
        :param resource_config: This structure contains configuration details about an integration between CloudWatch Logs and another entity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-integration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_integration_props = logs.CfnIntegrationProps(
                integration_name="integrationName",
                integration_type="integrationType",
                resource_config=logs.CfnIntegration.ResourceConfigProperty(
                    open_search_resource_config=logs.CfnIntegration.OpenSearchResourceConfigProperty(
                        dashboard_viewer_principals=["dashboardViewerPrincipals"],
                        data_source_role_arn="dataSourceRoleArn",
            
                        # the properties below are optional
                        application_arn="applicationArn",
                        kms_key_arn="kmsKeyArn",
                        retention_days=123
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3fde65aad1184bb5a5e5498b7fec6844a978b48eb0a9d57607f44ec0c65fc3a)
            check_type(argname="argument integration_name", value=integration_name, expected_type=type_hints["integration_name"])
            check_type(argname="argument integration_type", value=integration_type, expected_type=type_hints["integration_type"])
            check_type(argname="argument resource_config", value=resource_config, expected_type=type_hints["resource_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "integration_name": integration_name,
            "integration_type": integration_type,
            "resource_config": resource_config,
        }

    @builtins.property
    def integration_name(self) -> builtins.str:
        '''The name of this integration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-integration.html#cfn-logs-integration-integrationname
        '''
        result = self._values.get("integration_name")
        assert result is not None, "Required property 'integration_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_type(self) -> builtins.str:
        '''The type of integration.

        Integrations with OpenSearch Service have the type ``OPENSEARCH`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-integration.html#cfn-logs-integration-integrationtype
        '''
        result = self._values.get("integration_type")
        assert result is not None, "Required property 'integration_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnIntegration.ResourceConfigProperty]:
        '''This structure contains configuration details about an integration between CloudWatch Logs and another entity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-integration.html#cfn-logs-integration-resourceconfig
        '''
        result = self._values.get("resource_config")
        assert result is not None, "Required property 'resource_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnIntegration.ResourceConfigProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLogAnomalyDetector(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnLogAnomalyDetector",
):
    '''Creates or updates an *anomaly detector* that regularly scans one or more log groups and look for patterns and anomalies in the logs.

    An anomaly detector can help surface issues by automatically discovering anomalies in your log event traffic. An anomaly detector uses machine learning algorithms to scan log events and find *patterns* . A pattern is a shared text structure that recurs among your log fields. Patterns provide a useful tool for analyzing large sets of logs because a large number of log events can often be compressed into a few patterns.

    The anomaly detector uses pattern recognition to find ``anomalies`` , which are unusual log events. It compares current log events and patterns with trained baselines.

    Fields within a pattern are called *tokens* . Fields that vary within a pattern, such as a request ID or timestamp, are referred to as *dynamic tokens* and represented by ``<*>`` .

    For more information see `Log anomaly detection <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html
    :cloudformationResource: AWS::Logs::LogAnomalyDetector
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_log_anomaly_detector = logs.CfnLogAnomalyDetector(self, "MyCfnLogAnomalyDetector",
            account_id="accountId",
            anomaly_visibility_time=123,
            detector_name="detectorName",
            evaluation_frequency="evaluationFrequency",
            filter_pattern="filterPattern",
            kms_key_id="kmsKeyId",
            log_group_arn_list=["logGroupArnList"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        account_id: typing.Optional[builtins.str] = None,
        anomaly_visibility_time: typing.Optional[jsii.Number] = None,
        detector_name: typing.Optional[builtins.str] = None,
        evaluation_frequency: typing.Optional[builtins.str] = None,
        filter_pattern: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_group_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param account_id: The ID of the account to create the anomaly detector in.
        :param anomaly_visibility_time: The number of days to have visibility on an anomaly. After this time period has elapsed for an anomaly, it will be automatically baselined and the anomaly detector will treat new occurrences of a similar anomaly as normal. Therefore, if you do not correct the cause of an anomaly during the time period specified in ``AnomalyVisibilityTime`` , it will be considered normal going forward and will not be detected as an anomaly.
        :param detector_name: A name for this anomaly detector.
        :param evaluation_frequency: Specifies how often the anomaly detector is to run and look for anomalies. Set this value according to the frequency that the log group receives new logs. For example, if the log group receives new log events every 10 minutes, then 15 minutes might be a good setting for ``EvaluationFrequency`` .
        :param filter_pattern: You can use this parameter to limit the anomaly detection model to examine only log events that match the pattern you specify here. For more information, see `Filter and Pattern Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`_ .
        :param kms_key_id: Optionally assigns a AWS KMS key to secure this anomaly detector and its findings. If a key is assigned, the anomalies found and the model used by this detector are encrypted at rest with the key. If a key is assigned to an anomaly detector, a user must have permissions for both this key and for the anomaly detector to retrieve information about the anomalies that it finds. For more information about using a AWS KMS key and to see the required IAM policy, see `Use a AWS KMS key with an anomaly detector <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection-KMS.html>`_ .
        :param log_group_arn_list: The ARN of the log group that is associated with this anomaly detector. You can specify only one log group ARN.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d152ea0809d051d39430771f957ddf1edb48a2711f5f1dac144632c4025106f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLogAnomalyDetectorProps(
            account_id=account_id,
            anomaly_visibility_time=anomaly_visibility_time,
            detector_name=detector_name,
            evaluation_frequency=evaluation_frequency,
            filter_pattern=filter_pattern,
            kms_key_id=kms_key_id,
            log_group_arn_list=log_group_arn_list,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6002d02f1da3550c2407847cbf1810c63c4cb68d5609b2890cad4cb306056324)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b8a73ba8c4ce52064896eb40ab1c6e467c30f9682ff3ef6376d101fbbce16202)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAnomalyDetectorArn")
    def attr_anomaly_detector_arn(self) -> builtins.str:
        '''The ARN of the anomaly detector.

        :cloudformationAttribute: AnomalyDetectorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAnomalyDetectorArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAnomalyDetectorStatus")
    def attr_anomaly_detector_status(self) -> builtins.str:
        '''Specifies whether the anomaly detector is currently active.

        :cloudformationAttribute: AnomalyDetectorStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAnomalyDetectorStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTimeStamp")
    def attr_creation_time_stamp(self) -> _IResolvable_da3f097b:
        '''The time that the anomaly detector was created.

        :cloudformationAttribute: CreationTimeStamp
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrCreationTimeStamp"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTimeStamp")
    def attr_last_modified_time_stamp(self) -> _IResolvable_da3f097b:
        '''The time that the anomaly detector was most recently modified.

        :cloudformationAttribute: LastModifiedTimeStamp
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLastModifiedTimeStamp"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the account to create the anomaly detector in.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7091ec3c1c0b4552340a41d082b9a8b05727396563c6735b32c808e4f4a9070)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="anomalyVisibilityTime")
    def anomaly_visibility_time(self) -> typing.Optional[jsii.Number]:
        '''The number of days to have visibility on an anomaly.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "anomalyVisibilityTime"))

    @anomaly_visibility_time.setter
    def anomaly_visibility_time(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4568b027e5608ed08e1434d2fc055c05356712bc434041b26212701c5881dd15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anomalyVisibilityTime", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="detectorName")
    def detector_name(self) -> typing.Optional[builtins.str]:
        '''A name for this anomaly detector.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "detectorName"))

    @detector_name.setter
    def detector_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e029b96055f74ee8a1506c21562c10f01dc81a628d9217edc344d32c509e4c01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="evaluationFrequency")
    def evaluation_frequency(self) -> typing.Optional[builtins.str]:
        '''Specifies how often the anomaly detector is to run and look for anomalies.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluationFrequency"))

    @evaluation_frequency.setter
    def evaluation_frequency(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a18b33d5cf65ad2b2c4c21d6c527f99b8ac41d21d5b6357d7bda666a78e5b05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationFrequency", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="filterPattern")
    def filter_pattern(self) -> typing.Optional[builtins.str]:
        '''You can use this parameter to limit the anomaly detection model to examine only log events that match the pattern you specify here.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterPattern"))

    @filter_pattern.setter
    def filter_pattern(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6022589a1d3385b97bbf672ecb067e6569c73966e3009ac7e9e5f211d37f740e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterPattern", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Optionally assigns a AWS KMS key to secure this anomaly detector and its findings.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d7970b3814e2fb4a7bdf38b8f455da8249766c8616b4813e2bfe621651215a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logGroupArnList")
    def log_group_arn_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARN of the log group that is associated with this anomaly detector.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "logGroupArnList"))

    @log_group_arn_list.setter
    def log_group_arn_list(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5113cbbd1e159d109496838f7c2de7bb9765d5d8f294094b0b933c1193e2331)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupArnList", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnLogAnomalyDetectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "anomaly_visibility_time": "anomalyVisibilityTime",
        "detector_name": "detectorName",
        "evaluation_frequency": "evaluationFrequency",
        "filter_pattern": "filterPattern",
        "kms_key_id": "kmsKeyId",
        "log_group_arn_list": "logGroupArnList",
    },
)
class CfnLogAnomalyDetectorProps:
    def __init__(
        self,
        *,
        account_id: typing.Optional[builtins.str] = None,
        anomaly_visibility_time: typing.Optional[jsii.Number] = None,
        detector_name: typing.Optional[builtins.str] = None,
        evaluation_frequency: typing.Optional[builtins.str] = None,
        filter_pattern: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_group_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLogAnomalyDetector``.

        :param account_id: The ID of the account to create the anomaly detector in.
        :param anomaly_visibility_time: The number of days to have visibility on an anomaly. After this time period has elapsed for an anomaly, it will be automatically baselined and the anomaly detector will treat new occurrences of a similar anomaly as normal. Therefore, if you do not correct the cause of an anomaly during the time period specified in ``AnomalyVisibilityTime`` , it will be considered normal going forward and will not be detected as an anomaly.
        :param detector_name: A name for this anomaly detector.
        :param evaluation_frequency: Specifies how often the anomaly detector is to run and look for anomalies. Set this value according to the frequency that the log group receives new logs. For example, if the log group receives new log events every 10 minutes, then 15 minutes might be a good setting for ``EvaluationFrequency`` .
        :param filter_pattern: You can use this parameter to limit the anomaly detection model to examine only log events that match the pattern you specify here. For more information, see `Filter and Pattern Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`_ .
        :param kms_key_id: Optionally assigns a AWS KMS key to secure this anomaly detector and its findings. If a key is assigned, the anomalies found and the model used by this detector are encrypted at rest with the key. If a key is assigned to an anomaly detector, a user must have permissions for both this key and for the anomaly detector to retrieve information about the anomalies that it finds. For more information about using a AWS KMS key and to see the required IAM policy, see `Use a AWS KMS key with an anomaly detector <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection-KMS.html>`_ .
        :param log_group_arn_list: The ARN of the log group that is associated with this anomaly detector. You can specify only one log group ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_log_anomaly_detector_props = logs.CfnLogAnomalyDetectorProps(
                account_id="accountId",
                anomaly_visibility_time=123,
                detector_name="detectorName",
                evaluation_frequency="evaluationFrequency",
                filter_pattern="filterPattern",
                kms_key_id="kmsKeyId",
                log_group_arn_list=["logGroupArnList"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73c93feb7d3595f49f16b50d5ef5c97b24e9aba98c12935428a8e2019fd66a2b)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument anomaly_visibility_time", value=anomaly_visibility_time, expected_type=type_hints["anomaly_visibility_time"])
            check_type(argname="argument detector_name", value=detector_name, expected_type=type_hints["detector_name"])
            check_type(argname="argument evaluation_frequency", value=evaluation_frequency, expected_type=type_hints["evaluation_frequency"])
            check_type(argname="argument filter_pattern", value=filter_pattern, expected_type=type_hints["filter_pattern"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument log_group_arn_list", value=log_group_arn_list, expected_type=type_hints["log_group_arn_list"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account_id is not None:
            self._values["account_id"] = account_id
        if anomaly_visibility_time is not None:
            self._values["anomaly_visibility_time"] = anomaly_visibility_time
        if detector_name is not None:
            self._values["detector_name"] = detector_name
        if evaluation_frequency is not None:
            self._values["evaluation_frequency"] = evaluation_frequency
        if filter_pattern is not None:
            self._values["filter_pattern"] = filter_pattern
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if log_group_arn_list is not None:
            self._values["log_group_arn_list"] = log_group_arn_list

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the account to create the anomaly detector in.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html#cfn-logs-loganomalydetector-accountid
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def anomaly_visibility_time(self) -> typing.Optional[jsii.Number]:
        '''The number of days to have visibility on an anomaly.

        After this time period has elapsed for an anomaly, it will be automatically baselined and the anomaly detector will treat new occurrences of a similar anomaly as normal. Therefore, if you do not correct the cause of an anomaly during the time period specified in ``AnomalyVisibilityTime`` , it will be considered normal going forward and will not be detected as an anomaly.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html#cfn-logs-loganomalydetector-anomalyvisibilitytime
        '''
        result = self._values.get("anomaly_visibility_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def detector_name(self) -> typing.Optional[builtins.str]:
        '''A name for this anomaly detector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html#cfn-logs-loganomalydetector-detectorname
        '''
        result = self._values.get("detector_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluation_frequency(self) -> typing.Optional[builtins.str]:
        '''Specifies how often the anomaly detector is to run and look for anomalies.

        Set this value according to the frequency that the log group receives new logs. For example, if the log group receives new log events every 10 minutes, then 15 minutes might be a good setting for ``EvaluationFrequency`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html#cfn-logs-loganomalydetector-evaluationfrequency
        '''
        result = self._values.get("evaluation_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter_pattern(self) -> typing.Optional[builtins.str]:
        '''You can use this parameter to limit the anomaly detection model to examine only log events that match the pattern you specify here.

        For more information, see `Filter and Pattern Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html#cfn-logs-loganomalydetector-filterpattern
        '''
        result = self._values.get("filter_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Optionally assigns a AWS KMS key to secure this anomaly detector and its findings.

        If a key is assigned, the anomalies found and the model used by this detector are encrypted at rest with the key. If a key is assigned to an anomaly detector, a user must have permissions for both this key and for the anomaly detector to retrieve information about the anomalies that it finds.

        For more information about using a AWS KMS key and to see the required IAM policy, see `Use a AWS KMS key with an anomaly detector <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection-KMS.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html#cfn-logs-loganomalydetector-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_group_arn_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARN of the log group that is associated with this anomaly detector.

        You can specify only one log group ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loganomalydetector.html#cfn-logs-loganomalydetector-loggrouparnlist
        '''
        result = self._values.get("log_group_arn_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLogAnomalyDetectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLogGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnLogGroup",
):
    '''The ``AWS::Logs::LogGroup`` resource specifies a log group.

    A log group defines common properties for log streams, such as their retention and access control rules. Each log stream must belong to one log group.

    You can create up to 1,000,000 log groups per Region per account. You must use the following guidelines when naming a log group:

    - Log group names must be unique within a Region for an AWS account.
    - Log group names can be between 1 and 512 characters long.
    - Log group names consist of the following characters: a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), and '.' (period).

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html
    :cloudformationResource: AWS::Logs::LogGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        # data_protection_policy: Any
        # field_index_policies: Any
        # resource_policy_document: Any
        
        cfn_log_group = logs.CfnLogGroup(self, "MyCfnLogGroup",
            data_protection_policy=data_protection_policy,
            field_index_policies=[field_index_policies],
            kms_key_id="kmsKeyId",
            log_group_class="logGroupClass",
            log_group_name="logGroupName",
            resource_policy_document=resource_policy_document,
            retention_in_days=123,
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        data_protection_policy: typing.Any = None,
        field_index_policies: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_group_class: typing.Optional[builtins.str] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        resource_policy_document: typing.Any = None,
        retention_in_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data_protection_policy: Creates a data protection policy and assigns it to the log group. A data protection policy can help safeguard sensitive data that's ingested by the log group by auditing and masking the sensitive log data. When a user who does not have permission to view masked data views a log event that includes masked data, the sensitive data is replaced by asterisks. For more information, including a list of types of data that can be audited and masked, see `Protect sensitive log data with masking <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html>`_ .
        :param field_index_policies: Creates or updates a *field index policy* for the specified log group. Only log groups in the Standard log class support field index policies. For more information about log classes, see `Log classes <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html>`_ . You can use field index policies to create *field indexes* on fields found in log events in the log group. Creating field indexes lowers the costs for CloudWatch Logs Insights queries that reference those field indexes, because these queries attempt to skip the processing of log events that are known to not match the indexed field. Good fields to index are fields that you often need to query for and fields that have high cardinality of values Common examples of indexes include request ID, session ID, userID, and instance IDs. For more information, see `Create field indexes to improve query performance and reduce costs <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html>`_ . Currently, this array supports only one field index policy object.
        :param kms_key_id: The Amazon Resource Name (ARN) of the AWS KMS key to use when encrypting log data. To associate an AWS KMS key with the log group, specify the ARN of that KMS key here. If you do so, ingested data is encrypted using this key. This association is stored as long as the data encrypted with the KMS key is still within CloudWatch Logs . This enables CloudWatch Logs to decrypt this data whenever it is requested. If you attempt to associate a KMS key with the log group but the KMS key doesn't exist or is deactivated, you will receive an ``InvalidParameterException`` error. Log group data is always encrypted in CloudWatch Logs . If you omit this key, the encryption does not use AWS KMS . For more information, see `Encrypt log data in CloudWatch Logs using AWS Key Management Service <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html>`_
        :param log_group_class: Specifies the log group class for this log group. There are two classes:. - The ``Standard`` log class supports all CloudWatch Logs features. - The ``Infrequent Access`` log class supports a subset of CloudWatch Logs features and incurs lower costs. For details about the features supported by each class, see `Log classes <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html>`_ Default: - "STANDARD"
        :param log_group_name: The name of the log group. If you don't specify a name, AWS CloudFormation generates a unique ID for the log group.
        :param resource_policy_document: 
        :param retention_in_days: The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, and 3653. To set a log group so that its log events do not expire, use `DeleteRetentionPolicy <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.html>`_ .
        :param tags: An array of key-value pairs to apply to the log group. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e283e76ec168d67513d106f9413697672f161b29f03fa9b13486e96b13319c0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLogGroupProps(
            data_protection_policy=data_protection_policy,
            field_index_policies=field_index_policies,
            kms_key_id=kms_key_id,
            log_group_class=log_group_class,
            log_group_name=log_group_name,
            resource_policy_document=resource_policy_document,
            retention_in_days=retention_in_days,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c5bac0ef7ae74529e652cc24b33213b3432954607a3665dd72bd69b68490c7c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__167d66406821a4fe8a6ca05ec99424e7c4abd7946ba6eb30ee37e04443759ddc)
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
        '''The ARN of the log group, such as ``arn:aws:logs:us-west-1:123456789012:log-group:/mystack-testgroup-12ABC1AB12A1:*``.

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
    @jsii.member(jsii_name="dataProtectionPolicy")
    def data_protection_policy(self) -> typing.Any:
        '''Creates a data protection policy and assigns it to the log group.'''
        return typing.cast(typing.Any, jsii.get(self, "dataProtectionPolicy"))

    @data_protection_policy.setter
    def data_protection_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__427539e290b46019fba84ec8aa72f953c2d26dfe978de85330819964c3cea37e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataProtectionPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fieldIndexPolicies")
    def field_index_policies(
        self,
    ) -> typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]]:
        '''Creates or updates a *field index policy* for the specified log group.'''
        return typing.cast(typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]], jsii.get(self, "fieldIndexPolicies"))

    @field_index_policies.setter
    def field_index_policies(
        self,
        value: typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b4f37a255340908d68ce2d6149f1bb01ab5104c15a9b60474e51dde5b10d526)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldIndexPolicies", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS KMS key to use when encrypting log data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fc22b518f14684135ca2ffa0556628df055b32df3a769085c35ae8ef72d5677)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logGroupClass")
    def log_group_class(self) -> typing.Optional[builtins.str]:
        '''Specifies the log group class for this log group.

        There are two classes:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupClass"))

    @log_group_class.setter
    def log_group_class(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc12e80d5e08442f63a358d7f964b44915adb40d9341cdbd7ae2bf730d5a0fbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupClass", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the log group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08bea1f6b59cbce316d19aa0ff5db07ed0da20b04cc322eb41788ce24f8f2d31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyDocument")
    def resource_policy_document(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "resourcePolicyDocument"))

    @resource_policy_document.setter
    def resource_policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d6853e85debe88051bdf2f6ab68103e166533560e34248419263b9c0f7dd03e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourcePolicyDocument", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="retentionInDays")
    def retention_in_days(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain the log events in the specified log group.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInDays"))

    @retention_in_days.setter
    def retention_in_days(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d977a18b9031aeb9d37e4baf6f3eccb9ebf070ad2e33a30cfba9f69fbaf62408)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInDays", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the log group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ea9a0a37724d334e68ee325d75e901df12c6765b4c229366a1cef4038c07187)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnLogGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_protection_policy": "dataProtectionPolicy",
        "field_index_policies": "fieldIndexPolicies",
        "kms_key_id": "kmsKeyId",
        "log_group_class": "logGroupClass",
        "log_group_name": "logGroupName",
        "resource_policy_document": "resourcePolicyDocument",
        "retention_in_days": "retentionInDays",
        "tags": "tags",
    },
)
class CfnLogGroupProps:
    def __init__(
        self,
        *,
        data_protection_policy: typing.Any = None,
        field_index_policies: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_group_class: typing.Optional[builtins.str] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        resource_policy_document: typing.Any = None,
        retention_in_days: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLogGroup``.

        :param data_protection_policy: Creates a data protection policy and assigns it to the log group. A data protection policy can help safeguard sensitive data that's ingested by the log group by auditing and masking the sensitive log data. When a user who does not have permission to view masked data views a log event that includes masked data, the sensitive data is replaced by asterisks. For more information, including a list of types of data that can be audited and masked, see `Protect sensitive log data with masking <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html>`_ .
        :param field_index_policies: Creates or updates a *field index policy* for the specified log group. Only log groups in the Standard log class support field index policies. For more information about log classes, see `Log classes <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html>`_ . You can use field index policies to create *field indexes* on fields found in log events in the log group. Creating field indexes lowers the costs for CloudWatch Logs Insights queries that reference those field indexes, because these queries attempt to skip the processing of log events that are known to not match the indexed field. Good fields to index are fields that you often need to query for and fields that have high cardinality of values Common examples of indexes include request ID, session ID, userID, and instance IDs. For more information, see `Create field indexes to improve query performance and reduce costs <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html>`_ . Currently, this array supports only one field index policy object.
        :param kms_key_id: The Amazon Resource Name (ARN) of the AWS KMS key to use when encrypting log data. To associate an AWS KMS key with the log group, specify the ARN of that KMS key here. If you do so, ingested data is encrypted using this key. This association is stored as long as the data encrypted with the KMS key is still within CloudWatch Logs . This enables CloudWatch Logs to decrypt this data whenever it is requested. If you attempt to associate a KMS key with the log group but the KMS key doesn't exist or is deactivated, you will receive an ``InvalidParameterException`` error. Log group data is always encrypted in CloudWatch Logs . If you omit this key, the encryption does not use AWS KMS . For more information, see `Encrypt log data in CloudWatch Logs using AWS Key Management Service <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html>`_
        :param log_group_class: Specifies the log group class for this log group. There are two classes:. - The ``Standard`` log class supports all CloudWatch Logs features. - The ``Infrequent Access`` log class supports a subset of CloudWatch Logs features and incurs lower costs. For details about the features supported by each class, see `Log classes <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html>`_ Default: - "STANDARD"
        :param log_group_name: The name of the log group. If you don't specify a name, AWS CloudFormation generates a unique ID for the log group.
        :param resource_policy_document: 
        :param retention_in_days: The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, and 3653. To set a log group so that its log events do not expire, use `DeleteRetentionPolicy <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.html>`_ .
        :param tags: An array of key-value pairs to apply to the log group. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            # data_protection_policy: Any
            # field_index_policies: Any
            # resource_policy_document: Any
            
            cfn_log_group_props = logs.CfnLogGroupProps(
                data_protection_policy=data_protection_policy,
                field_index_policies=[field_index_policies],
                kms_key_id="kmsKeyId",
                log_group_class="logGroupClass",
                log_group_name="logGroupName",
                resource_policy_document=resource_policy_document,
                retention_in_days=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a2ba122502a64b05bea3e56f15389c84f127761b660b1d06de3ea638b95f816)
            check_type(argname="argument data_protection_policy", value=data_protection_policy, expected_type=type_hints["data_protection_policy"])
            check_type(argname="argument field_index_policies", value=field_index_policies, expected_type=type_hints["field_index_policies"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument log_group_class", value=log_group_class, expected_type=type_hints["log_group_class"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument resource_policy_document", value=resource_policy_document, expected_type=type_hints["resource_policy_document"])
            check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if data_protection_policy is not None:
            self._values["data_protection_policy"] = data_protection_policy
        if field_index_policies is not None:
            self._values["field_index_policies"] = field_index_policies
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if log_group_class is not None:
            self._values["log_group_class"] = log_group_class
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if resource_policy_document is not None:
            self._values["resource_policy_document"] = resource_policy_document
        if retention_in_days is not None:
            self._values["retention_in_days"] = retention_in_days
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data_protection_policy(self) -> typing.Any:
        '''Creates a data protection policy and assigns it to the log group.

        A data protection policy can help safeguard sensitive data that's ingested by the log group by auditing and masking the sensitive log data. When a user who does not have permission to view masked data views a log event that includes masked data, the sensitive data is replaced by asterisks.

        For more information, including a list of types of data that can be audited and masked, see `Protect sensitive log data with masking <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-dataprotectionpolicy
        '''
        result = self._values.get("data_protection_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def field_index_policies(
        self,
    ) -> typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]]:
        '''Creates or updates a *field index policy* for the specified log group.

        Only log groups in the Standard log class support field index policies. For more information about log classes, see `Log classes <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html>`_ .

        You can use field index policies to create *field indexes* on fields found in log events in the log group. Creating field indexes lowers the costs for CloudWatch Logs Insights queries that reference those field indexes, because these queries attempt to skip the processing of log events that are known to not match the indexed field. Good fields to index are fields that you often need to query for and fields that have high cardinality of values Common examples of indexes include request ID, session ID, userID, and instance IDs. For more information, see `Create field indexes to improve query performance and reduce costs <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html>`_ .

        Currently, this array supports only one field index policy object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-fieldindexpolicies
        '''
        result = self._values.get("field_index_policies")
        return typing.cast(typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS KMS key to use when encrypting log data.

        To associate an AWS KMS key with the log group, specify the ARN of that KMS key here. If you do so, ingested data is encrypted using this key. This association is stored as long as the data encrypted with the KMS key is still within CloudWatch Logs . This enables CloudWatch Logs to decrypt this data whenever it is requested.

        If you attempt to associate a KMS key with the log group but the KMS key doesn't exist or is deactivated, you will receive an ``InvalidParameterException`` error.

        Log group data is always encrypted in CloudWatch Logs . If you omit this key, the encryption does not use AWS KMS . For more information, see `Encrypt log data in CloudWatch Logs using AWS Key Management Service <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_group_class(self) -> typing.Optional[builtins.str]:
        '''Specifies the log group class for this log group. There are two classes:.

        - The ``Standard`` log class supports all CloudWatch Logs features.
        - The ``Infrequent Access`` log class supports a subset of CloudWatch Logs features and incurs lower costs.

        For details about the features supported by each class, see `Log classes <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html>`_

        :default: - "STANDARD"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-loggroupclass
        '''
        result = self._values.get("log_group_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the log group.

        If you don't specify a name, AWS CloudFormation generates a unique ID for the log group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-loggroupname
        '''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_policy_document(self) -> typing.Any:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-resourcepolicydocument
        '''
        result = self._values.get("resource_policy_document")
        return typing.cast(typing.Any, result)

    @builtins.property
    def retention_in_days(self) -> typing.Optional[jsii.Number]:
        '''The number of days to retain the log events in the specified log group.

        Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, and 3653.

        To set a log group so that its log events do not expire, use `DeleteRetentionPolicy <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-retentionindays
        '''
        result = self._values.get("retention_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the log group.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLogGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLogStream(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnLogStream",
):
    '''The ``AWS::Logs::LogStream`` resource specifies an Amazon CloudWatch Logs log stream in a specific log group.

    A log stream represents the sequence of events coming from an application instance or resource that you are monitoring.

    There is no limit on the number of log streams that you can create for a log group.

    You must use the following guidelines when naming a log stream:

    - Log stream names must be unique within the log group.
    - Log stream names can be between 1 and 512 characters long.
    - The ':' (colon) and '*' (asterisk) characters are not allowed.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html
    :cloudformationResource: AWS::Logs::LogStream
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_log_stream = logs.CfnLogStream(self, "MyCfnLogStream",
            log_group_name="logGroupName",
        
            # the properties below are optional
            log_stream_name="logStreamName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        log_group_name: builtins.str,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param log_group_name: The name of the log group where the log stream is created.
        :param log_stream_name: The name of the log stream. The name must be unique within the log group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68392ef44019b9b5ee681acb5bd13c481e1cc999bc1f1773e84c70b5a04190b7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLogStreamProps(
            log_group_name=log_group_name, log_stream_name=log_stream_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64fb9d8e354f9197a9998608e06c1be2deb6b929ddb7835470385c91e16d110a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ec4cadc779471f71fa1f1b77d2bda5c706e530b0ead1517f46ec34940fee5da)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        '''The name of the log group where the log stream is created.'''
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28f49c7b712326ca2be5a290a29a4430589b6c15c4da1f34afb773fcc0456112)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''The name of the log stream.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamName"))

    @log_stream_name.setter
    def log_stream_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e3f8ff96c3dac6c45a8d31d07a3223b27eebb1e1c6aa1676d6cf0cfc0bcacb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamName", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnLogStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class CfnLogStreamProps:
    def __init__(
        self,
        *,
        log_group_name: builtins.str,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnLogStream``.

        :param log_group_name: The name of the log group where the log stream is created.
        :param log_stream_name: The name of the log stream. The name must be unique within the log group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_log_stream_props = logs.CfnLogStreamProps(
                log_group_name="logGroupName",
            
                # the properties below are optional
                log_stream_name="logStreamName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab2d708d8a8c684eb8753554b20ecf7de790ffc112520d594cacb903aff379ea)
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_group_name": log_group_name,
        }
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''The name of the log group where the log stream is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html#cfn-logs-logstream-loggroupname
        '''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''The name of the log stream.

        The name must be unique within the log group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html#cfn-logs-logstream-logstreamname
        '''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLogStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMetricFilter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnMetricFilter",
):
    '''The ``AWS::Logs::MetricFilter`` resource specifies a metric filter that describes how CloudWatch Logs extracts information from logs and transforms it into Amazon CloudWatch metrics.

    If you have multiple metric filters that are associated with a log group, all the filters are applied to the log streams in that group.

    The maximum number of metric filters that can be associated with a log group is 100.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html
    :cloudformationResource: AWS::Logs::MetricFilter
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_metric_filter = logs.CfnMetricFilter(self, "MyCfnMetricFilter",
            filter_pattern="filterPattern",
            log_group_name="logGroupName",
            metric_transformations=[logs.CfnMetricFilter.MetricTransformationProperty(
                metric_name="metricName",
                metric_namespace="metricNamespace",
                metric_value="metricValue",
        
                # the properties below are optional
                default_value=123,
                dimensions=[logs.CfnMetricFilter.DimensionProperty(
                    key="key",
                    value="value"
                )],
                unit="unit"
            )],
        
            # the properties below are optional
            apply_on_transformed_logs=False,
            filter_name="filterName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        filter_pattern: builtins.str,
        log_group_name: builtins.str,
        metric_transformations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMetricFilter.MetricTransformationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        apply_on_transformed_logs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        filter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param filter_pattern: A filter pattern for extracting metric data out of ingested log events. For more information, see `Filter and Pattern Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`_ .
        :param log_group_name: The name of an existing log group that you want to associate with this metric filter.
        :param metric_transformations: The metric transformations.
        :param apply_on_transformed_logs: This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see `PutTransformer <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html>`_ . If this value is ``true`` , the metric filter is applied on the transformed version of the log events instead of the original ingested log events.
        :param filter_name: The name of the metric filter.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaa6a2018a5f10ec1a79f547b81a628d6f434d037b49c5975131bba2d6fd2786)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMetricFilterProps(
            filter_pattern=filter_pattern,
            log_group_name=log_group_name,
            metric_transformations=metric_transformations,
            apply_on_transformed_logs=apply_on_transformed_logs,
            filter_name=filter_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa5f65c3d38181c3265e71ca5f37737480594a08405697ef96fc18254e2a9899)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aed2b5842b90369a626b9acdfbfb87dab07b9debcde1b1964b8b0dabb330ea2e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="filterPattern")
    def filter_pattern(self) -> builtins.str:
        '''A filter pattern for extracting metric data out of ingested log events.'''
        return typing.cast(builtins.str, jsii.get(self, "filterPattern"))

    @filter_pattern.setter
    def filter_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fdc6521987ce3f017024e20e1e0fb59a35415aa424ed169b346a59793c88b73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterPattern", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        '''The name of an existing log group that you want to associate with this metric filter.'''
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae16ea786b9d9ed9d5bfe824932074163b1aa6379bed22eb2671f3ed0818bf26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="metricTransformations")
    def metric_transformations(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricFilter.MetricTransformationProperty"]]]:
        '''The metric transformations.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricFilter.MetricTransformationProperty"]]], jsii.get(self, "metricTransformations"))

    @metric_transformations.setter
    def metric_transformations(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricFilter.MetricTransformationProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e42e8a9e143351ba28d452f886abff3c46adff74b2c2fc8876dc18aabf51dcba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricTransformations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="applyOnTransformedLogs")
    def apply_on_transformed_logs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''This parameter is valid only for log groups that have an active log transformer.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "applyOnTransformedLogs"))

    @apply_on_transformed_logs.setter
    def apply_on_transformed_logs(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ace95a6c73bb2a95ee90d8e4e4ad81a77108a607e59d44e12214965f5ebf9073)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyOnTransformedLogs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="filterName")
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric filter.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterName"))

    @filter_name.setter
    def filter_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed6515d6733ea675274296cf9952fb0b41bd1778277ae74bde9739d81a205382)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterName", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnMetricFilter.DimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class DimensionProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''Specifies the CloudWatch metric dimensions to publish with this metric.

            Because dimensions are part of the unique identifier for a metric, whenever a unique dimension name/value pair is extracted from your logs, you are creating a new variation of that metric.

            For more information about publishing dimensions with metrics created by metric filters, see `Publishing dimensions with metrics from values in JSON or space-delimited log events <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html#logs-metric-filters-dimensions>`_ .
            .. epigraph::

               Metrics extracted from log events are charged as custom metrics. To prevent unexpected high charges, do not specify high-cardinality fields such as ``IPAddress`` or ``requestID`` as dimensions. Each different value found for a dimension is treated as a separate metric and accrues charges as a separate custom metric.

               To help prevent accidental high charges, Amazon disables a metric filter if it generates 1000 different name/value pairs for the dimensions that you have specified within a certain amount of time.

               You can also set up a billing alarm to alert you if your charges are higher than expected. For more information, see `Creating a Billing Alarm to Monitor Your Estimated AWS Charges <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html>`_ .

            :param key: The name for the CloudWatch metric dimension that the metric filter creates. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (:).
            :param value: The log event field that will contain the value for this dimension. This dimension will only be published for a metric if the value is found in the log event. For example, ``$.eventType`` for JSON log events, or ``$server`` for space-delimited log events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                dimension_property = logs.CfnMetricFilter.DimensionProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9fad5f3c7dec2c3bafa74c42e2398a046d9cc8c861abfac39c6e9e77c2b65b41)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The name for the CloudWatch metric dimension that the metric filter creates.

            Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (:).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html#cfn-logs-metricfilter-dimension-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The log event field that will contain the value for this dimension.

            This dimension will only be published for a metric if the value is found in the log event. For example, ``$.eventType`` for JSON log events, or ``$server`` for space-delimited log events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-dimension.html#cfn-logs-metricfilter-dimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnMetricFilter.MetricTransformationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "metric_namespace": "metricNamespace",
            "metric_value": "metricValue",
            "default_value": "defaultValue",
            "dimensions": "dimensions",
            "unit": "unit",
        },
    )
    class MetricTransformationProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            metric_namespace: builtins.str,
            metric_value: builtins.str,
            default_value: typing.Optional[jsii.Number] = None,
            dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMetricFilter.DimensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``MetricTransformation`` is a property of the ``AWS::Logs::MetricFilter`` resource that describes how to transform log streams into a CloudWatch metric.

            :param metric_name: The name of the CloudWatch metric.
            :param metric_namespace: A custom namespace to contain your metric in CloudWatch. Use namespaces to group together metrics that are similar. For more information, see `Namespaces <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace>`_ .
            :param metric_value: The value that is published to the CloudWatch metric. For example, if you're counting the occurrences of a particular term like ``Error`` , specify 1 for the metric value. If you're counting the number of bytes transferred, reference the value that is in the log event by using $. followed by the name of the field that you specified in the filter pattern, such as ``$.size`` .
            :param default_value: (Optional) The value to emit when a filter pattern does not match a log event. This value can be null.
            :param dimensions: The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions. .. epigraph:: Metrics extracted from log events are charged as custom metrics. To prevent unexpected high charges, do not specify high-cardinality fields such as ``IPAddress`` or ``requestID`` as dimensions. Each different value found for a dimension is treated as a separate metric and accrues charges as a separate custom metric. CloudWatch Logs disables a metric filter if it generates 1000 different name/value pairs for your specified dimensions within a certain amount of time. This helps to prevent accidental high charges. You can also set up a billing alarm to alert you if your charges are higher than expected. For more information, see `Creating a Billing Alarm to Monitor Your Estimated AWS Charges <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html>`_ .
            :param unit: The unit to assign to the metric. If you omit this, the unit is set as ``None`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                metric_transformation_property = logs.CfnMetricFilter.MetricTransformationProperty(
                    metric_name="metricName",
                    metric_namespace="metricNamespace",
                    metric_value="metricValue",
                
                    # the properties below are optional
                    default_value=123,
                    dimensions=[logs.CfnMetricFilter.DimensionProperty(
                        key="key",
                        value="value"
                    )],
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8989e36bc84de1e18d069af1bb22845cf409685cbd8a8fe22cd131474e0d7958)
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument metric_namespace", value=metric_namespace, expected_type=type_hints["metric_namespace"])
                check_type(argname="argument metric_value", value=metric_value, expected_type=type_hints["metric_value"])
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "metric_name": metric_name,
                "metric_namespace": metric_namespace,
                "metric_value": metric_value,
            }
            if default_value is not None:
                self._values["default_value"] = default_value
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''The name of the CloudWatch metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_namespace(self) -> builtins.str:
            '''A custom namespace to contain your metric in CloudWatch.

            Use namespaces to group together metrics that are similar. For more information, see `Namespaces <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-metricnamespace
            '''
            result = self._values.get("metric_namespace")
            assert result is not None, "Required property 'metric_namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_value(self) -> builtins.str:
            '''The value that is published to the CloudWatch metric.

            For example, if you're counting the occurrences of a particular term like ``Error`` , specify 1 for the metric value. If you're counting the number of bytes transferred, reference the value that is in the log event by using $. followed by the name of the field that you specified in the filter pattern, such as ``$.size`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-metricvalue
            '''
            result = self._values.get("metric_value")
            assert result is not None, "Required property 'metric_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def default_value(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The value to emit when a filter pattern does not match a log event.

            This value can be null.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricFilter.DimensionProperty"]]]]:
            '''The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions.

            .. epigraph::

               Metrics extracted from log events are charged as custom metrics. To prevent unexpected high charges, do not specify high-cardinality fields such as ``IPAddress`` or ``requestID`` as dimensions. Each different value found for a dimension is treated as a separate metric and accrues charges as a separate custom metric.

               CloudWatch Logs disables a metric filter if it generates 1000 different name/value pairs for your specified dimensions within a certain amount of time. This helps to prevent accidental high charges.

               You can also set up a billing alarm to alert you if your charges are higher than expected. For more information, see `Creating a Billing Alarm to Monitor Your Estimated AWS Charges <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMetricFilter.DimensionProperty"]]]], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''The unit to assign to the metric.

            If you omit this, the unit is set as ``None`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricTransformationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnMetricFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "filter_pattern": "filterPattern",
        "log_group_name": "logGroupName",
        "metric_transformations": "metricTransformations",
        "apply_on_transformed_logs": "applyOnTransformedLogs",
        "filter_name": "filterName",
    },
)
class CfnMetricFilterProps:
    def __init__(
        self,
        *,
        filter_pattern: builtins.str,
        log_group_name: builtins.str,
        metric_transformations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricFilter.MetricTransformationProperty, typing.Dict[builtins.str, typing.Any]]]]],
        apply_on_transformed_logs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        filter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMetricFilter``.

        :param filter_pattern: A filter pattern for extracting metric data out of ingested log events. For more information, see `Filter and Pattern Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`_ .
        :param log_group_name: The name of an existing log group that you want to associate with this metric filter.
        :param metric_transformations: The metric transformations.
        :param apply_on_transformed_logs: This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see `PutTransformer <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html>`_ . If this value is ``true`` , the metric filter is applied on the transformed version of the log events instead of the original ingested log events.
        :param filter_name: The name of the metric filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_metric_filter_props = logs.CfnMetricFilterProps(
                filter_pattern="filterPattern",
                log_group_name="logGroupName",
                metric_transformations=[logs.CfnMetricFilter.MetricTransformationProperty(
                    metric_name="metricName",
                    metric_namespace="metricNamespace",
                    metric_value="metricValue",
            
                    # the properties below are optional
                    default_value=123,
                    dimensions=[logs.CfnMetricFilter.DimensionProperty(
                        key="key",
                        value="value"
                    )],
                    unit="unit"
                )],
            
                # the properties below are optional
                apply_on_transformed_logs=False,
                filter_name="filterName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__524e2e94ad4843f66081953f516426a1396490f271842ac0c5ca7c7ecb84011e)
            check_type(argname="argument filter_pattern", value=filter_pattern, expected_type=type_hints["filter_pattern"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument metric_transformations", value=metric_transformations, expected_type=type_hints["metric_transformations"])
            check_type(argname="argument apply_on_transformed_logs", value=apply_on_transformed_logs, expected_type=type_hints["apply_on_transformed_logs"])
            check_type(argname="argument filter_name", value=filter_name, expected_type=type_hints["filter_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filter_pattern": filter_pattern,
            "log_group_name": log_group_name,
            "metric_transformations": metric_transformations,
        }
        if apply_on_transformed_logs is not None:
            self._values["apply_on_transformed_logs"] = apply_on_transformed_logs
        if filter_name is not None:
            self._values["filter_name"] = filter_name

    @builtins.property
    def filter_pattern(self) -> builtins.str:
        '''A filter pattern for extracting metric data out of ingested log events.

        For more information, see `Filter and Pattern Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-logs-metricfilter-filterpattern
        '''
        result = self._values.get("filter_pattern")
        assert result is not None, "Required property 'filter_pattern' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''The name of an existing log group that you want to associate with this metric filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-logs-metricfilter-loggroupname
        '''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_transformations(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMetricFilter.MetricTransformationProperty]]]:
        '''The metric transformations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-logs-metricfilter-metrictransformations
        '''
        result = self._values.get("metric_transformations")
        assert result is not None, "Required property 'metric_transformations' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMetricFilter.MetricTransformationProperty]]], result)

    @builtins.property
    def apply_on_transformed_logs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''This parameter is valid only for log groups that have an active log transformer.

        For more information about log transformers, see `PutTransformer <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html>`_ .

        If this value is ``true`` , the metric filter is applied on the transformed version of the log events instead of the original ingested log events.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-logs-metricfilter-applyontransformedlogs
        '''
        result = self._values.get("apply_on_transformed_logs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-logs-metricfilter-filtername
        '''
        result = self._values.get("filter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMetricFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnQueryDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnQueryDefinition",
):
    '''Creates a query definition for CloudWatch Logs Insights.

    For more information, see `Analyzing Log Data with CloudWatch Logs Insights <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html
    :cloudformationResource: AWS::Logs::QueryDefinition
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_query_definition = logs.CfnQueryDefinition(self, "MyCfnQueryDefinition",
            name="name",
            query_string="queryString",
        
            # the properties below are optional
            log_group_names=["logGroupNames"],
            query_language="queryLanguage"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        query_string: builtins.str,
        log_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_language: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A name for the query definition. .. epigraph:: You can use the name to create a folder structure for your queries. To create a folder, use a forward slash (/) to prefix your desired query name with your desired folder name. For example, ``*folder-name* / *query-name*`` .
        :param query_string: The query string to use for this query definition. For more information, see `CloudWatch Logs Insights Query Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html>`_ .
        :param log_group_names: Use this parameter if you want the query to query only certain log groups.
        :param query_language: The query language used for this query. For more information about the query languages that CloudWatch Logs supports, see `Supported query languages <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html>`_ . Default: - "CWLI"
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d10075ae036bdf9f4049570cf68ab72c79ee717f007f45628b52d2ea5aa64ae)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnQueryDefinitionProps(
            name=name,
            query_string=query_string,
            log_group_names=log_group_names,
            query_language=query_language,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dd626642ab8510fa9005787d00adbbd508a543616e89979ad57ba0be9f38bad)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d445c0915cb40f09b489a0802b2b2b0c035e244acf419b2452990fd8568900fe)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrQueryDefinitionId")
    def attr_query_definition_id(self) -> builtins.str:
        '''The ID of the query definition.

        :cloudformationAttribute: QueryDefinitionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQueryDefinitionId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the query definition.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a970de5992ab8622f5a1c04c70c2066cfaee94719e9aba8c8edbe863ddcce298)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> builtins.str:
        '''The query string to use for this query definition.'''
        return typing.cast(builtins.str, jsii.get(self, "queryString"))

    @query_string.setter
    def query_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__005c13f188808f7829e17c5ce9ca7e9ae473e50b0b0b1ed4f95b8e35cfd6a6df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryString", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logGroupNames")
    def log_group_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Use this parameter if you want the query to query only certain log groups.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "logGroupNames"))

    @log_group_names.setter
    def log_group_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1d922394643a9758400b7e596dd6c6fe61ab7e1fb96d4a93a7061d0e3b5c39d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupNames", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="queryLanguage")
    def query_language(self) -> typing.Optional[builtins.str]:
        '''The query language used for this query.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryLanguage"))

    @query_language.setter
    def query_language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26eee5ed8d061567be82d404491f5a77b58778884692c8fbe2cf1ded06c91cd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryLanguage", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnQueryDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "query_string": "queryString",
        "log_group_names": "logGroupNames",
        "query_language": "queryLanguage",
    },
)
class CfnQueryDefinitionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        query_string: builtins.str,
        log_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_language: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnQueryDefinition``.

        :param name: A name for the query definition. .. epigraph:: You can use the name to create a folder structure for your queries. To create a folder, use a forward slash (/) to prefix your desired query name with your desired folder name. For example, ``*folder-name* / *query-name*`` .
        :param query_string: The query string to use for this query definition. For more information, see `CloudWatch Logs Insights Query Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html>`_ .
        :param log_group_names: Use this parameter if you want the query to query only certain log groups.
        :param query_language: The query language used for this query. For more information about the query languages that CloudWatch Logs supports, see `Supported query languages <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html>`_ . Default: - "CWLI"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_query_definition_props = logs.CfnQueryDefinitionProps(
                name="name",
                query_string="queryString",
            
                # the properties below are optional
                log_group_names=["logGroupNames"],
                query_language="queryLanguage"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd7180e50961abf6b838dfc21ba186cc5b2c551eae8357613767f891abe51780)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument log_group_names", value=log_group_names, expected_type=type_hints["log_group_names"])
            check_type(argname="argument query_language", value=query_language, expected_type=type_hints["query_language"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "query_string": query_string,
        }
        if log_group_names is not None:
            self._values["log_group_names"] = log_group_names
        if query_language is not None:
            self._values["query_language"] = query_language

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the query definition.

        .. epigraph::

           You can use the name to create a folder structure for your queries. To create a folder, use a forward slash (/) to prefix your desired query name with your desired folder name. For example, ``*folder-name* / *query-name*`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html#cfn-logs-querydefinition-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_string(self) -> builtins.str:
        '''The query string to use for this query definition.

        For more information, see `CloudWatch Logs Insights Query Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html#cfn-logs-querydefinition-querystring
        '''
        result = self._values.get("query_string")
        assert result is not None, "Required property 'query_string' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_group_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Use this parameter if you want the query to query only certain log groups.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html#cfn-logs-querydefinition-loggroupnames
        '''
        result = self._values.get("log_group_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def query_language(self) -> typing.Optional[builtins.str]:
        '''The query language used for this query.

        For more information about the query languages that CloudWatch Logs supports, see `Supported query languages <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html>`_ .

        :default: - "CWLI"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-querydefinition.html#cfn-logs-querydefinition-querylanguage
        '''
        result = self._values.get("query_language")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQueryDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourcePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnResourcePolicy",
):
    '''Creates or updates a resource policy that allows other AWS services to put log events to this account.

    An account can have up to 10 resource policies per AWS Region.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-resourcepolicy.html
    :cloudformationResource: AWS::Logs::ResourcePolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_resource_policy = logs.CfnResourcePolicy(self, "MyCfnResourcePolicy",
            policy_document="policyDocument",
            policy_name="policyName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_document: builtins.str,
        policy_name: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy_document: The details of the policy. It must be formatted in JSON, and you must use backslashes to escape characters that need to be escaped in JSON strings, such as double quote marks.
        :param policy_name: The name of the resource policy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96eb8f500492c7ddcaba9f292d2aa1c488941affca3b4911cd4ce9636c1ce721)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourcePolicyProps(
            policy_document=policy_document, policy_name=policy_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a2e3f9cc2e418bf4cc4f8f63fc54eed1907f2c1b38483cc8c59d2f8b653c69f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__94bd685f258ef991a46514a1b4f58ba0b0bf9314fc8055746b8652c965857253)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> builtins.str:
        '''The details of the policy.'''
        return typing.cast(builtins.str, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fd3f538cb966d97639dd18283329cf7c5f581a2f069d6d37e7cd0ab5cedb7fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of the resource policy.'''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de9476941a8f893fee016885d888db6d17d101f4ad44646ba809adde15261aed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnResourcePolicyProps",
    jsii_struct_bases=[],
    name_mapping={"policy_document": "policyDocument", "policy_name": "policyName"},
)
class CfnResourcePolicyProps:
    def __init__(
        self,
        *,
        policy_document: builtins.str,
        policy_name: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnResourcePolicy``.

        :param policy_document: The details of the policy. It must be formatted in JSON, and you must use backslashes to escape characters that need to be escaped in JSON strings, such as double quote marks.
        :param policy_name: The name of the resource policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-resourcepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_resource_policy_props = logs.CfnResourcePolicyProps(
                policy_document="policyDocument",
                policy_name="policyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ab184a479fd32db068d45168ec1b6bf45cf1a4a3d64847b519a088388c84df8)
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_document": policy_document,
            "policy_name": policy_name,
        }

    @builtins.property
    def policy_document(self) -> builtins.str:
        '''The details of the policy.

        It must be formatted in JSON, and you must use backslashes to escape characters that need to be escaped in JSON strings, such as double quote marks.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-resourcepolicy.html#cfn-logs-resourcepolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The name of the resource policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-resourcepolicy.html#cfn-logs-resourcepolicy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourcePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSubscriptionFilter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnSubscriptionFilter",
):
    '''The ``AWS::Logs::SubscriptionFilter`` resource specifies a subscription filter and associates it with the specified log group.

    Subscription filters allow you to subscribe to a real-time stream of log events and have them delivered to a specific destination. Currently, the supported destinations are:

    - An Amazon Kinesis data stream belonging to the same account as the subscription filter, for same-account delivery.
    - A logical destination that belongs to a different account, for cross-account delivery.
    - An Amazon Kinesis Firehose delivery stream that belongs to the same account as the subscription filter, for same-account delivery.
    - An AWS Lambda function that belongs to the same account as the subscription filter, for same-account delivery.

    There can be as many as two subscription filters associated with a log group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html
    :cloudformationResource: AWS::Logs::SubscriptionFilter
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_subscription_filter = logs.CfnSubscriptionFilter(self, "MyCfnSubscriptionFilter",
            destination_arn="destinationArn",
            filter_pattern="filterPattern",
            log_group_name="logGroupName",
        
            # the properties below are optional
            apply_on_transformed_logs=False,
            distribution="distribution",
            filter_name="filterName",
            role_arn="roleArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        destination_arn: builtins.str,
        filter_pattern: builtins.str,
        log_group_name: builtins.str,
        apply_on_transformed_logs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        distribution: typing.Optional[builtins.str] = None,
        filter_name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination_arn: The Amazon Resource Name (ARN) of the destination.
        :param filter_pattern: The filtering expressions that restrict what gets delivered to the destination AWS resource. For more information about the filter pattern syntax, see `Filter and Pattern Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`_ .
        :param log_group_name: The log group to associate with the subscription filter. All log events that are uploaded to this log group are filtered and delivered to the specified AWS resource if the filter pattern matches the log events.
        :param apply_on_transformed_logs: This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see `PutTransformer <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html>`_ . If this value is ``true`` , the subscription filter is applied on the transformed version of the log events instead of the original ingested log events.
        :param distribution: The method used to distribute log data to the destination, which can be either random or grouped by log stream.
        :param filter_name: The name of the subscription filter.
        :param role_arn: The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c7a154450656ee0f7e524d596c7e140faad893a71a7c8b9b8a85fe730a1dcf9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSubscriptionFilterProps(
            destination_arn=destination_arn,
            filter_pattern=filter_pattern,
            log_group_name=log_group_name,
            apply_on_transformed_logs=apply_on_transformed_logs,
            distribution=distribution,
            filter_name=filter_name,
            role_arn=role_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fd7a0e99337509280da552b557b613a8fcb858acf9e84e9aacbe572366bca99)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c7e4c15a871de67a808634e0ce4138af489acd8a95e0b0e5e5cb1829aa66805)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="destinationArn")
    def destination_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the destination.'''
        return typing.cast(builtins.str, jsii.get(self, "destinationArn"))

    @destination_arn.setter
    def destination_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcf92dedad133b23741e31710f66784d3728a1a96f5d9b514b8a80f012d7b84c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="filterPattern")
    def filter_pattern(self) -> builtins.str:
        '''The filtering expressions that restrict what gets delivered to the destination AWS resource.'''
        return typing.cast(builtins.str, jsii.get(self, "filterPattern"))

    @filter_pattern.setter
    def filter_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5af0335707946ab6b7311049c978104cfb68f9d36688e1bf25585706ebcbb08a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterPattern", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        '''The log group to associate with the subscription filter.'''
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfa4dbdd67c0f388eefe38fe86bae9148a44785d56910a1951619c1205e4eb56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="applyOnTransformedLogs")
    def apply_on_transformed_logs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''This parameter is valid only for log groups that have an active log transformer.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "applyOnTransformedLogs"))

    @apply_on_transformed_logs.setter
    def apply_on_transformed_logs(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9575bfc33fe73bebe8b16e0496334b59edcb3f2b7fbf109199f2fc70d96487c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyOnTransformedLogs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="distribution")
    def distribution(self) -> typing.Optional[builtins.str]:
        '''The method used to distribute log data to the destination, which can be either random or grouped by log stream.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distribution"))

    @distribution.setter
    def distribution(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4730d6086a07b6e1f3b3d7251138c936aa909d17834505b0c341ec6b421adf19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distribution", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="filterName")
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subscription filter.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterName"))

    @filter_name.setter
    def filter_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ccf855abfc15a31ed667e6619b6f1711fc4ef753c64ec0b754421d81c8edb75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cdca0b99d7b39060b314b323073c0a48e25972ff085f24a455a00339addb4ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnSubscriptionFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_arn": "destinationArn",
        "filter_pattern": "filterPattern",
        "log_group_name": "logGroupName",
        "apply_on_transformed_logs": "applyOnTransformedLogs",
        "distribution": "distribution",
        "filter_name": "filterName",
        "role_arn": "roleArn",
    },
)
class CfnSubscriptionFilterProps:
    def __init__(
        self,
        *,
        destination_arn: builtins.str,
        filter_pattern: builtins.str,
        log_group_name: builtins.str,
        apply_on_transformed_logs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        distribution: typing.Optional[builtins.str] = None,
        filter_name: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSubscriptionFilter``.

        :param destination_arn: The Amazon Resource Name (ARN) of the destination.
        :param filter_pattern: The filtering expressions that restrict what gets delivered to the destination AWS resource. For more information about the filter pattern syntax, see `Filter and Pattern Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`_ .
        :param log_group_name: The log group to associate with the subscription filter. All log events that are uploaded to this log group are filtered and delivered to the specified AWS resource if the filter pattern matches the log events.
        :param apply_on_transformed_logs: This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see `PutTransformer <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html>`_ . If this value is ``true`` , the subscription filter is applied on the transformed version of the log events instead of the original ingested log events.
        :param distribution: The method used to distribute log data to the destination, which can be either random or grouped by log stream.
        :param filter_name: The name of the subscription filter.
        :param role_arn: The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_subscription_filter_props = logs.CfnSubscriptionFilterProps(
                destination_arn="destinationArn",
                filter_pattern="filterPattern",
                log_group_name="logGroupName",
            
                # the properties below are optional
                apply_on_transformed_logs=False,
                distribution="distribution",
                filter_name="filterName",
                role_arn="roleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1250ecc947a5eb57e428cd8fedeb9ae0f6da4eb03c22d674fa019a076ee8b507)
            check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
            check_type(argname="argument filter_pattern", value=filter_pattern, expected_type=type_hints["filter_pattern"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument apply_on_transformed_logs", value=apply_on_transformed_logs, expected_type=type_hints["apply_on_transformed_logs"])
            check_type(argname="argument distribution", value=distribution, expected_type=type_hints["distribution"])
            check_type(argname="argument filter_name", value=filter_name, expected_type=type_hints["filter_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_arn": destination_arn,
            "filter_pattern": filter_pattern,
            "log_group_name": log_group_name,
        }
        if apply_on_transformed_logs is not None:
            self._values["apply_on_transformed_logs"] = apply_on_transformed_logs
        if distribution is not None:
            self._values["distribution"] = distribution
        if filter_name is not None:
            self._values["filter_name"] = filter_name
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def destination_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-destinationarn
        '''
        result = self._values.get("destination_arn")
        assert result is not None, "Required property 'destination_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter_pattern(self) -> builtins.str:
        '''The filtering expressions that restrict what gets delivered to the destination AWS resource.

        For more information about the filter pattern syntax, see `Filter and Pattern Syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-filterpattern
        '''
        result = self._values.get("filter_pattern")
        assert result is not None, "Required property 'filter_pattern' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''The log group to associate with the subscription filter.

        All log events that are uploaded to this log group are filtered and delivered to the specified AWS resource if the filter pattern matches the log events.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-loggroupname
        '''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def apply_on_transformed_logs(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''This parameter is valid only for log groups that have an active log transformer.

        For more information about log transformers, see `PutTransformer <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html>`_ .

        If this value is ``true`` , the subscription filter is applied on the transformed version of the log events instead of the original ingested log events.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-applyontransformedlogs
        '''
        result = self._values.get("apply_on_transformed_logs")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def distribution(self) -> typing.Optional[builtins.str]:
        '''The method used to distribute log data to the destination, which can be either random or grouped by log stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-distribution
        '''
        result = self._values.get("distribution")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subscription filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-filtername
        '''
        result = self._values.get("filter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream.

        You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-logs-subscriptionfilter-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSubscriptionFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTransformer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CfnTransformer",
):
    '''Creates or updates a *log transformer* for a single log group.

    You use log transformers to transform log events into a different format, making them easier for you to process and analyze. You can also transform logs from different sources into standardized formats that contains relevant, source-specific information.

    After you have created a transformer, CloudWatch Logs performs the transformations at the time of log ingestion. You can then refer to the transformed versions of the logs during operations such as querying with CloudWatch Logs Insights or creating metric filters or subscription filers.

    You can also use a transformer to copy metadata from metadata keys into the log events themselves. This metadata can include log group name, log stream name, account ID and Region.

    A transformer for a log group is a series of processors, where each processor applies one type of transformation to the log events ingested into this log group. The processors work one after another, in the order that you list them, like a pipeline. For more information about the available processors to use in a transformer, see `Processors that you can use <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-Processors>`_ .

    Having log events in standardized format enables visibility across your applications for your log analysis, reporting, and alarming needs. CloudWatch Logs provides transformation for common log types with out-of-the-box transformation templates for major AWS log sources such as VPC flow logs, Lambda, and Amazon RDS. You can use pre-built transformation templates or create custom transformation policies.

    You can create transformers only for the log groups in the Standard log class.

    You can also set up a transformer at the account level. For more information, see `PutAccountPolicy <https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutAccountPolicy.html>`_ . If there is both a log-group level transformer created with ``PutTransformer`` and an account-level transformer that could apply to the same log group, the log group uses only the log-group level transformer. It ignores the account-level transformer.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-transformer.html
    :cloudformationResource: AWS::Logs::Transformer
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        cfn_transformer = logs.CfnTransformer(self, "MyCfnTransformer",
            log_group_identifier="logGroupIdentifier",
            transformer_config=[logs.CfnTransformer.ProcessorProperty(
                add_keys=logs.CfnTransformer.AddKeysProperty(
                    entries=[logs.CfnTransformer.AddKeyEntryProperty(
                        key="key",
                        value="value",
        
                        # the properties below are optional
                        overwrite_if_exists=False
                    )]
                ),
                copy_value=logs.CfnTransformer.CopyValueProperty(
                    entries=[logs.CfnTransformer.CopyValueEntryProperty(
                        source="source",
                        target="target",
        
                        # the properties below are optional
                        overwrite_if_exists=False
                    )]
                ),
                csv=logs.CfnTransformer.CsvProperty(
                    columns=["columns"],
                    delimiter="delimiter",
                    quote_character="quoteCharacter",
                    source="source"
                ),
                date_time_converter=logs.CfnTransformer.DateTimeConverterProperty(
                    match_patterns=["matchPatterns"],
                    source="source",
                    target="target",
        
                    # the properties below are optional
                    locale="locale",
                    source_timezone="sourceTimezone",
                    target_format="targetFormat",
                    target_timezone="targetTimezone"
                ),
                delete_keys=logs.CfnTransformer.DeleteKeysProperty(
                    with_keys=["withKeys"]
                ),
                grok=logs.CfnTransformer.GrokProperty(
                    match="match",
        
                    # the properties below are optional
                    source="source"
                ),
                list_to_map=logs.CfnTransformer.ListToMapProperty(
                    key="key",
                    source="source",
        
                    # the properties below are optional
                    flatten=False,
                    flattened_element="flattenedElement",
                    target="target",
                    value_key="valueKey"
                ),
                lower_case_string=logs.CfnTransformer.LowerCaseStringProperty(
                    with_keys=["withKeys"]
                ),
                move_keys=logs.CfnTransformer.MoveKeysProperty(
                    entries=[logs.CfnTransformer.MoveKeyEntryProperty(
                        source="source",
                        target="target",
        
                        # the properties below are optional
                        overwrite_if_exists=False
                    )]
                ),
                parse_cloudfront=logs.CfnTransformer.ParseCloudfrontProperty(
                    source="source"
                ),
                parse_json=logs.CfnTransformer.ParseJSONProperty(
                    destination="destination",
                    source="source"
                ),
                parse_key_value=logs.CfnTransformer.ParseKeyValueProperty(
                    destination="destination",
                    field_delimiter="fieldDelimiter",
                    key_prefix="keyPrefix",
                    key_value_delimiter="keyValueDelimiter",
                    non_match_value="nonMatchValue",
                    overwrite_if_exists=False,
                    source="source"
                ),
                parse_postgres=logs.CfnTransformer.ParsePostgresProperty(
                    source="source"
                ),
                parse_route53=logs.CfnTransformer.ParseRoute53Property(
                    source="source"
                ),
                parse_to_ocsf=logs.CfnTransformer.ParseToOCSFProperty(
                    event_source="eventSource",
                    ocsf_version="ocsfVersion",
        
                    # the properties below are optional
                    source="source"
                ),
                parse_vpc=logs.CfnTransformer.ParseVPCProperty(
                    source="source"
                ),
                parse_waf=logs.CfnTransformer.ParseWAFProperty(
                    source="source"
                ),
                rename_keys=logs.CfnTransformer.RenameKeysProperty(
                    entries=[logs.CfnTransformer.RenameKeyEntryProperty(
                        key="key",
                        rename_to="renameTo",
        
                        # the properties below are optional
                        overwrite_if_exists=False
                    )]
                ),
                split_string=logs.CfnTransformer.SplitStringProperty(
                    entries=[logs.CfnTransformer.SplitStringEntryProperty(
                        delimiter="delimiter",
                        source="source"
                    )]
                ),
                substitute_string=logs.CfnTransformer.SubstituteStringProperty(
                    entries=[logs.CfnTransformer.SubstituteStringEntryProperty(
                        from="from",
                        source="source",
                        to="to"
                    )]
                ),
                trim_string=logs.CfnTransformer.TrimStringProperty(
                    with_keys=["withKeys"]
                ),
                type_converter=logs.CfnTransformer.TypeConverterProperty(
                    entries=[logs.CfnTransformer.TypeConverterEntryProperty(
                        key="key",
                        type="type"
                    )]
                ),
                upper_case_string=logs.CfnTransformer.UpperCaseStringProperty(
                    with_keys=["withKeys"]
                )
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        log_group_identifier: builtins.str,
        transformer_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.ProcessorProperty", typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param log_group_identifier: Specify either the name or ARN of the log group to create the transformer for.
        :param transformer_config: This structure is an array that contains the configuration of this log transformer. A log transformer is an array of processors, where each processor applies one type of transformation to the log events that are ingested.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0c03d4d08bfd70f5af2f86af828209e7341e321bb84773f474ad12623e4f673)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTransformerProps(
            log_group_identifier=log_group_identifier,
            transformer_config=transformer_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c5843dc7e0596939f9aed5094347614692a37bcb3deec88eef302aa9f4a3949)
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
            type_hints = typing.get_type_hints(_typecheckingstub__19ee38bba53fb110c3d77fa4bcc6fc2150881fe447a82d6fd44edb6f6b793cbb)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="logGroupIdentifier")
    def log_group_identifier(self) -> builtins.str:
        '''Specify either the name or ARN of the log group to create the transformer for.'''
        return typing.cast(builtins.str, jsii.get(self, "logGroupIdentifier"))

    @log_group_identifier.setter
    def log_group_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f753044b1fead2c548a763e25eaaf3b48d20a74b766e774ba28f4389d3b647ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="transformerConfig")
    def transformer_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ProcessorProperty"]]]:
        '''This structure is an array that contains the configuration of this log transformer.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ProcessorProperty"]]], jsii.get(self, "transformerConfig"))

    @transformer_config.setter
    def transformer_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ProcessorProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46991b9d950418a62c8d1284c385ff33c88585c1a5b8ba86a023f964716d83c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transformerConfig", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.AddKeyEntryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "key": "key",
            "value": "value",
            "overwrite_if_exists": "overwriteIfExists",
        },
    )
    class AddKeyEntryProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: builtins.str,
            overwrite_if_exists: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''This object defines one key that will be added with the `addKeys <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-addKey>`_ processor.

            :param key: The key of the new entry to be added to the log event.
            :param value: The value of the new entry to be added to the log event.
            :param overwrite_if_exists: Specifies whether to overwrite the value if the key already exists in the log event. If you omit this, the default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-addkeyentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                add_key_entry_property = logs.CfnTransformer.AddKeyEntryProperty(
                    key="key",
                    value="value",
                
                    # the properties below are optional
                    overwrite_if_exists=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__879568f32dc44bc4801f0d91ac950375c54ad1e240274f3d74b36735a63912cb)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument overwrite_if_exists", value=overwrite_if_exists, expected_type=type_hints["overwrite_if_exists"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }
            if overwrite_if_exists is not None:
                self._values["overwrite_if_exists"] = overwrite_if_exists

        @builtins.property
        def key(self) -> builtins.str:
            '''The key of the new entry to be added to the log event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-addkeyentry.html#cfn-logs-transformer-addkeyentry-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value of the new entry to be added to the log event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-addkeyentry.html#cfn-logs-transformer-addkeyentry-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def overwrite_if_exists(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether to overwrite the value if the key already exists in the log event.

            If you omit this, the default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-addkeyentry.html#cfn-logs-transformer-addkeyentry-overwriteifexists
            '''
            result = self._values.get("overwrite_if_exists")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddKeyEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.AddKeysProperty",
        jsii_struct_bases=[],
        name_mapping={"entries": "entries"},
    )
    class AddKeysProperty:
        def __init__(
            self,
            *,
            entries: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.AddKeyEntryProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''This processor adds new key-value pairs to the log event.

            For more information about this processor including examples, see `addKeys <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-addKeys>`_ in the *CloudWatch Logs User Guide* .

            :param entries: An array of objects, where each object contains the information about one key to add to the log event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-addkeys.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                add_keys_property = logs.CfnTransformer.AddKeysProperty(
                    entries=[logs.CfnTransformer.AddKeyEntryProperty(
                        key="key",
                        value="value",
                
                        # the properties below are optional
                        overwrite_if_exists=False
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3fc52570a1b3881374a9cb70551ee446a27ce71ba7d9ac9332130f1b362d8d9)
                check_type(argname="argument entries", value=entries, expected_type=type_hints["entries"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entries": entries,
            }

        @builtins.property
        def entries(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.AddKeyEntryProperty"]]]:
            '''An array of objects, where each object contains the information about one key to add to the log event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-addkeys.html#cfn-logs-transformer-addkeys-entries
            '''
            result = self._values.get("entries")
            assert result is not None, "Required property 'entries' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.AddKeyEntryProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddKeysProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.CopyValueEntryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source": "source",
            "target": "target",
            "overwrite_if_exists": "overwriteIfExists",
        },
    )
    class CopyValueEntryProperty:
        def __init__(
            self,
            *,
            source: builtins.str,
            target: builtins.str,
            overwrite_if_exists: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''This object defines one value to be copied with the `copyValue <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-copyValue>`_ processor.

            :param source: The key to copy.
            :param target: The key of the field to copy the value to.
            :param overwrite_if_exists: Specifies whether to overwrite the value if the destination key already exists. If you omit this, the default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-copyvalueentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                copy_value_entry_property = logs.CfnTransformer.CopyValueEntryProperty(
                    source="source",
                    target="target",
                
                    # the properties below are optional
                    overwrite_if_exists=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__770aa2786aabe822e197169c0efa5a50e7ed836e01b793d89c28592ddf4e8159)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
                check_type(argname="argument overwrite_if_exists", value=overwrite_if_exists, expected_type=type_hints["overwrite_if_exists"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source": source,
                "target": target,
            }
            if overwrite_if_exists is not None:
                self._values["overwrite_if_exists"] = overwrite_if_exists

        @builtins.property
        def source(self) -> builtins.str:
            '''The key to copy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-copyvalueentry.html#cfn-logs-transformer-copyvalueentry-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target(self) -> builtins.str:
            '''The key of the field to copy the value to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-copyvalueentry.html#cfn-logs-transformer-copyvalueentry-target
            '''
            result = self._values.get("target")
            assert result is not None, "Required property 'target' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def overwrite_if_exists(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether to overwrite the value if the destination key already exists.

            If you omit this, the default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-copyvalueentry.html#cfn-logs-transformer-copyvalueentry-overwriteifexists
            '''
            result = self._values.get("overwrite_if_exists")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CopyValueEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.CopyValueProperty",
        jsii_struct_bases=[],
        name_mapping={"entries": "entries"},
    )
    class CopyValueProperty:
        def __init__(
            self,
            *,
            entries: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.CopyValueEntryProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''This processor copies values within a log event.

            You can also use this processor to add metadata to log events by copying the values of the following metadata keys into the log events: ``@logGroupName`` , ``@logGroupStream`` , ``@accountId`` , ``@regionName`` .

            For more information about this processor including examples, see `copyValue <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-copyValue>`_ in the *CloudWatch Logs User Guide* .

            :param entries: An array of ``CopyValueEntry`` objects, where each object contains the information about one field value to copy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-copyvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                copy_value_property = logs.CfnTransformer.CopyValueProperty(
                    entries=[logs.CfnTransformer.CopyValueEntryProperty(
                        source="source",
                        target="target",
                
                        # the properties below are optional
                        overwrite_if_exists=False
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3d4839dece23811375e7ae8c44e802cb44e36138e19c2a7bf162dc3271f26eb)
                check_type(argname="argument entries", value=entries, expected_type=type_hints["entries"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entries": entries,
            }

        @builtins.property
        def entries(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.CopyValueEntryProperty"]]]:
            '''An array of ``CopyValueEntry`` objects, where each object contains the information about one field value to copy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-copyvalue.html#cfn-logs-transformer-copyvalue-entries
            '''
            result = self._values.get("entries")
            assert result is not None, "Required property 'entries' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.CopyValueEntryProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CopyValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.CsvProperty",
        jsii_struct_bases=[],
        name_mapping={
            "columns": "columns",
            "delimiter": "delimiter",
            "quote_character": "quoteCharacter",
            "source": "source",
        },
    )
    class CsvProperty:
        def __init__(
            self,
            *,
            columns: typing.Optional[typing.Sequence[builtins.str]] = None,
            delimiter: typing.Optional[builtins.str] = None,
            quote_character: typing.Optional[builtins.str] = None,
            source: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``CSV`` processor parses comma-separated values (CSV) from the log events into columns.

            For more information about this processor including examples, see `csv <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-csv>`_ in the *CloudWatch Logs User Guide* .

            :param columns: An array of names to use for the columns in the transformed log event. If you omit this, default column names ( ``[column_1, column_2 ...]`` ) are used.
            :param delimiter: The character used to separate each column in the original comma-separated value log event. If you omit this, the processor looks for the comma ``,`` character as the delimiter.
            :param quote_character: The character used used as a text qualifier for a single column of data. If you omit this, the double quotation mark ``"`` character is used.
            :param source: The path to the field in the log event that has the comma separated values to be parsed. If you omit this value, the whole log message is processed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-csv.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                csv_property = logs.CfnTransformer.CsvProperty(
                    columns=["columns"],
                    delimiter="delimiter",
                    quote_character="quoteCharacter",
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f1385464dc0aa2b930428f3a7b360b1e2046ff9ffcef856103ab40799795933d)
                check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
                check_type(argname="argument delimiter", value=delimiter, expected_type=type_hints["delimiter"])
                check_type(argname="argument quote_character", value=quote_character, expected_type=type_hints["quote_character"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if columns is not None:
                self._values["columns"] = columns
            if delimiter is not None:
                self._values["delimiter"] = delimiter
            if quote_character is not None:
                self._values["quote_character"] = quote_character
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def columns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of names to use for the columns in the transformed log event.

            If you omit this, default column names ( ``[column_1, column_2 ...]`` ) are used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-csv.html#cfn-logs-transformer-csv-columns
            '''
            result = self._values.get("columns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def delimiter(self) -> typing.Optional[builtins.str]:
            '''The character used to separate each column in the original comma-separated value log event.

            If you omit this, the processor looks for the comma ``,`` character as the delimiter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-csv.html#cfn-logs-transformer-csv-delimiter
            '''
            result = self._values.get("delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def quote_character(self) -> typing.Optional[builtins.str]:
            '''The character used used as a text qualifier for a single column of data.

            If you omit this, the double quotation mark ``"`` character is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-csv.html#cfn-logs-transformer-csv-quotecharacter
            '''
            result = self._values.get("quote_character")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''The path to the field in the log event that has the comma separated values to be parsed.

            If you omit this value, the whole log message is processed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-csv.html#cfn-logs-transformer-csv-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CsvProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.DateTimeConverterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "match_patterns": "matchPatterns",
            "source": "source",
            "target": "target",
            "locale": "locale",
            "source_timezone": "sourceTimezone",
            "target_format": "targetFormat",
            "target_timezone": "targetTimezone",
        },
    )
    class DateTimeConverterProperty:
        def __init__(
            self,
            *,
            match_patterns: typing.Sequence[builtins.str],
            source: builtins.str,
            target: builtins.str,
            locale: typing.Optional[builtins.str] = None,
            source_timezone: typing.Optional[builtins.str] = None,
            target_format: typing.Optional[builtins.str] = None,
            target_timezone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This processor converts a datetime string into a format that you specify.

            For more information about this processor including examples, see `datetimeConverter <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-datetimeConverter>`_ in the *CloudWatch Logs User Guide* .

            :param match_patterns: A list of patterns to match against the ``source`` field.
            :param source: The key to apply the date conversion to.
            :param target: The JSON field to store the result in.
            :param locale: The locale of the source field. If you omit this, the default of ``locale.ROOT`` is used.
            :param source_timezone: The time zone of the source field. If you omit this, the default used is the UTC zone.
            :param target_format: The datetime format to use for the converted data in the target field. If you omit this, the default of ``yyyy-MM-dd'T'HH:mm:ss.SSS'Z`` is used.
            :param target_timezone: The time zone of the target field. If you omit this, the default used is the UTC zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-datetimeconverter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                date_time_converter_property = logs.CfnTransformer.DateTimeConverterProperty(
                    match_patterns=["matchPatterns"],
                    source="source",
                    target="target",
                
                    # the properties below are optional
                    locale="locale",
                    source_timezone="sourceTimezone",
                    target_format="targetFormat",
                    target_timezone="targetTimezone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2af961327d1e6181fea10642711cd58b1ba36b3343696caa3884a622b90f1ab2)
                check_type(argname="argument match_patterns", value=match_patterns, expected_type=type_hints["match_patterns"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
                check_type(argname="argument locale", value=locale, expected_type=type_hints["locale"])
                check_type(argname="argument source_timezone", value=source_timezone, expected_type=type_hints["source_timezone"])
                check_type(argname="argument target_format", value=target_format, expected_type=type_hints["target_format"])
                check_type(argname="argument target_timezone", value=target_timezone, expected_type=type_hints["target_timezone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "match_patterns": match_patterns,
                "source": source,
                "target": target,
            }
            if locale is not None:
                self._values["locale"] = locale
            if source_timezone is not None:
                self._values["source_timezone"] = source_timezone
            if target_format is not None:
                self._values["target_format"] = target_format
            if target_timezone is not None:
                self._values["target_timezone"] = target_timezone

        @builtins.property
        def match_patterns(self) -> typing.List[builtins.str]:
            '''A list of patterns to match against the ``source`` field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-datetimeconverter.html#cfn-logs-transformer-datetimeconverter-matchpatterns
            '''
            result = self._values.get("match_patterns")
            assert result is not None, "Required property 'match_patterns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def source(self) -> builtins.str:
            '''The key to apply the date conversion to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-datetimeconverter.html#cfn-logs-transformer-datetimeconverter-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target(self) -> builtins.str:
            '''The JSON field to store the result in.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-datetimeconverter.html#cfn-logs-transformer-datetimeconverter-target
            '''
            result = self._values.get("target")
            assert result is not None, "Required property 'target' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def locale(self) -> typing.Optional[builtins.str]:
            '''The locale of the source field.

            If you omit this, the default of ``locale.ROOT`` is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-datetimeconverter.html#cfn-logs-transformer-datetimeconverter-locale
            '''
            result = self._values.get("locale")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_timezone(self) -> typing.Optional[builtins.str]:
            '''The time zone of the source field.

            If you omit this, the default used is the UTC zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-datetimeconverter.html#cfn-logs-transformer-datetimeconverter-sourcetimezone
            '''
            result = self._values.get("source_timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_format(self) -> typing.Optional[builtins.str]:
            '''The datetime format to use for the converted data in the target field.

            If you omit this, the default of ``yyyy-MM-dd'T'HH:mm:ss.SSS'Z`` is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-datetimeconverter.html#cfn-logs-transformer-datetimeconverter-targetformat
            '''
            result = self._values.get("target_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_timezone(self) -> typing.Optional[builtins.str]:
            '''The time zone of the target field.

            If you omit this, the default used is the UTC zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-datetimeconverter.html#cfn-logs-transformer-datetimeconverter-targettimezone
            '''
            result = self._values.get("target_timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DateTimeConverterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.DeleteKeysProperty",
        jsii_struct_bases=[],
        name_mapping={"with_keys": "withKeys"},
    )
    class DeleteKeysProperty:
        def __init__(self, *, with_keys: typing.Sequence[builtins.str]) -> None:
            '''This processor deletes entries from a log event. These entries are key-value pairs.

            For more information about this processor including examples, see `deleteKeys <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-deleteKeys>`_ in the *CloudWatch Logs User Guide* .

            :param with_keys: The list of keys to delete.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-deletekeys.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                delete_keys_property = logs.CfnTransformer.DeleteKeysProperty(
                    with_keys=["withKeys"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__889df1b9ea69f6af4e4c3b5c3713a2fe9738d592121c1e3fda581dd8eb227e7b)
                check_type(argname="argument with_keys", value=with_keys, expected_type=type_hints["with_keys"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "with_keys": with_keys,
            }

        @builtins.property
        def with_keys(self) -> typing.List[builtins.str]:
            '''The list of keys to delete.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-deletekeys.html#cfn-logs-transformer-deletekeys-withkeys
            '''
            result = self._values.get("with_keys")
            assert result is not None, "Required property 'with_keys' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeleteKeysProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.GrokProperty",
        jsii_struct_bases=[],
        name_mapping={"match": "match", "source": "source"},
    )
    class GrokProperty:
        def __init__(
            self,
            *,
            match: builtins.str,
            source: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This processor uses pattern matching to parse and structure unstructured data.

            This processor can also extract fields from log messages.

            For more information about this processor including examples, see `grok <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-Grok>`_ in the *CloudWatch Logs User Guide* .

            :param match: The grok pattern to match against the log event. For a list of supported grok patterns, see `Supported grok patterns <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#Grok-Patterns>`_ .
            :param source: The path to the field in the log event that you want to parse. If you omit this value, the whole log message is parsed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-grok.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                grok_property = logs.CfnTransformer.GrokProperty(
                    match="match",
                
                    # the properties below are optional
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__099136f924dd58199de2c070d0c9c967072f377ef3449d963d69903d6bfb2b15)
                check_type(argname="argument match", value=match, expected_type=type_hints["match"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "match": match,
            }
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def match(self) -> builtins.str:
            '''The grok pattern to match against the log event.

            For a list of supported grok patterns, see `Supported grok patterns <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#Grok-Patterns>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-grok.html#cfn-logs-transformer-grok-match
            '''
            result = self._values.get("match")
            assert result is not None, "Required property 'match' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''The path to the field in the log event that you want to parse.

            If you omit this value, the whole log message is parsed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-grok.html#cfn-logs-transformer-grok-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrokProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.ListToMapProperty",
        jsii_struct_bases=[],
        name_mapping={
            "key": "key",
            "source": "source",
            "flatten": "flatten",
            "flattened_element": "flattenedElement",
            "target": "target",
            "value_key": "valueKey",
        },
    )
    class ListToMapProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            source: builtins.str,
            flatten: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            flattened_element: typing.Optional[builtins.str] = None,
            target: typing.Optional[builtins.str] = None,
            value_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This processor takes a list of objects that contain key fields, and converts them into a map of target keys.

            For more information about this processor including examples, see `listToMap <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-listToMap>`_ in the *CloudWatch Logs User Guide* .

            :param key: The key of the field to be extracted as keys in the generated map.
            :param source: The key in the log event that has a list of objects that will be converted to a map.
            :param flatten: A Boolean value to indicate whether the list will be flattened into single items. Specify ``true`` to flatten the list. The default is ``false``
            :param flattened_element: If you set ``flatten`` to ``true`` , use ``flattenedElement`` to specify which element, ``first`` or ``last`` , to keep. You must specify this parameter if ``flatten`` is ``true``
            :param target: The key of the field that will hold the generated map.
            :param value_key: If this is specified, the values that you specify in this parameter will be extracted from the ``source`` objects and put into the values of the generated map. Otherwise, original objects in the source list will be put into the values of the generated map.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-listtomap.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                list_to_map_property = logs.CfnTransformer.ListToMapProperty(
                    key="key",
                    source="source",
                
                    # the properties below are optional
                    flatten=False,
                    flattened_element="flattenedElement",
                    target="target",
                    value_key="valueKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b34ca3744eb410b795c48cbf2325a84de8b8980ad35f615e5fcf729b3098d007)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
                check_type(argname="argument flatten", value=flatten, expected_type=type_hints["flatten"])
                check_type(argname="argument flattened_element", value=flattened_element, expected_type=type_hints["flattened_element"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
                check_type(argname="argument value_key", value=value_key, expected_type=type_hints["value_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "source": source,
            }
            if flatten is not None:
                self._values["flatten"] = flatten
            if flattened_element is not None:
                self._values["flattened_element"] = flattened_element
            if target is not None:
                self._values["target"] = target
            if value_key is not None:
                self._values["value_key"] = value_key

        @builtins.property
        def key(self) -> builtins.str:
            '''The key of the field to be extracted as keys in the generated map.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-listtomap.html#cfn-logs-transformer-listtomap-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source(self) -> builtins.str:
            '''The key in the log event that has a list of objects that will be converted to a map.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-listtomap.html#cfn-logs-transformer-listtomap-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def flatten(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean value to indicate whether the list will be flattened into single items.

            Specify ``true`` to flatten the list. The default is ``false``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-listtomap.html#cfn-logs-transformer-listtomap-flatten
            '''
            result = self._values.get("flatten")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def flattened_element(self) -> typing.Optional[builtins.str]:
            '''If you set ``flatten`` to ``true`` , use ``flattenedElement`` to specify which element, ``first`` or ``last`` , to keep.

            You must specify this parameter if ``flatten`` is ``true``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-listtomap.html#cfn-logs-transformer-listtomap-flattenedelement
            '''
            result = self._values.get("flattened_element")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target(self) -> typing.Optional[builtins.str]:
            '''The key of the field that will hold the generated map.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-listtomap.html#cfn-logs-transformer-listtomap-target
            '''
            result = self._values.get("target")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value_key(self) -> typing.Optional[builtins.str]:
            '''If this is specified, the values that you specify in this parameter will be extracted from the ``source`` objects and put into the values of the generated map.

            Otherwise, original objects in the source list will be put into the values of the generated map.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-listtomap.html#cfn-logs-transformer-listtomap-valuekey
            '''
            result = self._values.get("value_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ListToMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.LowerCaseStringProperty",
        jsii_struct_bases=[],
        name_mapping={"with_keys": "withKeys"},
    )
    class LowerCaseStringProperty:
        def __init__(self, *, with_keys: typing.Sequence[builtins.str]) -> None:
            '''This processor converts a string to lowercase.

            For more information about this processor including examples, see `lowerCaseString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-lowerCaseString>`_ in the *CloudWatch Logs User Guide* .

            :param with_keys: The array caontaining the keys of the fields to convert to lowercase.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-lowercasestring.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                lower_case_string_property = logs.CfnTransformer.LowerCaseStringProperty(
                    with_keys=["withKeys"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d32b67f5aac5c1b18f4a4d4a4bb442a6cf892d46e66945200fe60ccc5d71c2c7)
                check_type(argname="argument with_keys", value=with_keys, expected_type=type_hints["with_keys"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "with_keys": with_keys,
            }

        @builtins.property
        def with_keys(self) -> typing.List[builtins.str]:
            '''The array caontaining the keys of the fields to convert to lowercase.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-lowercasestring.html#cfn-logs-transformer-lowercasestring-withkeys
            '''
            result = self._values.get("with_keys")
            assert result is not None, "Required property 'with_keys' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LowerCaseStringProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.MoveKeyEntryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source": "source",
            "target": "target",
            "overwrite_if_exists": "overwriteIfExists",
        },
    )
    class MoveKeyEntryProperty:
        def __init__(
            self,
            *,
            source: builtins.str,
            target: builtins.str,
            overwrite_if_exists: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''This object defines one key that will be moved with the `moveKey <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-moveKey>`_ processor.

            :param source: The key to move.
            :param target: The key to move to.
            :param overwrite_if_exists: Specifies whether to overwrite the value if the destination key already exists. If you omit this, the default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-movekeyentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                move_key_entry_property = logs.CfnTransformer.MoveKeyEntryProperty(
                    source="source",
                    target="target",
                
                    # the properties below are optional
                    overwrite_if_exists=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0ff8ce5ccfdd76db0297923b7f4cc2aa11420c3e5ab87b3401e1e4be83c56f3a)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
                check_type(argname="argument overwrite_if_exists", value=overwrite_if_exists, expected_type=type_hints["overwrite_if_exists"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source": source,
                "target": target,
            }
            if overwrite_if_exists is not None:
                self._values["overwrite_if_exists"] = overwrite_if_exists

        @builtins.property
        def source(self) -> builtins.str:
            '''The key to move.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-movekeyentry.html#cfn-logs-transformer-movekeyentry-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target(self) -> builtins.str:
            '''The key to move to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-movekeyentry.html#cfn-logs-transformer-movekeyentry-target
            '''
            result = self._values.get("target")
            assert result is not None, "Required property 'target' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def overwrite_if_exists(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether to overwrite the value if the destination key already exists.

            If you omit this, the default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-movekeyentry.html#cfn-logs-transformer-movekeyentry-overwriteifexists
            '''
            result = self._values.get("overwrite_if_exists")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MoveKeyEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.MoveKeysProperty",
        jsii_struct_bases=[],
        name_mapping={"entries": "entries"},
    )
    class MoveKeysProperty:
        def __init__(
            self,
            *,
            entries: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.MoveKeyEntryProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''This processor moves a key from one field to another. The original key is deleted.

            For more information about this processor including examples, see `moveKeys <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-moveKeys>`_ in the *CloudWatch Logs User Guide* .

            :param entries: An array of objects, where each object contains the information about one key to move.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-movekeys.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                move_keys_property = logs.CfnTransformer.MoveKeysProperty(
                    entries=[logs.CfnTransformer.MoveKeyEntryProperty(
                        source="source",
                        target="target",
                
                        # the properties below are optional
                        overwrite_if_exists=False
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6916994ad9bc82ff8e94137ddfb22219a21c5349390075aac61c70d8daf6eeef)
                check_type(argname="argument entries", value=entries, expected_type=type_hints["entries"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entries": entries,
            }

        @builtins.property
        def entries(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.MoveKeyEntryProperty"]]]:
            '''An array of objects, where each object contains the information about one key to move.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-movekeys.html#cfn-logs-transformer-movekeys-entries
            '''
            result = self._values.get("entries")
            assert result is not None, "Required property 'entries' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.MoveKeyEntryProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MoveKeysProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.ParseCloudfrontProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source"},
    )
    class ParseCloudfrontProperty:
        def __init__(self, *, source: typing.Optional[builtins.str] = None) -> None:
            '''This processor parses CloudFront vended logs, extract fields, and convert them into JSON format.

            Encoded field values are decoded. Values that are integers and doubles are treated as such. For more information about this processor including examples, see `parseCloudfront <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseCloudfront>`_

            For more information about CloudFront log format, see `Configure and use standard logs (access logs) <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html>`_ .

            If you use this processor, it must be the first processor in your transformer.

            :param source: Omit this parameter and the whole log message will be processed by this processor. No other value than ``@message`` is allowed for ``source`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsecloudfront.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                parse_cloudfront_property = logs.CfnTransformer.ParseCloudfrontProperty(
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ea8f836c26b6d6931c5db3b778b2cad26fc04ee23f83ad14bafce0cb66a0c5ae)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''Omit this parameter and the whole log message will be processed by this processor.

            No other value than ``@message`` is allowed for ``source`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsecloudfront.html#cfn-logs-transformer-parsecloudfront-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParseCloudfrontProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.ParseJSONProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination", "source": "source"},
    )
    class ParseJSONProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[builtins.str] = None,
            source: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This processor parses log events that are in JSON format.

            It can extract JSON key-value pairs and place them under a destination that you specify.

            Additionally, because you must have at least one parse-type processor in a transformer, you can use ``ParseJSON`` as that processor for JSON-format logs, so that you can also apply other processors, such as mutate processors, to these logs.

            For more information about this processor including examples, see `parseJSON <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseJSON>`_ in the *CloudWatch Logs User Guide* .

            :param destination: The location to put the parsed key value pair into. If you omit this parameter, it is placed under the root node.
            :param source: Path to the field in the log event that will be parsed. Use dot notation to access child fields. For example, ``store.book``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsejson.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                parse_jSONProperty = logs.CfnTransformer.ParseJSONProperty(
                    destination="destination",
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__394c2c2eedd7ab4a72bfd587d0d7e1cc8fdb937698e47c61eb614a5cecb1ef74)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def destination(self) -> typing.Optional[builtins.str]:
            '''The location to put the parsed key value pair into.

            If you omit this parameter, it is placed under the root node.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsejson.html#cfn-logs-transformer-parsejson-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''Path to the field in the log event that will be parsed.

            Use dot notation to access child fields. For example, ``store.book``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsejson.html#cfn-logs-transformer-parsejson-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParseJSONProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.ParseKeyValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination": "destination",
            "field_delimiter": "fieldDelimiter",
            "key_prefix": "keyPrefix",
            "key_value_delimiter": "keyValueDelimiter",
            "non_match_value": "nonMatchValue",
            "overwrite_if_exists": "overwriteIfExists",
            "source": "source",
        },
    )
    class ParseKeyValueProperty:
        def __init__(
            self,
            *,
            destination: typing.Optional[builtins.str] = None,
            field_delimiter: typing.Optional[builtins.str] = None,
            key_prefix: typing.Optional[builtins.str] = None,
            key_value_delimiter: typing.Optional[builtins.str] = None,
            non_match_value: typing.Optional[builtins.str] = None,
            overwrite_if_exists: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            source: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This processor parses a specified field in the original log event into key-value pairs.

            For more information about this processor including examples, see `parseKeyValue <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseKeyValue>`_ in the *CloudWatch Logs User Guide* .

            :param destination: The destination field to put the extracted key-value pairs into.
            :param field_delimiter: The field delimiter string that is used between key-value pairs in the original log events. If you omit this, the ampersand ``&`` character is used.
            :param key_prefix: If you want to add a prefix to all transformed keys, specify it here.
            :param key_value_delimiter: The delimiter string to use between the key and value in each pair in the transformed log event. If you omit this, the equal ``=`` character is used.
            :param non_match_value: A value to insert into the value field in the result, when a key-value pair is not successfully split.
            :param overwrite_if_exists: Specifies whether to overwrite the value if the destination key already exists. If you omit this, the default is ``false`` .
            :param source: Path to the field in the log event that will be parsed. Use dot notation to access child fields. For example, ``store.book``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsekeyvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                parse_key_value_property = logs.CfnTransformer.ParseKeyValueProperty(
                    destination="destination",
                    field_delimiter="fieldDelimiter",
                    key_prefix="keyPrefix",
                    key_value_delimiter="keyValueDelimiter",
                    non_match_value="nonMatchValue",
                    overwrite_if_exists=False,
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ed79a8a8bfee98dc8705bad692617a694795f1862e628cdb6f4fbb9624efcd8c)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument field_delimiter", value=field_delimiter, expected_type=type_hints["field_delimiter"])
                check_type(argname="argument key_prefix", value=key_prefix, expected_type=type_hints["key_prefix"])
                check_type(argname="argument key_value_delimiter", value=key_value_delimiter, expected_type=type_hints["key_value_delimiter"])
                check_type(argname="argument non_match_value", value=non_match_value, expected_type=type_hints["non_match_value"])
                check_type(argname="argument overwrite_if_exists", value=overwrite_if_exists, expected_type=type_hints["overwrite_if_exists"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination is not None:
                self._values["destination"] = destination
            if field_delimiter is not None:
                self._values["field_delimiter"] = field_delimiter
            if key_prefix is not None:
                self._values["key_prefix"] = key_prefix
            if key_value_delimiter is not None:
                self._values["key_value_delimiter"] = key_value_delimiter
            if non_match_value is not None:
                self._values["non_match_value"] = non_match_value
            if overwrite_if_exists is not None:
                self._values["overwrite_if_exists"] = overwrite_if_exists
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def destination(self) -> typing.Optional[builtins.str]:
            '''The destination field to put the extracted key-value pairs into.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsekeyvalue.html#cfn-logs-transformer-parsekeyvalue-destination
            '''
            result = self._values.get("destination")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def field_delimiter(self) -> typing.Optional[builtins.str]:
            '''The field delimiter string that is used between key-value pairs in the original log events.

            If you omit this, the ampersand ``&`` character is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsekeyvalue.html#cfn-logs-transformer-parsekeyvalue-fielddelimiter
            '''
            result = self._values.get("field_delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_prefix(self) -> typing.Optional[builtins.str]:
            '''If you want to add a prefix to all transformed keys, specify it here.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsekeyvalue.html#cfn-logs-transformer-parsekeyvalue-keyprefix
            '''
            result = self._values.get("key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_value_delimiter(self) -> typing.Optional[builtins.str]:
            '''The delimiter string to use between the key and value in each pair in the transformed log event.

            If you omit this, the equal ``=`` character is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsekeyvalue.html#cfn-logs-transformer-parsekeyvalue-keyvaluedelimiter
            '''
            result = self._values.get("key_value_delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def non_match_value(self) -> typing.Optional[builtins.str]:
            '''A value to insert into the value field in the result, when a key-value pair is not successfully split.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsekeyvalue.html#cfn-logs-transformer-parsekeyvalue-nonmatchvalue
            '''
            result = self._values.get("non_match_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def overwrite_if_exists(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether to overwrite the value if the destination key already exists.

            If you omit this, the default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsekeyvalue.html#cfn-logs-transformer-parsekeyvalue-overwriteifexists
            '''
            result = self._values.get("overwrite_if_exists")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''Path to the field in the log event that will be parsed.

            Use dot notation to access child fields. For example, ``store.book``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsekeyvalue.html#cfn-logs-transformer-parsekeyvalue-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParseKeyValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.ParsePostgresProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source"},
    )
    class ParsePostgresProperty:
        def __init__(self, *, source: typing.Optional[builtins.str] = None) -> None:
            '''Use this processor to parse RDS for PostgreSQL vended logs, extract fields, and and convert them into a JSON format.

            This processor always processes the entire log event message. For more information about this processor including examples, see `parsePostGres <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parsePostGres>`_ .

            For more information about RDS for PostgreSQL log format, see `RDS for PostgreSQL database log filesTCP flag sequence <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.PostgreSQL.html#USER_LogAccess.Concepts.PostgreSQL.Log_Format.log-line-prefix>`_ .
            .. epigraph::

               If you use this processor, it must be the first processor in your transformer.

            :param source: Omit this parameter and the whole log message will be processed by this processor. No other value than ``@message`` is allowed for ``source`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsepostgres.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                parse_postgres_property = logs.CfnTransformer.ParsePostgresProperty(
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__952e8e660ca1672ad750873df677aa7489259b5396f80da6748f9d792d7e7bf0)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''Omit this parameter and the whole log message will be processed by this processor.

            No other value than ``@message`` is allowed for ``source`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsepostgres.html#cfn-logs-transformer-parsepostgres-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParsePostgresProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.ParseRoute53Property",
        jsii_struct_bases=[],
        name_mapping={"source": "source"},
    )
    class ParseRoute53Property:
        def __init__(self, *, source: typing.Optional[builtins.str] = None) -> None:
            '''Use this processor to parse Route 53 vended logs, extract fields, and and convert them into a JSON format.

            This processor always processes the entire log event message. For more information about this processor including examples, see `parseRoute53 <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseRoute53>`_ .
            .. epigraph::

               If you use this processor, it must be the first processor in your transformer.

            :param source: Omit this parameter and the whole log message will be processed by this processor. No other value than ``@message`` is allowed for ``source`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parseroute53.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                parse_route53_property = logs.CfnTransformer.ParseRoute53Property(
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__658801a998622d7af47eb8512eb68d2858ed8827da8b177c87996a73cda1431c)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''Omit this parameter and the whole log message will be processed by this processor.

            No other value than ``@message`` is allowed for ``source`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parseroute53.html#cfn-logs-transformer-parseroute53-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParseRoute53Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.ParseToOCSFProperty",
        jsii_struct_bases=[],
        name_mapping={
            "event_source": "eventSource",
            "ocsf_version": "ocsfVersion",
            "source": "source",
        },
    )
    class ParseToOCSFProperty:
        def __init__(
            self,
            *,
            event_source: builtins.str,
            ocsf_version: builtins.str,
            source: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This processor converts logs into `Open Cybersecurity Schema Framework (OCSF) <https://docs.aws.amazon.com/https://ocsf.io>`_ events.

            For more information about this processor including examples, see `parseToOSCF <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseToOCSF>`_ in the *CloudWatch Logs User Guide* .

            :param event_source: Specify the service or process that produces the log events that will be converted with this processor.
            :param ocsf_version: Specify which version of the OCSF schema to use for the transformed log events.
            :param source: The path to the field in the log event that you want to parse. If you omit this value, the whole log message is parsed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsetoocsf.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                parse_to_oCSFProperty = logs.CfnTransformer.ParseToOCSFProperty(
                    event_source="eventSource",
                    ocsf_version="ocsfVersion",
                
                    # the properties below are optional
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6febe08cc73af735295ba9258de19bd6c4f1b389f2b1e4fd5e0d66977951c589)
                check_type(argname="argument event_source", value=event_source, expected_type=type_hints["event_source"])
                check_type(argname="argument ocsf_version", value=ocsf_version, expected_type=type_hints["ocsf_version"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "event_source": event_source,
                "ocsf_version": ocsf_version,
            }
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def event_source(self) -> builtins.str:
            '''Specify the service or process that produces the log events that will be converted with this processor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsetoocsf.html#cfn-logs-transformer-parsetoocsf-eventsource
            '''
            result = self._values.get("event_source")
            assert result is not None, "Required property 'event_source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ocsf_version(self) -> builtins.str:
            '''Specify which version of the OCSF schema to use for the transformed log events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsetoocsf.html#cfn-logs-transformer-parsetoocsf-ocsfversion
            '''
            result = self._values.get("ocsf_version")
            assert result is not None, "Required property 'ocsf_version' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''The path to the field in the log event that you want to parse.

            If you omit this value, the whole log message is parsed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsetoocsf.html#cfn-logs-transformer-parsetoocsf-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParseToOCSFProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.ParseVPCProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source"},
    )
    class ParseVPCProperty:
        def __init__(self, *, source: typing.Optional[builtins.str] = None) -> None:
            '''Use this processor to parse Amazon VPC vended logs, extract fields, and and convert them into a JSON format.

            This processor always processes the entire log event message.

            This processor doesn't support custom log formats, such as NAT gateway logs. For more information about custom log formats in Amazon VPC, see `parseVPC <https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-records-examples.html#flow-log-example-tcp-flag>`_ For more information about this processor including examples, see `parseVPC <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseVPC>`_ .
            .. epigraph::

               If you use this processor, it must be the first processor in your transformer.

            :param source: Omit this parameter and the whole log message will be processed by this processor. No other value than ``@message`` is allowed for ``source`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsevpc.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                parse_vPCProperty = logs.CfnTransformer.ParseVPCProperty(
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__08e824a8839365028da24b6eaa3d4989ea1bda6be8234968a2991fd59b09e4d4)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''Omit this parameter and the whole log message will be processed by this processor.

            No other value than ``@message`` is allowed for ``source`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsevpc.html#cfn-logs-transformer-parsevpc-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParseVPCProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.ParseWAFProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source"},
    )
    class ParseWAFProperty:
        def __init__(self, *, source: typing.Optional[builtins.str] = None) -> None:
            '''Use this processor to parse AWS WAF vended logs, extract fields, and and convert them into a JSON format.

            This processor always processes the entire log event message. For more information about this processor including examples, see `parseWAF <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parsePostGres>`_ .

            For more information about AWS WAF log format, see `Log examples for web ACL traffic <https://docs.aws.amazon.com/waf/latest/developerguide/logging-examples.html>`_ .
            .. epigraph::

               If you use this processor, it must be the first processor in your transformer.

            :param source: Omit this parameter and the whole log message will be processed by this processor. No other value than ``@message`` is allowed for ``source`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsewaf.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                parse_wAFProperty = logs.CfnTransformer.ParseWAFProperty(
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1b26bfc2a0a2e670d7d7c901f15a99ddaa76f77d049946758f799b74137c6cfd)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''Omit this parameter and the whole log message will be processed by this processor.

            No other value than ``@message`` is allowed for ``source`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-parsewaf.html#cfn-logs-transformer-parsewaf-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParseWAFProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.ProcessorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_keys": "addKeys",
            "copy_value": "copyValue",
            "csv": "csv",
            "date_time_converter": "dateTimeConverter",
            "delete_keys": "deleteKeys",
            "grok": "grok",
            "list_to_map": "listToMap",
            "lower_case_string": "lowerCaseString",
            "move_keys": "moveKeys",
            "parse_cloudfront": "parseCloudfront",
            "parse_json": "parseJson",
            "parse_key_value": "parseKeyValue",
            "parse_postgres": "parsePostgres",
            "parse_route53": "parseRoute53",
            "parse_to_ocsf": "parseToOcsf",
            "parse_vpc": "parseVpc",
            "parse_waf": "parseWaf",
            "rename_keys": "renameKeys",
            "split_string": "splitString",
            "substitute_string": "substituteString",
            "trim_string": "trimString",
            "type_converter": "typeConverter",
            "upper_case_string": "upperCaseString",
        },
    )
    class ProcessorProperty:
        def __init__(
            self,
            *,
            add_keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.AddKeysProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            copy_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.CopyValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            csv: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.CsvProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            date_time_converter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.DateTimeConverterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            delete_keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.DeleteKeysProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            grok: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.GrokProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            list_to_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.ListToMapProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            lower_case_string: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.LowerCaseStringProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            move_keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.MoveKeysProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            parse_cloudfront: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.ParseCloudfrontProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            parse_json: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.ParseJSONProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            parse_key_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.ParseKeyValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            parse_postgres: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.ParsePostgresProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            parse_route53: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.ParseRoute53Property", typing.Dict[builtins.str, typing.Any]]]] = None,
            parse_to_ocsf: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.ParseToOCSFProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            parse_vpc: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.ParseVPCProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            parse_waf: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.ParseWAFProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            rename_keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.RenameKeysProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            split_string: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.SplitStringProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            substitute_string: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.SubstituteStringProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            trim_string: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.TrimStringProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            type_converter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.TypeConverterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            upper_case_string: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.UpperCaseStringProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''This structure contains the information about one processor in a log transformer.

            :param add_keys: Use this parameter to include the `addKeys <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-addKeys>`_ processor in your transformer.
            :param copy_value: Use this parameter to include the `copyValue <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-copyValue>`_ processor in your transformer.
            :param csv: Use this parameter to include the `CSV <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-CSV>`_ processor in your transformer.
            :param date_time_converter: Use this parameter to include the `datetimeConverter <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-datetimeConverter>`_ processor in your transformer.
            :param delete_keys: Use this parameter to include the `deleteKeys <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-deleteKeys>`_ processor in your transformer.
            :param grok: Use this parameter to include the `grok <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-grok>`_ processor in your transformer.
            :param list_to_map: Use this parameter to include the `listToMap <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-listToMap>`_ processor in your transformer.
            :param lower_case_string: Use this parameter to include the `lowerCaseString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-lowerCaseString>`_ processor in your transformer.
            :param move_keys: Use this parameter to include the `moveKeys <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-moveKeys>`_ processor in your transformer.
            :param parse_cloudfront: Use this parameter to include the `parseCloudfront <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseCloudfront>`_ processor in your transformer. If you use this processor, it must be the first processor in your transformer.
            :param parse_json: Use this parameter to include the `parseJSON <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseJSON>`_ processor in your transformer.
            :param parse_key_value: Use this parameter to include the `parseKeyValue <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseKeyValue>`_ processor in your transformer.
            :param parse_postgres: Use this parameter to include the `parsePostGres <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parsePostGres>`_ processor in your transformer. If you use this processor, it must be the first processor in your transformer.
            :param parse_route53: Use this parameter to include the `parseRoute53 <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseRoute53>`_ processor in your transformer. If you use this processor, it must be the first processor in your transformer.
            :param parse_to_ocsf: Use this parameter to convert logs into Open Cybersecurity Schema (OCSF) format.
            :param parse_vpc: Use this parameter to include the `parseVPC <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseVPC>`_ processor in your transformer. If you use this processor, it must be the first processor in your transformer.
            :param parse_waf: Use this parameter to include the `parseWAF <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseWAF>`_ processor in your transformer. If you use this processor, it must be the first processor in your transformer.
            :param rename_keys: Use this parameter to include the `renameKeys <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-renameKeys>`_ processor in your transformer.
            :param split_string: Use this parameter to include the `splitString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-splitString>`_ processor in your transformer.
            :param substitute_string: Use this parameter to include the `substituteString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-substituteString>`_ processor in your transformer.
            :param trim_string: Use this parameter to include the `trimString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-trimString>`_ processor in your transformer.
            :param type_converter: Use this parameter to include the `typeConverter <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-typeConverter>`_ processor in your transformer.
            :param upper_case_string: Use this parameter to include the `upperCaseString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-upperCaseString>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                processor_property = logs.CfnTransformer.ProcessorProperty(
                    add_keys=logs.CfnTransformer.AddKeysProperty(
                        entries=[logs.CfnTransformer.AddKeyEntryProperty(
                            key="key",
                            value="value",
                
                            # the properties below are optional
                            overwrite_if_exists=False
                        )]
                    ),
                    copy_value=logs.CfnTransformer.CopyValueProperty(
                        entries=[logs.CfnTransformer.CopyValueEntryProperty(
                            source="source",
                            target="target",
                
                            # the properties below are optional
                            overwrite_if_exists=False
                        )]
                    ),
                    csv=logs.CfnTransformer.CsvProperty(
                        columns=["columns"],
                        delimiter="delimiter",
                        quote_character="quoteCharacter",
                        source="source"
                    ),
                    date_time_converter=logs.CfnTransformer.DateTimeConverterProperty(
                        match_patterns=["matchPatterns"],
                        source="source",
                        target="target",
                
                        # the properties below are optional
                        locale="locale",
                        source_timezone="sourceTimezone",
                        target_format="targetFormat",
                        target_timezone="targetTimezone"
                    ),
                    delete_keys=logs.CfnTransformer.DeleteKeysProperty(
                        with_keys=["withKeys"]
                    ),
                    grok=logs.CfnTransformer.GrokProperty(
                        match="match",
                
                        # the properties below are optional
                        source="source"
                    ),
                    list_to_map=logs.CfnTransformer.ListToMapProperty(
                        key="key",
                        source="source",
                
                        # the properties below are optional
                        flatten=False,
                        flattened_element="flattenedElement",
                        target="target",
                        value_key="valueKey"
                    ),
                    lower_case_string=logs.CfnTransformer.LowerCaseStringProperty(
                        with_keys=["withKeys"]
                    ),
                    move_keys=logs.CfnTransformer.MoveKeysProperty(
                        entries=[logs.CfnTransformer.MoveKeyEntryProperty(
                            source="source",
                            target="target",
                
                            # the properties below are optional
                            overwrite_if_exists=False
                        )]
                    ),
                    parse_cloudfront=logs.CfnTransformer.ParseCloudfrontProperty(
                        source="source"
                    ),
                    parse_json=logs.CfnTransformer.ParseJSONProperty(
                        destination="destination",
                        source="source"
                    ),
                    parse_key_value=logs.CfnTransformer.ParseKeyValueProperty(
                        destination="destination",
                        field_delimiter="fieldDelimiter",
                        key_prefix="keyPrefix",
                        key_value_delimiter="keyValueDelimiter",
                        non_match_value="nonMatchValue",
                        overwrite_if_exists=False,
                        source="source"
                    ),
                    parse_postgres=logs.CfnTransformer.ParsePostgresProperty(
                        source="source"
                    ),
                    parse_route53=logs.CfnTransformer.ParseRoute53Property(
                        source="source"
                    ),
                    parse_to_ocsf=logs.CfnTransformer.ParseToOCSFProperty(
                        event_source="eventSource",
                        ocsf_version="ocsfVersion",
                
                        # the properties below are optional
                        source="source"
                    ),
                    parse_vpc=logs.CfnTransformer.ParseVPCProperty(
                        source="source"
                    ),
                    parse_waf=logs.CfnTransformer.ParseWAFProperty(
                        source="source"
                    ),
                    rename_keys=logs.CfnTransformer.RenameKeysProperty(
                        entries=[logs.CfnTransformer.RenameKeyEntryProperty(
                            key="key",
                            rename_to="renameTo",
                
                            # the properties below are optional
                            overwrite_if_exists=False
                        )]
                    ),
                    split_string=logs.CfnTransformer.SplitStringProperty(
                        entries=[logs.CfnTransformer.SplitStringEntryProperty(
                            delimiter="delimiter",
                            source="source"
                        )]
                    ),
                    substitute_string=logs.CfnTransformer.SubstituteStringProperty(
                        entries=[logs.CfnTransformer.SubstituteStringEntryProperty(
                            from="from",
                            source="source",
                            to="to"
                        )]
                    ),
                    trim_string=logs.CfnTransformer.TrimStringProperty(
                        with_keys=["withKeys"]
                    ),
                    type_converter=logs.CfnTransformer.TypeConverterProperty(
                        entries=[logs.CfnTransformer.TypeConverterEntryProperty(
                            key="key",
                            type="type"
                        )]
                    ),
                    upper_case_string=logs.CfnTransformer.UpperCaseStringProperty(
                        with_keys=["withKeys"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e487fac0bac06039bca1700fdccd6ce85e8e1fbb80d54937d3dbfdb8f5267202)
                check_type(argname="argument add_keys", value=add_keys, expected_type=type_hints["add_keys"])
                check_type(argname="argument copy_value", value=copy_value, expected_type=type_hints["copy_value"])
                check_type(argname="argument csv", value=csv, expected_type=type_hints["csv"])
                check_type(argname="argument date_time_converter", value=date_time_converter, expected_type=type_hints["date_time_converter"])
                check_type(argname="argument delete_keys", value=delete_keys, expected_type=type_hints["delete_keys"])
                check_type(argname="argument grok", value=grok, expected_type=type_hints["grok"])
                check_type(argname="argument list_to_map", value=list_to_map, expected_type=type_hints["list_to_map"])
                check_type(argname="argument lower_case_string", value=lower_case_string, expected_type=type_hints["lower_case_string"])
                check_type(argname="argument move_keys", value=move_keys, expected_type=type_hints["move_keys"])
                check_type(argname="argument parse_cloudfront", value=parse_cloudfront, expected_type=type_hints["parse_cloudfront"])
                check_type(argname="argument parse_json", value=parse_json, expected_type=type_hints["parse_json"])
                check_type(argname="argument parse_key_value", value=parse_key_value, expected_type=type_hints["parse_key_value"])
                check_type(argname="argument parse_postgres", value=parse_postgres, expected_type=type_hints["parse_postgres"])
                check_type(argname="argument parse_route53", value=parse_route53, expected_type=type_hints["parse_route53"])
                check_type(argname="argument parse_to_ocsf", value=parse_to_ocsf, expected_type=type_hints["parse_to_ocsf"])
                check_type(argname="argument parse_vpc", value=parse_vpc, expected_type=type_hints["parse_vpc"])
                check_type(argname="argument parse_waf", value=parse_waf, expected_type=type_hints["parse_waf"])
                check_type(argname="argument rename_keys", value=rename_keys, expected_type=type_hints["rename_keys"])
                check_type(argname="argument split_string", value=split_string, expected_type=type_hints["split_string"])
                check_type(argname="argument substitute_string", value=substitute_string, expected_type=type_hints["substitute_string"])
                check_type(argname="argument trim_string", value=trim_string, expected_type=type_hints["trim_string"])
                check_type(argname="argument type_converter", value=type_converter, expected_type=type_hints["type_converter"])
                check_type(argname="argument upper_case_string", value=upper_case_string, expected_type=type_hints["upper_case_string"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if add_keys is not None:
                self._values["add_keys"] = add_keys
            if copy_value is not None:
                self._values["copy_value"] = copy_value
            if csv is not None:
                self._values["csv"] = csv
            if date_time_converter is not None:
                self._values["date_time_converter"] = date_time_converter
            if delete_keys is not None:
                self._values["delete_keys"] = delete_keys
            if grok is not None:
                self._values["grok"] = grok
            if list_to_map is not None:
                self._values["list_to_map"] = list_to_map
            if lower_case_string is not None:
                self._values["lower_case_string"] = lower_case_string
            if move_keys is not None:
                self._values["move_keys"] = move_keys
            if parse_cloudfront is not None:
                self._values["parse_cloudfront"] = parse_cloudfront
            if parse_json is not None:
                self._values["parse_json"] = parse_json
            if parse_key_value is not None:
                self._values["parse_key_value"] = parse_key_value
            if parse_postgres is not None:
                self._values["parse_postgres"] = parse_postgres
            if parse_route53 is not None:
                self._values["parse_route53"] = parse_route53
            if parse_to_ocsf is not None:
                self._values["parse_to_ocsf"] = parse_to_ocsf
            if parse_vpc is not None:
                self._values["parse_vpc"] = parse_vpc
            if parse_waf is not None:
                self._values["parse_waf"] = parse_waf
            if rename_keys is not None:
                self._values["rename_keys"] = rename_keys
            if split_string is not None:
                self._values["split_string"] = split_string
            if substitute_string is not None:
                self._values["substitute_string"] = substitute_string
            if trim_string is not None:
                self._values["trim_string"] = trim_string
            if type_converter is not None:
                self._values["type_converter"] = type_converter
            if upper_case_string is not None:
                self._values["upper_case_string"] = upper_case_string

        @builtins.property
        def add_keys(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.AddKeysProperty"]]:
            '''Use this parameter to include the `addKeys <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-addKeys>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-addkeys
            '''
            result = self._values.get("add_keys")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.AddKeysProperty"]], result)

        @builtins.property
        def copy_value(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.CopyValueProperty"]]:
            '''Use this parameter to include the `copyValue <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-copyValue>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-copyvalue
            '''
            result = self._values.get("copy_value")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.CopyValueProperty"]], result)

        @builtins.property
        def csv(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.CsvProperty"]]:
            '''Use this parameter to include the `CSV <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-CSV>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-csv
            '''
            result = self._values.get("csv")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.CsvProperty"]], result)

        @builtins.property
        def date_time_converter(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.DateTimeConverterProperty"]]:
            '''Use this parameter to include the `datetimeConverter <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-datetimeConverter>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-datetimeconverter
            '''
            result = self._values.get("date_time_converter")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.DateTimeConverterProperty"]], result)

        @builtins.property
        def delete_keys(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.DeleteKeysProperty"]]:
            '''Use this parameter to include the `deleteKeys <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-deleteKeys>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-deletekeys
            '''
            result = self._values.get("delete_keys")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.DeleteKeysProperty"]], result)

        @builtins.property
        def grok(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.GrokProperty"]]:
            '''Use this parameter to include the `grok <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-grok>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-grok
            '''
            result = self._values.get("grok")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.GrokProperty"]], result)

        @builtins.property
        def list_to_map(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ListToMapProperty"]]:
            '''Use this parameter to include the `listToMap <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-listToMap>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-listtomap
            '''
            result = self._values.get("list_to_map")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ListToMapProperty"]], result)

        @builtins.property
        def lower_case_string(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.LowerCaseStringProperty"]]:
            '''Use this parameter to include the `lowerCaseString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-lowerCaseString>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-lowercasestring
            '''
            result = self._values.get("lower_case_string")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.LowerCaseStringProperty"]], result)

        @builtins.property
        def move_keys(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.MoveKeysProperty"]]:
            '''Use this parameter to include the `moveKeys <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-moveKeys>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-movekeys
            '''
            result = self._values.get("move_keys")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.MoveKeysProperty"]], result)

        @builtins.property
        def parse_cloudfront(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParseCloudfrontProperty"]]:
            '''Use this parameter to include the `parseCloudfront <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseCloudfront>`_ processor in your transformer.

            If you use this processor, it must be the first processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-parsecloudfront
            '''
            result = self._values.get("parse_cloudfront")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParseCloudfrontProperty"]], result)

        @builtins.property
        def parse_json(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParseJSONProperty"]]:
            '''Use this parameter to include the `parseJSON <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseJSON>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-parsejson
            '''
            result = self._values.get("parse_json")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParseJSONProperty"]], result)

        @builtins.property
        def parse_key_value(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParseKeyValueProperty"]]:
            '''Use this parameter to include the `parseKeyValue <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseKeyValue>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-parsekeyvalue
            '''
            result = self._values.get("parse_key_value")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParseKeyValueProperty"]], result)

        @builtins.property
        def parse_postgres(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParsePostgresProperty"]]:
            '''Use this parameter to include the `parsePostGres <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parsePostGres>`_ processor in your transformer.

            If you use this processor, it must be the first processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-parsepostgres
            '''
            result = self._values.get("parse_postgres")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParsePostgresProperty"]], result)

        @builtins.property
        def parse_route53(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParseRoute53Property"]]:
            '''Use this parameter to include the `parseRoute53 <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseRoute53>`_ processor in your transformer.

            If you use this processor, it must be the first processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-parseroute53
            '''
            result = self._values.get("parse_route53")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParseRoute53Property"]], result)

        @builtins.property
        def parse_to_ocsf(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParseToOCSFProperty"]]:
            '''Use this parameter to convert logs into Open Cybersecurity Schema (OCSF) format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-parsetoocsf
            '''
            result = self._values.get("parse_to_ocsf")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParseToOCSFProperty"]], result)

        @builtins.property
        def parse_vpc(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParseVPCProperty"]]:
            '''Use this parameter to include the `parseVPC <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-parseVPC>`_ processor in your transformer.

            If you use this processor, it must be the first processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-parsevpc
            '''
            result = self._values.get("parse_vpc")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParseVPCProperty"]], result)

        @builtins.property
        def parse_waf(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParseWAFProperty"]]:
            '''Use this parameter to include the `parseWAF <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseWAF>`_ processor in your transformer.

            If you use this processor, it must be the first processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-parsewaf
            '''
            result = self._values.get("parse_waf")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.ParseWAFProperty"]], result)

        @builtins.property
        def rename_keys(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.RenameKeysProperty"]]:
            '''Use this parameter to include the `renameKeys <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-renameKeys>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-renamekeys
            '''
            result = self._values.get("rename_keys")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.RenameKeysProperty"]], result)

        @builtins.property
        def split_string(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.SplitStringProperty"]]:
            '''Use this parameter to include the `splitString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-splitString>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-splitstring
            '''
            result = self._values.get("split_string")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.SplitStringProperty"]], result)

        @builtins.property
        def substitute_string(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.SubstituteStringProperty"]]:
            '''Use this parameter to include the `substituteString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-substituteString>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-substitutestring
            '''
            result = self._values.get("substitute_string")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.SubstituteStringProperty"]], result)

        @builtins.property
        def trim_string(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.TrimStringProperty"]]:
            '''Use this parameter to include the `trimString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-trimString>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-trimstring
            '''
            result = self._values.get("trim_string")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.TrimStringProperty"]], result)

        @builtins.property
        def type_converter(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.TypeConverterProperty"]]:
            '''Use this parameter to include the `typeConverter <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-typeConverter>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-typeconverter
            '''
            result = self._values.get("type_converter")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.TypeConverterProperty"]], result)

        @builtins.property
        def upper_case_string(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.UpperCaseStringProperty"]]:
            '''Use this parameter to include the `upperCaseString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-upperCaseString>`_ processor in your transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-processor.html#cfn-logs-transformer-processor-uppercasestring
            '''
            result = self._values.get("upper_case_string")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.UpperCaseStringProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProcessorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.RenameKeyEntryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "key": "key",
            "rename_to": "renameTo",
            "overwrite_if_exists": "overwriteIfExists",
        },
    )
    class RenameKeyEntryProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            rename_to: builtins.str,
            overwrite_if_exists: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''This object defines one key that will be renamed with the `renameKey <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-renameKey>`_ processor.

            :param key: The key to rename.
            :param rename_to: The string to use for the new key name.
            :param overwrite_if_exists: Specifies whether to overwrite the existing value if the destination key already exists. The default is ``false``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-renamekeyentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                rename_key_entry_property = logs.CfnTransformer.RenameKeyEntryProperty(
                    key="key",
                    rename_to="renameTo",
                
                    # the properties below are optional
                    overwrite_if_exists=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7a85b1ee0f4dc04b37555c8dcf6594a9f1494dd85258af0ff01d94ea67e474eb)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument rename_to", value=rename_to, expected_type=type_hints["rename_to"])
                check_type(argname="argument overwrite_if_exists", value=overwrite_if_exists, expected_type=type_hints["overwrite_if_exists"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "rename_to": rename_to,
            }
            if overwrite_if_exists is not None:
                self._values["overwrite_if_exists"] = overwrite_if_exists

        @builtins.property
        def key(self) -> builtins.str:
            '''The key to rename.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-renamekeyentry.html#cfn-logs-transformer-renamekeyentry-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def rename_to(self) -> builtins.str:
            '''The string to use for the new key name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-renamekeyentry.html#cfn-logs-transformer-renamekeyentry-renameto
            '''
            result = self._values.get("rename_to")
            assert result is not None, "Required property 'rename_to' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def overwrite_if_exists(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether to overwrite the existing value if the destination key already exists.

            The default is ``false``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-renamekeyentry.html#cfn-logs-transformer-renamekeyentry-overwriteifexists
            '''
            result = self._values.get("overwrite_if_exists")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RenameKeyEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.RenameKeysProperty",
        jsii_struct_bases=[],
        name_mapping={"entries": "entries"},
    )
    class RenameKeysProperty:
        def __init__(
            self,
            *,
            entries: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.RenameKeyEntryProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Use this processor to rename keys in a log event.

            For more information about this processor including examples, see `renameKeys <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-renameKeys>`_ in the *CloudWatch Logs User Guide* .

            :param entries: An array of ``RenameKeyEntry`` objects, where each object contains the information about a single key to rename.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-renamekeys.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                rename_keys_property = logs.CfnTransformer.RenameKeysProperty(
                    entries=[logs.CfnTransformer.RenameKeyEntryProperty(
                        key="key",
                        rename_to="renameTo",
                
                        # the properties below are optional
                        overwrite_if_exists=False
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__90cce6196aaf5dd8168c63be372944c4df28a731ebef948494876ab7bcfe3456)
                check_type(argname="argument entries", value=entries, expected_type=type_hints["entries"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entries": entries,
            }

        @builtins.property
        def entries(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.RenameKeyEntryProperty"]]]:
            '''An array of ``RenameKeyEntry`` objects, where each object contains the information about a single key to rename.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-renamekeys.html#cfn-logs-transformer-renamekeys-entries
            '''
            result = self._values.get("entries")
            assert result is not None, "Required property 'entries' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.RenameKeyEntryProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RenameKeysProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.SplitStringEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"delimiter": "delimiter", "source": "source"},
    )
    class SplitStringEntryProperty:
        def __init__(self, *, delimiter: builtins.str, source: builtins.str) -> None:
            '''This object defines one log field that will be split with the `splitString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-splitString>`_ processor.

            :param delimiter: The separator characters to split the string entry on.
            :param source: The key of the field to split.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-splitstringentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                split_string_entry_property = logs.CfnTransformer.SplitStringEntryProperty(
                    delimiter="delimiter",
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__263b02ba09218a6ff88ba5eed377f56a72b8e09134a489ef9267e6e6a5faf67d)
                check_type(argname="argument delimiter", value=delimiter, expected_type=type_hints["delimiter"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "delimiter": delimiter,
                "source": source,
            }

        @builtins.property
        def delimiter(self) -> builtins.str:
            '''The separator characters to split the string entry on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-splitstringentry.html#cfn-logs-transformer-splitstringentry-delimiter
            '''
            result = self._values.get("delimiter")
            assert result is not None, "Required property 'delimiter' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source(self) -> builtins.str:
            '''The key of the field to split.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-splitstringentry.html#cfn-logs-transformer-splitstringentry-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SplitStringEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.SplitStringProperty",
        jsii_struct_bases=[],
        name_mapping={"entries": "entries"},
    )
    class SplitStringProperty:
        def __init__(
            self,
            *,
            entries: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.SplitStringEntryProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Use this processor to split a field into an array of strings using a delimiting character.

            For more information about this processor including examples, see `splitString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-splitString>`_ in the *CloudWatch Logs User Guide* .

            :param entries: An array of ``SplitStringEntry`` objects, where each object contains the information about one field to split.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-splitstring.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                split_string_property = logs.CfnTransformer.SplitStringProperty(
                    entries=[logs.CfnTransformer.SplitStringEntryProperty(
                        delimiter="delimiter",
                        source="source"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__552fccafc9e15edea19c4f34ad5e5bf5f20ad80ad4a2596cc08fa01251ecb3fb)
                check_type(argname="argument entries", value=entries, expected_type=type_hints["entries"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entries": entries,
            }

        @builtins.property
        def entries(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.SplitStringEntryProperty"]]]:
            '''An array of ``SplitStringEntry`` objects, where each object contains the information about one field to split.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-splitstring.html#cfn-logs-transformer-splitstring-entries
            '''
            result = self._values.get("entries")
            assert result is not None, "Required property 'entries' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.SplitStringEntryProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SplitStringProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.SubstituteStringEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"from_": "from", "source": "source", "to": "to"},
    )
    class SubstituteStringEntryProperty:
        def __init__(
            self,
            *,
            from_: builtins.str,
            source: builtins.str,
            to: builtins.str,
        ) -> None:
            '''This object defines one log field key that will be replaced using the `substituteString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-substituteString>`_ processor.

            :param from_: The regular expression string to be replaced. Special regex characters such as [ and ] must be escaped using \\ when using double quotes and with \\ when using single quotes. For more information, see `Class Pattern <https://docs.aws.amazon.com/https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html>`_ on the Oracle web site.
            :param source: The key to modify.
            :param to: The string to be substituted for each match of ``from``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-substitutestringentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                substitute_string_entry_property = logs.CfnTransformer.SubstituteStringEntryProperty(
                    from="from",
                    source="source",
                    to="to"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f98269160c0c5038977ab2dc5c8938f02bf529b4d2cf342b072783c01286953d)
                check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
                check_type(argname="argument to", value=to, expected_type=type_hints["to"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "from_": from_,
                "source": source,
                "to": to,
            }

        @builtins.property
        def from_(self) -> builtins.str:
            '''The regular expression string to be replaced.

            Special regex characters such as [ and ] must be escaped using \\ when using double quotes and with \\ when using single quotes. For more information, see `Class Pattern <https://docs.aws.amazon.com/https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html>`_ on the Oracle web site.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-substitutestringentry.html#cfn-logs-transformer-substitutestringentry-from
            '''
            result = self._values.get("from_")
            assert result is not None, "Required property 'from_' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source(self) -> builtins.str:
            '''The key to modify.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-substitutestringentry.html#cfn-logs-transformer-substitutestringentry-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def to(self) -> builtins.str:
            '''The string to be substituted for each match of ``from``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-substitutestringentry.html#cfn-logs-transformer-substitutestringentry-to
            '''
            result = self._values.get("to")
            assert result is not None, "Required property 'to' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubstituteStringEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.SubstituteStringProperty",
        jsii_struct_bases=[],
        name_mapping={"entries": "entries"},
    )
    class SubstituteStringProperty:
        def __init__(
            self,
            *,
            entries: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.SubstituteStringEntryProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''This processor matches a key’s value against a regular expression and replaces all matches with a replacement string.

            For more information about this processor including examples, see `substituteString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-substituteString>`_ in the *CloudWatch Logs User Guide* .

            :param entries: An array of objects, where each object contains the information about one key to match and replace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-substitutestring.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                substitute_string_property = logs.CfnTransformer.SubstituteStringProperty(
                    entries=[logs.CfnTransformer.SubstituteStringEntryProperty(
                        from="from",
                        source="source",
                        to="to"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__81f76cf00b73242928401fed6e15762b2a6c06efee29159b7934e0f71a3c624f)
                check_type(argname="argument entries", value=entries, expected_type=type_hints["entries"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entries": entries,
            }

        @builtins.property
        def entries(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.SubstituteStringEntryProperty"]]]:
            '''An array of objects, where each object contains the information about one key to match and replace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-substitutestring.html#cfn-logs-transformer-substitutestring-entries
            '''
            result = self._values.get("entries")
            assert result is not None, "Required property 'entries' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.SubstituteStringEntryProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubstituteStringProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.TrimStringProperty",
        jsii_struct_bases=[],
        name_mapping={"with_keys": "withKeys"},
    )
    class TrimStringProperty:
        def __init__(self, *, with_keys: typing.Sequence[builtins.str]) -> None:
            '''Use this processor to remove leading and trailing whitespace.

            For more information about this processor including examples, see `trimString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-trimString>`_ in the *CloudWatch Logs User Guide* .

            :param with_keys: The array containing the keys of the fields to trim.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-trimstring.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                trim_string_property = logs.CfnTransformer.TrimStringProperty(
                    with_keys=["withKeys"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1d17872b8cad5d87a29ef7e4340a3141858904086ebef37ac6ec56490ff5b63b)
                check_type(argname="argument with_keys", value=with_keys, expected_type=type_hints["with_keys"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "with_keys": with_keys,
            }

        @builtins.property
        def with_keys(self) -> typing.List[builtins.str]:
            '''The array containing the keys of the fields to trim.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-trimstring.html#cfn-logs-transformer-trimstring-withkeys
            '''
            result = self._values.get("with_keys")
            assert result is not None, "Required property 'with_keys' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrimStringProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.TypeConverterEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "type": "type"},
    )
    class TypeConverterEntryProperty:
        def __init__(self, *, key: builtins.str, type: builtins.str) -> None:
            '''This object defines one value type that will be converted using the `typeConverter <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-typeConverter>`_ processor.

            :param key: The key with the value that is to be converted to a different type.
            :param type: The type to convert the field value to. Valid values are ``integer`` , ``double`` , ``string`` and ``boolean`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-typeconverterentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                type_converter_entry_property = logs.CfnTransformer.TypeConverterEntryProperty(
                    key="key",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c9ac92cdcbb756bea8e1541d9c9004ad6fa1ed1f73a1b4e7b62f9742f67146dd)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "type": type,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The key with the value that is to be converted to a different type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-typeconverterentry.html#cfn-logs-transformer-typeconverterentry-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type to convert the field value to.

            Valid values are ``integer`` , ``double`` , ``string`` and ``boolean`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-typeconverterentry.html#cfn-logs-transformer-typeconverterentry-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TypeConverterEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.TypeConverterProperty",
        jsii_struct_bases=[],
        name_mapping={"entries": "entries"},
    )
    class TypeConverterProperty:
        def __init__(
            self,
            *,
            entries: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.TypeConverterEntryProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Use this processor to convert a value type associated with the specified key to the specified type.

            It's a casting processor that changes the types of the specified fields. Values can be converted into one of the following datatypes: ``integer`` , ``double`` , ``string`` and ``boolean`` .

            For more information about this processor including examples, see `trimString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-trimString>`_ in the *CloudWatch Logs User Guide* .

            :param entries: An array of ``TypeConverterEntry`` objects, where each object contains the information about one field to change the type of.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-typeconverter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                type_converter_property = logs.CfnTransformer.TypeConverterProperty(
                    entries=[logs.CfnTransformer.TypeConverterEntryProperty(
                        key="key",
                        type="type"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3816b1190f1a44d3474db3d4b860789dcf8860b70a135dc25eabc95a3a9224dc)
                check_type(argname="argument entries", value=entries, expected_type=type_hints["entries"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entries": entries,
            }

        @builtins.property
        def entries(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.TypeConverterEntryProperty"]]]:
            '''An array of ``TypeConverterEntry`` objects, where each object contains the information about one field to change the type of.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-typeconverter.html#cfn-logs-transformer-typeconverter-entries
            '''
            result = self._values.get("entries")
            assert result is not None, "Required property 'entries' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.TypeConverterEntryProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TypeConverterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_logs.CfnTransformer.UpperCaseStringProperty",
        jsii_struct_bases=[],
        name_mapping={"with_keys": "withKeys"},
    )
    class UpperCaseStringProperty:
        def __init__(self, *, with_keys: typing.Sequence[builtins.str]) -> None:
            '''This processor converts a string field to uppercase.

            For more information about this processor including examples, see `upperCaseString <https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-upperCaseString>`_ in the *CloudWatch Logs User Guide* .

            :param with_keys: The array of containing the keys of the field to convert to uppercase.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-uppercasestring.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_logs as logs
                
                upper_case_string_property = logs.CfnTransformer.UpperCaseStringProperty(
                    with_keys=["withKeys"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__79e92ae9fa026aa82c90fea81fa17a5b6bb260575c11df9b13ca682a992251e2)
                check_type(argname="argument with_keys", value=with_keys, expected_type=type_hints["with_keys"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "with_keys": with_keys,
            }

        @builtins.property
        def with_keys(self) -> typing.List[builtins.str]:
            '''The array of containing the keys of the field to convert to uppercase.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-transformer-uppercasestring.html#cfn-logs-transformer-uppercasestring-withkeys
            '''
            result = self._values.get("with_keys")
            assert result is not None, "Required property 'with_keys' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpperCaseStringProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CfnTransformerProps",
    jsii_struct_bases=[],
    name_mapping={
        "log_group_identifier": "logGroupIdentifier",
        "transformer_config": "transformerConfig",
    },
)
class CfnTransformerProps:
    def __init__(
        self,
        *,
        log_group_identifier: builtins.str,
        transformer_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.ProcessorProperty, typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''Properties for defining a ``CfnTransformer``.

        :param log_group_identifier: Specify either the name or ARN of the log group to create the transformer for.
        :param transformer_config: This structure is an array that contains the configuration of this log transformer. A log transformer is an array of processors, where each processor applies one type of transformation to the log events that are ingested.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-transformer.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            cfn_transformer_props = logs.CfnTransformerProps(
                log_group_identifier="logGroupIdentifier",
                transformer_config=[logs.CfnTransformer.ProcessorProperty(
                    add_keys=logs.CfnTransformer.AddKeysProperty(
                        entries=[logs.CfnTransformer.AddKeyEntryProperty(
                            key="key",
                            value="value",
            
                            # the properties below are optional
                            overwrite_if_exists=False
                        )]
                    ),
                    copy_value=logs.CfnTransformer.CopyValueProperty(
                        entries=[logs.CfnTransformer.CopyValueEntryProperty(
                            source="source",
                            target="target",
            
                            # the properties below are optional
                            overwrite_if_exists=False
                        )]
                    ),
                    csv=logs.CfnTransformer.CsvProperty(
                        columns=["columns"],
                        delimiter="delimiter",
                        quote_character="quoteCharacter",
                        source="source"
                    ),
                    date_time_converter=logs.CfnTransformer.DateTimeConverterProperty(
                        match_patterns=["matchPatterns"],
                        source="source",
                        target="target",
            
                        # the properties below are optional
                        locale="locale",
                        source_timezone="sourceTimezone",
                        target_format="targetFormat",
                        target_timezone="targetTimezone"
                    ),
                    delete_keys=logs.CfnTransformer.DeleteKeysProperty(
                        with_keys=["withKeys"]
                    ),
                    grok=logs.CfnTransformer.GrokProperty(
                        match="match",
            
                        # the properties below are optional
                        source="source"
                    ),
                    list_to_map=logs.CfnTransformer.ListToMapProperty(
                        key="key",
                        source="source",
            
                        # the properties below are optional
                        flatten=False,
                        flattened_element="flattenedElement",
                        target="target",
                        value_key="valueKey"
                    ),
                    lower_case_string=logs.CfnTransformer.LowerCaseStringProperty(
                        with_keys=["withKeys"]
                    ),
                    move_keys=logs.CfnTransformer.MoveKeysProperty(
                        entries=[logs.CfnTransformer.MoveKeyEntryProperty(
                            source="source",
                            target="target",
            
                            # the properties below are optional
                            overwrite_if_exists=False
                        )]
                    ),
                    parse_cloudfront=logs.CfnTransformer.ParseCloudfrontProperty(
                        source="source"
                    ),
                    parse_json=logs.CfnTransformer.ParseJSONProperty(
                        destination="destination",
                        source="source"
                    ),
                    parse_key_value=logs.CfnTransformer.ParseKeyValueProperty(
                        destination="destination",
                        field_delimiter="fieldDelimiter",
                        key_prefix="keyPrefix",
                        key_value_delimiter="keyValueDelimiter",
                        non_match_value="nonMatchValue",
                        overwrite_if_exists=False,
                        source="source"
                    ),
                    parse_postgres=logs.CfnTransformer.ParsePostgresProperty(
                        source="source"
                    ),
                    parse_route53=logs.CfnTransformer.ParseRoute53Property(
                        source="source"
                    ),
                    parse_to_ocsf=logs.CfnTransformer.ParseToOCSFProperty(
                        event_source="eventSource",
                        ocsf_version="ocsfVersion",
            
                        # the properties below are optional
                        source="source"
                    ),
                    parse_vpc=logs.CfnTransformer.ParseVPCProperty(
                        source="source"
                    ),
                    parse_waf=logs.CfnTransformer.ParseWAFProperty(
                        source="source"
                    ),
                    rename_keys=logs.CfnTransformer.RenameKeysProperty(
                        entries=[logs.CfnTransformer.RenameKeyEntryProperty(
                            key="key",
                            rename_to="renameTo",
            
                            # the properties below are optional
                            overwrite_if_exists=False
                        )]
                    ),
                    split_string=logs.CfnTransformer.SplitStringProperty(
                        entries=[logs.CfnTransformer.SplitStringEntryProperty(
                            delimiter="delimiter",
                            source="source"
                        )]
                    ),
                    substitute_string=logs.CfnTransformer.SubstituteStringProperty(
                        entries=[logs.CfnTransformer.SubstituteStringEntryProperty(
                            from="from",
                            source="source",
                            to="to"
                        )]
                    ),
                    trim_string=logs.CfnTransformer.TrimStringProperty(
                        with_keys=["withKeys"]
                    ),
                    type_converter=logs.CfnTransformer.TypeConverterProperty(
                        entries=[logs.CfnTransformer.TypeConverterEntryProperty(
                            key="key",
                            type="type"
                        )]
                    ),
                    upper_case_string=logs.CfnTransformer.UpperCaseStringProperty(
                        with_keys=["withKeys"]
                    )
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a546e5df5e922961501b15adaa49ec492ffe516851869f75aacd2acfe0283eee)
            check_type(argname="argument log_group_identifier", value=log_group_identifier, expected_type=type_hints["log_group_identifier"])
            check_type(argname="argument transformer_config", value=transformer_config, expected_type=type_hints["transformer_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_group_identifier": log_group_identifier,
            "transformer_config": transformer_config,
        }

    @builtins.property
    def log_group_identifier(self) -> builtins.str:
        '''Specify either the name or ARN of the log group to create the transformer for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-transformer.html#cfn-logs-transformer-loggroupidentifier
        '''
        result = self._values.get("log_group_identifier")
        assert result is not None, "Required property 'log_group_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transformer_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTransformer.ProcessorProperty]]]:
        '''This structure is an array that contains the configuration of this log transformer.

        A log transformer is an array of processors, where each processor applies one type of transformation to the log events that are ingested.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-transformer.html#cfn-logs-transformer-transformerconfig
        '''
        result = self._values.get("transformer_config")
        assert result is not None, "Required property 'transformer_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTransformer.ProcessorProperty]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTransformerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.ColumnRestriction",
    jsii_struct_bases=[],
    name_mapping={
        "comparison": "comparison",
        "number_value": "numberValue",
        "string_value": "stringValue",
    },
)
class ColumnRestriction:
    def __init__(
        self,
        *,
        comparison: builtins.str,
        number_value: typing.Optional[jsii.Number] = None,
        string_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param comparison: Comparison operator to use.
        :param number_value: Number value to compare to. Exactly one of 'stringValue' and 'numberValue' must be set.
        :param string_value: String value to compare to. Exactly one of 'stringValue' and 'numberValue' must be set.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            column_restriction = logs.ColumnRestriction(
                comparison="comparison",
            
                # the properties below are optional
                number_value=123,
                string_value="stringValue"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2766fe6d7d19a8737daff90dd79e476a2d4dcde95605b7656e40b088fdf6e64)
            check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
            check_type(argname="argument number_value", value=number_value, expected_type=type_hints["number_value"])
            check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "comparison": comparison,
        }
        if number_value is not None:
            self._values["number_value"] = number_value
        if string_value is not None:
            self._values["string_value"] = string_value

    @builtins.property
    def comparison(self) -> builtins.str:
        '''Comparison operator to use.'''
        result = self._values.get("comparison")
        assert result is not None, "Required property 'comparison' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def number_value(self) -> typing.Optional[jsii.Number]:
        '''Number value to compare to.

        Exactly one of 'stringValue' and 'numberValue' must be set.
        '''
        result = self._values.get("number_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def string_value(self) -> typing.Optional[builtins.str]:
        '''String value to compare to.

        Exactly one of 'stringValue' and 'numberValue' must be set.
        '''
        result = self._values.get("string_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ColumnRestriction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CopyValueEntryProperty",
    jsii_struct_bases=[],
    name_mapping={
        "source": "source",
        "target": "target",
        "overwrite_if_exists": "overwriteIfExists",
    },
)
class CopyValueEntryProperty:
    def __init__(
        self,
        *,
        source: builtins.str,
        target: builtins.str,
        overwrite_if_exists: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''This object defines one value to be copied with the copyValue processor.

        :param source: The key to copy.
        :param target: The key of the field to copy the value to.
        :param overwrite_if_exists: Specifies whether to overwrite the value if the target key already exists. Default: false

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            copy_value_entry_property = logs.CopyValueEntryProperty(
                source="source",
                target="target",
            
                # the properties below are optional
                overwrite_if_exists=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e58c798612261b35fc101134a189fa095e471b40cde2b522022473cb130c8ffd)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument overwrite_if_exists", value=overwrite_if_exists, expected_type=type_hints["overwrite_if_exists"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source": source,
            "target": target,
        }
        if overwrite_if_exists is not None:
            self._values["overwrite_if_exists"] = overwrite_if_exists

    @builtins.property
    def source(self) -> builtins.str:
        '''The key to copy.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''The key of the field to copy the value to.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def overwrite_if_exists(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether to overwrite the value if the target key already exists.

        :default: false
        '''
        result = self._values.get("overwrite_if_exists")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CopyValueEntryProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CopyValueProperty",
    jsii_struct_bases=[],
    name_mapping={"entries": "entries"},
)
class CopyValueProperty:
    def __init__(
        self,
        *,
        entries: typing.Sequence[typing.Union[CopyValueEntryProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Copy Value processor, copies values from source to target for each entry.

        This processor copies values within a log event.
        You can also use this processor to add metadata to log events by copying values from metadata keys.
        For more information about this processor including examples, see copyValue in the CloudWatch Logs User Guide.

        :param entries: List of sources and target to copy. An array of CopyValueEntry objects, where each object contains information about one field value to copy.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            copy_value_property = logs.CopyValueProperty(
                entries=[logs.CopyValueEntryProperty(
                    source="source",
                    target="target",
            
                    # the properties below are optional
                    overwrite_if_exists=False
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e1d63720cc55ad0f9fd25a9ccd1c33e428ce8f9353bb8eb3a0ffe5316b5e40d)
            check_type(argname="argument entries", value=entries, expected_type=type_hints["entries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entries": entries,
        }

    @builtins.property
    def entries(self) -> typing.List[CopyValueEntryProperty]:
        '''List of sources and target to copy.

        An array of CopyValueEntry objects, where each object contains information about one field value to copy.
        '''
        result = self._values.get("entries")
        assert result is not None, "Required property 'entries' is missing"
        return typing.cast(typing.List[CopyValueEntryProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CopyValueProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CrossAccountDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "role": "role",
        "target_arn": "targetArn",
        "destination_name": "destinationName",
    },
)
class CrossAccountDestinationProps:
    def __init__(
        self,
        *,
        role: _IRole_235f5d8e,
        target_arn: builtins.str,
        destination_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a CrossAccountDestination.

        :param role: The role to assume that grants permissions to write to 'target'. The role must be assumable by 'logs.{REGION}.amazonaws.com'.
        :param target_arn: The log destination target's ARN.
        :param destination_name: The name of the log destination. Default: Automatically generated

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_logs as logs
            
            # role: iam.Role
            
            cross_account_destination_props = logs.CrossAccountDestinationProps(
                role=role,
                target_arn="targetArn",
            
                # the properties below are optional
                destination_name="destinationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4be07d68ab857f5ae6300c8382cb03fbeec1052d13af65659f773e30196e8c1)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            check_type(argname="argument destination_name", value=destination_name, expected_type=type_hints["destination_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role": role,
            "target_arn": target_arn,
        }
        if destination_name is not None:
            self._values["destination_name"] = destination_name

    @builtins.property
    def role(self) -> _IRole_235f5d8e:
        '''The role to assume that grants permissions to write to 'target'.

        The role must be assumable by 'logs.{REGION}.amazonaws.com'.
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(_IRole_235f5d8e, result)

    @builtins.property
    def target_arn(self) -> builtins.str:
        '''The log destination target's ARN.'''
        result = self._values.get("target_arn")
        assert result is not None, "Required property 'target_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_name(self) -> typing.Optional[builtins.str]:
        '''The name of the log destination.

        :default: Automatically generated
        '''
        result = self._values.get("destination_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CrossAccountDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.CsvProperty",
    jsii_struct_bases=[],
    name_mapping={
        "columns": "columns",
        "delimiter": "delimiter",
        "quote_character": "quoteCharacter",
        "source": "source",
    },
)
class CsvProperty:
    def __init__(
        self,
        *,
        columns: typing.Optional[typing.Sequence[builtins.str]] = None,
        delimiter: typing.Optional["DelimiterCharacter"] = None,
        quote_character: typing.Optional["QuoteCharacter"] = None,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The CSV processor parses comma-separated values (CSV) from the log events into columns.

        For more information about this processor including examples, see csv in the CloudWatch Logs User Guide.

        :param columns: An array of names to use for the columns in the transformed log event. Default: - Column names ([column_1, column_2 ...]) are used
        :param delimiter: Character used to separate each column in the original comma-separated value log event. Default: DelimiterCharacter.COMMA
        :param quote_character: Character used as a text qualifier for a single column of data. Default: QuoteCharacter.DOUBLE_QUOTE
        :param source: The path to the field in the log event that has the comma separated values to be parsed. Default: '@message'

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            csv_property = logs.CsvProperty(
                columns=["columns"],
                delimiter=logs.DelimiterCharacter.COMMA,
                quote_character=logs.QuoteCharacter.DOUBLE_QUOTE,
                source="source"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c40d29b973c2c88882518795acd7090c9554983c5f83ed50100c80f59d45e767)
            check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
            check_type(argname="argument delimiter", value=delimiter, expected_type=type_hints["delimiter"])
            check_type(argname="argument quote_character", value=quote_character, expected_type=type_hints["quote_character"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if columns is not None:
            self._values["columns"] = columns
        if delimiter is not None:
            self._values["delimiter"] = delimiter
        if quote_character is not None:
            self._values["quote_character"] = quote_character
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def columns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of names to use for the columns in the transformed log event.

        :default: - Column names ([column_1, column_2 ...]) are used
        '''
        result = self._values.get("columns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def delimiter(self) -> typing.Optional["DelimiterCharacter"]:
        '''Character used to separate each column in the original comma-separated value log event.

        :default: DelimiterCharacter.COMMA
        '''
        result = self._values.get("delimiter")
        return typing.cast(typing.Optional["DelimiterCharacter"], result)

    @builtins.property
    def quote_character(self) -> typing.Optional["QuoteCharacter"]:
        '''Character used as a text qualifier for a single column of data.

        :default: QuoteCharacter.DOUBLE_QUOTE
        '''
        result = self._values.get("quote_character")
        return typing.cast(typing.Optional["QuoteCharacter"], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''The path to the field in the log event that has the comma separated values to be parsed.

        :default: '@message'
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CsvProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.DataConverterProps",
    jsii_struct_bases=[BaseProcessorProps],
    name_mapping={
        "type": "type",
        "date_time_converter_options": "dateTimeConverterOptions",
        "type_converter_options": "typeConverterOptions",
    },
)
class DataConverterProps(BaseProcessorProps):
    def __init__(
        self,
        *,
        type: "DataConverterType",
        date_time_converter_options: typing.Optional[typing.Union["DateTimeConverterProperty", typing.Dict[builtins.str, typing.Any]]] = None,
        type_converter_options: typing.Optional[typing.Union["TypeConverterProperty", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Properties for creating data converter processors.

        :param type: The type of data conversion operation.
        :param date_time_converter_options: Options for datetime conversion. Required when type is DATETIME_CONVERTER. Default: - No date time converter processor is created if not set
        :param type_converter_options: Options for type conversion. Required when type is TYPE_CONVERTER. Default: - No type convertor processor is created if not set

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            data_converter_props = logs.DataConverterProps(
                type=logs.DataConverterType.TYPE_CONVERTER,
            
                # the properties below are optional
                date_time_converter_options=logs.DateTimeConverterProperty(
                    locale="locale",
                    match_patterns=["matchPatterns"],
                    source="source",
                    target="target",
            
                    # the properties below are optional
                    source_timezone="sourceTimezone",
                    target_format="targetFormat",
                    target_timezone="targetTimezone"
                ),
                type_converter_options=logs.TypeConverterProperty(
                    entries=[logs.TypeConverterEntryProperty(
                        key="key",
                        type=logs.TypeConverterType.BOOLEAN
                    )]
                )
            )
        '''
        if isinstance(date_time_converter_options, dict):
            date_time_converter_options = DateTimeConverterProperty(**date_time_converter_options)
        if isinstance(type_converter_options, dict):
            type_converter_options = TypeConverterProperty(**type_converter_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5d3ea1ab4dc61f97346ae6ae2134ce81803e6f823c3b99e67d009a033371f84)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument date_time_converter_options", value=date_time_converter_options, expected_type=type_hints["date_time_converter_options"])
            check_type(argname="argument type_converter_options", value=type_converter_options, expected_type=type_hints["type_converter_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if date_time_converter_options is not None:
            self._values["date_time_converter_options"] = date_time_converter_options
        if type_converter_options is not None:
            self._values["type_converter_options"] = type_converter_options

    @builtins.property
    def type(self) -> "DataConverterType":
        '''The type of data conversion operation.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("DataConverterType", result)

    @builtins.property
    def date_time_converter_options(
        self,
    ) -> typing.Optional["DateTimeConverterProperty"]:
        '''Options for datetime conversion.

        Required when type is DATETIME_CONVERTER.

        :default: - No date time converter processor is created if not set
        '''
        result = self._values.get("date_time_converter_options")
        return typing.cast(typing.Optional["DateTimeConverterProperty"], result)

    @builtins.property
    def type_converter_options(self) -> typing.Optional["TypeConverterProperty"]:
        '''Options for type conversion.

        Required when type is TYPE_CONVERTER.

        :default: - No type convertor processor is created if not set
        '''
        result = self._values.get("type_converter_options")
        return typing.cast(typing.Optional["TypeConverterProperty"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataConverterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.DataConverterType")
class DataConverterType(enum.Enum):
    '''Types of data conversion operations.

    Defines operations that can convert data from one format to another.
    '''

    TYPE_CONVERTER = "TYPE_CONVERTER"
    '''Convert data types.'''
    DATETIME_CONVERTER = "DATETIME_CONVERTER"
    '''Convert datetime formats.'''


class DataIdentifier(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.DataIdentifier",
):
    '''A data protection identifier.

    If an identifier is supported but not in this class, it can be passed in the constructor instead.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_kinesisfirehose as firehose
        
        
        log_group_destination = logs.LogGroup(self, "LogGroupLambdaAudit",
            log_group_name="auditDestinationForCDK"
        )
        
        bucket = s3.Bucket(self, "audit-bucket")
        s3_destination = firehose.S3Bucket(bucket)
        
        delivery_stream = firehose.DeliveryStream(self, "Delivery Stream",
            destination=s3_destination
        )
        
        data_protection_policy = logs.DataProtectionPolicy(
            name="data protection policy",
            description="policy description",
            identifiers=[logs.DataIdentifier.DRIVERSLICENSE_US,  # managed data identifier
                logs.DataIdentifier("EmailAddress"),  # forward compatibility for new managed data identifiers
                logs.CustomDataIdentifier("EmployeeId", "EmployeeId-\\d{9}")
            ],  # custom data identifier
            log_group_audit_destination=log_group_destination,
            s3_bucket_audit_destination=bucket,
            delivery_stream_name_audit_destination=delivery_stream.delivery_stream_name
        )
        
        logs.LogGroup(self, "LogGroupLambda",
            log_group_name="cdkIntegLogGroup",
            data_protection_policy=data_protection_policy
        )
    '''

    def __init__(self, name: builtins.str) -> None:
        '''Create a managed data identifier not in the list of static members.

        This is used to maintain forward compatibility, in case a new managed identifier is supported but not updated in CDK yet.

        :param name: - name of the identifier.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15f2f9a4aba70e88d25dcda444a45fe96535b0317fb974d64d2b70c8e6982915)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        jsii.create(self.__class__, self, [name])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ADDRESS")
    def ADDRESS(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "ADDRESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWSSECRETKEY")
    def AWSSECRETKEY(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "AWSSECRETKEY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BANKACCOUNTNUMBER_DE")
    def BANKACCOUNTNUMBER_DE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "BANKACCOUNTNUMBER_DE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BANKACCOUNTNUMBER_ES")
    def BANKACCOUNTNUMBER_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "BANKACCOUNTNUMBER_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BANKACCOUNTNUMBER_FR")
    def BANKACCOUNTNUMBER_FR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "BANKACCOUNTNUMBER_FR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BANKACCOUNTNUMBER_GB")
    def BANKACCOUNTNUMBER_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "BANKACCOUNTNUMBER_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BANKACCOUNTNUMBER_IT")
    def BANKACCOUNTNUMBER_IT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "BANKACCOUNTNUMBER_IT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BANKACCOUNTNUMBER_US")
    def BANKACCOUNTNUMBER_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "BANKACCOUNTNUMBER_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CEPCODE_BR")
    def CEPCODE_BR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "CEPCODE_BR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CNPJ_BR")
    def CNPJ_BR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "CNPJ_BR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CPFCODE_BR")
    def CPFCODE_BR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "CPFCODE_BR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CREDITCARDEXPIRATION")
    def CREDITCARDEXPIRATION(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "CREDITCARDEXPIRATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CREDITCARDNUMBER")
    def CREDITCARDNUMBER(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "CREDITCARDNUMBER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CREDITCARDSECURITYCODE")
    def CREDITCARDSECURITYCODE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "CREDITCARDSECURITYCODE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_AT")
    def DRIVERSLICENSE_AT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_AT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_AU")
    def DRIVERSLICENSE_AU(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_AU"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_BE")
    def DRIVERSLICENSE_BE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_BE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_BG")
    def DRIVERSLICENSE_BG(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_BG"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_CA")
    def DRIVERSLICENSE_CA(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_CA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_CY")
    def DRIVERSLICENSE_CY(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_CY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_CZ")
    def DRIVERSLICENSE_CZ(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_CZ"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_DE")
    def DRIVERSLICENSE_DE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_DE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_DK")
    def DRIVERSLICENSE_DK(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_DK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_EE")
    def DRIVERSLICENSE_EE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_EE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_ES")
    def DRIVERSLICENSE_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_FI")
    def DRIVERSLICENSE_FI(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_FI"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_FR")
    def DRIVERSLICENSE_FR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_FR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_GB")
    def DRIVERSLICENSE_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_GR")
    def DRIVERSLICENSE_GR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_GR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_HR")
    def DRIVERSLICENSE_HR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_HR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_HU")
    def DRIVERSLICENSE_HU(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_HU"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_IE")
    def DRIVERSLICENSE_IE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_IE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_IT")
    def DRIVERSLICENSE_IT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_IT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_LT")
    def DRIVERSLICENSE_LT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_LT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_LU")
    def DRIVERSLICENSE_LU(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_LU"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_LV")
    def DRIVERSLICENSE_LV(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_LV"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_MT")
    def DRIVERSLICENSE_MT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_MT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_NL")
    def DRIVERSLICENSE_NL(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_NL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_PL")
    def DRIVERSLICENSE_PL(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_PL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_PT")
    def DRIVERSLICENSE_PT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_PT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_RO")
    def DRIVERSLICENSE_RO(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_RO"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_SE")
    def DRIVERSLICENSE_SE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_SE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_SI")
    def DRIVERSLICENSE_SI(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_SI"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_SK")
    def DRIVERSLICENSE_SK(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_SK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRIVERSLICENSE_US")
    def DRIVERSLICENSE_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRIVERSLICENSE_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DRUGENFORCEMENTAGENCYNUMBER_US")
    def DRUGENFORCEMENTAGENCYNUMBER_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "DRUGENFORCEMENTAGENCYNUMBER_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELECTORALROLLNUMBER_GB")
    def ELECTORALROLLNUMBER_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "ELECTORALROLLNUMBER_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EMAILADDRESS")
    def EMAILADDRESS(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "EMAILADDRESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="HEALTHCAREPROCEDURECODE_US")
    def HEALTHCAREPROCEDURECODE_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "HEALTHCAREPROCEDURECODE_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="HEALTHINSURANCECARDNUMBER_EU")
    def HEALTHINSURANCECARDNUMBER_EU(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "HEALTHINSURANCECARDNUMBER_EU"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="HEALTHINSURANCECLAIMNUMBER_US")
    def HEALTHINSURANCECLAIMNUMBER_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "HEALTHINSURANCECLAIMNUMBER_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="HEALTHINSURANCENUMBER_FR")
    def HEALTHINSURANCENUMBER_FR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "HEALTHINSURANCENUMBER_FR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="INDIVIDUALTAXIDENTIFICATIONNUMBER_US")
    def INDIVIDUALTAXIDENTIFICATIONNUMBER_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "INDIVIDUALTAXIDENTIFICATIONNUMBER_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="INSEECODE_FR")
    def INSEECODE_FR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "INSEECODE_FR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IPADDRESS")
    def IPADDRESS(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "IPADDRESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LATLONG")
    def LATLONG(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "LATLONG"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MEDICAREBENEFICIARYNUMBER_US")
    def MEDICAREBENEFICIARYNUMBER_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "MEDICAREBENEFICIARYNUMBER_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NAME")
    def NAME(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NAME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NATIONALDRUGCODE_US")
    def NATIONALDRUGCODE_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NATIONALDRUGCODE_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NATIONALIDENTIFICATIONNUMBER_DE")
    def NATIONALIDENTIFICATIONNUMBER_DE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NATIONALIDENTIFICATIONNUMBER_DE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NATIONALIDENTIFICATIONNUMBER_ES")
    def NATIONALIDENTIFICATIONNUMBER_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NATIONALIDENTIFICATIONNUMBER_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NATIONALIDENTIFICATIONNUMBER_IT")
    def NATIONALIDENTIFICATIONNUMBER_IT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NATIONALIDENTIFICATIONNUMBER_IT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NATIONALINSURANCENUMBER_GB")
    def NATIONALINSURANCENUMBER_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NATIONALINSURANCENUMBER_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NATIONALPROVIDERID_US")
    def NATIONALPROVIDERID_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NATIONALPROVIDERID_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NHSNUMBER_GB")
    def NHSNUMBER_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NHSNUMBER_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NIENUMBER_ES")
    def NIENUMBER_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NIENUMBER_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NIFNUMBER_ES")
    def NIFNUMBER_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "NIFNUMBER_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSSHPRIVATEKEY")
    def OPENSSHPRIVATEKEY(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "OPENSSHPRIVATEKEY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PASSPORTNUMBER_CA")
    def PASSPORTNUMBER_CA(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PASSPORTNUMBER_CA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PASSPORTNUMBER_DE")
    def PASSPORTNUMBER_DE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PASSPORTNUMBER_DE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PASSPORTNUMBER_ES")
    def PASSPORTNUMBER_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PASSPORTNUMBER_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PASSPORTNUMBER_FR")
    def PASSPORTNUMBER_FR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PASSPORTNUMBER_FR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PASSPORTNUMBER_GB")
    def PASSPORTNUMBER_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PASSPORTNUMBER_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PASSPORTNUMBER_IT")
    def PASSPORTNUMBER_IT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PASSPORTNUMBER_IT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PASSPORTNUMBER_US")
    def PASSPORTNUMBER_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PASSPORTNUMBER_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PERMANENTRESIDENCENUMBER_CA")
    def PERMANENTRESIDENCENUMBER_CA(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PERMANENTRESIDENCENUMBER_CA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PERSONALHEALTHNUMBER_CA")
    def PERSONALHEALTHNUMBER_CA(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PERSONALHEALTHNUMBER_CA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PGPPRIVATEKEY")
    def PGPPRIVATEKEY(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PGPPRIVATEKEY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PHONENUMBER_BR")
    def PHONENUMBER_BR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PHONENUMBER_BR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PHONENUMBER_DE")
    def PHONENUMBER_DE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PHONENUMBER_DE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PHONENUMBER_ES")
    def PHONENUMBER_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PHONENUMBER_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PHONENUMBER_FR")
    def PHONENUMBER_FR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PHONENUMBER_FR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PHONENUMBER_GB")
    def PHONENUMBER_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PHONENUMBER_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PHONENUMBER_IT")
    def PHONENUMBER_IT(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PHONENUMBER_IT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PHONENUMBER_US")
    def PHONENUMBER_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PHONENUMBER_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PKCSPRIVATEKEY")
    def PKCSPRIVATEKEY(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PKCSPRIVATEKEY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="POSTALCODE_CA")
    def POSTALCODE_CA(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "POSTALCODE_CA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PUTTYPRIVATEKEY")
    def PUTTYPRIVATEKEY(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "PUTTYPRIVATEKEY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RGNUMBER_BR")
    def RGNUMBER_BR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "RGNUMBER_BR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SOCIALINSURANCENUMBER_CA")
    def SOCIALINSURANCENUMBER_CA(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "SOCIALINSURANCENUMBER_CA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SSN_ES")
    def SSN_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "SSN_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SSN_US")
    def SSN_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "SSN_US"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TAXID_DE")
    def TAXID_DE(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "TAXID_DE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TAXID_ES")
    def TAXID_ES(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "TAXID_ES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TAXID_FR")
    def TAXID_FR(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "TAXID_FR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TAXID_GB")
    def TAXID_GB(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "TAXID_GB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VEHICLEIDENTIFICATIONNUMBER")
    def VEHICLEIDENTIFICATIONNUMBER(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "VEHICLEIDENTIFICATIONNUMBER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ZIPCODE_US")
    def ZIPCODE_US(cls) -> "DataIdentifier":
        return typing.cast("DataIdentifier", jsii.sget(cls, "ZIPCODE_US"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''- name of the identifier.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))


class DataProtectionPolicy(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.DataProtectionPolicy",
):
    '''Creates a data protection policy for CloudWatch Logs log groups.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_kinesisfirehose as firehose
        
        
        log_group_destination = logs.LogGroup(self, "LogGroupLambdaAudit",
            log_group_name="auditDestinationForCDK"
        )
        
        bucket = s3.Bucket(self, "audit-bucket")
        s3_destination = firehose.S3Bucket(bucket)
        
        delivery_stream = firehose.DeliveryStream(self, "Delivery Stream",
            destination=s3_destination
        )
        
        data_protection_policy = logs.DataProtectionPolicy(
            name="data protection policy",
            description="policy description",
            identifiers=[logs.DataIdentifier.DRIVERSLICENSE_US,  # managed data identifier
                logs.DataIdentifier("EmailAddress"),  # forward compatibility for new managed data identifiers
                logs.CustomDataIdentifier("EmployeeId", "EmployeeId-\\d{9}")
            ],  # custom data identifier
            log_group_audit_destination=log_group_destination,
            s3_bucket_audit_destination=bucket,
            delivery_stream_name_audit_destination=delivery_stream.delivery_stream_name
        )
        
        logs.LogGroup(self, "LogGroupLambda",
            log_group_name="cdkIntegLogGroup",
            data_protection_policy=data_protection_policy
        )
    '''

    def __init__(
        self,
        *,
        identifiers: typing.Sequence[DataIdentifier],
        delivery_stream_name_audit_destination: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        log_group_audit_destination: typing.Optional["ILogGroup"] = None,
        name: typing.Optional[builtins.str] = None,
        s3_bucket_audit_destination: typing.Optional[_IBucket_42e086fd] = None,
    ) -> None:
        '''
        :param identifiers: List of data protection identifiers. Managed data identifiers must be in the following list: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL-managed-data-identifiers.html Custom data identifiers must have a valid regex defined: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL-custom-data-identifiers.html#custom-data-identifiers-constraints
        :param delivery_stream_name_audit_destination: Amazon Data Firehose delivery stream to send audit findings to. The delivery stream must already exist. Default: - no firehose delivery stream audit destination
        :param description: Description of the data protection policy. Default: - 'cdk generated data protection policy'
        :param log_group_audit_destination: CloudWatch Logs log group to send audit findings to. The log group must already exist prior to creating the data protection policy. Default: - no CloudWatch Logs audit destination
        :param name: Name of the data protection policy. Default: - 'data-protection-policy-cdk'
        :param s3_bucket_audit_destination: S3 bucket to send audit findings to. The bucket must already exist. Default: - no S3 bucket audit destination
        '''
        props = DataProtectionPolicyProps(
            identifiers=identifiers,
            delivery_stream_name_audit_destination=delivery_stream_name_audit_destination,
            description=description,
            log_group_audit_destination=log_group_audit_destination,
            name=name,
            s3_bucket_audit_destination=s3_bucket_audit_destination,
        )

        jsii.create(self.__class__, self, [props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.DataProtectionPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "identifiers": "identifiers",
        "delivery_stream_name_audit_destination": "deliveryStreamNameAuditDestination",
        "description": "description",
        "log_group_audit_destination": "logGroupAuditDestination",
        "name": "name",
        "s3_bucket_audit_destination": "s3BucketAuditDestination",
    },
)
class DataProtectionPolicyProps:
    def __init__(
        self,
        *,
        identifiers: typing.Sequence[DataIdentifier],
        delivery_stream_name_audit_destination: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        log_group_audit_destination: typing.Optional["ILogGroup"] = None,
        name: typing.Optional[builtins.str] = None,
        s3_bucket_audit_destination: typing.Optional[_IBucket_42e086fd] = None,
    ) -> None:
        '''Properties for creating a data protection policy.

        :param identifiers: List of data protection identifiers. Managed data identifiers must be in the following list: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL-managed-data-identifiers.html Custom data identifiers must have a valid regex defined: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL-custom-data-identifiers.html#custom-data-identifiers-constraints
        :param delivery_stream_name_audit_destination: Amazon Data Firehose delivery stream to send audit findings to. The delivery stream must already exist. Default: - no firehose delivery stream audit destination
        :param description: Description of the data protection policy. Default: - 'cdk generated data protection policy'
        :param log_group_audit_destination: CloudWatch Logs log group to send audit findings to. The log group must already exist prior to creating the data protection policy. Default: - no CloudWatch Logs audit destination
        :param name: Name of the data protection policy. Default: - 'data-protection-policy-cdk'
        :param s3_bucket_audit_destination: S3 bucket to send audit findings to. The bucket must already exist. Default: - no S3 bucket audit destination

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_kinesisfirehose as firehose
            
            
            log_group_destination = logs.LogGroup(self, "LogGroupLambdaAudit",
                log_group_name="auditDestinationForCDK"
            )
            
            bucket = s3.Bucket(self, "audit-bucket")
            s3_destination = firehose.S3Bucket(bucket)
            
            delivery_stream = firehose.DeliveryStream(self, "Delivery Stream",
                destination=s3_destination
            )
            
            data_protection_policy = logs.DataProtectionPolicy(
                name="data protection policy",
                description="policy description",
                identifiers=[logs.DataIdentifier.DRIVERSLICENSE_US,  # managed data identifier
                    logs.DataIdentifier("EmailAddress"),  # forward compatibility for new managed data identifiers
                    logs.CustomDataIdentifier("EmployeeId", "EmployeeId-\\d{9}")
                ],  # custom data identifier
                log_group_audit_destination=log_group_destination,
                s3_bucket_audit_destination=bucket,
                delivery_stream_name_audit_destination=delivery_stream.delivery_stream_name
            )
            
            logs.LogGroup(self, "LogGroupLambda",
                log_group_name="cdkIntegLogGroup",
                data_protection_policy=data_protection_policy
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7783165e1d00e232a8ee35869f53b7ff500c9680f96b895f705e24475c7b6b2)
            check_type(argname="argument identifiers", value=identifiers, expected_type=type_hints["identifiers"])
            check_type(argname="argument delivery_stream_name_audit_destination", value=delivery_stream_name_audit_destination, expected_type=type_hints["delivery_stream_name_audit_destination"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument log_group_audit_destination", value=log_group_audit_destination, expected_type=type_hints["log_group_audit_destination"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument s3_bucket_audit_destination", value=s3_bucket_audit_destination, expected_type=type_hints["s3_bucket_audit_destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identifiers": identifiers,
        }
        if delivery_stream_name_audit_destination is not None:
            self._values["delivery_stream_name_audit_destination"] = delivery_stream_name_audit_destination
        if description is not None:
            self._values["description"] = description
        if log_group_audit_destination is not None:
            self._values["log_group_audit_destination"] = log_group_audit_destination
        if name is not None:
            self._values["name"] = name
        if s3_bucket_audit_destination is not None:
            self._values["s3_bucket_audit_destination"] = s3_bucket_audit_destination

    @builtins.property
    def identifiers(self) -> typing.List[DataIdentifier]:
        '''List of data protection identifiers.

        Managed data identifiers must be in the following list: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL-managed-data-identifiers.html
        Custom data identifiers must have a valid regex defined: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL-custom-data-identifiers.html#custom-data-identifiers-constraints
        '''
        result = self._values.get("identifiers")
        assert result is not None, "Required property 'identifiers' is missing"
        return typing.cast(typing.List[DataIdentifier], result)

    @builtins.property
    def delivery_stream_name_audit_destination(self) -> typing.Optional[builtins.str]:
        '''Amazon Data Firehose delivery stream to send audit findings to.

        The delivery stream must already exist.

        :default: - no firehose delivery stream audit destination
        '''
        result = self._values.get("delivery_stream_name_audit_destination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the data protection policy.

        :default: - 'cdk generated data protection policy'
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_group_audit_destination(self) -> typing.Optional["ILogGroup"]:
        '''CloudWatch Logs log group to send audit findings to.

        The log group must already exist prior to creating the data protection policy.

        :default: - no CloudWatch Logs audit destination
        '''
        result = self._values.get("log_group_audit_destination")
        return typing.cast(typing.Optional["ILogGroup"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the data protection policy.

        :default: - 'data-protection-policy-cdk'
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_bucket_audit_destination(self) -> typing.Optional[_IBucket_42e086fd]:
        '''S3 bucket to send audit findings to.

        The bucket must already exist.

        :default: - no S3 bucket audit destination
        '''
        result = self._values.get("s3_bucket_audit_destination")
        return typing.cast(typing.Optional[_IBucket_42e086fd], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataProtectionPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.DateTimeConverterProperty",
    jsii_struct_bases=[],
    name_mapping={
        "locale": "locale",
        "match_patterns": "matchPatterns",
        "source": "source",
        "target": "target",
        "source_timezone": "sourceTimezone",
        "target_format": "targetFormat",
        "target_timezone": "targetTimezone",
    },
)
class DateTimeConverterProperty:
    def __init__(
        self,
        *,
        locale: builtins.str,
        match_patterns: typing.Sequence[builtins.str],
        source: builtins.str,
        target: builtins.str,
        source_timezone: typing.Optional[builtins.str] = None,
        target_format: typing.Optional[builtins.str] = None,
        target_timezone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''This processor converts a datetime string into a format that you specify.

        For more information about this processor including examples, see datetimeConverter in the CloudWatch Logs User Guide.

        :param locale: The locale of the source field.
        :param match_patterns: A list of patterns to match against the source field.
        :param source: The key to apply the date conversion to.
        :param target: The JSON field to store the result in.
        :param source_timezone: The time zone of the source field. Default: UTC
        :param target_format: The datetime format to use for the converted data in the target field. Default: "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'"
        :param target_timezone: The time zone of the target field. Default: UTC

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            date_time_converter_property = logs.DateTimeConverterProperty(
                locale="locale",
                match_patterns=["matchPatterns"],
                source="source",
                target="target",
            
                # the properties below are optional
                source_timezone="sourceTimezone",
                target_format="targetFormat",
                target_timezone="targetTimezone"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35bff5994e76c17a7e4672ebf2d30e06b26eb34c402c647a8af28f310c672633)
            check_type(argname="argument locale", value=locale, expected_type=type_hints["locale"])
            check_type(argname="argument match_patterns", value=match_patterns, expected_type=type_hints["match_patterns"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument source_timezone", value=source_timezone, expected_type=type_hints["source_timezone"])
            check_type(argname="argument target_format", value=target_format, expected_type=type_hints["target_format"])
            check_type(argname="argument target_timezone", value=target_timezone, expected_type=type_hints["target_timezone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "locale": locale,
            "match_patterns": match_patterns,
            "source": source,
            "target": target,
        }
        if source_timezone is not None:
            self._values["source_timezone"] = source_timezone
        if target_format is not None:
            self._values["target_format"] = target_format
        if target_timezone is not None:
            self._values["target_timezone"] = target_timezone

    @builtins.property
    def locale(self) -> builtins.str:
        '''The locale of the source field.'''
        result = self._values.get("locale")
        assert result is not None, "Required property 'locale' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_patterns(self) -> typing.List[builtins.str]:
        '''A list of patterns to match against the source field.'''
        result = self._values.get("match_patterns")
        assert result is not None, "Required property 'match_patterns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def source(self) -> builtins.str:
        '''The key to apply the date conversion to.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''The JSON field to store the result in.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_timezone(self) -> typing.Optional[builtins.str]:
        '''The time zone of the source field.

        :default: UTC
        '''
        result = self._values.get("source_timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_format(self) -> typing.Optional[builtins.str]:
        '''The datetime format to use for the converted data in the target field.

        :default: "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'"
        '''
        result = self._values.get("target_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_timezone(self) -> typing.Optional[builtins.str]:
        '''The time zone of the target field.

        :default: UTC
        '''
        result = self._values.get("target_timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DateTimeConverterProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.DateTimeFormat")
class DateTimeFormat(enum.Enum):
    '''Standard datetime formats for the DateTimeConverter processor.

    Provides common format patterns for date/time conversion.
    '''

    ISO_8601 = "ISO_8601"
    '''ISO 8601 format (yyyy-MM-ddTHH:mm:ssZ).'''
    UNIX_TIMESTAMP = "UNIX_TIMESTAMP"
    '''Unix timestamp (seconds since epoch).'''
    CUSTOM = "CUSTOM"
    '''Custom format specified by the targetFormat parameter.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.DelimiterCharacter")
class DelimiterCharacter(enum.Enum):
    '''Valid delimiter characters for CSV processor.

    Defines the character used to separate each column in CSV data.
    '''

    COMMA = "COMMA"
    '''Comma character.'''
    TAB = "TAB"
    '''Tab character.'''
    SPACE = "SPACE"
    '''Space character.'''
    SEMICOLON = "SEMICOLON"
    '''Semicolon character.'''
    PIPE = "PIPE"
    '''Pipe character.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.Distribution")
class Distribution(enum.Enum):
    '''The method used to distribute log data to the destination.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_logs_destinations as destinations
        import aws_cdk.aws_kinesis as kinesis
        
        # stream: kinesis.Stream
        # log_group: logs.LogGroup
        
        
        logs.SubscriptionFilter(self, "Subscription",
            log_group=log_group,
            destination=destinations.KinesisDestination(stream),
            filter_pattern=logs.FilterPattern.all_terms("ERROR", "MainThread"),
            filter_name="ErrorInMainThread",
            distribution=logs.Distribution.RANDOM
        )
    '''

    BY_LOG_STREAM = "BY_LOG_STREAM"
    '''Log events from the same log stream are kept together and sent to the same destination.'''
    RANDOM = "RANDOM"
    '''Log events are distributed across the log destinations randomly.'''


class FieldIndexPolicy(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.FieldIndexPolicy",
):
    '''Creates a field index policy for CloudWatch Logs log groups.

    :exampleMetadata: infused

    Example::

        field_index_policy = logs.FieldIndexPolicy(
            fields=["Operation", "RequestId"]
        )
        
        logs.LogGroup(self, "LogGroup",
            log_group_name="cdkIntegLogGroup",
            field_index_policies=[field_index_policy]
        )
    '''

    def __init__(self, *, fields: typing.Sequence[builtins.str]) -> None:
        '''
        :param fields: List of fields to index in log events. Default: no fields
        '''
        props = FieldIndexPolicyProps(fields=fields)

        jsii.create(self.__class__, self, [props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.FieldIndexPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"fields": "fields"},
)
class FieldIndexPolicyProps:
    def __init__(self, *, fields: typing.Sequence[builtins.str]) -> None:
        '''Properties for creating field index policies.

        :param fields: List of fields to index in log events. Default: no fields

        :exampleMetadata: infused

        Example::

            field_index_policy = logs.FieldIndexPolicy(
                fields=["Operation", "RequestId"]
            )
            
            logs.LogGroup(self, "LogGroup",
                log_group_name="cdkIntegLogGroup",
                field_index_policies=[field_index_policy]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8587c6606bf8df6db1fab55d5f7ea689b5960f088bf6825593078b791719378c)
            check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fields": fields,
        }

    @builtins.property
    def fields(self) -> typing.List[builtins.str]:
        '''List of fields to index in log events.

        :default: no fields
        '''
        result = self._values.get("fields")
        assert result is not None, "Required property 'fields' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FieldIndexPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FilterPattern(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.FilterPattern",
):
    '''A collection of static methods to generate appropriate ILogPatterns.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_logs_destinations as destinations
        
        # fn: lambda.Function
        # log_group: logs.LogGroup
        
        
        logs.SubscriptionFilter(self, "Subscription",
            log_group=log_group,
            destination=destinations.LambdaDestination(fn),
            filter_pattern=logs.FilterPattern.all_terms("ERROR", "MainThread"),
            filter_name="ErrorInMainThread"
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="all")
    @builtins.classmethod
    def all(cls, *patterns: "JsonPattern") -> "JsonPattern":
        '''A JSON log pattern that matches if all given JSON log patterns match.

        :param patterns: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef6e7314c6a5197496584b4f3fc9dc8a24050e8d3d30eabb788540b98e00e4f0)
            check_type(argname="argument patterns", value=patterns, expected_type=typing.Tuple[type_hints["patterns"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "all", [*patterns]))

    @jsii.member(jsii_name="allEvents")
    @builtins.classmethod
    def all_events(cls) -> "IFilterPattern":
        '''A log pattern that matches all events.'''
        return typing.cast("IFilterPattern", jsii.sinvoke(cls, "allEvents", []))

    @jsii.member(jsii_name="allTerms")
    @builtins.classmethod
    def all_terms(cls, *terms: builtins.str) -> "IFilterPattern":
        '''A log pattern that matches if all the strings given appear in the event.

        :param terms: The words to search for. All terms must match.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c83797f363cc2a7f1bb9ea15ea4f4d7eeed745e9d300970e536e8df78633b0a6)
            check_type(argname="argument terms", value=terms, expected_type=typing.Tuple[type_hints["terms"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("IFilterPattern", jsii.sinvoke(cls, "allTerms", [*terms]))

    @jsii.member(jsii_name="any")
    @builtins.classmethod
    def any(cls, *patterns: "JsonPattern") -> "JsonPattern":
        '''A JSON log pattern that matches if any of the given JSON log patterns match.

        :param patterns: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06cd0420e64a91321c2dbdcdb6fa54fa56bffd0eab770aa6aa4000670f1beec3)
            check_type(argname="argument patterns", value=patterns, expected_type=typing.Tuple[type_hints["patterns"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "any", [*patterns]))

    @jsii.member(jsii_name="anyTerm")
    @builtins.classmethod
    def any_term(cls, *terms: builtins.str) -> "IFilterPattern":
        '''A log pattern that matches if any of the strings given appear in the event.

        :param terms: The words to search for. Any terms must match.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b38181b10ed8fe5993dd7ec40690693fe0d164f997f37ddbf297f8b840de2b18)
            check_type(argname="argument terms", value=terms, expected_type=typing.Tuple[type_hints["terms"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("IFilterPattern", jsii.sinvoke(cls, "anyTerm", [*terms]))

    @jsii.member(jsii_name="anyTermGroup")
    @builtins.classmethod
    def any_term_group(
        cls,
        *term_groups: typing.List[builtins.str],
    ) -> "IFilterPattern":
        '''A log pattern that matches if any of the given term groups matches the event.

        A term group matches an event if all the terms in it appear in the event string.

        :param term_groups: A list of term groups to search for. Any one of the clauses must match.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2623b46359820ca611b2cf65fab9b8e6c24ef2bd3d30bcebc3d022b2173b58ee)
            check_type(argname="argument term_groups", value=term_groups, expected_type=typing.Tuple[type_hints["term_groups"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("IFilterPattern", jsii.sinvoke(cls, "anyTermGroup", [*term_groups]))

    @jsii.member(jsii_name="booleanValue")
    @builtins.classmethod
    def boolean_value(
        cls,
        json_field: builtins.str,
        value: builtins.bool,
    ) -> "JsonPattern":
        '''A JSON log pattern that matches if the field exists and equals the boolean value.

        :param json_field: Field inside JSON. Example: "$.myField"
        :param value: The value to match.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0e87f500ca69757a8ec1184452b5b2b45c68758c062a77bc2248afd2c3b793e)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "booleanValue", [json_field, value]))

    @jsii.member(jsii_name="exists")
    @builtins.classmethod
    def exists(cls, json_field: builtins.str) -> "JsonPattern":
        '''A JSON log patter that matches if the field exists.

        This is a readable convenience wrapper over 'field = *'

        :param json_field: Field inside JSON. Example: "$.myField"
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56192ad48c0fbacd0f9f10fc26eebe8f311d8164217227e094a00a61f7c0d300)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "exists", [json_field]))

    @jsii.member(jsii_name="isNull")
    @builtins.classmethod
    def is_null(cls, json_field: builtins.str) -> "JsonPattern":
        '''A JSON log pattern that matches if the field exists and has the special value 'null'.

        :param json_field: Field inside JSON. Example: "$.myField"
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93deee33b43c0efbe360f5ef6a60ba3cd0c1af95d7ca176abb95a482e1be8748)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "isNull", [json_field]))

    @jsii.member(jsii_name="literal")
    @builtins.classmethod
    def literal(cls, log_pattern_string: builtins.str) -> "IFilterPattern":
        '''Use the given string as log pattern.

        See https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html
        for information on writing log patterns.

        :param log_pattern_string: The pattern string to use.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65d91e718fc9d96060c30c68dee958f370d2ae16fbb2e3cf8f0030e0408b3320)
            check_type(argname="argument log_pattern_string", value=log_pattern_string, expected_type=type_hints["log_pattern_string"])
        return typing.cast("IFilterPattern", jsii.sinvoke(cls, "literal", [log_pattern_string]))

    @jsii.member(jsii_name="notExists")
    @builtins.classmethod
    def not_exists(cls, json_field: builtins.str) -> "JsonPattern":
        '''A JSON log pattern that matches if the field does not exist.

        :param json_field: Field inside JSON. Example: "$.myField"
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a90c7e4fc8c86ca2759be152abbd3a44e4e78851d525cdb047698b1825283849)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "notExists", [json_field]))

    @jsii.member(jsii_name="numberValue")
    @builtins.classmethod
    def number_value(
        cls,
        json_field: builtins.str,
        comparison: builtins.str,
        value: jsii.Number,
    ) -> "JsonPattern":
        '''A JSON log pattern that compares numerical values.

        This pattern only matches if the event is a JSON event, and the indicated field inside
        compares with the value in the indicated way.

        Use '$' to indicate the root of the JSON structure. The comparison operator can only
        compare equality or inequality. The '*' wildcard may appear in the value may at the
        start or at the end.

        For more information, see:

        https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html

        :param json_field: Field inside JSON. Example: "$.myField"
        :param comparison: Comparison to carry out. One of =, !=, <, <=, >, >=.
        :param value: The numerical value to compare to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1cb7dce1caa0866199f67de4ab23972e5d6dc3cd90ca77ce9a5f09f7dc2b1fa)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
            check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "numberValue", [json_field, comparison, value]))

    @jsii.member(jsii_name="regexValue")
    @builtins.classmethod
    def regex_value(
        cls,
        json_field: builtins.str,
        comparison: builtins.str,
        value: builtins.str,
    ) -> "JsonPattern":
        '''A JSON log pattern that compares against a Regex values.

        This pattern only matches if the event is a JSON event, and the indicated field inside
        compares with the regex value.

        Use '$' to indicate the root of the JSON structure. The comparison operator can only
        compare equality or inequality.

        For more information, see:

        https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html

        :param json_field: Field inside JSON. Example: "$.myField"
        :param comparison: Comparison to carry out. Either = or !=.
        :param value: The regex value to compare to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a7a4c0a4a33b651a6a0a1fe2ce451f20e4fa36e60b8a3b9bd496de7c0f04c0f)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
            check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "regexValue", [json_field, comparison, value]))

    @jsii.member(jsii_name="spaceDelimited")
    @builtins.classmethod
    def space_delimited(cls, *columns: builtins.str) -> "SpaceDelimitedTextPattern":
        '''A space delimited log pattern matcher.

        The log event is divided into space-delimited columns (optionally
        enclosed by "" or [] to capture spaces into column values), and names
        are given to each column.

        '...' may be specified once to match any number of columns.

        Afterwards, conditions may be added to individual columns.

        :param columns: The columns in the space-delimited log stream.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f5f56f60ccfd9dae1e3e3f54e54d87c6fb3e287c5bd2ad7924a4578ee4f8121)
            check_type(argname="argument columns", value=columns, expected_type=typing.Tuple[type_hints["columns"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("SpaceDelimitedTextPattern", jsii.sinvoke(cls, "spaceDelimited", [*columns]))

    @jsii.member(jsii_name="stringValue")
    @builtins.classmethod
    def string_value(
        cls,
        json_field: builtins.str,
        comparison: builtins.str,
        value: builtins.str,
    ) -> "JsonPattern":
        '''A JSON log pattern that compares string values.

        This pattern only matches if the event is a JSON event, and the indicated field inside
        compares with the string value.

        Use '$' to indicate the root of the JSON structure. The comparison operator can only
        compare equality or inequality. The '*' wildcard may appear in the value may at the
        start or at the end.

        For more information, see:

        https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html

        :param json_field: Field inside JSON. Example: "$.myField"
        :param comparison: Comparison to carry out. Either = or !=.
        :param value: The string value to compare to. May use '*' as wildcard at start or end of string.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31ecfe1cc2c14607ed9938dc33b51889185e1c9f4ea9e9e7ce494ae69f7d3374)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
            check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("JsonPattern", jsii.sinvoke(cls, "stringValue", [json_field, comparison, value]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.GrokProperty",
    jsii_struct_bases=[],
    name_mapping={"match": "match", "source": "source"},
)
class GrokProperty:
    def __init__(
        self,
        *,
        match: builtins.str,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''This processor uses pattern matching to parse and structure unstructured data.

        This processor can also extract fields from log messages.
        For more information about this processor including examples, see grok in the CloudWatch Logs User Guide.

        :param match: The grok pattern to match against the log event. For a list of supported grok patterns, see Supported grok patterns in the CloudWatch Logs User Guide.
        :param source: The path to the field in the log event that you want to parse. Default: '@message'

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            grok_property = logs.GrokProperty(
                match="match",
            
                # the properties below are optional
                source="source"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bba907d658ad5356562b8df18cf762bf9555e12e481aa8388b0a62d7ad1c35cd)
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "match": match,
        }
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def match(self) -> builtins.str:
        '''The grok pattern to match against the log event.

        For a list of supported grok patterns,
        see Supported grok patterns in the CloudWatch Logs User Guide.
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''The path to the field in the log event that you want to parse.

        :default: '@message'
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrokProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_logs.IFilterPattern")
class IFilterPattern(typing_extensions.Protocol):
    '''Interface for objects that can render themselves to log patterns.'''

    @builtins.property
    @jsii.member(jsii_name="logPatternString")
    def log_pattern_string(self) -> builtins.str:
        ...


class _IFilterPatternProxy:
    '''Interface for objects that can render themselves to log patterns.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_logs.IFilterPattern"

    @builtins.property
    @jsii.member(jsii_name="logPatternString")
    def log_pattern_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logPatternString"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFilterPattern).__jsii_proxy_class__ = lambda : _IFilterPatternProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_logs.ILogGroup")
class ILogGroup(_IResourceWithPolicy_720d64fc, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> builtins.str:
        '''The ARN of this log group, with ':*' appended.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        '''The name of this log group.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addMetricFilter")
    def add_metric_filter(
        self,
        id: builtins.str,
        *,
        filter_pattern: IFilterPattern,
        metric_name: builtins.str,
        metric_namespace: builtins.str,
        default_value: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        filter_name: typing.Optional[builtins.str] = None,
        metric_value: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> "MetricFilter":
        '''Create a new Metric Filter on this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param filter_pattern: Pattern to search for log events.
        :param metric_name: The name of the metric to emit.
        :param metric_namespace: The namespace of the metric to emit.
        :param default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
        :param dimensions: The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions. Default: - No dimensions attached to metrics.
        :param filter_name: The name of the metric filter. Default: - Cloudformation generated name.
        :param metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"
        :param unit: The unit to assign to the metric. Default: - No unit attached to metrics.
        '''
        ...

    @jsii.member(jsii_name="addStream")
    def add_stream(
        self,
        id: builtins.str,
        *,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> "LogStream":
        '''Create a new Log Stream for this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated
        '''
        ...

    @jsii.member(jsii_name="addSubscriptionFilter")
    def add_subscription_filter(
        self,
        id: builtins.str,
        *,
        destination: "ILogSubscriptionDestination",
        filter_pattern: IFilterPattern,
        distribution: typing.Optional[Distribution] = None,
        filter_name: typing.Optional[builtins.str] = None,
    ) -> "SubscriptionFilter":
        '''Create a new Subscription Filter on this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
        :param filter_pattern: Log events matching this pattern will be sent to the destination.
        :param distribution: The method used to distribute log data to the destination. This property can only be used with KinesisDestination. Default: Distribution.BY_LOG_STREAM
        :param filter_name: The name of the subscription filter. Default: Automatically generated
        '''
        ...

    @jsii.member(jsii_name="addTransformer")
    def add_transformer(
        self,
        id: builtins.str,
        *,
        transformer_config: typing.Sequence["IProcessor"],
        transformer_name: builtins.str,
    ) -> "Transformer":
        '''Create a new Transformer on this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param transformer_config: List of processors in a transformer.
        :param transformer_name: Name of the transformer.
        '''
        ...

    @jsii.member(jsii_name="extractMetric")
    def extract_metric(
        self,
        json_field: builtins.str,
        metric_namespace: builtins.str,
        metric_name: builtins.str,
    ) -> _Metric_e396a4dc:
        '''Extract a metric from structured log events in the LogGroup.

        Creates a MetricFilter on this LogGroup that will extract the value
        of the indicated JSON field in all records where it occurs.

        The metric will be available in CloudWatch Metrics under the
        indicated namespace and name.

        :param json_field: JSON field to extract (example: '$.myfield').
        :param metric_namespace: Namespace to emit the metric under.
        :param metric_name: Name to emit the metric under.

        :return: A Metric object representing the extracted metric
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Give the indicated permissions on this log group and all streams.

        :param grantee: -
        :param actions: -
        '''
        ...

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Give permissions to read from this log group and streams.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Give permissions to write to create and write to streams in this log group.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="logGroupPhysicalName")
    def log_group_physical_name(self) -> builtins.str:
        '''Public method to get the physical name of this log group.'''
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
        '''Return the given named metric for this Log Group.

        :param metric_name: The name of the metric.
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
        '''The volume of log events in uncompressed bytes uploaded to CloudWatch Logs.

        When used with the LogGroupName dimension, this is the volume of log events
        in uncompressed bytes uploaded to the log group.

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

    @jsii.member(jsii_name="metricIncomingLogEvents")
    def metric_incoming_log_events(
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
        '''The number of log events uploaded to CloudWatch Logs.

        When used with the LogGroupName dimension, this is the number of
        log events uploaded to the log group.

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


class _ILogGroupProxy(
    jsii.proxy_for(_IResourceWithPolicy_720d64fc), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_logs.ILogGroup"

    @builtins.property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> builtins.str:
        '''The ARN of this log group, with ':*' appended.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "logGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        '''The name of this log group.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @jsii.member(jsii_name="addMetricFilter")
    def add_metric_filter(
        self,
        id: builtins.str,
        *,
        filter_pattern: IFilterPattern,
        metric_name: builtins.str,
        metric_namespace: builtins.str,
        default_value: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        filter_name: typing.Optional[builtins.str] = None,
        metric_value: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> "MetricFilter":
        '''Create a new Metric Filter on this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param filter_pattern: Pattern to search for log events.
        :param metric_name: The name of the metric to emit.
        :param metric_namespace: The namespace of the metric to emit.
        :param default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
        :param dimensions: The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions. Default: - No dimensions attached to metrics.
        :param filter_name: The name of the metric filter. Default: - Cloudformation generated name.
        :param metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"
        :param unit: The unit to assign to the metric. Default: - No unit attached to metrics.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c3910e9df11478e889b7f25e252df8a33e79b82dd18c304bf83e6be63f60c95)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = MetricFilterOptions(
            filter_pattern=filter_pattern,
            metric_name=metric_name,
            metric_namespace=metric_namespace,
            default_value=default_value,
            dimensions=dimensions,
            filter_name=filter_name,
            metric_value=metric_value,
            unit=unit,
        )

        return typing.cast("MetricFilter", jsii.invoke(self, "addMetricFilter", [id, props]))

    @jsii.member(jsii_name="addStream")
    def add_stream(
        self,
        id: builtins.str,
        *,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> "LogStream":
        '''Create a new Log Stream for this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad3db791d4d809f8716f4717b634e830370009e865e37f5c54e65cc5c5d57102)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StreamOptions(log_stream_name=log_stream_name)

        return typing.cast("LogStream", jsii.invoke(self, "addStream", [id, props]))

    @jsii.member(jsii_name="addSubscriptionFilter")
    def add_subscription_filter(
        self,
        id: builtins.str,
        *,
        destination: "ILogSubscriptionDestination",
        filter_pattern: IFilterPattern,
        distribution: typing.Optional[Distribution] = None,
        filter_name: typing.Optional[builtins.str] = None,
    ) -> "SubscriptionFilter":
        '''Create a new Subscription Filter on this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
        :param filter_pattern: Log events matching this pattern will be sent to the destination.
        :param distribution: The method used to distribute log data to the destination. This property can only be used with KinesisDestination. Default: Distribution.BY_LOG_STREAM
        :param filter_name: The name of the subscription filter. Default: Automatically generated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3445e5a6f896ca9cd9e8a527d7229440b3a517fd59dc21bc08b64ef68e4f4eaa)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SubscriptionFilterOptions(
            destination=destination,
            filter_pattern=filter_pattern,
            distribution=distribution,
            filter_name=filter_name,
        )

        return typing.cast("SubscriptionFilter", jsii.invoke(self, "addSubscriptionFilter", [id, props]))

    @jsii.member(jsii_name="addTransformer")
    def add_transformer(
        self,
        id: builtins.str,
        *,
        transformer_config: typing.Sequence["IProcessor"],
        transformer_name: builtins.str,
    ) -> "Transformer":
        '''Create a new Transformer on this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param transformer_config: List of processors in a transformer.
        :param transformer_name: Name of the transformer.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48b998ae428fa24bcd8e738e7f4b31c609a8b722db7837c472033393d2ad8523)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TransformerOptions(
            transformer_config=transformer_config, transformer_name=transformer_name
        )

        return typing.cast("Transformer", jsii.invoke(self, "addTransformer", [id, props]))

    @jsii.member(jsii_name="extractMetric")
    def extract_metric(
        self,
        json_field: builtins.str,
        metric_namespace: builtins.str,
        metric_name: builtins.str,
    ) -> _Metric_e396a4dc:
        '''Extract a metric from structured log events in the LogGroup.

        Creates a MetricFilter on this LogGroup that will extract the value
        of the indicated JSON field in all records where it occurs.

        The metric will be available in CloudWatch Metrics under the
        indicated namespace and name.

        :param json_field: JSON field to extract (example: '$.myfield').
        :param metric_namespace: Namespace to emit the metric under.
        :param metric_name: Name to emit the metric under.

        :return: A Metric object representing the extracted metric
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dc31b09300449039c7ac2db2c1e23ab325c60cc2fa2fa9ee5b513c2e1d62f7b)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
            check_type(argname="argument metric_namespace", value=metric_namespace, expected_type=type_hints["metric_namespace"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "extractMetric", [json_field, metric_namespace, metric_name]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Give the indicated permissions on this log group and all streams.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d45146324c9cc51983b9b92779906c83ea73e499386493771cdd256c131ca87)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Give permissions to read from this log group and streams.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10f2b216c33139da1022d0b7d73974166dcf17c508e30913421c9f89375a9bb0)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Give permissions to write to create and write to streams in this log group.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__558c66823e9e8b21feeb1abd2b6534206c929fdf82184f3c0d1aff2942610538)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWrite", [grantee]))

    @jsii.member(jsii_name="logGroupPhysicalName")
    def log_group_physical_name(self) -> builtins.str:
        '''Public method to get the physical name of this log group.'''
        return typing.cast(builtins.str, jsii.invoke(self, "logGroupPhysicalName", []))

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
        '''Return the given named metric for this Log Group.

        :param metric_name: The name of the metric.
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
            type_hints = typing.get_type_hints(_typecheckingstub__e63ab70f8bacc728cdbf61171dfc0b89720bb794e34d29336b9486edb7738afb)
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
        '''The volume of log events in uncompressed bytes uploaded to CloudWatch Logs.

        When used with the LogGroupName dimension, this is the volume of log events
        in uncompressed bytes uploaded to the log group.

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

    @jsii.member(jsii_name="metricIncomingLogEvents")
    def metric_incoming_log_events(
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
        '''The number of log events uploaded to CloudWatch Logs.

        When used with the LogGroupName dimension, this is the number of
        log events uploaded to the log group.

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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricIncomingLogEvents", [props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILogGroup).__jsii_proxy_class__ = lambda : _ILogGroupProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_logs.ILogStream")
class ILogStream(_IResource_c80c4260, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        '''The name of this log stream.

        :attribute: true
        '''
        ...


class _ILogStreamProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_logs.ILogStream"

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        '''The name of this log stream.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILogStream).__jsii_proxy_class__ = lambda : _ILogStreamProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_logs.ILogSubscriptionDestination")
class ILogSubscriptionDestination(typing_extensions.Protocol):
    '''Interface for classes that can be the destination of a log Subscription.'''

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        source_log_group: ILogGroup,
    ) -> "LogSubscriptionDestinationConfig":
        '''Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        :param scope: -
        :param source_log_group: -
        '''
        ...


class _ILogSubscriptionDestinationProxy:
    '''Interface for classes that can be the destination of a log Subscription.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_logs.ILogSubscriptionDestination"

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        source_log_group: ILogGroup,
    ) -> "LogSubscriptionDestinationConfig":
        '''Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        :param scope: -
        :param source_log_group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d2d750464949100272f59f23f28dae31a40c84ad1d188b0cd44fdca6ca395d5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument source_log_group", value=source_log_group, expected_type=type_hints["source_log_group"])
        return typing.cast("LogSubscriptionDestinationConfig", jsii.invoke(self, "bind", [scope, source_log_group]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILogSubscriptionDestination).__jsii_proxy_class__ = lambda : _ILogSubscriptionDestinationProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_logs.IProcessor")
class IProcessor(typing_extensions.Protocol):
    '''Interface representing a single processor in a CloudWatch Logs transformer.

    A log transformer is a series of processors, where each processor applies one type of transformation
    to the log events. The processors work one after another, in the order that they are listed, like a pipeline.
    '''

    pass


class _IProcessorProxy:
    '''Interface representing a single processor in a CloudWatch Logs transformer.

    A log transformer is a series of processors, where each processor applies one type of transformation
    to the log events. The processors work one after another, in the order that they are listed, like a pipeline.
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_logs.IProcessor"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProcessor).__jsii_proxy_class__ = lambda : _IProcessorProxy


@jsii.implements(IProcessor)
class JsonMutatorProcessor(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.JsonMutatorProcessor",
):
    '''Processor for JSON mutation operations.

    :exampleMetadata: infused

    Example::

        # Create a log group
        log_group = logs.LogGroup(self, "MyLogGroup")
        
        # Create a JSON parser processor
        json_parser = logs.ParserProcessor(
            type=logs.ParserProcessorType.JSON
        )
        
        # Create a processor to add keys
        add_keys_processor = logs.JsonMutatorProcessor(
            type=logs.JsonMutatorType.ADD_KEYS,
            add_keys_options=logs.AddKeysProperty(
                entries=[logs.AddKeyEntryProperty(
                    key="metadata.transformed_in",
                    value="CloudWatchLogs"
                )]
            )
        )
        
        # Create a transformer with these processors
        logs.Transformer(self, "Transformer",
            transformer_name="MyTransformer",
            log_group=log_group,
            transformer_config=[json_parser, add_keys_processor]
        )
    '''

    def __init__(
        self,
        *,
        type: "JsonMutatorType",
        add_keys_options: typing.Optional[typing.Union[AddKeysProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        copy_value_options: typing.Optional[typing.Union[CopyValueProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        delete_keys_options: typing.Optional[typing.Union["ProcessorDeleteKeysProperty", typing.Dict[builtins.str, typing.Any]]] = None,
        list_to_map_options: typing.Optional[typing.Union["ListToMapProperty", typing.Dict[builtins.str, typing.Any]]] = None,
        move_keys_options: typing.Optional[typing.Union["MoveKeysProperty", typing.Dict[builtins.str, typing.Any]]] = None,
        rename_keys_options: typing.Optional[typing.Union["RenameKeysProperty", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Creates a new JSON mutator processor.

        :param type: The type of JSON mutation operation.
        :param add_keys_options: Options for adding keys. Required when type is ADD_KEYS. Default: - No adding keys processor is created if props not set
        :param copy_value_options: Options for copying values. Required when type is COPY_VALUE. Default: - No copy value processor is created if props not set
        :param delete_keys_options: Keys to delete. Required when type is DELETE_KEYS. Default: - No delete key processor is created if props not set
        :param list_to_map_options: Options for converting lists to maps. Required when type is LIST_TO_MAP. Default: - No list-to-map processor is created if props not set
        :param move_keys_options: Options for moving keys. Required when type is MOVE_KEYS. Default: - No move key processor is created if props not set
        :param rename_keys_options: Options for renaming keys. Required when type is RENAME_KEYS. Default: - No rename key processor is created if props not set
        '''
        props = JsonMutatorProps(
            type=type,
            add_keys_options=add_keys_options,
            copy_value_options=copy_value_options,
            delete_keys_options=delete_keys_options,
            list_to_map_options=list_to_map_options,
            move_keys_options=move_keys_options,
            rename_keys_options=rename_keys_options,
        )

        jsii.create(self.__class__, self, [props])

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "JsonMutatorType":
        '''The type of JSON mutation operation.'''
        return typing.cast("JsonMutatorType", jsii.get(self, "type"))

    @type.setter
    def type(self, value: "JsonMutatorType") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b6fd8557ef63d3b8ca1f2a3259dda6c618aa23213e0cb491a14321743e64f65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.JsonMutatorProps",
    jsii_struct_bases=[BaseProcessorProps],
    name_mapping={
        "type": "type",
        "add_keys_options": "addKeysOptions",
        "copy_value_options": "copyValueOptions",
        "delete_keys_options": "deleteKeysOptions",
        "list_to_map_options": "listToMapOptions",
        "move_keys_options": "moveKeysOptions",
        "rename_keys_options": "renameKeysOptions",
    },
)
class JsonMutatorProps(BaseProcessorProps):
    def __init__(
        self,
        *,
        type: "JsonMutatorType",
        add_keys_options: typing.Optional[typing.Union[AddKeysProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        copy_value_options: typing.Optional[typing.Union[CopyValueProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        delete_keys_options: typing.Optional[typing.Union["ProcessorDeleteKeysProperty", typing.Dict[builtins.str, typing.Any]]] = None,
        list_to_map_options: typing.Optional[typing.Union["ListToMapProperty", typing.Dict[builtins.str, typing.Any]]] = None,
        move_keys_options: typing.Optional[typing.Union["MoveKeysProperty", typing.Dict[builtins.str, typing.Any]]] = None,
        rename_keys_options: typing.Optional[typing.Union["RenameKeysProperty", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Properties for creating JSON mutator processors.

        :param type: The type of JSON mutation operation.
        :param add_keys_options: Options for adding keys. Required when type is ADD_KEYS. Default: - No adding keys processor is created if props not set
        :param copy_value_options: Options for copying values. Required when type is COPY_VALUE. Default: - No copy value processor is created if props not set
        :param delete_keys_options: Keys to delete. Required when type is DELETE_KEYS. Default: - No delete key processor is created if props not set
        :param list_to_map_options: Options for converting lists to maps. Required when type is LIST_TO_MAP. Default: - No list-to-map processor is created if props not set
        :param move_keys_options: Options for moving keys. Required when type is MOVE_KEYS. Default: - No move key processor is created if props not set
        :param rename_keys_options: Options for renaming keys. Required when type is RENAME_KEYS. Default: - No rename key processor is created if props not set

        :exampleMetadata: infused

        Example::

            # Create a log group
            log_group = logs.LogGroup(self, "MyLogGroup")
            
            # Create a JSON parser processor
            json_parser = logs.ParserProcessor(
                type=logs.ParserProcessorType.JSON
            )
            
            # Create a processor to add keys
            add_keys_processor = logs.JsonMutatorProcessor(
                type=logs.JsonMutatorType.ADD_KEYS,
                add_keys_options=logs.AddKeysProperty(
                    entries=[logs.AddKeyEntryProperty(
                        key="metadata.transformed_in",
                        value="CloudWatchLogs"
                    )]
                )
            )
            
            # Create a transformer with these processors
            logs.Transformer(self, "Transformer",
                transformer_name="MyTransformer",
                log_group=log_group,
                transformer_config=[json_parser, add_keys_processor]
            )
        '''
        if isinstance(add_keys_options, dict):
            add_keys_options = AddKeysProperty(**add_keys_options)
        if isinstance(copy_value_options, dict):
            copy_value_options = CopyValueProperty(**copy_value_options)
        if isinstance(delete_keys_options, dict):
            delete_keys_options = ProcessorDeleteKeysProperty(**delete_keys_options)
        if isinstance(list_to_map_options, dict):
            list_to_map_options = ListToMapProperty(**list_to_map_options)
        if isinstance(move_keys_options, dict):
            move_keys_options = MoveKeysProperty(**move_keys_options)
        if isinstance(rename_keys_options, dict):
            rename_keys_options = RenameKeysProperty(**rename_keys_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__388e83b4e8d42783305526c15dea5cd4e43051ab109847e7efb099d2b96f365f)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument add_keys_options", value=add_keys_options, expected_type=type_hints["add_keys_options"])
            check_type(argname="argument copy_value_options", value=copy_value_options, expected_type=type_hints["copy_value_options"])
            check_type(argname="argument delete_keys_options", value=delete_keys_options, expected_type=type_hints["delete_keys_options"])
            check_type(argname="argument list_to_map_options", value=list_to_map_options, expected_type=type_hints["list_to_map_options"])
            check_type(argname="argument move_keys_options", value=move_keys_options, expected_type=type_hints["move_keys_options"])
            check_type(argname="argument rename_keys_options", value=rename_keys_options, expected_type=type_hints["rename_keys_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if add_keys_options is not None:
            self._values["add_keys_options"] = add_keys_options
        if copy_value_options is not None:
            self._values["copy_value_options"] = copy_value_options
        if delete_keys_options is not None:
            self._values["delete_keys_options"] = delete_keys_options
        if list_to_map_options is not None:
            self._values["list_to_map_options"] = list_to_map_options
        if move_keys_options is not None:
            self._values["move_keys_options"] = move_keys_options
        if rename_keys_options is not None:
            self._values["rename_keys_options"] = rename_keys_options

    @builtins.property
    def type(self) -> "JsonMutatorType":
        '''The type of JSON mutation operation.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("JsonMutatorType", result)

    @builtins.property
    def add_keys_options(self) -> typing.Optional[AddKeysProperty]:
        '''Options for adding keys.

        Required when type is ADD_KEYS.

        :default: - No adding keys processor is created if props not set
        '''
        result = self._values.get("add_keys_options")
        return typing.cast(typing.Optional[AddKeysProperty], result)

    @builtins.property
    def copy_value_options(self) -> typing.Optional[CopyValueProperty]:
        '''Options for copying values.

        Required when type is COPY_VALUE.

        :default: - No copy value processor is created if props not set
        '''
        result = self._values.get("copy_value_options")
        return typing.cast(typing.Optional[CopyValueProperty], result)

    @builtins.property
    def delete_keys_options(self) -> typing.Optional["ProcessorDeleteKeysProperty"]:
        '''Keys to delete.

        Required when type is DELETE_KEYS.

        :default: - No delete key processor is created if props not set
        '''
        result = self._values.get("delete_keys_options")
        return typing.cast(typing.Optional["ProcessorDeleteKeysProperty"], result)

    @builtins.property
    def list_to_map_options(self) -> typing.Optional["ListToMapProperty"]:
        '''Options for converting lists to maps.

        Required when type is LIST_TO_MAP.

        :default: - No list-to-map processor is created if props not set
        '''
        result = self._values.get("list_to_map_options")
        return typing.cast(typing.Optional["ListToMapProperty"], result)

    @builtins.property
    def move_keys_options(self) -> typing.Optional["MoveKeysProperty"]:
        '''Options for moving keys.

        Required when type is MOVE_KEYS.

        :default: - No move key processor is created if props not set
        '''
        result = self._values.get("move_keys_options")
        return typing.cast(typing.Optional["MoveKeysProperty"], result)

    @builtins.property
    def rename_keys_options(self) -> typing.Optional["RenameKeysProperty"]:
        '''Options for renaming keys.

        Required when type is RENAME_KEYS.

        :default: - No rename key processor is created if props not set
        '''
        result = self._values.get("rename_keys_options")
        return typing.cast(typing.Optional["RenameKeysProperty"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JsonMutatorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.JsonMutatorType")
class JsonMutatorType(enum.Enum):
    '''Types of JSON mutation operations.

    Defines operations that can be performed to modify the JSON structure of log events.

    :exampleMetadata: infused

    Example::

        # Create a log group
        log_group = logs.LogGroup(self, "MyLogGroup")
        
        # Create a JSON parser processor
        json_parser = logs.ParserProcessor(
            type=logs.ParserProcessorType.JSON
        )
        
        # Create a processor to add keys
        add_keys_processor = logs.JsonMutatorProcessor(
            type=logs.JsonMutatorType.ADD_KEYS,
            add_keys_options=logs.AddKeysProperty(
                entries=[logs.AddKeyEntryProperty(
                    key="metadata.transformed_in",
                    value="CloudWatchLogs"
                )]
            )
        )
        
        # Create a transformer with these processors
        logs.Transformer(self, "Transformer",
            transformer_name="MyTransformer",
            log_group=log_group,
            transformer_config=[json_parser, add_keys_processor]
        )
    '''

    ADD_KEYS = "ADD_KEYS"
    '''Add new keys to the log event.'''
    DELETE_KEYS = "DELETE_KEYS"
    '''Delete keys from the log event.'''
    MOVE_KEYS = "MOVE_KEYS"
    '''Move keys to different locations.'''
    RENAME_KEYS = "RENAME_KEYS"
    '''Rename keys in the log event.'''
    COPY_VALUE = "COPY_VALUE"
    '''Copy values between keys.'''
    LIST_TO_MAP = "LIST_TO_MAP"
    '''Convert a list to a map.'''


@jsii.implements(IFilterPattern)
class JsonPattern(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_logs.JsonPattern",
):
    '''Base class for patterns that only match JSON log events.

    :exampleMetadata: lit=aws-logs/test/integ.metricfilter.lit.ts infused

    Example::

        MetricFilter(self, "MetricFilter",
            log_group=log_group,
            metric_namespace="MyApp",
            metric_name="Latency",
            filter_pattern=FilterPattern.all(
                FilterPattern.exists("$.latency"),
                FilterPattern.regex_value("$.message", "=", "bind: address already in use")),
            metric_value="$.latency"
        )
    '''

    def __init__(self, json_pattern_string: builtins.str) -> None:
        '''
        :param json_pattern_string: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63b70184328854d0009cc9ba82f6a6720fd48ccf9458964b5cc75f6cfb653549)
            check_type(argname="argument json_pattern_string", value=json_pattern_string, expected_type=type_hints["json_pattern_string"])
        jsii.create(self.__class__, self, [json_pattern_string])

    @builtins.property
    @jsii.member(jsii_name="jsonPatternString")
    def json_pattern_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jsonPatternString"))

    @builtins.property
    @jsii.member(jsii_name="logPatternString")
    def log_pattern_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logPatternString"))


class _JsonPatternProxy(JsonPattern):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, JsonPattern).__jsii_proxy_class__ = lambda : _JsonPatternProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.KeyValueDelimiter")
class KeyValueDelimiter(enum.Enum):
    '''Valid key-value delimiters for ParseKeyValue processor.

    Defines the delimiter string to use between the key and value in each pair.
    '''

    EQUAL = "EQUAL"
    '''Equal sign (default).'''
    COLON = "COLON"
    '''Colon character.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.KeyValuePairDelimiter")
class KeyValuePairDelimiter(enum.Enum):
    '''Valid field delimiters for ParseKeyValue processor.

    Defines the delimiter string used between key-value pairs in the original log events.
    '''

    AMPERSAND = "AMPERSAND"
    '''Ampersand character (default).'''
    SEMICOLON = "SEMICOLON"
    '''Semicolon character.'''
    SPACE = "SPACE"
    '''Space character.'''
    NEWLINE = "NEWLINE"
    '''Newline character.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.ListToMapProperty",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "source": "source",
        "flatten": "flatten",
        "flattened_element": "flattenedElement",
        "target": "target",
        "value_key": "valueKey",
    },
)
class ListToMapProperty:
    def __init__(
        self,
        *,
        key: builtins.str,
        source: builtins.str,
        flatten: typing.Optional[builtins.bool] = None,
        flattened_element: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        value_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''This processor takes a list of objects that contain key fields, and converts them into a map of target keys.

        For more information about this processor including examples, see listToMap in the CloudWatch Logs User Guide.

        :param key: The key of the field to be extracted as keys in the generated map.
        :param source: The key in the log event that has a list of objects that will be converted to a map.
        :param flatten: A Boolean value to indicate whether the list will be flattened into single items. Default: false
        :param flattened_element: If you set flatten to true, use flattenedElement to specify which element, first or last, to keep. You must specify this parameter if flatten is true. Default: - Must be specified if flatten is true and if flatten is false, has no effect
        :param target: The key of the field that will hold the generated map. Default: - Stored at the root of the log event
        :param value_key: If this is specified, the values that you specify in this parameter will be extracted from the source objects and put into the values of the generated map. Default: - Original objects in the source list will be put into the values of the generated map

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            list_to_map_property = logs.ListToMapProperty(
                key="key",
                source="source",
            
                # the properties below are optional
                flatten=False,
                flattened_element="flattenedElement",
                target="target",
                value_key="valueKey"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1db693d7e35418cf07e62ac333914baf11457ace8ba9e2fb52d10d55e134533)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument flatten", value=flatten, expected_type=type_hints["flatten"])
            check_type(argname="argument flattened_element", value=flattened_element, expected_type=type_hints["flattened_element"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument value_key", value=value_key, expected_type=type_hints["value_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "source": source,
        }
        if flatten is not None:
            self._values["flatten"] = flatten
        if flattened_element is not None:
            self._values["flattened_element"] = flattened_element
        if target is not None:
            self._values["target"] = target
        if value_key is not None:
            self._values["value_key"] = value_key

    @builtins.property
    def key(self) -> builtins.str:
        '''The key of the field to be extracted as keys in the generated map.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''The key in the log event that has a list of objects that will be converted to a map.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def flatten(self) -> typing.Optional[builtins.bool]:
        '''A Boolean value to indicate whether the list will be flattened into single items.

        :default: false
        '''
        result = self._values.get("flatten")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def flattened_element(self) -> typing.Optional[builtins.str]:
        '''If you set flatten to true, use flattenedElement to specify which element, first or last, to keep.

        You must specify this parameter if flatten is true.

        :default: - Must be specified if flatten is true and if flatten is false, has no effect
        '''
        result = self._values.get("flattened_element")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''The key of the field that will hold the generated map.

        :default: - Stored at the root of the log event
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value_key(self) -> typing.Optional[builtins.str]:
        '''If this is specified, the values that you specify in this parameter will be extracted from the source objects and put into the values of the generated map.

        :default: - Original objects in the source list will be put into the values of the generated map
        '''
        result = self._values.get("value_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListToMapProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ILogGroup)
class LogGroup(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.LogGroup",
):
    '''Define a CloudWatch Log Group.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_logs as logs
        
        
        log_group = logs.LogGroup(self, "Log Group")
        log_bucket = s3.Bucket(self, "S3 Bucket")
        
        tasks.EmrContainersStartJobRun(self, "EMR Containers Start Job Run",
            virtual_cluster=tasks.VirtualClusterInput.from_virtual_cluster_id("de92jdei2910fwedz"),
            release_label=tasks.ReleaseLabel.EMR_6_2_0,
            job_driver=tasks.JobDriver(
                spark_submit_job_driver=tasks.SparkSubmitJobDriver(
                    entry_point=sfn.TaskInput.from_text("local:///usr/lib/spark/examples/src/main/python/pi.py"),
                    spark_submit_parameters="--conf spark.executor.instances=2 --conf spark.executor.memory=2G --conf spark.executor.cores=2 --conf spark.driver.cores=1"
                )
            ),
            monitoring=tasks.Monitoring(
                log_group=log_group,
                log_bucket=log_bucket
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        data_protection_policy: typing.Optional[DataProtectionPolicy] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        field_index_policies: typing.Optional[typing.Sequence[FieldIndexPolicy]] = None,
        log_group_class: typing.Optional["LogGroupClass"] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        retention: typing.Optional["RetentionDays"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param data_protection_policy: Data Protection Policy for this log group. Default: - no data protection policy
        :param encryption_key: The KMS customer managed key to encrypt the log group with. Default: Server-side encryption managed by the CloudWatch Logs service
        :param field_index_policies: Field Index Policies for this log group. Default: - no field index policies for this log group.
        :param log_group_class: The class of the log group. Possible values are: STANDARD and INFREQUENT_ACCESS. INFREQUENT_ACCESS class provides customers a cost-effective way to consolidate logs which supports querying using Logs Insights. The logGroupClass property cannot be changed once the log group is created. Default: LogGroupClass.STANDARD
        :param log_group_name: Name of the log group. Default: Automatically generated
        :param removal_policy: Determine the removal policy of this log group. Normally you want to retain the log group so you can diagnose issues from logs even after a deployment that no longer includes the log group. In that case, use the normal date-based retention policy to age out your logs. Default: RemovalPolicy.Retain
        :param retention: How long, in days, the log contents will be retained. To retain all logs, set this value to RetentionDays.INFINITE. Default: RetentionDays.TWO_YEARS
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__308a02ff022bfc4531ef0c547fbfb8db809293b3cda70c61106c9bc271126e70)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LogGroupProps(
            data_protection_policy=data_protection_policy,
            encryption_key=encryption_key,
            field_index_policies=field_index_policies,
            log_group_class=log_group_class,
            log_group_name=log_group_name,
            removal_policy=removal_policy,
            retention=retention,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromLogGroupArn")
    @builtins.classmethod
    def from_log_group_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        log_group_arn: builtins.str,
    ) -> ILogGroup:
        '''Import an existing LogGroup given its ARN.

        :param scope: -
        :param id: -
        :param log_group_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94bc59386fc670bf1438201199282e56f015468fe650487225ccaca3ae495cd7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
        return typing.cast(ILogGroup, jsii.sinvoke(cls, "fromLogGroupArn", [scope, id, log_group_arn]))

    @jsii.member(jsii_name="fromLogGroupName")
    @builtins.classmethod
    def from_log_group_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        log_group_name: builtins.str,
    ) -> ILogGroup:
        '''Import an existing LogGroup given its name.

        :param scope: -
        :param id: -
        :param log_group_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9988695c3237dc33d233c2bca8c1a32b8ca9135d661974af7b593667d7199d2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
        return typing.cast(ILogGroup, jsii.sinvoke(cls, "fromLogGroupName", [scope, id, log_group_name]))

    @jsii.member(jsii_name="addMetricFilter")
    def add_metric_filter(
        self,
        id: builtins.str,
        *,
        filter_pattern: IFilterPattern,
        metric_name: builtins.str,
        metric_namespace: builtins.str,
        default_value: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        filter_name: typing.Optional[builtins.str] = None,
        metric_value: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> "MetricFilter":
        '''Create a new Metric Filter on this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param filter_pattern: Pattern to search for log events.
        :param metric_name: The name of the metric to emit.
        :param metric_namespace: The namespace of the metric to emit.
        :param default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
        :param dimensions: The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions. Default: - No dimensions attached to metrics.
        :param filter_name: The name of the metric filter. Default: - Cloudformation generated name.
        :param metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"
        :param unit: The unit to assign to the metric. Default: - No unit attached to metrics.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60bdb647264d5f9edd37cf7e07a8b1cde70ce81f1ebb17eb131efa9d12a73e70)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = MetricFilterOptions(
            filter_pattern=filter_pattern,
            metric_name=metric_name,
            metric_namespace=metric_namespace,
            default_value=default_value,
            dimensions=dimensions,
            filter_name=filter_name,
            metric_value=metric_value,
            unit=unit,
        )

        return typing.cast("MetricFilter", jsii.invoke(self, "addMetricFilter", [id, props]))

    @jsii.member(jsii_name="addStream")
    def add_stream(
        self,
        id: builtins.str,
        *,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> "LogStream":
        '''Create a new Log Stream for this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a24d4a9b6baaaae57b481202eeb591bd2f9c75a23a136632347af1c7954e70d)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StreamOptions(log_stream_name=log_stream_name)

        return typing.cast("LogStream", jsii.invoke(self, "addStream", [id, props]))

    @jsii.member(jsii_name="addSubscriptionFilter")
    def add_subscription_filter(
        self,
        id: builtins.str,
        *,
        destination: ILogSubscriptionDestination,
        filter_pattern: IFilterPattern,
        distribution: typing.Optional[Distribution] = None,
        filter_name: typing.Optional[builtins.str] = None,
    ) -> "SubscriptionFilter":
        '''Create a new Subscription Filter on this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
        :param filter_pattern: Log events matching this pattern will be sent to the destination.
        :param distribution: The method used to distribute log data to the destination. This property can only be used with KinesisDestination. Default: Distribution.BY_LOG_STREAM
        :param filter_name: The name of the subscription filter. Default: Automatically generated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a53e1c08918ff12981b248135756d8f20c9acc571a2cab87ee6a3504361564b6)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SubscriptionFilterOptions(
            destination=destination,
            filter_pattern=filter_pattern,
            distribution=distribution,
            filter_name=filter_name,
        )

        return typing.cast("SubscriptionFilter", jsii.invoke(self, "addSubscriptionFilter", [id, props]))

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(
        self,
        statement: _PolicyStatement_0fe33853,
    ) -> _AddToResourcePolicyResult_1d0a53ad:
        '''Adds a statement to the resource policy associated with this log group.

        A resource policy will be automatically created upon the first call to ``addToResourcePolicy``.

        Any ARN Principals inside of the statement will be converted into AWS Account ID strings
        because CloudWatch Logs Resource Policies do not accept ARN principals.

        :param statement: The policy statement to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f61b70f15ff76b195297fc3fa75909dc7046483a164b76160596773157f547f)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(_AddToResourcePolicyResult_1d0a53ad, jsii.invoke(self, "addToResourcePolicy", [statement]))

    @jsii.member(jsii_name="addTransformer")
    def add_transformer(
        self,
        id: builtins.str,
        *,
        transformer_config: typing.Sequence[IProcessor],
        transformer_name: builtins.str,
    ) -> "Transformer":
        '''Create a new Transformer on this Log Group.

        :param id: Unique identifier for the construct in its parent.
        :param transformer_config: List of processors in a transformer.
        :param transformer_name: Name of the transformer.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a47fe63f1fc66b79ef415b28ffcfb0a1d225c29859afcdcffa2b69c56711466)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TransformerOptions(
            transformer_config=transformer_config, transformer_name=transformer_name
        )

        return typing.cast("Transformer", jsii.invoke(self, "addTransformer", [id, props]))

    @jsii.member(jsii_name="extractMetric")
    def extract_metric(
        self,
        json_field: builtins.str,
        metric_namespace: builtins.str,
        metric_name: builtins.str,
    ) -> _Metric_e396a4dc:
        '''Extract a metric from structured log events in the LogGroup.

        Creates a MetricFilter on this LogGroup that will extract the value
        of the indicated JSON field in all records where it occurs.

        The metric will be available in CloudWatch Metrics under the
        indicated namespace and name.

        :param json_field: JSON field to extract (example: '$.myfield').
        :param metric_namespace: Namespace to emit the metric under.
        :param metric_name: Name to emit the metric under.

        :return: A Metric object representing the extracted metric
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fec042a3492600efc8a11c082c58cb34995746a66ce985d97fd5c74ba47f0b96)
            check_type(argname="argument json_field", value=json_field, expected_type=type_hints["json_field"])
            check_type(argname="argument metric_namespace", value=metric_namespace, expected_type=type_hints["metric_namespace"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "extractMetric", [json_field, metric_namespace, metric_name]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Give the indicated permissions on this log group and all streams.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9a9cb0e1cec11a01408a7a448100c7b05edddf5bb005abd006a834d3c923bb7)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Give permissions to read and filter events from this log group.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__049a7f93ec71ef52ad5919516c695afd1e3f1185bfaadbf66b872fe23abae4db)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Give permissions to create and write to streams in this log group.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c97b414675dc468df60a1d999b2ddb74ddf42567d0d8ac3af19bb44f4022b1b0)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWrite", [grantee]))

    @jsii.member(jsii_name="logGroupPhysicalName")
    def log_group_physical_name(self) -> builtins.str:
        '''Public method to get the physical name of this log group.

        :return: Physical name of log group
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "logGroupPhysicalName", []))

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
        '''Creates a CloudWatch metric for this log group.

        :param metric_name: - The name of the metric to create.
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

        :return:

        A CloudWatch Metric object representing the specified metric for this log group.

        This method creates a CloudWatch Metric object with predefined settings for the log group.
        It sets the namespace to 'AWS/Logs' and the statistic to 'Sum' by default.

        The created metric is automatically associated with this log group using the ``attachTo`` method.

        Common metric names for log groups include:

        - 'IncomingBytes': The volume of log data in bytes ingested into the log group.
        - 'IncomingLogEvents': The number of log events ingested into the log group.

        Example::
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afd13314ef52ff283429f1992d9ab29ab14998262e884015dc1d0af12ff9df43)
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
        '''Creates a CloudWatch metric for the volume of incoming log data in bytes to this log group.

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

        :return:

        A CloudWatch Metric object representing the IncomingBytes metric.

        This method allows you to monitor the volume of data being ingested into the log group.
        It's useful for understanding the size of your logs, which can impact storage costs
        and help in identifying unexpectedly large log entries.

        Example usage::

        const logGroup = new logs.LogGroup(this, 'MyLogGroup');
        logGroup.metricIncomingBytes().createAlarm(stack, 'IncomingBytesPerInstanceAlarm', {
        threshold: 1,
        evaluationPeriods: 1,
        });
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

    @jsii.member(jsii_name="metricIncomingLogEvents")
    def metric_incoming_log_events(
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
        '''Creates a CloudWatch metric for the number of incoming log events to this log group.

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

        :return:

        A CloudWatch Metric object representing the IncomingLogEvents metric.

        This method allows you to monitor the rate at which log events are being ingested
        into the log group. It's useful for understanding the volume of logging activity
        and can help in capacity planning or detecting unusual spikes in logging.

        Example usage::

        const logGroup = new logs.LogGroup(this, 'MyLogGroup');
        logGroup.metricIncomingLogEvents().createAlarm(stack, 'IncomingEventsPerInstanceAlarm', {
        threshold: 1,
        evaluationPeriods: 1,
        });
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricIncomingLogEvents", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))

    @builtins.property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> builtins.str:
        '''The ARN of this log group.'''
        return typing.cast(builtins.str, jsii.get(self, "logGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        '''The name of this log group.'''
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.LogGroupClass")
class LogGroupClass(enum.Enum):
    '''Class of Log Group.'''

    STANDARD = "STANDARD"
    '''Default class of logs services.'''
    INFREQUENT_ACCESS = "INFREQUENT_ACCESS"
    '''Class for reduced logs services.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.LogGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_protection_policy": "dataProtectionPolicy",
        "encryption_key": "encryptionKey",
        "field_index_policies": "fieldIndexPolicies",
        "log_group_class": "logGroupClass",
        "log_group_name": "logGroupName",
        "removal_policy": "removalPolicy",
        "retention": "retention",
    },
)
class LogGroupProps:
    def __init__(
        self,
        *,
        data_protection_policy: typing.Optional[DataProtectionPolicy] = None,
        encryption_key: typing.Optional[_IKey_5f11635f] = None,
        field_index_policies: typing.Optional[typing.Sequence[FieldIndexPolicy]] = None,
        log_group_class: typing.Optional[LogGroupClass] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        retention: typing.Optional["RetentionDays"] = None,
    ) -> None:
        '''Properties for a LogGroup.

        :param data_protection_policy: Data Protection Policy for this log group. Default: - no data protection policy
        :param encryption_key: The KMS customer managed key to encrypt the log group with. Default: Server-side encryption managed by the CloudWatch Logs service
        :param field_index_policies: Field Index Policies for this log group. Default: - no field index policies for this log group.
        :param log_group_class: The class of the log group. Possible values are: STANDARD and INFREQUENT_ACCESS. INFREQUENT_ACCESS class provides customers a cost-effective way to consolidate logs which supports querying using Logs Insights. The logGroupClass property cannot be changed once the log group is created. Default: LogGroupClass.STANDARD
        :param log_group_name: Name of the log group. Default: Automatically generated
        :param removal_policy: Determine the removal policy of this log group. Normally you want to retain the log group so you can diagnose issues from logs even after a deployment that no longer includes the log group. In that case, use the normal date-based retention policy to age out your logs. Default: RemovalPolicy.Retain
        :param retention: How long, in days, the log contents will be retained. To retain all logs, set this value to RetentionDays.INFINITE. Default: RetentionDays.TWO_YEARS

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_kinesisfirehose as firehose
            
            
            log_group_destination = logs.LogGroup(self, "LogGroupLambdaAudit",
                log_group_name="auditDestinationForCDK"
            )
            
            bucket = s3.Bucket(self, "audit-bucket")
            s3_destination = firehose.S3Bucket(bucket)
            
            delivery_stream = firehose.DeliveryStream(self, "Delivery Stream",
                destination=s3_destination
            )
            
            data_protection_policy = logs.DataProtectionPolicy(
                name="data protection policy",
                description="policy description",
                identifiers=[logs.DataIdentifier.DRIVERSLICENSE_US,  # managed data identifier
                    logs.DataIdentifier("EmailAddress"),  # forward compatibility for new managed data identifiers
                    logs.CustomDataIdentifier("EmployeeId", "EmployeeId-\\d{9}")
                ],  # custom data identifier
                log_group_audit_destination=log_group_destination,
                s3_bucket_audit_destination=bucket,
                delivery_stream_name_audit_destination=delivery_stream.delivery_stream_name
            )
            
            logs.LogGroup(self, "LogGroupLambda",
                log_group_name="cdkIntegLogGroup",
                data_protection_policy=data_protection_policy
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df51a93f7809d59dd37d78a60967e0071dab4876ea1cd5ecd658ac3c8eae1320)
            check_type(argname="argument data_protection_policy", value=data_protection_policy, expected_type=type_hints["data_protection_policy"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument field_index_policies", value=field_index_policies, expected_type=type_hints["field_index_policies"])
            check_type(argname="argument log_group_class", value=log_group_class, expected_type=type_hints["log_group_class"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument retention", value=retention, expected_type=type_hints["retention"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if data_protection_policy is not None:
            self._values["data_protection_policy"] = data_protection_policy
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if field_index_policies is not None:
            self._values["field_index_policies"] = field_index_policies
        if log_group_class is not None:
            self._values["log_group_class"] = log_group_class
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if retention is not None:
            self._values["retention"] = retention

    @builtins.property
    def data_protection_policy(self) -> typing.Optional[DataProtectionPolicy]:
        '''Data Protection Policy for this log group.

        :default: - no data protection policy
        '''
        result = self._values.get("data_protection_policy")
        return typing.cast(typing.Optional[DataProtectionPolicy], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The KMS customer managed key to encrypt the log group with.

        :default: Server-side encryption managed by the CloudWatch Logs service
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def field_index_policies(self) -> typing.Optional[typing.List[FieldIndexPolicy]]:
        '''Field Index Policies for this log group.

        :default: - no field index policies for this log group.
        '''
        result = self._values.get("field_index_policies")
        return typing.cast(typing.Optional[typing.List[FieldIndexPolicy]], result)

    @builtins.property
    def log_group_class(self) -> typing.Optional[LogGroupClass]:
        '''The class of the log group. Possible values are: STANDARD and INFREQUENT_ACCESS.

        INFREQUENT_ACCESS class provides customers a cost-effective way to consolidate
        logs which supports querying using Logs Insights. The logGroupClass property cannot
        be changed once the log group is created.

        :default: LogGroupClass.STANDARD
        '''
        result = self._values.get("log_group_class")
        return typing.cast(typing.Optional[LogGroupClass], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''Name of the log group.

        :default: Automatically generated
        '''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''Determine the removal policy of this log group.

        Normally you want to retain the log group so you can diagnose issues
        from logs even after a deployment that no longer includes the log group.
        In that case, use the normal date-based retention policy to age out your
        logs.

        :default: RemovalPolicy.Retain
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def retention(self) -> typing.Optional["RetentionDays"]:
        '''How long, in days, the log contents will be retained.

        To retain all logs, set this value to RetentionDays.INFINITE.

        :default: RetentionDays.TWO_YEARS
        '''
        result = self._values.get("retention")
        return typing.cast(typing.Optional["RetentionDays"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogRetention(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.LogRetention",
):
    '''Creates a custom resource to control the retention policy of a CloudWatch Logs log group.

    The log group is created if it doesn't already exist. The policy
    is removed when ``retentionDays`` is ``undefined`` or equal to ``Infinity``.
    Log group can be created in the region that is different from stack region by
    specifying ``logGroupRegion``

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_iam as iam
        from aws_cdk import aws_logs as logs
        
        # role: iam.Role
        
        log_retention = logs.LogRetention(self, "MyLogRetention",
            log_group_name="logGroupName",
            retention=logs.RetentionDays.ONE_DAY,
        
            # the properties below are optional
            log_group_region="logGroupRegion",
            log_retention_retry_options=logs.LogRetentionRetryOptions(
                base=cdk.Duration.minutes(30),
                max_retries=123
            ),
            removal_policy=cdk.RemovalPolicy.DESTROY,
            role=role
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        log_group_name: builtins.str,
        retention: "RetentionDays",
        log_group_region: typing.Optional[builtins.str] = None,
        log_retention_retry_options: typing.Optional[typing.Union["LogRetentionRetryOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param log_group_name: The log group name.
        :param retention: The number of days log events are kept in CloudWatch Logs.
        :param log_group_region: The region where the log group should be created. Default: - same region as the stack
        :param log_retention_retry_options: Retry options for all AWS API calls. Default: - AWS SDK default retry options
        :param removal_policy: The removalPolicy for the log group when the stack is deleted. Default: RemovalPolicy.RETAIN
        :param role: The IAM role for the Lambda function associated with the custom resource. Default: - A new role is created
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4507613a235a88592d0ebd7d0dbe61f494620068c75fef42db8c09f2dfde8cc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LogRetentionProps(
            log_group_name=log_group_name,
            retention=retention,
            log_group_region=log_group_region,
            log_retention_retry_options=log_retention_retry_options,
            removal_policy=removal_policy,
            role=role,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))

    @builtins.property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> builtins.str:
        '''The ARN of the LogGroup.'''
        return typing.cast(builtins.str, jsii.get(self, "logGroupArn"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.LogRetentionProps",
    jsii_struct_bases=[],
    name_mapping={
        "log_group_name": "logGroupName",
        "retention": "retention",
        "log_group_region": "logGroupRegion",
        "log_retention_retry_options": "logRetentionRetryOptions",
        "removal_policy": "removalPolicy",
        "role": "role",
    },
)
class LogRetentionProps:
    def __init__(
        self,
        *,
        log_group_name: builtins.str,
        retention: "RetentionDays",
        log_group_region: typing.Optional[builtins.str] = None,
        log_retention_retry_options: typing.Optional[typing.Union["LogRetentionRetryOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Construction properties for a LogRetention.

        :param log_group_name: The log group name.
        :param retention: The number of days log events are kept in CloudWatch Logs.
        :param log_group_region: The region where the log group should be created. Default: - same region as the stack
        :param log_retention_retry_options: Retry options for all AWS API calls. Default: - AWS SDK default retry options
        :param removal_policy: The removalPolicy for the log group when the stack is deleted. Default: RemovalPolicy.RETAIN
        :param role: The IAM role for the Lambda function associated with the custom resource. Default: - A new role is created

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_logs as logs
            
            # role: iam.Role
            
            log_retention_props = logs.LogRetentionProps(
                log_group_name="logGroupName",
                retention=logs.RetentionDays.ONE_DAY,
            
                # the properties below are optional
                log_group_region="logGroupRegion",
                log_retention_retry_options=logs.LogRetentionRetryOptions(
                    base=cdk.Duration.minutes(30),
                    max_retries=123
                ),
                removal_policy=cdk.RemovalPolicy.DESTROY,
                role=role
            )
        '''
        if isinstance(log_retention_retry_options, dict):
            log_retention_retry_options = LogRetentionRetryOptions(**log_retention_retry_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__318a9234eb28bfd26692eac8fd1ea9c47cedbd175a0dc53714860906302a980b)
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument retention", value=retention, expected_type=type_hints["retention"])
            check_type(argname="argument log_group_region", value=log_group_region, expected_type=type_hints["log_group_region"])
            check_type(argname="argument log_retention_retry_options", value=log_retention_retry_options, expected_type=type_hints["log_retention_retry_options"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_group_name": log_group_name,
            "retention": retention,
        }
        if log_group_region is not None:
            self._values["log_group_region"] = log_group_region
        if log_retention_retry_options is not None:
            self._values["log_retention_retry_options"] = log_retention_retry_options
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''The log group name.'''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention(self) -> "RetentionDays":
        '''The number of days log events are kept in CloudWatch Logs.'''
        result = self._values.get("retention")
        assert result is not None, "Required property 'retention' is missing"
        return typing.cast("RetentionDays", result)

    @builtins.property
    def log_group_region(self) -> typing.Optional[builtins.str]:
        '''The region where the log group should be created.

        :default: - same region as the stack
        '''
        result = self._values.get("log_group_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_retention_retry_options(
        self,
    ) -> typing.Optional["LogRetentionRetryOptions"]:
        '''Retry options for all AWS API calls.

        :default: - AWS SDK default retry options
        '''
        result = self._values.get("log_retention_retry_options")
        return typing.cast(typing.Optional["LogRetentionRetryOptions"], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''The removalPolicy for the log group when the stack is deleted.

        :default: RemovalPolicy.RETAIN
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role for the Lambda function associated with the custom resource.

        :default: - A new role is created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogRetentionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.LogRetentionRetryOptions",
    jsii_struct_bases=[],
    name_mapping={"base": "base", "max_retries": "maxRetries"},
)
class LogRetentionRetryOptions:
    def __init__(
        self,
        *,
        base: typing.Optional[_Duration_4839e8c3] = None,
        max_retries: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Retry options for all AWS API calls.

        :param base: (deprecated) The base duration to use in the exponential backoff for operation retries. Default: - none, not used anymore
        :param max_retries: The maximum amount of retries. Default: 5

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_logs as logs
            
            log_retention_retry_options = logs.LogRetentionRetryOptions(
                base=cdk.Duration.minutes(30),
                max_retries=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9636a1cfdc99034fff1c4ef9550b1c380d0f51a19f14b506c85c32184b950d42)
            check_type(argname="argument base", value=base, expected_type=type_hints["base"])
            check_type(argname="argument max_retries", value=max_retries, expected_type=type_hints["max_retries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if base is not None:
            self._values["base"] = base
        if max_retries is not None:
            self._values["max_retries"] = max_retries

    @builtins.property
    def base(self) -> typing.Optional[_Duration_4839e8c3]:
        '''(deprecated) The base duration to use in the exponential backoff for operation retries.

        :default: - none, not used anymore

        :deprecated: Unused since the upgrade to AWS SDK v3, which uses a different retry strategy

        :stability: deprecated
        '''
        result = self._values.get("base")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def max_retries(self) -> typing.Optional[jsii.Number]:
        '''The maximum amount of retries.

        :default: 5
        '''
        result = self._values.get("max_retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogRetentionRetryOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ILogStream)
class LogStream(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.LogStream",
):
    '''Define a Log Stream in a Log Group.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_logs as logs
        
        # log_group: logs.LogGroup
        
        log_stream = logs.LogStream(self, "MyLogStream",
            log_group=log_group,
        
            # the properties below are optional
            log_stream_name="logStreamName",
            removal_policy=cdk.RemovalPolicy.DESTROY
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        log_group: ILogGroup,
        log_stream_name: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param log_group: The log group to create a log stream for.
        :param log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated
        :param removal_policy: Determine what happens when the log stream resource is removed from the app. Normally you want to retain the log stream so you can diagnose issues from logs even after a deployment that no longer includes the log stream. The date-based retention policy of your log group will age out the logs after a certain time. Default: RemovalPolicy.Retain
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7b310f4ff2940ed4dffa21e4ffde6e0f0bb15bdf93db6bd6d34466158da5c47)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LogStreamProps(
            log_group=log_group,
            log_stream_name=log_stream_name,
            removal_policy=removal_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromLogStreamName")
    @builtins.classmethod
    def from_log_stream_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        log_stream_name: builtins.str,
    ) -> ILogStream:
        '''Import an existing LogGroup.

        :param scope: -
        :param id: -
        :param log_stream_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c90257c192f43807c3ca64b0dfd7f0d8f24a0e76af49b59d49ef0b271d7e85a0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        return typing.cast(ILogStream, jsii.sinvoke(cls, "fromLogStreamName", [scope, id, log_stream_name]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))

    @builtins.property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> builtins.str:
        '''The name of this log stream.'''
        return typing.cast(builtins.str, jsii.get(self, "logStreamName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.LogStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "log_group": "logGroup",
        "log_stream_name": "logStreamName",
        "removal_policy": "removalPolicy",
    },
)
class LogStreamProps:
    def __init__(
        self,
        *,
        log_group: ILogGroup,
        log_stream_name: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    ) -> None:
        '''Properties for a LogStream.

        :param log_group: The log group to create a log stream for.
        :param log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated
        :param removal_policy: Determine what happens when the log stream resource is removed from the app. Normally you want to retain the log stream so you can diagnose issues from logs even after a deployment that no longer includes the log stream. The date-based retention policy of your log group will age out the logs after a certain time. Default: RemovalPolicy.Retain

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_logs as logs
            
            # log_group: logs.LogGroup
            
            log_stream_props = logs.LogStreamProps(
                log_group=log_group,
            
                # the properties below are optional
                log_stream_name="logStreamName",
                removal_policy=cdk.RemovalPolicy.DESTROY
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f49a14f2b0eea132d7cea27db911c1bac5a2370d8c93686afb12d7bf18544ca)
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_group": log_group,
        }
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def log_group(self) -> ILogGroup:
        '''The log group to create a log stream for.'''
        result = self._values.get("log_group")
        assert result is not None, "Required property 'log_group' is missing"
        return typing.cast(ILogGroup, result)

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''The name of the log stream to create.

        The name must be unique within the log group.

        :default: Automatically generated
        '''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''Determine what happens when the log stream resource is removed from the app.

        Normally you want to retain the log stream so you can diagnose issues from
        logs even after a deployment that no longer includes the log stream.

        The date-based retention policy of your log group will age out the logs
        after a certain time.

        :default: RemovalPolicy.Retain
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.LogSubscriptionDestinationConfig",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "role": "role"},
)
class LogSubscriptionDestinationConfig:
    def __init__(
        self,
        *,
        arn: builtins.str,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Properties returned by a Subscription destination.

        :param arn: The ARN of the subscription's destination.
        :param role: The role to assume to write log events to the destination. Default: No role assumed

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_logs as logs
            
            # role: iam.Role
            
            log_subscription_destination_config = logs.LogSubscriptionDestinationConfig(
                arn="arn",
            
                # the properties below are optional
                role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__396d59c2514d8bfe65a7a6f818257b42d5f5c9b200fa30ed27db93bc6e8328e0)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "arn": arn,
        }
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def arn(self) -> builtins.str:
        '''The ARN of the subscription's destination.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The role to assume to write log events to the destination.

        :default: No role assumed
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogSubscriptionDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MetricFilter(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.MetricFilter",
):
    '''A filter that extracts information from CloudWatch Logs and emits to CloudWatch Metrics.

    :exampleMetadata: lit=aws-logs/test/integ.metricfilter.lit.ts infused

    Example::

        MetricFilter(self, "MetricFilter",
            log_group=log_group,
            metric_namespace="MyApp",
            metric_name="Latency",
            filter_pattern=FilterPattern.all(
                FilterPattern.exists("$.latency"),
                FilterPattern.regex_value("$.message", "=", "bind: address already in use")),
            metric_value="$.latency"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        log_group: ILogGroup,
        filter_pattern: IFilterPattern,
        metric_name: builtins.str,
        metric_namespace: builtins.str,
        default_value: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        filter_name: typing.Optional[builtins.str] = None,
        metric_value: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param log_group: The log group to create the filter on.
        :param filter_pattern: Pattern to search for log events.
        :param metric_name: The name of the metric to emit.
        :param metric_namespace: The namespace of the metric to emit.
        :param default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
        :param dimensions: The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions. Default: - No dimensions attached to metrics.
        :param filter_name: The name of the metric filter. Default: - Cloudformation generated name.
        :param metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"
        :param unit: The unit to assign to the metric. Default: - No unit attached to metrics.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d62ba20acf6180e35fd081efe9f21747bf2bd8765dd3a4a5c41cc0f41f079a1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = MetricFilterProps(
            log_group=log_group,
            filter_pattern=filter_pattern,
            metric_name=metric_name,
            metric_namespace=metric_namespace,
            default_value=default_value,
            dimensions=dimensions,
            filter_name=filter_name,
            metric_value=metric_value,
            unit=unit,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="metric")
    def metric(
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
        '''Return the given named metric for this Metric Filter.

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

        :default: avg over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metric", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.MetricFilterOptions",
    jsii_struct_bases=[],
    name_mapping={
        "filter_pattern": "filterPattern",
        "metric_name": "metricName",
        "metric_namespace": "metricNamespace",
        "default_value": "defaultValue",
        "dimensions": "dimensions",
        "filter_name": "filterName",
        "metric_value": "metricValue",
        "unit": "unit",
    },
)
class MetricFilterOptions:
    def __init__(
        self,
        *,
        filter_pattern: IFilterPattern,
        metric_name: builtins.str,
        metric_namespace: builtins.str,
        default_value: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        filter_name: typing.Optional[builtins.str] = None,
        metric_value: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> None:
        '''Properties for a MetricFilter created from a LogGroup.

        :param filter_pattern: Pattern to search for log events.
        :param metric_name: The name of the metric to emit.
        :param metric_namespace: The namespace of the metric to emit.
        :param default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
        :param dimensions: The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions. Default: - No dimensions attached to metrics.
        :param filter_name: The name of the metric filter. Default: - Cloudformation generated name.
        :param metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"
        :param unit: The unit to assign to the metric. Default: - No unit attached to metrics.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cloudwatch as cloudwatch
            from aws_cdk import aws_logs as logs
            
            # filter_pattern: logs.IFilterPattern
            
            metric_filter_options = logs.MetricFilterOptions(
                filter_pattern=filter_pattern,
                metric_name="metricName",
                metric_namespace="metricNamespace",
            
                # the properties below are optional
                default_value=123,
                dimensions={
                    "dimensions_key": "dimensions"
                },
                filter_name="filterName",
                metric_value="metricValue",
                unit=cloudwatch.Unit.SECONDS
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5bb9c8220568f1b3f6adf2d20dcfde3ada18ce4351110a49b3a0707812e51fe)
            check_type(argname="argument filter_pattern", value=filter_pattern, expected_type=type_hints["filter_pattern"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument metric_namespace", value=metric_namespace, expected_type=type_hints["metric_namespace"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument filter_name", value=filter_name, expected_type=type_hints["filter_name"])
            check_type(argname="argument metric_value", value=metric_value, expected_type=type_hints["metric_value"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filter_pattern": filter_pattern,
            "metric_name": metric_name,
            "metric_namespace": metric_namespace,
        }
        if default_value is not None:
            self._values["default_value"] = default_value
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if filter_name is not None:
            self._values["filter_name"] = filter_name
        if metric_value is not None:
            self._values["metric_value"] = metric_value
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def filter_pattern(self) -> IFilterPattern:
        '''Pattern to search for log events.'''
        result = self._values.get("filter_pattern")
        assert result is not None, "Required property 'filter_pattern' is missing"
        return typing.cast(IFilterPattern, result)

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''The name of the metric to emit.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_namespace(self) -> builtins.str:
        '''The namespace of the metric to emit.'''
        result = self._values.get("metric_namespace")
        assert result is not None, "Required property 'metric_namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> typing.Optional[jsii.Number]:
        '''The value to emit if the pattern does not match a particular event.

        :default: No metric emitted.
        '''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The fields to use as dimensions for the metric.

        One metric filter can include as many as three dimensions.

        :default: - No dimensions attached to metrics.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-dimensions
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric filter.

        :default: - Cloudformation generated name.
        '''
        result = self._values.get("filter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_value(self) -> typing.Optional[builtins.str]:
        '''The value to emit for the metric.

        Can either be a literal number (typically "1"), or the name of a field in the structure
        to take the value from the matched event. If you are using a field value, the field
        value must have been matched using the pattern.

        If you want to specify a field from a matched JSON structure, use '$.fieldName',
        and make sure the field is in the pattern (if only as '$.fieldName = *').

        If you want to specify a field from a matched space-delimited structure,
        use '$fieldName'.

        :default: "1"
        '''
        result = self._values.get("metric_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional[_Unit_61bc6f70]:
        '''The unit to assign to the metric.

        :default: - No unit attached to metrics.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-unit
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[_Unit_61bc6f70], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricFilterOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.MetricFilterProps",
    jsii_struct_bases=[MetricFilterOptions],
    name_mapping={
        "filter_pattern": "filterPattern",
        "metric_name": "metricName",
        "metric_namespace": "metricNamespace",
        "default_value": "defaultValue",
        "dimensions": "dimensions",
        "filter_name": "filterName",
        "metric_value": "metricValue",
        "unit": "unit",
        "log_group": "logGroup",
    },
)
class MetricFilterProps(MetricFilterOptions):
    def __init__(
        self,
        *,
        filter_pattern: IFilterPattern,
        metric_name: builtins.str,
        metric_namespace: builtins.str,
        default_value: typing.Optional[jsii.Number] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        filter_name: typing.Optional[builtins.str] = None,
        metric_value: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
        log_group: ILogGroup,
    ) -> None:
        '''Properties for a MetricFilter.

        :param filter_pattern: Pattern to search for log events.
        :param metric_name: The name of the metric to emit.
        :param metric_namespace: The namespace of the metric to emit.
        :param default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
        :param dimensions: The fields to use as dimensions for the metric. One metric filter can include as many as three dimensions. Default: - No dimensions attached to metrics.
        :param filter_name: The name of the metric filter. Default: - Cloudformation generated name.
        :param metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"
        :param unit: The unit to assign to the metric. Default: - No unit attached to metrics.
        :param log_group: The log group to create the filter on.

        :exampleMetadata: lit=aws-logs/test/integ.metricfilter.lit.ts infused

        Example::

            MetricFilter(self, "MetricFilter",
                log_group=log_group,
                metric_namespace="MyApp",
                metric_name="Latency",
                filter_pattern=FilterPattern.all(
                    FilterPattern.exists("$.latency"),
                    FilterPattern.regex_value("$.message", "=", "bind: address already in use")),
                metric_value="$.latency"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66722f3b881a30b7ce1b9efa7c76f2539915abe8fe84a770e1e2c47657d59d79)
            check_type(argname="argument filter_pattern", value=filter_pattern, expected_type=type_hints["filter_pattern"])
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument metric_namespace", value=metric_namespace, expected_type=type_hints["metric_namespace"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
            check_type(argname="argument filter_name", value=filter_name, expected_type=type_hints["filter_name"])
            check_type(argname="argument metric_value", value=metric_value, expected_type=type_hints["metric_value"])
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filter_pattern": filter_pattern,
            "metric_name": metric_name,
            "metric_namespace": metric_namespace,
            "log_group": log_group,
        }
        if default_value is not None:
            self._values["default_value"] = default_value
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if filter_name is not None:
            self._values["filter_name"] = filter_name
        if metric_value is not None:
            self._values["metric_value"] = metric_value
        if unit is not None:
            self._values["unit"] = unit

    @builtins.property
    def filter_pattern(self) -> IFilterPattern:
        '''Pattern to search for log events.'''
        result = self._values.get("filter_pattern")
        assert result is not None, "Required property 'filter_pattern' is missing"
        return typing.cast(IFilterPattern, result)

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''The name of the metric to emit.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_namespace(self) -> builtins.str:
        '''The namespace of the metric to emit.'''
        result = self._values.get("metric_namespace")
        assert result is not None, "Required property 'metric_namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> typing.Optional[jsii.Number]:
        '''The value to emit if the pattern does not match a particular event.

        :default: No metric emitted.
        '''
        result = self._values.get("default_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dimensions(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The fields to use as dimensions for the metric.

        One metric filter can include as many as three dimensions.

        :default: - No dimensions attached to metrics.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-dimensions
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the metric filter.

        :default: - Cloudformation generated name.
        '''
        result = self._values.get("filter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metric_value(self) -> typing.Optional[builtins.str]:
        '''The value to emit for the metric.

        Can either be a literal number (typically "1"), or the name of a field in the structure
        to take the value from the matched event. If you are using a field value, the field
        value must have been matched using the pattern.

        If you want to specify a field from a matched JSON structure, use '$.fieldName',
        and make sure the field is in the pattern (if only as '$.fieldName = *').

        If you want to specify a field from a matched space-delimited structure,
        use '$fieldName'.

        :default: "1"
        '''
        result = self._values.get("metric_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unit(self) -> typing.Optional[_Unit_61bc6f70]:
        '''The unit to assign to the metric.

        :default: - No unit attached to metrics.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-logs-metricfilter-metrictransformation-unit
        '''
        result = self._values.get("unit")
        return typing.cast(typing.Optional[_Unit_61bc6f70], result)

    @builtins.property
    def log_group(self) -> ILogGroup:
        '''The log group to create the filter on.'''
        result = self._values.get("log_group")
        assert result is not None, "Required property 'log_group' is missing"
        return typing.cast(ILogGroup, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.MoveKeyEntryProperty",
    jsii_struct_bases=[],
    name_mapping={
        "source": "source",
        "target": "target",
        "overwrite_if_exists": "overwriteIfExists",
    },
)
class MoveKeyEntryProperty:
    def __init__(
        self,
        *,
        source: builtins.str,
        target: builtins.str,
        overwrite_if_exists: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''This object defines one key that will be moved with the moveKey processor.

        :param source: The key to move.
        :param target: The key to move to.
        :param overwrite_if_exists: Specifies whether to overwrite the value if the target key already exists. Default: false

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            move_key_entry_property = logs.MoveKeyEntryProperty(
                source="source",
                target="target",
            
                # the properties below are optional
                overwrite_if_exists=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da6f3038d5062508ca2dfbdb25c57768aae2900767d6f37a477e7a62987a2f6b)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument overwrite_if_exists", value=overwrite_if_exists, expected_type=type_hints["overwrite_if_exists"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source": source,
            "target": target,
        }
        if overwrite_if_exists is not None:
            self._values["overwrite_if_exists"] = overwrite_if_exists

    @builtins.property
    def source(self) -> builtins.str:
        '''The key to move.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''The key to move to.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def overwrite_if_exists(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether to overwrite the value if the target key already exists.

        :default: false
        '''
        result = self._values.get("overwrite_if_exists")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MoveKeyEntryProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.MoveKeysProperty",
    jsii_struct_bases=[],
    name_mapping={"entries": "entries"},
)
class MoveKeysProperty:
    def __init__(
        self,
        *,
        entries: typing.Sequence[typing.Union[MoveKeyEntryProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''This processor moves a key from one field to another.

        The original key is deleted.
        For more information about this processor including examples, see moveKeys in the CloudWatch Logs User Guide.

        :param entries: An array of objects, where each object contains information about one key to move.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            move_keys_property = logs.MoveKeysProperty(
                entries=[logs.MoveKeyEntryProperty(
                    source="source",
                    target="target",
            
                    # the properties below are optional
                    overwrite_if_exists=False
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d508581afde346c3dc6a7ad903e06a2c24df4ce3b379d82c518c2e7a374e9409)
            check_type(argname="argument entries", value=entries, expected_type=type_hints["entries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entries": entries,
        }

    @builtins.property
    def entries(self) -> typing.List[MoveKeyEntryProperty]:
        '''An array of objects, where each object contains information about one key to move.'''
        result = self._values.get("entries")
        assert result is not None, "Required property 'entries' is missing"
        return typing.cast(typing.List[MoveKeyEntryProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MoveKeysProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.OCSFSourceType")
class OCSFSourceType(enum.Enum):
    '''Types of event sources supported to convert to OCSF format.'''

    CLOUD_TRAIL = "CLOUD_TRAIL"
    '''Log events from CloudTrail.'''
    ROUTE53_RESOLVER = "ROUTE53_RESOLVER"
    '''Log events from Route53Resolver.'''
    VPC_FLOW = "VPC_FLOW"
    '''Log events from VPCFlow.'''
    EKS_AUDIT = "EKS_AUDIT"
    '''Log events from EKSAudit.'''
    AWS_WAF = "AWS_WAF"
    '''Log events from AWSWAF.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.OCSFVersion")
class OCSFVersion(enum.Enum):
    '''OCSF Schema versions supported by transformers.'''

    V1_1 = "V1_1"
    '''OCSF schema version 1.1.

    :see: https://schema.ocsf.io/1.1.0/
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.ParseJSONProperty",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination", "source": "source"},
)
class ParseJSONProperty:
    def __init__(
        self,
        *,
        destination: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''This processor parses log events that are in JSON format.

        It can extract JSON key-value pairs and place them
        under a destination that you specify.
        Additionally, because you must have at least one parse-type processor in a transformer, you can use ParseJSON as that
        processor for JSON-format logs, so that you can also apply other processors, such as mutate processors, to these logs.
        For more information about this processor including examples, see parseJSON in the CloudWatch Logs User Guide.

        :param destination: The location to put the parsed key value pair into. Default: - Placed under root of log event
        :param source: Path to the field in the log event that will be parsed. Use dot notation to access child fields. Default: '@message'

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            parse_jSONProperty = logs.ParseJSONProperty(
                destination="destination",
                source="source"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27216275bd8f254a8df2b93102ca26e488f09ce5ec9e4c3b50617d9234e9f31e)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''The location to put the parsed key value pair into.

        :default: - Placed under root of log event
        '''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Path to the field in the log event that will be parsed.

        Use dot notation to access child fields.

        :default: '@message'
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ParseJSONProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.ParseKeyValueProperty",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "field_delimiter": "fieldDelimiter",
        "key_prefix": "keyPrefix",
        "key_value_delimiter": "keyValueDelimiter",
        "non_match_value": "nonMatchValue",
        "overwrite_if_exists": "overwriteIfExists",
        "source": "source",
    },
)
class ParseKeyValueProperty:
    def __init__(
        self,
        *,
        destination: typing.Optional[builtins.str] = None,
        field_delimiter: typing.Optional[KeyValuePairDelimiter] = None,
        key_prefix: typing.Optional[builtins.str] = None,
        key_value_delimiter: typing.Optional[KeyValueDelimiter] = None,
        non_match_value: typing.Optional[builtins.str] = None,
        overwrite_if_exists: typing.Optional[builtins.bool] = None,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''This processor parses a specified field in the original log event into key-value pairs.

        For more information about this processor including examples, see parseKeyValue in the CloudWatch Logs User Guide.

        :param destination: The destination field to put the extracted key-value pairs into. Default: - Places at the root of the JSON input.
        :param field_delimiter: The field delimiter string that is used between key-value pairs in the original log events. Default: KeyValuePairDelimiter.AMPERSAND
        :param key_prefix: If you want to add a prefix to all transformed keys, specify it here. Default: - No prefix is added to the keys.
        :param key_value_delimiter: The delimiter string to use between the key and value in each pair in the transformed log event. Default: KeyValueDelimiter.EQUAL
        :param non_match_value: A value to insert into the value field in the result, when a key-value pair is not successfully split. Default: - No values is inserted when split is not successful.
        :param overwrite_if_exists: Specifies whether to overwrite the value if the destination key already exists. Default: false
        :param source: Path to the field in the log event that will be parsed. Use dot notation to access child fields. Default: '@message'

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            parse_key_value_property = logs.ParseKeyValueProperty(
                destination="destination",
                field_delimiter=logs.KeyValuePairDelimiter.AMPERSAND,
                key_prefix="keyPrefix",
                key_value_delimiter=logs.KeyValueDelimiter.EQUAL,
                non_match_value="nonMatchValue",
                overwrite_if_exists=False,
                source="source"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3318dff47923fe5f4ad247b238d1986eef32599700ab67d15852a597a0339379)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument field_delimiter", value=field_delimiter, expected_type=type_hints["field_delimiter"])
            check_type(argname="argument key_prefix", value=key_prefix, expected_type=type_hints["key_prefix"])
            check_type(argname="argument key_value_delimiter", value=key_value_delimiter, expected_type=type_hints["key_value_delimiter"])
            check_type(argname="argument non_match_value", value=non_match_value, expected_type=type_hints["non_match_value"])
            check_type(argname="argument overwrite_if_exists", value=overwrite_if_exists, expected_type=type_hints["overwrite_if_exists"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if destination is not None:
            self._values["destination"] = destination
        if field_delimiter is not None:
            self._values["field_delimiter"] = field_delimiter
        if key_prefix is not None:
            self._values["key_prefix"] = key_prefix
        if key_value_delimiter is not None:
            self._values["key_value_delimiter"] = key_value_delimiter
        if non_match_value is not None:
            self._values["non_match_value"] = non_match_value
        if overwrite_if_exists is not None:
            self._values["overwrite_if_exists"] = overwrite_if_exists
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''The destination field to put the extracted key-value pairs into.

        :default: - Places at the root of the JSON input.
        '''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def field_delimiter(self) -> typing.Optional[KeyValuePairDelimiter]:
        '''The field delimiter string that is used between key-value pairs in the original log events.

        :default: KeyValuePairDelimiter.AMPERSAND
        '''
        result = self._values.get("field_delimiter")
        return typing.cast(typing.Optional[KeyValuePairDelimiter], result)

    @builtins.property
    def key_prefix(self) -> typing.Optional[builtins.str]:
        '''If you want to add a prefix to all transformed keys, specify it here.

        :default: - No prefix is added to the keys.
        '''
        result = self._values.get("key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_value_delimiter(self) -> typing.Optional[KeyValueDelimiter]:
        '''The delimiter string to use between the key and value in each pair in the transformed log event.

        :default: KeyValueDelimiter.EQUAL
        '''
        result = self._values.get("key_value_delimiter")
        return typing.cast(typing.Optional[KeyValueDelimiter], result)

    @builtins.property
    def non_match_value(self) -> typing.Optional[builtins.str]:
        '''A value to insert into the value field in the result, when a key-value pair is not successfully split.

        :default: - No values is inserted when split is not successful.
        '''
        result = self._values.get("non_match_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overwrite_if_exists(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether to overwrite the value if the destination key already exists.

        :default: false
        '''
        result = self._values.get("overwrite_if_exists")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Path to the field in the log event that will be parsed.

        Use dot notation to access child fields.

        :default: '@message'
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ParseKeyValueProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.ParseToOCSFProperty",
    jsii_struct_bases=[],
    name_mapping={
        "event_source": "eventSource",
        "ocsf_version": "ocsfVersion",
        "source": "source",
    },
)
class ParseToOCSFProperty:
    def __init__(
        self,
        *,
        event_source: OCSFSourceType,
        ocsf_version: OCSFVersion,
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Processor to parse events from CloudTrail, Route53Resolver, VPCFlow, EKSAudit and AWSWAF into OCSF V1.1 format.

        :param event_source: Type of input log event source to convert to OCSF format.
        :param ocsf_version: Version of OCSF schema to convert to.
        :param source: Path to the field in the log event that will be parsed. Use dot notation to access child fields. Default: '@message'

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            parse_to_oCSFProperty = logs.ParseToOCSFProperty(
                event_source=logs.OCSFSourceType.CLOUD_TRAIL,
                ocsf_version=logs.OCSFVersion.V1_1,
            
                # the properties below are optional
                source="source"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__735c1599edef90b0d0dbcf40602bb77ce633f8947966bf268b4c6dde7571e25a)
            check_type(argname="argument event_source", value=event_source, expected_type=type_hints["event_source"])
            check_type(argname="argument ocsf_version", value=ocsf_version, expected_type=type_hints["ocsf_version"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_source": event_source,
            "ocsf_version": ocsf_version,
        }
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def event_source(self) -> OCSFSourceType:
        '''Type of input log event source to convert to OCSF format.'''
        result = self._values.get("event_source")
        assert result is not None, "Required property 'event_source' is missing"
        return typing.cast(OCSFSourceType, result)

    @builtins.property
    def ocsf_version(self) -> OCSFVersion:
        '''Version of OCSF schema to convert to.'''
        result = self._values.get("ocsf_version")
        assert result is not None, "Required property 'ocsf_version' is missing"
        return typing.cast(OCSFVersion, result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Path to the field in the log event that will be parsed.

        Use dot notation to access child fields.

        :default: '@message'
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ParseToOCSFProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IProcessor)
class ParserProcessor(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.ParserProcessor",
):
    '''Parser processor for common data formats.

    :exampleMetadata: infused

    Example::

        # Create a log group
        log_group = logs.LogGroup(self, "MyLogGroup")
        
        # Create a JSON parser processor
        json_parser = logs.ParserProcessor(
            type=logs.ParserProcessorType.JSON
        )
        
        # Create a processor to add keys
        add_keys_processor = logs.JsonMutatorProcessor(
            type=logs.JsonMutatorType.ADD_KEYS,
            add_keys_options=logs.AddKeysProperty(
                entries=[logs.AddKeyEntryProperty(
                    key="metadata.transformed_in",
                    value="CloudWatchLogs"
                )]
            )
        )
        
        # Create a transformer with these processors
        logs.Transformer(self, "Transformer",
            transformer_name="MyTransformer",
            log_group=log_group,
            transformer_config=[json_parser, add_keys_processor]
        )
    '''

    def __init__(
        self,
        *,
        type: "ParserProcessorType",
        csv_options: typing.Optional[typing.Union[CsvProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        grok_options: typing.Optional[typing.Union[GrokProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        json_options: typing.Optional[typing.Union[ParseJSONProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        key_value_options: typing.Optional[typing.Union[ParseKeyValueProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        parse_to_ocsf_options: typing.Optional[typing.Union[ParseToOCSFProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Creates a new parser processor.

        :param type: The type of parser processor.
        :param csv_options: Options for CSV parser. Required when type is CSV. Default: - No CSV parser is created if props not set
        :param grok_options: Options for Grok parser. Required when type is GROK. Default: - No Grok parser is created if props not set
        :param json_options: Options for JSON parser. Required when type is JSON. Default: - No JSON parser is created if props not set
        :param key_value_options: Options for key-value parser. Required when type is KEY_VALUE. Default: - No key-value parser is created if props not set
        :param parse_to_ocsf_options: Options for ParseToOCSF parser. Required when type is set to OCSF Default: - no OCSF parser is created.
        '''
        props = ParserProcessorProps(
            type=type,
            csv_options=csv_options,
            grok_options=grok_options,
            json_options=json_options,
            key_value_options=key_value_options,
            parse_to_ocsf_options=parse_to_ocsf_options,
        )

        jsii.create(self.__class__, self, [props])

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "ParserProcessorType":
        '''The type of parser.'''
        return typing.cast("ParserProcessorType", jsii.get(self, "type"))

    @type.setter
    def type(self, value: "ParserProcessorType") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a13b8703c16230a1b0b020e63fbdce04c68089e17624ad5d83abcab651aff88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.ParserProcessorProps",
    jsii_struct_bases=[BaseProcessorProps],
    name_mapping={
        "type": "type",
        "csv_options": "csvOptions",
        "grok_options": "grokOptions",
        "json_options": "jsonOptions",
        "key_value_options": "keyValueOptions",
        "parse_to_ocsf_options": "parseToOCSFOptions",
    },
)
class ParserProcessorProps(BaseProcessorProps):
    def __init__(
        self,
        *,
        type: "ParserProcessorType",
        csv_options: typing.Optional[typing.Union[CsvProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        grok_options: typing.Optional[typing.Union[GrokProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        json_options: typing.Optional[typing.Union[ParseJSONProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        key_value_options: typing.Optional[typing.Union[ParseKeyValueProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        parse_to_ocsf_options: typing.Optional[typing.Union[ParseToOCSFProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Properties for creating configurable parser processors.

        :param type: The type of parser processor.
        :param csv_options: Options for CSV parser. Required when type is CSV. Default: - No CSV parser is created if props not set
        :param grok_options: Options for Grok parser. Required when type is GROK. Default: - No Grok parser is created if props not set
        :param json_options: Options for JSON parser. Required when type is JSON. Default: - No JSON parser is created if props not set
        :param key_value_options: Options for key-value parser. Required when type is KEY_VALUE. Default: - No key-value parser is created if props not set
        :param parse_to_ocsf_options: Options for ParseToOCSF parser. Required when type is set to OCSF Default: - no OCSF parser is created.

        :exampleMetadata: infused

        Example::

            # Create a log group
            log_group = logs.LogGroup(self, "MyLogGroup")
            
            # Create a JSON parser processor
            json_parser = logs.ParserProcessor(
                type=logs.ParserProcessorType.JSON
            )
            
            # Create a processor to add keys
            add_keys_processor = logs.JsonMutatorProcessor(
                type=logs.JsonMutatorType.ADD_KEYS,
                add_keys_options=logs.AddKeysProperty(
                    entries=[logs.AddKeyEntryProperty(
                        key="metadata.transformed_in",
                        value="CloudWatchLogs"
                    )]
                )
            )
            
            # Create a transformer with these processors
            logs.Transformer(self, "Transformer",
                transformer_name="MyTransformer",
                log_group=log_group,
                transformer_config=[json_parser, add_keys_processor]
            )
        '''
        if isinstance(csv_options, dict):
            csv_options = CsvProperty(**csv_options)
        if isinstance(grok_options, dict):
            grok_options = GrokProperty(**grok_options)
        if isinstance(json_options, dict):
            json_options = ParseJSONProperty(**json_options)
        if isinstance(key_value_options, dict):
            key_value_options = ParseKeyValueProperty(**key_value_options)
        if isinstance(parse_to_ocsf_options, dict):
            parse_to_ocsf_options = ParseToOCSFProperty(**parse_to_ocsf_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a32cf5eb9ebc811676ec4f9fad1e89dcb2f56561cb63fe216912ac5458a9f85)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument csv_options", value=csv_options, expected_type=type_hints["csv_options"])
            check_type(argname="argument grok_options", value=grok_options, expected_type=type_hints["grok_options"])
            check_type(argname="argument json_options", value=json_options, expected_type=type_hints["json_options"])
            check_type(argname="argument key_value_options", value=key_value_options, expected_type=type_hints["key_value_options"])
            check_type(argname="argument parse_to_ocsf_options", value=parse_to_ocsf_options, expected_type=type_hints["parse_to_ocsf_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if csv_options is not None:
            self._values["csv_options"] = csv_options
        if grok_options is not None:
            self._values["grok_options"] = grok_options
        if json_options is not None:
            self._values["json_options"] = json_options
        if key_value_options is not None:
            self._values["key_value_options"] = key_value_options
        if parse_to_ocsf_options is not None:
            self._values["parse_to_ocsf_options"] = parse_to_ocsf_options

    @builtins.property
    def type(self) -> "ParserProcessorType":
        '''The type of parser processor.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("ParserProcessorType", result)

    @builtins.property
    def csv_options(self) -> typing.Optional[CsvProperty]:
        '''Options for CSV parser.

        Required when type is CSV.

        :default: - No CSV parser is created if props not set
        '''
        result = self._values.get("csv_options")
        return typing.cast(typing.Optional[CsvProperty], result)

    @builtins.property
    def grok_options(self) -> typing.Optional[GrokProperty]:
        '''Options for Grok parser.

        Required when type is GROK.

        :default: - No Grok parser is created if props not set
        '''
        result = self._values.get("grok_options")
        return typing.cast(typing.Optional[GrokProperty], result)

    @builtins.property
    def json_options(self) -> typing.Optional[ParseJSONProperty]:
        '''Options for JSON parser.

        Required when type is JSON.

        :default: - No JSON parser is created if props not set
        '''
        result = self._values.get("json_options")
        return typing.cast(typing.Optional[ParseJSONProperty], result)

    @builtins.property
    def key_value_options(self) -> typing.Optional[ParseKeyValueProperty]:
        '''Options for key-value parser.

        Required when type is KEY_VALUE.

        :default: - No key-value parser is created if props not set
        '''
        result = self._values.get("key_value_options")
        return typing.cast(typing.Optional[ParseKeyValueProperty], result)

    @builtins.property
    def parse_to_ocsf_options(self) -> typing.Optional[ParseToOCSFProperty]:
        '''Options for ParseToOCSF parser.

        Required when type is set to OCSF

        :default: - no OCSF parser is created.
        '''
        result = self._values.get("parse_to_ocsf_options")
        return typing.cast(typing.Optional[ParseToOCSFProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ParserProcessorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.ParserProcessorType")
class ParserProcessorType(enum.Enum):
    '''Types of configurable parser processors.

    Defines the various parser types that can be used to process log events.

    :exampleMetadata: infused

    Example::

        # Create a log group
        log_group = logs.LogGroup(self, "MyLogGroup")
        
        # Create a JSON parser processor
        json_parser = logs.ParserProcessor(
            type=logs.ParserProcessorType.JSON
        )
        
        # Create a processor to add keys
        add_keys_processor = logs.JsonMutatorProcessor(
            type=logs.JsonMutatorType.ADD_KEYS,
            add_keys_options=logs.AddKeysProperty(
                entries=[logs.AddKeyEntryProperty(
                    key="metadata.transformed_in",
                    value="CloudWatchLogs"
                )]
            )
        )
        
        # Create a transformer with these processors
        logs.Transformer(self, "Transformer",
            transformer_name="MyTransformer",
            log_group=log_group,
            transformer_config=[json_parser, add_keys_processor]
        )
    '''

    JSON = "JSON"
    '''Parse log entries as JSON.'''
    KEY_VALUE = "KEY_VALUE"
    '''Parse log entries as key-value pairs.'''
    CSV = "CSV"
    '''Parse log entries in CSV format.'''
    GROK = "GROK"
    '''Parse log entries using Grok patterns.'''
    OCSF = "OCSF"
    '''Parse logs to OCSF format.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.ProcessorDeleteKeysProperty",
    jsii_struct_bases=[],
    name_mapping={"with_keys": "withKeys"},
)
class ProcessorDeleteKeysProperty:
    def __init__(self, *, with_keys: typing.Sequence[builtins.str]) -> None:
        '''This processor adds new key-value pairs to the log event.

        For more information about this processor including examples, see addKeys in the CloudWatch Logs User Guide.

        :param with_keys: A list of keys to delete.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            processor_delete_keys_property = logs.ProcessorDeleteKeysProperty(
                with_keys=["withKeys"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0d7219b7469a32f19b7207dbd41b09b6d3953b5505ac4fc08e7139136f7308d)
            check_type(argname="argument with_keys", value=with_keys, expected_type=type_hints["with_keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "with_keys": with_keys,
        }

    @builtins.property
    def with_keys(self) -> typing.List[builtins.str]:
        '''A list of keys to delete.'''
        result = self._values.get("with_keys")
        assert result is not None, "Required property 'with_keys' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProcessorDeleteKeysProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QueryDefinition(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.QueryDefinition",
):
    '''Define a query definition for CloudWatch Logs Insights.

    :exampleMetadata: infused

    Example::

        logs.QueryDefinition(self, "QueryDefinition",
            query_definition_name="MyQuery",
            query_string=logs.QueryString(
                fields=["@timestamp", "@message"],
                parse_statements=["@message \"[*] *\" as loggingType, loggingMessage", "@message \"<*>: *\" as differentLoggingType, differentLoggingMessage"
                ],
                filter_statements=["loggingType = \"ERROR\"", "loggingMessage = \"A very strange error occurred!\""
                ],
                stats_statements=["count(loggingMessage) as loggingErrors", "count(differentLoggingMessage) as differentLoggingErrors"
                ],
                sort="@timestamp desc",
                limit=20
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        query_definition_name: builtins.str,
        query_string: "QueryString",
        log_groups: typing.Optional[typing.Sequence[ILogGroup]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param query_definition_name: Name of the query definition.
        :param query_string: The query string to use for this query definition.
        :param log_groups: Specify certain log groups for the query definition. Default: - no specified log groups
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7cb87fa9a91fccd75052278e9031242b20cab41bb53f8f18544b867e01e5d41)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = QueryDefinitionProps(
            query_definition_name=query_definition_name,
            query_string=query_string,
            log_groups=log_groups,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))

    @builtins.property
    @jsii.member(jsii_name="queryDefinitionId")
    def query_definition_id(self) -> builtins.str:
        '''The ID of the query definition.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "queryDefinitionId"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.QueryDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "query_definition_name": "queryDefinitionName",
        "query_string": "queryString",
        "log_groups": "logGroups",
    },
)
class QueryDefinitionProps:
    def __init__(
        self,
        *,
        query_definition_name: builtins.str,
        query_string: "QueryString",
        log_groups: typing.Optional[typing.Sequence[ILogGroup]] = None,
    ) -> None:
        '''Properties for a QueryDefinition.

        :param query_definition_name: Name of the query definition.
        :param query_string: The query string to use for this query definition.
        :param log_groups: Specify certain log groups for the query definition. Default: - no specified log groups

        :exampleMetadata: infused

        Example::

            logs.QueryDefinition(self, "QueryDefinition",
                query_definition_name="MyQuery",
                query_string=logs.QueryString(
                    fields=["@timestamp", "@message"],
                    parse_statements=["@message \"[*] *\" as loggingType, loggingMessage", "@message \"<*>: *\" as differentLoggingType, differentLoggingMessage"
                    ],
                    filter_statements=["loggingType = \"ERROR\"", "loggingMessage = \"A very strange error occurred!\""
                    ],
                    stats_statements=["count(loggingMessage) as loggingErrors", "count(differentLoggingMessage) as differentLoggingErrors"
                    ],
                    sort="@timestamp desc",
                    limit=20
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__993712107c64f2acd19761e2b930e6e052534d1100257989bcf307bb6168b668)
            check_type(argname="argument query_definition_name", value=query_definition_name, expected_type=type_hints["query_definition_name"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument log_groups", value=log_groups, expected_type=type_hints["log_groups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "query_definition_name": query_definition_name,
            "query_string": query_string,
        }
        if log_groups is not None:
            self._values["log_groups"] = log_groups

    @builtins.property
    def query_definition_name(self) -> builtins.str:
        '''Name of the query definition.'''
        result = self._values.get("query_definition_name")
        assert result is not None, "Required property 'query_definition_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_string(self) -> "QueryString":
        '''The query string to use for this query definition.'''
        result = self._values.get("query_string")
        assert result is not None, "Required property 'query_string' is missing"
        return typing.cast("QueryString", result)

    @builtins.property
    def log_groups(self) -> typing.Optional[typing.List[ILogGroup]]:
        '''Specify certain log groups for the query definition.

        :default: - no specified log groups
        '''
        result = self._values.get("log_groups")
        return typing.cast(typing.Optional[typing.List[ILogGroup]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueryDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class QueryString(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.QueryString",
):
    '''Define a QueryString.

    :exampleMetadata: infused

    Example::

        logs.QueryDefinition(self, "QueryDefinition",
            query_definition_name="MyQuery",
            query_string=logs.QueryString(
                fields=["@timestamp", "@message"],
                parse_statements=["@message \"[*] *\" as loggingType, loggingMessage", "@message \"<*>: *\" as differentLoggingType, differentLoggingMessage"
                ],
                filter_statements=["loggingType = \"ERROR\"", "loggingMessage = \"A very strange error occurred!\""
                ],
                stats_statements=["count(loggingMessage) as loggingErrors", "count(differentLoggingMessage) as differentLoggingErrors"
                ],
                sort="@timestamp desc",
                limit=20
            )
        )
    '''

    def __init__(
        self,
        *,
        display: typing.Optional[builtins.str] = None,
        fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        filter: typing.Optional[builtins.str] = None,
        filter_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        limit: typing.Optional[jsii.Number] = None,
        parse: typing.Optional[builtins.str] = None,
        parse_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        sort: typing.Optional[builtins.str] = None,
        stats: typing.Optional[builtins.str] = None,
        stats_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param display: Specifies which fields to display in the query results. Default: - no display in QueryString
        :param fields: Retrieves the specified fields from log events for display. Default: - no fields in QueryString
        :param filter: (deprecated) A single statement for filtering the results of a query based on a boolean expression. Default: - no filter in QueryString
        :param filter_statements: An array of one or more statements for filtering the results of a query based on a boolean expression. Each provided statement generates a separate filter line in the query string. Note: If provided, this property overrides any value provided for the ``filter`` property. Default: - no filter in QueryString
        :param limit: Specifies the number of log events returned by the query. Default: - no limit in QueryString
        :param parse: (deprecated) A single statement for parsing data from a log field and creating ephemeral fields that can be processed further in the query. Default: - no parse in QueryString
        :param parse_statements: An array of one or more statements for parsing data from a log field and creating ephemeral fields that can be processed further in the query. Each provided statement generates a separate parse line in the query string. Note: If provided, this property overrides any value provided for the ``parse`` property. Default: - no parse in QueryString
        :param sort: Sorts the retrieved log events. Default: - no sort in QueryString
        :param stats: (deprecated) A single statement for using log field values to calculate aggregate statistics. Default: - no stats in QueryString
        :param stats_statements: An array of one or more statements for calculating aggregate statistics. CloudWatch Logs Insights supports up to two stats commands in a single query. Each provided statement generates a separate stats line in the query string. Note: If provided, this property overrides any value provided for the ``stats`` property. Default: - no stats in QueryString
        '''
        props = QueryStringProps(
            display=display,
            fields=fields,
            filter=filter,
            filter_statements=filter_statements,
            limit=limit,
            parse=parse,
            parse_statements=parse_statements,
            sort=sort,
            stats=stats,
            stats_statements=stats_statements,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''String representation of this QueryString.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="hasStatsAndStatsStatements")
    def has_stats_and_stats_statements(self) -> builtins.bool:
        '''If the props for the query string have both stats and statsStatements.'''
        return typing.cast(builtins.bool, jsii.get(self, "hasStatsAndStatsStatements"))

    @builtins.property
    @jsii.member(jsii_name="statsStatementsLength")
    def stats_statements_length(self) -> typing.Optional[jsii.Number]:
        '''Length of statsStatements.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statsStatementsLength"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.QueryStringProps",
    jsii_struct_bases=[],
    name_mapping={
        "display": "display",
        "fields": "fields",
        "filter": "filter",
        "filter_statements": "filterStatements",
        "limit": "limit",
        "parse": "parse",
        "parse_statements": "parseStatements",
        "sort": "sort",
        "stats": "stats",
        "stats_statements": "statsStatements",
    },
)
class QueryStringProps:
    def __init__(
        self,
        *,
        display: typing.Optional[builtins.str] = None,
        fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        filter: typing.Optional[builtins.str] = None,
        filter_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        limit: typing.Optional[jsii.Number] = None,
        parse: typing.Optional[builtins.str] = None,
        parse_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
        sort: typing.Optional[builtins.str] = None,
        stats: typing.Optional[builtins.str] = None,
        stats_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for a QueryString.

        :param display: Specifies which fields to display in the query results. Default: - no display in QueryString
        :param fields: Retrieves the specified fields from log events for display. Default: - no fields in QueryString
        :param filter: (deprecated) A single statement for filtering the results of a query based on a boolean expression. Default: - no filter in QueryString
        :param filter_statements: An array of one or more statements for filtering the results of a query based on a boolean expression. Each provided statement generates a separate filter line in the query string. Note: If provided, this property overrides any value provided for the ``filter`` property. Default: - no filter in QueryString
        :param limit: Specifies the number of log events returned by the query. Default: - no limit in QueryString
        :param parse: (deprecated) A single statement for parsing data from a log field and creating ephemeral fields that can be processed further in the query. Default: - no parse in QueryString
        :param parse_statements: An array of one or more statements for parsing data from a log field and creating ephemeral fields that can be processed further in the query. Each provided statement generates a separate parse line in the query string. Note: If provided, this property overrides any value provided for the ``parse`` property. Default: - no parse in QueryString
        :param sort: Sorts the retrieved log events. Default: - no sort in QueryString
        :param stats: (deprecated) A single statement for using log field values to calculate aggregate statistics. Default: - no stats in QueryString
        :param stats_statements: An array of one or more statements for calculating aggregate statistics. CloudWatch Logs Insights supports up to two stats commands in a single query. Each provided statement generates a separate stats line in the query string. Note: If provided, this property overrides any value provided for the ``stats`` property. Default: - no stats in QueryString

        :exampleMetadata: infused

        Example::

            logs.QueryDefinition(self, "QueryDefinition",
                query_definition_name="MyQuery",
                query_string=logs.QueryString(
                    fields=["@timestamp", "@message"],
                    parse_statements=["@message \"[*] *\" as loggingType, loggingMessage", "@message \"<*>: *\" as differentLoggingType, differentLoggingMessage"
                    ],
                    filter_statements=["loggingType = \"ERROR\"", "loggingMessage = \"A very strange error occurred!\""
                    ],
                    stats_statements=["count(loggingMessage) as loggingErrors", "count(differentLoggingMessage) as differentLoggingErrors"
                    ],
                    sort="@timestamp desc",
                    limit=20
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d205eb2ac9b46de0083e3387b95b00f2362e2ade91d5c581e5d8cde68293b28d)
            check_type(argname="argument display", value=display, expected_type=type_hints["display"])
            check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument filter_statements", value=filter_statements, expected_type=type_hints["filter_statements"])
            check_type(argname="argument limit", value=limit, expected_type=type_hints["limit"])
            check_type(argname="argument parse", value=parse, expected_type=type_hints["parse"])
            check_type(argname="argument parse_statements", value=parse_statements, expected_type=type_hints["parse_statements"])
            check_type(argname="argument sort", value=sort, expected_type=type_hints["sort"])
            check_type(argname="argument stats", value=stats, expected_type=type_hints["stats"])
            check_type(argname="argument stats_statements", value=stats_statements, expected_type=type_hints["stats_statements"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if display is not None:
            self._values["display"] = display
        if fields is not None:
            self._values["fields"] = fields
        if filter is not None:
            self._values["filter"] = filter
        if filter_statements is not None:
            self._values["filter_statements"] = filter_statements
        if limit is not None:
            self._values["limit"] = limit
        if parse is not None:
            self._values["parse"] = parse
        if parse_statements is not None:
            self._values["parse_statements"] = parse_statements
        if sort is not None:
            self._values["sort"] = sort
        if stats is not None:
            self._values["stats"] = stats
        if stats_statements is not None:
            self._values["stats_statements"] = stats_statements

    @builtins.property
    def display(self) -> typing.Optional[builtins.str]:
        '''Specifies which fields to display in the query results.

        :default: - no display in QueryString
        '''
        result = self._values.get("display")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Retrieves the specified fields from log events for display.

        :default: - no fields in QueryString
        '''
        result = self._values.get("fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def filter(self) -> typing.Optional[builtins.str]:
        '''(deprecated) A single statement for filtering the results of a query based on a boolean expression.

        :default: - no filter in QueryString

        :deprecated: Use ``filterStatements`` instead

        :stability: deprecated
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of one or more statements for filtering the results of a query based on a boolean expression.

        Each provided statement generates a separate filter line in the query string.

        Note: If provided, this property overrides any value provided for the ``filter`` property.

        :default: - no filter in QueryString
        '''
        result = self._values.get("filter_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def limit(self) -> typing.Optional[jsii.Number]:
        '''Specifies the number of log events returned by the query.

        :default: - no limit in QueryString
        '''
        result = self._values.get("limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parse(self) -> typing.Optional[builtins.str]:
        '''(deprecated) A single statement for parsing data from a log field and creating ephemeral fields that can be processed further in the query.

        :default: - no parse in QueryString

        :deprecated: Use ``parseStatements`` instead

        :stability: deprecated
        '''
        result = self._values.get("parse")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parse_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of one or more statements for parsing data from a log field and creating ephemeral fields that can be processed further in the query.

        Each provided statement generates a separate
        parse line in the query string.

        Note: If provided, this property overrides any value provided for the ``parse`` property.

        :default: - no parse in QueryString
        '''
        result = self._values.get("parse_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sort(self) -> typing.Optional[builtins.str]:
        '''Sorts the retrieved log events.

        :default: - no sort in QueryString
        '''
        result = self._values.get("sort")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stats(self) -> typing.Optional[builtins.str]:
        '''(deprecated) A single statement for using log field values to calculate aggregate statistics.

        :default: - no stats in QueryString

        :deprecated: Use ``statsStatements`` instead

        :stability: deprecated
        '''
        result = self._values.get("stats")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stats_statements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of one or more statements for calculating aggregate statistics.

        CloudWatch Logs Insights supports up to two stats commands in a single query.
        Each provided statement generates a separate stats line in the query string.

        Note: If provided, this property overrides any value provided for the ``stats`` property.

        :default: - no stats in QueryString
        '''
        result = self._values.get("stats_statements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueryStringProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.QuoteCharacter")
class QuoteCharacter(enum.Enum):
    '''Valid quote characters for CSV processor.

    Defines the character used as a text qualifier for a single column of data.
    '''

    DOUBLE_QUOTE = "DOUBLE_QUOTE"
    '''Double quote character (default).'''
    SINGLE_QUOTE = "SINGLE_QUOTE"
    '''Single quote character.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.RenameKeyEntryProperty",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "rename_to": "renameTo",
        "overwrite_if_exists": "overwriteIfExists",
    },
)
class RenameKeyEntryProperty:
    def __init__(
        self,
        *,
        key: builtins.str,
        rename_to: builtins.str,
        overwrite_if_exists: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''This object defines one key that will be renamed with the renameKey processor.

        :param key: The key to rename.
        :param rename_to: The string to use for the new key name.
        :param overwrite_if_exists: Whether to overwrite the target key if it already exists. Default: false

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            rename_key_entry_property = logs.RenameKeyEntryProperty(
                key="key",
                rename_to="renameTo",
            
                # the properties below are optional
                overwrite_if_exists=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79c7d64341c225a9e8d9c156812001b053b87c33197fc3f9fb96e14931bf62f8)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument rename_to", value=rename_to, expected_type=type_hints["rename_to"])
            check_type(argname="argument overwrite_if_exists", value=overwrite_if_exists, expected_type=type_hints["overwrite_if_exists"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "rename_to": rename_to,
        }
        if overwrite_if_exists is not None:
            self._values["overwrite_if_exists"] = overwrite_if_exists

    @builtins.property
    def key(self) -> builtins.str:
        '''The key to rename.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rename_to(self) -> builtins.str:
        '''The string to use for the new key name.'''
        result = self._values.get("rename_to")
        assert result is not None, "Required property 'rename_to' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def overwrite_if_exists(self) -> typing.Optional[builtins.bool]:
        '''Whether to overwrite the target key if it already exists.

        :default: false
        '''
        result = self._values.get("overwrite_if_exists")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RenameKeyEntryProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.RenameKeysProperty",
    jsii_struct_bases=[],
    name_mapping={"entries": "entries"},
)
class RenameKeysProperty:
    def __init__(
        self,
        *,
        entries: typing.Sequence[typing.Union[RenameKeyEntryProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Use this processor to rename keys in a log event.

        For more information about this processor including examples, see renameKeys in the CloudWatch Logs User Guide.

        :param entries: An array of RenameKeyEntry objects, where each object contains information about one key to rename.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            rename_keys_property = logs.RenameKeysProperty(
                entries=[logs.RenameKeyEntryProperty(
                    key="key",
                    rename_to="renameTo",
            
                    # the properties below are optional
                    overwrite_if_exists=False
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__198823a45c6e5e4862ca8d9502cccda6799064b56d480db08bb111e19d801f21)
            check_type(argname="argument entries", value=entries, expected_type=type_hints["entries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entries": entries,
        }

    @builtins.property
    def entries(self) -> typing.List[RenameKeyEntryProperty]:
        '''An array of RenameKeyEntry objects, where each object contains information about one key to rename.'''
        result = self._values.get("entries")
        assert result is not None, "Required property 'entries' is missing"
        return typing.cast(typing.List[RenameKeyEntryProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RenameKeysProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ResourcePolicy(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.ResourcePolicy",
):
    '''Resource Policy for CloudWatch Log Groups.

    Policies define the operations that are allowed on this resource.

    You almost never need to define this construct directly.

    All AWS resources that support resource policies have a method called
    ``addToResourcePolicy()``, which will automatically create a new resource
    policy if one doesn't exist yet, otherwise it will add to the existing
    policy.

    Prefer to use ``addToResourcePolicy()`` instead.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        from aws_cdk import aws_logs as logs
        
        # policy_statement: iam.PolicyStatement
        
        resource_policy = logs.ResourcePolicy(self, "MyResourcePolicy",
            policy_statements=[policy_statement],
            resource_policy_name="resourcePolicyName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_statements: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        resource_policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param policy_statements: Initial statements to add to the resource policy. Default: - No statements
        :param resource_policy_name: Name of the log group resource policy. Default: - Uses a unique id based on the construct path
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__772b118f71acb9e446b4948b9aac7bf360262cdeddc09c1f28708795cdb48c74)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ResourcePolicyProps(
            policy_statements=policy_statements,
            resource_policy_name=resource_policy_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))

    @builtins.property
    @jsii.member(jsii_name="document")
    def document(self) -> _PolicyDocument_3ac34393:
        '''The IAM policy document for this resource policy.'''
        return typing.cast(_PolicyDocument_3ac34393, jsii.get(self, "document"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.ResourcePolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy_statements": "policyStatements",
        "resource_policy_name": "resourcePolicyName",
    },
)
class ResourcePolicyProps:
    def __init__(
        self,
        *,
        policy_statements: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        resource_policy_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties to define Cloudwatch log group resource policy.

        :param policy_statements: Initial statements to add to the resource policy. Default: - No statements
        :param resource_policy_name: Name of the log group resource policy. Default: - Uses a unique id based on the construct path

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_logs as logs
            
            # policy_statement: iam.PolicyStatement
            
            resource_policy_props = logs.ResourcePolicyProps(
                policy_statements=[policy_statement],
                resource_policy_name="resourcePolicyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4f5108e8fcf5bafe964b9be836229eed1f4ac734a83be621801cd6304143286)
            check_type(argname="argument policy_statements", value=policy_statements, expected_type=type_hints["policy_statements"])
            check_type(argname="argument resource_policy_name", value=resource_policy_name, expected_type=type_hints["resource_policy_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if policy_statements is not None:
            self._values["policy_statements"] = policy_statements
        if resource_policy_name is not None:
            self._values["resource_policy_name"] = resource_policy_name

    @builtins.property
    def policy_statements(
        self,
    ) -> typing.Optional[typing.List[_PolicyStatement_0fe33853]]:
        '''Initial statements to add to the resource policy.

        :default: - No statements
        '''
        result = self._values.get("policy_statements")
        return typing.cast(typing.Optional[typing.List[_PolicyStatement_0fe33853]], result)

    @builtins.property
    def resource_policy_name(self) -> typing.Optional[builtins.str]:
        '''Name of the log group resource policy.

        :default: - Uses a unique id based on the construct path
        '''
        result = self._values.get("resource_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourcePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.RetentionDays")
class RetentionDays(enum.Enum):
    '''How long, in days, the log contents will be retained.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_logs as logs
        
        
        api_key_provider = appsync.AppSyncAuthProvider(
            authorization_type=appsync.AppSyncAuthorizationType.API_KEY
        )
        
        api = appsync.EventApi(self, "api",
            api_name="Api",
            owner_contact="OwnerContact",
            authorization_config=appsync.EventApiAuthConfig(
                auth_providers=[api_key_provider
                ],
                connection_auth_mode_types=[appsync.AppSyncAuthorizationType.API_KEY
                ],
                default_publish_auth_mode_types=[appsync.AppSyncAuthorizationType.API_KEY
                ],
                default_subscribe_auth_mode_types=[appsync.AppSyncAuthorizationType.API_KEY
                ]
            ),
            log_config=appsync.AppSyncLogConfig(
                field_log_level=appsync.AppSyncFieldLogLevel.INFO,
                retention=logs.RetentionDays.ONE_WEEK
            )
        )
        
        api.add_channel_namespace("default")
    '''

    ONE_DAY = "ONE_DAY"
    '''1 day.'''
    THREE_DAYS = "THREE_DAYS"
    '''3 days.'''
    FIVE_DAYS = "FIVE_DAYS"
    '''5 days.'''
    ONE_WEEK = "ONE_WEEK"
    '''1 week.'''
    TWO_WEEKS = "TWO_WEEKS"
    '''2 weeks.'''
    ONE_MONTH = "ONE_MONTH"
    '''1 month.'''
    TWO_MONTHS = "TWO_MONTHS"
    '''2 months.'''
    THREE_MONTHS = "THREE_MONTHS"
    '''3 months.'''
    FOUR_MONTHS = "FOUR_MONTHS"
    '''4 months.'''
    FIVE_MONTHS = "FIVE_MONTHS"
    '''5 months.'''
    SIX_MONTHS = "SIX_MONTHS"
    '''6 months.'''
    ONE_YEAR = "ONE_YEAR"
    '''1 year.'''
    THIRTEEN_MONTHS = "THIRTEEN_MONTHS"
    '''13 months.'''
    EIGHTEEN_MONTHS = "EIGHTEEN_MONTHS"
    '''18 months.'''
    TWO_YEARS = "TWO_YEARS"
    '''2 years.'''
    THREE_YEARS = "THREE_YEARS"
    '''3 years.'''
    FIVE_YEARS = "FIVE_YEARS"
    '''5 years.'''
    SIX_YEARS = "SIX_YEARS"
    '''6 years.'''
    SEVEN_YEARS = "SEVEN_YEARS"
    '''7 years.'''
    EIGHT_YEARS = "EIGHT_YEARS"
    '''8 years.'''
    NINE_YEARS = "NINE_YEARS"
    '''9 years.'''
    TEN_YEARS = "TEN_YEARS"
    '''10 years.'''
    INFINITE = "INFINITE"
    '''Retain logs forever.'''


@jsii.implements(IFilterPattern)
class SpaceDelimitedTextPattern(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.SpaceDelimitedTextPattern",
):
    '''Space delimited text pattern.

    :exampleMetadata: infused

    Example::

        # Search for all events where the component is "HttpServer" and the
        # result code is not equal to 200.
        pattern = logs.FilterPattern.space_delimited("time", "component", "...", "result_code", "latency").where_string("component", "=", "HttpServer").where_number("result_code", "!=", 200)
    '''

    def __init__(
        self,
        columns: typing.Sequence[builtins.str],
        restrictions: typing.Mapping[builtins.str, typing.Sequence[typing.Union[ColumnRestriction, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param columns: -
        :param restrictions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b056cc11acf9eec747709139eb527ca4dbbf26be0a7b192c65f6ce27af65184)
            check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
            check_type(argname="argument restrictions", value=restrictions, expected_type=type_hints["restrictions"])
        jsii.create(self.__class__, self, [columns, restrictions])

    @jsii.member(jsii_name="construct")
    @builtins.classmethod
    def construct(
        cls,
        columns: typing.Sequence[builtins.str],
    ) -> "SpaceDelimitedTextPattern":
        '''Construct a new instance of a space delimited text pattern.

        Since this class must be public, we can't rely on the user only creating it through
        the ``LogPattern.spaceDelimited()`` factory function. We must therefore validate the
        argument in the constructor. Since we're returning a copy on every mutation, and we
        don't want to re-validate the same things on every construction, we provide a limited
        set of mutator functions and only validate the new data every time.

        :param columns: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d1e9e085756c1b7939b77b321d912811c1ae652d0160b5c494b0894d37e178)
            check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
        return typing.cast("SpaceDelimitedTextPattern", jsii.sinvoke(cls, "construct", [columns]))

    @jsii.member(jsii_name="whereNumber")
    def where_number(
        self,
        column_name: builtins.str,
        comparison: builtins.str,
        value: jsii.Number,
    ) -> "SpaceDelimitedTextPattern":
        '''Restrict where the pattern applies.

        :param column_name: -
        :param comparison: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9837cdc1b4560186b7313c523de825a85b6c099daae328e79ce8c2a6fcc1431f)
            check_type(argname="argument column_name", value=column_name, expected_type=type_hints["column_name"])
            check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("SpaceDelimitedTextPattern", jsii.invoke(self, "whereNumber", [column_name, comparison, value]))

    @jsii.member(jsii_name="whereString")
    def where_string(
        self,
        column_name: builtins.str,
        comparison: builtins.str,
        value: builtins.str,
    ) -> "SpaceDelimitedTextPattern":
        '''Restrict where the pattern applies.

        :param column_name: -
        :param comparison: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__071ad580f6d865947c2434ea9ce22e541c8aabe0aaf4f627b337988d5c6c6ccd)
            check_type(argname="argument column_name", value=column_name, expected_type=type_hints["column_name"])
            check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("SpaceDelimitedTextPattern", jsii.invoke(self, "whereString", [column_name, comparison, value]))

    @builtins.property
    @jsii.member(jsii_name="logPatternString")
    def log_pattern_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logPatternString"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.SplitStringEntryProperty",
    jsii_struct_bases=[],
    name_mapping={"delimiter": "delimiter", "source": "source"},
)
class SplitStringEntryProperty:
    def __init__(self, *, delimiter: DelimiterCharacter, source: builtins.str) -> None:
        '''This object defines one log field that will be split with the splitString processor.

        :param delimiter: The separator character to split the string on.
        :param source: The key of the field to split.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            split_string_entry_property = logs.SplitStringEntryProperty(
                delimiter=logs.DelimiterCharacter.COMMA,
                source="source"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0da5731b4ea06065f3a14013f1f462ddb062c7a6f696ed9790bdebff32f6b487)
            check_type(argname="argument delimiter", value=delimiter, expected_type=type_hints["delimiter"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delimiter": delimiter,
            "source": source,
        }

    @builtins.property
    def delimiter(self) -> DelimiterCharacter:
        '''The separator character to split the string on.'''
        result = self._values.get("delimiter")
        assert result is not None, "Required property 'delimiter' is missing"
        return typing.cast(DelimiterCharacter, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''The key of the field to split.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SplitStringEntryProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.SplitStringProperty",
    jsii_struct_bases=[],
    name_mapping={"entries": "entries"},
)
class SplitStringProperty:
    def __init__(
        self,
        *,
        entries: typing.Sequence[typing.Union[SplitStringEntryProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Use this processor to split a field into an array of strings using a delimiting character.

        For more information about this processor including examples, see splitString in the CloudWatch Logs User Guide.

        :param entries: An array of SplitStringEntry objects, where each object contains information about one field to split.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            split_string_property = logs.SplitStringProperty(
                entries=[logs.SplitStringEntryProperty(
                    delimiter=logs.DelimiterCharacter.COMMA,
                    source="source"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93325aed54aeb72271014f8d01393fe4bead496c1b4b9a96fe2628a72856b895)
            check_type(argname="argument entries", value=entries, expected_type=type_hints["entries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entries": entries,
        }

    @builtins.property
    def entries(self) -> typing.List[SplitStringEntryProperty]:
        '''An array of SplitStringEntry objects, where each object contains information about one field to split.'''
        result = self._values.get("entries")
        assert result is not None, "Required property 'entries' is missing"
        return typing.cast(typing.List[SplitStringEntryProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SplitStringProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.StreamOptions",
    jsii_struct_bases=[],
    name_mapping={"log_stream_name": "logStreamName"},
)
class StreamOptions:
    def __init__(
        self,
        *,
        log_stream_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a new LogStream created from a LogGroup.

        :param log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            stream_options = logs.StreamOptions(
                log_stream_name="logStreamName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faa627faaa2e41610592354837a6717d48ec540f225e5fa931868e06dda19d5e)
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if log_stream_name is not None:
            self._values["log_stream_name"] = log_stream_name

    @builtins.property
    def log_stream_name(self) -> typing.Optional[builtins.str]:
        '''The name of the log stream to create.

        The name must be unique within the log group.

        :default: Automatically generated
        '''
        result = self._values.get("log_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IProcessor)
class StringMutatorProcessor(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.StringMutatorProcessor",
):
    '''Processor for string mutation operations.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        string_mutator_processor = logs.StringMutatorProcessor(
            type=logs.StringMutatorType.LOWER_CASE,
        
            # the properties below are optional
            lower_case_keys=["lowerCaseKeys"],
            split_options=logs.SplitStringProperty(
                entries=[logs.SplitStringEntryProperty(
                    delimiter=logs.DelimiterCharacter.COMMA,
                    source="source"
                )]
            ),
            substitute_options=logs.SubstituteStringProperty(
                entries=[logs.SubstituteStringEntryProperty(
                    from="from",
                    source="source",
                    to="to"
                )]
            ),
            trim_keys=["trimKeys"],
            upper_case_keys=["upperCaseKeys"]
        )
    '''

    def __init__(
        self,
        *,
        type: "StringMutatorType",
        lower_case_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        split_options: typing.Optional[typing.Union[SplitStringProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        substitute_options: typing.Optional[typing.Union["SubstituteStringProperty", typing.Dict[builtins.str, typing.Any]]] = None,
        trim_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        upper_case_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Creates a new string mutator processor.

        :param type: The type of string mutation operation.
        :param lower_case_keys: Keys for strings to convert to lowercase. Required when type is LOWER_CASE. Default: - No lowercase processor is created if props not set
        :param split_options: Options for string splitting. Required when type is SPLIT. Default: - No string splitting processor is created if props not set
        :param substitute_options: Options for string substitution. Required when type is SUBSTITUTE. Default: - No string substitution processor is created if props not set
        :param trim_keys: Keys for strings to trim. Required when type is TRIM. Default: - No trim processor is created if props not set
        :param upper_case_keys: Keys for strings to convert to uppercase. Required when type is UPPER_CASE. Default: - No uppercase processor is created if props not set
        '''
        props = StringMutatorProps(
            type=type,
            lower_case_keys=lower_case_keys,
            split_options=split_options,
            substitute_options=substitute_options,
            trim_keys=trim_keys,
            upper_case_keys=upper_case_keys,
        )

        jsii.create(self.__class__, self, [props])

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> "StringMutatorType":
        '''The type of string mutation operation.'''
        return typing.cast("StringMutatorType", jsii.get(self, "type"))

    @type.setter
    def type(self, value: "StringMutatorType") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc8c1fe39cd0dbda92f882107b130bc9378206d263f648e0ae3930de51c6987f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.StringMutatorProps",
    jsii_struct_bases=[BaseProcessorProps],
    name_mapping={
        "type": "type",
        "lower_case_keys": "lowerCaseKeys",
        "split_options": "splitOptions",
        "substitute_options": "substituteOptions",
        "trim_keys": "trimKeys",
        "upper_case_keys": "upperCaseKeys",
    },
)
class StringMutatorProps(BaseProcessorProps):
    def __init__(
        self,
        *,
        type: "StringMutatorType",
        lower_case_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        split_options: typing.Optional[typing.Union[SplitStringProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        substitute_options: typing.Optional[typing.Union["SubstituteStringProperty", typing.Dict[builtins.str, typing.Any]]] = None,
        trim_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        upper_case_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for creating string mutator processors.

        :param type: The type of string mutation operation.
        :param lower_case_keys: Keys for strings to convert to lowercase. Required when type is LOWER_CASE. Default: - No lowercase processor is created if props not set
        :param split_options: Options for string splitting. Required when type is SPLIT. Default: - No string splitting processor is created if props not set
        :param substitute_options: Options for string substitution. Required when type is SUBSTITUTE. Default: - No string substitution processor is created if props not set
        :param trim_keys: Keys for strings to trim. Required when type is TRIM. Default: - No trim processor is created if props not set
        :param upper_case_keys: Keys for strings to convert to uppercase. Required when type is UPPER_CASE. Default: - No uppercase processor is created if props not set

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            string_mutator_props = logs.StringMutatorProps(
                type=logs.StringMutatorType.LOWER_CASE,
            
                # the properties below are optional
                lower_case_keys=["lowerCaseKeys"],
                split_options=logs.SplitStringProperty(
                    entries=[logs.SplitStringEntryProperty(
                        delimiter=logs.DelimiterCharacter.COMMA,
                        source="source"
                    )]
                ),
                substitute_options=logs.SubstituteStringProperty(
                    entries=[logs.SubstituteStringEntryProperty(
                        from="from",
                        source="source",
                        to="to"
                    )]
                ),
                trim_keys=["trimKeys"],
                upper_case_keys=["upperCaseKeys"]
            )
        '''
        if isinstance(split_options, dict):
            split_options = SplitStringProperty(**split_options)
        if isinstance(substitute_options, dict):
            substitute_options = SubstituteStringProperty(**substitute_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9a1cadbe7ded283aeca06e2d5345cb01473604a502a95e3776eb51172e23ea5)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument lower_case_keys", value=lower_case_keys, expected_type=type_hints["lower_case_keys"])
            check_type(argname="argument split_options", value=split_options, expected_type=type_hints["split_options"])
            check_type(argname="argument substitute_options", value=substitute_options, expected_type=type_hints["substitute_options"])
            check_type(argname="argument trim_keys", value=trim_keys, expected_type=type_hints["trim_keys"])
            check_type(argname="argument upper_case_keys", value=upper_case_keys, expected_type=type_hints["upper_case_keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if lower_case_keys is not None:
            self._values["lower_case_keys"] = lower_case_keys
        if split_options is not None:
            self._values["split_options"] = split_options
        if substitute_options is not None:
            self._values["substitute_options"] = substitute_options
        if trim_keys is not None:
            self._values["trim_keys"] = trim_keys
        if upper_case_keys is not None:
            self._values["upper_case_keys"] = upper_case_keys

    @builtins.property
    def type(self) -> "StringMutatorType":
        '''The type of string mutation operation.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("StringMutatorType", result)

    @builtins.property
    def lower_case_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Keys for strings to convert to lowercase.

        Required when type is LOWER_CASE.

        :default: - No lowercase processor is created if props not set
        '''
        result = self._values.get("lower_case_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def split_options(self) -> typing.Optional[SplitStringProperty]:
        '''Options for string splitting.

        Required when type is SPLIT.

        :default: - No string splitting processor is created if props not set
        '''
        result = self._values.get("split_options")
        return typing.cast(typing.Optional[SplitStringProperty], result)

    @builtins.property
    def substitute_options(self) -> typing.Optional["SubstituteStringProperty"]:
        '''Options for string substitution.

        Required when type is SUBSTITUTE.

        :default: - No string substitution processor is created if props not set
        '''
        result = self._values.get("substitute_options")
        return typing.cast(typing.Optional["SubstituteStringProperty"], result)

    @builtins.property
    def trim_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Keys for strings to trim.

        Required when type is TRIM.

        :default: - No trim processor is created if props not set
        '''
        result = self._values.get("trim_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def upper_case_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Keys for strings to convert to uppercase.

        Required when type is UPPER_CASE.

        :default: - No uppercase processor is created if props not set
        '''
        result = self._values.get("upper_case_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StringMutatorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.StringMutatorType")
class StringMutatorType(enum.Enum):
    '''Types of string mutation operations.

    Defines various operations that can be performed to modify string values in log events.
    '''

    LOWER_CASE = "LOWER_CASE"
    '''Convert strings to lowercase.'''
    UPPER_CASE = "UPPER_CASE"
    '''Convert strings to uppercase.'''
    TRIM = "TRIM"
    '''Trim whitespace from strings.'''
    SPLIT = "SPLIT"
    '''Split strings by delimiter.'''
    SUBSTITUTE = "SUBSTITUTE"
    '''Replace substrings in strings.'''


class SubscriptionFilter(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.SubscriptionFilter",
):
    '''A new Subscription on a CloudWatch log group.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_logs_destinations as destinations
        
        # fn: lambda.Function
        # log_group: logs.LogGroup
        
        
        logs.SubscriptionFilter(self, "Subscription",
            log_group=log_group,
            destination=destinations.LambdaDestination(fn),
            filter_pattern=logs.FilterPattern.all_terms("ERROR", "MainThread"),
            filter_name="ErrorInMainThread"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        log_group: ILogGroup,
        destination: ILogSubscriptionDestination,
        filter_pattern: IFilterPattern,
        distribution: typing.Optional[Distribution] = None,
        filter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param log_group: The log group to create the subscription on.
        :param destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
        :param filter_pattern: Log events matching this pattern will be sent to the destination.
        :param distribution: The method used to distribute log data to the destination. This property can only be used with KinesisDestination. Default: Distribution.BY_LOG_STREAM
        :param filter_name: The name of the subscription filter. Default: Automatically generated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3c78d3f905ddfb9bb1ff8466a0b030e7b262b0793c43d2667b561e420cbb3c7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SubscriptionFilterProps(
            log_group=log_group,
            destination=destination,
            filter_pattern=filter_pattern,
            distribution=distribution,
            filter_name=filter_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.SubscriptionFilterOptions",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "filter_pattern": "filterPattern",
        "distribution": "distribution",
        "filter_name": "filterName",
    },
)
class SubscriptionFilterOptions:
    def __init__(
        self,
        *,
        destination: ILogSubscriptionDestination,
        filter_pattern: IFilterPattern,
        distribution: typing.Optional[Distribution] = None,
        filter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a new SubscriptionFilter created from a LogGroup.

        :param destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
        :param filter_pattern: Log events matching this pattern will be sent to the destination.
        :param distribution: The method used to distribute log data to the destination. This property can only be used with KinesisDestination. Default: Distribution.BY_LOG_STREAM
        :param filter_name: The name of the subscription filter. Default: Automatically generated

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            # filter_pattern: logs.IFilterPattern
            # log_subscription_destination: logs.ILogSubscriptionDestination
            
            subscription_filter_options = logs.SubscriptionFilterOptions(
                destination=log_subscription_destination,
                filter_pattern=filter_pattern,
            
                # the properties below are optional
                distribution=logs.Distribution.BY_LOG_STREAM,
                filter_name="filterName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__177a84e94bfd826b20adc1107770c972772c540b0a1ac8475f63476502450a73)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument filter_pattern", value=filter_pattern, expected_type=type_hints["filter_pattern"])
            check_type(argname="argument distribution", value=distribution, expected_type=type_hints["distribution"])
            check_type(argname="argument filter_name", value=filter_name, expected_type=type_hints["filter_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
            "filter_pattern": filter_pattern,
        }
        if distribution is not None:
            self._values["distribution"] = distribution
        if filter_name is not None:
            self._values["filter_name"] = filter_name

    @builtins.property
    def destination(self) -> ILogSubscriptionDestination:
        '''The destination to send the filtered events to.

        For example, a Kinesis stream or a Lambda function.
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(ILogSubscriptionDestination, result)

    @builtins.property
    def filter_pattern(self) -> IFilterPattern:
        '''Log events matching this pattern will be sent to the destination.'''
        result = self._values.get("filter_pattern")
        assert result is not None, "Required property 'filter_pattern' is missing"
        return typing.cast(IFilterPattern, result)

    @builtins.property
    def distribution(self) -> typing.Optional[Distribution]:
        '''The method used to distribute log data to the destination.

        This property can only be used with KinesisDestination.

        :default: Distribution.BY_LOG_STREAM
        '''
        result = self._values.get("distribution")
        return typing.cast(typing.Optional[Distribution], result)

    @builtins.property
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subscription filter.

        :default: Automatically generated
        '''
        result = self._values.get("filter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionFilterOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.SubscriptionFilterProps",
    jsii_struct_bases=[SubscriptionFilterOptions],
    name_mapping={
        "destination": "destination",
        "filter_pattern": "filterPattern",
        "distribution": "distribution",
        "filter_name": "filterName",
        "log_group": "logGroup",
    },
)
class SubscriptionFilterProps(SubscriptionFilterOptions):
    def __init__(
        self,
        *,
        destination: ILogSubscriptionDestination,
        filter_pattern: IFilterPattern,
        distribution: typing.Optional[Distribution] = None,
        filter_name: typing.Optional[builtins.str] = None,
        log_group: ILogGroup,
    ) -> None:
        '''Properties for a SubscriptionFilter.

        :param destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
        :param filter_pattern: Log events matching this pattern will be sent to the destination.
        :param distribution: The method used to distribute log data to the destination. This property can only be used with KinesisDestination. Default: Distribution.BY_LOG_STREAM
        :param filter_name: The name of the subscription filter. Default: Automatically generated
        :param log_group: The log group to create the subscription on.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_logs_destinations as destinations
            
            # fn: lambda.Function
            # log_group: logs.LogGroup
            
            
            logs.SubscriptionFilter(self, "Subscription",
                log_group=log_group,
                destination=destinations.LambdaDestination(fn),
                filter_pattern=logs.FilterPattern.all_terms("ERROR", "MainThread"),
                filter_name="ErrorInMainThread"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb936c8dd6a8ee03c9e8f4ffbe991c19b4b98648bbdd91f03367a058de3e8268)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument filter_pattern", value=filter_pattern, expected_type=type_hints["filter_pattern"])
            check_type(argname="argument distribution", value=distribution, expected_type=type_hints["distribution"])
            check_type(argname="argument filter_name", value=filter_name, expected_type=type_hints["filter_name"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
            "filter_pattern": filter_pattern,
            "log_group": log_group,
        }
        if distribution is not None:
            self._values["distribution"] = distribution
        if filter_name is not None:
            self._values["filter_name"] = filter_name

    @builtins.property
    def destination(self) -> ILogSubscriptionDestination:
        '''The destination to send the filtered events to.

        For example, a Kinesis stream or a Lambda function.
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(ILogSubscriptionDestination, result)

    @builtins.property
    def filter_pattern(self) -> IFilterPattern:
        '''Log events matching this pattern will be sent to the destination.'''
        result = self._values.get("filter_pattern")
        assert result is not None, "Required property 'filter_pattern' is missing"
        return typing.cast(IFilterPattern, result)

    @builtins.property
    def distribution(self) -> typing.Optional[Distribution]:
        '''The method used to distribute log data to the destination.

        This property can only be used with KinesisDestination.

        :default: Distribution.BY_LOG_STREAM
        '''
        result = self._values.get("distribution")
        return typing.cast(typing.Optional[Distribution], result)

    @builtins.property
    def filter_name(self) -> typing.Optional[builtins.str]:
        '''The name of the subscription filter.

        :default: Automatically generated
        '''
        result = self._values.get("filter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_group(self) -> ILogGroup:
        '''The log group to create the subscription on.'''
        result = self._values.get("log_group")
        assert result is not None, "Required property 'log_group' is missing"
        return typing.cast(ILogGroup, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.SubstituteStringEntryProperty",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "source": "source", "to": "to"},
)
class SubstituteStringEntryProperty:
    def __init__(
        self,
        *,
        from_: builtins.str,
        source: builtins.str,
        to: builtins.str,
    ) -> None:
        '''This object defines one log field key that will be replaced using the substituteString processor.

        :param from_: The regular expression string to be replaced.
        :param source: The key to modify.
        :param to: The string to be substituted for each match of from.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            substitute_string_entry_property = logs.SubstituteStringEntryProperty(
                from="from",
                source="source",
                to="to"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89f40c023205edf817c714afaa5f89f95fb9d2d1229d815efc0d03dcd3c928a9)
            check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument to", value=to, expected_type=type_hints["to"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "from_": from_,
            "source": source,
            "to": to,
        }

    @builtins.property
    def from_(self) -> builtins.str:
        '''The regular expression string to be replaced.'''
        result = self._values.get("from_")
        assert result is not None, "Required property 'from_' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''The key to modify.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def to(self) -> builtins.str:
        '''The string to be substituted for each match of from.'''
        result = self._values.get("to")
        assert result is not None, "Required property 'to' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubstituteStringEntryProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.SubstituteStringProperty",
    jsii_struct_bases=[],
    name_mapping={"entries": "entries"},
)
class SubstituteStringProperty:
    def __init__(
        self,
        *,
        entries: typing.Sequence[typing.Union[SubstituteStringEntryProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''This processor matches a key's value against a regular expression and replaces all matches with a replacement string.

        For more information about this processor including examples, see substituteString in the CloudWatch Logs User Guide.

        :param entries: An array of objects, where each object contains information about one key to match and replace.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            substitute_string_property = logs.SubstituteStringProperty(
                entries=[logs.SubstituteStringEntryProperty(
                    from="from",
                    source="source",
                    to="to"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89623f0009740e6c093be416eda3b9572559011ccffe3a9d8d28a3cbd2683a71)
            check_type(argname="argument entries", value=entries, expected_type=type_hints["entries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entries": entries,
        }

    @builtins.property
    def entries(self) -> typing.List[SubstituteStringEntryProperty]:
        '''An array of objects, where each object contains information about one key to match and replace.'''
        result = self._values.get("entries")
        assert result is not None, "Required property 'entries' is missing"
        return typing.cast(typing.List[SubstituteStringEntryProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubstituteStringProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Transformer(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.Transformer",
):
    '''Represent the L2 construct for the AWS::Logs::Transformer CloudFormation resource.

    :exampleMetadata: infused

    Example::

        # Create a log group
        log_group = logs.LogGroup(self, "MyLogGroup")
        
        # Create a JSON parser processor
        json_parser = logs.ParserProcessor(
            type=logs.ParserProcessorType.JSON
        )
        
        # Create a processor to add keys
        add_keys_processor = logs.JsonMutatorProcessor(
            type=logs.JsonMutatorType.ADD_KEYS,
            add_keys_options=logs.AddKeysProperty(
                entries=[logs.AddKeyEntryProperty(
                    key="metadata.transformed_in",
                    value="CloudWatchLogs"
                )]
            )
        )
        
        # Create a transformer with these processors
        logs.Transformer(self, "Transformer",
            transformer_name="MyTransformer",
            log_group=log_group,
            transformer_config=[json_parser, add_keys_processor]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        log_group: ILogGroup,
        transformer_config: typing.Sequence[IProcessor],
        transformer_name: builtins.str,
    ) -> None:
        '''The Transformer L2 construct that represents AWS::Logs::Transformer CFN resource.

        :param scope: -
        :param id: -
        :param log_group: Existing log group that you want to associate with this transformer.
        :param transformer_config: List of processors in a transformer.
        :param transformer_name: Name of the transformer.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15229fc0be2da1cdc000826d3fc7c0eb70960587299f27c938a1fd71c98c1d2d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TransformerProps(
            log_group=log_group,
            transformer_config=transformer_config,
            transformer_name=transformer_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''The property injection ID for this resource class.

        Used by the CDK frameworks for managing resource lifecycle.
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.TransformerOptions",
    jsii_struct_bases=[],
    name_mapping={
        "transformer_config": "transformerConfig",
        "transformer_name": "transformerName",
    },
)
class TransformerOptions:
    def __init__(
        self,
        *,
        transformer_config: typing.Sequence[IProcessor],
        transformer_name: builtins.str,
    ) -> None:
        '''Properties for Transformer created from LogGroup.

        :param transformer_config: List of processors in a transformer.
        :param transformer_name: Name of the transformer.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            # processor: logs.IProcessor
            
            transformer_options = logs.TransformerOptions(
                transformer_config=[processor],
                transformer_name="transformerName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fb14deb68ad2a391c38083a4ab9599103e7918f73904352784a6fbf0fa0ad15)
            check_type(argname="argument transformer_config", value=transformer_config, expected_type=type_hints["transformer_config"])
            check_type(argname="argument transformer_name", value=transformer_name, expected_type=type_hints["transformer_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "transformer_config": transformer_config,
            "transformer_name": transformer_name,
        }

    @builtins.property
    def transformer_config(self) -> typing.List[IProcessor]:
        '''List of processors in a transformer.'''
        result = self._values.get("transformer_config")
        assert result is not None, "Required property 'transformer_config' is missing"
        return typing.cast(typing.List[IProcessor], result)

    @builtins.property
    def transformer_name(self) -> builtins.str:
        '''Name of the transformer.'''
        result = self._values.get("transformer_name")
        assert result is not None, "Required property 'transformer_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransformerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.TransformerProps",
    jsii_struct_bases=[],
    name_mapping={
        "log_group": "logGroup",
        "transformer_config": "transformerConfig",
        "transformer_name": "transformerName",
    },
)
class TransformerProps:
    def __init__(
        self,
        *,
        log_group: ILogGroup,
        transformer_config: typing.Sequence[IProcessor],
        transformer_name: builtins.str,
    ) -> None:
        '''The Resource properties for AWS::Logs::Transformer resource.

        This
        interface defines all configuration options for the CfnTransformer construct.

        :param log_group: Existing log group that you want to associate with this transformer.
        :param transformer_config: List of processors in a transformer.
        :param transformer_name: Name of the transformer.

        :exampleMetadata: infused

        Example::

            # Create a log group
            log_group = logs.LogGroup(self, "MyLogGroup")
            
            # Create a JSON parser processor
            json_parser = logs.ParserProcessor(
                type=logs.ParserProcessorType.JSON
            )
            
            # Create a processor to add keys
            add_keys_processor = logs.JsonMutatorProcessor(
                type=logs.JsonMutatorType.ADD_KEYS,
                add_keys_options=logs.AddKeysProperty(
                    entries=[logs.AddKeyEntryProperty(
                        key="metadata.transformed_in",
                        value="CloudWatchLogs"
                    )]
                )
            )
            
            # Create a transformer with these processors
            logs.Transformer(self, "Transformer",
                transformer_name="MyTransformer",
                log_group=log_group,
                transformer_config=[json_parser, add_keys_processor]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c44d5878511fc89516420ebac8e669a5edc49cf01182e21ae66e8d8f47e3df4b)
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            check_type(argname="argument transformer_config", value=transformer_config, expected_type=type_hints["transformer_config"])
            check_type(argname="argument transformer_name", value=transformer_name, expected_type=type_hints["transformer_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_group": log_group,
            "transformer_config": transformer_config,
            "transformer_name": transformer_name,
        }

    @builtins.property
    def log_group(self) -> ILogGroup:
        '''Existing log group that you want to associate with this transformer.'''
        result = self._values.get("log_group")
        assert result is not None, "Required property 'log_group' is missing"
        return typing.cast(ILogGroup, result)

    @builtins.property
    def transformer_config(self) -> typing.List[IProcessor]:
        '''List of processors in a transformer.'''
        result = self._values.get("transformer_config")
        assert result is not None, "Required property 'transformer_config' is missing"
        return typing.cast(typing.List[IProcessor], result)

    @builtins.property
    def transformer_name(self) -> builtins.str:
        '''Name of the transformer.'''
        result = self._values.get("transformer_name")
        assert result is not None, "Required property 'transformer_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransformerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.TypeConverterEntryProperty",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "type": "type"},
)
class TypeConverterEntryProperty:
    def __init__(self, *, key: builtins.str, type: "TypeConverterType") -> None:
        '''This object defines one value type that will be converted using the typeConverter processor.

        :param key: The key with the value that is to be converted to a different type.
        :param type: The data type to convert the field value to.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            type_converter_entry_property = logs.TypeConverterEntryProperty(
                key="key",
                type=logs.TypeConverterType.BOOLEAN
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0be65a0bf0645c5557fac9906c47d395393b2aea1d3d5f1f33ebd91b9f247a77)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "type": type,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''The key with the value that is to be converted to a different type.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> "TypeConverterType":
        '''The data type to convert the field value to.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("TypeConverterType", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TypeConverterEntryProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.TypeConverterProperty",
    jsii_struct_bases=[],
    name_mapping={"entries": "entries"},
)
class TypeConverterProperty:
    def __init__(
        self,
        *,
        entries: typing.Sequence[typing.Union[TypeConverterEntryProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Use this processor to convert a value type associated with the specified key to the specified type.

        It's a casting processor that changes the types of the specified fields.
        For more information about this processor including examples, see typeConverter in the CloudWatch Logs User Guide.

        :param entries: An array of TypeConverterEntry objects, where each object contains information about one field to change the type of.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            type_converter_property = logs.TypeConverterProperty(
                entries=[logs.TypeConverterEntryProperty(
                    key="key",
                    type=logs.TypeConverterType.BOOLEAN
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c16a2fb884c15b78b564dcb7d166ce474c411638d2de9600531d96d93f88910)
            check_type(argname="argument entries", value=entries, expected_type=type_hints["entries"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entries": entries,
        }

    @builtins.property
    def entries(self) -> typing.List[TypeConverterEntryProperty]:
        '''An array of TypeConverterEntry objects, where each object contains information about one field to change the type of.'''
        result = self._values.get("entries")
        assert result is not None, "Required property 'entries' is missing"
        return typing.cast(typing.List[TypeConverterEntryProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TypeConverterProperty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.TypeConverterType")
class TypeConverterType(enum.Enum):
    '''Valid data types for type conversion in the TypeConverter processor.

    Used to specify the target data type for field conversion.
    '''

    BOOLEAN = "BOOLEAN"
    '''Convert value to boolean type.'''
    INTEGER = "INTEGER"
    '''Convert value to integer type.'''
    DOUBLE = "DOUBLE"
    '''Convert value to double (floating point) type.'''
    STRING = "STRING"
    '''Convert value to string type.'''


@jsii.implements(IProcessor)
class VendedLogParser(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.VendedLogParser",
):
    '''Parser processor for AWS vended logs.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        vended_log_parser = logs.VendedLogParser(
            log_type=logs.VendedLogType.CLOUDFRONT,
        
            # the properties below are optional
            source="source"
        )
    '''

    def __init__(
        self,
        *,
        log_type: "VendedLogType",
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Creates a new vended log parser processor.

        :param log_type: The type of AWS vended log to parse.
        :param source: Source field to parse.
        '''
        props = VendedLogParserProps(log_type=log_type, source=source)

        jsii.create(self.__class__, self, [props])

    @builtins.property
    @jsii.member(jsii_name="logType")
    def log_type(self) -> "VendedLogType":
        '''The type of AWS vended log.'''
        return typing.cast("VendedLogType", jsii.get(self, "logType"))

    @log_type.setter
    def log_type(self, value: "VendedLogType") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcaaf986081bc45f10c5e81d15b15c27b04392687542820b3ca2da24add5605d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logType", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs.VendedLogParserProps",
    jsii_struct_bases=[BaseProcessorProps],
    name_mapping={"log_type": "logType", "source": "source"},
)
class VendedLogParserProps(BaseProcessorProps):
    def __init__(
        self,
        *,
        log_type: "VendedLogType",
        source: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for creating AWS vended log parsers.

        :param log_type: The type of AWS vended log to parse.
        :param source: Source field to parse.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs as logs
            
            vended_log_parser_props = logs.VendedLogParserProps(
                log_type=logs.VendedLogType.CLOUDFRONT,
            
                # the properties below are optional
                source="source"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e317a7d0a3ab35fb963ce2b635f89cd9aabf90244799cafa76755dd69ebdbbe)
            check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_type": log_type,
        }
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def log_type(self) -> "VendedLogType":
        '''The type of AWS vended log to parse.'''
        result = self._values.get("log_type")
        assert result is not None, "Required property 'log_type' is missing"
        return typing.cast("VendedLogType", result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Source field to parse.

        :message: true
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VendedLogParserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_logs.VendedLogType")
class VendedLogType(enum.Enum):
    '''Types of AWS vended logs with built-in parsers.

    AWS provides specialized parsers for common log formats produced by various AWS services.
    '''

    CLOUDFRONT = "CLOUDFRONT"
    '''Parse CloudFront logs.'''
    VPC = "VPC"
    '''Parse VPC flow logs.'''
    WAF = "WAF"
    '''Parse AWS WAF logs.'''
    ROUTE53 = "ROUTE53"
    '''Parse Route 53 logs.'''
    POSTGRES = "POSTGRES"
    '''Parse PostgreSQL logs.'''


@jsii.implements(ILogSubscriptionDestination)
class CrossAccountDestination(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CrossAccountDestination",
):
    '''A new CloudWatch Logs Destination for use in cross-account scenarios.

    CrossAccountDestinations are used to subscribe a Kinesis stream in a
    different account to a CloudWatch Subscription.

    Consumers will hardly ever need to use this class. Instead, directly
    subscribe a Kinesis stream using the integration class in the
    ``aws-cdk-lib/aws-logs-destinations`` package; if necessary, a
    ``CrossAccountDestination`` will be created automatically.

    :resource: AWS::Logs::Destination
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        from aws_cdk import aws_logs as logs
        
        # role: iam.Role
        
        cross_account_destination = logs.CrossAccountDestination(self, "MyCrossAccountDestination",
            role=role,
            target_arn="targetArn",
        
            # the properties below are optional
            destination_name="destinationName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        role: _IRole_235f5d8e,
        target_arn: builtins.str,
        destination_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param role: The role to assume that grants permissions to write to 'target'. The role must be assumable by 'logs.{REGION}.amazonaws.com'.
        :param target_arn: The log destination target's ARN.
        :param destination_name: The name of the log destination. Default: Automatically generated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f78998ef1421583d87d205e0c66668e415d3a06be064cfc35682d8884a01ad56)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CrossAccountDestinationProps(
            role=role, target_arn=target_arn, destination_name=destination_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: _PolicyStatement_0fe33853) -> None:
        '''
        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a3a6f7c79a2740b0e52fcc48d64fb4e96cfdc2abd91649f986c7d67b9d5ee67)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addToPolicy", [statement]))

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        _source_log_group: ILogGroup,
    ) -> LogSubscriptionDestinationConfig:
        '''Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        :param _scope: -
        :param _source_log_group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__901846e19d9ba5beee9ef4784401b7413f0b32b2034ea5700b5fa8a30a1c0394)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument _source_log_group", value=_source_log_group, expected_type=type_hints["_source_log_group"])
        return typing.cast(LogSubscriptionDestinationConfig, jsii.invoke(self, "bind", [_scope, _source_log_group]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))

    @builtins.property
    @jsii.member(jsii_name="destinationArn")
    def destination_arn(self) -> builtins.str:
        '''The ARN of this CrossAccountDestination object.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "destinationArn"))

    @builtins.property
    @jsii.member(jsii_name="destinationName")
    def destination_name(self) -> builtins.str:
        '''The name of this CrossAccountDestination object.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "destinationName"))

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> _PolicyDocument_3ac34393:
        '''Policy object of this CrossAccountDestination object.'''
        return typing.cast(_PolicyDocument_3ac34393, jsii.get(self, "policyDocument"))


class CustomDataIdentifier(
    DataIdentifier,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.CustomDataIdentifier",
):
    '''A custom data identifier.

    Include a custom data identifier name and regular expression in the JSON policy used to define the data protection policy.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_kinesisfirehose as firehose
        
        
        log_group_destination = logs.LogGroup(self, "LogGroupLambdaAudit",
            log_group_name="auditDestinationForCDK"
        )
        
        bucket = s3.Bucket(self, "audit-bucket")
        s3_destination = firehose.S3Bucket(bucket)
        
        delivery_stream = firehose.DeliveryStream(self, "Delivery Stream",
            destination=s3_destination
        )
        
        data_protection_policy = logs.DataProtectionPolicy(
            name="data protection policy",
            description="policy description",
            identifiers=[logs.DataIdentifier.DRIVERSLICENSE_US,  # managed data identifier
                logs.DataIdentifier("EmailAddress"),  # forward compatibility for new managed data identifiers
                logs.CustomDataIdentifier("EmployeeId", "EmployeeId-\\d{9}")
            ],  # custom data identifier
            log_group_audit_destination=log_group_destination,
            s3_bucket_audit_destination=bucket,
            delivery_stream_name_audit_destination=delivery_stream.delivery_stream_name
        )
        
        logs.LogGroup(self, "LogGroupLambda",
            log_group_name="cdkIntegLogGroup",
            data_protection_policy=data_protection_policy
        )
    '''

    def __init__(self, name: builtins.str, regex: builtins.str) -> None:
        '''Create a custom data identifier.

        :param name: - the name of the custom data identifier. This cannot share the same name as a managed data identifier.
        :param regex: - the regular expression to detect and mask log events for.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8962f986463b4e81629495838f26c8990feeca56061597cb66e94771b4cfb79d)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
        jsii.create(self.__class__, self, [name, regex])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''String representation of a CustomDataIdentifier.

        :return: the name and RegEx of the custom data identifier
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''- the name of the custom data identifier.

        This cannot share the same name as a managed data identifier.
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="regex")
    def regex(self) -> builtins.str:
        '''- the regular expression to detect and mask log events for.'''
        return typing.cast(builtins.str, jsii.get(self, "regex"))


@jsii.implements(IProcessor)
class DataConverterProcessor(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs.DataConverterProcessor",
):
    '''Processor for data conversion operations.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_logs as logs
        
        data_converter_processor = logs.DataConverterProcessor(
            type=logs.DataConverterType.TYPE_CONVERTER,
        
            # the properties below are optional
            date_time_converter_options=logs.DateTimeConverterProperty(
                locale="locale",
                match_patterns=["matchPatterns"],
                source="source",
                target="target",
        
                # the properties below are optional
                source_timezone="sourceTimezone",
                target_format="targetFormat",
                target_timezone="targetTimezone"
            ),
            type_converter_options=logs.TypeConverterProperty(
                entries=[logs.TypeConverterEntryProperty(
                    key="key",
                    type=logs.TypeConverterType.BOOLEAN
                )]
            )
        )
    '''

    def __init__(
        self,
        *,
        type: DataConverterType,
        date_time_converter_options: typing.Optional[typing.Union[DateTimeConverterProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        type_converter_options: typing.Optional[typing.Union[TypeConverterProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Creates a new data converter processor.

        :param type: The type of data conversion operation.
        :param date_time_converter_options: Options for datetime conversion. Required when type is DATETIME_CONVERTER. Default: - No date time converter processor is created if not set
        :param type_converter_options: Options for type conversion. Required when type is TYPE_CONVERTER. Default: - No type convertor processor is created if not set
        '''
        props = DataConverterProps(
            type=type,
            date_time_converter_options=date_time_converter_options,
            type_converter_options=type_converter_options,
        )

        jsii.create(self.__class__, self, [props])

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> DataConverterType:
        '''The type of data conversion operation.'''
        return typing.cast(DataConverterType, jsii.get(self, "type"))

    @type.setter
    def type(self, value: DataConverterType) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bea2654ebc88ef45acb691425a17897e52198e8f268040b952558fccd601704e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "AddKeyEntryProperty",
    "AddKeysProperty",
    "BaseProcessorProps",
    "CfnAccountPolicy",
    "CfnAccountPolicyProps",
    "CfnDelivery",
    "CfnDeliveryDestination",
    "CfnDeliveryDestinationProps",
    "CfnDeliveryProps",
    "CfnDeliverySource",
    "CfnDeliverySourceProps",
    "CfnDestination",
    "CfnDestinationProps",
    "CfnIntegration",
    "CfnIntegrationProps",
    "CfnLogAnomalyDetector",
    "CfnLogAnomalyDetectorProps",
    "CfnLogGroup",
    "CfnLogGroupProps",
    "CfnLogStream",
    "CfnLogStreamProps",
    "CfnMetricFilter",
    "CfnMetricFilterProps",
    "CfnQueryDefinition",
    "CfnQueryDefinitionProps",
    "CfnResourcePolicy",
    "CfnResourcePolicyProps",
    "CfnSubscriptionFilter",
    "CfnSubscriptionFilterProps",
    "CfnTransformer",
    "CfnTransformerProps",
    "ColumnRestriction",
    "CopyValueEntryProperty",
    "CopyValueProperty",
    "CrossAccountDestination",
    "CrossAccountDestinationProps",
    "CsvProperty",
    "CustomDataIdentifier",
    "DataConverterProcessor",
    "DataConverterProps",
    "DataConverterType",
    "DataIdentifier",
    "DataProtectionPolicy",
    "DataProtectionPolicyProps",
    "DateTimeConverterProperty",
    "DateTimeFormat",
    "DelimiterCharacter",
    "Distribution",
    "FieldIndexPolicy",
    "FieldIndexPolicyProps",
    "FilterPattern",
    "GrokProperty",
    "IFilterPattern",
    "ILogGroup",
    "ILogStream",
    "ILogSubscriptionDestination",
    "IProcessor",
    "JsonMutatorProcessor",
    "JsonMutatorProps",
    "JsonMutatorType",
    "JsonPattern",
    "KeyValueDelimiter",
    "KeyValuePairDelimiter",
    "ListToMapProperty",
    "LogGroup",
    "LogGroupClass",
    "LogGroupProps",
    "LogRetention",
    "LogRetentionProps",
    "LogRetentionRetryOptions",
    "LogStream",
    "LogStreamProps",
    "LogSubscriptionDestinationConfig",
    "MetricFilter",
    "MetricFilterOptions",
    "MetricFilterProps",
    "MoveKeyEntryProperty",
    "MoveKeysProperty",
    "OCSFSourceType",
    "OCSFVersion",
    "ParseJSONProperty",
    "ParseKeyValueProperty",
    "ParseToOCSFProperty",
    "ParserProcessor",
    "ParserProcessorProps",
    "ParserProcessorType",
    "ProcessorDeleteKeysProperty",
    "QueryDefinition",
    "QueryDefinitionProps",
    "QueryString",
    "QueryStringProps",
    "QuoteCharacter",
    "RenameKeyEntryProperty",
    "RenameKeysProperty",
    "ResourcePolicy",
    "ResourcePolicyProps",
    "RetentionDays",
    "SpaceDelimitedTextPattern",
    "SplitStringEntryProperty",
    "SplitStringProperty",
    "StreamOptions",
    "StringMutatorProcessor",
    "StringMutatorProps",
    "StringMutatorType",
    "SubscriptionFilter",
    "SubscriptionFilterOptions",
    "SubscriptionFilterProps",
    "SubstituteStringEntryProperty",
    "SubstituteStringProperty",
    "Transformer",
    "TransformerOptions",
    "TransformerProps",
    "TypeConverterEntryProperty",
    "TypeConverterProperty",
    "TypeConverterType",
    "VendedLogParser",
    "VendedLogParserProps",
    "VendedLogType",
]

publication.publish()

def _typecheckingstub__8699e0d43c18a23430a2882c1d81b6da80014a083961d49ed805738cd51f592a(
    *,
    key: builtins.str,
    value: builtins.str,
    overwrite_if_exists: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1836386a927cf6c05c8ee3f32e141f2a818ce87d4aba162406325e50620c0c9b(
    *,
    entries: typing.Sequence[typing.Union[AddKeyEntryProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__125a77dd271c26d92d39f5fc5e47e588668423ade67a45afc5817e4df1ee8dd0(
    scope_: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_document: builtins.str,
    policy_name: builtins.str,
    policy_type: builtins.str,
    scope: typing.Optional[builtins.str] = None,
    selection_criteria: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebfd4fb8cf24056dd4dacb27f135740e6f55ee47d01767451cebf21c25f0837a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fa52c452e9fe5605a874b3dd89e31ad16dc4f246300b4319af792307b4ae876(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c653a261ed47c5ebab7b21521ba00f1e039f43a3aee30163835cda4b9b741be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a3c39fb59cb9806cbee8cf38c347eab7bc33fee8e2148f96faae887592ab14c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6152ad747f0f8c8124fd42f55dd6679b842c8faa8ef76cc08b3c59d43df9e9c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a2b34c27c4f47efc3559774d8625b4374c145ac113ac7b65b32dbafd795a627(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a0aa0c45a0d208ef1b05bb6d298b1a3b8a6a93293ddc0c629f797b5ea4fb8a3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e40dcebab5dfdd5fd816fda98a9c4e710aa8bc28c8bbd574a9451defb6d0d66(
    *,
    policy_document: builtins.str,
    policy_name: builtins.str,
    policy_type: builtins.str,
    scope: typing.Optional[builtins.str] = None,
    selection_criteria: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9ab4424636fed5b3c6cadfbae9a75acc19c7a49cc86eb71fbcb77cb343b3f59(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    delivery_destination_arn: builtins.str,
    delivery_source_name: builtins.str,
    field_delimiter: typing.Optional[builtins.str] = None,
    record_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    s3_enable_hive_compatible_path: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    s3_suffix_path: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99f7221e967e1cfd1a9552bf514bfffa267c72d3a082920609edd6fcf762914f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62e336df1727ca28efe4ebc70d80806e2800addcc81668613e49206280c6b492(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a50c8581f8db077c41c10f79c036d162827109bb24b65891dfc33cf502c6e78b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4ec9d68f7c2d7007a4afa644bcc4bc69a917cf74e5a3f6a6be17358ae262e09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bd08694e6454ec1e8a7caa24ed3783c9708c421fe32b6506c73b7844a9734e3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c57c7d1aa190b754df4f2f3cfe02326fa2d33aa925f4476a48f1ad8480bd7c58(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__883ead422cb217bb6d7d85bba609b57a45ff8726f927790c48273417346f9faa(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb1b6261fa6fe536f7b593af4c257808a0259533f08f144df15cc67bd0293e52(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__000a573f2c99f6b1460750af0c01cc2fc0278bcaf6f21b31ed533ebcf516c233(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b48efa0b7b05ab2d9f1417a0b1e0cd7f28039825d1520fe16f6f8dca79d8d4fc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    delivery_destination_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryDestination.DestinationPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    destination_resource_arn: typing.Optional[builtins.str] = None,
    output_format: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2db73754a49fde6308de1010ac96a197f9965c58bd5d9e7fc31cc846e853ab8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5af9dd3e40ccb4916d015c0cc40c6ae0c7210e9132f0dbf357f2e527552a5fa8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fdc8a995b69cc816b4deffcde2adde43de71476430695742e74896d1e844841(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__318bc8d97cf7e7f129b83631444b5c478bd65a7e80725c9b3be7e3cc4a600b05(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryDestination.DestinationPolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__831ddd5c5bd5a90cbf966f9a711dcab92a21ca60debf21106dbe34c3b30fce44(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72800638f30c315cbdfab3a9dcdd94e12b62e350f96e85c9fbc816f012ede070(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4f5227f043e0a8609b64c4a174886ba54b2825ada7e9a1dffe8fd35487fa5af(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__476eb70b6b82939807d3600d63a802f799886d0c7cc23550944471a71b16233e(
    *,
    delivery_destination_name: typing.Optional[builtins.str] = None,
    delivery_destination_policy: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53bbf04ee2b4b7e83a98258d41a973972fae20f7537731a0fbcda3e7c5f46c1c(
    *,
    name: builtins.str,
    delivery_destination_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryDestination.DestinationPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    destination_resource_arn: typing.Optional[builtins.str] = None,
    output_format: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b538310aec1f59690c78c4bf171f8ecae0a76d174388a130cf6154213614117c(
    *,
    delivery_destination_arn: builtins.str,
    delivery_source_name: builtins.str,
    field_delimiter: typing.Optional[builtins.str] = None,
    record_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    s3_enable_hive_compatible_path: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    s3_suffix_path: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ab0297a02d5ec18fef514a89fa2743d7fb62f4e7b1fd892c1bd7ee901ef99c4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    log_type: typing.Optional[builtins.str] = None,
    resource_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7c152d845b9eb6bc70785b4e0e32dec0dce7f287b55eaf85acdcea613be11d3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c67b6491f677638c6c1cb36e66c12c782c6221d3f036515d784e31181d6603e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46ee2cc4bb6930c90c749220d8d5170a97f90cc490afa3d4564c90e7f6d9a79a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fafd9abe15a418ef0eafe4df0701cb0c5bd2181041f5fd30e006939ddedc10d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd0e55d64bccd98b6356d6f16e4ae7dc18393fe37b5ae94cd2dde9e7ecd15097(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c56ccd3093218052492eee7c66b0cf9e8156a37606a1c8a35551c977444ed97e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bd979785c6ee68de5cc10f2dec7ca694c3327ec47aa59e93668d849404cd7df(
    *,
    name: builtins.str,
    log_type: typing.Optional[builtins.str] = None,
    resource_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44e37c6c2772abdacfbcd01df5c5418fca8937b435df3890a5a5cb3437b9bab5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination_name: builtins.str,
    role_arn: builtins.str,
    target_arn: builtins.str,
    destination_policy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96cb24255178be4bad07466bab77f2ccec3a7bf2f35acfe8bf018152eb28bb7e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f9dedbbaf433f224026d220b3fb36706410370925367aeada047e8858f484ac(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5158605e72fe974296ad671ff50605f46d8a94d78d818e766756296254fa5758(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__908d4772c2472f7ef1a59ee7f794734117f87a8908ceda3def1feff5578217c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90e291c0d065725c0ff62d5808258937a46aa7e3d79209721b2ffdb32fc0db6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b0569830af0faea41307b4fd071b0ef86a0b49f3514f3050bfa53cc72d3ddee(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e2da427145601b64454ab268bb3be33f3c089ff53e25e2b9a66fd51a6d385db(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faf2f9f88fd096e79a2445aab3efdc3a85509df7ba06ffc305c9faf39fa77a56(
    *,
    destination_name: builtins.str,
    role_arn: builtins.str,
    target_arn: builtins.str,
    destination_policy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d25ae5aedb6cfa0b6f3765f329d81581fbcd3ff378cc552133e5d0fdd6d99ff(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    integration_name: builtins.str,
    integration_type: builtins.str,
    resource_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ResourceConfigProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4444f0ef7fd9d069bfce488a66baa068bb1b87a18239a8510d4cfa183a652a0b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed5813f598ecc3cd5a557ae647d3d2e9b8b9b4d638ea5a9a5ac68d4ef1281007(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c789029fae3c40d804160d555fcd880577fad4f74f1191f7b52562964594751e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e7ea06be2423b6609ab61f003f306246fb58e590842d8ee6d0b889e4e4d1bce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e70a870af94762893ff1564b472074d1ad1ea7d25c502af37606c4cce91a529a(
    value: typing.Union[_IResolvable_da3f097b, CfnIntegration.ResourceConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c674a258b3e224416fabb1fbddb9ff6620ca73f500c2c766f439b1ff2d42221(
    *,
    dashboard_viewer_principals: typing.Sequence[builtins.str],
    data_source_role_arn: builtins.str,
    application_arn: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    retention_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0dad8c7beab9d66f0a9d16731a931e58e75731a8cb6142e5ecd221eea5f4bab(
    *,
    open_search_resource_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.OpenSearchResourceConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3fde65aad1184bb5a5e5498b7fec6844a978b48eb0a9d57607f44ec0c65fc3a(
    *,
    integration_name: builtins.str,
    integration_type: builtins.str,
    resource_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ResourceConfigProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d152ea0809d051d39430771f957ddf1edb48a2711f5f1dac144632c4025106f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account_id: typing.Optional[builtins.str] = None,
    anomaly_visibility_time: typing.Optional[jsii.Number] = None,
    detector_name: typing.Optional[builtins.str] = None,
    evaluation_frequency: typing.Optional[builtins.str] = None,
    filter_pattern: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_group_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6002d02f1da3550c2407847cbf1810c63c4cb68d5609b2890cad4cb306056324(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8a73ba8c4ce52064896eb40ab1c6e467c30f9682ff3ef6376d101fbbce16202(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7091ec3c1c0b4552340a41d082b9a8b05727396563c6735b32c808e4f4a9070(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4568b027e5608ed08e1434d2fc055c05356712bc434041b26212701c5881dd15(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e029b96055f74ee8a1506c21562c10f01dc81a628d9217edc344d32c509e4c01(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a18b33d5cf65ad2b2c4c21d6c527f99b8ac41d21d5b6357d7bda666a78e5b05(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6022589a1d3385b97bbf672ecb067e6569c73966e3009ac7e9e5f211d37f740e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d7970b3814e2fb4a7bdf38b8f455da8249766c8616b4813e2bfe621651215a8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5113cbbd1e159d109496838f7c2de7bb9765d5d8f294094b0b933c1193e2331(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73c93feb7d3595f49f16b50d5ef5c97b24e9aba98c12935428a8e2019fd66a2b(
    *,
    account_id: typing.Optional[builtins.str] = None,
    anomaly_visibility_time: typing.Optional[jsii.Number] = None,
    detector_name: typing.Optional[builtins.str] = None,
    evaluation_frequency: typing.Optional[builtins.str] = None,
    filter_pattern: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_group_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e283e76ec168d67513d106f9413697672f161b29f03fa9b13486e96b13319c0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_protection_policy: typing.Any = None,
    field_index_policies: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_group_class: typing.Optional[builtins.str] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    resource_policy_document: typing.Any = None,
    retention_in_days: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c5bac0ef7ae74529e652cc24b33213b3432954607a3665dd72bd69b68490c7c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__167d66406821a4fe8a6ca05ec99424e7c4abd7946ba6eb30ee37e04443759ddc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__427539e290b46019fba84ec8aa72f953c2d26dfe978de85330819964c3cea37e(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b4f37a255340908d68ce2d6149f1bb01ab5104c15a9b60474e51dde5b10d526(
    value: typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fc22b518f14684135ca2ffa0556628df055b32df3a769085c35ae8ef72d5677(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc12e80d5e08442f63a358d7f964b44915adb40d9341cdbd7ae2bf730d5a0fbf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08bea1f6b59cbce316d19aa0ff5db07ed0da20b04cc322eb41788ce24f8f2d31(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d6853e85debe88051bdf2f6ab68103e166533560e34248419263b9c0f7dd03e(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d977a18b9031aeb9d37e4baf6f3eccb9ebf070ad2e33a30cfba9f69fbaf62408(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ea9a0a37724d334e68ee325d75e901df12c6765b4c229366a1cef4038c07187(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a2ba122502a64b05bea3e56f15389c84f127761b660b1d06de3ea638b95f816(
    *,
    data_protection_policy: typing.Any = None,
    field_index_policies: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_group_class: typing.Optional[builtins.str] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    resource_policy_document: typing.Any = None,
    retention_in_days: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68392ef44019b9b5ee681acb5bd13c481e1cc999bc1f1773e84c70b5a04190b7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    log_group_name: builtins.str,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64fb9d8e354f9197a9998608e06c1be2deb6b929ddb7835470385c91e16d110a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ec4cadc779471f71fa1f1b77d2bda5c706e530b0ead1517f46ec34940fee5da(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28f49c7b712326ca2be5a290a29a4430589b6c15c4da1f34afb773fcc0456112(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e3f8ff96c3dac6c45a8d31d07a3223b27eebb1e1c6aa1676d6cf0cfc0bcacb8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab2d708d8a8c684eb8753554b20ecf7de790ffc112520d594cacb903aff379ea(
    *,
    log_group_name: builtins.str,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaa6a2018a5f10ec1a79f547b81a628d6f434d037b49c5975131bba2d6fd2786(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    filter_pattern: builtins.str,
    log_group_name: builtins.str,
    metric_transformations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricFilter.MetricTransformationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    apply_on_transformed_logs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    filter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa5f65c3d38181c3265e71ca5f37737480594a08405697ef96fc18254e2a9899(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aed2b5842b90369a626b9acdfbfb87dab07b9debcde1b1964b8b0dabb330ea2e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fdc6521987ce3f017024e20e1e0fb59a35415aa424ed169b346a59793c88b73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae16ea786b9d9ed9d5bfe824932074163b1aa6379bed22eb2671f3ed0818bf26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e42e8a9e143351ba28d452f886abff3c46adff74b2c2fc8876dc18aabf51dcba(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMetricFilter.MetricTransformationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ace95a6c73bb2a95ee90d8e4e4ad81a77108a607e59d44e12214965f5ebf9073(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed6515d6733ea675274296cf9952fb0b41bd1778277ae74bde9739d81a205382(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fad5f3c7dec2c3bafa74c42e2398a046d9cc8c861abfac39c6e9e77c2b65b41(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8989e36bc84de1e18d069af1bb22845cf409685cbd8a8fe22cd131474e0d7958(
    *,
    metric_name: builtins.str,
    metric_namespace: builtins.str,
    metric_value: builtins.str,
    default_value: typing.Optional[jsii.Number] = None,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricFilter.DimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__524e2e94ad4843f66081953f516426a1396490f271842ac0c5ca7c7ecb84011e(
    *,
    filter_pattern: builtins.str,
    log_group_name: builtins.str,
    metric_transformations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMetricFilter.MetricTransformationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    apply_on_transformed_logs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    filter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d10075ae036bdf9f4049570cf68ab72c79ee717f007f45628b52d2ea5aa64ae(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    query_string: builtins.str,
    log_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    query_language: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dd626642ab8510fa9005787d00adbbd508a543616e89979ad57ba0be9f38bad(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d445c0915cb40f09b489a0802b2b2b0c035e244acf419b2452990fd8568900fe(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a970de5992ab8622f5a1c04c70c2066cfaee94719e9aba8c8edbe863ddcce298(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__005c13f188808f7829e17c5ce9ca7e9ae473e50b0b0b1ed4f95b8e35cfd6a6df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1d922394643a9758400b7e596dd6c6fe61ab7e1fb96d4a93a7061d0e3b5c39d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26eee5ed8d061567be82d404491f5a77b58778884692c8fbe2cf1ded06c91cd9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd7180e50961abf6b838dfc21ba186cc5b2c551eae8357613767f891abe51780(
    *,
    name: builtins.str,
    query_string: builtins.str,
    log_group_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    query_language: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96eb8f500492c7ddcaba9f292d2aa1c488941affca3b4911cd4ce9636c1ce721(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_document: builtins.str,
    policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a2e3f9cc2e418bf4cc4f8f63fc54eed1907f2c1b38483cc8c59d2f8b653c69f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94bd685f258ef991a46514a1b4f58ba0b0bf9314fc8055746b8652c965857253(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fd3f538cb966d97639dd18283329cf7c5f581a2f069d6d37e7cd0ab5cedb7fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de9476941a8f893fee016885d888db6d17d101f4ad44646ba809adde15261aed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ab184a479fd32db068d45168ec1b6bf45cf1a4a3d64847b519a088388c84df8(
    *,
    policy_document: builtins.str,
    policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c7a154450656ee0f7e524d596c7e140faad893a71a7c8b9b8a85fe730a1dcf9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination_arn: builtins.str,
    filter_pattern: builtins.str,
    log_group_name: builtins.str,
    apply_on_transformed_logs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    distribution: typing.Optional[builtins.str] = None,
    filter_name: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd7a0e99337509280da552b557b613a8fcb858acf9e84e9aacbe572366bca99(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c7e4c15a871de67a808634e0ce4138af489acd8a95e0b0e5e5cb1829aa66805(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcf92dedad133b23741e31710f66784d3728a1a96f5d9b514b8a80f012d7b84c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5af0335707946ab6b7311049c978104cfb68f9d36688e1bf25585706ebcbb08a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa4dbdd67c0f388eefe38fe86bae9148a44785d56910a1951619c1205e4eb56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9575bfc33fe73bebe8b16e0496334b59edcb3f2b7fbf109199f2fc70d96487c5(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4730d6086a07b6e1f3b3d7251138c936aa909d17834505b0c341ec6b421adf19(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ccf855abfc15a31ed667e6619b6f1711fc4ef753c64ec0b754421d81c8edb75(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cdca0b99d7b39060b314b323073c0a48e25972ff085f24a455a00339addb4ee(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1250ecc947a5eb57e428cd8fedeb9ae0f6da4eb03c22d674fa019a076ee8b507(
    *,
    destination_arn: builtins.str,
    filter_pattern: builtins.str,
    log_group_name: builtins.str,
    apply_on_transformed_logs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    distribution: typing.Optional[builtins.str] = None,
    filter_name: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0c03d4d08bfd70f5af2f86af828209e7341e321bb84773f474ad12623e4f673(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    log_group_identifier: builtins.str,
    transformer_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.ProcessorProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c5843dc7e0596939f9aed5094347614692a37bcb3deec88eef302aa9f4a3949(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19ee38bba53fb110c3d77fa4bcc6fc2150881fe447a82d6fd44edb6f6b793cbb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f753044b1fead2c548a763e25eaaf3b48d20a74b766e774ba28f4389d3b647ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46991b9d950418a62c8d1284c385ff33c88585c1a5b8ba86a023f964716d83c5(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTransformer.ProcessorProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__879568f32dc44bc4801f0d91ac950375c54ad1e240274f3d74b36735a63912cb(
    *,
    key: builtins.str,
    value: builtins.str,
    overwrite_if_exists: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3fc52570a1b3881374a9cb70551ee446a27ce71ba7d9ac9332130f1b362d8d9(
    *,
    entries: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.AddKeyEntryProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__770aa2786aabe822e197169c0efa5a50e7ed836e01b793d89c28592ddf4e8159(
    *,
    source: builtins.str,
    target: builtins.str,
    overwrite_if_exists: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3d4839dece23811375e7ae8c44e802cb44e36138e19c2a7bf162dc3271f26eb(
    *,
    entries: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.CopyValueEntryProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1385464dc0aa2b930428f3a7b360b1e2046ff9ffcef856103ab40799795933d(
    *,
    columns: typing.Optional[typing.Sequence[builtins.str]] = None,
    delimiter: typing.Optional[builtins.str] = None,
    quote_character: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2af961327d1e6181fea10642711cd58b1ba36b3343696caa3884a622b90f1ab2(
    *,
    match_patterns: typing.Sequence[builtins.str],
    source: builtins.str,
    target: builtins.str,
    locale: typing.Optional[builtins.str] = None,
    source_timezone: typing.Optional[builtins.str] = None,
    target_format: typing.Optional[builtins.str] = None,
    target_timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__889df1b9ea69f6af4e4c3b5c3713a2fe9738d592121c1e3fda581dd8eb227e7b(
    *,
    with_keys: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__099136f924dd58199de2c070d0c9c967072f377ef3449d963d69903d6bfb2b15(
    *,
    match: builtins.str,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b34ca3744eb410b795c48cbf2325a84de8b8980ad35f615e5fcf729b3098d007(
    *,
    key: builtins.str,
    source: builtins.str,
    flatten: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    flattened_element: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
    value_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d32b67f5aac5c1b18f4a4d4a4bb442a6cf892d46e66945200fe60ccc5d71c2c7(
    *,
    with_keys: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ff8ce5ccfdd76db0297923b7f4cc2aa11420c3e5ab87b3401e1e4be83c56f3a(
    *,
    source: builtins.str,
    target: builtins.str,
    overwrite_if_exists: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6916994ad9bc82ff8e94137ddfb22219a21c5349390075aac61c70d8daf6eeef(
    *,
    entries: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.MoveKeyEntryProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea8f836c26b6d6931c5db3b778b2cad26fc04ee23f83ad14bafce0cb66a0c5ae(
    *,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__394c2c2eedd7ab4a72bfd587d0d7e1cc8fdb937698e47c61eb614a5cecb1ef74(
    *,
    destination: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed79a8a8bfee98dc8705bad692617a694795f1862e628cdb6f4fbb9624efcd8c(
    *,
    destination: typing.Optional[builtins.str] = None,
    field_delimiter: typing.Optional[builtins.str] = None,
    key_prefix: typing.Optional[builtins.str] = None,
    key_value_delimiter: typing.Optional[builtins.str] = None,
    non_match_value: typing.Optional[builtins.str] = None,
    overwrite_if_exists: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__952e8e660ca1672ad750873df677aa7489259b5396f80da6748f9d792d7e7bf0(
    *,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__658801a998622d7af47eb8512eb68d2858ed8827da8b177c87996a73cda1431c(
    *,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6febe08cc73af735295ba9258de19bd6c4f1b389f2b1e4fd5e0d66977951c589(
    *,
    event_source: builtins.str,
    ocsf_version: builtins.str,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08e824a8839365028da24b6eaa3d4989ea1bda6be8234968a2991fd59b09e4d4(
    *,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b26bfc2a0a2e670d7d7c901f15a99ddaa76f77d049946758f799b74137c6cfd(
    *,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e487fac0bac06039bca1700fdccd6ce85e8e1fbb80d54937d3dbfdb8f5267202(
    *,
    add_keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.AddKeysProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    copy_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.CopyValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    csv: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.CsvProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    date_time_converter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.DateTimeConverterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delete_keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.DeleteKeysProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    grok: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.GrokProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    list_to_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.ListToMapProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lower_case_string: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.LowerCaseStringProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    move_keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.MoveKeysProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parse_cloudfront: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.ParseCloudfrontProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parse_json: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.ParseJSONProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parse_key_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.ParseKeyValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parse_postgres: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.ParsePostgresProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parse_route53: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.ParseRoute53Property, typing.Dict[builtins.str, typing.Any]]]] = None,
    parse_to_ocsf: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.ParseToOCSFProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parse_vpc: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.ParseVPCProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parse_waf: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.ParseWAFProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rename_keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.RenameKeysProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    split_string: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.SplitStringProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    substitute_string: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.SubstituteStringProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    trim_string: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.TrimStringProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    type_converter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.TypeConverterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    upper_case_string: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.UpperCaseStringProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a85b1ee0f4dc04b37555c8dcf6594a9f1494dd85258af0ff01d94ea67e474eb(
    *,
    key: builtins.str,
    rename_to: builtins.str,
    overwrite_if_exists: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90cce6196aaf5dd8168c63be372944c4df28a731ebef948494876ab7bcfe3456(
    *,
    entries: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.RenameKeyEntryProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__263b02ba09218a6ff88ba5eed377f56a72b8e09134a489ef9267e6e6a5faf67d(
    *,
    delimiter: builtins.str,
    source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__552fccafc9e15edea19c4f34ad5e5bf5f20ad80ad4a2596cc08fa01251ecb3fb(
    *,
    entries: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.SplitStringEntryProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f98269160c0c5038977ab2dc5c8938f02bf529b4d2cf342b072783c01286953d(
    *,
    from_: builtins.str,
    source: builtins.str,
    to: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81f76cf00b73242928401fed6e15762b2a6c06efee29159b7934e0f71a3c624f(
    *,
    entries: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.SubstituteStringEntryProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d17872b8cad5d87a29ef7e4340a3141858904086ebef37ac6ec56490ff5b63b(
    *,
    with_keys: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9ac92cdcbb756bea8e1541d9c9004ad6fa1ed1f73a1b4e7b62f9742f67146dd(
    *,
    key: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3816b1190f1a44d3474db3d4b860789dcf8860b70a135dc25eabc95a3a9224dc(
    *,
    entries: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.TypeConverterEntryProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79e92ae9fa026aa82c90fea81fa17a5b6bb260575c11df9b13ca682a992251e2(
    *,
    with_keys: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a546e5df5e922961501b15adaa49ec492ffe516851869f75aacd2acfe0283eee(
    *,
    log_group_identifier: builtins.str,
    transformer_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.ProcessorProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2766fe6d7d19a8737daff90dd79e476a2d4dcde95605b7656e40b088fdf6e64(
    *,
    comparison: builtins.str,
    number_value: typing.Optional[jsii.Number] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e58c798612261b35fc101134a189fa095e471b40cde2b522022473cb130c8ffd(
    *,
    source: builtins.str,
    target: builtins.str,
    overwrite_if_exists: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e1d63720cc55ad0f9fd25a9ccd1c33e428ce8f9353bb8eb3a0ffe5316b5e40d(
    *,
    entries: typing.Sequence[typing.Union[CopyValueEntryProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4be07d68ab857f5ae6300c8382cb03fbeec1052d13af65659f773e30196e8c1(
    *,
    role: _IRole_235f5d8e,
    target_arn: builtins.str,
    destination_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c40d29b973c2c88882518795acd7090c9554983c5f83ed50100c80f59d45e767(
    *,
    columns: typing.Optional[typing.Sequence[builtins.str]] = None,
    delimiter: typing.Optional[DelimiterCharacter] = None,
    quote_character: typing.Optional[QuoteCharacter] = None,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5d3ea1ab4dc61f97346ae6ae2134ce81803e6f823c3b99e67d009a033371f84(
    *,
    type: DataConverterType,
    date_time_converter_options: typing.Optional[typing.Union[DateTimeConverterProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    type_converter_options: typing.Optional[typing.Union[TypeConverterProperty, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15f2f9a4aba70e88d25dcda444a45fe96535b0317fb974d64d2b70c8e6982915(
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7783165e1d00e232a8ee35869f53b7ff500c9680f96b895f705e24475c7b6b2(
    *,
    identifiers: typing.Sequence[DataIdentifier],
    delivery_stream_name_audit_destination: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    log_group_audit_destination: typing.Optional[ILogGroup] = None,
    name: typing.Optional[builtins.str] = None,
    s3_bucket_audit_destination: typing.Optional[_IBucket_42e086fd] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35bff5994e76c17a7e4672ebf2d30e06b26eb34c402c647a8af28f310c672633(
    *,
    locale: builtins.str,
    match_patterns: typing.Sequence[builtins.str],
    source: builtins.str,
    target: builtins.str,
    source_timezone: typing.Optional[builtins.str] = None,
    target_format: typing.Optional[builtins.str] = None,
    target_timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8587c6606bf8df6db1fab55d5f7ea689b5960f088bf6825593078b791719378c(
    *,
    fields: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef6e7314c6a5197496584b4f3fc9dc8a24050e8d3d30eabb788540b98e00e4f0(
    *patterns: JsonPattern,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c83797f363cc2a7f1bb9ea15ea4f4d7eeed745e9d300970e536e8df78633b0a6(
    *terms: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06cd0420e64a91321c2dbdcdb6fa54fa56bffd0eab770aa6aa4000670f1beec3(
    *patterns: JsonPattern,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b38181b10ed8fe5993dd7ec40690693fe0d164f997f37ddbf297f8b840de2b18(
    *terms: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2623b46359820ca611b2cf65fab9b8e6c24ef2bd3d30bcebc3d022b2173b58ee(
    *term_groups: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0e87f500ca69757a8ec1184452b5b2b45c68758c062a77bc2248afd2c3b793e(
    json_field: builtins.str,
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56192ad48c0fbacd0f9f10fc26eebe8f311d8164217227e094a00a61f7c0d300(
    json_field: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93deee33b43c0efbe360f5ef6a60ba3cd0c1af95d7ca176abb95a482e1be8748(
    json_field: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65d91e718fc9d96060c30c68dee958f370d2ae16fbb2e3cf8f0030e0408b3320(
    log_pattern_string: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a90c7e4fc8c86ca2759be152abbd3a44e4e78851d525cdb047698b1825283849(
    json_field: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1cb7dce1caa0866199f67de4ab23972e5d6dc3cd90ca77ce9a5f09f7dc2b1fa(
    json_field: builtins.str,
    comparison: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a7a4c0a4a33b651a6a0a1fe2ce451f20e4fa36e60b8a3b9bd496de7c0f04c0f(
    json_field: builtins.str,
    comparison: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f5f56f60ccfd9dae1e3e3f54e54d87c6fb3e287c5bd2ad7924a4578ee4f8121(
    *columns: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31ecfe1cc2c14607ed9938dc33b51889185e1c9f4ea9e9e7ce494ae69f7d3374(
    json_field: builtins.str,
    comparison: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bba907d658ad5356562b8df18cf762bf9555e12e481aa8388b0a62d7ad1c35cd(
    *,
    match: builtins.str,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c3910e9df11478e889b7f25e252df8a33e79b82dd18c304bf83e6be63f60c95(
    id: builtins.str,
    *,
    filter_pattern: IFilterPattern,
    metric_name: builtins.str,
    metric_namespace: builtins.str,
    default_value: typing.Optional[jsii.Number] = None,
    dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    filter_name: typing.Optional[builtins.str] = None,
    metric_value: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad3db791d4d809f8716f4717b634e830370009e865e37f5c54e65cc5c5d57102(
    id: builtins.str,
    *,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3445e5a6f896ca9cd9e8a527d7229440b3a517fd59dc21bc08b64ef68e4f4eaa(
    id: builtins.str,
    *,
    destination: ILogSubscriptionDestination,
    filter_pattern: IFilterPattern,
    distribution: typing.Optional[Distribution] = None,
    filter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48b998ae428fa24bcd8e738e7f4b31c609a8b722db7837c472033393d2ad8523(
    id: builtins.str,
    *,
    transformer_config: typing.Sequence[IProcessor],
    transformer_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dc31b09300449039c7ac2db2c1e23ab325c60cc2fa2fa9ee5b513c2e1d62f7b(
    json_field: builtins.str,
    metric_namespace: builtins.str,
    metric_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d45146324c9cc51983b9b92779906c83ea73e499386493771cdd256c131ca87(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10f2b216c33139da1022d0b7d73974166dcf17c508e30913421c9f89375a9bb0(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__558c66823e9e8b21feeb1abd2b6534206c929fdf82184f3c0d1aff2942610538(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e63ab70f8bacc728cdbf61171dfc0b89720bb794e34d29336b9486edb7738afb(
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

def _typecheckingstub__0d2d750464949100272f59f23f28dae31a40c84ad1d188b0cd44fdca6ca395d5(
    scope: _constructs_77d1e7e8.Construct,
    source_log_group: ILogGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b6fd8557ef63d3b8ca1f2a3259dda6c618aa23213e0cb491a14321743e64f65(
    value: JsonMutatorType,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__388e83b4e8d42783305526c15dea5cd4e43051ab109847e7efb099d2b96f365f(
    *,
    type: JsonMutatorType,
    add_keys_options: typing.Optional[typing.Union[AddKeysProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    copy_value_options: typing.Optional[typing.Union[CopyValueProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    delete_keys_options: typing.Optional[typing.Union[ProcessorDeleteKeysProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    list_to_map_options: typing.Optional[typing.Union[ListToMapProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    move_keys_options: typing.Optional[typing.Union[MoveKeysProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    rename_keys_options: typing.Optional[typing.Union[RenameKeysProperty, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63b70184328854d0009cc9ba82f6a6720fd48ccf9458964b5cc75f6cfb653549(
    json_pattern_string: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1db693d7e35418cf07e62ac333914baf11457ace8ba9e2fb52d10d55e134533(
    *,
    key: builtins.str,
    source: builtins.str,
    flatten: typing.Optional[builtins.bool] = None,
    flattened_element: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
    value_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__308a02ff022bfc4531ef0c547fbfb8db809293b3cda70c61106c9bc271126e70(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_protection_policy: typing.Optional[DataProtectionPolicy] = None,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    field_index_policies: typing.Optional[typing.Sequence[FieldIndexPolicy]] = None,
    log_group_class: typing.Optional[LogGroupClass] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    retention: typing.Optional[RetentionDays] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94bc59386fc670bf1438201199282e56f015468fe650487225ccaca3ae495cd7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    log_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9988695c3237dc33d233c2bca8c1a32b8ca9135d661974af7b593667d7199d2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    log_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60bdb647264d5f9edd37cf7e07a8b1cde70ce81f1ebb17eb131efa9d12a73e70(
    id: builtins.str,
    *,
    filter_pattern: IFilterPattern,
    metric_name: builtins.str,
    metric_namespace: builtins.str,
    default_value: typing.Optional[jsii.Number] = None,
    dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    filter_name: typing.Optional[builtins.str] = None,
    metric_value: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a24d4a9b6baaaae57b481202eeb591bd2f9c75a23a136632347af1c7954e70d(
    id: builtins.str,
    *,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a53e1c08918ff12981b248135756d8f20c9acc571a2cab87ee6a3504361564b6(
    id: builtins.str,
    *,
    destination: ILogSubscriptionDestination,
    filter_pattern: IFilterPattern,
    distribution: typing.Optional[Distribution] = None,
    filter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f61b70f15ff76b195297fc3fa75909dc7046483a164b76160596773157f547f(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a47fe63f1fc66b79ef415b28ffcfb0a1d225c29859afcdcffa2b69c56711466(
    id: builtins.str,
    *,
    transformer_config: typing.Sequence[IProcessor],
    transformer_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fec042a3492600efc8a11c082c58cb34995746a66ce985d97fd5c74ba47f0b96(
    json_field: builtins.str,
    metric_namespace: builtins.str,
    metric_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9a9cb0e1cec11a01408a7a448100c7b05edddf5bb005abd006a834d3c923bb7(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__049a7f93ec71ef52ad5919516c695afd1e3f1185bfaadbf66b872fe23abae4db(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c97b414675dc468df60a1d999b2ddb74ddf42567d0d8ac3af19bb44f4022b1b0(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afd13314ef52ff283429f1992d9ab29ab14998262e884015dc1d0af12ff9df43(
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

def _typecheckingstub__df51a93f7809d59dd37d78a60967e0071dab4876ea1cd5ecd658ac3c8eae1320(
    *,
    data_protection_policy: typing.Optional[DataProtectionPolicy] = None,
    encryption_key: typing.Optional[_IKey_5f11635f] = None,
    field_index_policies: typing.Optional[typing.Sequence[FieldIndexPolicy]] = None,
    log_group_class: typing.Optional[LogGroupClass] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    retention: typing.Optional[RetentionDays] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4507613a235a88592d0ebd7d0dbe61f494620068c75fef42db8c09f2dfde8cc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    log_group_name: builtins.str,
    retention: RetentionDays,
    log_group_region: typing.Optional[builtins.str] = None,
    log_retention_retry_options: typing.Optional[typing.Union[LogRetentionRetryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__318a9234eb28bfd26692eac8fd1ea9c47cedbd175a0dc53714860906302a980b(
    *,
    log_group_name: builtins.str,
    retention: RetentionDays,
    log_group_region: typing.Optional[builtins.str] = None,
    log_retention_retry_options: typing.Optional[typing.Union[LogRetentionRetryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9636a1cfdc99034fff1c4ef9550b1c380d0f51a19f14b506c85c32184b950d42(
    *,
    base: typing.Optional[_Duration_4839e8c3] = None,
    max_retries: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7b310f4ff2940ed4dffa21e4ffde6e0f0bb15bdf93db6bd6d34466158da5c47(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    log_group: ILogGroup,
    log_stream_name: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c90257c192f43807c3ca64b0dfd7f0d8f24a0e76af49b59d49ef0b271d7e85a0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    log_stream_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f49a14f2b0eea132d7cea27db911c1bac5a2370d8c93686afb12d7bf18544ca(
    *,
    log_group: ILogGroup,
    log_stream_name: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__396d59c2514d8bfe65a7a6f818257b42d5f5c9b200fa30ed27db93bc6e8328e0(
    *,
    arn: builtins.str,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d62ba20acf6180e35fd081efe9f21747bf2bd8765dd3a4a5c41cc0f41f079a1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    log_group: ILogGroup,
    filter_pattern: IFilterPattern,
    metric_name: builtins.str,
    metric_namespace: builtins.str,
    default_value: typing.Optional[jsii.Number] = None,
    dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    filter_name: typing.Optional[builtins.str] = None,
    metric_value: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5bb9c8220568f1b3f6adf2d20dcfde3ada18ce4351110a49b3a0707812e51fe(
    *,
    filter_pattern: IFilterPattern,
    metric_name: builtins.str,
    metric_namespace: builtins.str,
    default_value: typing.Optional[jsii.Number] = None,
    dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    filter_name: typing.Optional[builtins.str] = None,
    metric_value: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66722f3b881a30b7ce1b9efa7c76f2539915abe8fe84a770e1e2c47657d59d79(
    *,
    filter_pattern: IFilterPattern,
    metric_name: builtins.str,
    metric_namespace: builtins.str,
    default_value: typing.Optional[jsii.Number] = None,
    dimensions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    filter_name: typing.Optional[builtins.str] = None,
    metric_value: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
    log_group: ILogGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da6f3038d5062508ca2dfbdb25c57768aae2900767d6f37a477e7a62987a2f6b(
    *,
    source: builtins.str,
    target: builtins.str,
    overwrite_if_exists: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d508581afde346c3dc6a7ad903e06a2c24df4ce3b379d82c518c2e7a374e9409(
    *,
    entries: typing.Sequence[typing.Union[MoveKeyEntryProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27216275bd8f254a8df2b93102ca26e488f09ce5ec9e4c3b50617d9234e9f31e(
    *,
    destination: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3318dff47923fe5f4ad247b238d1986eef32599700ab67d15852a597a0339379(
    *,
    destination: typing.Optional[builtins.str] = None,
    field_delimiter: typing.Optional[KeyValuePairDelimiter] = None,
    key_prefix: typing.Optional[builtins.str] = None,
    key_value_delimiter: typing.Optional[KeyValueDelimiter] = None,
    non_match_value: typing.Optional[builtins.str] = None,
    overwrite_if_exists: typing.Optional[builtins.bool] = None,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__735c1599edef90b0d0dbcf40602bb77ce633f8947966bf268b4c6dde7571e25a(
    *,
    event_source: OCSFSourceType,
    ocsf_version: OCSFVersion,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a13b8703c16230a1b0b020e63fbdce04c68089e17624ad5d83abcab651aff88(
    value: ParserProcessorType,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a32cf5eb9ebc811676ec4f9fad1e89dcb2f56561cb63fe216912ac5458a9f85(
    *,
    type: ParserProcessorType,
    csv_options: typing.Optional[typing.Union[CsvProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    grok_options: typing.Optional[typing.Union[GrokProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    json_options: typing.Optional[typing.Union[ParseJSONProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    key_value_options: typing.Optional[typing.Union[ParseKeyValueProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    parse_to_ocsf_options: typing.Optional[typing.Union[ParseToOCSFProperty, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0d7219b7469a32f19b7207dbd41b09b6d3953b5505ac4fc08e7139136f7308d(
    *,
    with_keys: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7cb87fa9a91fccd75052278e9031242b20cab41bb53f8f18544b867e01e5d41(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    query_definition_name: builtins.str,
    query_string: QueryString,
    log_groups: typing.Optional[typing.Sequence[ILogGroup]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__993712107c64f2acd19761e2b930e6e052534d1100257989bcf307bb6168b668(
    *,
    query_definition_name: builtins.str,
    query_string: QueryString,
    log_groups: typing.Optional[typing.Sequence[ILogGroup]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d205eb2ac9b46de0083e3387b95b00f2362e2ade91d5c581e5d8cde68293b28d(
    *,
    display: typing.Optional[builtins.str] = None,
    fields: typing.Optional[typing.Sequence[builtins.str]] = None,
    filter: typing.Optional[builtins.str] = None,
    filter_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
    limit: typing.Optional[jsii.Number] = None,
    parse: typing.Optional[builtins.str] = None,
    parse_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
    sort: typing.Optional[builtins.str] = None,
    stats: typing.Optional[builtins.str] = None,
    stats_statements: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79c7d64341c225a9e8d9c156812001b053b87c33197fc3f9fb96e14931bf62f8(
    *,
    key: builtins.str,
    rename_to: builtins.str,
    overwrite_if_exists: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__198823a45c6e5e4862ca8d9502cccda6799064b56d480db08bb111e19d801f21(
    *,
    entries: typing.Sequence[typing.Union[RenameKeyEntryProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__772b118f71acb9e446b4948b9aac7bf360262cdeddc09c1f28708795cdb48c74(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_statements: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    resource_policy_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4f5108e8fcf5bafe964b9be836229eed1f4ac734a83be621801cd6304143286(
    *,
    policy_statements: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    resource_policy_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b056cc11acf9eec747709139eb527ca4dbbf26be0a7b192c65f6ce27af65184(
    columns: typing.Sequence[builtins.str],
    restrictions: typing.Mapping[builtins.str, typing.Sequence[typing.Union[ColumnRestriction, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d1e9e085756c1b7939b77b321d912811c1ae652d0160b5c494b0894d37e178(
    columns: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9837cdc1b4560186b7313c523de825a85b6c099daae328e79ce8c2a6fcc1431f(
    column_name: builtins.str,
    comparison: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__071ad580f6d865947c2434ea9ce22e541c8aabe0aaf4f627b337988d5c6c6ccd(
    column_name: builtins.str,
    comparison: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0da5731b4ea06065f3a14013f1f462ddb062c7a6f696ed9790bdebff32f6b487(
    *,
    delimiter: DelimiterCharacter,
    source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93325aed54aeb72271014f8d01393fe4bead496c1b4b9a96fe2628a72856b895(
    *,
    entries: typing.Sequence[typing.Union[SplitStringEntryProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faa627faaa2e41610592354837a6717d48ec540f225e5fa931868e06dda19d5e(
    *,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc8c1fe39cd0dbda92f882107b130bc9378206d263f648e0ae3930de51c6987f(
    value: StringMutatorType,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9a1cadbe7ded283aeca06e2d5345cb01473604a502a95e3776eb51172e23ea5(
    *,
    type: StringMutatorType,
    lower_case_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    split_options: typing.Optional[typing.Union[SplitStringProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    substitute_options: typing.Optional[typing.Union[SubstituteStringProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    trim_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    upper_case_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c78d3f905ddfb9bb1ff8466a0b030e7b262b0793c43d2667b561e420cbb3c7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    log_group: ILogGroup,
    destination: ILogSubscriptionDestination,
    filter_pattern: IFilterPattern,
    distribution: typing.Optional[Distribution] = None,
    filter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__177a84e94bfd826b20adc1107770c972772c540b0a1ac8475f63476502450a73(
    *,
    destination: ILogSubscriptionDestination,
    filter_pattern: IFilterPattern,
    distribution: typing.Optional[Distribution] = None,
    filter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb936c8dd6a8ee03c9e8f4ffbe991c19b4b98648bbdd91f03367a058de3e8268(
    *,
    destination: ILogSubscriptionDestination,
    filter_pattern: IFilterPattern,
    distribution: typing.Optional[Distribution] = None,
    filter_name: typing.Optional[builtins.str] = None,
    log_group: ILogGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89f40c023205edf817c714afaa5f89f95fb9d2d1229d815efc0d03dcd3c928a9(
    *,
    from_: builtins.str,
    source: builtins.str,
    to: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89623f0009740e6c093be416eda3b9572559011ccffe3a9d8d28a3cbd2683a71(
    *,
    entries: typing.Sequence[typing.Union[SubstituteStringEntryProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15229fc0be2da1cdc000826d3fc7c0eb70960587299f27c938a1fd71c98c1d2d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    log_group: ILogGroup,
    transformer_config: typing.Sequence[IProcessor],
    transformer_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fb14deb68ad2a391c38083a4ab9599103e7918f73904352784a6fbf0fa0ad15(
    *,
    transformer_config: typing.Sequence[IProcessor],
    transformer_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c44d5878511fc89516420ebac8e669a5edc49cf01182e21ae66e8d8f47e3df4b(
    *,
    log_group: ILogGroup,
    transformer_config: typing.Sequence[IProcessor],
    transformer_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0be65a0bf0645c5557fac9906c47d395393b2aea1d3d5f1f33ebd91b9f247a77(
    *,
    key: builtins.str,
    type: TypeConverterType,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c16a2fb884c15b78b564dcb7d166ce474c411638d2de9600531d96d93f88910(
    *,
    entries: typing.Sequence[typing.Union[TypeConverterEntryProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcaaf986081bc45f10c5e81d15b15c27b04392687542820b3ca2da24add5605d(
    value: VendedLogType,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e317a7d0a3ab35fb963ce2b635f89cd9aabf90244799cafa76755dd69ebdbbe(
    *,
    log_type: VendedLogType,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f78998ef1421583d87d205e0c66668e415d3a06be064cfc35682d8884a01ad56(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    role: _IRole_235f5d8e,
    target_arn: builtins.str,
    destination_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a3a6f7c79a2740b0e52fcc48d64fb4e96cfdc2abd91649f986c7d67b9d5ee67(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__901846e19d9ba5beee9ef4784401b7413f0b32b2034ea5700b5fa8a30a1c0394(
    _scope: _constructs_77d1e7e8.Construct,
    _source_log_group: ILogGroup,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8962f986463b4e81629495838f26c8990feeca56061597cb66e94771b4cfb79d(
    name: builtins.str,
    regex: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bea2654ebc88ef45acb691425a17897e52198e8f268040b952558fccd601704e(
    value: DataConverterType,
) -> None:
    """Type checking stubs"""
    pass
