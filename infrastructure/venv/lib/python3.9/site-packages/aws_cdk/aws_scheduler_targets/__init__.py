r'''
# Amazon EventBridge Scheduler Targets Construct Library

[Amazon EventBridge Scheduler](https://aws.amazon.com/blogs/compute/introducing-amazon-eventbridge-scheduler/) is a feature from Amazon EventBridge
that allows you to create, run, and manage scheduled tasks at scale. With EventBridge Scheduler, you can schedule millions of one-time or recurring tasks across various AWS services without provisioning or managing underlying infrastructure.

This library contains integration classes for Amazon EventBridge Scheduler to call any
number of supported AWS Services.

The following targets are supported:

1. `targets.LambdaInvoke`: [Invoke an AWS Lambda function](#invoke-a-lambda-function)
2. `targets.StepFunctionsStartExecution`: [Start an AWS Step Function](#start-an-aws-step-function)
3. `targets.CodeBuildStartBuild`: [Start a CodeBuild job](#start-a-codebuild-job)
4. `targets.SqsSendMessage`: [Send a Message to an Amazon SQS Queue](#send-a-message-to-an-sqs-queue)
5. `targets.SnsPublish`: [Publish messages to an Amazon SNS topic](#publish-messages-to-an-amazon-sns-topic)
6. `targets.EventBridgePutEvents`: [Put Events on EventBridge](#send-events-to-an-eventbridge-event-bus)
7. `targets.InspectorStartAssessmentRun`: [Start an Amazon Inspector assessment run](#start-an-amazon-inspector-assessment-run)
8. `targets.KinesisStreamPutRecord`: [Put a record to an Amazon Kinesis Data Stream](#put-a-record-to-an-amazon-kinesis-data-stream)
9. `targets.FirehosePutRecord`: [Put a record to an Amazon Data Firehose](#put-a-record-to-an-amazon-data-firehose)
10. `targets.CodePipelineStartPipelineExecution`: [Start a CodePipeline execution](#start-a-codepipeline-execution)
11. `targets.SageMakerStartPipelineExecution`: [Start a SageMaker pipeline execution](#start-a-sagemaker-pipeline-execution)
12. `targets.EcsRunTask`: [Start a new ECS task](#schedule-an-ecs-task-run)
13. `targets.Universal`: [Invoke a wider set of AWS API](#invoke-a-wider-set-of-aws-api)

## Invoke a Lambda function

Use the `LambdaInvoke` target to invoke a lambda function.

The code snippet below creates an event rule with a Lambda function as a target
called every hour by EventBridge Scheduler with a custom payload. You can optionally attach a
[dead letter queue](https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html).

```python
import aws_cdk.aws_lambda as lambda_


fn = lambda_.Function(self, "MyFunc",
    runtime=lambda_.Runtime.NODEJS_LATEST,
    handler="index.handler",
    code=lambda_.Code.from_inline("exports.handler = handler.toString()")
)

dlq = sqs.Queue(self, "DLQ",
    queue_name="MyDLQ"
)

target = targets.LambdaInvoke(fn,
    dead_letter_queue=dlq,
    max_event_age=Duration.minutes(1),
    retry_attempts=3,
    input=ScheduleTargetInput.from_object({
        "payload": "useful"
    })
)

schedule = Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.hours(1)),
    target=target
)
```

## Start an AWS Step Function

Use the `StepFunctionsStartExecution` target to start a new execution on a StepFunction.

The code snippet below creates an event rule with a Step Function as a target
called every hour by EventBridge Scheduler with a custom payload.

```python
import aws_cdk.aws_stepfunctions as sfn
import aws_cdk.aws_stepfunctions_tasks as tasks


payload = {
    "Name": "MyParameter",
    "Value": "🌥️"
}

put_parameter_step = tasks.CallAwsService(self, "PutParameter",
    service="ssm",
    action="putParameter",
    iam_resources=["*"],
    parameters={
        "Name.$": "$.Name",
        "Value.$": "$.Value",
        "Type": "String",
        "Overwrite": True
    }
)

state_machine = sfn.StateMachine(self, "StateMachine",
    definition_body=sfn.DefinitionBody.from_chainable(put_parameter_step)
)

Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.hours(1)),
    target=targets.StepFunctionsStartExecution(state_machine,
        input=ScheduleTargetInput.from_object(payload)
    )
)
```

## Start a CodeBuild job

Use the `CodeBuildStartBuild` target to start a new build run on a CodeBuild project.

The code snippet below creates an event rule with a CodeBuild project as target which is
called every hour by EventBridge Scheduler.

```python
import aws_cdk.aws_codebuild as codebuild

# project: codebuild.Project


Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.minutes(60)),
    target=targets.CodeBuildStartBuild(project)
)
```

## Send a Message To an SQS Queue

Use the `SqsSendMessage` target to send a message to an SQS Queue.

The code snippet below creates an event rule with an SQS Queue as a target
called every hour by EventBridge Scheduler with a custom payload.

Contains the `messageGroupId` to use when the target is a FIFO queue. If you specify
a FIFO queue as a target, the queue must have content-based deduplication enabled.

```python
payload = "test"
message_group_id = "id"
queue = sqs.Queue(self, "MyQueue",
    fifo=True,
    content_based_deduplication=True
)

target = targets.SqsSendMessage(queue,
    input=ScheduleTargetInput.from_text(payload),
    message_group_id=message_group_id
)

Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.minutes(1)),
    target=target
)
```

## Publish messages to an Amazon SNS topic

Use the `SnsPublish` target to publish messages to an Amazon SNS topic.

The code snippets below create an event rule with a Amazon SNS topic as a target.
It's called every hour by Amazon EventBridge Scheduler with a custom payload.

```python
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
```

## Send events to an EventBridge event bus

Use the `EventBridgePutEvents` target to send events to an EventBridge event bus.

The code snippet below creates an event rule with an EventBridge event bus as a target
called every hour by EventBridge Scheduler with a custom event payload.

```python
import aws_cdk.aws_events as events


event_bus = events.EventBus(self, "EventBus",
    event_bus_name="DomainEvents"
)

event_entry = targets.EventBridgePutEventsEntry(
    event_bus=event_bus,
    source="PetService",
    detail=ScheduleTargetInput.from_object({"Name": "Fluffy"}),
    detail_type="🐶"
)

Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.hours(1)),
    target=targets.EventBridgePutEvents(event_entry)
)
```

## Start an Amazon Inspector assessment run

Use the `InspectorStartAssessmentRun` target to start an Inspector assessment run.

The code snippet below creates an event rule with an assessment template as the target which is
called every hour by EventBridge Scheduler.

```python
import aws_cdk.aws_inspector as inspector

# cfn_assessment_template: inspector.CfnAssessmentTemplate


assessment_template = inspector.AssessmentTemplate.from_cfn_assessment_template(self, "MyAssessmentTemplate", cfn_assessment_template)

Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.minutes(60)),
    target=targets.InspectorStartAssessmentRun(assessment_template)
)
```

## Put a record to an Amazon Kinesis Data Stream

Use the `KinesisStreamPutRecord` target to put a record to an Amazon Kinesis Data Stream.

The code snippet below creates an event rule with a stream as the target which is
called every hour by EventBridge Scheduler.

```python
import aws_cdk.aws_kinesis as kinesis


stream = kinesis.Stream(self, "MyStream")

Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.minutes(60)),
    target=targets.KinesisStreamPutRecord(stream,
        partition_key="key"
    )
)
```

## Put a record to an Amazon Data Firehose

Use the `FirehosePutRecord` target to put a record to an Amazon Data Firehose delivery stream.

The code snippet below creates an event rule with a delivery stream as a target
called every hour by EventBridge Scheduler with a custom payload.

```python
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
```

## Start a CodePipeline execution

Use the `CodePipelineStartPipelineExecution` target to start a new execution for a CodePipeline pipeline.

The code snippet below creates an event rule with a CodePipeline pipeline as the target which is
called every hour by EventBridge Scheduler.

```python
import aws_cdk.aws_codepipeline as codepipeline

# pipeline: codepipeline.Pipeline


Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.minutes(60)),
    target=targets.CodePipelineStartPipelineExecution(pipeline)
)
```

## Start a SageMaker pipeline execution

Use the `SageMakerStartPipelineExecution` target to start a new execution for a SageMaker pipeline.

The code snippet below creates an event rule with a SageMaker pipeline as the target which is
called every hour by EventBridge Scheduler.

```python
import aws_cdk.aws_sagemaker as sagemaker

# pipeline: sagemaker.IPipeline


Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.minutes(60)),
    target=targets.SageMakerStartPipelineExecution(pipeline,
        pipeline_parameter_list=[targets.SageMakerPipelineParameter(
            name="parameter-name",
            value="parameter-value"
        )]
    )
)
```

## Schedule an ECS task run

Use the `EcsRunTask` target to schedule an ECS task run for a cluster.

The code snippet below creates an event rule with a Fargate task definition and cluster as the target which is called every hour by EventBridge Scheduler.

```python
import aws_cdk.aws_ecs as ecs

# cluster: ecs.ICluster
# task_definition: ecs.FargateTaskDefinition


Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(cdk.Duration.minutes(60)),
    target=targets.EcsRunFargateTask(cluster,
        task_definition=task_definition
    )
)
```

The code snippet below creates an event rule with a EC2 task definition and cluster as the target which is called every hour by EventBridge Scheduler.

```python
import aws_cdk.aws_ecs as ecs

# cluster: ecs.ICluster
# task_definition: ecs.Ec2TaskDefinition


Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(cdk.Duration.minutes(60)),
    target=targets.EcsRunEc2Task(cluster,
        task_definition=task_definition
    )
)
```

## Invoke a wider set of AWS API

Use the `Universal` target to invoke AWS API. See [https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-targets-universal.html](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-targets-universal.html)

The code snippet below creates an event rule with AWS API as the target which is
called at midnight every day by EventBridge Scheduler.

```python
Schedule(self, "Schedule",
    schedule=ScheduleExpression.cron(
        minute="0",
        hour="0"
    ),
    target=targets.Universal(
        service="rds",
        action="stopDBCluster",
        input=ScheduleTargetInput.from_object({
            "DbClusterIdentifier": "my-db"
        })
    )
)
```

The `service` must be in lowercase and the `action` must be in camelCase.

By default, an IAM policy for the Scheduler is extracted from the API call. The action in the policy is constructed using the `service` and `action` prop.
Re-using the example above, the action will be `rds:stopDBCluster`. Note that not all IAM actions follow the same pattern. In such scenario, please use the
`policyStatements` prop to override the policy:

```python
Schedule(self, "Schedule",
    schedule=ScheduleExpression.rate(Duration.minutes(60)),
    target=targets.Universal(
        service="sqs",
        action="sendMessage",
        policy_statements=[
            iam.PolicyStatement(
                actions=["sqs:SendMessage"],
                resources=["arn:aws:sqs:us-east-1:123456789012:my_queue"]
            ),
            iam.PolicyStatement(
                actions=["kms:Decrypt", "kms:GenerateDataKey*"],
                resources=["arn:aws:kms:us-east-1:123456789012:key/0987dcba-09fe-87dc-65ba-ab0987654321"]
            )
        ]
    )
)
```

> Note: The default policy uses `*` in the resources field as CDK does not have a straight forward way to auto-discover the resources permission required.
> It is recommended that you scope the field down to specific resources to have a better security posture.
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

from .. import Duration as _Duration_4839e8c3
from ..aws_codebuild import IProject as _IProject_aafae30a
from ..aws_codepipeline import IPipeline as _IPipeline_0931f838
from ..aws_ec2 import (
    ISecurityGroup as _ISecurityGroup_acf8a799,
    SubnetSelection as _SubnetSelection_e57d76df,
)
from ..aws_ecs import (
    CapacityProviderStrategy as _CapacityProviderStrategy_8d7b6657,
    FargatePlatformVersion as _FargatePlatformVersion_55d8be5c,
    ICluster as _ICluster_16cddd09,
    PlacementConstraint as _PlacementConstraint_11d82a52,
    PlacementStrategy as _PlacementStrategy_2bb6c232,
    TaskDefinition as _TaskDefinition_a541a103,
)
from ..aws_events import IEventBus as _IEventBus_88d13111
from ..aws_iam import (
    IRole as _IRole_235f5d8e, PolicyStatement as _PolicyStatement_0fe33853
)
from ..aws_inspector import IAssessmentTemplate as _IAssessmentTemplate_495c2d4e
from ..aws_kinesis import IStream as _IStream_4e2457d2
from ..aws_kinesisfirehose import IDeliveryStream as _IDeliveryStream_8f118861
from ..aws_lambda import IFunction as _IFunction_6adb0ab8
from ..aws_sagemaker import IPipeline as _IPipeline_3f0dad92
from ..aws_scheduler import (
    ISchedule as _ISchedule_4a32574d,
    IScheduleTarget as _IScheduleTarget_46344d95,
    ScheduleTargetConfig as _ScheduleTargetConfig_74216353,
    ScheduleTargetInput as _ScheduleTargetInput_dd30d070,
)
from ..aws_sns import ITopic as _ITopic_9eca4852
from ..aws_sqs import IQueue as _IQueue_7ed6f679
from ..aws_stepfunctions import IStateMachine as _IStateMachine_73e8d2b0


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler_targets.EventBridgePutEventsEntry",
    jsii_struct_bases=[],
    name_mapping={
        "detail": "detail",
        "detail_type": "detailType",
        "event_bus": "eventBus",
        "source": "source",
    },
)
class EventBridgePutEventsEntry:
    def __init__(
        self,
        *,
        detail: _ScheduleTargetInput_dd30d070,
        detail_type: builtins.str,
        event_bus: _IEventBus_88d13111,
        source: builtins.str,
    ) -> None:
        '''An entry to be sent to EventBridge.

        :param detail: The event body. Can either be provided as an object or as a JSON-serialized string
        :param detail_type: Used along with the source field to help identify the fields and values expected in the detail field. For example, events by CloudTrail have detail type "AWS API Call via CloudTrail"
        :param event_bus: The event bus the entry will be sent to.
        :param source: The service or application that caused this event to be generated. Example value: ``com.example.service``

        :see: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEventsRequestEntry.html
        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_events as events
            
            
            event_bus = events.EventBus(self, "EventBus",
                event_bus_name="DomainEvents"
            )
            
            event_entry = targets.EventBridgePutEventsEntry(
                event_bus=event_bus,
                source="PetService",
                detail=ScheduleTargetInput.from_object({"Name": "Fluffy"}),
                detail_type="🐶"
            )
            
            Schedule(self, "Schedule",
                schedule=ScheduleExpression.rate(Duration.hours(1)),
                target=targets.EventBridgePutEvents(event_entry)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c20ea1ffb2760df785aee8014a687654066d35e08ebf631810b29af40f20952b)
            check_type(argname="argument detail", value=detail, expected_type=type_hints["detail"])
            check_type(argname="argument detail_type", value=detail_type, expected_type=type_hints["detail_type"])
            check_type(argname="argument event_bus", value=event_bus, expected_type=type_hints["event_bus"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detail": detail,
            "detail_type": detail_type,
            "event_bus": event_bus,
            "source": source,
        }

    @builtins.property
    def detail(self) -> _ScheduleTargetInput_dd30d070:
        '''The event body.

        Can either be provided as an object or as a JSON-serialized string

        Example::

            ScheduleTargetInput.from_text("{\"instance-id\": \"i-1234567890abcdef0\", \"state\": \"terminated\"}")
            ScheduleTargetInput.from_object({"Message": "Hello from a friendly event :)"})
        '''
        result = self._values.get("detail")
        assert result is not None, "Required property 'detail' is missing"
        return typing.cast(_ScheduleTargetInput_dd30d070, result)

    @builtins.property
    def detail_type(self) -> builtins.str:
        '''Used along with the source field to help identify the fields and values expected in the detail field.

        For example, events by CloudTrail have detail type "AWS API Call via CloudTrail"

        :see: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html
        '''
        result = self._values.get("detail_type")
        assert result is not None, "Required property 'detail_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_bus(self) -> _IEventBus_88d13111:
        '''The event bus the entry will be sent to.'''
        result = self._values.get("event_bus")
        assert result is not None, "Required property 'event_bus' is missing"
        return typing.cast(_IEventBus_88d13111, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''The service or application that caused this event to be generated.

        Example value: ``com.example.service``

        :see: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventBridgePutEventsEntry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler_targets.SageMakerPipelineParameter",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class SageMakerPipelineParameter:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''Properties for a pipeline parameter.

        :param name: Name of parameter to start execution of a SageMaker Model Building Pipeline.
        :param value: Value of parameter to start execution of a SageMaker Model Building Pipeline.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_scheduler_targets as scheduler_targets
            
            sage_maker_pipeline_parameter = scheduler_targets.SageMakerPipelineParameter(
                name="name",
                value="value"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9b88d9119f8045f4c3b695d8ed58b7f5b8833e798cbc2660e4c8ba59fc95cb1)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of parameter to start execution of a SageMaker Model Building Pipeline.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of parameter to start execution of a SageMaker Model Building Pipeline.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SageMakerPipelineParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ScheduleTargetBase(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.ScheduleTargetBase",
):
    '''Base class for Schedule Targets.'''

    def __init__(
        self,
        base_props: typing.Union["ScheduleTargetBaseProps", typing.Dict[builtins.str, typing.Any]],
        target_arn: builtins.str,
    ) -> None:
        '''
        :param base_props: -
        :param target_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d830072c02aa1c93302e9c28e7f88fb42c5a6a2a9deec3c567a7179aebb7d89)
            check_type(argname="argument base_props", value=base_props, expected_type=type_hints["base_props"])
            check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
        jsii.create(self.__class__, self, [base_props, target_arn])

    @jsii.member(jsii_name="addTargetActionToRole")
    @abc.abstractmethod
    def _add_target_action_to_role(self, role: _IRole_235f5d8e) -> None:
        '''
        :param role: -
        '''
        ...

    @jsii.member(jsii_name="bind")
    def bind(self, schedule: _ISchedule_4a32574d) -> _ScheduleTargetConfig_74216353:
        '''Create a return a Schedule Target Configuration for the given schedule.

        :param schedule: -

        :return: a Schedule Target Configuration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01737bee0bf8db4b920430443ea84a27c1c2f6246bd71927150a4fb28accc32d)
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
        return typing.cast(_ScheduleTargetConfig_74216353, jsii.invoke(self, "bind", [schedule]))

    @jsii.member(jsii_name="bindBaseTargetConfig")
    def _bind_base_target_config(
        self,
        _schedule: _ISchedule_4a32574d,
    ) -> _ScheduleTargetConfig_74216353:
        '''
        :param _schedule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd8a5015bbf00d1130163ba73634014dc8420ec6c2484ca7ca7e2d9776b12c60)
            check_type(argname="argument _schedule", value=_schedule, expected_type=type_hints["_schedule"])
        return typing.cast(_ScheduleTargetConfig_74216353, jsii.invoke(self, "bindBaseTargetConfig", [_schedule]))

    @builtins.property
    @jsii.member(jsii_name="targetArn")
    def _target_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetArn"))


class _ScheduleTargetBaseProxy(ScheduleTargetBase):
    @jsii.member(jsii_name="addTargetActionToRole")
    def _add_target_action_to_role(self, role: _IRole_235f5d8e) -> None:
        '''
        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13ff83395a9b3dcc596bc1aa8b656c8638facf50a6854e6d21772607443b3efc)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "addTargetActionToRole", [role]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, ScheduleTargetBase).__jsii_proxy_class__ = lambda : _ScheduleTargetBaseProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler_targets.ScheduleTargetBaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "input": "input",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "role": "role",
    },
)
class ScheduleTargetBaseProps:
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Base properties for a Schedule Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target

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
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29dad4add4695787b706ed4741ddf63b9b8130a1bdf3339dff7939d0917e60de)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if input is not None:
            self._values["input"] = input
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def input(self) -> typing.Optional[_ScheduleTargetInput_dd30d070]:
        '''Input passed to the target.

        :default: - no input.
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[_ScheduleTargetInput_dd30d070], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Scheduler sends to a target for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the target returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf.

        If none provided templates target will automatically create an IAM role with all the minimum necessary
        permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets
        will grant minimal required permissions.

        :default: - created by target
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduleTargetBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IScheduleTarget_46344d95)
class SnsPublish(
    ScheduleTargetBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.SnsPublish",
):
    '''Use an Amazon SNS topic as a target for AWS EventBridge Scheduler.

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

    def __init__(
        self,
        topic: _ITopic_9eca4852,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param topic: -
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__961b73901f7c52b4629b4552b6be3585368cfc6c4de258420a2e2c4c9108b398)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        props = ScheduleTargetBaseProps(
            dead_letter_queue=dead_letter_queue,
            input=input,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
            role=role,
        )

        jsii.create(self.__class__, self, [topic, props])

    @jsii.member(jsii_name="addTargetActionToRole")
    def _add_target_action_to_role(self, role: _IRole_235f5d8e) -> None:
        '''
        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6302629a59c54cd7dafc566171c4a283657f72f44a44767384888df0e6012021)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "addTargetActionToRole", [role]))


@jsii.implements(_IScheduleTarget_46344d95)
class SqsSendMessage(
    ScheduleTargetBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.SqsSendMessage",
):
    '''Use an Amazon SQS Queue as a target for AWS EventBridge Scheduler.

    :exampleMetadata: infused

    Example::

        payload = "test"
        message_group_id = "id"
        queue = sqs.Queue(self, "MyQueue",
            fifo=True,
            content_based_deduplication=True
        )
        
        target = targets.SqsSendMessage(queue,
            input=ScheduleTargetInput.from_text(payload),
            message_group_id=message_group_id
        )
        
        Schedule(self, "Schedule",
            schedule=ScheduleExpression.rate(Duration.minutes(1)),
            target=target
        )
    '''

    def __init__(
        self,
        queue: _IQueue_7ed6f679,
        *,
        message_group_id: typing.Optional[builtins.str] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param queue: -
        :param message_group_id: The FIFO message group ID to use as the target. This must be specified when the target is a FIFO queue. If you specify a FIFO queue as a target, the queue must have content-based deduplication enabled. A length of ``messageGroupId`` must be between 1 and 128. Default: - no message group ID
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a86c2fb46323ac8851887e951da0704b179c89e96fbc73b43048720c09f816d0)
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
        props = SqsSendMessageProps(
            message_group_id=message_group_id,
            dead_letter_queue=dead_letter_queue,
            input=input,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
            role=role,
        )

        jsii.create(self.__class__, self, [queue, props])

    @jsii.member(jsii_name="addTargetActionToRole")
    def _add_target_action_to_role(self, role: _IRole_235f5d8e) -> None:
        '''
        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eef58dbd8df5d2551bec19ddf4779f0177025eb93b55e41899b7c2ad6298258b)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "addTargetActionToRole", [role]))

    @jsii.member(jsii_name="bindBaseTargetConfig")
    def _bind_base_target_config(
        self,
        _schedule: _ISchedule_4a32574d,
    ) -> _ScheduleTargetConfig_74216353:
        '''
        :param _schedule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc4c92c6b396957e8236f2f491374f5459edff0144a288b6c967faa0660c413d)
            check_type(argname="argument _schedule", value=_schedule, expected_type=type_hints["_schedule"])
        return typing.cast(_ScheduleTargetConfig_74216353, jsii.invoke(self, "bindBaseTargetConfig", [_schedule]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler_targets.SqsSendMessageProps",
    jsii_struct_bases=[ScheduleTargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "input": "input",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "role": "role",
        "message_group_id": "messageGroupId",
    },
)
class SqsSendMessageProps(ScheduleTargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        message_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a SQS Queue Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        :param message_group_id: The FIFO message group ID to use as the target. This must be specified when the target is a FIFO queue. If you specify a FIFO queue as a target, the queue must have content-based deduplication enabled. A length of ``messageGroupId`` must be between 1 and 128. Default: - no message group ID

        :exampleMetadata: infused

        Example::

            payload = "test"
            message_group_id = "id"
            queue = sqs.Queue(self, "MyQueue",
                fifo=True,
                content_based_deduplication=True
            )
            
            target = targets.SqsSendMessage(queue,
                input=ScheduleTargetInput.from_text(payload),
                message_group_id=message_group_id
            )
            
            Schedule(self, "Schedule",
                schedule=ScheduleExpression.rate(Duration.minutes(1)),
                target=target
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9b071d098054dd80fee122aca519dd583724dcca2e31d39c850498cbc64a259)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument message_group_id", value=message_group_id, expected_type=type_hints["message_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if input is not None:
            self._values["input"] = input
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if role is not None:
            self._values["role"] = role
        if message_group_id is not None:
            self._values["message_group_id"] = message_group_id

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def input(self) -> typing.Optional[_ScheduleTargetInput_dd30d070]:
        '''Input passed to the target.

        :default: - no input.
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[_ScheduleTargetInput_dd30d070], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Scheduler sends to a target for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the target returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf.

        If none provided templates target will automatically create an IAM role with all the minimum necessary
        permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets
        will grant minimal required permissions.

        :default: - created by target
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def message_group_id(self) -> typing.Optional[builtins.str]:
        '''The FIFO message group ID to use as the target.

        This must be specified when the target is a FIFO queue. If you specify
        a FIFO queue as a target, the queue must have content-based deduplication enabled.

        A length of ``messageGroupId`` must be between 1 and 128.

        :default: - no message group ID

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sqsparameters.html#cfn-scheduler-schedule-sqsparameters-messagegroupid
        '''
        result = self._values.get("message_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqsSendMessageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IScheduleTarget_46344d95)
class StepFunctionsStartExecution(
    ScheduleTargetBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.StepFunctionsStartExecution",
):
    '''Use an AWS Step function as a target for AWS EventBridge Scheduler.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_stepfunctions as sfn
        import aws_cdk.aws_stepfunctions_tasks as tasks
        
        
        payload = {
            "Name": "MyParameter",
            "Value": "🌥️"
        }
        
        put_parameter_step = tasks.CallAwsService(self, "PutParameter",
            service="ssm",
            action="putParameter",
            iam_resources=["*"],
            parameters={
                "Name.$": "$.Name",
                "Value.$": "$.Value",
                "Type": "String",
                "Overwrite": True
            }
        )
        
        state_machine = sfn.StateMachine(self, "StateMachine",
            definition_body=sfn.DefinitionBody.from_chainable(put_parameter_step)
        )
        
        Schedule(self, "Schedule",
            schedule=ScheduleExpression.rate(Duration.hours(1)),
            target=targets.StepFunctionsStartExecution(state_machine,
                input=ScheduleTargetInput.from_object(payload)
            )
        )
    '''

    def __init__(
        self,
        state_machine: _IStateMachine_73e8d2b0,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param state_machine: -
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6f72a14975c4b50622c65c3545124a5a40541c99ee789b2764dd89dbe6db65e)
            check_type(argname="argument state_machine", value=state_machine, expected_type=type_hints["state_machine"])
        props = ScheduleTargetBaseProps(
            dead_letter_queue=dead_letter_queue,
            input=input,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
            role=role,
        )

        jsii.create(self.__class__, self, [state_machine, props])

    @jsii.member(jsii_name="addTargetActionToRole")
    def _add_target_action_to_role(self, role: _IRole_235f5d8e) -> None:
        '''
        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdb74e28e429f1b8574596c9b7d69dbbe6d4a87709fe0afeee3a982c558eefa6)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "addTargetActionToRole", [role]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler_targets.Tag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class Tag:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''Metadata that you apply to a resource to help categorize and organize the resource.

        Each tag consists of a key and an optional value, both of which you define.

        :param key: Key is the name of the tag.
        :param value: Value is the metadata contents of the tag.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_scheduler_targets as scheduler_targets
            
            tag = scheduler_targets.Tag(
                key="key",
                value="value"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d7e0165c9edbeca9c1f67729ca5e04e783483e5161d761577189cfb4595daf8)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Key is the name of the tag.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value is the metadata contents of the tag.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Tag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IScheduleTarget_46344d95)
class Universal(
    ScheduleTargetBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.Universal",
):
    '''Use a wider set of AWS API as a target for AWS EventBridge Scheduler.

    :see: https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-targets-universal.html
    :exampleMetadata: infused

    Example::

        Schedule(self, "Schedule",
            schedule=ScheduleExpression.cron(
                minute="0",
                hour="0"
            ),
            target=targets.Universal(
                service="rds",
                action="stopDBCluster",
                input=ScheduleTargetInput.from_object({
                    "DbClusterIdentifier": "my-db"
                })
            )
        )
    '''

    def __init__(
        self,
        *,
        action: builtins.str,
        service: builtins.str,
        policy_statements: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param action: The API action to call. Must be camelCase. You cannot use read-only API actions such as common GET operations.
        :param service: The AWS service to call. This must be in lowercase.
        :param policy_statements: The IAM policy statements needed to invoke the target. These statements are attached to the Scheduler's role. Note that the default may not be the correct actions as not all AWS services follows the same IAM action pattern, or there may be more actions needed to invoke the target. Default: - Policy with ``service:action`` action only.
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        '''
        props = UniversalTargetProps(
            action=action,
            service=service,
            policy_statements=policy_statements,
            dead_letter_queue=dead_letter_queue,
            input=input,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
            role=role,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="addTargetActionToRole")
    def _add_target_action_to_role(self, role: _IRole_235f5d8e) -> None:
        '''
        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__198e835ff77413b2cbd7a9aad16223af355077748c1e61e3dc51f2c3390c66ca)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "addTargetActionToRole", [role]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler_targets.UniversalTargetProps",
    jsii_struct_bases=[ScheduleTargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "input": "input",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "role": "role",
        "action": "action",
        "service": "service",
        "policy_statements": "policyStatements",
    },
)
class UniversalTargetProps(ScheduleTargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        action: builtins.str,
        service: builtins.str,
        policy_statements: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
    ) -> None:
        '''Properties for a Universal Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        :param action: The API action to call. Must be camelCase. You cannot use read-only API actions such as common GET operations.
        :param service: The AWS service to call. This must be in lowercase.
        :param policy_statements: The IAM policy statements needed to invoke the target. These statements are attached to the Scheduler's role. Note that the default may not be the correct actions as not all AWS services follows the same IAM action pattern, or there may be more actions needed to invoke the target. Default: - Policy with ``service:action`` action only.

        :exampleMetadata: infused

        Example::

            Schedule(self, "Schedule",
                schedule=ScheduleExpression.cron(
                    minute="0",
                    hour="0"
                ),
                target=targets.Universal(
                    service="rds",
                    action="stopDBCluster",
                    input=ScheduleTargetInput.from_object({
                        "DbClusterIdentifier": "my-db"
                    })
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aebf9e651de63ef570a11970d3762c22b62acdcb5386c5ba69076181e926f71)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument policy_statements", value=policy_statements, expected_type=type_hints["policy_statements"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "service": service,
        }
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if input is not None:
            self._values["input"] = input
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if role is not None:
            self._values["role"] = role
        if policy_statements is not None:
            self._values["policy_statements"] = policy_statements

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def input(self) -> typing.Optional[_ScheduleTargetInput_dd30d070]:
        '''Input passed to the target.

        :default: - no input.
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[_ScheduleTargetInput_dd30d070], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Scheduler sends to a target for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the target returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf.

        If none provided templates target will automatically create an IAM role with all the minimum necessary
        permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets
        will grant minimal required permissions.

        :default: - created by target
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def action(self) -> builtins.str:
        '''The API action to call. Must be camelCase.

        You cannot use read-only API actions such as common GET operations.

        :see: https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-targets-universal.html#unsupported-api-actions
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''The AWS service to call.

        This must be in lowercase.
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_statements(
        self,
    ) -> typing.Optional[typing.List[_PolicyStatement_0fe33853]]:
        '''The IAM policy statements needed to invoke the target. These statements are attached to the Scheduler's role.

        Note that the default may not be the correct actions as not all AWS services follows the same IAM action pattern, or there may be more actions needed to invoke the target.

        :default: - Policy with ``service:action`` action only.
        '''
        result = self._values.get("policy_statements")
        return typing.cast(typing.Optional[typing.List[_PolicyStatement_0fe33853]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UniversalTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IScheduleTarget_46344d95)
class CodeBuildStartBuild(
    ScheduleTargetBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.CodeBuildStartBuild",
):
    '''Use an AWS CodeBuild as a target for AWS EventBridge Scheduler.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_codebuild as codebuild
        
        # project: codebuild.Project
        
        
        Schedule(self, "Schedule",
            schedule=ScheduleExpression.rate(Duration.minutes(60)),
            target=targets.CodeBuildStartBuild(project)
        )
    '''

    def __init__(
        self,
        project: _IProject_aafae30a,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param project: -
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eacc4f0e06890a24c88fe0c8814a8e396c6c6442e38857fee0168c08fca876ea)
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
        props = ScheduleTargetBaseProps(
            dead_letter_queue=dead_letter_queue,
            input=input,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
            role=role,
        )

        jsii.create(self.__class__, self, [project, props])

    @jsii.member(jsii_name="addTargetActionToRole")
    def _add_target_action_to_role(self, role: _IRole_235f5d8e) -> None:
        '''
        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7638691fb0294fb00596be4967a0508a1091ee4b552678b943b548af397963ba)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "addTargetActionToRole", [role]))


@jsii.implements(_IScheduleTarget_46344d95)
class CodePipelineStartPipelineExecution(
    ScheduleTargetBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.CodePipelineStartPipelineExecution",
):
    '''Use an AWS CodePipeline pipeline as a target for AWS EventBridge Scheduler.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_codepipeline as codepipeline
        
        # pipeline: codepipeline.Pipeline
        
        
        Schedule(self, "Schedule",
            schedule=ScheduleExpression.rate(Duration.minutes(60)),
            target=targets.CodePipelineStartPipelineExecution(pipeline)
        )
    '''

    def __init__(
        self,
        pipeline: _IPipeline_0931f838,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param pipeline: -
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f972d090ad80411fc0dff42233ee8b4ff2a48be68b7d646d1c7606a3cfb7fe56)
            check_type(argname="argument pipeline", value=pipeline, expected_type=type_hints["pipeline"])
        props = ScheduleTargetBaseProps(
            dead_letter_queue=dead_letter_queue,
            input=input,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
            role=role,
        )

        jsii.create(self.__class__, self, [pipeline, props])

    @jsii.member(jsii_name="addTargetActionToRole")
    def _add_target_action_to_role(self, role: _IRole_235f5d8e) -> None:
        '''
        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31c5911116f5629c2adf9d1968007740095affaa6dad806ac8e1672101368386)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "addTargetActionToRole", [role]))


@jsii.implements(_IScheduleTarget_46344d95)
class EcsRunTask(
    ScheduleTargetBase,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.EcsRunTask",
):
    '''Schedule an ECS Task using AWS EventBridge Scheduler.'''

    def __init__(
        self,
        cluster: _ICluster_16cddd09,
        *,
        task_definition: _TaskDefinition_a541a103,
        capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_CapacityProviderStrategy_8d7b6657, typing.Dict[builtins.str, typing.Any]]]] = None,
        enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
        enable_execute_command: typing.Optional[builtins.bool] = None,
        group: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.bool] = None,
        reference_id: typing.Optional[builtins.str] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_count: typing.Optional[jsii.Number] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param cluster: -
        :param task_definition: The task definition to use for scheduled tasks. Note: this must be TaskDefinition, and not ITaskDefinition, as it requires properties that are not known for imported task definitions If you want to run a RunTask with an imported task definition, consider using a Universal target.
        :param capacity_provider_strategies: The capacity provider strategy to use for the task. Default: - No capacity provider strategy
        :param enable_ecs_managed_tags: Specifies whether to enable Amazon ECS managed tags for the task. Default: - false
        :param enable_execute_command: Whether to enable execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task. Default: - false
        :param group: Specifies an ECS task group for the task. Default: - No group
        :param propagate_tags: Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Default: - No tag propagation
        :param reference_id: The reference ID to use for the task. Default: - No reference ID.
        :param security_groups: The security groups associated with the task. These security groups must all be in the same VPC. Controls inbound and outbound network access for the task. Default: - The security group for the VPC is used.
        :param tags: The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Default: - No tags
        :param task_count: The number of tasks to create based on TaskDefinition. Default: 1
        :param vpc_subnets: The subnets associated with the task. These subnets must all be in the same VPC. The task will be launched in these subnets. Default: - all private subnets of the VPC are selected.
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ddc91e6308e91fc95fa167254f8538961d19df122eeefb13d6881448afdc147)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
        props = EcsRunTaskBaseProps(
            task_definition=task_definition,
            capacity_provider_strategies=capacity_provider_strategies,
            enable_ecs_managed_tags=enable_ecs_managed_tags,
            enable_execute_command=enable_execute_command,
            group=group,
            propagate_tags=propagate_tags,
            reference_id=reference_id,
            security_groups=security_groups,
            tags=tags,
            task_count=task_count,
            vpc_subnets=vpc_subnets,
            dead_letter_queue=dead_letter_queue,
            input=input,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
            role=role,
        )

        jsii.create(self.__class__, self, [cluster, props])

    @jsii.member(jsii_name="addTargetActionToRole")
    def _add_target_action_to_role(self, role: _IRole_235f5d8e) -> None:
        '''
        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79f6648875df7112d642839162e2032e0cc5691244ea631e24984dc06b70af68)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "addTargetActionToRole", [role]))

    @jsii.member(jsii_name="bindBaseTargetConfig")
    def _bind_base_target_config(
        self,
        _schedule: _ISchedule_4a32574d,
    ) -> _ScheduleTargetConfig_74216353:
        '''
        :param _schedule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__658a297adc726b826b6ad0f740dd1153f7cd0ec47ab734b7e0c3748d30bd5285)
            check_type(argname="argument _schedule", value=_schedule, expected_type=type_hints["_schedule"])
        return typing.cast(_ScheduleTargetConfig_74216353, jsii.invoke(self, "bindBaseTargetConfig", [_schedule]))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def _cluster(self) -> _ICluster_16cddd09:
        return typing.cast(_ICluster_16cddd09, jsii.get(self, "cluster"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def _props(self) -> "EcsRunTaskBaseProps":
        return typing.cast("EcsRunTaskBaseProps", jsii.get(self, "props"))


class _EcsRunTaskProxy(
    EcsRunTask,
    jsii.proxy_for(ScheduleTargetBase), # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, EcsRunTask).__jsii_proxy_class__ = lambda : _EcsRunTaskProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler_targets.EcsRunTaskBaseProps",
    jsii_struct_bases=[ScheduleTargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "input": "input",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "role": "role",
        "task_definition": "taskDefinition",
        "capacity_provider_strategies": "capacityProviderStrategies",
        "enable_ecs_managed_tags": "enableEcsManagedTags",
        "enable_execute_command": "enableExecuteCommand",
        "group": "group",
        "propagate_tags": "propagateTags",
        "reference_id": "referenceId",
        "security_groups": "securityGroups",
        "tags": "tags",
        "task_count": "taskCount",
        "vpc_subnets": "vpcSubnets",
    },
)
class EcsRunTaskBaseProps(ScheduleTargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        task_definition: _TaskDefinition_a541a103,
        capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_CapacityProviderStrategy_8d7b6657, typing.Dict[builtins.str, typing.Any]]]] = None,
        enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
        enable_execute_command: typing.Optional[builtins.bool] = None,
        group: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.bool] = None,
        reference_id: typing.Optional[builtins.str] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_count: typing.Optional[jsii.Number] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Parameters for scheduling ECS Run Task (common to EC2 and Fargate launch types).

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        :param task_definition: The task definition to use for scheduled tasks. Note: this must be TaskDefinition, and not ITaskDefinition, as it requires properties that are not known for imported task definitions If you want to run a RunTask with an imported task definition, consider using a Universal target.
        :param capacity_provider_strategies: The capacity provider strategy to use for the task. Default: - No capacity provider strategy
        :param enable_ecs_managed_tags: Specifies whether to enable Amazon ECS managed tags for the task. Default: - false
        :param enable_execute_command: Whether to enable execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task. Default: - false
        :param group: Specifies an ECS task group for the task. Default: - No group
        :param propagate_tags: Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Default: - No tag propagation
        :param reference_id: The reference ID to use for the task. Default: - No reference ID.
        :param security_groups: The security groups associated with the task. These security groups must all be in the same VPC. Controls inbound and outbound network access for the task. Default: - The security group for the VPC is used.
        :param tags: The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Default: - No tags
        :param task_count: The number of tasks to create based on TaskDefinition. Default: 1
        :param vpc_subnets: The subnets associated with the task. These subnets must all be in the same VPC. The task will be launched in these subnets. Default: - all private subnets of the VPC are selected.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_ec2 as ec2
            from aws_cdk import aws_ecs as ecs
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_scheduler as scheduler
            from aws_cdk import aws_scheduler_targets as scheduler_targets
            from aws_cdk import aws_sqs as sqs
            
            # queue: sqs.Queue
            # role: iam.Role
            # schedule_target_input: scheduler.ScheduleTargetInput
            # security_group: ec2.SecurityGroup
            # subnet: ec2.Subnet
            # subnet_filter: ec2.SubnetFilter
            # task_definition: ecs.TaskDefinition
            
            ecs_run_task_base_props = scheduler_targets.EcsRunTaskBaseProps(
                task_definition=task_definition,
            
                # the properties below are optional
                capacity_provider_strategies=[ecs.CapacityProviderStrategy(
                    capacity_provider="capacityProvider",
            
                    # the properties below are optional
                    base=123,
                    weight=123
                )],
                dead_letter_queue=queue,
                enable_ecs_managed_tags=False,
                enable_execute_command=False,
                group="group",
                input=schedule_target_input,
                max_event_age=cdk.Duration.minutes(30),
                propagate_tags=False,
                reference_id="referenceId",
                retry_attempts=123,
                role=role,
                security_groups=[security_group],
                tags=[scheduler_targets.Tag(
                    key="key",
                    value="value"
                )],
                task_count=123,
                vpc_subnets=ec2.SubnetSelection(
                    availability_zones=["availabilityZones"],
                    one_per_az=False,
                    subnet_filters=[subnet_filter],
                    subnet_group_name="subnetGroupName",
                    subnets=[subnet],
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                )
            )
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_e57d76df(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c784746a1d7efa2d6a0675e480c2ab5615af6620ac4fc75d4bc282aeb3ca6632)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
            check_type(argname="argument capacity_provider_strategies", value=capacity_provider_strategies, expected_type=type_hints["capacity_provider_strategies"])
            check_type(argname="argument enable_ecs_managed_tags", value=enable_ecs_managed_tags, expected_type=type_hints["enable_ecs_managed_tags"])
            check_type(argname="argument enable_execute_command", value=enable_execute_command, expected_type=type_hints["enable_execute_command"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
            check_type(argname="argument reference_id", value=reference_id, expected_type=type_hints["reference_id"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument task_count", value=task_count, expected_type=type_hints["task_count"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "task_definition": task_definition,
        }
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if input is not None:
            self._values["input"] = input
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if role is not None:
            self._values["role"] = role
        if capacity_provider_strategies is not None:
            self._values["capacity_provider_strategies"] = capacity_provider_strategies
        if enable_ecs_managed_tags is not None:
            self._values["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            self._values["enable_execute_command"] = enable_execute_command
        if group is not None:
            self._values["group"] = group
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags
        if reference_id is not None:
            self._values["reference_id"] = reference_id
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if tags is not None:
            self._values["tags"] = tags
        if task_count is not None:
            self._values["task_count"] = task_count
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def input(self) -> typing.Optional[_ScheduleTargetInput_dd30d070]:
        '''Input passed to the target.

        :default: - no input.
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[_ScheduleTargetInput_dd30d070], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Scheduler sends to a target for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the target returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf.

        If none provided templates target will automatically create an IAM role with all the minimum necessary
        permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets
        will grant minimal required permissions.

        :default: - created by target
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def task_definition(self) -> _TaskDefinition_a541a103:
        '''The task definition to use for scheduled tasks.

        Note: this must be TaskDefinition, and not ITaskDefinition,
        as it requires properties that are not known for imported task definitions
        If you want to run a RunTask with an imported task definition,
        consider using a Universal target.
        '''
        result = self._values.get("task_definition")
        assert result is not None, "Required property 'task_definition' is missing"
        return typing.cast(_TaskDefinition_a541a103, result)

    @builtins.property
    def capacity_provider_strategies(
        self,
    ) -> typing.Optional[typing.List[_CapacityProviderStrategy_8d7b6657]]:
        '''The capacity provider strategy to use for the task.

        :default: - No capacity provider strategy
        '''
        result = self._values.get("capacity_provider_strategies")
        return typing.cast(typing.Optional[typing.List[_CapacityProviderStrategy_8d7b6657]], result)

    @builtins.property
    def enable_ecs_managed_tags(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether to enable Amazon ECS managed tags for the task.

        :default: - false
        '''
        result = self._values.get("enable_ecs_managed_tags")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_execute_command(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable execute command functionality for the containers in this task.

        If true, this enables execute command functionality on all containers in the task.

        :default: - false
        '''
        result = self._values.get("enable_execute_command")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Specifies an ECS task group for the task.

        :default: - No group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def propagate_tags(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether to propagate the tags from the task definition to the task.

        If no value is specified, the tags are not propagated.

        :default: - No tag propagation
        '''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def reference_id(self) -> typing.Optional[builtins.str]:
        '''The reference ID to use for the task.

        :default: - No reference ID.
        '''
        result = self._values.get("reference_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_acf8a799]]:
        '''The security groups associated with the task.

        These security groups must all be in the same VPC.
        Controls inbound and outbound network access for the task.

        :default: - The security group for the VPC is used.
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_ISecurityGroup_acf8a799]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[Tag]]:
        '''The metadata that you apply to the task to help you categorize and organize them.

        Each tag consists of a key and an optional value, both of which you define.

        :default: - No tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[Tag]], result)

    @builtins.property
    def task_count(self) -> typing.Optional[jsii.Number]:
        '''The number of tasks to create based on TaskDefinition.

        :default: 1
        '''
        result = self._values.get("task_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_e57d76df]:
        '''The subnets associated with the task.

        These subnets must all be in the same VPC.
        The task will be launched in these subnets.

        :default: - all private subnets of the VPC are selected.
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_SubnetSelection_e57d76df], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsRunTaskBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IScheduleTarget_46344d95)
class EventBridgePutEvents(
    ScheduleTargetBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.EventBridgePutEvents",
):
    '''Send an event to an AWS EventBridge by AWS EventBridge Scheduler.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_events as events
        
        
        event_bus = events.EventBus(self, "EventBus",
            event_bus_name="DomainEvents"
        )
        
        event_entry = targets.EventBridgePutEventsEntry(
            event_bus=event_bus,
            source="PetService",
            detail=ScheduleTargetInput.from_object({"Name": "Fluffy"}),
            detail_type="🐶"
        )
        
        Schedule(self, "Schedule",
            schedule=ScheduleExpression.rate(Duration.hours(1)),
            target=targets.EventBridgePutEvents(event_entry)
        )
    '''

    def __init__(
        self,
        entry: typing.Union[EventBridgePutEventsEntry, typing.Dict[builtins.str, typing.Any]],
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param entry: -
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a0df4258a838e5a88cccc129492e95670a6c48a3a143968daf3304cda11b0d6)
            check_type(argname="argument entry", value=entry, expected_type=type_hints["entry"])
        props = ScheduleTargetBaseProps(
            dead_letter_queue=dead_letter_queue,
            input=input,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
            role=role,
        )

        jsii.create(self.__class__, self, [entry, props])

    @jsii.member(jsii_name="addTargetActionToRole")
    def _add_target_action_to_role(self, role: _IRole_235f5d8e) -> None:
        '''
        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1baf9e2dc73c33da6a0e98590a98ae30c013c30b80ac84aa641d341184758895)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "addTargetActionToRole", [role]))

    @jsii.member(jsii_name="bindBaseTargetConfig")
    def _bind_base_target_config(
        self,
        _schedule: _ISchedule_4a32574d,
    ) -> _ScheduleTargetConfig_74216353:
        '''
        :param _schedule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bee2e860ddd29c71210c85b0d9356d7ffe68cb7e6730ee46e7d37cf1658eb30)
            check_type(argname="argument _schedule", value=_schedule, expected_type=type_hints["_schedule"])
        return typing.cast(_ScheduleTargetConfig_74216353, jsii.invoke(self, "bindBaseTargetConfig", [_schedule]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler_targets.FargateTaskProps",
    jsii_struct_bases=[EcsRunTaskBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "input": "input",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "role": "role",
        "task_definition": "taskDefinition",
        "capacity_provider_strategies": "capacityProviderStrategies",
        "enable_ecs_managed_tags": "enableEcsManagedTags",
        "enable_execute_command": "enableExecuteCommand",
        "group": "group",
        "propagate_tags": "propagateTags",
        "reference_id": "referenceId",
        "security_groups": "securityGroups",
        "tags": "tags",
        "task_count": "taskCount",
        "vpc_subnets": "vpcSubnets",
        "assign_public_ip": "assignPublicIp",
        "platform_version": "platformVersion",
    },
)
class FargateTaskProps(EcsRunTaskBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        task_definition: _TaskDefinition_a541a103,
        capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_CapacityProviderStrategy_8d7b6657, typing.Dict[builtins.str, typing.Any]]]] = None,
        enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
        enable_execute_command: typing.Optional[builtins.bool] = None,
        group: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.bool] = None,
        reference_id: typing.Optional[builtins.str] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_count: typing.Optional[jsii.Number] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        assign_public_ip: typing.Optional[builtins.bool] = None,
        platform_version: typing.Optional[_FargatePlatformVersion_55d8be5c] = None,
    ) -> None:
        '''Properties for scheduling an ECS Fargate Task.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        :param task_definition: The task definition to use for scheduled tasks. Note: this must be TaskDefinition, and not ITaskDefinition, as it requires properties that are not known for imported task definitions If you want to run a RunTask with an imported task definition, consider using a Universal target.
        :param capacity_provider_strategies: The capacity provider strategy to use for the task. Default: - No capacity provider strategy
        :param enable_ecs_managed_tags: Specifies whether to enable Amazon ECS managed tags for the task. Default: - false
        :param enable_execute_command: Whether to enable execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task. Default: - false
        :param group: Specifies an ECS task group for the task. Default: - No group
        :param propagate_tags: Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Default: - No tag propagation
        :param reference_id: The reference ID to use for the task. Default: - No reference ID.
        :param security_groups: The security groups associated with the task. These security groups must all be in the same VPC. Controls inbound and outbound network access for the task. Default: - The security group for the VPC is used.
        :param tags: The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Default: - No tags
        :param task_count: The number of tasks to create based on TaskDefinition. Default: 1
        :param vpc_subnets: The subnets associated with the task. These subnets must all be in the same VPC. The task will be launched in these subnets. Default: - all private subnets of the VPC are selected.
        :param assign_public_ip: Specifies whether the task's elastic network interface receives a public IP address. If true, the task will receive a public IP address and be accessible from the internet. Should only be set to true when using public subnets. Default: - true if the subnet type is PUBLIC, otherwise false
        :param platform_version: Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. Platform versions determine the underlying runtime environment for the task. Default: - LATEST

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_ecs as ecs
            
            # cluster: ecs.ICluster
            # task_definition: ecs.FargateTaskDefinition
            
            
            Schedule(self, "Schedule",
                schedule=ScheduleExpression.rate(cdk.Duration.minutes(60)),
                target=targets.EcsRunFargateTask(cluster,
                    task_definition=task_definition
                )
            )
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_e57d76df(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0044a48616a5f6b274082e4beba47a9cda8ff42476a3bbf0a62e271138d58442)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
            check_type(argname="argument capacity_provider_strategies", value=capacity_provider_strategies, expected_type=type_hints["capacity_provider_strategies"])
            check_type(argname="argument enable_ecs_managed_tags", value=enable_ecs_managed_tags, expected_type=type_hints["enable_ecs_managed_tags"])
            check_type(argname="argument enable_execute_command", value=enable_execute_command, expected_type=type_hints["enable_execute_command"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
            check_type(argname="argument reference_id", value=reference_id, expected_type=type_hints["reference_id"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument task_count", value=task_count, expected_type=type_hints["task_count"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
            check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
            check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "task_definition": task_definition,
        }
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if input is not None:
            self._values["input"] = input
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if role is not None:
            self._values["role"] = role
        if capacity_provider_strategies is not None:
            self._values["capacity_provider_strategies"] = capacity_provider_strategies
        if enable_ecs_managed_tags is not None:
            self._values["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            self._values["enable_execute_command"] = enable_execute_command
        if group is not None:
            self._values["group"] = group
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags
        if reference_id is not None:
            self._values["reference_id"] = reference_id
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if tags is not None:
            self._values["tags"] = tags
        if task_count is not None:
            self._values["task_count"] = task_count
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if assign_public_ip is not None:
            self._values["assign_public_ip"] = assign_public_ip
        if platform_version is not None:
            self._values["platform_version"] = platform_version

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def input(self) -> typing.Optional[_ScheduleTargetInput_dd30d070]:
        '''Input passed to the target.

        :default: - no input.
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[_ScheduleTargetInput_dd30d070], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Scheduler sends to a target for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the target returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf.

        If none provided templates target will automatically create an IAM role with all the minimum necessary
        permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets
        will grant minimal required permissions.

        :default: - created by target
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def task_definition(self) -> _TaskDefinition_a541a103:
        '''The task definition to use for scheduled tasks.

        Note: this must be TaskDefinition, and not ITaskDefinition,
        as it requires properties that are not known for imported task definitions
        If you want to run a RunTask with an imported task definition,
        consider using a Universal target.
        '''
        result = self._values.get("task_definition")
        assert result is not None, "Required property 'task_definition' is missing"
        return typing.cast(_TaskDefinition_a541a103, result)

    @builtins.property
    def capacity_provider_strategies(
        self,
    ) -> typing.Optional[typing.List[_CapacityProviderStrategy_8d7b6657]]:
        '''The capacity provider strategy to use for the task.

        :default: - No capacity provider strategy
        '''
        result = self._values.get("capacity_provider_strategies")
        return typing.cast(typing.Optional[typing.List[_CapacityProviderStrategy_8d7b6657]], result)

    @builtins.property
    def enable_ecs_managed_tags(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether to enable Amazon ECS managed tags for the task.

        :default: - false
        '''
        result = self._values.get("enable_ecs_managed_tags")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_execute_command(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable execute command functionality for the containers in this task.

        If true, this enables execute command functionality on all containers in the task.

        :default: - false
        '''
        result = self._values.get("enable_execute_command")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Specifies an ECS task group for the task.

        :default: - No group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def propagate_tags(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether to propagate the tags from the task definition to the task.

        If no value is specified, the tags are not propagated.

        :default: - No tag propagation
        '''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def reference_id(self) -> typing.Optional[builtins.str]:
        '''The reference ID to use for the task.

        :default: - No reference ID.
        '''
        result = self._values.get("reference_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_acf8a799]]:
        '''The security groups associated with the task.

        These security groups must all be in the same VPC.
        Controls inbound and outbound network access for the task.

        :default: - The security group for the VPC is used.
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_ISecurityGroup_acf8a799]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[Tag]]:
        '''The metadata that you apply to the task to help you categorize and organize them.

        Each tag consists of a key and an optional value, both of which you define.

        :default: - No tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[Tag]], result)

    @builtins.property
    def task_count(self) -> typing.Optional[jsii.Number]:
        '''The number of tasks to create based on TaskDefinition.

        :default: 1
        '''
        result = self._values.get("task_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_e57d76df]:
        '''The subnets associated with the task.

        These subnets must all be in the same VPC.
        The task will be launched in these subnets.

        :default: - all private subnets of the VPC are selected.
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_SubnetSelection_e57d76df], result)

    @builtins.property
    def assign_public_ip(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether the task's elastic network interface receives a public IP address.

        If true, the task will receive a public IP address and be accessible from the internet.
        Should only be set to true when using public subnets.

        :default: - true if the subnet type is PUBLIC, otherwise false
        '''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def platform_version(self) -> typing.Optional[_FargatePlatformVersion_55d8be5c]:
        '''Specifies the platform version for the task.

        Specify only the numeric portion of the platform version, such as 1.1.0.
        Platform versions determine the underlying runtime environment for the task.

        :default: - LATEST
        '''
        result = self._values.get("platform_version")
        return typing.cast(typing.Optional[_FargatePlatformVersion_55d8be5c], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FargateTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IScheduleTarget_46344d95)
class FirehosePutRecord(
    ScheduleTargetBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.FirehosePutRecord",
):
    '''Use an Amazon Data Firehose as a target for AWS EventBridge Scheduler.

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
        delivery_stream: _IDeliveryStream_8f118861,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param delivery_stream: -
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__530a834e1b0aa54fcdcc7fc227e7d1c3328b1fe4d8b7a8b2c737ee83541bde6f)
            check_type(argname="argument delivery_stream", value=delivery_stream, expected_type=type_hints["delivery_stream"])
        props = ScheduleTargetBaseProps(
            dead_letter_queue=dead_letter_queue,
            input=input,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
            role=role,
        )

        jsii.create(self.__class__, self, [delivery_stream, props])

    @jsii.member(jsii_name="addTargetActionToRole")
    def _add_target_action_to_role(self, role: _IRole_235f5d8e) -> None:
        '''
        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12ef15c1799d86a7551586a9a9e97d06dd1a9ac00d3ff8f956b86ee6936fa7ea)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "addTargetActionToRole", [role]))


@jsii.implements(_IScheduleTarget_46344d95)
class InspectorStartAssessmentRun(
    ScheduleTargetBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.InspectorStartAssessmentRun",
):
    '''Use an Amazon Inspector as a target for AWS EventBridge Scheduler.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_inspector as inspector
        
        # cfn_assessment_template: inspector.CfnAssessmentTemplate
        
        
        assessment_template = inspector.AssessmentTemplate.from_cfn_assessment_template(self, "MyAssessmentTemplate", cfn_assessment_template)
        
        Schedule(self, "Schedule",
            schedule=ScheduleExpression.rate(Duration.minutes(60)),
            target=targets.InspectorStartAssessmentRun(assessment_template)
        )
    '''

    def __init__(
        self,
        template: _IAssessmentTemplate_495c2d4e,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param template: -
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__827e380295982b1bf320134c0d482e805db91e38e0a4e6207c777b292c586409)
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
        props = ScheduleTargetBaseProps(
            dead_letter_queue=dead_letter_queue,
            input=input,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
            role=role,
        )

        jsii.create(self.__class__, self, [template, props])

    @jsii.member(jsii_name="addTargetActionToRole")
    def _add_target_action_to_role(self, role: _IRole_235f5d8e) -> None:
        '''
        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b0a5298c5996dd44a33a53ddb1de44b183dab3534ae35332944ef46add41c3c)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "addTargetActionToRole", [role]))


@jsii.implements(_IScheduleTarget_46344d95)
class KinesisStreamPutRecord(
    ScheduleTargetBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.KinesisStreamPutRecord",
):
    '''Use an Amazon Kinesis Data Streams as a target for AWS EventBridge Scheduler.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_kinesis as kinesis
        
        
        stream = kinesis.Stream(self, "MyStream")
        
        Schedule(self, "Schedule",
            schedule=ScheduleExpression.rate(Duration.minutes(60)),
            target=targets.KinesisStreamPutRecord(stream,
                partition_key="key"
            )
        )
    '''

    def __init__(
        self,
        stream: _IStream_4e2457d2,
        *,
        partition_key: builtins.str,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param stream: -
        :param partition_key: The shard to which EventBridge Scheduler sends the event. The length must be between 1 and 256.
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__844d4109ae2a35450c62ac93b6c125635f2ea9d42ffb8e4860d25d1e02b1064a)
            check_type(argname="argument stream", value=stream, expected_type=type_hints["stream"])
        props = KinesisStreamPutRecordProps(
            partition_key=partition_key,
            dead_letter_queue=dead_letter_queue,
            input=input,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
            role=role,
        )

        jsii.create(self.__class__, self, [stream, props])

    @jsii.member(jsii_name="addTargetActionToRole")
    def _add_target_action_to_role(self, role: _IRole_235f5d8e) -> None:
        '''
        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f68362f38606eda9d16e9f454710bd99b8cd843f84c5c0019bf2ea0a83d96d0)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "addTargetActionToRole", [role]))

    @jsii.member(jsii_name="bindBaseTargetConfig")
    def _bind_base_target_config(
        self,
        _schedule: _ISchedule_4a32574d,
    ) -> _ScheduleTargetConfig_74216353:
        '''
        :param _schedule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13086e22bbba8b22a5916cdb6de3619bfa3160b4ffb06dd0b18358feff854092)
            check_type(argname="argument _schedule", value=_schedule, expected_type=type_hints["_schedule"])
        return typing.cast(_ScheduleTargetConfig_74216353, jsii.invoke(self, "bindBaseTargetConfig", [_schedule]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler_targets.KinesisStreamPutRecordProps",
    jsii_struct_bases=[ScheduleTargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "input": "input",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "role": "role",
        "partition_key": "partitionKey",
    },
)
class KinesisStreamPutRecordProps(ScheduleTargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        partition_key: builtins.str,
    ) -> None:
        '''Properties for a Kinesis Data Streams Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        :param partition_key: The shard to which EventBridge Scheduler sends the event. The length must be between 1 and 256.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_kinesis as kinesis
            
            
            stream = kinesis.Stream(self, "MyStream")
            
            Schedule(self, "Schedule",
                schedule=ScheduleExpression.rate(Duration.minutes(60)),
                target=targets.KinesisStreamPutRecord(stream,
                    partition_key="key"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__567db217f348a6c029d70c629fc520a2f785e26b04a4275cad20a047e712f916)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument partition_key", value=partition_key, expected_type=type_hints["partition_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "partition_key": partition_key,
        }
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if input is not None:
            self._values["input"] = input
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def input(self) -> typing.Optional[_ScheduleTargetInput_dd30d070]:
        '''Input passed to the target.

        :default: - no input.
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[_ScheduleTargetInput_dd30d070], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Scheduler sends to a target for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the target returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf.

        If none provided templates target will automatically create an IAM role with all the minimum necessary
        permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets
        will grant minimal required permissions.

        :default: - created by target
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def partition_key(self) -> builtins.str:
        '''The shard to which EventBridge Scheduler sends the event.

        The length must be between 1 and 256.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-kinesisparameters.html
        '''
        result = self._values.get("partition_key")
        assert result is not None, "Required property 'partition_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisStreamPutRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IScheduleTarget_46344d95)
class LambdaInvoke(
    ScheduleTargetBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.LambdaInvoke",
):
    '''Use an AWS Lambda function as a target for AWS EventBridge Scheduler.

    :exampleMetadata: infused

    Example::

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
    '''

    def __init__(
        self,
        func: _IFunction_6adb0ab8,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param func: -
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dd794e954362778258936b279d00e4ee11901171e9167c30c46af0264354987)
            check_type(argname="argument func", value=func, expected_type=type_hints["func"])
        props = ScheduleTargetBaseProps(
            dead_letter_queue=dead_letter_queue,
            input=input,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
            role=role,
        )

        jsii.create(self.__class__, self, [func, props])

    @jsii.member(jsii_name="addTargetActionToRole")
    def _add_target_action_to_role(self, role: _IRole_235f5d8e) -> None:
        '''
        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26671fb6a31106b3127d1e1ee335ad2e53f34baa3f498ccf404d68a494683324)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "addTargetActionToRole", [role]))


@jsii.implements(_IScheduleTarget_46344d95)
class SageMakerStartPipelineExecution(
    ScheduleTargetBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.SageMakerStartPipelineExecution",
):
    '''Use a SageMaker pipeline as a target for AWS EventBridge Scheduler.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_sagemaker as sagemaker
        
        # pipeline: sagemaker.IPipeline
        
        
        Schedule(self, "Schedule",
            schedule=ScheduleExpression.rate(Duration.minutes(60)),
            target=targets.SageMakerStartPipelineExecution(pipeline,
                pipeline_parameter_list=[targets.SageMakerPipelineParameter(
                    name="parameter-name",
                    value="parameter-value"
                )]
            )
        )
    '''

    def __init__(
        self,
        pipeline: _IPipeline_3f0dad92,
        *,
        pipeline_parameter_list: typing.Optional[typing.Sequence[typing.Union[SageMakerPipelineParameter, typing.Dict[builtins.str, typing.Any]]]] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param pipeline: -
        :param pipeline_parameter_list: List of parameter names and values to use when executing the SageMaker Model Building Pipeline. The length must be between 0 and 200. Default: - no pipeline parameter list
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b4d5d553374833e946836908362ee222905ef0a763dcb21589a9af03c37b17b)
            check_type(argname="argument pipeline", value=pipeline, expected_type=type_hints["pipeline"])
        props = SageMakerStartPipelineExecutionProps(
            pipeline_parameter_list=pipeline_parameter_list,
            dead_letter_queue=dead_letter_queue,
            input=input,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
            role=role,
        )

        jsii.create(self.__class__, self, [pipeline, props])

    @jsii.member(jsii_name="addTargetActionToRole")
    def _add_target_action_to_role(self, role: _IRole_235f5d8e) -> None:
        '''
        :param role: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae0f7cdeb8aec78a69856eda18285d709f05365e1ff2cd96bf0165c868a6e7fb)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        return typing.cast(None, jsii.invoke(self, "addTargetActionToRole", [role]))

    @jsii.member(jsii_name="bindBaseTargetConfig")
    def _bind_base_target_config(
        self,
        schedule: _ISchedule_4a32574d,
    ) -> _ScheduleTargetConfig_74216353:
        '''
        :param schedule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d9975ba29adcd67e9e835e8a8a9b18c31ac8ad5864fa85ddfb1051ca2290643)
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
        return typing.cast(_ScheduleTargetConfig_74216353, jsii.invoke(self, "bindBaseTargetConfig", [schedule]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler_targets.SageMakerStartPipelineExecutionProps",
    jsii_struct_bases=[ScheduleTargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "input": "input",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "role": "role",
        "pipeline_parameter_list": "pipelineParameterList",
    },
)
class SageMakerStartPipelineExecutionProps(ScheduleTargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        pipeline_parameter_list: typing.Optional[typing.Sequence[typing.Union[SageMakerPipelineParameter, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for a SageMaker Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        :param pipeline_parameter_list: List of parameter names and values to use when executing the SageMaker Model Building Pipeline. The length must be between 0 and 200. Default: - no pipeline parameter list

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_sagemaker as sagemaker
            
            # pipeline: sagemaker.IPipeline
            
            
            Schedule(self, "Schedule",
                schedule=ScheduleExpression.rate(Duration.minutes(60)),
                target=targets.SageMakerStartPipelineExecution(pipeline,
                    pipeline_parameter_list=[targets.SageMakerPipelineParameter(
                        name="parameter-name",
                        value="parameter-value"
                    )]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e472e64e333014fc5530dd24fc7c0935430768f0699ea44f2dfd3d955bf20bc2)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument pipeline_parameter_list", value=pipeline_parameter_list, expected_type=type_hints["pipeline_parameter_list"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if input is not None:
            self._values["input"] = input
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if role is not None:
            self._values["role"] = role
        if pipeline_parameter_list is not None:
            self._values["pipeline_parameter_list"] = pipeline_parameter_list

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def input(self) -> typing.Optional[_ScheduleTargetInput_dd30d070]:
        '''Input passed to the target.

        :default: - no input.
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[_ScheduleTargetInput_dd30d070], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Scheduler sends to a target for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the target returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf.

        If none provided templates target will automatically create an IAM role with all the minimum necessary
        permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets
        will grant minimal required permissions.

        :default: - created by target
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def pipeline_parameter_list(
        self,
    ) -> typing.Optional[typing.List[SageMakerPipelineParameter]]:
        '''List of parameter names and values to use when executing the SageMaker Model Building Pipeline.

        The length must be between 0 and 200.

        :default: - no pipeline parameter list

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-scheduler-schedule-sagemakerpipelineparameters.html#cfn-scheduler-schedule-sagemakerpipelineparameters-pipelineparameterlist
        '''
        result = self._values.get("pipeline_parameter_list")
        return typing.cast(typing.Optional[typing.List[SageMakerPipelineParameter]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SageMakerStartPipelineExecutionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_scheduler_targets.Ec2TaskProps",
    jsii_struct_bases=[EcsRunTaskBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "input": "input",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "role": "role",
        "task_definition": "taskDefinition",
        "capacity_provider_strategies": "capacityProviderStrategies",
        "enable_ecs_managed_tags": "enableEcsManagedTags",
        "enable_execute_command": "enableExecuteCommand",
        "group": "group",
        "propagate_tags": "propagateTags",
        "reference_id": "referenceId",
        "security_groups": "securityGroups",
        "tags": "tags",
        "task_count": "taskCount",
        "vpc_subnets": "vpcSubnets",
        "placement_constraints": "placementConstraints",
        "placement_strategies": "placementStrategies",
    },
)
class Ec2TaskProps(EcsRunTaskBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        task_definition: _TaskDefinition_a541a103,
        capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_CapacityProviderStrategy_8d7b6657, typing.Dict[builtins.str, typing.Any]]]] = None,
        enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
        enable_execute_command: typing.Optional[builtins.bool] = None,
        group: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.bool] = None,
        reference_id: typing.Optional[builtins.str] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_count: typing.Optional[jsii.Number] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        placement_constraints: typing.Optional[typing.Sequence[_PlacementConstraint_11d82a52]] = None,
        placement_strategies: typing.Optional[typing.Sequence[_PlacementStrategy_2bb6c232]] = None,
    ) -> None:
        '''Properties for scheduling an ECS Task on EC2.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        :param task_definition: The task definition to use for scheduled tasks. Note: this must be TaskDefinition, and not ITaskDefinition, as it requires properties that are not known for imported task definitions If you want to run a RunTask with an imported task definition, consider using a Universal target.
        :param capacity_provider_strategies: The capacity provider strategy to use for the task. Default: - No capacity provider strategy
        :param enable_ecs_managed_tags: Specifies whether to enable Amazon ECS managed tags for the task. Default: - false
        :param enable_execute_command: Whether to enable execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task. Default: - false
        :param group: Specifies an ECS task group for the task. Default: - No group
        :param propagate_tags: Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Default: - No tag propagation
        :param reference_id: The reference ID to use for the task. Default: - No reference ID.
        :param security_groups: The security groups associated with the task. These security groups must all be in the same VPC. Controls inbound and outbound network access for the task. Default: - The security group for the VPC is used.
        :param tags: The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Default: - No tags
        :param task_count: The number of tasks to create based on TaskDefinition. Default: 1
        :param vpc_subnets: The subnets associated with the task. These subnets must all be in the same VPC. The task will be launched in these subnets. Default: - all private subnets of the VPC are selected.
        :param placement_constraints: The rules that must be met in order to place a task on a container instance. Default: - No placement constraints.
        :param placement_strategies: The algorithm for selecting container instances for task placement. Default: - No placement strategies.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_ecs as ecs
            
            # cluster: ecs.ICluster
            # task_definition: ecs.Ec2TaskDefinition
            
            
            Schedule(self, "Schedule",
                schedule=ScheduleExpression.rate(cdk.Duration.minutes(60)),
                target=targets.EcsRunEc2Task(cluster,
                    task_definition=task_definition
                )
            )
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _SubnetSelection_e57d76df(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1411b21d63f24c8e116e80d07b271db391e0744a2d90d4aa94f5d32c29e37c72)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
            check_type(argname="argument capacity_provider_strategies", value=capacity_provider_strategies, expected_type=type_hints["capacity_provider_strategies"])
            check_type(argname="argument enable_ecs_managed_tags", value=enable_ecs_managed_tags, expected_type=type_hints["enable_ecs_managed_tags"])
            check_type(argname="argument enable_execute_command", value=enable_execute_command, expected_type=type_hints["enable_execute_command"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument propagate_tags", value=propagate_tags, expected_type=type_hints["propagate_tags"])
            check_type(argname="argument reference_id", value=reference_id, expected_type=type_hints["reference_id"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument task_count", value=task_count, expected_type=type_hints["task_count"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
            check_type(argname="argument placement_constraints", value=placement_constraints, expected_type=type_hints["placement_constraints"])
            check_type(argname="argument placement_strategies", value=placement_strategies, expected_type=type_hints["placement_strategies"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "task_definition": task_definition,
        }
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if input is not None:
            self._values["input"] = input
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if role is not None:
            self._values["role"] = role
        if capacity_provider_strategies is not None:
            self._values["capacity_provider_strategies"] = capacity_provider_strategies
        if enable_ecs_managed_tags is not None:
            self._values["enable_ecs_managed_tags"] = enable_ecs_managed_tags
        if enable_execute_command is not None:
            self._values["enable_execute_command"] = enable_execute_command
        if group is not None:
            self._values["group"] = group
        if propagate_tags is not None:
            self._values["propagate_tags"] = propagate_tags
        if reference_id is not None:
            self._values["reference_id"] = reference_id
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if tags is not None:
            self._values["tags"] = tags
        if task_count is not None:
            self._values["task_count"] = task_count
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if placement_constraints is not None:
            self._values["placement_constraints"] = placement_constraints
        if placement_strategies is not None:
            self._values["placement_strategies"] = placement_strategies

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[_IQueue_7ed6f679]:
        '''The SQS queue to be used as deadLetterQueue.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[_IQueue_7ed6f679], result)

    @builtins.property
    def input(self) -> typing.Optional[_ScheduleTargetInput_dd30d070]:
        '''Input passed to the target.

        :default: - no input.
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[_ScheduleTargetInput_dd30d070], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum age of a request that Scheduler sends to a target for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the target returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf.

        If none provided templates target will automatically create an IAM role with all the minimum necessary
        permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets
        will grant minimal required permissions.

        :default: - created by target
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def task_definition(self) -> _TaskDefinition_a541a103:
        '''The task definition to use for scheduled tasks.

        Note: this must be TaskDefinition, and not ITaskDefinition,
        as it requires properties that are not known for imported task definitions
        If you want to run a RunTask with an imported task definition,
        consider using a Universal target.
        '''
        result = self._values.get("task_definition")
        assert result is not None, "Required property 'task_definition' is missing"
        return typing.cast(_TaskDefinition_a541a103, result)

    @builtins.property
    def capacity_provider_strategies(
        self,
    ) -> typing.Optional[typing.List[_CapacityProviderStrategy_8d7b6657]]:
        '''The capacity provider strategy to use for the task.

        :default: - No capacity provider strategy
        '''
        result = self._values.get("capacity_provider_strategies")
        return typing.cast(typing.Optional[typing.List[_CapacityProviderStrategy_8d7b6657]], result)

    @builtins.property
    def enable_ecs_managed_tags(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether to enable Amazon ECS managed tags for the task.

        :default: - false
        '''
        result = self._values.get("enable_ecs_managed_tags")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_execute_command(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable execute command functionality for the containers in this task.

        If true, this enables execute command functionality on all containers in the task.

        :default: - false
        '''
        result = self._values.get("enable_execute_command")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Specifies an ECS task group for the task.

        :default: - No group
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def propagate_tags(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether to propagate the tags from the task definition to the task.

        If no value is specified, the tags are not propagated.

        :default: - No tag propagation
        '''
        result = self._values.get("propagate_tags")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def reference_id(self) -> typing.Optional[builtins.str]:
        '''The reference ID to use for the task.

        :default: - No reference ID.
        '''
        result = self._values.get("reference_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[_ISecurityGroup_acf8a799]]:
        '''The security groups associated with the task.

        These security groups must all be in the same VPC.
        Controls inbound and outbound network access for the task.

        :default: - The security group for the VPC is used.
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_ISecurityGroup_acf8a799]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[Tag]]:
        '''The metadata that you apply to the task to help you categorize and organize them.

        Each tag consists of a key and an optional value, both of which you define.

        :default: - No tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[Tag]], result)

    @builtins.property
    def task_count(self) -> typing.Optional[jsii.Number]:
        '''The number of tasks to create based on TaskDefinition.

        :default: 1
        '''
        result = self._values.get("task_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_SubnetSelection_e57d76df]:
        '''The subnets associated with the task.

        These subnets must all be in the same VPC.
        The task will be launched in these subnets.

        :default: - all private subnets of the VPC are selected.
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_SubnetSelection_e57d76df], result)

    @builtins.property
    def placement_constraints(
        self,
    ) -> typing.Optional[typing.List[_PlacementConstraint_11d82a52]]:
        '''The rules that must be met in order to place a task on a container instance.

        :default: - No placement constraints.
        '''
        result = self._values.get("placement_constraints")
        return typing.cast(typing.Optional[typing.List[_PlacementConstraint_11d82a52]], result)

    @builtins.property
    def placement_strategies(
        self,
    ) -> typing.Optional[typing.List[_PlacementStrategy_2bb6c232]]:
        '''The algorithm for selecting container instances for task placement.

        :default: - No placement strategies.
        '''
        result = self._values.get("placement_strategies")
        return typing.cast(typing.Optional[typing.List[_PlacementStrategy_2bb6c232]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2TaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EcsRunEc2Task(
    EcsRunTask,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.EcsRunEc2Task",
):
    '''Schedule an ECS Task on EC2 using AWS EventBridge Scheduler.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_ecs as ecs
        
        # cluster: ecs.ICluster
        # task_definition: ecs.Ec2TaskDefinition
        
        
        Schedule(self, "Schedule",
            schedule=ScheduleExpression.rate(cdk.Duration.minutes(60)),
            target=targets.EcsRunEc2Task(cluster,
                task_definition=task_definition
            )
        )
    '''

    def __init__(
        self,
        cluster: _ICluster_16cddd09,
        *,
        placement_constraints: typing.Optional[typing.Sequence[_PlacementConstraint_11d82a52]] = None,
        placement_strategies: typing.Optional[typing.Sequence[_PlacementStrategy_2bb6c232]] = None,
        task_definition: _TaskDefinition_a541a103,
        capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_CapacityProviderStrategy_8d7b6657, typing.Dict[builtins.str, typing.Any]]]] = None,
        enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
        enable_execute_command: typing.Optional[builtins.bool] = None,
        group: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.bool] = None,
        reference_id: typing.Optional[builtins.str] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_count: typing.Optional[jsii.Number] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param cluster: -
        :param placement_constraints: The rules that must be met in order to place a task on a container instance. Default: - No placement constraints.
        :param placement_strategies: The algorithm for selecting container instances for task placement. Default: - No placement strategies.
        :param task_definition: The task definition to use for scheduled tasks. Note: this must be TaskDefinition, and not ITaskDefinition, as it requires properties that are not known for imported task definitions If you want to run a RunTask with an imported task definition, consider using a Universal target.
        :param capacity_provider_strategies: The capacity provider strategy to use for the task. Default: - No capacity provider strategy
        :param enable_ecs_managed_tags: Specifies whether to enable Amazon ECS managed tags for the task. Default: - false
        :param enable_execute_command: Whether to enable execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task. Default: - false
        :param group: Specifies an ECS task group for the task. Default: - No group
        :param propagate_tags: Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Default: - No tag propagation
        :param reference_id: The reference ID to use for the task. Default: - No reference ID.
        :param security_groups: The security groups associated with the task. These security groups must all be in the same VPC. Controls inbound and outbound network access for the task. Default: - The security group for the VPC is used.
        :param tags: The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Default: - No tags
        :param task_count: The number of tasks to create based on TaskDefinition. Default: 1
        :param vpc_subnets: The subnets associated with the task. These subnets must all be in the same VPC. The task will be launched in these subnets. Default: - all private subnets of the VPC are selected.
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__746d976dc3c24e8de8cadcf42b961c78853df37a7880455598cfcde142867902)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
        props = Ec2TaskProps(
            placement_constraints=placement_constraints,
            placement_strategies=placement_strategies,
            task_definition=task_definition,
            capacity_provider_strategies=capacity_provider_strategies,
            enable_ecs_managed_tags=enable_ecs_managed_tags,
            enable_execute_command=enable_execute_command,
            group=group,
            propagate_tags=propagate_tags,
            reference_id=reference_id,
            security_groups=security_groups,
            tags=tags,
            task_count=task_count,
            vpc_subnets=vpc_subnets,
            dead_letter_queue=dead_letter_queue,
            input=input,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
            role=role,
        )

        jsii.create(self.__class__, self, [cluster, props])

    @jsii.member(jsii_name="bindBaseTargetConfig")
    def _bind_base_target_config(
        self,
        _schedule: _ISchedule_4a32574d,
    ) -> _ScheduleTargetConfig_74216353:
        '''
        :param _schedule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c048ed62488b8de83127af7a33e8932cd4af11ae2b50e4c9515301957758a6c7)
            check_type(argname="argument _schedule", value=_schedule, expected_type=type_hints["_schedule"])
        return typing.cast(_ScheduleTargetConfig_74216353, jsii.invoke(self, "bindBaseTargetConfig", [_schedule]))


class EcsRunFargateTask(
    EcsRunTask,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_scheduler_targets.EcsRunFargateTask",
):
    '''Schedule an ECS Task on Fargate using AWS EventBridge Scheduler.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_ecs as ecs
        
        # cluster: ecs.ICluster
        # task_definition: ecs.FargateTaskDefinition
        
        
        Schedule(self, "Schedule",
            schedule=ScheduleExpression.rate(cdk.Duration.minutes(60)),
            target=targets.EcsRunFargateTask(cluster,
                task_definition=task_definition
            )
        )
    '''

    def __init__(
        self,
        cluster: _ICluster_16cddd09,
        *,
        assign_public_ip: typing.Optional[builtins.bool] = None,
        platform_version: typing.Optional[_FargatePlatformVersion_55d8be5c] = None,
        task_definition: _TaskDefinition_a541a103,
        capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_CapacityProviderStrategy_8d7b6657, typing.Dict[builtins.str, typing.Any]]]] = None,
        enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
        enable_execute_command: typing.Optional[builtins.bool] = None,
        group: typing.Optional[builtins.str] = None,
        propagate_tags: typing.Optional[builtins.bool] = None,
        reference_id: typing.Optional[builtins.str] = None,
        security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_count: typing.Optional[jsii.Number] = None,
        vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
        dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
        input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
        max_event_age: typing.Optional[_Duration_4839e8c3] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param cluster: -
        :param assign_public_ip: Specifies whether the task's elastic network interface receives a public IP address. If true, the task will receive a public IP address and be accessible from the internet. Should only be set to true when using public subnets. Default: - true if the subnet type is PUBLIC, otherwise false
        :param platform_version: Specifies the platform version for the task. Specify only the numeric portion of the platform version, such as 1.1.0. Platform versions determine the underlying runtime environment for the task. Default: - LATEST
        :param task_definition: The task definition to use for scheduled tasks. Note: this must be TaskDefinition, and not ITaskDefinition, as it requires properties that are not known for imported task definitions If you want to run a RunTask with an imported task definition, consider using a Universal target.
        :param capacity_provider_strategies: The capacity provider strategy to use for the task. Default: - No capacity provider strategy
        :param enable_ecs_managed_tags: Specifies whether to enable Amazon ECS managed tags for the task. Default: - false
        :param enable_execute_command: Whether to enable execute command functionality for the containers in this task. If true, this enables execute command functionality on all containers in the task. Default: - false
        :param group: Specifies an ECS task group for the task. Default: - No group
        :param propagate_tags: Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags are not propagated. Default: - No tag propagation
        :param reference_id: The reference ID to use for the task. Default: - No reference ID.
        :param security_groups: The security groups associated with the task. These security groups must all be in the same VPC. Controls inbound and outbound network access for the task. Default: - The security group for the VPC is used.
        :param tags: The metadata that you apply to the task to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Default: - No tags
        :param task_count: The number of tasks to create based on TaskDefinition. Default: 1
        :param vpc_subnets: The subnets associated with the task. These subnets must all be in the same VPC. The task will be launched in these subnets. Default: - all private subnets of the VPC are selected.
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param input: Input passed to the target. Default: - no input.
        :param max_event_age: The maximum age of a request that Scheduler sends to a target for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the target returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param role: An execution role is an IAM role that EventBridge Scheduler assumes in order to interact with other AWS services on your behalf. If none provided templates target will automatically create an IAM role with all the minimum necessary permissions to interact with the templated target. If you wish you may specify your own IAM role, then the templated targets will grant minimal required permissions. Default: - created by target
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78c355ce63d9e4845ecd3f3fb90d1a3fe8ebc7a6e515996d93a54cbf09be582d)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
        props = FargateTaskProps(
            assign_public_ip=assign_public_ip,
            platform_version=platform_version,
            task_definition=task_definition,
            capacity_provider_strategies=capacity_provider_strategies,
            enable_ecs_managed_tags=enable_ecs_managed_tags,
            enable_execute_command=enable_execute_command,
            group=group,
            propagate_tags=propagate_tags,
            reference_id=reference_id,
            security_groups=security_groups,
            tags=tags,
            task_count=task_count,
            vpc_subnets=vpc_subnets,
            dead_letter_queue=dead_letter_queue,
            input=input,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
            role=role,
        )

        jsii.create(self.__class__, self, [cluster, props])

    @jsii.member(jsii_name="bindBaseTargetConfig")
    def _bind_base_target_config(
        self,
        _schedule: _ISchedule_4a32574d,
    ) -> _ScheduleTargetConfig_74216353:
        '''
        :param _schedule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__922a85e32cff3eab12f4b0f6b998b5d7e2370b966dbee4458874c3806ebde41e)
            check_type(argname="argument _schedule", value=_schedule, expected_type=type_hints["_schedule"])
        return typing.cast(_ScheduleTargetConfig_74216353, jsii.invoke(self, "bindBaseTargetConfig", [_schedule]))


__all__ = [
    "CodeBuildStartBuild",
    "CodePipelineStartPipelineExecution",
    "Ec2TaskProps",
    "EcsRunEc2Task",
    "EcsRunFargateTask",
    "EcsRunTask",
    "EcsRunTaskBaseProps",
    "EventBridgePutEvents",
    "EventBridgePutEventsEntry",
    "FargateTaskProps",
    "FirehosePutRecord",
    "InspectorStartAssessmentRun",
    "KinesisStreamPutRecord",
    "KinesisStreamPutRecordProps",
    "LambdaInvoke",
    "SageMakerPipelineParameter",
    "SageMakerStartPipelineExecution",
    "SageMakerStartPipelineExecutionProps",
    "ScheduleTargetBase",
    "ScheduleTargetBaseProps",
    "SnsPublish",
    "SqsSendMessage",
    "SqsSendMessageProps",
    "StepFunctionsStartExecution",
    "Tag",
    "Universal",
    "UniversalTargetProps",
]

publication.publish()

def _typecheckingstub__c20ea1ffb2760df785aee8014a687654066d35e08ebf631810b29af40f20952b(
    *,
    detail: _ScheduleTargetInput_dd30d070,
    detail_type: builtins.str,
    event_bus: _IEventBus_88d13111,
    source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9b88d9119f8045f4c3b695d8ed58b7f5b8833e798cbc2660e4c8ba59fc95cb1(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d830072c02aa1c93302e9c28e7f88fb42c5a6a2a9deec3c567a7179aebb7d89(
    base_props: typing.Union[ScheduleTargetBaseProps, typing.Dict[builtins.str, typing.Any]],
    target_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01737bee0bf8db4b920430443ea84a27c1c2f6246bd71927150a4fb28accc32d(
    schedule: _ISchedule_4a32574d,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd8a5015bbf00d1130163ba73634014dc8420ec6c2484ca7ca7e2d9776b12c60(
    _schedule: _ISchedule_4a32574d,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13ff83395a9b3dcc596bc1aa8b656c8638facf50a6854e6d21772607443b3efc(
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29dad4add4695787b706ed4741ddf63b9b8130a1bdf3339dff7939d0917e60de(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__961b73901f7c52b4629b4552b6be3585368cfc6c4de258420a2e2c4c9108b398(
    topic: _ITopic_9eca4852,
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6302629a59c54cd7dafc566171c4a283657f72f44a44767384888df0e6012021(
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a86c2fb46323ac8851887e951da0704b179c89e96fbc73b43048720c09f816d0(
    queue: _IQueue_7ed6f679,
    *,
    message_group_id: typing.Optional[builtins.str] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eef58dbd8df5d2551bec19ddf4779f0177025eb93b55e41899b7c2ad6298258b(
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc4c92c6b396957e8236f2f491374f5459edff0144a288b6c967faa0660c413d(
    _schedule: _ISchedule_4a32574d,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9b071d098054dd80fee122aca519dd583724dcca2e31d39c850498cbc64a259(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    message_group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6f72a14975c4b50622c65c3545124a5a40541c99ee789b2764dd89dbe6db65e(
    state_machine: _IStateMachine_73e8d2b0,
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdb74e28e429f1b8574596c9b7d69dbbe6d4a87709fe0afeee3a982c558eefa6(
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d7e0165c9edbeca9c1f67729ca5e04e783483e5161d761577189cfb4595daf8(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__198e835ff77413b2cbd7a9aad16223af355077748c1e61e3dc51f2c3390c66ca(
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aebf9e651de63ef570a11970d3762c22b62acdcb5386c5ba69076181e926f71(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    action: builtins.str,
    service: builtins.str,
    policy_statements: typing.Optional[typing.Sequence[_PolicyStatement_0fe33853]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eacc4f0e06890a24c88fe0c8814a8e396c6c6442e38857fee0168c08fca876ea(
    project: _IProject_aafae30a,
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7638691fb0294fb00596be4967a0508a1091ee4b552678b943b548af397963ba(
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f972d090ad80411fc0dff42233ee8b4ff2a48be68b7d646d1c7606a3cfb7fe56(
    pipeline: _IPipeline_0931f838,
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31c5911116f5629c2adf9d1968007740095affaa6dad806ac8e1672101368386(
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ddc91e6308e91fc95fa167254f8538961d19df122eeefb13d6881448afdc147(
    cluster: _ICluster_16cddd09,
    *,
    task_definition: _TaskDefinition_a541a103,
    capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_CapacityProviderStrategy_8d7b6657, typing.Dict[builtins.str, typing.Any]]]] = None,
    enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
    enable_execute_command: typing.Optional[builtins.bool] = None,
    group: typing.Optional[builtins.str] = None,
    propagate_tags: typing.Optional[builtins.bool] = None,
    reference_id: typing.Optional[builtins.str] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_count: typing.Optional[jsii.Number] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79f6648875df7112d642839162e2032e0cc5691244ea631e24984dc06b70af68(
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__658a297adc726b826b6ad0f740dd1153f7cd0ec47ab734b7e0c3748d30bd5285(
    _schedule: _ISchedule_4a32574d,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c784746a1d7efa2d6a0675e480c2ab5615af6620ac4fc75d4bc282aeb3ca6632(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    task_definition: _TaskDefinition_a541a103,
    capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_CapacityProviderStrategy_8d7b6657, typing.Dict[builtins.str, typing.Any]]]] = None,
    enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
    enable_execute_command: typing.Optional[builtins.bool] = None,
    group: typing.Optional[builtins.str] = None,
    propagate_tags: typing.Optional[builtins.bool] = None,
    reference_id: typing.Optional[builtins.str] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_count: typing.Optional[jsii.Number] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a0df4258a838e5a88cccc129492e95670a6c48a3a143968daf3304cda11b0d6(
    entry: typing.Union[EventBridgePutEventsEntry, typing.Dict[builtins.str, typing.Any]],
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1baf9e2dc73c33da6a0e98590a98ae30c013c30b80ac84aa641d341184758895(
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bee2e860ddd29c71210c85b0d9356d7ffe68cb7e6730ee46e7d37cf1658eb30(
    _schedule: _ISchedule_4a32574d,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0044a48616a5f6b274082e4beba47a9cda8ff42476a3bbf0a62e271138d58442(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    task_definition: _TaskDefinition_a541a103,
    capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_CapacityProviderStrategy_8d7b6657, typing.Dict[builtins.str, typing.Any]]]] = None,
    enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
    enable_execute_command: typing.Optional[builtins.bool] = None,
    group: typing.Optional[builtins.str] = None,
    propagate_tags: typing.Optional[builtins.bool] = None,
    reference_id: typing.Optional[builtins.str] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_count: typing.Optional[jsii.Number] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    assign_public_ip: typing.Optional[builtins.bool] = None,
    platform_version: typing.Optional[_FargatePlatformVersion_55d8be5c] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__530a834e1b0aa54fcdcc7fc227e7d1c3328b1fe4d8b7a8b2c737ee83541bde6f(
    delivery_stream: _IDeliveryStream_8f118861,
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12ef15c1799d86a7551586a9a9e97d06dd1a9ac00d3ff8f956b86ee6936fa7ea(
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__827e380295982b1bf320134c0d482e805db91e38e0a4e6207c777b292c586409(
    template: _IAssessmentTemplate_495c2d4e,
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b0a5298c5996dd44a33a53ddb1de44b183dab3534ae35332944ef46add41c3c(
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__844d4109ae2a35450c62ac93b6c125635f2ea9d42ffb8e4860d25d1e02b1064a(
    stream: _IStream_4e2457d2,
    *,
    partition_key: builtins.str,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f68362f38606eda9d16e9f454710bd99b8cd843f84c5c0019bf2ea0a83d96d0(
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13086e22bbba8b22a5916cdb6de3619bfa3160b4ffb06dd0b18358feff854092(
    _schedule: _ISchedule_4a32574d,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__567db217f348a6c029d70c629fc520a2f785e26b04a4275cad20a047e712f916(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    partition_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dd794e954362778258936b279d00e4ee11901171e9167c30c46af0264354987(
    func: _IFunction_6adb0ab8,
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26671fb6a31106b3127d1e1ee335ad2e53f34baa3f498ccf404d68a494683324(
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b4d5d553374833e946836908362ee222905ef0a763dcb21589a9af03c37b17b(
    pipeline: _IPipeline_3f0dad92,
    *,
    pipeline_parameter_list: typing.Optional[typing.Sequence[typing.Union[SageMakerPipelineParameter, typing.Dict[builtins.str, typing.Any]]]] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae0f7cdeb8aec78a69856eda18285d709f05365e1ff2cd96bf0165c868a6e7fb(
    role: _IRole_235f5d8e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d9975ba29adcd67e9e835e8a8a9b18c31ac8ad5864fa85ddfb1051ca2290643(
    schedule: _ISchedule_4a32574d,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e472e64e333014fc5530dd24fc7c0935430768f0699ea44f2dfd3d955bf20bc2(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    pipeline_parameter_list: typing.Optional[typing.Sequence[typing.Union[SageMakerPipelineParameter, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1411b21d63f24c8e116e80d07b271db391e0744a2d90d4aa94f5d32c29e37c72(
    *,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    task_definition: _TaskDefinition_a541a103,
    capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_CapacityProviderStrategy_8d7b6657, typing.Dict[builtins.str, typing.Any]]]] = None,
    enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
    enable_execute_command: typing.Optional[builtins.bool] = None,
    group: typing.Optional[builtins.str] = None,
    propagate_tags: typing.Optional[builtins.bool] = None,
    reference_id: typing.Optional[builtins.str] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_count: typing.Optional[jsii.Number] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    placement_constraints: typing.Optional[typing.Sequence[_PlacementConstraint_11d82a52]] = None,
    placement_strategies: typing.Optional[typing.Sequence[_PlacementStrategy_2bb6c232]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__746d976dc3c24e8de8cadcf42b961c78853df37a7880455598cfcde142867902(
    cluster: _ICluster_16cddd09,
    *,
    placement_constraints: typing.Optional[typing.Sequence[_PlacementConstraint_11d82a52]] = None,
    placement_strategies: typing.Optional[typing.Sequence[_PlacementStrategy_2bb6c232]] = None,
    task_definition: _TaskDefinition_a541a103,
    capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_CapacityProviderStrategy_8d7b6657, typing.Dict[builtins.str, typing.Any]]]] = None,
    enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
    enable_execute_command: typing.Optional[builtins.bool] = None,
    group: typing.Optional[builtins.str] = None,
    propagate_tags: typing.Optional[builtins.bool] = None,
    reference_id: typing.Optional[builtins.str] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_count: typing.Optional[jsii.Number] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c048ed62488b8de83127af7a33e8932cd4af11ae2b50e4c9515301957758a6c7(
    _schedule: _ISchedule_4a32574d,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78c355ce63d9e4845ecd3f3fb90d1a3fe8ebc7a6e515996d93a54cbf09be582d(
    cluster: _ICluster_16cddd09,
    *,
    assign_public_ip: typing.Optional[builtins.bool] = None,
    platform_version: typing.Optional[_FargatePlatformVersion_55d8be5c] = None,
    task_definition: _TaskDefinition_a541a103,
    capacity_provider_strategies: typing.Optional[typing.Sequence[typing.Union[_CapacityProviderStrategy_8d7b6657, typing.Dict[builtins.str, typing.Any]]]] = None,
    enable_ecs_managed_tags: typing.Optional[builtins.bool] = None,
    enable_execute_command: typing.Optional[builtins.bool] = None,
    group: typing.Optional[builtins.str] = None,
    propagate_tags: typing.Optional[builtins.bool] = None,
    reference_id: typing.Optional[builtins.str] = None,
    security_groups: typing.Optional[typing.Sequence[_ISecurityGroup_acf8a799]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[Tag, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_count: typing.Optional[jsii.Number] = None,
    vpc_subnets: typing.Optional[typing.Union[_SubnetSelection_e57d76df, typing.Dict[builtins.str, typing.Any]]] = None,
    dead_letter_queue: typing.Optional[_IQueue_7ed6f679] = None,
    input: typing.Optional[_ScheduleTargetInput_dd30d070] = None,
    max_event_age: typing.Optional[_Duration_4839e8c3] = None,
    retry_attempts: typing.Optional[jsii.Number] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__922a85e32cff3eab12f4b0f6b998b5d7e2370b966dbee4458874c3806ebde41e(
    _schedule: _ISchedule_4a32574d,
) -> None:
    """Type checking stubs"""
    pass
