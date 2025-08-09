r'''
# Amazon EventBridge Scheduler Construct Library

[Amazon EventBridge Scheduler](https://aws.amazon.com/blogs/compute/introducing-amazon-eventbridge-scheduler/) is a feature from Amazon EventBridge
that allows you to create, run, and manage scheduled tasks at scale. With EventBridge Scheduler, you can schedule millions of one-time or recurring tasks across various AWS services without provisioning or managing underlying infrastructure.

1. **Schedule**: A schedule is the main resource you create, configure, and manage using Amazon EventBridge Scheduler. Every schedule has a schedule expression that determines when, and with what frequency, the schedule runs. EventBridge Scheduler supports three types of schedules: rate, cron, and one-time schedules. When you create a schedule, you configure a target for the schedule to invoke.
2. **Target**: A target is an API operation that EventBridge Scheduler calls on your behalf every time your schedule runs. EventBridge Scheduler
   supports two types of targets: templated targets and universal targets. Templated targets invoke common API operations across a core groups of
   services. For example, EventBridge Scheduler supports templated targets for invoking AWS Lambda Function or starting execution of Step Functions state
   machine. For API operations that are not supported by templated targets you can use customizable universal targets. Universal targets support calling
   more than 6,000 API operations across over 270 AWS services.
3. **Schedule Group**: A schedule group is an Amazon EventBridge Scheduler resource that you use to organize your schedules. Your AWS account comes
   with a default scheduler group. A new schedule will always be added to a scheduling group. If you do not provide a scheduling group to add to, it
   will be added to the default scheduling group. You can create up to 500 schedule groups in your AWS account. Groups can be used to organize the
   schedules logically, access the schedule metrics and manage permissions at group granularity (see details below). Schedule groups support tagging.
   With EventBridge Scheduler, you apply tags to schedule groups, not to individual schedules to organize your resources.

## Defining a schedule

```python
# fn: lambda.Function


target = targets.LambdaInvoke(fn,
    input=ScheduleTargetInput.from_object({
        "payload": "useful"
    })
)

schedule = Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.minutes(10)),
    target=target,
    description="This is a test schedule that invokes a lambda function every 10 minutes."
)
```

### Schedule Expressions

You can choose from three schedule types when configuring your schedule: rate-based, cron-based, and one-time schedules.

Both rate-based and cron-based schedules are recurring schedules. You can configure each recurring schedule type using a schedule expression.

For
cron-based schedules you can specify a time zone in which EventBridge Scheduler evaluates the expression.

```python
# target: targets.LambdaInvoke


rate_based_schedule = Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.minutes(10)),
    target=target,
    description="This is a test rate-based schedule"
)

cron_based_schedule = Schedule(self, "Schedule",
    schedule=ScheduleExpression.cron(
        minute="0",
        hour="23",
        day="20",
        month="11",
        time_zone=TimeZone.AMERICA_NEW_YORK
    ),
    target=target,
    description="This is a test cron-based schedule that will run at 11:00 PM, on day 20 of the month, only in November in New York timezone"
)
```

A one-time schedule is a schedule that invokes a target only once. You configure a one-time schedule by specifying the time of day, date,
and time zone in which EventBridge Scheduler evaluates the schedule.

```python
# target: targets.LambdaInvoke


one_time_schedule = Schedule(self, "Schedule",
    schedule=ScheduleExpression.at(
        Date(2022, 10, 20, 19, 20, 23), TimeZone.AMERICA_NEW_YORK),
    target=target,
    description="This is a one-time schedule in New York timezone"
)
```

### Grouping Schedules

Your AWS account comes with a default scheduler group. You can access the default group in CDK with:

```python
default_schedule_group = ScheduleGroup.from_default_schedule_group(self, "DefaultGroup")
```

You can add a schedule to a custom scheduling group managed by you. If a custom group is not specified, the schedule is added to the default group.

```python
# target: targets.LambdaInvoke


schedule_group = ScheduleGroup(self, "ScheduleGroup",
    schedule_group_name="MyScheduleGroup"
)

Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.minutes(10)),
    target=target,
    schedule_group=schedule_group
)
```

### Disabling Schedules

By default, a schedule will be enabled. You can disable a schedule by setting the `enabled` property to false:

```python
# target: targets.LambdaInvoke


Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.minutes(10)),
    target=target,
    enabled=False
)
```

### Configuring a start and end time of the Schedule

If you choose a recurring schedule, you can set the start and end time of the Schedule by specifying the `start` and `end`.

```python
# target: targets.LambdaInvoke


Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(cdk.Duration.hours(12)),
    target=target,
    start=Date("2023-01-01T00:00:00.000Z"),
    end=Date("2023-02-01T00:00:00.000Z")
)
```

## Scheduler Targets

The `aws-cdk-lib/aws-scheduler-targets` module includes classes that implement the `IScheduleTarget` interface for
various AWS services. EventBridge Scheduler supports two types of targets:

1. **Templated targets** which invoke common API
   operations across a core groups of services, and
2. **Universal targets** that you can customize to call more
   than 6,000 operations across over 270 services.

A list of supported targets can be found at `aws-cdk-lib/aws-scheduler-targets`.

### Input

Targets can be invoked with a custom input. The `ScheduleTargetInput` class supports free-form text input and JSON-formatted object input:

```python
input = ScheduleTargetInput.from_object({
    "QueueName": "MyQueue"
})
```

You can include context attributes in your target payload. EventBridge Scheduler will replace each keyword with
its respective value and deliver it to the target. See
[full list of supported context attributes](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-context-attributes.html):

1. `ContextAttribute.scheduleArn()` – The ARN of the schedule.
2. `ContextAttribute.scheduledTime()` – The time you specified for the schedule to invoke its target, e.g., 2022-03-22T18:59:43Z.
3. `ContextAttribute.executionId()` – The unique ID that EventBridge Scheduler assigns for each attempted invocation of a target, e.g., d32c5kddcf5bb8c3.
4. `ContextAttribute.attemptNumber()` – A counter that identifies the attempt number for the current invocation, e.g., 1.

```python
text = f"Attempt number: {ContextAttribute.attemptNumber}"
input = ScheduleTargetInput.from_text(text)
```

### Specifying an execution role

An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf.

The classes for templated schedule targets automatically create an IAM role with all the minimum necessary
permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets
will grant minimal required permissions. For example, the `LambdaInvoke` target will grant the
IAM execution role `lambda:InvokeFunction` permission to invoke the Lambda function.

```python
# fn: lambda.Function


role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("scheduler.amazonaws.com")
)

target = targets.LambdaInvoke(fn,
    input=ScheduleTargetInput.from_object({
        "payload": "useful"
    }),
    role=role
)
```

### Specifying an encryption key

EventBridge Scheduler integrates with AWS Key Management Service (AWS KMS) to encrypt and decrypt your data using an AWS KMS key.
EventBridge Scheduler supports two types of KMS keys: AWS owned keys, and customer managed keys.

By default, all events in Scheduler are encrypted with a key that AWS owns and manages.
If you wish you can also provide a customer managed key to encrypt and decrypt the payload that your schedule delivers to its target using the `key` property.
Target classes will automatically add AWS `kms:Decrypt` permission to your schedule's execution role permissions policy.

```python
# key: kms.Key
# fn: lambda.Function


target = targets.LambdaInvoke(fn,
    input=ScheduleTargetInput.from_object({
        "payload": "useful"
    })
)

schedule = Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.minutes(10)),
    target=target,
    key=key
)
```

> See [Data protection in Amazon EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/data-protection.html) for more details.

## Configuring flexible time windows

You can configure flexible time windows by specifying the `timeWindow` property.
Flexible time windows are disabled by default.

```python
# target: targets.LambdaInvoke


schedule = Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.hours(12)),
    target=target,
    time_window=TimeWindow.flexible(Duration.hours(10))
)
```

> See [Configuring flexible time windows](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-flexible-time-windows.html) for more details.

## Error-handling

You can configure how your schedule handles failures, when EventBridge Scheduler is unable to deliver an event
successfully to a target, by using two primary mechanisms: a retry policy, and a dead-letter queue (DLQ).

A retry policy determines the number of times EventBridge Scheduler must retry a failed event, and how long
to keep an unprocessed event.

A DLQ is a standard Amazon SQS queue EventBridge Scheduler uses to deliver failed events to, after the retry
policy has been exhausted. You can use a DLQ to troubleshoot issues with your schedule or its downstream target.
If you've configured a retry policy for your schedule, EventBridge Scheduler delivers the dead-letter event after
exhausting the maximum number of retries you set in the retry policy.

```python
# fn: lambda.Function


dlq = sqs.Queue(self, "DLQ",
    queue_name="MyDLQ"
)

target = targets.LambdaInvoke(fn,
    dead_letter_queue=dlq,
    max_event_age=Duration.minutes(1),
    retry_attempts=3
)
```

## Monitoring

You can monitor Amazon EventBridge Scheduler using CloudWatch, which collects raw data
and processes it into readable, near real-time metrics. EventBridge Scheduler emits
a set of metrics for all schedules, and an additional set of metrics for schedules that
have an associated dead-letter queue (DLQ). If you configure a DLQ for your schedule,
EventBridge Scheduler publishes additional metrics when your schedule exhausts its retry policy.

### Metrics for all schedules

The `Schedule` class provides static methods for accessing all schedules metrics with default configuration, such as `metricAllErrors` for viewing errors when executing targets.

```python
cloudwatch.Alarm(self, "SchedulesErrorAlarm",
    metric=Schedule.metric_all_errors(),
    threshold=0,
    evaluation_periods=1
)
```

### Metrics for a Schedule Group

To view metrics for a specific group you can use methods on class `ScheduleGroup`:

```python
schedule_group = ScheduleGroup(self, "ScheduleGroup",
    schedule_group_name="MyScheduleGroup"
)

cloudwatch.Alarm(self, "MyGroupErrorAlarm",
    metric=schedule_group.metric_target_errors(),
    evaluation_periods=1,
    threshold=0
)

# Or use default group
default_schedule_group = ScheduleGroup.from_default_schedule_group(self, "DefaultScheduleGroup")
cloudwatch.Alarm(self, "DefaultScheduleGroupErrorAlarm",
    metric=default_schedule_group.metric_target_errors(),
    evaluation_periods=1,
    threshold=0
)
```

See full list of metrics and their description at
[Monitoring Using CloudWatch Metrics](https://docs.aws.amazon.com/scheduler/latest/UserGuide/monitoring-cloudwatch.html)
in the *AWS EventBridge Scheduler User Guide*.
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
    RemovalPolicy as _RemovalPolicy_9f93c814,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TimeZone as _TimeZone_cdd72ac9,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_cloudwatch import (
    Metric as _Metric_e396a4dc,
    MetricOptions as _MetricOptions_1788b62f,
    Unit as _Unit_61bc6f70,
)
from ..aws_events import CronOptions as _CronOptions_6401a7a0
from ..aws_iam import (
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IRole as _IRole_235f5d8e,
)
from ..aws_kms import IKey as _IKey_5f11635f


@jsii.implements(_IInspectable_c2943556)
class CfnSchedule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule",
):
    '''A *schedule* is the main resource you create, configure, and manage using Amazon EventBridge Scheduler.

    Every schedule has a *schedule expression* that determines when, and with what frequency, the schedule runs. EventBridge Scheduler supports three types of schedules: rate, cron, and one-time schedules. For more information about different schedule types, see `Schedule types <https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html>`_ in the *EventBridge Scheduler User Guide* .

    When you create a schedule, you configure a target for the schedule to invoke. A target is an API operation that EventBridge Scheduler calls on your behalf every time your schedule runs. EventBridge Scheduler supports two types of targets: *templated* targets invoke common API operations across a core groups of services, and customizeable *universal* targets that you can use to call more than 6,000 operations across over 270 services. For more information about configuring targets, see `Managing targets <https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-targets.html>`_ in the *EventBridge Scheduler User Guide* .

    For more information about managing schedules, changing the schedule state, setting up flexible time windows, and configuring a dead-letter queue for a schedule, see `Managing a schedule <https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule.html>`_ in the *EventBridge Scheduler User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html
    :cloudformationResource: AWS::Scheduler::Schedule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_scheduler as scheduler
        
        # tags: Any
        
        cfn_schedule = scheduler.CfnSchedule(self, "MyCfnSchedule",
            flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                mode="mode",
        
                # the properties below are optional
                maximum_window_in_minutes=123
            ),
            schedule_expression="scheduleExpression",
            target=scheduler.CfnSchedule.TargetProperty(
                arn="arn",
                role_arn="roleArn",
        
                # the properties below are optional
                dead_letter_config=scheduler.CfnSchedule.DeadLetterConfigProperty(
                    arn="arn"
                ),
                ecs_parameters=scheduler.CfnSchedule.EcsParametersProperty(
                    task_definition_arn="taskDefinitionArn",
        
                    # the properties below are optional
                    capacity_provider_strategy=[scheduler.CfnSchedule.CapacityProviderStrategyItemProperty(
                        capacity_provider="capacityProvider",
        
                        # the properties below are optional
                        base=123,
                        weight=123
                    )],
                    enable_ecs_managed_tags=False,
                    enable_execute_command=False,
                    group="group",
                    launch_type="launchType",
                    network_configuration=scheduler.CfnSchedule.NetworkConfigurationProperty(
                        awsvpc_configuration=scheduler.CfnSchedule.AwsVpcConfigurationProperty(
                            subnets=["subnets"],
        
                            # the properties below are optional
                            assign_public_ip="assignPublicIp",
                            security_groups=["securityGroups"]
                        )
                    ),
                    placement_constraints=[scheduler.CfnSchedule.PlacementConstraintProperty(
                        expression="expression",
                        type="type"
                    )],
                    placement_strategy=[scheduler.CfnSchedule.PlacementStrategyProperty(
                        field="field",
                        type="type"
                    )],
                    platform_version="platformVersion",
                    propagate_tags="propagateTags",
                    reference_id="referenceId",
                    tags=tags,
                    task_count=123
                ),
                event_bridge_parameters=scheduler.CfnSchedule.EventBridgeParametersProperty(
                    detail_type="detailType",
                    source="source"
                ),
                input="input",
                kinesis_parameters=scheduler.CfnSchedule.KinesisParametersProperty(
                    partition_key="partitionKey"
                ),
                retry_policy=scheduler.CfnSchedule.RetryPolicyProperty(
                    maximum_event_age_in_seconds=123,
                    maximum_retry_attempts=123
                ),
                sage_maker_pipeline_parameters=scheduler.CfnSchedule.SageMakerPipelineParametersProperty(
                    pipeline_parameter_list=[scheduler.CfnSchedule.SageMakerPipelineParameterProperty(
                        name="name",
                        value="value"
                    )]
                ),
                sqs_parameters=scheduler.CfnSchedule.SqsParametersProperty(
                    message_group_id="messageGroupId"
                )
            ),
        
            # the properties below are optional
            description="description",
            end_date="endDate",
            group_name="groupName",
            kms_key_arn="kmsKeyArn",
            name="name",
            schedule_expression_timezone="scheduleExpressionTimezone",
            start_date="startDate",
            state="state"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        flexible_time_window: typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedule.FlexibleTimeWindowProperty", typing.Dict[builtins.str, typing.Any]]],
        schedule_expression: builtins.str,
        target: typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedule.TargetProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        end_date: typing.Optional[builtins.str] = None,
        group_name: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        schedule_expression_timezone: typing.Optional[builtins.str] = None,
        start_date: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param flexible_time_window: Allows you to configure a time window during which EventBridge Scheduler invokes the schedule.
        :param schedule_expression: The expression that defines when the schedule runs. The following formats are supported. - ``at`` expression - ``at(yyyy-mm-ddThh:mm:ss)`` - ``rate`` expression - ``rate(value unit)`` - ``cron`` expression - ``cron(fields)`` You can use ``at`` expressions to create one-time schedules that invoke a target once, at the time and in the time zone, that you specify. You can use ``rate`` and ``cron`` expressions to create recurring schedules. Rate-based schedules are useful when you want to invoke a target at regular intervals, such as every 15 minutes or every five days. Cron-based schedules are useful when you want to invoke a target periodically at a specific time, such as at 8:00 am (UTC+0) every 1st day of the month. A ``cron`` expression consists of six fields separated by white spaces: ``(minutes hours day_of_month month day_of_week year)`` . A ``rate`` expression consists of a *value* as a positive integer, and a *unit* with the following options: ``minute`` | ``minutes`` | ``hour`` | ``hours`` | ``day`` | ``days`` For more information and examples, see `Schedule types on EventBridge Scheduler <https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html>`_ in the *EventBridge Scheduler User Guide* .
        :param target: The schedule's target details.
        :param description: The description you specify for the schedule.
        :param end_date: The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the ``EndDate`` you specify. EventBridge Scheduler ignores ``EndDate`` for one-time schedules.
        :param group_name: The name of the schedule group associated with this schedule.
        :param kms_key_arn: The Amazon Resource Name (ARN) for the customer managed KMS key that EventBridge Scheduler will use to encrypt and decrypt your data.
        :param name: The name of the schedule.
        :param schedule_expression_timezone: The timezone in which the scheduling expression is evaluated.
        :param start_date: The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the ``StartDate`` you specify. EventBridge Scheduler ignores ``StartDate`` for one-time schedules.
        :param state: Specifies whether the schedule is enabled or disabled. *Allowed Values* : ``ENABLED`` | ``DISABLED``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__503b74ac170f15626de2456b6f8c40d2cdc1ab21574c821e051517099f516ea4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScheduleProps(
            flexible_time_window=flexible_time_window,
            schedule_expression=schedule_expression,
            target=target,
            description=description,
            end_date=end_date,
            group_name=group_name,
            kms_key_arn=kms_key_arn,
            name=name,
            schedule_expression_timezone=schedule_expression_timezone,
            start_date=start_date,
            state=state,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__859c33780944a757aa0069dfe861a7f9ee3aaa6d51b1881276590d23b3cbc11d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1c9dd58f37a9f244d09bdbca3ac4ea0869a0855a2cb760325d51c0d8beed730d)
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
        '''The Amazon Resource Name (ARN) for the Amazon EventBridge Scheduler schedule.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="flexibleTimeWindow")
    def flexible_time_window(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnSchedule.FlexibleTimeWindowProperty"]:
        '''Allows you to configure a time window during which EventBridge Scheduler invokes the schedule.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnSchedule.FlexibleTimeWindowProperty"], jsii.get(self, "flexibleTimeWindow"))

    @flexible_time_window.setter
    def flexible_time_window(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnSchedule.FlexibleTimeWindowProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__596e14fe3c5d30f5608996086027eaf3ff49cf0205d5a551a9e0895e2be75f2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flexibleTimeWindow", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scheduleExpression")
    def schedule_expression(self) -> builtins.str:
        '''The expression that defines when the schedule runs.

        The following formats are supported.
        '''
        return typing.cast(builtins.str, jsii.get(self, "scheduleExpression"))

    @schedule_expression.setter
    def schedule_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86a3656a00e3dadf75b2e58b2162ed9850cd46df81630349120c362c216f94db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleExpression", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnSchedule.TargetProperty"]:
        '''The schedule's target details.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnSchedule.TargetProperty"], jsii.get(self, "target"))

    @target.setter
    def target(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnSchedule.TargetProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9658077cef2602ca00d25f391105ce442d6a0a3efef1ca5be55db053ede80a78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description you specify for the schedule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5864139b51db95ec1c3e6c947b577675bb4f83133b1f5476864d71c4009c2386)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="endDate")
    def end_date(self) -> typing.Optional[builtins.str]:
        '''The date, in UTC, before which the schedule can invoke its target.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endDate"))

    @end_date.setter
    def end_date(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3d0ae7ef525e3a588544a09eb7ec3271c357974ae47f41180a7aeb9086e2594)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endDate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the schedule group associated with this schedule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1860ec4ad4204d90b7f2756ff633582f92f7f97d174b16a7da8e36811ebdc98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the customer managed KMS key that EventBridge Scheduler will use to encrypt and decrypt your data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c65947df9a6be40d839d971ea07ff6a85493b9cfbab03c61fc17e54bdd0e9276)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the schedule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb6bd8d80ac829e96128e011c87e852bfea080bdcd859bfdf98c7874542dc1b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scheduleExpressionTimezone")
    def schedule_expression_timezone(self) -> typing.Optional[builtins.str]:
        '''The timezone in which the scheduling expression is evaluated.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleExpressionTimezone"))

    @schedule_expression_timezone.setter
    def schedule_expression_timezone(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb337d25b9d34da19dbe88b72514ea1e1e7a235cd91b7597abecd038498e11a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleExpressionTimezone", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="startDate")
    def start_date(self) -> typing.Optional[builtins.str]:
        '''The date, in UTC, after which the schedule can begin invoking its target.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startDate"))

    @start_date.setter
    def start_date(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38fc94567c401ce05bf3ed2461327df25f05b71764228be5a3f95fec0573d007)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startDate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''Specifies whether the schedule is enabled or disabled.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__986ef975482735e4fbf46592da626ebfd4ca9636ad053fe886d40f9856d1483e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.AwsVpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "subnets": "subnets",
            "assign_public_ip": "assignPublicIp",
            "security_groups": "securityGroups",
        },
    )
    class AwsVpcConfigurationProperty:
        def __init__(
            self,
            *,
            subnets: typing.Sequence[builtins.str],
            assign_public_ip: typing.Optional[builtins.str] = None,
            security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''This structure specifies the VPC subnets and security groups for the task, and whether a public IP address is to be used.

            This structure is relevant only for ECS tasks that use the awsvpc network mode.

            :param subnets: Specifies the subnets associated with the task. These subnets must all be in the same VPC. You can specify as many as 16 subnets.
            :param assign_public_ip: Specifies whether the task's elastic network interface receives a public IP address. You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters`` is set to ``FARGATE`` .
            :param security_groups: Specifies the security groups associated with the task. These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-awsvpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                aws_vpc_configuration_property = scheduler.CfnSchedule.AwsVpcConfigurationProperty(
                    subnets=["subnets"],
                
                    # the properties below are optional
                    assign_public_ip="assignPublicIp",
                    security_groups=["securityGroups"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4be9629f7b1d55fb08861d6713480d5fa198e6e40012bcf701a627e532032afb)
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
                check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "subnets": subnets,
            }
            if assign_public_ip is not None:
                self._values["assign_public_ip"] = assign_public_ip
            if security_groups is not None:
                self._values["security_groups"] = security_groups

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''Specifies the subnets associated with the task.

            These subnets must all be in the same VPC. You can specify as many as 16 subnets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-awsvpcconfiguration.html#cfn-scheduler-schedule-awsvpcconfiguration-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def assign_public_ip(self) -> typing.Optional[builtins.str]:
            '''Specifies whether the task's elastic network interface receives a public IP address.

            You can specify ``ENABLED`` only when ``LaunchType`` in ``EcsParameters`` is set to ``FARGATE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-awsvpcconfiguration.html#cfn-scheduler-schedule-awsvpcconfiguration-assignpublicip
            '''
            result = self._values.get("assign_public_ip")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies the security groups associated with the task.

            These security groups must all be in the same VPC. You can specify as many as five security groups. If you do not specify a security group, the default security group for the VPC is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-awsvpcconfiguration.html#cfn-scheduler-schedule-awsvpcconfiguration-securitygroups
            '''
            result = self._values.get("security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsVpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.CapacityProviderStrategyItemProperty",
        jsii_struct_bases=[],
        name_mapping={
            "capacity_provider": "capacityProvider",
            "base": "base",
            "weight": "weight",
        },
    )
    class CapacityProviderStrategyItemProperty:
        def __init__(
            self,
            *,
            capacity_provider: builtins.str,
            base: typing.Optional[jsii.Number] = None,
            weight: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The details of a capacity provider strategy.

            :param capacity_provider: The short name of the capacity provider.
            :param base: The base value designates how many tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined. If no value is specified, the default value of ``0`` is used. Default: - 0
            :param weight: The weight value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider. The weight value is taken into consideration after the base value, if defined, is satisfied. Default: - 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                capacity_provider_strategy_item_property = scheduler.CfnSchedule.CapacityProviderStrategyItemProperty(
                    capacity_provider="capacityProvider",
                
                    # the properties below are optional
                    base=123,
                    weight=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1d8897162eaa13dfb81dc83e782d5936ed604f09ed623574ad9d0fabc4a1ab7e)
                check_type(argname="argument capacity_provider", value=capacity_provider, expected_type=type_hints["capacity_provider"])
                check_type(argname="argument base", value=base, expected_type=type_hints["base"])
                check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "capacity_provider": capacity_provider,
            }
            if base is not None:
                self._values["base"] = base
            if weight is not None:
                self._values["weight"] = weight

        @builtins.property
        def capacity_provider(self) -> builtins.str:
            '''The short name of the capacity provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html#cfn-scheduler-schedule-capacityproviderstrategyitem-capacityprovider
            '''
            result = self._values.get("capacity_provider")
            assert result is not None, "Required property 'capacity_provider' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def base(self) -> typing.Optional[jsii.Number]:
            '''The base value designates how many tasks, at a minimum, to run on the specified capacity provider.

            Only one capacity provider in a capacity provider strategy can have a base defined. If no value is specified, the default value of ``0`` is used.

            :default: - 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html#cfn-scheduler-schedule-capacityproviderstrategyitem-base
            '''
            result = self._values.get("base")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def weight(self) -> typing.Optional[jsii.Number]:
            '''The weight value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider.

            The weight value is taken into consideration after the base value, if defined, is satisfied.

            :default: - 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-capacityproviderstrategyitem.html#cfn-scheduler-schedule-capacityproviderstrategyitem-weight
            '''
            result = self._values.get("weight")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapacityProviderStrategyItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.DeadLetterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class DeadLetterConfigProperty:
        def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
            '''An object that contains information about an Amazon SQS queue that EventBridge Scheduler uses as a dead-letter queue for your schedule.

            If specified, EventBridge Scheduler delivers failed events that could not be successfully delivered to a target to the queue.

            :param arn: The Amazon Resource Name (ARN) of the SQS queue specified as the destination for the dead-letter queue.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-deadletterconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                dead_letter_config_property = scheduler.CfnSchedule.DeadLetterConfigProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__147909ee33401019ceeec9c9c260dd3ac0812db04c597e1b63c26f0608f61069)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the SQS queue specified as the destination for the dead-letter queue.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-deadletterconfig.html#cfn-scheduler-schedule-deadletterconfig-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeadLetterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.EcsParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "task_definition_arn": "taskDefinitionArn",
            "capacity_provider_strategy": "capacityProviderStrategy",
            "enable_ecs_managed_tags": "enableEcsManagedTags",
            "enable_execute_command": "enableExecuteCommand",
            "group": "group",
            "launch_type": "launchType",
            "network_configuration": "networkConfiguration",
            "placement_constraints": "placementConstraints",
            "placement_strategy": "placementStrategy",
            "platform_version": "platformVersion",
            "propagate_tags": "propagateTags",
            "reference_id": "referenceId",
            "tags": "tags",
            "task_count": "taskCount",
        },
    )
    class EcsParametersProperty:
        def __init__(
            self,
            *,
            task_definition_arn: builtins.str,
            capacity_provider_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedule.CapacityProviderStrategyItemProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            enable_execute_command: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            group: typing.Optional[builtins.str] = None,
            launch_type: typing.Optional[builtins.str] = None,
            network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedule.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            placement_constraints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedule.PlacementConstraintProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            placement_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedule.PlacementStrategyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            platform_version: typing.Optional[builtins.str] = None,
            propagate_tags: typing.Optional[builtins.str] = None,
            reference_id: typing.Optional[builtins.str] = None,
            tags: typing.Any = None,
            task_count: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The templated target type for the Amazon ECS ```RunTask`` <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html>`_ API operation.

            :param task_definition_arn: The Amazon Resource Name (ARN) of the task definition to use if the event target is an Amazon ECS task.
            :param capacity_provider_strategy: The capacity provider strategy to use for the task.
            :param enable_ecs_managed_tags: Specifies whether to enable Amazon ECS managed tags for the task. For more information, see `Tagging Your Amazon ECS Resources <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html>`_ in the *Amazon ECS Developer Guide* .
            :param enable_execute_command: Whether or not to enable the execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task.
            :param group: Specifies an Amazon ECS task group for the task. The maximum length is 255 characters.
            :param launch_type: Specifies the launch type on which your task is running. The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The ``FARGATE`` value is supported only in the Regions where Fargate with Amazon ECS is supported. For more information, see `AWS Fargate on Amazon ECS <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html>`_ in the *Amazon ECS Developer Guide* .
            :param network_configuration: This structure specifies the network configuration for an ECS task.
            :param placement_constraints: An array of placement constraint objects to use for the task. You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).
            :param placement_strategy: The task placement strategy for a task or service.
            :param platform_version: Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as ``1.1.0`` .
            :param propagate_tags: Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the Amazon ECS ```TagResource`` <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html>`_ API action.
            :param reference_id: The reference ID to use for the task.
            :param tags: The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. For more information, see ```RunTask`` <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html>`_ in the *Amazon ECS API Reference* .
            :param task_count: The number of tasks to create based on ``TaskDefinition`` . The default is ``1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                # tags: Any
                
                ecs_parameters_property = scheduler.CfnSchedule.EcsParametersProperty(
                    task_definition_arn="taskDefinitionArn",
                
                    # the properties below are optional
                    capacity_provider_strategy=[scheduler.CfnSchedule.CapacityProviderStrategyItemProperty(
                        capacity_provider="capacityProvider",
                
                        # the properties below are optional
                        base=123,
                        weight=123
                    )],
                    enable_ecs_managed_tags=False,
                    enable_execute_command=False,
                    group="group",
                    launch_type="launchType",
                    network_configuration=scheduler.CfnSchedule.NetworkConfigurationProperty(
                        awsvpc_configuration=scheduler.CfnSchedule.AwsVpcConfigurationProperty(
                            subnets=["subnets"],
                
                            # the properties below are optional
                            assign_public_ip="assignPublicIp",
                            security_groups=["securityGroups"]
                        )
                    ),
                    placement_constraints=[scheduler.CfnSchedule.PlacementConstraintProperty(
                        expression="expression",
                        type="type"
                    )],
                    placement_strategy=[scheduler.CfnSchedule.PlacementStrategyProperty(
                        field="field",
                        type="type"
                    )],
                    platform_version="platformVersion",
                    propagate_tags="propagateTags",
                    reference_id="referenceId",
                    tags=tags,
                    task_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9dc612a243a7e6a4107ac15e844d139b177440cb37d514af299c8365e71f4cf1)
                check_type(argname="argument task_definition_arn", value=task_definition_arn, expected_type=type_hints["task_definition_arn"])
                check_type(argname="argument capacity_provider_strategy", value=capacity_provider_strategy, expected_type=type_hints["capacity_provider_strategy"])
                check_type(argname="argument enable_ecs_managed_tags", value=enable_ecs_managed_tags, expected_type=type_hints["enable_ecs_managed_tags"])
                check_type(argname="argument enable_execute_command", value=enable_execute_command, expected_type=type_hints["enable_execute_command"])
                check_type(argname="argument group", value=group, expected_type=type_hints["group"])
                check_type(argname="argument launch_type", value=launch_type, expected_type=type_hints["launch_type"])
                check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
                check_type(argname="argument placement_constraints", value=placement_constraints, expected_type=type_hints["placement_constraints"])
                check_type(argname="argument placement_strategy", value=placement_strategy, expected_type=type_hints["placement_strategy"])
                check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
                check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
                check_type(argname="argument reference_id", value=reference_id, expected_type=type_hints["reference_id"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
                check_type(argname="argument task_count", value=task_count, expected_type=type_hints["task_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "task_definition_arn": task_definition_arn,
            }
            if capacity_provider_strategy is not None:
                self._values["capacity_provider_strategy"] = capacity_provider_strategy
            if enable_ecs_managed_tags is not None:
                self._values["enable_ecs_managed_tags"] = enable_ecs_managed_tags
            if enable_execute_command is not None:
                self._values["enable_execute_command"] = enable_execute_command
            if group is not None:
                self._values["group"] = group
            if launch_type is not None:
                self._values["launch_type"] = launch_type
            if network_configuration is not None:
                self._values["network_configuration"] = network_configuration
            if placement_constraints is not None:
                self._values["placement_constraints"] = placement_constraints
            if placement_strategy is not None:
                self._values["placement_strategy"] = placement_strategy
            if platform_version is not None:
                self._values["platform_version"] = platform_version
            if propagate_tags is not None:
                self._values["propagate_tags"] = propagate_tags
            if reference_id is not None:
                self._values["reference_id"] = reference_id
            if tags is not None:
                self._values["tags"] = tags
            if task_count is not None:
                self._values["task_count"] = task_count

        @builtins.property
        def task_definition_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the task definition to use if the event target is an Amazon ECS task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-taskdefinitionarn
            '''
            result = self._values.get("task_definition_arn")
            assert result is not None, "Required property 'task_definition_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def capacity_provider_strategy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSchedule.CapacityProviderStrategyItemProperty"]]]]:
            '''The capacity provider strategy to use for the task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-capacityproviderstrategy
            '''
            result = self._values.get("capacity_provider_strategy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSchedule.CapacityProviderStrategyItemProperty"]]]], result)

        @builtins.property
        def enable_ecs_managed_tags(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether to enable Amazon ECS managed tags for the task.

            For more information, see `Tagging Your Amazon ECS Resources <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html>`_ in the *Amazon ECS Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-enableecsmanagedtags
            '''
            result = self._values.get("enable_ecs_managed_tags")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def enable_execute_command(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether or not to enable the execute command functionality for the containers in this task.

            If true, this enables execute command functionality on all containers in the task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-enableexecutecommand
            '''
            result = self._values.get("enable_execute_command")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def group(self) -> typing.Optional[builtins.str]:
            '''Specifies an Amazon ECS task group for the task.

            The maximum length is 255 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-group
            '''
            result = self._values.get("group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_type(self) -> typing.Optional[builtins.str]:
            '''Specifies the launch type on which your task is running.

            The launch type that you specify here must match one of the launch type (compatibilities) of the target task. The ``FARGATE`` value is supported only in the Regions where Fargate with Amazon ECS is supported. For more information, see `AWS Fargate on Amazon ECS <https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html>`_ in the *Amazon ECS Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-launchtype
            '''
            result = self._values.get("launch_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def network_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.NetworkConfigurationProperty"]]:
            '''This structure specifies the network configuration for an ECS task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-networkconfiguration
            '''
            result = self._values.get("network_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.NetworkConfigurationProperty"]], result)

        @builtins.property
        def placement_constraints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSchedule.PlacementConstraintProperty"]]]]:
            '''An array of placement constraint objects to use for the task.

            You can specify up to 10 constraints per task (including constraints in the task definition and those specified at runtime).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-placementconstraints
            '''
            result = self._values.get("placement_constraints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSchedule.PlacementConstraintProperty"]]]], result)

        @builtins.property
        def placement_strategy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSchedule.PlacementStrategyProperty"]]]]:
            '''The task placement strategy for a task or service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-placementstrategy
            '''
            result = self._values.get("placement_strategy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSchedule.PlacementStrategyProperty"]]]], result)

        @builtins.property
        def platform_version(self) -> typing.Optional[builtins.str]:
            '''Specifies the platform version for the task.

            Specify only the numeric portion of the platform version, such as ``1.1.0`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-platformversion
            '''
            result = self._values.get("platform_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def propagate_tags(self) -> typing.Optional[builtins.str]:
            '''Specifies whether to propagate the tags from the task definition to the task.

            If no value is specified, the tags are not propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the Amazon ECS ```TagResource`` <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html>`_ API action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-propagatetags
            '''
            result = self._values.get("propagate_tags")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def reference_id(self) -> typing.Optional[builtins.str]:
            '''The reference ID to use for the task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-referenceid
            '''
            result = self._values.get("reference_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Any:
            '''The metadata that you apply to the task to help you categorize and organize them.

            Each tag consists of a key and an optional value, both of which you define. For more information, see ```RunTask`` <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html>`_ in the *Amazon ECS API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Any, result)

        @builtins.property
        def task_count(self) -> typing.Optional[jsii.Number]:
            '''The number of tasks to create based on ``TaskDefinition`` .

            The default is ``1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-ecsparameters.html#cfn-scheduler-schedule-ecsparameters-taskcount
            '''
            result = self._values.get("task_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EcsParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.EventBridgeParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"detail_type": "detailType", "source": "source"},
    )
    class EventBridgeParametersProperty:
        def __init__(self, *, detail_type: builtins.str, source: builtins.str) -> None:
            '''The templated target type for the EventBridge ```PutEvents`` <https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html>`_ API operation.

            :param detail_type: A free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail.
            :param source: The source of the event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-eventbridgeparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                event_bridge_parameters_property = scheduler.CfnSchedule.EventBridgeParametersProperty(
                    detail_type="detailType",
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0e0c05434c8347bffb5179e8c9bc22fdc3ff4fdae681d5b9d995e0f7c8c1900)
                check_type(argname="argument detail_type", value=detail_type, expected_type=type_hints["detail_type"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "detail_type": detail_type,
                "source": source,
            }

        @builtins.property
        def detail_type(self) -> builtins.str:
            '''A free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-eventbridgeparameters.html#cfn-scheduler-schedule-eventbridgeparameters-detailtype
            '''
            result = self._values.get("detail_type")
            assert result is not None, "Required property 'detail_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source(self) -> builtins.str:
            '''The source of the event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-eventbridgeparameters.html#cfn-scheduler-schedule-eventbridgeparameters-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventBridgeParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.FlexibleTimeWindowProperty",
        jsii_struct_bases=[],
        name_mapping={
            "mode": "mode",
            "maximum_window_in_minutes": "maximumWindowInMinutes",
        },
    )
    class FlexibleTimeWindowProperty:
        def __init__(
            self,
            *,
            mode: builtins.str,
            maximum_window_in_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Allows you to configure a time window during which EventBridge Scheduler invokes the schedule.

            :param mode: Determines whether the schedule is invoked within a flexible time window. You must use quotation marks when you specify this value in your JSON or YAML template. *Allowed Values* : ``"OFF"`` | ``"FLEXIBLE"``
            :param maximum_window_in_minutes: The maximum time window during which a schedule can be invoked. *Minimum* : ``1`` *Maximum* : ``1440``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-flexibletimewindow.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                flexible_time_window_property = scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                    mode="mode",
                
                    # the properties below are optional
                    maximum_window_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7d4dffb710d1a3208f37cc6de0f2cddceb53e1178391bdc54cfedb8ca6626ec4)
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
                check_type(argname="argument maximum_window_in_minutes", value=maximum_window_in_minutes, expected_type=type_hints["maximum_window_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mode": mode,
            }
            if maximum_window_in_minutes is not None:
                self._values["maximum_window_in_minutes"] = maximum_window_in_minutes

        @builtins.property
        def mode(self) -> builtins.str:
            '''Determines whether the schedule is invoked within a flexible time window.

            You must use quotation marks when you specify this value in your JSON or YAML template.

            *Allowed Values* : ``"OFF"`` | ``"FLEXIBLE"``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-flexibletimewindow.html#cfn-scheduler-schedule-flexibletimewindow-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def maximum_window_in_minutes(self) -> typing.Optional[jsii.Number]:
            '''The maximum time window during which a schedule can be invoked.

            *Minimum* : ``1``

            *Maximum* : ``1440``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-flexibletimewindow.html#cfn-scheduler-schedule-flexibletimewindow-maximumwindowinminutes
            '''
            result = self._values.get("maximum_window_in_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlexibleTimeWindowProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.KinesisParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"partition_key": "partitionKey"},
    )
    class KinesisParametersProperty:
        def __init__(self, *, partition_key: builtins.str) -> None:
            '''The templated target type for the Amazon Kinesis ```PutRecord`` <https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html>`_ API operation.

            :param partition_key: Specifies the shard to which EventBridge Scheduler sends the event. For more information, see `Amazon Kinesis Data Streams terminology and concepts <https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html>`_ in the *Amazon Kinesis Streams Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-kinesisparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                kinesis_parameters_property = scheduler.CfnSchedule.KinesisParametersProperty(
                    partition_key="partitionKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__21a3b10246bef07a2f7fc56bf58e08c66b0fd77f7770804a87bf867fa8541cbb)
                check_type(argname="argument partition_key", value=partition_key, expected_type=type_hints["partition_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "partition_key": partition_key,
            }

        @builtins.property
        def partition_key(self) -> builtins.str:
            '''Specifies the shard to which EventBridge Scheduler sends the event.

            For more information, see `Amazon Kinesis Data Streams terminology and concepts <https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html>`_ in the *Amazon Kinesis Streams Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-kinesisparameters.html#cfn-scheduler-schedule-kinesisparameters-partitionkey
            '''
            result = self._values.get("partition_key")
            assert result is not None, "Required property 'partition_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"awsvpc_configuration": "awsvpcConfiguration"},
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            awsvpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedule.AwsVpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the network configuration for an ECS task.

            :param awsvpc_configuration: Specifies the Amazon VPC subnets and security groups for the task, and whether a public IP address is to be used. This structure is relevant only for ECS tasks that use the awsvpc network mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-networkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                network_configuration_property = scheduler.CfnSchedule.NetworkConfigurationProperty(
                    awsvpc_configuration=scheduler.CfnSchedule.AwsVpcConfigurationProperty(
                        subnets=["subnets"],
                
                        # the properties below are optional
                        assign_public_ip="assignPublicIp",
                        security_groups=["securityGroups"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__428ddbfd1435a3560f182001dfcf151c620cba65c309e87341f84eb7d60ba492)
                check_type(argname="argument awsvpc_configuration", value=awsvpc_configuration, expected_type=type_hints["awsvpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if awsvpc_configuration is not None:
                self._values["awsvpc_configuration"] = awsvpc_configuration

        @builtins.property
        def awsvpc_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.AwsVpcConfigurationProperty"]]:
            '''Specifies the Amazon VPC subnets and security groups for the task, and whether a public IP address is to be used.

            This structure is relevant only for ECS tasks that use the awsvpc network mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-networkconfiguration.html#cfn-scheduler-schedule-networkconfiguration-awsvpcconfiguration
            '''
            result = self._values.get("awsvpc_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.AwsVpcConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.PlacementConstraintProperty",
        jsii_struct_bases=[],
        name_mapping={"expression": "expression", "type": "type"},
    )
    class PlacementConstraintProperty:
        def __init__(
            self,
            *,
            expression: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object representing a constraint on task placement.

            :param expression: A cluster query language expression to apply to the constraint. You cannot specify an expression if the constraint type is ``distinctInstance`` . For more information, see `Cluster query language <https://docs.aws.amazon.com/latest/developerguide/cluster-query-language.html>`_ in the *Amazon ECS Developer Guide* .
            :param type: The type of constraint. Use ``distinctInstance`` to ensure that each task in a particular group is running on a different container instance. Use ``memberOf`` to restrict the selection to a group of valid candidates.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementconstraint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                placement_constraint_property = scheduler.CfnSchedule.PlacementConstraintProperty(
                    expression="expression",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb19941ef1169a4cc78daf82b7ea64663f5a28f890fbeded34448dd3f0a3c16f)
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if expression is not None:
                self._values["expression"] = expression
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def expression(self) -> typing.Optional[builtins.str]:
            '''A cluster query language expression to apply to the constraint.

            You cannot specify an expression if the constraint type is ``distinctInstance`` . For more information, see `Cluster query language <https://docs.aws.amazon.com/latest/developerguide/cluster-query-language.html>`_ in the *Amazon ECS Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementconstraint.html#cfn-scheduler-schedule-placementconstraint-expression
            '''
            result = self._values.get("expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of constraint.

            Use ``distinctInstance`` to ensure that each task in a particular group is running on a different container instance. Use ``memberOf`` to restrict the selection to a group of valid candidates.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementconstraint.html#cfn-scheduler-schedule-placementconstraint-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PlacementConstraintProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.PlacementStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={"field": "field", "type": "type"},
    )
    class PlacementStrategyProperty:
        def __init__(
            self,
            *,
            field: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The task placement strategy for a task or service.

            :param field: The field to apply the placement strategy against. For the spread placement strategy, valid values are ``instanceId`` (or ``instanceId`` , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as ``attribute:ecs.availability-zone`` . For the binpack placement strategy, valid values are ``cpu`` and ``memory`` . For the random placement strategy, this field is not used.
            :param type: The type of placement strategy. The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementstrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                placement_strategy_property = scheduler.CfnSchedule.PlacementStrategyProperty(
                    field="field",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2d9dc80c7a08a059d79aa3db1c44bcc28c84872422d6fd991bbca1124a384865)
                check_type(argname="argument field", value=field, expected_type=type_hints["field"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if field is not None:
                self._values["field"] = field
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def field(self) -> typing.Optional[builtins.str]:
            '''The field to apply the placement strategy against.

            For the spread placement strategy, valid values are ``instanceId`` (or ``instanceId`` , which has the same effect), or any platform or custom attribute that is applied to a container instance, such as ``attribute:ecs.availability-zone`` . For the binpack placement strategy, valid values are ``cpu`` and ``memory`` . For the random placement strategy, this field is not used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementstrategy.html#cfn-scheduler-schedule-placementstrategy-field
            '''
            result = self._values.get("field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of placement strategy.

            The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-placementstrategy.html#cfn-scheduler-schedule-placementstrategy-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PlacementStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.RetryPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "maximum_event_age_in_seconds": "maximumEventAgeInSeconds",
            "maximum_retry_attempts": "maximumRetryAttempts",
        },
    )
    class RetryPolicyProperty:
        def __init__(
            self,
            *,
            maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
            maximum_retry_attempts: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''A ``RetryPolicy`` object that includes information about the retry policy settings, including the maximum age of an event, and the maximum number of times EventBridge Scheduler will try to deliver the event to a target.

            :param maximum_event_age_in_seconds: The maximum amount of time, in seconds, to continue to make retry attempts.
            :param maximum_retry_attempts: The maximum number of retry attempts to make before the request fails. Retry attempts with exponential backoff continue until either the maximum number of attempts is made or until the duration of the ``MaximumEventAgeInSeconds`` is reached.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-retrypolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                retry_policy_property = scheduler.CfnSchedule.RetryPolicyProperty(
                    maximum_event_age_in_seconds=123,
                    maximum_retry_attempts=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb66e495a2f0291cd0e58a71fc127fa67ed8d10f2d977b132a1770f7b3a1f92d)
                check_type(argname="argument maximum_event_age_in_seconds", value=maximum_event_age_in_seconds, expected_type=type_hints["maximum_event_age_in_seconds"])
                check_type(argname="argument maximum_retry_attempts", value=maximum_retry_attempts, expected_type=type_hints["maximum_retry_attempts"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if maximum_event_age_in_seconds is not None:
                self._values["maximum_event_age_in_seconds"] = maximum_event_age_in_seconds
            if maximum_retry_attempts is not None:
                self._values["maximum_retry_attempts"] = maximum_retry_attempts

        @builtins.property
        def maximum_event_age_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of time, in seconds, to continue to make retry attempts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-retrypolicy.html#cfn-scheduler-schedule-retrypolicy-maximumeventageinseconds
            '''
            result = self._values.get("maximum_event_age_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_retry_attempts(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of retry attempts to make before the request fails.

            Retry attempts with exponential backoff continue until either the maximum number of attempts is made or until the duration of the ``MaximumEventAgeInSeconds`` is reached.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-retrypolicy.html#cfn-scheduler-schedule-retrypolicy-maximumretryattempts
            '''
            result = self._values.get("maximum_retry_attempts")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetryPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.SageMakerPipelineParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class SageMakerPipelineParameterProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''The name and value pair of a parameter to use to start execution of a SageMaker Model Building Pipeline.

            :param name: Name of parameter to start execution of a SageMaker Model Building Pipeline.
            :param value: Value of parameter to start execution of a SageMaker Model Building Pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                sage_maker_pipeline_parameter_property = scheduler.CfnSchedule.SageMakerPipelineParameterProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c29c10cb7c0592826b32a3dc5e923a7c8d2f8b6bd9a0fe45759d650269d9f4d)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''Name of parameter to start execution of a SageMaker Model Building Pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameter.html#cfn-scheduler-schedule-sagemakerpipelineparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''Value of parameter to start execution of a SageMaker Model Building Pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameter.html#cfn-scheduler-schedule-sagemakerpipelineparameter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SageMakerPipelineParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.SageMakerPipelineParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"pipeline_parameter_list": "pipelineParameterList"},
    )
    class SageMakerPipelineParametersProperty:
        def __init__(
            self,
            *,
            pipeline_parameter_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedule.SageMakerPipelineParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The templated target type for the Amazon SageMaker ```StartPipelineExecution`` <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartPipelineExecution.html>`_ API operation.

            :param pipeline_parameter_list: List of parameter names and values to use when executing the SageMaker Model Building Pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                sage_maker_pipeline_parameters_property = scheduler.CfnSchedule.SageMakerPipelineParametersProperty(
                    pipeline_parameter_list=[scheduler.CfnSchedule.SageMakerPipelineParameterProperty(
                        name="name",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a0de727f226b2279098ba22fdf1aa02e57d81187ed9063acc8d789604e1a7f88)
                check_type(argname="argument pipeline_parameter_list", value=pipeline_parameter_list, expected_type=type_hints["pipeline_parameter_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if pipeline_parameter_list is not None:
                self._values["pipeline_parameter_list"] = pipeline_parameter_list

        @builtins.property
        def pipeline_parameter_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSchedule.SageMakerPipelineParameterProperty"]]]]:
            '''List of parameter names and values to use when executing the SageMaker Model Building Pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameters.html#cfn-scheduler-schedule-sagemakerpipelineparameters-pipelineparameterlist
            '''
            result = self._values.get("pipeline_parameter_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSchedule.SageMakerPipelineParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SageMakerPipelineParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.SqsParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"message_group_id": "messageGroupId"},
    )
    class SqsParametersProperty:
        def __init__(
            self,
            *,
            message_group_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The templated target type for the Amazon SQS ```SendMessage`` <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html>`_ API operation. Contains the message group ID to use when the target is a FIFO queue. If you specify an Amazon SQS FIFO queue as a target, the queue must have content-based deduplication enabled. For more information, see `Using the Amazon SQS message deduplication ID <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html>`_ in the *Amazon SQS Developer Guide* .

            :param message_group_id: The FIFO message group ID to use as the target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sqsparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                sqs_parameters_property = scheduler.CfnSchedule.SqsParametersProperty(
                    message_group_id="messageGroupId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__13762215f810c9b64aba5ce7769b7babcff69eaa35d5d19f712b7515022da7fb)
                check_type(argname="argument message_group_id", value=message_group_id, expected_type=type_hints["message_group_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if message_group_id is not None:
                self._values["message_group_id"] = message_group_id

        @builtins.property
        def message_group_id(self) -> typing.Optional[builtins.str]:
            '''The FIFO message group ID to use as the target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sqsparameters.html#cfn-scheduler-schedule-sqsparameters-messagegroupid
            '''
            result = self._values.get("message_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqsParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_scheduler.CfnSchedule.TargetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "role_arn": "roleArn",
            "dead_letter_config": "deadLetterConfig",
            "ecs_parameters": "ecsParameters",
            "event_bridge_parameters": "eventBridgeParameters",
            "input": "input",
            "kinesis_parameters": "kinesisParameters",
            "retry_policy": "retryPolicy",
            "sage_maker_pipeline_parameters": "sageMakerPipelineParameters",
            "sqs_parameters": "sqsParameters",
        },
    )
    class TargetProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            role_arn: builtins.str,
            dead_letter_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedule.DeadLetterConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ecs_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedule.EcsParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            event_bridge_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedule.EventBridgeParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            input: typing.Optional[builtins.str] = None,
            kinesis_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedule.KinesisParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedule.RetryPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sage_maker_pipeline_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedule.SageMakerPipelineParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sqs_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSchedule.SqsParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The schedule's target.

            EventBridge Scheduler supports templated target that invoke common API operations, as well as universal targets that you can customize to invoke over 6,000 API operations across more than 270 services. You can only specify one templated or universal target for a schedule.

            :param arn: The Amazon Resource Name (ARN) of the target.
            :param role_arn: The Amazon Resource Name (ARN) of the IAM role that EventBridge Scheduler will use for this target when the schedule is invoked.
            :param dead_letter_config: An object that contains information about an Amazon SQS queue that EventBridge Scheduler uses as a dead-letter queue for your schedule. If specified, EventBridge Scheduler delivers failed events that could not be successfully delivered to a target to the queue.
            :param ecs_parameters: The templated target type for the Amazon ECS ```RunTask`` <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html>`_ API operation.
            :param event_bridge_parameters: The templated target type for the EventBridge ```PutEvents`` <https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html>`_ API operation.
            :param input: The text, or well-formed JSON, passed to the target. If you are configuring a templated Lambda , AWS Step Functions , or Amazon EventBridge target, the input must be a well-formed JSON. For all other target types, a JSON is not required. If you do not specify anything for this field, Amazon EventBridge Scheduler delivers a default notification to the target.
            :param kinesis_parameters: The templated target type for the Amazon Kinesis ```PutRecord`` <https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html>`_ API operation.
            :param retry_policy: A ``RetryPolicy`` object that includes information about the retry policy settings, including the maximum age of an event, and the maximum number of times EventBridge Scheduler will try to deliver the event to a target.
            :param sage_maker_pipeline_parameters: The templated target type for the Amazon SageMaker ```StartPipelineExecution`` <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartPipelineExecution.html>`_ API operation.
            :param sqs_parameters: The templated target type for the Amazon SQS ```SendMessage`` <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html>`_ API operation. Contains the message group ID to use when the target is a FIFO queue. If you specify an Amazon SQS FIFO queue as a target, the queue must have content-based deduplication enabled. For more information, see `Using the Amazon SQS message deduplication ID <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html>`_ in the *Amazon SQS Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_scheduler as scheduler
                
                # tags: Any
                
                target_property = scheduler.CfnSchedule.TargetProperty(
                    arn="arn",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    dead_letter_config=scheduler.CfnSchedule.DeadLetterConfigProperty(
                        arn="arn"
                    ),
                    ecs_parameters=scheduler.CfnSchedule.EcsParametersProperty(
                        task_definition_arn="taskDefinitionArn",
                
                        # the properties below are optional
                        capacity_provider_strategy=[scheduler.CfnSchedule.CapacityProviderStrategyItemProperty(
                            capacity_provider="capacityProvider",
                
                            # the properties below are optional
                            base=123,
                            weight=123
                        )],
                        enable_ecs_managed_tags=False,
                        enable_execute_command=False,
                        group="group",
                        launch_type="launchType",
                        network_configuration=scheduler.CfnSchedule.NetworkConfigurationProperty(
                            awsvpc_configuration=scheduler.CfnSchedule.AwsVpcConfigurationProperty(
                                subnets=["subnets"],
                
                                # the properties below are optional
                                assign_public_ip="assignPublicIp",
                                security_groups=["securityGroups"]
                            )
                        ),
                        placement_constraints=[scheduler.CfnSchedule.PlacementConstraintProperty(
                            expression="expression",
                            type="type"
                        )],
                        placement_strategy=[scheduler.CfnSchedule.PlacementStrategyProperty(
                            field="field",
                            type="type"
                        )],
                        platform_version="platformVersion",
                        propagate_tags="propagateTags",
                        reference_id="referenceId",
                        tags=tags,
                        task_count=123
                    ),
                    event_bridge_parameters=scheduler.CfnSchedule.EventBridgeParametersProperty(
                        detail_type="detailType",
                        source="source"
                    ),
                    input="input",
                    kinesis_parameters=scheduler.CfnSchedule.KinesisParametersProperty(
                        partition_key="partitionKey"
                    ),
                    retry_policy=scheduler.CfnSchedule.RetryPolicyProperty(
                        maximum_event_age_in_seconds=123,
                        maximum_retry_attempts=123
                    ),
                    sage_maker_pipeline_parameters=scheduler.CfnSchedule.SageMakerPipelineParametersProperty(
                        pipeline_parameter_list=[scheduler.CfnSchedule.SageMakerPipelineParameterProperty(
                            name="name",
                            value="value"
                        )]
                    ),
                    sqs_parameters=scheduler.CfnSchedule.SqsParametersProperty(
                        message_group_id="messageGroupId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bd5d0419478021d0554d24683f11134f17bb914856367055c32d004d8348a516)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument dead_letter_config", value=dead_letter_config, expected_type=type_hints["dead_letter_config"])
                check_type(argname="argument ecs_parameters", value=ecs_parameters, expected_type=type_hints["ecs_parameters"])
                check_type(argname="argument event_bridge_parameters", value=event_bridge_parameters, expected_type=type_hints["event_bridge_parameters"])
                check_type(argname="argument input", value=input, expected_type=type_hints["input"])
                check_type(argname="argument kinesis_parameters", value=kinesis_parameters, expected_type=type_hints["kinesis_parameters"])
                check_type(argname="argument retry_policy", value=retry_policy, expected_type=type_hints["retry_policy"])
                check_type(argname="argument sage_maker_pipeline_parameters", value=sage_maker_pipeline_parameters, expected_type=type_hints["sage_maker_pipeline_parameters"])
                check_type(argname="argument sqs_parameters", value=sqs_parameters, expected_type=type_hints["sqs_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "arn": arn,
                "role_arn": role_arn,
            }
            if dead_letter_config is not None:
                self._values["dead_letter_config"] = dead_letter_config
            if ecs_parameters is not None:
                self._values["ecs_parameters"] = ecs_parameters
            if event_bridge_parameters is not None:
                self._values["event_bridge_parameters"] = event_bridge_parameters
            if input is not None:
                self._values["input"] = input
            if kinesis_parameters is not None:
                self._values["kinesis_parameters"] = kinesis_parameters
            if retry_policy is not None:
                self._values["retry_policy"] = retry_policy
            if sage_maker_pipeline_parameters is not None:
                self._values["sage_maker_pipeline_parameters"] = sage_maker_pipeline_parameters
            if sqs_parameters is not None:
                self._values["sqs_parameters"] = sqs_parameters

        @builtins.property
        def arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the IAM role that EventBridge Scheduler will use for this target when the schedule is invoked.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dead_letter_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.DeadLetterConfigProperty"]]:
            '''An object that contains information about an Amazon SQS queue that EventBridge Scheduler uses as a dead-letter queue for your schedule.

            If specified, EventBridge Scheduler delivers failed events that could not be successfully delivered to a target to the queue.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-deadletterconfig
            '''
            result = self._values.get("dead_letter_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.DeadLetterConfigProperty"]], result)

        @builtins.property
        def ecs_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.EcsParametersProperty"]]:
            '''The templated target type for the Amazon ECS ```RunTask`` <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html>`_ API operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-ecsparameters
            '''
            result = self._values.get("ecs_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.EcsParametersProperty"]], result)

        @builtins.property
        def event_bridge_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.EventBridgeParametersProperty"]]:
            '''The templated target type for the EventBridge ```PutEvents`` <https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html>`_ API operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-eventbridgeparameters
            '''
            result = self._values.get("event_bridge_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.EventBridgeParametersProperty"]], result)

        @builtins.property
        def input(self) -> typing.Optional[builtins.str]:
            '''The text, or well-formed JSON, passed to the target.

            If you are configuring a templated Lambda , AWS Step Functions , or Amazon EventBridge target, the input must be a well-formed JSON. For all other target types, a JSON is not required. If you do not specify anything for this field, Amazon EventBridge Scheduler delivers a default notification to the target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-input
            '''
            result = self._values.get("input")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kinesis_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.KinesisParametersProperty"]]:
            '''The templated target type for the Amazon Kinesis ```PutRecord`` <https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html>`_ API operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-kinesisparameters
            '''
            result = self._values.get("kinesis_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.KinesisParametersProperty"]], result)

        @builtins.property
        def retry_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.RetryPolicyProperty"]]:
            '''A ``RetryPolicy`` object that includes information about the retry policy settings, including the maximum age of an event, and the maximum number of times EventBridge Scheduler will try to deliver the event to a target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-retrypolicy
            '''
            result = self._values.get("retry_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.RetryPolicyProperty"]], result)

        @builtins.property
        def sage_maker_pipeline_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.SageMakerPipelineParametersProperty"]]:
            '''The templated target type for the Amazon SageMaker ```StartPipelineExecution`` <https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartPipelineExecution.html>`_ API operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-sagemakerpipelineparameters
            '''
            result = self._values.get("sage_maker_pipeline_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.SageMakerPipelineParametersProperty"]], result)

        @builtins.property
        def sqs_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.SqsParametersProperty"]]:
            '''The templated target type for the Amazon SQS ```SendMessage`` <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html>`_ API operation. Contains the message group ID to use when the target is a FIFO queue. If you specify an Amazon SQS FIFO queue as a target, the queue must have content-based deduplication enabled. For more information, see `Using the Amazon SQS message deduplication ID <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html>`_ in the *Amazon SQS Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-target.html#cfn-scheduler-schedule-target-sqsparameters
            '''
            result = self._values.get("sqs_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSchedule.SqsParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnScheduleGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler.CfnScheduleGroup",
):
    '''A *schedule group* is an Amazon EventBridge Scheduler resource you use to organize your schedules.

    Your AWS account comes with a ``default`` scheduler group. You associate a new schedule with the ``default`` group or with schedule groups that you create and manage. You can create up to `500 schedule groups <https://docs.aws.amazon.com/scheduler/latest/UserGuide/scheduler-quotas.html>`_ in your AWS account. With EventBridge Scheduler, you apply `tags <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ to schedule groups, not to individual schedules to organize your resources.

    For more information about managing schedule groups, see `Managing a schedule group <https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-group.html>`_ in the *EventBridge Scheduler User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html
    :cloudformationResource: AWS::Scheduler::ScheduleGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_scheduler as scheduler
        
        cfn_schedule_group = scheduler.CfnScheduleGroup(self, "MyCfnScheduleGroup",
            name="name",
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
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the schedule group.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55d5637c9b973d98ef3a23b13bf274e0a35bc07dfc27542f9b7185600a26a15e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScheduleGroupProps(name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e179ed3a5ae801985e05b869adcf8daec39217aada45fa23844dd021dea92bda)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a163f755c33c470bd9bc8ba9ec2282566382000d7a5adbc8bba7aa9bd8e707d3)
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
        '''The Amazon Resource Name (ARN) of the schedule group.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationDate")
    def attr_creation_date(self) -> builtins.str:
        '''The date and time at which the schedule group was created.

        :cloudformationAttribute: CreationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationDate")
    def attr_last_modification_date(self) -> builtins.str:
        '''The time at which the schedule group was last modified.

        :cloudformationAttribute: LastModificationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''Specifies the state of the schedule group.

        *Allowed Values* : ``ACTIVE`` | ``DELETING``

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the schedule group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e895b806668d11dd73b56d4fec496161e9b77b48c3e3475d06f4798d8a636529)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c803209b899e8ad5a9aaaa50de8f083948fedec73e43cc9c9b541cd5fdf20f5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler.CfnScheduleGroupProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "tags": "tags"},
)
class CfnScheduleGroupProps:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnScheduleGroup``.

        :param name: The name of the schedule group.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_scheduler as scheduler
            
            cfn_schedule_group_props = scheduler.CfnScheduleGroupProps(
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9ebba0a3ae0883796e2ff900e8a82e62b8e0870420b26e180905979808a13e7)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the schedule group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html#cfn-scheduler-schedulegroup-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedulegroup.html#cfn-scheduler-schedulegroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScheduleGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler.CfnScheduleProps",
    jsii_struct_bases=[],
    name_mapping={
        "flexible_time_window": "flexibleTimeWindow",
        "schedule_expression": "scheduleExpression",
        "target": "target",
        "description": "description",
        "end_date": "endDate",
        "group_name": "groupName",
        "kms_key_arn": "kmsKeyArn",
        "name": "name",
        "schedule_expression_timezone": "scheduleExpressionTimezone",
        "start_date": "startDate",
        "state": "state",
    },
)
class CfnScheduleProps:
    def __init__(
        self,
        *,
        flexible_time_window: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.FlexibleTimeWindowProperty, typing.Dict[builtins.str, typing.Any]]],
        schedule_expression: builtins.str,
        target: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.TargetProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        end_date: typing.Optional[builtins.str] = None,
        group_name: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        schedule_expression_timezone: typing.Optional[builtins.str] = None,
        start_date: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSchedule``.

        :param flexible_time_window: Allows you to configure a time window during which EventBridge Scheduler invokes the schedule.
        :param schedule_expression: The expression that defines when the schedule runs. The following formats are supported. - ``at`` expression - ``at(yyyy-mm-ddThh:mm:ss)`` - ``rate`` expression - ``rate(value unit)`` - ``cron`` expression - ``cron(fields)`` You can use ``at`` expressions to create one-time schedules that invoke a target once, at the time and in the time zone, that you specify. You can use ``rate`` and ``cron`` expressions to create recurring schedules. Rate-based schedules are useful when you want to invoke a target at regular intervals, such as every 15 minutes or every five days. Cron-based schedules are useful when you want to invoke a target periodically at a specific time, such as at 8:00 am (UTC+0) every 1st day of the month. A ``cron`` expression consists of six fields separated by white spaces: ``(minutes hours day_of_month month day_of_week year)`` . A ``rate`` expression consists of a *value* as a positive integer, and a *unit* with the following options: ``minute`` | ``minutes`` | ``hour`` | ``hours`` | ``day`` | ``days`` For more information and examples, see `Schedule types on EventBridge Scheduler <https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html>`_ in the *EventBridge Scheduler User Guide* .
        :param target: The schedule's target details.
        :param description: The description you specify for the schedule.
        :param end_date: The date, in UTC, before which the schedule can invoke its target. Depending on the schedule's recurrence expression, invocations might stop on, or before, the ``EndDate`` you specify. EventBridge Scheduler ignores ``EndDate`` for one-time schedules.
        :param group_name: The name of the schedule group associated with this schedule.
        :param kms_key_arn: The Amazon Resource Name (ARN) for the customer managed KMS key that EventBridge Scheduler will use to encrypt and decrypt your data.
        :param name: The name of the schedule.
        :param schedule_expression_timezone: The timezone in which the scheduling expression is evaluated.
        :param start_date: The date, in UTC, after which the schedule can begin invoking its target. Depending on the schedule's recurrence expression, invocations might occur on, or after, the ``StartDate`` you specify. EventBridge Scheduler ignores ``StartDate`` for one-time schedules.
        :param state: Specifies whether the schedule is enabled or disabled. *Allowed Values* : ``ENABLED`` | ``DISABLED``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_scheduler as scheduler
            
            # tags: Any
            
            cfn_schedule_props = scheduler.CfnScheduleProps(
                flexible_time_window=scheduler.CfnSchedule.FlexibleTimeWindowProperty(
                    mode="mode",
            
                    # the properties below are optional
                    maximum_window_in_minutes=123
                ),
                schedule_expression="scheduleExpression",
                target=scheduler.CfnSchedule.TargetProperty(
                    arn="arn",
                    role_arn="roleArn",
            
                    # the properties below are optional
                    dead_letter_config=scheduler.CfnSchedule.DeadLetterConfigProperty(
                        arn="arn"
                    ),
                    ecs_parameters=scheduler.CfnSchedule.EcsParametersProperty(
                        task_definition_arn="taskDefinitionArn",
            
                        # the properties below are optional
                        capacity_provider_strategy=[scheduler.CfnSchedule.CapacityProviderStrategyItemProperty(
                            capacity_provider="capacityProvider",
            
                            # the properties below are optional
                            base=123,
                            weight=123
                        )],
                        enable_ecs_managed_tags=False,
                        enable_execute_command=False,
                        group="group",
                        launch_type="launchType",
                        network_configuration=scheduler.CfnSchedule.NetworkConfigurationProperty(
                            awsvpc_configuration=scheduler.CfnSchedule.AwsVpcConfigurationProperty(
                                subnets=["subnets"],
            
                                # the properties below are optional
                                assign_public_ip="assignPublicIp",
                                security_groups=["securityGroups"]
                            )
                        ),
                        placement_constraints=[scheduler.CfnSchedule.PlacementConstraintProperty(
                            expression="expression",
                            type="type"
                        )],
                        placement_strategy=[scheduler.CfnSchedule.PlacementStrategyProperty(
                            field="field",
                            type="type"
                        )],
                        platform_version="platformVersion",
                        propagate_tags="propagateTags",
                        reference_id="referenceId",
                        tags=tags,
                        task_count=123
                    ),
                    event_bridge_parameters=scheduler.CfnSchedule.EventBridgeParametersProperty(
                        detail_type="detailType",
                        source="source"
                    ),
                    input="input",
                    kinesis_parameters=scheduler.CfnSchedule.KinesisParametersProperty(
                        partition_key="partitionKey"
                    ),
                    retry_policy=scheduler.CfnSchedule.RetryPolicyProperty(
                        maximum_event_age_in_seconds=123,
                        maximum_retry_attempts=123
                    ),
                    sage_maker_pipeline_parameters=scheduler.CfnSchedule.SageMakerPipelineParametersProperty(
                        pipeline_parameter_list=[scheduler.CfnSchedule.SageMakerPipelineParameterProperty(
                            name="name",
                            value="value"
                        )]
                    ),
                    sqs_parameters=scheduler.CfnSchedule.SqsParametersProperty(
                        message_group_id="messageGroupId"
                    )
                ),
            
                # the properties below are optional
                description="description",
                end_date="endDate",
                group_name="groupName",
                kms_key_arn="kmsKeyArn",
                name="name",
                schedule_expression_timezone="scheduleExpressionTimezone",
                start_date="startDate",
                state="state"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7259f3f17d67e55e8ad4459f637d0d8aa80d57d58cb928f6b0403a6097a4ecf1)
            check_type(argname="argument flexible_time_window", value=flexible_time_window, expected_type=type_hints["flexible_time_window"])
            check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument end_date", value=end_date, expected_type=type_hints["end_date"])
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schedule_expression_timezone", value=schedule_expression_timezone, expected_type=type_hints["schedule_expression_timezone"])
            check_type(argname="argument start_date", value=start_date, expected_type=type_hints["start_date"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flexible_time_window": flexible_time_window,
            "schedule_expression": schedule_expression,
            "target": target,
        }
        if description is not None:
            self._values["description"] = description
        if end_date is not None:
            self._values["end_date"] = end_date
        if group_name is not None:
            self._values["group_name"] = group_name
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if name is not None:
            self._values["name"] = name
        if schedule_expression_timezone is not None:
            self._values["schedule_expression_timezone"] = schedule_expression_timezone
        if start_date is not None:
            self._values["start_date"] = start_date
        if state is not None:
            self._values["state"] = state

    @builtins.property
    def flexible_time_window(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnSchedule.FlexibleTimeWindowProperty]:
        '''Allows you to configure a time window during which EventBridge Scheduler invokes the schedule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-flexibletimewindow
        '''
        result = self._values.get("flexible_time_window")
        assert result is not None, "Required property 'flexible_time_window' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnSchedule.FlexibleTimeWindowProperty], result)

    @builtins.property
    def schedule_expression(self) -> builtins.str:
        '''The expression that defines when the schedule runs. The following formats are supported.

        - ``at`` expression - ``at(yyyy-mm-ddThh:mm:ss)``
        - ``rate`` expression - ``rate(value unit)``
        - ``cron`` expression - ``cron(fields)``

        You can use ``at`` expressions to create one-time schedules that invoke a target once, at the time and in the time zone, that you specify. You can use ``rate`` and ``cron`` expressions to create recurring schedules. Rate-based schedules are useful when you want to invoke a target at regular intervals, such as every 15 minutes or every five days. Cron-based schedules are useful when you want to invoke a target periodically at a specific time, such as at 8:00 am (UTC+0) every 1st day of the month.

        A ``cron`` expression consists of six fields separated by white spaces: ``(minutes hours day_of_month month day_of_week year)`` .

        A ``rate`` expression consists of a *value* as a positive integer, and a *unit* with the following options: ``minute`` | ``minutes`` | ``hour`` | ``hours`` | ``day`` | ``days``

        For more information and examples, see `Schedule types on EventBridge Scheduler <https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html>`_ in the *EventBridge Scheduler User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-scheduleexpression
        '''
        result = self._values.get("schedule_expression")
        assert result is not None, "Required property 'schedule_expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> typing.Union[_IResolvable_da3f097b, CfnSchedule.TargetProperty]:
        '''The schedule's target details.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-target
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnSchedule.TargetProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description you specify for the schedule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def end_date(self) -> typing.Optional[builtins.str]:
        '''The date, in UTC, before which the schedule can invoke its target.

        Depending on the schedule's recurrence expression, invocations might stop on, or before, the ``EndDate`` you specify.
        EventBridge Scheduler ignores ``EndDate`` for one-time schedules.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-enddate
        '''
        result = self._values.get("end_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the schedule group associated with this schedule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-groupname
        '''
        result = self._values.get("group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the customer managed KMS key that EventBridge Scheduler will use to encrypt and decrypt your data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the schedule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_expression_timezone(self) -> typing.Optional[builtins.str]:
        '''The timezone in which the scheduling expression is evaluated.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-scheduleexpressiontimezone
        '''
        result = self._values.get("schedule_expression_timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_date(self) -> typing.Optional[builtins.str]:
        '''The date, in UTC, after which the schedule can begin invoking its target.

        Depending on the schedule's recurrence expression, invocations might occur on, or after, the ``StartDate`` you specify.
        EventBridge Scheduler ignores ``StartDate`` for one-time schedules.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-startdate
        '''
        result = self._values.get("start_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Specifies whether the schedule is enabled or disabled.

        *Allowed Values* : ``ENABLED`` | ``DISABLED``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html#cfn-scheduler-schedule-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScheduleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContextAttribute(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler.ContextAttribute",
):
    '''A set of convenient static methods representing the Scheduler Context Attributes.

    These Context Attributes keywords can be used inside a ScheduleTargetInput.

    :see: https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-context-attributes.html
    '''

    @jsii.member(jsii_name="fromName")
    @builtins.classmethod
    def from_name(cls, name: builtins.str) -> builtins.str:
        '''Escape hatch for other Context Attributes that may be added in the future.

        :param name: - name will replace xxx in <aws.scheduler.xxx>.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3ffc32f8d37e5b3c60f6299c8f15649e00e5778ef81be54ecc2ffbb99ac1bbc)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "fromName", [name]))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Convert the path to the field in the event pattern to JSON.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="attemptNumber")
    def attempt_number(cls) -> builtins.str:
        '''A counter that identifies the attempt number for the current invocation, for example, 1.'''
        return typing.cast(builtins.str, jsii.sget(cls, "attemptNumber"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="executionId")
    def execution_id(cls) -> builtins.str:
        '''The unique ID that EventBridge Scheduler assigns for each attempted invocation of a target, for example, d32c5kddcf5bb8c3.'''
        return typing.cast(builtins.str, jsii.sget(cls, "executionId"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="scheduleArn")
    def schedule_arn(cls) -> builtins.str:
        '''The ARN of the schedule.'''
        return typing.cast(builtins.str, jsii.sget(cls, "scheduleArn"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="scheduledTime")
    def scheduled_time(cls) -> builtins.str:
        '''The time you specified for the schedule to invoke its target, for example, 2022-03-22T18:59:43Z.'''
        return typing.cast(builtins.str, jsii.sget(cls, "scheduledTime"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler.CronOptionsWithTimezone",
    jsii_struct_bases=[_CronOptions_6401a7a0],
    name_mapping={
        "day": "day",
        "hour": "hour",
        "minute": "minute",
        "month": "month",
        "week_day": "weekDay",
        "year": "year",
        "time_zone": "timeZone",
    },
)
class CronOptionsWithTimezone(_CronOptions_6401a7a0):
    def __init__(
        self,
        *,
        day: typing.Optional[builtins.str] = None,
        hour: typing.Optional[builtins.str] = None,
        minute: typing.Optional[builtins.str] = None,
        month: typing.Optional[builtins.str] = None,
        week_day: typing.Optional[builtins.str] = None,
        year: typing.Optional[builtins.str] = None,
        time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
    ) -> None:
        '''Options to configure a cron expression.

        All fields are strings so you can use complex expressions. Absence of
        a field implies '*' or '?', whichever one is appropriate.

        :param day: The day of the month to run this rule at. Default: - Every day of the month
        :param hour: The hour to run this rule at. Default: - Every hour
        :param minute: The minute to run this rule at. Default: - Every minute
        :param month: The month to run this rule at. Default: - Every month
        :param week_day: The day of the week to run this rule at. Default: - Any day of the week
        :param year: The year to run this rule at. Default: - Every year
        :param time_zone: The timezone to run the schedule in. Default: - TimeZone.ETC_UTC

        :see: https://docs.aws.amazon.com/eventbridge/latest/userguide/scheduled-events.html#cron-expressions
        :exampleMetadata: infused

        Example::

            # target: targets.LambdaInvoke
            
            
            rate_based_schedule = Schedule(self, "Schedule",
                schedule=ScheduleExpression.rate(Duration.minutes(10)),
                target=target,
                description="This is a test rate-based schedule"
            )
            
            cron_based_schedule = Schedule(self, "Schedule",
                schedule=ScheduleExpression.cron(
                    minute="0",
                    hour="23",
                    day="20",
                    month="11",
                    time_zone=TimeZone.AMERICA_NEW_YORK
                ),
                target=target,
                description="This is a test cron-based schedule that will run at 11:00 PM, on day 20 of the month, only in November in New York timezone"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c87f71f166be27f7417012dedd810bd7b3cedb2ec7d0a0493ca36f93993f6c5b)
            check_type(argname="argument day", value=day, expected_type=type_hints["day"])
            check_type(argname="argument hour", value=hour, expected_type=type_hints["hour"])
            check_type(argname="argument minute", value=minute, expected_type=type_hints["minute"])
            check_type(argname="argument month", value=month, expected_type=type_hints["month"])
            check_type(argname="argument week_day", value=week_day, expected_type=type_hints["week_day"])
            check_type(argname="argument year", value=year, expected_type=type_hints["year"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if day is not None:
            self._values["day"] = day
        if hour is not None:
            self._values["hour"] = hour
        if minute is not None:
            self._values["minute"] = minute
        if month is not None:
            self._values["month"] = month
        if week_day is not None:
            self._values["week_day"] = week_day
        if year is not None:
            self._values["year"] = year
        if time_zone is not None:
            self._values["time_zone"] = time_zone

    @builtins.property
    def day(self) -> typing.Optional[builtins.str]:
        '''The day of the month to run this rule at.

        :default: - Every day of the month
        '''
        result = self._values.get("day")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hour(self) -> typing.Optional[builtins.str]:
        '''The hour to run this rule at.

        :default: - Every hour
        '''
        result = self._values.get("hour")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minute(self) -> typing.Optional[builtins.str]:
        '''The minute to run this rule at.

        :default: - Every minute
        '''
        result = self._values.get("minute")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def month(self) -> typing.Optional[builtins.str]:
        '''The month to run this rule at.

        :default: - Every month
        '''
        result = self._values.get("month")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def week_day(self) -> typing.Optional[builtins.str]:
        '''The day of the week to run this rule at.

        :default: - Any day of the week
        '''
        result = self._values.get("week_day")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def year(self) -> typing.Optional[builtins.str]:
        '''The year to run this rule at.

        :default: - Every year
        '''
        result = self._values.get("year")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[_TimeZone_cdd72ac9]:
        '''The timezone to run the schedule in.

        :default: - TimeZone.ETC_UTC
        '''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[_TimeZone_cdd72ac9], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CronOptionsWithTimezone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_scheduler.ISchedule")
class ISchedule(_IResource_c80c4260, typing_extensions.Protocol):
    '''Interface representing a created or an imported ``Schedule``.'''

    @builtins.property
    @jsii.member(jsii_name="scheduleArn")
    def schedule_arn(self) -> builtins.str:
        '''The arn of the schedule.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="scheduleName")
    def schedule_name(self) -> builtins.str:
        '''The name of the schedule.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="scheduleGroup")
    def schedule_group(self) -> typing.Optional["IScheduleGroup"]:
        '''The schedule group associated with this schedule.'''
        ...


class _IScheduleProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Interface representing a created or an imported ``Schedule``.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_scheduler.ISchedule"

    @builtins.property
    @jsii.member(jsii_name="scheduleArn")
    def schedule_arn(self) -> builtins.str:
        '''The arn of the schedule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "scheduleArn"))

    @builtins.property
    @jsii.member(jsii_name="scheduleName")
    def schedule_name(self) -> builtins.str:
        '''The name of the schedule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "scheduleName"))

    @builtins.property
    @jsii.member(jsii_name="scheduleGroup")
    def schedule_group(self) -> typing.Optional["IScheduleGroup"]:
        '''The schedule group associated with this schedule.'''
        return typing.cast(typing.Optional["IScheduleGroup"], jsii.get(self, "scheduleGroup"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchedule).__jsii_proxy_class__ = lambda : _IScheduleProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_scheduler.IScheduleGroup")
class IScheduleGroup(_IResource_c80c4260, typing_extensions.Protocol):
    '''Interface representing a created or an imported ``ScheduleGroup``.'''

    @builtins.property
    @jsii.member(jsii_name="scheduleGroupArn")
    def schedule_group_arn(self) -> builtins.str:
        '''The arn of the schedule group.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="scheduleGroupName")
    def schedule_group_name(self) -> builtins.str:
        '''The name of the schedule group.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the indicated permissions on this group to the given principal.

        :param grantee: -
        :param actions: -
        '''
        ...

    @jsii.member(jsii_name="grantDeleteSchedules")
    def grant_delete_schedules(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant delete schedule permission for schedules in this group to the given principal.

        :param identity: -
        '''
        ...

    @jsii.member(jsii_name="grantReadSchedules")
    def grant_read_schedules(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant list and get schedule permissions for schedules in this group to the given principal.

        :param identity: -
        '''
        ...

    @jsii.member(jsii_name="grantWriteSchedules")
    def grant_write_schedules(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant create and update schedule permissions for schedules in this group to the given principal.

        :param identity: -
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
        '''Return the given named metric for this group schedules.

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

        :default: - sum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricAttempts")
    def metric_attempts(
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
        '''Metric for all invocation attempts.

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

        :default: - sum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricDropped")
    def metric_dropped(
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
        '''Metric for dropped invocations when EventBridge Scheduler stops attempting to invoke the target after a schedule's retry policy has been exhausted.

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

        :default: - sum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricFailedToBeSentToDLQ")
    def metric_failed_to_be_sent_to_dlq(
        self,
        error_code: typing.Optional[builtins.str] = None,
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
        '''Metric for failed invocations that also failed to deliver to DLQ.

        :param error_code: -
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

        :default: - sum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricSentToDLQ")
    def metric_sent_to_dlq(
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
        '''Metric for invocations delivered to the DLQ.

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

        :default: - sum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricSentToDLQTruncated")
    def metric_sent_to_dlq_truncated(
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
        '''Metric for delivery of failed invocations to DLQ when the payload of the event sent to the DLQ exceeds the maximum size allowed by Amazon SQS.

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

        :default: - sum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricTargetErrors")
    def metric_target_errors(
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
        '''Emitted when the target returns an exception after EventBridge Scheduler calls the target API.

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

        :default: - sum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricTargetThrottled")
    def metric_target_throttled(
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
        '''Metric for invocation failures due to API throttling by the target.

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

        :default: - sum over 5 minutes
        '''
        ...

    @jsii.member(jsii_name="metricThrottled")
    def metric_throttled(
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
        '''Metric for the number of invocations that were throttled because it exceeds your service quotas.

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

        :default: - sum over 5 minutes

        :see: https://docs.aws.amazon.com/scheduler/latest/UserGuide/scheduler-quotas.html
        '''
        ...


class _IScheduleGroupProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Interface representing a created or an imported ``ScheduleGroup``.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_scheduler.IScheduleGroup"

    @builtins.property
    @jsii.member(jsii_name="scheduleGroupArn")
    def schedule_group_arn(self) -> builtins.str:
        '''The arn of the schedule group.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "scheduleGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="scheduleGroupName")
    def schedule_group_name(self) -> builtins.str:
        '''The name of the schedule group.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "scheduleGroupName"))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the indicated permissions on this group to the given principal.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__190f03a36ab90eca0db1bdfd7c06d5891c61b69defb1c7be61f45d771a66e130)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantDeleteSchedules")
    def grant_delete_schedules(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant delete schedule permission for schedules in this group to the given principal.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__579ff4205e0ccb1830f899a44fc742e9853277ba0f82091be749e20b4fdbf1c2)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantDeleteSchedules", [identity]))

    @jsii.member(jsii_name="grantReadSchedules")
    def grant_read_schedules(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant list and get schedule permissions for schedules in this group to the given principal.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66f280f7a41957c98ada2240887b088985bbe273d1067b2c4f83f8ca69d09aae)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantReadSchedules", [identity]))

    @jsii.member(jsii_name="grantWriteSchedules")
    def grant_write_schedules(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant create and update schedule permissions for schedules in this group to the given principal.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f189e0a2b180ceb7d47a54524a64df15a2d1c7a5efe1e25873a64a68692c1d18)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWriteSchedules", [identity]))

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
        '''Return the given named metric for this group schedules.

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

        :default: - sum over 5 minutes
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1a1c48be5584426072c1f842a1e31e59436e2cefe7df9e84b5a3115ad743d3e)
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

    @jsii.member(jsii_name="metricAttempts")
    def metric_attempts(
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
        '''Metric for all invocation attempts.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricAttempts", [props]))

    @jsii.member(jsii_name="metricDropped")
    def metric_dropped(
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
        '''Metric for dropped invocations when EventBridge Scheduler stops attempting to invoke the target after a schedule's retry policy has been exhausted.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricDropped", [props]))

    @jsii.member(jsii_name="metricFailedToBeSentToDLQ")
    def metric_failed_to_be_sent_to_dlq(
        self,
        error_code: typing.Optional[builtins.str] = None,
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
        '''Metric for failed invocations that also failed to deliver to DLQ.

        :param error_code: -
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

        :default: - sum over 5 minutes
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43e3d3a73dae7296d8e1b29562f7a8fbdf941fb9885fa0ddcc13164e2352e68d)
            check_type(argname="argument error_code", value=error_code, expected_type=type_hints["error_code"])
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricFailedToBeSentToDLQ", [error_code, props]))

    @jsii.member(jsii_name="metricSentToDLQ")
    def metric_sent_to_dlq(
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
        '''Metric for invocations delivered to the DLQ.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSentToDLQ", [props]))

    @jsii.member(jsii_name="metricSentToDLQTruncated")
    def metric_sent_to_dlq_truncated(
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
        '''Metric for delivery of failed invocations to DLQ when the payload of the event sent to the DLQ exceeds the maximum size allowed by Amazon SQS.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSentToDLQTruncated", [props]))

    @jsii.member(jsii_name="metricTargetErrors")
    def metric_target_errors(
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
        '''Emitted when the target returns an exception after EventBridge Scheduler calls the target API.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricTargetErrors", [props]))

    @jsii.member(jsii_name="metricTargetThrottled")
    def metric_target_throttled(
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
        '''Metric for invocation failures due to API throttling by the target.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricTargetThrottled", [props]))

    @jsii.member(jsii_name="metricThrottled")
    def metric_throttled(
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
        '''Metric for the number of invocations that were throttled because it exceeds your service quotas.

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

        :default: - sum over 5 minutes

        :see: https://docs.aws.amazon.com/scheduler/latest/UserGuide/scheduler-quotas.html
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricThrottled", [props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScheduleGroup).__jsii_proxy_class__ = lambda : _IScheduleGroupProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_scheduler.IScheduleTarget")
class IScheduleTarget(typing_extensions.Protocol):
    '''Interface representing a Event Bridge Schedule Target.'''

    @jsii.member(jsii_name="bind")
    def bind(self, _schedule: ISchedule) -> "ScheduleTargetConfig":
        '''Returns the schedule target specification.

        :param _schedule: a schedule the target should be added to.
        '''
        ...


class _IScheduleTargetProxy:
    '''Interface representing a Event Bridge Schedule Target.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_scheduler.IScheduleTarget"

    @jsii.member(jsii_name="bind")
    def bind(self, _schedule: ISchedule) -> "ScheduleTargetConfig":
        '''Returns the schedule target specification.

        :param _schedule: a schedule the target should be added to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1db14aa1db4d786b1846e49587706992ee79b66245d52b5efebd763ccbd24c94)
            check_type(argname="argument _schedule", value=_schedule, expected_type=type_hints["_schedule"])
        return typing.cast("ScheduleTargetConfig", jsii.invoke(self, "bind", [_schedule]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScheduleTarget).__jsii_proxy_class__ = lambda : _IScheduleTargetProxy


@jsii.implements(ISchedule)
class Schedule(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler.Schedule",
):
    '''An EventBridge Schedule.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_kinesisfirehose as firehose
        # delivery_stream: firehose.IDeliveryStream
        
        
        payload = {
            "Data": "record"
        }
        
        Schedule(self, "Schedule",
            schedule=ScheduleExpression.rate(Duration.minutes(60)),
            target=targets.FirehosePutRecord(delivery_stream,
                input=ScheduleTargetInput.from_object(payload)
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        schedule: "ScheduleExpression",
        target: IScheduleTarget,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        end: typing.Optional[datetime.datetime] = None,
        key: typing.Optional[_IKey_5f11635f] = None,
        schedule_group: typing.Optional[IScheduleGroup] = None,
        schedule_name: typing.Optional[builtins.str] = None,
        start: typing.Optional[datetime.datetime] = None,
        time_window: typing.Optional["TimeWindow"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param schedule: The expression that defines when the schedule runs. Can be either a ``at``, ``rate`` or ``cron`` expression.
        :param target: The schedule's target details.
        :param description: The description you specify for the schedule. Default: - no value
        :param enabled: Indicates whether the schedule is enabled. Default: true
        :param end: The date, in UTC, before which the schedule can invoke its target. EventBridge Scheduler ignores end for one-time schedules. Default: - no value
        :param key: The customer managed KMS key that EventBridge Scheduler will use to encrypt and decrypt your data. Default: - All events in Scheduler are encrypted with a key that AWS owns and manages.
        :param schedule_group: The schedule's group. Default: - By default a schedule will be associated with the ``default`` group.
        :param schedule_name: The name of the schedule. Up to 64 letters (uppercase and lowercase), numbers, hyphens, underscores and dots are allowed. Default: - A unique name will be generated
        :param start: The date, in UTC, after which the schedule can begin invoking its target. EventBridge Scheduler ignores start for one-time schedules. Default: - no value
        :param time_window: A time window during which EventBridge Scheduler invokes the schedule. Default: TimeWindow.off()
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5e74b4c774095daccbb01abe34df777261be2bfce9f7ec773cd8688b17dbb98)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ScheduleProps(
            schedule=schedule,
            target=target,
            description=description,
            enabled=enabled,
            end=end,
            key=key,
            schedule_group=schedule_group,
            schedule_name=schedule_name,
            start=start,
            time_window=time_window,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromScheduleArn")
    @builtins.classmethod
    def from_schedule_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        schedule_arn: builtins.str,
    ) -> ISchedule:
        '''Import an existing schedule using the ARN.

        :param scope: -
        :param id: -
        :param schedule_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1372455178922293375a1300f4c6e69cee5bc442b16f4036c84aafb7d9332f93)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument schedule_arn", value=schedule_arn, expected_type=type_hints["schedule_arn"])
        return typing.cast(ISchedule, jsii.sinvoke(cls, "fromScheduleArn", [scope, id, schedule_arn]))

    @jsii.member(jsii_name="metricAll")
    @builtins.classmethod
    def metric_all(
        cls,
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
        '''Return the given named metric for all schedules.

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

        :default: - sum over 5 minutes
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e9697edf3bddfcbab866b7220407b409d24e19d71a4831cc2eae389b626c1d7)
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

        return typing.cast(_Metric_e396a4dc, jsii.sinvoke(cls, "metricAll", [metric_name, props]))

    @jsii.member(jsii_name="metricAllAttempts")
    @builtins.classmethod
    def metric_all_attempts(
        cls,
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
        '''Metric for all invocation attempts across all schedules.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.sinvoke(cls, "metricAllAttempts", [props]))

    @jsii.member(jsii_name="metricAllDropped")
    @builtins.classmethod
    def metric_all_dropped(
        cls,
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
        '''Metric for dropped invocations when EventBridge Scheduler stops attempting to invoke the target after a schedule's retry policy has been exhausted.

        Metric is calculated for all schedules.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.sinvoke(cls, "metricAllDropped", [props]))

    @jsii.member(jsii_name="metricAllErrors")
    @builtins.classmethod
    def metric_all_errors(
        cls,
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
        '''Emitted when the target returns an exception after EventBridge Scheduler calls the target API across all schedules.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.sinvoke(cls, "metricAllErrors", [props]))

    @jsii.member(jsii_name="metricAllFailedToBeSentToDLQ")
    @builtins.classmethod
    def metric_all_failed_to_be_sent_to_dlq(
        cls,
        error_code: typing.Optional[builtins.str] = None,
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
        '''Metric for failed invocations that also failed to deliver to DLQ across all schedules.

        :param error_code: -
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

        :default: - sum over 5 minutes
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__897a723a752bdf5a7cbd4dc9c673edd8862b55def0dfc20984054c323d651b0d)
            check_type(argname="argument error_code", value=error_code, expected_type=type_hints["error_code"])
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

        return typing.cast(_Metric_e396a4dc, jsii.sinvoke(cls, "metricAllFailedToBeSentToDLQ", [error_code, props]))

    @jsii.member(jsii_name="metricAllSentToDLQ")
    @builtins.classmethod
    def metric_all_sent_to_dlq(
        cls,
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
        '''Metric for invocations delivered to the DLQ across all schedules.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.sinvoke(cls, "metricAllSentToDLQ", [props]))

    @jsii.member(jsii_name="metricAllSentToDLQTruncated")
    @builtins.classmethod
    def metric_all_sent_to_dlq_truncated(
        cls,
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
        '''Metric for delivery of failed invocations to DLQ when the payload of the event sent to the DLQ exceeds the maximum size allowed by Amazon SQS.

        Metric is calculated for all schedules.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.sinvoke(cls, "metricAllSentToDLQTruncated", [props]))

    @jsii.member(jsii_name="metricAllTargetThrottled")
    @builtins.classmethod
    def metric_all_target_throttled(
        cls,
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
        '''Metric for invocation failures due to API throttling by the target across all schedules.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.sinvoke(cls, "metricAllTargetThrottled", [props]))

    @jsii.member(jsii_name="metricAllThrottled")
    @builtins.classmethod
    def metric_all_throttled(
        cls,
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
        '''Metric for the number of invocations that were throttled across all schedules.

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

        :default: - sum over 5 minutes

        :see: https://docs.aws.amazon.com/scheduler/latest/UserGuide/scheduler-quotas.html
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

        return typing.cast(_Metric_e396a4dc, jsii.sinvoke(cls, "metricAllThrottled", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))

    @builtins.property
    @jsii.member(jsii_name="scheduleArn")
    def schedule_arn(self) -> builtins.str:
        '''The arn of the schedule.'''
        return typing.cast(builtins.str, jsii.get(self, "scheduleArn"))

    @builtins.property
    @jsii.member(jsii_name="scheduleName")
    def schedule_name(self) -> builtins.str:
        '''The name of the schedule.'''
        return typing.cast(builtins.str, jsii.get(self, "scheduleName"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The customer managed KMS key that EventBridge Scheduler will use to encrypt and decrypt your data.'''
        return typing.cast(typing.Optional[_IKey_5f11635f], jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="scheduleGroup")
    def schedule_group(self) -> typing.Optional[IScheduleGroup]:
        '''The schedule group associated with this schedule.'''
        return typing.cast(typing.Optional[IScheduleGroup], jsii.get(self, "scheduleGroup"))


class ScheduleExpression(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_scheduler.ScheduleExpression",
):
    '''ScheduleExpression for EventBridge Schedule.

    You can choose from three schedule types when configuring your schedule: rate-based, cron-based, and one-time schedules.
    Both rate-based and cron-based schedules are recurring schedules.

    :see: https://docs.aws.amazon.com/scheduler/latest/UserGuide/schedule-types.html
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_kinesisfirehose as firehose
        # delivery_stream: firehose.IDeliveryStream
        
        
        payload = {
            "Data": "record"
        }
        
        Schedule(self, "Schedule",
            schedule=ScheduleExpression.rate(Duration.minutes(60)),
            target=targets.FirehosePutRecord(delivery_stream,
                input=ScheduleTargetInput.from_object(payload)
            )
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="at")
    @builtins.classmethod
    def at(
        cls,
        date: datetime.datetime,
        time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
    ) -> "ScheduleExpression":
        '''Construct a one-time schedule from a date.

        :param date: The date and time to use. The millisecond part will be ignored.
        :param time_zone: The time zone to use for interpreting the date. Default: - UTC
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__175909e9c50b88b6e35fc2db4998caa986e6da11a9a20dbde9c02ee1ca0b00b8)
            check_type(argname="argument date", value=date, expected_type=type_hints["date"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
        return typing.cast("ScheduleExpression", jsii.sinvoke(cls, "at", [date, time_zone]))

    @jsii.member(jsii_name="cron")
    @builtins.classmethod
    def cron(
        cls,
        *,
        time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
        day: typing.Optional[builtins.str] = None,
        hour: typing.Optional[builtins.str] = None,
        minute: typing.Optional[builtins.str] = None,
        month: typing.Optional[builtins.str] = None,
        week_day: typing.Optional[builtins.str] = None,
        year: typing.Optional[builtins.str] = None,
    ) -> "ScheduleExpression":
        '''Create a recurring schedule from a set of cron fields and time zone.

        :param time_zone: The timezone to run the schedule in. Default: - TimeZone.ETC_UTC
        :param day: The day of the month to run this rule at. Default: - Every day of the month
        :param hour: The hour to run this rule at. Default: - Every hour
        :param minute: The minute to run this rule at. Default: - Every minute
        :param month: The month to run this rule at. Default: - Every month
        :param week_day: The day of the week to run this rule at. Default: - Any day of the week
        :param year: The year to run this rule at. Default: - Every year
        '''
        options = CronOptionsWithTimezone(
            time_zone=time_zone,
            day=day,
            hour=hour,
            minute=minute,
            month=month,
            week_day=week_day,
            year=year,
        )

        return typing.cast("ScheduleExpression", jsii.sinvoke(cls, "cron", [options]))

    @jsii.member(jsii_name="expression")
    @builtins.classmethod
    def expression(
        cls,
        expression: builtins.str,
        time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
    ) -> "ScheduleExpression":
        '''Construct a schedule from a literal schedule expression.

        :param expression: The expression to use. Must be in a format that EventBridge will recognize
        :param time_zone: The time zone to use for interpreting the expression. Default: - UTC
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21e89766a8d616bfc00e75a22774b5d41c55681b6f5f623f08f201c835dd2902)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
        return typing.cast("ScheduleExpression", jsii.sinvoke(cls, "expression", [expression, time_zone]))

    @jsii.member(jsii_name="rate")
    @builtins.classmethod
    def rate(cls, duration: _Duration_4839e8c3) -> "ScheduleExpression":
        '''Construct a recurring schedule from an interval and a time unit.

        Rates may be defined with any unit of time, but when converted into minutes, the duration must be a positive whole number of minutes.

        :param duration: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97a45c9b75fc81cb3d47817d0893dffb28ebc87496c4a4eedb9cf73b57a68cc5)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
        return typing.cast("ScheduleExpression", jsii.sinvoke(cls, "rate", [duration]))

    @builtins.property
    @jsii.member(jsii_name="expressionString")
    @abc.abstractmethod
    def expression_string(self) -> builtins.str:
        '''Retrieve the expression for this schedule.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    @abc.abstractmethod
    def time_zone(self) -> typing.Optional[_TimeZone_cdd72ac9]:
        '''Retrieve the expression for this schedule.'''
        ...


class _ScheduleExpressionProxy(ScheduleExpression):
    @builtins.property
    @jsii.member(jsii_name="expressionString")
    def expression_string(self) -> builtins.str:
        '''Retrieve the expression for this schedule.'''
        return typing.cast(builtins.str, jsii.get(self, "expressionString"))

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> typing.Optional[_TimeZone_cdd72ac9]:
        '''Retrieve the expression for this schedule.'''
        return typing.cast(typing.Optional[_TimeZone_cdd72ac9], jsii.get(self, "timeZone"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, ScheduleExpression).__jsii_proxy_class__ = lambda : _ScheduleExpressionProxy


@jsii.implements(IScheduleGroup)
class ScheduleGroup(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler.ScheduleGroup",
):
    '''A Schedule Group.

    :resource: AWS::Scheduler::ScheduleGroup
    :exampleMetadata: infused

    Example::

        # target: targets.LambdaInvoke
        
        
        schedule_group = ScheduleGroup(self, "ScheduleGroup",
            schedule_group_name="MyScheduleGroup"
        )
        
        Schedule(self, "Schedule",
            schedule=ScheduleExpression.rate(Duration.minutes(10)),
            target=target,
            schedule_group=schedule_group
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        schedule_group_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param removal_policy: The removal policy for the group. If the group is removed also all schedules are removed. Default: RemovalPolicy.RETAIN
        :param schedule_group_name: The name of the schedule group. Up to 64 letters (uppercase and lowercase), numbers, hyphens, underscores and dots are allowed. Default: - A unique name will be generated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__736972893d2822201f3b54995126456a9f4766921d769ea7836c13c49c015d53)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ScheduleGroupProps(
            removal_policy=removal_policy, schedule_group_name=schedule_group_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromDefaultScheduleGroup")
    @builtins.classmethod
    def from_default_schedule_group(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
    ) -> IScheduleGroup:
        '''Import a default schedule group.

        :param scope: construct scope.
        :param id: construct id.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7b5a1fbdcbfd0ad106f45caf1d995619df8d064b8587659c5461157f6e48926)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(IScheduleGroup, jsii.sinvoke(cls, "fromDefaultScheduleGroup", [scope, id]))

    @jsii.member(jsii_name="fromScheduleGroupArn")
    @builtins.classmethod
    def from_schedule_group_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        schedule_group_arn: builtins.str,
    ) -> IScheduleGroup:
        '''Import an external schedule group by ARN.

        :param scope: construct scope.
        :param id: construct id.
        :param schedule_group_arn: the ARN of the schedule group to import (e.g. ``arn:aws:scheduler:region:account-id:schedule-group/group-name``).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c77731a2b0fb48c74a722651a8f036cef9066af4a6dd7b73c0b9b2d119bc36d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument schedule_group_arn", value=schedule_group_arn, expected_type=type_hints["schedule_group_arn"])
        return typing.cast(IScheduleGroup, jsii.sinvoke(cls, "fromScheduleGroupArn", [scope, id, schedule_group_arn]))

    @jsii.member(jsii_name="fromScheduleGroupName")
    @builtins.classmethod
    def from_schedule_group_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        schedule_group_name: builtins.str,
    ) -> IScheduleGroup:
        '''Import an existing schedule group with a given name.

        :param scope: construct scope.
        :param id: construct id.
        :param schedule_group_name: the name of the existing schedule group to import.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0eef3cd9167e1bcf64df7282dec1f362eaac5659d22625afac3c28dcc0b7edb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument schedule_group_name", value=schedule_group_name, expected_type=type_hints["schedule_group_name"])
        return typing.cast(IScheduleGroup, jsii.sinvoke(cls, "fromScheduleGroupName", [scope, id, schedule_group_name]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _IGrantable_71c4f5de,
        *actions: builtins.str,
    ) -> _Grant_a7ae64f8:
        '''Grant the indicated permissions on this schedule group to the given principal.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1603de1685aaaf14ff1514df8394bc631af9b5e6f8b79a44c31ff5e24157a7e0)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantDeleteSchedules")
    def grant_delete_schedules(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant delete schedule permission for schedules in this group to the given principal.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15bda48b16b2099393ebcd41e9be05dd66aaf7faaeae1ba65b42220d7667bce5)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantDeleteSchedules", [identity]))

    @jsii.member(jsii_name="grantReadSchedules")
    def grant_read_schedules(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant list and get schedule permissions for schedules in this group to the given principal.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55a9d37bafcef8d26af6e888f5ab8b2aef1359b02c7a510049f6e900c986b797)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantReadSchedules", [identity]))

    @jsii.member(jsii_name="grantWriteSchedules")
    def grant_write_schedules(self, identity: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant create and update schedule permissions for schedules in this group to the given principal.

        :param identity: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2cc2856526773b02c8dfcbfcca6cf534cc4a4b00a0b0de1e8fe166c071534ab)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantWriteSchedules", [identity]))

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
        '''Return the given named metric for this schedule group.

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

        :default: - sum over 5 minutes
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__634bd225463be60303d9d1588926bbaa9fbd72c940ca54fecf9724d90fdefe64)
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

    @jsii.member(jsii_name="metricAttempts")
    def metric_attempts(
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
        '''Metric for all invocation attempts.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricAttempts", [props]))

    @jsii.member(jsii_name="metricDropped")
    def metric_dropped(
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
        '''Metric for dropped invocations when EventBridge Scheduler stops attempting to invoke the target after a schedule's retry policy has been exhausted.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricDropped", [props]))

    @jsii.member(jsii_name="metricFailedToBeSentToDLQ")
    def metric_failed_to_be_sent_to_dlq(
        self,
        error_code: typing.Optional[builtins.str] = None,
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
        '''Metric for failed invocations that also failed to deliver to DLQ.

        :param error_code: -
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

        :default: - sum over 5 minutes
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca970bf647095b0a6fd282ecce93e19b12761be780f7fac1db8cc3b6f97c0cbf)
            check_type(argname="argument error_code", value=error_code, expected_type=type_hints["error_code"])
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricFailedToBeSentToDLQ", [error_code, props]))

    @jsii.member(jsii_name="metricSentToDLQ")
    def metric_sent_to_dlq(
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
        '''Metric for invocations delivered to the DLQ.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSentToDLQ", [props]))

    @jsii.member(jsii_name="metricSentToDLQTruncated")
    def metric_sent_to_dlq_truncated(
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
        '''Metric for delivery of failed invocations to DLQ when the payload of the event sent to the DLQ exceeds the maximum size allowed by Amazon SQS.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricSentToDLQTruncated", [props]))

    @jsii.member(jsii_name="metricTargetErrors")
    def metric_target_errors(
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
        '''Emitted when the target returns an exception after EventBridge Scheduler calls the target API.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricTargetErrors", [props]))

    @jsii.member(jsii_name="metricTargetThrottled")
    def metric_target_throttled(
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
        '''Metric for invocation failures due to API throttling by the target.

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

        :default: - sum over 5 minutes
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricTargetThrottled", [props]))

    @jsii.member(jsii_name="metricThrottled")
    def metric_throttled(
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
        '''Metric for the number of invocations that were throttled because it exceeds your service quotas.

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

        :default: - sum over 5 minutes

        :see: https://docs.aws.amazon.com/scheduler/latest/UserGuide/scheduler-quotas.html
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

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricThrottled", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="PROPERTY_INJECTION_ID")
    def PROPERTY_INJECTION_ID(cls) -> builtins.str:
        '''Uniquely identifies this class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PROPERTY_INJECTION_ID"))

    @builtins.property
    @jsii.member(jsii_name="scheduleGroupArn")
    def schedule_group_arn(self) -> builtins.str:
        '''The arn of the schedule group.'''
        return typing.cast(builtins.str, jsii.get(self, "scheduleGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="scheduleGroupName")
    def schedule_group_name(self) -> builtins.str:
        '''The name of the schedule group.'''
        return typing.cast(builtins.str, jsii.get(self, "scheduleGroupName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler.ScheduleGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "removal_policy": "removalPolicy",
        "schedule_group_name": "scheduleGroupName",
    },
)
class ScheduleGroupProps:
    def __init__(
        self,
        *,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        schedule_group_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a Schedule Group.

        :param removal_policy: The removal policy for the group. If the group is removed also all schedules are removed. Default: RemovalPolicy.RETAIN
        :param schedule_group_name: The name of the schedule group. Up to 64 letters (uppercase and lowercase), numbers, hyphens, underscores and dots are allowed. Default: - A unique name will be generated

        :exampleMetadata: infused

        Example::

            # target: targets.LambdaInvoke
            
            
            schedule_group = ScheduleGroup(self, "ScheduleGroup",
                schedule_group_name="MyScheduleGroup"
            )
            
            Schedule(self, "Schedule",
                schedule=ScheduleExpression.rate(Duration.minutes(10)),
                target=target,
                schedule_group=schedule_group
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00f616ddd843f7dab1625531f0a0666a403b81004bd707155fc676f64bb15c34)
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument schedule_group_name", value=schedule_group_name, expected_type=type_hints["schedule_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if schedule_group_name is not None:
            self._values["schedule_group_name"] = schedule_group_name

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''The removal policy for the group.

        If the group is removed also all schedules are removed.

        :default: RemovalPolicy.RETAIN
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def schedule_group_name(self) -> typing.Optional[builtins.str]:
        '''The name of the schedule group.

        Up to 64 letters (uppercase and lowercase), numbers, hyphens, underscores and dots are allowed.

        :default: - A unique name will be generated
        '''
        result = self._values.get("schedule_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduleGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler.ScheduleProps",
    jsii_struct_bases=[],
    name_mapping={
        "schedule": "schedule",
        "target": "target",
        "description": "description",
        "enabled": "enabled",
        "end": "end",
        "key": "key",
        "schedule_group": "scheduleGroup",
        "schedule_name": "scheduleName",
        "start": "start",
        "time_window": "timeWindow",
    },
)
class ScheduleProps:
    def __init__(
        self,
        *,
        schedule: ScheduleExpression,
        target: IScheduleTarget,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        end: typing.Optional[datetime.datetime] = None,
        key: typing.Optional[_IKey_5f11635f] = None,
        schedule_group: typing.Optional[IScheduleGroup] = None,
        schedule_name: typing.Optional[builtins.str] = None,
        start: typing.Optional[datetime.datetime] = None,
        time_window: typing.Optional["TimeWindow"] = None,
    ) -> None:
        '''Construction properties for ``Schedule``.

        :param schedule: The expression that defines when the schedule runs. Can be either a ``at``, ``rate`` or ``cron`` expression.
        :param target: The schedule's target details.
        :param description: The description you specify for the schedule. Default: - no value
        :param enabled: Indicates whether the schedule is enabled. Default: true
        :param end: The date, in UTC, before which the schedule can invoke its target. EventBridge Scheduler ignores end for one-time schedules. Default: - no value
        :param key: The customer managed KMS key that EventBridge Scheduler will use to encrypt and decrypt your data. Default: - All events in Scheduler are encrypted with a key that AWS owns and manages.
        :param schedule_group: The schedule's group. Default: - By default a schedule will be associated with the ``default`` group.
        :param schedule_name: The name of the schedule. Up to 64 letters (uppercase and lowercase), numbers, hyphens, underscores and dots are allowed. Default: - A unique name will be generated
        :param start: The date, in UTC, after which the schedule can begin invoking its target. EventBridge Scheduler ignores start for one-time schedules. Default: - no value
        :param time_window: A time window during which EventBridge Scheduler invokes the schedule. Default: TimeWindow.off()

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_kinesisfirehose as firehose
            # delivery_stream: firehose.IDeliveryStream
            
            
            payload = {
                "Data": "record"
            }
            
            Schedule(self, "Schedule",
                schedule=ScheduleExpression.rate(Duration.minutes(60)),
                target=targets.FirehosePutRecord(delivery_stream,
                    input=ScheduleTargetInput.from_object(payload)
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1a1cbc6cf4c30e6930150f969adcdfef2b116842e4bcb34a1adcf13677e296f)
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument schedule_group", value=schedule_group, expected_type=type_hints["schedule_group"])
            check_type(argname="argument schedule_name", value=schedule_name, expected_type=type_hints["schedule_name"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument time_window", value=time_window, expected_type=type_hints["time_window"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schedule": schedule,
            "target": target,
        }
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if end is not None:
            self._values["end"] = end
        if key is not None:
            self._values["key"] = key
        if schedule_group is not None:
            self._values["schedule_group"] = schedule_group
        if schedule_name is not None:
            self._values["schedule_name"] = schedule_name
        if start is not None:
            self._values["start"] = start
        if time_window is not None:
            self._values["time_window"] = time_window

    @builtins.property
    def schedule(self) -> ScheduleExpression:
        '''The expression that defines when the schedule runs.

        Can be either a ``at``, ``rate``
        or ``cron`` expression.
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(ScheduleExpression, result)

    @builtins.property
    def target(self) -> IScheduleTarget:
        '''The schedule's target details.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(IScheduleTarget, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description you specify for the schedule.

        :default: - no value
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Indicates whether the schedule is enabled.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def end(self) -> typing.Optional[datetime.datetime]:
        '''The date, in UTC, before which the schedule can invoke its target.

        EventBridge Scheduler ignores end for one-time schedules.

        :default: - no value
        '''
        result = self._values.get("end")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The customer managed KMS key that EventBridge Scheduler will use to encrypt and decrypt your data.

        :default: - All events in Scheduler are encrypted with a key that AWS owns and manages.
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def schedule_group(self) -> typing.Optional[IScheduleGroup]:
        '''The schedule's group.

        :default: - By default a schedule will be associated with the ``default`` group.
        '''
        result = self._values.get("schedule_group")
        return typing.cast(typing.Optional[IScheduleGroup], result)

    @builtins.property
    def schedule_name(self) -> typing.Optional[builtins.str]:
        '''The name of the schedule.

        Up to 64 letters (uppercase and lowercase), numbers, hyphens, underscores and dots are allowed.

        :default: - A unique name will be generated
        '''
        result = self._values.get("schedule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start(self) -> typing.Optional[datetime.datetime]:
        '''The date, in UTC, after which the schedule can begin invoking its target.

        EventBridge Scheduler ignores start for one-time schedules.

        :default: - no value
        '''
        result = self._values.get("start")
        return typing.cast(typing.Optional[datetime.datetime], result)

    @builtins.property
    def time_window(self) -> typing.Optional["TimeWindow"]:
        '''A time window during which EventBridge Scheduler invokes the schedule.

        :default: TimeWindow.off()

        :see: https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-flexible-time-windows.html
        '''
        result = self._values.get("time_window")
        return typing.cast(typing.Optional["TimeWindow"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler.ScheduleTargetConfig",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "role": "role",
        "dead_letter_config": "deadLetterConfig",
        "ecs_parameters": "ecsParameters",
        "event_bridge_parameters": "eventBridgeParameters",
        "input": "input",
        "kinesis_parameters": "kinesisParameters",
        "retry_policy": "retryPolicy",
        "sage_maker_pipeline_parameters": "sageMakerPipelineParameters",
        "sqs_parameters": "sqsParameters",
    },
)
class ScheduleTargetConfig:
    def __init__(
        self,
        *,
        arn: builtins.str,
        role: _IRole_235f5d8e,
        dead_letter_config: typing.Optional[typing.Union[CfnSchedule.DeadLetterConfigProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        ecs_parameters: typing.Optional[typing.Union[CfnSchedule.EcsParametersProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        event_bridge_parameters: typing.Optional[typing.Union[CfnSchedule.EventBridgeParametersProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        input: typing.Optional["ScheduleTargetInput"] = None,
        kinesis_parameters: typing.Optional[typing.Union[CfnSchedule.KinesisParametersProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        retry_policy: typing.Optional[typing.Union[CfnSchedule.RetryPolicyProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        sage_maker_pipeline_parameters: typing.Optional[typing.Union[CfnSchedule.SageMakerPipelineParametersProperty, typing.Dict[builtins.str, typing.Any]]] = None,
        sqs_parameters: typing.Optional[typing.Union[CfnSchedule.SqsParametersProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Config of a Schedule Target used during initialization of Schedule.

        :param arn: The Amazon Resource Name (ARN) of the target.
        :param role: Role to use to invoke this event target.
        :param dead_letter_config: An object that contains information about an Amazon SQS queue that EventBridge Scheduler uses as a dead-letter queue for your schedule. If specified, EventBridge Scheduler delivers failed events that could not be successfully delivered to a target to the queue. Default: - No dead-letter queue
        :param ecs_parameters: The templated target type for the Amazon ECS RunTask API Operation. Default: - No parameters
        :param event_bridge_parameters: The templated target type for the EventBridge PutEvents API operation. Default: - No parameters
        :param input: What input to pass to the target. Default: - No input
        :param kinesis_parameters: The templated target type for the Amazon Kinesis PutRecord API operation. Default: - No parameters
        :param retry_policy: A ``RetryPolicy`` object that includes information about the retry policy settings, including the maximum age of an event, and the maximum number of times EventBridge Scheduler will try to deliver the event to a target. Default: - Maximum retry attempts of 185 and maximum age of 86400 seconds (1 day)
        :param sage_maker_pipeline_parameters: The templated target type for the Amazon SageMaker StartPipelineExecution API operation. Default: - No parameters
        :param sqs_parameters: The templated target type for the Amazon SQS SendMessage API Operation. Default: - No parameters

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_scheduler as scheduler
            
            # role: iam.Role
            # schedule_target_input: scheduler.ScheduleTargetInput
            # tags: Any
            
            schedule_target_config = scheduler.ScheduleTargetConfig(
                arn="arn",
                role=role,
            
                # the properties below are optional
                dead_letter_config=scheduler.CfnSchedule.DeadLetterConfigProperty(
                    arn="arn"
                ),
                ecs_parameters=scheduler.CfnSchedule.EcsParametersProperty(
                    task_definition_arn="taskDefinitionArn",
            
                    # the properties below are optional
                    capacity_provider_strategy=[scheduler.CfnSchedule.CapacityProviderStrategyItemProperty(
                        capacity_provider="capacityProvider",
            
                        # the properties below are optional
                        base=123,
                        weight=123
                    )],
                    enable_ecs_managed_tags=False,
                    enable_execute_command=False,
                    group="group",
                    launch_type="launchType",
                    network_configuration=scheduler.CfnSchedule.NetworkConfigurationProperty(
                        awsvpc_configuration=scheduler.CfnSchedule.AwsVpcConfigurationProperty(
                            subnets=["subnets"],
            
                            # the properties below are optional
                            assign_public_ip="assignPublicIp",
                            security_groups=["securityGroups"]
                        )
                    ),
                    placement_constraints=[scheduler.CfnSchedule.PlacementConstraintProperty(
                        expression="expression",
                        type="type"
                    )],
                    placement_strategy=[scheduler.CfnSchedule.PlacementStrategyProperty(
                        field="field",
                        type="type"
                    )],
                    platform_version="platformVersion",
                    propagate_tags="propagateTags",
                    reference_id="referenceId",
                    tags=tags,
                    task_count=123
                ),
                event_bridge_parameters=scheduler.CfnSchedule.EventBridgeParametersProperty(
                    detail_type="detailType",
                    source="source"
                ),
                input=schedule_target_input,
                kinesis_parameters=scheduler.CfnSchedule.KinesisParametersProperty(
                    partition_key="partitionKey"
                ),
                retry_policy=scheduler.CfnSchedule.RetryPolicyProperty(
                    maximum_event_age_in_seconds=123,
                    maximum_retry_attempts=123
                ),
                sage_maker_pipeline_parameters=scheduler.CfnSchedule.SageMakerPipelineParametersProperty(
                    pipeline_parameter_list=[scheduler.CfnSchedule.SageMakerPipelineParameterProperty(
                        name="name",
                        value="value"
                    )]
                ),
                sqs_parameters=scheduler.CfnSchedule.SqsParametersProperty(
                    message_group_id="messageGroupId"
                )
            )
        '''
        if isinstance(dead_letter_config, dict):
            dead_letter_config = CfnSchedule.DeadLetterConfigProperty(**dead_letter_config)
        if isinstance(ecs_parameters, dict):
            ecs_parameters = CfnSchedule.EcsParametersProperty(**ecs_parameters)
        if isinstance(event_bridge_parameters, dict):
            event_bridge_parameters = CfnSchedule.EventBridgeParametersProperty(**event_bridge_parameters)
        if isinstance(kinesis_parameters, dict):
            kinesis_parameters = CfnSchedule.KinesisParametersProperty(**kinesis_parameters)
        if isinstance(retry_policy, dict):
            retry_policy = CfnSchedule.RetryPolicyProperty(**retry_policy)
        if isinstance(sage_maker_pipeline_parameters, dict):
            sage_maker_pipeline_parameters = CfnSchedule.SageMakerPipelineParametersProperty(**sage_maker_pipeline_parameters)
        if isinstance(sqs_parameters, dict):
            sqs_parameters = CfnSchedule.SqsParametersProperty(**sqs_parameters)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39b25a1f04a872a013c3ee593bb9140da10796639b130bc7f2461018358c6292)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument dead_letter_config", value=dead_letter_config, expected_type=type_hints["dead_letter_config"])
            check_type(argname="argument ecs_parameters", value=ecs_parameters, expected_type=type_hints["ecs_parameters"])
            check_type(argname="argument event_bridge_parameters", value=event_bridge_parameters, expected_type=type_hints["event_bridge_parameters"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument kinesis_parameters", value=kinesis_parameters, expected_type=type_hints["kinesis_parameters"])
            check_type(argname="argument retry_policy", value=retry_policy, expected_type=type_hints["retry_policy"])
            check_type(argname="argument sage_maker_pipeline_parameters", value=sage_maker_pipeline_parameters, expected_type=type_hints["sage_maker_pipeline_parameters"])
            check_type(argname="argument sqs_parameters", value=sqs_parameters, expected_type=type_hints["sqs_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "arn": arn,
            "role": role,
        }
        if dead_letter_config is not None:
            self._values["dead_letter_config"] = dead_letter_config
        if ecs_parameters is not None:
            self._values["ecs_parameters"] = ecs_parameters
        if event_bridge_parameters is not None:
            self._values["event_bridge_parameters"] = event_bridge_parameters
        if input is not None:
            self._values["input"] = input
        if kinesis_parameters is not None:
            self._values["kinesis_parameters"] = kinesis_parameters
        if retry_policy is not None:
            self._values["retry_policy"] = retry_policy
        if sage_maker_pipeline_parameters is not None:
            self._values["sage_maker_pipeline_parameters"] = sage_maker_pipeline_parameters
        if sqs_parameters is not None:
            self._values["sqs_parameters"] = sqs_parameters

    @builtins.property
    def arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the target.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> _IRole_235f5d8e:
        '''Role to use to invoke this event target.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(_IRole_235f5d8e, result)

    @builtins.property
    def dead_letter_config(
        self,
    ) -> typing.Optional[CfnSchedule.DeadLetterConfigProperty]:
        '''An object that contains information about an Amazon SQS queue that EventBridge Scheduler uses as a dead-letter queue for your schedule.

        If specified, EventBridge Scheduler delivers failed events that could not be successfully delivered to a target to the queue.

        :default: - No dead-letter queue
        '''
        result = self._values.get("dead_letter_config")
        return typing.cast(typing.Optional[CfnSchedule.DeadLetterConfigProperty], result)

    @builtins.property
    def ecs_parameters(self) -> typing.Optional[CfnSchedule.EcsParametersProperty]:
        '''The templated target type for the Amazon ECS RunTask API Operation.

        :default: - No parameters
        '''
        result = self._values.get("ecs_parameters")
        return typing.cast(typing.Optional[CfnSchedule.EcsParametersProperty], result)

    @builtins.property
    def event_bridge_parameters(
        self,
    ) -> typing.Optional[CfnSchedule.EventBridgeParametersProperty]:
        '''The templated target type for the EventBridge PutEvents API operation.

        :default: - No parameters
        '''
        result = self._values.get("event_bridge_parameters")
        return typing.cast(typing.Optional[CfnSchedule.EventBridgeParametersProperty], result)

    @builtins.property
    def input(self) -> typing.Optional["ScheduleTargetInput"]:
        '''What input to pass to the target.

        :default: - No input
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional["ScheduleTargetInput"], result)

    @builtins.property
    def kinesis_parameters(
        self,
    ) -> typing.Optional[CfnSchedule.KinesisParametersProperty]:
        '''The templated target type for the Amazon Kinesis PutRecord API operation.

        :default: - No parameters
        '''
        result = self._values.get("kinesis_parameters")
        return typing.cast(typing.Optional[CfnSchedule.KinesisParametersProperty], result)

    @builtins.property
    def retry_policy(self) -> typing.Optional[CfnSchedule.RetryPolicyProperty]:
        '''A ``RetryPolicy`` object that includes information about the retry policy settings, including the maximum age of an event, and the maximum number of times EventBridge Scheduler will try to deliver the event to a target.

        :default: - Maximum retry attempts of 185 and maximum age of 86400 seconds (1 day)
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional[CfnSchedule.RetryPolicyProperty], result)

    @builtins.property
    def sage_maker_pipeline_parameters(
        self,
    ) -> typing.Optional[CfnSchedule.SageMakerPipelineParametersProperty]:
        '''The templated target type for the Amazon SageMaker StartPipelineExecution API operation.

        :default: - No parameters
        '''
        result = self._values.get("sage_maker_pipeline_parameters")
        return typing.cast(typing.Optional[CfnSchedule.SageMakerPipelineParametersProperty], result)

    @builtins.property
    def sqs_parameters(self) -> typing.Optional[CfnSchedule.SqsParametersProperty]:
        '''The templated target type for the Amazon SQS SendMessage API Operation.

        :default: - No parameters
        '''
        result = self._values.get("sqs_parameters")
        return typing.cast(typing.Optional[CfnSchedule.SqsParametersProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduleTargetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ScheduleTargetInput(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_scheduler.ScheduleTargetInput",
):
    '''The text or well-formed JSON input passed to the target of the schedule.

    Tokens and ContextAttribute may be used in the input.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_sns as sns
        
        
        topic = sns.Topic(self, "Topic")
        
        payload = {
            "message": "Hello scheduler!"
        }
        
        target = targets.SnsPublish(topic,
            input=ScheduleTargetInput.from_object(payload)
        )
        
        Schedule(self, "Schedule",
            schedule=ScheduleExpression.rate(Duration.hours(1)),
            target=target
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromObject")
    @builtins.classmethod
    def from_object(cls, obj: typing.Any) -> "ScheduleTargetInput":
        '''Pass a JSON object to the target.

        The object will be transformed into a well-formed JSON string in the final template.

        :param obj: object to use to convert to JSON to use as input for the target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fdac9a672a0bc2eb981e9971ac41140aa1074946d827f45e5c9d4d78673f0cd)
            check_type(argname="argument obj", value=obj, expected_type=type_hints["obj"])
        return typing.cast("ScheduleTargetInput", jsii.sinvoke(cls, "fromObject", [obj]))

    @jsii.member(jsii_name="fromText")
    @builtins.classmethod
    def from_text(cls, text: builtins.str) -> "ScheduleTargetInput":
        '''Pass simple text to the target.

        For passing complex values like JSON object to a target use method
        ``ScheduleTargetInput.fromObject()`` instead.

        :param text: Text to use as the input for the target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0925fac0caa3d8fe93a0fe4320d4f08133f45e33174afd1af78bf68282a68524)
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        return typing.cast("ScheduleTargetInput", jsii.sinvoke(cls, "fromText", [text]))

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, schedule: ISchedule) -> builtins.str:
        '''Return the input properties for this input object.

        :param schedule: -
        '''
        ...


class _ScheduleTargetInputProxy(ScheduleTargetInput):
    @jsii.member(jsii_name="bind")
    def bind(self, schedule: ISchedule) -> builtins.str:
        '''Return the input properties for this input object.

        :param schedule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a35be52ccc2276f18b489131a0846e36e39c8e364f156c20793828399d6d4527)
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
        return typing.cast(builtins.str, jsii.invoke(self, "bind", [schedule]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, ScheduleTargetInput).__jsii_proxy_class__ = lambda : _ScheduleTargetInputProxy


class TimeWindow(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler.TimeWindow",
):
    '''A time window during which EventBridge Scheduler invokes the schedule.

    :exampleMetadata: infused

    Example::

        # target: targets.LambdaInvoke
        
        
        schedule = Schedule(self, "Schedule",
            schedule=ScheduleExpression.rate(Duration.hours(12)),
            target=target,
            time_window=TimeWindow.flexible(Duration.hours(10))
        )
    '''

    @jsii.member(jsii_name="flexible")
    @builtins.classmethod
    def flexible(cls, max_window: _Duration_4839e8c3) -> "TimeWindow":
        '''TimeWindow is enabled.

        :param max_window: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dd8fc85f0f89b4cd8d1345003a4cdf1c778546716260aab856c858e92935511)
            check_type(argname="argument max_window", value=max_window, expected_type=type_hints["max_window"])
        return typing.cast("TimeWindow", jsii.sinvoke(cls, "flexible", [max_window]))

    @jsii.member(jsii_name="off")
    @builtins.classmethod
    def off(cls) -> "TimeWindow":
        '''TimeWindow is disabled.'''
        return typing.cast("TimeWindow", jsii.sinvoke(cls, "off", []))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        '''Determines whether the schedule is invoked within a flexible time window.'''
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @builtins.property
    @jsii.member(jsii_name="maxWindow")
    def max_window(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum time window during which the schedule can be invoked.

        Must be between 1 to 1440 minutes.

        :default: - no value
        '''
        return typing.cast(typing.Optional[_Duration_4839e8c3], jsii.get(self, "maxWindow"))


__all__ = [
    "CfnSchedule",
    "CfnScheduleGroup",
    "CfnScheduleGroupProps",
    "CfnScheduleProps",
    "ContextAttribute",
    "CronOptionsWithTimezone",
    "ISchedule",
    "IScheduleGroup",
    "IScheduleTarget",
    "Schedule",
    "ScheduleExpression",
    "ScheduleGroup",
    "ScheduleGroupProps",
    "ScheduleProps",
    "ScheduleTargetConfig",
    "ScheduleTargetInput",
    "TimeWindow",
]

publication.publish()

def _typecheckingstub__503b74ac170f15626de2456b6f8c40d2cdc1ab21574c821e051517099f516ea4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    flexible_time_window: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.FlexibleTimeWindowProperty, typing.Dict[builtins.str, typing.Any]]],
    schedule_expression: builtins.str,
    target: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.TargetProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    end_date: typing.Optional[builtins.str] = None,
    group_name: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    schedule_expression_timezone: typing.Optional[builtins.str] = None,
    start_date: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__859c33780944a757aa0069dfe861a7f9ee3aaa6d51b1881276590d23b3cbc11d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c9dd58f37a9f244d09bdbca3ac4ea0869a0855a2cb760325d51c0d8beed730d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__596e14fe3c5d30f5608996086027eaf3ff49cf0205d5a551a9e0895e2be75f2a(
    value: typing.Union[_IResolvable_da3f097b, CfnSchedule.FlexibleTimeWindowProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86a3656a00e3dadf75b2e58b2162ed9850cd46df81630349120c362c216f94db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9658077cef2602ca00d25f391105ce442d6a0a3efef1ca5be55db053ede80a78(
    value: typing.Union[_IResolvable_da3f097b, CfnSchedule.TargetProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5864139b51db95ec1c3e6c947b577675bb4f83133b1f5476864d71c4009c2386(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3d0ae7ef525e3a588544a09eb7ec3271c357974ae47f41180a7aeb9086e2594(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1860ec4ad4204d90b7f2756ff633582f92f7f97d174b16a7da8e36811ebdc98(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c65947df9a6be40d839d971ea07ff6a85493b9cfbab03c61fc17e54bdd0e9276(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb6bd8d80ac829e96128e011c87e852bfea080bdcd859bfdf98c7874542dc1b5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb337d25b9d34da19dbe88b72514ea1e1e7a235cd91b7597abecd038498e11a9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38fc94567c401ce05bf3ed2461327df25f05b71764228be5a3f95fec0573d007(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__986ef975482735e4fbf46592da626ebfd4ca9636ad053fe886d40f9856d1483e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4be9629f7b1d55fb08861d6713480d5fa198e6e40012bcf701a627e532032afb(
    *,
    subnets: typing.Sequence[builtins.str],
    assign_public_ip: typing.Optional[builtins.str] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d8897162eaa13dfb81dc83e782d5936ed604f09ed623574ad9d0fabc4a1ab7e(
    *,
    capacity_provider: builtins.str,
    base: typing.Optional[jsii.Number] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__147909ee33401019ceeec9c9c260dd3ac0812db04c597e1b63c26f0608f61069(
    *,
    arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dc612a243a7e6a4107ac15e844d139b177440cb37d514af299c8365e71f4cf1(
    *,
    task_definition_arn: builtins.str,
    capacity_provider_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.CapacityProviderStrategyItemProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    enable_ecs_managed_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_execute_command: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    group: typing.Optional[builtins.str] = None,
    launch_type: typing.Optional[builtins.str] = None,
    network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    placement_constraints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.PlacementConstraintProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    placement_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.PlacementStrategyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    platform_version: typing.Optional[builtins.str] = None,
    propagate_tags: typing.Optional[builtins.str] = None,
    reference_id: typing.Optional[builtins.str] = None,
    tags: typing.Any = None,
    task_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0e0c05434c8347bffb5179e8c9bc22fdc3ff4fdae681d5b9d995e0f7c8c1900(
    *,
    detail_type: builtins.str,
    source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d4dffb710d1a3208f37cc6de0f2cddceb53e1178391bdc54cfedb8ca6626ec4(
    *,
    mode: builtins.str,
    maximum_window_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21a3b10246bef07a2f7fc56bf58e08c66b0fd77f7770804a87bf867fa8541cbb(
    *,
    partition_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__428ddbfd1435a3560f182001dfcf151c620cba65c309e87341f84eb7d60ba492(
    *,
    awsvpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.AwsVpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb19941ef1169a4cc78daf82b7ea64663f5a28f890fbeded34448dd3f0a3c16f(
    *,
    expression: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d9dc80c7a08a059d79aa3db1c44bcc28c84872422d6fd991bbca1124a384865(
    *,
    field: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb66e495a2f0291cd0e58a71fc127fa67ed8d10f2d977b132a1770f7b3a1f92d(
    *,
    maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c29c10cb7c0592826b32a3dc5e923a7c8d2f8b6bd9a0fe45759d650269d9f4d(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0de727f226b2279098ba22fdf1aa02e57d81187ed9063acc8d789604e1a7f88(
    *,
    pipeline_parameter_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.SageMakerPipelineParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13762215f810c9b64aba5ce7769b7babcff69eaa35d5d19f712b7515022da7fb(
    *,
    message_group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd5d0419478021d0554d24683f11134f17bb914856367055c32d004d8348a516(
    *,
    arn: builtins.str,
    role_arn: builtins.str,
    dead_letter_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.DeadLetterConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ecs_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.EcsParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    event_bridge_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.EventBridgeParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    input: typing.Optional[builtins.str] = None,
    kinesis_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.KinesisParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.RetryPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sage_maker_pipeline_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.SageMakerPipelineParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sqs_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.SqsParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55d5637c9b973d98ef3a23b13bf274e0a35bc07dfc27542f9b7185600a26a15e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e179ed3a5ae801985e05b869adcf8daec39217aada45fa23844dd021dea92bda(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a163f755c33c470bd9bc8ba9ec2282566382000d7a5adbc8bba7aa9bd8e707d3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e895b806668d11dd73b56d4fec496161e9b77b48c3e3475d06f4798d8a636529(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c803209b899e8ad5a9aaaa50de8f083948fedec73e43cc9c9b541cd5fdf20f5a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9ebba0a3ae0883796e2ff900e8a82e62b8e0870420b26e180905979808a13e7(
    *,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7259f3f17d67e55e8ad4459f637d0d8aa80d57d58cb928f6b0403a6097a4ecf1(
    *,
    flexible_time_window: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.FlexibleTimeWindowProperty, typing.Dict[builtins.str, typing.Any]]],
    schedule_expression: builtins.str,
    target: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSchedule.TargetProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    end_date: typing.Optional[builtins.str] = None,
    group_name: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    schedule_expression_timezone: typing.Optional[builtins.str] = None,
    start_date: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3ffc32f8d37e5b3c60f6299c8f15649e00e5778ef81be54ecc2ffbb99ac1bbc(
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c87f71f166be27f7417012dedd810bd7b3cedb2ec7d0a0493ca36f93993f6c5b(
    *,
    day: typing.Optional[builtins.str] = None,
    hour: typing.Optional[builtins.str] = None,
    minute: typing.Optional[builtins.str] = None,
    month: typing.Optional[builtins.str] = None,
    week_day: typing.Optional[builtins.str] = None,
    year: typing.Optional[builtins.str] = None,
    time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__190f03a36ab90eca0db1bdfd7c06d5891c61b69defb1c7be61f45d771a66e130(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__579ff4205e0ccb1830f899a44fc742e9853277ba0f82091be749e20b4fdbf1c2(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66f280f7a41957c98ada2240887b088985bbe273d1067b2c4f83f8ca69d09aae(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f189e0a2b180ceb7d47a54524a64df15a2d1c7a5efe1e25873a64a68692c1d18(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1a1c48be5584426072c1f842a1e31e59436e2cefe7df9e84b5a3115ad743d3e(
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

def _typecheckingstub__43e3d3a73dae7296d8e1b29562f7a8fbdf941fb9885fa0ddcc13164e2352e68d(
    error_code: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__1db14aa1db4d786b1846e49587706992ee79b66245d52b5efebd763ccbd24c94(
    _schedule: ISchedule,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5e74b4c774095daccbb01abe34df777261be2bfce9f7ec773cd8688b17dbb98(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    schedule: ScheduleExpression,
    target: IScheduleTarget,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    end: typing.Optional[datetime.datetime] = None,
    key: typing.Optional[_IKey_5f11635f] = None,
    schedule_group: typing.Optional[IScheduleGroup] = None,
    schedule_name: typing.Optional[builtins.str] = None,
    start: typing.Optional[datetime.datetime] = None,
    time_window: typing.Optional[TimeWindow] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1372455178922293375a1300f4c6e69cee5bc442b16f4036c84aafb7d9332f93(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    schedule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e9697edf3bddfcbab866b7220407b409d24e19d71a4831cc2eae389b626c1d7(
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

def _typecheckingstub__897a723a752bdf5a7cbd4dc9c673edd8862b55def0dfc20984054c323d651b0d(
    error_code: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__175909e9c50b88b6e35fc2db4998caa986e6da11a9a20dbde9c02ee1ca0b00b8(
    date: datetime.datetime,
    time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21e89766a8d616bfc00e75a22774b5d41c55681b6f5f623f08f201c835dd2902(
    expression: builtins.str,
    time_zone: typing.Optional[_TimeZone_cdd72ac9] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97a45c9b75fc81cb3d47817d0893dffb28ebc87496c4a4eedb9cf73b57a68cc5(
    duration: _Duration_4839e8c3,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__736972893d2822201f3b54995126456a9f4766921d769ea7836c13c49c015d53(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    schedule_group_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7b5a1fbdcbfd0ad106f45caf1d995619df8d064b8587659c5461157f6e48926(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c77731a2b0fb48c74a722651a8f036cef9066af4a6dd7b73c0b9b2d119bc36d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    schedule_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0eef3cd9167e1bcf64df7282dec1f362eaac5659d22625afac3c28dcc0b7edb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    schedule_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1603de1685aaaf14ff1514df8394bc631af9b5e6f8b79a44c31ff5e24157a7e0(
    grantee: _IGrantable_71c4f5de,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15bda48b16b2099393ebcd41e9be05dd66aaf7faaeae1ba65b42220d7667bce5(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55a9d37bafcef8d26af6e888f5ab8b2aef1359b02c7a510049f6e900c986b797(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2cc2856526773b02c8dfcbfcca6cf534cc4a4b00a0b0de1e8fe166c071534ab(
    identity: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__634bd225463be60303d9d1588926bbaa9fbd72c940ca54fecf9724d90fdefe64(
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

def _typecheckingstub__ca970bf647095b0a6fd282ecce93e19b12761be780f7fac1db8cc3b6f97c0cbf(
    error_code: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__00f616ddd843f7dab1625531f0a0666a403b81004bd707155fc676f64bb15c34(
    *,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    schedule_group_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1a1cbc6cf4c30e6930150f969adcdfef2b116842e4bcb34a1adcf13677e296f(
    *,
    schedule: ScheduleExpression,
    target: IScheduleTarget,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    end: typing.Optional[datetime.datetime] = None,
    key: typing.Optional[_IKey_5f11635f] = None,
    schedule_group: typing.Optional[IScheduleGroup] = None,
    schedule_name: typing.Optional[builtins.str] = None,
    start: typing.Optional[datetime.datetime] = None,
    time_window: typing.Optional[TimeWindow] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39b25a1f04a872a013c3ee593bb9140da10796639b130bc7f2461018358c6292(
    *,
    arn: builtins.str,
    role: _IRole_235f5d8e,
    dead_letter_config: typing.Optional[typing.Union[CfnSchedule.DeadLetterConfigProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    ecs_parameters: typing.Optional[typing.Union[CfnSchedule.EcsParametersProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    event_bridge_parameters: typing.Optional[typing.Union[CfnSchedule.EventBridgeParametersProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    input: typing.Optional[ScheduleTargetInput] = None,
    kinesis_parameters: typing.Optional[typing.Union[CfnSchedule.KinesisParametersProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    retry_policy: typing.Optional[typing.Union[CfnSchedule.RetryPolicyProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    sage_maker_pipeline_parameters: typing.Optional[typing.Union[CfnSchedule.SageMakerPipelineParametersProperty, typing.Dict[builtins.str, typing.Any]]] = None,
    sqs_parameters: typing.Optional[typing.Union[CfnSchedule.SqsParametersProperty, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fdac9a672a0bc2eb981e9971ac41140aa1074946d827f45e5c9d4d78673f0cd(
    obj: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0925fac0caa3d8fe93a0fe4320d4f08133f45e33174afd1af78bf68282a68524(
    text: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a35be52ccc2276f18b489131a0846e36e39c8e364f156c20793828399d6d4527(
    schedule: ISchedule,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dd8fc85f0f89b4cd8d1345003a4cdf1c778546716260aab856c858e92935511(
    max_window: _Duration_4839e8c3,
) -> None:
    """Type checking stubs"""
    pass
