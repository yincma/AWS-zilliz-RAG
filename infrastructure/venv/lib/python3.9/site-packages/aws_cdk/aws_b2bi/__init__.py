r'''
# AWS::B2BI Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_b2bi as b2bi
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for B2BI construct libraries](https://constructs.dev/search?q=b2bi)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::B2BI resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_B2BI.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::B2BI](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_B2BI.html).

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
class CfnCapability(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_b2bi.CfnCapability",
):
    '''Instantiates a capability based on the specified parameters.

    A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-capability.html
    :cloudformationResource: AWS::B2BI::Capability
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_b2bi as b2bi
        
        cfn_capability = b2bi.CfnCapability(self, "MyCfnCapability",
            configuration=b2bi.CfnCapability.CapabilityConfigurationProperty(
                edi=b2bi.CfnCapability.EdiConfigurationProperty(
                    input_location=b2bi.CfnCapability.S3LocationProperty(
                        bucket_name="bucketName",
                        key="key"
                    ),
                    output_location=b2bi.CfnCapability.S3LocationProperty(
                        bucket_name="bucketName",
                        key="key"
                    ),
                    transformer_id="transformerId",
                    type=b2bi.CfnCapability.EdiTypeProperty(
                        x12_details=b2bi.CfnCapability.X12DetailsProperty(
                            transaction_set="transactionSet",
                            version="version"
                        )
                    ),
        
                    # the properties below are optional
                    capability_direction="capabilityDirection"
                )
            ),
            name="name",
            type="type",
        
            # the properties below are optional
            instructions_documents=[b2bi.CfnCapability.S3LocationProperty(
                bucket_name="bucketName",
                key="key"
            )],
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
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapability.CapabilityConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        type: builtins.str,
        instructions_documents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapability.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration: Specifies a structure that contains the details for a capability.
        :param name: The display name of the capability.
        :param type: Returns the type of the capability. Currently, only ``edi`` is supported.
        :param instructions_documents: Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.
        :param tags: Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e2c877d8f658a8bd5b2b87fa89276114a47d5d48d6051351c42b159c7c68d05)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCapabilityProps(
            configuration=configuration,
            name=name,
            type=type,
            instructions_documents=instructions_documents,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69250f68db11c0c5d1b5dc6e2fd42eb03c44b04345584670f06ca66a9283eb35)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7a0734db8cefbd4089ea9d0b9242a32f9ce5d439e96d8bf60ea3bf4754e3a55)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCapabilityArn")
    def attr_capability_arn(self) -> builtins.str:
        '''Returns an Amazon Resource Name (ARN) for a specific AWS resource, such as a capability, partnership, profile, or transformer.

        :cloudformationAttribute: CapabilityArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCapabilityArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCapabilityId")
    def attr_capability_id(self) -> builtins.str:
        '''Returns a system-assigned unique identifier for the capability.

        :cloudformationAttribute: CapabilityId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCapabilityId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Returns a timestamp for creation date and time of the capability.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''Returns a timestamp that identifies the most recent date and time that the capability was modified.

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

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
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCapability.CapabilityConfigurationProperty"]:
        '''Specifies a structure that contains the details for a capability.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCapability.CapabilityConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCapability.CapabilityConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e6a4e9debdcf2674a26e8ca0b9f4a771680d6f10a5d05a55ab8bc8c5063b78a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The display name of the capability.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__149152bfddb988a9aebbfe4cc00f98c6da302293c4bccdb6a2521efdcc265cad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''Returns the type of the capability.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0ac989543b8899d87e7022c05ecf79b8ac846fbb7cbefb25e6bf8a03d5b52da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="instructionsDocuments")
    def instructions_documents(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCapability.S3LocationProperty"]]]]:
        '''Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCapability.S3LocationProperty"]]]], jsii.get(self, "instructionsDocuments"))

    @instructions_documents.setter
    def instructions_documents(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCapability.S3LocationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__933e64c6fb43bdf92fe13796dc8381041bc9d46c8db437f72d8df9acf46d8ef9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instructionsDocuments", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9706dcfa23b620c2db12e1df4414f3a9f0b63bdbd7e3a8ac3944f66549703153)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnCapability.CapabilityConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"edi": "edi"},
    )
    class CapabilityConfigurationProperty:
        def __init__(
            self,
            *,
            edi: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapability.EdiConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A capability object.

            Currently, only EDI (electronic data interchange) capabilities are supported. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.

            :param edi: An EDI (electronic data interchange) configuration object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-capabilityconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                capability_configuration_property = b2bi.CfnCapability.CapabilityConfigurationProperty(
                    edi=b2bi.CfnCapability.EdiConfigurationProperty(
                        input_location=b2bi.CfnCapability.S3LocationProperty(
                            bucket_name="bucketName",
                            key="key"
                        ),
                        output_location=b2bi.CfnCapability.S3LocationProperty(
                            bucket_name="bucketName",
                            key="key"
                        ),
                        transformer_id="transformerId",
                        type=b2bi.CfnCapability.EdiTypeProperty(
                            x12_details=b2bi.CfnCapability.X12DetailsProperty(
                                transaction_set="transactionSet",
                                version="version"
                            )
                        ),
                
                        # the properties below are optional
                        capability_direction="capabilityDirection"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b39bfeb55ed086d5de5f443fd847773c175cdd988755a308ee0889c0b428322e)
                check_type(argname="argument edi", value=edi, expected_type=type_hints["edi"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "edi": edi,
            }

        @builtins.property
        def edi(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCapability.EdiConfigurationProperty"]:
            '''An EDI (electronic data interchange) configuration object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-capabilityconfiguration.html#cfn-b2bi-capability-capabilityconfiguration-edi
            '''
            result = self._values.get("edi")
            assert result is not None, "Required property 'edi' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCapability.EdiConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapabilityConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnCapability.EdiConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_location": "inputLocation",
            "output_location": "outputLocation",
            "transformer_id": "transformerId",
            "type": "type",
            "capability_direction": "capabilityDirection",
        },
    )
    class EdiConfigurationProperty:
        def __init__(
            self,
            *,
            input_location: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapability.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]],
            output_location: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapability.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]],
            transformer_id: builtins.str,
            type: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapability.EdiTypeProperty", typing.Dict[builtins.str, typing.Any]]],
            capability_direction: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the details for the EDI (electronic data interchange) transformation.

            :param input_location: Contains the Amazon S3 bucket and prefix for the location of the input file, which is contained in an ``S3Location`` object.
            :param output_location: Contains the Amazon S3 bucket and prefix for the location of the output file, which is contained in an ``S3Location`` object.
            :param transformer_id: Returns the system-assigned unique identifier for the transformer.
            :param type: Returns the type of the capability. Currently, only ``edi`` is supported.
            :param capability_direction: Specifies whether this is capability is for inbound or outbound transformations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-ediconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                edi_configuration_property = b2bi.CfnCapability.EdiConfigurationProperty(
                    input_location=b2bi.CfnCapability.S3LocationProperty(
                        bucket_name="bucketName",
                        key="key"
                    ),
                    output_location=b2bi.CfnCapability.S3LocationProperty(
                        bucket_name="bucketName",
                        key="key"
                    ),
                    transformer_id="transformerId",
                    type=b2bi.CfnCapability.EdiTypeProperty(
                        x12_details=b2bi.CfnCapability.X12DetailsProperty(
                            transaction_set="transactionSet",
                            version="version"
                        )
                    ),
                
                    # the properties below are optional
                    capability_direction="capabilityDirection"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6057bec99d8a1adeb15f82ebd6a5c206f528d80ccf6eaebcc8e44d83d415ec72)
                check_type(argname="argument input_location", value=input_location, expected_type=type_hints["input_location"])
                check_type(argname="argument output_location", value=output_location, expected_type=type_hints["output_location"])
                check_type(argname="argument transformer_id", value=transformer_id, expected_type=type_hints["transformer_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument capability_direction", value=capability_direction, expected_type=type_hints["capability_direction"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_location": input_location,
                "output_location": output_location,
                "transformer_id": transformer_id,
                "type": type,
            }
            if capability_direction is not None:
                self._values["capability_direction"] = capability_direction

        @builtins.property
        def input_location(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCapability.S3LocationProperty"]:
            '''Contains the Amazon S3 bucket and prefix for the location of the input file, which is contained in an ``S3Location`` object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-ediconfiguration.html#cfn-b2bi-capability-ediconfiguration-inputlocation
            '''
            result = self._values.get("input_location")
            assert result is not None, "Required property 'input_location' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCapability.S3LocationProperty"], result)

        @builtins.property
        def output_location(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCapability.S3LocationProperty"]:
            '''Contains the Amazon S3 bucket and prefix for the location of the output file, which is contained in an ``S3Location`` object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-ediconfiguration.html#cfn-b2bi-capability-ediconfiguration-outputlocation
            '''
            result = self._values.get("output_location")
            assert result is not None, "Required property 'output_location' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCapability.S3LocationProperty"], result)

        @builtins.property
        def transformer_id(self) -> builtins.str:
            '''Returns the system-assigned unique identifier for the transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-ediconfiguration.html#cfn-b2bi-capability-ediconfiguration-transformerid
            '''
            result = self._values.get("transformer_id")
            assert result is not None, "Required property 'transformer_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCapability.EdiTypeProperty"]:
            '''Returns the type of the capability.

            Currently, only ``edi`` is supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-ediconfiguration.html#cfn-b2bi-capability-ediconfiguration-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCapability.EdiTypeProperty"], result)

        @builtins.property
        def capability_direction(self) -> typing.Optional[builtins.str]:
            '''Specifies whether this is capability is for inbound or outbound transformations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-ediconfiguration.html#cfn-b2bi-capability-ediconfiguration-capabilitydirection
            '''
            result = self._values.get("capability_direction")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EdiConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnCapability.EdiTypeProperty",
        jsii_struct_bases=[],
        name_mapping={"x12_details": "x12Details"},
    )
    class EdiTypeProperty:
        def __init__(
            self,
            *,
            x12_details: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapability.X12DetailsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param x12_details: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-editype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                edi_type_property = b2bi.CfnCapability.EdiTypeProperty(
                    x12_details=b2bi.CfnCapability.X12DetailsProperty(
                        transaction_set="transactionSet",
                        version="version"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a9ca50562e4e831dbcf7fdb06d87922ec9144632d5572bc4430820884ab15edb)
                check_type(argname="argument x12_details", value=x12_details, expected_type=type_hints["x12_details"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "x12_details": x12_details,
            }

        @builtins.property
        def x12_details(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCapability.X12DetailsProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-editype.html#cfn-b2bi-capability-editype-x12details
            '''
            result = self._values.get("x12_details")
            assert result is not None, "Required property 'x12_details' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCapability.X12DetailsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EdiTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnCapability.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName", "key": "key"},
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket_name: typing.Optional[builtins.str] = None,
            key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the details for the Amazon S3 file location that is being used with AWS B2B Data Interchange.

            File locations in Amazon S3 are identified using a combination of the bucket and key.

            :param bucket_name: Specifies the name of the Amazon S3 bucket.
            :param key: Specifies the Amazon S3 key for the file location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                s3_location_property = b2bi.CfnCapability.S3LocationProperty(
                    bucket_name="bucketName",
                    key="key"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aca06398ec10ba74b5ba2cf86fa1032b9983a30858a85eb04ecadf48a95e5056)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket_name is not None:
                self._values["bucket_name"] = bucket_name
            if key is not None:
                self._values["key"] = key

        @builtins.property
        def bucket_name(self) -> typing.Optional[builtins.str]:
            '''Specifies the name of the Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-s3location.html#cfn-b2bi-capability-s3location-bucketname
            '''
            result = self._values.get("bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''Specifies the Amazon S3 key for the file location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-s3location.html#cfn-b2bi-capability-s3location-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnCapability.X12DetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"transaction_set": "transactionSet", "version": "version"},
    )
    class X12DetailsProperty:
        def __init__(
            self,
            *,
            transaction_set: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param transaction_set: Returns an enumerated type where each value identifies an X12 transaction set. Transaction sets are maintained by the X12 Accredited Standards Committee.
            :param version: Returns the version to use for the specified X12 transaction set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-x12details.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                x12_details_property = b2bi.CfnCapability.X12DetailsProperty(
                    transaction_set="transactionSet",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7a92fd26779dc45009be0b9ca0aefb7b988fae928b06b6b46f41995a7bd338e7)
                check_type(argname="argument transaction_set", value=transaction_set, expected_type=type_hints["transaction_set"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if transaction_set is not None:
                self._values["transaction_set"] = transaction_set
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def transaction_set(self) -> typing.Optional[builtins.str]:
            '''Returns an enumerated type where each value identifies an X12 transaction set.

            Transaction sets are maintained by the X12 Accredited Standards Committee.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-x12details.html#cfn-b2bi-capability-x12details-transactionset
            '''
            result = self._values.get("transaction_set")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''Returns the version to use for the specified X12 transaction set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-x12details.html#cfn-b2bi-capability-x12details-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "X12DetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_b2bi.CfnCapabilityProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "name": "name",
        "type": "type",
        "instructions_documents": "instructionsDocuments",
        "tags": "tags",
    },
)
class CfnCapabilityProps:
    def __init__(
        self,
        *,
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.CapabilityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        type: builtins.str,
        instructions_documents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCapability``.

        :param configuration: Specifies a structure that contains the details for a capability.
        :param name: The display name of the capability.
        :param type: Returns the type of the capability. Currently, only ``edi`` is supported.
        :param instructions_documents: Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.
        :param tags: Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-capability.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_b2bi as b2bi
            
            cfn_capability_props = b2bi.CfnCapabilityProps(
                configuration=b2bi.CfnCapability.CapabilityConfigurationProperty(
                    edi=b2bi.CfnCapability.EdiConfigurationProperty(
                        input_location=b2bi.CfnCapability.S3LocationProperty(
                            bucket_name="bucketName",
                            key="key"
                        ),
                        output_location=b2bi.CfnCapability.S3LocationProperty(
                            bucket_name="bucketName",
                            key="key"
                        ),
                        transformer_id="transformerId",
                        type=b2bi.CfnCapability.EdiTypeProperty(
                            x12_details=b2bi.CfnCapability.X12DetailsProperty(
                                transaction_set="transactionSet",
                                version="version"
                            )
                        ),
            
                        # the properties below are optional
                        capability_direction="capabilityDirection"
                    )
                ),
                name="name",
                type="type",
            
                # the properties below are optional
                instructions_documents=[b2bi.CfnCapability.S3LocationProperty(
                    bucket_name="bucketName",
                    key="key"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83b1800b6ac31ea75ae49999ff7054acf5205e3155bfc92964d45204eac123bb)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument instructions_documents", value=instructions_documents, expected_type=type_hints["instructions_documents"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration": configuration,
            "name": name,
            "type": type,
        }
        if instructions_documents is not None:
            self._values["instructions_documents"] = instructions_documents
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCapability.CapabilityConfigurationProperty]:
        '''Specifies a structure that contains the details for a capability.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-capability.html#cfn-b2bi-capability-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCapability.CapabilityConfigurationProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The display name of the capability.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-capability.html#cfn-b2bi-capability-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Returns the type of the capability.

        Currently, only ``edi`` is supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-capability.html#cfn-b2bi-capability-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instructions_documents(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCapability.S3LocationProperty]]]]:
        '''Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability.

        Each item contains the name of the bucket and the key, to identify the document's location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-capability.html#cfn-b2bi-capability-instructionsdocuments
        '''
        result = self._values.get("instructions_documents")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCapability.S3LocationProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type.

        You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-capability.html#cfn-b2bi-capability-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCapabilityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnPartnership(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnership",
):
    '''Creates a partnership between a customer and a trading partner, based on the supplied parameters.

    A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html
    :cloudformationResource: AWS::B2BI::Partnership
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_b2bi as b2bi
        
        cfn_partnership = b2bi.CfnPartnership(self, "MyCfnPartnership",
            capabilities=["capabilities"],
            email="email",
            name="name",
            profile_id="profileId",
        
            # the properties below are optional
            capability_options=b2bi.CfnPartnership.CapabilityOptionsProperty(
                inbound_edi=b2bi.CfnPartnership.InboundEdiOptionsProperty(
                    x12=b2bi.CfnPartnership.X12InboundEdiOptionsProperty(
                        acknowledgment_options=b2bi.CfnPartnership.X12AcknowledgmentOptionsProperty(
                            functional_acknowledgment="functionalAcknowledgment",
                            technical_acknowledgment="technicalAcknowledgment"
                        )
                    )
                ),
                outbound_edi=b2bi.CfnPartnership.OutboundEdiOptionsProperty(
                    x12=b2bi.CfnPartnership.X12EnvelopeProperty(
                        common=b2bi.CfnPartnership.X12OutboundEdiHeadersProperty(
                            control_numbers=b2bi.CfnPartnership.X12ControlNumbersProperty(
                                starting_functional_group_control_number=123,
                                starting_interchange_control_number=123,
                                starting_transaction_set_control_number=123
                            ),
                            delimiters=b2bi.CfnPartnership.X12DelimitersProperty(
                                component_separator="componentSeparator",
                                data_element_separator="dataElementSeparator",
                                segment_terminator="segmentTerminator"
                            ),
                            functional_group_headers=b2bi.CfnPartnership.X12FunctionalGroupHeadersProperty(
                                application_receiver_code="applicationReceiverCode",
                                application_sender_code="applicationSenderCode",
                                responsible_agency_code="responsibleAgencyCode"
                            ),
                            gs05_time_format="gs05TimeFormat",
                            interchange_control_headers=b2bi.CfnPartnership.X12InterchangeControlHeadersProperty(
                                acknowledgment_requested_code="acknowledgmentRequestedCode",
                                receiver_id="receiverId",
                                receiver_id_qualifier="receiverIdQualifier",
                                repetition_separator="repetitionSeparator",
                                sender_id="senderId",
                                sender_id_qualifier="senderIdQualifier",
                                usage_indicator_code="usageIndicatorCode"
                            ),
                            validate_edi=False
                        ),
                        wrap_options=b2bi.CfnPartnership.WrapOptionsProperty(
                            line_length=123,
                            line_terminator="lineTerminator",
                            wrap_by="wrapBy"
                        )
                    )
                )
            ),
            phone="phone",
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
        capabilities: typing.Sequence[builtins.str],
        email: builtins.str,
        name: builtins.str,
        profile_id: builtins.str,
        capability_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartnership.CapabilityOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        phone: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param capabilities: Returns one or more capabilities associated with this partnership.
        :param email: Specifies the email address associated with this trading partner.
        :param name: Returns the name of the partnership.
        :param profile_id: Returns the unique, system-generated identifier for the profile connected to this partnership.
        :param capability_options: Contains the details for an Outbound EDI capability.
        :param phone: Specifies the phone number associated with the partnership.
        :param tags: A key-value pair for a specific partnership. Tags are metadata that you can use to search for and group capabilities for various purposes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__187ce4b824b0d27162e457adfee9761451ebc9ba1fbb31b215de741e20aea463)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPartnershipProps(
            capabilities=capabilities,
            email=email,
            name=name,
            profile_id=profile_id,
            capability_options=capability_options,
            phone=phone,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d250a045aef9262deb5ac9bdfc02b08a37a777ba8e105b1406ebfad2ee8edc9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__97e66f59482a5e62e1d52e1f96109cae79dc6c60b4b84b9ac971718f61abed32)
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
        '''Returns a timestamp for creation date and time of the partnership.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''Returns a timestamp that identifies the most recent date and time that the partnership was modified.

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrPartnershipArn")
    def attr_partnership_arn(self) -> builtins.str:
        '''Returns an Amazon Resource Name (ARN) for a specific AWS resource, such as a capability, partnership, profile, or transformer.

        :cloudformationAttribute: PartnershipArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPartnershipArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPartnershipId")
    def attr_partnership_id(self) -> builtins.str:
        '''Returns the unique, system-generated identifier for a partnership.

        :cloudformationAttribute: PartnershipId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPartnershipId"))

    @builtins.property
    @jsii.member(jsii_name="attrTradingPartnerId")
    def attr_trading_partner_id(self) -> builtins.str:
        '''Returns the unique, system-generated identifier for a trading partner.

        :cloudformationAttribute: TradingPartnerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTradingPartnerId"))

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
    @jsii.member(jsii_name="capabilities")
    def capabilities(self) -> typing.List[builtins.str]:
        '''Returns one or more capabilities associated with this partnership.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "capabilities"))

    @capabilities.setter
    def capabilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0980f94d13e92ad52bd4f6a10906045804439d25bf3126b627f3a97eb79eb594)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capabilities", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        '''Specifies the email address associated with this trading partner.'''
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2873a98dfd303be4e91fec1a674c6ab1a7382e5563610406e047403b795f1a06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Returns the name of the partnership.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2391403bfc3a496d7ff98fb633ece3257a09478e6bed5d4c1c2ec23cd35687c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="profileId")
    def profile_id(self) -> builtins.str:
        '''Returns the unique, system-generated identifier for the profile connected to this partnership.'''
        return typing.cast(builtins.str, jsii.get(self, "profileId"))

    @profile_id.setter
    def profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__126b2c043f2647e2a052eca52ec8432ea60287721a3e645fe4dd65583feb42de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="capabilityOptions")
    def capability_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.CapabilityOptionsProperty"]]:
        '''Contains the details for an Outbound EDI capability.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.CapabilityOptionsProperty"]], jsii.get(self, "capabilityOptions"))

    @capability_options.setter
    def capability_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.CapabilityOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d35bf90164602b28a7873c9bbcf2cebf61f26952d369e2a905926b650b1a22e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capabilityOptions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="phone")
    def phone(self) -> typing.Optional[builtins.str]:
        '''Specifies the phone number associated with the partnership.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phone"))

    @phone.setter
    def phone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5555f48f20bc825c44c857244fae3207c272ec76cbe060a463105d2c86113010)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phone", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key-value pair for a specific partnership.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc0c0a6e8431d11899a318046b450bc4efc00486d9f20286940067c7fa335411)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnership.CapabilityOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"inbound_edi": "inboundEdi", "outbound_edi": "outboundEdi"},
    )
    class CapabilityOptionsProperty:
        def __init__(
            self,
            *,
            inbound_edi: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartnership.InboundEdiOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            outbound_edi: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartnership.OutboundEdiOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains the details for an Outbound EDI capability.

            :param inbound_edi: A structure that contains the inbound EDI options for the capability.
            :param outbound_edi: A structure that contains the outbound EDI options.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-capabilityoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                capability_options_property = b2bi.CfnPartnership.CapabilityOptionsProperty(
                    inbound_edi=b2bi.CfnPartnership.InboundEdiOptionsProperty(
                        x12=b2bi.CfnPartnership.X12InboundEdiOptionsProperty(
                            acknowledgment_options=b2bi.CfnPartnership.X12AcknowledgmentOptionsProperty(
                                functional_acknowledgment="functionalAcknowledgment",
                                technical_acknowledgment="technicalAcknowledgment"
                            )
                        )
                    ),
                    outbound_edi=b2bi.CfnPartnership.OutboundEdiOptionsProperty(
                        x12=b2bi.CfnPartnership.X12EnvelopeProperty(
                            common=b2bi.CfnPartnership.X12OutboundEdiHeadersProperty(
                                control_numbers=b2bi.CfnPartnership.X12ControlNumbersProperty(
                                    starting_functional_group_control_number=123,
                                    starting_interchange_control_number=123,
                                    starting_transaction_set_control_number=123
                                ),
                                delimiters=b2bi.CfnPartnership.X12DelimitersProperty(
                                    component_separator="componentSeparator",
                                    data_element_separator="dataElementSeparator",
                                    segment_terminator="segmentTerminator"
                                ),
                                functional_group_headers=b2bi.CfnPartnership.X12FunctionalGroupHeadersProperty(
                                    application_receiver_code="applicationReceiverCode",
                                    application_sender_code="applicationSenderCode",
                                    responsible_agency_code="responsibleAgencyCode"
                                ),
                                gs05_time_format="gs05TimeFormat",
                                interchange_control_headers=b2bi.CfnPartnership.X12InterchangeControlHeadersProperty(
                                    acknowledgment_requested_code="acknowledgmentRequestedCode",
                                    receiver_id="receiverId",
                                    receiver_id_qualifier="receiverIdQualifier",
                                    repetition_separator="repetitionSeparator",
                                    sender_id="senderId",
                                    sender_id_qualifier="senderIdQualifier",
                                    usage_indicator_code="usageIndicatorCode"
                                ),
                                validate_edi=False
                            ),
                            wrap_options=b2bi.CfnPartnership.WrapOptionsProperty(
                                line_length=123,
                                line_terminator="lineTerminator",
                                wrap_by="wrapBy"
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__489c8d62d1ea0d603790b535b3f02b6d30eee2c7a02cd1b1d2a497a7f9f54c2b)
                check_type(argname="argument inbound_edi", value=inbound_edi, expected_type=type_hints["inbound_edi"])
                check_type(argname="argument outbound_edi", value=outbound_edi, expected_type=type_hints["outbound_edi"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if inbound_edi is not None:
                self._values["inbound_edi"] = inbound_edi
            if outbound_edi is not None:
                self._values["outbound_edi"] = outbound_edi

        @builtins.property
        def inbound_edi(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.InboundEdiOptionsProperty"]]:
            '''A structure that contains the inbound EDI options for the capability.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-capabilityoptions.html#cfn-b2bi-partnership-capabilityoptions-inboundedi
            '''
            result = self._values.get("inbound_edi")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.InboundEdiOptionsProperty"]], result)

        @builtins.property
        def outbound_edi(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.OutboundEdiOptionsProperty"]]:
            '''A structure that contains the outbound EDI options.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-capabilityoptions.html#cfn-b2bi-partnership-capabilityoptions-outboundedi
            '''
            result = self._values.get("outbound_edi")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.OutboundEdiOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapabilityOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnership.InboundEdiOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"x12": "x12"},
    )
    class InboundEdiOptionsProperty:
        def __init__(
            self,
            *,
            x12: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartnership.X12InboundEdiOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains options for processing inbound EDI files.

            These options allow for customizing how incoming EDI documents are processed.

            :param x12: A structure that contains X12-specific options for processing inbound X12 EDI files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-inboundedioptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                inbound_edi_options_property = b2bi.CfnPartnership.InboundEdiOptionsProperty(
                    x12=b2bi.CfnPartnership.X12InboundEdiOptionsProperty(
                        acknowledgment_options=b2bi.CfnPartnership.X12AcknowledgmentOptionsProperty(
                            functional_acknowledgment="functionalAcknowledgment",
                            technical_acknowledgment="technicalAcknowledgment"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b6c324487b61389216d4c37a2c38661a9fd27a782f0b1d30b4da2197c02472ca)
                check_type(argname="argument x12", value=x12, expected_type=type_hints["x12"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if x12 is not None:
                self._values["x12"] = x12

        @builtins.property
        def x12(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12InboundEdiOptionsProperty"]]:
            '''A structure that contains X12-specific options for processing inbound X12 EDI files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-inboundedioptions.html#cfn-b2bi-partnership-inboundedioptions-x12
            '''
            result = self._values.get("x12")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12InboundEdiOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InboundEdiOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnership.OutboundEdiOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"x12": "x12"},
    )
    class OutboundEdiOptionsProperty:
        def __init__(
            self,
            *,
            x12: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartnership.X12EnvelopeProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A container for outbound EDI options.

            :param x12: A structure that contains an X12 envelope structure.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-outboundedioptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                outbound_edi_options_property = b2bi.CfnPartnership.OutboundEdiOptionsProperty(
                    x12=b2bi.CfnPartnership.X12EnvelopeProperty(
                        common=b2bi.CfnPartnership.X12OutboundEdiHeadersProperty(
                            control_numbers=b2bi.CfnPartnership.X12ControlNumbersProperty(
                                starting_functional_group_control_number=123,
                                starting_interchange_control_number=123,
                                starting_transaction_set_control_number=123
                            ),
                            delimiters=b2bi.CfnPartnership.X12DelimitersProperty(
                                component_separator="componentSeparator",
                                data_element_separator="dataElementSeparator",
                                segment_terminator="segmentTerminator"
                            ),
                            functional_group_headers=b2bi.CfnPartnership.X12FunctionalGroupHeadersProperty(
                                application_receiver_code="applicationReceiverCode",
                                application_sender_code="applicationSenderCode",
                                responsible_agency_code="responsibleAgencyCode"
                            ),
                            gs05_time_format="gs05TimeFormat",
                            interchange_control_headers=b2bi.CfnPartnership.X12InterchangeControlHeadersProperty(
                                acknowledgment_requested_code="acknowledgmentRequestedCode",
                                receiver_id="receiverId",
                                receiver_id_qualifier="receiverIdQualifier",
                                repetition_separator="repetitionSeparator",
                                sender_id="senderId",
                                sender_id_qualifier="senderIdQualifier",
                                usage_indicator_code="usageIndicatorCode"
                            ),
                            validate_edi=False
                        ),
                        wrap_options=b2bi.CfnPartnership.WrapOptionsProperty(
                            line_length=123,
                            line_terminator="lineTerminator",
                            wrap_by="wrapBy"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__32687b2a777cf504a9e11c6386b8aa7795645f807660aecf3f5bdddf1b953268)
                check_type(argname="argument x12", value=x12, expected_type=type_hints["x12"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "x12": x12,
            }

        @builtins.property
        def x12(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12EnvelopeProperty"]:
            '''A structure that contains an X12 envelope structure.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-outboundedioptions.html#cfn-b2bi-partnership-outboundedioptions-x12
            '''
            result = self._values.get("x12")
            assert result is not None, "Required property 'x12' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12EnvelopeProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutboundEdiOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnership.WrapOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "line_length": "lineLength",
            "line_terminator": "lineTerminator",
            "wrap_by": "wrapBy",
        },
    )
    class WrapOptionsProperty:
        def __init__(
            self,
            *,
            line_length: typing.Optional[jsii.Number] = None,
            line_terminator: typing.Optional[builtins.str] = None,
            wrap_by: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param line_length: 
            :param line_terminator: 
            :param wrap_by: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-wrapoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                wrap_options_property = b2bi.CfnPartnership.WrapOptionsProperty(
                    line_length=123,
                    line_terminator="lineTerminator",
                    wrap_by="wrapBy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e655ba69d2815891585dad9698c9aca0d8f46825094f69219bf726ac7cc3dfb3)
                check_type(argname="argument line_length", value=line_length, expected_type=type_hints["line_length"])
                check_type(argname="argument line_terminator", value=line_terminator, expected_type=type_hints["line_terminator"])
                check_type(argname="argument wrap_by", value=wrap_by, expected_type=type_hints["wrap_by"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if line_length is not None:
                self._values["line_length"] = line_length
            if line_terminator is not None:
                self._values["line_terminator"] = line_terminator
            if wrap_by is not None:
                self._values["wrap_by"] = wrap_by

        @builtins.property
        def line_length(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-wrapoptions.html#cfn-b2bi-partnership-wrapoptions-linelength
            '''
            result = self._values.get("line_length")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def line_terminator(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-wrapoptions.html#cfn-b2bi-partnership-wrapoptions-lineterminator
            '''
            result = self._values.get("line_terminator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def wrap_by(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-wrapoptions.html#cfn-b2bi-partnership-wrapoptions-wrapby
            '''
            result = self._values.get("wrap_by")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WrapOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnership.X12AcknowledgmentOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "functional_acknowledgment": "functionalAcknowledgment",
            "technical_acknowledgment": "technicalAcknowledgment",
        },
    )
    class X12AcknowledgmentOptionsProperty:
        def __init__(
            self,
            *,
            functional_acknowledgment: builtins.str,
            technical_acknowledgment: builtins.str,
        ) -> None:
            '''
            :param functional_acknowledgment: 
            :param technical_acknowledgment: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12acknowledgmentoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                x12_acknowledgment_options_property = b2bi.CfnPartnership.X12AcknowledgmentOptionsProperty(
                    functional_acknowledgment="functionalAcknowledgment",
                    technical_acknowledgment="technicalAcknowledgment"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cd25022ffe4e73fd8bbd9369b880ae7c91c4a3b0583614cce2974320e88eaa3a)
                check_type(argname="argument functional_acknowledgment", value=functional_acknowledgment, expected_type=type_hints["functional_acknowledgment"])
                check_type(argname="argument technical_acknowledgment", value=technical_acknowledgment, expected_type=type_hints["technical_acknowledgment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "functional_acknowledgment": functional_acknowledgment,
                "technical_acknowledgment": technical_acknowledgment,
            }

        @builtins.property
        def functional_acknowledgment(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12acknowledgmentoptions.html#cfn-b2bi-partnership-x12acknowledgmentoptions-functionalacknowledgment
            '''
            result = self._values.get("functional_acknowledgment")
            assert result is not None, "Required property 'functional_acknowledgment' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def technical_acknowledgment(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12acknowledgmentoptions.html#cfn-b2bi-partnership-x12acknowledgmentoptions-technicalacknowledgment
            '''
            result = self._values.get("technical_acknowledgment")
            assert result is not None, "Required property 'technical_acknowledgment' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "X12AcknowledgmentOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnership.X12ControlNumbersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "starting_functional_group_control_number": "startingFunctionalGroupControlNumber",
            "starting_interchange_control_number": "startingInterchangeControlNumber",
            "starting_transaction_set_control_number": "startingTransactionSetControlNumber",
        },
    )
    class X12ControlNumbersProperty:
        def __init__(
            self,
            *,
            starting_functional_group_control_number: typing.Optional[jsii.Number] = None,
            starting_interchange_control_number: typing.Optional[jsii.Number] = None,
            starting_transaction_set_control_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param starting_functional_group_control_number: 
            :param starting_interchange_control_number: 
            :param starting_transaction_set_control_number: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12controlnumbers.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                x12_control_numbers_property = b2bi.CfnPartnership.X12ControlNumbersProperty(
                    starting_functional_group_control_number=123,
                    starting_interchange_control_number=123,
                    starting_transaction_set_control_number=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__30e0c21f8439a660cced0c707b2b1ab5d0199f9710dc5113cb9fcde22546bef9)
                check_type(argname="argument starting_functional_group_control_number", value=starting_functional_group_control_number, expected_type=type_hints["starting_functional_group_control_number"])
                check_type(argname="argument starting_interchange_control_number", value=starting_interchange_control_number, expected_type=type_hints["starting_interchange_control_number"])
                check_type(argname="argument starting_transaction_set_control_number", value=starting_transaction_set_control_number, expected_type=type_hints["starting_transaction_set_control_number"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if starting_functional_group_control_number is not None:
                self._values["starting_functional_group_control_number"] = starting_functional_group_control_number
            if starting_interchange_control_number is not None:
                self._values["starting_interchange_control_number"] = starting_interchange_control_number
            if starting_transaction_set_control_number is not None:
                self._values["starting_transaction_set_control_number"] = starting_transaction_set_control_number

        @builtins.property
        def starting_functional_group_control_number(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12controlnumbers.html#cfn-b2bi-partnership-x12controlnumbers-startingfunctionalgroupcontrolnumber
            '''
            result = self._values.get("starting_functional_group_control_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def starting_interchange_control_number(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12controlnumbers.html#cfn-b2bi-partnership-x12controlnumbers-startinginterchangecontrolnumber
            '''
            result = self._values.get("starting_interchange_control_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def starting_transaction_set_control_number(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12controlnumbers.html#cfn-b2bi-partnership-x12controlnumbers-startingtransactionsetcontrolnumber
            '''
            result = self._values.get("starting_transaction_set_control_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "X12ControlNumbersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnership.X12DelimitersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "component_separator": "componentSeparator",
            "data_element_separator": "dataElementSeparator",
            "segment_terminator": "segmentTerminator",
        },
    )
    class X12DelimitersProperty:
        def __init__(
            self,
            *,
            component_separator: typing.Optional[builtins.str] = None,
            data_element_separator: typing.Optional[builtins.str] = None,
            segment_terminator: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param component_separator: 
            :param data_element_separator: 
            :param segment_terminator: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12delimiters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                x12_delimiters_property = b2bi.CfnPartnership.X12DelimitersProperty(
                    component_separator="componentSeparator",
                    data_element_separator="dataElementSeparator",
                    segment_terminator="segmentTerminator"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1c64e6cc29ab2abf7a0ebb687d8309174a673c2096776d261df47c9bb5f6044b)
                check_type(argname="argument component_separator", value=component_separator, expected_type=type_hints["component_separator"])
                check_type(argname="argument data_element_separator", value=data_element_separator, expected_type=type_hints["data_element_separator"])
                check_type(argname="argument segment_terminator", value=segment_terminator, expected_type=type_hints["segment_terminator"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if component_separator is not None:
                self._values["component_separator"] = component_separator
            if data_element_separator is not None:
                self._values["data_element_separator"] = data_element_separator
            if segment_terminator is not None:
                self._values["segment_terminator"] = segment_terminator

        @builtins.property
        def component_separator(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12delimiters.html#cfn-b2bi-partnership-x12delimiters-componentseparator
            '''
            result = self._values.get("component_separator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_element_separator(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12delimiters.html#cfn-b2bi-partnership-x12delimiters-dataelementseparator
            '''
            result = self._values.get("data_element_separator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def segment_terminator(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12delimiters.html#cfn-b2bi-partnership-x12delimiters-segmentterminator
            '''
            result = self._values.get("segment_terminator")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "X12DelimitersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnership.X12EnvelopeProperty",
        jsii_struct_bases=[],
        name_mapping={"common": "common", "wrap_options": "wrapOptions"},
    )
    class X12EnvelopeProperty:
        def __init__(
            self,
            *,
            common: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartnership.X12OutboundEdiHeadersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            wrap_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartnership.WrapOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A wrapper structure for an X12 definition object.

            the X12 envelope ensures the integrity of the data and the efficiency of the information exchange. The X12 message structure has hierarchical levels. From highest to the lowest, they are:

            - Interchange Envelope
            - Functional Group
            - Transaction Set

            :param common: A container for the X12 outbound EDI headers.
            :param wrap_options: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12envelope.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                x12_envelope_property = b2bi.CfnPartnership.X12EnvelopeProperty(
                    common=b2bi.CfnPartnership.X12OutboundEdiHeadersProperty(
                        control_numbers=b2bi.CfnPartnership.X12ControlNumbersProperty(
                            starting_functional_group_control_number=123,
                            starting_interchange_control_number=123,
                            starting_transaction_set_control_number=123
                        ),
                        delimiters=b2bi.CfnPartnership.X12DelimitersProperty(
                            component_separator="componentSeparator",
                            data_element_separator="dataElementSeparator",
                            segment_terminator="segmentTerminator"
                        ),
                        functional_group_headers=b2bi.CfnPartnership.X12FunctionalGroupHeadersProperty(
                            application_receiver_code="applicationReceiverCode",
                            application_sender_code="applicationSenderCode",
                            responsible_agency_code="responsibleAgencyCode"
                        ),
                        gs05_time_format="gs05TimeFormat",
                        interchange_control_headers=b2bi.CfnPartnership.X12InterchangeControlHeadersProperty(
                            acknowledgment_requested_code="acknowledgmentRequestedCode",
                            receiver_id="receiverId",
                            receiver_id_qualifier="receiverIdQualifier",
                            repetition_separator="repetitionSeparator",
                            sender_id="senderId",
                            sender_id_qualifier="senderIdQualifier",
                            usage_indicator_code="usageIndicatorCode"
                        ),
                        validate_edi=False
                    ),
                    wrap_options=b2bi.CfnPartnership.WrapOptionsProperty(
                        line_length=123,
                        line_terminator="lineTerminator",
                        wrap_by="wrapBy"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__30e9a528379ffdff1b0693f52a617de66a178b919d5d3ddc1c68309cc0a86afc)
                check_type(argname="argument common", value=common, expected_type=type_hints["common"])
                check_type(argname="argument wrap_options", value=wrap_options, expected_type=type_hints["wrap_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if common is not None:
                self._values["common"] = common
            if wrap_options is not None:
                self._values["wrap_options"] = wrap_options

        @builtins.property
        def common(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12OutboundEdiHeadersProperty"]]:
            '''A container for the X12 outbound EDI headers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12envelope.html#cfn-b2bi-partnership-x12envelope-common
            '''
            result = self._values.get("common")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12OutboundEdiHeadersProperty"]], result)

        @builtins.property
        def wrap_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.WrapOptionsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12envelope.html#cfn-b2bi-partnership-x12envelope-wrapoptions
            '''
            result = self._values.get("wrap_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.WrapOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "X12EnvelopeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnership.X12FunctionalGroupHeadersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_receiver_code": "applicationReceiverCode",
            "application_sender_code": "applicationSenderCode",
            "responsible_agency_code": "responsibleAgencyCode",
        },
    )
    class X12FunctionalGroupHeadersProperty:
        def __init__(
            self,
            *,
            application_receiver_code: typing.Optional[builtins.str] = None,
            application_sender_code: typing.Optional[builtins.str] = None,
            responsible_agency_code: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param application_receiver_code: 
            :param application_sender_code: 
            :param responsible_agency_code: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12functionalgroupheaders.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                x12_functional_group_headers_property = b2bi.CfnPartnership.X12FunctionalGroupHeadersProperty(
                    application_receiver_code="applicationReceiverCode",
                    application_sender_code="applicationSenderCode",
                    responsible_agency_code="responsibleAgencyCode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b107041a5b51efd672a9b2f3b5bb8ce2f8376a1dc4cddc6a58a089e0fc49b53)
                check_type(argname="argument application_receiver_code", value=application_receiver_code, expected_type=type_hints["application_receiver_code"])
                check_type(argname="argument application_sender_code", value=application_sender_code, expected_type=type_hints["application_sender_code"])
                check_type(argname="argument responsible_agency_code", value=responsible_agency_code, expected_type=type_hints["responsible_agency_code"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if application_receiver_code is not None:
                self._values["application_receiver_code"] = application_receiver_code
            if application_sender_code is not None:
                self._values["application_sender_code"] = application_sender_code
            if responsible_agency_code is not None:
                self._values["responsible_agency_code"] = responsible_agency_code

        @builtins.property
        def application_receiver_code(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12functionalgroupheaders.html#cfn-b2bi-partnership-x12functionalgroupheaders-applicationreceivercode
            '''
            result = self._values.get("application_receiver_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def application_sender_code(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12functionalgroupheaders.html#cfn-b2bi-partnership-x12functionalgroupheaders-applicationsendercode
            '''
            result = self._values.get("application_sender_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def responsible_agency_code(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12functionalgroupheaders.html#cfn-b2bi-partnership-x12functionalgroupheaders-responsibleagencycode
            '''
            result = self._values.get("responsible_agency_code")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "X12FunctionalGroupHeadersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnership.X12InboundEdiOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"acknowledgment_options": "acknowledgmentOptions"},
    )
    class X12InboundEdiOptionsProperty:
        def __init__(
            self,
            *,
            acknowledgment_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartnership.X12AcknowledgmentOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains options specific to processing inbound X12 EDI files.

            :param acknowledgment_options: Specifies acknowledgment options for inbound X12 EDI files. These options control how functional and technical acknowledgments are handled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12inboundedioptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                x12_inbound_edi_options_property = b2bi.CfnPartnership.X12InboundEdiOptionsProperty(
                    acknowledgment_options=b2bi.CfnPartnership.X12AcknowledgmentOptionsProperty(
                        functional_acknowledgment="functionalAcknowledgment",
                        technical_acknowledgment="technicalAcknowledgment"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__25951703b6b17888b8fded1f4b04ca4482b7f065fc950fd49d36619cde5b1ad6)
                check_type(argname="argument acknowledgment_options", value=acknowledgment_options, expected_type=type_hints["acknowledgment_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if acknowledgment_options is not None:
                self._values["acknowledgment_options"] = acknowledgment_options

        @builtins.property
        def acknowledgment_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12AcknowledgmentOptionsProperty"]]:
            '''Specifies acknowledgment options for inbound X12 EDI files.

            These options control how functional and technical acknowledgments are handled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12inboundedioptions.html#cfn-b2bi-partnership-x12inboundedioptions-acknowledgmentoptions
            '''
            result = self._values.get("acknowledgment_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12AcknowledgmentOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "X12InboundEdiOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnership.X12InterchangeControlHeadersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "acknowledgment_requested_code": "acknowledgmentRequestedCode",
            "receiver_id": "receiverId",
            "receiver_id_qualifier": "receiverIdQualifier",
            "repetition_separator": "repetitionSeparator",
            "sender_id": "senderId",
            "sender_id_qualifier": "senderIdQualifier",
            "usage_indicator_code": "usageIndicatorCode",
        },
    )
    class X12InterchangeControlHeadersProperty:
        def __init__(
            self,
            *,
            acknowledgment_requested_code: typing.Optional[builtins.str] = None,
            receiver_id: typing.Optional[builtins.str] = None,
            receiver_id_qualifier: typing.Optional[builtins.str] = None,
            repetition_separator: typing.Optional[builtins.str] = None,
            sender_id: typing.Optional[builtins.str] = None,
            sender_id_qualifier: typing.Optional[builtins.str] = None,
            usage_indicator_code: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param acknowledgment_requested_code: 
            :param receiver_id: 
            :param receiver_id_qualifier: 
            :param repetition_separator: 
            :param sender_id: 
            :param sender_id_qualifier: 
            :param usage_indicator_code: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12interchangecontrolheaders.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                x12_interchange_control_headers_property = b2bi.CfnPartnership.X12InterchangeControlHeadersProperty(
                    acknowledgment_requested_code="acknowledgmentRequestedCode",
                    receiver_id="receiverId",
                    receiver_id_qualifier="receiverIdQualifier",
                    repetition_separator="repetitionSeparator",
                    sender_id="senderId",
                    sender_id_qualifier="senderIdQualifier",
                    usage_indicator_code="usageIndicatorCode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2cd06c107bbc9de62cfdd484dd7527f5641c4d03e973675f4638b3441dcb2630)
                check_type(argname="argument acknowledgment_requested_code", value=acknowledgment_requested_code, expected_type=type_hints["acknowledgment_requested_code"])
                check_type(argname="argument receiver_id", value=receiver_id, expected_type=type_hints["receiver_id"])
                check_type(argname="argument receiver_id_qualifier", value=receiver_id_qualifier, expected_type=type_hints["receiver_id_qualifier"])
                check_type(argname="argument repetition_separator", value=repetition_separator, expected_type=type_hints["repetition_separator"])
                check_type(argname="argument sender_id", value=sender_id, expected_type=type_hints["sender_id"])
                check_type(argname="argument sender_id_qualifier", value=sender_id_qualifier, expected_type=type_hints["sender_id_qualifier"])
                check_type(argname="argument usage_indicator_code", value=usage_indicator_code, expected_type=type_hints["usage_indicator_code"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if acknowledgment_requested_code is not None:
                self._values["acknowledgment_requested_code"] = acknowledgment_requested_code
            if receiver_id is not None:
                self._values["receiver_id"] = receiver_id
            if receiver_id_qualifier is not None:
                self._values["receiver_id_qualifier"] = receiver_id_qualifier
            if repetition_separator is not None:
                self._values["repetition_separator"] = repetition_separator
            if sender_id is not None:
                self._values["sender_id"] = sender_id
            if sender_id_qualifier is not None:
                self._values["sender_id_qualifier"] = sender_id_qualifier
            if usage_indicator_code is not None:
                self._values["usage_indicator_code"] = usage_indicator_code

        @builtins.property
        def acknowledgment_requested_code(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12interchangecontrolheaders.html#cfn-b2bi-partnership-x12interchangecontrolheaders-acknowledgmentrequestedcode
            '''
            result = self._values.get("acknowledgment_requested_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def receiver_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12interchangecontrolheaders.html#cfn-b2bi-partnership-x12interchangecontrolheaders-receiverid
            '''
            result = self._values.get("receiver_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def receiver_id_qualifier(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12interchangecontrolheaders.html#cfn-b2bi-partnership-x12interchangecontrolheaders-receiveridqualifier
            '''
            result = self._values.get("receiver_id_qualifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def repetition_separator(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12interchangecontrolheaders.html#cfn-b2bi-partnership-x12interchangecontrolheaders-repetitionseparator
            '''
            result = self._values.get("repetition_separator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sender_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12interchangecontrolheaders.html#cfn-b2bi-partnership-x12interchangecontrolheaders-senderid
            '''
            result = self._values.get("sender_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sender_id_qualifier(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12interchangecontrolheaders.html#cfn-b2bi-partnership-x12interchangecontrolheaders-senderidqualifier
            '''
            result = self._values.get("sender_id_qualifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def usage_indicator_code(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12interchangecontrolheaders.html#cfn-b2bi-partnership-x12interchangecontrolheaders-usageindicatorcode
            '''
            result = self._values.get("usage_indicator_code")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "X12InterchangeControlHeadersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnership.X12OutboundEdiHeadersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "control_numbers": "controlNumbers",
            "delimiters": "delimiters",
            "functional_group_headers": "functionalGroupHeaders",
            "gs05_time_format": "gs05TimeFormat",
            "interchange_control_headers": "interchangeControlHeaders",
            "validate_edi": "validateEdi",
        },
    )
    class X12OutboundEdiHeadersProperty:
        def __init__(
            self,
            *,
            control_numbers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartnership.X12ControlNumbersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            delimiters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartnership.X12DelimitersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            functional_group_headers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartnership.X12FunctionalGroupHeadersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            gs05_time_format: typing.Optional[builtins.str] = None,
            interchange_control_headers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPartnership.X12InterchangeControlHeadersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            validate_edi: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''A structure containing the details for an outbound EDI object.

            :param control_numbers: Specifies control number configuration for outbound X12 EDI headers. These settings determine the starting values for interchange, functional group, and transaction set control numbers.
            :param delimiters: The delimiters, for example semicolon ( ``;`` ), that separates sections of the headers for the X12 object.
            :param functional_group_headers: The functional group headers for the X12 object.
            :param gs05_time_format: 
            :param interchange_control_headers: In X12 EDI messages, delimiters are used to mark the end of segments or elements, and are defined in the interchange control header.
            :param validate_edi: Specifies whether or not to validate the EDI for this X12 object: ``TRUE`` or ``FALSE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12outboundediheaders.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                x12_outbound_edi_headers_property = b2bi.CfnPartnership.X12OutboundEdiHeadersProperty(
                    control_numbers=b2bi.CfnPartnership.X12ControlNumbersProperty(
                        starting_functional_group_control_number=123,
                        starting_interchange_control_number=123,
                        starting_transaction_set_control_number=123
                    ),
                    delimiters=b2bi.CfnPartnership.X12DelimitersProperty(
                        component_separator="componentSeparator",
                        data_element_separator="dataElementSeparator",
                        segment_terminator="segmentTerminator"
                    ),
                    functional_group_headers=b2bi.CfnPartnership.X12FunctionalGroupHeadersProperty(
                        application_receiver_code="applicationReceiverCode",
                        application_sender_code="applicationSenderCode",
                        responsible_agency_code="responsibleAgencyCode"
                    ),
                    gs05_time_format="gs05TimeFormat",
                    interchange_control_headers=b2bi.CfnPartnership.X12InterchangeControlHeadersProperty(
                        acknowledgment_requested_code="acknowledgmentRequestedCode",
                        receiver_id="receiverId",
                        receiver_id_qualifier="receiverIdQualifier",
                        repetition_separator="repetitionSeparator",
                        sender_id="senderId",
                        sender_id_qualifier="senderIdQualifier",
                        usage_indicator_code="usageIndicatorCode"
                    ),
                    validate_edi=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8e80431a1b65f39f118b4a0b397a523502dcc49a5197848bd82eff40dc153d1c)
                check_type(argname="argument control_numbers", value=control_numbers, expected_type=type_hints["control_numbers"])
                check_type(argname="argument delimiters", value=delimiters, expected_type=type_hints["delimiters"])
                check_type(argname="argument functional_group_headers", value=functional_group_headers, expected_type=type_hints["functional_group_headers"])
                check_type(argname="argument gs05_time_format", value=gs05_time_format, expected_type=type_hints["gs05_time_format"])
                check_type(argname="argument interchange_control_headers", value=interchange_control_headers, expected_type=type_hints["interchange_control_headers"])
                check_type(argname="argument validate_edi", value=validate_edi, expected_type=type_hints["validate_edi"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if control_numbers is not None:
                self._values["control_numbers"] = control_numbers
            if delimiters is not None:
                self._values["delimiters"] = delimiters
            if functional_group_headers is not None:
                self._values["functional_group_headers"] = functional_group_headers
            if gs05_time_format is not None:
                self._values["gs05_time_format"] = gs05_time_format
            if interchange_control_headers is not None:
                self._values["interchange_control_headers"] = interchange_control_headers
            if validate_edi is not None:
                self._values["validate_edi"] = validate_edi

        @builtins.property
        def control_numbers(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12ControlNumbersProperty"]]:
            '''Specifies control number configuration for outbound X12 EDI headers.

            These settings determine the starting values for interchange, functional group, and transaction set control numbers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12outboundediheaders.html#cfn-b2bi-partnership-x12outboundediheaders-controlnumbers
            '''
            result = self._values.get("control_numbers")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12ControlNumbersProperty"]], result)

        @builtins.property
        def delimiters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12DelimitersProperty"]]:
            '''The delimiters, for example semicolon ( ``;`` ), that separates sections of the headers for the X12 object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12outboundediheaders.html#cfn-b2bi-partnership-x12outboundediheaders-delimiters
            '''
            result = self._values.get("delimiters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12DelimitersProperty"]], result)

        @builtins.property
        def functional_group_headers(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12FunctionalGroupHeadersProperty"]]:
            '''The functional group headers for the X12 object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12outboundediheaders.html#cfn-b2bi-partnership-x12outboundediheaders-functionalgroupheaders
            '''
            result = self._values.get("functional_group_headers")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12FunctionalGroupHeadersProperty"]], result)

        @builtins.property
        def gs05_time_format(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12outboundediheaders.html#cfn-b2bi-partnership-x12outboundediheaders-gs05timeformat
            '''
            result = self._values.get("gs05_time_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def interchange_control_headers(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12InterchangeControlHeadersProperty"]]:
            '''In X12 EDI messages, delimiters are used to mark the end of segments or elements, and are defined in the interchange control header.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12outboundediheaders.html#cfn-b2bi-partnership-x12outboundediheaders-interchangecontrolheaders
            '''
            result = self._values.get("interchange_control_headers")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPartnership.X12InterchangeControlHeadersProperty"]], result)

        @builtins.property
        def validate_edi(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether or not to validate the EDI for this X12 object: ``TRUE`` or ``FALSE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-partnership-x12outboundediheaders.html#cfn-b2bi-partnership-x12outboundediheaders-validateedi
            '''
            result = self._values.get("validate_edi")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "X12OutboundEdiHeadersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnershipProps",
    jsii_struct_bases=[],
    name_mapping={
        "capabilities": "capabilities",
        "email": "email",
        "name": "name",
        "profile_id": "profileId",
        "capability_options": "capabilityOptions",
        "phone": "phone",
        "tags": "tags",
    },
)
class CfnPartnershipProps:
    def __init__(
        self,
        *,
        capabilities: typing.Sequence[builtins.str],
        email: builtins.str,
        name: builtins.str,
        profile_id: builtins.str,
        capability_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnership.CapabilityOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        phone: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPartnership``.

        :param capabilities: Returns one or more capabilities associated with this partnership.
        :param email: Specifies the email address associated with this trading partner.
        :param name: Returns the name of the partnership.
        :param profile_id: Returns the unique, system-generated identifier for the profile connected to this partnership.
        :param capability_options: Contains the details for an Outbound EDI capability.
        :param phone: Specifies the phone number associated with the partnership.
        :param tags: A key-value pair for a specific partnership. Tags are metadata that you can use to search for and group capabilities for various purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_b2bi as b2bi
            
            cfn_partnership_props = b2bi.CfnPartnershipProps(
                capabilities=["capabilities"],
                email="email",
                name="name",
                profile_id="profileId",
            
                # the properties below are optional
                capability_options=b2bi.CfnPartnership.CapabilityOptionsProperty(
                    inbound_edi=b2bi.CfnPartnership.InboundEdiOptionsProperty(
                        x12=b2bi.CfnPartnership.X12InboundEdiOptionsProperty(
                            acknowledgment_options=b2bi.CfnPartnership.X12AcknowledgmentOptionsProperty(
                                functional_acknowledgment="functionalAcknowledgment",
                                technical_acknowledgment="technicalAcknowledgment"
                            )
                        )
                    ),
                    outbound_edi=b2bi.CfnPartnership.OutboundEdiOptionsProperty(
                        x12=b2bi.CfnPartnership.X12EnvelopeProperty(
                            common=b2bi.CfnPartnership.X12OutboundEdiHeadersProperty(
                                control_numbers=b2bi.CfnPartnership.X12ControlNumbersProperty(
                                    starting_functional_group_control_number=123,
                                    starting_interchange_control_number=123,
                                    starting_transaction_set_control_number=123
                                ),
                                delimiters=b2bi.CfnPartnership.X12DelimitersProperty(
                                    component_separator="componentSeparator",
                                    data_element_separator="dataElementSeparator",
                                    segment_terminator="segmentTerminator"
                                ),
                                functional_group_headers=b2bi.CfnPartnership.X12FunctionalGroupHeadersProperty(
                                    application_receiver_code="applicationReceiverCode",
                                    application_sender_code="applicationSenderCode",
                                    responsible_agency_code="responsibleAgencyCode"
                                ),
                                gs05_time_format="gs05TimeFormat",
                                interchange_control_headers=b2bi.CfnPartnership.X12InterchangeControlHeadersProperty(
                                    acknowledgment_requested_code="acknowledgmentRequestedCode",
                                    receiver_id="receiverId",
                                    receiver_id_qualifier="receiverIdQualifier",
                                    repetition_separator="repetitionSeparator",
                                    sender_id="senderId",
                                    sender_id_qualifier="senderIdQualifier",
                                    usage_indicator_code="usageIndicatorCode"
                                ),
                                validate_edi=False
                            ),
                            wrap_options=b2bi.CfnPartnership.WrapOptionsProperty(
                                line_length=123,
                                line_terminator="lineTerminator",
                                wrap_by="wrapBy"
                            )
                        )
                    )
                ),
                phone="phone",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18d814bec885d4c9defe3c391c4892f53df8f0ca2dd0011baaccd4959105a243)
            check_type(argname="argument capabilities", value=capabilities, expected_type=type_hints["capabilities"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
            check_type(argname="argument capability_options", value=capability_options, expected_type=type_hints["capability_options"])
            check_type(argname="argument phone", value=phone, expected_type=type_hints["phone"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capabilities": capabilities,
            "email": email,
            "name": name,
            "profile_id": profile_id,
        }
        if capability_options is not None:
            self._values["capability_options"] = capability_options
        if phone is not None:
            self._values["phone"] = phone
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def capabilities(self) -> typing.List[builtins.str]:
        '''Returns one or more capabilities associated with this partnership.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html#cfn-b2bi-partnership-capabilities
        '''
        result = self._values.get("capabilities")
        assert result is not None, "Required property 'capabilities' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def email(self) -> builtins.str:
        '''Specifies the email address associated with this trading partner.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html#cfn-b2bi-partnership-email
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Returns the name of the partnership.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html#cfn-b2bi-partnership-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile_id(self) -> builtins.str:
        '''Returns the unique, system-generated identifier for the profile connected to this partnership.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html#cfn-b2bi-partnership-profileid
        '''
        result = self._values.get("profile_id")
        assert result is not None, "Required property 'profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capability_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPartnership.CapabilityOptionsProperty]]:
        '''Contains the details for an Outbound EDI capability.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html#cfn-b2bi-partnership-capabilityoptions
        '''
        result = self._values.get("capability_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPartnership.CapabilityOptionsProperty]], result)

    @builtins.property
    def phone(self) -> typing.Optional[builtins.str]:
        '''Specifies the phone number associated with the partnership.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html#cfn-b2bi-partnership-phone
        '''
        result = self._values.get("phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key-value pair for a specific partnership.

        Tags are metadata that you can use to search for and group capabilities for various purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html#cfn-b2bi-partnership-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPartnershipProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_b2bi.CfnProfile",
):
    '''Creates a customer profile.

    You can have up to five customer profiles, each representing a distinct private network. A profile is the mechanism used to create the concept of a private network.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html
    :cloudformationResource: AWS::B2BI::Profile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_b2bi as b2bi
        
        cfn_profile = b2bi.CfnProfile(self, "MyCfnProfile",
            business_name="businessName",
            logging="logging",
            name="name",
            phone="phone",
        
            # the properties below are optional
            email="email",
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
        business_name: builtins.str,
        logging: builtins.str,
        name: builtins.str,
        phone: builtins.str,
        email: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param business_name: Returns the name for the business associated with this profile.
        :param logging: Specifies whether or not logging is enabled for this profile.
        :param name: Returns the display name for profile.
        :param phone: 
        :param email: 
        :param tags: A key-value pair for a specific profile. Tags are metadata that you can use to search for and group capabilities for various purposes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e54fea50428e19dd273372ef5650a89d4610c6422804677c9be788a76aadf8a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProfileProps(
            business_name=business_name,
            logging=logging,
            name=name,
            phone=phone,
            email=email,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5271088abc585a3db11af1eacb47274605ad9acc14f75da9da9239d3a3697541)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a829f83cb367edec2f2e051795937696b3dcb1d1ab356574e9c6ad4badf3ce17)
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
        '''Returns the timestamp for creation date and time of the profile.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLogGroupName")
    def attr_log_group_name(self) -> builtins.str:
        '''Returns the name of the logging group.

        :cloudformationAttribute: LogGroupName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLogGroupName"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''Returns the timestamp that identifies the most recent date and time that the profile was modified.

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrProfileArn")
    def attr_profile_arn(self) -> builtins.str:
        '''Returns an Amazon Resource Name (ARN) for the profile.

        :cloudformationAttribute: ProfileArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProfileArn"))

    @builtins.property
    @jsii.member(jsii_name="attrProfileId")
    def attr_profile_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ProfileId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProfileId"))

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
    @jsii.member(jsii_name="businessName")
    def business_name(self) -> builtins.str:
        '''Returns the name for the business associated with this profile.'''
        return typing.cast(builtins.str, jsii.get(self, "businessName"))

    @business_name.setter
    def business_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__504646617c098f5bad7128cc7a515f70f2c86e5d34b43f63aa27a2ad543b4e01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "businessName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> builtins.str:
        '''Specifies whether or not logging is enabled for this profile.'''
        return typing.cast(builtins.str, jsii.get(self, "logging"))

    @logging.setter
    def logging(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__127f59e663824bfd0cc39ab3ed6020d41d54a2b30e31fc71b46ce48e510ff366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logging", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Returns the display name for profile.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__978cb41c2583c736d786df05be25dfaaa254556b513af9850f95c4f5f7999380)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="phone")
    def phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phone"))

    @phone.setter
    def phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aa6ce25bb49d6882927fd231d1e147e27ba9905d54248c88718171a9e0fdd5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phone", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0936f8c78a965c88641d39b7a6e2d4e7ad2bd7f48de6870270d842ba0ccdc34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key-value pair for a specific profile.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b70ada00d6d35989093b4f1b185f6deaa1f9c1404a82bc792e6f4dc53684b45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_b2bi.CfnProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "business_name": "businessName",
        "logging": "logging",
        "name": "name",
        "phone": "phone",
        "email": "email",
        "tags": "tags",
    },
)
class CfnProfileProps:
    def __init__(
        self,
        *,
        business_name: builtins.str,
        logging: builtins.str,
        name: builtins.str,
        phone: builtins.str,
        email: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProfile``.

        :param business_name: Returns the name for the business associated with this profile.
        :param logging: Specifies whether or not logging is enabled for this profile.
        :param name: Returns the display name for profile.
        :param phone: 
        :param email: 
        :param tags: A key-value pair for a specific profile. Tags are metadata that you can use to search for and group capabilities for various purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_b2bi as b2bi
            
            cfn_profile_props = b2bi.CfnProfileProps(
                business_name="businessName",
                logging="logging",
                name="name",
                phone="phone",
            
                # the properties below are optional
                email="email",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85c233c5836835af7c38d9812c75649ec2fc027fa20a2af7be215694f4d322e4)
            check_type(argname="argument business_name", value=business_name, expected_type=type_hints["business_name"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument phone", value=phone, expected_type=type_hints["phone"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "business_name": business_name,
            "logging": logging,
            "name": name,
            "phone": phone,
        }
        if email is not None:
            self._values["email"] = email
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def business_name(self) -> builtins.str:
        '''Returns the name for the business associated with this profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html#cfn-b2bi-profile-businessname
        '''
        result = self._values.get("business_name")
        assert result is not None, "Required property 'business_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def logging(self) -> builtins.str:
        '''Specifies whether or not logging is enabled for this profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html#cfn-b2bi-profile-logging
        '''
        result = self._values.get("logging")
        assert result is not None, "Required property 'logging' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Returns the display name for profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html#cfn-b2bi-profile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html#cfn-b2bi-profile-phone
        '''
        result = self._values.get("phone")
        assert result is not None, "Required property 'phone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html#cfn-b2bi-profile-email
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key-value pair for a specific profile.

        Tags are metadata that you can use to search for and group capabilities for various purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html#cfn-b2bi-profile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnTransformer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformer",
):
    '''Creates a transformer. AWS B2B Data Interchange currently supports two scenarios:.

    - *Inbound EDI* : the AWS customer receives an EDI file from their trading partner. AWS B2B Data Interchange converts this EDI file into a JSON or XML file with a service-defined structure. A mapping template provided by the customer, in JSONata or XSLT format, is optionally applied to this file to produce a JSON or XML file with the structure the customer requires.
    - *Outbound EDI* : the AWS customer has a JSON or XML file containing data that they wish to use in an EDI file. A mapping template, provided by the customer (in either JSONata or XSLT format) is applied to this file to generate a JSON or XML file in the service-defined structure. This file is then converted to an EDI file.

    .. epigraph::

       The following fields are provided for backwards compatibility only: ``fileFormat`` , ``mappingTemplate`` , ``ediType`` , and ``sampleDocument`` .

       - Use the ``mapping`` data type in place of ``mappingTemplate`` and ``fileFormat``
       - Use the ``sampleDocuments`` data type in place of ``sampleDocument``
       - Use either the ``inputConversion`` or ``outputConversion`` in place of ``ediType``

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html
    :cloudformationResource: AWS::B2BI::Transformer
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_b2bi as b2bi
        
        cfn_transformer = b2bi.CfnTransformer(self, "MyCfnTransformer",
            name="name",
            status="status",
        
            # the properties below are optional
            edi_type=b2bi.CfnTransformer.EdiTypeProperty(
                x12_details=b2bi.CfnTransformer.X12DetailsProperty(
                    transaction_set="transactionSet",
                    version="version"
                )
            ),
            file_format="fileFormat",
            input_conversion=b2bi.CfnTransformer.InputConversionProperty(
                from_format="fromFormat",
        
                # the properties below are optional
                advanced_options=b2bi.CfnTransformer.AdvancedOptionsProperty(
                    x12=b2bi.CfnTransformer.X12AdvancedOptionsProperty(
                        split_options=b2bi.CfnTransformer.X12SplitOptionsProperty(
                            split_by="splitBy"
                        )
                    )
                ),
                format_options=b2bi.CfnTransformer.FormatOptionsProperty(
                    x12=b2bi.CfnTransformer.X12DetailsProperty(
                        transaction_set="transactionSet",
                        version="version"
                    )
                )
            ),
            mapping=b2bi.CfnTransformer.MappingProperty(
                template_language="templateLanguage",
        
                # the properties below are optional
                template="template"
            ),
            mapping_template="mappingTemplate",
            output_conversion=b2bi.CfnTransformer.OutputConversionProperty(
                to_format="toFormat",
        
                # the properties below are optional
                format_options=b2bi.CfnTransformer.FormatOptionsProperty(
                    x12=b2bi.CfnTransformer.X12DetailsProperty(
                        transaction_set="transactionSet",
                        version="version"
                    )
                )
            ),
            sample_document="sampleDocument",
            sample_documents=b2bi.CfnTransformer.SampleDocumentsProperty(
                bucket_name="bucketName",
                keys=[b2bi.CfnTransformer.SampleDocumentKeysProperty(
                    input="input",
                    output="output"
                )]
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
        name: builtins.str,
        status: builtins.str,
        edi_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.EdiTypeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        file_format: typing.Optional[builtins.str] = None,
        input_conversion: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.InputConversionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        mapping: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.MappingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        mapping_template: typing.Optional[builtins.str] = None,
        output_conversion: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.OutputConversionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sample_document: typing.Optional[builtins.str] = None,
        sample_documents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.SampleDocumentsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Returns the descriptive name for the transformer.
        :param status: Returns the state of the newly created transformer. The transformer can be either ``active`` or ``inactive`` . For the transformer to be used in a capability, its status must ``active`` .
        :param edi_type: 
        :param file_format: 
        :param input_conversion: Returns a structure that contains the format options for the transformation.
        :param mapping: Returns the structure that contains the mapping template and its language (either XSLT or JSONATA).
        :param mapping_template: (deprecated) This shape is deprecated: This is a legacy trait. Please use input-conversion or output-conversion.
        :param output_conversion: Returns the ``OutputConversion`` object, which contains the format options for the outbound transformation.
        :param sample_document: (deprecated) This shape is deprecated: This is a legacy trait. Please use input-conversion or output-conversion.
        :param sample_documents: Returns a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.
        :param tags: A key-value pair for a specific transformer. Tags are metadata that you can use to search for and group capabilities for various purposes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb0d6d0f8083b8bc38eb61c54d65c6e72d668ba067f31569d0213bf7dafff2c9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTransformerProps(
            name=name,
            status=status,
            edi_type=edi_type,
            file_format=file_format,
            input_conversion=input_conversion,
            mapping=mapping,
            mapping_template=mapping_template,
            output_conversion=output_conversion,
            sample_document=sample_document,
            sample_documents=sample_documents,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd0b05118fb2d551f3054a5c85d10fe283c5ca2b9e830ef5a31a1eb7e66fce63)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8de580bfd50f433c0cd75e13649e7f911981404484637058415a594dac3eea03)
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
        '''Returns a timestamp indicating when the transformer was created.

        For example, ``2023-07-20T19:58:44.624Z`` .

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''Returns a timestamp representing the date and time for the most recent change for the transformer object.

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrTransformerArn")
    def attr_transformer_arn(self) -> builtins.str:
        '''Returns an Amazon Resource Name (ARN) for a specific transformer.

        :cloudformationAttribute: TransformerArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTransformerArn"))

    @builtins.property
    @jsii.member(jsii_name="attrTransformerId")
    def attr_transformer_id(self) -> builtins.str:
        '''The system-assigned unique identifier for the transformer.

        :cloudformationAttribute: TransformerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTransformerId"))

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
        '''Returns the descriptive name for the transformer.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1302a1da7c175d27a541e2b1a5f25f80a4dac4f0a966ee8cddf6d1014ea81395)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        '''Returns the state of the newly created transformer.'''
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa8b2ecdc80ffc3d3b7ddf2cc4493b19df8fa02a3f0dbcf2ea74744b53c3b54c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ediType")
    def edi_type(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.EdiTypeProperty"]]:
        '''
        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.EdiTypeProperty"]], jsii.get(self, "ediType"))

    @edi_type.setter
    def edi_type(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.EdiTypeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e29c7d30dfbbc72fddf07313c1a9cb2eb14ed42c55e23bc13564603f6928f89c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ediType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fileFormat")
    def file_format(self) -> typing.Optional[builtins.str]:
        '''
        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileFormat"))

    @file_format.setter
    def file_format(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2fb21eeda84a5b3d95ee7d5d0e82a546522729b7fd5930fd6ed068055475615)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileFormat", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="inputConversion")
    def input_conversion(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.InputConversionProperty"]]:
        '''Returns a structure that contains the format options for the transformation.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.InputConversionProperty"]], jsii.get(self, "inputConversion"))

    @input_conversion.setter
    def input_conversion(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.InputConversionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__056cb33326d8ab962996a430d43268cf524779e42269f6fd11778cc6ada79b5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputConversion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mapping")
    def mapping(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.MappingProperty"]]:
        '''Returns the structure that contains the mapping template and its language (either XSLT or JSONATA).'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.MappingProperty"]], jsii.get(self, "mapping"))

    @mapping.setter
    def mapping(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.MappingProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e387342b420c26f3bab05e439e7cdb6476c7ca408b9af77f2e83cd5901615494)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mapping", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mappingTemplate")
    def mapping_template(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This shape is deprecated: This is a legacy trait.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mappingTemplate"))

    @mapping_template.setter
    def mapping_template(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__685af615cb66c99ad9251a37e75e2851545a2603e7b07280b617d52d744fdf10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mappingTemplate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outputConversion")
    def output_conversion(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.OutputConversionProperty"]]:
        '''Returns the ``OutputConversion`` object, which contains the format options for the outbound transformation.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.OutputConversionProperty"]], jsii.get(self, "outputConversion"))

    @output_conversion.setter
    def output_conversion(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.OutputConversionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7557543c524bd85a7f46e69222077c401410694a495823c77e5acfd9862974c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputConversion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sampleDocument")
    def sample_document(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This shape is deprecated: This is a legacy trait.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sampleDocument"))

    @sample_document.setter
    def sample_document(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c2214b3717f190a30ff1cc1b45298208906824b8d93bfb181ad552ca17e7a7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleDocument", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sampleDocuments")
    def sample_documents(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.SampleDocumentsProperty"]]:
        '''Returns a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.SampleDocumentsProperty"]], jsii.get(self, "sampleDocuments"))

    @sample_documents.setter
    def sample_documents(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.SampleDocumentsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57efa3bbcc026952ce89a7f735c98632dc48e0c850f121c3bdc93c2fe4983d66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleDocuments", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key-value pair for a specific transformer.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4ec179f77fa2da856518d97a9b83e88d0c96784ca483f80c070b398e5655b89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformer.AdvancedOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"x12": "x12"},
    )
    class AdvancedOptionsProperty:
        def __init__(
            self,
            *,
            x12: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.X12AdvancedOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param x12: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-advancedoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                advanced_options_property = b2bi.CfnTransformer.AdvancedOptionsProperty(
                    x12=b2bi.CfnTransformer.X12AdvancedOptionsProperty(
                        split_options=b2bi.CfnTransformer.X12SplitOptionsProperty(
                            split_by="splitBy"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bb01391868543c9042ef70dbd21634249f177cb7ac9ad6ddf2b2583c136e529b)
                check_type(argname="argument x12", value=x12, expected_type=type_hints["x12"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if x12 is not None:
                self._values["x12"] = x12

        @builtins.property
        def x12(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.X12AdvancedOptionsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-advancedoptions.html#cfn-b2bi-transformer-advancedoptions-x12
            '''
            result = self._values.get("x12")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.X12AdvancedOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdvancedOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformer.EdiTypeProperty",
        jsii_struct_bases=[],
        name_mapping={"x12_details": "x12Details"},
    )
    class EdiTypeProperty:
        def __init__(
            self,
            *,
            x12_details: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.X12DetailsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param x12_details: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-editype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                edi_type_property = b2bi.CfnTransformer.EdiTypeProperty(
                    x12_details=b2bi.CfnTransformer.X12DetailsProperty(
                        transaction_set="transactionSet",
                        version="version"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0a90856b523d4a63e08c58604f08df0cd4ca6647b6d8b2bf4c0c6238831a179a)
                check_type(argname="argument x12_details", value=x12_details, expected_type=type_hints["x12_details"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "x12_details": x12_details,
            }

        @builtins.property
        def x12_details(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTransformer.X12DetailsProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-editype.html#cfn-b2bi-transformer-editype-x12details
            '''
            result = self._values.get("x12_details")
            assert result is not None, "Required property 'x12_details' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTransformer.X12DetailsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EdiTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformer.FormatOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"x12": "x12"},
    )
    class FormatOptionsProperty:
        def __init__(
            self,
            *,
            x12: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.X12DetailsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param x12: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-formatoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                format_options_property = b2bi.CfnTransformer.FormatOptionsProperty(
                    x12=b2bi.CfnTransformer.X12DetailsProperty(
                        transaction_set="transactionSet",
                        version="version"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4fd1bb8229a0f694482eb19adf96ad49a74295bc6d7acb9ae073773371f3b26e)
                check_type(argname="argument x12", value=x12, expected_type=type_hints["x12"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "x12": x12,
            }

        @builtins.property
        def x12(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTransformer.X12DetailsProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-formatoptions.html#cfn-b2bi-transformer-formatoptions-x12
            '''
            result = self._values.get("x12")
            assert result is not None, "Required property 'x12' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTransformer.X12DetailsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FormatOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformer.InputConversionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "from_format": "fromFormat",
            "advanced_options": "advancedOptions",
            "format_options": "formatOptions",
        },
    )
    class InputConversionProperty:
        def __init__(
            self,
            *,
            from_format: builtins.str,
            advanced_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.AdvancedOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            format_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.FormatOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param from_format: 
            :param advanced_options: 
            :param format_options: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-inputconversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                input_conversion_property = b2bi.CfnTransformer.InputConversionProperty(
                    from_format="fromFormat",
                
                    # the properties below are optional
                    advanced_options=b2bi.CfnTransformer.AdvancedOptionsProperty(
                        x12=b2bi.CfnTransformer.X12AdvancedOptionsProperty(
                            split_options=b2bi.CfnTransformer.X12SplitOptionsProperty(
                                split_by="splitBy"
                            )
                        )
                    ),
                    format_options=b2bi.CfnTransformer.FormatOptionsProperty(
                        x12=b2bi.CfnTransformer.X12DetailsProperty(
                            transaction_set="transactionSet",
                            version="version"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__26660093b7b88e1d4689618f27b43e1e286cfcdb3adbc4c515c4b29513332a12)
                check_type(argname="argument from_format", value=from_format, expected_type=type_hints["from_format"])
                check_type(argname="argument advanced_options", value=advanced_options, expected_type=type_hints["advanced_options"])
                check_type(argname="argument format_options", value=format_options, expected_type=type_hints["format_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "from_format": from_format,
            }
            if advanced_options is not None:
                self._values["advanced_options"] = advanced_options
            if format_options is not None:
                self._values["format_options"] = format_options

        @builtins.property
        def from_format(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-inputconversion.html#cfn-b2bi-transformer-inputconversion-fromformat
            '''
            result = self._values.get("from_format")
            assert result is not None, "Required property 'from_format' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def advanced_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.AdvancedOptionsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-inputconversion.html#cfn-b2bi-transformer-inputconversion-advancedoptions
            '''
            result = self._values.get("advanced_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.AdvancedOptionsProperty"]], result)

        @builtins.property
        def format_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.FormatOptionsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-inputconversion.html#cfn-b2bi-transformer-inputconversion-formatoptions
            '''
            result = self._values.get("format_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.FormatOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputConversionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformer.MappingProperty",
        jsii_struct_bases=[],
        name_mapping={"template_language": "templateLanguage", "template": "template"},
    )
    class MappingProperty:
        def __init__(
            self,
            *,
            template_language: builtins.str,
            template: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param template_language: 
            :param template: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-mapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                mapping_property = b2bi.CfnTransformer.MappingProperty(
                    template_language="templateLanguage",
                
                    # the properties below are optional
                    template="template"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0ab01eed6892d54284d211380c1147d43f8287b1d284d94cfbe020e4733c0c53)
                check_type(argname="argument template_language", value=template_language, expected_type=type_hints["template_language"])
                check_type(argname="argument template", value=template, expected_type=type_hints["template"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "template_language": template_language,
            }
            if template is not None:
                self._values["template"] = template

        @builtins.property
        def template_language(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-mapping.html#cfn-b2bi-transformer-mapping-templatelanguage
            '''
            result = self._values.get("template_language")
            assert result is not None, "Required property 'template_language' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def template(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-mapping.html#cfn-b2bi-transformer-mapping-template
            '''
            result = self._values.get("template")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformer.OutputConversionProperty",
        jsii_struct_bases=[],
        name_mapping={"to_format": "toFormat", "format_options": "formatOptions"},
    )
    class OutputConversionProperty:
        def __init__(
            self,
            *,
            to_format: builtins.str,
            format_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.FormatOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param to_format: 
            :param format_options: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-outputconversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                output_conversion_property = b2bi.CfnTransformer.OutputConversionProperty(
                    to_format="toFormat",
                
                    # the properties below are optional
                    format_options=b2bi.CfnTransformer.FormatOptionsProperty(
                        x12=b2bi.CfnTransformer.X12DetailsProperty(
                            transaction_set="transactionSet",
                            version="version"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dba363199b2c0b97d3ba296b1d26754261d2515646da5bce6b98f57eff2c1d59)
                check_type(argname="argument to_format", value=to_format, expected_type=type_hints["to_format"])
                check_type(argname="argument format_options", value=format_options, expected_type=type_hints["format_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "to_format": to_format,
            }
            if format_options is not None:
                self._values["format_options"] = format_options

        @builtins.property
        def to_format(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-outputconversion.html#cfn-b2bi-transformer-outputconversion-toformat
            '''
            result = self._values.get("to_format")
            assert result is not None, "Required property 'to_format' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def format_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.FormatOptionsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-outputconversion.html#cfn-b2bi-transformer-outputconversion-formatoptions
            '''
            result = self._values.get("format_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.FormatOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputConversionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformer.SampleDocumentKeysProperty",
        jsii_struct_bases=[],
        name_mapping={"input": "input", "output": "output"},
    )
    class SampleDocumentKeysProperty:
        def __init__(
            self,
            *,
            input: typing.Optional[builtins.str] = None,
            output: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param input: 
            :param output: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-sampledocumentkeys.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                sample_document_keys_property = b2bi.CfnTransformer.SampleDocumentKeysProperty(
                    input="input",
                    output="output"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4a55402dd251ebf996fa89475f3a74890134f31b512e9f6a30126f32b8dc1195)
                check_type(argname="argument input", value=input, expected_type=type_hints["input"])
                check_type(argname="argument output", value=output, expected_type=type_hints["output"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if input is not None:
                self._values["input"] = input
            if output is not None:
                self._values["output"] = output

        @builtins.property
        def input(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-sampledocumentkeys.html#cfn-b2bi-transformer-sampledocumentkeys-input
            '''
            result = self._values.get("input")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-sampledocumentkeys.html#cfn-b2bi-transformer-sampledocumentkeys-output
            '''
            result = self._values.get("output")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SampleDocumentKeysProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformer.SampleDocumentsProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName", "keys": "keys"},
    )
    class SampleDocumentsProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            keys: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.SampleDocumentKeysProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''
            :param bucket_name: 
            :param keys: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-sampledocuments.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                sample_documents_property = b2bi.CfnTransformer.SampleDocumentsProperty(
                    bucket_name="bucketName",
                    keys=[b2bi.CfnTransformer.SampleDocumentKeysProperty(
                        input="input",
                        output="output"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f6b7e60975e30fa176cbce1116829b7ea73143bc6b12e63afdd39fa252357221)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument keys", value=keys, expected_type=type_hints["keys"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
                "keys": keys,
            }

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-sampledocuments.html#cfn-b2bi-transformer-sampledocuments-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def keys(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.SampleDocumentKeysProperty"]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-sampledocuments.html#cfn-b2bi-transformer-sampledocuments-keys
            '''
            result = self._values.get("keys")
            assert result is not None, "Required property 'keys' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTransformer.SampleDocumentKeysProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SampleDocumentsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformer.X12AdvancedOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"split_options": "splitOptions"},
    )
    class X12AdvancedOptionsProperty:
        def __init__(
            self,
            *,
            split_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.X12SplitOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param split_options: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-x12advancedoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                x12_advanced_options_property = b2bi.CfnTransformer.X12AdvancedOptionsProperty(
                    split_options=b2bi.CfnTransformer.X12SplitOptionsProperty(
                        split_by="splitBy"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0d6cdec7bccb6d811748cbb3f28ec5b4408f4496a924455516c3f90fd268b81c)
                check_type(argname="argument split_options", value=split_options, expected_type=type_hints["split_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if split_options is not None:
                self._values["split_options"] = split_options

        @builtins.property
        def split_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.X12SplitOptionsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-x12advancedoptions.html#cfn-b2bi-transformer-x12advancedoptions-splitoptions
            '''
            result = self._values.get("split_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransformer.X12SplitOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "X12AdvancedOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformer.X12DetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"transaction_set": "transactionSet", "version": "version"},
    )
    class X12DetailsProperty:
        def __init__(
            self,
            *,
            transaction_set: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that contains the X12 transaction set and version.

            The X12 structure is used when the system transforms an EDI (electronic data interchange) file.
            .. epigraph::

               If an EDI input file contains more than one transaction, each transaction must have the same transaction set and version, for example 214/4010. If not, the transformer cannot parse the file.

            :param transaction_set: Returns an enumerated type where each value identifies an X12 transaction set. Transaction sets are maintained by the X12 Accredited Standards Committee.
            :param version: Returns the version to use for the specified X12 transaction set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-x12details.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                x12_details_property = b2bi.CfnTransformer.X12DetailsProperty(
                    transaction_set="transactionSet",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6c52ecd7c7c399e4bebfaf5bf8793e65928fdad0c0133ff1ce55c05683b44ac7)
                check_type(argname="argument transaction_set", value=transaction_set, expected_type=type_hints["transaction_set"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if transaction_set is not None:
                self._values["transaction_set"] = transaction_set
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def transaction_set(self) -> typing.Optional[builtins.str]:
            '''Returns an enumerated type where each value identifies an X12 transaction set.

            Transaction sets are maintained by the X12 Accredited Standards Committee.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-x12details.html#cfn-b2bi-transformer-x12details-transactionset
            '''
            result = self._values.get("transaction_set")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''Returns the version to use for the specified X12 transaction set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-x12details.html#cfn-b2bi-transformer-x12details-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "X12DetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformer.X12SplitOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"split_by": "splitBy"},
    )
    class X12SplitOptionsProperty:
        def __init__(self, *, split_by: typing.Optional[builtins.str] = None) -> None:
            '''
            :param split_by: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-x12splitoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                x12_split_options_property = b2bi.CfnTransformer.X12SplitOptionsProperty(
                    split_by="splitBy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8eda5d523e00df1c59382ff9b447e68e4b9960ae993e8a6bceb3337c0646dede)
                check_type(argname="argument split_by", value=split_by, expected_type=type_hints["split_by"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if split_by is not None:
                self._values["split_by"] = split_by

        @builtins.property
        def split_by(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-x12splitoptions.html#cfn-b2bi-transformer-x12splitoptions-splitby
            '''
            result = self._values.get("split_by")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "X12SplitOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformerProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "status": "status",
        "edi_type": "ediType",
        "file_format": "fileFormat",
        "input_conversion": "inputConversion",
        "mapping": "mapping",
        "mapping_template": "mappingTemplate",
        "output_conversion": "outputConversion",
        "sample_document": "sampleDocument",
        "sample_documents": "sampleDocuments",
        "tags": "tags",
    },
)
class CfnTransformerProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        status: builtins.str,
        edi_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.EdiTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        file_format: typing.Optional[builtins.str] = None,
        input_conversion: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.InputConversionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        mapping: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.MappingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        mapping_template: typing.Optional[builtins.str] = None,
        output_conversion: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.OutputConversionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sample_document: typing.Optional[builtins.str] = None,
        sample_documents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.SampleDocumentsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTransformer``.

        :param name: Returns the descriptive name for the transformer.
        :param status: Returns the state of the newly created transformer. The transformer can be either ``active`` or ``inactive`` . For the transformer to be used in a capability, its status must ``active`` .
        :param edi_type: 
        :param file_format: 
        :param input_conversion: Returns a structure that contains the format options for the transformation.
        :param mapping: Returns the structure that contains the mapping template and its language (either XSLT or JSONATA).
        :param mapping_template: (deprecated) This shape is deprecated: This is a legacy trait. Please use input-conversion or output-conversion.
        :param output_conversion: Returns the ``OutputConversion`` object, which contains the format options for the outbound transformation.
        :param sample_document: (deprecated) This shape is deprecated: This is a legacy trait. Please use input-conversion or output-conversion.
        :param sample_documents: Returns a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.
        :param tags: A key-value pair for a specific transformer. Tags are metadata that you can use to search for and group capabilities for various purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_b2bi as b2bi
            
            cfn_transformer_props = b2bi.CfnTransformerProps(
                name="name",
                status="status",
            
                # the properties below are optional
                edi_type=b2bi.CfnTransformer.EdiTypeProperty(
                    x12_details=b2bi.CfnTransformer.X12DetailsProperty(
                        transaction_set="transactionSet",
                        version="version"
                    )
                ),
                file_format="fileFormat",
                input_conversion=b2bi.CfnTransformer.InputConversionProperty(
                    from_format="fromFormat",
            
                    # the properties below are optional
                    advanced_options=b2bi.CfnTransformer.AdvancedOptionsProperty(
                        x12=b2bi.CfnTransformer.X12AdvancedOptionsProperty(
                            split_options=b2bi.CfnTransformer.X12SplitOptionsProperty(
                                split_by="splitBy"
                            )
                        )
                    ),
                    format_options=b2bi.CfnTransformer.FormatOptionsProperty(
                        x12=b2bi.CfnTransformer.X12DetailsProperty(
                            transaction_set="transactionSet",
                            version="version"
                        )
                    )
                ),
                mapping=b2bi.CfnTransformer.MappingProperty(
                    template_language="templateLanguage",
            
                    # the properties below are optional
                    template="template"
                ),
                mapping_template="mappingTemplate",
                output_conversion=b2bi.CfnTransformer.OutputConversionProperty(
                    to_format="toFormat",
            
                    # the properties below are optional
                    format_options=b2bi.CfnTransformer.FormatOptionsProperty(
                        x12=b2bi.CfnTransformer.X12DetailsProperty(
                            transaction_set="transactionSet",
                            version="version"
                        )
                    )
                ),
                sample_document="sampleDocument",
                sample_documents=b2bi.CfnTransformer.SampleDocumentsProperty(
                    bucket_name="bucketName",
                    keys=[b2bi.CfnTransformer.SampleDocumentKeysProperty(
                        input="input",
                        output="output"
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69e342f03b6075725a81423ccb4db79ba04bb935c9a3fd129f49fd2954e7cc21)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument edi_type", value=edi_type, expected_type=type_hints["edi_type"])
            check_type(argname="argument file_format", value=file_format, expected_type=type_hints["file_format"])
            check_type(argname="argument input_conversion", value=input_conversion, expected_type=type_hints["input_conversion"])
            check_type(argname="argument mapping", value=mapping, expected_type=type_hints["mapping"])
            check_type(argname="argument mapping_template", value=mapping_template, expected_type=type_hints["mapping_template"])
            check_type(argname="argument output_conversion", value=output_conversion, expected_type=type_hints["output_conversion"])
            check_type(argname="argument sample_document", value=sample_document, expected_type=type_hints["sample_document"])
            check_type(argname="argument sample_documents", value=sample_documents, expected_type=type_hints["sample_documents"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "status": status,
        }
        if edi_type is not None:
            self._values["edi_type"] = edi_type
        if file_format is not None:
            self._values["file_format"] = file_format
        if input_conversion is not None:
            self._values["input_conversion"] = input_conversion
        if mapping is not None:
            self._values["mapping"] = mapping
        if mapping_template is not None:
            self._values["mapping_template"] = mapping_template
        if output_conversion is not None:
            self._values["output_conversion"] = output_conversion
        if sample_document is not None:
            self._values["sample_document"] = sample_document
        if sample_documents is not None:
            self._values["sample_documents"] = sample_documents
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''Returns the descriptive name for the transformer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> builtins.str:
        '''Returns the state of the newly created transformer.

        The transformer can be either ``active`` or ``inactive`` . For the transformer to be used in a capability, its status must ``active`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-status
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def edi_type(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransformer.EdiTypeProperty]]:
        '''
        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-editype
        :stability: deprecated
        '''
        result = self._values.get("edi_type")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransformer.EdiTypeProperty]], result)

    @builtins.property
    def file_format(self) -> typing.Optional[builtins.str]:
        '''
        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-fileformat
        :stability: deprecated
        '''
        result = self._values.get("file_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_conversion(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransformer.InputConversionProperty]]:
        '''Returns a structure that contains the format options for the transformation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-inputconversion
        '''
        result = self._values.get("input_conversion")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransformer.InputConversionProperty]], result)

    @builtins.property
    def mapping(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransformer.MappingProperty]]:
        '''Returns the structure that contains the mapping template and its language (either XSLT or JSONATA).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-mapping
        '''
        result = self._values.get("mapping")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransformer.MappingProperty]], result)

    @builtins.property
    def mapping_template(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This shape is deprecated: This is a legacy trait.

        Please use input-conversion or output-conversion.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-mappingtemplate
        :stability: deprecated
        '''
        result = self._values.get("mapping_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_conversion(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransformer.OutputConversionProperty]]:
        '''Returns the ``OutputConversion`` object, which contains the format options for the outbound transformation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-outputconversion
        '''
        result = self._values.get("output_conversion")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransformer.OutputConversionProperty]], result)

    @builtins.property
    def sample_document(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This shape is deprecated: This is a legacy trait.

        Please use input-conversion or output-conversion.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-sampledocument
        :stability: deprecated
        '''
        result = self._values.get("sample_document")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sample_documents(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransformer.SampleDocumentsProperty]]:
        '''Returns a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-sampledocuments
        '''
        result = self._values.get("sample_documents")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransformer.SampleDocumentsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key-value pair for a specific transformer.

        Tags are metadata that you can use to search for and group capabilities for various purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTransformerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCapability",
    "CfnCapabilityProps",
    "CfnPartnership",
    "CfnPartnershipProps",
    "CfnProfile",
    "CfnProfileProps",
    "CfnTransformer",
    "CfnTransformerProps",
]

publication.publish()

def _typecheckingstub__0e2c877d8f658a8bd5b2b87fa89276114a47d5d48d6051351c42b159c7c68d05(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.CapabilityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    type: builtins.str,
    instructions_documents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69250f68db11c0c5d1b5dc6e2fd42eb03c44b04345584670f06ca66a9283eb35(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7a0734db8cefbd4089ea9d0b9242a32f9ce5d439e96d8bf60ea3bf4754e3a55(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e6a4e9debdcf2674a26e8ca0b9f4a771680d6f10a5d05a55ab8bc8c5063b78a(
    value: typing.Union[_IResolvable_da3f097b, CfnCapability.CapabilityConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__149152bfddb988a9aebbfe4cc00f98c6da302293c4bccdb6a2521efdcc265cad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0ac989543b8899d87e7022c05ecf79b8ac846fbb7cbefb25e6bf8a03d5b52da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__933e64c6fb43bdf92fe13796dc8381041bc9d46c8db437f72d8df9acf46d8ef9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCapability.S3LocationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9706dcfa23b620c2db12e1df4414f3a9f0b63bdbd7e3a8ac3944f66549703153(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b39bfeb55ed086d5de5f443fd847773c175cdd988755a308ee0889c0b428322e(
    *,
    edi: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.EdiConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6057bec99d8a1adeb15f82ebd6a5c206f528d80ccf6eaebcc8e44d83d415ec72(
    *,
    input_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
    output_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
    transformer_id: builtins.str,
    type: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.EdiTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    capability_direction: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9ca50562e4e831dbcf7fdb06d87922ec9144632d5572bc4430820884ab15edb(
    *,
    x12_details: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.X12DetailsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aca06398ec10ba74b5ba2cf86fa1032b9983a30858a85eb04ecadf48a95e5056(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a92fd26779dc45009be0b9ca0aefb7b988fae928b06b6b46f41995a7bd338e7(
    *,
    transaction_set: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83b1800b6ac31ea75ae49999ff7054acf5205e3155bfc92964d45204eac123bb(
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.CapabilityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    type: builtins.str,
    instructions_documents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__187ce4b824b0d27162e457adfee9761451ebc9ba1fbb31b215de741e20aea463(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    capabilities: typing.Sequence[builtins.str],
    email: builtins.str,
    name: builtins.str,
    profile_id: builtins.str,
    capability_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnership.CapabilityOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    phone: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d250a045aef9262deb5ac9bdfc02b08a37a777ba8e105b1406ebfad2ee8edc9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97e66f59482a5e62e1d52e1f96109cae79dc6c60b4b84b9ac971718f61abed32(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0980f94d13e92ad52bd4f6a10906045804439d25bf3126b627f3a97eb79eb594(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2873a98dfd303be4e91fec1a674c6ab1a7382e5563610406e047403b795f1a06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2391403bfc3a496d7ff98fb633ece3257a09478e6bed5d4c1c2ec23cd35687c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__126b2c043f2647e2a052eca52ec8432ea60287721a3e645fe4dd65583feb42de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d35bf90164602b28a7873c9bbcf2cebf61f26952d369e2a905926b650b1a22e9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPartnership.CapabilityOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5555f48f20bc825c44c857244fae3207c272ec76cbe060a463105d2c86113010(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc0c0a6e8431d11899a318046b450bc4efc00486d9f20286940067c7fa335411(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__489c8d62d1ea0d603790b535b3f02b6d30eee2c7a02cd1b1d2a497a7f9f54c2b(
    *,
    inbound_edi: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnership.InboundEdiOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    outbound_edi: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnership.OutboundEdiOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6c324487b61389216d4c37a2c38661a9fd27a782f0b1d30b4da2197c02472ca(
    *,
    x12: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnership.X12InboundEdiOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32687b2a777cf504a9e11c6386b8aa7795645f807660aecf3f5bdddf1b953268(
    *,
    x12: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnership.X12EnvelopeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e655ba69d2815891585dad9698c9aca0d8f46825094f69219bf726ac7cc3dfb3(
    *,
    line_length: typing.Optional[jsii.Number] = None,
    line_terminator: typing.Optional[builtins.str] = None,
    wrap_by: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd25022ffe4e73fd8bbd9369b880ae7c91c4a3b0583614cce2974320e88eaa3a(
    *,
    functional_acknowledgment: builtins.str,
    technical_acknowledgment: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30e0c21f8439a660cced0c707b2b1ab5d0199f9710dc5113cb9fcde22546bef9(
    *,
    starting_functional_group_control_number: typing.Optional[jsii.Number] = None,
    starting_interchange_control_number: typing.Optional[jsii.Number] = None,
    starting_transaction_set_control_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c64e6cc29ab2abf7a0ebb687d8309174a673c2096776d261df47c9bb5f6044b(
    *,
    component_separator: typing.Optional[builtins.str] = None,
    data_element_separator: typing.Optional[builtins.str] = None,
    segment_terminator: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30e9a528379ffdff1b0693f52a617de66a178b919d5d3ddc1c68309cc0a86afc(
    *,
    common: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnership.X12OutboundEdiHeadersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    wrap_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnership.WrapOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b107041a5b51efd672a9b2f3b5bb8ce2f8376a1dc4cddc6a58a089e0fc49b53(
    *,
    application_receiver_code: typing.Optional[builtins.str] = None,
    application_sender_code: typing.Optional[builtins.str] = None,
    responsible_agency_code: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25951703b6b17888b8fded1f4b04ca4482b7f065fc950fd49d36619cde5b1ad6(
    *,
    acknowledgment_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnership.X12AcknowledgmentOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cd06c107bbc9de62cfdd484dd7527f5641c4d03e973675f4638b3441dcb2630(
    *,
    acknowledgment_requested_code: typing.Optional[builtins.str] = None,
    receiver_id: typing.Optional[builtins.str] = None,
    receiver_id_qualifier: typing.Optional[builtins.str] = None,
    repetition_separator: typing.Optional[builtins.str] = None,
    sender_id: typing.Optional[builtins.str] = None,
    sender_id_qualifier: typing.Optional[builtins.str] = None,
    usage_indicator_code: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e80431a1b65f39f118b4a0b397a523502dcc49a5197848bd82eff40dc153d1c(
    *,
    control_numbers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnership.X12ControlNumbersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delimiters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnership.X12DelimitersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    functional_group_headers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnership.X12FunctionalGroupHeadersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    gs05_time_format: typing.Optional[builtins.str] = None,
    interchange_control_headers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnership.X12InterchangeControlHeadersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    validate_edi: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18d814bec885d4c9defe3c391c4892f53df8f0ca2dd0011baaccd4959105a243(
    *,
    capabilities: typing.Sequence[builtins.str],
    email: builtins.str,
    name: builtins.str,
    profile_id: builtins.str,
    capability_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPartnership.CapabilityOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    phone: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e54fea50428e19dd273372ef5650a89d4610c6422804677c9be788a76aadf8a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    business_name: builtins.str,
    logging: builtins.str,
    name: builtins.str,
    phone: builtins.str,
    email: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5271088abc585a3db11af1eacb47274605ad9acc14f75da9da9239d3a3697541(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a829f83cb367edec2f2e051795937696b3dcb1d1ab356574e9c6ad4badf3ce17(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__504646617c098f5bad7128cc7a515f70f2c86e5d34b43f63aa27a2ad543b4e01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__127f59e663824bfd0cc39ab3ed6020d41d54a2b30e31fc71b46ce48e510ff366(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__978cb41c2583c736d786df05be25dfaaa254556b513af9850f95c4f5f7999380(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aa6ce25bb49d6882927fd231d1e147e27ba9905d54248c88718171a9e0fdd5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0936f8c78a965c88641d39b7a6e2d4e7ad2bd7f48de6870270d842ba0ccdc34(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b70ada00d6d35989093b4f1b185f6deaa1f9c1404a82bc792e6f4dc53684b45(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85c233c5836835af7c38d9812c75649ec2fc027fa20a2af7be215694f4d322e4(
    *,
    business_name: builtins.str,
    logging: builtins.str,
    name: builtins.str,
    phone: builtins.str,
    email: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb0d6d0f8083b8bc38eb61c54d65c6e72d668ba067f31569d0213bf7dafff2c9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    status: builtins.str,
    edi_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.EdiTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    file_format: typing.Optional[builtins.str] = None,
    input_conversion: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.InputConversionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mapping: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.MappingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mapping_template: typing.Optional[builtins.str] = None,
    output_conversion: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.OutputConversionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sample_document: typing.Optional[builtins.str] = None,
    sample_documents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.SampleDocumentsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd0b05118fb2d551f3054a5c85d10fe283c5ca2b9e830ef5a31a1eb7e66fce63(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8de580bfd50f433c0cd75e13649e7f911981404484637058415a594dac3eea03(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1302a1da7c175d27a541e2b1a5f25f80a4dac4f0a966ee8cddf6d1014ea81395(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa8b2ecdc80ffc3d3b7ddf2cc4493b19df8fa02a3f0dbcf2ea74744b53c3b54c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e29c7d30dfbbc72fddf07313c1a9cb2eb14ed42c55e23bc13564603f6928f89c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransformer.EdiTypeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2fb21eeda84a5b3d95ee7d5d0e82a546522729b7fd5930fd6ed068055475615(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__056cb33326d8ab962996a430d43268cf524779e42269f6fd11778cc6ada79b5f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransformer.InputConversionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e387342b420c26f3bab05e439e7cdb6476c7ca408b9af77f2e83cd5901615494(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransformer.MappingProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__685af615cb66c99ad9251a37e75e2851545a2603e7b07280b617d52d744fdf10(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7557543c524bd85a7f46e69222077c401410694a495823c77e5acfd9862974c8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransformer.OutputConversionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c2214b3717f190a30ff1cc1b45298208906824b8d93bfb181ad552ca17e7a7d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57efa3bbcc026952ce89a7f735c98632dc48e0c850f121c3bdc93c2fe4983d66(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransformer.SampleDocumentsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4ec179f77fa2da856518d97a9b83e88d0c96784ca483f80c070b398e5655b89(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb01391868543c9042ef70dbd21634249f177cb7ac9ad6ddf2b2583c136e529b(
    *,
    x12: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.X12AdvancedOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a90856b523d4a63e08c58604f08df0cd4ca6647b6d8b2bf4c0c6238831a179a(
    *,
    x12_details: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.X12DetailsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd1bb8229a0f694482eb19adf96ad49a74295bc6d7acb9ae073773371f3b26e(
    *,
    x12: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.X12DetailsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26660093b7b88e1d4689618f27b43e1e286cfcdb3adbc4c515c4b29513332a12(
    *,
    from_format: builtins.str,
    advanced_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.AdvancedOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    format_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.FormatOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ab01eed6892d54284d211380c1147d43f8287b1d284d94cfbe020e4733c0c53(
    *,
    template_language: builtins.str,
    template: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dba363199b2c0b97d3ba296b1d26754261d2515646da5bce6b98f57eff2c1d59(
    *,
    to_format: builtins.str,
    format_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.FormatOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a55402dd251ebf996fa89475f3a74890134f31b512e9f6a30126f32b8dc1195(
    *,
    input: typing.Optional[builtins.str] = None,
    output: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6b7e60975e30fa176cbce1116829b7ea73143bc6b12e63afdd39fa252357221(
    *,
    bucket_name: builtins.str,
    keys: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.SampleDocumentKeysProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d6cdec7bccb6d811748cbb3f28ec5b4408f4496a924455516c3f90fd268b81c(
    *,
    split_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.X12SplitOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c52ecd7c7c399e4bebfaf5bf8793e65928fdad0c0133ff1ce55c05683b44ac7(
    *,
    transaction_set: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8eda5d523e00df1c59382ff9b447e68e4b9960ae993e8a6bceb3337c0646dede(
    *,
    split_by: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69e342f03b6075725a81423ccb4db79ba04bb935c9a3fd129f49fd2954e7cc21(
    *,
    name: builtins.str,
    status: builtins.str,
    edi_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.EdiTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    file_format: typing.Optional[builtins.str] = None,
    input_conversion: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.InputConversionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mapping: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.MappingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mapping_template: typing.Optional[builtins.str] = None,
    output_conversion: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.OutputConversionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sample_document: typing.Optional[builtins.str] = None,
    sample_documents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.SampleDocumentsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
