r'''
# AWS::QBusiness Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_qbusiness as qbusiness
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for QBusiness construct libraries](https://constructs.dev/search?q=qbusiness)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::QBusiness resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_QBusiness.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::QBusiness](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_QBusiness.html).

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
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnApplication",
):
    '''Creates an Amazon Q Business application.

    .. epigraph::

       There are new tiers for Amazon Q Business. Not all features in Amazon Q Business Pro are also available in Amazon Q Business Lite. For information on what's included in Amazon Q Business Lite and what's included in Amazon Q Business Pro, see `Amazon Q Business tiers <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#user-sub-tiers>`_ . You must use the Amazon Q Business console to assign subscription tiers to users.

       An Amazon Q Apps service linked role will be created if it's absent in the AWS account when ``QAppsConfiguration`` is enabled in the request. For more information, see `Using service-linked roles for Q Apps <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles-qapps.html>`_ .

       When you create an application, Amazon Q Business may securely transmit data for processing from your selected AWS region, but within your geography. For more information, see `Cross region inference in Amazon Q Business <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html
    :cloudformationResource: AWS::QBusiness::Application
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_qbusiness as qbusiness
        
        cfn_application = qbusiness.CfnApplication(self, "MyCfnApplication",
            display_name="displayName",
        
            # the properties below are optional
            attachments_configuration=qbusiness.CfnApplication.AttachmentsConfigurationProperty(
                attachments_control_mode="attachmentsControlMode"
            ),
            auto_subscription_configuration=qbusiness.CfnApplication.AutoSubscriptionConfigurationProperty(
                auto_subscribe="autoSubscribe",
        
                # the properties below are optional
                default_subscription_type="defaultSubscriptionType"
            ),
            client_ids_for_oidc=["clientIdsForOidc"],
            description="description",
            encryption_configuration=qbusiness.CfnApplication.EncryptionConfigurationProperty(
                kms_key_id="kmsKeyId"
            ),
            iam_identity_provider_arn="iamIdentityProviderArn",
            identity_center_instance_arn="identityCenterInstanceArn",
            identity_type="identityType",
            personalization_configuration=qbusiness.CfnApplication.PersonalizationConfigurationProperty(
                personalization_control_mode="personalizationControlMode"
            ),
            q_apps_configuration=qbusiness.CfnApplication.QAppsConfigurationProperty(
                q_apps_control_mode="qAppsControlMode"
            ),
            quick_sight_configuration=qbusiness.CfnApplication.QuickSightConfigurationProperty(
                client_namespace="clientNamespace"
            ),
            role_arn="roleArn",
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
        display_name: builtins.str,
        attachments_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.AttachmentsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        auto_subscription_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.AutoSubscriptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        client_ids_for_oidc: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        iam_identity_provider_arn: typing.Optional[builtins.str] = None,
        identity_center_instance_arn: typing.Optional[builtins.str] = None,
        identity_type: typing.Optional[builtins.str] = None,
        personalization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.PersonalizationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        q_apps_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.QAppsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        quick_sight_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.QuickSightConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param display_name: The name of the Amazon Q Business application.
        :param attachments_configuration: Configuration information for the file upload during chat feature.
        :param auto_subscription_configuration: Subscription configuration information for an Amazon Q Business application using IAM identity federation for user management.
        :param client_ids_for_oidc: The OIDC client ID for a Amazon Q Business application.
        :param description: A description for the Amazon Q Business application.
        :param encryption_configuration: Provides the identifier of the AWS KMS key used to encrypt data indexed by Amazon Q Business. Amazon Q Business doesn't support asymmetric keys.
        :param iam_identity_provider_arn: The Amazon Resource Name (ARN) of an identity provider being used by an Amazon Q Business application.
        :param identity_center_instance_arn: The Amazon Resource Name (ARN) of the IAM Identity Center instance you are either creating for—or connecting to—your Amazon Q Business application. *Required* : ``Yes``
        :param identity_type: The authentication type being used by a Amazon Q Business application.
        :param personalization_configuration: Configuration information about chat response personalization. For more information, see `Personalizing chat responses <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html>`_ .
        :param q_apps_configuration: Configuration information about Amazon Q Apps.
        :param quick_sight_configuration: The Amazon QuickSight configuration for an Amazon Q Business application that uses QuickSight as the identity provider.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM role with permissions to access your Amazon CloudWatch logs and metrics. If this property is not specified, Amazon Q Business will create a `service linked role (SLR) <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles.html#slr-permissions>`_ and use it as the application's role.
        :param tags: A list of key-value pairs that identify or categorize your Amazon Q Business application. You can also use tags to help control access to the application. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2c95edfee8896187b03149b15ce3604b3a59bfb3b08abd73c5672b7c0fc870b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            display_name=display_name,
            attachments_configuration=attachments_configuration,
            auto_subscription_configuration=auto_subscription_configuration,
            client_ids_for_oidc=client_ids_for_oidc,
            description=description,
            encryption_configuration=encryption_configuration,
            iam_identity_provider_arn=iam_identity_provider_arn,
            identity_center_instance_arn=identity_center_instance_arn,
            identity_type=identity_type,
            personalization_configuration=personalization_configuration,
            q_apps_configuration=q_apps_configuration,
            quick_sight_configuration=quick_sight_configuration,
            role_arn=role_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47a4b6795acfe5e89f676295cf4c40b3a8dced361f2d77a9b9d10c72aa48712c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d7a38d26d56344056de3cf30103a79b8126175e49d814d22bd2a8de217fa1cd)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationArn")
    def attr_application_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Q Business application.

        :cloudformationAttribute: ApplicationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationId")
    def attr_application_id(self) -> builtins.str:
        '''The identifier for the Amazon Q Business application.

        :cloudformationAttribute: ApplicationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The Unix timestamp when the Amazon Q Business application was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentityCenterApplicationArn")
    def attr_identity_center_application_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AWS IAM Identity Center instance attached to your Amazon Q Business application.

        :cloudformationAttribute: IdentityCenterApplicationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityCenterApplicationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the Amazon Q Business application.

        The application is ready to use when the status is ``ACTIVE`` .

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The Unix timestamp when the Amazon Q Business application was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''The name of the Amazon Q Business application.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33b274b95ca4bace4d079a2b1a1973f1ffbc3a648fc9107b7c44cb7f842f4da1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="attachmentsConfiguration")
    def attachments_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.AttachmentsConfigurationProperty"]]:
        '''Configuration information for the file upload during chat feature.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.AttachmentsConfigurationProperty"]], jsii.get(self, "attachmentsConfiguration"))

    @attachments_configuration.setter
    def attachments_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.AttachmentsConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57c12a095537be640da7b57fecbf3b07e85d4c25f19b33011eba52664eb319bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attachmentsConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="autoSubscriptionConfiguration")
    def auto_subscription_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.AutoSubscriptionConfigurationProperty"]]:
        '''Subscription configuration information for an Amazon Q Business application using IAM identity federation for user management.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.AutoSubscriptionConfigurationProperty"]], jsii.get(self, "autoSubscriptionConfiguration"))

    @auto_subscription_configuration.setter
    def auto_subscription_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.AutoSubscriptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b35a2b0fba0b74bf88677e8d09b2943fd8623f4b30bfa5113d4dd6400769370)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoSubscriptionConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="clientIdsForOidc")
    def client_ids_for_oidc(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The OIDC client ID for a Amazon Q Business application.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clientIdsForOidc"))

    @client_ids_for_oidc.setter
    def client_ids_for_oidc(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e16dbf7c72949c3994e85619024d1169320455f5129fc42720ee3369ccfe5013)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientIdsForOidc", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the Amazon Q Business application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc81ccdbed36f390524b7f7b30696df462f8857fc5dbadb944cf0de3caf79186)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.EncryptionConfigurationProperty"]]:
        '''Provides the identifier of the AWS KMS key used to encrypt data indexed by Amazon Q Business.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.EncryptionConfigurationProperty"]], jsii.get(self, "encryptionConfiguration"))

    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.EncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6de90c5382cc0edcebad422dab80436e0194a3dee33a2061cee4fd766fca3803)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iamIdentityProviderArn")
    def iam_identity_provider_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an identity provider being used by an Amazon Q Business application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamIdentityProviderArn"))

    @iam_identity_provider_arn.setter
    def iam_identity_provider_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b960c5b2a263370b2ed8902e4658a930ce9de4e1d95a848786663e3d07945d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamIdentityProviderArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="identityCenterInstanceArn")
    def identity_center_instance_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM Identity Center instance you are either creating for—or connecting to—your Amazon Q Business application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityCenterInstanceArn"))

    @identity_center_instance_arn.setter
    def identity_center_instance_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e51ab74f20033849c9b717566b2c1f59a066782ff0aafb4adb05ce552f5019a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityCenterInstanceArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="identityType")
    def identity_type(self) -> typing.Optional[builtins.str]:
        '''The authentication type being used by a Amazon Q Business application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityType"))

    @identity_type.setter
    def identity_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44221a178b075fcdd809e631de43085ff6e3f91b9741304fd15e1a0dc442eae1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="personalizationConfiguration")
    def personalization_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.PersonalizationConfigurationProperty"]]:
        '''Configuration information about chat response personalization.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.PersonalizationConfigurationProperty"]], jsii.get(self, "personalizationConfiguration"))

    @personalization_configuration.setter
    def personalization_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.PersonalizationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa9c62867ef8fd21c925099f5633037e806bdc6c1fd8880e42968edf98de8ec2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "personalizationConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="qAppsConfiguration")
    def q_apps_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.QAppsConfigurationProperty"]]:
        '''Configuration information about Amazon Q Apps.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.QAppsConfigurationProperty"]], jsii.get(self, "qAppsConfiguration"))

    @q_apps_configuration.setter
    def q_apps_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.QAppsConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53d92c70961aea8a11ca2bb523fd9f10d2b780d9bda90114e0350e538ef5bd70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "qAppsConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="quickSightConfiguration")
    def quick_sight_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.QuickSightConfigurationProperty"]]:
        '''The Amazon QuickSight configuration for an Amazon Q Business application that uses QuickSight as the identity provider.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.QuickSightConfigurationProperty"]], jsii.get(self, "quickSightConfiguration"))

    @quick_sight_configuration.setter
    def quick_sight_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.QuickSightConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__289094e649887b05a6dfd8fdfb09369f7df0be2c7c7ede77435c953ed16f9d97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quickSightConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an IAM role with permissions to access your Amazon CloudWatch logs and metrics.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1658266e462038ba089b94b22bb7d75b2047bb6b00110e1a3ad8d2941efe4b91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that identify or categorize your Amazon Q Business application.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71701e84c409132b62c2159d4eb096fd21722d0898465ad5f753fb5e9336a3d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnApplication.AttachmentsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"attachments_control_mode": "attachmentsControlMode"},
    )
    class AttachmentsConfigurationProperty:
        def __init__(self, *, attachments_control_mode: builtins.str) -> None:
            '''Configuration information for the file upload during chat feature.

            :param attachments_control_mode: Status information about whether file upload functionality is activated or deactivated for your end user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-attachmentsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                attachments_configuration_property = qbusiness.CfnApplication.AttachmentsConfigurationProperty(
                    attachments_control_mode="attachmentsControlMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e846388f34383d4a53c1ad7c73621d6c0612dd1cab1047d5850af68422a622cc)
                check_type(argname="argument attachments_control_mode", value=attachments_control_mode, expected_type=type_hints["attachments_control_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attachments_control_mode": attachments_control_mode,
            }

        @builtins.property
        def attachments_control_mode(self) -> builtins.str:
            '''Status information about whether file upload functionality is activated or deactivated for your end user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-attachmentsconfiguration.html#cfn-qbusiness-application-attachmentsconfiguration-attachmentscontrolmode
            '''
            result = self._values.get("attachments_control_mode")
            assert result is not None, "Required property 'attachments_control_mode' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttachmentsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnApplication.AutoSubscriptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auto_subscribe": "autoSubscribe",
            "default_subscription_type": "defaultSubscriptionType",
        },
    )
    class AutoSubscriptionConfigurationProperty:
        def __init__(
            self,
            *,
            auto_subscribe: builtins.str,
            default_subscription_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Subscription configuration information for an Amazon Q Business application using IAM identity federation for user management.

            :param auto_subscribe: Describes whether automatic subscriptions are enabled for an Amazon Q Business application using IAM identity federation for user management.
            :param default_subscription_type: Describes the default subscription type assigned to an Amazon Q Business application using IAM identity federation for user management. If the value for ``autoSubscribe`` is set to ``ENABLED`` you must select a value for this field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-autosubscriptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                auto_subscription_configuration_property = qbusiness.CfnApplication.AutoSubscriptionConfigurationProperty(
                    auto_subscribe="autoSubscribe",
                
                    # the properties below are optional
                    default_subscription_type="defaultSubscriptionType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__14d50e4994c3366ddeb7da76131ecc6e103dc3ed4c7bb2ec4ce982b547d2ab3b)
                check_type(argname="argument auto_subscribe", value=auto_subscribe, expected_type=type_hints["auto_subscribe"])
                check_type(argname="argument default_subscription_type", value=default_subscription_type, expected_type=type_hints["default_subscription_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "auto_subscribe": auto_subscribe,
            }
            if default_subscription_type is not None:
                self._values["default_subscription_type"] = default_subscription_type

        @builtins.property
        def auto_subscribe(self) -> builtins.str:
            '''Describes whether automatic subscriptions are enabled for an Amazon Q Business application using IAM identity federation for user management.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-autosubscriptionconfiguration.html#cfn-qbusiness-application-autosubscriptionconfiguration-autosubscribe
            '''
            result = self._values.get("auto_subscribe")
            assert result is not None, "Required property 'auto_subscribe' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def default_subscription_type(self) -> typing.Optional[builtins.str]:
            '''Describes the default subscription type assigned to an Amazon Q Business application using IAM identity federation for user management.

            If the value for ``autoSubscribe`` is set to ``ENABLED`` you must select a value for this field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-autosubscriptionconfiguration.html#cfn-qbusiness-application-autosubscriptionconfiguration-defaultsubscriptiontype
            '''
            result = self._values.get("default_subscription_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoSubscriptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnApplication.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_id": "kmsKeyId"},
    )
    class EncryptionConfigurationProperty:
        def __init__(self, *, kms_key_id: typing.Optional[builtins.str] = None) -> None:
            '''Provides the identifier of the AWS KMS key used to encrypt data indexed by Amazon Q Business.

            Amazon Q Business doesn't support asymmetric keys.

            :param kms_key_id: The identifier of the AWS KMS key. Amazon Q Business doesn't support asymmetric keys.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                encryption_configuration_property = qbusiness.CfnApplication.EncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3ddb5009b3c1bf36876f4e9d68c61c40a1e8a10287a7a292f89a801fcc9ca73)
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The identifier of the AWS KMS key.

            Amazon Q Business doesn't support asymmetric keys.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-encryptionconfiguration.html#cfn-qbusiness-application-encryptionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
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
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnApplication.PersonalizationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"personalization_control_mode": "personalizationControlMode"},
    )
    class PersonalizationConfigurationProperty:
        def __init__(self, *, personalization_control_mode: builtins.str) -> None:
            '''Configuration information about chat response personalization.

            For more information, see `Personalizing chat responses <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html>`_ .

            :param personalization_control_mode: An option to allow Amazon Q Business to customize chat responses using user specific metadata—specifically, location and job information—in your IAM Identity Center instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-personalizationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                personalization_configuration_property = qbusiness.CfnApplication.PersonalizationConfigurationProperty(
                    personalization_control_mode="personalizationControlMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__05c530a7a40f7de7f808af2f7755372bf178629a393e2508771fc91224c8446f)
                check_type(argname="argument personalization_control_mode", value=personalization_control_mode, expected_type=type_hints["personalization_control_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "personalization_control_mode": personalization_control_mode,
            }

        @builtins.property
        def personalization_control_mode(self) -> builtins.str:
            '''An option to allow Amazon Q Business to customize chat responses using user specific metadata—specifically, location and job information—in your IAM Identity Center instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-personalizationconfiguration.html#cfn-qbusiness-application-personalizationconfiguration-personalizationcontrolmode
            '''
            result = self._values.get("personalization_control_mode")
            assert result is not None, "Required property 'personalization_control_mode' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PersonalizationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnApplication.QAppsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"q_apps_control_mode": "qAppsControlMode"},
    )
    class QAppsConfigurationProperty:
        def __init__(self, *, q_apps_control_mode: builtins.str) -> None:
            '''Configuration information about Amazon Q Apps.

            :param q_apps_control_mode: Status information about whether end users can create and use Amazon Q Apps in the web experience.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-qappsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                q_apps_configuration_property = qbusiness.CfnApplication.QAppsConfigurationProperty(
                    q_apps_control_mode="qAppsControlMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6b7142160185e09a91c9d85e4a5dafc98a64398c744201a937b09ca7cc1de37e)
                check_type(argname="argument q_apps_control_mode", value=q_apps_control_mode, expected_type=type_hints["q_apps_control_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "q_apps_control_mode": q_apps_control_mode,
            }

        @builtins.property
        def q_apps_control_mode(self) -> builtins.str:
            '''Status information about whether end users can create and use Amazon Q Apps in the web experience.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-qappsconfiguration.html#cfn-qbusiness-application-qappsconfiguration-qappscontrolmode
            '''
            result = self._values.get("q_apps_control_mode")
            assert result is not None, "Required property 'q_apps_control_mode' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QAppsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnApplication.QuickSightConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"client_namespace": "clientNamespace"},
    )
    class QuickSightConfigurationProperty:
        def __init__(self, *, client_namespace: builtins.str) -> None:
            '''The Amazon QuickSight configuration for an Amazon Q Business application that uses QuickSight as the identity provider.

            For more information, see `Creating an Amazon QuickSight integrated application <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-quicksight-integrated-application.html>`_ .

            :param client_namespace: The Amazon QuickSight namespace that is used as the identity provider. For more information about QuickSight namespaces, see `Namespace operations <https://docs.aws.amazon.com/quicksight/latest/developerguide/namespace-operations.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-quicksightconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                quick_sight_configuration_property = qbusiness.CfnApplication.QuickSightConfigurationProperty(
                    client_namespace="clientNamespace"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2a553c98b052035d7e975a15cd8521cc9a275d10bf22d783650de9883bdd715a)
                check_type(argname="argument client_namespace", value=client_namespace, expected_type=type_hints["client_namespace"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "client_namespace": client_namespace,
            }

        @builtins.property
        def client_namespace(self) -> builtins.str:
            '''The Amazon QuickSight namespace that is used as the identity provider.

            For more information about QuickSight namespaces, see `Namespace operations <https://docs.aws.amazon.com/quicksight/latest/developerguide/namespace-operations.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-application-quicksightconfiguration.html#cfn-qbusiness-application-quicksightconfiguration-clientnamespace
            '''
            result = self._values.get("client_namespace")
            assert result is not None, "Required property 'client_namespace' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QuickSightConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "attachments_configuration": "attachmentsConfiguration",
        "auto_subscription_configuration": "autoSubscriptionConfiguration",
        "client_ids_for_oidc": "clientIdsForOidc",
        "description": "description",
        "encryption_configuration": "encryptionConfiguration",
        "iam_identity_provider_arn": "iamIdentityProviderArn",
        "identity_center_instance_arn": "identityCenterInstanceArn",
        "identity_type": "identityType",
        "personalization_configuration": "personalizationConfiguration",
        "q_apps_configuration": "qAppsConfiguration",
        "quick_sight_configuration": "quickSightConfiguration",
        "role_arn": "roleArn",
        "tags": "tags",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        attachments_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.AttachmentsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        auto_subscription_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.AutoSubscriptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        client_ids_for_oidc: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        iam_identity_provider_arn: typing.Optional[builtins.str] = None,
        identity_center_instance_arn: typing.Optional[builtins.str] = None,
        identity_type: typing.Optional[builtins.str] = None,
        personalization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.PersonalizationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        q_apps_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.QAppsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        quick_sight_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.QuickSightConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param display_name: The name of the Amazon Q Business application.
        :param attachments_configuration: Configuration information for the file upload during chat feature.
        :param auto_subscription_configuration: Subscription configuration information for an Amazon Q Business application using IAM identity federation for user management.
        :param client_ids_for_oidc: The OIDC client ID for a Amazon Q Business application.
        :param description: A description for the Amazon Q Business application.
        :param encryption_configuration: Provides the identifier of the AWS KMS key used to encrypt data indexed by Amazon Q Business. Amazon Q Business doesn't support asymmetric keys.
        :param iam_identity_provider_arn: The Amazon Resource Name (ARN) of an identity provider being used by an Amazon Q Business application.
        :param identity_center_instance_arn: The Amazon Resource Name (ARN) of the IAM Identity Center instance you are either creating for—or connecting to—your Amazon Q Business application. *Required* : ``Yes``
        :param identity_type: The authentication type being used by a Amazon Q Business application.
        :param personalization_configuration: Configuration information about chat response personalization. For more information, see `Personalizing chat responses <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html>`_ .
        :param q_apps_configuration: Configuration information about Amazon Q Apps.
        :param quick_sight_configuration: The Amazon QuickSight configuration for an Amazon Q Business application that uses QuickSight as the identity provider.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM role with permissions to access your Amazon CloudWatch logs and metrics. If this property is not specified, Amazon Q Business will create a `service linked role (SLR) <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles.html#slr-permissions>`_ and use it as the application's role.
        :param tags: A list of key-value pairs that identify or categorize your Amazon Q Business application. You can also use tags to help control access to the application. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_qbusiness as qbusiness
            
            cfn_application_props = qbusiness.CfnApplicationProps(
                display_name="displayName",
            
                # the properties below are optional
                attachments_configuration=qbusiness.CfnApplication.AttachmentsConfigurationProperty(
                    attachments_control_mode="attachmentsControlMode"
                ),
                auto_subscription_configuration=qbusiness.CfnApplication.AutoSubscriptionConfigurationProperty(
                    auto_subscribe="autoSubscribe",
            
                    # the properties below are optional
                    default_subscription_type="defaultSubscriptionType"
                ),
                client_ids_for_oidc=["clientIdsForOidc"],
                description="description",
                encryption_configuration=qbusiness.CfnApplication.EncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                ),
                iam_identity_provider_arn="iamIdentityProviderArn",
                identity_center_instance_arn="identityCenterInstanceArn",
                identity_type="identityType",
                personalization_configuration=qbusiness.CfnApplication.PersonalizationConfigurationProperty(
                    personalization_control_mode="personalizationControlMode"
                ),
                q_apps_configuration=qbusiness.CfnApplication.QAppsConfigurationProperty(
                    q_apps_control_mode="qAppsControlMode"
                ),
                quick_sight_configuration=qbusiness.CfnApplication.QuickSightConfigurationProperty(
                    client_namespace="clientNamespace"
                ),
                role_arn="roleArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd218bde3aa6ce3304b30e1d4799c501a50db8db5cef8926c28924af066170bb)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument attachments_configuration", value=attachments_configuration, expected_type=type_hints["attachments_configuration"])
            check_type(argname="argument auto_subscription_configuration", value=auto_subscription_configuration, expected_type=type_hints["auto_subscription_configuration"])
            check_type(argname="argument client_ids_for_oidc", value=client_ids_for_oidc, expected_type=type_hints["client_ids_for_oidc"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument iam_identity_provider_arn", value=iam_identity_provider_arn, expected_type=type_hints["iam_identity_provider_arn"])
            check_type(argname="argument identity_center_instance_arn", value=identity_center_instance_arn, expected_type=type_hints["identity_center_instance_arn"])
            check_type(argname="argument identity_type", value=identity_type, expected_type=type_hints["identity_type"])
            check_type(argname="argument personalization_configuration", value=personalization_configuration, expected_type=type_hints["personalization_configuration"])
            check_type(argname="argument q_apps_configuration", value=q_apps_configuration, expected_type=type_hints["q_apps_configuration"])
            check_type(argname="argument quick_sight_configuration", value=quick_sight_configuration, expected_type=type_hints["quick_sight_configuration"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "display_name": display_name,
        }
        if attachments_configuration is not None:
            self._values["attachments_configuration"] = attachments_configuration
        if auto_subscription_configuration is not None:
            self._values["auto_subscription_configuration"] = auto_subscription_configuration
        if client_ids_for_oidc is not None:
            self._values["client_ids_for_oidc"] = client_ids_for_oidc
        if description is not None:
            self._values["description"] = description
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if iam_identity_provider_arn is not None:
            self._values["iam_identity_provider_arn"] = iam_identity_provider_arn
        if identity_center_instance_arn is not None:
            self._values["identity_center_instance_arn"] = identity_center_instance_arn
        if identity_type is not None:
            self._values["identity_type"] = identity_type
        if personalization_configuration is not None:
            self._values["personalization_configuration"] = personalization_configuration
        if q_apps_configuration is not None:
            self._values["q_apps_configuration"] = q_apps_configuration
        if quick_sight_configuration is not None:
            self._values["quick_sight_configuration"] = quick_sight_configuration
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the Amazon Q Business application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html#cfn-qbusiness-application-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attachments_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.AttachmentsConfigurationProperty]]:
        '''Configuration information for the file upload during chat feature.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html#cfn-qbusiness-application-attachmentsconfiguration
        '''
        result = self._values.get("attachments_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.AttachmentsConfigurationProperty]], result)

    @builtins.property
    def auto_subscription_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.AutoSubscriptionConfigurationProperty]]:
        '''Subscription configuration information for an Amazon Q Business application using IAM identity federation for user management.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html#cfn-qbusiness-application-autosubscriptionconfiguration
        '''
        result = self._values.get("auto_subscription_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.AutoSubscriptionConfigurationProperty]], result)

    @builtins.property
    def client_ids_for_oidc(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The OIDC client ID for a Amazon Q Business application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html#cfn-qbusiness-application-clientidsforoidc
        '''
        result = self._values.get("client_ids_for_oidc")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the Amazon Q Business application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html#cfn-qbusiness-application-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.EncryptionConfigurationProperty]]:
        '''Provides the identifier of the AWS KMS key used to encrypt data indexed by Amazon Q Business.

        Amazon Q Business doesn't support asymmetric keys.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html#cfn-qbusiness-application-encryptionconfiguration
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.EncryptionConfigurationProperty]], result)

    @builtins.property
    def iam_identity_provider_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an identity provider being used by an Amazon Q Business application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html#cfn-qbusiness-application-iamidentityproviderarn
        '''
        result = self._values.get("iam_identity_provider_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_center_instance_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM Identity Center instance you are either creating for—or connecting to—your Amazon Q Business application.

        *Required* : ``Yes``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html#cfn-qbusiness-application-identitycenterinstancearn
        '''
        result = self._values.get("identity_center_instance_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_type(self) -> typing.Optional[builtins.str]:
        '''The authentication type being used by a Amazon Q Business application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html#cfn-qbusiness-application-identitytype
        '''
        result = self._values.get("identity_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def personalization_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.PersonalizationConfigurationProperty]]:
        '''Configuration information about chat response personalization.

        For more information, see `Personalizing chat responses <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html#cfn-qbusiness-application-personalizationconfiguration
        '''
        result = self._values.get("personalization_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.PersonalizationConfigurationProperty]], result)

    @builtins.property
    def q_apps_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.QAppsConfigurationProperty]]:
        '''Configuration information about Amazon Q Apps.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html#cfn-qbusiness-application-qappsconfiguration
        '''
        result = self._values.get("q_apps_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.QAppsConfigurationProperty]], result)

    @builtins.property
    def quick_sight_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.QuickSightConfigurationProperty]]:
        '''The Amazon QuickSight configuration for an Amazon Q Business application that uses QuickSight as the identity provider.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html#cfn-qbusiness-application-quicksightconfiguration
        '''
        result = self._values.get("quick_sight_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.QuickSightConfigurationProperty]], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an IAM role with permissions to access your Amazon CloudWatch logs and metrics.

        If this property is not specified, Amazon Q Business will create a `service linked role (SLR) <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles.html#slr-permissions>`_ and use it as the application's role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html#cfn-qbusiness-application-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that identify or categorize your Amazon Q Business application.

        You can also use tags to help control access to the application. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-application.html#cfn-qbusiness-application-tags
        :: .
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnDataAccessor(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataAccessor",
):
    '''Creates a new data accessor for an ISV to access data from a Amazon Q Business application.

    The data accessor is an entity that represents the ISV's access to the Amazon Q Business application's data. It includes the IAM role ARN for the ISV, a friendly name, and a set of action configurations that define the specific actions the ISV is allowed to perform and any associated data filters. When the data accessor is created, an IAM Identity Center application is also created to manage the ISV's identity and authentication for accessing the Amazon Q Business application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-dataaccessor.html
    :cloudformationResource: AWS::QBusiness::DataAccessor
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_qbusiness as qbusiness
        
        # attribute_filter_property_: qbusiness.CfnDataAccessor.AttributeFilterProperty
        
        cfn_data_accessor = qbusiness.CfnDataAccessor(self, "MyCfnDataAccessor",
            action_configurations=[qbusiness.CfnDataAccessor.ActionConfigurationProperty(
                action="action",
        
                # the properties below are optional
                filter_configuration=qbusiness.CfnDataAccessor.ActionFilterConfigurationProperty(
                    document_attribute_filter=qbusiness.CfnDataAccessor.AttributeFilterProperty(
                        and_all_filters=[attribute_filter_property_],
                        contains_all=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                            name="name",
                            value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        contains_any=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                            name="name",
                            value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        equals_to=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                            name="name",
                            value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        greater_than=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                            name="name",
                            value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        greater_than_or_equals=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                            name="name",
                            value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        less_than=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                            name="name",
                            value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        less_than_or_equals=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                            name="name",
                            value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        not_filter=attribute_filter_property_,
                        or_all_filters=[attribute_filter_property_]
                    )
                )
            )],
            application_id="applicationId",
            display_name="displayName",
            principal="principal",
        
            # the properties below are optional
            authentication_detail=qbusiness.CfnDataAccessor.DataAccessorAuthenticationDetailProperty(
                authentication_type="authenticationType",
        
                # the properties below are optional
                authentication_configuration=qbusiness.CfnDataAccessor.DataAccessorAuthenticationConfigurationProperty(
                    idc_trusted_token_issuer_configuration=qbusiness.CfnDataAccessor.DataAccessorIdcTrustedTokenIssuerConfigurationProperty(
                        idc_trusted_token_issuer_arn="idcTrustedTokenIssuerArn"
                    )
                ),
                external_ids=["externalIds"]
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
        action_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.ActionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        application_id: builtins.str,
        display_name: builtins.str,
        principal: builtins.str,
        authentication_detail: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.DataAccessorAuthenticationDetailProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param action_configurations: A list of action configurations specifying the allowed actions and any associated filters.
        :param application_id: The unique identifier of the Amazon Q Business application.
        :param display_name: The friendly name of the data accessor.
        :param principal: The Amazon Resource Name (ARN) of the IAM role for the ISV associated with this data accessor.
        :param authentication_detail: The authentication configuration details for the data accessor. This specifies how the ISV authenticates when accessing data through this data accessor.
        :param tags: The tags to associate with the data accessor.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b7ecf69912e25edcd2354b3e0497931ea6bf042b1aabc881c8677d2f9be633)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataAccessorProps(
            action_configurations=action_configurations,
            application_id=application_id,
            display_name=display_name,
            principal=principal,
            authentication_detail=authentication_detail,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff90302eca1e0f24b3ab926881bc0099a551d74c3a71debb214f222b63ff0ee4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__75e79c605177a09c4ca1c1253b30113e8f2b7e023dafa75d6583c9b993c3a905)
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
        '''The timestamp when the data accessor was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDataAccessorArn")
    def attr_data_accessor_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the data accessor.

        :cloudformationAttribute: DataAccessorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDataAccessorArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDataAccessorId")
    def attr_data_accessor_id(self) -> builtins.str:
        '''The unique identifier of the data accessor.

        :cloudformationAttribute: DataAccessorId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDataAccessorId"))

    @builtins.property
    @jsii.member(jsii_name="attrIdcApplicationArn")
    def attr_idc_application_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the associated IAM Identity Center application.

        :cloudformationAttribute: IdcApplicationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdcApplicationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the data accessor was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="actionConfigurations")
    def action_configurations(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.ActionConfigurationProperty"]]]:
        '''A list of action configurations specifying the allowed actions and any associated filters.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.ActionConfigurationProperty"]]], jsii.get(self, "actionConfigurations"))

    @action_configurations.setter
    def action_configurations(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.ActionConfigurationProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a27c05d04ed77ea1630a00c4575933bd29a7548e12cd5406b1a703d094f618f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier of the Amazon Q Business application.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d51b8675a76ff8aa3cd324d2a65da776f4afb1d4600f74839c262998a87adb06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''The friendly name of the data accessor.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d24d4191af1a9b63f7ef66ae53cd5e78c9587db0b3d4e54adc5863415cdec9f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role for the ISV associated with this data accessor.'''
        return typing.cast(builtins.str, jsii.get(self, "principal"))

    @principal.setter
    def principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd64ede16f385d2990fa12fa363564c55f359fed279a75365018e42cd6e63fff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="authenticationDetail")
    def authentication_detail(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DataAccessorAuthenticationDetailProperty"]]:
        '''The authentication configuration details for the data accessor.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DataAccessorAuthenticationDetailProperty"]], jsii.get(self, "authenticationDetail"))

    @authentication_detail.setter
    def authentication_detail(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DataAccessorAuthenticationDetailProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aa34af043257e0411af6e09ebeda77531edcaba51ad9fd392b4515b8c730792)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationDetail", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to associate with the data accessor.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17fcd903858daed5111fdf34ce66e12720cfa6fd9e1712eb5744a4b8c06fb1fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataAccessor.ActionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "filter_configuration": "filterConfiguration",
        },
    )
    class ActionConfigurationProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.ActionFilterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies an allowed action and its associated filter configuration.

            :param action: The Amazon Q Business action that is allowed.
            :param filter_configuration: The filter configuration for the action, if any.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-actionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                # attribute_filter_property_: qbusiness.CfnDataAccessor.AttributeFilterProperty
                
                action_configuration_property = qbusiness.CfnDataAccessor.ActionConfigurationProperty(
                    action="action",
                
                    # the properties below are optional
                    filter_configuration=qbusiness.CfnDataAccessor.ActionFilterConfigurationProperty(
                        document_attribute_filter=qbusiness.CfnDataAccessor.AttributeFilterProperty(
                            and_all_filters=[attribute_filter_property_],
                            contains_all=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                                name="name",
                                value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                    date_value="dateValue",
                                    long_value=123,
                                    string_list_value=["stringListValue"],
                                    string_value="stringValue"
                                )
                            ),
                            contains_any=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                                name="name",
                                value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                    date_value="dateValue",
                                    long_value=123,
                                    string_list_value=["stringListValue"],
                                    string_value="stringValue"
                                )
                            ),
                            equals_to=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                                name="name",
                                value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                    date_value="dateValue",
                                    long_value=123,
                                    string_list_value=["stringListValue"],
                                    string_value="stringValue"
                                )
                            ),
                            greater_than=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                                name="name",
                                value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                    date_value="dateValue",
                                    long_value=123,
                                    string_list_value=["stringListValue"],
                                    string_value="stringValue"
                                )
                            ),
                            greater_than_or_equals=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                                name="name",
                                value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                    date_value="dateValue",
                                    long_value=123,
                                    string_list_value=["stringListValue"],
                                    string_value="stringValue"
                                )
                            ),
                            less_than=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                                name="name",
                                value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                    date_value="dateValue",
                                    long_value=123,
                                    string_list_value=["stringListValue"],
                                    string_value="stringValue"
                                )
                            ),
                            less_than_or_equals=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                                name="name",
                                value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                    date_value="dateValue",
                                    long_value=123,
                                    string_list_value=["stringListValue"],
                                    string_value="stringValue"
                                )
                            ),
                            not_filter=attribute_filter_property_,
                            or_all_filters=[attribute_filter_property_]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__070f31842bf80fdbf737bccdee5b0121eca70d5c6c0d69c119f4d283e3dc8f0f)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument filter_configuration", value=filter_configuration, expected_type=type_hints["filter_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
            }
            if filter_configuration is not None:
                self._values["filter_configuration"] = filter_configuration

        @builtins.property
        def action(self) -> builtins.str:
            '''The Amazon Q Business action that is allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-actionconfiguration.html#cfn-qbusiness-dataaccessor-actionconfiguration-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def filter_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.ActionFilterConfigurationProperty"]]:
            '''The filter configuration for the action, if any.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-actionconfiguration.html#cfn-qbusiness-dataaccessor-actionconfiguration-filterconfiguration
            '''
            result = self._values.get("filter_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.ActionFilterConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataAccessor.ActionFilterConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"document_attribute_filter": "documentAttributeFilter"},
    )
    class ActionFilterConfigurationProperty:
        def __init__(
            self,
            *,
            document_attribute_filter: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.AttributeFilterProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Specifies filters to apply to an allowed action.

            :param document_attribute_filter: Enables filtering of responses based on document attributes or metadata fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-actionfilterconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                # attribute_filter_property_: qbusiness.CfnDataAccessor.AttributeFilterProperty
                
                action_filter_configuration_property = qbusiness.CfnDataAccessor.ActionFilterConfigurationProperty(
                    document_attribute_filter=qbusiness.CfnDataAccessor.AttributeFilterProperty(
                        and_all_filters=[attribute_filter_property_],
                        contains_all=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                            name="name",
                            value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        contains_any=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                            name="name",
                            value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        equals_to=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                            name="name",
                            value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        greater_than=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                            name="name",
                            value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        greater_than_or_equals=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                            name="name",
                            value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        less_than=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                            name="name",
                            value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        less_than_or_equals=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                            name="name",
                            value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        not_filter=attribute_filter_property_,
                        or_all_filters=[attribute_filter_property_]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d8fdd75aa62747889da79fe0b8ab1526d92b0a13360be1d371fd7ca34ee6894e)
                check_type(argname="argument document_attribute_filter", value=document_attribute_filter, expected_type=type_hints["document_attribute_filter"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "document_attribute_filter": document_attribute_filter,
            }

        @builtins.property
        def document_attribute_filter(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.AttributeFilterProperty"]:
            '''Enables filtering of responses based on document attributes or metadata fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-actionfilterconfiguration.html#cfn-qbusiness-dataaccessor-actionfilterconfiguration-documentattributefilter
            '''
            result = self._values.get("document_attribute_filter")
            assert result is not None, "Required property 'document_attribute_filter' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.AttributeFilterProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionFilterConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataAccessor.AttributeFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "and_all_filters": "andAllFilters",
            "contains_all": "containsAll",
            "contains_any": "containsAny",
            "equals_to": "equalsTo",
            "greater_than": "greaterThan",
            "greater_than_or_equals": "greaterThanOrEquals",
            "less_than": "lessThan",
            "less_than_or_equals": "lessThanOrEquals",
            "not_filter": "notFilter",
            "or_all_filters": "orAllFilters",
        },
    )
    class AttributeFilterProperty:
        def __init__(
            self,
            *,
            and_all_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.AttributeFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            contains_all: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.DocumentAttributeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            contains_any: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.DocumentAttributeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            equals_to: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.DocumentAttributeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            greater_than: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.DocumentAttributeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            greater_than_or_equals: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.DocumentAttributeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            less_than: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.DocumentAttributeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            less_than_or_equals: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.DocumentAttributeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            not_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.AttributeFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            or_all_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.AttributeFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Enables filtering of responses based on document attributes or metadata fields.

            :param and_all_filters: Performs a logical ``AND`` operation on all supplied filters.
            :param contains_all: Returns ``true`` when a document contains all the specified document attributes or metadata fields. Supported for the following `document attribute value types <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html>`_ : ``stringListValue`` .
            :param contains_any: Returns ``true`` when a document contains any of the specified document attributes or metadata fields. Supported for the following `document attribute value types <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html>`_ : ``stringListValue`` .
            :param equals_to: Performs an equals operation on two document attributes or metadata fields. Supported for the following `document attribute value types <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html>`_ : ``dateValue`` , ``longValue`` , ``stringListValue`` and ``stringValue`` .
            :param greater_than: Performs a greater than operation on two document attributes or metadata fields. Supported for the following `document attribute value types <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html>`_ : ``dateValue`` and ``longValue`` .
            :param greater_than_or_equals: Performs a greater or equals than operation on two document attributes or metadata fields. Supported for the following `document attribute value types <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html>`_ : ``dateValue`` and ``longValue`` .
            :param less_than: Performs a less than operation on two document attributes or metadata fields. Supported for the following `document attribute value types <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html>`_ : ``dateValue`` and ``longValue`` .
            :param less_than_or_equals: Performs a less than or equals operation on two document attributes or metadata fields.Supported for the following `document attribute value type <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html>`_ : ``dateValue`` and ``longValue`` .
            :param not_filter: Performs a logical ``NOT`` operation on all supplied filters.
            :param or_all_filters: Performs a logical ``OR`` operation on all supplied filters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-attributefilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                # attribute_filter_property_: qbusiness.CfnDataAccessor.AttributeFilterProperty
                
                attribute_filter_property = qbusiness.CfnDataAccessor.AttributeFilterProperty(
                    and_all_filters=[attribute_filter_property_],
                    contains_all=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                        name="name",
                        value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    ),
                    contains_any=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                        name="name",
                        value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    ),
                    equals_to=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                        name="name",
                        value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    ),
                    greater_than=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                        name="name",
                        value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    ),
                    greater_than_or_equals=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                        name="name",
                        value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    ),
                    less_than=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                        name="name",
                        value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    ),
                    less_than_or_equals=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                        name="name",
                        value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    ),
                    not_filter=attribute_filter_property_,
                    or_all_filters=[attribute_filter_property_]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e0944dd9fc73c38902199011a9a1b06a552398d255157793794e769d86581ed7)
                check_type(argname="argument and_all_filters", value=and_all_filters, expected_type=type_hints["and_all_filters"])
                check_type(argname="argument contains_all", value=contains_all, expected_type=type_hints["contains_all"])
                check_type(argname="argument contains_any", value=contains_any, expected_type=type_hints["contains_any"])
                check_type(argname="argument equals_to", value=equals_to, expected_type=type_hints["equals_to"])
                check_type(argname="argument greater_than", value=greater_than, expected_type=type_hints["greater_than"])
                check_type(argname="argument greater_than_or_equals", value=greater_than_or_equals, expected_type=type_hints["greater_than_or_equals"])
                check_type(argname="argument less_than", value=less_than, expected_type=type_hints["less_than"])
                check_type(argname="argument less_than_or_equals", value=less_than_or_equals, expected_type=type_hints["less_than_or_equals"])
                check_type(argname="argument not_filter", value=not_filter, expected_type=type_hints["not_filter"])
                check_type(argname="argument or_all_filters", value=or_all_filters, expected_type=type_hints["or_all_filters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if and_all_filters is not None:
                self._values["and_all_filters"] = and_all_filters
            if contains_all is not None:
                self._values["contains_all"] = contains_all
            if contains_any is not None:
                self._values["contains_any"] = contains_any
            if equals_to is not None:
                self._values["equals_to"] = equals_to
            if greater_than is not None:
                self._values["greater_than"] = greater_than
            if greater_than_or_equals is not None:
                self._values["greater_than_or_equals"] = greater_than_or_equals
            if less_than is not None:
                self._values["less_than"] = less_than
            if less_than_or_equals is not None:
                self._values["less_than_or_equals"] = less_than_or_equals
            if not_filter is not None:
                self._values["not_filter"] = not_filter
            if or_all_filters is not None:
                self._values["or_all_filters"] = or_all_filters

        @builtins.property
        def and_all_filters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.AttributeFilterProperty"]]]]:
            '''Performs a logical ``AND`` operation on all supplied filters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-attributefilter.html#cfn-qbusiness-dataaccessor-attributefilter-andallfilters
            '''
            result = self._values.get("and_all_filters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.AttributeFilterProperty"]]]], result)

        @builtins.property
        def contains_all(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeProperty"]]:
            '''Returns ``true`` when a document contains all the specified document attributes or metadata fields.

            Supported for the following `document attribute value types <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html>`_ : ``stringListValue`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-attributefilter.html#cfn-qbusiness-dataaccessor-attributefilter-containsall
            '''
            result = self._values.get("contains_all")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeProperty"]], result)

        @builtins.property
        def contains_any(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeProperty"]]:
            '''Returns ``true`` when a document contains any of the specified document attributes or metadata fields.

            Supported for the following `document attribute value types <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html>`_ : ``stringListValue`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-attributefilter.html#cfn-qbusiness-dataaccessor-attributefilter-containsany
            '''
            result = self._values.get("contains_any")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeProperty"]], result)

        @builtins.property
        def equals_to(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeProperty"]]:
            '''Performs an equals operation on two document attributes or metadata fields.

            Supported for the following `document attribute value types <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html>`_ : ``dateValue`` , ``longValue`` , ``stringListValue`` and ``stringValue`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-attributefilter.html#cfn-qbusiness-dataaccessor-attributefilter-equalsto
            '''
            result = self._values.get("equals_to")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeProperty"]], result)

        @builtins.property
        def greater_than(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeProperty"]]:
            '''Performs a greater than operation on two document attributes or metadata fields.

            Supported for the following `document attribute value types <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html>`_ : ``dateValue`` and ``longValue`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-attributefilter.html#cfn-qbusiness-dataaccessor-attributefilter-greaterthan
            '''
            result = self._values.get("greater_than")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeProperty"]], result)

        @builtins.property
        def greater_than_or_equals(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeProperty"]]:
            '''Performs a greater or equals than operation on two document attributes or metadata fields.

            Supported for the following `document attribute value types <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html>`_ : ``dateValue`` and ``longValue`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-attributefilter.html#cfn-qbusiness-dataaccessor-attributefilter-greaterthanorequals
            '''
            result = self._values.get("greater_than_or_equals")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeProperty"]], result)

        @builtins.property
        def less_than(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeProperty"]]:
            '''Performs a less than operation on two document attributes or metadata fields.

            Supported for the following `document attribute value types <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html>`_ : ``dateValue`` and ``longValue`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-attributefilter.html#cfn-qbusiness-dataaccessor-attributefilter-lessthan
            '''
            result = self._values.get("less_than")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeProperty"]], result)

        @builtins.property
        def less_than_or_equals(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeProperty"]]:
            '''Performs a less than or equals operation on two document attributes or metadata fields.Supported for the following `document attribute value type <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeValue.html>`_ : ``dateValue`` and ``longValue`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-attributefilter.html#cfn-qbusiness-dataaccessor-attributefilter-lessthanorequals
            '''
            result = self._values.get("less_than_or_equals")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeProperty"]], result)

        @builtins.property
        def not_filter(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.AttributeFilterProperty"]]:
            '''Performs a logical ``NOT`` operation on all supplied filters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-attributefilter.html#cfn-qbusiness-dataaccessor-attributefilter-notfilter
            '''
            result = self._values.get("not_filter")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.AttributeFilterProperty"]], result)

        @builtins.property
        def or_all_filters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.AttributeFilterProperty"]]]]:
            '''Performs a logical ``OR`` operation on all supplied filters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-attributefilter.html#cfn-qbusiness-dataaccessor-attributefilter-orallfilters
            '''
            result = self._values.get("or_all_filters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.AttributeFilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataAccessor.DataAccessorAuthenticationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "idc_trusted_token_issuer_configuration": "idcTrustedTokenIssuerConfiguration",
        },
    )
    class DataAccessorAuthenticationConfigurationProperty:
        def __init__(
            self,
            *,
            idc_trusted_token_issuer_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.DataAccessorIdcTrustedTokenIssuerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A union type that contains the specific authentication configuration based on the authentication type selected.

            :param idc_trusted_token_issuer_configuration: Configuration for IAM Identity Center Trusted Token Issuer (TTI) authentication used when the authentication type is ``AWS_IAM_IDC_TTI`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                data_accessor_authentication_configuration_property = qbusiness.CfnDataAccessor.DataAccessorAuthenticationConfigurationProperty(
                    idc_trusted_token_issuer_configuration=qbusiness.CfnDataAccessor.DataAccessorIdcTrustedTokenIssuerConfigurationProperty(
                        idc_trusted_token_issuer_arn="idcTrustedTokenIssuerArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5026e300a407a951a2bf85ba48cf1646fb1b1672f84f2ea26974311fd2b650de)
                check_type(argname="argument idc_trusted_token_issuer_configuration", value=idc_trusted_token_issuer_configuration, expected_type=type_hints["idc_trusted_token_issuer_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "idc_trusted_token_issuer_configuration": idc_trusted_token_issuer_configuration,
            }

        @builtins.property
        def idc_trusted_token_issuer_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DataAccessorIdcTrustedTokenIssuerConfigurationProperty"]:
            '''Configuration for IAM Identity Center Trusted Token Issuer (TTI) authentication used when the authentication type is ``AWS_IAM_IDC_TTI`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationconfiguration.html#cfn-qbusiness-dataaccessor-dataaccessorauthenticationconfiguration-idctrustedtokenissuerconfiguration
            '''
            result = self._values.get("idc_trusted_token_issuer_configuration")
            assert result is not None, "Required property 'idc_trusted_token_issuer_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DataAccessorIdcTrustedTokenIssuerConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataAccessorAuthenticationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataAccessor.DataAccessorAuthenticationDetailProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_type": "authenticationType",
            "authentication_configuration": "authenticationConfiguration",
            "external_ids": "externalIds",
        },
    )
    class DataAccessorAuthenticationDetailProperty:
        def __init__(
            self,
            *,
            authentication_type: builtins.str,
            authentication_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.DataAccessorAuthenticationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            external_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Contains the authentication configuration details for a data accessor.

            This structure defines how the ISV authenticates when accessing data through the data accessor.

            :param authentication_type: The type of authentication to use for the data accessor. This determines how the ISV authenticates when accessing data. You can use one of two authentication types: - ``AWS_IAM_IDC_TTI`` - Authentication using IAM Identity Center Trusted Token Issuer (TTI). This authentication type allows the ISV to use a trusted token issuer to generate tokens for accessing the data. - ``AWS_IAM_IDC_AUTH_CODE`` - Authentication using IAM Identity Center authorization code flow. This authentication type uses the standard OAuth 2.0 authorization code flow for authentication.
            :param authentication_configuration: The specific authentication configuration based on the authentication type.
            :param external_ids: A list of external identifiers associated with this authentication configuration. These are used to correlate the data accessor with external systems.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationdetail.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                data_accessor_authentication_detail_property = qbusiness.CfnDataAccessor.DataAccessorAuthenticationDetailProperty(
                    authentication_type="authenticationType",
                
                    # the properties below are optional
                    authentication_configuration=qbusiness.CfnDataAccessor.DataAccessorAuthenticationConfigurationProperty(
                        idc_trusted_token_issuer_configuration=qbusiness.CfnDataAccessor.DataAccessorIdcTrustedTokenIssuerConfigurationProperty(
                            idc_trusted_token_issuer_arn="idcTrustedTokenIssuerArn"
                        )
                    ),
                    external_ids=["externalIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ce3d0eb33f705ecbcd9b23e1fae7014cc8010d410a8398ce3feea55694ebed37)
                check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
                check_type(argname="argument authentication_configuration", value=authentication_configuration, expected_type=type_hints["authentication_configuration"])
                check_type(argname="argument external_ids", value=external_ids, expected_type=type_hints["external_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authentication_type": authentication_type,
            }
            if authentication_configuration is not None:
                self._values["authentication_configuration"] = authentication_configuration
            if external_ids is not None:
                self._values["external_ids"] = external_ids

        @builtins.property
        def authentication_type(self) -> builtins.str:
            '''The type of authentication to use for the data accessor.

            This determines how the ISV authenticates when accessing data. You can use one of two authentication types:

            - ``AWS_IAM_IDC_TTI`` - Authentication using IAM Identity Center Trusted Token Issuer (TTI). This authentication type allows the ISV to use a trusted token issuer to generate tokens for accessing the data.
            - ``AWS_IAM_IDC_AUTH_CODE`` - Authentication using IAM Identity Center authorization code flow. This authentication type uses the standard OAuth 2.0 authorization code flow for authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationdetail.html#cfn-qbusiness-dataaccessor-dataaccessorauthenticationdetail-authenticationtype
            '''
            result = self._values.get("authentication_type")
            assert result is not None, "Required property 'authentication_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def authentication_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DataAccessorAuthenticationConfigurationProperty"]]:
            '''The specific authentication configuration based on the authentication type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationdetail.html#cfn-qbusiness-dataaccessor-dataaccessorauthenticationdetail-authenticationconfiguration
            '''
            result = self._values.get("authentication_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DataAccessorAuthenticationConfigurationProperty"]], result)

        @builtins.property
        def external_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of external identifiers associated with this authentication configuration.

            These are used to correlate the data accessor with external systems.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-dataaccessorauthenticationdetail.html#cfn-qbusiness-dataaccessor-dataaccessorauthenticationdetail-externalids
            '''
            result = self._values.get("external_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataAccessorAuthenticationDetailProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataAccessor.DataAccessorIdcTrustedTokenIssuerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"idc_trusted_token_issuer_arn": "idcTrustedTokenIssuerArn"},
    )
    class DataAccessorIdcTrustedTokenIssuerConfigurationProperty:
        def __init__(self, *, idc_trusted_token_issuer_arn: builtins.str) -> None:
            '''Configuration details for IAM Identity Center Trusted Token Issuer (TTI) authentication.

            :param idc_trusted_token_issuer_arn: The Amazon Resource Name (ARN) of the IAM Identity Center Trusted Token Issuer that will be used for authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-dataaccessoridctrustedtokenissuerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                data_accessor_idc_trusted_token_issuer_configuration_property = qbusiness.CfnDataAccessor.DataAccessorIdcTrustedTokenIssuerConfigurationProperty(
                    idc_trusted_token_issuer_arn="idcTrustedTokenIssuerArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aa8bef9d39508faf93f48a0365a4605be496aa8cf95d29ab54e4ceabbabaef4d)
                check_type(argname="argument idc_trusted_token_issuer_arn", value=idc_trusted_token_issuer_arn, expected_type=type_hints["idc_trusted_token_issuer_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "idc_trusted_token_issuer_arn": idc_trusted_token_issuer_arn,
            }

        @builtins.property
        def idc_trusted_token_issuer_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the IAM Identity Center Trusted Token Issuer that will be used for authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-dataaccessoridctrustedtokenissuerconfiguration.html#cfn-qbusiness-dataaccessor-dataaccessoridctrustedtokenissuerconfiguration-idctrustedtokenissuerarn
            '''
            result = self._values.get("idc_trusted_token_issuer_arn")
            assert result is not None, "Required property 'idc_trusted_token_issuer_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataAccessorIdcTrustedTokenIssuerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataAccessor.DocumentAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class DocumentAttributeProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            value: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataAccessor.DocumentAttributeValueProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A document attribute or metadata field.

            :param name: The identifier for the attribute.
            :param value: The value of the attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-documentattribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                document_attribute_property = qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                    name="name",
                    value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                        date_value="dateValue",
                        long_value=123,
                        string_list_value=["stringListValue"],
                        string_value="stringValue"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fc877a8d06303e2294e4f8e5813534f57082fb9476b669bafe4451af29bb5979)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The identifier for the attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-documentattribute.html#cfn-qbusiness-dataaccessor-documentattribute-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeValueProperty"]:
            '''The value of the attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-documentattribute.html#cfn-qbusiness-dataaccessor-documentattribute-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDataAccessor.DocumentAttributeValueProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataAccessor.DocumentAttributeValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "date_value": "dateValue",
            "long_value": "longValue",
            "string_list_value": "stringListValue",
            "string_value": "stringValue",
        },
    )
    class DocumentAttributeValueProperty:
        def __init__(
            self,
            *,
            date_value: typing.Optional[builtins.str] = None,
            long_value: typing.Optional[jsii.Number] = None,
            string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
            string_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The value of a document attribute.

            You can only provide one value for a document attribute.

            :param date_value: A date expressed as an ISO 8601 string. It's important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.
            :param long_value: A long integer value.
            :param string_list_value: A list of strings.
            :param string_value: A string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-documentattributevalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                document_attribute_value_property = qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                    date_value="dateValue",
                    long_value=123,
                    string_list_value=["stringListValue"],
                    string_value="stringValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__edee8eec89905fde650437fb2fcf2bc7ddeaecc251be16c2ca1d64d79b7eb5a5)
                check_type(argname="argument date_value", value=date_value, expected_type=type_hints["date_value"])
                check_type(argname="argument long_value", value=long_value, expected_type=type_hints["long_value"])
                check_type(argname="argument string_list_value", value=string_list_value, expected_type=type_hints["string_list_value"])
                check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if date_value is not None:
                self._values["date_value"] = date_value
            if long_value is not None:
                self._values["long_value"] = long_value
            if string_list_value is not None:
                self._values["string_list_value"] = string_list_value
            if string_value is not None:
                self._values["string_value"] = string_value

        @builtins.property
        def date_value(self) -> typing.Optional[builtins.str]:
            '''A date expressed as an ISO 8601 string.

            It's important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-documentattributevalue.html#cfn-qbusiness-dataaccessor-documentattributevalue-datevalue
            '''
            result = self._values.get("date_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def long_value(self) -> typing.Optional[jsii.Number]:
            '''A long integer value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-documentattributevalue.html#cfn-qbusiness-dataaccessor-documentattributevalue-longvalue
            '''
            result = self._values.get("long_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def string_list_value(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of strings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-documentattributevalue.html#cfn-qbusiness-dataaccessor-documentattributevalue-stringlistvalue
            '''
            result = self._values.get("string_list_value")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            '''A string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-dataaccessor-documentattributevalue.html#cfn-qbusiness-dataaccessor-documentattributevalue-stringvalue
            '''
            result = self._values.get("string_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentAttributeValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataAccessorProps",
    jsii_struct_bases=[],
    name_mapping={
        "action_configurations": "actionConfigurations",
        "application_id": "applicationId",
        "display_name": "displayName",
        "principal": "principal",
        "authentication_detail": "authenticationDetail",
        "tags": "tags",
    },
)
class CfnDataAccessorProps:
    def __init__(
        self,
        *,
        action_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.ActionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
        application_id: builtins.str,
        display_name: builtins.str,
        principal: builtins.str,
        authentication_detail: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.DataAccessorAuthenticationDetailProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataAccessor``.

        :param action_configurations: A list of action configurations specifying the allowed actions and any associated filters.
        :param application_id: The unique identifier of the Amazon Q Business application.
        :param display_name: The friendly name of the data accessor.
        :param principal: The Amazon Resource Name (ARN) of the IAM role for the ISV associated with this data accessor.
        :param authentication_detail: The authentication configuration details for the data accessor. This specifies how the ISV authenticates when accessing data through this data accessor.
        :param tags: The tags to associate with the data accessor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-dataaccessor.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_qbusiness as qbusiness
            
            # attribute_filter_property_: qbusiness.CfnDataAccessor.AttributeFilterProperty
            
            cfn_data_accessor_props = qbusiness.CfnDataAccessorProps(
                action_configurations=[qbusiness.CfnDataAccessor.ActionConfigurationProperty(
                    action="action",
            
                    # the properties below are optional
                    filter_configuration=qbusiness.CfnDataAccessor.ActionFilterConfigurationProperty(
                        document_attribute_filter=qbusiness.CfnDataAccessor.AttributeFilterProperty(
                            and_all_filters=[attribute_filter_property_],
                            contains_all=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                                name="name",
                                value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                    date_value="dateValue",
                                    long_value=123,
                                    string_list_value=["stringListValue"],
                                    string_value="stringValue"
                                )
                            ),
                            contains_any=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                                name="name",
                                value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                    date_value="dateValue",
                                    long_value=123,
                                    string_list_value=["stringListValue"],
                                    string_value="stringValue"
                                )
                            ),
                            equals_to=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                                name="name",
                                value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                    date_value="dateValue",
                                    long_value=123,
                                    string_list_value=["stringListValue"],
                                    string_value="stringValue"
                                )
                            ),
                            greater_than=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                                name="name",
                                value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                    date_value="dateValue",
                                    long_value=123,
                                    string_list_value=["stringListValue"],
                                    string_value="stringValue"
                                )
                            ),
                            greater_than_or_equals=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                                name="name",
                                value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                    date_value="dateValue",
                                    long_value=123,
                                    string_list_value=["stringListValue"],
                                    string_value="stringValue"
                                )
                            ),
                            less_than=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                                name="name",
                                value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                    date_value="dateValue",
                                    long_value=123,
                                    string_list_value=["stringListValue"],
                                    string_value="stringValue"
                                )
                            ),
                            less_than_or_equals=qbusiness.CfnDataAccessor.DocumentAttributeProperty(
                                name="name",
                                value=qbusiness.CfnDataAccessor.DocumentAttributeValueProperty(
                                    date_value="dateValue",
                                    long_value=123,
                                    string_list_value=["stringListValue"],
                                    string_value="stringValue"
                                )
                            ),
                            not_filter=attribute_filter_property_,
                            or_all_filters=[attribute_filter_property_]
                        )
                    )
                )],
                application_id="applicationId",
                display_name="displayName",
                principal="principal",
            
                # the properties below are optional
                authentication_detail=qbusiness.CfnDataAccessor.DataAccessorAuthenticationDetailProperty(
                    authentication_type="authenticationType",
            
                    # the properties below are optional
                    authentication_configuration=qbusiness.CfnDataAccessor.DataAccessorAuthenticationConfigurationProperty(
                        idc_trusted_token_issuer_configuration=qbusiness.CfnDataAccessor.DataAccessorIdcTrustedTokenIssuerConfigurationProperty(
                            idc_trusted_token_issuer_arn="idcTrustedTokenIssuerArn"
                        )
                    ),
                    external_ids=["externalIds"]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dfde2d4c17793fa3cb9793a9171b9042ac55727b3f0c3a17f1606cab5545458)
            check_type(argname="argument action_configurations", value=action_configurations, expected_type=type_hints["action_configurations"])
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument authentication_detail", value=authentication_detail, expected_type=type_hints["authentication_detail"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_configurations": action_configurations,
            "application_id": application_id,
            "display_name": display_name,
            "principal": principal,
        }
        if authentication_detail is not None:
            self._values["authentication_detail"] = authentication_detail
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def action_configurations(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataAccessor.ActionConfigurationProperty]]]:
        '''A list of action configurations specifying the allowed actions and any associated filters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-dataaccessor.html#cfn-qbusiness-dataaccessor-actionconfigurations
        '''
        result = self._values.get("action_configurations")
        assert result is not None, "Required property 'action_configurations' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataAccessor.ActionConfigurationProperty]]], result)

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier of the Amazon Q Business application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-dataaccessor.html#cfn-qbusiness-dataaccessor-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The friendly name of the data accessor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-dataaccessor.html#cfn-qbusiness-dataaccessor-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role for the ISV associated with this data accessor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-dataaccessor.html#cfn-qbusiness-dataaccessor-principal
        '''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authentication_detail(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataAccessor.DataAccessorAuthenticationDetailProperty]]:
        '''The authentication configuration details for the data accessor.

        This specifies how the ISV authenticates when accessing data through this data accessor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-dataaccessor.html#cfn-qbusiness-dataaccessor-authenticationdetail
        '''
        result = self._values.get("authentication_detail")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataAccessor.DataAccessorAuthenticationDetailProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to associate with the data accessor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-dataaccessor.html#cfn-qbusiness-dataaccessor-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataAccessorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnDataSource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataSource",
):
    '''Creates a data source connector for an Amazon Q Business application.

    ``CreateDataSource`` is a synchronous operation. The operation returns 200 if the data source was successfully created. Otherwise, an exception is raised.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html
    :cloudformationResource: AWS::QBusiness::DataSource
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_qbusiness as qbusiness
        
        # configuration: Any
        
        cfn_data_source = qbusiness.CfnDataSource(self, "MyCfnDataSource",
            application_id="applicationId",
            configuration=configuration,
            display_name="displayName",
            index_id="indexId",
        
            # the properties below are optional
            description="description",
            document_enrichment_configuration=qbusiness.CfnDataSource.DocumentEnrichmentConfigurationProperty(
                inline_configurations=[qbusiness.CfnDataSource.InlineDocumentEnrichmentConfigurationProperty(
                    condition=qbusiness.CfnDataSource.DocumentAttributeConditionProperty(
                        key="key",
                        operator="operator",
        
                        # the properties below are optional
                        value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    ),
                    document_content_operator="documentContentOperator",
                    target=qbusiness.CfnDataSource.DocumentAttributeTargetProperty(
                        key="key",
        
                        # the properties below are optional
                        attribute_value_operator="attributeValueOperator",
                        value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    )
                )],
                post_extraction_hook_configuration=qbusiness.CfnDataSource.HookConfigurationProperty(
                    invocation_condition=qbusiness.CfnDataSource.DocumentAttributeConditionProperty(
                        key="key",
                        operator="operator",
        
                        # the properties below are optional
                        value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    ),
                    lambda_arn="lambdaArn",
                    role_arn="roleArn",
                    s3_bucket_name="s3BucketName"
                ),
                pre_extraction_hook_configuration=qbusiness.CfnDataSource.HookConfigurationProperty(
                    invocation_condition=qbusiness.CfnDataSource.DocumentAttributeConditionProperty(
                        key="key",
                        operator="operator",
        
                        # the properties below are optional
                        value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    ),
                    lambda_arn="lambdaArn",
                    role_arn="roleArn",
                    s3_bucket_name="s3BucketName"
                )
            ),
            media_extraction_configuration=qbusiness.CfnDataSource.MediaExtractionConfigurationProperty(
                audio_extraction_configuration=qbusiness.CfnDataSource.AudioExtractionConfigurationProperty(
                    audio_extraction_status="audioExtractionStatus"
                ),
                image_extraction_configuration=qbusiness.CfnDataSource.ImageExtractionConfigurationProperty(
                    image_extraction_status="imageExtractionStatus"
                ),
                video_extraction_configuration=qbusiness.CfnDataSource.VideoExtractionConfigurationProperty(
                    video_extraction_status="videoExtractionStatus"
                )
            ),
            role_arn="roleArn",
            sync_schedule="syncSchedule",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_configuration=qbusiness.CfnDataSource.DataSourceVpcConfigurationProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        configuration: typing.Any,
        display_name: builtins.str,
        index_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        document_enrichment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.DocumentEnrichmentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        media_extraction_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.MediaExtractionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        sync_schedule: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.DataSourceVpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The identifier of the Amazon Q Business application the data source will be attached to.
        :param configuration: Use this property to specify a JSON or YAML schema with configuration properties specific to your data source connector to connect your data source repository to Amazon Q Business . You must use the JSON or YAML schema provided by Amazon Q . The following links have the configuration properties and schemas for AWS CloudFormation for the following connectors: - `Amazon Simple Storage Service <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-cfn.html>`_ - `Amazon Q Web Crawler <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-crawler-cfn.html>`_ Similarly, you can find configuration templates and properties for your specific data source using the following steps: - Navigate to the `Supported connectors <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connectors-list.html>`_ page in the Amazon Q Business User Guide, and select the data source connector of your choice. - Then, from that specific data source connector's page, choose the topic containing *Using AWS CloudFormation* to find the schemas for your data source connector, including configuration parameter descriptions and examples.
        :param display_name: The name of the Amazon Q Business data source.
        :param index_id: The identifier of the index the data source is attached to.
        :param description: A description for the data source connector.
        :param document_enrichment_configuration: Provides the configuration information for altering document metadata and content during the document ingestion process. For more information, see `Custom document enrichment <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html>`_ .
        :param media_extraction_configuration: The configuration for extracting information from media in documents.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources.
        :param sync_schedule: Sets the frequency for Amazon Q Business to check the documents in your data source repository and update your index. If you don't set a schedule, Amazon Q Business won't periodically update the index. Specify a ``cron-`` format schedule string or an empty string to indicate that the index is updated on demand. You can't specify the ``Schedule`` parameter when the ``Type`` parameter is set to ``CUSTOM`` . If you do, you receive a ``ValidationException`` exception.
        :param tags: A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -
        :param vpc_configuration: Configuration information for an Amazon VPC (Virtual Private Cloud) to connect to your data source. For more information, see `Using Amazon VPC with Amazon Q Business connectors <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connector-vpc.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44090f525589bca757ae88a29adc87bbfc36c3149c7964dfd32c2ce59b69db58)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataSourceProps(
            application_id=application_id,
            configuration=configuration,
            display_name=display_name,
            index_id=index_id,
            description=description,
            document_enrichment_configuration=document_enrichment_configuration,
            media_extraction_configuration=media_extraction_configuration,
            role_arn=role_arn,
            sync_schedule=sync_schedule,
            tags=tags,
            vpc_configuration=vpc_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd73286fa4603be5641a3ab936a93b6e83fc252d5d52182c6f0fe270c5b2a406)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7cb4db65ad9a4064e0bd46d63da12c54d5ac52caacffc9558dcf744690635e34)
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
        '''The Unix timestamp when the Amazon Q Business data source was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDataSourceArn")
    def attr_data_source_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a data source in an Amazon Q Business application.

        :cloudformationAttribute: DataSourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDataSourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDataSourceId")
    def attr_data_source_id(self) -> builtins.str:
        '''The identifier of the Amazon Q Business data source.

        :cloudformationAttribute: DataSourceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDataSourceId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the Amazon Q Business data source.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''The type of the Amazon Q Business data source.

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The Unix timestamp when the Amazon Q Business data source was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The identifier of the Amazon Q Business application the data source will be attached to.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8744e8719ac2ce0a440adec3d28e40857aa43a2f9e7d48ebb99d9244f314b5a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> typing.Any:
        '''Use this property to specify a JSON or YAML schema with configuration properties specific to your data source connector to connect your data source repository to Amazon Q Business .'''
        return typing.cast(typing.Any, jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__033036d2c97cbb0707403571def9bb03fcccaabedc00afaa4905a276eaa169f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''The name of the Amazon Q Business data source.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3480e9c01e998df4f3c9b61416967b6ad224790241607484ad0376c1d24b18c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="indexId")
    def index_id(self) -> builtins.str:
        '''The identifier of the index the data source is attached to.'''
        return typing.cast(builtins.str, jsii.get(self, "indexId"))

    @index_id.setter
    def index_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4ad13a5736b96bc7b5adfb1cf4b9e58f4559cef04a6fb6756627a56e47c0e83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the data source connector.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81151bd66f1686e0470c9ae1dddd9a5cd72c8ceb371d917771c8268073fc8a76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="documentEnrichmentConfiguration")
    def document_enrichment_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DocumentEnrichmentConfigurationProperty"]]:
        '''Provides the configuration information for altering document metadata and content during the document ingestion process.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DocumentEnrichmentConfigurationProperty"]], jsii.get(self, "documentEnrichmentConfiguration"))

    @document_enrichment_configuration.setter
    def document_enrichment_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DocumentEnrichmentConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe2866ff8510082e320bc29f43593004da60817112846504497bbb0dbac73cc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentEnrichmentConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mediaExtractionConfiguration")
    def media_extraction_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.MediaExtractionConfigurationProperty"]]:
        '''The configuration for extracting information from media in documents.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.MediaExtractionConfigurationProperty"]], jsii.get(self, "mediaExtractionConfiguration"))

    @media_extraction_configuration.setter
    def media_extraction_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.MediaExtractionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61d3297e7877958a257749ac6dada8495933c305bc80bd233f5feb0fe4960a81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mediaExtractionConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d17e6c9d50eaaabc9ce2688b35a56e877aaf39df8cd76e73354477d7d5c11a84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="syncSchedule")
    def sync_schedule(self) -> typing.Optional[builtins.str]:
        '''Sets the frequency for Amazon Q Business to check the documents in your data source repository and update your index.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "syncSchedule"))

    @sync_schedule.setter
    def sync_schedule(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d95ad8757220562be3c4a2a414d2a025dbf8de65b35ee49cd77167e02940024b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncSchedule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that identify or categorize the data source connector.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0de23b55ca19c08a4a44c0f9e5ef175e05b82d5a4bdd9d882f044cad9d03ad5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcConfiguration")
    def vpc_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DataSourceVpcConfigurationProperty"]]:
        '''Configuration information for an Amazon VPC (Virtual Private Cloud) to connect to your data source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DataSourceVpcConfigurationProperty"]], jsii.get(self, "vpcConfiguration"))

    @vpc_configuration.setter
    def vpc_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DataSourceVpcConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a2baf273288668ce3827242609bec0e4533974d4ecb7707e426b1a449d645ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfiguration", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataSource.AudioExtractionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"audio_extraction_status": "audioExtractionStatus"},
    )
    class AudioExtractionConfigurationProperty:
        def __init__(self, *, audio_extraction_status: builtins.str) -> None:
            '''Configuration settings for audio content extraction and processing.

            :param audio_extraction_status: The status of audio extraction (ENABLED or DISABLED) for processing audio content from files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-audioextractionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                audio_extraction_configuration_property = qbusiness.CfnDataSource.AudioExtractionConfigurationProperty(
                    audio_extraction_status="audioExtractionStatus"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7aa789e6cda3c90d0db840a9741bbd7eb7b84f0436483843586f56121cdfe2a1)
                check_type(argname="argument audio_extraction_status", value=audio_extraction_status, expected_type=type_hints["audio_extraction_status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "audio_extraction_status": audio_extraction_status,
            }

        @builtins.property
        def audio_extraction_status(self) -> builtins.str:
            '''The status of audio extraction (ENABLED or DISABLED) for processing audio content from files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-audioextractionconfiguration.html#cfn-qbusiness-datasource-audioextractionconfiguration-audioextractionstatus
            '''
            result = self._values.get("audio_extraction_status")
            assert result is not None, "Required property 'audio_extraction_status' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioExtractionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataSource.DataSourceVpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class DataSourceVpcConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_ids: typing.Sequence[builtins.str],
        ) -> None:
            '''Provides configuration information needed to connect to an Amazon VPC (Virtual Private Cloud).

            :param security_group_ids: A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Q Business to connect to the data source.
            :param subnet_ids: A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-datasourcevpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                data_source_vpc_configuration_property = qbusiness.CfnDataSource.DataSourceVpcConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__df3bb5deb9e194276e6702b02f19aa8cb471bee4bf023f5613bcb797abcb6c0f)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnet_ids": subnet_ids,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''A list of identifiers of security groups within your Amazon VPC.

            The security groups should enable Amazon Q Business to connect to the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-datasourcevpcconfiguration.html#cfn-qbusiness-datasource-datasourcevpcconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''A list of identifiers for subnets within your Amazon VPC.

            The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-datasourcevpcconfiguration.html#cfn-qbusiness-datasource-datasourcevpcconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceVpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataSource.DocumentAttributeConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "operator": "operator", "value": "value"},
    )
    class DocumentAttributeConditionProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            operator: builtins.str,
            value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.DocumentAttributeValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The condition used for the target document attribute or metadata field when ingesting documents into Amazon Q Business.

            You use this with ```DocumentAttributeTarget`` <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeTarget.html>`_ to apply the condition.

            For example, you can create the 'Department' target field and have it prefill department names associated with the documents based on information in the 'Source_URI' field. Set the condition that if the 'Source_URI' field contains 'financial' in its URI value, then prefill the target field 'Department' with the target value 'Finance' for the document.

            Amazon Q Business can't create a target field if it has not already been created as an index field. After you create your index field, you can create a document metadata field using ``DocumentAttributeTarget`` . Amazon Q Business then will map your newly created metadata field to your index field.

            :param key: The identifier of the document attribute used for the condition. For example, 'Source_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents. Amazon Q Business currently doesn't support ``_document_body`` as an attribute key used for the condition.
            :param operator: The identifier of the document attribute used for the condition. For example, 'Source_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents. Amazon Q Business currently does not support ``_document_body`` as an attribute key used for the condition.
            :param value: The value of a document attribute. You can only provide one value for a document attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributecondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                document_attribute_condition_property = qbusiness.CfnDataSource.DocumentAttributeConditionProperty(
                    key="key",
                    operator="operator",
                
                    # the properties below are optional
                    value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                        date_value="dateValue",
                        long_value=123,
                        string_list_value=["stringListValue"],
                        string_value="stringValue"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__faa143d45871c83d6e11352afa882fd65640863f02336e1b649bb0c8fa098521)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "operator": operator,
            }
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> builtins.str:
            '''The identifier of the document attribute used for the condition.

            For example, 'Source_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.

            Amazon Q Business currently doesn't support ``_document_body`` as an attribute key used for the condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributecondition.html#cfn-qbusiness-datasource-documentattributecondition-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def operator(self) -> builtins.str:
            '''The identifier of the document attribute used for the condition.

            For example, 'Source_URI' could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.

            Amazon Q Business currently does not support ``_document_body`` as an attribute key used for the condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributecondition.html#cfn-qbusiness-datasource-documentattributecondition-operator
            '''
            result = self._values.get("operator")
            assert result is not None, "Required property 'operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DocumentAttributeValueProperty"]]:
            '''The value of a document attribute.

            You can only provide one value for a document attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributecondition.html#cfn-qbusiness-datasource-documentattributecondition-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DocumentAttributeValueProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentAttributeConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataSource.DocumentAttributeTargetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "key": "key",
            "attribute_value_operator": "attributeValueOperator",
            "value": "value",
        },
    )
    class DocumentAttributeTargetProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            attribute_value_operator: typing.Optional[builtins.str] = None,
            value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.DocumentAttributeValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The target document attribute or metadata field you want to alter when ingesting documents into Amazon Q Business.

            For example, you can delete all customer identification numbers associated with the documents, stored in the document metadata field called 'Customer_ID' by setting the target key as 'Customer_ID' and the deletion flag to ``TRUE`` . This removes all customer ID values in the field 'Customer_ID'. This would scrub personally identifiable information from each document's metadata.

            Amazon Q Business can't create a target field if it has not already been created as an index field. After you create your index field, you can create a document metadata field using ```DocumentAttributeTarget`` <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeTarget.html>`_ . Amazon Q Business will then map your newly created document attribute to your index field.

            You can also use this with ```DocumentAttributeCondition`` <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeCondition.html>`_ .

            :param key: The identifier of the target document attribute or metadata field. For example, 'Department' could be an identifier for the target attribute or metadata field that includes the department names associated with the documents.
            :param attribute_value_operator: ``TRUE`` to delete the existing target value for your specified target attribute key. You cannot create a target value and set this to ``TRUE`` .
            :param value: The value of a document attribute. You can only provide one value for a document attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributetarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                document_attribute_target_property = qbusiness.CfnDataSource.DocumentAttributeTargetProperty(
                    key="key",
                
                    # the properties below are optional
                    attribute_value_operator="attributeValueOperator",
                    value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                        date_value="dateValue",
                        long_value=123,
                        string_list_value=["stringListValue"],
                        string_value="stringValue"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d708153a1aeec62ef33a5e5a47aab28a65d6a8ff6b4222dddee34e2ca80657d1)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument attribute_value_operator", value=attribute_value_operator, expected_type=type_hints["attribute_value_operator"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
            }
            if attribute_value_operator is not None:
                self._values["attribute_value_operator"] = attribute_value_operator
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> builtins.str:
            '''The identifier of the target document attribute or metadata field.

            For example, 'Department' could be an identifier for the target attribute or metadata field that includes the department names associated with the documents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributetarget.html#cfn-qbusiness-datasource-documentattributetarget-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attribute_value_operator(self) -> typing.Optional[builtins.str]:
            '''``TRUE`` to delete the existing target value for your specified target attribute key.

            You cannot create a target value and set this to ``TRUE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributetarget.html#cfn-qbusiness-datasource-documentattributetarget-attributevalueoperator
            '''
            result = self._values.get("attribute_value_operator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DocumentAttributeValueProperty"]]:
            '''The value of a document attribute.

            You can only provide one value for a document attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributetarget.html#cfn-qbusiness-datasource-documentattributetarget-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DocumentAttributeValueProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentAttributeTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataSource.DocumentAttributeValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "date_value": "dateValue",
            "long_value": "longValue",
            "string_list_value": "stringListValue",
            "string_value": "stringValue",
        },
    )
    class DocumentAttributeValueProperty:
        def __init__(
            self,
            *,
            date_value: typing.Optional[builtins.str] = None,
            long_value: typing.Optional[jsii.Number] = None,
            string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
            string_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The value of a document attribute.

            You can only provide one value for a document attribute.

            :param date_value: A date expressed as an ISO 8601 string. It's important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.
            :param long_value: A long integer value.
            :param string_list_value: A list of strings.
            :param string_value: A string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributevalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                document_attribute_value_property = qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                    date_value="dateValue",
                    long_value=123,
                    string_list_value=["stringListValue"],
                    string_value="stringValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__732ff9c08b1e4382c875518343d9cd2daa4054ae31bb370a40d7e1a2f63524ba)
                check_type(argname="argument date_value", value=date_value, expected_type=type_hints["date_value"])
                check_type(argname="argument long_value", value=long_value, expected_type=type_hints["long_value"])
                check_type(argname="argument string_list_value", value=string_list_value, expected_type=type_hints["string_list_value"])
                check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if date_value is not None:
                self._values["date_value"] = date_value
            if long_value is not None:
                self._values["long_value"] = long_value
            if string_list_value is not None:
                self._values["string_list_value"] = string_list_value
            if string_value is not None:
                self._values["string_value"] = string_value

        @builtins.property
        def date_value(self) -> typing.Optional[builtins.str]:
            '''A date expressed as an ISO 8601 string.

            It's important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributevalue.html#cfn-qbusiness-datasource-documentattributevalue-datevalue
            '''
            result = self._values.get("date_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def long_value(self) -> typing.Optional[jsii.Number]:
            '''A long integer value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributevalue.html#cfn-qbusiness-datasource-documentattributevalue-longvalue
            '''
            result = self._values.get("long_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def string_list_value(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of strings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributevalue.html#cfn-qbusiness-datasource-documentattributevalue-stringlistvalue
            '''
            result = self._values.get("string_list_value")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            '''A string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentattributevalue.html#cfn-qbusiness-datasource-documentattributevalue-stringvalue
            '''
            result = self._values.get("string_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentAttributeValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataSource.DocumentEnrichmentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "inline_configurations": "inlineConfigurations",
            "post_extraction_hook_configuration": "postExtractionHookConfiguration",
            "pre_extraction_hook_configuration": "preExtractionHookConfiguration",
        },
    )
    class DocumentEnrichmentConfigurationProperty:
        def __init__(
            self,
            *,
            inline_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.InlineDocumentEnrichmentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            post_extraction_hook_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.HookConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            pre_extraction_hook_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.HookConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides the configuration information for altering document metadata and content during the document ingestion process.

            For more information, see `Custom document enrichment <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html>`_ .

            :param inline_configurations: Configuration information to alter document attributes or metadata fields and content when ingesting documents into Amazon Q Business.
            :param post_extraction_hook_configuration: Configuration information for invoking a Lambda function in AWS Lambda on the structured documents with their metadata and text extracted. You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see `Using Lambda functions <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/cde-lambda-operations.html>`_ .
            :param pre_extraction_hook_configuration: Configuration information for invoking a Lambda function in AWS Lambda on the original or raw documents before extracting their metadata and text. You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see `Using Lambda functions <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/cde-lambda-operations.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentenrichmentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                document_enrichment_configuration_property = qbusiness.CfnDataSource.DocumentEnrichmentConfigurationProperty(
                    inline_configurations=[qbusiness.CfnDataSource.InlineDocumentEnrichmentConfigurationProperty(
                        condition=qbusiness.CfnDataSource.DocumentAttributeConditionProperty(
                            key="key",
                            operator="operator",
                
                            # the properties below are optional
                            value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        document_content_operator="documentContentOperator",
                        target=qbusiness.CfnDataSource.DocumentAttributeTargetProperty(
                            key="key",
                
                            # the properties below are optional
                            attribute_value_operator="attributeValueOperator",
                            value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        )
                    )],
                    post_extraction_hook_configuration=qbusiness.CfnDataSource.HookConfigurationProperty(
                        invocation_condition=qbusiness.CfnDataSource.DocumentAttributeConditionProperty(
                            key="key",
                            operator="operator",
                
                            # the properties below are optional
                            value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        lambda_arn="lambdaArn",
                        role_arn="roleArn",
                        s3_bucket_name="s3BucketName"
                    ),
                    pre_extraction_hook_configuration=qbusiness.CfnDataSource.HookConfigurationProperty(
                        invocation_condition=qbusiness.CfnDataSource.DocumentAttributeConditionProperty(
                            key="key",
                            operator="operator",
                
                            # the properties below are optional
                            value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        lambda_arn="lambdaArn",
                        role_arn="roleArn",
                        s3_bucket_name="s3BucketName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9a842fef6354222b46871e910d15813711d18a6c607448aa28aded9095e40088)
                check_type(argname="argument inline_configurations", value=inline_configurations, expected_type=type_hints["inline_configurations"])
                check_type(argname="argument post_extraction_hook_configuration", value=post_extraction_hook_configuration, expected_type=type_hints["post_extraction_hook_configuration"])
                check_type(argname="argument pre_extraction_hook_configuration", value=pre_extraction_hook_configuration, expected_type=type_hints["pre_extraction_hook_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if inline_configurations is not None:
                self._values["inline_configurations"] = inline_configurations
            if post_extraction_hook_configuration is not None:
                self._values["post_extraction_hook_configuration"] = post_extraction_hook_configuration
            if pre_extraction_hook_configuration is not None:
                self._values["pre_extraction_hook_configuration"] = pre_extraction_hook_configuration

        @builtins.property
        def inline_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.InlineDocumentEnrichmentConfigurationProperty"]]]]:
            '''Configuration information to alter document attributes or metadata fields and content when ingesting documents into Amazon Q Business.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentenrichmentconfiguration.html#cfn-qbusiness-datasource-documentenrichmentconfiguration-inlineconfigurations
            '''
            result = self._values.get("inline_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataSource.InlineDocumentEnrichmentConfigurationProperty"]]]], result)

        @builtins.property
        def post_extraction_hook_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.HookConfigurationProperty"]]:
            '''Configuration information for invoking a Lambda function in AWS Lambda on the structured documents with their metadata and text extracted.

            You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see `Using Lambda functions <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/cde-lambda-operations.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentenrichmentconfiguration.html#cfn-qbusiness-datasource-documentenrichmentconfiguration-postextractionhookconfiguration
            '''
            result = self._values.get("post_extraction_hook_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.HookConfigurationProperty"]], result)

        @builtins.property
        def pre_extraction_hook_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.HookConfigurationProperty"]]:
            '''Configuration information for invoking a Lambda function in AWS Lambda on the original or raw documents before extracting their metadata and text.

            You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see `Using Lambda functions <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/cde-lambda-operations.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-documentenrichmentconfiguration.html#cfn-qbusiness-datasource-documentenrichmentconfiguration-preextractionhookconfiguration
            '''
            result = self._values.get("pre_extraction_hook_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.HookConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentEnrichmentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataSource.HookConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "invocation_condition": "invocationCondition",
            "lambda_arn": "lambdaArn",
            "role_arn": "roleArn",
            "s3_bucket_name": "s3BucketName",
        },
    )
    class HookConfigurationProperty:
        def __init__(
            self,
            *,
            invocation_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.DocumentAttributeConditionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            lambda_arn: typing.Optional[builtins.str] = None,
            role_arn: typing.Optional[builtins.str] = None,
            s3_bucket_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides the configuration information for invoking a Lambda function in AWS Lambda to alter document metadata and content when ingesting documents into Amazon Q Business.

            You can configure your Lambda function using the ``PreExtractionHookConfiguration`` parameter if you want to apply advanced alterations on the original or raw documents.

            If you want to apply advanced alterations on the Amazon Q Business structured documents, you must configure your Lambda function using ``PostExtractionHookConfiguration`` .

            You can only invoke one Lambda function. However, this function can invoke other functions it requires.

            For more information, see `Custom document enrichment <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html>`_ .

            :param invocation_condition: The condition used for when a Lambda function should be invoked. For example, you can specify a condition that if there are empty date-time values, then Amazon Q Business should invoke a function that inserts the current date-time.
            :param lambda_arn: The Amazon Resource Name (ARN) of the Lambda function during ingestion. For more information, see `Using Lambda functions for Amazon Q Business document enrichment <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cde-lambda-operations.html>`_ .
            :param role_arn: The Amazon Resource Name (ARN) of a role with permission to run ``PreExtractionHookConfiguration`` and ``PostExtractionHookConfiguration`` for altering document metadata and content during the document ingestion process.
            :param s3_bucket_name: Stores the original, raw documents or the structured, parsed documents before and after altering them. For more information, see `Data contracts for Lambda functions <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/cde-lambda-operations.html#cde-lambda-operations-data-contracts>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-hookconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                hook_configuration_property = qbusiness.CfnDataSource.HookConfigurationProperty(
                    invocation_condition=qbusiness.CfnDataSource.DocumentAttributeConditionProperty(
                        key="key",
                        operator="operator",
                
                        # the properties below are optional
                        value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    ),
                    lambda_arn="lambdaArn",
                    role_arn="roleArn",
                    s3_bucket_name="s3BucketName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3c33bb8fd2eb803e7000af5893f4f1c6c2062cdbf9cefd30bb8af8419e8f9815)
                check_type(argname="argument invocation_condition", value=invocation_condition, expected_type=type_hints["invocation_condition"])
                check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if invocation_condition is not None:
                self._values["invocation_condition"] = invocation_condition
            if lambda_arn is not None:
                self._values["lambda_arn"] = lambda_arn
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if s3_bucket_name is not None:
                self._values["s3_bucket_name"] = s3_bucket_name

        @builtins.property
        def invocation_condition(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DocumentAttributeConditionProperty"]]:
            '''The condition used for when a Lambda function should be invoked.

            For example, you can specify a condition that if there are empty date-time values, then Amazon Q Business should invoke a function that inserts the current date-time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-hookconfiguration.html#cfn-qbusiness-datasource-hookconfiguration-invocationcondition
            '''
            result = self._values.get("invocation_condition")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DocumentAttributeConditionProperty"]], result)

        @builtins.property
        def lambda_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Lambda function during ingestion.

            For more information, see `Using Lambda functions for Amazon Q Business document enrichment <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cde-lambda-operations.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-hookconfiguration.html#cfn-qbusiness-datasource-hookconfiguration-lambdaarn
            '''
            result = self._values.get("lambda_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of a role with permission to run ``PreExtractionHookConfiguration`` and ``PostExtractionHookConfiguration`` for altering document metadata and content during the document ingestion process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-hookconfiguration.html#cfn-qbusiness-datasource-hookconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_bucket_name(self) -> typing.Optional[builtins.str]:
            '''Stores the original, raw documents or the structured, parsed documents before and after altering them.

            For more information, see `Data contracts for Lambda functions <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/cde-lambda-operations.html#cde-lambda-operations-data-contracts>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-hookconfiguration.html#cfn-qbusiness-datasource-hookconfiguration-s3bucketname
            '''
            result = self._values.get("s3_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HookConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataSource.ImageExtractionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"image_extraction_status": "imageExtractionStatus"},
    )
    class ImageExtractionConfigurationProperty:
        def __init__(self, *, image_extraction_status: builtins.str) -> None:
            '''The configuration for extracting semantic meaning from images in documents.

            For more information, see `Extracting semantic meaning from images and visuals <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/extracting-meaning-from-images.html>`_ .

            :param image_extraction_status: Specify whether to extract semantic meaning from images and visuals from documents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-imageextractionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                image_extraction_configuration_property = qbusiness.CfnDataSource.ImageExtractionConfigurationProperty(
                    image_extraction_status="imageExtractionStatus"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__40e7364b05e4957f04891e99e2b4de3fa819ddcc49a154a8118fdf016503e031)
                check_type(argname="argument image_extraction_status", value=image_extraction_status, expected_type=type_hints["image_extraction_status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "image_extraction_status": image_extraction_status,
            }

        @builtins.property
        def image_extraction_status(self) -> builtins.str:
            '''Specify whether to extract semantic meaning from images and visuals from documents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-imageextractionconfiguration.html#cfn-qbusiness-datasource-imageextractionconfiguration-imageextractionstatus
            '''
            result = self._values.get("image_extraction_status")
            assert result is not None, "Required property 'image_extraction_status' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageExtractionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataSource.InlineDocumentEnrichmentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "condition": "condition",
            "document_content_operator": "documentContentOperator",
            "target": "target",
        },
    )
    class InlineDocumentEnrichmentConfigurationProperty:
        def __init__(
            self,
            *,
            condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.DocumentAttributeConditionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            document_content_operator: typing.Optional[builtins.str] = None,
            target: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.DocumentAttributeTargetProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides the configuration information for applying basic logic to alter document metadata and content when ingesting documents into Amazon Q Business.

            To apply advanced logic, to go beyond what you can do with basic logic, see ```HookConfiguration`` <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_HookConfiguration.html>`_ .

            For more information, see `Custom document enrichment <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html>`_ .

            :param condition: Configuration of the condition used for the target document attribute or metadata field when ingesting documents into Amazon Q Business .
            :param document_content_operator: ``TRUE`` to delete content if the condition used for the target attribute is met.
            :param target: Configuration of the target document attribute or metadata field when ingesting documents into Amazon Q Business . You can also include a value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-inlinedocumentenrichmentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                inline_document_enrichment_configuration_property = qbusiness.CfnDataSource.InlineDocumentEnrichmentConfigurationProperty(
                    condition=qbusiness.CfnDataSource.DocumentAttributeConditionProperty(
                        key="key",
                        operator="operator",
                
                        # the properties below are optional
                        value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    ),
                    document_content_operator="documentContentOperator",
                    target=qbusiness.CfnDataSource.DocumentAttributeTargetProperty(
                        key="key",
                
                        # the properties below are optional
                        attribute_value_operator="attributeValueOperator",
                        value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                            date_value="dateValue",
                            long_value=123,
                            string_list_value=["stringListValue"],
                            string_value="stringValue"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2025544f51e1e49d0d5dbfb988fb4b22f5cc28a154bdb2e2fe6039f0e941da63)
                check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
                check_type(argname="argument document_content_operator", value=document_content_operator, expected_type=type_hints["document_content_operator"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if condition is not None:
                self._values["condition"] = condition
            if document_content_operator is not None:
                self._values["document_content_operator"] = document_content_operator
            if target is not None:
                self._values["target"] = target

        @builtins.property
        def condition(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DocumentAttributeConditionProperty"]]:
            '''Configuration of the condition used for the target document attribute or metadata field when ingesting documents into Amazon Q Business .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-inlinedocumentenrichmentconfiguration.html#cfn-qbusiness-datasource-inlinedocumentenrichmentconfiguration-condition
            '''
            result = self._values.get("condition")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DocumentAttributeConditionProperty"]], result)

        @builtins.property
        def document_content_operator(self) -> typing.Optional[builtins.str]:
            '''``TRUE`` to delete content if the condition used for the target attribute is met.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-inlinedocumentenrichmentconfiguration.html#cfn-qbusiness-datasource-inlinedocumentenrichmentconfiguration-documentcontentoperator
            '''
            result = self._values.get("document_content_operator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DocumentAttributeTargetProperty"]]:
            '''Configuration of the target document attribute or metadata field when ingesting documents into Amazon Q Business .

            You can also include a value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-inlinedocumentenrichmentconfiguration.html#cfn-qbusiness-datasource-inlinedocumentenrichmentconfiguration-target
            '''
            result = self._values.get("target")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.DocumentAttributeTargetProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InlineDocumentEnrichmentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataSource.MediaExtractionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_extraction_configuration": "audioExtractionConfiguration",
            "image_extraction_configuration": "imageExtractionConfiguration",
            "video_extraction_configuration": "videoExtractionConfiguration",
        },
    )
    class MediaExtractionConfigurationProperty:
        def __init__(
            self,
            *,
            audio_extraction_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.AudioExtractionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            image_extraction_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.ImageExtractionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            video_extraction_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataSource.VideoExtractionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration for extracting information from media in documents.

            :param audio_extraction_configuration: Configuration settings for extracting and processing audio content from media files.
            :param image_extraction_configuration: The configuration for extracting semantic meaning from images in documents. For more information, see `Extracting semantic meaning from images and visuals <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/extracting-meaning-from-images.html>`_ .
            :param video_extraction_configuration: Configuration settings for extracting and processing video content from media files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-mediaextractionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                media_extraction_configuration_property = qbusiness.CfnDataSource.MediaExtractionConfigurationProperty(
                    audio_extraction_configuration=qbusiness.CfnDataSource.AudioExtractionConfigurationProperty(
                        audio_extraction_status="audioExtractionStatus"
                    ),
                    image_extraction_configuration=qbusiness.CfnDataSource.ImageExtractionConfigurationProperty(
                        image_extraction_status="imageExtractionStatus"
                    ),
                    video_extraction_configuration=qbusiness.CfnDataSource.VideoExtractionConfigurationProperty(
                        video_extraction_status="videoExtractionStatus"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__45d49817772a3b69716257ee4a29683841b4420b41115ce7a18bc124fe4f9f87)
                check_type(argname="argument audio_extraction_configuration", value=audio_extraction_configuration, expected_type=type_hints["audio_extraction_configuration"])
                check_type(argname="argument image_extraction_configuration", value=image_extraction_configuration, expected_type=type_hints["image_extraction_configuration"])
                check_type(argname="argument video_extraction_configuration", value=video_extraction_configuration, expected_type=type_hints["video_extraction_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if audio_extraction_configuration is not None:
                self._values["audio_extraction_configuration"] = audio_extraction_configuration
            if image_extraction_configuration is not None:
                self._values["image_extraction_configuration"] = image_extraction_configuration
            if video_extraction_configuration is not None:
                self._values["video_extraction_configuration"] = video_extraction_configuration

        @builtins.property
        def audio_extraction_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.AudioExtractionConfigurationProperty"]]:
            '''Configuration settings for extracting and processing audio content from media files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-mediaextractionconfiguration.html#cfn-qbusiness-datasource-mediaextractionconfiguration-audioextractionconfiguration
            '''
            result = self._values.get("audio_extraction_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.AudioExtractionConfigurationProperty"]], result)

        @builtins.property
        def image_extraction_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.ImageExtractionConfigurationProperty"]]:
            '''The configuration for extracting semantic meaning from images in documents.

            For more information, see `Extracting semantic meaning from images and visuals <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/extracting-meaning-from-images.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-mediaextractionconfiguration.html#cfn-qbusiness-datasource-mediaextractionconfiguration-imageextractionconfiguration
            '''
            result = self._values.get("image_extraction_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.ImageExtractionConfigurationProperty"]], result)

        @builtins.property
        def video_extraction_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.VideoExtractionConfigurationProperty"]]:
            '''Configuration settings for extracting and processing video content from media files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-mediaextractionconfiguration.html#cfn-qbusiness-datasource-mediaextractionconfiguration-videoextractionconfiguration
            '''
            result = self._values.get("video_extraction_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataSource.VideoExtractionConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaExtractionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataSource.VideoExtractionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"video_extraction_status": "videoExtractionStatus"},
    )
    class VideoExtractionConfigurationProperty:
        def __init__(self, *, video_extraction_status: builtins.str) -> None:
            '''Configuration settings for video content extraction and processing.

            :param video_extraction_status: The status of video extraction (ENABLED or DISABLED) for processing video content from files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-videoextractionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                video_extraction_configuration_property = qbusiness.CfnDataSource.VideoExtractionConfigurationProperty(
                    video_extraction_status="videoExtractionStatus"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f97caeacd344e3e67dbf0813f2131b0e4d7a3ac8e1f32dcc24431822f666336b)
                check_type(argname="argument video_extraction_status", value=video_extraction_status, expected_type=type_hints["video_extraction_status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "video_extraction_status": video_extraction_status,
            }

        @builtins.property
        def video_extraction_status(self) -> builtins.str:
            '''The status of video extraction (ENABLED or DISABLED) for processing video content from files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-datasource-videoextractionconfiguration.html#cfn-qbusiness-datasource-videoextractionconfiguration-videoextractionstatus
            '''
            result = self._values.get("video_extraction_status")
            assert result is not None, "Required property 'video_extraction_status' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoExtractionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "configuration": "configuration",
        "display_name": "displayName",
        "index_id": "indexId",
        "description": "description",
        "document_enrichment_configuration": "documentEnrichmentConfiguration",
        "media_extraction_configuration": "mediaExtractionConfiguration",
        "role_arn": "roleArn",
        "sync_schedule": "syncSchedule",
        "tags": "tags",
        "vpc_configuration": "vpcConfiguration",
    },
)
class CfnDataSourceProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        configuration: typing.Any,
        display_name: builtins.str,
        index_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        document_enrichment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DocumentEnrichmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        media_extraction_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.MediaExtractionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        sync_schedule: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DataSourceVpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataSource``.

        :param application_id: The identifier of the Amazon Q Business application the data source will be attached to.
        :param configuration: Use this property to specify a JSON or YAML schema with configuration properties specific to your data source connector to connect your data source repository to Amazon Q Business . You must use the JSON or YAML schema provided by Amazon Q . The following links have the configuration properties and schemas for AWS CloudFormation for the following connectors: - `Amazon Simple Storage Service <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-cfn.html>`_ - `Amazon Q Web Crawler <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-crawler-cfn.html>`_ Similarly, you can find configuration templates and properties for your specific data source using the following steps: - Navigate to the `Supported connectors <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connectors-list.html>`_ page in the Amazon Q Business User Guide, and select the data source connector of your choice. - Then, from that specific data source connector's page, choose the topic containing *Using AWS CloudFormation* to find the schemas for your data source connector, including configuration parameter descriptions and examples.
        :param display_name: The name of the Amazon Q Business data source.
        :param index_id: The identifier of the index the data source is attached to.
        :param description: A description for the data source connector.
        :param document_enrichment_configuration: Provides the configuration information for altering document metadata and content during the document ingestion process. For more information, see `Custom document enrichment <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html>`_ .
        :param media_extraction_configuration: The configuration for extracting information from media in documents.
        :param role_arn: The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources.
        :param sync_schedule: Sets the frequency for Amazon Q Business to check the documents in your data source repository and update your index. If you don't set a schedule, Amazon Q Business won't periodically update the index. Specify a ``cron-`` format schedule string or an empty string to indicate that the index is updated on demand. You can't specify the ``Schedule`` parameter when the ``Type`` parameter is set to ``CUSTOM`` . If you do, you receive a ``ValidationException`` exception.
        :param tags: A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -
        :param vpc_configuration: Configuration information for an Amazon VPC (Virtual Private Cloud) to connect to your data source. For more information, see `Using Amazon VPC with Amazon Q Business connectors <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connector-vpc.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_qbusiness as qbusiness
            
            # configuration: Any
            
            cfn_data_source_props = qbusiness.CfnDataSourceProps(
                application_id="applicationId",
                configuration=configuration,
                display_name="displayName",
                index_id="indexId",
            
                # the properties below are optional
                description="description",
                document_enrichment_configuration=qbusiness.CfnDataSource.DocumentEnrichmentConfigurationProperty(
                    inline_configurations=[qbusiness.CfnDataSource.InlineDocumentEnrichmentConfigurationProperty(
                        condition=qbusiness.CfnDataSource.DocumentAttributeConditionProperty(
                            key="key",
                            operator="operator",
            
                            # the properties below are optional
                            value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        document_content_operator="documentContentOperator",
                        target=qbusiness.CfnDataSource.DocumentAttributeTargetProperty(
                            key="key",
            
                            # the properties below are optional
                            attribute_value_operator="attributeValueOperator",
                            value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        )
                    )],
                    post_extraction_hook_configuration=qbusiness.CfnDataSource.HookConfigurationProperty(
                        invocation_condition=qbusiness.CfnDataSource.DocumentAttributeConditionProperty(
                            key="key",
                            operator="operator",
            
                            # the properties below are optional
                            value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        lambda_arn="lambdaArn",
                        role_arn="roleArn",
                        s3_bucket_name="s3BucketName"
                    ),
                    pre_extraction_hook_configuration=qbusiness.CfnDataSource.HookConfigurationProperty(
                        invocation_condition=qbusiness.CfnDataSource.DocumentAttributeConditionProperty(
                            key="key",
                            operator="operator",
            
                            # the properties below are optional
                            value=qbusiness.CfnDataSource.DocumentAttributeValueProperty(
                                date_value="dateValue",
                                long_value=123,
                                string_list_value=["stringListValue"],
                                string_value="stringValue"
                            )
                        ),
                        lambda_arn="lambdaArn",
                        role_arn="roleArn",
                        s3_bucket_name="s3BucketName"
                    )
                ),
                media_extraction_configuration=qbusiness.CfnDataSource.MediaExtractionConfigurationProperty(
                    audio_extraction_configuration=qbusiness.CfnDataSource.AudioExtractionConfigurationProperty(
                        audio_extraction_status="audioExtractionStatus"
                    ),
                    image_extraction_configuration=qbusiness.CfnDataSource.ImageExtractionConfigurationProperty(
                        image_extraction_status="imageExtractionStatus"
                    ),
                    video_extraction_configuration=qbusiness.CfnDataSource.VideoExtractionConfigurationProperty(
                        video_extraction_status="videoExtractionStatus"
                    )
                ),
                role_arn="roleArn",
                sync_schedule="syncSchedule",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_configuration=qbusiness.CfnDataSource.DataSourceVpcConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0cb43c018c99c9e24bb29f0d009e1ded318999b690c706f1e2e099d30a9fe07)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument index_id", value=index_id, expected_type=type_hints["index_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument document_enrichment_configuration", value=document_enrichment_configuration, expected_type=type_hints["document_enrichment_configuration"])
            check_type(argname="argument media_extraction_configuration", value=media_extraction_configuration, expected_type=type_hints["media_extraction_configuration"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument sync_schedule", value=sync_schedule, expected_type=type_hints["sync_schedule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "configuration": configuration,
            "display_name": display_name,
            "index_id": index_id,
        }
        if description is not None:
            self._values["description"] = description
        if document_enrichment_configuration is not None:
            self._values["document_enrichment_configuration"] = document_enrichment_configuration
        if media_extraction_configuration is not None:
            self._values["media_extraction_configuration"] = media_extraction_configuration
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if sync_schedule is not None:
            self._values["sync_schedule"] = sync_schedule
        if tags is not None:
            self._values["tags"] = tags
        if vpc_configuration is not None:
            self._values["vpc_configuration"] = vpc_configuration

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The identifier of the Amazon Q Business application the data source will be attached to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html#cfn-qbusiness-datasource-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(self) -> typing.Any:
        '''Use this property to specify a JSON or YAML schema with configuration properties specific to your data source connector to connect your data source repository to Amazon Q Business .

        You must use the JSON or YAML schema provided by Amazon Q .

        The following links have the configuration properties and schemas for AWS CloudFormation for the following connectors:

        - `Amazon Simple Storage Service <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-cfn.html>`_
        - `Amazon Q Web Crawler <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-crawler-cfn.html>`_

        Similarly, you can find configuration templates and properties for your specific data source using the following steps:

        - Navigate to the `Supported connectors <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connectors-list.html>`_ page in the Amazon Q Business User Guide, and select the data source connector of your choice.
        - Then, from that specific data source connector's page, choose the topic containing *Using AWS CloudFormation* to find the schemas for your data source connector, including configuration parameter descriptions and examples.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html#cfn-qbusiness-datasource-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the Amazon Q Business data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html#cfn-qbusiness-datasource-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_id(self) -> builtins.str:
        '''The identifier of the index the data source is attached to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html#cfn-qbusiness-datasource-indexid
        '''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the data source connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html#cfn-qbusiness-datasource-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_enrichment_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DocumentEnrichmentConfigurationProperty]]:
        '''Provides the configuration information for altering document metadata and content during the document ingestion process.

        For more information, see `Custom document enrichment <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html#cfn-qbusiness-datasource-documentenrichmentconfiguration
        '''
        result = self._values.get("document_enrichment_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DocumentEnrichmentConfigurationProperty]], result)

    @builtins.property
    def media_extraction_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.MediaExtractionConfigurationProperty]]:
        '''The configuration for extracting information from media in documents.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html#cfn-qbusiness-datasource-mediaextractionconfiguration
        '''
        result = self._values.get("media_extraction_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.MediaExtractionConfigurationProperty]], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html#cfn-qbusiness-datasource-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sync_schedule(self) -> typing.Optional[builtins.str]:
        '''Sets the frequency for Amazon Q Business to check the documents in your data source repository and update your index.

        If you don't set a schedule, Amazon Q Business won't periodically update the index.

        Specify a ``cron-`` format schedule string or an empty string to indicate that the index is updated on demand. You can't specify the ``Schedule`` parameter when the ``Type`` parameter is set to ``CUSTOM`` . If you do, you receive a ``ValidationException`` exception.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html#cfn-qbusiness-datasource-syncschedule
        '''
        result = self._values.get("sync_schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that identify or categorize the data source connector.

        You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html#cfn-qbusiness-datasource-tags
        :: .
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DataSourceVpcConfigurationProperty]]:
        '''Configuration information for an Amazon VPC (Virtual Private Cloud) to connect to your data source.

        For more information, see `Using Amazon VPC with Amazon Q Business connectors <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connector-vpc.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-datasource.html#cfn-qbusiness-datasource-vpcconfiguration
        '''
        result = self._values.get("vpc_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DataSourceVpcConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnIndex(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnIndex",
):
    '''Creates an Amazon Q Business index.

    To determine if index creation has completed, check the ``Status`` field returned from a call to ``DescribeIndex`` . The ``Status`` field is set to ``ACTIVE`` when the index is ready to use.

    Once the index is active, you can index your documents using the ```BatchPutDocument`` <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchPutDocument.html>`_ API or the ```CreateDataSource`` <https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html>`_ API.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-index.html
    :cloudformationResource: AWS::QBusiness::Index
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_qbusiness as qbusiness
        
        cfn_index = qbusiness.CfnIndex(self, "MyCfnIndex",
            application_id="applicationId",
            display_name="displayName",
        
            # the properties below are optional
            capacity_configuration=qbusiness.CfnIndex.IndexCapacityConfigurationProperty(
                units=123
            ),
            description="description",
            document_attribute_configurations=[qbusiness.CfnIndex.DocumentAttributeConfigurationProperty(
                name="name",
                search="search",
                type="type"
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            type="type"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        display_name: builtins.str,
        capacity_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIndex.IndexCapacityConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        document_attribute_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIndex.DocumentAttributeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The identifier of the Amazon Q Business application using the index.
        :param display_name: The name of the index.
        :param capacity_configuration: The capacity units you want to provision for your index. You can add and remove capacity to fit your usage needs.
        :param description: A description for the Amazon Q Business index.
        :param document_attribute_configurations: Configuration information for document attributes. Document attributes are metadata or fields associated with your documents. For example, the company department name associated with each document. For more information, see `Understanding document attributes <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/doc-attributes.html>`_ .
        :param tags: A list of key-value pairs that identify or categorize the index. You can also use tags to help control access to the index. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -
        :param type: The index type that's suitable for your needs. For more information on what's included in each type of index, see `Amazon Q Business tiers <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#index-tiers>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c457625f955b1ba56d35bffbcea827abe87347b80fd33090422ef2a8092cd10e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIndexProps(
            application_id=application_id,
            display_name=display_name,
            capacity_configuration=capacity_configuration,
            description=description,
            document_attribute_configurations=document_attribute_configurations,
            tags=tags,
            type=type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc39e6b7456662ae032c4446b1ba1e83f54ae382ca6aabc48cbb69fac624aef4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ccebcb19696a76d2278342081344ed6aff74ba711a12c7cbea56e4141c1e5a8e)
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
        '''The Unix timestamp when the index was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrIndexArn")
    def attr_index_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of an Amazon Q Business index.

        :cloudformationAttribute: IndexArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIndexArn"))

    @builtins.property
    @jsii.member(jsii_name="attrIndexId")
    def attr_index_id(self) -> builtins.str:
        '''The identifier for the index.

        :cloudformationAttribute: IndexId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIndexId"))

    @builtins.property
    @jsii.member(jsii_name="attrIndexStatistics")
    def attr_index_statistics(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: IndexStatistics
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIndexStatistics"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current status of the index.

        When the status is ``ACTIVE`` , the index is ready.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The Unix timestamp when the index was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The identifier of the Amazon Q Business application using the index.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54ff836942c63690dc16a9e4027a9abd09b398c38793f26cca38af64610bbe71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''The name of the index.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4544cd5fba280d2357dbc3ee91f9e13aef38c4a53c6724b7e9e5f519c4e884cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="capacityConfiguration")
    def capacity_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.IndexCapacityConfigurationProperty"]]:
        '''The capacity units you want to provision for your index.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.IndexCapacityConfigurationProperty"]], jsii.get(self, "capacityConfiguration"))

    @capacity_configuration.setter
    def capacity_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.IndexCapacityConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f6c721ddc40768da88ec10387c1ad38a220a25dbc3088182cc077f9e0481f58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the Amazon Q Business index.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b986b341eaa6de5f44cf18bf19e514c21ac9e68197655e6ac87cd46eaa48c11d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="documentAttributeConfigurations")
    def document_attribute_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIndex.DocumentAttributeConfigurationProperty"]]]]:
        '''Configuration information for document attributes.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIndex.DocumentAttributeConfigurationProperty"]]]], jsii.get(self, "documentAttributeConfigurations"))

    @document_attribute_configurations.setter
    def document_attribute_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIndex.DocumentAttributeConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcf5f23ed97cc59f3cf9c24f10906f928933142ac816c6896d51159e901208fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "documentAttributeConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that identify or categorize the index.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2007e1968cafb6cf72816a82731de79853a45701bf488b078fb39be6d392338b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The index type that's suitable for your needs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b9d98917178d25544f20415f3d2719e55f952a06eaafca35fcbf7305cbf2ce2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnIndex.DocumentAttributeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "search": "search", "type": "type"},
    )
    class DocumentAttributeConfigurationProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            search: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration information for document attributes.

            Document attributes are metadata or fields associated with your documents. For example, the company department name associated with each document.

            For more information, see `Understanding document attributes <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/doc-attributes.html>`_ .

            :param name: The name of the document attribute.
            :param search: Information about whether the document attribute can be used by an end user to search for information on their web experience.
            :param type: The type of document attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-index-documentattributeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                document_attribute_configuration_property = qbusiness.CfnIndex.DocumentAttributeConfigurationProperty(
                    name="name",
                    search="search",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2d0cead578e39a3d615afa214bd45404540048cc5c5294a13dc51d68c94cea7c)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument search", value=search, expected_type=type_hints["search"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if search is not None:
                self._values["search"] = search
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the document attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-index-documentattributeconfiguration.html#cfn-qbusiness-index-documentattributeconfiguration-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def search(self) -> typing.Optional[builtins.str]:
            '''Information about whether the document attribute can be used by an end user to search for information on their web experience.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-index-documentattributeconfiguration.html#cfn-qbusiness-index-documentattributeconfiguration-search
            '''
            result = self._values.get("search")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of document attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-index-documentattributeconfiguration.html#cfn-qbusiness-index-documentattributeconfiguration-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentAttributeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnIndex.IndexCapacityConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"units": "units"},
    )
    class IndexCapacityConfigurationProperty:
        def __init__(self, *, units: typing.Optional[jsii.Number] = None) -> None:
            '''Provides information about index capacity configuration.

            :param units: The number of storage units configured for an Amazon Q Business index.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-index-indexcapacityconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                index_capacity_configuration_property = qbusiness.CfnIndex.IndexCapacityConfigurationProperty(
                    units=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e9aec8c22fc6bbbb296721a0ec2a0851e079e8e6bb48cde9ad3338210a91789e)
                check_type(argname="argument units", value=units, expected_type=type_hints["units"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if units is not None:
                self._values["units"] = units

        @builtins.property
        def units(self) -> typing.Optional[jsii.Number]:
            '''The number of storage units configured for an Amazon Q Business index.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-index-indexcapacityconfiguration.html#cfn-qbusiness-index-indexcapacityconfiguration-units
            '''
            result = self._values.get("units")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IndexCapacityConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnIndex.IndexStatisticsProperty",
        jsii_struct_bases=[],
        name_mapping={"text_document_statistics": "textDocumentStatistics"},
    )
    class IndexStatisticsProperty:
        def __init__(
            self,
            *,
            text_document_statistics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIndex.TextDocumentStatisticsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides information about the number of documents in an index.

            :param text_document_statistics: The number of documents indexed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-index-indexstatistics.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                index_statistics_property = qbusiness.CfnIndex.IndexStatisticsProperty(
                    text_document_statistics=qbusiness.CfnIndex.TextDocumentStatisticsProperty(
                        indexed_text_bytes=123,
                        indexed_text_document_count=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2f224eda571af2cef15f793eab49628d157ba54696a8e8bfa469fa8ac5c66802)
                check_type(argname="argument text_document_statistics", value=text_document_statistics, expected_type=type_hints["text_document_statistics"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if text_document_statistics is not None:
                self._values["text_document_statistics"] = text_document_statistics

        @builtins.property
        def text_document_statistics(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.TextDocumentStatisticsProperty"]]:
            '''The number of documents indexed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-index-indexstatistics.html#cfn-qbusiness-index-indexstatistics-textdocumentstatistics
            '''
            result = self._values.get("text_document_statistics")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIndex.TextDocumentStatisticsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IndexStatisticsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnIndex.TextDocumentStatisticsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "indexed_text_bytes": "indexedTextBytes",
            "indexed_text_document_count": "indexedTextDocumentCount",
        },
    )
    class TextDocumentStatisticsProperty:
        def __init__(
            self,
            *,
            indexed_text_bytes: typing.Optional[jsii.Number] = None,
            indexed_text_document_count: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Provides information about text documents in an index.

            :param indexed_text_bytes: The total size, in bytes, of the indexed documents.
            :param indexed_text_document_count: The number of text documents indexed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-index-textdocumentstatistics.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                text_document_statistics_property = qbusiness.CfnIndex.TextDocumentStatisticsProperty(
                    indexed_text_bytes=123,
                    indexed_text_document_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__53655170c0e554a34ac668a43b8c91b79ec330d9f9720473bc0190dd37864bb9)
                check_type(argname="argument indexed_text_bytes", value=indexed_text_bytes, expected_type=type_hints["indexed_text_bytes"])
                check_type(argname="argument indexed_text_document_count", value=indexed_text_document_count, expected_type=type_hints["indexed_text_document_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if indexed_text_bytes is not None:
                self._values["indexed_text_bytes"] = indexed_text_bytes
            if indexed_text_document_count is not None:
                self._values["indexed_text_document_count"] = indexed_text_document_count

        @builtins.property
        def indexed_text_bytes(self) -> typing.Optional[jsii.Number]:
            '''The total size, in bytes, of the indexed documents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-index-textdocumentstatistics.html#cfn-qbusiness-index-textdocumentstatistics-indexedtextbytes
            '''
            result = self._values.get("indexed_text_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def indexed_text_document_count(self) -> typing.Optional[jsii.Number]:
            '''The number of text documents indexed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-index-textdocumentstatistics.html#cfn-qbusiness-index-textdocumentstatistics-indexedtextdocumentcount
            '''
            result = self._values.get("indexed_text_document_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TextDocumentStatisticsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnIndexProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "display_name": "displayName",
        "capacity_configuration": "capacityConfiguration",
        "description": "description",
        "document_attribute_configurations": "documentAttributeConfigurations",
        "tags": "tags",
        "type": "type",
    },
)
class CfnIndexProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        display_name: builtins.str,
        capacity_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.IndexCapacityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        document_attribute_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.DocumentAttributeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnIndex``.

        :param application_id: The identifier of the Amazon Q Business application using the index.
        :param display_name: The name of the index.
        :param capacity_configuration: The capacity units you want to provision for your index. You can add and remove capacity to fit your usage needs.
        :param description: A description for the Amazon Q Business index.
        :param document_attribute_configurations: Configuration information for document attributes. Document attributes are metadata or fields associated with your documents. For example, the company department name associated with each document. For more information, see `Understanding document attributes <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/doc-attributes.html>`_ .
        :param tags: A list of key-value pairs that identify or categorize the index. You can also use tags to help control access to the index. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -
        :param type: The index type that's suitable for your needs. For more information on what's included in each type of index, see `Amazon Q Business tiers <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#index-tiers>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-index.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_qbusiness as qbusiness
            
            cfn_index_props = qbusiness.CfnIndexProps(
                application_id="applicationId",
                display_name="displayName",
            
                # the properties below are optional
                capacity_configuration=qbusiness.CfnIndex.IndexCapacityConfigurationProperty(
                    units=123
                ),
                description="description",
                document_attribute_configurations=[qbusiness.CfnIndex.DocumentAttributeConfigurationProperty(
                    name="name",
                    search="search",
                    type="type"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                type="type"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92562a229c76d1c1bf48f7735d22def1e598923d94ebef2d66b70a174c48887e)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument capacity_configuration", value=capacity_configuration, expected_type=type_hints["capacity_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument document_attribute_configurations", value=document_attribute_configurations, expected_type=type_hints["document_attribute_configurations"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "display_name": display_name,
        }
        if capacity_configuration is not None:
            self._values["capacity_configuration"] = capacity_configuration
        if description is not None:
            self._values["description"] = description
        if document_attribute_configurations is not None:
            self._values["document_attribute_configurations"] = document_attribute_configurations
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The identifier of the Amazon Q Business application using the index.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-index.html#cfn-qbusiness-index-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the index.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-index.html#cfn-qbusiness-index-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIndex.IndexCapacityConfigurationProperty]]:
        '''The capacity units you want to provision for your index.

        You can add and remove capacity to fit your usage needs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-index.html#cfn-qbusiness-index-capacityconfiguration
        '''
        result = self._values.get("capacity_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIndex.IndexCapacityConfigurationProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the Amazon Q Business index.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-index.html#cfn-qbusiness-index-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def document_attribute_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnIndex.DocumentAttributeConfigurationProperty]]]]:
        '''Configuration information for document attributes.

        Document attributes are metadata or fields associated with your documents. For example, the company department name associated with each document.

        For more information, see `Understanding document attributes <https://docs.aws.amazon.com/amazonq/latest/business-use-dg/doc-attributes.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-index.html#cfn-qbusiness-index-documentattributeconfigurations
        '''
        result = self._values.get("document_attribute_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnIndex.DocumentAttributeConfigurationProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that identify or categorize the index.

        You can also use tags to help control access to the index. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-index.html#cfn-qbusiness-index-tags
        :: .
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The index type that's suitable for your needs.

        For more information on what's included in each type of index, see `Amazon Q Business tiers <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#index-tiers>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-index.html#cfn-qbusiness-index-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIndexProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPermission(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnPermission",
):
    '''Adds or updates a permission policy for a Amazon Q Business application, allowing cross-account access for an ISV.

    This operation creates a new policy statement for the specified Amazon Q Business application. The policy statement defines the IAM actions that the ISV is allowed to perform on the Amazon Q Business application's resources.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-permission.html
    :cloudformationResource: AWS::QBusiness::Permission
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_qbusiness as qbusiness
        
        cfn_permission = qbusiness.CfnPermission(self, "MyCfnPermission",
            actions=["actions"],
            application_id="applicationId",
            principal="principal",
            statement_id="statementId",
        
            # the properties below are optional
            conditions=[qbusiness.CfnPermission.ConditionProperty(
                condition_key="conditionKey",
                condition_operator="conditionOperator",
                condition_values=["conditionValues"]
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        actions: typing.Sequence[builtins.str],
        application_id: builtins.str,
        principal: builtins.str,
        statement_id: builtins.str,
        conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPermission.ConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param actions: The list of Amazon Q Business actions that the ISV is allowed to perform.
        :param application_id: The unique identifier of the Amazon Q Business application.
        :param principal: Provides user and group information used for filtering documents to use for generating Amazon Q Business conversation responses.
        :param statement_id: A unique identifier for the policy statement.
        :param conditions: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa8b9992ffebedf4dda280be4bd0aa5dade8d62a6c092d850b1b1bb8df042ee8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPermissionProps(
            actions=actions,
            application_id=application_id,
            principal=principal,
            statement_id=statement_id,
            conditions=conditions,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__486d860cba58c25ad8a704d89ac04d1c97b77e0a8335b95ea6b91e0055822d82)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b04db3dd9150fe212749577b23464a861914114372d66de4e94f86f0c249312)
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
    @jsii.member(jsii_name="actions")
    def actions(self) -> typing.List[builtins.str]:
        '''The list of Amazon Q Business actions that the ISV is allowed to perform.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "actions"))

    @actions.setter
    def actions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39d8a75c9a38f2eedadc1f546593db77ee47e4125872cb57b22cf5548b71f021)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The unique identifier of the Amazon Q Business application.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8fe48822501c0010e5b09bf79b5fbff369d246e10a55c9aa06207fb883b9011)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        '''Provides user and group information used for filtering documents to use for generating Amazon Q Business conversation responses.'''
        return typing.cast(builtins.str, jsii.get(self, "principal"))

    @principal.setter
    def principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0006a2c0010c9479f601e5c854918c05afd29c14583b90821fa3cec8abe28068)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="statementId")
    def statement_id(self) -> builtins.str:
        '''A unique identifier for the policy statement.'''
        return typing.cast(builtins.str, jsii.get(self, "statementId"))

    @statement_id.setter
    def statement_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bf1e79f20a58bfbabb1ce356f12e0ce01131844f0c50f11db4e0f82f47f71e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statementId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="conditions")
    def conditions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPermission.ConditionProperty"]]]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPermission.ConditionProperty"]]]], jsii.get(self, "conditions"))

    @conditions.setter
    def conditions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPermission.ConditionProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df7eedd7834a134466643c8bd40b7906fe6b7fcc7f482e5265aec4bb05607f6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conditions", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnPermission.ConditionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "condition_key": "conditionKey",
            "condition_operator": "conditionOperator",
            "condition_values": "conditionValues",
        },
    )
    class ConditionProperty:
        def __init__(
            self,
            *,
            condition_key: builtins.str,
            condition_operator: builtins.str,
            condition_values: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param condition_key: 
            :param condition_operator: 
            :param condition_values: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-permission-condition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                condition_property = qbusiness.CfnPermission.ConditionProperty(
                    condition_key="conditionKey",
                    condition_operator="conditionOperator",
                    condition_values=["conditionValues"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__39a9bd842be75583d990f7774438e331f4161b57ee4d98a449b293c0e014f90d)
                check_type(argname="argument condition_key", value=condition_key, expected_type=type_hints["condition_key"])
                check_type(argname="argument condition_operator", value=condition_operator, expected_type=type_hints["condition_operator"])
                check_type(argname="argument condition_values", value=condition_values, expected_type=type_hints["condition_values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "condition_key": condition_key,
                "condition_operator": condition_operator,
                "condition_values": condition_values,
            }

        @builtins.property
        def condition_key(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-permission-condition.html#cfn-qbusiness-permission-condition-conditionkey
            '''
            result = self._values.get("condition_key")
            assert result is not None, "Required property 'condition_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def condition_operator(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-permission-condition.html#cfn-qbusiness-permission-condition-conditionoperator
            '''
            result = self._values.get("condition_operator")
            assert result is not None, "Required property 'condition_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def condition_values(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-permission-condition.html#cfn-qbusiness-permission-condition-conditionvalues
            '''
            result = self._values.get("condition_values")
            assert result is not None, "Required property 'condition_values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnPermissionProps",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "application_id": "applicationId",
        "principal": "principal",
        "statement_id": "statementId",
        "conditions": "conditions",
    },
)
class CfnPermissionProps:
    def __init__(
        self,
        *,
        actions: typing.Sequence[builtins.str],
        application_id: builtins.str,
        principal: builtins.str,
        statement_id: builtins.str,
        conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermission.ConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPermission``.

        :param actions: The list of Amazon Q Business actions that the ISV is allowed to perform.
        :param application_id: The unique identifier of the Amazon Q Business application.
        :param principal: Provides user and group information used for filtering documents to use for generating Amazon Q Business conversation responses.
        :param statement_id: A unique identifier for the policy statement.
        :param conditions: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-permission.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_qbusiness as qbusiness
            
            cfn_permission_props = qbusiness.CfnPermissionProps(
                actions=["actions"],
                application_id="applicationId",
                principal="principal",
                statement_id="statementId",
            
                # the properties below are optional
                conditions=[qbusiness.CfnPermission.ConditionProperty(
                    condition_key="conditionKey",
                    condition_operator="conditionOperator",
                    condition_values=["conditionValues"]
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ea87fcda68d4a26468f5e5d1c394a46d117b80b00274f61bbd36b0329a0a8c4)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument statement_id", value=statement_id, expected_type=type_hints["statement_id"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "application_id": application_id,
            "principal": principal,
            "statement_id": statement_id,
        }
        if conditions is not None:
            self._values["conditions"] = conditions

    @builtins.property
    def actions(self) -> typing.List[builtins.str]:
        '''The list of Amazon Q Business actions that the ISV is allowed to perform.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-permission.html#cfn-qbusiness-permission-actions
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The unique identifier of the Amazon Q Business application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-permission.html#cfn-qbusiness-permission-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal(self) -> builtins.str:
        '''Provides user and group information used for filtering documents to use for generating Amazon Q Business conversation responses.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-permission.html#cfn-qbusiness-permission-principal
        '''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statement_id(self) -> builtins.str:
        '''A unique identifier for the policy statement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-permission.html#cfn-qbusiness-permission-statementid
        '''
        result = self._values.get("statement_id")
        assert result is not None, "Required property 'statement_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conditions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPermission.ConditionProperty]]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-permission.html#cfn-qbusiness-permission-conditions
        '''
        result = self._values.get("conditions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPermission.ConditionProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPermissionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnPlugin(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnPlugin",
):
    '''Information about an Amazon Q Business plugin and its configuration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-plugin.html
    :cloudformationResource: AWS::QBusiness::Plugin
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_qbusiness as qbusiness
        
        # no_auth_configuration: Any
        
        cfn_plugin = qbusiness.CfnPlugin(self, "MyCfnPlugin",
            auth_configuration=qbusiness.CfnPlugin.PluginAuthConfigurationProperty(
                basic_auth_configuration=qbusiness.CfnPlugin.BasicAuthConfigurationProperty(
                    role_arn="roleArn",
                    secret_arn="secretArn"
                ),
                no_auth_configuration=no_auth_configuration,
                o_auth2_client_credential_configuration=qbusiness.CfnPlugin.OAuth2ClientCredentialConfigurationProperty(
                    role_arn="roleArn",
                    secret_arn="secretArn",
        
                    # the properties below are optional
                    authorization_url="authorizationUrl",
                    token_url="tokenUrl"
                )
            ),
            display_name="displayName",
            type="type",
        
            # the properties below are optional
            application_id="applicationId",
            custom_plugin_configuration=qbusiness.CfnPlugin.CustomPluginConfigurationProperty(
                api_schema=qbusiness.CfnPlugin.APISchemaProperty(
                    payload="payload",
                    s3=qbusiness.CfnPlugin.S3Property(
                        bucket="bucket",
                        key="key"
                    )
                ),
                api_schema_type="apiSchemaType",
                description="description"
            ),
            server_url="serverUrl",
            state="state",
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
        auth_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlugin.PluginAuthConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        display_name: builtins.str,
        type: builtins.str,
        application_id: typing.Optional[builtins.str] = None,
        custom_plugin_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlugin.CustomPluginConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        server_url: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param auth_configuration: Authentication configuration information for an Amazon Q Business plugin.
        :param display_name: The name of the plugin.
        :param type: The type of the plugin.
        :param application_id: The identifier of the application that will contain the plugin.
        :param custom_plugin_configuration: Configuration information required to create a custom plugin.
        :param server_url: The plugin server URL used for configuration.
        :param state: The current status of the plugin.
        :param tags: A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65b6fb8d65ff428790a22d304932f2713710d70a9f6d789d819489f81a05b6f1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPluginProps(
            auth_configuration=auth_configuration,
            display_name=display_name,
            type=type,
            application_id=application_id,
            custom_plugin_configuration=custom_plugin_configuration,
            server_url=server_url,
            state=state,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fec924728d6923b494037839fb41ee39d956abff0dc273347be667ed27df77ff)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc4e2ac4c2bff624e773994eee3ffed34fc99668cd3dc39ca6b437875ecc9db3)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBuildStatus")
    def attr_build_status(self) -> builtins.str:
        '''The current status of a plugin.

        A plugin is modified asynchronously.

        :cloudformationAttribute: BuildStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBuildStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp for when the plugin was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrPluginArn")
    def attr_plugin_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a plugin.

        :cloudformationAttribute: PluginArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPluginArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPluginId")
    def attr_plugin_id(self) -> builtins.str:
        '''The identifier of the plugin.

        :cloudformationAttribute: PluginId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPluginId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp for when the plugin was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="authConfiguration")
    def auth_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnPlugin.PluginAuthConfigurationProperty"]:
        '''Authentication configuration information for an Amazon Q Business plugin.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPlugin.PluginAuthConfigurationProperty"], jsii.get(self, "authConfiguration"))

    @auth_configuration.setter
    def auth_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnPlugin.PluginAuthConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc09bef25ae0d3b934b9f84632eb962f4421b7e977774cbd9588396218197347)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''The name of the plugin.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3763a7a98296d5eaa6a62be4515663f4255d3a3e157dd717034c5ccf1e2ef323)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the plugin.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fb0c242fab3286e70f3bc5d132c40cefb0d3796d14ea543a14437f3494d980a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the application that will contain the plugin.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b30e993c552d6b7b2897c130ead401b972163585b579b8261fba5f11c45ea7f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="customPluginConfiguration")
    def custom_plugin_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlugin.CustomPluginConfigurationProperty"]]:
        '''Configuration information required to create a custom plugin.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlugin.CustomPluginConfigurationProperty"]], jsii.get(self, "customPluginConfiguration"))

    @custom_plugin_configuration.setter
    def custom_plugin_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlugin.CustomPluginConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca8ebc7a910b53db546c0124994a836ad4abf9624aa8a90b48603c35f2536b6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customPluginConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serverUrl")
    def server_url(self) -> typing.Optional[builtins.str]:
        '''The plugin server URL used for configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverUrl"))

    @server_url.setter
    def server_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc4df0ea830d17e6a6176b82211b1924f080b964b8936cbebb663e6fa55f87b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''The current status of the plugin.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d484260cba976d4aa57562eaeb794488a5d8e68c91f221a7292e9a740fc35a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that identify or categorize the data source connector.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5f493e517da9a6377b62a1cf76303e94908f2643bc058b74f238336623aa73c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnPlugin.APISchemaProperty",
        jsii_struct_bases=[],
        name_mapping={"payload": "payload", "s3": "s3"},
    )
    class APISchemaProperty:
        def __init__(
            self,
            *,
            payload: typing.Optional[builtins.str] = None,
            s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlugin.S3Property", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains details about the OpenAPI schema for a custom plugin.

            For more information, see `custom plugin OpenAPI schemas <https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/custom-plugin.html#plugins-api-schema>`_ . You can either include the schema directly in the payload field or you can upload it to an S3 bucket and specify the S3 bucket location in the ``s3`` field.

            :param payload: The JSON or YAML-formatted payload defining the OpenAPI schema for a custom plugin.
            :param s3: Contains details about the S3 object containing the OpenAPI schema for a custom plugin. The schema could be in either JSON or YAML format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-apischema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                a_pISchema_property = qbusiness.CfnPlugin.APISchemaProperty(
                    payload="payload",
                    s3=qbusiness.CfnPlugin.S3Property(
                        bucket="bucket",
                        key="key"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__000221b1c4915448dbcbd7992684ae4bb62f1df7f27a3a97095792e5b41bede9)
                check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if payload is not None:
                self._values["payload"] = payload
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def payload(self) -> typing.Optional[builtins.str]:
            '''The JSON or YAML-formatted payload defining the OpenAPI schema for a custom plugin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-apischema.html#cfn-qbusiness-plugin-apischema-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlugin.S3Property"]]:
            '''Contains details about the S3 object containing the OpenAPI schema for a custom plugin.

            The schema could be in either JSON or YAML format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-apischema.html#cfn-qbusiness-plugin-apischema-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlugin.S3Property"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "APISchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnPlugin.BasicAuthConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn", "secret_arn": "secretArn"},
    )
    class BasicAuthConfigurationProperty:
        def __init__(self, *, role_arn: builtins.str, secret_arn: builtins.str) -> None:
            '''Information about the basic authentication credentials used to configure a plugin.

            :param role_arn: The ARN of an IAM role used by Amazon Q Business to access the basic authentication credentials stored in a Secrets Manager secret.
            :param secret_arn: The ARN of the Secrets Manager secret that stores the basic authentication credentials used for plugin configuration..

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-basicauthconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                basic_auth_configuration_property = qbusiness.CfnPlugin.BasicAuthConfigurationProperty(
                    role_arn="roleArn",
                    secret_arn="secretArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf3d694e6789020aa132884a8dde4093d7a29a567925c540d842ca3be3c21140)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "secret_arn": secret_arn,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of an IAM role used by Amazon Q Business to access the basic authentication credentials stored in a Secrets Manager secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-basicauthconfiguration.html#cfn-qbusiness-plugin-basicauthconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The ARN of the Secrets Manager secret that stores the basic authentication credentials used for plugin configuration..

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-basicauthconfiguration.html#cfn-qbusiness-plugin-basicauthconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BasicAuthConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnPlugin.CustomPluginConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "api_schema": "apiSchema",
            "api_schema_type": "apiSchemaType",
            "description": "description",
        },
    )
    class CustomPluginConfigurationProperty:
        def __init__(
            self,
            *,
            api_schema: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlugin.APISchemaProperty", typing.Dict[builtins.str, typing.Any]]],
            api_schema_type: builtins.str,
            description: builtins.str,
        ) -> None:
            '''Configuration information required to create a custom plugin.

            :param api_schema: Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema.
            :param api_schema_type: The type of OpenAPI schema to use.
            :param description: A description for your custom plugin configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-custompluginconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                custom_plugin_configuration_property = qbusiness.CfnPlugin.CustomPluginConfigurationProperty(
                    api_schema=qbusiness.CfnPlugin.APISchemaProperty(
                        payload="payload",
                        s3=qbusiness.CfnPlugin.S3Property(
                            bucket="bucket",
                            key="key"
                        )
                    ),
                    api_schema_type="apiSchemaType",
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b0d7174f1197c1724dbfaa655cabb50877063a350e7de7a6595b3362e938610c)
                check_type(argname="argument api_schema", value=api_schema, expected_type=type_hints["api_schema"])
                check_type(argname="argument api_schema_type", value=api_schema_type, expected_type=type_hints["api_schema_type"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "api_schema": api_schema,
                "api_schema_type": api_schema_type,
                "description": description,
            }

        @builtins.property
        def api_schema(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnPlugin.APISchemaProperty"]:
            '''Contains either details about the S3 object containing the OpenAPI schema for the action group or the JSON or YAML-formatted payload defining the schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-custompluginconfiguration.html#cfn-qbusiness-plugin-custompluginconfiguration-apischema
            '''
            result = self._values.get("api_schema")
            assert result is not None, "Required property 'api_schema' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPlugin.APISchemaProperty"], result)

        @builtins.property
        def api_schema_type(self) -> builtins.str:
            '''The type of OpenAPI schema to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-custompluginconfiguration.html#cfn-qbusiness-plugin-custompluginconfiguration-apischematype
            '''
            result = self._values.get("api_schema_type")
            assert result is not None, "Required property 'api_schema_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> builtins.str:
            '''A description for your custom plugin configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-custompluginconfiguration.html#cfn-qbusiness-plugin-custompluginconfiguration-description
            '''
            result = self._values.get("description")
            assert result is not None, "Required property 'description' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomPluginConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnPlugin.OAuth2ClientCredentialConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "secret_arn": "secretArn",
            "authorization_url": "authorizationUrl",
            "token_url": "tokenUrl",
        },
    )
    class OAuth2ClientCredentialConfigurationProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            secret_arn: builtins.str,
            authorization_url: typing.Optional[builtins.str] = None,
            token_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the OAuth 2.0 authentication credential/token used to configure a plugin.

            :param role_arn: The ARN of an IAM role used by Amazon Q Business to access the OAuth 2.0 authentication credentials stored in a Secrets Manager secret.
            :param secret_arn: The ARN of the Secrets Manager secret that stores the OAuth 2.0 credentials/token used for plugin configuration.
            :param authorization_url: The redirect URL required by the OAuth 2.0 protocol for Amazon Q Business to authenticate a plugin user through a third party authentication server.
            :param token_url: The URL required by the OAuth 2.0 protocol to exchange an end user authorization code for an access token.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-oauth2clientcredentialconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                o_auth2_client_credential_configuration_property = qbusiness.CfnPlugin.OAuth2ClientCredentialConfigurationProperty(
                    role_arn="roleArn",
                    secret_arn="secretArn",
                
                    # the properties below are optional
                    authorization_url="authorizationUrl",
                    token_url="tokenUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5bc6d1d65b9c1e5c3607318c662a2a393df7ecf909b2d2ef7437364ade744000)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument authorization_url", value=authorization_url, expected_type=type_hints["authorization_url"])
                check_type(argname="argument token_url", value=token_url, expected_type=type_hints["token_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "secret_arn": secret_arn,
            }
            if authorization_url is not None:
                self._values["authorization_url"] = authorization_url
            if token_url is not None:
                self._values["token_url"] = token_url

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of an IAM role used by Amazon Q Business to access the OAuth 2.0 authentication credentials stored in a Secrets Manager secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-oauth2clientcredentialconfiguration.html#cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The ARN of the Secrets Manager secret that stores the OAuth 2.0 credentials/token used for plugin configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-oauth2clientcredentialconfiguration.html#cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def authorization_url(self) -> typing.Optional[builtins.str]:
            '''The redirect URL required by the OAuth 2.0 protocol for Amazon Q Business to authenticate a plugin user through a third party authentication server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-oauth2clientcredentialconfiguration.html#cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-authorizationurl
            '''
            result = self._values.get("authorization_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def token_url(self) -> typing.Optional[builtins.str]:
            '''The URL required by the OAuth 2.0 protocol to exchange an end user authorization code for an access token.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-oauth2clientcredentialconfiguration.html#cfn-qbusiness-plugin-oauth2clientcredentialconfiguration-tokenurl
            '''
            result = self._values.get("token_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OAuth2ClientCredentialConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnPlugin.PluginAuthConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "basic_auth_configuration": "basicAuthConfiguration",
            "no_auth_configuration": "noAuthConfiguration",
            "o_auth2_client_credential_configuration": "oAuth2ClientCredentialConfiguration",
        },
    )
    class PluginAuthConfigurationProperty:
        def __init__(
            self,
            *,
            basic_auth_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlugin.BasicAuthConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            no_auth_configuration: typing.Any = None,
            o_auth2_client_credential_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlugin.OAuth2ClientCredentialConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Authentication configuration information for an Amazon Q Business plugin.

            :param basic_auth_configuration: Information about the basic authentication credentials used to configure a plugin.
            :param no_auth_configuration: Information about invoking a custom plugin without any authentication.
            :param o_auth2_client_credential_configuration: Information about the OAuth 2.0 authentication credential/token used to configure a plugin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-pluginauthconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                # no_auth_configuration: Any
                
                plugin_auth_configuration_property = qbusiness.CfnPlugin.PluginAuthConfigurationProperty(
                    basic_auth_configuration=qbusiness.CfnPlugin.BasicAuthConfigurationProperty(
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    ),
                    no_auth_configuration=no_auth_configuration,
                    o_auth2_client_credential_configuration=qbusiness.CfnPlugin.OAuth2ClientCredentialConfigurationProperty(
                        role_arn="roleArn",
                        secret_arn="secretArn",
                
                        # the properties below are optional
                        authorization_url="authorizationUrl",
                        token_url="tokenUrl"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__794967140c3985d1690a000f51a65af5981b07a000a2f040ae98c0f6715c5908)
                check_type(argname="argument basic_auth_configuration", value=basic_auth_configuration, expected_type=type_hints["basic_auth_configuration"])
                check_type(argname="argument no_auth_configuration", value=no_auth_configuration, expected_type=type_hints["no_auth_configuration"])
                check_type(argname="argument o_auth2_client_credential_configuration", value=o_auth2_client_credential_configuration, expected_type=type_hints["o_auth2_client_credential_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if basic_auth_configuration is not None:
                self._values["basic_auth_configuration"] = basic_auth_configuration
            if no_auth_configuration is not None:
                self._values["no_auth_configuration"] = no_auth_configuration
            if o_auth2_client_credential_configuration is not None:
                self._values["o_auth2_client_credential_configuration"] = o_auth2_client_credential_configuration

        @builtins.property
        def basic_auth_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlugin.BasicAuthConfigurationProperty"]]:
            '''Information about the basic authentication credentials used to configure a plugin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-pluginauthconfiguration.html#cfn-qbusiness-plugin-pluginauthconfiguration-basicauthconfiguration
            '''
            result = self._values.get("basic_auth_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlugin.BasicAuthConfigurationProperty"]], result)

        @builtins.property
        def no_auth_configuration(self) -> typing.Any:
            '''Information about invoking a custom plugin without any authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-pluginauthconfiguration.html#cfn-qbusiness-plugin-pluginauthconfiguration-noauthconfiguration
            '''
            result = self._values.get("no_auth_configuration")
            return typing.cast(typing.Any, result)

        @builtins.property
        def o_auth2_client_credential_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlugin.OAuth2ClientCredentialConfigurationProperty"]]:
            '''Information about the OAuth 2.0 authentication credential/token used to configure a plugin.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-pluginauthconfiguration.html#cfn-qbusiness-plugin-pluginauthconfiguration-oauth2clientcredentialconfiguration
            '''
            result = self._values.get("o_auth2_client_credential_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlugin.OAuth2ClientCredentialConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PluginAuthConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnPlugin.S3Property",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key"},
    )
    class S3Property:
        def __init__(self, *, bucket: builtins.str, key: builtins.str) -> None:
            '''Information required for Amazon Q Business to find a specific file in an Amazon S3 bucket.

            :param bucket: The name of the S3 bucket that contains the file.
            :param key: The name of the file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-s3.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                s3_property = qbusiness.CfnPlugin.S3Property(
                    bucket="bucket",
                    key="key"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4f7a033a4dede9d0d05480348522d93d5c1d4a0e27d0009e6612ae5c51706450)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
            }

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The name of the S3 bucket that contains the file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-s3.html#cfn-qbusiness-plugin-s3-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The name of the file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-plugin-s3.html#cfn-qbusiness-plugin-s3-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnPluginProps",
    jsii_struct_bases=[],
    name_mapping={
        "auth_configuration": "authConfiguration",
        "display_name": "displayName",
        "type": "type",
        "application_id": "applicationId",
        "custom_plugin_configuration": "customPluginConfiguration",
        "server_url": "serverUrl",
        "state": "state",
        "tags": "tags",
    },
)
class CfnPluginProps:
    def __init__(
        self,
        *,
        auth_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlugin.PluginAuthConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        display_name: builtins.str,
        type: builtins.str,
        application_id: typing.Optional[builtins.str] = None,
        custom_plugin_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlugin.CustomPluginConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        server_url: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPlugin``.

        :param auth_configuration: Authentication configuration information for an Amazon Q Business plugin.
        :param display_name: The name of the plugin.
        :param type: The type of the plugin.
        :param application_id: The identifier of the application that will contain the plugin.
        :param custom_plugin_configuration: Configuration information required to create a custom plugin.
        :param server_url: The plugin server URL used for configuration.
        :param state: The current status of the plugin.
        :param tags: A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-plugin.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_qbusiness as qbusiness
            
            # no_auth_configuration: Any
            
            cfn_plugin_props = qbusiness.CfnPluginProps(
                auth_configuration=qbusiness.CfnPlugin.PluginAuthConfigurationProperty(
                    basic_auth_configuration=qbusiness.CfnPlugin.BasicAuthConfigurationProperty(
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    ),
                    no_auth_configuration=no_auth_configuration,
                    o_auth2_client_credential_configuration=qbusiness.CfnPlugin.OAuth2ClientCredentialConfigurationProperty(
                        role_arn="roleArn",
                        secret_arn="secretArn",
            
                        # the properties below are optional
                        authorization_url="authorizationUrl",
                        token_url="tokenUrl"
                    )
                ),
                display_name="displayName",
                type="type",
            
                # the properties below are optional
                application_id="applicationId",
                custom_plugin_configuration=qbusiness.CfnPlugin.CustomPluginConfigurationProperty(
                    api_schema=qbusiness.CfnPlugin.APISchemaProperty(
                        payload="payload",
                        s3=qbusiness.CfnPlugin.S3Property(
                            bucket="bucket",
                            key="key"
                        )
                    ),
                    api_schema_type="apiSchemaType",
                    description="description"
                ),
                server_url="serverUrl",
                state="state",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84b206da5d8532987dc555e3bb32deb781317bbd9702ad893387d9a51e07b05f)
            check_type(argname="argument auth_configuration", value=auth_configuration, expected_type=type_hints["auth_configuration"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument custom_plugin_configuration", value=custom_plugin_configuration, expected_type=type_hints["custom_plugin_configuration"])
            check_type(argname="argument server_url", value=server_url, expected_type=type_hints["server_url"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auth_configuration": auth_configuration,
            "display_name": display_name,
            "type": type,
        }
        if application_id is not None:
            self._values["application_id"] = application_id
        if custom_plugin_configuration is not None:
            self._values["custom_plugin_configuration"] = custom_plugin_configuration
        if server_url is not None:
            self._values["server_url"] = server_url
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def auth_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnPlugin.PluginAuthConfigurationProperty]:
        '''Authentication configuration information for an Amazon Q Business plugin.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-plugin.html#cfn-qbusiness-plugin-authconfiguration
        '''
        result = self._values.get("auth_configuration")
        assert result is not None, "Required property 'auth_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnPlugin.PluginAuthConfigurationProperty], result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of the plugin.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-plugin.html#cfn-qbusiness-plugin-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the plugin.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-plugin.html#cfn-qbusiness-plugin-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the application that will contain the plugin.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-plugin.html#cfn-qbusiness-plugin-applicationid
        '''
        result = self._values.get("application_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_plugin_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPlugin.CustomPluginConfigurationProperty]]:
        '''Configuration information required to create a custom plugin.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-plugin.html#cfn-qbusiness-plugin-custompluginconfiguration
        '''
        result = self._values.get("custom_plugin_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPlugin.CustomPluginConfigurationProperty]], result)

    @builtins.property
    def server_url(self) -> typing.Optional[builtins.str]:
        '''The plugin server URL used for configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-plugin.html#cfn-qbusiness-plugin-serverurl
        '''
        result = self._values.get("server_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''The current status of the plugin.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-plugin.html#cfn-qbusiness-plugin-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that identify or categorize the data source connector.

        You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-plugin.html#cfn-qbusiness-plugin-tags
        :: .
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPluginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnRetriever(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnRetriever",
):
    '''Adds a retriever to your Amazon Q Business application.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-retriever.html
    :cloudformationResource: AWS::QBusiness::Retriever
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_qbusiness as qbusiness
        
        cfn_retriever = qbusiness.CfnRetriever(self, "MyCfnRetriever",
            application_id="applicationId",
            configuration=qbusiness.CfnRetriever.RetrieverConfigurationProperty(
                kendra_index_configuration=qbusiness.CfnRetriever.KendraIndexConfigurationProperty(
                    index_id="indexId"
                ),
                native_index_configuration=qbusiness.CfnRetriever.NativeIndexConfigurationProperty(
                    index_id="indexId"
                )
            ),
            display_name="displayName",
            type="type",
        
            # the properties below are optional
            role_arn="roleArn",
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
        application_id: builtins.str,
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRetriever.RetrieverConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        display_name: builtins.str,
        type: builtins.str,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The identifier of the Amazon Q Business application using the retriever.
        :param configuration: Provides information on how the retriever used for your Amazon Q Business application is configured.
        :param display_name: The name of your retriever.
        :param type: The type of your retriever.
        :param role_arn: The ARN of an IAM role used by Amazon Q Business to access the basic authentication credentials stored in a Secrets Manager secret.
        :param tags: A list of key-value pairs that identify or categorize the retriever. You can also use tags to help control access to the retriever. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__793749362ec6ccd890aa9273b100a2ba004492449f0dba0ea4eb4909560d6761)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRetrieverProps(
            application_id=application_id,
            configuration=configuration,
            display_name=display_name,
            type=type,
            role_arn=role_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__013b1c812aa4f36fb41a3e6e2da02553a56882a0b9e6a92ca26d883a232dfb06)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d9a004f85d31923ae2ecfb060d2466d212e1a4b3eb2b1d0a85dac42f69eb890d)
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
        '''The Unix timestamp when the retriever was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrRetrieverArn")
    def attr_retriever_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role associated with the retriever.

        :cloudformationAttribute: RetrieverArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRetrieverArn"))

    @builtins.property
    @jsii.member(jsii_name="attrRetrieverId")
    def attr_retriever_id(self) -> builtins.str:
        '''The identifier of the retriever used by your Amazon Q Business application.

        :cloudformationAttribute: RetrieverId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRetrieverId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of your retriever.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The Unix timestamp when the retriever was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The identifier of the Amazon Q Business application using the retriever.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe00bdbe02b12a657cfeff7e2758f761be1b99feb8a57c9d90eefb2a27988ba5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRetriever.RetrieverConfigurationProperty"]:
        '''Provides information on how the retriever used for your Amazon Q Business application is configured.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRetriever.RetrieverConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnRetriever.RetrieverConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__217b852c34b828ca9e117a115c4c1102c46f4c52ed7ae79bf971909a3b377950)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''The name of your retriever.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0210d78e5dd49ca379837adfff5fc5c7423190f4b404ead346c53e8cb560f7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of your retriever.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71e17a562de6a77df0f17f7c55a951b865eb0257648446cd07b68dd023e7f408)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an IAM role used by Amazon Q Business to access the basic authentication credentials stored in a Secrets Manager secret.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02e9bb09b1c416cf967c103b8f223187ac470c6c171ef163f428010c529749e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that identify or categorize the retriever.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e5b60be4a7320479711492eed9182af16eefeea87cf17ce9fbe556d9595c602)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnRetriever.KendraIndexConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"index_id": "indexId"},
    )
    class KendraIndexConfigurationProperty:
        def __init__(self, *, index_id: builtins.str) -> None:
            '''Stores an Amazon Kendra index as a retriever.

            :param index_id: The identifier of the Amazon Kendra index.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-retriever-kendraindexconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                kendra_index_configuration_property = qbusiness.CfnRetriever.KendraIndexConfigurationProperty(
                    index_id="indexId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1d067d57356504f1eb2ff62bfca1f5b675d526d553b4a48e366c1185d56eb861)
                check_type(argname="argument index_id", value=index_id, expected_type=type_hints["index_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "index_id": index_id,
            }

        @builtins.property
        def index_id(self) -> builtins.str:
            '''The identifier of the Amazon Kendra index.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-retriever-kendraindexconfiguration.html#cfn-qbusiness-retriever-kendraindexconfiguration-indexid
            '''
            result = self._values.get("index_id")
            assert result is not None, "Required property 'index_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KendraIndexConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnRetriever.NativeIndexConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"index_id": "indexId"},
    )
    class NativeIndexConfigurationProperty:
        def __init__(self, *, index_id: builtins.str) -> None:
            '''Configuration information for an Amazon Q Business index.

            :param index_id: The identifier for the Amazon Q Business index.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-retriever-nativeindexconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                native_index_configuration_property = qbusiness.CfnRetriever.NativeIndexConfigurationProperty(
                    index_id="indexId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc0a2d6ec7e39104efb95392cc9115abfce755af10ee176a49e2ab8bd89ad1c9)
                check_type(argname="argument index_id", value=index_id, expected_type=type_hints["index_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "index_id": index_id,
            }

        @builtins.property
        def index_id(self) -> builtins.str:
            '''The identifier for the Amazon Q Business index.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-retriever-nativeindexconfiguration.html#cfn-qbusiness-retriever-nativeindexconfiguration-indexid
            '''
            result = self._values.get("index_id")
            assert result is not None, "Required property 'index_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NativeIndexConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnRetriever.RetrieverConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kendra_index_configuration": "kendraIndexConfiguration",
            "native_index_configuration": "nativeIndexConfiguration",
        },
    )
    class RetrieverConfigurationProperty:
        def __init__(
            self,
            *,
            kendra_index_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRetriever.KendraIndexConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            native_index_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRetriever.NativeIndexConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides information on how the retriever used for your Amazon Q Business application is configured.

            :param kendra_index_configuration: Provides information on how the Amazon Kendra index used as a retriever for your Amazon Q Business application is configured.
            :param native_index_configuration: Provides information on how a Amazon Q Business index used as a retriever for your Amazon Q Business application is configured.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-retriever-retrieverconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                retriever_configuration_property = qbusiness.CfnRetriever.RetrieverConfigurationProperty(
                    kendra_index_configuration=qbusiness.CfnRetriever.KendraIndexConfigurationProperty(
                        index_id="indexId"
                    ),
                    native_index_configuration=qbusiness.CfnRetriever.NativeIndexConfigurationProperty(
                        index_id="indexId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9a87eb68b4d13ad399e3831bda05bdee7126f9c5a1a3f94de678194cb12a2855)
                check_type(argname="argument kendra_index_configuration", value=kendra_index_configuration, expected_type=type_hints["kendra_index_configuration"])
                check_type(argname="argument native_index_configuration", value=native_index_configuration, expected_type=type_hints["native_index_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kendra_index_configuration is not None:
                self._values["kendra_index_configuration"] = kendra_index_configuration
            if native_index_configuration is not None:
                self._values["native_index_configuration"] = native_index_configuration

        @builtins.property
        def kendra_index_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRetriever.KendraIndexConfigurationProperty"]]:
            '''Provides information on how the Amazon Kendra index used as a retriever for your Amazon Q Business application is configured.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-retriever-retrieverconfiguration.html#cfn-qbusiness-retriever-retrieverconfiguration-kendraindexconfiguration
            '''
            result = self._values.get("kendra_index_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRetriever.KendraIndexConfigurationProperty"]], result)

        @builtins.property
        def native_index_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRetriever.NativeIndexConfigurationProperty"]]:
            '''Provides information on how a Amazon Q Business index used as a retriever for your Amazon Q Business application is configured.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-retriever-retrieverconfiguration.html#cfn-qbusiness-retriever-retrieverconfiguration-nativeindexconfiguration
            '''
            result = self._values.get("native_index_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRetriever.NativeIndexConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetrieverConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnRetrieverProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "configuration": "configuration",
        "display_name": "displayName",
        "type": "type",
        "role_arn": "roleArn",
        "tags": "tags",
    },
)
class CfnRetrieverProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRetriever.RetrieverConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        display_name: builtins.str,
        type: builtins.str,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRetriever``.

        :param application_id: The identifier of the Amazon Q Business application using the retriever.
        :param configuration: Provides information on how the retriever used for your Amazon Q Business application is configured.
        :param display_name: The name of your retriever.
        :param type: The type of your retriever.
        :param role_arn: The ARN of an IAM role used by Amazon Q Business to access the basic authentication credentials stored in a Secrets Manager secret.
        :param tags: A list of key-value pairs that identify or categorize the retriever. You can also use tags to help control access to the retriever. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-retriever.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_qbusiness as qbusiness
            
            cfn_retriever_props = qbusiness.CfnRetrieverProps(
                application_id="applicationId",
                configuration=qbusiness.CfnRetriever.RetrieverConfigurationProperty(
                    kendra_index_configuration=qbusiness.CfnRetriever.KendraIndexConfigurationProperty(
                        index_id="indexId"
                    ),
                    native_index_configuration=qbusiness.CfnRetriever.NativeIndexConfigurationProperty(
                        index_id="indexId"
                    )
                ),
                display_name="displayName",
                type="type",
            
                # the properties below are optional
                role_arn="roleArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d26f55565cdfd207bc3128a08abf6cd7e371950c5a332ccf3973859a33980b6)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "configuration": configuration,
            "display_name": display_name,
            "type": type,
        }
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The identifier of the Amazon Q Business application using the retriever.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-retriever.html#cfn-qbusiness-retriever-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnRetriever.RetrieverConfigurationProperty]:
        '''Provides information on how the retriever used for your Amazon Q Business application is configured.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-retriever.html#cfn-qbusiness-retriever-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnRetriever.RetrieverConfigurationProperty], result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''The name of your retriever.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-retriever.html#cfn-qbusiness-retriever-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of your retriever.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-retriever.html#cfn-qbusiness-retriever-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of an IAM role used by Amazon Q Business to access the basic authentication credentials stored in a Secrets Manager secret.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-retriever.html#cfn-qbusiness-retriever-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that identify or categorize the retriever.

        You can also use tags to help control access to the retriever. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-retriever.html#cfn-qbusiness-retriever-tags
        :: .
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRetrieverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnWebExperience(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnWebExperience",
):
    '''Creates an Amazon Q Business web experience.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-webexperience.html
    :cloudformationResource: AWS::QBusiness::WebExperience
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_qbusiness as qbusiness
        
        cfn_web_experience = qbusiness.CfnWebExperience(self, "MyCfnWebExperience",
            application_id="applicationId",
        
            # the properties below are optional
            browser_extension_configuration=qbusiness.CfnWebExperience.BrowserExtensionConfigurationProperty(
                enabled_browser_extensions=["enabledBrowserExtensions"]
            ),
            customization_configuration=qbusiness.CfnWebExperience.CustomizationConfigurationProperty(
                custom_css_url="customCssUrl",
                favicon_url="faviconUrl",
                font_url="fontUrl",
                logo_url="logoUrl"
            ),
            identity_provider_configuration=qbusiness.CfnWebExperience.IdentityProviderConfigurationProperty(
                open_id_connect_configuration=qbusiness.CfnWebExperience.OpenIDConnectProviderConfigurationProperty(
                    secrets_arn="secretsArn",
                    secrets_role="secretsRole"
                ),
                saml_configuration=qbusiness.CfnWebExperience.SamlProviderConfigurationProperty(
                    authentication_url="authenticationUrl"
                )
            ),
            origins=["origins"],
            role_arn="roleArn",
            sample_prompts_control_mode="samplePromptsControlMode",
            subtitle="subtitle",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            title="title",
            welcome_message="welcomeMessage"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        browser_extension_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWebExperience.BrowserExtensionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        customization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWebExperience.CustomizationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        identity_provider_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWebExperience.IdentityProviderConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        sample_prompts_control_mode: typing.Optional[builtins.str] = None,
        subtitle: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        title: typing.Optional[builtins.str] = None,
        welcome_message: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_id: The identifier of the Amazon Q Business web experience.
        :param browser_extension_configuration: The container for browser extension configuration for an Amazon Q Business web experience.
        :param customization_configuration: Contains the configuration information to customize the logo, font, and color of an Amazon Q Business web experience with individual files for each property or a CSS file for them all.
        :param identity_provider_configuration: Provides information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
        :param origins: Sets the website domain origins that are allowed to embed the Amazon Q Business web experience. The *domain origin* refers to the base URL for accessing a website including the protocol ( ``http/https`` ), the domain name, and the port number (if specified). .. epigraph:: You must only submit a *base URL* and not a full path. For example, ``https://docs.aws.amazon.com`` .
        :param role_arn: The Amazon Resource Name (ARN) of the service role attached to your web experience. .. epigraph:: The ``roleArn`` parameter is required when your Amazon Q Business application is created with IAM Identity Center. It is not required for SAML-based applications.
        :param sample_prompts_control_mode: Determines whether sample prompts are enabled in the web experience for an end user.
        :param subtitle: A subtitle to personalize your Amazon Q Business web experience.
        :param tags: A list of key-value pairs that identify or categorize your Amazon Q Business web experience. You can also use tags to help control access to the web experience. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -
        :param title: The title for your Amazon Q Business web experience.
        :param welcome_message: A message in an Amazon Q Business web experience.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__357871375e43a0ed6fbb398668ece13df26dff3afca5c98268a56fffdb09ec8d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWebExperienceProps(
            application_id=application_id,
            browser_extension_configuration=browser_extension_configuration,
            customization_configuration=customization_configuration,
            identity_provider_configuration=identity_provider_configuration,
            origins=origins,
            role_arn=role_arn,
            sample_prompts_control_mode=sample_prompts_control_mode,
            subtitle=subtitle,
            tags=tags,
            title=title,
            welcome_message=welcome_message,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18f54626970b688afafe657434af722476d6086ca982ba2b3c0785ca472ce28e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__84d2429ec4e0f829c4548e994cc7bffc96574be7e836657297f4565bd58c2bf3)
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
        '''The Unix timestamp when the Amazon Q Business application was last updated.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDefaultEndpoint")
    def attr_default_endpoint(self) -> builtins.str:
        '''The endpoint URLs for your Amazon Q Business web experience.

        The URLs are unique and fully hosted by AWS .

        :cloudformationAttribute: DefaultEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDefaultEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of your Amazon Q Business web experience.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The Unix timestamp when your Amazon Q Business web experience was updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrWebExperienceArn")
    def attr_web_experience_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of an Amazon Q Business web experience.

        :cloudformationAttribute: WebExperienceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWebExperienceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrWebExperienceId")
    def attr_web_experience_id(self) -> builtins.str:
        '''The identifier of your Amazon Q Business web experience.

        :cloudformationAttribute: WebExperienceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWebExperienceId"))

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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''The identifier of the Amazon Q Business web experience.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__994b24302ed92226579fa1ecdeef04d0cb66956019e467efcd9374ab264f8f90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="browserExtensionConfiguration")
    def browser_extension_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWebExperience.BrowserExtensionConfigurationProperty"]]:
        '''The container for browser extension configuration for an Amazon Q Business web experience.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWebExperience.BrowserExtensionConfigurationProperty"]], jsii.get(self, "browserExtensionConfiguration"))

    @browser_extension_configuration.setter
    def browser_extension_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWebExperience.BrowserExtensionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a0cdf2a88c334b7d14f1ec069e84cd3cde5e237c3b2738cec3187653fcd4075)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "browserExtensionConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="customizationConfiguration")
    def customization_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWebExperience.CustomizationConfigurationProperty"]]:
        '''Contains the configuration information to customize the logo, font, and color of an Amazon Q Business web experience with individual files for each property or a CSS file for them all.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWebExperience.CustomizationConfigurationProperty"]], jsii.get(self, "customizationConfiguration"))

    @customization_configuration.setter
    def customization_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWebExperience.CustomizationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf72d65c47bcc616319908521026308ce2d7a5972c8d440077fbbf82ebb97663)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customizationConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="identityProviderConfiguration")
    def identity_provider_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWebExperience.IdentityProviderConfigurationProperty"]]:
        '''Provides information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWebExperience.IdentityProviderConfigurationProperty"]], jsii.get(self, "identityProviderConfiguration"))

    @identity_provider_configuration.setter
    def identity_provider_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWebExperience.IdentityProviderConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__037151dbe9f2f36da364495e39b2467a261694df042a6b81d84e5c2c34771ac4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="origins")
    def origins(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Sets the website domain origins that are allowed to embed the Amazon Q Business web experience.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "origins"))

    @origins.setter
    def origins(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efefc83f84ced0d16f9a7d4536640a373b6576081faef2262e41578447add1df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "origins", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the service role attached to your web experience.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e93af1c8c50a8fbbba5f2f4c0d1013951bd550b401230f1ec2637c4955cea1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="samplePromptsControlMode")
    def sample_prompts_control_mode(self) -> typing.Optional[builtins.str]:
        '''Determines whether sample prompts are enabled in the web experience for an end user.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "samplePromptsControlMode"))

    @sample_prompts_control_mode.setter
    def sample_prompts_control_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bc39c1915319ccfd9bde90f397adff04c0e3cf7775254eb327fb93987a541f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samplePromptsControlMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subtitle")
    def subtitle(self) -> typing.Optional[builtins.str]:
        '''A subtitle to personalize your Amazon Q Business web experience.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subtitle"))

    @subtitle.setter
    def subtitle(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4a35577085528c30fbee7242c0023bcd3ff26b129706d1aaca7044143958243)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subtitle", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that identify or categorize your Amazon Q Business web experience.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28dfc304b43632af9e6915e06d6d8106a7a8e887153b3c37db8331f47b275d30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> typing.Optional[builtins.str]:
        '''The title for your Amazon Q Business web experience.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "title"))

    @title.setter
    def title(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b6d52e113fec7d083295c445d34ded7755cb3f797753c6ea3a174a05082795b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="welcomeMessage")
    def welcome_message(self) -> typing.Optional[builtins.str]:
        '''A message in an Amazon Q Business web experience.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "welcomeMessage"))

    @welcome_message.setter
    def welcome_message(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dc11f2c0364936c993f550de31ea07513a76ae6f389384341e03770b293ecaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "welcomeMessage", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnWebExperience.BrowserExtensionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled_browser_extensions": "enabledBrowserExtensions"},
    )
    class BrowserExtensionConfigurationProperty:
        def __init__(
            self,
            *,
            enabled_browser_extensions: typing.Sequence[builtins.str],
        ) -> None:
            '''The container for browser extension configuration for an Amazon Q Business web experience.

            :param enabled_browser_extensions: Specify the browser extensions allowed for your Amazon Q web experience. - ``CHROME`` — Enables the extension for Chromium-based browsers (Google Chrome, Microsoft Edge, Opera, etc.). - ``FIREFOX`` — Enables the extension for Mozilla Firefox. - ``CHROME`` and ``FIREFOX`` — Enable the extension for Chromium-based browsers and Mozilla Firefox.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-browserextensionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                browser_extension_configuration_property = qbusiness.CfnWebExperience.BrowserExtensionConfigurationProperty(
                    enabled_browser_extensions=["enabledBrowserExtensions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f63b3566e87de98155904278bf52684ee22c6e0894e4de3e473b4a1ff103b900)
                check_type(argname="argument enabled_browser_extensions", value=enabled_browser_extensions, expected_type=type_hints["enabled_browser_extensions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled_browser_extensions": enabled_browser_extensions,
            }

        @builtins.property
        def enabled_browser_extensions(self) -> typing.List[builtins.str]:
            '''Specify the browser extensions allowed for your Amazon Q web experience.

            - ``CHROME`` — Enables the extension for Chromium-based browsers (Google Chrome, Microsoft Edge, Opera, etc.).
            - ``FIREFOX`` — Enables the extension for Mozilla Firefox.
            - ``CHROME`` and ``FIREFOX`` — Enable the extension for Chromium-based browsers and Mozilla Firefox.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-browserextensionconfiguration.html#cfn-qbusiness-webexperience-browserextensionconfiguration-enabledbrowserextensions
            '''
            result = self._values.get("enabled_browser_extensions")
            assert result is not None, "Required property 'enabled_browser_extensions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BrowserExtensionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnWebExperience.CustomizationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_css_url": "customCssUrl",
            "favicon_url": "faviconUrl",
            "font_url": "fontUrl",
            "logo_url": "logoUrl",
        },
    )
    class CustomizationConfigurationProperty:
        def __init__(
            self,
            *,
            custom_css_url: typing.Optional[builtins.str] = None,
            favicon_url: typing.Optional[builtins.str] = None,
            font_url: typing.Optional[builtins.str] = None,
            logo_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains the configuration information to customize the logo, font, and color of an Amazon Q Business web experience with individual files for each property or a CSS file for them all.

            :param custom_css_url: Provides the URL where the custom CSS file is hosted for an Amazon Q web experience.
            :param favicon_url: Provides the URL where the custom favicon file is hosted for an Amazon Q web experience.
            :param font_url: Provides the URL where the custom font file is hosted for an Amazon Q web experience.
            :param logo_url: Provides the URL where the custom logo file is hosted for an Amazon Q web experience.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-customizationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                customization_configuration_property = qbusiness.CfnWebExperience.CustomizationConfigurationProperty(
                    custom_css_url="customCssUrl",
                    favicon_url="faviconUrl",
                    font_url="fontUrl",
                    logo_url="logoUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a0715100f79db57a5a95a4fef0f7ea187376551e20bd796d1d430e1fd8d50a4d)
                check_type(argname="argument custom_css_url", value=custom_css_url, expected_type=type_hints["custom_css_url"])
                check_type(argname="argument favicon_url", value=favicon_url, expected_type=type_hints["favicon_url"])
                check_type(argname="argument font_url", value=font_url, expected_type=type_hints["font_url"])
                check_type(argname="argument logo_url", value=logo_url, expected_type=type_hints["logo_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_css_url is not None:
                self._values["custom_css_url"] = custom_css_url
            if favicon_url is not None:
                self._values["favicon_url"] = favicon_url
            if font_url is not None:
                self._values["font_url"] = font_url
            if logo_url is not None:
                self._values["logo_url"] = logo_url

        @builtins.property
        def custom_css_url(self) -> typing.Optional[builtins.str]:
            '''Provides the URL where the custom CSS file is hosted for an Amazon Q web experience.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-customizationconfiguration.html#cfn-qbusiness-webexperience-customizationconfiguration-customcssurl
            '''
            result = self._values.get("custom_css_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def favicon_url(self) -> typing.Optional[builtins.str]:
            '''Provides the URL where the custom favicon file is hosted for an Amazon Q web experience.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-customizationconfiguration.html#cfn-qbusiness-webexperience-customizationconfiguration-faviconurl
            '''
            result = self._values.get("favicon_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def font_url(self) -> typing.Optional[builtins.str]:
            '''Provides the URL where the custom font file is hosted for an Amazon Q web experience.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-customizationconfiguration.html#cfn-qbusiness-webexperience-customizationconfiguration-fonturl
            '''
            result = self._values.get("font_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def logo_url(self) -> typing.Optional[builtins.str]:
            '''Provides the URL where the custom logo file is hosted for an Amazon Q web experience.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-customizationconfiguration.html#cfn-qbusiness-webexperience-customizationconfiguration-logourl
            '''
            result = self._values.get("logo_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomizationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnWebExperience.IdentityProviderConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "open_id_connect_configuration": "openIdConnectConfiguration",
            "saml_configuration": "samlConfiguration",
        },
    )
    class IdentityProviderConfigurationProperty:
        def __init__(
            self,
            *,
            open_id_connect_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWebExperience.OpenIDConnectProviderConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            saml_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWebExperience.SamlProviderConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.

            :param open_id_connect_configuration: The OIDC-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
            :param saml_configuration: The SAML 2.0-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-identityproviderconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                identity_provider_configuration_property = qbusiness.CfnWebExperience.IdentityProviderConfigurationProperty(
                    open_id_connect_configuration=qbusiness.CfnWebExperience.OpenIDConnectProviderConfigurationProperty(
                        secrets_arn="secretsArn",
                        secrets_role="secretsRole"
                    ),
                    saml_configuration=qbusiness.CfnWebExperience.SamlProviderConfigurationProperty(
                        authentication_url="authenticationUrl"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f792f47d6a0722e8b808ad22d67aec07629a1e7351865cae0ee890cff9ba5c1a)
                check_type(argname="argument open_id_connect_configuration", value=open_id_connect_configuration, expected_type=type_hints["open_id_connect_configuration"])
                check_type(argname="argument saml_configuration", value=saml_configuration, expected_type=type_hints["saml_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if open_id_connect_configuration is not None:
                self._values["open_id_connect_configuration"] = open_id_connect_configuration
            if saml_configuration is not None:
                self._values["saml_configuration"] = saml_configuration

        @builtins.property
        def open_id_connect_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWebExperience.OpenIDConnectProviderConfigurationProperty"]]:
            '''The OIDC-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-identityproviderconfiguration.html#cfn-qbusiness-webexperience-identityproviderconfiguration-openidconnectconfiguration
            '''
            result = self._values.get("open_id_connect_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWebExperience.OpenIDConnectProviderConfigurationProperty"]], result)

        @builtins.property
        def saml_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWebExperience.SamlProviderConfigurationProperty"]]:
            '''The SAML 2.0-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-identityproviderconfiguration.html#cfn-qbusiness-webexperience-identityproviderconfiguration-samlconfiguration
            '''
            result = self._values.get("saml_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWebExperience.SamlProviderConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentityProviderConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnWebExperience.OpenIDConnectProviderConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"secrets_arn": "secretsArn", "secrets_role": "secretsRole"},
    )
    class OpenIDConnectProviderConfigurationProperty:
        def __init__(
            self,
            *,
            secrets_arn: builtins.str,
            secrets_role: builtins.str,
        ) -> None:
            '''Information about the OIDC-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.

            :param secrets_arn: The Amazon Resource Name (ARN) of a Secrets Manager secret containing the OIDC client secret.
            :param secrets_role: An IAM role with permissions to access AWS KMS to decrypt the Secrets Manager secret containing your OIDC client secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-openidconnectproviderconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                open_iDConnect_provider_configuration_property = qbusiness.CfnWebExperience.OpenIDConnectProviderConfigurationProperty(
                    secrets_arn="secretsArn",
                    secrets_role="secretsRole"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__83ea977b859d6c4c1e46fa972ce0e7d691c60d57b7c59adbe13d851526eb765e)
                check_type(argname="argument secrets_arn", value=secrets_arn, expected_type=type_hints["secrets_arn"])
                check_type(argname="argument secrets_role", value=secrets_role, expected_type=type_hints["secrets_role"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "secrets_arn": secrets_arn,
                "secrets_role": secrets_role,
            }

        @builtins.property
        def secrets_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of a Secrets Manager secret containing the OIDC client secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-openidconnectproviderconfiguration.html#cfn-qbusiness-webexperience-openidconnectproviderconfiguration-secretsarn
            '''
            result = self._values.get("secrets_arn")
            assert result is not None, "Required property 'secrets_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secrets_role(self) -> builtins.str:
            '''An IAM role with permissions to access AWS KMS to decrypt the Secrets Manager secret containing your OIDC client secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-openidconnectproviderconfiguration.html#cfn-qbusiness-webexperience-openidconnectproviderconfiguration-secretsrole
            '''
            result = self._values.get("secrets_role")
            assert result is not None, "Required property 'secrets_role' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenIDConnectProviderConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_qbusiness.CfnWebExperience.SamlProviderConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"authentication_url": "authenticationUrl"},
    )
    class SamlProviderConfigurationProperty:
        def __init__(self, *, authentication_url: builtins.str) -> None:
            '''Information about the SAML 2.0-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.

            :param authentication_url: The URL where Amazon Q Business end users will be redirected for authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-samlproviderconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_qbusiness as qbusiness
                
                saml_provider_configuration_property = qbusiness.CfnWebExperience.SamlProviderConfigurationProperty(
                    authentication_url="authenticationUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7f19a9da1f3a1cf2eefff3580476a949609debe65a8fc477af11c893d5b4453b)
                check_type(argname="argument authentication_url", value=authentication_url, expected_type=type_hints["authentication_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authentication_url": authentication_url,
            }

        @builtins.property
        def authentication_url(self) -> builtins.str:
            '''The URL where Amazon Q Business end users will be redirected for authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qbusiness-webexperience-samlproviderconfiguration.html#cfn-qbusiness-webexperience-samlproviderconfiguration-authenticationurl
            '''
            result = self._values.get("authentication_url")
            assert result is not None, "Required property 'authentication_url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SamlProviderConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_qbusiness.CfnWebExperienceProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "browser_extension_configuration": "browserExtensionConfiguration",
        "customization_configuration": "customizationConfiguration",
        "identity_provider_configuration": "identityProviderConfiguration",
        "origins": "origins",
        "role_arn": "roleArn",
        "sample_prompts_control_mode": "samplePromptsControlMode",
        "subtitle": "subtitle",
        "tags": "tags",
        "title": "title",
        "welcome_message": "welcomeMessage",
    },
)
class CfnWebExperienceProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        browser_extension_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebExperience.BrowserExtensionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        customization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebExperience.CustomizationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        identity_provider_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebExperience.IdentityProviderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        role_arn: typing.Optional[builtins.str] = None,
        sample_prompts_control_mode: typing.Optional[builtins.str] = None,
        subtitle: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        title: typing.Optional[builtins.str] = None,
        welcome_message: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnWebExperience``.

        :param application_id: The identifier of the Amazon Q Business web experience.
        :param browser_extension_configuration: The container for browser extension configuration for an Amazon Q Business web experience.
        :param customization_configuration: Contains the configuration information to customize the logo, font, and color of an Amazon Q Business web experience with individual files for each property or a CSS file for them all.
        :param identity_provider_configuration: Provides information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.
        :param origins: Sets the website domain origins that are allowed to embed the Amazon Q Business web experience. The *domain origin* refers to the base URL for accessing a website including the protocol ( ``http/https`` ), the domain name, and the port number (if specified). .. epigraph:: You must only submit a *base URL* and not a full path. For example, ``https://docs.aws.amazon.com`` .
        :param role_arn: The Amazon Resource Name (ARN) of the service role attached to your web experience. .. epigraph:: The ``roleArn`` parameter is required when your Amazon Q Business application is created with IAM Identity Center. It is not required for SAML-based applications.
        :param sample_prompts_control_mode: Determines whether sample prompts are enabled in the web experience for an end user.
        :param subtitle: A subtitle to personalize your Amazon Q Business web experience.
        :param tags: A list of key-value pairs that identify or categorize your Amazon Q Business web experience. You can also use tags to help control access to the web experience. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -
        :param title: The title for your Amazon Q Business web experience.
        :param welcome_message: A message in an Amazon Q Business web experience.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-webexperience.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_qbusiness as qbusiness
            
            cfn_web_experience_props = qbusiness.CfnWebExperienceProps(
                application_id="applicationId",
            
                # the properties below are optional
                browser_extension_configuration=qbusiness.CfnWebExperience.BrowserExtensionConfigurationProperty(
                    enabled_browser_extensions=["enabledBrowserExtensions"]
                ),
                customization_configuration=qbusiness.CfnWebExperience.CustomizationConfigurationProperty(
                    custom_css_url="customCssUrl",
                    favicon_url="faviconUrl",
                    font_url="fontUrl",
                    logo_url="logoUrl"
                ),
                identity_provider_configuration=qbusiness.CfnWebExperience.IdentityProviderConfigurationProperty(
                    open_id_connect_configuration=qbusiness.CfnWebExperience.OpenIDConnectProviderConfigurationProperty(
                        secrets_arn="secretsArn",
                        secrets_role="secretsRole"
                    ),
                    saml_configuration=qbusiness.CfnWebExperience.SamlProviderConfigurationProperty(
                        authentication_url="authenticationUrl"
                    )
                ),
                origins=["origins"],
                role_arn="roleArn",
                sample_prompts_control_mode="samplePromptsControlMode",
                subtitle="subtitle",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                title="title",
                welcome_message="welcomeMessage"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58d2b12e60ffd88803f1746b34f5f9b5b77805b460b8074165db15b9de292293)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument browser_extension_configuration", value=browser_extension_configuration, expected_type=type_hints["browser_extension_configuration"])
            check_type(argname="argument customization_configuration", value=customization_configuration, expected_type=type_hints["customization_configuration"])
            check_type(argname="argument identity_provider_configuration", value=identity_provider_configuration, expected_type=type_hints["identity_provider_configuration"])
            check_type(argname="argument origins", value=origins, expected_type=type_hints["origins"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument sample_prompts_control_mode", value=sample_prompts_control_mode, expected_type=type_hints["sample_prompts_control_mode"])
            check_type(argname="argument subtitle", value=subtitle, expected_type=type_hints["subtitle"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument welcome_message", value=welcome_message, expected_type=type_hints["welcome_message"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
        }
        if browser_extension_configuration is not None:
            self._values["browser_extension_configuration"] = browser_extension_configuration
        if customization_configuration is not None:
            self._values["customization_configuration"] = customization_configuration
        if identity_provider_configuration is not None:
            self._values["identity_provider_configuration"] = identity_provider_configuration
        if origins is not None:
            self._values["origins"] = origins
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if sample_prompts_control_mode is not None:
            self._values["sample_prompts_control_mode"] = sample_prompts_control_mode
        if subtitle is not None:
            self._values["subtitle"] = subtitle
        if tags is not None:
            self._values["tags"] = tags
        if title is not None:
            self._values["title"] = title
        if welcome_message is not None:
            self._values["welcome_message"] = welcome_message

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The identifier of the Amazon Q Business web experience.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-webexperience.html#cfn-qbusiness-webexperience-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def browser_extension_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWebExperience.BrowserExtensionConfigurationProperty]]:
        '''The container for browser extension configuration for an Amazon Q Business web experience.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-webexperience.html#cfn-qbusiness-webexperience-browserextensionconfiguration
        '''
        result = self._values.get("browser_extension_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWebExperience.BrowserExtensionConfigurationProperty]], result)

    @builtins.property
    def customization_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWebExperience.CustomizationConfigurationProperty]]:
        '''Contains the configuration information to customize the logo, font, and color of an Amazon Q Business web experience with individual files for each property or a CSS file for them all.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-webexperience.html#cfn-qbusiness-webexperience-customizationconfiguration
        '''
        result = self._values.get("customization_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWebExperience.CustomizationConfigurationProperty]], result)

    @builtins.property
    def identity_provider_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWebExperience.IdentityProviderConfigurationProperty]]:
        '''Provides information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-webexperience.html#cfn-qbusiness-webexperience-identityproviderconfiguration
        '''
        result = self._values.get("identity_provider_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWebExperience.IdentityProviderConfigurationProperty]], result)

    @builtins.property
    def origins(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Sets the website domain origins that are allowed to embed the Amazon Q Business web experience.

        The *domain origin* refers to the base URL for accessing a website including the protocol ( ``http/https`` ), the domain name, and the port number (if specified).
        .. epigraph::

           You must only submit a *base URL* and not a full path. For example, ``https://docs.aws.amazon.com`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-webexperience.html#cfn-qbusiness-webexperience-origins
        '''
        result = self._values.get("origins")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the service role attached to your web experience.

        .. epigraph::

           The ``roleArn`` parameter is required when your Amazon Q Business application is created with IAM Identity Center. It is not required for SAML-based applications.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-webexperience.html#cfn-qbusiness-webexperience-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sample_prompts_control_mode(self) -> typing.Optional[builtins.str]:
        '''Determines whether sample prompts are enabled in the web experience for an end user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-webexperience.html#cfn-qbusiness-webexperience-samplepromptscontrolmode
        '''
        result = self._values.get("sample_prompts_control_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subtitle(self) -> typing.Optional[builtins.str]:
        '''A subtitle to personalize your Amazon Q Business web experience.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-webexperience.html#cfn-qbusiness-webexperience-subtitle
        '''
        result = self._values.get("subtitle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that identify or categorize your Amazon Q Business web experience.

        You can also use tags to help control access to the web experience. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + -

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-webexperience.html#cfn-qbusiness-webexperience-tags
        :: .
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''The title for your Amazon Q Business web experience.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-webexperience.html#cfn-qbusiness-webexperience-title
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def welcome_message(self) -> typing.Optional[builtins.str]:
        '''A message in an Amazon Q Business web experience.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-webexperience.html#cfn-qbusiness-webexperience-welcomemessage
        '''
        result = self._values.get("welcome_message")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWebExperienceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
    "CfnDataAccessor",
    "CfnDataAccessorProps",
    "CfnDataSource",
    "CfnDataSourceProps",
    "CfnIndex",
    "CfnIndexProps",
    "CfnPermission",
    "CfnPermissionProps",
    "CfnPlugin",
    "CfnPluginProps",
    "CfnRetriever",
    "CfnRetrieverProps",
    "CfnWebExperience",
    "CfnWebExperienceProps",
]

publication.publish()

def _typecheckingstub__e2c95edfee8896187b03149b15ce3604b3a59bfb3b08abd73c5672b7c0fc870b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    display_name: builtins.str,
    attachments_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.AttachmentsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    auto_subscription_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.AutoSubscriptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    client_ids_for_oidc: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iam_identity_provider_arn: typing.Optional[builtins.str] = None,
    identity_center_instance_arn: typing.Optional[builtins.str] = None,
    identity_type: typing.Optional[builtins.str] = None,
    personalization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.PersonalizationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    q_apps_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.QAppsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    quick_sight_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.QuickSightConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47a4b6795acfe5e89f676295cf4c40b3a8dced361f2d77a9b9d10c72aa48712c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d7a38d26d56344056de3cf30103a79b8126175e49d814d22bd2a8de217fa1cd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33b274b95ca4bace4d079a2b1a1973f1ffbc3a648fc9107b7c44cb7f842f4da1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57c12a095537be640da7b57fecbf3b07e85d4c25f19b33011eba52664eb319bf(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.AttachmentsConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b35a2b0fba0b74bf88677e8d09b2943fd8623f4b30bfa5113d4dd6400769370(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.AutoSubscriptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e16dbf7c72949c3994e85619024d1169320455f5129fc42720ee3369ccfe5013(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc81ccdbed36f390524b7f7b30696df462f8857fc5dbadb944cf0de3caf79186(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6de90c5382cc0edcebad422dab80436e0194a3dee33a2061cee4fd766fca3803(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.EncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b960c5b2a263370b2ed8902e4658a930ce9de4e1d95a848786663e3d07945d0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e51ab74f20033849c9b717566b2c1f59a066782ff0aafb4adb05ce552f5019a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44221a178b075fcdd809e631de43085ff6e3f91b9741304fd15e1a0dc442eae1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa9c62867ef8fd21c925099f5633037e806bdc6c1fd8880e42968edf98de8ec2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.PersonalizationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53d92c70961aea8a11ca2bb523fd9f10d2b780d9bda90114e0350e538ef5bd70(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.QAppsConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__289094e649887b05a6dfd8fdfb09369f7df0be2c7c7ede77435c953ed16f9d97(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.QuickSightConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1658266e462038ba089b94b22bb7d75b2047bb6b00110e1a3ad8d2941efe4b91(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71701e84c409132b62c2159d4eb096fd21722d0898465ad5f753fb5e9336a3d4(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e846388f34383d4a53c1ad7c73621d6c0612dd1cab1047d5850af68422a622cc(
    *,
    attachments_control_mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14d50e4994c3366ddeb7da76131ecc6e103dc3ed4c7bb2ec4ce982b547d2ab3b(
    *,
    auto_subscribe: builtins.str,
    default_subscription_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3ddb5009b3c1bf36876f4e9d68c61c40a1e8a10287a7a292f89a801fcc9ca73(
    *,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c530a7a40f7de7f808af2f7755372bf178629a393e2508771fc91224c8446f(
    *,
    personalization_control_mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b7142160185e09a91c9d85e4a5dafc98a64398c744201a937b09ca7cc1de37e(
    *,
    q_apps_control_mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a553c98b052035d7e975a15cd8521cc9a275d10bf22d783650de9883bdd715a(
    *,
    client_namespace: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd218bde3aa6ce3304b30e1d4799c501a50db8db5cef8926c28924af066170bb(
    *,
    display_name: builtins.str,
    attachments_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.AttachmentsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    auto_subscription_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.AutoSubscriptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    client_ids_for_oidc: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iam_identity_provider_arn: typing.Optional[builtins.str] = None,
    identity_center_instance_arn: typing.Optional[builtins.str] = None,
    identity_type: typing.Optional[builtins.str] = None,
    personalization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.PersonalizationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    q_apps_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.QAppsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    quick_sight_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.QuickSightConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b7ecf69912e25edcd2354b3e0497931ea6bf042b1aabc881c8677d2f9be633(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    action_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.ActionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    application_id: builtins.str,
    display_name: builtins.str,
    principal: builtins.str,
    authentication_detail: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.DataAccessorAuthenticationDetailProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff90302eca1e0f24b3ab926881bc0099a551d74c3a71debb214f222b63ff0ee4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75e79c605177a09c4ca1c1253b30113e8f2b7e023dafa75d6583c9b993c3a905(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a27c05d04ed77ea1630a00c4575933bd29a7548e12cd5406b1a703d094f618f7(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataAccessor.ActionConfigurationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d51b8675a76ff8aa3cd324d2a65da776f4afb1d4600f74839c262998a87adb06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d24d4191af1a9b63f7ef66ae53cd5e78c9587db0b3d4e54adc5863415cdec9f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd64ede16f385d2990fa12fa363564c55f359fed279a75365018e42cd6e63fff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aa34af043257e0411af6e09ebeda77531edcaba51ad9fd392b4515b8c730792(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataAccessor.DataAccessorAuthenticationDetailProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17fcd903858daed5111fdf34ce66e12720cfa6fd9e1712eb5744a4b8c06fb1fe(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__070f31842bf80fdbf737bccdee5b0121eca70d5c6c0d69c119f4d283e3dc8f0f(
    *,
    action: builtins.str,
    filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.ActionFilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8fdd75aa62747889da79fe0b8ab1526d92b0a13360be1d371fd7ca34ee6894e(
    *,
    document_attribute_filter: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.AttributeFilterProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0944dd9fc73c38902199011a9a1b06a552398d255157793794e769d86581ed7(
    *,
    and_all_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.AttributeFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    contains_all: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.DocumentAttributeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    contains_any: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.DocumentAttributeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    equals_to: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.DocumentAttributeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    greater_than: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.DocumentAttributeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    greater_than_or_equals: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.DocumentAttributeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    less_than: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.DocumentAttributeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    less_than_or_equals: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.DocumentAttributeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    not_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.AttributeFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    or_all_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.AttributeFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5026e300a407a951a2bf85ba48cf1646fb1b1672f84f2ea26974311fd2b650de(
    *,
    idc_trusted_token_issuer_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.DataAccessorIdcTrustedTokenIssuerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce3d0eb33f705ecbcd9b23e1fae7014cc8010d410a8398ce3feea55694ebed37(
    *,
    authentication_type: builtins.str,
    authentication_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.DataAccessorAuthenticationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    external_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa8bef9d39508faf93f48a0365a4605be496aa8cf95d29ab54e4ceabbabaef4d(
    *,
    idc_trusted_token_issuer_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc877a8d06303e2294e4f8e5813534f57082fb9476b669bafe4451af29bb5979(
    *,
    name: builtins.str,
    value: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.DocumentAttributeValueProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edee8eec89905fde650437fb2fcf2bc7ddeaecc251be16c2ca1d64d79b7eb5a5(
    *,
    date_value: typing.Optional[builtins.str] = None,
    long_value: typing.Optional[jsii.Number] = None,
    string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dfde2d4c17793fa3cb9793a9171b9042ac55727b3f0c3a17f1606cab5545458(
    *,
    action_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.ActionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    application_id: builtins.str,
    display_name: builtins.str,
    principal: builtins.str,
    authentication_detail: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataAccessor.DataAccessorAuthenticationDetailProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44090f525589bca757ae88a29adc87bbfc36c3149c7964dfd32c2ce59b69db58(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    configuration: typing.Any,
    display_name: builtins.str,
    index_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    document_enrichment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DocumentEnrichmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    media_extraction_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.MediaExtractionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    sync_schedule: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DataSourceVpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd73286fa4603be5641a3ab936a93b6e83fc252d5d52182c6f0fe270c5b2a406(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cb4db65ad9a4064e0bd46d63da12c54d5ac52caacffc9558dcf744690635e34(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8744e8719ac2ce0a440adec3d28e40857aa43a2f9e7d48ebb99d9244f314b5a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__033036d2c97cbb0707403571def9bb03fcccaabedc00afaa4905a276eaa169f8(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3480e9c01e998df4f3c9b61416967b6ad224790241607484ad0376c1d24b18c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4ad13a5736b96bc7b5adfb1cf4b9e58f4559cef04a6fb6756627a56e47c0e83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81151bd66f1686e0470c9ae1dddd9a5cd72c8ceb371d917771c8268073fc8a76(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe2866ff8510082e320bc29f43593004da60817112846504497bbb0dbac73cc0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DocumentEnrichmentConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61d3297e7877958a257749ac6dada8495933c305bc80bd233f5feb0fe4960a81(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.MediaExtractionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d17e6c9d50eaaabc9ce2688b35a56e877aaf39df8cd76e73354477d7d5c11a84(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d95ad8757220562be3c4a2a414d2a025dbf8de65b35ee49cd77167e02940024b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0de23b55ca19c08a4a44c0f9e5ef175e05b82d5a4bdd9d882f044cad9d03ad5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a2baf273288668ce3827242609bec0e4533974d4ecb7707e426b1a449d645ed(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataSource.DataSourceVpcConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aa789e6cda3c90d0db840a9741bbd7eb7b84f0436483843586f56121cdfe2a1(
    *,
    audio_extraction_status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df3bb5deb9e194276e6702b02f19aa8cb471bee4bf023f5613bcb797abcb6c0f(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faa143d45871c83d6e11352afa882fd65640863f02336e1b649bb0c8fa098521(
    *,
    key: builtins.str,
    operator: builtins.str,
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DocumentAttributeValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d708153a1aeec62ef33a5e5a47aab28a65d6a8ff6b4222dddee34e2ca80657d1(
    *,
    key: builtins.str,
    attribute_value_operator: typing.Optional[builtins.str] = None,
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DocumentAttributeValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__732ff9c08b1e4382c875518343d9cd2daa4054ae31bb370a40d7e1a2f63524ba(
    *,
    date_value: typing.Optional[builtins.str] = None,
    long_value: typing.Optional[jsii.Number] = None,
    string_list_value: typing.Optional[typing.Sequence[builtins.str]] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a842fef6354222b46871e910d15813711d18a6c607448aa28aded9095e40088(
    *,
    inline_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.InlineDocumentEnrichmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    post_extraction_hook_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.HookConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    pre_extraction_hook_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.HookConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c33bb8fd2eb803e7000af5893f4f1c6c2062cdbf9cefd30bb8af8419e8f9815(
    *,
    invocation_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DocumentAttributeConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lambda_arn: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    s3_bucket_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40e7364b05e4957f04891e99e2b4de3fa819ddcc49a154a8118fdf016503e031(
    *,
    image_extraction_status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2025544f51e1e49d0d5dbfb988fb4b22f5cc28a154bdb2e2fe6039f0e941da63(
    *,
    condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DocumentAttributeConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    document_content_operator: typing.Optional[builtins.str] = None,
    target: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DocumentAttributeTargetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45d49817772a3b69716257ee4a29683841b4420b41115ce7a18bc124fe4f9f87(
    *,
    audio_extraction_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.AudioExtractionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_extraction_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.ImageExtractionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    video_extraction_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.VideoExtractionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f97caeacd344e3e67dbf0813f2131b0e4d7a3ac8e1f32dcc24431822f666336b(
    *,
    video_extraction_status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0cb43c018c99c9e24bb29f0d009e1ded318999b690c706f1e2e099d30a9fe07(
    *,
    application_id: builtins.str,
    configuration: typing.Any,
    display_name: builtins.str,
    index_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    document_enrichment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DocumentEnrichmentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    media_extraction_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.MediaExtractionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    sync_schedule: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataSource.DataSourceVpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c457625f955b1ba56d35bffbcea827abe87347b80fd33090422ef2a8092cd10e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    display_name: builtins.str,
    capacity_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.IndexCapacityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    document_attribute_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.DocumentAttributeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc39e6b7456662ae032c4446b1ba1e83f54ae382ca6aabc48cbb69fac624aef4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccebcb19696a76d2278342081344ed6aff74ba711a12c7cbea56e4141c1e5a8e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54ff836942c63690dc16a9e4027a9abd09b398c38793f26cca38af64610bbe71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4544cd5fba280d2357dbc3ee91f9e13aef38c4a53c6724b7e9e5f519c4e884cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f6c721ddc40768da88ec10387c1ad38a220a25dbc3088182cc077f9e0481f58(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIndex.IndexCapacityConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b986b341eaa6de5f44cf18bf19e514c21ac9e68197655e6ac87cd46eaa48c11d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcf5f23ed97cc59f3cf9c24f10906f928933142ac816c6896d51159e901208fb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnIndex.DocumentAttributeConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2007e1968cafb6cf72816a82731de79853a45701bf488b078fb39be6d392338b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b9d98917178d25544f20415f3d2719e55f952a06eaafca35fcbf7305cbf2ce2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d0cead578e39a3d615afa214bd45404540048cc5c5294a13dc51d68c94cea7c(
    *,
    name: typing.Optional[builtins.str] = None,
    search: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9aec8c22fc6bbbb296721a0ec2a0851e079e8e6bb48cde9ad3338210a91789e(
    *,
    units: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f224eda571af2cef15f793eab49628d157ba54696a8e8bfa469fa8ac5c66802(
    *,
    text_document_statistics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.TextDocumentStatisticsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53655170c0e554a34ac668a43b8c91b79ec330d9f9720473bc0190dd37864bb9(
    *,
    indexed_text_bytes: typing.Optional[jsii.Number] = None,
    indexed_text_document_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92562a229c76d1c1bf48f7735d22def1e598923d94ebef2d66b70a174c48887e(
    *,
    application_id: builtins.str,
    display_name: builtins.str,
    capacity_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.IndexCapacityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    document_attribute_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.DocumentAttributeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa8b9992ffebedf4dda280be4bd0aa5dade8d62a6c092d850b1b1bb8df042ee8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    actions: typing.Sequence[builtins.str],
    application_id: builtins.str,
    principal: builtins.str,
    statement_id: builtins.str,
    conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermission.ConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__486d860cba58c25ad8a704d89ac04d1c97b77e0a8335b95ea6b91e0055822d82(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b04db3dd9150fe212749577b23464a861914114372d66de4e94f86f0c249312(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39d8a75c9a38f2eedadc1f546593db77ee47e4125872cb57b22cf5548b71f021(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8fe48822501c0010e5b09bf79b5fbff369d246e10a55c9aa06207fb883b9011(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0006a2c0010c9479f601e5c854918c05afd29c14583b90821fa3cec8abe28068(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bf1e79f20a58bfbabb1ce356f12e0ce01131844f0c50f11db4e0f82f47f71e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df7eedd7834a134466643c8bd40b7906fe6b7fcc7f482e5265aec4bb05607f6a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPermission.ConditionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39a9bd842be75583d990f7774438e331f4161b57ee4d98a449b293c0e014f90d(
    *,
    condition_key: builtins.str,
    condition_operator: builtins.str,
    condition_values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea87fcda68d4a26468f5e5d1c394a46d117b80b00274f61bbd36b0329a0a8c4(
    *,
    actions: typing.Sequence[builtins.str],
    application_id: builtins.str,
    principal: builtins.str,
    statement_id: builtins.str,
    conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermission.ConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65b6fb8d65ff428790a22d304932f2713710d70a9f6d789d819489f81a05b6f1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    auth_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlugin.PluginAuthConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    display_name: builtins.str,
    type: builtins.str,
    application_id: typing.Optional[builtins.str] = None,
    custom_plugin_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlugin.CustomPluginConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    server_url: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fec924728d6923b494037839fb41ee39d956abff0dc273347be667ed27df77ff(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc4e2ac4c2bff624e773994eee3ffed34fc99668cd3dc39ca6b437875ecc9db3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc09bef25ae0d3b934b9f84632eb962f4421b7e977774cbd9588396218197347(
    value: typing.Union[_IResolvable_da3f097b, CfnPlugin.PluginAuthConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3763a7a98296d5eaa6a62be4515663f4255d3a3e157dd717034c5ccf1e2ef323(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fb0c242fab3286e70f3bc5d132c40cefb0d3796d14ea543a14437f3494d980a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b30e993c552d6b7b2897c130ead401b972163585b579b8261fba5f11c45ea7f5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca8ebc7a910b53db546c0124994a836ad4abf9624aa8a90b48603c35f2536b6b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPlugin.CustomPluginConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc4df0ea830d17e6a6176b82211b1924f080b964b8936cbebb663e6fa55f87b6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d484260cba976d4aa57562eaeb794488a5d8e68c91f221a7292e9a740fc35a7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5f493e517da9a6377b62a1cf76303e94908f2643bc058b74f238336623aa73c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__000221b1c4915448dbcbd7992684ae4bb62f1df7f27a3a97095792e5b41bede9(
    *,
    payload: typing.Optional[builtins.str] = None,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlugin.S3Property, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf3d694e6789020aa132884a8dde4093d7a29a567925c540d842ca3be3c21140(
    *,
    role_arn: builtins.str,
    secret_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d7174f1197c1724dbfaa655cabb50877063a350e7de7a6595b3362e938610c(
    *,
    api_schema: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlugin.APISchemaProperty, typing.Dict[builtins.str, typing.Any]]],
    api_schema_type: builtins.str,
    description: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bc6d1d65b9c1e5c3607318c662a2a393df7ecf909b2d2ef7437364ade744000(
    *,
    role_arn: builtins.str,
    secret_arn: builtins.str,
    authorization_url: typing.Optional[builtins.str] = None,
    token_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__794967140c3985d1690a000f51a65af5981b07a000a2f040ae98c0f6715c5908(
    *,
    basic_auth_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlugin.BasicAuthConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    no_auth_configuration: typing.Any = None,
    o_auth2_client_credential_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlugin.OAuth2ClientCredentialConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f7a033a4dede9d0d05480348522d93d5c1d4a0e27d0009e6612ae5c51706450(
    *,
    bucket: builtins.str,
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84b206da5d8532987dc555e3bb32deb781317bbd9702ad893387d9a51e07b05f(
    *,
    auth_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlugin.PluginAuthConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    display_name: builtins.str,
    type: builtins.str,
    application_id: typing.Optional[builtins.str] = None,
    custom_plugin_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlugin.CustomPluginConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    server_url: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__793749362ec6ccd890aa9273b100a2ba004492449f0dba0ea4eb4909560d6761(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRetriever.RetrieverConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    display_name: builtins.str,
    type: builtins.str,
    role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__013b1c812aa4f36fb41a3e6e2da02553a56882a0b9e6a92ca26d883a232dfb06(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9a004f85d31923ae2ecfb060d2466d212e1a4b3eb2b1d0a85dac42f69eb890d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe00bdbe02b12a657cfeff7e2758f761be1b99feb8a57c9d90eefb2a27988ba5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__217b852c34b828ca9e117a115c4c1102c46f4c52ed7ae79bf971909a3b377950(
    value: typing.Union[_IResolvable_da3f097b, CfnRetriever.RetrieverConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0210d78e5dd49ca379837adfff5fc5c7423190f4b404ead346c53e8cb560f7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71e17a562de6a77df0f17f7c55a951b865eb0257648446cd07b68dd023e7f408(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02e9bb09b1c416cf967c103b8f223187ac470c6c171ef163f428010c529749e0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e5b60be4a7320479711492eed9182af16eefeea87cf17ce9fbe556d9595c602(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d067d57356504f1eb2ff62bfca1f5b675d526d553b4a48e366c1185d56eb861(
    *,
    index_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc0a2d6ec7e39104efb95392cc9115abfce755af10ee176a49e2ab8bd89ad1c9(
    *,
    index_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a87eb68b4d13ad399e3831bda05bdee7126f9c5a1a3f94de678194cb12a2855(
    *,
    kendra_index_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRetriever.KendraIndexConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    native_index_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRetriever.NativeIndexConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d26f55565cdfd207bc3128a08abf6cd7e371950c5a332ccf3973859a33980b6(
    *,
    application_id: builtins.str,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRetriever.RetrieverConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    display_name: builtins.str,
    type: builtins.str,
    role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__357871375e43a0ed6fbb398668ece13df26dff3afca5c98268a56fffdb09ec8d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_id: builtins.str,
    browser_extension_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebExperience.BrowserExtensionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    customization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebExperience.CustomizationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    identity_provider_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebExperience.IdentityProviderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    origins: typing.Optional[typing.Sequence[builtins.str]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    sample_prompts_control_mode: typing.Optional[builtins.str] = None,
    subtitle: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    title: typing.Optional[builtins.str] = None,
    welcome_message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18f54626970b688afafe657434af722476d6086ca982ba2b3c0785ca472ce28e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84d2429ec4e0f829c4548e994cc7bffc96574be7e836657297f4565bd58c2bf3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__994b24302ed92226579fa1ecdeef04d0cb66956019e467efcd9374ab264f8f90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a0cdf2a88c334b7d14f1ec069e84cd3cde5e237c3b2738cec3187653fcd4075(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWebExperience.BrowserExtensionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf72d65c47bcc616319908521026308ce2d7a5972c8d440077fbbf82ebb97663(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWebExperience.CustomizationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__037151dbe9f2f36da364495e39b2467a261694df042a6b81d84e5c2c34771ac4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWebExperience.IdentityProviderConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efefc83f84ced0d16f9a7d4536640a373b6576081faef2262e41578447add1df(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e93af1c8c50a8fbbba5f2f4c0d1013951bd550b401230f1ec2637c4955cea1b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bc39c1915319ccfd9bde90f397adff04c0e3cf7775254eb327fb93987a541f3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4a35577085528c30fbee7242c0023bcd3ff26b129706d1aaca7044143958243(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28dfc304b43632af9e6915e06d6d8106a7a8e887153b3c37db8331f47b275d30(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b6d52e113fec7d083295c445d34ded7755cb3f797753c6ea3a174a05082795b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dc11f2c0364936c993f550de31ea07513a76ae6f389384341e03770b293ecaf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f63b3566e87de98155904278bf52684ee22c6e0894e4de3e473b4a1ff103b900(
    *,
    enabled_browser_extensions: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0715100f79db57a5a95a4fef0f7ea187376551e20bd796d1d430e1fd8d50a4d(
    *,
    custom_css_url: typing.Optional[builtins.str] = None,
    favicon_url: typing.Optional[builtins.str] = None,
    font_url: typing.Optional[builtins.str] = None,
    logo_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f792f47d6a0722e8b808ad22d67aec07629a1e7351865cae0ee890cff9ba5c1a(
    *,
    open_id_connect_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebExperience.OpenIDConnectProviderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    saml_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebExperience.SamlProviderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83ea977b859d6c4c1e46fa972ce0e7d691c60d57b7c59adbe13d851526eb765e(
    *,
    secrets_arn: builtins.str,
    secrets_role: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f19a9da1f3a1cf2eefff3580476a949609debe65a8fc477af11c893d5b4453b(
    *,
    authentication_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58d2b12e60ffd88803f1746b34f5f9b5b77805b460b8074165db15b9de292293(
    *,
    application_id: builtins.str,
    browser_extension_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebExperience.BrowserExtensionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    customization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebExperience.CustomizationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    identity_provider_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWebExperience.IdentityProviderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    origins: typing.Optional[typing.Sequence[builtins.str]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    sample_prompts_control_mode: typing.Optional[builtins.str] = None,
    subtitle: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    title: typing.Optional[builtins.str] = None,
    welcome_message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
