r'''
# AWS::SSMQuickSetup Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_ssmquicksetup as ssmquicksetup
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SSMQuickSetup construct libraries](https://constructs.dev/search?q=ssmquicksetup)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SSMQuickSetup resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSMQuickSetup.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SSMQuickSetup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSMQuickSetup.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnConfigurationManager(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ssmquicksetup.CfnConfigurationManager",
):
    '''Creates a Quick Setup configuration manager resource.

    This object is a collection of desired state configurations for multiple configuration definitions and summaries describing the deployments of those definitions.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmquicksetup-configurationmanager.html
    :cloudformationResource: AWS::SSMQuickSetup::ConfigurationManager
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ssmquicksetup as ssmquicksetup
        
        cfn_configuration_manager = ssmquicksetup.CfnConfigurationManager(self, "MyCfnConfigurationManager",
            configuration_definitions=[ssmquicksetup.CfnConfigurationManager.ConfigurationDefinitionProperty(
                parameters={
                    "parameters_key": "parameters"
                },
                type="type",
        
                # the properties below are optional
                id="id",
                local_deployment_administration_role_arn="localDeploymentAdministrationRoleArn",
                local_deployment_execution_role_name="localDeploymentExecutionRoleName",
                type_version="typeVersion"
            )],
        
            # the properties below are optional
            description="description",
            name="name",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        configuration_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationManager.ConfigurationDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration_definitions: The definition of the Quick Setup configuration that the configuration manager deploys.
        :param description: The description of the configuration.
        :param name: The name of the configuration.
        :param tags: Key-value pairs of metadata to assign to the configuration manager.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12a9f65dcaf9bde5bcf296a113eb81107c3f8fa3375cf583d296e98f6c35b8bc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationManagerProps(
            configuration_definitions=configuration_definitions,
            description=description,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e179f5a174a371bbe7011b09d95b0c0f8863380aab0eca42d0e1c516056fd7f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__10d90d0d66ba3df3f5de0b8ff99770b8d42dfd5facc456d26ad810ff8b812062)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The datetime stamp when the configuration manager was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedAt")
    def attr_last_modified_at(self) -> builtins.str:
        '''The datetime stamp when the configuration manager was last updated.

        :cloudformationAttribute: LastModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrManagerArn")
    def attr_manager_arn(self) -> builtins.str:
        '''The ARN of the Quick Setup configuration.

        :cloudformationAttribute: ManagerArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrManagerArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusSummaries")
    def attr_status_summaries(self) -> _IResolvable_da3f097b:
        '''Summaries of the state of the configuration manager.

        These summaries include an aggregate of the statuses from the configuration definition associated with the configuration manager. This includes deployment statuses, association statuses, drift statuses, health checks, and more.

        :cloudformationAttribute: StatusSummaries
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrStatusSummaries"))

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
    @jsii.member(jsii_name="configurationDefinitions")
    def configuration_definitions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationManager.ConfigurationDefinitionProperty"]]]:
        '''The definition of the Quick Setup configuration that the configuration manager deploys.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationManager.ConfigurationDefinitionProperty"]]], jsii.get(self, "configurationDefinitions"))

    @configuration_definitions.setter
    def configuration_definitions(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationManager.ConfigurationDefinitionProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f9aeebefd7ded0fa6621da4ee350d72e44673d4d472c3967d6a19c3b1ec3fb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationDefinitions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5852dd23f0023b595328038c8285dd65948105e865dc6f9a8d33fa247d3cafdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a06c169a588f9a4b4d4faaa65107990461de3b50e29cd51fe8259fe6982b259f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key-value pairs of metadata to assign to the configuration manager.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e616ab12615353ce8adb7959fdd264518ca60136764500b5507fb35dd10ead43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmquicksetup.CfnConfigurationManager.ConfigurationDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameters": "parameters",
            "type": "type",
            "id": "id",
            "local_deployment_administration_role_arn": "localDeploymentAdministrationRoleArn",
            "local_deployment_execution_role_name": "localDeploymentExecutionRoleName",
            "type_version": "typeVersion",
        },
    )
    class ConfigurationDefinitionProperty:
        def __init__(
            self,
            *,
            parameters: typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b],
            type: builtins.str,
            id: typing.Optional[builtins.str] = None,
            local_deployment_administration_role_arn: typing.Optional[builtins.str] = None,
            local_deployment_execution_role_name: typing.Optional[builtins.str] = None,
            type_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The definition of a Quick Setup configuration.

            :param parameters: The parameters for the configuration definition type. Parameters for configuration definitions vary based the configuration type. The following lists outline the parameters for each configuration type. - **AWS Config Recording (Type: AWS QuickSetupType-CFGRecording)** - - ``RecordAllResources`` - Description: (Optional) A boolean value that determines whether all supported resources are recorded. The default value is " ``true`` ". - ``ResourceTypesToRecord`` - Description: (Optional) A comma separated list of resource types you want to record. - ``RecordGlobalResourceTypes`` - Description: (Optional) A boolean value that determines whether global resources are recorded with all resource configurations. The default value is " ``false`` ". - ``GlobalResourceTypesRegion`` - Description: (Optional) Determines the AWS Region where global resources are recorded. - ``UseCustomBucket`` - Description: (Optional) A boolean value that determines whether a custom Amazon S3 bucket is used for delivery. The default value is " ``false`` ". - ``DeliveryBucketName`` - Description: (Optional) The name of the Amazon S3 bucket you want AWS Config to deliver configuration snapshots and configuration history files to. - ``DeliveryBucketPrefix`` - Description: (Optional) The key prefix you want to use in the custom Amazon S3 bucket. - ``NotificationOptions`` - Description: (Optional) Determines the notification configuration for the recorder. The valid values are ``NoStreaming`` , ``UseExistingTopic`` , and ``CreateTopic`` . The default value is ``NoStreaming`` . - ``CustomDeliveryTopicAccountId`` - Description: (Optional) The ID of the AWS account where the Amazon SNS topic you want to use for notifications resides. You must specify a value for this parameter if you use the ``UseExistingTopic`` notification option. - ``CustomDeliveryTopicName`` - Description: (Optional) The name of the Amazon SNS topic you want to use for notifications. You must specify a value for this parameter if you use the ``UseExistingTopic`` notification option. - ``RemediationSchedule`` - Description: (Optional) A rate expression that defines the schedule for drift remediation. The valid values are ``rate(30 days)`` , ``rate(7 days)`` , ``rate(1 days)`` , and ``none`` . The default value is " ``none`` ". - ``TargetAccounts`` - Description: (Optional) The ID of the AWS account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either ``TargetAccounts`` or ``TargetOrganizationalUnits`` . - ``TargetOrganizationalUnits`` - Description: (Optional) The ID of the root of your Organization. This configuration type doesn't currently support choosing specific OUs. The configuration will be deployed to all the OUs in the Organization. - ``TargetRegions`` - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to. - **Change Manager (Type: AWS QuickSetupType-SSMChangeMgr)** - - ``DelegatedAccountId`` - Description: (Required) The ID of the delegated administrator account. - ``JobFunction`` - Description: (Required) The name for the Change Manager job function. - ``PermissionType`` - Description: (Optional) Specifies whether you want to use default administrator permissions for the job function role, or provide a custom IAM policy. The valid values are ``CustomPermissions`` and ``AdminPermissions`` . The default value for the parameter is ``CustomerPermissions`` . - ``CustomPermissions`` - Description: (Optional) A JSON string containing the IAM policy you want your job function to use. You must provide a value for this parameter if you specify ``CustomPermissions`` for the ``PermissionType`` parameter. - ``TargetOrganizationalUnits`` - Description: (Required) A comma separated list of organizational units (OUs) you want to deploy the configuration to. - ``TargetRegions`` - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to. - **Conformance Packs (Type: AWS QuickSetupType-CFGCPacks)** - - ``DelegatedAccountId`` - Description: (Optional) The ID of the delegated administrator account. This parameter is required for Organization deployments. - ``RemediationSchedule`` - Description: (Optional) A rate expression that defines the schedule for drift remediation. The valid values are ``rate(30 days)`` , ``rate(14 days)`` , ``rate(2 days)`` , and ``none`` . The default value is " ``none`` ". - ``CPackNames`` - Description: (Required) A comma separated list of AWS Config conformance packs. - ``TargetAccounts`` - Description: (Optional) The ID of the AWS account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either ``TargetAccounts`` or ``TargetOrganizationalUnits`` . - ``TargetOrganizationalUnits`` - Description: (Optional) The ID of the root of your Organization. This configuration type doesn't currently support choosing specific OUs. The configuration will be deployed to all the OUs in the Organization. - ``TargetRegions`` - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to. - **Default Host Management Configuration (Type: AWS QuickSetupType-DHMC)** - - ``UpdateSSMAgent`` - Description: (Optional) A boolean value that determines whether the SSM Agent is updated on the target instances every 2 weeks. The default value is " ``true`` ". - ``TargetOrganizationalUnits`` - Description: (Required) A comma separated list of organizational units (OUs) you want to deploy the configuration to. - ``TargetRegions`` - Description: (Required) The AWS Regions to deploy the configuration to. For this type, the parameter only accepts a value of ``AllRegions`` . - **DevOps Guru (Type: AWS QuickSetupType-DevOpsGuru)** - - ``AnalyseAllResources`` - Description: (Optional) A boolean value that determines whether DevOps Guru analyzes all AWS CloudFormation stacks in the account. The default value is " ``false`` ". - ``EnableSnsNotifications`` - Description: (Optional) A boolean value that determines whether DevOps Guru sends notifications when an insight is created. The default value is " ``true`` ". - ``EnableSsmOpsItems`` - Description: (Optional) A boolean value that determines whether DevOps Guru creates an OpsCenter OpsItem when an insight is created. The default value is " ``true`` ". - ``EnableDriftRemediation`` - Description: (Optional) A boolean value that determines whether a drift remediation schedule is used. The default value is " ``false`` ". - ``RemediationSchedule`` - Description: (Optional) A rate expression that defines the schedule for drift remediation. The valid values are ``rate(30 days)`` , ``rate(14 days)`` , ``rate(1 days)`` , and ``none`` . The default value is " ``none`` ". - ``TargetAccounts`` - Description: (Optional) The ID of the AWS account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either ``TargetAccounts`` or ``TargetOrganizationalUnits`` . - ``TargetOrganizationalUnits`` - Description: (Optional) A comma separated list of organizational units (OUs) you want to deploy the configuration to. - ``TargetRegions`` - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to. - **Distributor (Type: AWS QuickSetupType-Distributor)** - - ``PackagesToInstall`` - Description: (Required) A comma separated list of packages you want to install on the target instances. The valid values are ``AWSEFSTools`` , ``AWSCWAgent`` , and ``AWSEC2LaunchAgent`` . - ``RemediationSchedule`` - Description: (Optional) A rate expression that defines the schedule for drift remediation. The valid values are ``rate(30 days)`` , ``rate(14 days)`` , ``rate(2 days)`` , and ``none`` . The default value is " ``rate(30 days)`` ". - ``IsPolicyAttachAllowed`` - Description: (Optional) A boolean value that determines whether Quick Setup attaches policies to instances profiles already associated with the target instances. The default value is " ``false`` ". - ``TargetType`` - Description: (Optional) Determines how instances are targeted for local account deployments. Don't specify a value for this parameter if you're deploying to OUs. The valid values are ``*`` , ``InstanceIds`` , ``ResourceGroups`` , and ``Tags`` . Use ``*`` to target all instances in the account. - ``TargetInstances`` - Description: (Optional) A comma separated list of instance IDs. You must provide a value for this parameter if you specify ``InstanceIds`` for the ``TargetType`` parameter. - ``TargetTagKey`` - Description: (Required) The tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify ``Tags`` for the ``TargetType`` parameter. - ``TargetTagValue`` - Description: (Required) The value of the tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify ``Tags`` for the ``TargetType`` parameter. - ``ResourceGroupName`` - Description: (Required) The name of the resource group associated with the instances you want to target. You must provide a value for this parameter if you specify ``ResourceGroups`` for the ``TargetType`` parameter. - ``TargetAccounts`` - Description: (Optional) The ID of the AWS account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either ``TargetAccounts`` or ``TargetOrganizationalUnits`` . - ``TargetOrganizationalUnits`` - Description: (Optional) A comma separated list of organizational units (OUs) you want to deploy the configuration to. - ``TargetRegions`` - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to. - **Host Management (Type: AWS QuickSetupType-SSMHostMgmt)** - - ``UpdateSSMAgent`` - Description: (Optional) A boolean value that determines whether the SSM Agent is updated on the target instances every 2 weeks. The default value is " ``true`` ". - ``UpdateEc2LaunchAgent`` - Description: (Optional) A boolean value that determines whether the EC2 Launch agent is updated on the target instances every month. The default value is " ``false`` ". - ``CollectInventory`` - Description: (Optional) A boolean value that determines whether instance metadata is collected on the target instances every 30 minutes. The default value is " ``true`` ". - ``ScanInstances`` - Description: (Optional) A boolean value that determines whether the target instances are scanned daily for available patches. The default value is " ``true`` ". - ``InstallCloudWatchAgent`` - Description: (Optional) A boolean value that determines whether the Amazon CloudWatch agent is installed on the target instances. The default value is " ``false`` ". - ``UpdateCloudWatchAgent`` - Description: (Optional) A boolean value that determines whether the Amazon CloudWatch agent is updated on the target instances every month. The default value is " ``false`` ". - ``IsPolicyAttachAllowed`` - Description: (Optional) A boolean value that determines whether Quick Setup attaches policies to instances profiles already associated with the target instances. The default value is " ``false`` ". - ``TargetType`` - Description: (Optional) Determines how instances are targeted for local account deployments. Don't specify a value for this parameter if you're deploying to OUs. The valid values are ``*`` , ``InstanceIds`` , ``ResourceGroups`` , and ``Tags`` . Use ``*`` to target all instances in the account. - ``TargetInstances`` - Description: (Optional) A comma separated list of instance IDs. You must provide a value for this parameter if you specify ``InstanceIds`` for the ``TargetType`` parameter. - ``TargetTagKey`` - Description: (Optional) The tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify ``Tags`` for the ``TargetType`` parameter. - ``TargetTagValue`` - Description: (Optional) The value of the tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify ``Tags`` for the ``TargetType`` parameter. - ``ResourceGroupName`` - Description: (Optional) The name of the resource group associated with the instances you want to target. You must provide a value for this parameter if you specify ``ResourceGroups`` for the ``TargetType`` parameter. - ``TargetAccounts`` - Description: (Optional) The ID of the AWS account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either ``TargetAccounts`` or ``TargetOrganizationalUnits`` . - ``TargetOrganizationalUnits`` - Description: (Optional) A comma separated list of organizational units (OUs) you want to deploy the configuration to. - ``TargetRegions`` - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to. - **OpsCenter (Type: AWS QuickSetupType-SSMOpsCenter)** - - ``DelegatedAccountId`` - Description: (Required) The ID of the delegated administrator account. - ``TargetOrganizationalUnits`` - Description: (Required) A comma separated list of organizational units (OUs) you want to deploy the configuration to. - ``TargetRegions`` - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to. - **Patch Policy (Type: AWS QuickSetupType-PatchPolicy)** - - ``PatchPolicyName`` - Description: (Required) A name for the patch policy. The value you provide is applied to target Amazon EC2 instances as a tag. - ``SelectedPatchBaselines`` - Description: (Required) An array of JSON objects containing the information for the patch baselines to include in your patch policy. - ``PatchBaselineUseDefault`` - Description: (Optional) A value that determines whether the selected patch baselines are all AWS provided. Supported values are ``default`` and ``custom`` . - ``PatchBaselineRegion`` - Description: (Required) The AWS Region where the patch baseline exist. - ``ConfigurationOptionsPatchOperation`` - Description: (Optional) Determines whether target instances scan for available patches, or scan and install available patches. The valid values are ``Scan`` and ``ScanAndInstall`` . The default value for the parameter is ``Scan`` . - ``ConfigurationOptionsScanValue`` - Description: (Optional) A cron expression that is used as the schedule for when instances scan for available patches. - ``ConfigurationOptionsInstallValue`` - Description: (Optional) A cron expression that is used as the schedule for when instances install available patches. - ``ConfigurationOptionsScanNextInterval`` - Description: (Optional) A boolean value that determines whether instances should scan for available patches at the next cron interval. The default value is " ``false`` ". - ``ConfigurationOptionsInstallNextInterval`` - Description: (Optional) A boolean value that determines whether instances should scan for available patches at the next cron interval. The default value is " ``false`` ". - ``RebootOption`` - Description: (Optional) Determines whether instances are rebooted after patches are installed. Valid values are ``RebootIfNeeded`` and ``NoReboot`` . - ``IsPolicyAttachAllowed`` - Description: (Optional) A boolean value that determines whether Quick Setup attaches policies to instances profiles already associated with the target instances. The default value is " ``false`` ". - ``OutputLogEnableS3`` - Description: (Optional) A boolean value that determines whether command output logs are sent to Amazon S3. - ``OutputS3Location`` - Description: (Optional) Information about the Amazon S3 bucket where you want to store the output details of the request. - ``OutputBucketRegion`` - Description: (Optional) The AWS Region where the Amazon S3 bucket you want to deliver command output to is located. - ``OutputS3BucketName`` - Description: (Optional) The name of the Amazon S3 bucket you want to deliver command output to. - ``OutputS3KeyPrefix`` - Description: (Optional) The key prefix you want to use in the custom Amazon S3 bucket. - ``TargetType`` - Description: (Optional) Determines how instances are targeted for local account deployments. Don't specify a value for this parameter if you're deploying to OUs. The valid values are ``*`` , ``InstanceIds`` , ``ResourceGroups`` , and ``Tags`` . Use ``*`` to target all instances in the account. - ``TargetInstances`` - Description: (Optional) A comma separated list of instance IDs. You must provide a value for this parameter if you specify ``InstanceIds`` for the ``TargetType`` parameter. - ``TargetTagKey`` - Description: (Required) The tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify ``Tags`` for the ``TargetType`` parameter. - ``TargetTagValue`` - Description: (Required) The value of the tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify ``Tags`` for the ``TargetType`` parameter. - ``ResourceGroupName`` - Description: (Required) The name of the resource group associated with the instances you want to target. You must provide a value for this parameter if you specify ``ResourceGroups`` for the ``TargetType`` parameter. - ``TargetAccounts`` - Description: (Optional) The ID of the AWS account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either ``TargetAccounts`` or ``TargetOrganizationalUnits`` . - ``TargetOrganizationalUnits`` - Description: (Optional) A comma separated list of organizational units (OUs) you want to deploy the configuration to. - ``TargetRegions`` - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to. - **Resource Explorer (Type: AWS QuickSetupType-ResourceExplorer)** - - ``SelectedAggregatorRegion`` - Description: (Required) The AWS Region where you want to create the aggregator index. - ``ReplaceExistingAggregator`` - Description: (Required) A boolean value that determines whether to demote an existing aggregator if it is in a Region that differs from the value you specify for the ``SelectedAggregatorRegion`` . - ``TargetOrganizationalUnits`` - Description: (Required) A comma separated list of organizational units (OUs) you want to deploy the configuration to. - ``TargetRegions`` - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to. - **Resource Scheduler (Type: AWS QuickSetupType-Scheduler)** - - ``TargetTagKey`` - Description: (Required) The tag key assigned to the instances you want to target. - ``TargetTagValue`` - Description: (Required) The value of the tag key assigned to the instances you want to target. - ``ICalendarString`` - Description: (Required) An iCalendar formatted string containing the schedule you want Change Manager to use. - ``TargetAccounts`` - Description: (Optional) The ID of the AWS account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either ``TargetAccounts`` or ``TargetOrganizationalUnits`` . - ``TargetOrganizationalUnits`` - Description: (Optional) A comma separated list of organizational units (OUs) you want to deploy the configuration to. - ``TargetRegions`` - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to.
            :param type: The type of the Quick Setup configuration.
            :param id: The ID of the configuration definition.
            :param local_deployment_administration_role_arn: The ARN of the IAM role used to administrate local configuration deployments. .. epigraph:: Although this element is listed as "Required: No", a value can be omitted only for organizational deployments of types other than ``AWSQuickSetupType-PatchPolicy`` . A value must be provided when you are running an organizational deployment for a patch policy or running any type of deployment for a single account.
            :param local_deployment_execution_role_name: The name of the IAM role used to deploy local configurations. .. epigraph:: Although this element is listed as "Required: No", a value can be omitted only for organizational deployments of types other than ``AWSQuickSetupType-PatchPolicy`` . A value must be provided when you are running an organizational deployment for a patch policy or running any type of deployment for a single account.
            :param type_version: The version of the Quick Setup type used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmquicksetup-configurationmanager-configurationdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmquicksetup as ssmquicksetup
                
                configuration_definition_property = ssmquicksetup.CfnConfigurationManager.ConfigurationDefinitionProperty(
                    parameters={
                        "parameters_key": "parameters"
                    },
                    type="type",
                
                    # the properties below are optional
                    id="id",
                    local_deployment_administration_role_arn="localDeploymentAdministrationRoleArn",
                    local_deployment_execution_role_name="localDeploymentExecutionRoleName",
                    type_version="typeVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5de88cdf2c4ba7069e306fade91e021ab2a61a9f9d1bdde1ced8a9f3f54e2741)
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument local_deployment_administration_role_arn", value=local_deployment_administration_role_arn, expected_type=type_hints["local_deployment_administration_role_arn"])
                check_type(argname="argument local_deployment_execution_role_name", value=local_deployment_execution_role_name, expected_type=type_hints["local_deployment_execution_role_name"])
                check_type(argname="argument type_version", value=type_version, expected_type=type_hints["type_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parameters": parameters,
                "type": type,
            }
            if id is not None:
                self._values["id"] = id
            if local_deployment_administration_role_arn is not None:
                self._values["local_deployment_administration_role_arn"] = local_deployment_administration_role_arn
            if local_deployment_execution_role_name is not None:
                self._values["local_deployment_execution_role_name"] = local_deployment_execution_role_name
            if type_version is not None:
                self._values["type_version"] = type_version

        @builtins.property
        def parameters(
            self,
        ) -> typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]:
            '''The parameters for the configuration definition type.

            Parameters for configuration definitions vary based the configuration type. The following lists outline the parameters for each configuration type.

            - **AWS Config Recording (Type: AWS QuickSetupType-CFGRecording)** - - ``RecordAllResources``
            - Description: (Optional) A boolean value that determines whether all supported resources are recorded. The default value is " ``true`` ".
            - ``ResourceTypesToRecord``
            - Description: (Optional) A comma separated list of resource types you want to record.
            - ``RecordGlobalResourceTypes``
            - Description: (Optional) A boolean value that determines whether global resources are recorded with all resource configurations. The default value is " ``false`` ".
            - ``GlobalResourceTypesRegion``
            - Description: (Optional) Determines the AWS Region where global resources are recorded.
            - ``UseCustomBucket``
            - Description: (Optional) A boolean value that determines whether a custom Amazon S3 bucket is used for delivery. The default value is " ``false`` ".
            - ``DeliveryBucketName``
            - Description: (Optional) The name of the Amazon S3 bucket you want AWS Config to deliver configuration snapshots and configuration history files to.
            - ``DeliveryBucketPrefix``
            - Description: (Optional) The key prefix you want to use in the custom Amazon S3 bucket.
            - ``NotificationOptions``
            - Description: (Optional) Determines the notification configuration for the recorder. The valid values are ``NoStreaming`` , ``UseExistingTopic`` , and ``CreateTopic`` . The default value is ``NoStreaming`` .
            - ``CustomDeliveryTopicAccountId``
            - Description: (Optional) The ID of the AWS account where the Amazon SNS topic you want to use for notifications resides. You must specify a value for this parameter if you use the ``UseExistingTopic`` notification option.
            - ``CustomDeliveryTopicName``
            - Description: (Optional) The name of the Amazon SNS topic you want to use for notifications. You must specify a value for this parameter if you use the ``UseExistingTopic`` notification option.
            - ``RemediationSchedule``
            - Description: (Optional) A rate expression that defines the schedule for drift remediation. The valid values are ``rate(30 days)`` , ``rate(7 days)`` , ``rate(1 days)`` , and ``none`` . The default value is " ``none`` ".
            - ``TargetAccounts``
            - Description: (Optional) The ID of the AWS account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either ``TargetAccounts`` or ``TargetOrganizationalUnits`` .
            - ``TargetOrganizationalUnits``
            - Description: (Optional) The ID of the root of your Organization. This configuration type doesn't currently support choosing specific OUs. The configuration will be deployed to all the OUs in the Organization.
            - ``TargetRegions``
            - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to.
            - **Change Manager (Type: AWS QuickSetupType-SSMChangeMgr)** - - ``DelegatedAccountId``
            - Description: (Required) The ID of the delegated administrator account.
            - ``JobFunction``
            - Description: (Required) The name for the Change Manager job function.
            - ``PermissionType``
            - Description: (Optional) Specifies whether you want to use default administrator permissions for the job function role, or provide a custom IAM policy. The valid values are ``CustomPermissions`` and ``AdminPermissions`` . The default value for the parameter is ``CustomerPermissions`` .
            - ``CustomPermissions``
            - Description: (Optional) A JSON string containing the IAM policy you want your job function to use. You must provide a value for this parameter if you specify ``CustomPermissions`` for the ``PermissionType`` parameter.
            - ``TargetOrganizationalUnits``
            - Description: (Required) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
            - ``TargetRegions``
            - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to.
            - **Conformance Packs (Type: AWS QuickSetupType-CFGCPacks)** - - ``DelegatedAccountId``
            - Description: (Optional) The ID of the delegated administrator account. This parameter is required for Organization deployments.
            - ``RemediationSchedule``
            - Description: (Optional) A rate expression that defines the schedule for drift remediation. The valid values are ``rate(30 days)`` , ``rate(14 days)`` , ``rate(2 days)`` , and ``none`` . The default value is " ``none`` ".
            - ``CPackNames``
            - Description: (Required) A comma separated list of AWS Config conformance packs.
            - ``TargetAccounts``
            - Description: (Optional) The ID of the AWS account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either ``TargetAccounts`` or ``TargetOrganizationalUnits`` .
            - ``TargetOrganizationalUnits``
            - Description: (Optional) The ID of the root of your Organization. This configuration type doesn't currently support choosing specific OUs. The configuration will be deployed to all the OUs in the Organization.
            - ``TargetRegions``
            - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to.
            - **Default Host Management Configuration (Type: AWS QuickSetupType-DHMC)** - - ``UpdateSSMAgent``
            - Description: (Optional) A boolean value that determines whether the SSM Agent is updated on the target instances every 2 weeks. The default value is " ``true`` ".
            - ``TargetOrganizationalUnits``
            - Description: (Required) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
            - ``TargetRegions``
            - Description: (Required) The AWS Regions to deploy the configuration to. For this type, the parameter only accepts a value of ``AllRegions`` .
            - **DevOps Guru (Type: AWS QuickSetupType-DevOpsGuru)** - - ``AnalyseAllResources``
            - Description: (Optional) A boolean value that determines whether DevOps Guru analyzes all AWS CloudFormation stacks in the account. The default value is " ``false`` ".
            - ``EnableSnsNotifications``
            - Description: (Optional) A boolean value that determines whether DevOps Guru sends notifications when an insight is created. The default value is " ``true`` ".
            - ``EnableSsmOpsItems``
            - Description: (Optional) A boolean value that determines whether DevOps Guru creates an OpsCenter OpsItem when an insight is created. The default value is " ``true`` ".
            - ``EnableDriftRemediation``
            - Description: (Optional) A boolean value that determines whether a drift remediation schedule is used. The default value is " ``false`` ".
            - ``RemediationSchedule``
            - Description: (Optional) A rate expression that defines the schedule for drift remediation. The valid values are ``rate(30 days)`` , ``rate(14 days)`` , ``rate(1 days)`` , and ``none`` . The default value is " ``none`` ".
            - ``TargetAccounts``
            - Description: (Optional) The ID of the AWS account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either ``TargetAccounts`` or ``TargetOrganizationalUnits`` .
            - ``TargetOrganizationalUnits``
            - Description: (Optional) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
            - ``TargetRegions``
            - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to.
            - **Distributor (Type: AWS QuickSetupType-Distributor)** - - ``PackagesToInstall``
            - Description: (Required) A comma separated list of packages you want to install on the target instances. The valid values are ``AWSEFSTools`` , ``AWSCWAgent`` , and ``AWSEC2LaunchAgent`` .
            - ``RemediationSchedule``
            - Description: (Optional) A rate expression that defines the schedule for drift remediation. The valid values are ``rate(30 days)`` , ``rate(14 days)`` , ``rate(2 days)`` , and ``none`` . The default value is " ``rate(30 days)`` ".
            - ``IsPolicyAttachAllowed``
            - Description: (Optional) A boolean value that determines whether Quick Setup attaches policies to instances profiles already associated with the target instances. The default value is " ``false`` ".
            - ``TargetType``
            - Description: (Optional) Determines how instances are targeted for local account deployments. Don't specify a value for this parameter if you're deploying to OUs. The valid values are ``*`` , ``InstanceIds`` , ``ResourceGroups`` , and ``Tags`` . Use ``*`` to target all instances in the account.
            - ``TargetInstances``
            - Description: (Optional) A comma separated list of instance IDs. You must provide a value for this parameter if you specify ``InstanceIds`` for the ``TargetType`` parameter.
            - ``TargetTagKey``
            - Description: (Required) The tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify ``Tags`` for the ``TargetType`` parameter.
            - ``TargetTagValue``
            - Description: (Required) The value of the tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify ``Tags`` for the ``TargetType`` parameter.
            - ``ResourceGroupName``
            - Description: (Required) The name of the resource group associated with the instances you want to target. You must provide a value for this parameter if you specify ``ResourceGroups`` for the ``TargetType`` parameter.
            - ``TargetAccounts``
            - Description: (Optional) The ID of the AWS account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either ``TargetAccounts`` or ``TargetOrganizationalUnits`` .
            - ``TargetOrganizationalUnits``
            - Description: (Optional) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
            - ``TargetRegions``
            - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to.
            - **Host Management (Type: AWS QuickSetupType-SSMHostMgmt)** - - ``UpdateSSMAgent``
            - Description: (Optional) A boolean value that determines whether the SSM Agent is updated on the target instances every 2 weeks. The default value is " ``true`` ".
            - ``UpdateEc2LaunchAgent``
            - Description: (Optional) A boolean value that determines whether the EC2 Launch agent is updated on the target instances every month. The default value is " ``false`` ".
            - ``CollectInventory``
            - Description: (Optional) A boolean value that determines whether instance metadata is collected on the target instances every 30 minutes. The default value is " ``true`` ".
            - ``ScanInstances``
            - Description: (Optional) A boolean value that determines whether the target instances are scanned daily for available patches. The default value is " ``true`` ".
            - ``InstallCloudWatchAgent``
            - Description: (Optional) A boolean value that determines whether the Amazon CloudWatch agent is installed on the target instances. The default value is " ``false`` ".
            - ``UpdateCloudWatchAgent``
            - Description: (Optional) A boolean value that determines whether the Amazon CloudWatch agent is updated on the target instances every month. The default value is " ``false`` ".
            - ``IsPolicyAttachAllowed``
            - Description: (Optional) A boolean value that determines whether Quick Setup attaches policies to instances profiles already associated with the target instances. The default value is " ``false`` ".
            - ``TargetType``
            - Description: (Optional) Determines how instances are targeted for local account deployments. Don't specify a value for this parameter if you're deploying to OUs. The valid values are ``*`` , ``InstanceIds`` , ``ResourceGroups`` , and ``Tags`` . Use ``*`` to target all instances in the account.
            - ``TargetInstances``
            - Description: (Optional) A comma separated list of instance IDs. You must provide a value for this parameter if you specify ``InstanceIds`` for the ``TargetType`` parameter.
            - ``TargetTagKey``
            - Description: (Optional) The tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify ``Tags`` for the ``TargetType`` parameter.
            - ``TargetTagValue``
            - Description: (Optional) The value of the tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify ``Tags`` for the ``TargetType`` parameter.
            - ``ResourceGroupName``
            - Description: (Optional) The name of the resource group associated with the instances you want to target. You must provide a value for this parameter if you specify ``ResourceGroups`` for the ``TargetType`` parameter.
            - ``TargetAccounts``
            - Description: (Optional) The ID of the AWS account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either ``TargetAccounts`` or ``TargetOrganizationalUnits`` .
            - ``TargetOrganizationalUnits``
            - Description: (Optional) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
            - ``TargetRegions``
            - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to.
            - **OpsCenter (Type: AWS QuickSetupType-SSMOpsCenter)** - - ``DelegatedAccountId``
            - Description: (Required) The ID of the delegated administrator account.
            - ``TargetOrganizationalUnits``
            - Description: (Required) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
            - ``TargetRegions``
            - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to.
            - **Patch Policy (Type: AWS QuickSetupType-PatchPolicy)** - - ``PatchPolicyName``
            - Description: (Required) A name for the patch policy. The value you provide is applied to target Amazon EC2 instances as a tag.
            - ``SelectedPatchBaselines``
            - Description: (Required) An array of JSON objects containing the information for the patch baselines to include in your patch policy.
            - ``PatchBaselineUseDefault``
            - Description: (Optional) A value that determines whether the selected patch baselines are all AWS provided. Supported values are ``default`` and ``custom`` .
            - ``PatchBaselineRegion``
            - Description: (Required) The AWS Region where the patch baseline exist.
            - ``ConfigurationOptionsPatchOperation``
            - Description: (Optional) Determines whether target instances scan for available patches, or scan and install available patches. The valid values are ``Scan`` and ``ScanAndInstall`` . The default value for the parameter is ``Scan`` .
            - ``ConfigurationOptionsScanValue``
            - Description: (Optional) A cron expression that is used as the schedule for when instances scan for available patches.
            - ``ConfigurationOptionsInstallValue``
            - Description: (Optional) A cron expression that is used as the schedule for when instances install available patches.
            - ``ConfigurationOptionsScanNextInterval``
            - Description: (Optional) A boolean value that determines whether instances should scan for available patches at the next cron interval. The default value is " ``false`` ".
            - ``ConfigurationOptionsInstallNextInterval``
            - Description: (Optional) A boolean value that determines whether instances should scan for available patches at the next cron interval. The default value is " ``false`` ".
            - ``RebootOption``
            - Description: (Optional) Determines whether instances are rebooted after patches are installed. Valid values are ``RebootIfNeeded`` and ``NoReboot`` .
            - ``IsPolicyAttachAllowed``
            - Description: (Optional) A boolean value that determines whether Quick Setup attaches policies to instances profiles already associated with the target instances. The default value is " ``false`` ".
            - ``OutputLogEnableS3``
            - Description: (Optional) A boolean value that determines whether command output logs are sent to Amazon S3.
            - ``OutputS3Location``
            - Description: (Optional) Information about the Amazon S3 bucket where you want to store the output details of the request.
            - ``OutputBucketRegion``
            - Description: (Optional) The AWS Region where the Amazon S3 bucket you want to deliver command output to is located.
            - ``OutputS3BucketName``
            - Description: (Optional) The name of the Amazon S3 bucket you want to deliver command output to.
            - ``OutputS3KeyPrefix``
            - Description: (Optional) The key prefix you want to use in the custom Amazon S3 bucket.
            - ``TargetType``
            - Description: (Optional) Determines how instances are targeted for local account deployments. Don't specify a value for this parameter if you're deploying to OUs. The valid values are ``*`` , ``InstanceIds`` , ``ResourceGroups`` , and ``Tags`` . Use ``*`` to target all instances in the account.
            - ``TargetInstances``
            - Description: (Optional) A comma separated list of instance IDs. You must provide a value for this parameter if you specify ``InstanceIds`` for the ``TargetType`` parameter.
            - ``TargetTagKey``
            - Description: (Required) The tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify ``Tags`` for the ``TargetType`` parameter.
            - ``TargetTagValue``
            - Description: (Required) The value of the tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify ``Tags`` for the ``TargetType`` parameter.
            - ``ResourceGroupName``
            - Description: (Required) The name of the resource group associated with the instances you want to target. You must provide a value for this parameter if you specify ``ResourceGroups`` for the ``TargetType`` parameter.
            - ``TargetAccounts``
            - Description: (Optional) The ID of the AWS account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either ``TargetAccounts`` or ``TargetOrganizationalUnits`` .
            - ``TargetOrganizationalUnits``
            - Description: (Optional) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
            - ``TargetRegions``
            - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to.
            - **Resource Explorer (Type: AWS QuickSetupType-ResourceExplorer)** - - ``SelectedAggregatorRegion``
            - Description: (Required) The AWS Region where you want to create the aggregator index.
            - ``ReplaceExistingAggregator``
            - Description: (Required) A boolean value that determines whether to demote an existing aggregator if it is in a Region that differs from the value you specify for the ``SelectedAggregatorRegion`` .
            - ``TargetOrganizationalUnits``
            - Description: (Required) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
            - ``TargetRegions``
            - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to.
            - **Resource Scheduler (Type: AWS QuickSetupType-Scheduler)** - - ``TargetTagKey``
            - Description: (Required) The tag key assigned to the instances you want to target.
            - ``TargetTagValue``
            - Description: (Required) The value of the tag key assigned to the instances you want to target.
            - ``ICalendarString``
            - Description: (Required) An iCalendar formatted string containing the schedule you want Change Manager to use.
            - ``TargetAccounts``
            - Description: (Optional) The ID of the AWS account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either ``TargetAccounts`` or ``TargetOrganizationalUnits`` .
            - ``TargetOrganizationalUnits``
            - Description: (Optional) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
            - ``TargetRegions``
            - Description: (Required) A comma separated list of AWS Regions you want to deploy the configuration to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmquicksetup-configurationmanager-configurationdefinition.html#cfn-ssmquicksetup-configurationmanager-configurationdefinition-parameters
            '''
            result = self._values.get("parameters")
            assert result is not None, "Required property 'parameters' is missing"
            return typing.cast(typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the Quick Setup configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmquicksetup-configurationmanager-configurationdefinition.html#cfn-ssmquicksetup-configurationmanager-configurationdefinition-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The ID of the configuration definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmquicksetup-configurationmanager-configurationdefinition.html#cfn-ssmquicksetup-configurationmanager-configurationdefinition-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def local_deployment_administration_role_arn(
            self,
        ) -> typing.Optional[builtins.str]:
            '''The ARN of the IAM role used to administrate local configuration deployments.

            .. epigraph::

               Although this element is listed as "Required: No", a value can be omitted only for organizational deployments of types other than ``AWSQuickSetupType-PatchPolicy`` . A value must be provided when you are running an organizational deployment for a patch policy or running any type of deployment for a single account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmquicksetup-configurationmanager-configurationdefinition.html#cfn-ssmquicksetup-configurationmanager-configurationdefinition-localdeploymentadministrationrolearn
            '''
            result = self._values.get("local_deployment_administration_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def local_deployment_execution_role_name(self) -> typing.Optional[builtins.str]:
            '''The name of the IAM role used to deploy local configurations.

            .. epigraph::

               Although this element is listed as "Required: No", a value can be omitted only for organizational deployments of types other than ``AWSQuickSetupType-PatchPolicy`` . A value must be provided when you are running an organizational deployment for a patch policy or running any type of deployment for a single account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmquicksetup-configurationmanager-configurationdefinition.html#cfn-ssmquicksetup-configurationmanager-configurationdefinition-localdeploymentexecutionrolename
            '''
            result = self._values.get("local_deployment_execution_role_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type_version(self) -> typing.Optional[builtins.str]:
            '''The version of the Quick Setup type used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmquicksetup-configurationmanager-configurationdefinition.html#cfn-ssmquicksetup-configurationmanager-configurationdefinition-typeversion
            '''
            result = self._values.get("type_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ssmquicksetup.CfnConfigurationManager.StatusSummaryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "last_updated_at": "lastUpdatedAt",
            "status_type": "statusType",
            "status": "status",
            "status_details": "statusDetails",
            "status_message": "statusMessage",
        },
    )
    class StatusSummaryProperty:
        def __init__(
            self,
            *,
            last_updated_at: builtins.str,
            status_type: builtins.str,
            status: typing.Optional[builtins.str] = None,
            status_details: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            status_message: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A summarized description of the status.

            :param last_updated_at: The datetime stamp when the status was last updated.
            :param status_type: The type of a status summary.
            :param status: The current status.
            :param status_details: Details about the status.
            :param status_message: When applicable, returns an informational message relevant to the current status and status type of the status summary object. We don't recommend implementing parsing logic around this value since the messages returned can vary in format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmquicksetup-configurationmanager-statussummary.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ssmquicksetup as ssmquicksetup
                
                status_summary_property = ssmquicksetup.CfnConfigurationManager.StatusSummaryProperty(
                    last_updated_at="lastUpdatedAt",
                    status_type="statusType",
                
                    # the properties below are optional
                    status="status",
                    status_details={
                        "status_details_key": "statusDetails"
                    },
                    status_message="statusMessage"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0a15d3717729affa2b751047a4b5b72469d29c10060f85ac60b65e8bc8f4a4e1)
                check_type(argname="argument last_updated_at", value=last_updated_at, expected_type=type_hints["last_updated_at"])
                check_type(argname="argument status_type", value=status_type, expected_type=type_hints["status_type"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument status_details", value=status_details, expected_type=type_hints["status_details"])
                check_type(argname="argument status_message", value=status_message, expected_type=type_hints["status_message"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "last_updated_at": last_updated_at,
                "status_type": status_type,
            }
            if status is not None:
                self._values["status"] = status
            if status_details is not None:
                self._values["status_details"] = status_details
            if status_message is not None:
                self._values["status_message"] = status_message

        @builtins.property
        def last_updated_at(self) -> builtins.str:
            '''The datetime stamp when the status was last updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmquicksetup-configurationmanager-statussummary.html#cfn-ssmquicksetup-configurationmanager-statussummary-lastupdatedat
            '''
            result = self._values.get("last_updated_at")
            assert result is not None, "Required property 'last_updated_at' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def status_type(self) -> builtins.str:
            '''The type of a status summary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmquicksetup-configurationmanager-statussummary.html#cfn-ssmquicksetup-configurationmanager-statussummary-statustype
            '''
            result = self._values.get("status_type")
            assert result is not None, "Required property 'status_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The current status.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmquicksetup-configurationmanager-statussummary.html#cfn-ssmquicksetup-configurationmanager-statussummary-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status_details(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''Details about the status.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmquicksetup-configurationmanager-statussummary.html#cfn-ssmquicksetup-configurationmanager-statussummary-statusdetails
            '''
            result = self._values.get("status_details")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def status_message(self) -> typing.Optional[builtins.str]:
            '''When applicable, returns an informational message relevant to the current status and status type of the status summary object.

            We don't recommend implementing parsing logic around this value since the messages returned can vary in format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssmquicksetup-configurationmanager-statussummary.html#cfn-ssmquicksetup-configurationmanager-statussummary-statusmessage
            '''
            result = self._values.get("status_message")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatusSummaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ssmquicksetup.CfnConfigurationManagerProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_definitions": "configurationDefinitions",
        "description": "description",
        "name": "name",
        "tags": "tags",
    },
)
class CfnConfigurationManagerProps:
    def __init__(
        self,
        *,
        configuration_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationManager.ConfigurationDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigurationManager``.

        :param configuration_definitions: The definition of the Quick Setup configuration that the configuration manager deploys.
        :param description: The description of the configuration.
        :param name: The name of the configuration.
        :param tags: Key-value pairs of metadata to assign to the configuration manager.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmquicksetup-configurationmanager.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ssmquicksetup as ssmquicksetup
            
            cfn_configuration_manager_props = ssmquicksetup.CfnConfigurationManagerProps(
                configuration_definitions=[ssmquicksetup.CfnConfigurationManager.ConfigurationDefinitionProperty(
                    parameters={
                        "parameters_key": "parameters"
                    },
                    type="type",
            
                    # the properties below are optional
                    id="id",
                    local_deployment_administration_role_arn="localDeploymentAdministrationRoleArn",
                    local_deployment_execution_role_name="localDeploymentExecutionRoleName",
                    type_version="typeVersion"
                )],
            
                # the properties below are optional
                description="description",
                name="name",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bd2e12c3bb5f4087218fbe0db9640c52d608411ab3980220b7dd2ff438750e0)
            check_type(argname="argument configuration_definitions", value=configuration_definitions, expected_type=type_hints["configuration_definitions"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_definitions": configuration_definitions,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def configuration_definitions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationManager.ConfigurationDefinitionProperty]]]:
        '''The definition of the Quick Setup configuration that the configuration manager deploys.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmquicksetup-configurationmanager.html#cfn-ssmquicksetup-configurationmanager-configurationdefinitions
        '''
        result = self._values.get("configuration_definitions")
        assert result is not None, "Required property 'configuration_definitions' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationManager.ConfigurationDefinitionProperty]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmquicksetup-configurationmanager.html#cfn-ssmquicksetup-configurationmanager-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmquicksetup-configurationmanager.html#cfn-ssmquicksetup-configurationmanager-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key-value pairs of metadata to assign to the configuration manager.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmquicksetup-configurationmanager.html#cfn-ssmquicksetup-configurationmanager-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationManagerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConfigurationManager",
    "CfnConfigurationManagerProps",
]

publication.publish()

def _typecheckingstub__12a9f65dcaf9bde5bcf296a113eb81107c3f8fa3375cf583d296e98f6c35b8bc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationManager.ConfigurationDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e179f5a174a371bbe7011b09d95b0c0f8863380aab0eca42d0e1c516056fd7f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10d90d0d66ba3df3f5de0b8ff99770b8d42dfd5facc456d26ad810ff8b812062(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f9aeebefd7ded0fa6621da4ee350d72e44673d4d472c3967d6a19c3b1ec3fb9(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationManager.ConfigurationDefinitionProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5852dd23f0023b595328038c8285dd65948105e865dc6f9a8d33fa247d3cafdf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a06c169a588f9a4b4d4faaa65107990461de3b50e29cd51fe8259fe6982b259f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e616ab12615353ce8adb7959fdd264518ca60136764500b5507fb35dd10ead43(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5de88cdf2c4ba7069e306fade91e021ab2a61a9f9d1bdde1ced8a9f3f54e2741(
    *,
    parameters: typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b],
    type: builtins.str,
    id: typing.Optional[builtins.str] = None,
    local_deployment_administration_role_arn: typing.Optional[builtins.str] = None,
    local_deployment_execution_role_name: typing.Optional[builtins.str] = None,
    type_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a15d3717729affa2b751047a4b5b72469d29c10060f85ac60b65e8bc8f4a4e1(
    *,
    last_updated_at: builtins.str,
    status_type: builtins.str,
    status: typing.Optional[builtins.str] = None,
    status_details: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    status_message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bd2e12c3bb5f4087218fbe0db9640c52d608411ab3980220b7dd2ff438750e0(
    *,
    configuration_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationManager.ConfigurationDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
