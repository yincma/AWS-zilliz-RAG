r'''
# AWS::Notifications Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_notifications as notifications
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Notifications construct libraries](https://constructs.dev/search?q=notifications)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Notifications resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Notifications.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Notifications](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Notifications.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnChannelAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_notifications.CfnChannelAssociation",
):
    '''The ``AWS::Notifications::ChannelAssociation`` resource associates a ``Channel`` with a ``NotificationConfiguration`` for AWS User Notifications .

    For more information about AWS User Notifications , see the `AWS User Notifications User Guide <https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-channelassociation.html
    :cloudformationResource: AWS::Notifications::ChannelAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_notifications as notifications
        
        cfn_channel_association = notifications.CfnChannelAssociation(self, "MyCfnChannelAssociation",
            arn="arn",
            notification_configuration_arn="notificationConfigurationArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        arn: builtins.str,
        notification_configuration_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param arn: The Amazon Resource Name (ARN) of the ``Channel`` .
        :param notification_configuration_arn: The ARN of the ``NotificationConfiguration`` associated with the ``Channel`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96bfb9a9cbe4c6b38cb964bde4e63ccdb746cc48ac8dd61661a318886da6ba7f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnChannelAssociationProps(
            arn=arn, notification_configuration_arn=notification_configuration_arn
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0ffcf7c83a3beb5a9feedb6bf40d486b1aa9bad41565ae2a782129cc7450e94)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad26b3aa74c912ac52ae9f4bfb186ae1996d8ffa2fff5b28d9a9dcb2f5ceffbf)
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
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the ``Channel`` .'''
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02aa05d5cab2ed92674dea9fe8bfd20781091f494e9c3e3da3e1cedb24710ade)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="notificationConfigurationArn")
    def notification_configuration_arn(self) -> builtins.str:
        '''The ARN of the ``NotificationConfiguration`` associated with the ``Channel`` .'''
        return typing.cast(builtins.str, jsii.get(self, "notificationConfigurationArn"))

    @notification_configuration_arn.setter
    def notification_configuration_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b2d69598efa0d97ebfbcf163b7e00dfefacab9bb759efc23a009243fcbc29fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationConfigurationArn", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_notifications.CfnChannelAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "notification_configuration_arn": "notificationConfigurationArn",
    },
)
class CfnChannelAssociationProps:
    def __init__(
        self,
        *,
        arn: builtins.str,
        notification_configuration_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnChannelAssociation``.

        :param arn: The Amazon Resource Name (ARN) of the ``Channel`` .
        :param notification_configuration_arn: The ARN of the ``NotificationConfiguration`` associated with the ``Channel`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-channelassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_notifications as notifications
            
            cfn_channel_association_props = notifications.CfnChannelAssociationProps(
                arn="arn",
                notification_configuration_arn="notificationConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3df32ecb43a8f1e94c1f975e24a79631c45fd6739c1d7bea0e44c5c169b5137c)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument notification_configuration_arn", value=notification_configuration_arn, expected_type=type_hints["notification_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "arn": arn,
            "notification_configuration_arn": notification_configuration_arn,
        }

    @builtins.property
    def arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the ``Channel`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-channelassociation.html#cfn-notifications-channelassociation-arn
        '''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notification_configuration_arn(self) -> builtins.str:
        '''The ARN of the ``NotificationConfiguration`` associated with the ``Channel`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-channelassociation.html#cfn-notifications-channelassociation-notificationconfigurationarn
        '''
        result = self._values.get("notification_configuration_arn")
        assert result is not None, "Required property 'notification_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEventRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_notifications.CfnEventRule",
):
    '''Creates an ```EventRule`` <https://docs.aws.amazon.com/notifications/latest/userguide/glossary.html>`_ that is associated with a specified ``NotificationConfiguration`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-eventrule.html
    :cloudformationResource: AWS::Notifications::EventRule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_notifications as notifications
        
        cfn_event_rule = notifications.CfnEventRule(self, "MyCfnEventRule",
            event_type="eventType",
            notification_configuration_arn="notificationConfigurationArn",
            regions=["regions"],
            source="source",
        
            # the properties below are optional
            event_pattern="eventPattern"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        event_type: builtins.str,
        notification_configuration_arn: builtins.str,
        regions: typing.Sequence[builtins.str],
        source: builtins.str,
        event_pattern: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param event_type: The event type this rule should match with the EventBridge events. It must match with atleast one of the valid EventBridge event types. For example, Amazon EC2 Instance State change Notification and Amazon CloudWatch State Change. For more information, see `Event delivery from AWS services <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level>`_ in the *Amazon EventBridge User Guide* .
        :param notification_configuration_arn: The ARN for the ``NotificationConfiguration`` associated with this ``EventRule`` .
        :param regions: A list of AWS Regions that send events to this ``EventRule`` .
        :param source: The event source this rule should match with the EventBridge event sources. It must match with atleast one of the valid EventBridge event sources. Only AWS service sourced events are supported. For example, ``aws.ec2`` and ``aws.cloudwatch`` . For more information, see `Event delivery from AWS services <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level>`_ in the *Amazon EventBridge User Guide* .
        :param event_pattern: An additional event pattern used to further filter the events this ``EventRule`` receives. For more information, see `Amazon EventBridge event patterns <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html>`_ in the *Amazon EventBridge User Guide.*
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec202e2ad7890be955535389c490f73db69e1ae4c0e2b9af79f33a0bb4e4dd47)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventRuleProps(
            event_type=event_type,
            notification_configuration_arn=notification_configuration_arn,
            regions=regions,
            source=source,
            event_pattern=event_pattern,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c5fa74e0d9c81586c85ebd06110e66abfa6f3eca8a5c7b89fcce4d070b434dd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed227bd8ca507740b963532ef2c249c436e3f1a0953bcfbfccc5dd84abff63b2)
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
        '''The Amazon Resource Name (ARN) of the ``EventRule`` .

        AWS CloudFormation stack generates this ARN and then uses this ARN associated with the ``NotificationConfiguration`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The creation time of the ``EventRule`` .

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrManagedRules")
    def attr_managed_rules(self) -> typing.List[builtins.str]:
        '''A list of Amazon EventBridge Managed Rule ARNs associated with this ``EventRule`` .

        .. epigraph::

           These are created by AWS User Notifications within your account so your ``EventRules`` can function.

        :cloudformationAttribute: ManagedRules
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrManagedRules"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusSummaryByRegion")
    def attr_status_summary_by_region(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: StatusSummaryByRegion
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrStatusSummaryByRegion"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(self) -> builtins.str:
        '''The event type this rule should match with the EventBridge events.'''
        return typing.cast(builtins.str, jsii.get(self, "eventType"))

    @event_type.setter
    def event_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81d1b153a0905b2c5814e482bb87c0a8b11d3eff5d9c870657097be4c79e4804)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="notificationConfigurationArn")
    def notification_configuration_arn(self) -> builtins.str:
        '''The ARN for the ``NotificationConfiguration`` associated with this ``EventRule`` .'''
        return typing.cast(builtins.str, jsii.get(self, "notificationConfigurationArn"))

    @notification_configuration_arn.setter
    def notification_configuration_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f6731a75b69e9828e94cd56f13e2484ab994f7e17e1fb8ce1e0518eb23853cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationConfigurationArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="regions")
    def regions(self) -> typing.List[builtins.str]:
        '''A list of AWS Regions that send events to this ``EventRule`` .'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regions"))

    @regions.setter
    def regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89531f65574302c5ac9ea674da6b36a9b39096ba5050cb8e7e2a0da2b5d03e67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        '''The event source this rule should match with the EventBridge event sources.'''
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5f84ae06950218222a75646d0393c6dc744540c903f93356dc4cc8b58b9454b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="eventPattern")
    def event_pattern(self) -> typing.Optional[builtins.str]:
        '''An additional event pattern used to further filter the events this ``EventRule`` receives.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventPattern"))

    @event_pattern.setter
    def event_pattern(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c9ba9ceb13f4bbb20d1fdcbc4db9f3bbd193000353fb7d213848faaf0dacf8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventPattern", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_notifications.CfnEventRule.EventRuleStatusSummaryProperty",
        jsii_struct_bases=[],
        name_mapping={"reason": "reason", "status": "status"},
    )
    class EventRuleStatusSummaryProperty:
        def __init__(self, *, reason: builtins.str, status: builtins.str) -> None:
            '''Provides additional information about the current ``EventRule`` status.

            :param reason: A human-readable reason for ``EventRuleStatus`` .
            :param status: The status of the ``EventRule`` . - Values: - ``ACTIVE`` - The ``EventRule`` can process events. - ``INACTIVE`` - The ``EventRule`` may be unable to process events. - ``CREATING`` - The ``EventRule`` is being created. Only ``GET`` and ``LIST`` calls can be run. - ``UPDATING`` - The ``EventRule`` is being updated. Only ``GET`` and ``LIST`` calls can be run. - ``DELETING`` - The ``EventRule`` is being deleted. Only ``GET`` and ``LIST`` calls can be run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-notifications-eventrule-eventrulestatussummary.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_notifications as notifications
                
                event_rule_status_summary_property = notifications.CfnEventRule.EventRuleStatusSummaryProperty(
                    reason="reason",
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0862e7de7e4f6b1de2036652d175c4ef1949f04dadc360833e7e4899191d6fea)
                check_type(argname="argument reason", value=reason, expected_type=type_hints["reason"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "reason": reason,
                "status": status,
            }

        @builtins.property
        def reason(self) -> builtins.str:
            '''A human-readable reason for ``EventRuleStatus`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-notifications-eventrule-eventrulestatussummary.html#cfn-notifications-eventrule-eventrulestatussummary-reason
            '''
            result = self._values.get("reason")
            assert result is not None, "Required property 'reason' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def status(self) -> builtins.str:
            '''The status of the ``EventRule`` .

            - Values:
            - ``ACTIVE``
            - The ``EventRule`` can process events.
            - ``INACTIVE``
            - The ``EventRule`` may be unable to process events.
            - ``CREATING``
            - The ``EventRule`` is being created.

            Only ``GET`` and ``LIST`` calls can be run.

            - ``UPDATING``
            - The ``EventRule`` is being updated.

            Only ``GET`` and ``LIST`` calls can be run.

            - ``DELETING``
            - The ``EventRule`` is being deleted.

            Only ``GET`` and ``LIST`` calls can be run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-notifications-eventrule-eventrulestatussummary.html#cfn-notifications-eventrule-eventrulestatussummary-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventRuleStatusSummaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_notifications.CfnEventRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "event_type": "eventType",
        "notification_configuration_arn": "notificationConfigurationArn",
        "regions": "regions",
        "source": "source",
        "event_pattern": "eventPattern",
    },
)
class CfnEventRuleProps:
    def __init__(
        self,
        *,
        event_type: builtins.str,
        notification_configuration_arn: builtins.str,
        regions: typing.Sequence[builtins.str],
        source: builtins.str,
        event_pattern: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnEventRule``.

        :param event_type: The event type this rule should match with the EventBridge events. It must match with atleast one of the valid EventBridge event types. For example, Amazon EC2 Instance State change Notification and Amazon CloudWatch State Change. For more information, see `Event delivery from AWS services <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level>`_ in the *Amazon EventBridge User Guide* .
        :param notification_configuration_arn: The ARN for the ``NotificationConfiguration`` associated with this ``EventRule`` .
        :param regions: A list of AWS Regions that send events to this ``EventRule`` .
        :param source: The event source this rule should match with the EventBridge event sources. It must match with atleast one of the valid EventBridge event sources. Only AWS service sourced events are supported. For example, ``aws.ec2`` and ``aws.cloudwatch`` . For more information, see `Event delivery from AWS services <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level>`_ in the *Amazon EventBridge User Guide* .
        :param event_pattern: An additional event pattern used to further filter the events this ``EventRule`` receives. For more information, see `Amazon EventBridge event patterns <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html>`_ in the *Amazon EventBridge User Guide.*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-eventrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_notifications as notifications
            
            cfn_event_rule_props = notifications.CfnEventRuleProps(
                event_type="eventType",
                notification_configuration_arn="notificationConfigurationArn",
                regions=["regions"],
                source="source",
            
                # the properties below are optional
                event_pattern="eventPattern"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9518b7cf584ffb7ba5a4fb79f7584397ea33a005b8aebaa07c3bc5e5dc33bddb)
            check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
            check_type(argname="argument notification_configuration_arn", value=notification_configuration_arn, expected_type=type_hints["notification_configuration_arn"])
            check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument event_pattern", value=event_pattern, expected_type=type_hints["event_pattern"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_type": event_type,
            "notification_configuration_arn": notification_configuration_arn,
            "regions": regions,
            "source": source,
        }
        if event_pattern is not None:
            self._values["event_pattern"] = event_pattern

    @builtins.property
    def event_type(self) -> builtins.str:
        '''The event type this rule should match with the EventBridge events.

        It must match with atleast one of the valid EventBridge event types. For example, Amazon EC2 Instance State change Notification and Amazon CloudWatch State Change. For more information, see `Event delivery from AWS services <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level>`_ in the *Amazon EventBridge User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-eventrule.html#cfn-notifications-eventrule-eventtype
        '''
        result = self._values.get("event_type")
        assert result is not None, "Required property 'event_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notification_configuration_arn(self) -> builtins.str:
        '''The ARN for the ``NotificationConfiguration`` associated with this ``EventRule`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-eventrule.html#cfn-notifications-eventrule-notificationconfigurationarn
        '''
        result = self._values.get("notification_configuration_arn")
        assert result is not None, "Required property 'notification_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regions(self) -> typing.List[builtins.str]:
        '''A list of AWS Regions that send events to this ``EventRule`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-eventrule.html#cfn-notifications-eventrule-regions
        '''
        result = self._values.get("regions")
        assert result is not None, "Required property 'regions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def source(self) -> builtins.str:
        '''The event source this rule should match with the EventBridge event sources.

        It must match with atleast one of the valid EventBridge event sources. Only AWS service sourced events are supported. For example, ``aws.ec2`` and ``aws.cloudwatch`` . For more information, see `Event delivery from AWS services <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event.html#eb-service-event-delivery-level>`_ in the *Amazon EventBridge User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-eventrule.html#cfn-notifications-eventrule-source
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_pattern(self) -> typing.Optional[builtins.str]:
        '''An additional event pattern used to further filter the events this ``EventRule`` receives.

        For more information, see `Amazon EventBridge event patterns <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html>`_ in the *Amazon EventBridge User Guide.*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-eventrule.html#cfn-notifications-eventrule-eventpattern
        '''
        result = self._values.get("event_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnManagedNotificationAccountContactAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_notifications.CfnManagedNotificationAccountContactAssociation",
):
    '''Associates an Account Management Contact with a ``ManagedNotificationConfiguration`` for AWS User Notifications .

    For more information about AWS User Notifications , see the `AWS User Notifications User Guide <https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html>`_ . For more information about Account Management Contacts, see the `Account Management Reference Guide <https://docs.aws.amazon.com/accounts/latest/reference/API_AlternateContact.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-managednotificationaccountcontactassociation.html
    :cloudformationResource: AWS::Notifications::ManagedNotificationAccountContactAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_notifications as notifications
        
        cfn_managed_notification_account_contact_association = notifications.CfnManagedNotificationAccountContactAssociation(self, "MyCfnManagedNotificationAccountContactAssociation",
            contact_identifier="contactIdentifier",
            managed_notification_configuration_arn="managedNotificationConfigurationArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        contact_identifier: builtins.str,
        managed_notification_configuration_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param contact_identifier: The unique identifier of the notification contact associated with the AWS account. For more information about the contact types associated with an account, see the `Account Management Reference Guide <https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html#manage-acct-update-contact-alternate-orgs>`_ .
        :param managed_notification_configuration_arn: The ARN of the ``ManagedNotificationConfiguration`` to be associated with the ``Channel`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96181d9832ab883e4a967003ef3b840ed10f8d410e4b8ceaf721368c4c5a02c5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnManagedNotificationAccountContactAssociationProps(
            contact_identifier=contact_identifier,
            managed_notification_configuration_arn=managed_notification_configuration_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e73fa971227b1056e5bdcd4163fefc79baa11c9eed51c86f5d29a3bad3f50bf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__de22b92704255b6e9b389d8f1530aceab75300d39a63f9c91fd889e615c93935)
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
    @jsii.member(jsii_name="contactIdentifier")
    def contact_identifier(self) -> builtins.str:
        '''The unique identifier of the notification contact associated with the AWS account.'''
        return typing.cast(builtins.str, jsii.get(self, "contactIdentifier"))

    @contact_identifier.setter
    def contact_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f2864c82adf8222b71008a7a43d8ab7d77f3e9d371a6bd3a63ef3451fafcb60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="managedNotificationConfigurationArn")
    def managed_notification_configuration_arn(self) -> builtins.str:
        '''The ARN of the ``ManagedNotificationConfiguration`` to be associated with the ``Channel`` .'''
        return typing.cast(builtins.str, jsii.get(self, "managedNotificationConfigurationArn"))

    @managed_notification_configuration_arn.setter
    def managed_notification_configuration_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__723689b4f7e0ee73e180c6e8b0a172092e4905133e6f8e7994d8a793b8c63e79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedNotificationConfigurationArn", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_notifications.CfnManagedNotificationAccountContactAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "contact_identifier": "contactIdentifier",
        "managed_notification_configuration_arn": "managedNotificationConfigurationArn",
    },
)
class CfnManagedNotificationAccountContactAssociationProps:
    def __init__(
        self,
        *,
        contact_identifier: builtins.str,
        managed_notification_configuration_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnManagedNotificationAccountContactAssociation``.

        :param contact_identifier: The unique identifier of the notification contact associated with the AWS account. For more information about the contact types associated with an account, see the `Account Management Reference Guide <https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html#manage-acct-update-contact-alternate-orgs>`_ .
        :param managed_notification_configuration_arn: The ARN of the ``ManagedNotificationConfiguration`` to be associated with the ``Channel`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-managednotificationaccountcontactassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_notifications as notifications
            
            cfn_managed_notification_account_contact_association_props = notifications.CfnManagedNotificationAccountContactAssociationProps(
                contact_identifier="contactIdentifier",
                managed_notification_configuration_arn="managedNotificationConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ba701ff30108b1aeca6e33e95e36c02bce0446db03324798ed5b79a966800cc)
            check_type(argname="argument contact_identifier", value=contact_identifier, expected_type=type_hints["contact_identifier"])
            check_type(argname="argument managed_notification_configuration_arn", value=managed_notification_configuration_arn, expected_type=type_hints["managed_notification_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contact_identifier": contact_identifier,
            "managed_notification_configuration_arn": managed_notification_configuration_arn,
        }

    @builtins.property
    def contact_identifier(self) -> builtins.str:
        '''The unique identifier of the notification contact associated with the AWS account.

        For more information about the contact types associated with an account, see the `Account Management Reference Guide <https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact-alternate.html#manage-acct-update-contact-alternate-orgs>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-managednotificationaccountcontactassociation.html#cfn-notifications-managednotificationaccountcontactassociation-contactidentifier
        '''
        result = self._values.get("contact_identifier")
        assert result is not None, "Required property 'contact_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def managed_notification_configuration_arn(self) -> builtins.str:
        '''The ARN of the ``ManagedNotificationConfiguration`` to be associated with the ``Channel`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-managednotificationaccountcontactassociation.html#cfn-notifications-managednotificationaccountcontactassociation-managednotificationconfigurationarn
        '''
        result = self._values.get("managed_notification_configuration_arn")
        assert result is not None, "Required property 'managed_notification_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnManagedNotificationAccountContactAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnManagedNotificationAdditionalChannelAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_notifications.CfnManagedNotificationAdditionalChannelAssociation",
):
    '''Associates a ``Channel`` with a ``ManagedNotificationAdditionalChannelAssociation`` for AWS User Notifications .

    For more information about AWS User Notifications , see the `AWS User Notifications User Guide <https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-managednotificationadditionalchannelassociation.html
    :cloudformationResource: AWS::Notifications::ManagedNotificationAdditionalChannelAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_notifications as notifications
        
        cfn_managed_notification_additional_channel_association = notifications.CfnManagedNotificationAdditionalChannelAssociation(self, "MyCfnManagedNotificationAdditionalChannelAssociation",
            channel_arn="channelArn",
            managed_notification_configuration_arn="managedNotificationConfigurationArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        channel_arn: builtins.str,
        managed_notification_configuration_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param channel_arn: The ARN of the ``Channel`` .
        :param managed_notification_configuration_arn: The ARN of the ``ManagedNotificationAdditionalChannelAssociation`` associated with the ``Channel`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ca734986c83660130935052d366897b8c8be9a3097eeb3e4d8a8e55d157be14)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnManagedNotificationAdditionalChannelAssociationProps(
            channel_arn=channel_arn,
            managed_notification_configuration_arn=managed_notification_configuration_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e28e0910e1ca8649c67a2f410907337d1630631c5619cb29f1f8aea6b44f1ae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a2506d928b82af9fe5027dc3a3d36bec7429236e90e696056589e09d98371bdf)
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
    @jsii.member(jsii_name="channelArn")
    def channel_arn(self) -> builtins.str:
        '''The ARN of the ``Channel`` .'''
        return typing.cast(builtins.str, jsii.get(self, "channelArn"))

    @channel_arn.setter
    def channel_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae2aafbc82a652d2ce3c5194be413585028b15cdada72b53c5ecf469375ef2a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="managedNotificationConfigurationArn")
    def managed_notification_configuration_arn(self) -> builtins.str:
        '''The ARN of the ``ManagedNotificationAdditionalChannelAssociation`` associated with the ``Channel`` .'''
        return typing.cast(builtins.str, jsii.get(self, "managedNotificationConfigurationArn"))

    @managed_notification_configuration_arn.setter
    def managed_notification_configuration_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3420dbc2928b8b5bd017053f781f8eb1c6893c1b43a27f7854a5dbeb64b60445)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedNotificationConfigurationArn", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_notifications.CfnManagedNotificationAdditionalChannelAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_arn": "channelArn",
        "managed_notification_configuration_arn": "managedNotificationConfigurationArn",
    },
)
class CfnManagedNotificationAdditionalChannelAssociationProps:
    def __init__(
        self,
        *,
        channel_arn: builtins.str,
        managed_notification_configuration_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnManagedNotificationAdditionalChannelAssociation``.

        :param channel_arn: The ARN of the ``Channel`` .
        :param managed_notification_configuration_arn: The ARN of the ``ManagedNotificationAdditionalChannelAssociation`` associated with the ``Channel`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-managednotificationadditionalchannelassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_notifications as notifications
            
            cfn_managed_notification_additional_channel_association_props = notifications.CfnManagedNotificationAdditionalChannelAssociationProps(
                channel_arn="channelArn",
                managed_notification_configuration_arn="managedNotificationConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63600091503bee10f7ba2c01f3247b370b8b2bca175e1cc3db1e6800e18fedd9)
            check_type(argname="argument channel_arn", value=channel_arn, expected_type=type_hints["channel_arn"])
            check_type(argname="argument managed_notification_configuration_arn", value=managed_notification_configuration_arn, expected_type=type_hints["managed_notification_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_arn": channel_arn,
            "managed_notification_configuration_arn": managed_notification_configuration_arn,
        }

    @builtins.property
    def channel_arn(self) -> builtins.str:
        '''The ARN of the ``Channel`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-managednotificationadditionalchannelassociation.html#cfn-notifications-managednotificationadditionalchannelassociation-channelarn
        '''
        result = self._values.get("channel_arn")
        assert result is not None, "Required property 'channel_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def managed_notification_configuration_arn(self) -> builtins.str:
        '''The ARN of the ``ManagedNotificationAdditionalChannelAssociation`` associated with the ``Channel`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-managednotificationadditionalchannelassociation.html#cfn-notifications-managednotificationadditionalchannelassociation-managednotificationconfigurationarn
        '''
        result = self._values.get("managed_notification_configuration_arn")
        assert result is not None, "Required property 'managed_notification_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnManagedNotificationAdditionalChannelAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnNotificationConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_notifications.CfnNotificationConfiguration",
):
    '''Configures a ``NotificationConfiguration`` for AWS User Notifications .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-notificationconfiguration.html
    :cloudformationResource: AWS::Notifications::NotificationConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_notifications as notifications
        
        cfn_notification_configuration = notifications.CfnNotificationConfiguration(self, "MyCfnNotificationConfiguration",
            description="description",
            name="name",
        
            # the properties below are optional
            aggregation_duration="aggregationDuration",
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
        description: builtins.str,
        name: builtins.str,
        aggregation_duration: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: The description of the ``NotificationConfiguration`` .
        :param name: The name of the ``NotificationConfiguration`` . Supports RFC 3986's unreserved characters.
        :param aggregation_duration: The aggregation preference of the ``NotificationConfiguration`` . - Values: - ``LONG`` - Aggregate notifications for long periods of time (12 hours). - ``SHORT`` - Aggregate notifications for short periods of time (5 minutes). - ``NONE`` - Don't aggregate notifications.
        :param tags: A map of tags assigned to a ``NotificationConfiguration`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5a1cf31f790937b5967ad78a42e8a6c98b04b21643bfcdd379cabb7f43b17f1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNotificationConfigurationProps(
            description=description,
            name=name,
            aggregation_duration=aggregation_duration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99c4c6bcfdad64190a4b003dd211cb1c28e0aed4b082d0cef3b986b4d46b4d0d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed80b7239a03619bfe17128260c1ef875a0004bef6f44982a06bac0ca7dd24dd)
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
        '''The Amazon Resource Name (ARN) of the ``NotificationConfiguration`` resource.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The creation time of the ``NotificationConfiguration`` .

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current status of the ``NotificationConfiguration`` .

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the ``NotificationConfiguration`` .'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b56129db1bc5e2b088f2e953b3a5cadd65fbae6a6d2e9bff79548baba4e1c65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the ``NotificationConfiguration`` .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71e66aa92e41cd8989cfdac8332aacd83371fe96d00b1cfb8e4f8f6c74bdeefc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="aggregationDuration")
    def aggregation_duration(self) -> typing.Optional[builtins.str]:
        '''The aggregation preference of the ``NotificationConfiguration`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationDuration"))

    @aggregation_duration.setter
    def aggregation_duration(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce9aa4a245c055d6b2e72d9ea7585d89b52c50836000693cef5f09365372734c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationDuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map of tags assigned to a ``NotificationConfiguration`` .'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d80fd02377dda29814fae801cf32c8200e2aa5b9ff4b7440916ad6d4efbeb00b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_notifications.CfnNotificationConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "name": "name",
        "aggregation_duration": "aggregationDuration",
        "tags": "tags",
    },
)
class CfnNotificationConfigurationProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        name: builtins.str,
        aggregation_duration: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnNotificationConfiguration``.

        :param description: The description of the ``NotificationConfiguration`` .
        :param name: The name of the ``NotificationConfiguration`` . Supports RFC 3986's unreserved characters.
        :param aggregation_duration: The aggregation preference of the ``NotificationConfiguration`` . - Values: - ``LONG`` - Aggregate notifications for long periods of time (12 hours). - ``SHORT`` - Aggregate notifications for short periods of time (5 minutes). - ``NONE`` - Don't aggregate notifications.
        :param tags: A map of tags assigned to a ``NotificationConfiguration`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-notificationconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_notifications as notifications
            
            cfn_notification_configuration_props = notifications.CfnNotificationConfigurationProps(
                description="description",
                name="name",
            
                # the properties below are optional
                aggregation_duration="aggregationDuration",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2533f954a13ead8ba0e86dbad3d4401450ff85451a17c80b370344cb112ae478)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument aggregation_duration", value=aggregation_duration, expected_type=type_hints["aggregation_duration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "name": name,
        }
        if aggregation_duration is not None:
            self._values["aggregation_duration"] = aggregation_duration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> builtins.str:
        '''The description of the ``NotificationConfiguration`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-notificationconfiguration.html#cfn-notifications-notificationconfiguration-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the ``NotificationConfiguration`` .

        Supports RFC 3986's unreserved characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-notificationconfiguration.html#cfn-notifications-notificationconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aggregation_duration(self) -> typing.Optional[builtins.str]:
        '''The aggregation preference of the ``NotificationConfiguration`` .

        - Values:
        - ``LONG``
        - Aggregate notifications for long periods of time (12 hours).
        - ``SHORT``
        - Aggregate notifications for short periods of time (5 minutes).
        - ``NONE``
        - Don't aggregate notifications.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-notificationconfiguration.html#cfn-notifications-notificationconfiguration-aggregationduration
        '''
        result = self._values.get("aggregation_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map of tags assigned to a ``NotificationConfiguration`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-notificationconfiguration.html#cfn-notifications-notificationconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNotificationConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnNotificationHub(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_notifications.CfnNotificationHub",
):
    '''Configures a ``NotificationHub`` for AWS User Notifications .

    For more information about notification hub, see the `AWS User Notifications User Guide <https://docs.aws.amazon.com/notifications/latest/userguide/notification-hubs.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-notificationhub.html
    :cloudformationResource: AWS::Notifications::NotificationHub
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_notifications as notifications
        
        cfn_notification_hub = notifications.CfnNotificationHub(self, "MyCfnNotificationHub",
            region="region"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        region: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param region: The ``NotificationHub`` Region.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68d72929c95357a15821df7d24b28076913c2c16ae8caa651de92ab7110ee545)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNotificationHubProps(region=region)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__567dd116772fd10bcdaf956ec536dc5810b4f3cc3f16ccd9a9d86db8519bb2ad)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8cdcacace93e52a000661ec6fb6dc815044c226939c4984a920cbeabbad2c65d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The date and time the ``NotificationHubOverview`` was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrNotificationHubStatusSummary")
    def attr_notification_hub_status_summary(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: NotificationHubStatusSummary
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrNotificationHubStatusSummary"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        '''The ``NotificationHub`` Region.'''
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__865411d5534fe323b415ed4cf0f3a74893e03d33d1ae33e8d515a71e49d41f82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_notifications.CfnNotificationHub.NotificationHubStatusSummaryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "notification_hub_status": "notificationHubStatus",
            "notification_hub_status_reason": "notificationHubStatusReason",
        },
    )
    class NotificationHubStatusSummaryProperty:
        def __init__(
            self,
            *,
            notification_hub_status: builtins.str,
            notification_hub_status_reason: builtins.str,
        ) -> None:
            '''Provides additional information about the current ``NotificationHub`` status.

            :param notification_hub_status: Indicates the current status of the ``NotificationHub`` .
            :param notification_hub_status_reason: An explanation for the current status.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-notifications-notificationhub-notificationhubstatussummary.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_notifications as notifications
                
                notification_hub_status_summary_property = notifications.CfnNotificationHub.NotificationHubStatusSummaryProperty(
                    notification_hub_status="notificationHubStatus",
                    notification_hub_status_reason="notificationHubStatusReason"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8aa8a0cc3749f69e28b77cefd47fc05557b9a1869a97350b92cdcb9f3438b543)
                check_type(argname="argument notification_hub_status", value=notification_hub_status, expected_type=type_hints["notification_hub_status"])
                check_type(argname="argument notification_hub_status_reason", value=notification_hub_status_reason, expected_type=type_hints["notification_hub_status_reason"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "notification_hub_status": notification_hub_status,
                "notification_hub_status_reason": notification_hub_status_reason,
            }

        @builtins.property
        def notification_hub_status(self) -> builtins.str:
            '''Indicates the current status of the ``NotificationHub`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-notifications-notificationhub-notificationhubstatussummary.html#cfn-notifications-notificationhub-notificationhubstatussummary-notificationhubstatus
            '''
            result = self._values.get("notification_hub_status")
            assert result is not None, "Required property 'notification_hub_status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def notification_hub_status_reason(self) -> builtins.str:
            '''An explanation for the current status.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-notifications-notificationhub-notificationhubstatussummary.html#cfn-notifications-notificationhub-notificationhubstatussummary-notificationhubstatusreason
            '''
            result = self._values.get("notification_hub_status_reason")
            assert result is not None, "Required property 'notification_hub_status_reason' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationHubStatusSummaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_notifications.CfnNotificationHubProps",
    jsii_struct_bases=[],
    name_mapping={"region": "region"},
)
class CfnNotificationHubProps:
    def __init__(self, *, region: builtins.str) -> None:
        '''Properties for defining a ``CfnNotificationHub``.

        :param region: The ``NotificationHub`` Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-notificationhub.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_notifications as notifications
            
            cfn_notification_hub_props = notifications.CfnNotificationHubProps(
                region="region"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__920924baa84f6463cdd237bcaa739a631a79dad627c4370064c68f1de8c3c630)
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "region": region,
        }

    @builtins.property
    def region(self) -> builtins.str:
        '''The ``NotificationHub`` Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notifications-notificationhub.html#cfn-notifications-notificationhub-region
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNotificationHubProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnChannelAssociation",
    "CfnChannelAssociationProps",
    "CfnEventRule",
    "CfnEventRuleProps",
    "CfnManagedNotificationAccountContactAssociation",
    "CfnManagedNotificationAccountContactAssociationProps",
    "CfnManagedNotificationAdditionalChannelAssociation",
    "CfnManagedNotificationAdditionalChannelAssociationProps",
    "CfnNotificationConfiguration",
    "CfnNotificationConfigurationProps",
    "CfnNotificationHub",
    "CfnNotificationHubProps",
]

publication.publish()

def _typecheckingstub__96bfb9a9cbe4c6b38cb964bde4e63ccdb746cc48ac8dd61661a318886da6ba7f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    arn: builtins.str,
    notification_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0ffcf7c83a3beb5a9feedb6bf40d486b1aa9bad41565ae2a782129cc7450e94(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad26b3aa74c912ac52ae9f4bfb186ae1996d8ffa2fff5b28d9a9dcb2f5ceffbf(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02aa05d5cab2ed92674dea9fe8bfd20781091f494e9c3e3da3e1cedb24710ade(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b2d69598efa0d97ebfbcf163b7e00dfefacab9bb759efc23a009243fcbc29fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3df32ecb43a8f1e94c1f975e24a79631c45fd6739c1d7bea0e44c5c169b5137c(
    *,
    arn: builtins.str,
    notification_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec202e2ad7890be955535389c490f73db69e1ae4c0e2b9af79f33a0bb4e4dd47(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    event_type: builtins.str,
    notification_configuration_arn: builtins.str,
    regions: typing.Sequence[builtins.str],
    source: builtins.str,
    event_pattern: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c5fa74e0d9c81586c85ebd06110e66abfa6f3eca8a5c7b89fcce4d070b434dd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed227bd8ca507740b963532ef2c249c436e3f1a0953bcfbfccc5dd84abff63b2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81d1b153a0905b2c5814e482bb87c0a8b11d3eff5d9c870657097be4c79e4804(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f6731a75b69e9828e94cd56f13e2484ab994f7e17e1fb8ce1e0518eb23853cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89531f65574302c5ac9ea674da6b36a9b39096ba5050cb8e7e2a0da2b5d03e67(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5f84ae06950218222a75646d0393c6dc744540c903f93356dc4cc8b58b9454b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c9ba9ceb13f4bbb20d1fdcbc4db9f3bbd193000353fb7d213848faaf0dacf8d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0862e7de7e4f6b1de2036652d175c4ef1949f04dadc360833e7e4899191d6fea(
    *,
    reason: builtins.str,
    status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9518b7cf584ffb7ba5a4fb79f7584397ea33a005b8aebaa07c3bc5e5dc33bddb(
    *,
    event_type: builtins.str,
    notification_configuration_arn: builtins.str,
    regions: typing.Sequence[builtins.str],
    source: builtins.str,
    event_pattern: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96181d9832ab883e4a967003ef3b840ed10f8d410e4b8ceaf721368c4c5a02c5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    contact_identifier: builtins.str,
    managed_notification_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e73fa971227b1056e5bdcd4163fefc79baa11c9eed51c86f5d29a3bad3f50bf(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de22b92704255b6e9b389d8f1530aceab75300d39a63f9c91fd889e615c93935(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f2864c82adf8222b71008a7a43d8ab7d77f3e9d371a6bd3a63ef3451fafcb60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__723689b4f7e0ee73e180c6e8b0a172092e4905133e6f8e7994d8a793b8c63e79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ba701ff30108b1aeca6e33e95e36c02bce0446db03324798ed5b79a966800cc(
    *,
    contact_identifier: builtins.str,
    managed_notification_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ca734986c83660130935052d366897b8c8be9a3097eeb3e4d8a8e55d157be14(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel_arn: builtins.str,
    managed_notification_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e28e0910e1ca8649c67a2f410907337d1630631c5619cb29f1f8aea6b44f1ae(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2506d928b82af9fe5027dc3a3d36bec7429236e90e696056589e09d98371bdf(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae2aafbc82a652d2ce3c5194be413585028b15cdada72b53c5ecf469375ef2a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3420dbc2928b8b5bd017053f781f8eb1c6893c1b43a27f7854a5dbeb64b60445(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63600091503bee10f7ba2c01f3247b370b8b2bca175e1cc3db1e6800e18fedd9(
    *,
    channel_arn: builtins.str,
    managed_notification_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5a1cf31f790937b5967ad78a42e8a6c98b04b21643bfcdd379cabb7f43b17f1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: builtins.str,
    name: builtins.str,
    aggregation_duration: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99c4c6bcfdad64190a4b003dd211cb1c28e0aed4b082d0cef3b986b4d46b4d0d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed80b7239a03619bfe17128260c1ef875a0004bef6f44982a06bac0ca7dd24dd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b56129db1bc5e2b088f2e953b3a5cadd65fbae6a6d2e9bff79548baba4e1c65(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71e66aa92e41cd8989cfdac8332aacd83371fe96d00b1cfb8e4f8f6c74bdeefc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce9aa4a245c055d6b2e72d9ea7585d89b52c50836000693cef5f09365372734c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d80fd02377dda29814fae801cf32c8200e2aa5b9ff4b7440916ad6d4efbeb00b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2533f954a13ead8ba0e86dbad3d4401450ff85451a17c80b370344cb112ae478(
    *,
    description: builtins.str,
    name: builtins.str,
    aggregation_duration: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68d72929c95357a15821df7d24b28076913c2c16ae8caa651de92ab7110ee545(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__567dd116772fd10bcdaf956ec536dc5810b4f3cc3f16ccd9a9d86db8519bb2ad(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cdcacace93e52a000661ec6fb6dc815044c226939c4984a920cbeabbad2c65d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__865411d5534fe323b415ed4cf0f3a74893e03d33d1ae33e8d515a71e49d41f82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aa8a0cc3749f69e28b77cefd47fc05557b9a1869a97350b92cdcb9f3438b543(
    *,
    notification_hub_status: builtins.str,
    notification_hub_status_reason: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__920924baa84f6463cdd237bcaa739a631a79dad627c4370064c68f1de8c3c630(
    *,
    region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
