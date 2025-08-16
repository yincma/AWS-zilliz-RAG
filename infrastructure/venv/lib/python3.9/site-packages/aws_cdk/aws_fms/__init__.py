r'''
# AWS::FMS Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_fms as fms
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for FMS construct libraries](https://constructs.dev/search?q=fms)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::FMS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_FMS.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::FMS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_FMS.html).

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
    ITaggable as _ITaggable_36806126,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnNotificationChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_fms.CfnNotificationChannel",
):
    '''Designates the IAM role and Amazon Simple Notification Service (SNS) topic to use to record SNS logs.

    To perform this action outside of the console, you must configure the SNS topic to allow the role ``AWSServiceRoleForFMS`` to publish SNS logs. For more information, see `Firewall Manager required permissions for API actions <https://docs.aws.amazon.com/waf/latest/developerguide/fms-api-permissions-ref.html>`_ in the *AWS Firewall Manager Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html
    :cloudformationResource: AWS::FMS::NotificationChannel
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_fms as fms
        
        cfn_notification_channel = fms.CfnNotificationChannel(self, "MyCfnNotificationChannel",
            sns_role_name="snsRoleName",
            sns_topic_arn="snsTopicArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        sns_role_name: builtins.str,
        sns_topic_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param sns_role_name: The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record AWS Firewall Manager activity.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the SNS topic that collects notifications from AWS Firewall Manager .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a03e25c676e3f843e7365938075353612a65a3a2bd2538074f016448b29053c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNotificationChannelProps(
            sns_role_name=sns_role_name, sns_topic_arn=sns_topic_arn
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eae25dcbfb8d4710a66ea0f6804d609f2c8fbb762e291caa42156e2d5e0a5ccd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__27e0110b31984037127ddfc8639de3754907e90f7485cfd5b43a5fbe4ad39717)
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
    @jsii.member(jsii_name="snsRoleName")
    def sns_role_name(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record AWS Firewall Manager activity.'''
        return typing.cast(builtins.str, jsii.get(self, "snsRoleName"))

    @sns_role_name.setter
    def sns_role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00bd3c5f6e0b7d08ecc3e9d3f09ce0486f75f4e24649a6e59140bdaa48e6e9ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsRoleName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the SNS topic that collects notifications from AWS Firewall Manager .'''
        return typing.cast(builtins.str, jsii.get(self, "snsTopicArn"))

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d5dd2548355a1129e0085759bb293de343519fe581ead5c659ceff8ec36b346)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicArn", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_fms.CfnNotificationChannelProps",
    jsii_struct_bases=[],
    name_mapping={"sns_role_name": "snsRoleName", "sns_topic_arn": "snsTopicArn"},
)
class CfnNotificationChannelProps:
    def __init__(
        self,
        *,
        sns_role_name: builtins.str,
        sns_topic_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnNotificationChannel``.

        :param sns_role_name: The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record AWS Firewall Manager activity.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the SNS topic that collects notifications from AWS Firewall Manager .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_fms as fms
            
            cfn_notification_channel_props = fms.CfnNotificationChannelProps(
                sns_role_name="snsRoleName",
                sns_topic_arn="snsTopicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5624e06a5ce62823c414e320e35e25799cfeb05a7db7fa7dc3f5353d1e0fe469)
            check_type(argname="argument sns_role_name", value=sns_role_name, expected_type=type_hints["sns_role_name"])
            check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sns_role_name": sns_role_name,
            "sns_topic_arn": sns_topic_arn,
        }

    @builtins.property
    def sns_role_name(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that allows Amazon SNS to record AWS Firewall Manager activity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snsrolename
        '''
        result = self._values.get("sns_role_name")
        assert result is not None, "Required property 'sns_role_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sns_topic_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the SNS topic that collects notifications from AWS Firewall Manager .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snstopicarn
        '''
        result = self._values.get("sns_topic_arn")
        assert result is not None, "Required property 'sns_topic_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNotificationChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_fms.CfnPolicy",
):
    '''An AWS Firewall Manager policy.

    A Firewall Manager policy is specific to the individual policy type. If you want to enforce multiple policy types across accounts, you can create multiple policies. You can create more than one policy for each type.

    If you add a new account to an organization that you created with AWS Organizations , Firewall Manager automatically applies the policy to the resources in that account that are within scope of the policy.

    Policies require some setup to use. For more information, see the sections on prerequisites and getting started under `Firewall Manager prerequisites <https://docs.aws.amazon.com/waf/latest/developerguide/fms-prereq.html>`_ .

    Firewall Manager provides the following types of policies:

    - *AWS WAF policy* - This policy applies AWS WAF web ACL protections to specified accounts and resources.
    - *Shield Advanced policy* - This policy applies Shield Advanced protection to specified accounts and resources.
    - *Security Groups policy* - This type of policy gives you control over security groups that are in use throughout your organization in AWS Organizations and lets you enforce a baseline set of rules across your organization.
    - *Network ACL policy* - This type of policy gives you control over the network ACLs that are in use throughout your organization in AWS Organizations and lets you enforce a baseline set of first and last network ACL rules across your organization.
    - *Network Firewall policy* - This policy applies Network Firewall protection to your organization's VPCs.
    - *DNS Firewall policy* - This policy applies Amazon Route 53 Resolver DNS Firewall protections to your organization's VPCs.
    - *Third-party firewall policy* - This policy applies third-party firewall protections. Third-party firewalls are available by subscription through the AWS Marketplace console at `AWS Marketplace <https://docs.aws.amazon.com/marketplace>`_ .
    - *Palo Alto Networks Cloud NGFW policy* - This policy applies Palo Alto Networks Cloud Next Generation Firewall (NGFW) protections and Palo Alto Networks Cloud NGFW rulestacks to your organization's VPCs.
    - *Fortigate CNF policy* - This policy applies Fortigate Cloud Native Firewall (CNF) protections. Fortigate CNF is a cloud-centered solution that blocks Zero-Day threats and secures cloud infrastructures with industry-leading advanced threat prevention, smart web application firewalls (WAF), and API protection.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html
    :cloudformationResource: AWS::FMS::Policy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_fms as fms
        
        cfn_policy = fms.CfnPolicy(self, "MyCfnPolicy",
            exclude_resource_tags=False,
            policy_name="policyName",
            remediation_enabled=False,
            security_service_policy_data=fms.CfnPolicy.SecurityServicePolicyDataProperty(
                type="type",
        
                # the properties below are optional
                managed_service_data="managedServiceData",
                policy_option=fms.CfnPolicy.PolicyOptionProperty(
                    network_acl_common_policy=fms.CfnPolicy.NetworkAclCommonPolicyProperty(
                        network_acl_entry_set=fms.CfnPolicy.NetworkAclEntrySetProperty(
                            force_remediate_for_first_entries=False,
                            force_remediate_for_last_entries=False,
        
                            # the properties below are optional
                            first_entries=[fms.CfnPolicy.NetworkAclEntryProperty(
                                egress=False,
                                protocol="protocol",
                                rule_action="ruleAction",
        
                                # the properties below are optional
                                cidr_block="cidrBlock",
                                icmp_type_code=fms.CfnPolicy.IcmpTypeCodeProperty(
                                    code=123,
                                    type=123
                                ),
                                ipv6_cidr_block="ipv6CidrBlock",
                                port_range=fms.CfnPolicy.PortRangeProperty(
                                    from=123,
                                    to=123
                                )
                            )],
                            last_entries=[fms.CfnPolicy.NetworkAclEntryProperty(
                                egress=False,
                                protocol="protocol",
                                rule_action="ruleAction",
        
                                # the properties below are optional
                                cidr_block="cidrBlock",
                                icmp_type_code=fms.CfnPolicy.IcmpTypeCodeProperty(
                                    code=123,
                                    type=123
                                ),
                                ipv6_cidr_block="ipv6CidrBlock",
                                port_range=fms.CfnPolicy.PortRangeProperty(
                                    from=123,
                                    to=123
                                )
                            )]
                        )
                    ),
                    network_firewall_policy=fms.CfnPolicy.NetworkFirewallPolicyProperty(
                        firewall_deployment_model="firewallDeploymentModel"
                    ),
                    third_party_firewall_policy=fms.CfnPolicy.ThirdPartyFirewallPolicyProperty(
                        firewall_deployment_model="firewallDeploymentModel"
                    )
                )
            ),
        
            # the properties below are optional
            delete_all_policy_resources=False,
            exclude_map={
                "account": ["account"],
                "orgunit": ["orgunit"]
            },
            include_map={
                "account": ["account"],
                "orgunit": ["orgunit"]
            },
            policy_description="policyDescription",
            resources_clean_up=False,
            resource_set_ids=["resourceSetIds"],
            resource_tag_logical_operator="resourceTagLogicalOperator",
            resource_tags=[fms.CfnPolicy.ResourceTagProperty(
                key="key",
        
                # the properties below are optional
                value="value"
            )],
            resource_type="resourceType",
            resource_type_list=["resourceTypeList"],
            tags=[fms.CfnPolicy.PolicyTagProperty(
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
        exclude_resource_tags: typing.Union[builtins.bool, _IResolvable_da3f097b],
        policy_name: builtins.str,
        remediation_enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        security_service_policy_data: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.SecurityServicePolicyDataProperty", typing.Dict[builtins.str, typing.Any]]],
        delete_all_policy_resources: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        exclude_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.IEMapProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        include_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.IEMapProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        policy_description: typing.Optional[builtins.str] = None,
        resources_clean_up: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        resource_set_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        resource_tag_logical_operator: typing.Optional[builtins.str] = None,
        resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.ResourceTagProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        resource_type: typing.Optional[builtins.str] = None,
        resource_type_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnPolicy.PolicyTagProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param exclude_resource_tags: Used only when tags are specified in the ``ResourceTags`` property. If this property is ``True`` , resources with the specified tags are not in scope of the policy. If it's ``False`` , only resources with the specified tags are in scope of the policy.
        :param policy_name: The name of the AWS Firewall Manager policy.
        :param remediation_enabled: Indicates if the policy should be automatically applied to new resources.
        :param security_service_policy_data: Details about the security service that is being used to protect the resources. This contains the following settings: - Type - Indicates the service type that the policy uses to protect the resource. For security group policies, Firewall Manager supports one security group for each common policy and for each content audit policy. This is an adjustable limit that you can increase by contacting . Valid values: ``DNS_FIREWALL`` | ``NETWORK_FIREWALL`` | ``SECURITY_GROUPS_COMMON`` | ``SECURITY_GROUPS_CONTENT_AUDIT`` | ``SECURITY_GROUPS_USAGE_AUDIT`` | ``SHIELD_ADVANCED`` | ``THIRD_PARTY_FIREWALL`` | ``WAFV2`` | ``WAF`` - ManagedServiceData - Details about the service that are specific to the service type, in JSON format. - Example: ``DNS_FIREWALL`` ``"{\\"type\\":\\"DNS_FIREWALL\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupId\\":\\"rslvr-frg-1\\",\\"priority\\":10}],\\"postProcessRuleGroups\\":[{\\"ruleGroupId\\":\\"rslvr-frg-2\\",\\"priority\\":9911}]}"`` .. epigraph:: Valid values for ``preProcessRuleGroups`` are between 1 and 99. Valid values for ``postProcessRuleGroups`` are between 9901 and 10000. - Example: ``NETWORK_FIREWALL`` - Centralized deployment model ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"awsNetworkFirewallConfig\\":{\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":true}},\\"firewallDeploymentModel\\":{\\"centralizedFirewallDeploymentModel\\":{\\"centralizedFirewallOrchestrationConfig\\":{\\"inspectionVpcIds\\":[{\\"resourceId\\":\\"vpc-1234\\",\\"accountId\\":\\"123456789011\\"}],\\"firewallCreationConfig\\":{\\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneId\\":null,\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]}]}},\\"allowedIPV4CidrList\\":[]}}}}"`` To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with automatic Availability Zone configuration ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\",\\"192.168.0.0/28\\"],\\"routeManagementAction\\":\\"OFF\\"},\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":true}}"`` With automatic Availbility Zone configuration, Firewall Manager chooses which Availability Zones to create the endpoints in. To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with automatic Availability Zone configuration and route management ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\",\\"192.168.0.0/28\\"],\\"routeManagementAction\\":\\"MONITOR\\",\\"routeManagementTargetTypes\\":[\\"InternetGateway\\"]},\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\": \\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":true}}"`` To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with custom Availability Zone configuration ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"fragmentcustomactionname\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\", \\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}},{\\"actionName\\":\\"fragmentcustomactionname\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"fragmentmetricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"firewallCreationConfig\\":{ \\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]},{\\"availabilityZoneName\\":\\"us-east-1b\\",\\"allowedIPV4CidrList\\":[ \\"10.0.0.0/28\\"]}]} },\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":null,\\"routeManagementAction\\":\\"OFF\\",\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":boolean}}"`` With custom Availability Zone configuration, you define which specific Availability Zones to create endpoints in by configuring ``firewallCreationConfig`` . To configure the Availability Zones in ``firewallCreationConfig`` , specify either the ``availabilityZoneName`` or ``availabilityZoneId`` parameter, not both parameters. To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with custom Availability Zone configuration and route management ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"fragmentcustomactionname\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}},{\\"actionName\\":\\"fragmentcustomactionname\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"fragmentmetricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"firewallCreationConfig\\":{\\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]},{\\"availabilityZoneName\\":\\"us-east-1b\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]}]}},\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":null,\\"routeManagementAction\\":\\"MONITOR\\",\\"routeManagementTargetTypes\\":[\\"InternetGateway\\"],\\"routeManagementConfig\\":{\\"allowCrossAZTrafficIfNoEndpoint\\":true}},\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":boolean}}"`` To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Example: ``THIRD_PARTY_FIREWALL`` - Palo Alto Networks Cloud Next-Generation Firewall centralized deployment model ``"{ \\"type\\":\\"THIRD_PARTY_FIREWALL\\", \\"thirdPartyFirewall\\":\\"PALO_ALTO_NETWORKS_CLOUD_NGFW\\", \\"thirdPartyFirewallConfig\\":{ \\"thirdPartyFirewallPolicyList\\":[\\"global-1\\"] },\\"firewallDeploymentModel\\":{\\"centralizedFirewallDeploymentModel\\":{\\"centralizedFirewallOrchestrationConfig\\":{\\"inspectionVpcIds\\":[{\\"resourceId\\":\\"vpc-1234\\",\\"accountId\\":\\"123456789011\\"}],\\"firewallCreationConfig\\":{\\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneId\\":null,\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]}]}},\\"allowedIPV4CidrList\\":[]}}}}"`` To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html>`_ to ``CENTRALIZED`` . - Example: ``THIRD_PARTY_FIREWALL`` - Palo Alto Networks Cloud Next-Generation Firewall distributed deployment model ``"{\\"type\\":\\"THIRD_PARTY_FIREWALL\\",\\"thirdPartyFirewall\\":\\"PALO_ALTO_NETWORKS_CLOUD_NGFW\\",\\"thirdPartyFirewallConfig\\":{\\"thirdPartyFirewallPolicyList\\":[\\"global-1\\"] },\\"firewallDeploymentModel\\":{ \\"distributedFirewallDeploymentModel\\":{ \\"distributedFirewallOrchestrationConfig\\":{\\"firewallCreationConfig\\":{\\"endpointLocation\\":{ \\"availabilityZoneConfigList\\":[ {\\"availabilityZoneName\\":\\"${AvailabilityZone}\\" } ] } }, \\"allowedIPV4CidrList\\":[ ] } } } }"`` To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Specification for ``SHIELD_ADVANCED`` for Amazon CloudFront distributions ``"{\\"type\\":\\"SHIELD_ADVANCED\\",\\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED|IGNORED|DISABLED\\", \\"automaticResponseAction\\":\\"BLOCK|COUNT\\"}, \\"overrideCustomerWebaclClassic\\":true|false}"`` For example: ``"{\\"type\\":\\"SHIELD_ADVANCED\\",\\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED\\", \\"automaticResponseAction\\":\\"COUNT\\"}}"`` The default value for ``automaticResponseStatus`` is ``IGNORED`` . The value for ``automaticResponseAction`` is only required when ``automaticResponseStatus`` is set to ``ENABLED`` . The default value for ``overrideCustomerWebaclClassic`` is ``false`` . For other resource types that you can protect with a Shield Advanced policy, this ``ManagedServiceData`` configuration is an empty string. - Example: ``WAFV2`` ``"{\\"type\\":\\"WAFV2\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupArn\\":null,\\"overrideAction\\":{\\"type\\":\\"NONE\\"},\\"managedRuleGroupIdentifier\\":{\\"version\\":null,\\"vendorName\\":\\"AWS\\",\\"managedRuleGroupName\\":\\"AWSManagedRulesAmazonIpReputationList\\"},\\"ruleGroupType\\":\\"ManagedRuleGroup\\",\\"excludeRules\\":[{\\"name\\":\\"NoUserAgent_HEADER\\"}]}],\\"postProcessRuleGroups\\":[],\\"defaultAction\\":{\\"type\\":\\"ALLOW\\"},\\"overrideCustomerWebACLAssociation\\":false,\\"loggingConfiguration\\":{\\"logDestinationConfigs\\":[\\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\\"],\\"redactedFields\\":[{\\"redactedFieldType\\":\\"SingleHeader\\",\\"redactedFieldValue\\":\\"Cookies\\"},{\\"redactedFieldType\\":\\"Method\\"}]}}"`` In the ``loggingConfiguration`` , you can specify one ``logDestinationConfigs`` , you can optionally provide up to 20 ``redactedFields`` , and the ``RedactedFieldType`` must be one of ``URI`` , ``QUERY_STRING`` , ``HEADER`` , or ``METHOD`` . - Example: ``AWS WAF Classic`` ``"{\\"type\\": \\"WAF\\", \\"ruleGroups\\": [{\\"id\\":\\"12345678-1bcd-9012-efga-0987654321ab\\", \\"overrideAction\\" : {\\"type\\": \\"COUNT\\"}}], \\"defaultAction\\": {\\"type\\": \\"BLOCK\\"}}"`` - Example: ``WAFV2`` - AWS Firewall Manager support for AWS WAF managed rule group versioning ``"{\\"type\\":\\"WAFV2\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupArn\\":null,\\"overrideAction\\":{\\"type\\":\\"NONE\\"},\\"managedRuleGroupIdentifier\\":{\\"versionEnabled\\":true,\\"version\\":\\"Version_2.0\\",\\"vendorName\\":\\"AWS\\",\\"managedRuleGroupName\\":\\"AWSManagedRulesCommonRuleSet\\"},\\"ruleGroupType\\":\\"ManagedRuleGroup\\",\\"excludeRules\\":[{\\"name\\":\\"NoUserAgent_HEADER\\"}]}],\\"postProcessRuleGroups\\":[],\\"defaultAction\\":{\\"type\\":\\"ALLOW\\"},\\"overrideCustomerWebACLAssociation\\":false,\\"loggingConfiguration\\":{\\"logDestinationConfigs\\":[\\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\\"],\\"redactedFields\\":[{\\"redactedFieldType\\":\\"SingleHeader\\",\\"redactedFieldValue\\":\\"Cookies\\"},{\\"redactedFieldType\\":\\"Method\\"}]}}"`` To use a specific version of a AWS WAF managed rule group in your Firewall Manager policy, you must set ``versionEnabled`` to ``true`` , and set ``version`` to the version you'd like to use. If you don't set ``versionEnabled`` to ``true`` , or if you omit ``versionEnabled`` , then Firewall Manager uses the default version of the AWS WAF managed rule group. - Example: ``SECURITY_GROUPS_COMMON`` ``"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false, \\"applyToAllEC2InstanceENIs\\":false,\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd\\"}]}"`` - Example: Shared VPCs. Apply the preceding policy to resources in shared VPCs as well as to those in VPCs that the account owns ``"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false, \\"applyToAllEC2InstanceENIs\\":false,\\"includeSharedVPC\\":true,\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd\\"}]}"`` - Example: ``SECURITY_GROUPS_CONTENT_AUDIT`` ``"{\\"type\\":\\"SECURITY_GROUPS_CONTENT_AUDIT\\",\\"securityGroups\\":[{\\"id\\":\\"sg-000e55995d61a06bd\\"}],\\"securityGroupAction\\":{\\"type\\":\\"ALLOW\\"}}"`` The security group action for content audit can be ``ALLOW`` or ``DENY`` . For ``ALLOW`` , all in-scope security group rules must be within the allowed range of the policy's security group rules. For ``DENY`` , all in-scope security group rules must not contain a value or a range that matches a rule value or range in the policy security group. - Example: ``SECURITY_GROUPS_USAGE_AUDIT`` ``"{\\"type\\":\\"SECURITY_GROUPS_USAGE_AUDIT\\",\\"deleteUnusedSecurityGroups\\":true,\\"coalesceRedundantSecurityGroups\\":true}"``
        :param delete_all_policy_resources: Used when deleting a policy. If ``true`` , Firewall Manager performs cleanup according to the policy type. For AWS WAF and Shield Advanced policies, Firewall Manager does the following: - Deletes rule groups created by Firewall Manager - Removes web ACLs from in-scope resources - Deletes web ACLs that contain no rules or rule groups For security group policies, Firewall Manager does the following for each security group in the policy: - Disassociates the security group from in-scope resources - Deletes the security group if it was created through Firewall Manager and if it's no longer associated with any resources through another policy After the cleanup, in-scope resources are no longer protected by web ACLs in this policy. Protection of out-of-scope resources remains unchanged. Scope is determined by tags that you create and accounts that you associate with the policy. When creating the policy, if you specify that only resources in specific accounts or with specific tags are in scope of the policy, those accounts and resources are handled by the policy. All others are out of scope. If you don't specify tags or accounts, all resources are in scope.
        :param exclude_map: Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to exclude from the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time. You can specify inclusions or exclusions, but not both. If you specify an ``IncludeMap`` , AWS Firewall Manager applies the policy to all accounts specified by the ``IncludeMap`` , and does not evaluate any ``ExcludeMap`` specifications. If you do not specify an ``IncludeMap`` , then Firewall Manager applies the policy to all accounts except for those specified by the ``ExcludeMap`` . You can specify account IDs, OUs, or a combination: - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` . - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` . - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .
        :param include_map: Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to include in the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time. You can specify inclusions or exclusions, but not both. If you specify an ``IncludeMap`` , AWS Firewall Manager applies the policy to all accounts specified by the ``IncludeMap`` , and does not evaluate any ``ExcludeMap`` specifications. If you do not specify an ``IncludeMap`` , then Firewall Manager applies the policy to all accounts except for those specified by the ``ExcludeMap`` . You can specify account IDs, OUs, or a combination: - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` . - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` . - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .
        :param policy_description: Your description of the AWS Firewall Manager policy.
        :param resources_clean_up: Indicates whether AWS Firewall Manager should automatically remove protections from resources that leave the policy scope and clean up resources that Firewall Manager is managing for accounts when those accounts leave policy scope. For example, Firewall Manager will disassociate a Firewall Manager managed web ACL from a protected customer resource when the customer resource leaves policy scope. By default, Firewall Manager doesn't remove protections or delete Firewall Manager managed resources. This option is not available for Shield Advanced or AWS WAF Classic policies.
        :param resource_set_ids: The unique identifiers of the resource sets used by the policy.
        :param resource_tag_logical_operator: Specifies whether to combine multiple resource tags with AND, so that a resource must have all tags to be included or excluded, or OR, so that a resource must have at least one tag. Default: ``AND``
        :param resource_tags: An array of ``ResourceTag`` objects, used to explicitly include resources in the policy scope or explicitly exclude them. If this isn't set, then tags aren't used to modify policy scope. See also ``ExcludeResourceTags`` .
        :param resource_type: The type of resource protected by or in scope of the policy. This is in the format shown in the `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`_ . To apply this policy to multiple resource types, specify a resource type of ``ResourceTypeList`` and then specify the resource types in a ``ResourceTypeList`` . The following are valid resource types for each Firewall Manager policy type: - AWS WAF Classic - ``AWS::ApiGateway::Stage`` , ``AWS::CloudFront::Distribution`` , and ``AWS::ElasticLoadBalancingV2::LoadBalancer`` . - AWS WAF - ``AWS::ApiGateway::Stage`` , ``AWS::ElasticLoadBalancingV2::LoadBalancer`` , and ``AWS::CloudFront::Distribution`` . - Shield Advanced - ``AWS::ElasticLoadBalancingV2::LoadBalancer`` , ``AWS::ElasticLoadBalancing::LoadBalancer`` , ``AWS::EC2::EIP`` , and ``AWS::CloudFront::Distribution`` . - Network ACL - ``AWS::EC2::Subnet`` . - Security group usage audit - ``AWS::EC2::SecurityGroup`` . - Security group content audit - ``AWS::EC2::SecurityGroup`` , ``AWS::EC2::NetworkInterface`` , and ``AWS::EC2::Instance`` . - DNS Firewall, AWS Network Firewall , and third-party firewall - ``AWS::EC2::VPC`` .
        :param resource_type_list: An array of ``ResourceType`` objects. Use this only to specify multiple resource types. To specify a single resource type, use ``ResourceType`` .
        :param tags: A collection of key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a29b3b13041b0ccbd18a0c29ff5cff0adbc0e2aedc87591f1c54ec7a1fc830b4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPolicyProps(
            exclude_resource_tags=exclude_resource_tags,
            policy_name=policy_name,
            remediation_enabled=remediation_enabled,
            security_service_policy_data=security_service_policy_data,
            delete_all_policy_resources=delete_all_policy_resources,
            exclude_map=exclude_map,
            include_map=include_map,
            policy_description=policy_description,
            resources_clean_up=resources_clean_up,
            resource_set_ids=resource_set_ids,
            resource_tag_logical_operator=resource_tag_logical_operator,
            resource_tags=resource_tags,
            resource_type=resource_type,
            resource_type_list=resource_type_list,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bd3d819ff879695091ea1782c6d44919a2d5d60ac904eb958a4baa5a9b7b105)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b5336d629941f59b9bc57ae2f0f9086302ff307956a981d17c0c74f56e281a98)
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
        '''The Amazon Resource Name (ARN) of the policy.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the policy.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="excludeResourceTags")
    def exclude_resource_tags(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Used only when tags are specified in the ``ResourceTags`` property.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "excludeResourceTags"))

    @exclude_resource_tags.setter
    def exclude_resource_tags(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20a6c43cec956bc22ae07e19e1af4001c23e93faad6ca1043a917bf0f5dcfc1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeResourceTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''The name of the AWS Firewall Manager policy.'''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62ed5a312383f144ece33d5d7f925fd2a4d83062b6024f0b02b573273b2f360d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="remediationEnabled")
    def remediation_enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Indicates if the policy should be automatically applied to new resources.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "remediationEnabled"))

    @remediation_enabled.setter
    def remediation_enabled(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce24f414c17fee1c6464201d3595af0f5eddf30ec4dc5532e27f42a5a60bfba0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remediationEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityServicePolicyData")
    def security_service_policy_data(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnPolicy.SecurityServicePolicyDataProperty"]:
        '''Details about the security service that is being used to protect the resources.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPolicy.SecurityServicePolicyDataProperty"], jsii.get(self, "securityServicePolicyData"))

    @security_service_policy_data.setter
    def security_service_policy_data(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnPolicy.SecurityServicePolicyDataProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c28ba46bb386f4176af9e17ecbe45582b554c7807d38f2929fb3fd7a81f3976)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityServicePolicyData", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deleteAllPolicyResources")
    def delete_all_policy_resources(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Used when deleting a policy.

        If ``true`` , Firewall Manager performs cleanup according to the policy type.
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "deleteAllPolicyResources"))

    @delete_all_policy_resources.setter
    def delete_all_policy_resources(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fe798b33151903c0017cb9d94013617a6afcad058e7ae0fe54c9cfd6dd679c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteAllPolicyResources", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="excludeMap")
    def exclude_map(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.IEMapProperty"]]:
        '''Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to exclude from the policy.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.IEMapProperty"]], jsii.get(self, "excludeMap"))

    @exclude_map.setter
    def exclude_map(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.IEMapProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8f8c8d7be71d632f5fd707992c674dd52c74761a09f147830413fcfba30c273)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeMap", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="includeMap")
    def include_map(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.IEMapProperty"]]:
        '''Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to include in the policy.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.IEMapProperty"]], jsii.get(self, "includeMap"))

    @include_map.setter
    def include_map(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.IEMapProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94290c92cb339b7d588eedc5f7e4693403e89224115f954743aa8b94e5920b0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeMap", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policyDescription")
    def policy_description(self) -> typing.Optional[builtins.str]:
        '''Your description of the AWS Firewall Manager policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyDescription"))

    @policy_description.setter
    def policy_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aba01c3384f02d2b5b8393ae170165a3fcecf0b67864bb9240d39b4518cee92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDescription", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourcesCleanUp")
    def resources_clean_up(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether AWS Firewall Manager should automatically remove protections from resources that leave the policy scope and clean up resources that Firewall Manager is managing for accounts when those accounts leave policy scope.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "resourcesCleanUp"))

    @resources_clean_up.setter
    def resources_clean_up(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12534b322db922dabec65a01e84b63ba7b3a489d9d25d5870fef80727d31a5c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourcesCleanUp", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceSetIds")
    def resource_set_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The unique identifiers of the resource sets used by the policy.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceSetIds"))

    @resource_set_ids.setter
    def resource_set_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__048e93c726f9c5fe6e9b627c041b37e3458add761a76189dddf42b880fc049a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceSetIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceTagLogicalOperator")
    def resource_tag_logical_operator(self) -> typing.Optional[builtins.str]:
        '''Specifies whether to combine multiple resource tags with AND, so that a resource must have all tags to be included or excluded, or OR, so that a resource must have at least one tag.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceTagLogicalOperator"))

    @resource_tag_logical_operator.setter
    def resource_tag_logical_operator(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c785568d3275bbfb3df2dd3b2ac1d97319f9c06330a57289261dce85d69868f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTagLogicalOperator", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPolicy.ResourceTagProperty"]]]]:
        '''An array of ``ResourceTag`` objects, used to explicitly include resources in the policy scope or explicitly exclude them.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPolicy.ResourceTagProperty"]]]], jsii.get(self, "resourceTags"))

    @resource_tags.setter
    def resource_tags(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPolicy.ResourceTagProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c77d40603d6f4c051dd3f9b5d662e1b2f8b3690fcfa612876de86b1cfb05ac0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> typing.Optional[builtins.str]:
        '''The type of resource protected by or in scope of the policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45fbd20db788e5f26784bca772c0c150d7f583f3b21916156a9f85bdbbbd064d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceTypeList")
    def resource_type_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of ``ResourceType`` objects.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceTypeList"))

    @resource_type_list.setter
    def resource_type_list(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__defb2e92d0f62de49ea900ef5497c0bb92b81e991fe094bca77e0bc3225a174e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTypeList", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnPolicy.PolicyTagProperty"]]:
        '''A collection of key:value pairs associated with an AWS resource.'''
        return typing.cast(typing.Optional[typing.List["CfnPolicy.PolicyTagProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnPolicy.PolicyTagProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e61b60deb504fb101d8b3c5d4d91824672d7a44fdd9537dec8f729c7d34256be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.IEMapProperty",
        jsii_struct_bases=[],
        name_mapping={"account": "account", "orgunit": "orgunit"},
    )
    class IEMapProperty:
        def __init__(
            self,
            *,
            account: typing.Optional[typing.Sequence[builtins.str]] = None,
            orgunit: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to include in or exclude from the policy.

            Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.

            This is used for the policy's ``IncludeMap`` and ``ExcludeMap`` .

            You can specify account IDs, OUs, or a combination:

            - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .
            - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` .
            - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .

            :param account: The account list for the map.
            :param orgunit: The organizational unit list for the map.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                i_eMap_property = {
                    "account": ["account"],
                    "orgunit": ["orgunit"]
                }
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6bcb551e43b08ef4828de279b99e59a3954c4cdc19c8adfe6bf93e810ce36917)
                check_type(argname="argument account", value=account, expected_type=type_hints["account"])
                check_type(argname="argument orgunit", value=orgunit, expected_type=type_hints["orgunit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if account is not None:
                self._values["account"] = account
            if orgunit is not None:
                self._values["orgunit"] = orgunit

        @builtins.property
        def account(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The account list for the map.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-account
            '''
            result = self._values.get("account")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def orgunit(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The organizational unit list for the map.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-orgunit
            '''
            result = self._values.get("orgunit")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IEMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.IcmpTypeCodeProperty",
        jsii_struct_bases=[],
        name_mapping={"code": "code", "type": "type"},
    )
    class IcmpTypeCodeProperty:
        def __init__(self, *, code: jsii.Number, type: jsii.Number) -> None:
            '''ICMP protocol: The ICMP type and code.

            :param code: ICMP code.
            :param type: ICMP type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-icmptypecode.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                icmp_type_code_property = fms.CfnPolicy.IcmpTypeCodeProperty(
                    code=123,
                    type=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__65b9cc6166ca508cd4c5ab4d066ea459564143dea548a99b579d93e51f574165)
                check_type(argname="argument code", value=code, expected_type=type_hints["code"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "code": code,
                "type": type,
            }

        @builtins.property
        def code(self) -> jsii.Number:
            '''ICMP code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-icmptypecode.html#cfn-fms-policy-icmptypecode-code
            '''
            result = self._values.get("code")
            assert result is not None, "Required property 'code' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def type(self) -> jsii.Number:
            '''ICMP type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-icmptypecode.html#cfn-fms-policy-icmptypecode-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IcmpTypeCodeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.NetworkAclCommonPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"network_acl_entry_set": "networkAclEntrySet"},
    )
    class NetworkAclCommonPolicyProperty:
        def __init__(
            self,
            *,
            network_acl_entry_set: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.NetworkAclEntrySetProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Defines a Firewall Manager network ACL policy.

            This is used in the ``PolicyOption`` of a ``SecurityServicePolicyData`` for a ``Policy`` , when the ``SecurityServicePolicyData`` type is set to ``NETWORK_ACL_COMMON`` .

            For information about network ACLs, see `Control traffic to subnets using network ACLs <https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html>`_ in the *Amazon Virtual Private Cloud User Guide* .

            :param network_acl_entry_set: The definition of the first and last rules for the network ACL policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclcommonpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                network_acl_common_policy_property = fms.CfnPolicy.NetworkAclCommonPolicyProperty(
                    network_acl_entry_set=fms.CfnPolicy.NetworkAclEntrySetProperty(
                        force_remediate_for_first_entries=False,
                        force_remediate_for_last_entries=False,
                
                        # the properties below are optional
                        first_entries=[fms.CfnPolicy.NetworkAclEntryProperty(
                            egress=False,
                            protocol="protocol",
                            rule_action="ruleAction",
                
                            # the properties below are optional
                            cidr_block="cidrBlock",
                            icmp_type_code=fms.CfnPolicy.IcmpTypeCodeProperty(
                                code=123,
                                type=123
                            ),
                            ipv6_cidr_block="ipv6CidrBlock",
                            port_range=fms.CfnPolicy.PortRangeProperty(
                                from=123,
                                to=123
                            )
                        )],
                        last_entries=[fms.CfnPolicy.NetworkAclEntryProperty(
                            egress=False,
                            protocol="protocol",
                            rule_action="ruleAction",
                
                            # the properties below are optional
                            cidr_block="cidrBlock",
                            icmp_type_code=fms.CfnPolicy.IcmpTypeCodeProperty(
                                code=123,
                                type=123
                            ),
                            ipv6_cidr_block="ipv6CidrBlock",
                            port_range=fms.CfnPolicy.PortRangeProperty(
                                from=123,
                                to=123
                            )
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6dfc57cc41dc1d1b1ebbc44d2e08c4db8913dbb8d25d9bff92c2c760de2fdc82)
                check_type(argname="argument network_acl_entry_set", value=network_acl_entry_set, expected_type=type_hints["network_acl_entry_set"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "network_acl_entry_set": network_acl_entry_set,
            }

        @builtins.property
        def network_acl_entry_set(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnPolicy.NetworkAclEntrySetProperty"]:
            '''The definition of the first and last rules for the network ACL policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclcommonpolicy.html#cfn-fms-policy-networkaclcommonpolicy-networkaclentryset
            '''
            result = self._values.get("network_acl_entry_set")
            assert result is not None, "Required property 'network_acl_entry_set' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPolicy.NetworkAclEntrySetProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkAclCommonPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.NetworkAclEntryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "egress": "egress",
            "protocol": "protocol",
            "rule_action": "ruleAction",
            "cidr_block": "cidrBlock",
            "icmp_type_code": "icmpTypeCode",
            "ipv6_cidr_block": "ipv6CidrBlock",
            "port_range": "portRange",
        },
    )
    class NetworkAclEntryProperty:
        def __init__(
            self,
            *,
            egress: typing.Union[builtins.bool, _IResolvable_da3f097b],
            protocol: builtins.str,
            rule_action: builtins.str,
            cidr_block: typing.Optional[builtins.str] = None,
            icmp_type_code: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.IcmpTypeCodeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ipv6_cidr_block: typing.Optional[builtins.str] = None,
            port_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.PortRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes a rule in a network ACL.

            Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining
            whether a packet should be allowed in or out of a subnet associated with the network ACL, AWS processes the entries in the network ACL according to the rule numbers, in ascending order.

            When you manage an individual network ACL, you explicitly specify the rule numbers. When you specify the network ACL rules in a Firewall Manager policy, you provide the rules to run first, in the order that you want them to run, and the rules to run last, in the order that you want them to run. Firewall Manager assigns the rule numbers for you when you save the network ACL policy specification.

            :param egress: Indicates whether the rule is an egress, or outbound, rule (applied to traffic leaving the subnet). If it's not an egress rule, then it's an ingress, or inbound, rule.
            :param protocol: The protocol number. A value of "-1" means all protocols.
            :param rule_action: Indicates whether to allow or deny the traffic that matches the rule.
            :param cidr_block: The IPv4 network range to allow or deny, in CIDR notation.
            :param icmp_type_code: ICMP protocol: The ICMP type and code.
            :param ipv6_cidr_block: The IPv6 network range to allow or deny, in CIDR notation.
            :param port_range: TCP or UDP protocols: The range of ports the rule applies to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                network_acl_entry_property = fms.CfnPolicy.NetworkAclEntryProperty(
                    egress=False,
                    protocol="protocol",
                    rule_action="ruleAction",
                
                    # the properties below are optional
                    cidr_block="cidrBlock",
                    icmp_type_code=fms.CfnPolicy.IcmpTypeCodeProperty(
                        code=123,
                        type=123
                    ),
                    ipv6_cidr_block="ipv6CidrBlock",
                    port_range=fms.CfnPolicy.PortRangeProperty(
                        from=123,
                        to=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7a315c8565b94dd4f1c73bc5bb6afd0ade3bc8461a7c74c1098d0d7f66076bf4)
                check_type(argname="argument egress", value=egress, expected_type=type_hints["egress"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument rule_action", value=rule_action, expected_type=type_hints["rule_action"])
                check_type(argname="argument cidr_block", value=cidr_block, expected_type=type_hints["cidr_block"])
                check_type(argname="argument icmp_type_code", value=icmp_type_code, expected_type=type_hints["icmp_type_code"])
                check_type(argname="argument ipv6_cidr_block", value=ipv6_cidr_block, expected_type=type_hints["ipv6_cidr_block"])
                check_type(argname="argument port_range", value=port_range, expected_type=type_hints["port_range"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "egress": egress,
                "protocol": protocol,
                "rule_action": rule_action,
            }
            if cidr_block is not None:
                self._values["cidr_block"] = cidr_block
            if icmp_type_code is not None:
                self._values["icmp_type_code"] = icmp_type_code
            if ipv6_cidr_block is not None:
                self._values["ipv6_cidr_block"] = ipv6_cidr_block
            if port_range is not None:
                self._values["port_range"] = port_range

        @builtins.property
        def egress(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether the rule is an egress, or outbound, rule (applied to traffic leaving the subnet).

            If it's not an egress rule, then it's an ingress, or inbound, rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclentry.html#cfn-fms-policy-networkaclentry-egress
            '''
            result = self._values.get("egress")
            assert result is not None, "Required property 'egress' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The protocol number.

            A value of "-1" means all protocols.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclentry.html#cfn-fms-policy-networkaclentry-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def rule_action(self) -> builtins.str:
            '''Indicates whether to allow or deny the traffic that matches the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclentry.html#cfn-fms-policy-networkaclentry-ruleaction
            '''
            result = self._values.get("rule_action")
            assert result is not None, "Required property 'rule_action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cidr_block(self) -> typing.Optional[builtins.str]:
            '''The IPv4 network range to allow or deny, in CIDR notation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclentry.html#cfn-fms-policy-networkaclentry-cidrblock
            '''
            result = self._values.get("cidr_block")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def icmp_type_code(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.IcmpTypeCodeProperty"]]:
            '''ICMP protocol: The ICMP type and code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclentry.html#cfn-fms-policy-networkaclentry-icmptypecode
            '''
            result = self._values.get("icmp_type_code")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.IcmpTypeCodeProperty"]], result)

        @builtins.property
        def ipv6_cidr_block(self) -> typing.Optional[builtins.str]:
            '''The IPv6 network range to allow or deny, in CIDR notation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclentry.html#cfn-fms-policy-networkaclentry-ipv6cidrblock
            '''
            result = self._values.get("ipv6_cidr_block")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port_range(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.PortRangeProperty"]]:
            '''TCP or UDP protocols: The range of ports the rule applies to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclentry.html#cfn-fms-policy-networkaclentry-portrange
            '''
            result = self._values.get("port_range")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.PortRangeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkAclEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.NetworkAclEntrySetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "force_remediate_for_first_entries": "forceRemediateForFirstEntries",
            "force_remediate_for_last_entries": "forceRemediateForLastEntries",
            "first_entries": "firstEntries",
            "last_entries": "lastEntries",
        },
    )
    class NetworkAclEntrySetProperty:
        def __init__(
            self,
            *,
            force_remediate_for_first_entries: typing.Union[builtins.bool, _IResolvable_da3f097b],
            force_remediate_for_last_entries: typing.Union[builtins.bool, _IResolvable_da3f097b],
            first_entries: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.NetworkAclEntryProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            last_entries: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.NetworkAclEntryProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The configuration of the first and last rules for the network ACL policy, and the remediation settings for each.

            :param force_remediate_for_first_entries: Applies only when remediation is enabled for the policy as a whole. Firewall Manager uses this setting when it finds policy violations that involve conflicts between the custom entries and the policy entries. If forced remediation is disabled, Firewall Manager marks the network ACL as noncompliant and does not try to remediate. For more information about the remediation behavior, see `Remediation for managed network ACLs <https://docs.aws.amazon.com/waf/latest/developerguide/network-acl-policies.html#network-acls-remediation>`_ in the *AWS Firewall Manager Developer Guide* .
            :param force_remediate_for_last_entries: Applies only when remediation is enabled for the policy as a whole. Firewall Manager uses this setting when it finds policy violations that involve conflicts between the custom entries and the policy entries. If forced remediation is disabled, Firewall Manager marks the network ACL as noncompliant and does not try to remediate. For more information about the remediation behavior, see `Remediation for managed network ACLs <https://docs.aws.amazon.com/waf/latest/developerguide/network-acl-policies.html#network-acls-remediation>`_ in the *AWS Firewall Manager Developer Guide* .
            :param first_entries: The rules that you want to run first in the Firewall Manager managed network ACLs. .. epigraph:: Provide these in the order in which you want them to run. Firewall Manager will assign the specific rule numbers for you, in the network ACLs that it creates. You must specify at least one first entry or one last entry in any network ACL policy.
            :param last_entries: The rules that you want to run last in the Firewall Manager managed network ACLs. .. epigraph:: Provide these in the order in which you want them to run. Firewall Manager will assign the specific rule numbers for you, in the network ACLs that it creates. You must specify at least one first entry or one last entry in any network ACL policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclentryset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                network_acl_entry_set_property = fms.CfnPolicy.NetworkAclEntrySetProperty(
                    force_remediate_for_first_entries=False,
                    force_remediate_for_last_entries=False,
                
                    # the properties below are optional
                    first_entries=[fms.CfnPolicy.NetworkAclEntryProperty(
                        egress=False,
                        protocol="protocol",
                        rule_action="ruleAction",
                
                        # the properties below are optional
                        cidr_block="cidrBlock",
                        icmp_type_code=fms.CfnPolicy.IcmpTypeCodeProperty(
                            code=123,
                            type=123
                        ),
                        ipv6_cidr_block="ipv6CidrBlock",
                        port_range=fms.CfnPolicy.PortRangeProperty(
                            from=123,
                            to=123
                        )
                    )],
                    last_entries=[fms.CfnPolicy.NetworkAclEntryProperty(
                        egress=False,
                        protocol="protocol",
                        rule_action="ruleAction",
                
                        # the properties below are optional
                        cidr_block="cidrBlock",
                        icmp_type_code=fms.CfnPolicy.IcmpTypeCodeProperty(
                            code=123,
                            type=123
                        ),
                        ipv6_cidr_block="ipv6CidrBlock",
                        port_range=fms.CfnPolicy.PortRangeProperty(
                            from=123,
                            to=123
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b2907f7090b00fafcfa0eb4f641b098a7fa37436ba6c4ffff2dafc1595c81a6e)
                check_type(argname="argument force_remediate_for_first_entries", value=force_remediate_for_first_entries, expected_type=type_hints["force_remediate_for_first_entries"])
                check_type(argname="argument force_remediate_for_last_entries", value=force_remediate_for_last_entries, expected_type=type_hints["force_remediate_for_last_entries"])
                check_type(argname="argument first_entries", value=first_entries, expected_type=type_hints["first_entries"])
                check_type(argname="argument last_entries", value=last_entries, expected_type=type_hints["last_entries"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "force_remediate_for_first_entries": force_remediate_for_first_entries,
                "force_remediate_for_last_entries": force_remediate_for_last_entries,
            }
            if first_entries is not None:
                self._values["first_entries"] = first_entries
            if last_entries is not None:
                self._values["last_entries"] = last_entries

        @builtins.property
        def force_remediate_for_first_entries(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Applies only when remediation is enabled for the policy as a whole.

            Firewall Manager uses this setting when it finds policy violations that involve conflicts between the custom entries and the policy entries.

            If forced remediation is disabled, Firewall Manager marks the network ACL as noncompliant and does not try to remediate. For more information about the remediation behavior, see `Remediation for managed network ACLs <https://docs.aws.amazon.com/waf/latest/developerguide/network-acl-policies.html#network-acls-remediation>`_ in the *AWS Firewall Manager Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclentryset.html#cfn-fms-policy-networkaclentryset-forceremediateforfirstentries
            '''
            result = self._values.get("force_remediate_for_first_entries")
            assert result is not None, "Required property 'force_remediate_for_first_entries' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def force_remediate_for_last_entries(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Applies only when remediation is enabled for the policy as a whole.

            Firewall Manager uses this setting when it finds policy violations that involve conflicts between the custom entries and the policy entries.

            If forced remediation is disabled, Firewall Manager marks the network ACL as noncompliant and does not try to remediate. For more information about the remediation behavior, see `Remediation for managed network ACLs <https://docs.aws.amazon.com/waf/latest/developerguide/network-acl-policies.html#network-acls-remediation>`_ in the *AWS Firewall Manager Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclentryset.html#cfn-fms-policy-networkaclentryset-forceremediateforlastentries
            '''
            result = self._values.get("force_remediate_for_last_entries")
            assert result is not None, "Required property 'force_remediate_for_last_entries' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def first_entries(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPolicy.NetworkAclEntryProperty"]]]]:
            '''The rules that you want to run first in the Firewall Manager managed network ACLs.

            .. epigraph::

               Provide these in the order in which you want them to run. Firewall Manager will assign the specific rule numbers for you, in the network ACLs that it creates.

            You must specify at least one first entry or one last entry in any network ACL policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclentryset.html#cfn-fms-policy-networkaclentryset-firstentries
            '''
            result = self._values.get("first_entries")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPolicy.NetworkAclEntryProperty"]]]], result)

        @builtins.property
        def last_entries(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPolicy.NetworkAclEntryProperty"]]]]:
            '''The rules that you want to run last in the Firewall Manager managed network ACLs.

            .. epigraph::

               Provide these in the order in which you want them to run. Firewall Manager will assign the specific rule numbers for you, in the network ACLs that it creates.

            You must specify at least one first entry or one last entry in any network ACL policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkaclentryset.html#cfn-fms-policy-networkaclentryset-lastentries
            '''
            result = self._values.get("last_entries")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPolicy.NetworkAclEntryProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkAclEntrySetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.NetworkFirewallPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"firewall_deployment_model": "firewallDeploymentModel"},
    )
    class NetworkFirewallPolicyProperty:
        def __init__(self, *, firewall_deployment_model: builtins.str) -> None:
            '''Configures the firewall policy deployment model of AWS Network Firewall .

            For information about Network Firewall deployment models, see `AWS Network Firewall example architectures with routing <https://docs.aws.amazon.com/network-firewall/latest/developerguide/architectures.html>`_ in the *Network Firewall Developer Guide* .

            :param firewall_deployment_model: Defines the deployment model to use for the firewall policy. To use a distributed model, set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html>`_ to ``DISTRIBUTED`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                network_firewall_policy_property = fms.CfnPolicy.NetworkFirewallPolicyProperty(
                    firewall_deployment_model="firewallDeploymentModel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1dee79c6872a0421399375d5fc2757431881011031a81ccd6674040de21bac13)
                check_type(argname="argument firewall_deployment_model", value=firewall_deployment_model, expected_type=type_hints["firewall_deployment_model"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "firewall_deployment_model": firewall_deployment_model,
            }

        @builtins.property
        def firewall_deployment_model(self) -> builtins.str:
            '''Defines the deployment model to use for the firewall policy.

            To use a distributed model, set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html>`_ to ``DISTRIBUTED`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html#cfn-fms-policy-networkfirewallpolicy-firewalldeploymentmodel
            '''
            result = self._values.get("firewall_deployment_model")
            assert result is not None, "Required property 'firewall_deployment_model' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkFirewallPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.PolicyOptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "network_acl_common_policy": "networkAclCommonPolicy",
            "network_firewall_policy": "networkFirewallPolicy",
            "third_party_firewall_policy": "thirdPartyFirewallPolicy",
        },
    )
    class PolicyOptionProperty:
        def __init__(
            self,
            *,
            network_acl_common_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.NetworkAclCommonPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            network_firewall_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.NetworkFirewallPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            third_party_firewall_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.ThirdPartyFirewallPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains the settings to configure a network ACL policy, a AWS Network Firewall firewall policy deployment model, or a third-party firewall policy.

            :param network_acl_common_policy: Defines a Firewall Manager network ACL policy.
            :param network_firewall_policy: Defines the deployment model to use for the firewall policy.
            :param third_party_firewall_policy: Defines the policy options for a third-party firewall policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policyoption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                policy_option_property = fms.CfnPolicy.PolicyOptionProperty(
                    network_acl_common_policy=fms.CfnPolicy.NetworkAclCommonPolicyProperty(
                        network_acl_entry_set=fms.CfnPolicy.NetworkAclEntrySetProperty(
                            force_remediate_for_first_entries=False,
                            force_remediate_for_last_entries=False,
                
                            # the properties below are optional
                            first_entries=[fms.CfnPolicy.NetworkAclEntryProperty(
                                egress=False,
                                protocol="protocol",
                                rule_action="ruleAction",
                
                                # the properties below are optional
                                cidr_block="cidrBlock",
                                icmp_type_code=fms.CfnPolicy.IcmpTypeCodeProperty(
                                    code=123,
                                    type=123
                                ),
                                ipv6_cidr_block="ipv6CidrBlock",
                                port_range=fms.CfnPolicy.PortRangeProperty(
                                    from=123,
                                    to=123
                                )
                            )],
                            last_entries=[fms.CfnPolicy.NetworkAclEntryProperty(
                                egress=False,
                                protocol="protocol",
                                rule_action="ruleAction",
                
                                # the properties below are optional
                                cidr_block="cidrBlock",
                                icmp_type_code=fms.CfnPolicy.IcmpTypeCodeProperty(
                                    code=123,
                                    type=123
                                ),
                                ipv6_cidr_block="ipv6CidrBlock",
                                port_range=fms.CfnPolicy.PortRangeProperty(
                                    from=123,
                                    to=123
                                )
                            )]
                        )
                    ),
                    network_firewall_policy=fms.CfnPolicy.NetworkFirewallPolicyProperty(
                        firewall_deployment_model="firewallDeploymentModel"
                    ),
                    third_party_firewall_policy=fms.CfnPolicy.ThirdPartyFirewallPolicyProperty(
                        firewall_deployment_model="firewallDeploymentModel"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5979520d8e95acd573ee171b00e0dcba3be3872b80af53615d64bc000f703299)
                check_type(argname="argument network_acl_common_policy", value=network_acl_common_policy, expected_type=type_hints["network_acl_common_policy"])
                check_type(argname="argument network_firewall_policy", value=network_firewall_policy, expected_type=type_hints["network_firewall_policy"])
                check_type(argname="argument third_party_firewall_policy", value=third_party_firewall_policy, expected_type=type_hints["third_party_firewall_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if network_acl_common_policy is not None:
                self._values["network_acl_common_policy"] = network_acl_common_policy
            if network_firewall_policy is not None:
                self._values["network_firewall_policy"] = network_firewall_policy
            if third_party_firewall_policy is not None:
                self._values["third_party_firewall_policy"] = third_party_firewall_policy

        @builtins.property
        def network_acl_common_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.NetworkAclCommonPolicyProperty"]]:
            '''Defines a Firewall Manager network ACL policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policyoption.html#cfn-fms-policy-policyoption-networkaclcommonpolicy
            '''
            result = self._values.get("network_acl_common_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.NetworkAclCommonPolicyProperty"]], result)

        @builtins.property
        def network_firewall_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.NetworkFirewallPolicyProperty"]]:
            '''Defines the deployment model to use for the firewall policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policyoption.html#cfn-fms-policy-policyoption-networkfirewallpolicy
            '''
            result = self._values.get("network_firewall_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.NetworkFirewallPolicyProperty"]], result)

        @builtins.property
        def third_party_firewall_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.ThirdPartyFirewallPolicyProperty"]]:
            '''Defines the policy options for a third-party firewall policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policyoption.html#cfn-fms-policy-policyoption-thirdpartyfirewallpolicy
            '''
            result = self._values.get("third_party_firewall_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.ThirdPartyFirewallPolicyProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.PolicyTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class PolicyTagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''A collection of key:value pairs associated with an AWS resource.

            The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.

            :param key: Part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as "customer." Tag keys are case-sensitive.
            :param value: Part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as "companyA" or "companyB." Tag values are case-sensitive.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                policy_tag_property = fms.CfnPolicy.PolicyTagProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d5ee16e00771d59c6939cbdec3cdf3c57cdb9a09a7e914e3faf7baaa7416d62)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''Part of the key:value pair that defines a tag.

            You can use a tag key to describe a category of information, such as "customer." Tag keys are case-sensitive.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html#cfn-fms-policy-policytag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''Part of the key:value pair that defines a tag.

            You can use a tag value to describe a specific value within a category, such as "companyA" or "companyB." Tag values are case-sensitive.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html#cfn-fms-policy-policytag-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.PortRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"from_": "from", "to": "to"},
    )
    class PortRangeProperty:
        def __init__(self, *, from_: jsii.Number, to: jsii.Number) -> None:
            '''TCP or UDP protocols: The range of ports the rule applies to.

            :param from_: The beginning port number of the range.
            :param to: The ending port number of the range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-portrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                port_range_property = fms.CfnPolicy.PortRangeProperty(
                    from=123,
                    to=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fbc1cd0112a3be4230fd0e2a96f8a5e7799f9f8c3925aad80c6eef4a1172da43)
                check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
                check_type(argname="argument to", value=to, expected_type=type_hints["to"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "from_": from_,
                "to": to,
            }

        @builtins.property
        def from_(self) -> jsii.Number:
            '''The beginning port number of the range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-portrange.html#cfn-fms-policy-portrange-from
            '''
            result = self._values.get("from_")
            assert result is not None, "Required property 'from_' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def to(self) -> jsii.Number:
            '''The ending port number of the range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-portrange.html#cfn-fms-policy-portrange-to
            '''
            result = self._values.get("to")
            assert result is not None, "Required property 'to' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.ResourceTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ResourceTagProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The resource tags that AWS Firewall Manager uses to determine if a particular resource should be included or excluded from the AWS Firewall Manager policy.

            Tags enable you to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value. Firewall Manager combines the tags with "AND" so that, if you add more than one tag to a policy scope, a resource must have all the specified tags to be included or excluded. For more information, see `Working with Tag Editor <https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html>`_ .

            :param key: The resource tag key.
            :param value: The resource tag value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                resource_tag_property = fms.CfnPolicy.ResourceTagProperty(
                    key="key",
                
                    # the properties below are optional
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1533af324aea7be8b3e806a7d4a851c48bea2139cd3bb0ce1cc81ff86e976487)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
            }
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> builtins.str:
            '''The resource tag key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html#cfn-fms-policy-resourcetag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The resource tag value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html#cfn-fms-policy-resourcetag-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.SecurityServicePolicyDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "managed_service_data": "managedServiceData",
            "policy_option": "policyOption",
        },
    )
    class SecurityServicePolicyDataProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            managed_service_data: typing.Optional[builtins.str] = None,
            policy_option: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.PolicyOptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Details about the security service that is being used to protect the resources.

            :param type: The service that the policy is using to protect the resources. This specifies the type of policy that is created, either an AWS WAF policy, a Shield Advanced policy, or a security group policy. For security group policies, Firewall Manager supports one security group for each common policy and for each content audit policy. This is an adjustable limit that you can increase by contacting SUPlong .
            :param managed_service_data: Details about the service that are specific to the service type, in JSON format. - Example: ``DNS_FIREWALL`` ``"{\\"type\\":\\"DNS_FIREWALL\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupId\\":\\"rslvr-frg-1\\",\\"priority\\":10}],\\"postProcessRuleGroups\\":[{\\"ruleGroupId\\":\\"rslvr-frg-2\\",\\"priority\\":9911}]}"`` .. epigraph:: Valid values for ``preProcessRuleGroups`` are between 1 and 99. Valid values for ``postProcessRuleGroups`` are between 9901 and 10000. - Example: ``NETWORK_FIREWALL`` - Centralized deployment model ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"awsNetworkFirewallConfig\\":{\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":true}},\\"firewallDeploymentModel\\":{\\"centralizedFirewallDeploymentModel\\":{\\"centralizedFirewallOrchestrationConfig\\":{\\"inspectionVpcIds\\":[{\\"resourceId\\":\\"vpc-1234\\",\\"accountId\\":\\"123456789011\\"}],\\"firewallCreationConfig\\":{\\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneId\\":null,\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]}]}},\\"allowedIPV4CidrList\\":[]}}}}"`` To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with automatic Availability Zone configuration ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\",\\"192.168.0.0/28\\"],\\"routeManagementAction\\":\\"OFF\\"},\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":true}}"`` With automatic Availbility Zone configuration, Firewall Manager chooses which Availability Zones to create the endpoints in. To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with automatic Availability Zone configuration and route management ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\",\\"192.168.0.0/28\\"],\\"routeManagementAction\\":\\"MONITOR\\",\\"routeManagementTargetTypes\\":[\\"InternetGateway\\"]},\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\": \\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":true}}"`` To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with custom Availability Zone configuration ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"fragmentcustomactionname\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\", \\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}},{\\"actionName\\":\\"fragmentcustomactionname\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"fragmentmetricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"firewallCreationConfig\\":{ \\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]},{\\"availabilityZoneName\\":\\"us-east-1b\\",\\"allowedIPV4CidrList\\":[ \\"10.0.0.0/28\\"]}]} },\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":null,\\"routeManagementAction\\":\\"OFF\\",\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":boolean}}"`` With custom Availability Zone configuration, you define which specific Availability Zones to create endpoints in by configuring ``firewallCreationConfig`` . To configure the Availability Zones in ``firewallCreationConfig`` , specify either the ``availabilityZoneName`` or ``availabilityZoneId`` parameter, not both parameters. To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with custom Availability Zone configuration and route management ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"fragmentcustomactionname\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}},{\\"actionName\\":\\"fragmentcustomactionname\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"fragmentmetricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"firewallCreationConfig\\":{\\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]},{\\"availabilityZoneName\\":\\"us-east-1b\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]}]}},\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":null,\\"routeManagementAction\\":\\"MONITOR\\",\\"routeManagementTargetTypes\\":[\\"InternetGateway\\"],\\"routeManagementConfig\\":{\\"allowCrossAZTrafficIfNoEndpoint\\":true}},\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":boolean}}"`` To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Example: ``THIRD_PARTY_FIREWALL`` - Palo Alto Networks Cloud Next-Generation Firewall centralized deployment model ``"{ \\"type\\":\\"THIRD_PARTY_FIREWALL\\", \\"thirdPartyFirewall\\":\\"PALO_ALTO_NETWORKS_CLOUD_NGFW\\", \\"thirdPartyFirewallConfig\\":{ \\"thirdPartyFirewallPolicyList\\":[\\"global-1\\"] },\\"firewallDeploymentModel\\":{\\"centralizedFirewallDeploymentModel\\":{\\"centralizedFirewallOrchestrationConfig\\":{\\"inspectionVpcIds\\":[{\\"resourceId\\":\\"vpc-1234\\",\\"accountId\\":\\"123456789011\\"}],\\"firewallCreationConfig\\":{\\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneId\\":null,\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]}]}},\\"allowedIPV4CidrList\\":[]}}}}"`` To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html>`_ to ``CENTRALIZED`` . - Example: ``THIRD_PARTY_FIREWALL`` - Palo Alto Networks Cloud Next-Generation Firewall distributed deployment model ``"{\\"type\\":\\"THIRD_PARTY_FIREWALL\\",\\"thirdPartyFirewall\\":\\"PALO_ALTO_NETWORKS_CLOUD_NGFW\\",\\"thirdPartyFirewallConfig\\":{\\"thirdPartyFirewallPolicyList\\":[\\"global-1\\"] },\\"firewallDeploymentModel\\":{ \\"distributedFirewallDeploymentModel\\":{ \\"distributedFirewallOrchestrationConfig\\":{\\"firewallCreationConfig\\":{\\"endpointLocation\\":{ \\"availabilityZoneConfigList\\":[ {\\"availabilityZoneName\\":\\"${AvailabilityZone}\\" } ] } }, \\"allowedIPV4CidrList\\":[ ] } } } }"`` To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Specification for ``SHIELD_ADVANCED`` for Amazon CloudFront distributions ``"{\\"type\\":\\"SHIELD_ADVANCED\\",\\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED|IGNORED|DISABLED\\", \\"automaticResponseAction\\":\\"BLOCK|COUNT\\"}, \\"overrideCustomerWebaclClassic\\":true|false}"`` For example: ``"{\\"type\\":\\"SHIELD_ADVANCED\\",\\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED\\", \\"automaticResponseAction\\":\\"COUNT\\"}}"`` The default value for ``automaticResponseStatus`` is ``IGNORED`` . The value for ``automaticResponseAction`` is only required when ``automaticResponseStatus`` is set to ``ENABLED`` . The default value for ``overrideCustomerWebaclClassic`` is ``false`` . For other resource types that you can protect with a Shield Advanced policy, this ``ManagedServiceData`` configuration is an empty string. - Example: ``WAFV2`` ``"{\\"type\\":\\"WAFV2\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupArn\\":null,\\"overrideAction\\":{\\"type\\":\\"NONE\\"},\\"managedRuleGroupIdentifier\\":{\\"version\\":null,\\"vendorName\\":\\"AWS\\",\\"managedRuleGroupName\\":\\"AWSManagedRulesAmazonIpReputationList\\"},\\"ruleGroupType\\":\\"ManagedRuleGroup\\",\\"excludeRules\\":[{\\"name\\":\\"NoUserAgent_HEADER\\"}]}],\\"postProcessRuleGroups\\":[],\\"defaultAction\\":{\\"type\\":\\"ALLOW\\"},\\"overrideCustomerWebACLAssociation\\":false,\\"loggingConfiguration\\":{\\"logDestinationConfigs\\":[\\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\\"],\\"redactedFields\\":[{\\"redactedFieldType\\":\\"SingleHeader\\",\\"redactedFieldValue\\":\\"Cookies\\"},{\\"redactedFieldType\\":\\"Method\\"}]}}"`` In the ``loggingConfiguration`` , you can specify one ``logDestinationConfigs`` , you can optionally provide up to 20 ``redactedFields`` , and the ``RedactedFieldType`` must be one of ``URI`` , ``QUERY_STRING`` , ``HEADER`` , or ``METHOD`` . - Example: ``AWS WAF Classic`` ``"{\\"type\\": \\"WAF\\", \\"ruleGroups\\": [{\\"id\\":\\"12345678-1bcd-9012-efga-0987654321ab\\", \\"overrideAction\\" : {\\"type\\": \\"COUNT\\"}}], \\"defaultAction\\": {\\"type\\": \\"BLOCK\\"}}"`` - Example: ``WAFV2`` - AWS Firewall Manager support for AWS WAF managed rule group versioning ``"{\\"type\\":\\"WAFV2\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupArn\\":null,\\"overrideAction\\":{\\"type\\":\\"NONE\\"},\\"managedRuleGroupIdentifier\\":{\\"versionEnabled\\":true,\\"version\\":\\"Version_2.0\\",\\"vendorName\\":\\"AWS\\",\\"managedRuleGroupName\\":\\"AWSManagedRulesCommonRuleSet\\"},\\"ruleGroupType\\":\\"ManagedRuleGroup\\",\\"excludeRules\\":[{\\"name\\":\\"NoUserAgent_HEADER\\"}]}],\\"postProcessRuleGroups\\":[],\\"defaultAction\\":{\\"type\\":\\"ALLOW\\"},\\"overrideCustomerWebACLAssociation\\":false,\\"loggingConfiguration\\":{\\"logDestinationConfigs\\":[\\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\\"],\\"redactedFields\\":[{\\"redactedFieldType\\":\\"SingleHeader\\",\\"redactedFieldValue\\":\\"Cookies\\"},{\\"redactedFieldType\\":\\"Method\\"}]}}"`` To use a specific version of a AWS WAF managed rule group in your Firewall Manager policy, you must set ``versionEnabled`` to ``true`` , and set ``version`` to the version you'd like to use. If you don't set ``versionEnabled`` to ``true`` , or if you omit ``versionEnabled`` , then Firewall Manager uses the default version of the AWS WAF managed rule group. - Example: ``SECURITY_GROUPS_COMMON`` ``"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false, \\"applyToAllEC2InstanceENIs\\":false,\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd\\"}]}"`` - Example: Shared VPCs. Apply the preceding policy to resources in shared VPCs as well as to those in VPCs that the account owns ``"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false, \\"applyToAllEC2InstanceENIs\\":false,\\"includeSharedVPC\\":true,\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd\\"}]}"`` - Example: ``SECURITY_GROUPS_CONTENT_AUDIT`` ``"{\\"type\\":\\"SECURITY_GROUPS_CONTENT_AUDIT\\",\\"securityGroups\\":[{\\"id\\":\\"sg-000e55995d61a06bd\\"}],\\"securityGroupAction\\":{\\"type\\":\\"ALLOW\\"}}"`` The security group action for content audit can be ``ALLOW`` or ``DENY`` . For ``ALLOW`` , all in-scope security group rules must be within the allowed range of the policy's security group rules. For ``DENY`` , all in-scope security group rules must not contain a value or a range that matches a rule value or range in the policy security group. - Example: ``SECURITY_GROUPS_USAGE_AUDIT`` ``"{\\"type\\":\\"SECURITY_GROUPS_USAGE_AUDIT\\",\\"deleteUnusedSecurityGroups\\":true,\\"coalesceRedundantSecurityGroups\\":true}"``
            :param policy_option: Contains the settings to configure a network ACL policy, a AWS Network Firewall firewall policy deployment model, or a third-party firewall policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                security_service_policy_data_property = fms.CfnPolicy.SecurityServicePolicyDataProperty(
                    type="type",
                
                    # the properties below are optional
                    managed_service_data="managedServiceData",
                    policy_option=fms.CfnPolicy.PolicyOptionProperty(
                        network_acl_common_policy=fms.CfnPolicy.NetworkAclCommonPolicyProperty(
                            network_acl_entry_set=fms.CfnPolicy.NetworkAclEntrySetProperty(
                                force_remediate_for_first_entries=False,
                                force_remediate_for_last_entries=False,
                
                                # the properties below are optional
                                first_entries=[fms.CfnPolicy.NetworkAclEntryProperty(
                                    egress=False,
                                    protocol="protocol",
                                    rule_action="ruleAction",
                
                                    # the properties below are optional
                                    cidr_block="cidrBlock",
                                    icmp_type_code=fms.CfnPolicy.IcmpTypeCodeProperty(
                                        code=123,
                                        type=123
                                    ),
                                    ipv6_cidr_block="ipv6CidrBlock",
                                    port_range=fms.CfnPolicy.PortRangeProperty(
                                        from=123,
                                        to=123
                                    )
                                )],
                                last_entries=[fms.CfnPolicy.NetworkAclEntryProperty(
                                    egress=False,
                                    protocol="protocol",
                                    rule_action="ruleAction",
                
                                    # the properties below are optional
                                    cidr_block="cidrBlock",
                                    icmp_type_code=fms.CfnPolicy.IcmpTypeCodeProperty(
                                        code=123,
                                        type=123
                                    ),
                                    ipv6_cidr_block="ipv6CidrBlock",
                                    port_range=fms.CfnPolicy.PortRangeProperty(
                                        from=123,
                                        to=123
                                    )
                                )]
                            )
                        ),
                        network_firewall_policy=fms.CfnPolicy.NetworkFirewallPolicyProperty(
                            firewall_deployment_model="firewallDeploymentModel"
                        ),
                        third_party_firewall_policy=fms.CfnPolicy.ThirdPartyFirewallPolicyProperty(
                            firewall_deployment_model="firewallDeploymentModel"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c049eeb7140522ded2ec5e8c352001a90a84400f6f8d601bcb6b17805b0a150e)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument managed_service_data", value=managed_service_data, expected_type=type_hints["managed_service_data"])
                check_type(argname="argument policy_option", value=policy_option, expected_type=type_hints["policy_option"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if managed_service_data is not None:
                self._values["managed_service_data"] = managed_service_data
            if policy_option is not None:
                self._values["policy_option"] = policy_option

        @builtins.property
        def type(self) -> builtins.str:
            '''The service that the policy is using to protect the resources.

            This specifies the type of policy that is created, either an AWS WAF policy, a Shield Advanced policy, or a security group policy. For security group policies, Firewall Manager supports one security group for each common policy and for each content audit policy. This is an adjustable limit that you can increase by contacting SUPlong .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html#cfn-fms-policy-securityservicepolicydata-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def managed_service_data(self) -> typing.Optional[builtins.str]:
            '''Details about the service that are specific to the service type, in JSON format.

            - Example: ``DNS_FIREWALL``

            ``"{\\"type\\":\\"DNS_FIREWALL\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupId\\":\\"rslvr-frg-1\\",\\"priority\\":10}],\\"postProcessRuleGroups\\":[{\\"ruleGroupId\\":\\"rslvr-frg-2\\",\\"priority\\":9911}]}"``
            .. epigraph::

               Valid values for ``preProcessRuleGroups`` are between 1 and 99. Valid values for ``postProcessRuleGroups`` are between 9901 and 10000.

            - Example: ``NETWORK_FIREWALL`` - Centralized deployment model

            ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"awsNetworkFirewallConfig\\":{\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":true}},\\"firewallDeploymentModel\\":{\\"centralizedFirewallDeploymentModel\\":{\\"centralizedFirewallOrchestrationConfig\\":{\\"inspectionVpcIds\\":[{\\"resourceId\\":\\"vpc-1234\\",\\"accountId\\":\\"123456789011\\"}],\\"firewallCreationConfig\\":{\\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneId\\":null,\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]}]}},\\"allowedIPV4CidrList\\":[]}}}}"``

            To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` .

            - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with automatic Availability Zone configuration

            ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\",\\"192.168.0.0/28\\"],\\"routeManagementAction\\":\\"OFF\\"},\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":true}}"``

            With automatic Availbility Zone configuration, Firewall Manager chooses which Availability Zones to create the endpoints in. To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` .

            - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with automatic Availability Zone configuration and route management

            ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\",\\"192.168.0.0/28\\"],\\"routeManagementAction\\":\\"MONITOR\\",\\"routeManagementTargetTypes\\":[\\"InternetGateway\\"]},\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\": \\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":true}}"``

            To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` .

            - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with custom Availability Zone configuration

            ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"fragmentcustomactionname\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\", \\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}},{\\"actionName\\":\\"fragmentcustomactionname\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"fragmentmetricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"firewallCreationConfig\\":{ \\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]},{\\"availabilityZoneName\\":\\"us-east-1b\\",\\"allowedIPV4CidrList\\":[ \\"10.0.0.0/28\\"]}]} },\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":null,\\"routeManagementAction\\":\\"OFF\\",\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":boolean}}"``

            With custom Availability Zone configuration, you define which specific Availability Zones to create endpoints in by configuring ``firewallCreationConfig`` . To configure the Availability Zones in ``firewallCreationConfig`` , specify either the ``availabilityZoneName`` or ``availabilityZoneId`` parameter, not both parameters.

            To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` .

            - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with custom Availability Zone configuration and route management

            ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"fragmentcustomactionname\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}},{\\"actionName\\":\\"fragmentcustomactionname\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"fragmentmetricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"firewallCreationConfig\\":{\\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]},{\\"availabilityZoneName\\":\\"us-east-1b\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]}]}},\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":null,\\"routeManagementAction\\":\\"MONITOR\\",\\"routeManagementTargetTypes\\":[\\"InternetGateway\\"],\\"routeManagementConfig\\":{\\"allowCrossAZTrafficIfNoEndpoint\\":true}},\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":boolean}}"``

            To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` .

            - Example: ``THIRD_PARTY_FIREWALL`` - Palo Alto Networks Cloud Next-Generation Firewall centralized deployment model

            ``"{ \\"type\\":\\"THIRD_PARTY_FIREWALL\\", \\"thirdPartyFirewall\\":\\"PALO_ALTO_NETWORKS_CLOUD_NGFW\\", \\"thirdPartyFirewallConfig\\":{ \\"thirdPartyFirewallPolicyList\\":[\\"global-1\\"] },\\"firewallDeploymentModel\\":{\\"centralizedFirewallDeploymentModel\\":{\\"centralizedFirewallOrchestrationConfig\\":{\\"inspectionVpcIds\\":[{\\"resourceId\\":\\"vpc-1234\\",\\"accountId\\":\\"123456789011\\"}],\\"firewallCreationConfig\\":{\\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneId\\":null,\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]}]}},\\"allowedIPV4CidrList\\":[]}}}}"``

            To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html>`_ to ``CENTRALIZED`` .

            - Example: ``THIRD_PARTY_FIREWALL`` - Palo Alto Networks Cloud Next-Generation Firewall distributed deployment model

            ``"{\\"type\\":\\"THIRD_PARTY_FIREWALL\\",\\"thirdPartyFirewall\\":\\"PALO_ALTO_NETWORKS_CLOUD_NGFW\\",\\"thirdPartyFirewallConfig\\":{\\"thirdPartyFirewallPolicyList\\":[\\"global-1\\"] },\\"firewallDeploymentModel\\":{ \\"distributedFirewallDeploymentModel\\":{ \\"distributedFirewallOrchestrationConfig\\":{\\"firewallCreationConfig\\":{\\"endpointLocation\\":{ \\"availabilityZoneConfigList\\":[ {\\"availabilityZoneName\\":\\"${AvailabilityZone}\\" } ] } }, \\"allowedIPV4CidrList\\":[ ] } } } }"``

            To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html>`_ to ``DISTRIBUTED`` .

            - Specification for ``SHIELD_ADVANCED`` for Amazon CloudFront distributions

            ``"{\\"type\\":\\"SHIELD_ADVANCED\\",\\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED|IGNORED|DISABLED\\", \\"automaticResponseAction\\":\\"BLOCK|COUNT\\"}, \\"overrideCustomerWebaclClassic\\":true|false}"``

            For example: ``"{\\"type\\":\\"SHIELD_ADVANCED\\",\\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED\\", \\"automaticResponseAction\\":\\"COUNT\\"}}"``

            The default value for ``automaticResponseStatus`` is ``IGNORED`` . The value for ``automaticResponseAction`` is only required when ``automaticResponseStatus`` is set to ``ENABLED`` . The default value for ``overrideCustomerWebaclClassic`` is ``false`` .

            For other resource types that you can protect with a Shield Advanced policy, this ``ManagedServiceData`` configuration is an empty string.

            - Example: ``WAFV2``

            ``"{\\"type\\":\\"WAFV2\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupArn\\":null,\\"overrideAction\\":{\\"type\\":\\"NONE\\"},\\"managedRuleGroupIdentifier\\":{\\"version\\":null,\\"vendorName\\":\\"AWS\\",\\"managedRuleGroupName\\":\\"AWSManagedRulesAmazonIpReputationList\\"},\\"ruleGroupType\\":\\"ManagedRuleGroup\\",\\"excludeRules\\":[{\\"name\\":\\"NoUserAgent_HEADER\\"}]}],\\"postProcessRuleGroups\\":[],\\"defaultAction\\":{\\"type\\":\\"ALLOW\\"},\\"overrideCustomerWebACLAssociation\\":false,\\"loggingConfiguration\\":{\\"logDestinationConfigs\\":[\\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\\"],\\"redactedFields\\":[{\\"redactedFieldType\\":\\"SingleHeader\\",\\"redactedFieldValue\\":\\"Cookies\\"},{\\"redactedFieldType\\":\\"Method\\"}]}}"``

            In the ``loggingConfiguration`` , you can specify one ``logDestinationConfigs`` , you can optionally provide up to 20 ``redactedFields`` , and the ``RedactedFieldType`` must be one of ``URI`` , ``QUERY_STRING`` , ``HEADER`` , or ``METHOD`` .

            - Example: ``AWS WAF Classic``

            ``"{\\"type\\": \\"WAF\\", \\"ruleGroups\\": [{\\"id\\":\\"12345678-1bcd-9012-efga-0987654321ab\\", \\"overrideAction\\" : {\\"type\\": \\"COUNT\\"}}], \\"defaultAction\\": {\\"type\\": \\"BLOCK\\"}}"``

            - Example: ``WAFV2`` - AWS Firewall Manager support for AWS WAF managed rule group versioning

            ``"{\\"type\\":\\"WAFV2\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupArn\\":null,\\"overrideAction\\":{\\"type\\":\\"NONE\\"},\\"managedRuleGroupIdentifier\\":{\\"versionEnabled\\":true,\\"version\\":\\"Version_2.0\\",\\"vendorName\\":\\"AWS\\",\\"managedRuleGroupName\\":\\"AWSManagedRulesCommonRuleSet\\"},\\"ruleGroupType\\":\\"ManagedRuleGroup\\",\\"excludeRules\\":[{\\"name\\":\\"NoUserAgent_HEADER\\"}]}],\\"postProcessRuleGroups\\":[],\\"defaultAction\\":{\\"type\\":\\"ALLOW\\"},\\"overrideCustomerWebACLAssociation\\":false,\\"loggingConfiguration\\":{\\"logDestinationConfigs\\":[\\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\\"],\\"redactedFields\\":[{\\"redactedFieldType\\":\\"SingleHeader\\",\\"redactedFieldValue\\":\\"Cookies\\"},{\\"redactedFieldType\\":\\"Method\\"}]}}"``

            To use a specific version of a AWS WAF managed rule group in your Firewall Manager policy, you must set ``versionEnabled`` to ``true`` , and set ``version`` to the version you'd like to use. If you don't set ``versionEnabled`` to ``true`` , or if you omit ``versionEnabled`` , then Firewall Manager uses the default version of the AWS WAF managed rule group.

            - Example: ``SECURITY_GROUPS_COMMON``

            ``"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false, \\"applyToAllEC2InstanceENIs\\":false,\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd\\"}]}"``

            - Example: Shared VPCs. Apply the preceding policy to resources in shared VPCs as well as to those in VPCs that the account owns

            ``"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false, \\"applyToAllEC2InstanceENIs\\":false,\\"includeSharedVPC\\":true,\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd\\"}]}"``

            - Example: ``SECURITY_GROUPS_CONTENT_AUDIT``

            ``"{\\"type\\":\\"SECURITY_GROUPS_CONTENT_AUDIT\\",\\"securityGroups\\":[{\\"id\\":\\"sg-000e55995d61a06bd\\"}],\\"securityGroupAction\\":{\\"type\\":\\"ALLOW\\"}}"``

            The security group action for content audit can be ``ALLOW`` or ``DENY`` . For ``ALLOW`` , all in-scope security group rules must be within the allowed range of the policy's security group rules. For ``DENY`` , all in-scope security group rules must not contain a value or a range that matches a rule value or range in the policy security group.

            - Example: ``SECURITY_GROUPS_USAGE_AUDIT``

            ``"{\\"type\\":\\"SECURITY_GROUPS_USAGE_AUDIT\\",\\"deleteUnusedSecurityGroups\\":true,\\"coalesceRedundantSecurityGroups\\":true}"``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html#cfn-fms-policy-securityservicepolicydata-managedservicedata
            '''
            result = self._values.get("managed_service_data")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def policy_option(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.PolicyOptionProperty"]]:
            '''Contains the settings to configure a network ACL policy, a AWS Network Firewall firewall policy deployment model, or a third-party firewall policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-securityservicepolicydata.html#cfn-fms-policy-securityservicepolicydata-policyoption
            '''
            result = self._values.get("policy_option")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.PolicyOptionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecurityServicePolicyDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_fms.CfnPolicy.ThirdPartyFirewallPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"firewall_deployment_model": "firewallDeploymentModel"},
    )
    class ThirdPartyFirewallPolicyProperty:
        def __init__(self, *, firewall_deployment_model: builtins.str) -> None:
            '''Configures the deployment model for the third-party firewall.

            :param firewall_deployment_model: Defines the deployment model to use for the third-party firewall policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_fms as fms
                
                third_party_firewall_policy_property = fms.CfnPolicy.ThirdPartyFirewallPolicyProperty(
                    firewall_deployment_model="firewallDeploymentModel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7f4a7c7a12ee187727472c21f2a6147ca000c43ae4d50b0ab60025dea29d98eb)
                check_type(argname="argument firewall_deployment_model", value=firewall_deployment_model, expected_type=type_hints["firewall_deployment_model"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "firewall_deployment_model": firewall_deployment_model,
            }

        @builtins.property
        def firewall_deployment_model(self) -> builtins.str:
            '''Defines the deployment model to use for the third-party firewall policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html#cfn-fms-policy-thirdpartyfirewallpolicy-firewalldeploymentmodel
            '''
            result = self._values.get("firewall_deployment_model")
            assert result is not None, "Required property 'firewall_deployment_model' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ThirdPartyFirewallPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_fms.CfnPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "exclude_resource_tags": "excludeResourceTags",
        "policy_name": "policyName",
        "remediation_enabled": "remediationEnabled",
        "security_service_policy_data": "securityServicePolicyData",
        "delete_all_policy_resources": "deleteAllPolicyResources",
        "exclude_map": "excludeMap",
        "include_map": "includeMap",
        "policy_description": "policyDescription",
        "resources_clean_up": "resourcesCleanUp",
        "resource_set_ids": "resourceSetIds",
        "resource_tag_logical_operator": "resourceTagLogicalOperator",
        "resource_tags": "resourceTags",
        "resource_type": "resourceType",
        "resource_type_list": "resourceTypeList",
        "tags": "tags",
    },
)
class CfnPolicyProps:
    def __init__(
        self,
        *,
        exclude_resource_tags: typing.Union[builtins.bool, _IResolvable_da3f097b],
        policy_name: builtins.str,
        remediation_enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        security_service_policy_data: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.SecurityServicePolicyDataProperty, typing.Dict[builtins.str, typing.Any]]],
        delete_all_policy_resources: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        exclude_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.IEMapProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        include_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.IEMapProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        policy_description: typing.Optional[builtins.str] = None,
        resources_clean_up: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        resource_set_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        resource_tag_logical_operator: typing.Optional[builtins.str] = None,
        resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        resource_type: typing.Optional[builtins.str] = None,
        resource_type_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnPolicy.PolicyTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPolicy``.

        :param exclude_resource_tags: Used only when tags are specified in the ``ResourceTags`` property. If this property is ``True`` , resources with the specified tags are not in scope of the policy. If it's ``False`` , only resources with the specified tags are in scope of the policy.
        :param policy_name: The name of the AWS Firewall Manager policy.
        :param remediation_enabled: Indicates if the policy should be automatically applied to new resources.
        :param security_service_policy_data: Details about the security service that is being used to protect the resources. This contains the following settings: - Type - Indicates the service type that the policy uses to protect the resource. For security group policies, Firewall Manager supports one security group for each common policy and for each content audit policy. This is an adjustable limit that you can increase by contacting . Valid values: ``DNS_FIREWALL`` | ``NETWORK_FIREWALL`` | ``SECURITY_GROUPS_COMMON`` | ``SECURITY_GROUPS_CONTENT_AUDIT`` | ``SECURITY_GROUPS_USAGE_AUDIT`` | ``SHIELD_ADVANCED`` | ``THIRD_PARTY_FIREWALL`` | ``WAFV2`` | ``WAF`` - ManagedServiceData - Details about the service that are specific to the service type, in JSON format. - Example: ``DNS_FIREWALL`` ``"{\\"type\\":\\"DNS_FIREWALL\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupId\\":\\"rslvr-frg-1\\",\\"priority\\":10}],\\"postProcessRuleGroups\\":[{\\"ruleGroupId\\":\\"rslvr-frg-2\\",\\"priority\\":9911}]}"`` .. epigraph:: Valid values for ``preProcessRuleGroups`` are between 1 and 99. Valid values for ``postProcessRuleGroups`` are between 9901 and 10000. - Example: ``NETWORK_FIREWALL`` - Centralized deployment model ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"awsNetworkFirewallConfig\\":{\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":true}},\\"firewallDeploymentModel\\":{\\"centralizedFirewallDeploymentModel\\":{\\"centralizedFirewallOrchestrationConfig\\":{\\"inspectionVpcIds\\":[{\\"resourceId\\":\\"vpc-1234\\",\\"accountId\\":\\"123456789011\\"}],\\"firewallCreationConfig\\":{\\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneId\\":null,\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]}]}},\\"allowedIPV4CidrList\\":[]}}}}"`` To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with automatic Availability Zone configuration ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\",\\"192.168.0.0/28\\"],\\"routeManagementAction\\":\\"OFF\\"},\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":true}}"`` With automatic Availbility Zone configuration, Firewall Manager chooses which Availability Zones to create the endpoints in. To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with automatic Availability Zone configuration and route management ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\",\\"192.168.0.0/28\\"],\\"routeManagementAction\\":\\"MONITOR\\",\\"routeManagementTargetTypes\\":[\\"InternetGateway\\"]},\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\": \\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":true}}"`` To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with custom Availability Zone configuration ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"fragmentcustomactionname\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\", \\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}},{\\"actionName\\":\\"fragmentcustomactionname\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"fragmentmetricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"firewallCreationConfig\\":{ \\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]},{\\"availabilityZoneName\\":\\"us-east-1b\\",\\"allowedIPV4CidrList\\":[ \\"10.0.0.0/28\\"]}]} },\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":null,\\"routeManagementAction\\":\\"OFF\\",\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":boolean}}"`` With custom Availability Zone configuration, you define which specific Availability Zones to create endpoints in by configuring ``firewallCreationConfig`` . To configure the Availability Zones in ``firewallCreationConfig`` , specify either the ``availabilityZoneName`` or ``availabilityZoneId`` parameter, not both parameters. To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with custom Availability Zone configuration and route management ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"fragmentcustomactionname\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}},{\\"actionName\\":\\"fragmentcustomactionname\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"fragmentmetricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"firewallCreationConfig\\":{\\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]},{\\"availabilityZoneName\\":\\"us-east-1b\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]}]}},\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":null,\\"routeManagementAction\\":\\"MONITOR\\",\\"routeManagementTargetTypes\\":[\\"InternetGateway\\"],\\"routeManagementConfig\\":{\\"allowCrossAZTrafficIfNoEndpoint\\":true}},\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":boolean}}"`` To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Example: ``THIRD_PARTY_FIREWALL`` - Palo Alto Networks Cloud Next-Generation Firewall centralized deployment model ``"{ \\"type\\":\\"THIRD_PARTY_FIREWALL\\", \\"thirdPartyFirewall\\":\\"PALO_ALTO_NETWORKS_CLOUD_NGFW\\", \\"thirdPartyFirewallConfig\\":{ \\"thirdPartyFirewallPolicyList\\":[\\"global-1\\"] },\\"firewallDeploymentModel\\":{\\"centralizedFirewallDeploymentModel\\":{\\"centralizedFirewallOrchestrationConfig\\":{\\"inspectionVpcIds\\":[{\\"resourceId\\":\\"vpc-1234\\",\\"accountId\\":\\"123456789011\\"}],\\"firewallCreationConfig\\":{\\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneId\\":null,\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]}]}},\\"allowedIPV4CidrList\\":[]}}}}"`` To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html>`_ to ``CENTRALIZED`` . - Example: ``THIRD_PARTY_FIREWALL`` - Palo Alto Networks Cloud Next-Generation Firewall distributed deployment model ``"{\\"type\\":\\"THIRD_PARTY_FIREWALL\\",\\"thirdPartyFirewall\\":\\"PALO_ALTO_NETWORKS_CLOUD_NGFW\\",\\"thirdPartyFirewallConfig\\":{\\"thirdPartyFirewallPolicyList\\":[\\"global-1\\"] },\\"firewallDeploymentModel\\":{ \\"distributedFirewallDeploymentModel\\":{ \\"distributedFirewallOrchestrationConfig\\":{\\"firewallCreationConfig\\":{\\"endpointLocation\\":{ \\"availabilityZoneConfigList\\":[ {\\"availabilityZoneName\\":\\"${AvailabilityZone}\\" } ] } }, \\"allowedIPV4CidrList\\":[ ] } } } }"`` To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html>`_ to ``DISTRIBUTED`` . - Specification for ``SHIELD_ADVANCED`` for Amazon CloudFront distributions ``"{\\"type\\":\\"SHIELD_ADVANCED\\",\\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED|IGNORED|DISABLED\\", \\"automaticResponseAction\\":\\"BLOCK|COUNT\\"}, \\"overrideCustomerWebaclClassic\\":true|false}"`` For example: ``"{\\"type\\":\\"SHIELD_ADVANCED\\",\\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED\\", \\"automaticResponseAction\\":\\"COUNT\\"}}"`` The default value for ``automaticResponseStatus`` is ``IGNORED`` . The value for ``automaticResponseAction`` is only required when ``automaticResponseStatus`` is set to ``ENABLED`` . The default value for ``overrideCustomerWebaclClassic`` is ``false`` . For other resource types that you can protect with a Shield Advanced policy, this ``ManagedServiceData`` configuration is an empty string. - Example: ``WAFV2`` ``"{\\"type\\":\\"WAFV2\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupArn\\":null,\\"overrideAction\\":{\\"type\\":\\"NONE\\"},\\"managedRuleGroupIdentifier\\":{\\"version\\":null,\\"vendorName\\":\\"AWS\\",\\"managedRuleGroupName\\":\\"AWSManagedRulesAmazonIpReputationList\\"},\\"ruleGroupType\\":\\"ManagedRuleGroup\\",\\"excludeRules\\":[{\\"name\\":\\"NoUserAgent_HEADER\\"}]}],\\"postProcessRuleGroups\\":[],\\"defaultAction\\":{\\"type\\":\\"ALLOW\\"},\\"overrideCustomerWebACLAssociation\\":false,\\"loggingConfiguration\\":{\\"logDestinationConfigs\\":[\\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\\"],\\"redactedFields\\":[{\\"redactedFieldType\\":\\"SingleHeader\\",\\"redactedFieldValue\\":\\"Cookies\\"},{\\"redactedFieldType\\":\\"Method\\"}]}}"`` In the ``loggingConfiguration`` , you can specify one ``logDestinationConfigs`` , you can optionally provide up to 20 ``redactedFields`` , and the ``RedactedFieldType`` must be one of ``URI`` , ``QUERY_STRING`` , ``HEADER`` , or ``METHOD`` . - Example: ``AWS WAF Classic`` ``"{\\"type\\": \\"WAF\\", \\"ruleGroups\\": [{\\"id\\":\\"12345678-1bcd-9012-efga-0987654321ab\\", \\"overrideAction\\" : {\\"type\\": \\"COUNT\\"}}], \\"defaultAction\\": {\\"type\\": \\"BLOCK\\"}}"`` - Example: ``WAFV2`` - AWS Firewall Manager support for AWS WAF managed rule group versioning ``"{\\"type\\":\\"WAFV2\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupArn\\":null,\\"overrideAction\\":{\\"type\\":\\"NONE\\"},\\"managedRuleGroupIdentifier\\":{\\"versionEnabled\\":true,\\"version\\":\\"Version_2.0\\",\\"vendorName\\":\\"AWS\\",\\"managedRuleGroupName\\":\\"AWSManagedRulesCommonRuleSet\\"},\\"ruleGroupType\\":\\"ManagedRuleGroup\\",\\"excludeRules\\":[{\\"name\\":\\"NoUserAgent_HEADER\\"}]}],\\"postProcessRuleGroups\\":[],\\"defaultAction\\":{\\"type\\":\\"ALLOW\\"},\\"overrideCustomerWebACLAssociation\\":false,\\"loggingConfiguration\\":{\\"logDestinationConfigs\\":[\\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\\"],\\"redactedFields\\":[{\\"redactedFieldType\\":\\"SingleHeader\\",\\"redactedFieldValue\\":\\"Cookies\\"},{\\"redactedFieldType\\":\\"Method\\"}]}}"`` To use a specific version of a AWS WAF managed rule group in your Firewall Manager policy, you must set ``versionEnabled`` to ``true`` , and set ``version`` to the version you'd like to use. If you don't set ``versionEnabled`` to ``true`` , or if you omit ``versionEnabled`` , then Firewall Manager uses the default version of the AWS WAF managed rule group. - Example: ``SECURITY_GROUPS_COMMON`` ``"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false, \\"applyToAllEC2InstanceENIs\\":false,\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd\\"}]}"`` - Example: Shared VPCs. Apply the preceding policy to resources in shared VPCs as well as to those in VPCs that the account owns ``"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false, \\"applyToAllEC2InstanceENIs\\":false,\\"includeSharedVPC\\":true,\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd\\"}]}"`` - Example: ``SECURITY_GROUPS_CONTENT_AUDIT`` ``"{\\"type\\":\\"SECURITY_GROUPS_CONTENT_AUDIT\\",\\"securityGroups\\":[{\\"id\\":\\"sg-000e55995d61a06bd\\"}],\\"securityGroupAction\\":{\\"type\\":\\"ALLOW\\"}}"`` The security group action for content audit can be ``ALLOW`` or ``DENY`` . For ``ALLOW`` , all in-scope security group rules must be within the allowed range of the policy's security group rules. For ``DENY`` , all in-scope security group rules must not contain a value or a range that matches a rule value or range in the policy security group. - Example: ``SECURITY_GROUPS_USAGE_AUDIT`` ``"{\\"type\\":\\"SECURITY_GROUPS_USAGE_AUDIT\\",\\"deleteUnusedSecurityGroups\\":true,\\"coalesceRedundantSecurityGroups\\":true}"``
        :param delete_all_policy_resources: Used when deleting a policy. If ``true`` , Firewall Manager performs cleanup according to the policy type. For AWS WAF and Shield Advanced policies, Firewall Manager does the following: - Deletes rule groups created by Firewall Manager - Removes web ACLs from in-scope resources - Deletes web ACLs that contain no rules or rule groups For security group policies, Firewall Manager does the following for each security group in the policy: - Disassociates the security group from in-scope resources - Deletes the security group if it was created through Firewall Manager and if it's no longer associated with any resources through another policy After the cleanup, in-scope resources are no longer protected by web ACLs in this policy. Protection of out-of-scope resources remains unchanged. Scope is determined by tags that you create and accounts that you associate with the policy. When creating the policy, if you specify that only resources in specific accounts or with specific tags are in scope of the policy, those accounts and resources are handled by the policy. All others are out of scope. If you don't specify tags or accounts, all resources are in scope.
        :param exclude_map: Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to exclude from the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time. You can specify inclusions or exclusions, but not both. If you specify an ``IncludeMap`` , AWS Firewall Manager applies the policy to all accounts specified by the ``IncludeMap`` , and does not evaluate any ``ExcludeMap`` specifications. If you do not specify an ``IncludeMap`` , then Firewall Manager applies the policy to all accounts except for those specified by the ``ExcludeMap`` . You can specify account IDs, OUs, or a combination: - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` . - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` . - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .
        :param include_map: Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to include in the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time. You can specify inclusions or exclusions, but not both. If you specify an ``IncludeMap`` , AWS Firewall Manager applies the policy to all accounts specified by the ``IncludeMap`` , and does not evaluate any ``ExcludeMap`` specifications. If you do not specify an ``IncludeMap`` , then Firewall Manager applies the policy to all accounts except for those specified by the ``ExcludeMap`` . You can specify account IDs, OUs, or a combination: - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` . - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` . - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .
        :param policy_description: Your description of the AWS Firewall Manager policy.
        :param resources_clean_up: Indicates whether AWS Firewall Manager should automatically remove protections from resources that leave the policy scope and clean up resources that Firewall Manager is managing for accounts when those accounts leave policy scope. For example, Firewall Manager will disassociate a Firewall Manager managed web ACL from a protected customer resource when the customer resource leaves policy scope. By default, Firewall Manager doesn't remove protections or delete Firewall Manager managed resources. This option is not available for Shield Advanced or AWS WAF Classic policies.
        :param resource_set_ids: The unique identifiers of the resource sets used by the policy.
        :param resource_tag_logical_operator: Specifies whether to combine multiple resource tags with AND, so that a resource must have all tags to be included or excluded, or OR, so that a resource must have at least one tag. Default: ``AND``
        :param resource_tags: An array of ``ResourceTag`` objects, used to explicitly include resources in the policy scope or explicitly exclude them. If this isn't set, then tags aren't used to modify policy scope. See also ``ExcludeResourceTags`` .
        :param resource_type: The type of resource protected by or in scope of the policy. This is in the format shown in the `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`_ . To apply this policy to multiple resource types, specify a resource type of ``ResourceTypeList`` and then specify the resource types in a ``ResourceTypeList`` . The following are valid resource types for each Firewall Manager policy type: - AWS WAF Classic - ``AWS::ApiGateway::Stage`` , ``AWS::CloudFront::Distribution`` , and ``AWS::ElasticLoadBalancingV2::LoadBalancer`` . - AWS WAF - ``AWS::ApiGateway::Stage`` , ``AWS::ElasticLoadBalancingV2::LoadBalancer`` , and ``AWS::CloudFront::Distribution`` . - Shield Advanced - ``AWS::ElasticLoadBalancingV2::LoadBalancer`` , ``AWS::ElasticLoadBalancing::LoadBalancer`` , ``AWS::EC2::EIP`` , and ``AWS::CloudFront::Distribution`` . - Network ACL - ``AWS::EC2::Subnet`` . - Security group usage audit - ``AWS::EC2::SecurityGroup`` . - Security group content audit - ``AWS::EC2::SecurityGroup`` , ``AWS::EC2::NetworkInterface`` , and ``AWS::EC2::Instance`` . - DNS Firewall, AWS Network Firewall , and third-party firewall - ``AWS::EC2::VPC`` .
        :param resource_type_list: An array of ``ResourceType`` objects. Use this only to specify multiple resource types. To specify a single resource type, use ``ResourceType`` .
        :param tags: A collection of key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_fms as fms
            
            cfn_policy_props = fms.CfnPolicyProps(
                exclude_resource_tags=False,
                policy_name="policyName",
                remediation_enabled=False,
                security_service_policy_data=fms.CfnPolicy.SecurityServicePolicyDataProperty(
                    type="type",
            
                    # the properties below are optional
                    managed_service_data="managedServiceData",
                    policy_option=fms.CfnPolicy.PolicyOptionProperty(
                        network_acl_common_policy=fms.CfnPolicy.NetworkAclCommonPolicyProperty(
                            network_acl_entry_set=fms.CfnPolicy.NetworkAclEntrySetProperty(
                                force_remediate_for_first_entries=False,
                                force_remediate_for_last_entries=False,
            
                                # the properties below are optional
                                first_entries=[fms.CfnPolicy.NetworkAclEntryProperty(
                                    egress=False,
                                    protocol="protocol",
                                    rule_action="ruleAction",
            
                                    # the properties below are optional
                                    cidr_block="cidrBlock",
                                    icmp_type_code=fms.CfnPolicy.IcmpTypeCodeProperty(
                                        code=123,
                                        type=123
                                    ),
                                    ipv6_cidr_block="ipv6CidrBlock",
                                    port_range=fms.CfnPolicy.PortRangeProperty(
                                        from=123,
                                        to=123
                                    )
                                )],
                                last_entries=[fms.CfnPolicy.NetworkAclEntryProperty(
                                    egress=False,
                                    protocol="protocol",
                                    rule_action="ruleAction",
            
                                    # the properties below are optional
                                    cidr_block="cidrBlock",
                                    icmp_type_code=fms.CfnPolicy.IcmpTypeCodeProperty(
                                        code=123,
                                        type=123
                                    ),
                                    ipv6_cidr_block="ipv6CidrBlock",
                                    port_range=fms.CfnPolicy.PortRangeProperty(
                                        from=123,
                                        to=123
                                    )
                                )]
                            )
                        ),
                        network_firewall_policy=fms.CfnPolicy.NetworkFirewallPolicyProperty(
                            firewall_deployment_model="firewallDeploymentModel"
                        ),
                        third_party_firewall_policy=fms.CfnPolicy.ThirdPartyFirewallPolicyProperty(
                            firewall_deployment_model="firewallDeploymentModel"
                        )
                    )
                ),
            
                # the properties below are optional
                delete_all_policy_resources=False,
                exclude_map={
                    "account": ["account"],
                    "orgunit": ["orgunit"]
                },
                include_map={
                    "account": ["account"],
                    "orgunit": ["orgunit"]
                },
                policy_description="policyDescription",
                resources_clean_up=False,
                resource_set_ids=["resourceSetIds"],
                resource_tag_logical_operator="resourceTagLogicalOperator",
                resource_tags=[fms.CfnPolicy.ResourceTagProperty(
                    key="key",
            
                    # the properties below are optional
                    value="value"
                )],
                resource_type="resourceType",
                resource_type_list=["resourceTypeList"],
                tags=[fms.CfnPolicy.PolicyTagProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8455eef74a6daf8d86ebd4c14f18184bf9c938d95a07a9902bf05c79f9b2b322)
            check_type(argname="argument exclude_resource_tags", value=exclude_resource_tags, expected_type=type_hints["exclude_resource_tags"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument remediation_enabled", value=remediation_enabled, expected_type=type_hints["remediation_enabled"])
            check_type(argname="argument security_service_policy_data", value=security_service_policy_data, expected_type=type_hints["security_service_policy_data"])
            check_type(argname="argument delete_all_policy_resources", value=delete_all_policy_resources, expected_type=type_hints["delete_all_policy_resources"])
            check_type(argname="argument exclude_map", value=exclude_map, expected_type=type_hints["exclude_map"])
            check_type(argname="argument include_map", value=include_map, expected_type=type_hints["include_map"])
            check_type(argname="argument policy_description", value=policy_description, expected_type=type_hints["policy_description"])
            check_type(argname="argument resources_clean_up", value=resources_clean_up, expected_type=type_hints["resources_clean_up"])
            check_type(argname="argument resource_set_ids", value=resource_set_ids, expected_type=type_hints["resource_set_ids"])
            check_type(argname="argument resource_tag_logical_operator", value=resource_tag_logical_operator, expected_type=type_hints["resource_tag_logical_operator"])
            check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument resource_type_list", value=resource_type_list, expected_type=type_hints["resource_type_list"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "exclude_resource_tags": exclude_resource_tags,
            "policy_name": policy_name,
            "remediation_enabled": remediation_enabled,
            "security_service_policy_data": security_service_policy_data,
        }
        if delete_all_policy_resources is not None:
            self._values["delete_all_policy_resources"] = delete_all_policy_resources
        if exclude_map is not None:
            self._values["exclude_map"] = exclude_map
        if include_map is not None:
            self._values["include_map"] = include_map
        if policy_description is not None:
            self._values["policy_description"] = policy_description
        if resources_clean_up is not None:
            self._values["resources_clean_up"] = resources_clean_up
        if resource_set_ids is not None:
            self._values["resource_set_ids"] = resource_set_ids
        if resource_tag_logical_operator is not None:
            self._values["resource_tag_logical_operator"] = resource_tag_logical_operator
        if resource_tags is not None:
            self._values["resource_tags"] = resource_tags
        if resource_type is not None:
            self._values["resource_type"] = resource_type
        if resource_type_list is not None:
            self._values["resource_type_list"] = resource_type_list
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def exclude_resource_tags(
        self,
    ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Used only when tags are specified in the ``ResourceTags`` property.

        If this property is ``True`` , resources with the specified tags are not in scope of the policy. If it's ``False`` , only resources with the specified tags are in scope of the policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excluderesourcetags
        '''
        result = self._values.get("exclude_resource_tags")
        assert result is not None, "Required property 'exclude_resource_tags' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The name of the AWS Firewall Manager policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def remediation_enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Indicates if the policy should be automatically applied to new resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-remediationenabled
        '''
        result = self._values.get("remediation_enabled")
        assert result is not None, "Required property 'remediation_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def security_service_policy_data(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnPolicy.SecurityServicePolicyDataProperty]:
        '''Details about the security service that is being used to protect the resources.

        This contains the following settings:

        - Type - Indicates the service type that the policy uses to protect the resource. For security group policies, Firewall Manager supports one security group for each common policy and for each content audit policy. This is an adjustable limit that you can increase by contacting  .

        Valid values: ``DNS_FIREWALL`` | ``NETWORK_FIREWALL`` | ``SECURITY_GROUPS_COMMON`` | ``SECURITY_GROUPS_CONTENT_AUDIT`` | ``SECURITY_GROUPS_USAGE_AUDIT`` | ``SHIELD_ADVANCED`` | ``THIRD_PARTY_FIREWALL`` | ``WAFV2`` | ``WAF``

        - ManagedServiceData - Details about the service that are specific to the service type, in JSON format.
        - Example: ``DNS_FIREWALL``

        ``"{\\"type\\":\\"DNS_FIREWALL\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupId\\":\\"rslvr-frg-1\\",\\"priority\\":10}],\\"postProcessRuleGroups\\":[{\\"ruleGroupId\\":\\"rslvr-frg-2\\",\\"priority\\":9911}]}"``
        .. epigraph::

           Valid values for ``preProcessRuleGroups`` are between 1 and 99. Valid values for ``postProcessRuleGroups`` are between 9901 and 10000.

        - Example: ``NETWORK_FIREWALL`` - Centralized deployment model

        ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"awsNetworkFirewallConfig\\":{\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":true}},\\"firewallDeploymentModel\\":{\\"centralizedFirewallDeploymentModel\\":{\\"centralizedFirewallOrchestrationConfig\\":{\\"inspectionVpcIds\\":[{\\"resourceId\\":\\"vpc-1234\\",\\"accountId\\":\\"123456789011\\"}],\\"firewallCreationConfig\\":{\\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneId\\":null,\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]}]}},\\"allowedIPV4CidrList\\":[]}}}}"``

        To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` .

        - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with automatic Availability Zone configuration

        ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\",\\"192.168.0.0/28\\"],\\"routeManagementAction\\":\\"OFF\\"},\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":true}}"``

        With automatic Availbility Zone configuration, Firewall Manager chooses which Availability Zones to create the endpoints in. To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` .

        - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with automatic Availability Zone configuration and route management

        ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\",\\"192.168.0.0/28\\"],\\"routeManagementAction\\":\\"MONITOR\\",\\"routeManagementTargetTypes\\":[\\"InternetGateway\\"]},\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\": \\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":true}}"``

        To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` .

        - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with custom Availability Zone configuration

        ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"fragmentcustomactionname\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\", \\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}},{\\"actionName\\":\\"fragmentcustomactionname\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"fragmentmetricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"firewallCreationConfig\\":{ \\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]},{\\"availabilityZoneName\\":\\"us-east-1b\\",\\"allowedIPV4CidrList\\":[ \\"10.0.0.0/28\\"]}]} },\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":null,\\"routeManagementAction\\":\\"OFF\\",\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":boolean}}"``

        With custom Availability Zone configuration, you define which specific Availability Zones to create endpoints in by configuring ``firewallCreationConfig`` . To configure the Availability Zones in ``firewallCreationConfig`` , specify either the ``availabilityZoneName`` or ``availabilityZoneId`` parameter, not both parameters.

        To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` .

        - Example: ``NETWORK_FIREWALL`` - Distributed deployment model with custom Availability Zone configuration and route management

        ``"{\\"type\\":\\"NETWORK_FIREWALL\\",\\"networkFirewallStatelessRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\\",\\"priority\\":1}],\\"networkFirewallStatelessDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"customActionName\\"],\\"networkFirewallStatelessFragmentDefaultActions\\":[\\"aws:forward_to_sfe\\",\\"fragmentcustomactionname\\"],\\"networkFirewallStatelessCustomActions\\":[{\\"actionName\\":\\"customActionName\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"metricdimensionvalue\\"}]}}},{\\"actionName\\":\\"fragmentcustomactionname\\",\\"actionDefinition\\":{\\"publishMetricAction\\":{\\"dimensions\\":[{\\"value\\":\\"fragmentmetricdimensionvalue\\"}]}}}],\\"networkFirewallStatefulRuleGroupReferences\\":[{\\"resourceARN\\":\\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\\"}],\\"networkFirewallOrchestrationConfig\\":{\\"firewallCreationConfig\\":{\\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]},{\\"availabilityZoneName\\":\\"us-east-1b\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]}]}},\\"singleFirewallEndpointPerVPC\\":false,\\"allowedIPV4CidrList\\":null,\\"routeManagementAction\\":\\"MONITOR\\",\\"routeManagementTargetTypes\\":[\\"InternetGateway\\"],\\"routeManagementConfig\\":{\\"allowCrossAZTrafficIfNoEndpoint\\":true}},\\"networkFirewallLoggingConfiguration\\":{\\"logDestinationConfigs\\":[{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"ALERT\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}},{\\"logDestinationType\\":\\"S3\\",\\"logType\\":\\"FLOW\\",\\"logDestination\\":{\\"bucketName\\":\\"s3-bucket-name\\"}}],\\"overrideExistingConfig\\":boolean}}"``

        To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html>`_ to ``DISTRIBUTED`` .

        - Example: ``THIRD_PARTY_FIREWALL`` - Palo Alto Networks Cloud Next-Generation Firewall centralized deployment model

        ``"{ \\"type\\":\\"THIRD_PARTY_FIREWALL\\", \\"thirdPartyFirewall\\":\\"PALO_ALTO_NETWORKS_CLOUD_NGFW\\", \\"thirdPartyFirewallConfig\\":{ \\"thirdPartyFirewallPolicyList\\":[\\"global-1\\"] },\\"firewallDeploymentModel\\":{\\"centralizedFirewallDeploymentModel\\":{\\"centralizedFirewallOrchestrationConfig\\":{\\"inspectionVpcIds\\":[{\\"resourceId\\":\\"vpc-1234\\",\\"accountId\\":\\"123456789011\\"}],\\"firewallCreationConfig\\":{\\"endpointLocation\\":{\\"availabilityZoneConfigList\\":[{\\"availabilityZoneId\\":null,\\"availabilityZoneName\\":\\"us-east-1a\\",\\"allowedIPV4CidrList\\":[\\"10.0.0.0/28\\"]}]}},\\"allowedIPV4CidrList\\":[]}}}}"``

        To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html>`_ to ``CENTRALIZED`` .

        - Example: ``THIRD_PARTY_FIREWALL`` - Palo Alto Networks Cloud Next-Generation Firewall distributed deployment model

        ``"{\\"type\\":\\"THIRD_PARTY_FIREWALL\\",\\"thirdPartyFirewall\\":\\"PALO_ALTO_NETWORKS_CLOUD_NGFW\\",\\"thirdPartyFirewallConfig\\":{\\"thirdPartyFirewallPolicyList\\":[\\"global-1\\"] },\\"firewallDeploymentModel\\":{ \\"distributedFirewallDeploymentModel\\":{ \\"distributedFirewallOrchestrationConfig\\":{\\"firewallCreationConfig\\":{\\"endpointLocation\\":{ \\"availabilityZoneConfigList\\":[ {\\"availabilityZoneName\\":\\"${AvailabilityZone}\\" } ] } }, \\"allowedIPV4CidrList\\":[ ] } } } }"``

        To use the distributed deployment model, you must set `FirewallDeploymentModel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html>`_ to ``DISTRIBUTED`` .

        - Specification for ``SHIELD_ADVANCED`` for Amazon CloudFront distributions

        ``"{\\"type\\":\\"SHIELD_ADVANCED\\",\\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED|IGNORED|DISABLED\\", \\"automaticResponseAction\\":\\"BLOCK|COUNT\\"}, \\"overrideCustomerWebaclClassic\\":true|false}"``

        For example: ``"{\\"type\\":\\"SHIELD_ADVANCED\\",\\"automaticResponseConfiguration\\": {\\"automaticResponseStatus\\":\\"ENABLED\\", \\"automaticResponseAction\\":\\"COUNT\\"}}"``

        The default value for ``automaticResponseStatus`` is ``IGNORED`` . The value for ``automaticResponseAction`` is only required when ``automaticResponseStatus`` is set to ``ENABLED`` . The default value for ``overrideCustomerWebaclClassic`` is ``false`` .

        For other resource types that you can protect with a Shield Advanced policy, this ``ManagedServiceData`` configuration is an empty string.

        - Example: ``WAFV2``

        ``"{\\"type\\":\\"WAFV2\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupArn\\":null,\\"overrideAction\\":{\\"type\\":\\"NONE\\"},\\"managedRuleGroupIdentifier\\":{\\"version\\":null,\\"vendorName\\":\\"AWS\\",\\"managedRuleGroupName\\":\\"AWSManagedRulesAmazonIpReputationList\\"},\\"ruleGroupType\\":\\"ManagedRuleGroup\\",\\"excludeRules\\":[{\\"name\\":\\"NoUserAgent_HEADER\\"}]}],\\"postProcessRuleGroups\\":[],\\"defaultAction\\":{\\"type\\":\\"ALLOW\\"},\\"overrideCustomerWebACLAssociation\\":false,\\"loggingConfiguration\\":{\\"logDestinationConfigs\\":[\\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\\"],\\"redactedFields\\":[{\\"redactedFieldType\\":\\"SingleHeader\\",\\"redactedFieldValue\\":\\"Cookies\\"},{\\"redactedFieldType\\":\\"Method\\"}]}}"``

        In the ``loggingConfiguration`` , you can specify one ``logDestinationConfigs`` , you can optionally provide up to 20 ``redactedFields`` , and the ``RedactedFieldType`` must be one of ``URI`` , ``QUERY_STRING`` , ``HEADER`` , or ``METHOD`` .

        - Example: ``AWS WAF Classic``

        ``"{\\"type\\": \\"WAF\\", \\"ruleGroups\\": [{\\"id\\":\\"12345678-1bcd-9012-efga-0987654321ab\\", \\"overrideAction\\" : {\\"type\\": \\"COUNT\\"}}], \\"defaultAction\\": {\\"type\\": \\"BLOCK\\"}}"``

        - Example: ``WAFV2`` - AWS Firewall Manager support for AWS WAF managed rule group versioning

        ``"{\\"type\\":\\"WAFV2\\",\\"preProcessRuleGroups\\":[{\\"ruleGroupArn\\":null,\\"overrideAction\\":{\\"type\\":\\"NONE\\"},\\"managedRuleGroupIdentifier\\":{\\"versionEnabled\\":true,\\"version\\":\\"Version_2.0\\",\\"vendorName\\":\\"AWS\\",\\"managedRuleGroupName\\":\\"AWSManagedRulesCommonRuleSet\\"},\\"ruleGroupType\\":\\"ManagedRuleGroup\\",\\"excludeRules\\":[{\\"name\\":\\"NoUserAgent_HEADER\\"}]}],\\"postProcessRuleGroups\\":[],\\"defaultAction\\":{\\"type\\":\\"ALLOW\\"},\\"overrideCustomerWebACLAssociation\\":false,\\"loggingConfiguration\\":{\\"logDestinationConfigs\\":[\\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\\"],\\"redactedFields\\":[{\\"redactedFieldType\\":\\"SingleHeader\\",\\"redactedFieldValue\\":\\"Cookies\\"},{\\"redactedFieldType\\":\\"Method\\"}]}}"``

        To use a specific version of a AWS WAF managed rule group in your Firewall Manager policy, you must set ``versionEnabled`` to ``true`` , and set ``version`` to the version you'd like to use. If you don't set ``versionEnabled`` to ``true`` , or if you omit ``versionEnabled`` , then Firewall Manager uses the default version of the AWS WAF managed rule group.

        - Example: ``SECURITY_GROUPS_COMMON``

        ``"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false, \\"applyToAllEC2InstanceENIs\\":false,\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd\\"}]}"``

        - Example: Shared VPCs. Apply the preceding policy to resources in shared VPCs as well as to those in VPCs that the account owns

        ``"{\\"type\\":\\"SECURITY_GROUPS_COMMON\\",\\"revertManualSecurityGroupChanges\\":false,\\"exclusiveResourceSecurityGroupManagement\\":false, \\"applyToAllEC2InstanceENIs\\":false,\\"includeSharedVPC\\":true,\\"securityGroups\\":[{\\"id\\":\\" sg-000e55995d61a06bd\\"}]}"``

        - Example: ``SECURITY_GROUPS_CONTENT_AUDIT``

        ``"{\\"type\\":\\"SECURITY_GROUPS_CONTENT_AUDIT\\",\\"securityGroups\\":[{\\"id\\":\\"sg-000e55995d61a06bd\\"}],\\"securityGroupAction\\":{\\"type\\":\\"ALLOW\\"}}"``

        The security group action for content audit can be ``ALLOW`` or ``DENY`` . For ``ALLOW`` , all in-scope security group rules must be within the allowed range of the policy's security group rules. For ``DENY`` , all in-scope security group rules must not contain a value or a range that matches a rule value or range in the policy security group.

        - Example: ``SECURITY_GROUPS_USAGE_AUDIT``

        ``"{\\"type\\":\\"SECURITY_GROUPS_USAGE_AUDIT\\",\\"deleteUnusedSecurityGroups\\":true,\\"coalesceRedundantSecurityGroups\\":true}"``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-securityservicepolicydata
        '''
        result = self._values.get("security_service_policy_data")
        assert result is not None, "Required property 'security_service_policy_data' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnPolicy.SecurityServicePolicyDataProperty], result)

    @builtins.property
    def delete_all_policy_resources(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Used when deleting a policy. If ``true`` , Firewall Manager performs cleanup according to the policy type.

        For AWS WAF and Shield Advanced policies, Firewall Manager does the following:

        - Deletes rule groups created by Firewall Manager
        - Removes web ACLs from in-scope resources
        - Deletes web ACLs that contain no rules or rule groups

        For security group policies, Firewall Manager does the following for each security group in the policy:

        - Disassociates the security group from in-scope resources
        - Deletes the security group if it was created through Firewall Manager and if it's no longer associated with any resources through another policy

        After the cleanup, in-scope resources are no longer protected by web ACLs in this policy. Protection of out-of-scope resources remains unchanged. Scope is determined by tags that you create and accounts that you associate with the policy. When creating the policy, if you specify that only resources in specific accounts or with specific tags are in scope of the policy, those accounts and resources are handled by the policy. All others are out of scope. If you don't specify tags or accounts, all resources are in scope.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-deleteallpolicyresources
        '''
        result = self._values.get("delete_all_policy_resources")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def exclude_map(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPolicy.IEMapProperty]]:
        '''Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to exclude from the policy.

        Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.

        You can specify inclusions or exclusions, but not both. If you specify an ``IncludeMap`` , AWS Firewall Manager applies the policy to all accounts specified by the ``IncludeMap`` , and does not evaluate any ``ExcludeMap`` specifications. If you do not specify an ``IncludeMap`` , then Firewall Manager applies the policy to all accounts except for those specified by the ``ExcludeMap`` .

        You can specify account IDs, OUs, or a combination:

        - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .
        - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` .
        - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excludemap
        '''
        result = self._values.get("exclude_map")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPolicy.IEMapProperty]], result)

    @builtins.property
    def include_map(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPolicy.IEMapProperty]]:
        '''Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to include in the policy.

        Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.

        You can specify inclusions or exclusions, but not both. If you specify an ``IncludeMap`` , AWS Firewall Manager applies the policy to all accounts specified by the ``IncludeMap`` , and does not evaluate any ``ExcludeMap`` specifications. If you do not specify an ``IncludeMap`` , then Firewall Manager applies the policy to all accounts except for those specified by the ``ExcludeMap`` .

        You can specify account IDs, OUs, or a combination:

        - Specify account IDs by setting the key to ``ACCOUNT`` . For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”]}`` .
        - Specify OUs by setting the key to ``ORGUNIT`` . For example, the following is a valid map: ``{“ORGUNIT” : [“ouid111”, “ouid112”]}`` .
        - Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: ``{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-includemap
        '''
        result = self._values.get("include_map")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPolicy.IEMapProperty]], result)

    @builtins.property
    def policy_description(self) -> typing.Optional[builtins.str]:
        '''Your description of the AWS Firewall Manager policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-policydescription
        '''
        result = self._values.get("policy_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resources_clean_up(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether AWS Firewall Manager should automatically remove protections from resources that leave the policy scope and clean up resources that Firewall Manager is managing for accounts when those accounts leave policy scope.

        For example, Firewall Manager will disassociate a Firewall Manager managed web ACL from a protected customer resource when the customer resource leaves policy scope.

        By default, Firewall Manager doesn't remove protections or delete Firewall Manager managed resources.

        This option is not available for Shield Advanced or AWS WAF Classic policies.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcescleanup
        '''
        result = self._values.get("resources_clean_up")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def resource_set_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The unique identifiers of the resource sets used by the policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcesetids
        '''
        result = self._values.get("resource_set_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def resource_tag_logical_operator(self) -> typing.Optional[builtins.str]:
        '''Specifies whether to combine multiple resource tags with AND, so that a resource must have all tags to be included or excluded, or OR, so that a resource must have at least one tag.

        Default: ``AND``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetaglogicaloperator
        '''
        result = self._values.get("resource_tag_logical_operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPolicy.ResourceTagProperty]]]]:
        '''An array of ``ResourceTag`` objects, used to explicitly include resources in the policy scope or explicitly exclude them.

        If this isn't set, then tags aren't used to modify policy scope. See also ``ExcludeResourceTags`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetags
        '''
        result = self._values.get("resource_tags")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPolicy.ResourceTagProperty]]]], result)

    @builtins.property
    def resource_type(self) -> typing.Optional[builtins.str]:
        '''The type of resource protected by or in scope of the policy.

        This is in the format shown in the `AWS Resource Types Reference <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>`_ . To apply this policy to multiple resource types, specify a resource type of ``ResourceTypeList`` and then specify the resource types in a ``ResourceTypeList`` .

        The following are valid resource types for each Firewall Manager policy type:

        - AWS WAF Classic - ``AWS::ApiGateway::Stage`` , ``AWS::CloudFront::Distribution`` , and ``AWS::ElasticLoadBalancingV2::LoadBalancer`` .
        - AWS WAF - ``AWS::ApiGateway::Stage`` , ``AWS::ElasticLoadBalancingV2::LoadBalancer`` , and ``AWS::CloudFront::Distribution`` .
        - Shield Advanced - ``AWS::ElasticLoadBalancingV2::LoadBalancer`` , ``AWS::ElasticLoadBalancing::LoadBalancer`` , ``AWS::EC2::EIP`` , and ``AWS::CloudFront::Distribution`` .
        - Network ACL - ``AWS::EC2::Subnet`` .
        - Security group usage audit - ``AWS::EC2::SecurityGroup`` .
        - Security group content audit - ``AWS::EC2::SecurityGroup`` , ``AWS::EC2::NetworkInterface`` , and ``AWS::EC2::Instance`` .
        - DNS Firewall, AWS Network Firewall , and third-party firewall - ``AWS::EC2::VPC`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetype
        '''
        result = self._values.get("resource_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_type_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of ``ResourceType`` objects.

        Use this only to specify multiple resource types. To specify a single resource type, use ``ResourceType`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetypelist
        '''
        result = self._values.get("resource_type_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnPolicy.PolicyTagProperty]]:
        '''A collection of key:value pairs associated with an AWS resource.

        The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnPolicy.PolicyTagProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnResourceSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_fms.CfnResourceSet",
):
    '''A set of resources to include in a policy.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-resourceset.html
    :cloudformationResource: AWS::FMS::ResourceSet
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_fms as fms
        
        cfn_resource_set = fms.CfnResourceSet(self, "MyCfnResourceSet",
            name="name",
            resource_type_list=["resourceTypeList"],
        
            # the properties below are optional
            description="description",
            resources=["resources"],
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
        resource_type_list: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The descriptive name of the resource set. You can't change the name of a resource set after you create it.
        :param resource_type_list: Determines the resources that can be associated to the resource set. Depending on your setting for max results and the number of resource sets, a single call might not return the full list.
        :param description: A description of the resource set.
        :param resources: 
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a4dcb98b2ac8a85db4734c3fc81a2a27145d1602529cf3cac45f86586536e3b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceSetProps(
            name=name,
            resource_type_list=resource_type_list,
            description=description,
            resources=resources,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d558d6e8f3a2845605396d576ea08cc396492c25719847f5b31d717c5d11745)
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
            type_hints = typing.get_type_hints(_typecheckingstub__43ace1cc1235bd169177faf8303876a3b377e847b1d1122d1f705870c18b6a82)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''A unique identifier for the resource set.

        This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    def name(self) -> builtins.str:
        '''The descriptive name of the resource set.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__031d7ff6b26b7d3f5a10172db514f9eb1ce9278ef97ad07fc977e55473e32862)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceTypeList")
    def resource_type_list(self) -> typing.List[builtins.str]:
        '''Determines the resources that can be associated to the resource set.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resourceTypeList"))

    @resource_type_list.setter
    def resource_type_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f8a509749b708e855f71ab43b7c1be875c670973fe31ce491bbd3ecd792af10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTypeList", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the resource set.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbd4ae8e333978d316c1b6772dfd81a2faa95a3d2e7f28767078a2a030d94720)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resources"))

    @resources.setter
    def resources(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7974c92e7d0af9d954e4b2da01bb2f3ca790c3b0685db7329c0c060f7b83bc0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resources", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b479b182181e5261c6adbabbb8cef907643db35729c086190efacadb1e0e731)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_fms.CfnResourceSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "resource_type_list": "resourceTypeList",
        "description": "description",
        "resources": "resources",
        "tags": "tags",
    },
)
class CfnResourceSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        resource_type_list: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnResourceSet``.

        :param name: The descriptive name of the resource set. You can't change the name of a resource set after you create it.
        :param resource_type_list: Determines the resources that can be associated to the resource set. Depending on your setting for max results and the number of resource sets, a single call might not return the full list.
        :param description: A description of the resource set.
        :param resources: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-resourceset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_fms as fms
            
            cfn_resource_set_props = fms.CfnResourceSetProps(
                name="name",
                resource_type_list=["resourceTypeList"],
            
                # the properties below are optional
                description="description",
                resources=["resources"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66a653a8499f7c22e2b32cf7a844c85faae63d65887e6ec136044eb44e1ebdaf)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_type_list", value=resource_type_list, expected_type=type_hints["resource_type_list"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "resource_type_list": resource_type_list,
        }
        if description is not None:
            self._values["description"] = description
        if resources is not None:
            self._values["resources"] = resources
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The descriptive name of the resource set.

        You can't change the name of a resource set after you create it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-resourceset.html#cfn-fms-resourceset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_type_list(self) -> typing.List[builtins.str]:
        '''Determines the resources that can be associated to the resource set.

        Depending on your setting for max results and the number of resource sets, a single call might not return the full list.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-resourceset.html#cfn-fms-resourceset-resourcetypelist
        '''
        result = self._values.get("resource_type_list")
        assert result is not None, "Required property 'resource_type_list' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the resource set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-resourceset.html#cfn-fms-resourceset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-resourceset.html#cfn-fms-resourceset-resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-resourceset.html#cfn-fms-resourceset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnNotificationChannel",
    "CfnNotificationChannelProps",
    "CfnPolicy",
    "CfnPolicyProps",
    "CfnResourceSet",
    "CfnResourceSetProps",
]

publication.publish()

def _typecheckingstub__7a03e25c676e3f843e7365938075353612a65a3a2bd2538074f016448b29053c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    sns_role_name: builtins.str,
    sns_topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eae25dcbfb8d4710a66ea0f6804d609f2c8fbb762e291caa42156e2d5e0a5ccd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27e0110b31984037127ddfc8639de3754907e90f7485cfd5b43a5fbe4ad39717(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00bd3c5f6e0b7d08ecc3e9d3f09ce0486f75f4e24649a6e59140bdaa48e6e9ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d5dd2548355a1129e0085759bb293de343519fe581ead5c659ceff8ec36b346(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5624e06a5ce62823c414e320e35e25799cfeb05a7db7fa7dc3f5353d1e0fe469(
    *,
    sns_role_name: builtins.str,
    sns_topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a29b3b13041b0ccbd18a0c29ff5cff0adbc0e2aedc87591f1c54ec7a1fc830b4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    exclude_resource_tags: typing.Union[builtins.bool, _IResolvable_da3f097b],
    policy_name: builtins.str,
    remediation_enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    security_service_policy_data: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.SecurityServicePolicyDataProperty, typing.Dict[builtins.str, typing.Any]]],
    delete_all_policy_resources: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    exclude_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.IEMapProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    include_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.IEMapProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    policy_description: typing.Optional[builtins.str] = None,
    resources_clean_up: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    resource_set_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_tag_logical_operator: typing.Optional[builtins.str] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_type: typing.Optional[builtins.str] = None,
    resource_type_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnPolicy.PolicyTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bd3d819ff879695091ea1782c6d44919a2d5d60ac904eb958a4baa5a9b7b105(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5336d629941f59b9bc57ae2f0f9086302ff307956a981d17c0c74f56e281a98(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a6c43cec956bc22ae07e19e1af4001c23e93faad6ca1043a917bf0f5dcfc1d(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62ed5a312383f144ece33d5d7f925fd2a4d83062b6024f0b02b573273b2f360d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce24f414c17fee1c6464201d3595af0f5eddf30ec4dc5532e27f42a5a60bfba0(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c28ba46bb386f4176af9e17ecbe45582b554c7807d38f2929fb3fd7a81f3976(
    value: typing.Union[_IResolvable_da3f097b, CfnPolicy.SecurityServicePolicyDataProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fe798b33151903c0017cb9d94013617a6afcad058e7ae0fe54c9cfd6dd679c2(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8f8c8d7be71d632f5fd707992c674dd52c74761a09f147830413fcfba30c273(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPolicy.IEMapProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94290c92cb339b7d588eedc5f7e4693403e89224115f954743aa8b94e5920b0f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPolicy.IEMapProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aba01c3384f02d2b5b8393ae170165a3fcecf0b67864bb9240d39b4518cee92(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12534b322db922dabec65a01e84b63ba7b3a489d9d25d5870fef80727d31a5c3(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__048e93c726f9c5fe6e9b627c041b37e3458add761a76189dddf42b880fc049a5(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c785568d3275bbfb3df2dd3b2ac1d97319f9c06330a57289261dce85d69868f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c77d40603d6f4c051dd3f9b5d662e1b2f8b3690fcfa612876de86b1cfb05ac0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPolicy.ResourceTagProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45fbd20db788e5f26784bca772c0c150d7f583f3b21916156a9f85bdbbbd064d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__defb2e92d0f62de49ea900ef5497c0bb92b81e991fe094bca77e0bc3225a174e(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e61b60deb504fb101d8b3c5d4d91824672d7a44fdd9537dec8f729c7d34256be(
    value: typing.Optional[typing.List[CfnPolicy.PolicyTagProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bcb551e43b08ef4828de279b99e59a3954c4cdc19c8adfe6bf93e810ce36917(
    *,
    account: typing.Optional[typing.Sequence[builtins.str]] = None,
    orgunit: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65b9cc6166ca508cd4c5ab4d066ea459564143dea548a99b579d93e51f574165(
    *,
    code: jsii.Number,
    type: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dfc57cc41dc1d1b1ebbc44d2e08c4db8913dbb8d25d9bff92c2c760de2fdc82(
    *,
    network_acl_entry_set: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.NetworkAclEntrySetProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a315c8565b94dd4f1c73bc5bb6afd0ade3bc8461a7c74c1098d0d7f66076bf4(
    *,
    egress: typing.Union[builtins.bool, _IResolvable_da3f097b],
    protocol: builtins.str,
    rule_action: builtins.str,
    cidr_block: typing.Optional[builtins.str] = None,
    icmp_type_code: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.IcmpTypeCodeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ipv6_cidr_block: typing.Optional[builtins.str] = None,
    port_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.PortRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2907f7090b00fafcfa0eb4f641b098a7fa37436ba6c4ffff2dafc1595c81a6e(
    *,
    force_remediate_for_first_entries: typing.Union[builtins.bool, _IResolvable_da3f097b],
    force_remediate_for_last_entries: typing.Union[builtins.bool, _IResolvable_da3f097b],
    first_entries: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.NetworkAclEntryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    last_entries: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.NetworkAclEntryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dee79c6872a0421399375d5fc2757431881011031a81ccd6674040de21bac13(
    *,
    firewall_deployment_model: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5979520d8e95acd573ee171b00e0dcba3be3872b80af53615d64bc000f703299(
    *,
    network_acl_common_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.NetworkAclCommonPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    network_firewall_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.NetworkFirewallPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    third_party_firewall_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.ThirdPartyFirewallPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d5ee16e00771d59c6939cbdec3cdf3c57cdb9a09a7e914e3faf7baaa7416d62(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbc1cd0112a3be4230fd0e2a96f8a5e7799f9f8c3925aad80c6eef4a1172da43(
    *,
    from_: jsii.Number,
    to: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1533af324aea7be8b3e806a7d4a851c48bea2139cd3bb0ce1cc81ff86e976487(
    *,
    key: builtins.str,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c049eeb7140522ded2ec5e8c352001a90a84400f6f8d601bcb6b17805b0a150e(
    *,
    type: builtins.str,
    managed_service_data: typing.Optional[builtins.str] = None,
    policy_option: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.PolicyOptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4a7c7a12ee187727472c21f2a6147ca000c43ae4d50b0ab60025dea29d98eb(
    *,
    firewall_deployment_model: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8455eef74a6daf8d86ebd4c14f18184bf9c938d95a07a9902bf05c79f9b2b322(
    *,
    exclude_resource_tags: typing.Union[builtins.bool, _IResolvable_da3f097b],
    policy_name: builtins.str,
    remediation_enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    security_service_policy_data: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.SecurityServicePolicyDataProperty, typing.Dict[builtins.str, typing.Any]]],
    delete_all_policy_resources: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    exclude_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.IEMapProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    include_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.IEMapProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    policy_description: typing.Optional[builtins.str] = None,
    resources_clean_up: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    resource_set_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_tag_logical_operator: typing.Optional[builtins.str] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_type: typing.Optional[builtins.str] = None,
    resource_type_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnPolicy.PolicyTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a4dcb98b2ac8a85db4734c3fc81a2a27145d1602529cf3cac45f86586536e3b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    resource_type_list: typing.Sequence[builtins.str],
    description: typing.Optional[builtins.str] = None,
    resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d558d6e8f3a2845605396d576ea08cc396492c25719847f5b31d717c5d11745(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43ace1cc1235bd169177faf8303876a3b377e847b1d1122d1f705870c18b6a82(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__031d7ff6b26b7d3f5a10172db514f9eb1ce9278ef97ad07fc977e55473e32862(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f8a509749b708e855f71ab43b7c1be875c670973fe31ce491bbd3ecd792af10(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbd4ae8e333978d316c1b6772dfd81a2faa95a3d2e7f28767078a2a030d94720(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7974c92e7d0af9d954e4b2da01bb2f3ca790c3b0685db7329c0c060f7b83bc0e(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b479b182181e5261c6adbabbb8cef907643db35729c086190efacadb1e0e731(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66a653a8499f7c22e2b32cf7a844c85faae63d65887e6ec136044eb44e1ebdaf(
    *,
    name: builtins.str,
    resource_type_list: typing.Sequence[builtins.str],
    description: typing.Optional[builtins.str] = None,
    resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
