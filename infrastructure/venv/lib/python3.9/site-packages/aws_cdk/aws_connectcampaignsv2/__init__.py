r'''
# AWS::ConnectCampaignsV2 Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_connectcampaignsv2 as connectcampaigns
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ConnectCampaignsV2 construct libraries](https://constructs.dev/search?q=connectcampaignsv2)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ConnectCampaignsV2 resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ConnectCampaignsV2.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ConnectCampaignsV2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ConnectCampaignsV2.html).

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


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnCampaign(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign",
):
    '''Creates an outbound campaign.

    .. epigraph::

       - For users to be able to view or edit a campaign at a later date by using the Amazon Connect user interface, you must add the instance ID as a tag. For example, ``{ "tags": {"owner": "arn:aws:connect:{REGION}:{AWS_ACCOUNT_ID}:instance/{CONNECT_INSTANCE_ID}"}}`` .
       - After a campaign is created, you can't add/remove source.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaignsv2-campaign.html
    :cloudformationResource: AWS::ConnectCampaignsV2::Campaign
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
        
        # agentless_config: Any
        
        cfn_campaign = connectcampaignsv2.CfnCampaign(self, "MyCfnCampaign",
            channel_subtype_config=connectcampaignsv2.CfnCampaign.ChannelSubtypeConfigProperty(
                email=connectcampaignsv2.CfnCampaign.EmailChannelSubtypeConfigProperty(
                    default_outbound_config=connectcampaignsv2.CfnCampaign.EmailOutboundConfigProperty(
                        connect_source_email_address="connectSourceEmailAddress",
                        wisdom_template_arn="wisdomTemplateArn",
        
                        # the properties below are optional
                        source_email_address_display_name="sourceEmailAddressDisplayName"
                    ),
                    outbound_mode=connectcampaignsv2.CfnCampaign.EmailOutboundModeProperty(
                        agentless_config=agentless_config
                    ),
        
                    # the properties below are optional
                    capacity=123
                ),
                sms=connectcampaignsv2.CfnCampaign.SmsChannelSubtypeConfigProperty(
                    default_outbound_config=connectcampaignsv2.CfnCampaign.SmsOutboundConfigProperty(
                        connect_source_phone_number_arn="connectSourcePhoneNumberArn",
                        wisdom_template_arn="wisdomTemplateArn"
                    ),
                    outbound_mode=connectcampaignsv2.CfnCampaign.SmsOutboundModeProperty(
                        agentless_config=agentless_config
                    ),
        
                    # the properties below are optional
                    capacity=123
                ),
                telephony=connectcampaignsv2.CfnCampaign.TelephonyChannelSubtypeConfigProperty(
                    default_outbound_config=connectcampaignsv2.CfnCampaign.TelephonyOutboundConfigProperty(
                        connect_contact_flow_id="connectContactFlowId",
        
                        # the properties below are optional
                        answer_machine_detection_config=connectcampaignsv2.CfnCampaign.AnswerMachineDetectionConfigProperty(
                            enable_answer_machine_detection=False,
        
                            # the properties below are optional
                            await_answer_machine_prompt=False
                        ),
                        connect_source_phone_number="connectSourcePhoneNumber"
                    ),
                    outbound_mode=connectcampaignsv2.CfnCampaign.TelephonyOutboundModeProperty(
                        agentless_config=agentless_config,
                        predictive_config=connectcampaignsv2.CfnCampaign.PredictiveConfigProperty(
                            bandwidth_allocation=123
                        ),
                        progressive_config=connectcampaignsv2.CfnCampaign.ProgressiveConfigProperty(
                            bandwidth_allocation=123
                        )
                    ),
        
                    # the properties below are optional
                    capacity=123,
                    connect_queue_id="connectQueueId"
                )
            ),
            connect_instance_id="connectInstanceId",
            name="name",
        
            # the properties below are optional
            communication_limits_override=connectcampaignsv2.CfnCampaign.CommunicationLimitsConfigProperty(
                all_channels_subtypes=connectcampaignsv2.CfnCampaign.CommunicationLimitsProperty(
                    communication_limit_list=[connectcampaignsv2.CfnCampaign.CommunicationLimitProperty(
                        frequency=123,
                        max_count_per_recipient=123,
                        unit="unit"
                    )]
                ),
                instance_limits_handling="instanceLimitsHandling"
            ),
            communication_time_config=connectcampaignsv2.CfnCampaign.CommunicationTimeConfigProperty(
                local_time_zone_config=connectcampaignsv2.CfnCampaign.LocalTimeZoneConfigProperty(
                    default_time_zone="defaultTimeZone",
                    local_time_zone_detection=["localTimeZoneDetection"]
                ),
        
                # the properties below are optional
                email=connectcampaignsv2.CfnCampaign.TimeWindowProperty(
                    open_hours=connectcampaignsv2.CfnCampaign.OpenHoursProperty(
                        daily_hours=[connectcampaignsv2.CfnCampaign.DailyHourProperty(
                            key="key",
                            value=[connectcampaignsv2.CfnCampaign.TimeRangeProperty(
                                end_time="endTime",
                                start_time="startTime"
                            )]
                        )]
                    ),
        
                    # the properties below are optional
                    restricted_periods=connectcampaignsv2.CfnCampaign.RestrictedPeriodsProperty(
                        restricted_period_list=[connectcampaignsv2.CfnCampaign.RestrictedPeriodProperty(
                            end_date="endDate",
                            start_date="startDate",
        
                            # the properties below are optional
                            name="name"
                        )]
                    )
                ),
                sms=connectcampaignsv2.CfnCampaign.TimeWindowProperty(
                    open_hours=connectcampaignsv2.CfnCampaign.OpenHoursProperty(
                        daily_hours=[connectcampaignsv2.CfnCampaign.DailyHourProperty(
                            key="key",
                            value=[connectcampaignsv2.CfnCampaign.TimeRangeProperty(
                                end_time="endTime",
                                start_time="startTime"
                            )]
                        )]
                    ),
        
                    # the properties below are optional
                    restricted_periods=connectcampaignsv2.CfnCampaign.RestrictedPeriodsProperty(
                        restricted_period_list=[connectcampaignsv2.CfnCampaign.RestrictedPeriodProperty(
                            end_date="endDate",
                            start_date="startDate",
        
                            # the properties below are optional
                            name="name"
                        )]
                    )
                ),
                telephony=connectcampaignsv2.CfnCampaign.TimeWindowProperty(
                    open_hours=connectcampaignsv2.CfnCampaign.OpenHoursProperty(
                        daily_hours=[connectcampaignsv2.CfnCampaign.DailyHourProperty(
                            key="key",
                            value=[connectcampaignsv2.CfnCampaign.TimeRangeProperty(
                                end_time="endTime",
                                start_time="startTime"
                            )]
                        )]
                    ),
        
                    # the properties below are optional
                    restricted_periods=connectcampaignsv2.CfnCampaign.RestrictedPeriodsProperty(
                        restricted_period_list=[connectcampaignsv2.CfnCampaign.RestrictedPeriodProperty(
                            end_date="endDate",
                            start_date="startDate",
        
                            # the properties below are optional
                            name="name"
                        )]
                    )
                )
            ),
            connect_campaign_flow_arn="connectCampaignFlowArn",
            schedule=connectcampaignsv2.CfnCampaign.ScheduleProperty(
                end_time="endTime",
                start_time="startTime",
        
                # the properties below are optional
                refresh_frequency="refreshFrequency"
            ),
            source=connectcampaignsv2.CfnCampaign.SourceProperty(
                customer_profiles_segment_arn="customerProfilesSegmentArn",
                event_trigger=connectcampaignsv2.CfnCampaign.EventTriggerProperty(
                    customer_profiles_domain_arn="customerProfilesDomainArn"
                )
            ),
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
        channel_subtype_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.ChannelSubtypeConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        connect_instance_id: builtins.str,
        name: builtins.str,
        communication_limits_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.CommunicationLimitsConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        communication_time_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.CommunicationTimeConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        connect_campaign_flow_arn: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.ScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.SourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param channel_subtype_config: Contains channel subtype configuration for an outbound campaign.
        :param connect_instance_id: The identifier of the Amazon Connect instance. You can find the ``instanceId`` in the ARN of the instance.
        :param name: The name of the outbound campaign.
        :param communication_limits_override: Communication limits configuration for an outbound campaign.
        :param communication_time_config: Contains communication time configuration for an outbound campaign.
        :param connect_campaign_flow_arn: The Amazon Resource Name (ARN) of the Amazon Connect campaign flow associated with the outbound campaign.
        :param schedule: Contains the schedule configuration.
        :param source: Contains source configuration.
        :param tags: The tags used to organize, track, or control access for this resource. For example, ``{ "tags": {"key1":"value1", "key2":"value2"} }`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__228f2b3a0b621ad8a32effe36abeb2d513f50077bd0ad5de7f33f1ea81da26bf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCampaignProps(
            channel_subtype_config=channel_subtype_config,
            connect_instance_id=connect_instance_id,
            name=name,
            communication_limits_override=communication_limits_override,
            communication_time_config=communication_time_config,
            connect_campaign_flow_arn=connect_campaign_flow_arn,
            schedule=schedule,
            source=source,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a3569f68d4e1cebb6aa0c64e1d5986831e6aae0db4d29cfdc75c914d15ffdce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c76203b12deea4c92c4180a4c58e9869df456b6f2b525019f1464142d4eec24c)
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
        '''The Amazon Resource Name (ARN).

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
    @jsii.member(jsii_name="channelSubtypeConfig")
    def channel_subtype_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCampaign.ChannelSubtypeConfigProperty"]:
        '''Contains channel subtype configuration for an outbound campaign.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCampaign.ChannelSubtypeConfigProperty"], jsii.get(self, "channelSubtypeConfig"))

    @channel_subtype_config.setter
    def channel_subtype_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCampaign.ChannelSubtypeConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5b5c43e63bf2a0bf41f238db2ecf2eed8032758072a77ebd8c459798f74fa0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelSubtypeConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="connectInstanceId")
    def connect_instance_id(self) -> builtins.str:
        '''The identifier of the Amazon Connect instance.'''
        return typing.cast(builtins.str, jsii.get(self, "connectInstanceId"))

    @connect_instance_id.setter
    def connect_instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dea841111eb9715b7977d34769972a35f4ff12770a8fd30c5e8756c52e2315dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectInstanceId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the outbound campaign.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a6ee2c8ab1041b75d3fc61f47c640e057770a39c0cd0f8b43528a1df4134a14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="communicationLimitsOverride")
    def communication_limits_override(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CommunicationLimitsConfigProperty"]]:
        '''Communication limits configuration for an outbound campaign.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CommunicationLimitsConfigProperty"]], jsii.get(self, "communicationLimitsOverride"))

    @communication_limits_override.setter
    def communication_limits_override(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CommunicationLimitsConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9a4f9850d67cc76e259c5826fc9085afbf3a202dbe3ba9f6af537bfd18c830a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "communicationLimitsOverride", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="communicationTimeConfig")
    def communication_time_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CommunicationTimeConfigProperty"]]:
        '''Contains communication time configuration for an outbound campaign.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CommunicationTimeConfigProperty"]], jsii.get(self, "communicationTimeConfig"))

    @communication_time_config.setter
    def communication_time_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CommunicationTimeConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f04ec307144a013ae0d78d8747dea1d25d0ab7e9abc18aaab84c15553a5bb868)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "communicationTimeConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="connectCampaignFlowArn")
    def connect_campaign_flow_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon Connect campaign flow associated with the outbound campaign.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectCampaignFlowArn"))

    @connect_campaign_flow_arn.setter
    def connect_campaign_flow_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c514dbfca338965ca2462164a214264c8a79ca12e54b81685d99cc57a888b73c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectCampaignFlowArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.ScheduleProperty"]]:
        '''Contains the schedule configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.ScheduleProperty"]], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.ScheduleProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96d94c4ddf36f3ab10421fbfcb861afdc6852b09a0b0783e33f602560dc90a87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.SourceProperty"]]:
        '''Contains source configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.SourceProperty"]], jsii.get(self, "source"))

    @source.setter
    def source(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.SourceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dd88e602a1609757680509707feb43ec965d5628d820f7eb876dc6ac055b404)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7a5de836c29e94a66b86ab16ab9047f892319b5f0f4bb59a47dc977cdb0fb0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.AnswerMachineDetectionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_answer_machine_detection": "enableAnswerMachineDetection",
            "await_answer_machine_prompt": "awaitAnswerMachinePrompt",
        },
    )
    class AnswerMachineDetectionConfigProperty:
        def __init__(
            self,
            *,
            enable_answer_machine_detection: typing.Union[builtins.bool, _IResolvable_da3f097b],
            await_answer_machine_prompt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Contains answering machine detection configuration.

            :param enable_answer_machine_detection: Enables answering machine detection.
            :param await_answer_machine_prompt: Whether or not waiting for an answer machine prompt is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-answermachinedetectionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                answer_machine_detection_config_property = connectcampaignsv2.CfnCampaign.AnswerMachineDetectionConfigProperty(
                    enable_answer_machine_detection=False,
                
                    # the properties below are optional
                    await_answer_machine_prompt=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cc9e20500646db1cdb84f99ed95755110a841a334cc195de359fe87f9f7051d5)
                check_type(argname="argument enable_answer_machine_detection", value=enable_answer_machine_detection, expected_type=type_hints["enable_answer_machine_detection"])
                check_type(argname="argument await_answer_machine_prompt", value=await_answer_machine_prompt, expected_type=type_hints["await_answer_machine_prompt"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enable_answer_machine_detection": enable_answer_machine_detection,
            }
            if await_answer_machine_prompt is not None:
                self._values["await_answer_machine_prompt"] = await_answer_machine_prompt

        @builtins.property
        def enable_answer_machine_detection(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Enables answering machine detection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-answermachinedetectionconfig.html#cfn-connectcampaignsv2-campaign-answermachinedetectionconfig-enableanswermachinedetection
            '''
            result = self._values.get("enable_answer_machine_detection")
            assert result is not None, "Required property 'enable_answer_machine_detection' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def await_answer_machine_prompt(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether or not waiting for an answer machine prompt is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-answermachinedetectionconfig.html#cfn-connectcampaignsv2-campaign-answermachinedetectionconfig-awaitanswermachineprompt
            '''
            result = self._values.get("await_answer_machine_prompt")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnswerMachineDetectionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.ChannelSubtypeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"email": "email", "sms": "sms", "telephony": "telephony"},
    )
    class ChannelSubtypeConfigProperty:
        def __init__(
            self,
            *,
            email: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.EmailChannelSubtypeConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.SmsChannelSubtypeConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            telephony: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.TelephonyChannelSubtypeConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains channel subtype configuration for an outbound campaign.

            :param email: The configuration of the email channel subtype.
            :param sms: The configuration of the SMS channel subtype.
            :param telephony: The configuration of the telephony channel subtype.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-channelsubtypeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                # agentless_config: Any
                
                channel_subtype_config_property = connectcampaignsv2.CfnCampaign.ChannelSubtypeConfigProperty(
                    email=connectcampaignsv2.CfnCampaign.EmailChannelSubtypeConfigProperty(
                        default_outbound_config=connectcampaignsv2.CfnCampaign.EmailOutboundConfigProperty(
                            connect_source_email_address="connectSourceEmailAddress",
                            wisdom_template_arn="wisdomTemplateArn",
                
                            # the properties below are optional
                            source_email_address_display_name="sourceEmailAddressDisplayName"
                        ),
                        outbound_mode=connectcampaignsv2.CfnCampaign.EmailOutboundModeProperty(
                            agentless_config=agentless_config
                        ),
                
                        # the properties below are optional
                        capacity=123
                    ),
                    sms=connectcampaignsv2.CfnCampaign.SmsChannelSubtypeConfigProperty(
                        default_outbound_config=connectcampaignsv2.CfnCampaign.SmsOutboundConfigProperty(
                            connect_source_phone_number_arn="connectSourcePhoneNumberArn",
                            wisdom_template_arn="wisdomTemplateArn"
                        ),
                        outbound_mode=connectcampaignsv2.CfnCampaign.SmsOutboundModeProperty(
                            agentless_config=agentless_config
                        ),
                
                        # the properties below are optional
                        capacity=123
                    ),
                    telephony=connectcampaignsv2.CfnCampaign.TelephonyChannelSubtypeConfigProperty(
                        default_outbound_config=connectcampaignsv2.CfnCampaign.TelephonyOutboundConfigProperty(
                            connect_contact_flow_id="connectContactFlowId",
                
                            # the properties below are optional
                            answer_machine_detection_config=connectcampaignsv2.CfnCampaign.AnswerMachineDetectionConfigProperty(
                                enable_answer_machine_detection=False,
                
                                # the properties below are optional
                                await_answer_machine_prompt=False
                            ),
                            connect_source_phone_number="connectSourcePhoneNumber"
                        ),
                        outbound_mode=connectcampaignsv2.CfnCampaign.TelephonyOutboundModeProperty(
                            agentless_config=agentless_config,
                            predictive_config=connectcampaignsv2.CfnCampaign.PredictiveConfigProperty(
                                bandwidth_allocation=123
                            ),
                            progressive_config=connectcampaignsv2.CfnCampaign.ProgressiveConfigProperty(
                                bandwidth_allocation=123
                            )
                        ),
                
                        # the properties below are optional
                        capacity=123,
                        connect_queue_id="connectQueueId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aae9c62c36e7d18a87df32d56bbdc6f7740c287aaac55c92832b7ca366aa6b5b)
                check_type(argname="argument email", value=email, expected_type=type_hints["email"])
                check_type(argname="argument sms", value=sms, expected_type=type_hints["sms"])
                check_type(argname="argument telephony", value=telephony, expected_type=type_hints["telephony"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if email is not None:
                self._values["email"] = email
            if sms is not None:
                self._values["sms"] = sms
            if telephony is not None:
                self._values["telephony"] = telephony

        @builtins.property
        def email(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.EmailChannelSubtypeConfigProperty"]]:
            '''The configuration of the email channel subtype.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-channelsubtypeconfig.html#cfn-connectcampaignsv2-campaign-channelsubtypeconfig-email
            '''
            result = self._values.get("email")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.EmailChannelSubtypeConfigProperty"]], result)

        @builtins.property
        def sms(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.SmsChannelSubtypeConfigProperty"]]:
            '''The configuration of the SMS channel subtype.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-channelsubtypeconfig.html#cfn-connectcampaignsv2-campaign-channelsubtypeconfig-sms
            '''
            result = self._values.get("sms")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.SmsChannelSubtypeConfigProperty"]], result)

        @builtins.property
        def telephony(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TelephonyChannelSubtypeConfigProperty"]]:
            '''The configuration of the telephony channel subtype.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-channelsubtypeconfig.html#cfn-connectcampaignsv2-campaign-channelsubtypeconfig-telephony
            '''
            result = self._values.get("telephony")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TelephonyChannelSubtypeConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ChannelSubtypeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.CommunicationLimitProperty",
        jsii_struct_bases=[],
        name_mapping={
            "frequency": "frequency",
            "max_count_per_recipient": "maxCountPerRecipient",
            "unit": "unit",
        },
    )
    class CommunicationLimitProperty:
        def __init__(
            self,
            *,
            frequency: jsii.Number,
            max_count_per_recipient: jsii.Number,
            unit: builtins.str,
        ) -> None:
            '''Contains information about a communication limit.

            :param frequency: The frequency of communication limit evaluation.
            :param max_count_per_recipient: The maximum outreaching count for each recipient.
            :param unit: The unit of communication limit evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-communicationlimit.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                communication_limit_property = connectcampaignsv2.CfnCampaign.CommunicationLimitProperty(
                    frequency=123,
                    max_count_per_recipient=123,
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7a4b2b207bce63b0696bef9d14a808bcf3bd9ae2746f645e72a80348100b732b)
                check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
                check_type(argname="argument max_count_per_recipient", value=max_count_per_recipient, expected_type=type_hints["max_count_per_recipient"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "frequency": frequency,
                "max_count_per_recipient": max_count_per_recipient,
                "unit": unit,
            }

        @builtins.property
        def frequency(self) -> jsii.Number:
            '''The frequency of communication limit evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-communicationlimit.html#cfn-connectcampaignsv2-campaign-communicationlimit-frequency
            '''
            result = self._values.get("frequency")
            assert result is not None, "Required property 'frequency' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max_count_per_recipient(self) -> jsii.Number:
            '''The maximum outreaching count for each recipient.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-communicationlimit.html#cfn-connectcampaignsv2-campaign-communicationlimit-maxcountperrecipient
            '''
            result = self._values.get("max_count_per_recipient")
            assert result is not None, "Required property 'max_count_per_recipient' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def unit(self) -> builtins.str:
            '''The unit of communication limit evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-communicationlimit.html#cfn-connectcampaignsv2-campaign-communicationlimit-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CommunicationLimitProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.CommunicationLimitsConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "all_channels_subtypes": "allChannelsSubtypes",
            "instance_limits_handling": "instanceLimitsHandling",
        },
    )
    class CommunicationLimitsConfigProperty:
        def __init__(
            self,
            *,
            all_channels_subtypes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.CommunicationLimitsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            instance_limits_handling: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains the communication limits configuration for an outbound campaign.

            :param all_channels_subtypes: The CommunicationLimits that apply to all channel subtypes defined in an outbound campaign.
            :param instance_limits_handling: Opt-in or Opt-out from instance-level limits.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-communicationlimitsconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                communication_limits_config_property = connectcampaignsv2.CfnCampaign.CommunicationLimitsConfigProperty(
                    all_channels_subtypes=connectcampaignsv2.CfnCampaign.CommunicationLimitsProperty(
                        communication_limit_list=[connectcampaignsv2.CfnCampaign.CommunicationLimitProperty(
                            frequency=123,
                            max_count_per_recipient=123,
                            unit="unit"
                        )]
                    ),
                    instance_limits_handling="instanceLimitsHandling"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5a5ca8627addc85a64908de980e86012a2ad9d04257fa86e81c4873e7a7d93be)
                check_type(argname="argument all_channels_subtypes", value=all_channels_subtypes, expected_type=type_hints["all_channels_subtypes"])
                check_type(argname="argument instance_limits_handling", value=instance_limits_handling, expected_type=type_hints["instance_limits_handling"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if all_channels_subtypes is not None:
                self._values["all_channels_subtypes"] = all_channels_subtypes
            if instance_limits_handling is not None:
                self._values["instance_limits_handling"] = instance_limits_handling

        @builtins.property
        def all_channels_subtypes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CommunicationLimitsProperty"]]:
            '''The CommunicationLimits that apply to all channel subtypes defined in an outbound campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-communicationlimitsconfig.html#cfn-connectcampaignsv2-campaign-communicationlimitsconfig-allchannelssubtypes
            '''
            result = self._values.get("all_channels_subtypes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CommunicationLimitsProperty"]], result)

        @builtins.property
        def instance_limits_handling(self) -> typing.Optional[builtins.str]:
            '''Opt-in or Opt-out from instance-level limits.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-communicationlimitsconfig.html#cfn-connectcampaignsv2-campaign-communicationlimitsconfig-instancelimitshandling
            '''
            result = self._values.get("instance_limits_handling")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CommunicationLimitsConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.CommunicationLimitsProperty",
        jsii_struct_bases=[],
        name_mapping={"communication_limit_list": "communicationLimitList"},
    )
    class CommunicationLimitsProperty:
        def __init__(
            self,
            *,
            communication_limit_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.CommunicationLimitProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Contains information about communication limits.

            :param communication_limit_list: The list of CommunicationLimits.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-communicationlimits.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                communication_limits_property = connectcampaignsv2.CfnCampaign.CommunicationLimitsProperty(
                    communication_limit_list=[connectcampaignsv2.CfnCampaign.CommunicationLimitProperty(
                        frequency=123,
                        max_count_per_recipient=123,
                        unit="unit"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__063b98187bfe10fef303f184ab9d1c8b1d41a5388eb6da2529b64fee8106550c)
                check_type(argname="argument communication_limit_list", value=communication_limit_list, expected_type=type_hints["communication_limit_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if communication_limit_list is not None:
                self._values["communication_limit_list"] = communication_limit_list

        @builtins.property
        def communication_limit_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CommunicationLimitProperty"]]]]:
            '''The list of CommunicationLimits.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-communicationlimits.html#cfn-connectcampaignsv2-campaign-communicationlimits-communicationlimitlist
            '''
            result = self._values.get("communication_limit_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.CommunicationLimitProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CommunicationLimitsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.CommunicationTimeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_time_zone_config": "localTimeZoneConfig",
            "email": "email",
            "sms": "sms",
            "telephony": "telephony",
        },
    )
    class CommunicationTimeConfigProperty:
        def __init__(
            self,
            *,
            local_time_zone_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.LocalTimeZoneConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            email: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.TimeWindowProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.TimeWindowProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            telephony: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.TimeWindowProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Communication time configuration for an outbound campaign.

            :param local_time_zone_config: The local timezone configuration.
            :param email: The communication time configuration for the email channel subtype.
            :param sms: The communication time configuration for the SMS channel subtype.
            :param telephony: The communication time configuration for the telephony channel subtype.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-communicationtimeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                communication_time_config_property = connectcampaignsv2.CfnCampaign.CommunicationTimeConfigProperty(
                    local_time_zone_config=connectcampaignsv2.CfnCampaign.LocalTimeZoneConfigProperty(
                        default_time_zone="defaultTimeZone",
                        local_time_zone_detection=["localTimeZoneDetection"]
                    ),
                
                    # the properties below are optional
                    email=connectcampaignsv2.CfnCampaign.TimeWindowProperty(
                        open_hours=connectcampaignsv2.CfnCampaign.OpenHoursProperty(
                            daily_hours=[connectcampaignsv2.CfnCampaign.DailyHourProperty(
                                key="key",
                                value=[connectcampaignsv2.CfnCampaign.TimeRangeProperty(
                                    end_time="endTime",
                                    start_time="startTime"
                                )]
                            )]
                        ),
                
                        # the properties below are optional
                        restricted_periods=connectcampaignsv2.CfnCampaign.RestrictedPeriodsProperty(
                            restricted_period_list=[connectcampaignsv2.CfnCampaign.RestrictedPeriodProperty(
                                end_date="endDate",
                                start_date="startDate",
                
                                # the properties below are optional
                                name="name"
                            )]
                        )
                    ),
                    sms=connectcampaignsv2.CfnCampaign.TimeWindowProperty(
                        open_hours=connectcampaignsv2.CfnCampaign.OpenHoursProperty(
                            daily_hours=[connectcampaignsv2.CfnCampaign.DailyHourProperty(
                                key="key",
                                value=[connectcampaignsv2.CfnCampaign.TimeRangeProperty(
                                    end_time="endTime",
                                    start_time="startTime"
                                )]
                            )]
                        ),
                
                        # the properties below are optional
                        restricted_periods=connectcampaignsv2.CfnCampaign.RestrictedPeriodsProperty(
                            restricted_period_list=[connectcampaignsv2.CfnCampaign.RestrictedPeriodProperty(
                                end_date="endDate",
                                start_date="startDate",
                
                                # the properties below are optional
                                name="name"
                            )]
                        )
                    ),
                    telephony=connectcampaignsv2.CfnCampaign.TimeWindowProperty(
                        open_hours=connectcampaignsv2.CfnCampaign.OpenHoursProperty(
                            daily_hours=[connectcampaignsv2.CfnCampaign.DailyHourProperty(
                                key="key",
                                value=[connectcampaignsv2.CfnCampaign.TimeRangeProperty(
                                    end_time="endTime",
                                    start_time="startTime"
                                )]
                            )]
                        ),
                
                        # the properties below are optional
                        restricted_periods=connectcampaignsv2.CfnCampaign.RestrictedPeriodsProperty(
                            restricted_period_list=[connectcampaignsv2.CfnCampaign.RestrictedPeriodProperty(
                                end_date="endDate",
                                start_date="startDate",
                
                                # the properties below are optional
                                name="name"
                            )]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3f2f2fbfc83eeac20d115af03889d47eb55561494e8fc488eeec30eb2e47752)
                check_type(argname="argument local_time_zone_config", value=local_time_zone_config, expected_type=type_hints["local_time_zone_config"])
                check_type(argname="argument email", value=email, expected_type=type_hints["email"])
                check_type(argname="argument sms", value=sms, expected_type=type_hints["sms"])
                check_type(argname="argument telephony", value=telephony, expected_type=type_hints["telephony"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "local_time_zone_config": local_time_zone_config,
            }
            if email is not None:
                self._values["email"] = email
            if sms is not None:
                self._values["sms"] = sms
            if telephony is not None:
                self._values["telephony"] = telephony

        @builtins.property
        def local_time_zone_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCampaign.LocalTimeZoneConfigProperty"]:
            '''The local timezone configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-communicationtimeconfig.html#cfn-connectcampaignsv2-campaign-communicationtimeconfig-localtimezoneconfig
            '''
            result = self._values.get("local_time_zone_config")
            assert result is not None, "Required property 'local_time_zone_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCampaign.LocalTimeZoneConfigProperty"], result)

        @builtins.property
        def email(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TimeWindowProperty"]]:
            '''The communication time configuration for the email channel subtype.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-communicationtimeconfig.html#cfn-connectcampaignsv2-campaign-communicationtimeconfig-email
            '''
            result = self._values.get("email")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TimeWindowProperty"]], result)

        @builtins.property
        def sms(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TimeWindowProperty"]]:
            '''The communication time configuration for the SMS channel subtype.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-communicationtimeconfig.html#cfn-connectcampaignsv2-campaign-communicationtimeconfig-sms
            '''
            result = self._values.get("sms")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TimeWindowProperty"]], result)

        @builtins.property
        def telephony(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TimeWindowProperty"]]:
            '''The communication time configuration for the telephony channel subtype.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-communicationtimeconfig.html#cfn-connectcampaignsv2-campaign-communicationtimeconfig-telephony
            '''
            result = self._values.get("telephony")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TimeWindowProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CommunicationTimeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.DailyHourProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class DailyHourProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.TimeRangeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The daily hours configuration.

            :param key: The key for DailyHour.
            :param value: The value for DailyHour.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-dailyhour.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                daily_hour_property = connectcampaignsv2.CfnCampaign.DailyHourProperty(
                    key="key",
                    value=[connectcampaignsv2.CfnCampaign.TimeRangeProperty(
                        end_time="endTime",
                        start_time="startTime"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__35e6acb6b0c0424f51f610f7f0a2abd4c482306c13db09f191eae079682c9f5c)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The key for DailyHour.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-dailyhour.html#cfn-connectcampaignsv2-campaign-dailyhour-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TimeRangeProperty"]]]]:
            '''The value for DailyHour.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-dailyhour.html#cfn-connectcampaignsv2-campaign-dailyhour-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TimeRangeProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DailyHourProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.EmailChannelSubtypeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_outbound_config": "defaultOutboundConfig",
            "outbound_mode": "outboundMode",
            "capacity": "capacity",
        },
    )
    class EmailChannelSubtypeConfigProperty:
        def __init__(
            self,
            *,
            default_outbound_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.EmailOutboundConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            outbound_mode: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.EmailOutboundModeProperty", typing.Dict[builtins.str, typing.Any]]],
            capacity: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The configuration for the email channel subtype.

            :param default_outbound_config: The default email outbound configuration of an outbound campaign.
            :param outbound_mode: The outbound mode for email of an outbound campaign.
            :param capacity: The allocation of email capacity between multiple running outbound campaigns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-emailchannelsubtypeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                # agentless_config: Any
                
                email_channel_subtype_config_property = connectcampaignsv2.CfnCampaign.EmailChannelSubtypeConfigProperty(
                    default_outbound_config=connectcampaignsv2.CfnCampaign.EmailOutboundConfigProperty(
                        connect_source_email_address="connectSourceEmailAddress",
                        wisdom_template_arn="wisdomTemplateArn",
                
                        # the properties below are optional
                        source_email_address_display_name="sourceEmailAddressDisplayName"
                    ),
                    outbound_mode=connectcampaignsv2.CfnCampaign.EmailOutboundModeProperty(
                        agentless_config=agentless_config
                    ),
                
                    # the properties below are optional
                    capacity=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ff9274643abefe2ecd29ff0322f3b49479b574757b18fe4f15225f01a19ef7ea)
                check_type(argname="argument default_outbound_config", value=default_outbound_config, expected_type=type_hints["default_outbound_config"])
                check_type(argname="argument outbound_mode", value=outbound_mode, expected_type=type_hints["outbound_mode"])
                check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "default_outbound_config": default_outbound_config,
                "outbound_mode": outbound_mode,
            }
            if capacity is not None:
                self._values["capacity"] = capacity

        @builtins.property
        def default_outbound_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCampaign.EmailOutboundConfigProperty"]:
            '''The default email outbound configuration of an outbound campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-emailchannelsubtypeconfig.html#cfn-connectcampaignsv2-campaign-emailchannelsubtypeconfig-defaultoutboundconfig
            '''
            result = self._values.get("default_outbound_config")
            assert result is not None, "Required property 'default_outbound_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCampaign.EmailOutboundConfigProperty"], result)

        @builtins.property
        def outbound_mode(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCampaign.EmailOutboundModeProperty"]:
            '''The outbound mode for email of an outbound campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-emailchannelsubtypeconfig.html#cfn-connectcampaignsv2-campaign-emailchannelsubtypeconfig-outboundmode
            '''
            result = self._values.get("outbound_mode")
            assert result is not None, "Required property 'outbound_mode' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCampaign.EmailOutboundModeProperty"], result)

        @builtins.property
        def capacity(self) -> typing.Optional[jsii.Number]:
            '''The allocation of email capacity between multiple running outbound campaigns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-emailchannelsubtypeconfig.html#cfn-connectcampaignsv2-campaign-emailchannelsubtypeconfig-capacity
            '''
            result = self._values.get("capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmailChannelSubtypeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.EmailOutboundConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connect_source_email_address": "connectSourceEmailAddress",
            "wisdom_template_arn": "wisdomTemplateArn",
            "source_email_address_display_name": "sourceEmailAddressDisplayName",
        },
    )
    class EmailOutboundConfigProperty:
        def __init__(
            self,
            *,
            connect_source_email_address: builtins.str,
            wisdom_template_arn: builtins.str,
            source_email_address_display_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The outbound configuration for email.

            :param connect_source_email_address: The Amazon Connect source email address.
            :param wisdom_template_arn: The Amazon Resource Name (ARN) of the Amazon Q in Connect template.
            :param source_email_address_display_name: The display name for the Amazon Connect source email address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-emailoutboundconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                email_outbound_config_property = connectcampaignsv2.CfnCampaign.EmailOutboundConfigProperty(
                    connect_source_email_address="connectSourceEmailAddress",
                    wisdom_template_arn="wisdomTemplateArn",
                
                    # the properties below are optional
                    source_email_address_display_name="sourceEmailAddressDisplayName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7b2c45c48dd3f984623dbcc344a83d9c26e929cd6947cc9f868ffe1b4d0341d1)
                check_type(argname="argument connect_source_email_address", value=connect_source_email_address, expected_type=type_hints["connect_source_email_address"])
                check_type(argname="argument wisdom_template_arn", value=wisdom_template_arn, expected_type=type_hints["wisdom_template_arn"])
                check_type(argname="argument source_email_address_display_name", value=source_email_address_display_name, expected_type=type_hints["source_email_address_display_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connect_source_email_address": connect_source_email_address,
                "wisdom_template_arn": wisdom_template_arn,
            }
            if source_email_address_display_name is not None:
                self._values["source_email_address_display_name"] = source_email_address_display_name

        @builtins.property
        def connect_source_email_address(self) -> builtins.str:
            '''The Amazon Connect source email address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-emailoutboundconfig.html#cfn-connectcampaignsv2-campaign-emailoutboundconfig-connectsourceemailaddress
            '''
            result = self._values.get("connect_source_email_address")
            assert result is not None, "Required property 'connect_source_email_address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def wisdom_template_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon Q in Connect template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-emailoutboundconfig.html#cfn-connectcampaignsv2-campaign-emailoutboundconfig-wisdomtemplatearn
            '''
            result = self._values.get("wisdom_template_arn")
            assert result is not None, "Required property 'wisdom_template_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_email_address_display_name(self) -> typing.Optional[builtins.str]:
            '''The display name for the Amazon Connect source email address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-emailoutboundconfig.html#cfn-connectcampaignsv2-campaign-emailoutboundconfig-sourceemailaddressdisplayname
            '''
            result = self._values.get("source_email_address_display_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmailOutboundConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.EmailOutboundModeProperty",
        jsii_struct_bases=[],
        name_mapping={"agentless_config": "agentlessConfig"},
    )
    class EmailOutboundModeProperty:
        def __init__(self, *, agentless_config: typing.Any = None) -> None:
            '''Contains information about email outbound mode.

            :param agentless_config: The agentless outbound mode configuration for email.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-emailoutboundmode.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                # agentless_config: Any
                
                email_outbound_mode_property = connectcampaignsv2.CfnCampaign.EmailOutboundModeProperty(
                    agentless_config=agentless_config
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__016ccd411110b9f8510f586be6901ef480857575d80a38ed7c7e81cae2ad5e94)
                check_type(argname="argument agentless_config", value=agentless_config, expected_type=type_hints["agentless_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if agentless_config is not None:
                self._values["agentless_config"] = agentless_config

        @builtins.property
        def agentless_config(self) -> typing.Any:
            '''The agentless outbound mode configuration for email.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-emailoutboundmode.html#cfn-connectcampaignsv2-campaign-emailoutboundmode-agentlessconfig
            '''
            result = self._values.get("agentless_config")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmailOutboundModeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.EventTriggerProperty",
        jsii_struct_bases=[],
        name_mapping={"customer_profiles_domain_arn": "customerProfilesDomainArn"},
    )
    class EventTriggerProperty:
        def __init__(
            self,
            *,
            customer_profiles_domain_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The event trigger of the campaign.

            :param customer_profiles_domain_arn: The Amazon Resource Name (ARN) of the Customer Profiles domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-eventtrigger.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                event_trigger_property = connectcampaignsv2.CfnCampaign.EventTriggerProperty(
                    customer_profiles_domain_arn="customerProfilesDomainArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c5c63db70e1b49ff8c093902378da25d9e1f34010626b2eeb9d25d6da292eb2c)
                check_type(argname="argument customer_profiles_domain_arn", value=customer_profiles_domain_arn, expected_type=type_hints["customer_profiles_domain_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if customer_profiles_domain_arn is not None:
                self._values["customer_profiles_domain_arn"] = customer_profiles_domain_arn

        @builtins.property
        def customer_profiles_domain_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Customer Profiles domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-eventtrigger.html#cfn-connectcampaignsv2-campaign-eventtrigger-customerprofilesdomainarn
            '''
            result = self._values.get("customer_profiles_domain_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventTriggerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.LocalTimeZoneConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_time_zone": "defaultTimeZone",
            "local_time_zone_detection": "localTimeZoneDetection",
        },
    )
    class LocalTimeZoneConfigProperty:
        def __init__(
            self,
            *,
            default_time_zone: typing.Optional[builtins.str] = None,
            local_time_zone_detection: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The configuration of timezone for recipient.

            :param default_time_zone: The timezone to use for all recipients.
            :param local_time_zone_detection: Detects methods for the recipient's timezone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-localtimezoneconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                local_time_zone_config_property = connectcampaignsv2.CfnCampaign.LocalTimeZoneConfigProperty(
                    default_time_zone="defaultTimeZone",
                    local_time_zone_detection=["localTimeZoneDetection"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c03234f264094d68479c6e1cf3801d50627e839a73b2f0cbeb95c82522f9a66e)
                check_type(argname="argument default_time_zone", value=default_time_zone, expected_type=type_hints["default_time_zone"])
                check_type(argname="argument local_time_zone_detection", value=local_time_zone_detection, expected_type=type_hints["local_time_zone_detection"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if default_time_zone is not None:
                self._values["default_time_zone"] = default_time_zone
            if local_time_zone_detection is not None:
                self._values["local_time_zone_detection"] = local_time_zone_detection

        @builtins.property
        def default_time_zone(self) -> typing.Optional[builtins.str]:
            '''The timezone to use for all recipients.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-localtimezoneconfig.html#cfn-connectcampaignsv2-campaign-localtimezoneconfig-defaulttimezone
            '''
            result = self._values.get("default_time_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def local_time_zone_detection(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''Detects methods for the recipient's timezone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-localtimezoneconfig.html#cfn-connectcampaignsv2-campaign-localtimezoneconfig-localtimezonedetection
            '''
            result = self._values.get("local_time_zone_detection")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocalTimeZoneConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.OpenHoursProperty",
        jsii_struct_bases=[],
        name_mapping={"daily_hours": "dailyHours"},
    )
    class OpenHoursProperty:
        def __init__(
            self,
            *,
            daily_hours: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.DailyHourProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Contains information about open hours.

            :param daily_hours: The daily hours configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-openhours.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                open_hours_property = connectcampaignsv2.CfnCampaign.OpenHoursProperty(
                    daily_hours=[connectcampaignsv2.CfnCampaign.DailyHourProperty(
                        key="key",
                        value=[connectcampaignsv2.CfnCampaign.TimeRangeProperty(
                            end_time="endTime",
                            start_time="startTime"
                        )]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9a34ace5bfcc35c52d69e6dd7ef3c38abf4d254290d5470f5104e49f2d115b39)
                check_type(argname="argument daily_hours", value=daily_hours, expected_type=type_hints["daily_hours"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "daily_hours": daily_hours,
            }

        @builtins.property
        def daily_hours(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.DailyHourProperty"]]]:
            '''The daily hours configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-openhours.html#cfn-connectcampaignsv2-campaign-openhours-dailyhours
            '''
            result = self._values.get("daily_hours")
            assert result is not None, "Required property 'daily_hours' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.DailyHourProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenHoursProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.PredictiveConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"bandwidth_allocation": "bandwidthAllocation"},
    )
    class PredictiveConfigProperty:
        def __init__(self, *, bandwidth_allocation: jsii.Number) -> None:
            '''Contains predictive outbound mode configuration.

            :param bandwidth_allocation: Bandwidth allocation for the predictive outbound mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-predictiveconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                predictive_config_property = connectcampaignsv2.CfnCampaign.PredictiveConfigProperty(
                    bandwidth_allocation=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a27014c548ec13c6446b07f461be7ed43556a2cb77433713ef38f272a14459fd)
                check_type(argname="argument bandwidth_allocation", value=bandwidth_allocation, expected_type=type_hints["bandwidth_allocation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bandwidth_allocation": bandwidth_allocation,
            }

        @builtins.property
        def bandwidth_allocation(self) -> jsii.Number:
            '''Bandwidth allocation for the predictive outbound mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-predictiveconfig.html#cfn-connectcampaignsv2-campaign-predictiveconfig-bandwidthallocation
            '''
            result = self._values.get("bandwidth_allocation")
            assert result is not None, "Required property 'bandwidth_allocation' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PredictiveConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.ProgressiveConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"bandwidth_allocation": "bandwidthAllocation"},
    )
    class ProgressiveConfigProperty:
        def __init__(self, *, bandwidth_allocation: jsii.Number) -> None:
            '''Contains the progressive outbound mode configuration.

            :param bandwidth_allocation: Bandwidth allocation for the progressive outbound mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-progressiveconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                progressive_config_property = connectcampaignsv2.CfnCampaign.ProgressiveConfigProperty(
                    bandwidth_allocation=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6504302e8d20b62038efca8c5dfe9bbddfc485cc88de44f995d599a39017ddbe)
                check_type(argname="argument bandwidth_allocation", value=bandwidth_allocation, expected_type=type_hints["bandwidth_allocation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bandwidth_allocation": bandwidth_allocation,
            }

        @builtins.property
        def bandwidth_allocation(self) -> jsii.Number:
            '''Bandwidth allocation for the progressive outbound mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-progressiveconfig.html#cfn-connectcampaignsv2-campaign-progressiveconfig-bandwidthallocation
            '''
            result = self._values.get("bandwidth_allocation")
            assert result is not None, "Required property 'bandwidth_allocation' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProgressiveConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.RestrictedPeriodProperty",
        jsii_struct_bases=[],
        name_mapping={
            "end_date": "endDate",
            "start_date": "startDate",
            "name": "name",
        },
    )
    class RestrictedPeriodProperty:
        def __init__(
            self,
            *,
            end_date: builtins.str,
            start_date: builtins.str,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about a restricted period.

            :param end_date: The end date of the restricted period.
            :param start_date: The start date of the restricted period.
            :param name: The name of the restricted period.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-restrictedperiod.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                restricted_period_property = connectcampaignsv2.CfnCampaign.RestrictedPeriodProperty(
                    end_date="endDate",
                    start_date="startDate",
                
                    # the properties below are optional
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4f2a36f6fa12d741457cf955ef79fa845b855e1b170b7ea44a157f8f120f9b67)
                check_type(argname="argument end_date", value=end_date, expected_type=type_hints["end_date"])
                check_type(argname="argument start_date", value=start_date, expected_type=type_hints["start_date"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "end_date": end_date,
                "start_date": start_date,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def end_date(self) -> builtins.str:
            '''The end date of the restricted period.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-restrictedperiod.html#cfn-connectcampaignsv2-campaign-restrictedperiod-enddate
            '''
            result = self._values.get("end_date")
            assert result is not None, "Required property 'end_date' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_date(self) -> builtins.str:
            '''The start date of the restricted period.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-restrictedperiod.html#cfn-connectcampaignsv2-campaign-restrictedperiod-startdate
            '''
            result = self._values.get("start_date")
            assert result is not None, "Required property 'start_date' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the restricted period.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-restrictedperiod.html#cfn-connectcampaignsv2-campaign-restrictedperiod-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RestrictedPeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.RestrictedPeriodsProperty",
        jsii_struct_bases=[],
        name_mapping={"restricted_period_list": "restrictedPeriodList"},
    )
    class RestrictedPeriodsProperty:
        def __init__(
            self,
            *,
            restricted_period_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.RestrictedPeriodProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Contains information about restricted periods.

            :param restricted_period_list: The restricted period list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-restrictedperiods.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                restricted_periods_property = connectcampaignsv2.CfnCampaign.RestrictedPeriodsProperty(
                    restricted_period_list=[connectcampaignsv2.CfnCampaign.RestrictedPeriodProperty(
                        end_date="endDate",
                        start_date="startDate",
                
                        # the properties below are optional
                        name="name"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f30a61789fda85a4bb2aa71fc64566047bab737aa5220ee60d91e1e08d9a84dd)
                check_type(argname="argument restricted_period_list", value=restricted_period_list, expected_type=type_hints["restricted_period_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "restricted_period_list": restricted_period_list,
            }

        @builtins.property
        def restricted_period_list(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.RestrictedPeriodProperty"]]]:
            '''The restricted period list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-restrictedperiods.html#cfn-connectcampaignsv2-campaign-restrictedperiods-restrictedperiodlist
            '''
            result = self._values.get("restricted_period_list")
            assert result is not None, "Required property 'restricted_period_list' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.RestrictedPeriodProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RestrictedPeriodsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "end_time": "endTime",
            "start_time": "startTime",
            "refresh_frequency": "refreshFrequency",
        },
    )
    class ScheduleProperty:
        def __init__(
            self,
            *,
            end_time: builtins.str,
            start_time: builtins.str,
            refresh_frequency: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains the schedule configuration.

            :param end_time: The end time of the schedule in UTC.
            :param start_time: The start time of the schedule in UTC.
            :param refresh_frequency: The refresh frequency of the campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-schedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                schedule_property = connectcampaignsv2.CfnCampaign.ScheduleProperty(
                    end_time="endTime",
                    start_time="startTime",
                
                    # the properties below are optional
                    refresh_frequency="refreshFrequency"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b6a4567c8e5f09b06087beafe0e729f0ae431ebcefbe37d716e547d333cb24b)
                check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
                check_type(argname="argument refresh_frequency", value=refresh_frequency, expected_type=type_hints["refresh_frequency"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "end_time": end_time,
                "start_time": start_time,
            }
            if refresh_frequency is not None:
                self._values["refresh_frequency"] = refresh_frequency

        @builtins.property
        def end_time(self) -> builtins.str:
            '''The end time of the schedule in UTC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-schedule.html#cfn-connectcampaignsv2-campaign-schedule-endtime
            '''
            result = self._values.get("end_time")
            assert result is not None, "Required property 'end_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_time(self) -> builtins.str:
            '''The start time of the schedule in UTC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-schedule.html#cfn-connectcampaignsv2-campaign-schedule-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def refresh_frequency(self) -> typing.Optional[builtins.str]:
            '''The refresh frequency of the campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-schedule.html#cfn-connectcampaignsv2-campaign-schedule-refreshfrequency
            '''
            result = self._values.get("refresh_frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.SmsChannelSubtypeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_outbound_config": "defaultOutboundConfig",
            "outbound_mode": "outboundMode",
            "capacity": "capacity",
        },
    )
    class SmsChannelSubtypeConfigProperty:
        def __init__(
            self,
            *,
            default_outbound_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.SmsOutboundConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            outbound_mode: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.SmsOutboundModeProperty", typing.Dict[builtins.str, typing.Any]]],
            capacity: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The configuration for the SMS channel subtype.

            :param default_outbound_config: The default SMS outbound configuration of an outbound campaign.
            :param outbound_mode: The outbound mode of SMS for an outbound campaign.
            :param capacity: The allocation of SMS capacity between multiple running outbound campaigns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-smschannelsubtypeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                # agentless_config: Any
                
                sms_channel_subtype_config_property = connectcampaignsv2.CfnCampaign.SmsChannelSubtypeConfigProperty(
                    default_outbound_config=connectcampaignsv2.CfnCampaign.SmsOutboundConfigProperty(
                        connect_source_phone_number_arn="connectSourcePhoneNumberArn",
                        wisdom_template_arn="wisdomTemplateArn"
                    ),
                    outbound_mode=connectcampaignsv2.CfnCampaign.SmsOutboundModeProperty(
                        agentless_config=agentless_config
                    ),
                
                    # the properties below are optional
                    capacity=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b0d42ae0232d954af9167d51954642098f71dd226d554f1b2fab39b2c46726ee)
                check_type(argname="argument default_outbound_config", value=default_outbound_config, expected_type=type_hints["default_outbound_config"])
                check_type(argname="argument outbound_mode", value=outbound_mode, expected_type=type_hints["outbound_mode"])
                check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "default_outbound_config": default_outbound_config,
                "outbound_mode": outbound_mode,
            }
            if capacity is not None:
                self._values["capacity"] = capacity

        @builtins.property
        def default_outbound_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCampaign.SmsOutboundConfigProperty"]:
            '''The default SMS outbound configuration of an outbound campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-smschannelsubtypeconfig.html#cfn-connectcampaignsv2-campaign-smschannelsubtypeconfig-defaultoutboundconfig
            '''
            result = self._values.get("default_outbound_config")
            assert result is not None, "Required property 'default_outbound_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCampaign.SmsOutboundConfigProperty"], result)

        @builtins.property
        def outbound_mode(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCampaign.SmsOutboundModeProperty"]:
            '''The outbound mode of SMS for an outbound campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-smschannelsubtypeconfig.html#cfn-connectcampaignsv2-campaign-smschannelsubtypeconfig-outboundmode
            '''
            result = self._values.get("outbound_mode")
            assert result is not None, "Required property 'outbound_mode' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCampaign.SmsOutboundModeProperty"], result)

        @builtins.property
        def capacity(self) -> typing.Optional[jsii.Number]:
            '''The allocation of SMS capacity between multiple running outbound campaigns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-smschannelsubtypeconfig.html#cfn-connectcampaignsv2-campaign-smschannelsubtypeconfig-capacity
            '''
            result = self._values.get("capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SmsChannelSubtypeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.SmsOutboundConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connect_source_phone_number_arn": "connectSourcePhoneNumberArn",
            "wisdom_template_arn": "wisdomTemplateArn",
        },
    )
    class SmsOutboundConfigProperty:
        def __init__(
            self,
            *,
            connect_source_phone_number_arn: builtins.str,
            wisdom_template_arn: builtins.str,
        ) -> None:
            '''The outbound configuration for SMS.

            :param connect_source_phone_number_arn: The Amazon Resource Name (ARN) of the Amazon Connect source SMS phone number.
            :param wisdom_template_arn: The Amazon Resource Name (ARN) of the Amazon Q in Connect template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-smsoutboundconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                sms_outbound_config_property = connectcampaignsv2.CfnCampaign.SmsOutboundConfigProperty(
                    connect_source_phone_number_arn="connectSourcePhoneNumberArn",
                    wisdom_template_arn="wisdomTemplateArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__874dedca8982d2204aa531b3a554ca0a994b9ce64825e83b31a7a7563d08f262)
                check_type(argname="argument connect_source_phone_number_arn", value=connect_source_phone_number_arn, expected_type=type_hints["connect_source_phone_number_arn"])
                check_type(argname="argument wisdom_template_arn", value=wisdom_template_arn, expected_type=type_hints["wisdom_template_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connect_source_phone_number_arn": connect_source_phone_number_arn,
                "wisdom_template_arn": wisdom_template_arn,
            }

        @builtins.property
        def connect_source_phone_number_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon Connect source SMS phone number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-smsoutboundconfig.html#cfn-connectcampaignsv2-campaign-smsoutboundconfig-connectsourcephonenumberarn
            '''
            result = self._values.get("connect_source_phone_number_arn")
            assert result is not None, "Required property 'connect_source_phone_number_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def wisdom_template_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon Q in Connect template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-smsoutboundconfig.html#cfn-connectcampaignsv2-campaign-smsoutboundconfig-wisdomtemplatearn
            '''
            result = self._values.get("wisdom_template_arn")
            assert result is not None, "Required property 'wisdom_template_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SmsOutboundConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.SmsOutboundModeProperty",
        jsii_struct_bases=[],
        name_mapping={"agentless_config": "agentlessConfig"},
    )
    class SmsOutboundModeProperty:
        def __init__(self, *, agentless_config: typing.Any = None) -> None:
            '''Contains information about the SMS outbound mode.

            :param agentless_config: Contains agentless outbound mode configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-smsoutboundmode.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                # agentless_config: Any
                
                sms_outbound_mode_property = connectcampaignsv2.CfnCampaign.SmsOutboundModeProperty(
                    agentless_config=agentless_config
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__67957d238e403659f29fa8bf2db2164d694d327a14b84df3d61c10b2b3afd954)
                check_type(argname="argument agentless_config", value=agentless_config, expected_type=type_hints["agentless_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if agentless_config is not None:
                self._values["agentless_config"] = agentless_config

        @builtins.property
        def agentless_config(self) -> typing.Any:
            '''Contains agentless outbound mode configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-smsoutboundmode.html#cfn-connectcampaignsv2-campaign-smsoutboundmode-agentlessconfig
            '''
            result = self._values.get("agentless_config")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SmsOutboundModeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "customer_profiles_segment_arn": "customerProfilesSegmentArn",
            "event_trigger": "eventTrigger",
        },
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            customer_profiles_segment_arn: typing.Optional[builtins.str] = None,
            event_trigger: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.EventTriggerProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains source configuration.

            :param customer_profiles_segment_arn: The Amazon Resource Name (ARN) of the Customer Profiles segment.
            :param event_trigger: The event trigger of the campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-source.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                source_property = connectcampaignsv2.CfnCampaign.SourceProperty(
                    customer_profiles_segment_arn="customerProfilesSegmentArn",
                    event_trigger=connectcampaignsv2.CfnCampaign.EventTriggerProperty(
                        customer_profiles_domain_arn="customerProfilesDomainArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__48dbe2dd9c0147e5b2bea173aba4c056f8a83ba308e89c654331a4a77f46636d)
                check_type(argname="argument customer_profiles_segment_arn", value=customer_profiles_segment_arn, expected_type=type_hints["customer_profiles_segment_arn"])
                check_type(argname="argument event_trigger", value=event_trigger, expected_type=type_hints["event_trigger"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if customer_profiles_segment_arn is not None:
                self._values["customer_profiles_segment_arn"] = customer_profiles_segment_arn
            if event_trigger is not None:
                self._values["event_trigger"] = event_trigger

        @builtins.property
        def customer_profiles_segment_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Customer Profiles segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-source.html#cfn-connectcampaignsv2-campaign-source-customerprofilessegmentarn
            '''
            result = self._values.get("customer_profiles_segment_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def event_trigger(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.EventTriggerProperty"]]:
            '''The event trigger of the campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-source.html#cfn-connectcampaignsv2-campaign-source-eventtrigger
            '''
            result = self._values.get("event_trigger")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.EventTriggerProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.TelephonyChannelSubtypeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_outbound_config": "defaultOutboundConfig",
            "outbound_mode": "outboundMode",
            "capacity": "capacity",
            "connect_queue_id": "connectQueueId",
        },
    )
    class TelephonyChannelSubtypeConfigProperty:
        def __init__(
            self,
            *,
            default_outbound_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.TelephonyOutboundConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            outbound_mode: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.TelephonyOutboundModeProperty", typing.Dict[builtins.str, typing.Any]]],
            capacity: typing.Optional[jsii.Number] = None,
            connect_queue_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for the telephony channel subtype.

            :param default_outbound_config: The default telephony outbound configuration of an outbound campaign.
            :param outbound_mode: The outbound mode of telephony for an outbound campaign.
            :param capacity: The allocation of telephony capacity between multiple running outbound campaigns.
            :param connect_queue_id: The identifier of the Amazon Connect queue associated with telephony outbound requests of an outbound campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-telephonychannelsubtypeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                # agentless_config: Any
                
                telephony_channel_subtype_config_property = connectcampaignsv2.CfnCampaign.TelephonyChannelSubtypeConfigProperty(
                    default_outbound_config=connectcampaignsv2.CfnCampaign.TelephonyOutboundConfigProperty(
                        connect_contact_flow_id="connectContactFlowId",
                
                        # the properties below are optional
                        answer_machine_detection_config=connectcampaignsv2.CfnCampaign.AnswerMachineDetectionConfigProperty(
                            enable_answer_machine_detection=False,
                
                            # the properties below are optional
                            await_answer_machine_prompt=False
                        ),
                        connect_source_phone_number="connectSourcePhoneNumber"
                    ),
                    outbound_mode=connectcampaignsv2.CfnCampaign.TelephonyOutboundModeProperty(
                        agentless_config=agentless_config,
                        predictive_config=connectcampaignsv2.CfnCampaign.PredictiveConfigProperty(
                            bandwidth_allocation=123
                        ),
                        progressive_config=connectcampaignsv2.CfnCampaign.ProgressiveConfigProperty(
                            bandwidth_allocation=123
                        )
                    ),
                
                    # the properties below are optional
                    capacity=123,
                    connect_queue_id="connectQueueId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__19c776b12e28122b49a867e83503b94bf286d46879c32085c60a17f0213dc948)
                check_type(argname="argument default_outbound_config", value=default_outbound_config, expected_type=type_hints["default_outbound_config"])
                check_type(argname="argument outbound_mode", value=outbound_mode, expected_type=type_hints["outbound_mode"])
                check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
                check_type(argname="argument connect_queue_id", value=connect_queue_id, expected_type=type_hints["connect_queue_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "default_outbound_config": default_outbound_config,
                "outbound_mode": outbound_mode,
            }
            if capacity is not None:
                self._values["capacity"] = capacity
            if connect_queue_id is not None:
                self._values["connect_queue_id"] = connect_queue_id

        @builtins.property
        def default_outbound_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCampaign.TelephonyOutboundConfigProperty"]:
            '''The default telephony outbound configuration of an outbound campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-telephonychannelsubtypeconfig.html#cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-defaultoutboundconfig
            '''
            result = self._values.get("default_outbound_config")
            assert result is not None, "Required property 'default_outbound_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCampaign.TelephonyOutboundConfigProperty"], result)

        @builtins.property
        def outbound_mode(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCampaign.TelephonyOutboundModeProperty"]:
            '''The outbound mode of telephony for an outbound campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-telephonychannelsubtypeconfig.html#cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-outboundmode
            '''
            result = self._values.get("outbound_mode")
            assert result is not None, "Required property 'outbound_mode' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCampaign.TelephonyOutboundModeProperty"], result)

        @builtins.property
        def capacity(self) -> typing.Optional[jsii.Number]:
            '''The allocation of telephony capacity between multiple running outbound campaigns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-telephonychannelsubtypeconfig.html#cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-capacity
            '''
            result = self._values.get("capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def connect_queue_id(self) -> typing.Optional[builtins.str]:
            '''The identifier of the Amazon Connect queue associated with telephony outbound requests of an outbound campaign.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-telephonychannelsubtypeconfig.html#cfn-connectcampaignsv2-campaign-telephonychannelsubtypeconfig-connectqueueid
            '''
            result = self._values.get("connect_queue_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelephonyChannelSubtypeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.TelephonyOutboundConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connect_contact_flow_id": "connectContactFlowId",
            "answer_machine_detection_config": "answerMachineDetectionConfig",
            "connect_source_phone_number": "connectSourcePhoneNumber",
        },
    )
    class TelephonyOutboundConfigProperty:
        def __init__(
            self,
            *,
            connect_contact_flow_id: builtins.str,
            answer_machine_detection_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.AnswerMachineDetectionConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            connect_source_phone_number: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The outbound configuration for telephony.

            :param connect_contact_flow_id: The identifier of the published Amazon Connect contact flow.
            :param answer_machine_detection_config: The answering machine detection configuration.
            :param connect_source_phone_number: The Amazon Connect source phone number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-telephonyoutboundconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                telephony_outbound_config_property = connectcampaignsv2.CfnCampaign.TelephonyOutboundConfigProperty(
                    connect_contact_flow_id="connectContactFlowId",
                
                    # the properties below are optional
                    answer_machine_detection_config=connectcampaignsv2.CfnCampaign.AnswerMachineDetectionConfigProperty(
                        enable_answer_machine_detection=False,
                
                        # the properties below are optional
                        await_answer_machine_prompt=False
                    ),
                    connect_source_phone_number="connectSourcePhoneNumber"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2751a1c01ea2bfaf5fe6806fe1a585daea66baf82d5fe0a4cec77a9b592d901a)
                check_type(argname="argument connect_contact_flow_id", value=connect_contact_flow_id, expected_type=type_hints["connect_contact_flow_id"])
                check_type(argname="argument answer_machine_detection_config", value=answer_machine_detection_config, expected_type=type_hints["answer_machine_detection_config"])
                check_type(argname="argument connect_source_phone_number", value=connect_source_phone_number, expected_type=type_hints["connect_source_phone_number"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connect_contact_flow_id": connect_contact_flow_id,
            }
            if answer_machine_detection_config is not None:
                self._values["answer_machine_detection_config"] = answer_machine_detection_config
            if connect_source_phone_number is not None:
                self._values["connect_source_phone_number"] = connect_source_phone_number

        @builtins.property
        def connect_contact_flow_id(self) -> builtins.str:
            '''The identifier of the published Amazon Connect contact flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-telephonyoutboundconfig.html#cfn-connectcampaignsv2-campaign-telephonyoutboundconfig-connectcontactflowid
            '''
            result = self._values.get("connect_contact_flow_id")
            assert result is not None, "Required property 'connect_contact_flow_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def answer_machine_detection_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.AnswerMachineDetectionConfigProperty"]]:
            '''The answering machine detection configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-telephonyoutboundconfig.html#cfn-connectcampaignsv2-campaign-telephonyoutboundconfig-answermachinedetectionconfig
            '''
            result = self._values.get("answer_machine_detection_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.AnswerMachineDetectionConfigProperty"]], result)

        @builtins.property
        def connect_source_phone_number(self) -> typing.Optional[builtins.str]:
            '''The Amazon Connect source phone number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-telephonyoutboundconfig.html#cfn-connectcampaignsv2-campaign-telephonyoutboundconfig-connectsourcephonenumber
            '''
            result = self._values.get("connect_source_phone_number")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelephonyOutboundConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.TelephonyOutboundModeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "agentless_config": "agentlessConfig",
            "predictive_config": "predictiveConfig",
            "progressive_config": "progressiveConfig",
        },
    )
    class TelephonyOutboundModeProperty:
        def __init__(
            self,
            *,
            agentless_config: typing.Any = None,
            predictive_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.PredictiveConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            progressive_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.ProgressiveConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about telephony outbound mode.

            :param agentless_config: The agentless outbound mode configuration for telephony.
            :param predictive_config: Contains predictive outbound mode configuration.
            :param progressive_config: Contains progressive telephony outbound mode configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-telephonyoutboundmode.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                # agentless_config: Any
                
                telephony_outbound_mode_property = connectcampaignsv2.CfnCampaign.TelephonyOutboundModeProperty(
                    agentless_config=agentless_config,
                    predictive_config=connectcampaignsv2.CfnCampaign.PredictiveConfigProperty(
                        bandwidth_allocation=123
                    ),
                    progressive_config=connectcampaignsv2.CfnCampaign.ProgressiveConfigProperty(
                        bandwidth_allocation=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7582ea451819f82369b8beb09bc8c872c5424040d69392d7bc3ab56ee8813053)
                check_type(argname="argument agentless_config", value=agentless_config, expected_type=type_hints["agentless_config"])
                check_type(argname="argument predictive_config", value=predictive_config, expected_type=type_hints["predictive_config"])
                check_type(argname="argument progressive_config", value=progressive_config, expected_type=type_hints["progressive_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if agentless_config is not None:
                self._values["agentless_config"] = agentless_config
            if predictive_config is not None:
                self._values["predictive_config"] = predictive_config
            if progressive_config is not None:
                self._values["progressive_config"] = progressive_config

        @builtins.property
        def agentless_config(self) -> typing.Any:
            '''The agentless outbound mode configuration for telephony.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-telephonyoutboundmode.html#cfn-connectcampaignsv2-campaign-telephonyoutboundmode-agentlessconfig
            '''
            result = self._values.get("agentless_config")
            return typing.cast(typing.Any, result)

        @builtins.property
        def predictive_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.PredictiveConfigProperty"]]:
            '''Contains predictive outbound mode configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-telephonyoutboundmode.html#cfn-connectcampaignsv2-campaign-telephonyoutboundmode-predictiveconfig
            '''
            result = self._values.get("predictive_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.PredictiveConfigProperty"]], result)

        @builtins.property
        def progressive_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.ProgressiveConfigProperty"]]:
            '''Contains progressive telephony outbound mode configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-telephonyoutboundmode.html#cfn-connectcampaignsv2-campaign-telephonyoutboundmode-progressiveconfig
            '''
            result = self._values.get("progressive_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.ProgressiveConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelephonyOutboundModeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.TimeRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"end_time": "endTime", "start_time": "startTime"},
    )
    class TimeRangeProperty:
        def __init__(self, *, end_time: builtins.str, start_time: builtins.str) -> None:
            '''Contains information about a time range.

            :param end_time: The end time of the time range.
            :param start_time: The start time of the time range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-timerange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                time_range_property = connectcampaignsv2.CfnCampaign.TimeRangeProperty(
                    end_time="endTime",
                    start_time="startTime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fbaac78f440293f26b08d1c7d41436b21833649d5569bb99f4e6c2bda8bd9a4e)
                check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "end_time": end_time,
                "start_time": start_time,
            }

        @builtins.property
        def end_time(self) -> builtins.str:
            '''The end time of the time range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-timerange.html#cfn-connectcampaignsv2-campaign-timerange-endtime
            '''
            result = self._values.get("end_time")
            assert result is not None, "Required property 'end_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_time(self) -> builtins.str:
            '''The start time of the time range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-timerange.html#cfn-connectcampaignsv2-campaign-timerange-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaign.TimeWindowProperty",
        jsii_struct_bases=[],
        name_mapping={
            "open_hours": "openHours",
            "restricted_periods": "restrictedPeriods",
        },
    )
    class TimeWindowProperty:
        def __init__(
            self,
            *,
            open_hours: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.OpenHoursProperty", typing.Dict[builtins.str, typing.Any]]],
            restricted_periods: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.RestrictedPeriodsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about a time window.

            :param open_hours: The open hours configuration.
            :param restricted_periods: The restricted periods configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-timewindow.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
                
                time_window_property = connectcampaignsv2.CfnCampaign.TimeWindowProperty(
                    open_hours=connectcampaignsv2.CfnCampaign.OpenHoursProperty(
                        daily_hours=[connectcampaignsv2.CfnCampaign.DailyHourProperty(
                            key="key",
                            value=[connectcampaignsv2.CfnCampaign.TimeRangeProperty(
                                end_time="endTime",
                                start_time="startTime"
                            )]
                        )]
                    ),
                
                    # the properties below are optional
                    restricted_periods=connectcampaignsv2.CfnCampaign.RestrictedPeriodsProperty(
                        restricted_period_list=[connectcampaignsv2.CfnCampaign.RestrictedPeriodProperty(
                            end_date="endDate",
                            start_date="startDate",
                
                            # the properties below are optional
                            name="name"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__738a8f46b804533de9d82348af38a0b7f7c37f641c9240bef005d4c22b396f09)
                check_type(argname="argument open_hours", value=open_hours, expected_type=type_hints["open_hours"])
                check_type(argname="argument restricted_periods", value=restricted_periods, expected_type=type_hints["restricted_periods"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "open_hours": open_hours,
            }
            if restricted_periods is not None:
                self._values["restricted_periods"] = restricted_periods

        @builtins.property
        def open_hours(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCampaign.OpenHoursProperty"]:
            '''The open hours configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-timewindow.html#cfn-connectcampaignsv2-campaign-timewindow-openhours
            '''
            result = self._values.get("open_hours")
            assert result is not None, "Required property 'open_hours' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCampaign.OpenHoursProperty"], result)

        @builtins.property
        def restricted_periods(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.RestrictedPeriodsProperty"]]:
            '''The restricted periods configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connectcampaignsv2-campaign-timewindow.html#cfn-connectcampaignsv2-campaign-timewindow-restrictedperiods
            '''
            result = self._values.get("restricted_periods")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.RestrictedPeriodsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeWindowProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connectcampaignsv2.CfnCampaignProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_subtype_config": "channelSubtypeConfig",
        "connect_instance_id": "connectInstanceId",
        "name": "name",
        "communication_limits_override": "communicationLimitsOverride",
        "communication_time_config": "communicationTimeConfig",
        "connect_campaign_flow_arn": "connectCampaignFlowArn",
        "schedule": "schedule",
        "source": "source",
        "tags": "tags",
    },
)
class CfnCampaignProps:
    def __init__(
        self,
        *,
        channel_subtype_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.ChannelSubtypeConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        connect_instance_id: builtins.str,
        name: builtins.str,
        communication_limits_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CommunicationLimitsConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        communication_time_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CommunicationTimeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        connect_campaign_flow_arn: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.SourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCampaign``.

        :param channel_subtype_config: Contains channel subtype configuration for an outbound campaign.
        :param connect_instance_id: The identifier of the Amazon Connect instance. You can find the ``instanceId`` in the ARN of the instance.
        :param name: The name of the outbound campaign.
        :param communication_limits_override: Communication limits configuration for an outbound campaign.
        :param communication_time_config: Contains communication time configuration for an outbound campaign.
        :param connect_campaign_flow_arn: The Amazon Resource Name (ARN) of the Amazon Connect campaign flow associated with the outbound campaign.
        :param schedule: Contains the schedule configuration.
        :param source: Contains source configuration.
        :param tags: The tags used to organize, track, or control access for this resource. For example, ``{ "tags": {"key1":"value1", "key2":"value2"} }`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaignsv2-campaign.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connectcampaignsv2 as connectcampaignsv2
            
            # agentless_config: Any
            
            cfn_campaign_props = connectcampaignsv2.CfnCampaignProps(
                channel_subtype_config=connectcampaignsv2.CfnCampaign.ChannelSubtypeConfigProperty(
                    email=connectcampaignsv2.CfnCampaign.EmailChannelSubtypeConfigProperty(
                        default_outbound_config=connectcampaignsv2.CfnCampaign.EmailOutboundConfigProperty(
                            connect_source_email_address="connectSourceEmailAddress",
                            wisdom_template_arn="wisdomTemplateArn",
            
                            # the properties below are optional
                            source_email_address_display_name="sourceEmailAddressDisplayName"
                        ),
                        outbound_mode=connectcampaignsv2.CfnCampaign.EmailOutboundModeProperty(
                            agentless_config=agentless_config
                        ),
            
                        # the properties below are optional
                        capacity=123
                    ),
                    sms=connectcampaignsv2.CfnCampaign.SmsChannelSubtypeConfigProperty(
                        default_outbound_config=connectcampaignsv2.CfnCampaign.SmsOutboundConfigProperty(
                            connect_source_phone_number_arn="connectSourcePhoneNumberArn",
                            wisdom_template_arn="wisdomTemplateArn"
                        ),
                        outbound_mode=connectcampaignsv2.CfnCampaign.SmsOutboundModeProperty(
                            agentless_config=agentless_config
                        ),
            
                        # the properties below are optional
                        capacity=123
                    ),
                    telephony=connectcampaignsv2.CfnCampaign.TelephonyChannelSubtypeConfigProperty(
                        default_outbound_config=connectcampaignsv2.CfnCampaign.TelephonyOutboundConfigProperty(
                            connect_contact_flow_id="connectContactFlowId",
            
                            # the properties below are optional
                            answer_machine_detection_config=connectcampaignsv2.CfnCampaign.AnswerMachineDetectionConfigProperty(
                                enable_answer_machine_detection=False,
            
                                # the properties below are optional
                                await_answer_machine_prompt=False
                            ),
                            connect_source_phone_number="connectSourcePhoneNumber"
                        ),
                        outbound_mode=connectcampaignsv2.CfnCampaign.TelephonyOutboundModeProperty(
                            agentless_config=agentless_config,
                            predictive_config=connectcampaignsv2.CfnCampaign.PredictiveConfigProperty(
                                bandwidth_allocation=123
                            ),
                            progressive_config=connectcampaignsv2.CfnCampaign.ProgressiveConfigProperty(
                                bandwidth_allocation=123
                            )
                        ),
            
                        # the properties below are optional
                        capacity=123,
                        connect_queue_id="connectQueueId"
                    )
                ),
                connect_instance_id="connectInstanceId",
                name="name",
            
                # the properties below are optional
                communication_limits_override=connectcampaignsv2.CfnCampaign.CommunicationLimitsConfigProperty(
                    all_channels_subtypes=connectcampaignsv2.CfnCampaign.CommunicationLimitsProperty(
                        communication_limit_list=[connectcampaignsv2.CfnCampaign.CommunicationLimitProperty(
                            frequency=123,
                            max_count_per_recipient=123,
                            unit="unit"
                        )]
                    ),
                    instance_limits_handling="instanceLimitsHandling"
                ),
                communication_time_config=connectcampaignsv2.CfnCampaign.CommunicationTimeConfigProperty(
                    local_time_zone_config=connectcampaignsv2.CfnCampaign.LocalTimeZoneConfigProperty(
                        default_time_zone="defaultTimeZone",
                        local_time_zone_detection=["localTimeZoneDetection"]
                    ),
            
                    # the properties below are optional
                    email=connectcampaignsv2.CfnCampaign.TimeWindowProperty(
                        open_hours=connectcampaignsv2.CfnCampaign.OpenHoursProperty(
                            daily_hours=[connectcampaignsv2.CfnCampaign.DailyHourProperty(
                                key="key",
                                value=[connectcampaignsv2.CfnCampaign.TimeRangeProperty(
                                    end_time="endTime",
                                    start_time="startTime"
                                )]
                            )]
                        ),
            
                        # the properties below are optional
                        restricted_periods=connectcampaignsv2.CfnCampaign.RestrictedPeriodsProperty(
                            restricted_period_list=[connectcampaignsv2.CfnCampaign.RestrictedPeriodProperty(
                                end_date="endDate",
                                start_date="startDate",
            
                                # the properties below are optional
                                name="name"
                            )]
                        )
                    ),
                    sms=connectcampaignsv2.CfnCampaign.TimeWindowProperty(
                        open_hours=connectcampaignsv2.CfnCampaign.OpenHoursProperty(
                            daily_hours=[connectcampaignsv2.CfnCampaign.DailyHourProperty(
                                key="key",
                                value=[connectcampaignsv2.CfnCampaign.TimeRangeProperty(
                                    end_time="endTime",
                                    start_time="startTime"
                                )]
                            )]
                        ),
            
                        # the properties below are optional
                        restricted_periods=connectcampaignsv2.CfnCampaign.RestrictedPeriodsProperty(
                            restricted_period_list=[connectcampaignsv2.CfnCampaign.RestrictedPeriodProperty(
                                end_date="endDate",
                                start_date="startDate",
            
                                # the properties below are optional
                                name="name"
                            )]
                        )
                    ),
                    telephony=connectcampaignsv2.CfnCampaign.TimeWindowProperty(
                        open_hours=connectcampaignsv2.CfnCampaign.OpenHoursProperty(
                            daily_hours=[connectcampaignsv2.CfnCampaign.DailyHourProperty(
                                key="key",
                                value=[connectcampaignsv2.CfnCampaign.TimeRangeProperty(
                                    end_time="endTime",
                                    start_time="startTime"
                                )]
                            )]
                        ),
            
                        # the properties below are optional
                        restricted_periods=connectcampaignsv2.CfnCampaign.RestrictedPeriodsProperty(
                            restricted_period_list=[connectcampaignsv2.CfnCampaign.RestrictedPeriodProperty(
                                end_date="endDate",
                                start_date="startDate",
            
                                # the properties below are optional
                                name="name"
                            )]
                        )
                    )
                ),
                connect_campaign_flow_arn="connectCampaignFlowArn",
                schedule=connectcampaignsv2.CfnCampaign.ScheduleProperty(
                    end_time="endTime",
                    start_time="startTime",
            
                    # the properties below are optional
                    refresh_frequency="refreshFrequency"
                ),
                source=connectcampaignsv2.CfnCampaign.SourceProperty(
                    customer_profiles_segment_arn="customerProfilesSegmentArn",
                    event_trigger=connectcampaignsv2.CfnCampaign.EventTriggerProperty(
                        customer_profiles_domain_arn="customerProfilesDomainArn"
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c58eb40b443fce35feb659905089795642547d367bd583cc8addd65c75034e8)
            check_type(argname="argument channel_subtype_config", value=channel_subtype_config, expected_type=type_hints["channel_subtype_config"])
            check_type(argname="argument connect_instance_id", value=connect_instance_id, expected_type=type_hints["connect_instance_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument communication_limits_override", value=communication_limits_override, expected_type=type_hints["communication_limits_override"])
            check_type(argname="argument communication_time_config", value=communication_time_config, expected_type=type_hints["communication_time_config"])
            check_type(argname="argument connect_campaign_flow_arn", value=connect_campaign_flow_arn, expected_type=type_hints["connect_campaign_flow_arn"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_subtype_config": channel_subtype_config,
            "connect_instance_id": connect_instance_id,
            "name": name,
        }
        if communication_limits_override is not None:
            self._values["communication_limits_override"] = communication_limits_override
        if communication_time_config is not None:
            self._values["communication_time_config"] = communication_time_config
        if connect_campaign_flow_arn is not None:
            self._values["connect_campaign_flow_arn"] = connect_campaign_flow_arn
        if schedule is not None:
            self._values["schedule"] = schedule
        if source is not None:
            self._values["source"] = source
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def channel_subtype_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCampaign.ChannelSubtypeConfigProperty]:
        '''Contains channel subtype configuration for an outbound campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaignsv2-campaign.html#cfn-connectcampaignsv2-campaign-channelsubtypeconfig
        '''
        result = self._values.get("channel_subtype_config")
        assert result is not None, "Required property 'channel_subtype_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCampaign.ChannelSubtypeConfigProperty], result)

    @builtins.property
    def connect_instance_id(self) -> builtins.str:
        '''The identifier of the Amazon Connect instance.

        You can find the ``instanceId`` in the ARN of the instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaignsv2-campaign.html#cfn-connectcampaignsv2-campaign-connectinstanceid
        '''
        result = self._values.get("connect_instance_id")
        assert result is not None, "Required property 'connect_instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the outbound campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaignsv2-campaign.html#cfn-connectcampaignsv2-campaign-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def communication_limits_override(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.CommunicationLimitsConfigProperty]]:
        '''Communication limits configuration for an outbound campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaignsv2-campaign.html#cfn-connectcampaignsv2-campaign-communicationlimitsoverride
        '''
        result = self._values.get("communication_limits_override")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.CommunicationLimitsConfigProperty]], result)

    @builtins.property
    def communication_time_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.CommunicationTimeConfigProperty]]:
        '''Contains communication time configuration for an outbound campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaignsv2-campaign.html#cfn-connectcampaignsv2-campaign-communicationtimeconfig
        '''
        result = self._values.get("communication_time_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.CommunicationTimeConfigProperty]], result)

    @builtins.property
    def connect_campaign_flow_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon Connect campaign flow associated with the outbound campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaignsv2-campaign.html#cfn-connectcampaignsv2-campaign-connectcampaignflowarn
        '''
        result = self._values.get("connect_campaign_flow_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.ScheduleProperty]]:
        '''Contains the schedule configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaignsv2-campaign.html#cfn-connectcampaignsv2-campaign-schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.ScheduleProperty]], result)

    @builtins.property
    def source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.SourceProperty]]:
        '''Contains source configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaignsv2-campaign.html#cfn-connectcampaignsv2-campaign-source
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.SourceProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        For example, ``{ "tags": {"key1":"value1", "key2":"value2"} }`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connectcampaignsv2-campaign.html#cfn-connectcampaignsv2-campaign-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCampaignProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCampaign",
    "CfnCampaignProps",
]

publication.publish()

def _typecheckingstub__228f2b3a0b621ad8a32effe36abeb2d513f50077bd0ad5de7f33f1ea81da26bf(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel_subtype_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.ChannelSubtypeConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    connect_instance_id: builtins.str,
    name: builtins.str,
    communication_limits_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CommunicationLimitsConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    communication_time_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CommunicationTimeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    connect_campaign_flow_arn: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.SourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a3569f68d4e1cebb6aa0c64e1d5986831e6aae0db4d29cfdc75c914d15ffdce(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c76203b12deea4c92c4180a4c58e9869df456b6f2b525019f1464142d4eec24c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5b5c43e63bf2a0bf41f238db2ecf2eed8032758072a77ebd8c459798f74fa0c(
    value: typing.Union[_IResolvable_da3f097b, CfnCampaign.ChannelSubtypeConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dea841111eb9715b7977d34769972a35f4ff12770a8fd30c5e8756c52e2315dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a6ee2c8ab1041b75d3fc61f47c640e057770a39c0cd0f8b43528a1df4134a14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9a4f9850d67cc76e259c5826fc9085afbf3a202dbe3ba9f6af537bfd18c830a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.CommunicationLimitsConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f04ec307144a013ae0d78d8747dea1d25d0ab7e9abc18aaab84c15553a5bb868(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.CommunicationTimeConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c514dbfca338965ca2462164a214264c8a79ca12e54b81685d99cc57a888b73c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96d94c4ddf36f3ab10421fbfcb861afdc6852b09a0b0783e33f602560dc90a87(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.ScheduleProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dd88e602a1609757680509707feb43ec965d5628d820f7eb876dc6ac055b404(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCampaign.SourceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7a5de836c29e94a66b86ab16ab9047f892319b5f0f4bb59a47dc977cdb0fb0b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc9e20500646db1cdb84f99ed95755110a841a334cc195de359fe87f9f7051d5(
    *,
    enable_answer_machine_detection: typing.Union[builtins.bool, _IResolvable_da3f097b],
    await_answer_machine_prompt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aae9c62c36e7d18a87df32d56bbdc6f7740c287aaac55c92832b7ca366aa6b5b(
    *,
    email: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.EmailChannelSubtypeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.SmsChannelSubtypeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    telephony: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TelephonyChannelSubtypeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a4b2b207bce63b0696bef9d14a808bcf3bd9ae2746f645e72a80348100b732b(
    *,
    frequency: jsii.Number,
    max_count_per_recipient: jsii.Number,
    unit: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a5ca8627addc85a64908de980e86012a2ad9d04257fa86e81c4873e7a7d93be(
    *,
    all_channels_subtypes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CommunicationLimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    instance_limits_handling: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__063b98187bfe10fef303f184ab9d1c8b1d41a5388eb6da2529b64fee8106550c(
    *,
    communication_limit_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CommunicationLimitProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3f2f2fbfc83eeac20d115af03889d47eb55561494e8fc488eeec30eb2e47752(
    *,
    local_time_zone_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.LocalTimeZoneConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    email: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TimeWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TimeWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    telephony: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TimeWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35e6acb6b0c0424f51f610f7f0a2abd4c482306c13db09f191eae079682c9f5c(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TimeRangeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff9274643abefe2ecd29ff0322f3b49479b574757b18fe4f15225f01a19ef7ea(
    *,
    default_outbound_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.EmailOutboundConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    outbound_mode: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.EmailOutboundModeProperty, typing.Dict[builtins.str, typing.Any]]],
    capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b2c45c48dd3f984623dbcc344a83d9c26e929cd6947cc9f868ffe1b4d0341d1(
    *,
    connect_source_email_address: builtins.str,
    wisdom_template_arn: builtins.str,
    source_email_address_display_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__016ccd411110b9f8510f586be6901ef480857575d80a38ed7c7e81cae2ad5e94(
    *,
    agentless_config: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5c63db70e1b49ff8c093902378da25d9e1f34010626b2eeb9d25d6da292eb2c(
    *,
    customer_profiles_domain_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c03234f264094d68479c6e1cf3801d50627e839a73b2f0cbeb95c82522f9a66e(
    *,
    default_time_zone: typing.Optional[builtins.str] = None,
    local_time_zone_detection: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a34ace5bfcc35c52d69e6dd7ef3c38abf4d254290d5470f5104e49f2d115b39(
    *,
    daily_hours: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.DailyHourProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a27014c548ec13c6446b07f461be7ed43556a2cb77433713ef38f272a14459fd(
    *,
    bandwidth_allocation: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6504302e8d20b62038efca8c5dfe9bbddfc485cc88de44f995d599a39017ddbe(
    *,
    bandwidth_allocation: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f2a36f6fa12d741457cf955ef79fa845b855e1b170b7ea44a157f8f120f9b67(
    *,
    end_date: builtins.str,
    start_date: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f30a61789fda85a4bb2aa71fc64566047bab737aa5220ee60d91e1e08d9a84dd(
    *,
    restricted_period_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.RestrictedPeriodProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b6a4567c8e5f09b06087beafe0e729f0ae431ebcefbe37d716e547d333cb24b(
    *,
    end_time: builtins.str,
    start_time: builtins.str,
    refresh_frequency: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d42ae0232d954af9167d51954642098f71dd226d554f1b2fab39b2c46726ee(
    *,
    default_outbound_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.SmsOutboundConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    outbound_mode: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.SmsOutboundModeProperty, typing.Dict[builtins.str, typing.Any]]],
    capacity: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__874dedca8982d2204aa531b3a554ca0a994b9ce64825e83b31a7a7563d08f262(
    *,
    connect_source_phone_number_arn: builtins.str,
    wisdom_template_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67957d238e403659f29fa8bf2db2164d694d327a14b84df3d61c10b2b3afd954(
    *,
    agentless_config: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48dbe2dd9c0147e5b2bea173aba4c056f8a83ba308e89c654331a4a77f46636d(
    *,
    customer_profiles_segment_arn: typing.Optional[builtins.str] = None,
    event_trigger: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.EventTriggerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19c776b12e28122b49a867e83503b94bf286d46879c32085c60a17f0213dc948(
    *,
    default_outbound_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TelephonyOutboundConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    outbound_mode: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TelephonyOutboundModeProperty, typing.Dict[builtins.str, typing.Any]]],
    capacity: typing.Optional[jsii.Number] = None,
    connect_queue_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2751a1c01ea2bfaf5fe6806fe1a585daea66baf82d5fe0a4cec77a9b592d901a(
    *,
    connect_contact_flow_id: builtins.str,
    answer_machine_detection_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.AnswerMachineDetectionConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    connect_source_phone_number: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7582ea451819f82369b8beb09bc8c872c5424040d69392d7bc3ab56ee8813053(
    *,
    agentless_config: typing.Any = None,
    predictive_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.PredictiveConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    progressive_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.ProgressiveConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbaac78f440293f26b08d1c7d41436b21833649d5569bb99f4e6c2bda8bd9a4e(
    *,
    end_time: builtins.str,
    start_time: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__738a8f46b804533de9d82348af38a0b7f7c37f641c9240bef005d4c22b396f09(
    *,
    open_hours: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.OpenHoursProperty, typing.Dict[builtins.str, typing.Any]]],
    restricted_periods: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.RestrictedPeriodsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c58eb40b443fce35feb659905089795642547d367bd583cc8addd65c75034e8(
    *,
    channel_subtype_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.ChannelSubtypeConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    connect_instance_id: builtins.str,
    name: builtins.str,
    communication_limits_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CommunicationLimitsConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    communication_time_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CommunicationTimeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    connect_campaign_flow_arn: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.SourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
