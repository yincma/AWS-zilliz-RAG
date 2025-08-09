r'''
# AWS::AIOps Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_aiops as aiops
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AIOps construct libraries](https://constructs.dev/search?q=aiops)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AIOps resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AIOps.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AIOps](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AIOps.html).

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
class CfnInvestigationGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_aiops.CfnInvestigationGroup",
):
    '''Creates an *investigation group* in your account.

    Creating an investigation group is a one-time setup task for each Region in your account. It is a necessary task to be able to perform investigations.

    Settings in the investigation group help you centrally manage the common properties of your investigations, such as the following:

    - Who can access the investigations
    - Whether investigation data is encrypted with a customer managed AWS Key Management Service key.
    - How long investigations and their data are retained by default.

    Currently, you can have one investigation group in each Region in your account. Each investigation in a Region is a part of the investigation group in that Region

    To create an investigation group and set up CloudWatch investigations, you must be signed in to an IAM principal that has either the ``AIOpsConsoleAdminPolicy`` or the ``AdministratorAccess`` IAM policy attached, or to an account that has similar permissions.
    .. epigraph::

       You can configure CloudWatch alarms to start investigations and add events to investigations. If you create your investigation group with ``CreateInvestigationGroup`` and you want to enable alarms to do this, you must use ``PutInvestigationGroupPolicy`` to create a resource policy that grants this permission to CloudWatch alarms.

       For more information about configuring CloudWatch alarms, see `Using Amazon CloudWatch alarms <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aiops-investigationgroup.html
    :cloudformationResource: AWS::AIOps::InvestigationGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_aiops as aiops
        
        cfn_investigation_group = aiops.CfnInvestigationGroup(self, "MyCfnInvestigationGroup",
            name="name",
        
            # the properties below are optional
            chatbot_notification_channels=[aiops.CfnInvestigationGroup.ChatbotNotificationChannelProperty(
                chat_configuration_arns=["chatConfigurationArns"],
                sns_topic_arn="snsTopicArn"
            )],
            cross_account_configurations=[aiops.CfnInvestigationGroup.CrossAccountConfigurationProperty(
                source_role_arn="sourceRoleArn"
            )],
            encryption_config=aiops.CfnInvestigationGroup.EncryptionConfigMapProperty(
                encryption_configuration_type="encryptionConfigurationType",
                kms_key_id="kmsKeyId"
            ),
            investigation_group_policy="investigationGroupPolicy",
            is_cloud_trail_event_history_enabled=False,
            retention_in_days=123,
            role_arn="roleArn",
            tag_key_boundaries=["tagKeyBoundaries"],
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
        chatbot_notification_channels: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInvestigationGroup.ChatbotNotificationChannelProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        cross_account_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInvestigationGroup.CrossAccountConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        encryption_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInvestigationGroup.EncryptionConfigMapProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        investigation_group_policy: typing.Optional[builtins.str] = None,
        is_cloud_trail_event_history_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        retention_in_days: typing.Optional[jsii.Number] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tag_key_boundaries: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Specify either the name or the ARN of the investigation group that you want to view. This is used to set the name of the investigation group.
        :param chatbot_notification_channels: Use this property to integrate CloudWatch investigations with chat applications. This property is an array. For the first string, specify the ARN of an Amazon SNS topic. For the array of strings, specify the ARNs of one or more chat applications configurations that you want to associate with that topic. For more information about these configuration ARNs, see `Getting started with Amazon Q in chat applications <https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html>`_ and `Resource type defined by AWS Chatbot <https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html#awschatbot-resources-for-iam-policies>`_ .
        :param cross_account_configurations: List of ``sourceRoleArn`` values that have been configured for cross-account access.
        :param encryption_config: Specifies the customer managed AWS KMS key that the investigation group uses to encrypt data, if there is one. If not, the investigation group uses an AWS key to encrypt the data.
        :param investigation_group_policy: Returns the JSON of the IAM resource policy associated with the specified investigation group in a string. For example, ``{\\"Version\\":\\"2012-10-17\\",\\"Statement\\":[{\\"Effect\\":\\"Allow\\",\\"Principal\\":{\\"Service\\":\\"aiops.alarms.cloudwatch.amazonaws.com\\"},\\"Action\\":[\\"aiops:CreateInvestigation\\",\\"aiops:CreateInvestigationEvent\\"],\\"Resource\\":\\"*\\",\\"Condition\\":{\\"StringEquals\\":{\\"aws:SourceAccount\\":\\"111122223333\\"},\\"ArnLike\\":{\\"aws:SourceArn\\":\\"arn:aws:cloudwatch:us-east-1:111122223333:alarm:*\\"}}}]}`` .
        :param is_cloud_trail_event_history_enabled: Specify ``true`` to enable CloudWatch investigations to have access to change events that are recorded by CloudTrail. The default is ``true`` .
        :param retention_in_days: Specifies how long that investigation data is kept.
        :param role_arn: The ARN of the IAM role that the investigation group uses for permissions to gather data.
        :param tag_key_boundaries: Displays the custom tag keys for custom applications in your system that you have specified in the investigation group. Resource tags help CloudWatch investigations narrow the search space when it is unable to discover definite relationships between resources.
        :param tags: The list of key-value pairs to associate with the resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f390e65acdf4efe0289b1b8e5f17c031f7a88a13963effed34b7d4944b31dd7e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInvestigationGroupProps(
            name=name,
            chatbot_notification_channels=chatbot_notification_channels,
            cross_account_configurations=cross_account_configurations,
            encryption_config=encryption_config,
            investigation_group_policy=investigation_group_policy,
            is_cloud_trail_event_history_enabled=is_cloud_trail_event_history_enabled,
            retention_in_days=retention_in_days,
            role_arn=role_arn,
            tag_key_boundaries=tag_key_boundaries,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a532233685b19239d88980a7d9b4a8384450db2dc5593ebca70b4c1bca8faf14)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ada159a27791012fd3d77245257dddda16f3719a8e4bd5e53e293ff27dceacb7)
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
        '''The Amazon Resource Name (ARN) of the investigation group.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time that the investigation group was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> builtins.str:
        '''The name of the user who created the investigation group.

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedAt")
    def attr_last_modified_at(self) -> builtins.str:
        '''The date and time that the investigation group was most recently modified.

        :cloudformationAttribute: LastModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedBy")
    def attr_last_modified_by(self) -> builtins.str:
        '''The name of the user who created the investigation group.

        :cloudformationAttribute: LastModifiedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedBy"))

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
        '''Specify either the name or the ARN of the investigation group that you want to view.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68d7a3472d5ddc810dbc073636686c470b0fe6568b144fc7473b578e828715b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="chatbotNotificationChannels")
    def chatbot_notification_channels(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInvestigationGroup.ChatbotNotificationChannelProperty"]]]]:
        '''Use this property to integrate CloudWatch investigations with chat applications.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInvestigationGroup.ChatbotNotificationChannelProperty"]]]], jsii.get(self, "chatbotNotificationChannels"))

    @chatbot_notification_channels.setter
    def chatbot_notification_channels(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInvestigationGroup.ChatbotNotificationChannelProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5db4331534a87e764a8534aad930983f78144efc39dc99f450b39b9adabfe898)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "chatbotNotificationChannels", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="crossAccountConfigurations")
    def cross_account_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInvestigationGroup.CrossAccountConfigurationProperty"]]]]:
        '''List of ``sourceRoleArn`` values that have been configured for cross-account access.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInvestigationGroup.CrossAccountConfigurationProperty"]]]], jsii.get(self, "crossAccountConfigurations"))

    @cross_account_configurations.setter
    def cross_account_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInvestigationGroup.CrossAccountConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cab3f68c7637d356559913c4b9be139738c64bd676003ea2810dd4ddafef47e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossAccountConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="encryptionConfig")
    def encryption_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInvestigationGroup.EncryptionConfigMapProperty"]]:
        '''Specifies the customer managed AWS KMS key that the investigation group uses to encrypt data, if there is one.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInvestigationGroup.EncryptionConfigMapProperty"]], jsii.get(self, "encryptionConfig"))

    @encryption_config.setter
    def encryption_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInvestigationGroup.EncryptionConfigMapProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f51c34e4f09d967ae3c411a2743d3d857ce2c925f1d1b67c9152dd736522694)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="investigationGroupPolicy")
    def investigation_group_policy(self) -> typing.Optional[builtins.str]:
        '''Returns the JSON of the IAM resource policy associated with the specified investigation group in a string.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "investigationGroupPolicy"))

    @investigation_group_policy.setter
    def investigation_group_policy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a878340860e2c35de4d03b82df1e97245d5f40120fa110076a32f436fd31ddaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "investigationGroupPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="isCloudTrailEventHistoryEnabled")
    def is_cloud_trail_event_history_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specify ``true`` to enable CloudWatch investigations to have access to change events that are recorded by CloudTrail.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "isCloudTrailEventHistoryEnabled"))

    @is_cloud_trail_event_history_enabled.setter
    def is_cloud_trail_event_history_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fc3a119f870dceec4d1a3ba5b4f84971973ad9c990d3aa7c5bb5e2ff0005cba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isCloudTrailEventHistoryEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="retentionInDays")
    def retention_in_days(self) -> typing.Optional[jsii.Number]:
        '''Specifies how long that investigation data is kept.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInDays"))

    @retention_in_days.setter
    def retention_in_days(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb70ecd162c324b07d0ae455e2881185c11d02912ce9513cd8fd61e7de3c054c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInDays", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM role that the investigation group uses for permissions to gather data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3eb82bc9999595315778658f89b708e57ad701088d012c3391ce1a4e6721195)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagKeyBoundaries")
    def tag_key_boundaries(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Displays the custom tag keys for custom applications in your system that you have specified in the investigation group.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagKeyBoundaries"))

    @tag_key_boundaries.setter
    def tag_key_boundaries(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__847e58d896c672f6db334949abc5da531a40f943b791ff6c76da0751ee7be4ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKeyBoundaries", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value pairs to associate with the resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58e4b2d8c71fc2670bc24a5f274e0134fae9ffd7aeca95db0fed9e2d974499f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aiops.CfnInvestigationGroup.ChatbotNotificationChannelProperty",
        jsii_struct_bases=[],
        name_mapping={
            "chat_configuration_arns": "chatConfigurationArns",
            "sns_topic_arn": "snsTopicArn",
        },
    )
    class ChatbotNotificationChannelProperty:
        def __init__(
            self,
            *,
            chat_configuration_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            sns_topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use this structure to integrate CloudWatch investigations with chat applications.

            This structure is a string array. For the first string, specify the ARN of an Amazon SNS topic. For the array of strings, specify the ARNs of one or more chat applications configurations that you want to associate with that topic. For more information about these configuration ARNs, see `Getting started with Amazon Q in chat applications <https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html>`_ and `Resource type defined by AWS Chatbot <https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html#awschatbot-resources-for-iam-policies>`_ .

            :param chat_configuration_arns: Returns the Amazon Resource Name (ARN) of any third-party chat integrations configured for the account.
            :param sns_topic_arn: Returns the ARN of an Amazon SNS topic used for third-party chat integrations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aiops-investigationgroup-chatbotnotificationchannel.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aiops as aiops
                
                chatbot_notification_channel_property = aiops.CfnInvestigationGroup.ChatbotNotificationChannelProperty(
                    chat_configuration_arns=["chatConfigurationArns"],
                    sns_topic_arn="snsTopicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d67ba65a7634fe2bf96859c6a05258a6565faf2372426edac2b3d876dc0b9a61)
                check_type(argname="argument chat_configuration_arns", value=chat_configuration_arns, expected_type=type_hints["chat_configuration_arns"])
                check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if chat_configuration_arns is not None:
                self._values["chat_configuration_arns"] = chat_configuration_arns
            if sns_topic_arn is not None:
                self._values["sns_topic_arn"] = sns_topic_arn

        @builtins.property
        def chat_configuration_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Returns the Amazon Resource Name (ARN) of any third-party chat integrations configured for the account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aiops-investigationgroup-chatbotnotificationchannel.html#cfn-aiops-investigationgroup-chatbotnotificationchannel-chatconfigurationarns
            '''
            result = self._values.get("chat_configuration_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def sns_topic_arn(self) -> typing.Optional[builtins.str]:
            '''Returns the ARN of an Amazon SNS topic used for third-party chat integrations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aiops-investigationgroup-chatbotnotificationchannel.html#cfn-aiops-investigationgroup-chatbotnotificationchannel-snstopicarn
            '''
            result = self._values.get("sns_topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ChatbotNotificationChannelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aiops.CfnInvestigationGroup.CrossAccountConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"source_role_arn": "sourceRoleArn"},
    )
    class CrossAccountConfigurationProperty:
        def __init__(
            self,
            *,
            source_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This structure contains information about the cross-account configuration in the account.

            :param source_role_arn: The ARN of an existing role which will be used to do investigations on your behalf.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aiops-investigationgroup-crossaccountconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aiops as aiops
                
                cross_account_configuration_property = aiops.CfnInvestigationGroup.CrossAccountConfigurationProperty(
                    source_role_arn="sourceRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__686ab8dd38f6db168aebbeef0e137fd1f90381f42a12046db10e4ba4ac3a3e3f)
                check_type(argname="argument source_role_arn", value=source_role_arn, expected_type=type_hints["source_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source_role_arn is not None:
                self._values["source_role_arn"] = source_role_arn

        @builtins.property
        def source_role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of an existing role which will be used to do investigations on your behalf.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aiops-investigationgroup-crossaccountconfiguration.html#cfn-aiops-investigationgroup-crossaccountconfiguration-sourcerolearn
            '''
            result = self._values.get("source_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CrossAccountConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aiops.CfnInvestigationGroup.EncryptionConfigMapProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_configuration_type": "encryptionConfigurationType",
            "kms_key_id": "kmsKeyId",
        },
    )
    class EncryptionConfigMapProperty:
        def __init__(
            self,
            *,
            encryption_configuration_type: typing.Optional[builtins.str] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use this structure if you want to use a customer managed AWS KMS key to encrypt your investigation data.

            If you omit this parameter, CloudWatch investigations will use an AWS key to encrypt the data. For more information, see `Encryption of investigation data <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Security.html#Investigations-KMS>`_ .

            :param encryption_configuration_type: Displays whether investigation data is encrypted by a customer managed key or an AWS owned key.
            :param kms_key_id: If the investigation group uses a customer managed key for encryption, this field displays the ID of that key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aiops-investigationgroup-encryptionconfigmap.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aiops as aiops
                
                encryption_config_map_property = aiops.CfnInvestigationGroup.EncryptionConfigMapProperty(
                    encryption_configuration_type="encryptionConfigurationType",
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__822047880bb03db9129836b4da0b735fe316364e02aa10f8c042ba4d22f3c20f)
                check_type(argname="argument encryption_configuration_type", value=encryption_configuration_type, expected_type=type_hints["encryption_configuration_type"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encryption_configuration_type is not None:
                self._values["encryption_configuration_type"] = encryption_configuration_type
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def encryption_configuration_type(self) -> typing.Optional[builtins.str]:
            '''Displays whether investigation data is encrypted by a customer managed key or an AWS owned key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aiops-investigationgroup-encryptionconfigmap.html#cfn-aiops-investigationgroup-encryptionconfigmap-encryptionconfigurationtype
            '''
            result = self._values.get("encryption_configuration_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''If the investigation group uses a customer managed key for encryption, this field displays the ID of that key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aiops-investigationgroup-encryptionconfigmap.html#cfn-aiops-investigationgroup-encryptionconfigmap-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_aiops.CfnInvestigationGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "chatbot_notification_channels": "chatbotNotificationChannels",
        "cross_account_configurations": "crossAccountConfigurations",
        "encryption_config": "encryptionConfig",
        "investigation_group_policy": "investigationGroupPolicy",
        "is_cloud_trail_event_history_enabled": "isCloudTrailEventHistoryEnabled",
        "retention_in_days": "retentionInDays",
        "role_arn": "roleArn",
        "tag_key_boundaries": "tagKeyBoundaries",
        "tags": "tags",
    },
)
class CfnInvestigationGroupProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        chatbot_notification_channels: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInvestigationGroup.ChatbotNotificationChannelProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        cross_account_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInvestigationGroup.CrossAccountConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        encryption_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInvestigationGroup.EncryptionConfigMapProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        investigation_group_policy: typing.Optional[builtins.str] = None,
        is_cloud_trail_event_history_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        retention_in_days: typing.Optional[jsii.Number] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tag_key_boundaries: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInvestigationGroup``.

        :param name: Specify either the name or the ARN of the investigation group that you want to view. This is used to set the name of the investigation group.
        :param chatbot_notification_channels: Use this property to integrate CloudWatch investigations with chat applications. This property is an array. For the first string, specify the ARN of an Amazon SNS topic. For the array of strings, specify the ARNs of one or more chat applications configurations that you want to associate with that topic. For more information about these configuration ARNs, see `Getting started with Amazon Q in chat applications <https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html>`_ and `Resource type defined by AWS Chatbot <https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html#awschatbot-resources-for-iam-policies>`_ .
        :param cross_account_configurations: List of ``sourceRoleArn`` values that have been configured for cross-account access.
        :param encryption_config: Specifies the customer managed AWS KMS key that the investigation group uses to encrypt data, if there is one. If not, the investigation group uses an AWS key to encrypt the data.
        :param investigation_group_policy: Returns the JSON of the IAM resource policy associated with the specified investigation group in a string. For example, ``{\\"Version\\":\\"2012-10-17\\",\\"Statement\\":[{\\"Effect\\":\\"Allow\\",\\"Principal\\":{\\"Service\\":\\"aiops.alarms.cloudwatch.amazonaws.com\\"},\\"Action\\":[\\"aiops:CreateInvestigation\\",\\"aiops:CreateInvestigationEvent\\"],\\"Resource\\":\\"*\\",\\"Condition\\":{\\"StringEquals\\":{\\"aws:SourceAccount\\":\\"111122223333\\"},\\"ArnLike\\":{\\"aws:SourceArn\\":\\"arn:aws:cloudwatch:us-east-1:111122223333:alarm:*\\"}}}]}`` .
        :param is_cloud_trail_event_history_enabled: Specify ``true`` to enable CloudWatch investigations to have access to change events that are recorded by CloudTrail. The default is ``true`` .
        :param retention_in_days: Specifies how long that investigation data is kept.
        :param role_arn: The ARN of the IAM role that the investigation group uses for permissions to gather data.
        :param tag_key_boundaries: Displays the custom tag keys for custom applications in your system that you have specified in the investigation group. Resource tags help CloudWatch investigations narrow the search space when it is unable to discover definite relationships between resources.
        :param tags: The list of key-value pairs to associate with the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aiops-investigationgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_aiops as aiops
            
            cfn_investigation_group_props = aiops.CfnInvestigationGroupProps(
                name="name",
            
                # the properties below are optional
                chatbot_notification_channels=[aiops.CfnInvestigationGroup.ChatbotNotificationChannelProperty(
                    chat_configuration_arns=["chatConfigurationArns"],
                    sns_topic_arn="snsTopicArn"
                )],
                cross_account_configurations=[aiops.CfnInvestigationGroup.CrossAccountConfigurationProperty(
                    source_role_arn="sourceRoleArn"
                )],
                encryption_config=aiops.CfnInvestigationGroup.EncryptionConfigMapProperty(
                    encryption_configuration_type="encryptionConfigurationType",
                    kms_key_id="kmsKeyId"
                ),
                investigation_group_policy="investigationGroupPolicy",
                is_cloud_trail_event_history_enabled=False,
                retention_in_days=123,
                role_arn="roleArn",
                tag_key_boundaries=["tagKeyBoundaries"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d8bd4c8e0b3c95e52387aa0647c4f184b5f07925a09f1e74881b8a0738d25a8)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument chatbot_notification_channels", value=chatbot_notification_channels, expected_type=type_hints["chatbot_notification_channels"])
            check_type(argname="argument cross_account_configurations", value=cross_account_configurations, expected_type=type_hints["cross_account_configurations"])
            check_type(argname="argument encryption_config", value=encryption_config, expected_type=type_hints["encryption_config"])
            check_type(argname="argument investigation_group_policy", value=investigation_group_policy, expected_type=type_hints["investigation_group_policy"])
            check_type(argname="argument is_cloud_trail_event_history_enabled", value=is_cloud_trail_event_history_enabled, expected_type=type_hints["is_cloud_trail_event_history_enabled"])
            check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument tag_key_boundaries", value=tag_key_boundaries, expected_type=type_hints["tag_key_boundaries"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if chatbot_notification_channels is not None:
            self._values["chatbot_notification_channels"] = chatbot_notification_channels
        if cross_account_configurations is not None:
            self._values["cross_account_configurations"] = cross_account_configurations
        if encryption_config is not None:
            self._values["encryption_config"] = encryption_config
        if investigation_group_policy is not None:
            self._values["investigation_group_policy"] = investigation_group_policy
        if is_cloud_trail_event_history_enabled is not None:
            self._values["is_cloud_trail_event_history_enabled"] = is_cloud_trail_event_history_enabled
        if retention_in_days is not None:
            self._values["retention_in_days"] = retention_in_days
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if tag_key_boundaries is not None:
            self._values["tag_key_boundaries"] = tag_key_boundaries
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''Specify either the name or the ARN of the investigation group that you want to view.

        This is used to set the name of the investigation group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aiops-investigationgroup.html#cfn-aiops-investigationgroup-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def chatbot_notification_channels(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInvestigationGroup.ChatbotNotificationChannelProperty]]]]:
        '''Use this property to integrate CloudWatch investigations with chat applications.

        This property is an array. For the first string, specify the ARN of an Amazon SNS topic. For the array of strings, specify the ARNs of one or more chat applications configurations that you want to associate with that topic. For more information about these configuration ARNs, see `Getting started with Amazon Q in chat applications <https://docs.aws.amazon.com/chatbot/latest/adminguide/getting-started.html>`_ and `Resource type defined by AWS Chatbot <https://docs.aws.amazon.com/service-authorization/latest/reference/list_awschatbot.html#awschatbot-resources-for-iam-policies>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aiops-investigationgroup.html#cfn-aiops-investigationgroup-chatbotnotificationchannels
        '''
        result = self._values.get("chatbot_notification_channels")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInvestigationGroup.ChatbotNotificationChannelProperty]]]], result)

    @builtins.property
    def cross_account_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInvestigationGroup.CrossAccountConfigurationProperty]]]]:
        '''List of ``sourceRoleArn`` values that have been configured for cross-account access.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aiops-investigationgroup.html#cfn-aiops-investigationgroup-crossaccountconfigurations
        '''
        result = self._values.get("cross_account_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInvestigationGroup.CrossAccountConfigurationProperty]]]], result)

    @builtins.property
    def encryption_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInvestigationGroup.EncryptionConfigMapProperty]]:
        '''Specifies the customer managed AWS KMS key that the investigation group uses to encrypt data, if there is one.

        If not, the investigation group uses an AWS key to encrypt the data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aiops-investigationgroup.html#cfn-aiops-investigationgroup-encryptionconfig
        '''
        result = self._values.get("encryption_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInvestigationGroup.EncryptionConfigMapProperty]], result)

    @builtins.property
    def investigation_group_policy(self) -> typing.Optional[builtins.str]:
        '''Returns the JSON of the IAM resource policy associated with the specified investigation group in a string.

        For example, ``{\\"Version\\":\\"2012-10-17\\",\\"Statement\\":[{\\"Effect\\":\\"Allow\\",\\"Principal\\":{\\"Service\\":\\"aiops.alarms.cloudwatch.amazonaws.com\\"},\\"Action\\":[\\"aiops:CreateInvestigation\\",\\"aiops:CreateInvestigationEvent\\"],\\"Resource\\":\\"*\\",\\"Condition\\":{\\"StringEquals\\":{\\"aws:SourceAccount\\":\\"111122223333\\"},\\"ArnLike\\":{\\"aws:SourceArn\\":\\"arn:aws:cloudwatch:us-east-1:111122223333:alarm:*\\"}}}]}`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aiops-investigationgroup.html#cfn-aiops-investigationgroup-investigationgrouppolicy
        '''
        result = self._values.get("investigation_group_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_cloud_trail_event_history_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specify ``true`` to enable CloudWatch investigations to have access to change events that are recorded by CloudTrail.

        The default is ``true`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aiops-investigationgroup.html#cfn-aiops-investigationgroup-iscloudtraileventhistoryenabled
        '''
        result = self._values.get("is_cloud_trail_event_history_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def retention_in_days(self) -> typing.Optional[jsii.Number]:
        '''Specifies how long that investigation data is kept.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aiops-investigationgroup.html#cfn-aiops-investigationgroup-retentionindays
        '''
        result = self._values.get("retention_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IAM role that the investigation group uses for permissions to gather data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aiops-investigationgroup.html#cfn-aiops-investigationgroup-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_key_boundaries(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Displays the custom tag keys for custom applications in your system that you have specified in the investigation group.

        Resource tags help CloudWatch investigations narrow the search space when it is unable to discover definite relationships between resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aiops-investigationgroup.html#cfn-aiops-investigationgroup-tagkeyboundaries
        '''
        result = self._values.get("tag_key_boundaries")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value pairs to associate with the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aiops-investigationgroup.html#cfn-aiops-investigationgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInvestigationGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnInvestigationGroup",
    "CfnInvestigationGroupProps",
]

publication.publish()

def _typecheckingstub__f390e65acdf4efe0289b1b8e5f17c031f7a88a13963effed34b7d4944b31dd7e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    chatbot_notification_channels: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInvestigationGroup.ChatbotNotificationChannelProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    cross_account_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInvestigationGroup.CrossAccountConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    encryption_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInvestigationGroup.EncryptionConfigMapProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    investigation_group_policy: typing.Optional[builtins.str] = None,
    is_cloud_trail_event_history_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    retention_in_days: typing.Optional[jsii.Number] = None,
    role_arn: typing.Optional[builtins.str] = None,
    tag_key_boundaries: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a532233685b19239d88980a7d9b4a8384450db2dc5593ebca70b4c1bca8faf14(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ada159a27791012fd3d77245257dddda16f3719a8e4bd5e53e293ff27dceacb7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68d7a3472d5ddc810dbc073636686c470b0fe6568b144fc7473b578e828715b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5db4331534a87e764a8534aad930983f78144efc39dc99f450b39b9adabfe898(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInvestigationGroup.ChatbotNotificationChannelProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cab3f68c7637d356559913c4b9be139738c64bd676003ea2810dd4ddafef47e5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInvestigationGroup.CrossAccountConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f51c34e4f09d967ae3c411a2743d3d857ce2c925f1d1b67c9152dd736522694(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInvestigationGroup.EncryptionConfigMapProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a878340860e2c35de4d03b82df1e97245d5f40120fa110076a32f436fd31ddaf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fc3a119f870dceec4d1a3ba5b4f84971973ad9c990d3aa7c5bb5e2ff0005cba(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb70ecd162c324b07d0ae455e2881185c11d02912ce9513cd8fd61e7de3c054c(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3eb82bc9999595315778658f89b708e57ad701088d012c3391ce1a4e6721195(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__847e58d896c672f6db334949abc5da531a40f943b791ff6c76da0751ee7be4ea(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58e4b2d8c71fc2670bc24a5f274e0134fae9ffd7aeca95db0fed9e2d974499f7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d67ba65a7634fe2bf96859c6a05258a6565faf2372426edac2b3d876dc0b9a61(
    *,
    chat_configuration_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    sns_topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__686ab8dd38f6db168aebbeef0e137fd1f90381f42a12046db10e4ba4ac3a3e3f(
    *,
    source_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__822047880bb03db9129836b4da0b735fe316364e02aa10f8c042ba4d22f3c20f(
    *,
    encryption_configuration_type: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d8bd4c8e0b3c95e52387aa0647c4f184b5f07925a09f1e74881b8a0738d25a8(
    *,
    name: builtins.str,
    chatbot_notification_channels: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInvestigationGroup.ChatbotNotificationChannelProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    cross_account_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInvestigationGroup.CrossAccountConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    encryption_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInvestigationGroup.EncryptionConfigMapProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    investigation_group_policy: typing.Optional[builtins.str] = None,
    is_cloud_trail_event_history_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    retention_in_days: typing.Optional[jsii.Number] = None,
    role_arn: typing.Optional[builtins.str] = None,
    tag_key_boundaries: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
