r'''
# AWS::PCAConnectorSCEP Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_pcaconnectorscep as pcaconnectorscep
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for PCAConnectorSCEP construct libraries](https://constructs.dev/search?q=pcaconnectorscep)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::PCAConnectorSCEP resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_PCAConnectorSCEP.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::PCAConnectorSCEP](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_PCAConnectorSCEP.html).

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
class CfnChallenge(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pcaconnectorscep.CfnChallenge",
):
    '''For general-purpose connectors.

    Creates a *challenge password* for the specified connector. The SCEP protocol uses a challenge password to authenticate a request before issuing a certificate from a certificate authority (CA). Your SCEP clients include the challenge password as part of their certificate request to Connector for SCEP. To retrieve the connector Amazon Resource Names (ARNs) for the connectors in your account, call `ListConnectors <https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListConnectors.html>`_ .

    To create additional challenge passwords for the connector, call ``CreateChallenge`` again. We recommend frequently rotating your challenge passwords.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorscep-challenge.html
    :cloudformationResource: AWS::PCAConnectorSCEP::Challenge
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pcaconnectorscep as pcaconnectorscep
        
        cfn_challenge = pcaconnectorscep.CfnChallenge(self, "MyCfnChallenge",
            connector_arn="connectorArn",
        
            # the properties below are optional
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
        connector_arn: builtins.str,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param connector_arn: The Amazon Resource Name (ARN) of the connector.
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24eb7fbef30f2d313fbf471c0e0cb20de5d3f7212801db2cea706e879fcbffbb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnChallengeProps(connector_arn=connector_arn, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d35413f13465487597f5d259678227986782b9e226cea3ff09ffde5c120680ea)
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
            type_hints = typing.get_type_hints(_typecheckingstub__489654af0c0fb058e21c2b228cbdb80abf0c133d0fb41f63a099fdd056c22465)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrChallengeArn")
    def attr_challenge_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the challenge.

        :cloudformationAttribute: ChallengeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrChallengeArn"))

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
    @jsii.member(jsii_name="connectorArn")
    def connector_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the connector.'''
        return typing.cast(builtins.str, jsii.get(self, "connectorArn"))

    @connector_arn.setter
    def connector_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8915b9dc72ee63e750d3ef96a5cb2aff8a0fa11b46fd75a91cbaf3be0bbba4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02346c7d1384ddbe7e216be1ce5a2eaa7010ca8e5397d2d7987583123fa40455)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pcaconnectorscep.CfnChallengeProps",
    jsii_struct_bases=[],
    name_mapping={"connector_arn": "connectorArn", "tags": "tags"},
)
class CfnChallengeProps:
    def __init__(
        self,
        *,
        connector_arn: builtins.str,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnChallenge``.

        :param connector_arn: The Amazon Resource Name (ARN) of the connector.
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorscep-challenge.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pcaconnectorscep as pcaconnectorscep
            
            cfn_challenge_props = pcaconnectorscep.CfnChallengeProps(
                connector_arn="connectorArn",
            
                # the properties below are optional
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b914295b53d2239fac5aeded2d49fbf0b75e45d55296f667c76fc35288cf677)
            check_type(argname="argument connector_arn", value=connector_arn, expected_type=type_hints["connector_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_arn": connector_arn,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def connector_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorscep-challenge.html#cfn-pcaconnectorscep-challenge-connectorarn
        '''
        result = self._values.get("connector_arn")
        assert result is not None, "Required property 'connector_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorscep-challenge.html#cfn-pcaconnectorscep-challenge-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChallengeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnConnector(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pcaconnectorscep.CfnConnector",
):
    '''Connector for SCEP is a service that links AWS Private Certificate Authority to your SCEP-enabled devices.

    The connector brokers the exchange of certificates from AWS Private CA to your SCEP-enabled devices and mobile device management systems. The connector is a complex type that contains the connector's configuration settings.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorscep-connector.html
    :cloudformationResource: AWS::PCAConnectorSCEP::Connector
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pcaconnectorscep as pcaconnectorscep
        
        cfn_connector = pcaconnectorscep.CfnConnector(self, "MyCfnConnector",
            certificate_authority_arn="certificateAuthorityArn",
        
            # the properties below are optional
            mobile_device_management=pcaconnectorscep.CfnConnector.MobileDeviceManagementProperty(
                intune=pcaconnectorscep.CfnConnector.IntuneConfigurationProperty(
                    azure_application_id="azureApplicationId",
                    domain="domain"
                )
            ),
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
        certificate_authority_arn: builtins.str,
        mobile_device_management: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.MobileDeviceManagementProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param certificate_authority_arn: The Amazon Resource Name (ARN) of the certificate authority associated with the connector.
        :param mobile_device_management: Contains settings relevant to the mobile device management system that you chose for the connector. If you didn't configure ``MobileDeviceManagement`` , then the connector is for general-purpose use and this object is empty.
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5efd0f2c3577f33ffa31fd98d59e33eaca0d3cabdfa1d7d8ade08be89356b0d0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectorProps(
            certificate_authority_arn=certificate_authority_arn,
            mobile_device_management=mobile_device_management,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eee6bfac2d042060de9b313d40e4659513d1a0a075b1017f98c1994d42607873)
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
            type_hints = typing.get_type_hints(_typecheckingstub__adf209a078c66c8ab9a74de9a70bf8d8422bfbb7495bd4cd8a458eef3a8953f6)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectorArn")
    def attr_connector_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the connector.

        :cloudformationAttribute: ConnectorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectorArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpoint")
    def attr_endpoint(self) -> builtins.str:
        '''The connector's HTTPS public SCEP URL.

        :cloudformationAttribute: Endpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrOpenIdConfiguration")
    def attr_open_id_configuration(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: OpenIdConfiguration
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrOpenIdConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''The connector type.

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

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
    @jsii.member(jsii_name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the certificate authority associated with the connector.'''
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthorityArn"))

    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__772a20f66443bc64cac3bb4157e1e9369d67a7a8d2b4109d885cebc2c5d1d87b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthorityArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mobileDeviceManagement")
    def mobile_device_management(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.MobileDeviceManagementProperty"]]:
        '''Contains settings relevant to the mobile device management system that you chose for the connector.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.MobileDeviceManagementProperty"]], jsii.get(self, "mobileDeviceManagement"))

    @mobile_device_management.setter
    def mobile_device_management(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.MobileDeviceManagementProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ad5d7a17f85a90225f468c73bd52466319e1c0daa9fee8bb5eb5ffcd32bd5c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mobileDeviceManagement", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d236715afe6b31af4cde4435b078b9b7c3146267ef69426b668c4592a3fd9ddc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorscep.CfnConnector.IntuneConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "azure_application_id": "azureApplicationId",
            "domain": "domain",
        },
    )
    class IntuneConfigurationProperty:
        def __init__(
            self,
            *,
            azure_application_id: builtins.str,
            domain: builtins.str,
        ) -> None:
            '''Contains configuration details for use with Microsoft Intune.

            For information about using Connector for SCEP for Microsoft Intune, see `Using Connector for SCEP for Microsoft Intune <https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html>`_ .

            When you use Connector for SCEP for Microsoft Intune, certain functionalities are enabled by accessing Microsoft Intune through the Microsoft API. Your use of the Connector for SCEP and accompanying AWS services doesn't remove your need to have a valid license for your use of the Microsoft Intune service. You should also review the `Microsoft Intune® App Protection Policies <https://docs.aws.amazon.com/https://learn.microsoft.com/en-us/mem/intune/apps/app-protection-policy>`_ .

            :param azure_application_id: The directory (tenant) ID from your Microsoft Entra ID app registration.
            :param domain: The primary domain from your Microsoft Entra ID app registration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorscep-connector-intuneconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorscep as pcaconnectorscep
                
                intune_configuration_property = pcaconnectorscep.CfnConnector.IntuneConfigurationProperty(
                    azure_application_id="azureApplicationId",
                    domain="domain"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa2975290c35d1208654a35b712842396cf4971f0e927191534541fb868fd148)
                check_type(argname="argument azure_application_id", value=azure_application_id, expected_type=type_hints["azure_application_id"])
                check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "azure_application_id": azure_application_id,
                "domain": domain,
            }

        @builtins.property
        def azure_application_id(self) -> builtins.str:
            '''The directory (tenant) ID from your Microsoft Entra ID app registration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorscep-connector-intuneconfiguration.html#cfn-pcaconnectorscep-connector-intuneconfiguration-azureapplicationid
            '''
            result = self._values.get("azure_application_id")
            assert result is not None, "Required property 'azure_application_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def domain(self) -> builtins.str:
            '''The primary domain from your Microsoft Entra ID app registration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorscep-connector-intuneconfiguration.html#cfn-pcaconnectorscep-connector-intuneconfiguration-domain
            '''
            result = self._values.get("domain")
            assert result is not None, "Required property 'domain' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntuneConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorscep.CfnConnector.MobileDeviceManagementProperty",
        jsii_struct_bases=[],
        name_mapping={"intune": "intune"},
    )
    class MobileDeviceManagementProperty:
        def __init__(
            self,
            *,
            intune: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.IntuneConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''If you don't supply a value, by default Connector for SCEP creates a connector for general-purpose use.

            A general-purpose connector is designed to work with clients or endpoints that support the SCEP protocol, except Connector for SCEP for Microsoft Intune. For information about considerations and limitations with using Connector for SCEP, see `Considerations and Limitations <https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlc4scep-considerations-limitations.html>`_ .

            If you provide an ``IntuneConfiguration`` , Connector for SCEP creates a connector for use with Microsoft Intune, and you manage the challenge passwords using Microsoft Intune. For more information, see `Using Connector for SCEP for Microsoft Intune <https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html>`_ .

            :param intune: Configuration settings for use with Microsoft Intune. For information about using Connector for SCEP for Microsoft Intune, see `Using Connector for SCEP for Microsoft Intune <https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorscep-connector-mobiledevicemanagement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorscep as pcaconnectorscep
                
                mobile_device_management_property = pcaconnectorscep.CfnConnector.MobileDeviceManagementProperty(
                    intune=pcaconnectorscep.CfnConnector.IntuneConfigurationProperty(
                        azure_application_id="azureApplicationId",
                        domain="domain"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c4701fa7706fc9d7c8386eed695d80c9aca2ebe3e669df810d63415a244a9d2c)
                check_type(argname="argument intune", value=intune, expected_type=type_hints["intune"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "intune": intune,
            }

        @builtins.property
        def intune(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnConnector.IntuneConfigurationProperty"]:
            '''Configuration settings for use with Microsoft Intune.

            For information about using Connector for SCEP for Microsoft Intune, see `Using Connector for SCEP for Microsoft Intune <https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorscep-connector-mobiledevicemanagement.html#cfn-pcaconnectorscep-connector-mobiledevicemanagement-intune
            '''
            result = self._values.get("intune")
            assert result is not None, "Required property 'intune' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConnector.IntuneConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MobileDeviceManagementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorscep.CfnConnector.OpenIdConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audience": "audience",
            "issuer": "issuer",
            "subject": "subject",
        },
    )
    class OpenIdConfigurationProperty:
        def __init__(
            self,
            *,
            audience: typing.Optional[builtins.str] = None,
            issuer: typing.Optional[builtins.str] = None,
            subject: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains OpenID Connect (OIDC) parameters for use with Microsoft Intune.

            For more information about using Connector for SCEP for Microsoft Intune, see `Using Connector for SCEP for Microsoft Intune <https://docs.aws.amazon.com/privateca/latest/userguide/scep-connector.htmlconnector-for-scep-intune.html>`_ .

            :param audience: The audience value to copy into your Microsoft Entra app registration's OIDC.
            :param issuer: The issuer value to copy into your Microsoft Entra app registration's OIDC.
            :param subject: The subject value to copy into your Microsoft Entra app registration's OIDC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorscep-connector-openidconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorscep as pcaconnectorscep
                
                open_id_configuration_property = pcaconnectorscep.CfnConnector.OpenIdConfigurationProperty(
                    audience="audience",
                    issuer="issuer",
                    subject="subject"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__94fa39891872fe5b5cb744eb26f9e2aeaa4235adb9c2d31d752f535b72be5bb1)
                check_type(argname="argument audience", value=audience, expected_type=type_hints["audience"])
                check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
                check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if audience is not None:
                self._values["audience"] = audience
            if issuer is not None:
                self._values["issuer"] = issuer
            if subject is not None:
                self._values["subject"] = subject

        @builtins.property
        def audience(self) -> typing.Optional[builtins.str]:
            '''The audience value to copy into your Microsoft Entra app registration's OIDC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorscep-connector-openidconfiguration.html#cfn-pcaconnectorscep-connector-openidconfiguration-audience
            '''
            result = self._values.get("audience")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def issuer(self) -> typing.Optional[builtins.str]:
            '''The issuer value to copy into your Microsoft Entra app registration's OIDC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorscep-connector-openidconfiguration.html#cfn-pcaconnectorscep-connector-openidconfiguration-issuer
            '''
            result = self._values.get("issuer")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subject(self) -> typing.Optional[builtins.str]:
            '''The subject value to copy into your Microsoft Entra app registration's OIDC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorscep-connector-openidconfiguration.html#cfn-pcaconnectorscep-connector-openidconfiguration-subject
            '''
            result = self._values.get("subject")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenIdConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pcaconnectorscep.CfnConnectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_authority_arn": "certificateAuthorityArn",
        "mobile_device_management": "mobileDeviceManagement",
        "tags": "tags",
    },
)
class CfnConnectorProps:
    def __init__(
        self,
        *,
        certificate_authority_arn: builtins.str,
        mobile_device_management: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.MobileDeviceManagementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnector``.

        :param certificate_authority_arn: The Amazon Resource Name (ARN) of the certificate authority associated with the connector.
        :param mobile_device_management: Contains settings relevant to the mobile device management system that you chose for the connector. If you didn't configure ``MobileDeviceManagement`` , then the connector is for general-purpose use and this object is empty.
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorscep-connector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pcaconnectorscep as pcaconnectorscep
            
            cfn_connector_props = pcaconnectorscep.CfnConnectorProps(
                certificate_authority_arn="certificateAuthorityArn",
            
                # the properties below are optional
                mobile_device_management=pcaconnectorscep.CfnConnector.MobileDeviceManagementProperty(
                    intune=pcaconnectorscep.CfnConnector.IntuneConfigurationProperty(
                        azure_application_id="azureApplicationId",
                        domain="domain"
                    )
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c22911c5ba9019291e6d26ad4968076543da6a84dd36e0fdf942f0f31d64e393)
            check_type(argname="argument certificate_authority_arn", value=certificate_authority_arn, expected_type=type_hints["certificate_authority_arn"])
            check_type(argname="argument mobile_device_management", value=mobile_device_management, expected_type=type_hints["mobile_device_management"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_authority_arn": certificate_authority_arn,
        }
        if mobile_device_management is not None:
            self._values["mobile_device_management"] = mobile_device_management
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def certificate_authority_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the certificate authority associated with the connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorscep-connector.html#cfn-pcaconnectorscep-connector-certificateauthorityarn
        '''
        result = self._values.get("certificate_authority_arn")
        assert result is not None, "Required property 'certificate_authority_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mobile_device_management(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnector.MobileDeviceManagementProperty]]:
        '''Contains settings relevant to the mobile device management system that you chose for the connector.

        If you didn't configure ``MobileDeviceManagement`` , then the connector is for general-purpose use and this object is empty.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorscep-connector.html#cfn-pcaconnectorscep-connector-mobiledevicemanagement
        '''
        result = self._values.get("mobile_device_management")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnector.MobileDeviceManagementProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorscep-connector.html#cfn-pcaconnectorscep-connector-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnChallenge",
    "CfnChallengeProps",
    "CfnConnector",
    "CfnConnectorProps",
]

publication.publish()

def _typecheckingstub__24eb7fbef30f2d313fbf471c0e0cb20de5d3f7212801db2cea706e879fcbffbb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connector_arn: builtins.str,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d35413f13465487597f5d259678227986782b9e226cea3ff09ffde5c120680ea(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__489654af0c0fb058e21c2b228cbdb80abf0c133d0fb41f63a099fdd056c22465(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8915b9dc72ee63e750d3ef96a5cb2aff8a0fa11b46fd75a91cbaf3be0bbba4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02346c7d1384ddbe7e216be1ce5a2eaa7010ca8e5397d2d7987583123fa40455(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b914295b53d2239fac5aeded2d49fbf0b75e45d55296f667c76fc35288cf677(
    *,
    connector_arn: builtins.str,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5efd0f2c3577f33ffa31fd98d59e33eaca0d3cabdfa1d7d8ade08be89356b0d0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    certificate_authority_arn: builtins.str,
    mobile_device_management: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.MobileDeviceManagementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eee6bfac2d042060de9b313d40e4659513d1a0a075b1017f98c1994d42607873(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adf209a078c66c8ab9a74de9a70bf8d8422bfbb7495bd4cd8a458eef3a8953f6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__772a20f66443bc64cac3bb4157e1e9369d67a7a8d2b4109d885cebc2c5d1d87b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ad5d7a17f85a90225f468c73bd52466319e1c0daa9fee8bb5eb5ffcd32bd5c3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnector.MobileDeviceManagementProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d236715afe6b31af4cde4435b078b9b7c3146267ef69426b668c4592a3fd9ddc(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa2975290c35d1208654a35b712842396cf4971f0e927191534541fb868fd148(
    *,
    azure_application_id: builtins.str,
    domain: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4701fa7706fc9d7c8386eed695d80c9aca2ebe3e669df810d63415a244a9d2c(
    *,
    intune: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.IntuneConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94fa39891872fe5b5cb744eb26f9e2aeaa4235adb9c2d31d752f535b72be5bb1(
    *,
    audience: typing.Optional[builtins.str] = None,
    issuer: typing.Optional[builtins.str] = None,
    subject: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c22911c5ba9019291e6d26ad4968076543da6a84dd36e0fdf942f0f31d64e393(
    *,
    certificate_authority_arn: builtins.str,
    mobile_device_management: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.MobileDeviceManagementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
