r'''
# AWS::CleanRooms Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_cleanrooms as cleanrooms
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for CleanRooms construct libraries](https://constructs.dev/search?q=cleanrooms)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::CleanRooms resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CleanRooms.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::CleanRooms](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CleanRooms.html).

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
class CfnAnalysisTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnAnalysisTemplate",
):
    '''Creates a new analysis template.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html
    :cloudformationResource: AWS::CleanRooms::AnalysisTemplate
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanrooms as cleanrooms
        
        cfn_analysis_template = cleanrooms.CfnAnalysisTemplate(self, "MyCfnAnalysisTemplate",
            format="format",
            membership_identifier="membershipIdentifier",
            name="name",
            source=cleanrooms.CfnAnalysisTemplate.AnalysisSourceProperty(
                artifacts=cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactsProperty(
                    entry_point=cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactProperty(
                        location=cleanrooms.CfnAnalysisTemplate.S3LocationProperty(
                            bucket="bucket",
                            key="key"
                        )
                    ),
                    role_arn="roleArn",
        
                    # the properties below are optional
                    additional_artifacts=[cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactProperty(
                        location=cleanrooms.CfnAnalysisTemplate.S3LocationProperty(
                            bucket="bucket",
                            key="key"
                        )
                    )]
                ),
                text="text"
            ),
        
            # the properties below are optional
            analysis_parameters=[cleanrooms.CfnAnalysisTemplate.AnalysisParameterProperty(
                name="name",
                type="type",
        
                # the properties below are optional
                default_value="defaultValue"
            )],
            description="description",
            schema=cleanrooms.CfnAnalysisTemplate.AnalysisSchemaProperty(
                referenced_tables=["referencedTables"]
            ),
            source_metadata=cleanrooms.CfnAnalysisTemplate.AnalysisSourceMetadataProperty(
                artifacts=cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactMetadataProperty(
                    entry_point_hash=cleanrooms.CfnAnalysisTemplate.HashProperty(
                        sha256="sha256"
                    ),
        
                    # the properties below are optional
                    additional_artifact_hashes=[cleanrooms.CfnAnalysisTemplate.HashProperty(
                        sha256="sha256"
                    )]
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
        format: builtins.str,
        membership_identifier: builtins.str,
        name: builtins.str,
        source: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalysisTemplate.AnalysisSourceProperty", typing.Dict[builtins.str, typing.Any]]],
        analysis_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalysisTemplate.AnalysisParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        schema: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalysisTemplate.AnalysisSchemaProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        source_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalysisTemplate.AnalysisSourceMetadataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param format: The format of the analysis template.
        :param membership_identifier: The identifier for a membership resource.
        :param name: The name of the analysis template.
        :param source: The source of the analysis template.
        :param analysis_parameters: The parameters of the analysis template.
        :param description: The description of the analysis template.
        :param schema: The entire schema object.
        :param source_metadata: The source metadata for the analysis template.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e650aead4f74afeaf90193249293bee92f9a4eb687f4f9678e1a1368a887bfa)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAnalysisTemplateProps(
            format=format,
            membership_identifier=membership_identifier,
            name=name,
            source=source,
            analysis_parameters=analysis_parameters,
            description=description,
            schema=schema,
            source_metadata=source_metadata,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__def32f8279895eaf5ae2fed796049f11e8ecc1f14c53c7a40e54f77f97722f40)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d2f63941e3ccfc02c5fd40f68748b90631da131360cf742a7aa15eb0547f5b5)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAnalysisTemplateIdentifier")
    def attr_analysis_template_identifier(self) -> builtins.str:
        '''Returns the identifier for the analysis template.

        Example: ``a1b2c3d4-5678-90ab-cdef-EXAMPLE2222``

        :cloudformationAttribute: AnalysisTemplateIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAnalysisTemplateIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of the analysis template.

        Example: ``arn:aws:cleanrooms:us-east-1:111122223333:membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/analysistemplates/a1b2c3d4-5678-90ab-cdef-EXAMPLE2222``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollaborationArn")
    def attr_collaboration_arn(self) -> builtins.str:
        '''Returns the unique ARN for the analysis template’s associated collaboration.

        Example: ``arn:aws:cleanrooms:us-east-1:111122223333:collaboration/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333``

        :cloudformationAttribute: CollaborationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollaborationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollaborationIdentifier")
    def attr_collaboration_identifier(self) -> builtins.str:
        '''Returns the unique ID for the associated collaboration of the analysis template.

        Example: ``a1b2c3d4-5678-90ab-cdef-EXAMPLE33333``

        :cloudformationAttribute: CollaborationIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollaborationIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrMembershipArn")
    def attr_membership_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of the member who created the analysis template.

        Example: ``arn:aws:cleanrooms:us-east-1:111122223333:membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``

        :cloudformationAttribute: MembershipArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMembershipArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSchema")
    def attr_schema(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Schema
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrSchema"))

    @builtins.property
    @jsii.member(jsii_name="attrSchemaReferencedTables")
    def attr_schema_referenced_tables(self) -> typing.List[builtins.str]:
        '''
        :cloudformationAttribute: Schema.ReferencedTables
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrSchemaReferencedTables"))

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
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        '''The format of the analysis template.'''
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a99bf5a96bec195d52c514c174a5c532136760569f0863c25b3672fb0b2a9f3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="membershipIdentifier")
    def membership_identifier(self) -> builtins.str:
        '''The identifier for a membership resource.'''
        return typing.cast(builtins.str, jsii.get(self, "membershipIdentifier"))

    @membership_identifier.setter
    def membership_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__297b2b982e7135bfb11610ac18dcacab85dc955728c10a993db86affc23a6c85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "membershipIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the analysis template.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0ca9c50ab5c0e5399ff8164eb04d12b160d7880a66ad5c75586fef748051a2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisSourceProperty"]:
        '''The source of the analysis template.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisSourceProperty"], jsii.get(self, "source"))

    @source.setter
    def source(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisSourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53060281bd9759f7bd4026827422f1a24050a030c7c5574430af50f44bcdc81f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="analysisParameters")
    def analysis_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisParameterProperty"]]]]:
        '''The parameters of the analysis template.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisParameterProperty"]]]], jsii.get(self, "analysisParameters"))

    @analysis_parameters.setter
    def analysis_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1b12f58b0c5fa25bf8c085bcbec4d711cdcbcd2bcea3e5137ba027e35f34c9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "analysisParameters", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the analysis template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8ea0f1530d49d0cf3ea112be450d6887b42e42d18ffdc9233aac36569611c55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisSchemaProperty"]]:
        '''The entire schema object.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisSchemaProperty"]], jsii.get(self, "schema"))

    @schema.setter
    def schema(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisSchemaProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b08707b577f4e2e4847fc726614c034787b0608c33e3b6db3ed058d8262f49f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceMetadata")
    def source_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisSourceMetadataProperty"]]:
        '''The source metadata for the analysis template.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisSourceMetadataProperty"]], jsii.get(self, "sourceMetadata"))

    @source_metadata.setter
    def source_metadata(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisSourceMetadataProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9971674aa89ce0d927eab26c4a51b41fc5fd99b53e08ed11b02d3b3b8d184899)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceMetadata", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6d8c0e267965c3e8d9449c75e721dc4e1bccb98212af3c5be762ebb7322d8e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnAnalysisTemplate.AnalysisParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "type": "type", "default_value": "defaultValue"},
    )
    class AnalysisParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            type: builtins.str,
            default_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Optional.

            The member who can query can provide this placeholder for a literal data value in an analysis template.

            :param name: The name of the parameter. The name must use only alphanumeric, underscore (_), or hyphen (-) characters but cannot start or end with a hyphen.
            :param type: The type of parameter.
            :param default_value: Optional. The default value that is applied in the analysis template. The member who can query can override this value in the query editor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysisparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                analysis_parameter_property = cleanrooms.CfnAnalysisTemplate.AnalysisParameterProperty(
                    name="name",
                    type="type",
                
                    # the properties below are optional
                    default_value="defaultValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1f8aaf9054ec461e195e032043672bc5f9f627fd62d4544efda7b3ea2740b2d1)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "type": type,
            }
            if default_value is not None:
                self._values["default_value"] = default_value

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the parameter.

            The name must use only alphanumeric, underscore (_), or hyphen (-) characters but cannot start or end with a hyphen.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysisparameter.html#cfn-cleanrooms-analysistemplate-analysisparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysisparameter.html#cfn-cleanrooms-analysistemplate-analysisparameter-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def default_value(self) -> typing.Optional[builtins.str]:
            '''Optional.

            The default value that is applied in the analysis template. The member who can query can override this value in the query editor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysisparameter.html#cfn-cleanrooms-analysistemplate-analysisparameter-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnAnalysisTemplate.AnalysisSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={"referenced_tables": "referencedTables"},
    )
    class AnalysisSchemaProperty:
        def __init__(self, *, referenced_tables: typing.Sequence[builtins.str]) -> None:
            '''A relation within an analysis.

            :param referenced_tables: The tables referenced in the analysis schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysisschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                analysis_schema_property = cleanrooms.CfnAnalysisTemplate.AnalysisSchemaProperty(
                    referenced_tables=["referencedTables"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8f1f3d4aa401aad65536409e9f991c86250c627594c1b918fe7c42b5ac37c097)
                check_type(argname="argument referenced_tables", value=referenced_tables, expected_type=type_hints["referenced_tables"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "referenced_tables": referenced_tables,
            }

        @builtins.property
        def referenced_tables(self) -> typing.List[builtins.str]:
            '''The tables referenced in the analysis schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysisschema.html#cfn-cleanrooms-analysistemplate-analysisschema-referencedtables
            '''
            result = self._values.get("referenced_tables")
            assert result is not None, "Required property 'referenced_tables' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnAnalysisTemplate.AnalysisSourceMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={"artifacts": "artifacts"},
    )
    class AnalysisSourceMetadataProperty:
        def __init__(
            self,
            *,
            artifacts: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalysisTemplate.AnalysisTemplateArtifactMetadataProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The analysis source metadata.

            :param artifacts: The artifacts of the analysis source metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysissourcemetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                analysis_source_metadata_property = cleanrooms.CfnAnalysisTemplate.AnalysisSourceMetadataProperty(
                    artifacts=cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactMetadataProperty(
                        entry_point_hash=cleanrooms.CfnAnalysisTemplate.HashProperty(
                            sha256="sha256"
                        ),
                
                        # the properties below are optional
                        additional_artifact_hashes=[cleanrooms.CfnAnalysisTemplate.HashProperty(
                            sha256="sha256"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__142df4b782054f1f02b59fba238cf11ed294493aa487afe8597ffefc23299578)
                check_type(argname="argument artifacts", value=artifacts, expected_type=type_hints["artifacts"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "artifacts": artifacts,
            }

        @builtins.property
        def artifacts(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisTemplateArtifactMetadataProperty"]:
            '''The artifacts of the analysis source metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysissourcemetadata.html#cfn-cleanrooms-analysistemplate-analysissourcemetadata-artifacts
            '''
            result = self._values.get("artifacts")
            assert result is not None, "Required property 'artifacts' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisTemplateArtifactMetadataProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisSourceMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnAnalysisTemplate.AnalysisSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"artifacts": "artifacts", "text": "text"},
    )
    class AnalysisSourceProperty:
        def __init__(
            self,
            *,
            artifacts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalysisTemplate.AnalysisTemplateArtifactsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            text: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The structure that defines the body of the analysis template.

            :param artifacts: The artifacts of the analysis source.
            :param text: The query text.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysissource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                analysis_source_property = cleanrooms.CfnAnalysisTemplate.AnalysisSourceProperty(
                    artifacts=cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactsProperty(
                        entry_point=cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactProperty(
                            location=cleanrooms.CfnAnalysisTemplate.S3LocationProperty(
                                bucket="bucket",
                                key="key"
                            )
                        ),
                        role_arn="roleArn",
                
                        # the properties below are optional
                        additional_artifacts=[cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactProperty(
                            location=cleanrooms.CfnAnalysisTemplate.S3LocationProperty(
                                bucket="bucket",
                                key="key"
                            )
                        )]
                    ),
                    text="text"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bbdd92f3241147ec8ad458564c84f6695d3a3e85f93b5190554663d6327c512f)
                check_type(argname="argument artifacts", value=artifacts, expected_type=type_hints["artifacts"])
                check_type(argname="argument text", value=text, expected_type=type_hints["text"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if artifacts is not None:
                self._values["artifacts"] = artifacts
            if text is not None:
                self._values["text"] = text

        @builtins.property
        def artifacts(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisTemplateArtifactsProperty"]]:
            '''The artifacts of the analysis source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysissource.html#cfn-cleanrooms-analysistemplate-analysissource-artifacts
            '''
            result = self._values.get("artifacts")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisTemplateArtifactsProperty"]], result)

        @builtins.property
        def text(self) -> typing.Optional[builtins.str]:
            '''The query text.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysissource.html#cfn-cleanrooms-analysistemplate-analysissource-text
            '''
            result = self._values.get("text")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "entry_point_hash": "entryPointHash",
            "additional_artifact_hashes": "additionalArtifactHashes",
        },
    )
    class AnalysisTemplateArtifactMetadataProperty:
        def __init__(
            self,
            *,
            entry_point_hash: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalysisTemplate.HashProperty", typing.Dict[builtins.str, typing.Any]]],
            additional_artifact_hashes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalysisTemplate.HashProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The analysis template artifact metadata.

            :param entry_point_hash: The hash of the entry point for the analysis template artifact metadata.
            :param additional_artifact_hashes: Additional artifact hashes for the analysis template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysistemplateartifactmetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                analysis_template_artifact_metadata_property = cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactMetadataProperty(
                    entry_point_hash=cleanrooms.CfnAnalysisTemplate.HashProperty(
                        sha256="sha256"
                    ),
                
                    # the properties below are optional
                    additional_artifact_hashes=[cleanrooms.CfnAnalysisTemplate.HashProperty(
                        sha256="sha256"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__987e835d80cb906f68846a5d130091f8db0105378671d39598489b7cabd5fb36)
                check_type(argname="argument entry_point_hash", value=entry_point_hash, expected_type=type_hints["entry_point_hash"])
                check_type(argname="argument additional_artifact_hashes", value=additional_artifact_hashes, expected_type=type_hints["additional_artifact_hashes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entry_point_hash": entry_point_hash,
            }
            if additional_artifact_hashes is not None:
                self._values["additional_artifact_hashes"] = additional_artifact_hashes

        @builtins.property
        def entry_point_hash(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.HashProperty"]:
            '''The hash of the entry point for the analysis template artifact metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysistemplateartifactmetadata.html#cfn-cleanrooms-analysistemplate-analysistemplateartifactmetadata-entrypointhash
            '''
            result = self._values.get("entry_point_hash")
            assert result is not None, "Required property 'entry_point_hash' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.HashProperty"], result)

        @builtins.property
        def additional_artifact_hashes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.HashProperty"]]]]:
            '''Additional artifact hashes for the analysis template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysistemplateartifactmetadata.html#cfn-cleanrooms-analysistemplate-analysistemplateartifactmetadata-additionalartifacthashes
            '''
            result = self._values.get("additional_artifact_hashes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.HashProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisTemplateArtifactMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactProperty",
        jsii_struct_bases=[],
        name_mapping={"location": "location"},
    )
    class AnalysisTemplateArtifactProperty:
        def __init__(
            self,
            *,
            location: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalysisTemplate.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The analysis template artifact.

            :param location: The artifact location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysistemplateartifact.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                analysis_template_artifact_property = cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactProperty(
                    location=cleanrooms.CfnAnalysisTemplate.S3LocationProperty(
                        bucket="bucket",
                        key="key"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7f833b582ec423809f565e96fc9ba5d49349ac881791d343e35df1673b1c9644)
                check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "location": location,
            }

        @builtins.property
        def location(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.S3LocationProperty"]:
            '''The artifact location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysistemplateartifact.html#cfn-cleanrooms-analysistemplate-analysistemplateartifact-location
            '''
            result = self._values.get("location")
            assert result is not None, "Required property 'location' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.S3LocationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisTemplateArtifactProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "entry_point": "entryPoint",
            "role_arn": "roleArn",
            "additional_artifacts": "additionalArtifacts",
        },
    )
    class AnalysisTemplateArtifactsProperty:
        def __init__(
            self,
            *,
            entry_point: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalysisTemplate.AnalysisTemplateArtifactProperty", typing.Dict[builtins.str, typing.Any]]],
            role_arn: builtins.str,
            additional_artifacts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalysisTemplate.AnalysisTemplateArtifactProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The analysis template artifacts.

            :param entry_point: The entry point for the analysis template artifacts.
            :param role_arn: The role ARN for the analysis template artifacts.
            :param additional_artifacts: Additional artifacts for the analysis template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysistemplateartifacts.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                analysis_template_artifacts_property = cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactsProperty(
                    entry_point=cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactProperty(
                        location=cleanrooms.CfnAnalysisTemplate.S3LocationProperty(
                            bucket="bucket",
                            key="key"
                        )
                    ),
                    role_arn="roleArn",
                
                    # the properties below are optional
                    additional_artifacts=[cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactProperty(
                        location=cleanrooms.CfnAnalysisTemplate.S3LocationProperty(
                            bucket="bucket",
                            key="key"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__de78ae9ecad686157204e702611c0cf015331e3aa099f1e87ab18d5cd854abfb)
                check_type(argname="argument entry_point", value=entry_point, expected_type=type_hints["entry_point"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument additional_artifacts", value=additional_artifacts, expected_type=type_hints["additional_artifacts"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entry_point": entry_point,
                "role_arn": role_arn,
            }
            if additional_artifacts is not None:
                self._values["additional_artifacts"] = additional_artifacts

        @builtins.property
        def entry_point(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisTemplateArtifactProperty"]:
            '''The entry point for the analysis template artifacts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysistemplateartifacts.html#cfn-cleanrooms-analysistemplate-analysistemplateartifacts-entrypoint
            '''
            result = self._values.get("entry_point")
            assert result is not None, "Required property 'entry_point' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisTemplateArtifactProperty"], result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The role ARN for the analysis template artifacts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysistemplateartifacts.html#cfn-cleanrooms-analysistemplate-analysistemplateartifacts-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def additional_artifacts(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisTemplateArtifactProperty"]]]]:
            '''Additional artifacts for the analysis template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-analysistemplateartifacts.html#cfn-cleanrooms-analysistemplate-analysistemplateartifacts-additionalartifacts
            '''
            result = self._values.get("additional_artifacts")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalysisTemplate.AnalysisTemplateArtifactProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisTemplateArtifactsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnAnalysisTemplate.HashProperty",
        jsii_struct_bases=[],
        name_mapping={"sha256": "sha256"},
    )
    class HashProperty:
        def __init__(self, *, sha256: typing.Optional[builtins.str] = None) -> None:
            '''Hash.

            :param sha256: The SHA-256 hash value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-hash.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                hash_property = cleanrooms.CfnAnalysisTemplate.HashProperty(
                    sha256="sha256"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__43be85fff22ad377febb791857a9bfd90b262e37e83d363df6adfb5783ea6cb5)
                check_type(argname="argument sha256", value=sha256, expected_type=type_hints["sha256"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sha256 is not None:
                self._values["sha256"] = sha256

        @builtins.property
        def sha256(self) -> typing.Optional[builtins.str]:
            '''The SHA-256 hash value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-hash.html#cfn-cleanrooms-analysistemplate-hash-sha256
            '''
            result = self._values.get("sha256")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HashProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnAnalysisTemplate.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key"},
    )
    class S3LocationProperty:
        def __init__(self, *, bucket: builtins.str, key: builtins.str) -> None:
            '''The S3 location.

            :param bucket: The bucket name.
            :param key: The object key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                s3_location_property = cleanrooms.CfnAnalysisTemplate.S3LocationProperty(
                    bucket="bucket",
                    key="key"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7bb4aaebbf6530b26619974d56993c72a085bd8e9326904d3e54412c155e81e3)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
            }

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The bucket name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-s3location.html#cfn-cleanrooms-analysistemplate-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The object key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-analysistemplate-s3location.html#cfn-cleanrooms-analysistemplate-s3location-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnAnalysisTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "format": "format",
        "membership_identifier": "membershipIdentifier",
        "name": "name",
        "source": "source",
        "analysis_parameters": "analysisParameters",
        "description": "description",
        "schema": "schema",
        "source_metadata": "sourceMetadata",
        "tags": "tags",
    },
)
class CfnAnalysisTemplateProps:
    def __init__(
        self,
        *,
        format: builtins.str,
        membership_identifier: builtins.str,
        name: builtins.str,
        source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisSourceProperty, typing.Dict[builtins.str, typing.Any]]],
        analysis_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        schema: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisSchemaProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        source_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisSourceMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAnalysisTemplate``.

        :param format: The format of the analysis template.
        :param membership_identifier: The identifier for a membership resource.
        :param name: The name of the analysis template.
        :param source: The source of the analysis template.
        :param analysis_parameters: The parameters of the analysis template.
        :param description: The description of the analysis template.
        :param schema: The entire schema object.
        :param source_metadata: The source metadata for the analysis template.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanrooms as cleanrooms
            
            cfn_analysis_template_props = cleanrooms.CfnAnalysisTemplateProps(
                format="format",
                membership_identifier="membershipIdentifier",
                name="name",
                source=cleanrooms.CfnAnalysisTemplate.AnalysisSourceProperty(
                    artifacts=cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactsProperty(
                        entry_point=cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactProperty(
                            location=cleanrooms.CfnAnalysisTemplate.S3LocationProperty(
                                bucket="bucket",
                                key="key"
                            )
                        ),
                        role_arn="roleArn",
            
                        # the properties below are optional
                        additional_artifacts=[cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactProperty(
                            location=cleanrooms.CfnAnalysisTemplate.S3LocationProperty(
                                bucket="bucket",
                                key="key"
                            )
                        )]
                    ),
                    text="text"
                ),
            
                # the properties below are optional
                analysis_parameters=[cleanrooms.CfnAnalysisTemplate.AnalysisParameterProperty(
                    name="name",
                    type="type",
            
                    # the properties below are optional
                    default_value="defaultValue"
                )],
                description="description",
                schema=cleanrooms.CfnAnalysisTemplate.AnalysisSchemaProperty(
                    referenced_tables=["referencedTables"]
                ),
                source_metadata=cleanrooms.CfnAnalysisTemplate.AnalysisSourceMetadataProperty(
                    artifacts=cleanrooms.CfnAnalysisTemplate.AnalysisTemplateArtifactMetadataProperty(
                        entry_point_hash=cleanrooms.CfnAnalysisTemplate.HashProperty(
                            sha256="sha256"
                        ),
            
                        # the properties below are optional
                        additional_artifact_hashes=[cleanrooms.CfnAnalysisTemplate.HashProperty(
                            sha256="sha256"
                        )]
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1c797e3fa5f8683aa0eb66424f00b6b29c5014d5c45e7771fe0c5b1e9a973e8)
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument membership_identifier", value=membership_identifier, expected_type=type_hints["membership_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument analysis_parameters", value=analysis_parameters, expected_type=type_hints["analysis_parameters"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument source_metadata", value=source_metadata, expected_type=type_hints["source_metadata"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "format": format,
            "membership_identifier": membership_identifier,
            "name": name,
            "source": source,
        }
        if analysis_parameters is not None:
            self._values["analysis_parameters"] = analysis_parameters
        if description is not None:
            self._values["description"] = description
        if schema is not None:
            self._values["schema"] = schema
        if source_metadata is not None:
            self._values["source_metadata"] = source_metadata
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def format(self) -> builtins.str:
        '''The format of the analysis template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-format
        '''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def membership_identifier(self) -> builtins.str:
        '''The identifier for a membership resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-membershipidentifier
        '''
        result = self._values.get("membership_identifier")
        assert result is not None, "Required property 'membership_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the analysis template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAnalysisTemplate.AnalysisSourceProperty]:
        '''The source of the analysis template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-source
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAnalysisTemplate.AnalysisSourceProperty], result)

    @builtins.property
    def analysis_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnalysisTemplate.AnalysisParameterProperty]]]]:
        '''The parameters of the analysis template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-analysisparameters
        '''
        result = self._values.get("analysis_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnalysisTemplate.AnalysisParameterProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the analysis template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnalysisTemplate.AnalysisSchemaProperty]]:
        '''The entire schema object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-schema
        '''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnalysisTemplate.AnalysisSchemaProperty]], result)

    @builtins.property
    def source_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnalysisTemplate.AnalysisSourceMetadataProperty]]:
        '''The source metadata for the analysis template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-sourcemetadata
        '''
        result = self._values.get("source_metadata")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnalysisTemplate.AnalysisSourceMetadataProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.

        Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-analysistemplate.html#cfn-cleanrooms-analysistemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAnalysisTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnCollaboration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnCollaboration",
):
    '''Creates a new collaboration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html
    :cloudformationResource: AWS::CleanRooms::Collaboration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanrooms as cleanrooms
        
        cfn_collaboration = cleanrooms.CfnCollaboration(self, "MyCfnCollaboration",
            creator_display_name="creatorDisplayName",
            description="description",
            name="name",
            query_log_status="queryLogStatus",
        
            # the properties below are optional
            analytics_engine="analyticsEngine",
            creator_member_abilities=["creatorMemberAbilities"],
            creator_ml_member_abilities=cleanrooms.CfnCollaboration.MLMemberAbilitiesProperty(
                custom_ml_member_abilities=["customMlMemberAbilities"]
            ),
            creator_payment_configuration=cleanrooms.CfnCollaboration.PaymentConfigurationProperty(
                query_compute=cleanrooms.CfnCollaboration.QueryComputePaymentConfigProperty(
                    is_responsible=False
                ),
        
                # the properties below are optional
                job_compute=cleanrooms.CfnCollaboration.JobComputePaymentConfigProperty(
                    is_responsible=False
                ),
                machine_learning=cleanrooms.CfnCollaboration.MLPaymentConfigProperty(
                    model_inference=cleanrooms.CfnCollaboration.ModelInferencePaymentConfigProperty(
                        is_responsible=False
                    ),
                    model_training=cleanrooms.CfnCollaboration.ModelTrainingPaymentConfigProperty(
                        is_responsible=False
                    )
                )
            ),
            data_encryption_metadata=cleanrooms.CfnCollaboration.DataEncryptionMetadataProperty(
                allow_cleartext=False,
                allow_duplicates=False,
                allow_joins_on_columns_with_different_names=False,
                preserve_nulls=False
            ),
            job_log_status="jobLogStatus",
            members=[cleanrooms.CfnCollaboration.MemberSpecificationProperty(
                account_id="accountId",
                display_name="displayName",
        
                # the properties below are optional
                member_abilities=["memberAbilities"],
                ml_member_abilities=cleanrooms.CfnCollaboration.MLMemberAbilitiesProperty(
                    custom_ml_member_abilities=["customMlMemberAbilities"]
                ),
                payment_configuration=cleanrooms.CfnCollaboration.PaymentConfigurationProperty(
                    query_compute=cleanrooms.CfnCollaboration.QueryComputePaymentConfigProperty(
                        is_responsible=False
                    ),
        
                    # the properties below are optional
                    job_compute=cleanrooms.CfnCollaboration.JobComputePaymentConfigProperty(
                        is_responsible=False
                    ),
                    machine_learning=cleanrooms.CfnCollaboration.MLPaymentConfigProperty(
                        model_inference=cleanrooms.CfnCollaboration.ModelInferencePaymentConfigProperty(
                            is_responsible=False
                        ),
                        model_training=cleanrooms.CfnCollaboration.ModelTrainingPaymentConfigProperty(
                            is_responsible=False
                        )
                    )
                )
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
        creator_display_name: builtins.str,
        description: builtins.str,
        name: builtins.str,
        query_log_status: builtins.str,
        analytics_engine: typing.Optional[builtins.str] = None,
        creator_member_abilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        creator_ml_member_abilities: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCollaboration.MLMemberAbilitiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        creator_payment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCollaboration.PaymentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        data_encryption_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCollaboration.DataEncryptionMetadataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        job_log_status: typing.Optional[builtins.str] = None,
        members: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCollaboration.MemberSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param creator_display_name: A display name of the collaboration creator.
        :param description: A description of the collaboration provided by the collaboration owner.
        :param name: A human-readable identifier provided by the collaboration owner. Display names are not unique.
        :param query_log_status: An indicator as to whether query logging has been enabled or disabled for the collaboration. When ``ENABLED`` , AWS Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is ``DISABLED`` .
        :param analytics_engine: The analytics engine for the collaboration. .. epigraph:: After July 16, 2025, the ``CLEAN_ROOMS_SQL`` parameter will no longer be available.
        :param creator_member_abilities: The abilities granted to the collaboration creator. *Allowed values* ``CAN_QUERY`` | ``CAN_RECEIVE_RESULTS`` | ``CAN_RUN_JOB``
        :param creator_ml_member_abilities: The ML member abilities for a collaboration member.
        :param creator_payment_configuration: An object representing the collaboration member's payment responsibilities set by the collaboration creator.
        :param data_encryption_metadata: The settings for client-side encryption for cryptographic computing.
        :param job_log_status: An indicator as to whether job logging has been enabled or disabled for the collaboration. When ``ENABLED`` , AWS Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is ``DISABLED`` .
        :param members: A list of initial members, not including the creator. This list is immutable.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8995527da9ce4212caf3c1fdf601e4947c02ff1e364e92811ac8635be534111)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCollaborationProps(
            creator_display_name=creator_display_name,
            description=description,
            name=name,
            query_log_status=query_log_status,
            analytics_engine=analytics_engine,
            creator_member_abilities=creator_member_abilities,
            creator_ml_member_abilities=creator_ml_member_abilities,
            creator_payment_configuration=creator_payment_configuration,
            data_encryption_metadata=data_encryption_metadata,
            job_log_status=job_log_status,
            members=members,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43b0d208a10b53d5d7bf8e19cff7b1a7be86094960aa43579972861d563de44d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a9705b5c9f28f1d364782d5cb996ee4fe0e93dc0fbee1871bc10feeb5a547d9)
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
        '''Returns the Amazon Resource Name (ARN) of the specified collaboration.

        Example: ``arn:aws:cleanrooms:us-east-1:111122223333:collaboration/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollaborationIdentifier")
    def attr_collaboration_identifier(self) -> builtins.str:
        '''Returns the unique identifier of the specified collaboration.

        Example: ``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``

        :cloudformationAttribute: CollaborationIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollaborationIdentifier"))

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
    @jsii.member(jsii_name="creatorDisplayName")
    def creator_display_name(self) -> builtins.str:
        '''A display name of the collaboration creator.'''
        return typing.cast(builtins.str, jsii.get(self, "creatorDisplayName"))

    @creator_display_name.setter
    def creator_display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a9f17060755de314c6aea7e9fe1c03f18e31972fafbe5d1edf10b18250f60ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creatorDisplayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A description of the collaboration provided by the collaboration owner.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb5edb6a58e1c0f33620eadb56126089a140277fe87954ea4d3a06146b3559ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A human-readable identifier provided by the collaboration owner.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__585aa64e1eeaa11003c987d7230a1772b0683c9f8866457214d0242ba9d00d4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="queryLogStatus")
    def query_log_status(self) -> builtins.str:
        '''An indicator as to whether query logging has been enabled or disabled for the collaboration.'''
        return typing.cast(builtins.str, jsii.get(self, "queryLogStatus"))

    @query_log_status.setter
    def query_log_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa852049fd80eee6c2543d7576eb0c8f60a43d90ca97006450c31d8a1ed9df20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryLogStatus", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="analyticsEngine")
    def analytics_engine(self) -> typing.Optional[builtins.str]:
        '''The analytics engine for the collaboration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "analyticsEngine"))

    @analytics_engine.setter
    def analytics_engine(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1052deb6a86709adcf30bca5621af3b50e52d20c54f6e014b8baeaa998273732)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "analyticsEngine", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="creatorMemberAbilities")
    def creator_member_abilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The abilities granted to the collaboration creator.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "creatorMemberAbilities"))

    @creator_member_abilities.setter
    def creator_member_abilities(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ee81f8b64fd681cae1a860e0339dfa0ddeb287c4e709f0b34cc3c8bcf9bc6bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creatorMemberAbilities", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="creatorMlMemberAbilities")
    def creator_ml_member_abilities(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.MLMemberAbilitiesProperty"]]:
        '''The ML member abilities for a collaboration member.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.MLMemberAbilitiesProperty"]], jsii.get(self, "creatorMlMemberAbilities"))

    @creator_ml_member_abilities.setter
    def creator_ml_member_abilities(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.MLMemberAbilitiesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97c0d0f6cb32a0cbf54c04b4f619c67713dd848075c944908bc62665b42284a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creatorMlMemberAbilities", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="creatorPaymentConfiguration")
    def creator_payment_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.PaymentConfigurationProperty"]]:
        '''An object representing the collaboration member's payment responsibilities set by the collaboration creator.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.PaymentConfigurationProperty"]], jsii.get(self, "creatorPaymentConfiguration"))

    @creator_payment_configuration.setter
    def creator_payment_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.PaymentConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__991360bdd6af4d5b428da7f242ab1cc46f2a619a380ffdff6e2434a3e7541e84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creatorPaymentConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dataEncryptionMetadata")
    def data_encryption_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.DataEncryptionMetadataProperty"]]:
        '''The settings for client-side encryption for cryptographic computing.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.DataEncryptionMetadataProperty"]], jsii.get(self, "dataEncryptionMetadata"))

    @data_encryption_metadata.setter
    def data_encryption_metadata(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.DataEncryptionMetadataProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a86b18a30aac6a5afc1830c4adb282d4f0f3199f7c3d3ce99ffb24dad829a6eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataEncryptionMetadata", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="jobLogStatus")
    def job_log_status(self) -> typing.Optional[builtins.str]:
        '''An indicator as to whether job logging has been enabled or disabled for the collaboration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobLogStatus"))

    @job_log_status.setter
    def job_log_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4417cba39dba6b058b8e9e8165e109039205858f8f1e7237cc3fa2e9f60ee5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobLogStatus", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="members")
    def members(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.MemberSpecificationProperty"]]]]:
        '''A list of initial members, not including the creator.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.MemberSpecificationProperty"]]]], jsii.get(self, "members"))

    @members.setter
    def members(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.MemberSpecificationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e816963af09a7c3bdf0ca05211222f43d66929e9fa8216fe82e8fb6e27493bdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "members", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06877122efbe5bc41c92999ba727597f48590c383378ee73a94c91fe43305e60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnCollaboration.DataEncryptionMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allow_cleartext": "allowCleartext",
            "allow_duplicates": "allowDuplicates",
            "allow_joins_on_columns_with_different_names": "allowJoinsOnColumnsWithDifferentNames",
            "preserve_nulls": "preserveNulls",
        },
    )
    class DataEncryptionMetadataProperty:
        def __init__(
            self,
            *,
            allow_cleartext: typing.Union[builtins.bool, _IResolvable_da3f097b],
            allow_duplicates: typing.Union[builtins.bool, _IResolvable_da3f097b],
            allow_joins_on_columns_with_different_names: typing.Union[builtins.bool, _IResolvable_da3f097b],
            preserve_nulls: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''The settings for client-side encryption for cryptographic computing.

            :param allow_cleartext: Indicates whether encrypted tables can contain cleartext data ( ``TRUE`` ) or are to cryptographically process every column ( ``FALSE`` ).
            :param allow_duplicates: Indicates whether Fingerprint columns can contain duplicate entries ( ``TRUE`` ) or are to contain only non-repeated values ( ``FALSE`` ).
            :param allow_joins_on_columns_with_different_names: Indicates whether Fingerprint columns can be joined on any other Fingerprint column with a different name ( ``TRUE`` ) or can only be joined on Fingerprint columns of the same name ( ``FALSE`` ).
            :param preserve_nulls: Indicates whether NULL values are to be copied as NULL to encrypted tables ( ``TRUE`` ) or cryptographically processed ( ``FALSE`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                data_encryption_metadata_property = cleanrooms.CfnCollaboration.DataEncryptionMetadataProperty(
                    allow_cleartext=False,
                    allow_duplicates=False,
                    allow_joins_on_columns_with_different_names=False,
                    preserve_nulls=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b1d5c25162d0eabd19a06fd0a1ec26adcd8d8a0d12434d6ee8fbec8e27c21965)
                check_type(argname="argument allow_cleartext", value=allow_cleartext, expected_type=type_hints["allow_cleartext"])
                check_type(argname="argument allow_duplicates", value=allow_duplicates, expected_type=type_hints["allow_duplicates"])
                check_type(argname="argument allow_joins_on_columns_with_different_names", value=allow_joins_on_columns_with_different_names, expected_type=type_hints["allow_joins_on_columns_with_different_names"])
                check_type(argname="argument preserve_nulls", value=preserve_nulls, expected_type=type_hints["preserve_nulls"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allow_cleartext": allow_cleartext,
                "allow_duplicates": allow_duplicates,
                "allow_joins_on_columns_with_different_names": allow_joins_on_columns_with_different_names,
                "preserve_nulls": preserve_nulls,
            }

        @builtins.property
        def allow_cleartext(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether encrypted tables can contain cleartext data ( ``TRUE`` ) or are to cryptographically process every column ( ``FALSE`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html#cfn-cleanrooms-collaboration-dataencryptionmetadata-allowcleartext
            '''
            result = self._values.get("allow_cleartext")
            assert result is not None, "Required property 'allow_cleartext' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def allow_duplicates(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether Fingerprint columns can contain duplicate entries ( ``TRUE`` ) or are to contain only non-repeated values ( ``FALSE`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html#cfn-cleanrooms-collaboration-dataencryptionmetadata-allowduplicates
            '''
            result = self._values.get("allow_duplicates")
            assert result is not None, "Required property 'allow_duplicates' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def allow_joins_on_columns_with_different_names(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether Fingerprint columns can be joined on any other Fingerprint column with a different name ( ``TRUE`` ) or can only be joined on Fingerprint columns of the same name ( ``FALSE`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html#cfn-cleanrooms-collaboration-dataencryptionmetadata-allowjoinsoncolumnswithdifferentnames
            '''
            result = self._values.get("allow_joins_on_columns_with_different_names")
            assert result is not None, "Required property 'allow_joins_on_columns_with_different_names' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def preserve_nulls(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether NULL values are to be copied as NULL to encrypted tables ( ``TRUE`` ) or cryptographically processed ( ``FALSE`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-dataencryptionmetadata.html#cfn-cleanrooms-collaboration-dataencryptionmetadata-preservenulls
            '''
            result = self._values.get("preserve_nulls")
            assert result is not None, "Required property 'preserve_nulls' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataEncryptionMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnCollaboration.JobComputePaymentConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"is_responsible": "isResponsible"},
    )
    class JobComputePaymentConfigProperty:
        def __init__(
            self,
            *,
            is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''An object representing the collaboration member's payment responsibilities set by the collaboration creator for query and job compute costs.

            :param is_responsible: Indicates whether the collaboration creator has configured the collaboration member to pay for query and job compute costs ( ``TRUE`` ) or has not configured the collaboration member to pay for query and job compute costs ( ``FALSE`` ). Exactly one member can be configured to pay for query and job compute costs. An error is returned if the collaboration creator sets a ``TRUE`` value for more than one member in the collaboration. An error is returned if the collaboration creator sets a ``FALSE`` value for the member who can run queries and jobs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-jobcomputepaymentconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                job_compute_payment_config_property = cleanrooms.CfnCollaboration.JobComputePaymentConfigProperty(
                    is_responsible=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c083b467c80242022df99766953c94b800010fa09b9890251c092ef48906a8d6)
                check_type(argname="argument is_responsible", value=is_responsible, expected_type=type_hints["is_responsible"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "is_responsible": is_responsible,
            }

        @builtins.property
        def is_responsible(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether the collaboration creator has configured the collaboration member to pay for query and job compute costs ( ``TRUE`` ) or has not configured the collaboration member to pay for query and job compute costs ( ``FALSE`` ).

            Exactly one member can be configured to pay for query and job compute costs. An error is returned if the collaboration creator sets a ``TRUE`` value for more than one member in the collaboration.

            An error is returned if the collaboration creator sets a ``FALSE`` value for the member who can run queries and jobs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-jobcomputepaymentconfig.html#cfn-cleanrooms-collaboration-jobcomputepaymentconfig-isresponsible
            '''
            result = self._values.get("is_responsible")
            assert result is not None, "Required property 'is_responsible' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JobComputePaymentConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnCollaboration.MLMemberAbilitiesProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_ml_member_abilities": "customMlMemberAbilities"},
    )
    class MLMemberAbilitiesProperty:
        def __init__(
            self,
            *,
            custom_ml_member_abilities: typing.Sequence[builtins.str],
        ) -> None:
            '''The ML member abilities for a collaboration member.

            :param custom_ml_member_abilities: The custom ML member abilities for a collaboration member.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-mlmemberabilities.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                m_lMember_abilities_property = cleanrooms.CfnCollaboration.MLMemberAbilitiesProperty(
                    custom_ml_member_abilities=["customMlMemberAbilities"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1d12c181790032dcf002dcacb31cb4e50bd00d2ab068f38065b4ad7d1319d80c)
                check_type(argname="argument custom_ml_member_abilities", value=custom_ml_member_abilities, expected_type=type_hints["custom_ml_member_abilities"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "custom_ml_member_abilities": custom_ml_member_abilities,
            }

        @builtins.property
        def custom_ml_member_abilities(self) -> typing.List[builtins.str]:
            '''The custom ML member abilities for a collaboration member.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-mlmemberabilities.html#cfn-cleanrooms-collaboration-mlmemberabilities-custommlmemberabilities
            '''
            result = self._values.get("custom_ml_member_abilities")
            assert result is not None, "Required property 'custom_ml_member_abilities' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MLMemberAbilitiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnCollaboration.MLPaymentConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "model_inference": "modelInference",
            "model_training": "modelTraining",
        },
    )
    class MLPaymentConfigProperty:
        def __init__(
            self,
            *,
            model_inference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCollaboration.ModelInferencePaymentConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            model_training: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCollaboration.ModelTrainingPaymentConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An object representing the collaboration member's machine learning payment responsibilities set by the collaboration creator.

            :param model_inference: The payment responsibilities accepted by the member for model inference.
            :param model_training: The payment responsibilities accepted by the member for model training.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-mlpaymentconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                m_lPayment_config_property = cleanrooms.CfnCollaboration.MLPaymentConfigProperty(
                    model_inference=cleanrooms.CfnCollaboration.ModelInferencePaymentConfigProperty(
                        is_responsible=False
                    ),
                    model_training=cleanrooms.CfnCollaboration.ModelTrainingPaymentConfigProperty(
                        is_responsible=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__271514c890ff476984844077519496f6cd7107081ee5259613350b060c9bb355)
                check_type(argname="argument model_inference", value=model_inference, expected_type=type_hints["model_inference"])
                check_type(argname="argument model_training", value=model_training, expected_type=type_hints["model_training"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if model_inference is not None:
                self._values["model_inference"] = model_inference
            if model_training is not None:
                self._values["model_training"] = model_training

        @builtins.property
        def model_inference(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.ModelInferencePaymentConfigProperty"]]:
            '''The payment responsibilities accepted by the member for model inference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-mlpaymentconfig.html#cfn-cleanrooms-collaboration-mlpaymentconfig-modelinference
            '''
            result = self._values.get("model_inference")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.ModelInferencePaymentConfigProperty"]], result)

        @builtins.property
        def model_training(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.ModelTrainingPaymentConfigProperty"]]:
            '''The payment responsibilities accepted by the member for model training.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-mlpaymentconfig.html#cfn-cleanrooms-collaboration-mlpaymentconfig-modeltraining
            '''
            result = self._values.get("model_training")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.ModelTrainingPaymentConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MLPaymentConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnCollaboration.MemberSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_id": "accountId",
            "display_name": "displayName",
            "member_abilities": "memberAbilities",
            "ml_member_abilities": "mlMemberAbilities",
            "payment_configuration": "paymentConfiguration",
        },
    )
    class MemberSpecificationProperty:
        def __init__(
            self,
            *,
            account_id: builtins.str,
            display_name: builtins.str,
            member_abilities: typing.Optional[typing.Sequence[builtins.str]] = None,
            ml_member_abilities: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCollaboration.MLMemberAbilitiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            payment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCollaboration.PaymentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Basic metadata used to construct a new member.

            :param account_id: The identifier used to reference members of the collaboration. Currently only supports AWS account ID.
            :param display_name: The member's display name.
            :param member_abilities: The abilities granted to the collaboration member. *Allowed Values* : ``CAN_QUERY`` | ``CAN_RECEIVE_RESULTS``
            :param ml_member_abilities: The ML abilities granted to the collaboration member.
            :param payment_configuration: The collaboration member's payment responsibilities set by the collaboration creator. If the collaboration creator hasn't speciﬁed anyone as the member paying for query compute costs, then the member who can query is the default payer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-memberspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                member_specification_property = cleanrooms.CfnCollaboration.MemberSpecificationProperty(
                    account_id="accountId",
                    display_name="displayName",
                
                    # the properties below are optional
                    member_abilities=["memberAbilities"],
                    ml_member_abilities=cleanrooms.CfnCollaboration.MLMemberAbilitiesProperty(
                        custom_ml_member_abilities=["customMlMemberAbilities"]
                    ),
                    payment_configuration=cleanrooms.CfnCollaboration.PaymentConfigurationProperty(
                        query_compute=cleanrooms.CfnCollaboration.QueryComputePaymentConfigProperty(
                            is_responsible=False
                        ),
                
                        # the properties below are optional
                        job_compute=cleanrooms.CfnCollaboration.JobComputePaymentConfigProperty(
                            is_responsible=False
                        ),
                        machine_learning=cleanrooms.CfnCollaboration.MLPaymentConfigProperty(
                            model_inference=cleanrooms.CfnCollaboration.ModelInferencePaymentConfigProperty(
                                is_responsible=False
                            ),
                            model_training=cleanrooms.CfnCollaboration.ModelTrainingPaymentConfigProperty(
                                is_responsible=False
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2c9d415168b79c297b7313d0c42362a70fed420b1dda08e496b99813fbbd3248)
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
                check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
                check_type(argname="argument member_abilities", value=member_abilities, expected_type=type_hints["member_abilities"])
                check_type(argname="argument ml_member_abilities", value=ml_member_abilities, expected_type=type_hints["ml_member_abilities"])
                check_type(argname="argument payment_configuration", value=payment_configuration, expected_type=type_hints["payment_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_id": account_id,
                "display_name": display_name,
            }
            if member_abilities is not None:
                self._values["member_abilities"] = member_abilities
            if ml_member_abilities is not None:
                self._values["ml_member_abilities"] = ml_member_abilities
            if payment_configuration is not None:
                self._values["payment_configuration"] = payment_configuration

        @builtins.property
        def account_id(self) -> builtins.str:
            '''The identifier used to reference members of the collaboration.

            Currently only supports AWS account ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-memberspecification.html#cfn-cleanrooms-collaboration-memberspecification-accountid
            '''
            result = self._values.get("account_id")
            assert result is not None, "Required property 'account_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def display_name(self) -> builtins.str:
            '''The member's display name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-memberspecification.html#cfn-cleanrooms-collaboration-memberspecification-displayname
            '''
            result = self._values.get("display_name")
            assert result is not None, "Required property 'display_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def member_abilities(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The abilities granted to the collaboration member.

            *Allowed Values* : ``CAN_QUERY`` | ``CAN_RECEIVE_RESULTS``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-memberspecification.html#cfn-cleanrooms-collaboration-memberspecification-memberabilities
            '''
            result = self._values.get("member_abilities")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def ml_member_abilities(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.MLMemberAbilitiesProperty"]]:
            '''The ML abilities granted to the collaboration member.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-memberspecification.html#cfn-cleanrooms-collaboration-memberspecification-mlmemberabilities
            '''
            result = self._values.get("ml_member_abilities")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.MLMemberAbilitiesProperty"]], result)

        @builtins.property
        def payment_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.PaymentConfigurationProperty"]]:
            '''The collaboration member's payment responsibilities set by the collaboration creator.

            If the collaboration creator hasn't speciﬁed anyone as the member paying for query compute costs, then the member who can query is the default payer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-memberspecification.html#cfn-cleanrooms-collaboration-memberspecification-paymentconfiguration
            '''
            result = self._values.get("payment_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.PaymentConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemberSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnCollaboration.ModelInferencePaymentConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"is_responsible": "isResponsible"},
    )
    class ModelInferencePaymentConfigProperty:
        def __init__(
            self,
            *,
            is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''An object representing the collaboration member's model inference payment responsibilities set by the collaboration creator.

            :param is_responsible: Indicates whether the collaboration creator has configured the collaboration member to pay for model inference costs ( ``TRUE`` ) or has not configured the collaboration member to pay for model inference costs ( ``FALSE`` ). Exactly one member can be configured to pay for model inference costs. An error is returned if the collaboration creator sets a ``TRUE`` value for more than one member in the collaboration. If the collaboration creator hasn't specified anyone as the member paying for model inference costs, then the member who can query is the default payer. An error is returned if the collaboration creator sets a ``FALSE`` value for the member who can query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-modelinferencepaymentconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                model_inference_payment_config_property = cleanrooms.CfnCollaboration.ModelInferencePaymentConfigProperty(
                    is_responsible=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__91778bff8fa4786b2dc1aace0c2b468463ac1eb3971264546bddcbfe95dc8a99)
                check_type(argname="argument is_responsible", value=is_responsible, expected_type=type_hints["is_responsible"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "is_responsible": is_responsible,
            }

        @builtins.property
        def is_responsible(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether the collaboration creator has configured the collaboration member to pay for model inference costs ( ``TRUE`` ) or has not configured the collaboration member to pay for model inference costs ( ``FALSE`` ).

            Exactly one member can be configured to pay for model inference costs. An error is returned if the collaboration creator sets a ``TRUE`` value for more than one member in the collaboration.

            If the collaboration creator hasn't specified anyone as the member paying for model inference costs, then the member who can query is the default payer. An error is returned if the collaboration creator sets a ``FALSE`` value for the member who can query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-modelinferencepaymentconfig.html#cfn-cleanrooms-collaboration-modelinferencepaymentconfig-isresponsible
            '''
            result = self._values.get("is_responsible")
            assert result is not None, "Required property 'is_responsible' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelInferencePaymentConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnCollaboration.ModelTrainingPaymentConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"is_responsible": "isResponsible"},
    )
    class ModelTrainingPaymentConfigProperty:
        def __init__(
            self,
            *,
            is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''An object representing the collaboration member's model training payment responsibilities set by the collaboration creator.

            :param is_responsible: Indicates whether the collaboration creator has configured the collaboration member to pay for model training costs ( ``TRUE`` ) or has not configured the collaboration member to pay for model training costs ( ``FALSE`` ). Exactly one member can be configured to pay for model training costs. An error is returned if the collaboration creator sets a ``TRUE`` value for more than one member in the collaboration. If the collaboration creator hasn't specified anyone as the member paying for model training costs, then the member who can query is the default payer. An error is returned if the collaboration creator sets a ``FALSE`` value for the member who can query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-modeltrainingpaymentconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                model_training_payment_config_property = cleanrooms.CfnCollaboration.ModelTrainingPaymentConfigProperty(
                    is_responsible=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__35cebaf540e2e0f273400ebe690d288c30c23dab0b643fcadc0b6fa47a38e5c1)
                check_type(argname="argument is_responsible", value=is_responsible, expected_type=type_hints["is_responsible"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "is_responsible": is_responsible,
            }

        @builtins.property
        def is_responsible(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether the collaboration creator has configured the collaboration member to pay for model training costs ( ``TRUE`` ) or has not configured the collaboration member to pay for model training costs ( ``FALSE`` ).

            Exactly one member can be configured to pay for model training costs. An error is returned if the collaboration creator sets a ``TRUE`` value for more than one member in the collaboration.

            If the collaboration creator hasn't specified anyone as the member paying for model training costs, then the member who can query is the default payer. An error is returned if the collaboration creator sets a ``FALSE`` value for the member who can query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-modeltrainingpaymentconfig.html#cfn-cleanrooms-collaboration-modeltrainingpaymentconfig-isresponsible
            '''
            result = self._values.get("is_responsible")
            assert result is not None, "Required property 'is_responsible' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelTrainingPaymentConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnCollaboration.PaymentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "query_compute": "queryCompute",
            "job_compute": "jobCompute",
            "machine_learning": "machineLearning",
        },
    )
    class PaymentConfigurationProperty:
        def __init__(
            self,
            *,
            query_compute: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCollaboration.QueryComputePaymentConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            job_compute: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCollaboration.JobComputePaymentConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            machine_learning: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCollaboration.MLPaymentConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An object representing the collaboration member's payment responsibilities set by the collaboration creator.

            :param query_compute: The collaboration member's payment responsibilities set by the collaboration creator for query compute costs.
            :param job_compute: The compute configuration for the job.
            :param machine_learning: An object representing the collaboration member's machine learning payment responsibilities set by the collaboration creator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-paymentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                payment_configuration_property = cleanrooms.CfnCollaboration.PaymentConfigurationProperty(
                    query_compute=cleanrooms.CfnCollaboration.QueryComputePaymentConfigProperty(
                        is_responsible=False
                    ),
                
                    # the properties below are optional
                    job_compute=cleanrooms.CfnCollaboration.JobComputePaymentConfigProperty(
                        is_responsible=False
                    ),
                    machine_learning=cleanrooms.CfnCollaboration.MLPaymentConfigProperty(
                        model_inference=cleanrooms.CfnCollaboration.ModelInferencePaymentConfigProperty(
                            is_responsible=False
                        ),
                        model_training=cleanrooms.CfnCollaboration.ModelTrainingPaymentConfigProperty(
                            is_responsible=False
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4bb111eda28dfc76cbd93dac49286726320cc654bfb530550f97b9ec4cf32cbf)
                check_type(argname="argument query_compute", value=query_compute, expected_type=type_hints["query_compute"])
                check_type(argname="argument job_compute", value=job_compute, expected_type=type_hints["job_compute"])
                check_type(argname="argument machine_learning", value=machine_learning, expected_type=type_hints["machine_learning"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "query_compute": query_compute,
            }
            if job_compute is not None:
                self._values["job_compute"] = job_compute
            if machine_learning is not None:
                self._values["machine_learning"] = machine_learning

        @builtins.property
        def query_compute(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCollaboration.QueryComputePaymentConfigProperty"]:
            '''The collaboration member's payment responsibilities set by the collaboration creator for query compute costs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-paymentconfiguration.html#cfn-cleanrooms-collaboration-paymentconfiguration-querycompute
            '''
            result = self._values.get("query_compute")
            assert result is not None, "Required property 'query_compute' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCollaboration.QueryComputePaymentConfigProperty"], result)

        @builtins.property
        def job_compute(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.JobComputePaymentConfigProperty"]]:
            '''The compute configuration for the job.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-paymentconfiguration.html#cfn-cleanrooms-collaboration-paymentconfiguration-jobcompute
            '''
            result = self._values.get("job_compute")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.JobComputePaymentConfigProperty"]], result)

        @builtins.property
        def machine_learning(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.MLPaymentConfigProperty"]]:
            '''An object representing the collaboration member's machine learning payment responsibilities set by the collaboration creator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-paymentconfiguration.html#cfn-cleanrooms-collaboration-paymentconfiguration-machinelearning
            '''
            result = self._values.get("machine_learning")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCollaboration.MLPaymentConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PaymentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnCollaboration.QueryComputePaymentConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"is_responsible": "isResponsible"},
    )
    class QueryComputePaymentConfigProperty:
        def __init__(
            self,
            *,
            is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''An object representing the collaboration member's payment responsibilities set by the collaboration creator for query compute costs.

            :param is_responsible: Indicates whether the collaboration creator has configured the collaboration member to pay for query compute costs ( ``TRUE`` ) or has not configured the collaboration member to pay for query compute costs ( ``FALSE`` ). Exactly one member can be configured to pay for query compute costs. An error is returned if the collaboration creator sets a ``TRUE`` value for more than one member in the collaboration. If the collaboration creator hasn't specified anyone as the member paying for query compute costs, then the member who can query is the default payer. An error is returned if the collaboration creator sets a ``FALSE`` value for the member who can query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-querycomputepaymentconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                query_compute_payment_config_property = cleanrooms.CfnCollaboration.QueryComputePaymentConfigProperty(
                    is_responsible=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__691566df57f98e85a0cab7f982a0bb63684a2747f18e19d599214bacc63437b2)
                check_type(argname="argument is_responsible", value=is_responsible, expected_type=type_hints["is_responsible"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "is_responsible": is_responsible,
            }

        @builtins.property
        def is_responsible(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether the collaboration creator has configured the collaboration member to pay for query compute costs ( ``TRUE`` ) or has not configured the collaboration member to pay for query compute costs ( ``FALSE`` ).

            Exactly one member can be configured to pay for query compute costs. An error is returned if the collaboration creator sets a ``TRUE`` value for more than one member in the collaboration.

            If the collaboration creator hasn't specified anyone as the member paying for query compute costs, then the member who can query is the default payer. An error is returned if the collaboration creator sets a ``FALSE`` value for the member who can query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-collaboration-querycomputepaymentconfig.html#cfn-cleanrooms-collaboration-querycomputepaymentconfig-isresponsible
            '''
            result = self._values.get("is_responsible")
            assert result is not None, "Required property 'is_responsible' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueryComputePaymentConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnCollaborationProps",
    jsii_struct_bases=[],
    name_mapping={
        "creator_display_name": "creatorDisplayName",
        "description": "description",
        "name": "name",
        "query_log_status": "queryLogStatus",
        "analytics_engine": "analyticsEngine",
        "creator_member_abilities": "creatorMemberAbilities",
        "creator_ml_member_abilities": "creatorMlMemberAbilities",
        "creator_payment_configuration": "creatorPaymentConfiguration",
        "data_encryption_metadata": "dataEncryptionMetadata",
        "job_log_status": "jobLogStatus",
        "members": "members",
        "tags": "tags",
    },
)
class CfnCollaborationProps:
    def __init__(
        self,
        *,
        creator_display_name: builtins.str,
        description: builtins.str,
        name: builtins.str,
        query_log_status: builtins.str,
        analytics_engine: typing.Optional[builtins.str] = None,
        creator_member_abilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        creator_ml_member_abilities: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.MLMemberAbilitiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        creator_payment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.PaymentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        data_encryption_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.DataEncryptionMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        job_log_status: typing.Optional[builtins.str] = None,
        members: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.MemberSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCollaboration``.

        :param creator_display_name: A display name of the collaboration creator.
        :param description: A description of the collaboration provided by the collaboration owner.
        :param name: A human-readable identifier provided by the collaboration owner. Display names are not unique.
        :param query_log_status: An indicator as to whether query logging has been enabled or disabled for the collaboration. When ``ENABLED`` , AWS Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is ``DISABLED`` .
        :param analytics_engine: The analytics engine for the collaboration. .. epigraph:: After July 16, 2025, the ``CLEAN_ROOMS_SQL`` parameter will no longer be available.
        :param creator_member_abilities: The abilities granted to the collaboration creator. *Allowed values* ``CAN_QUERY`` | ``CAN_RECEIVE_RESULTS`` | ``CAN_RUN_JOB``
        :param creator_ml_member_abilities: The ML member abilities for a collaboration member.
        :param creator_payment_configuration: An object representing the collaboration member's payment responsibilities set by the collaboration creator.
        :param data_encryption_metadata: The settings for client-side encryption for cryptographic computing.
        :param job_log_status: An indicator as to whether job logging has been enabled or disabled for the collaboration. When ``ENABLED`` , AWS Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is ``DISABLED`` .
        :param members: A list of initial members, not including the creator. This list is immutable.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanrooms as cleanrooms
            
            cfn_collaboration_props = cleanrooms.CfnCollaborationProps(
                creator_display_name="creatorDisplayName",
                description="description",
                name="name",
                query_log_status="queryLogStatus",
            
                # the properties below are optional
                analytics_engine="analyticsEngine",
                creator_member_abilities=["creatorMemberAbilities"],
                creator_ml_member_abilities=cleanrooms.CfnCollaboration.MLMemberAbilitiesProperty(
                    custom_ml_member_abilities=["customMlMemberAbilities"]
                ),
                creator_payment_configuration=cleanrooms.CfnCollaboration.PaymentConfigurationProperty(
                    query_compute=cleanrooms.CfnCollaboration.QueryComputePaymentConfigProperty(
                        is_responsible=False
                    ),
            
                    # the properties below are optional
                    job_compute=cleanrooms.CfnCollaboration.JobComputePaymentConfigProperty(
                        is_responsible=False
                    ),
                    machine_learning=cleanrooms.CfnCollaboration.MLPaymentConfigProperty(
                        model_inference=cleanrooms.CfnCollaboration.ModelInferencePaymentConfigProperty(
                            is_responsible=False
                        ),
                        model_training=cleanrooms.CfnCollaboration.ModelTrainingPaymentConfigProperty(
                            is_responsible=False
                        )
                    )
                ),
                data_encryption_metadata=cleanrooms.CfnCollaboration.DataEncryptionMetadataProperty(
                    allow_cleartext=False,
                    allow_duplicates=False,
                    allow_joins_on_columns_with_different_names=False,
                    preserve_nulls=False
                ),
                job_log_status="jobLogStatus",
                members=[cleanrooms.CfnCollaboration.MemberSpecificationProperty(
                    account_id="accountId",
                    display_name="displayName",
            
                    # the properties below are optional
                    member_abilities=["memberAbilities"],
                    ml_member_abilities=cleanrooms.CfnCollaboration.MLMemberAbilitiesProperty(
                        custom_ml_member_abilities=["customMlMemberAbilities"]
                    ),
                    payment_configuration=cleanrooms.CfnCollaboration.PaymentConfigurationProperty(
                        query_compute=cleanrooms.CfnCollaboration.QueryComputePaymentConfigProperty(
                            is_responsible=False
                        ),
            
                        # the properties below are optional
                        job_compute=cleanrooms.CfnCollaboration.JobComputePaymentConfigProperty(
                            is_responsible=False
                        ),
                        machine_learning=cleanrooms.CfnCollaboration.MLPaymentConfigProperty(
                            model_inference=cleanrooms.CfnCollaboration.ModelInferencePaymentConfigProperty(
                                is_responsible=False
                            ),
                            model_training=cleanrooms.CfnCollaboration.ModelTrainingPaymentConfigProperty(
                                is_responsible=False
                            )
                        )
                    )
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2049291a9933df94c4258b33838a3aa8100d0214a4519c3d84e6d70ed724c55d)
            check_type(argname="argument creator_display_name", value=creator_display_name, expected_type=type_hints["creator_display_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query_log_status", value=query_log_status, expected_type=type_hints["query_log_status"])
            check_type(argname="argument analytics_engine", value=analytics_engine, expected_type=type_hints["analytics_engine"])
            check_type(argname="argument creator_member_abilities", value=creator_member_abilities, expected_type=type_hints["creator_member_abilities"])
            check_type(argname="argument creator_ml_member_abilities", value=creator_ml_member_abilities, expected_type=type_hints["creator_ml_member_abilities"])
            check_type(argname="argument creator_payment_configuration", value=creator_payment_configuration, expected_type=type_hints["creator_payment_configuration"])
            check_type(argname="argument data_encryption_metadata", value=data_encryption_metadata, expected_type=type_hints["data_encryption_metadata"])
            check_type(argname="argument job_log_status", value=job_log_status, expected_type=type_hints["job_log_status"])
            check_type(argname="argument members", value=members, expected_type=type_hints["members"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "creator_display_name": creator_display_name,
            "description": description,
            "name": name,
            "query_log_status": query_log_status,
        }
        if analytics_engine is not None:
            self._values["analytics_engine"] = analytics_engine
        if creator_member_abilities is not None:
            self._values["creator_member_abilities"] = creator_member_abilities
        if creator_ml_member_abilities is not None:
            self._values["creator_ml_member_abilities"] = creator_ml_member_abilities
        if creator_payment_configuration is not None:
            self._values["creator_payment_configuration"] = creator_payment_configuration
        if data_encryption_metadata is not None:
            self._values["data_encryption_metadata"] = data_encryption_metadata
        if job_log_status is not None:
            self._values["job_log_status"] = job_log_status
        if members is not None:
            self._values["members"] = members
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def creator_display_name(self) -> builtins.str:
        '''A display name of the collaboration creator.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-creatordisplayname
        '''
        result = self._values.get("creator_display_name")
        assert result is not None, "Required property 'creator_display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> builtins.str:
        '''A description of the collaboration provided by the collaboration owner.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A human-readable identifier provided by the collaboration owner.

        Display names are not unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_log_status(self) -> builtins.str:
        '''An indicator as to whether query logging has been enabled or disabled for the collaboration.

        When ``ENABLED`` , AWS Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is ``DISABLED`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-querylogstatus
        '''
        result = self._values.get("query_log_status")
        assert result is not None, "Required property 'query_log_status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def analytics_engine(self) -> typing.Optional[builtins.str]:
        '''The analytics engine for the collaboration.

        .. epigraph::

           After July 16, 2025, the ``CLEAN_ROOMS_SQL`` parameter will no longer be available.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-analyticsengine
        '''
        result = self._values.get("analytics_engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creator_member_abilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The abilities granted to the collaboration creator.

        *Allowed values* ``CAN_QUERY`` | ``CAN_RECEIVE_RESULTS`` | ``CAN_RUN_JOB``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-creatormemberabilities
        '''
        result = self._values.get("creator_member_abilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def creator_ml_member_abilities(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCollaboration.MLMemberAbilitiesProperty]]:
        '''The ML member abilities for a collaboration member.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-creatormlmemberabilities
        '''
        result = self._values.get("creator_ml_member_abilities")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCollaboration.MLMemberAbilitiesProperty]], result)

    @builtins.property
    def creator_payment_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCollaboration.PaymentConfigurationProperty]]:
        '''An object representing the collaboration member's payment responsibilities set by the collaboration creator.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-creatorpaymentconfiguration
        '''
        result = self._values.get("creator_payment_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCollaboration.PaymentConfigurationProperty]], result)

    @builtins.property
    def data_encryption_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCollaboration.DataEncryptionMetadataProperty]]:
        '''The settings for client-side encryption for cryptographic computing.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-dataencryptionmetadata
        '''
        result = self._values.get("data_encryption_metadata")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCollaboration.DataEncryptionMetadataProperty]], result)

    @builtins.property
    def job_log_status(self) -> typing.Optional[builtins.str]:
        '''An indicator as to whether job logging has been enabled or disabled for the collaboration.

        When ``ENABLED`` , AWS Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is ``DISABLED`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-joblogstatus
        '''
        result = self._values.get("job_log_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def members(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCollaboration.MemberSpecificationProperty]]]]:
        '''A list of initial members, not including the creator.

        This list is immutable.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-members
        '''
        result = self._values.get("members")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCollaboration.MemberSpecificationProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.

        Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-collaboration.html#cfn-cleanrooms-collaboration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollaborationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnConfiguredTable(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable",
):
    '''Creates a new configured table resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html
    :cloudformationResource: AWS::CleanRooms::ConfiguredTable
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanrooms as cleanrooms
        
        cfn_configured_table = cleanrooms.CfnConfiguredTable(self, "MyCfnConfiguredTable",
            allowed_columns=["allowedColumns"],
            analysis_method="analysisMethod",
            name="name",
            table_reference=cleanrooms.CfnConfiguredTable.TableReferenceProperty(
                athena=cleanrooms.CfnConfiguredTable.AthenaTableReferenceProperty(
                    database_name="databaseName",
                    table_name="tableName",
                    work_group="workGroup",
        
                    # the properties below are optional
                    output_location="outputLocation"
                ),
                glue=cleanrooms.CfnConfiguredTable.GlueTableReferenceProperty(
                    database_name="databaseName",
                    table_name="tableName"
                ),
                snowflake=cleanrooms.CfnConfiguredTable.SnowflakeTableReferenceProperty(
                    account_identifier="accountIdentifier",
                    database_name="databaseName",
                    schema_name="schemaName",
                    secret_arn="secretArn",
                    table_name="tableName",
                    table_schema=cleanrooms.CfnConfiguredTable.SnowflakeTableSchemaProperty(
                        v1=[cleanrooms.CfnConfiguredTable.SnowflakeTableSchemaV1Property(
                            column_name="columnName",
                            column_type="columnType"
                        )]
                    )
                )
            ),
        
            # the properties below are optional
            analysis_rules=[cleanrooms.CfnConfiguredTable.AnalysisRuleProperty(
                policy=cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty(
                    v1=cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property(
                        aggregation=cleanrooms.CfnConfiguredTable.AnalysisRuleAggregationProperty(
                            aggregate_columns=[cleanrooms.CfnConfiguredTable.AggregateColumnProperty(
                                column_names=["columnNames"],
                                function="function"
                            )],
                            dimension_columns=["dimensionColumns"],
                            join_columns=["joinColumns"],
                            output_constraints=[cleanrooms.CfnConfiguredTable.AggregationConstraintProperty(
                                column_name="columnName",
                                minimum=123,
                                type="type"
                            )],
                            scalar_functions=["scalarFunctions"],
        
                            # the properties below are optional
                            additional_analyses="additionalAnalyses",
                            allowed_join_operators=["allowedJoinOperators"],
                            join_required="joinRequired"
                        ),
                        custom=cleanrooms.CfnConfiguredTable.AnalysisRuleCustomProperty(
                            allowed_analyses=["allowedAnalyses"],
        
                            # the properties below are optional
                            additional_analyses="additionalAnalyses",
                            allowed_analysis_providers=["allowedAnalysisProviders"],
                            differential_privacy=cleanrooms.CfnConfiguredTable.DifferentialPrivacyProperty(
                                columns=[cleanrooms.CfnConfiguredTable.DifferentialPrivacyColumnProperty(
                                    name="name"
                                )]
                            ),
                            disallowed_output_columns=["disallowedOutputColumns"]
                        ),
                        list=cleanrooms.CfnConfiguredTable.AnalysisRuleListProperty(
                            join_columns=["joinColumns"],
                            list_columns=["listColumns"],
        
                            # the properties below are optional
                            additional_analyses="additionalAnalyses",
                            allowed_join_operators=["allowedJoinOperators"]
                        )
                    )
                ),
                type="type"
            )],
            description="description",
            selected_analysis_methods=["selectedAnalysisMethods"],
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
        allowed_columns: typing.Sequence[builtins.str],
        analysis_method: builtins.str,
        name: builtins.str,
        table_reference: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.TableReferenceProperty", typing.Dict[builtins.str, typing.Any]]],
        analysis_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.AnalysisRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        selected_analysis_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param allowed_columns: The columns within the underlying AWS Glue table that can be utilized within collaborations.
        :param analysis_method: The analysis method for the configured table. ``DIRECT_QUERY`` allows SQL queries to be run directly on this table. ``DIRECT_JOB`` allows PySpark jobs to be run directly on this table. ``MULTIPLE`` allows both SQL queries and PySpark jobs to be run directly on this table.
        :param name: A name for the configured table.
        :param table_reference: The table that this configured table represents.
        :param analysis_rules: The analysis rule that was created for the configured table.
        :param description: A description for the configured table.
        :param selected_analysis_methods: The selected analysis methods for the configured table.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6da68c3fc7e3c0674ddb5e2082cfb964074dd6f86f1df6dfcede15001d6f1259)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfiguredTableProps(
            allowed_columns=allowed_columns,
            analysis_method=analysis_method,
            name=name,
            table_reference=table_reference,
            analysis_rules=analysis_rules,
            description=description,
            selected_analysis_methods=selected_analysis_methods,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fecfad26837cc2fdccacfdfb035a18dcac563292f6d300d8052bc89207ae04fe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5c9224380ccb774fe3599e8c47969dd65412118923ba36f2fc0d722c916638e)
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
        '''Returns the Amazon Resource Name (ARN) of the specified configured table.

        Example: ``arn:aws:cleanrooms:us-east-1:111122223333:configuredtable/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrConfiguredTableIdentifier")
    def attr_configured_table_identifier(self) -> builtins.str:
        '''Returns the unique identifier of the specified configured table.

        Example: ``a1b2c3d4-5678-90ab-cdef-EXAMPLE33333``

        :cloudformationAttribute: ConfiguredTableIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfiguredTableIdentifier"))

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
    @jsii.member(jsii_name="allowedColumns")
    def allowed_columns(self) -> typing.List[builtins.str]:
        '''The columns within the underlying AWS Glue table that can be utilized within collaborations.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedColumns"))

    @allowed_columns.setter
    def allowed_columns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46e6aec85126d8c2d12db0e5442b4d56c199d90e95cd9b98b1c92b7652d7c7eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedColumns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="analysisMethod")
    def analysis_method(self) -> builtins.str:
        '''The analysis method for the configured table.'''
        return typing.cast(builtins.str, jsii.get(self, "analysisMethod"))

    @analysis_method.setter
    def analysis_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dd16c3f5e30018a39bada3627e112c5d99eea9283a9ad2de82b9790911c3169)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "analysisMethod", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the configured table.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8743fd9932eb6c0afe523245bfc3bc611bed75b8e179806716cdbd7e1e97f817)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tableReference")
    def table_reference(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.TableReferenceProperty"]:
        '''The table that this configured table represents.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.TableReferenceProperty"], jsii.get(self, "tableReference"))

    @table_reference.setter
    def table_reference(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.TableReferenceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81f7eaa704c6766bfee1be9d2d2b0c8cc4751fd3eb996d6d9902238bdc710232)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableReference", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="analysisRules")
    def analysis_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleProperty"]]]]:
        '''The analysis rule that was created for the configured table.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleProperty"]]]], jsii.get(self, "analysisRules"))

    @analysis_rules.setter
    def analysis_rules(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26267c9443103a44d253b803cbd021f980a5d2b9c34ee95ca6dfc809fab0f1e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "analysisRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the configured table.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c8634d59e391cfec8341b7e4b408bb2c2335c7e17e4ff15bc5f5d8abc23fd91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="selectedAnalysisMethods")
    def selected_analysis_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The selected analysis methods for the configured table.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "selectedAnalysisMethods"))

    @selected_analysis_methods.setter
    def selected_analysis_methods(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c04ca44ac5848879bc3057033050f0e47ffad283431a7189392ca761ec64d2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectedAnalysisMethods", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3a9395564381a20388411d14ffd2bda7a4d604b2cf7bf643f5e5bd129bdd0f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.AggregateColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"column_names": "columnNames", "function": "function"},
    )
    class AggregateColumnProperty:
        def __init__(
            self,
            *,
            column_names: typing.Sequence[builtins.str],
            function: builtins.str,
        ) -> None:
            '''Column in configured table that can be used in aggregate function in query.

            :param column_names: Column names in configured table of aggregate columns.
            :param function: Aggregation function that can be applied to aggregate column in query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregatecolumn.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                aggregate_column_property = cleanrooms.CfnConfiguredTable.AggregateColumnProperty(
                    column_names=["columnNames"],
                    function="function"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa417839f91cf8cc845476ca63e8e1d38ea951bbc307aaa969fdea5be7e16893)
                check_type(argname="argument column_names", value=column_names, expected_type=type_hints["column_names"])
                check_type(argname="argument function", value=function, expected_type=type_hints["function"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "column_names": column_names,
                "function": function,
            }

        @builtins.property
        def column_names(self) -> typing.List[builtins.str]:
            '''Column names in configured table of aggregate columns.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregatecolumn.html#cfn-cleanrooms-configuredtable-aggregatecolumn-columnnames
            '''
            result = self._values.get("column_names")
            assert result is not None, "Required property 'column_names' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def function(self) -> builtins.str:
            '''Aggregation function that can be applied to aggregate column in query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregatecolumn.html#cfn-cleanrooms-configuredtable-aggregatecolumn-function
            '''
            result = self._values.get("function")
            assert result is not None, "Required property 'function' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AggregateColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.AggregationConstraintProperty",
        jsii_struct_bases=[],
        name_mapping={
            "column_name": "columnName",
            "minimum": "minimum",
            "type": "type",
        },
    )
    class AggregationConstraintProperty:
        def __init__(
            self,
            *,
            column_name: builtins.str,
            minimum: jsii.Number,
            type: builtins.str,
        ) -> None:
            '''Constraint on query output removing output rows that do not meet a minimum number of distinct values of a specified column.

            :param column_name: Column in aggregation constraint for which there must be a minimum number of distinct values in an output row for it to be in the query output.
            :param minimum: The minimum number of distinct values that an output row must be an aggregation of. Minimum threshold of distinct values for a specified column that must exist in an output row for it to be in the query output.
            :param type: The type of aggregation the constraint allows. The only valid value is currently ``COUNT_DISTINCT``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregationconstraint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                aggregation_constraint_property = cleanrooms.CfnConfiguredTable.AggregationConstraintProperty(
                    column_name="columnName",
                    minimum=123,
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63f1cc4359753a41914fdd91e80c9746bf76bc8ab990f1c207bf527199e05de5)
                check_type(argname="argument column_name", value=column_name, expected_type=type_hints["column_name"])
                check_type(argname="argument minimum", value=minimum, expected_type=type_hints["minimum"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "column_name": column_name,
                "minimum": minimum,
                "type": type,
            }

        @builtins.property
        def column_name(self) -> builtins.str:
            '''Column in aggregation constraint for which there must be a minimum number of distinct values in an output row for it to be in the query output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregationconstraint.html#cfn-cleanrooms-configuredtable-aggregationconstraint-columnname
            '''
            result = self._values.get("column_name")
            assert result is not None, "Required property 'column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def minimum(self) -> jsii.Number:
            '''The minimum number of distinct values that an output row must be an aggregation of.

            Minimum threshold of distinct values for a specified column that must exist in an output row for it to be in the query output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregationconstraint.html#cfn-cleanrooms-configuredtable-aggregationconstraint-minimum
            '''
            result = self._values.get("minimum")
            assert result is not None, "Required property 'minimum' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of aggregation the constraint allows.

            The only valid value is currently ``COUNT_DISTINCT``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-aggregationconstraint.html#cfn-cleanrooms-configuredtable-aggregationconstraint-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AggregationConstraintProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.AnalysisRuleAggregationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aggregate_columns": "aggregateColumns",
            "dimension_columns": "dimensionColumns",
            "join_columns": "joinColumns",
            "output_constraints": "outputConstraints",
            "scalar_functions": "scalarFunctions",
            "additional_analyses": "additionalAnalyses",
            "allowed_join_operators": "allowedJoinOperators",
            "join_required": "joinRequired",
        },
    )
    class AnalysisRuleAggregationProperty:
        def __init__(
            self,
            *,
            aggregate_columns: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.AggregateColumnProperty", typing.Dict[builtins.str, typing.Any]]]]],
            dimension_columns: typing.Sequence[builtins.str],
            join_columns: typing.Sequence[builtins.str],
            output_constraints: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.AggregationConstraintProperty", typing.Dict[builtins.str, typing.Any]]]]],
            scalar_functions: typing.Sequence[builtins.str],
            additional_analyses: typing.Optional[builtins.str] = None,
            allowed_join_operators: typing.Optional[typing.Sequence[builtins.str]] = None,
            join_required: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A type of analysis rule that enables query structure and specified queries that produce aggregate statistics.

            :param aggregate_columns: The columns that query runners are allowed to use in aggregation queries.
            :param dimension_columns: The columns that query runners are allowed to select, group by, or filter by.
            :param join_columns: Columns in configured table that can be used in join statements and/or as aggregate columns. They can never be outputted directly.
            :param output_constraints: Columns that must meet a specific threshold value (after an aggregation function is applied to it) for each output row to be returned.
            :param scalar_functions: Set of scalar functions that are allowed to be used on dimension columns and the output of aggregation of metrics.
            :param additional_analyses: An indicator as to whether additional analyses (such as AWS Clean Rooms ML) can be applied to the output of the direct query. The ``additionalAnalyses`` parameter is currently supported for the list analysis rule ( ``AnalysisRuleList`` ) and the custom analysis rule ( ``AnalysisRuleCustom`` ).
            :param allowed_join_operators: Which logical operators (if any) are to be used in an INNER JOIN match condition. Default is ``AND`` .
            :param join_required: Control that requires member who runs query to do a join with their configured table and/or other configured table in query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                analysis_rule_aggregation_property = cleanrooms.CfnConfiguredTable.AnalysisRuleAggregationProperty(
                    aggregate_columns=[cleanrooms.CfnConfiguredTable.AggregateColumnProperty(
                        column_names=["columnNames"],
                        function="function"
                    )],
                    dimension_columns=["dimensionColumns"],
                    join_columns=["joinColumns"],
                    output_constraints=[cleanrooms.CfnConfiguredTable.AggregationConstraintProperty(
                        column_name="columnName",
                        minimum=123,
                        type="type"
                    )],
                    scalar_functions=["scalarFunctions"],
                
                    # the properties below are optional
                    additional_analyses="additionalAnalyses",
                    allowed_join_operators=["allowedJoinOperators"],
                    join_required="joinRequired"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7c88de0a4314f12e0bbceae5eb6edd232a937dc4a6b95c8eb383dabc0231d87e)
                check_type(argname="argument aggregate_columns", value=aggregate_columns, expected_type=type_hints["aggregate_columns"])
                check_type(argname="argument dimension_columns", value=dimension_columns, expected_type=type_hints["dimension_columns"])
                check_type(argname="argument join_columns", value=join_columns, expected_type=type_hints["join_columns"])
                check_type(argname="argument output_constraints", value=output_constraints, expected_type=type_hints["output_constraints"])
                check_type(argname="argument scalar_functions", value=scalar_functions, expected_type=type_hints["scalar_functions"])
                check_type(argname="argument additional_analyses", value=additional_analyses, expected_type=type_hints["additional_analyses"])
                check_type(argname="argument allowed_join_operators", value=allowed_join_operators, expected_type=type_hints["allowed_join_operators"])
                check_type(argname="argument join_required", value=join_required, expected_type=type_hints["join_required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "aggregate_columns": aggregate_columns,
                "dimension_columns": dimension_columns,
                "join_columns": join_columns,
                "output_constraints": output_constraints,
                "scalar_functions": scalar_functions,
            }
            if additional_analyses is not None:
                self._values["additional_analyses"] = additional_analyses
            if allowed_join_operators is not None:
                self._values["allowed_join_operators"] = allowed_join_operators
            if join_required is not None:
                self._values["join_required"] = join_required

        @builtins.property
        def aggregate_columns(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AggregateColumnProperty"]]]:
            '''The columns that query runners are allowed to use in aggregation queries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-aggregatecolumns
            '''
            result = self._values.get("aggregate_columns")
            assert result is not None, "Required property 'aggregate_columns' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AggregateColumnProperty"]]], result)

        @builtins.property
        def dimension_columns(self) -> typing.List[builtins.str]:
            '''The columns that query runners are allowed to select, group by, or filter by.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-dimensioncolumns
            '''
            result = self._values.get("dimension_columns")
            assert result is not None, "Required property 'dimension_columns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def join_columns(self) -> typing.List[builtins.str]:
            '''Columns in configured table that can be used in join statements and/or as aggregate columns.

            They can never be outputted directly.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-joincolumns
            '''
            result = self._values.get("join_columns")
            assert result is not None, "Required property 'join_columns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def output_constraints(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AggregationConstraintProperty"]]]:
            '''Columns that must meet a specific threshold value (after an aggregation function is applied to it) for each output row to be returned.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-outputconstraints
            '''
            result = self._values.get("output_constraints")
            assert result is not None, "Required property 'output_constraints' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AggregationConstraintProperty"]]], result)

        @builtins.property
        def scalar_functions(self) -> typing.List[builtins.str]:
            '''Set of scalar functions that are allowed to be used on dimension columns and the output of aggregation of metrics.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-scalarfunctions
            '''
            result = self._values.get("scalar_functions")
            assert result is not None, "Required property 'scalar_functions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def additional_analyses(self) -> typing.Optional[builtins.str]:
            '''An indicator as to whether additional analyses (such as AWS Clean Rooms ML) can be applied to the output of the direct query.

            The ``additionalAnalyses`` parameter is currently supported for the list analysis rule ( ``AnalysisRuleList`` ) and the custom analysis rule ( ``AnalysisRuleCustom`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-additionalanalyses
            '''
            result = self._values.get("additional_analyses")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def allowed_join_operators(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Which logical operators (if any) are to be used in an INNER JOIN match condition.

            Default is ``AND`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-allowedjoinoperators
            '''
            result = self._values.get("allowed_join_operators")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def join_required(self) -> typing.Optional[builtins.str]:
            '''Control that requires member who runs query to do a join with their configured table and/or other configured table in query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisruleaggregation.html#cfn-cleanrooms-configuredtable-analysisruleaggregation-joinrequired
            '''
            result = self._values.get("join_required")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisRuleAggregationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.AnalysisRuleCustomProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allowed_analyses": "allowedAnalyses",
            "additional_analyses": "additionalAnalyses",
            "allowed_analysis_providers": "allowedAnalysisProviders",
            "differential_privacy": "differentialPrivacy",
            "disallowed_output_columns": "disallowedOutputColumns",
        },
    )
    class AnalysisRuleCustomProperty:
        def __init__(
            self,
            *,
            allowed_analyses: typing.Sequence[builtins.str],
            additional_analyses: typing.Optional[builtins.str] = None,
            allowed_analysis_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
            differential_privacy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.DifferentialPrivacyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            disallowed_output_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A type of analysis rule that enables the table owner to approve custom SQL queries on their configured tables.

            It supports differential privacy.

            :param allowed_analyses: The ARN of the analysis templates that are allowed by the custom analysis rule.
            :param additional_analyses: An indicator as to whether additional analyses (such as AWS Clean Rooms ML) can be applied to the output of the direct query.
            :param allowed_analysis_providers: The IDs of the AWS accounts that are allowed to query by the custom analysis rule. Required when ``allowedAnalyses`` is ``ANY_QUERY`` .
            :param differential_privacy: The differential privacy configuration.
            :param disallowed_output_columns: A list of columns that aren't allowed to be shown in the query output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulecustom.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                analysis_rule_custom_property = cleanrooms.CfnConfiguredTable.AnalysisRuleCustomProperty(
                    allowed_analyses=["allowedAnalyses"],
                
                    # the properties below are optional
                    additional_analyses="additionalAnalyses",
                    allowed_analysis_providers=["allowedAnalysisProviders"],
                    differential_privacy=cleanrooms.CfnConfiguredTable.DifferentialPrivacyProperty(
                        columns=[cleanrooms.CfnConfiguredTable.DifferentialPrivacyColumnProperty(
                            name="name"
                        )]
                    ),
                    disallowed_output_columns=["disallowedOutputColumns"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fb34762d0bf6ed014ff8964f15e74deaeb8d3d74c070c1dc20496ef94ed7c8ec)
                check_type(argname="argument allowed_analyses", value=allowed_analyses, expected_type=type_hints["allowed_analyses"])
                check_type(argname="argument additional_analyses", value=additional_analyses, expected_type=type_hints["additional_analyses"])
                check_type(argname="argument allowed_analysis_providers", value=allowed_analysis_providers, expected_type=type_hints["allowed_analysis_providers"])
                check_type(argname="argument differential_privacy", value=differential_privacy, expected_type=type_hints["differential_privacy"])
                check_type(argname="argument disallowed_output_columns", value=disallowed_output_columns, expected_type=type_hints["disallowed_output_columns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allowed_analyses": allowed_analyses,
            }
            if additional_analyses is not None:
                self._values["additional_analyses"] = additional_analyses
            if allowed_analysis_providers is not None:
                self._values["allowed_analysis_providers"] = allowed_analysis_providers
            if differential_privacy is not None:
                self._values["differential_privacy"] = differential_privacy
            if disallowed_output_columns is not None:
                self._values["disallowed_output_columns"] = disallowed_output_columns

        @builtins.property
        def allowed_analyses(self) -> typing.List[builtins.str]:
            '''The ARN of the analysis templates that are allowed by the custom analysis rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulecustom.html#cfn-cleanrooms-configuredtable-analysisrulecustom-allowedanalyses
            '''
            result = self._values.get("allowed_analyses")
            assert result is not None, "Required property 'allowed_analyses' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def additional_analyses(self) -> typing.Optional[builtins.str]:
            '''An indicator as to whether additional analyses (such as AWS Clean Rooms ML) can be applied to the output of the direct query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulecustom.html#cfn-cleanrooms-configuredtable-analysisrulecustom-additionalanalyses
            '''
            result = self._values.get("additional_analyses")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def allowed_analysis_providers(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The IDs of the AWS accounts that are allowed to query by the custom analysis rule.

            Required when ``allowedAnalyses`` is ``ANY_QUERY`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulecustom.html#cfn-cleanrooms-configuredtable-analysisrulecustom-allowedanalysisproviders
            '''
            result = self._values.get("allowed_analysis_providers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def differential_privacy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.DifferentialPrivacyProperty"]]:
            '''The differential privacy configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulecustom.html#cfn-cleanrooms-configuredtable-analysisrulecustom-differentialprivacy
            '''
            result = self._values.get("differential_privacy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.DifferentialPrivacyProperty"]], result)

        @builtins.property
        def disallowed_output_columns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of columns that aren't allowed to be shown in the query output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulecustom.html#cfn-cleanrooms-configuredtable-analysisrulecustom-disallowedoutputcolumns
            '''
            result = self._values.get("disallowed_output_columns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisRuleCustomProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.AnalysisRuleListProperty",
        jsii_struct_bases=[],
        name_mapping={
            "join_columns": "joinColumns",
            "list_columns": "listColumns",
            "additional_analyses": "additionalAnalyses",
            "allowed_join_operators": "allowedJoinOperators",
        },
    )
    class AnalysisRuleListProperty:
        def __init__(
            self,
            *,
            join_columns: typing.Sequence[builtins.str],
            list_columns: typing.Sequence[builtins.str],
            additional_analyses: typing.Optional[builtins.str] = None,
            allowed_join_operators: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A type of analysis rule that enables row-level analysis.

            :param join_columns: Columns that can be used to join a configured table with the table of the member who can query and other members' configured tables.
            :param list_columns: Columns that can be listed in the output.
            :param additional_analyses: An indicator as to whether additional analyses (such as AWS Clean Rooms ML) can be applied to the output of the direct query.
            :param allowed_join_operators: The logical operators (if any) that are to be used in an INNER JOIN match condition. Default is ``AND`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulelist.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                analysis_rule_list_property = cleanrooms.CfnConfiguredTable.AnalysisRuleListProperty(
                    join_columns=["joinColumns"],
                    list_columns=["listColumns"],
                
                    # the properties below are optional
                    additional_analyses="additionalAnalyses",
                    allowed_join_operators=["allowedJoinOperators"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a0accd14fb8407350b8ede83ec532b76a492d21ad538a377f14413f98dae0fba)
                check_type(argname="argument join_columns", value=join_columns, expected_type=type_hints["join_columns"])
                check_type(argname="argument list_columns", value=list_columns, expected_type=type_hints["list_columns"])
                check_type(argname="argument additional_analyses", value=additional_analyses, expected_type=type_hints["additional_analyses"])
                check_type(argname="argument allowed_join_operators", value=allowed_join_operators, expected_type=type_hints["allowed_join_operators"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "join_columns": join_columns,
                "list_columns": list_columns,
            }
            if additional_analyses is not None:
                self._values["additional_analyses"] = additional_analyses
            if allowed_join_operators is not None:
                self._values["allowed_join_operators"] = allowed_join_operators

        @builtins.property
        def join_columns(self) -> typing.List[builtins.str]:
            '''Columns that can be used to join a configured table with the table of the member who can query and other members' configured tables.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulelist.html#cfn-cleanrooms-configuredtable-analysisrulelist-joincolumns
            '''
            result = self._values.get("join_columns")
            assert result is not None, "Required property 'join_columns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def list_columns(self) -> typing.List[builtins.str]:
            '''Columns that can be listed in the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulelist.html#cfn-cleanrooms-configuredtable-analysisrulelist-listcolumns
            '''
            result = self._values.get("list_columns")
            assert result is not None, "Required property 'list_columns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def additional_analyses(self) -> typing.Optional[builtins.str]:
            '''An indicator as to whether additional analyses (such as AWS Clean Rooms ML) can be applied to the output of the direct query.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulelist.html#cfn-cleanrooms-configuredtable-analysisrulelist-additionalanalyses
            '''
            result = self._values.get("additional_analyses")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def allowed_join_operators(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The logical operators (if any) that are to be used in an INNER JOIN match condition.

            Default is ``AND`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrulelist.html#cfn-cleanrooms-configuredtable-analysisrulelist-allowedjoinoperators
            '''
            result = self._values.get("allowed_join_operators")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisRuleListProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.AnalysisRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"policy": "policy", "type": "type"},
    )
    class AnalysisRuleProperty:
        def __init__(
            self,
            *,
            policy: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
        ) -> None:
            '''A specification about how data from the configured table can be used in a query.

            :param policy: A policy that describes the associated data usage limitations.
            :param type: The type of analysis rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                analysis_rule_property = cleanrooms.CfnConfiguredTable.AnalysisRuleProperty(
                    policy=cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty(
                        v1=cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property(
                            aggregation=cleanrooms.CfnConfiguredTable.AnalysisRuleAggregationProperty(
                                aggregate_columns=[cleanrooms.CfnConfiguredTable.AggregateColumnProperty(
                                    column_names=["columnNames"],
                                    function="function"
                                )],
                                dimension_columns=["dimensionColumns"],
                                join_columns=["joinColumns"],
                                output_constraints=[cleanrooms.CfnConfiguredTable.AggregationConstraintProperty(
                                    column_name="columnName",
                                    minimum=123,
                                    type="type"
                                )],
                                scalar_functions=["scalarFunctions"],
                
                                # the properties below are optional
                                additional_analyses="additionalAnalyses",
                                allowed_join_operators=["allowedJoinOperators"],
                                join_required="joinRequired"
                            ),
                            custom=cleanrooms.CfnConfiguredTable.AnalysisRuleCustomProperty(
                                allowed_analyses=["allowedAnalyses"],
                
                                # the properties below are optional
                                additional_analyses="additionalAnalyses",
                                allowed_analysis_providers=["allowedAnalysisProviders"],
                                differential_privacy=cleanrooms.CfnConfiguredTable.DifferentialPrivacyProperty(
                                    columns=[cleanrooms.CfnConfiguredTable.DifferentialPrivacyColumnProperty(
                                        name="name"
                                    )]
                                ),
                                disallowed_output_columns=["disallowedOutputColumns"]
                            ),
                            list=cleanrooms.CfnConfiguredTable.AnalysisRuleListProperty(
                                join_columns=["joinColumns"],
                                list_columns=["listColumns"],
                
                                # the properties below are optional
                                additional_analyses="additionalAnalyses",
                                allowed_join_operators=["allowedJoinOperators"]
                            )
                        )
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__124c3b77588197cdbfdd27c90ac026b586926dd1d223cf478cf9815b95327095)
                check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "policy": policy,
                "type": type,
            }

        @builtins.property
        def policy(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty"]:
            '''A policy that describes the associated data usage limitations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrule.html#cfn-cleanrooms-configuredtable-analysisrule-policy
            '''
            result = self._values.get("policy")
            assert result is not None, "Required property 'policy' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of analysis rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-analysisrule.html#cfn-cleanrooms-configuredtable-analysisrule-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.AthenaTableReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_name": "databaseName",
            "table_name": "tableName",
            "work_group": "workGroup",
            "output_location": "outputLocation",
        },
    )
    class AthenaTableReferenceProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            table_name: builtins.str,
            work_group: builtins.str,
            output_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A reference to a table within Athena.

            :param database_name: The database name.
            :param table_name: The table reference.
            :param work_group: The workgroup of the Athena table reference.
            :param output_location: The output location for the Athena table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-athenatablereference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                athena_table_reference_property = cleanrooms.CfnConfiguredTable.AthenaTableReferenceProperty(
                    database_name="databaseName",
                    table_name="tableName",
                    work_group="workGroup",
                
                    # the properties below are optional
                    output_location="outputLocation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__58a53beb1a0a90ec538b0213243c8721465a73c73f8bf745778a09f20fde15e2)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument work_group", value=work_group, expected_type=type_hints["work_group"])
                check_type(argname="argument output_location", value=output_location, expected_type=type_hints["output_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database_name": database_name,
                "table_name": table_name,
                "work_group": work_group,
            }
            if output_location is not None:
                self._values["output_location"] = output_location

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The database name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-athenatablereference.html#cfn-cleanrooms-configuredtable-athenatablereference-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The table reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-athenatablereference.html#cfn-cleanrooms-configuredtable-athenatablereference-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def work_group(self) -> builtins.str:
            '''The workgroup of the Athena table reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-athenatablereference.html#cfn-cleanrooms-configuredtable-athenatablereference-workgroup
            '''
            result = self._values.get("work_group")
            assert result is not None, "Required property 'work_group' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def output_location(self) -> typing.Optional[builtins.str]:
            '''The output location for the Athena table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-athenatablereference.html#cfn-cleanrooms-configuredtable-athenatablereference-outputlocation
            '''
            result = self._values.get("output_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AthenaTableReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"v1": "v1"},
    )
    class ConfiguredTableAnalysisRulePolicyProperty:
        def __init__(
            self,
            *,
            v1: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Controls on the query specifications that can be run on a configured table.

            :param v1: Controls on the query specifications that can be run on a configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                configured_table_analysis_rule_policy_property = cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty(
                    v1=cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property(
                        aggregation=cleanrooms.CfnConfiguredTable.AnalysisRuleAggregationProperty(
                            aggregate_columns=[cleanrooms.CfnConfiguredTable.AggregateColumnProperty(
                                column_names=["columnNames"],
                                function="function"
                            )],
                            dimension_columns=["dimensionColumns"],
                            join_columns=["joinColumns"],
                            output_constraints=[cleanrooms.CfnConfiguredTable.AggregationConstraintProperty(
                                column_name="columnName",
                                minimum=123,
                                type="type"
                            )],
                            scalar_functions=["scalarFunctions"],
                
                            # the properties below are optional
                            additional_analyses="additionalAnalyses",
                            allowed_join_operators=["allowedJoinOperators"],
                            join_required="joinRequired"
                        ),
                        custom=cleanrooms.CfnConfiguredTable.AnalysisRuleCustomProperty(
                            allowed_analyses=["allowedAnalyses"],
                
                            # the properties below are optional
                            additional_analyses="additionalAnalyses",
                            allowed_analysis_providers=["allowedAnalysisProviders"],
                            differential_privacy=cleanrooms.CfnConfiguredTable.DifferentialPrivacyProperty(
                                columns=[cleanrooms.CfnConfiguredTable.DifferentialPrivacyColumnProperty(
                                    name="name"
                                )]
                            ),
                            disallowed_output_columns=["disallowedOutputColumns"]
                        ),
                        list=cleanrooms.CfnConfiguredTable.AnalysisRuleListProperty(
                            join_columns=["joinColumns"],
                            list_columns=["listColumns"],
                
                            # the properties below are optional
                            additional_analyses="additionalAnalyses",
                            allowed_join_operators=["allowedJoinOperators"]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6f1e3e5a795ca7258552d46676801756cc639b2cf39b0a42555fb510dee59fc1)
                check_type(argname="argument v1", value=v1, expected_type=type_hints["v1"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "v1": v1,
            }

        @builtins.property
        def v1(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property"]:
            '''Controls on the query specifications that can be run on a configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicy.html#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicy-v1
            '''
            result = self._values.get("v1")
            assert result is not None, "Required property 'v1' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfiguredTableAnalysisRulePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property",
        jsii_struct_bases=[],
        name_mapping={
            "aggregation": "aggregation",
            "custom": "custom",
            "list": "list",
        },
    )
    class ConfiguredTableAnalysisRulePolicyV1Property:
        def __init__(
            self,
            *,
            aggregation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.AnalysisRuleAggregationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            custom: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.AnalysisRuleCustomProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.AnalysisRuleListProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Controls on the query specifications that can be run on a configured table.

            :param aggregation: Analysis rule type that enables only aggregation queries on a configured table.
            :param custom: Analysis rule type that enables custom SQL queries on a configured table.
            :param list: Analysis rule type that enables only list queries on a configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                configured_table_analysis_rule_policy_v1_property = cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property(
                    aggregation=cleanrooms.CfnConfiguredTable.AnalysisRuleAggregationProperty(
                        aggregate_columns=[cleanrooms.CfnConfiguredTable.AggregateColumnProperty(
                            column_names=["columnNames"],
                            function="function"
                        )],
                        dimension_columns=["dimensionColumns"],
                        join_columns=["joinColumns"],
                        output_constraints=[cleanrooms.CfnConfiguredTable.AggregationConstraintProperty(
                            column_name="columnName",
                            minimum=123,
                            type="type"
                        )],
                        scalar_functions=["scalarFunctions"],
                
                        # the properties below are optional
                        additional_analyses="additionalAnalyses",
                        allowed_join_operators=["allowedJoinOperators"],
                        join_required="joinRequired"
                    ),
                    custom=cleanrooms.CfnConfiguredTable.AnalysisRuleCustomProperty(
                        allowed_analyses=["allowedAnalyses"],
                
                        # the properties below are optional
                        additional_analyses="additionalAnalyses",
                        allowed_analysis_providers=["allowedAnalysisProviders"],
                        differential_privacy=cleanrooms.CfnConfiguredTable.DifferentialPrivacyProperty(
                            columns=[cleanrooms.CfnConfiguredTable.DifferentialPrivacyColumnProperty(
                                name="name"
                            )]
                        ),
                        disallowed_output_columns=["disallowedOutputColumns"]
                    ),
                    list=cleanrooms.CfnConfiguredTable.AnalysisRuleListProperty(
                        join_columns=["joinColumns"],
                        list_columns=["listColumns"],
                
                        # the properties below are optional
                        additional_analyses="additionalAnalyses",
                        allowed_join_operators=["allowedJoinOperators"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f3e07fc4df9c2eafb409dd0b417b9236aa995940875e48daa983efee06bd45fc)
                check_type(argname="argument aggregation", value=aggregation, expected_type=type_hints["aggregation"])
                check_type(argname="argument custom", value=custom, expected_type=type_hints["custom"])
                check_type(argname="argument list", value=list, expected_type=type_hints["list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aggregation is not None:
                self._values["aggregation"] = aggregation
            if custom is not None:
                self._values["custom"] = custom
            if list is not None:
                self._values["list"] = list

        @builtins.property
        def aggregation(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleAggregationProperty"]]:
            '''Analysis rule type that enables only aggregation queries on a configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1.html#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-aggregation
            '''
            result = self._values.get("aggregation")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleAggregationProperty"]], result)

        @builtins.property
        def custom(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleCustomProperty"]]:
            '''Analysis rule type that enables custom SQL queries on a configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1.html#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-custom
            '''
            result = self._values.get("custom")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleCustomProperty"]], result)

        @builtins.property
        def list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleListProperty"]]:
            '''Analysis rule type that enables only list queries on a configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1.html#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1-list
            '''
            result = self._values.get("list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AnalysisRuleListProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfiguredTableAnalysisRulePolicyV1Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.DifferentialPrivacyColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class DifferentialPrivacyColumnProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''Specifies the name of the column that contains the unique identifier of your users, whose privacy you want to protect.

            :param name: The name of the column, such as user_id, that contains the unique identifier of your users, whose privacy you want to protect. If you want to turn on differential privacy for two or more tables in a collaboration, you must configure the same column as the user identifier column in both analysis rules.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-differentialprivacycolumn.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                differential_privacy_column_property = cleanrooms.CfnConfiguredTable.DifferentialPrivacyColumnProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__db51d35ba24655ba0ff827d1b1f747a981c133aa166ad14ccd1ac62c4aa28235)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the column, such as user_id, that contains the unique identifier of your users, whose privacy you want to protect.

            If you want to turn on differential privacy for two or more tables in a collaboration, you must configure the same column as the user identifier column in both analysis rules.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-differentialprivacycolumn.html#cfn-cleanrooms-configuredtable-differentialprivacycolumn-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DifferentialPrivacyColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.DifferentialPrivacyProperty",
        jsii_struct_bases=[],
        name_mapping={"columns": "columns"},
    )
    class DifferentialPrivacyProperty:
        def __init__(
            self,
            *,
            columns: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.DifferentialPrivacyColumnProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The analysis method allowed for the configured tables.

            ``DIRECT_QUERY`` allows SQL queries to be run directly on this table.

            ``DIRECT_JOB`` allows PySpark jobs to be run directly on this table.

            ``MULTIPLE`` allows both SQL queries and PySpark jobs to be run directly on this table.

            :param columns: The name of the column, such as user_id, that contains the unique identifier of your users, whose privacy you want to protect. If you want to turn on differential privacy for two or more tables in a collaboration, you must configure the same column as the user identifier column in both analysis rules.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-differentialprivacy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                differential_privacy_property = cleanrooms.CfnConfiguredTable.DifferentialPrivacyProperty(
                    columns=[cleanrooms.CfnConfiguredTable.DifferentialPrivacyColumnProperty(
                        name="name"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__25cecdbb678db7c9fecdba89215b89eba238f35861c80f5cb848f3f80ef4e9e7)
                check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "columns": columns,
            }

        @builtins.property
        def columns(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.DifferentialPrivacyColumnProperty"]]]:
            '''The name of the column, such as user_id, that contains the unique identifier of your users, whose privacy you want to protect.

            If you want to turn on differential privacy for two or more tables in a collaboration, you must configure the same column as the user identifier column in both analysis rules.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-differentialprivacy.html#cfn-cleanrooms-configuredtable-differentialprivacy-columns
            '''
            result = self._values.get("columns")
            assert result is not None, "Required property 'columns' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.DifferentialPrivacyColumnProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DifferentialPrivacyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.GlueTableReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"database_name": "databaseName", "table_name": "tableName"},
    )
    class GlueTableReferenceProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            table_name: builtins.str,
        ) -> None:
            '''A reference to a table within an AWS Glue data catalog.

            :param database_name: The name of the database the AWS Glue table belongs to.
            :param table_name: The name of the AWS Glue table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-gluetablereference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                glue_table_reference_property = cleanrooms.CfnConfiguredTable.GlueTableReferenceProperty(
                    database_name="databaseName",
                    table_name="tableName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ad49810a315ae1c04064504cefbb3e0bc6fec52a1add50545955db56f0db50f9)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database_name": database_name,
                "table_name": table_name,
            }

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of the database the AWS Glue table belongs to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-gluetablereference.html#cfn-cleanrooms-configuredtable-gluetablereference-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The name of the AWS Glue table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-gluetablereference.html#cfn-cleanrooms-configuredtable-gluetablereference-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlueTableReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.SnowflakeTableReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_identifier": "accountIdentifier",
            "database_name": "databaseName",
            "schema_name": "schemaName",
            "secret_arn": "secretArn",
            "table_name": "tableName",
            "table_schema": "tableSchema",
        },
    )
    class SnowflakeTableReferenceProperty:
        def __init__(
            self,
            *,
            account_identifier: builtins.str,
            database_name: builtins.str,
            schema_name: builtins.str,
            secret_arn: builtins.str,
            table_name: builtins.str,
            table_schema: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.SnowflakeTableSchemaProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A reference to a table within Snowflake.

            :param account_identifier: The account identifier for the Snowflake table reference.
            :param database_name: The name of the database the Snowflake table belongs to.
            :param schema_name: The schema name of the Snowflake table reference.
            :param secret_arn: The secret ARN of the Snowflake table reference.
            :param table_name: The name of the Snowflake table.
            :param table_schema: The schema of the Snowflake table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-snowflaketablereference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                snowflake_table_reference_property = cleanrooms.CfnConfiguredTable.SnowflakeTableReferenceProperty(
                    account_identifier="accountIdentifier",
                    database_name="databaseName",
                    schema_name="schemaName",
                    secret_arn="secretArn",
                    table_name="tableName",
                    table_schema=cleanrooms.CfnConfiguredTable.SnowflakeTableSchemaProperty(
                        v1=[cleanrooms.CfnConfiguredTable.SnowflakeTableSchemaV1Property(
                            column_name="columnName",
                            column_type="columnType"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0bac88ed34f9327592c380e538ab50720af8f52dd5162e61df0aec6adf2833a)
                check_type(argname="argument account_identifier", value=account_identifier, expected_type=type_hints["account_identifier"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument table_schema", value=table_schema, expected_type=type_hints["table_schema"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_identifier": account_identifier,
                "database_name": database_name,
                "schema_name": schema_name,
                "secret_arn": secret_arn,
                "table_name": table_name,
                "table_schema": table_schema,
            }

        @builtins.property
        def account_identifier(self) -> builtins.str:
            '''The account identifier for the Snowflake table reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-snowflaketablereference.html#cfn-cleanrooms-configuredtable-snowflaketablereference-accountidentifier
            '''
            result = self._values.get("account_identifier")
            assert result is not None, "Required property 'account_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of the database the Snowflake table belongs to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-snowflaketablereference.html#cfn-cleanrooms-configuredtable-snowflaketablereference-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def schema_name(self) -> builtins.str:
            '''The schema name of the Snowflake table reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-snowflaketablereference.html#cfn-cleanrooms-configuredtable-snowflaketablereference-schemaname
            '''
            result = self._values.get("schema_name")
            assert result is not None, "Required property 'schema_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The secret ARN of the Snowflake table reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-snowflaketablereference.html#cfn-cleanrooms-configuredtable-snowflaketablereference-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The name of the Snowflake table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-snowflaketablereference.html#cfn-cleanrooms-configuredtable-snowflaketablereference-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_schema(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.SnowflakeTableSchemaProperty"]:
            '''The schema of the Snowflake table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-snowflaketablereference.html#cfn-cleanrooms-configuredtable-snowflaketablereference-tableschema
            '''
            result = self._values.get("table_schema")
            assert result is not None, "Required property 'table_schema' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.SnowflakeTableSchemaProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeTableReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.SnowflakeTableSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={"v1": "v1"},
    )
    class SnowflakeTableSchemaProperty:
        def __init__(
            self,
            *,
            v1: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.SnowflakeTableSchemaV1Property", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The schema of a Snowflake table.

            :param v1: The schema of a Snowflake table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-snowflaketableschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                snowflake_table_schema_property = cleanrooms.CfnConfiguredTable.SnowflakeTableSchemaProperty(
                    v1=[cleanrooms.CfnConfiguredTable.SnowflakeTableSchemaV1Property(
                        column_name="columnName",
                        column_type="columnType"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__239c59d3fbfbc31d3d63df05389a6d08ab60a5a59b54a1d142b38a1317d9924a)
                check_type(argname="argument v1", value=v1, expected_type=type_hints["v1"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "v1": v1,
            }

        @builtins.property
        def v1(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.SnowflakeTableSchemaV1Property"]]]:
            '''The schema of a Snowflake table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-snowflaketableschema.html#cfn-cleanrooms-configuredtable-snowflaketableschema-v1
            '''
            result = self._values.get("v1")
            assert result is not None, "Required property 'v1' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.SnowflakeTableSchemaV1Property"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeTableSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.SnowflakeTableSchemaV1Property",
        jsii_struct_bases=[],
        name_mapping={"column_name": "columnName", "column_type": "columnType"},
    )
    class SnowflakeTableSchemaV1Property:
        def __init__(
            self,
            *,
            column_name: builtins.str,
            column_type: builtins.str,
        ) -> None:
            '''The Snowflake table schema.

            :param column_name: The column name.
            :param column_type: The column's data type. Supported data types: ``ARRAY`` , ``BIGINT`` , ``BOOLEAN`` , ``CHAR`` , ``DATE`` , ``DECIMAL`` , ``DOUBLE`` , ``DOUBLE PRECISION`` , ``FLOAT`` , ``FLOAT4`` , ``INT`` , ``INTEGER`` , ``MAP`` , ``NUMERIC`` , ``NUMBER`` , ``REAL`` , ``SMALLINT`` , ``STRING`` , ``TIMESTAMP`` , ``TIMESTAMP_LTZ`` , ``TIMESTAMP_NTZ`` , ``DATETIME`` , ``TINYINT`` , ``VARCHAR`` , ``TEXT`` , ``CHARACTER`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-snowflaketableschemav1.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                snowflake_table_schema_v1_property = cleanrooms.CfnConfiguredTable.SnowflakeTableSchemaV1Property(
                    column_name="columnName",
                    column_type="columnType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__83fba8d181362fec1a7a64673d96ded09367f372899b9e1e5eb170f94c17c13f)
                check_type(argname="argument column_name", value=column_name, expected_type=type_hints["column_name"])
                check_type(argname="argument column_type", value=column_type, expected_type=type_hints["column_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "column_name": column_name,
                "column_type": column_type,
            }

        @builtins.property
        def column_name(self) -> builtins.str:
            '''The column name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-snowflaketableschemav1.html#cfn-cleanrooms-configuredtable-snowflaketableschemav1-columnname
            '''
            result = self._values.get("column_name")
            assert result is not None, "Required property 'column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def column_type(self) -> builtins.str:
            '''The column's data type.

            Supported data types: ``ARRAY`` , ``BIGINT`` , ``BOOLEAN`` , ``CHAR`` , ``DATE`` , ``DECIMAL`` , ``DOUBLE`` , ``DOUBLE PRECISION`` , ``FLOAT`` , ``FLOAT4`` , ``INT`` , ``INTEGER`` , ``MAP`` , ``NUMERIC`` , ``NUMBER`` , ``REAL`` , ``SMALLINT`` , ``STRING`` , ``TIMESTAMP`` , ``TIMESTAMP_LTZ`` , ``TIMESTAMP_NTZ`` , ``DATETIME`` , ``TINYINT`` , ``VARCHAR`` , ``TEXT`` , ``CHARACTER`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-snowflaketableschemav1.html#cfn-cleanrooms-configuredtable-snowflaketableschemav1-columntype
            '''
            result = self._values.get("column_type")
            assert result is not None, "Required property 'column_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeTableSchemaV1Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTable.TableReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"athena": "athena", "glue": "glue", "snowflake": "snowflake"},
    )
    class TableReferenceProperty:
        def __init__(
            self,
            *,
            athena: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.AthenaTableReferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            glue: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.GlueTableReferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            snowflake: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTable.SnowflakeTableReferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A pointer to the dataset that underlies this table.

            :param athena: If present, a reference to the Athena table referred to by this table reference.
            :param glue: If present, a reference to the AWS Glue table referred to by this table reference.
            :param snowflake: If present, a reference to the Snowflake table referred to by this table reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-tablereference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                table_reference_property = cleanrooms.CfnConfiguredTable.TableReferenceProperty(
                    athena=cleanrooms.CfnConfiguredTable.AthenaTableReferenceProperty(
                        database_name="databaseName",
                        table_name="tableName",
                        work_group="workGroup",
                
                        # the properties below are optional
                        output_location="outputLocation"
                    ),
                    glue=cleanrooms.CfnConfiguredTable.GlueTableReferenceProperty(
                        database_name="databaseName",
                        table_name="tableName"
                    ),
                    snowflake=cleanrooms.CfnConfiguredTable.SnowflakeTableReferenceProperty(
                        account_identifier="accountIdentifier",
                        database_name="databaseName",
                        schema_name="schemaName",
                        secret_arn="secretArn",
                        table_name="tableName",
                        table_schema=cleanrooms.CfnConfiguredTable.SnowflakeTableSchemaProperty(
                            v1=[cleanrooms.CfnConfiguredTable.SnowflakeTableSchemaV1Property(
                                column_name="columnName",
                                column_type="columnType"
                            )]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__48547ee47249030cb21aff2b6c33202b13d80f1552ddf62b21595c3e0bb02374)
                check_type(argname="argument athena", value=athena, expected_type=type_hints["athena"])
                check_type(argname="argument glue", value=glue, expected_type=type_hints["glue"])
                check_type(argname="argument snowflake", value=snowflake, expected_type=type_hints["snowflake"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if athena is not None:
                self._values["athena"] = athena
            if glue is not None:
                self._values["glue"] = glue
            if snowflake is not None:
                self._values["snowflake"] = snowflake

        @builtins.property
        def athena(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AthenaTableReferenceProperty"]]:
            '''If present, a reference to the Athena table referred to by this table reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-tablereference.html#cfn-cleanrooms-configuredtable-tablereference-athena
            '''
            result = self._values.get("athena")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.AthenaTableReferenceProperty"]], result)

        @builtins.property
        def glue(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.GlueTableReferenceProperty"]]:
            '''If present, a reference to the AWS Glue table referred to by this table reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-tablereference.html#cfn-cleanrooms-configuredtable-tablereference-glue
            '''
            result = self._values.get("glue")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.GlueTableReferenceProperty"]], result)

        @builtins.property
        def snowflake(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.SnowflakeTableReferenceProperty"]]:
            '''If present, a reference to the Snowflake table referred to by this table reference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtable-tablereference.html#cfn-cleanrooms-configuredtable-tablereference-snowflake
            '''
            result = self._values.get("snowflake")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTable.SnowflakeTableReferenceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnConfiguredTableAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTableAssociation",
):
    '''Creates a configured table association.

    A configured table association links a configured table with a collaboration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html
    :cloudformationResource: AWS::CleanRooms::ConfiguredTableAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanrooms as cleanrooms
        
        cfn_configured_table_association = cleanrooms.CfnConfiguredTableAssociation(self, "MyCfnConfiguredTableAssociation",
            configured_table_identifier="configuredTableIdentifier",
            membership_identifier="membershipIdentifier",
            name="name",
            role_arn="roleArn",
        
            # the properties below are optional
            configured_table_association_analysis_rules=[cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleProperty(
                policy=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyProperty(
                    v1=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyV1Property(
                        aggregation=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleAggregationProperty(
                            allowed_additional_analyses=["allowedAdditionalAnalyses"],
                            allowed_result_receivers=["allowedResultReceivers"]
                        ),
                        custom=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleCustomProperty(
                            allowed_additional_analyses=["allowedAdditionalAnalyses"],
                            allowed_result_receivers=["allowedResultReceivers"]
                        ),
                        list=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleListProperty(
                            allowed_additional_analyses=["allowedAdditionalAnalyses"],
                            allowed_result_receivers=["allowedResultReceivers"]
                        )
                    )
                ),
                type="type"
            )],
            description="description",
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
        configured_table_identifier: builtins.str,
        membership_identifier: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        configured_table_association_analysis_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configured_table_identifier: A unique identifier for the configured table to be associated to. Currently accepts a configured table ID.
        :param membership_identifier: The unique ID for the membership this configured table association belongs to.
        :param name: The name of the configured table association, in lowercase. The table is identified by this name when running protected queries against the underlying data.
        :param role_arn: The service will assume this role to access catalog metadata and query the table.
        :param configured_table_association_analysis_rules: An analysis rule for a configured table association. This analysis rule specifies how data from the table can be used within its associated collaboration. In the console, the ``ConfiguredTableAssociationAnalysisRule`` is referred to as the *collaboration analysis rule* .
        :param description: A description of the configured table association.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e813cbcc5b9d34191c933a4be199648c57161cd507f73f0659159b5b61777153)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfiguredTableAssociationProps(
            configured_table_identifier=configured_table_identifier,
            membership_identifier=membership_identifier,
            name=name,
            role_arn=role_arn,
            configured_table_association_analysis_rules=configured_table_association_analysis_rules,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e6d4b82c3edf32301796f14dea9ee962d5b6287982b67f53a6fce4d9e53e702)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b13025a7765c8fcc0096c7e63fe6d35197debf3b5ec554487f0710eeca7c147b)
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
        '''Returns the Amazon Resource Name (ARN) of the specified configured table association.

        Example: ``arn:aws:cleanrooms:us-east-1:111122223333:configuredtable/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrConfiguredTableAssociationIdentifier")
    def attr_configured_table_association_identifier(self) -> builtins.str:
        '''Returns the unique identifier of the specified configured table association.

        Example: ``a1b2c3d4-5678-90ab-cdef-EXAMPLE33333``

        :cloudformationAttribute: ConfiguredTableAssociationIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfiguredTableAssociationIdentifier"))

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
    @jsii.member(jsii_name="configuredTableIdentifier")
    def configured_table_identifier(self) -> builtins.str:
        '''A unique identifier for the configured table to be associated to.'''
        return typing.cast(builtins.str, jsii.get(self, "configuredTableIdentifier"))

    @configured_table_identifier.setter
    def configured_table_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9728a7769f77a5cdfb3417c1fc58a389ba8c6ef5730bb294ef56c67c4f965bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuredTableIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="membershipIdentifier")
    def membership_identifier(self) -> builtins.str:
        '''The unique ID for the membership this configured table association belongs to.'''
        return typing.cast(builtins.str, jsii.get(self, "membershipIdentifier"))

    @membership_identifier.setter
    def membership_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e0b566414c7844303646de783cb99821d6132816fd82629491db143d70bc328)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "membershipIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the configured table association, in lowercase.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bb6d6d8ed4af7ba2289b9a65f55feb240da577eb6c05a2a379ac3aa825876b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The service will assume this role to access catalog metadata and query the table.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ed3a131e342f3d6715894b34f9784b7f6a4bd2257ccd5640eee2873aff3a7bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="configuredTableAssociationAnalysisRules")
    def configured_table_association_analysis_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleProperty"]]]]:
        '''An analysis rule for a configured table association.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleProperty"]]]], jsii.get(self, "configuredTableAssociationAnalysisRules"))

    @configured_table_association_analysis_rules.setter
    def configured_table_association_analysis_rules(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0d0ff28b0fb4873494693033feac4f811d803307eb2eaf6b27473cd93db2ef0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuredTableAssociationAnalysisRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the configured table association.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c12987240d2469d3de49134d97df56891e19e780c69b74115f2054f5a34a614)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab43f7456a874349f59a592b725dc266f2d215b76da6fc373e63e5999b3ce75e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleAggregationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allowed_additional_analyses": "allowedAdditionalAnalyses",
            "allowed_result_receivers": "allowedResultReceivers",
        },
    )
    class ConfiguredTableAssociationAnalysisRuleAggregationProperty:
        def __init__(
            self,
            *,
            allowed_additional_analyses: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_result_receivers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The configured table association analysis rule applied to a configured table with the aggregation analysis rule.

            :param allowed_additional_analyses: The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output. The ``allowedAdditionalAnalyses`` parameter is currently supported for the list analysis rule ( ``AnalysisRuleList`` ) and the custom analysis rule ( ``AnalysisRuleCustom`` ).
            :param allowed_result_receivers: The list of collaboration members who are allowed to receive results of queries run with this configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                configured_table_association_analysis_rule_aggregation_property = cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleAggregationProperty(
                    allowed_additional_analyses=["allowedAdditionalAnalyses"],
                    allowed_result_receivers=["allowedResultReceivers"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__238152ae2ae96e49fa6c904bd319b8d4be8fd0916ce96bdf774850ad8ca69140)
                check_type(argname="argument allowed_additional_analyses", value=allowed_additional_analyses, expected_type=type_hints["allowed_additional_analyses"])
                check_type(argname="argument allowed_result_receivers", value=allowed_result_receivers, expected_type=type_hints["allowed_result_receivers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allowed_additional_analyses is not None:
                self._values["allowed_additional_analyses"] = allowed_additional_analyses
            if allowed_result_receivers is not None:
                self._values["allowed_result_receivers"] = allowed_result_receivers

        @builtins.property
        def allowed_additional_analyses(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.

            The ``allowedAdditionalAnalyses`` parameter is currently supported for the list analysis rule ( ``AnalysisRuleList`` ) and the custom analysis rule ( ``AnalysisRuleCustom`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation.html#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation-allowedadditionalanalyses
            '''
            result = self._values.get("allowed_additional_analyses")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_result_receivers(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of collaboration members who are allowed to receive results of queries run with this configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation.html#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisruleaggregation-allowedresultreceivers
            '''
            result = self._values.get("allowed_result_receivers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfiguredTableAssociationAnalysisRuleAggregationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleCustomProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allowed_additional_analyses": "allowedAdditionalAnalyses",
            "allowed_result_receivers": "allowedResultReceivers",
        },
    )
    class ConfiguredTableAssociationAnalysisRuleCustomProperty:
        def __init__(
            self,
            *,
            allowed_additional_analyses: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_result_receivers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The configured table association analysis rule applied to a configured table with the custom analysis rule.

            :param allowed_additional_analyses: The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.
            :param allowed_result_receivers: The list of collaboration members who are allowed to receive results of queries run with this configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulecustom.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                configured_table_association_analysis_rule_custom_property = cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleCustomProperty(
                    allowed_additional_analyses=["allowedAdditionalAnalyses"],
                    allowed_result_receivers=["allowedResultReceivers"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5a7ef0cf97c0f9da19de0009ec3e6fb3ffe6b6f987fc5b6203ab290eec858c53)
                check_type(argname="argument allowed_additional_analyses", value=allowed_additional_analyses, expected_type=type_hints["allowed_additional_analyses"])
                check_type(argname="argument allowed_result_receivers", value=allowed_result_receivers, expected_type=type_hints["allowed_result_receivers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allowed_additional_analyses is not None:
                self._values["allowed_additional_analyses"] = allowed_additional_analyses
            if allowed_result_receivers is not None:
                self._values["allowed_result_receivers"] = allowed_result_receivers

        @builtins.property
        def allowed_additional_analyses(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulecustom.html#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulecustom-allowedadditionalanalyses
            '''
            result = self._values.get("allowed_additional_analyses")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_result_receivers(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of collaboration members who are allowed to receive results of queries run with this configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulecustom.html#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulecustom-allowedresultreceivers
            '''
            result = self._values.get("allowed_result_receivers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfiguredTableAssociationAnalysisRuleCustomProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleListProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allowed_additional_analyses": "allowedAdditionalAnalyses",
            "allowed_result_receivers": "allowedResultReceivers",
        },
    )
    class ConfiguredTableAssociationAnalysisRuleListProperty:
        def __init__(
            self,
            *,
            allowed_additional_analyses: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_result_receivers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The configured table association analysis rule applied to a configured table with the list analysis rule.

            :param allowed_additional_analyses: The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.
            :param allowed_result_receivers: The list of collaboration members who are allowed to receive results of queries run with this configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulelist.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                configured_table_association_analysis_rule_list_property = cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleListProperty(
                    allowed_additional_analyses=["allowedAdditionalAnalyses"],
                    allowed_result_receivers=["allowedResultReceivers"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f6bcf6381ae16674a7b2d769e9d709e1ae56dbd9f4c003d1b9c9c8f5d385071f)
                check_type(argname="argument allowed_additional_analyses", value=allowed_additional_analyses, expected_type=type_hints["allowed_additional_analyses"])
                check_type(argname="argument allowed_result_receivers", value=allowed_result_receivers, expected_type=type_hints["allowed_result_receivers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allowed_additional_analyses is not None:
                self._values["allowed_additional_analyses"] = allowed_additional_analyses
            if allowed_result_receivers is not None:
                self._values["allowed_result_receivers"] = allowed_result_receivers

        @builtins.property
        def allowed_additional_analyses(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulelist.html#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulelist-allowedadditionalanalyses
            '''
            result = self._values.get("allowed_additional_analyses")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_result_receivers(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of collaboration members who are allowed to receive results of queries run with this configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulelist.html#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulelist-allowedresultreceivers
            '''
            result = self._values.get("allowed_result_receivers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfiguredTableAssociationAnalysisRuleListProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"v1": "v1"},
    )
    class ConfiguredTableAssociationAnalysisRulePolicyProperty:
        def __init__(
            self,
            *,
            v1: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyV1Property", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Controls on the query specifications that can be run on an associated configured table.

            :param v1: The policy for the configured table association analysis rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                configured_table_association_analysis_rule_policy_property = cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyProperty(
                    v1=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyV1Property(
                        aggregation=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleAggregationProperty(
                            allowed_additional_analyses=["allowedAdditionalAnalyses"],
                            allowed_result_receivers=["allowedResultReceivers"]
                        ),
                        custom=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleCustomProperty(
                            allowed_additional_analyses=["allowedAdditionalAnalyses"],
                            allowed_result_receivers=["allowedResultReceivers"]
                        ),
                        list=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleListProperty(
                            allowed_additional_analyses=["allowedAdditionalAnalyses"],
                            allowed_result_receivers=["allowedResultReceivers"]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__281bd2c034dea5decd044a63b24891762f44992aab75ab6780e712d520ae64f2)
                check_type(argname="argument v1", value=v1, expected_type=type_hints["v1"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "v1": v1,
            }

        @builtins.property
        def v1(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyV1Property"]:
            '''The policy for the configured table association analysis rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicy.html#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicy-v1
            '''
            result = self._values.get("v1")
            assert result is not None, "Required property 'v1' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyV1Property"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfiguredTableAssociationAnalysisRulePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyV1Property",
        jsii_struct_bases=[],
        name_mapping={
            "aggregation": "aggregation",
            "custom": "custom",
            "list": "list",
        },
    )
    class ConfiguredTableAssociationAnalysisRulePolicyV1Property:
        def __init__(
            self,
            *,
            aggregation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleAggregationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            custom: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleCustomProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleListProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Controls on the query specifications that can be run on an associated configured table.

            :param aggregation: Analysis rule type that enables only aggregation queries on a configured table.
            :param custom: Analysis rule type that enables the table owner to approve custom SQL queries on their configured tables. It supports differential privacy.
            :param list: Analysis rule type that enables only list queries on a configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                configured_table_association_analysis_rule_policy_v1_property = cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyV1Property(
                    aggregation=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleAggregationProperty(
                        allowed_additional_analyses=["allowedAdditionalAnalyses"],
                        allowed_result_receivers=["allowedResultReceivers"]
                    ),
                    custom=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleCustomProperty(
                        allowed_additional_analyses=["allowedAdditionalAnalyses"],
                        allowed_result_receivers=["allowedResultReceivers"]
                    ),
                    list=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleListProperty(
                        allowed_additional_analyses=["allowedAdditionalAnalyses"],
                        allowed_result_receivers=["allowedResultReceivers"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cc559a0692caa4463a4398f86a4304afc170424b5a1434972be11d3638e5bd07)
                check_type(argname="argument aggregation", value=aggregation, expected_type=type_hints["aggregation"])
                check_type(argname="argument custom", value=custom, expected_type=type_hints["custom"])
                check_type(argname="argument list", value=list, expected_type=type_hints["list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aggregation is not None:
                self._values["aggregation"] = aggregation
            if custom is not None:
                self._values["custom"] = custom
            if list is not None:
                self._values["list"] = list

        @builtins.property
        def aggregation(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleAggregationProperty"]]:
            '''Analysis rule type that enables only aggregation queries on a configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1.html#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-aggregation
            '''
            result = self._values.get("aggregation")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleAggregationProperty"]], result)

        @builtins.property
        def custom(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleCustomProperty"]]:
            '''Analysis rule type that enables the table owner to approve custom SQL queries on their configured tables.

            It supports differential privacy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1.html#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-custom
            '''
            result = self._values.get("custom")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleCustomProperty"]], result)

        @builtins.property
        def list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleListProperty"]]:
            '''Analysis rule type that enables only list queries on a configured table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1.html#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrulepolicyv1-list
            '''
            result = self._values.get("list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleListProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfiguredTableAssociationAnalysisRulePolicyV1Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"policy": "policy", "type": "type"},
    )
    class ConfiguredTableAssociationAnalysisRuleProperty:
        def __init__(
            self,
            *,
            policy: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
        ) -> None:
            '''An analysis rule for a configured table association.

            This analysis rule specifies how data from the table can be used within its associated collaboration. In the console, the ``ConfiguredTableAssociationAnalysisRule`` is referred to as the *collaboration analysis rule* .

            :param policy: The policy of the configured table association analysis rule.
            :param type: The type of the configured table association analysis rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                configured_table_association_analysis_rule_property = cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleProperty(
                    policy=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyProperty(
                        v1=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyV1Property(
                            aggregation=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleAggregationProperty(
                                allowed_additional_analyses=["allowedAdditionalAnalyses"],
                                allowed_result_receivers=["allowedResultReceivers"]
                            ),
                            custom=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleCustomProperty(
                                allowed_additional_analyses=["allowedAdditionalAnalyses"],
                                allowed_result_receivers=["allowedResultReceivers"]
                            ),
                            list=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleListProperty(
                                allowed_additional_analyses=["allowedAdditionalAnalyses"],
                                allowed_result_receivers=["allowedResultReceivers"]
                            )
                        )
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__720bc84933dd2d1faf77915df0b8b69bcbb3e46b9d6c11a06d41f925485184d8)
                check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "policy": policy,
                "type": type,
            }

        @builtins.property
        def policy(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyProperty"]:
            '''The policy of the configured table association analysis rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule.html#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule-policy
            '''
            result = self._values.get("policy")
            assert result is not None, "Required property 'policy' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the configured table association analysis rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule.html#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrule-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfiguredTableAssociationAnalysisRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTableAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "configured_table_identifier": "configuredTableIdentifier",
        "membership_identifier": "membershipIdentifier",
        "name": "name",
        "role_arn": "roleArn",
        "configured_table_association_analysis_rules": "configuredTableAssociationAnalysisRules",
        "description": "description",
        "tags": "tags",
    },
)
class CfnConfiguredTableAssociationProps:
    def __init__(
        self,
        *,
        configured_table_identifier: builtins.str,
        membership_identifier: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        configured_table_association_analysis_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfiguredTableAssociation``.

        :param configured_table_identifier: A unique identifier for the configured table to be associated to. Currently accepts a configured table ID.
        :param membership_identifier: The unique ID for the membership this configured table association belongs to.
        :param name: The name of the configured table association, in lowercase. The table is identified by this name when running protected queries against the underlying data.
        :param role_arn: The service will assume this role to access catalog metadata and query the table.
        :param configured_table_association_analysis_rules: An analysis rule for a configured table association. This analysis rule specifies how data from the table can be used within its associated collaboration. In the console, the ``ConfiguredTableAssociationAnalysisRule`` is referred to as the *collaboration analysis rule* .
        :param description: A description of the configured table association.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanrooms as cleanrooms
            
            cfn_configured_table_association_props = cleanrooms.CfnConfiguredTableAssociationProps(
                configured_table_identifier="configuredTableIdentifier",
                membership_identifier="membershipIdentifier",
                name="name",
                role_arn="roleArn",
            
                # the properties below are optional
                configured_table_association_analysis_rules=[cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleProperty(
                    policy=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyProperty(
                        v1=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyV1Property(
                            aggregation=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleAggregationProperty(
                                allowed_additional_analyses=["allowedAdditionalAnalyses"],
                                allowed_result_receivers=["allowedResultReceivers"]
                            ),
                            custom=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleCustomProperty(
                                allowed_additional_analyses=["allowedAdditionalAnalyses"],
                                allowed_result_receivers=["allowedResultReceivers"]
                            ),
                            list=cleanrooms.CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleListProperty(
                                allowed_additional_analyses=["allowedAdditionalAnalyses"],
                                allowed_result_receivers=["allowedResultReceivers"]
                            )
                        )
                    ),
                    type="type"
                )],
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__115dd625c37fad8a84b51d36bcabf9183ae442a7285c6ddd1efddd869faae1dc)
            check_type(argname="argument configured_table_identifier", value=configured_table_identifier, expected_type=type_hints["configured_table_identifier"])
            check_type(argname="argument membership_identifier", value=membership_identifier, expected_type=type_hints["membership_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument configured_table_association_analysis_rules", value=configured_table_association_analysis_rules, expected_type=type_hints["configured_table_association_analysis_rules"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configured_table_identifier": configured_table_identifier,
            "membership_identifier": membership_identifier,
            "name": name,
            "role_arn": role_arn,
        }
        if configured_table_association_analysis_rules is not None:
            self._values["configured_table_association_analysis_rules"] = configured_table_association_analysis_rules
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def configured_table_identifier(self) -> builtins.str:
        '''A unique identifier for the configured table to be associated to.

        Currently accepts a configured table ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-configuredtableidentifier
        '''
        result = self._values.get("configured_table_identifier")
        assert result is not None, "Required property 'configured_table_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def membership_identifier(self) -> builtins.str:
        '''The unique ID for the membership this configured table association belongs to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-membershipidentifier
        '''
        result = self._values.get("membership_identifier")
        assert result is not None, "Required property 'membership_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the configured table association, in lowercase.

        The table is identified by this name when running protected queries against the underlying data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The service will assume this role to access catalog metadata and query the table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configured_table_association_analysis_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleProperty]]]]:
        '''An analysis rule for a configured table association.

        This analysis rule specifies how data from the table can be used within its associated collaboration. In the console, the ``ConfiguredTableAssociationAnalysisRule`` is referred to as the *collaboration analysis rule* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-configuredtableassociationanalysisrules
        '''
        result = self._values.get("configured_table_association_analysis_rules")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the configured table association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.

        Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtableassociation.html#cfn-cleanrooms-configuredtableassociation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfiguredTableAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnConfiguredTableProps",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_columns": "allowedColumns",
        "analysis_method": "analysisMethod",
        "name": "name",
        "table_reference": "tableReference",
        "analysis_rules": "analysisRules",
        "description": "description",
        "selected_analysis_methods": "selectedAnalysisMethods",
        "tags": "tags",
    },
)
class CfnConfiguredTableProps:
    def __init__(
        self,
        *,
        allowed_columns: typing.Sequence[builtins.str],
        analysis_method: builtins.str,
        name: builtins.str,
        table_reference: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.TableReferenceProperty, typing.Dict[builtins.str, typing.Any]]],
        analysis_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AnalysisRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        selected_analysis_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfiguredTable``.

        :param allowed_columns: The columns within the underlying AWS Glue table that can be utilized within collaborations.
        :param analysis_method: The analysis method for the configured table. ``DIRECT_QUERY`` allows SQL queries to be run directly on this table. ``DIRECT_JOB`` allows PySpark jobs to be run directly on this table. ``MULTIPLE`` allows both SQL queries and PySpark jobs to be run directly on this table.
        :param name: A name for the configured table.
        :param table_reference: The table that this configured table represents.
        :param analysis_rules: The analysis rule that was created for the configured table.
        :param description: A description for the configured table.
        :param selected_analysis_methods: The selected analysis methods for the configured table.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanrooms as cleanrooms
            
            cfn_configured_table_props = cleanrooms.CfnConfiguredTableProps(
                allowed_columns=["allowedColumns"],
                analysis_method="analysisMethod",
                name="name",
                table_reference=cleanrooms.CfnConfiguredTable.TableReferenceProperty(
                    athena=cleanrooms.CfnConfiguredTable.AthenaTableReferenceProperty(
                        database_name="databaseName",
                        table_name="tableName",
                        work_group="workGroup",
            
                        # the properties below are optional
                        output_location="outputLocation"
                    ),
                    glue=cleanrooms.CfnConfiguredTable.GlueTableReferenceProperty(
                        database_name="databaseName",
                        table_name="tableName"
                    ),
                    snowflake=cleanrooms.CfnConfiguredTable.SnowflakeTableReferenceProperty(
                        account_identifier="accountIdentifier",
                        database_name="databaseName",
                        schema_name="schemaName",
                        secret_arn="secretArn",
                        table_name="tableName",
                        table_schema=cleanrooms.CfnConfiguredTable.SnowflakeTableSchemaProperty(
                            v1=[cleanrooms.CfnConfiguredTable.SnowflakeTableSchemaV1Property(
                                column_name="columnName",
                                column_type="columnType"
                            )]
                        )
                    )
                ),
            
                # the properties below are optional
                analysis_rules=[cleanrooms.CfnConfiguredTable.AnalysisRuleProperty(
                    policy=cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty(
                        v1=cleanrooms.CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property(
                            aggregation=cleanrooms.CfnConfiguredTable.AnalysisRuleAggregationProperty(
                                aggregate_columns=[cleanrooms.CfnConfiguredTable.AggregateColumnProperty(
                                    column_names=["columnNames"],
                                    function="function"
                                )],
                                dimension_columns=["dimensionColumns"],
                                join_columns=["joinColumns"],
                                output_constraints=[cleanrooms.CfnConfiguredTable.AggregationConstraintProperty(
                                    column_name="columnName",
                                    minimum=123,
                                    type="type"
                                )],
                                scalar_functions=["scalarFunctions"],
            
                                # the properties below are optional
                                additional_analyses="additionalAnalyses",
                                allowed_join_operators=["allowedJoinOperators"],
                                join_required="joinRequired"
                            ),
                            custom=cleanrooms.CfnConfiguredTable.AnalysisRuleCustomProperty(
                                allowed_analyses=["allowedAnalyses"],
            
                                # the properties below are optional
                                additional_analyses="additionalAnalyses",
                                allowed_analysis_providers=["allowedAnalysisProviders"],
                                differential_privacy=cleanrooms.CfnConfiguredTable.DifferentialPrivacyProperty(
                                    columns=[cleanrooms.CfnConfiguredTable.DifferentialPrivacyColumnProperty(
                                        name="name"
                                    )]
                                ),
                                disallowed_output_columns=["disallowedOutputColumns"]
                            ),
                            list=cleanrooms.CfnConfiguredTable.AnalysisRuleListProperty(
                                join_columns=["joinColumns"],
                                list_columns=["listColumns"],
            
                                # the properties below are optional
                                additional_analyses="additionalAnalyses",
                                allowed_join_operators=["allowedJoinOperators"]
                            )
                        )
                    ),
                    type="type"
                )],
                description="description",
                selected_analysis_methods=["selectedAnalysisMethods"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__881d5bc014e7a9ce8400d21437644071526768629f4ac0f4414f60ba95930f3f)
            check_type(argname="argument allowed_columns", value=allowed_columns, expected_type=type_hints["allowed_columns"])
            check_type(argname="argument analysis_method", value=analysis_method, expected_type=type_hints["analysis_method"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument table_reference", value=table_reference, expected_type=type_hints["table_reference"])
            check_type(argname="argument analysis_rules", value=analysis_rules, expected_type=type_hints["analysis_rules"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument selected_analysis_methods", value=selected_analysis_methods, expected_type=type_hints["selected_analysis_methods"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allowed_columns": allowed_columns,
            "analysis_method": analysis_method,
            "name": name,
            "table_reference": table_reference,
        }
        if analysis_rules is not None:
            self._values["analysis_rules"] = analysis_rules
        if description is not None:
            self._values["description"] = description
        if selected_analysis_methods is not None:
            self._values["selected_analysis_methods"] = selected_analysis_methods
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def allowed_columns(self) -> typing.List[builtins.str]:
        '''The columns within the underlying AWS Glue table that can be utilized within collaborations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-allowedcolumns
        '''
        result = self._values.get("allowed_columns")
        assert result is not None, "Required property 'allowed_columns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def analysis_method(self) -> builtins.str:
        '''The analysis method for the configured table.

        ``DIRECT_QUERY`` allows SQL queries to be run directly on this table.

        ``DIRECT_JOB`` allows PySpark jobs to be run directly on this table.

        ``MULTIPLE`` allows both SQL queries and PySpark jobs to be run directly on this table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-analysismethod
        '''
        result = self._values.get("analysis_method")
        assert result is not None, "Required property 'analysis_method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the configured table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_reference(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnConfiguredTable.TableReferenceProperty]:
        '''The table that this configured table represents.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-tablereference
        '''
        result = self._values.get("table_reference")
        assert result is not None, "Required property 'table_reference' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnConfiguredTable.TableReferenceProperty], result)

    @builtins.property
    def analysis_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfiguredTable.AnalysisRuleProperty]]]]:
        '''The analysis rule that was created for the configured table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-analysisrules
        '''
        result = self._values.get("analysis_rules")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfiguredTable.AnalysisRuleProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the configured table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def selected_analysis_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The selected analysis methods for the configured table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-selectedanalysismethods
        '''
        result = self._values.get("selected_analysis_methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.

        Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-configuredtable.html#cfn-cleanrooms-configuredtable-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfiguredTableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnIdMappingTable(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnIdMappingTable",
):
    '''Describes information about the ID mapping table.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idmappingtable.html
    :cloudformationResource: AWS::CleanRooms::IdMappingTable
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanrooms as cleanrooms
        
        cfn_id_mapping_table = cleanrooms.CfnIdMappingTable(self, "MyCfnIdMappingTable",
            input_reference_config=cleanrooms.CfnIdMappingTable.IdMappingTableInputReferenceConfigProperty(
                input_reference_arn="inputReferenceArn",
                manage_resource_policies=False
            ),
            membership_identifier="membershipIdentifier",
            name="name",
        
            # the properties below are optional
            description="description",
            kms_key_arn="kmsKeyArn",
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
        input_reference_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnIdMappingTable.IdMappingTableInputReferenceConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        membership_identifier: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param input_reference_config: The input reference configuration for the ID mapping table.
        :param membership_identifier: The unique identifier of the membership resource for the ID mapping table.
        :param name: The name of the ID mapping table.
        :param description: The description of the ID mapping table.
        :param kms_key_arn: The Amazon Resource Name (ARN) of the AWS KMS key.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a55eec871eed8ea740c3790e228bff6225a56f9406dd161a61af8218377c626)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIdMappingTableProps(
            input_reference_config=input_reference_config,
            membership_identifier=membership_identifier,
            name=name,
            description=description,
            kms_key_arn=kms_key_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fb4bed5d50335d140dfb97a8e1ece95e5918e41e8f333e7a21770aff551143c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__acdffe9d489cfb1fd064c08c8b300b2880a9e20996d6a0e15e197844adf31b6d)
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
        '''The Amazon Resource Name (ARN) of the ID mapping table.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollaborationArn")
    def attr_collaboration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the collaboration that contains this ID mapping table.

        :cloudformationAttribute: CollaborationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollaborationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollaborationIdentifier")
    def attr_collaboration_identifier(self) -> builtins.str:
        '''The unique identifier of the collaboration that contains this ID mapping table.

        :cloudformationAttribute: CollaborationIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollaborationIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrIdMappingTableIdentifier")
    def attr_id_mapping_table_identifier(self) -> builtins.str:
        '''The unique identifier of the ID mapping table identifier that you want to retrieve.

        :cloudformationAttribute: IdMappingTableIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdMappingTableIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrInputReferenceProperties")
    def attr_input_reference_properties(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: InputReferenceProperties
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrInputReferenceProperties"))

    @builtins.property
    @jsii.member(jsii_name="attrMembershipArn")
    def attr_membership_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the membership resource for the ID mapping table.

        :cloudformationAttribute: MembershipArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMembershipArn"))

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
    @jsii.member(jsii_name="inputReferenceConfig")
    def input_reference_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnIdMappingTable.IdMappingTableInputReferenceConfigProperty"]:
        '''The input reference configuration for the ID mapping table.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnIdMappingTable.IdMappingTableInputReferenceConfigProperty"], jsii.get(self, "inputReferenceConfig"))

    @input_reference_config.setter
    def input_reference_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnIdMappingTable.IdMappingTableInputReferenceConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80a1443fefffd729ef997de9fb9306db15cfda0ecccaa0f348c3f55a13fc2f6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputReferenceConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="membershipIdentifier")
    def membership_identifier(self) -> builtins.str:
        '''The unique identifier of the membership resource for the ID mapping table.'''
        return typing.cast(builtins.str, jsii.get(self, "membershipIdentifier"))

    @membership_identifier.setter
    def membership_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a608278f5ac9f4b2374d49aaae1f9c846f8320a4fb6cf2c093385273f313224c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "membershipIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the ID mapping table.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d89d3a813c07afbd9194e6ef736daf000c0d923680da83dd94897908ef16598)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the ID mapping table.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fe55d535ef13a6fa856ac8e5ba601c43e7ece61a7d5ddf03730c1f1ea475767)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS KMS key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1390f292c37578c0a018f5c4283630c58da4fdd1848e6bfb85b87946002dc103)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d6b9b9f29a25fa84794d9a566af8e18597086eba6792ac31fe185d0f74a9ff5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnIdMappingTable.IdMappingTableInputReferenceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_reference_arn": "inputReferenceArn",
            "manage_resource_policies": "manageResourcePolicies",
        },
    )
    class IdMappingTableInputReferenceConfigProperty:
        def __init__(
            self,
            *,
            input_reference_arn: builtins.str,
            manage_resource_policies: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Provides the input reference configuration for the ID mapping table.

            :param input_reference_arn: The Amazon Resource Name (ARN) of the referenced resource in AWS Entity Resolution . Valid values are ID mapping workflow ARNs.
            :param manage_resource_policies: When ``TRUE`` , AWS Clean Rooms manages permissions for the ID mapping table resource. When ``FALSE`` , the resource owner manages permissions for the ID mapping table resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                id_mapping_table_input_reference_config_property = cleanrooms.CfnIdMappingTable.IdMappingTableInputReferenceConfigProperty(
                    input_reference_arn="inputReferenceArn",
                    manage_resource_policies=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3e37f64c35b172103f8bfa9f0d30e75b382e86d01d38fd2e8eb28803124f2fbc)
                check_type(argname="argument input_reference_arn", value=input_reference_arn, expected_type=type_hints["input_reference_arn"])
                check_type(argname="argument manage_resource_policies", value=manage_resource_policies, expected_type=type_hints["manage_resource_policies"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_reference_arn": input_reference_arn,
                "manage_resource_policies": manage_resource_policies,
            }

        @builtins.property
        def input_reference_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the referenced resource in AWS Entity Resolution .

            Valid values are ID mapping workflow ARNs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig.html#cfn-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig-inputreferencearn
            '''
            result = self._values.get("input_reference_arn")
            assert result is not None, "Required property 'input_reference_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def manage_resource_policies(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''When ``TRUE`` , AWS Clean Rooms manages permissions for the ID mapping table resource.

            When ``FALSE`` , the resource owner manages permissions for the ID mapping table resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig.html#cfn-cleanrooms-idmappingtable-idmappingtableinputreferenceconfig-manageresourcepolicies
            '''
            result = self._values.get("manage_resource_policies")
            assert result is not None, "Required property 'manage_resource_policies' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdMappingTableInputReferenceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnIdMappingTable.IdMappingTableInputReferencePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"id_mapping_table_input_source": "idMappingTableInputSource"},
    )
    class IdMappingTableInputReferencePropertiesProperty:
        def __init__(
            self,
            *,
            id_mapping_table_input_source: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIdMappingTable.IdMappingTableInputSourceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The input reference properties for the ID mapping table.

            :param id_mapping_table_input_source: The input source of the ID mapping table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                id_mapping_table_input_reference_properties_property = cleanrooms.CfnIdMappingTable.IdMappingTableInputReferencePropertiesProperty(
                    id_mapping_table_input_source=[cleanrooms.CfnIdMappingTable.IdMappingTableInputSourceProperty(
                        id_namespace_association_id="idNamespaceAssociationId",
                        type="type"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0e2b496feb9017399bea5c97a77d2124b505586ff18a03d366e20cfcd893709e)
                check_type(argname="argument id_mapping_table_input_source", value=id_mapping_table_input_source, expected_type=type_hints["id_mapping_table_input_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id_mapping_table_input_source": id_mapping_table_input_source,
            }

        @builtins.property
        def id_mapping_table_input_source(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIdMappingTable.IdMappingTableInputSourceProperty"]]]:
            '''The input source of the ID mapping table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idmappingtable-idmappingtableinputreferenceproperties.html#cfn-cleanrooms-idmappingtable-idmappingtableinputreferenceproperties-idmappingtableinputsource
            '''
            result = self._values.get("id_mapping_table_input_source")
            assert result is not None, "Required property 'id_mapping_table_input_source' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIdMappingTable.IdMappingTableInputSourceProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdMappingTableInputReferencePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnIdMappingTable.IdMappingTableInputSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id_namespace_association_id": "idNamespaceAssociationId",
            "type": "type",
        },
    )
    class IdMappingTableInputSourceProperty:
        def __init__(
            self,
            *,
            id_namespace_association_id: builtins.str,
            type: builtins.str,
        ) -> None:
            '''The input source of the ID mapping table.

            :param id_namespace_association_id: The unique identifier of the ID namespace association.
            :param type: The type of the input source of the ID mapping table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idmappingtable-idmappingtableinputsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                id_mapping_table_input_source_property = cleanrooms.CfnIdMappingTable.IdMappingTableInputSourceProperty(
                    id_namespace_association_id="idNamespaceAssociationId",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__690a1415d215001f1d1f03e8ed0bfcd7231c35a0b31d54bd8fab7c8b51e81090)
                check_type(argname="argument id_namespace_association_id", value=id_namespace_association_id, expected_type=type_hints["id_namespace_association_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id_namespace_association_id": id_namespace_association_id,
                "type": type,
            }

        @builtins.property
        def id_namespace_association_id(self) -> builtins.str:
            '''The unique identifier of the ID namespace association.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idmappingtable-idmappingtableinputsource.html#cfn-cleanrooms-idmappingtable-idmappingtableinputsource-idnamespaceassociationid
            '''
            result = self._values.get("id_namespace_association_id")
            assert result is not None, "Required property 'id_namespace_association_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the input source of the ID mapping table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idmappingtable-idmappingtableinputsource.html#cfn-cleanrooms-idmappingtable-idmappingtableinputsource-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdMappingTableInputSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnIdMappingTableProps",
    jsii_struct_bases=[],
    name_mapping={
        "input_reference_config": "inputReferenceConfig",
        "membership_identifier": "membershipIdentifier",
        "name": "name",
        "description": "description",
        "kms_key_arn": "kmsKeyArn",
        "tags": "tags",
    },
)
class CfnIdMappingTableProps:
    def __init__(
        self,
        *,
        input_reference_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdMappingTable.IdMappingTableInputReferenceConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        membership_identifier: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnIdMappingTable``.

        :param input_reference_config: The input reference configuration for the ID mapping table.
        :param membership_identifier: The unique identifier of the membership resource for the ID mapping table.
        :param name: The name of the ID mapping table.
        :param description: The description of the ID mapping table.
        :param kms_key_arn: The Amazon Resource Name (ARN) of the AWS KMS key.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idmappingtable.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanrooms as cleanrooms
            
            cfn_id_mapping_table_props = cleanrooms.CfnIdMappingTableProps(
                input_reference_config=cleanrooms.CfnIdMappingTable.IdMappingTableInputReferenceConfigProperty(
                    input_reference_arn="inputReferenceArn",
                    manage_resource_policies=False
                ),
                membership_identifier="membershipIdentifier",
                name="name",
            
                # the properties below are optional
                description="description",
                kms_key_arn="kmsKeyArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__722f65baa0dd5025cc0e42e7e9c4015b3d215b4aa9bb587f8bb4acf1f72b6c17)
            check_type(argname="argument input_reference_config", value=input_reference_config, expected_type=type_hints["input_reference_config"])
            check_type(argname="argument membership_identifier", value=membership_identifier, expected_type=type_hints["membership_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "input_reference_config": input_reference_config,
            "membership_identifier": membership_identifier,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def input_reference_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnIdMappingTable.IdMappingTableInputReferenceConfigProperty]:
        '''The input reference configuration for the ID mapping table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idmappingtable.html#cfn-cleanrooms-idmappingtable-inputreferenceconfig
        '''
        result = self._values.get("input_reference_config")
        assert result is not None, "Required property 'input_reference_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnIdMappingTable.IdMappingTableInputReferenceConfigProperty], result)

    @builtins.property
    def membership_identifier(self) -> builtins.str:
        '''The unique identifier of the membership resource for the ID mapping table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idmappingtable.html#cfn-cleanrooms-idmappingtable-membershipidentifier
        '''
        result = self._values.get("membership_identifier")
        assert result is not None, "Required property 'membership_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the ID mapping table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idmappingtable.html#cfn-cleanrooms-idmappingtable-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the ID mapping table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idmappingtable.html#cfn-cleanrooms-idmappingtable-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS KMS key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idmappingtable.html#cfn-cleanrooms-idmappingtable-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.

        Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idmappingtable.html#cfn-cleanrooms-idmappingtable-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIdMappingTableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnIdNamespaceAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnIdNamespaceAssociation",
):
    '''Provides information to create the ID namespace association.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idnamespaceassociation.html
    :cloudformationResource: AWS::CleanRooms::IdNamespaceAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanrooms as cleanrooms
        
        cfn_id_namespace_association = cleanrooms.CfnIdNamespaceAssociation(self, "MyCfnIdNamespaceAssociation",
            input_reference_config=cleanrooms.CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferenceConfigProperty(
                input_reference_arn="inputReferenceArn",
                manage_resource_policies=False
            ),
            membership_identifier="membershipIdentifier",
            name="name",
        
            # the properties below are optional
            description="description",
            id_mapping_config=cleanrooms.CfnIdNamespaceAssociation.IdMappingConfigProperty(
                allow_use_as_dimension_column=False
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
        input_reference_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferenceConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        membership_identifier: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id_mapping_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIdNamespaceAssociation.IdMappingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param input_reference_config: The input reference configuration for the ID namespace association.
        :param membership_identifier: The unique identifier of the membership that contains the ID namespace association.
        :param name: The name of this ID namespace association.
        :param description: The description of the ID namespace association.
        :param id_mapping_config: The configuration settings for the ID mapping table.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f52a2f7a45be837d26654b8bb3a3d0fab7fd6c5d25ec9b81d04a38689a6194fc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIdNamespaceAssociationProps(
            input_reference_config=input_reference_config,
            membership_identifier=membership_identifier,
            name=name,
            description=description,
            id_mapping_config=id_mapping_config,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a273456bd42e75067e1919d356ca738d303809279e3242770cf1909b4c53be9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c20ff570488d7e6c55252cba585a051fa87292c8341512e81f14562e1f1655f5)
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
        '''The Amazon Resource Name (ARN) of the ID namespace association.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollaborationArn")
    def attr_collaboration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the collaboration that contains this ID namespace association.

        :cloudformationAttribute: CollaborationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollaborationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollaborationIdentifier")
    def attr_collaboration_identifier(self) -> builtins.str:
        '''The unique identifier of the collaboration that contains this ID namespace association.

        :cloudformationAttribute: CollaborationIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollaborationIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrIdNamespaceAssociationIdentifier")
    def attr_id_namespace_association_identifier(self) -> builtins.str:
        '''The unique identifier of the ID namespace association that you want to retrieve.

        :cloudformationAttribute: IdNamespaceAssociationIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdNamespaceAssociationIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrInputReferenceProperties")
    def attr_input_reference_properties(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: InputReferenceProperties
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrInputReferenceProperties"))

    @builtins.property
    @jsii.member(jsii_name="attrMembershipArn")
    def attr_membership_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the membership resource for this ID namespace association.

        :cloudformationAttribute: MembershipArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMembershipArn"))

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
    @jsii.member(jsii_name="inputReferenceConfig")
    def input_reference_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferenceConfigProperty"]:
        '''The input reference configuration for the ID namespace association.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferenceConfigProperty"], jsii.get(self, "inputReferenceConfig"))

    @input_reference_config.setter
    def input_reference_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferenceConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__314c1541c8ce4234c2ada25e682a151d92fd93edbed1b4fd9105dcda931dc8dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputReferenceConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="membershipIdentifier")
    def membership_identifier(self) -> builtins.str:
        '''The unique identifier of the membership that contains the ID namespace association.'''
        return typing.cast(builtins.str, jsii.get(self, "membershipIdentifier"))

    @membership_identifier.setter
    def membership_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6942bfe2fcc0b0271a549fbe0007f1450b5a3d401188d403b97a935468367b94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "membershipIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of this ID namespace association.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ae82ba9441ae418e38e9d46574ca3cf34f6664a35510b70e1232333ae528fcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the ID namespace association.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8650ed8694c75389ed6fa670c630c6fd8b2e1ada930bf70bddcc54e58397c79f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="idMappingConfig")
    def id_mapping_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIdNamespaceAssociation.IdMappingConfigProperty"]]:
        '''The configuration settings for the ID mapping table.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIdNamespaceAssociation.IdMappingConfigProperty"]], jsii.get(self, "idMappingConfig"))

    @id_mapping_config.setter
    def id_mapping_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIdNamespaceAssociation.IdMappingConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18b505cc42cf359a69612005213707ca66c0c1daa7090899390265f4b2a5aa3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idMappingConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb75b574b07bea6c872486b6d13e8f81b7b3304807da45e45a041c11f1b4a84d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnIdNamespaceAssociation.IdMappingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"allow_use_as_dimension_column": "allowUseAsDimensionColumn"},
    )
    class IdMappingConfigProperty:
        def __init__(
            self,
            *,
            allow_use_as_dimension_column: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''The configuration settings for the ID mapping table.

            :param allow_use_as_dimension_column: An indicator as to whether you can use your column as a dimension column in the ID mapping table ( ``TRUE`` ) or not ( ``FALSE`` ). Default is ``FALSE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idnamespaceassociation-idmappingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                id_mapping_config_property = cleanrooms.CfnIdNamespaceAssociation.IdMappingConfigProperty(
                    allow_use_as_dimension_column=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c7ab29f7c6ba8d3c436a4a92d514f1221e64c73743bc063c057464db677e1895)
                check_type(argname="argument allow_use_as_dimension_column", value=allow_use_as_dimension_column, expected_type=type_hints["allow_use_as_dimension_column"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allow_use_as_dimension_column": allow_use_as_dimension_column,
            }

        @builtins.property
        def allow_use_as_dimension_column(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''An indicator as to whether you can use your column as a dimension column in the ID mapping table ( ``TRUE`` ) or not ( ``FALSE`` ).

            Default is ``FALSE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idnamespaceassociation-idmappingconfig.html#cfn-cleanrooms-idnamespaceassociation-idmappingconfig-allowuseasdimensioncolumn
            '''
            result = self._values.get("allow_use_as_dimension_column")
            assert result is not None, "Required property 'allow_use_as_dimension_column' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdMappingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferenceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_reference_arn": "inputReferenceArn",
            "manage_resource_policies": "manageResourcePolicies",
        },
    )
    class IdNamespaceAssociationInputReferenceConfigProperty:
        def __init__(
            self,
            *,
            input_reference_arn: builtins.str,
            manage_resource_policies: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Provides the information for the ID namespace association input reference configuration.

            :param input_reference_arn: The Amazon Resource Name (ARN) of the AWS Entity Resolution resource that is being associated to the collaboration. Valid resource ARNs are from the ID namespaces that you own.
            :param manage_resource_policies: When ``TRUE`` , AWS Clean Rooms manages permissions for the ID namespace association resource. When ``FALSE`` , the resource owner manages permissions for the ID namespace association resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                id_namespace_association_input_reference_config_property = cleanrooms.CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferenceConfigProperty(
                    input_reference_arn="inputReferenceArn",
                    manage_resource_policies=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6a0c310848e9ee828aa0877d71d6e2c6b1ece9c6d43464be34c1eea8d23e0b85)
                check_type(argname="argument input_reference_arn", value=input_reference_arn, expected_type=type_hints["input_reference_arn"])
                check_type(argname="argument manage_resource_policies", value=manage_resource_policies, expected_type=type_hints["manage_resource_policies"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_reference_arn": input_reference_arn,
                "manage_resource_policies": manage_resource_policies,
            }

        @builtins.property
        def input_reference_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AWS Entity Resolution resource that is being associated to the collaboration.

            Valid resource ARNs are from the ID namespaces that you own.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig.html#cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig-inputreferencearn
            '''
            result = self._values.get("input_reference_arn")
            assert result is not None, "Required property 'input_reference_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def manage_resource_policies(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''When ``TRUE`` , AWS Clean Rooms manages permissions for the ID namespace association resource.

            When ``FALSE`` , the resource owner manages permissions for the ID namespace association resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig.html#cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceconfig-manageresourcepolicies
            '''
            result = self._values.get("manage_resource_policies")
            assert result is not None, "Required property 'manage_resource_policies' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdNamespaceAssociationInputReferenceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferencePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id_mapping_workflows_supported": "idMappingWorkflowsSupported",
            "id_namespace_type": "idNamespaceType",
        },
    )
    class IdNamespaceAssociationInputReferencePropertiesProperty:
        def __init__(
            self,
            *,
            id_mapping_workflows_supported: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
            id_namespace_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides the information for the ID namespace association input reference properties.

            :param id_mapping_workflows_supported: Defines how ID mapping workflows are supported for this ID namespace association.
            :param id_namespace_type: The ID namespace type for this ID namespace association.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                # id_mapping_workflows_supported: Any
                
                id_namespace_association_input_reference_properties_property = cleanrooms.CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferencePropertiesProperty(
                    id_mapping_workflows_supported=[id_mapping_workflows_supported],
                    id_namespace_type="idNamespaceType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d6f96ce848c511129f57c9b34eaf0bed9c2e0367e3f29de1038e211e4797e05)
                check_type(argname="argument id_mapping_workflows_supported", value=id_mapping_workflows_supported, expected_type=type_hints["id_mapping_workflows_supported"])
                check_type(argname="argument id_namespace_type", value=id_namespace_type, expected_type=type_hints["id_namespace_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if id_mapping_workflows_supported is not None:
                self._values["id_mapping_workflows_supported"] = id_mapping_workflows_supported
            if id_namespace_type is not None:
                self._values["id_namespace_type"] = id_namespace_type

        @builtins.property
        def id_mapping_workflows_supported(
            self,
        ) -> typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]]:
            '''Defines how ID mapping workflows are supported for this ID namespace association.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties.html#cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties-idmappingworkflowssupported
            '''
            result = self._values.get("id_mapping_workflows_supported")
            return typing.cast(typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]], result)

        @builtins.property
        def id_namespace_type(self) -> typing.Optional[builtins.str]:
            '''The ID namespace type for this ID namespace association.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties.html#cfn-cleanrooms-idnamespaceassociation-idnamespaceassociationinputreferenceproperties-idnamespacetype
            '''
            result = self._values.get("id_namespace_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdNamespaceAssociationInputReferencePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnIdNamespaceAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "input_reference_config": "inputReferenceConfig",
        "membership_identifier": "membershipIdentifier",
        "name": "name",
        "description": "description",
        "id_mapping_config": "idMappingConfig",
        "tags": "tags",
    },
)
class CfnIdNamespaceAssociationProps:
    def __init__(
        self,
        *,
        input_reference_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferenceConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        membership_identifier: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id_mapping_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdNamespaceAssociation.IdMappingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnIdNamespaceAssociation``.

        :param input_reference_config: The input reference configuration for the ID namespace association.
        :param membership_identifier: The unique identifier of the membership that contains the ID namespace association.
        :param name: The name of this ID namespace association.
        :param description: The description of the ID namespace association.
        :param id_mapping_config: The configuration settings for the ID mapping table.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idnamespaceassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanrooms as cleanrooms
            
            cfn_id_namespace_association_props = cleanrooms.CfnIdNamespaceAssociationProps(
                input_reference_config=cleanrooms.CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferenceConfigProperty(
                    input_reference_arn="inputReferenceArn",
                    manage_resource_policies=False
                ),
                membership_identifier="membershipIdentifier",
                name="name",
            
                # the properties below are optional
                description="description",
                id_mapping_config=cleanrooms.CfnIdNamespaceAssociation.IdMappingConfigProperty(
                    allow_use_as_dimension_column=False
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82e4c0093759d750139b85493d1dd6c9f0b65aa9075fa72356dbfcee3b0a8784)
            check_type(argname="argument input_reference_config", value=input_reference_config, expected_type=type_hints["input_reference_config"])
            check_type(argname="argument membership_identifier", value=membership_identifier, expected_type=type_hints["membership_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id_mapping_config", value=id_mapping_config, expected_type=type_hints["id_mapping_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "input_reference_config": input_reference_config,
            "membership_identifier": membership_identifier,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if id_mapping_config is not None:
            self._values["id_mapping_config"] = id_mapping_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def input_reference_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferenceConfigProperty]:
        '''The input reference configuration for the ID namespace association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idnamespaceassociation.html#cfn-cleanrooms-idnamespaceassociation-inputreferenceconfig
        '''
        result = self._values.get("input_reference_config")
        assert result is not None, "Required property 'input_reference_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferenceConfigProperty], result)

    @builtins.property
    def membership_identifier(self) -> builtins.str:
        '''The unique identifier of the membership that contains the ID namespace association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idnamespaceassociation.html#cfn-cleanrooms-idnamespaceassociation-membershipidentifier
        '''
        result = self._values.get("membership_identifier")
        assert result is not None, "Required property 'membership_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of this ID namespace association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idnamespaceassociation.html#cfn-cleanrooms-idnamespaceassociation-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the ID namespace association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idnamespaceassociation.html#cfn-cleanrooms-idnamespaceassociation-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id_mapping_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIdNamespaceAssociation.IdMappingConfigProperty]]:
        '''The configuration settings for the ID mapping table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idnamespaceassociation.html#cfn-cleanrooms-idnamespaceassociation-idmappingconfig
        '''
        result = self._values.get("id_mapping_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIdNamespaceAssociation.IdMappingConfigProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.

        Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-idnamespaceassociation.html#cfn-cleanrooms-idnamespaceassociation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIdNamespaceAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnMembership(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembership",
):
    '''Creates a membership for a specific collaboration identifier and joins the collaboration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html
    :cloudformationResource: AWS::CleanRooms::Membership
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanrooms as cleanrooms
        
        cfn_membership = cleanrooms.CfnMembership(self, "MyCfnMembership",
            collaboration_identifier="collaborationIdentifier",
            query_log_status="queryLogStatus",
        
            # the properties below are optional
            default_job_result_configuration=cleanrooms.CfnMembership.MembershipProtectedJobResultConfigurationProperty(
                output_configuration=cleanrooms.CfnMembership.MembershipProtectedJobOutputConfigurationProperty(
                    s3=cleanrooms.CfnMembership.ProtectedJobS3OutputConfigurationInputProperty(
                        bucket="bucket",
        
                        # the properties below are optional
                        key_prefix="keyPrefix"
                    )
                ),
                role_arn="roleArn"
            ),
            default_result_configuration=cleanrooms.CfnMembership.MembershipProtectedQueryResultConfigurationProperty(
                output_configuration=cleanrooms.CfnMembership.MembershipProtectedQueryOutputConfigurationProperty(
                    s3=cleanrooms.CfnMembership.ProtectedQueryS3OutputConfigurationProperty(
                        bucket="bucket",
                        result_format="resultFormat",
        
                        # the properties below are optional
                        key_prefix="keyPrefix",
                        single_file_output=False
                    )
                ),
        
                # the properties below are optional
                role_arn="roleArn"
            ),
            job_log_status="jobLogStatus",
            payment_configuration=cleanrooms.CfnMembership.MembershipPaymentConfigurationProperty(
                query_compute=cleanrooms.CfnMembership.MembershipQueryComputePaymentConfigProperty(
                    is_responsible=False
                ),
        
                # the properties below are optional
                job_compute=cleanrooms.CfnMembership.MembershipJobComputePaymentConfigProperty(
                    is_responsible=False
                ),
                machine_learning=cleanrooms.CfnMembership.MembershipMLPaymentConfigProperty(
                    model_inference=cleanrooms.CfnMembership.MembershipModelInferencePaymentConfigProperty(
                        is_responsible=False
                    ),
                    model_training=cleanrooms.CfnMembership.MembershipModelTrainingPaymentConfigProperty(
                        is_responsible=False
                    )
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
        collaboration_identifier: builtins.str,
        query_log_status: builtins.str,
        default_job_result_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMembership.MembershipProtectedJobResultConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        default_result_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMembership.MembershipProtectedQueryResultConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        job_log_status: typing.Optional[builtins.str] = None,
        payment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMembership.MembershipPaymentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param collaboration_identifier: The unique ID for the associated collaboration.
        :param query_log_status: An indicator as to whether query logging has been enabled or disabled for the membership. When ``ENABLED`` , AWS Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is ``DISABLED`` .
        :param default_job_result_configuration: The default job result configuration for the membership.
        :param default_result_configuration: The default protected query result configuration as specified by the member who can receive results.
        :param job_log_status: An indicator as to whether job logging has been enabled or disabled for the collaboration. When ``ENABLED`` , AWS Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is ``DISABLED`` .
        :param payment_configuration: The payment responsibilities accepted by the collaboration member.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74d43efdc8d8359f9de6878ad0f2d25ff79e584d96e5ca863178e6f14312cec1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMembershipProps(
            collaboration_identifier=collaboration_identifier,
            query_log_status=query_log_status,
            default_job_result_configuration=default_job_result_configuration,
            default_result_configuration=default_result_configuration,
            job_log_status=job_log_status,
            payment_configuration=payment_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f53a7e47a69cc6ee8550050a85dd5bd1dab4134d650a0e20c9312e56ea80fc60)
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
            type_hints = typing.get_type_hints(_typecheckingstub__78e173bbe42542972b47c21576e57269fe216eab7a86b44fadf695b6653d493d)
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
        '''Returns the Amazon Resource Name (ARN) of the specified membership.

        Example: ``arn:aws:cleanrooms:us-east-1:111122223333:membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollaborationArn")
    def attr_collaboration_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of the specified collaboration.

        Example: ``arn:aws:cleanrooms:us-east-1:111122223333:collaboration/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``

        :cloudformationAttribute: CollaborationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollaborationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollaborationCreatorAccountId")
    def attr_collaboration_creator_account_id(self) -> builtins.str:
        '''Returns the unique identifier of the specified collaboration creator account.

        Example: ``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``

        :cloudformationAttribute: CollaborationCreatorAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollaborationCreatorAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrMembershipIdentifier")
    def attr_membership_identifier(self) -> builtins.str:
        '''Returns the unique identifier of the specified membership.

        Example: ``a1b2c3d4-5678-90ab-cdef-EXAMPLE22222``

        :cloudformationAttribute: MembershipIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMembershipIdentifier"))

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
    @jsii.member(jsii_name="collaborationIdentifier")
    def collaboration_identifier(self) -> builtins.str:
        '''The unique ID for the associated collaboration.'''
        return typing.cast(builtins.str, jsii.get(self, "collaborationIdentifier"))

    @collaboration_identifier.setter
    def collaboration_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba2cc6691bad0d4fdbfa43d453737e19bbcc1b63648ed884849a27170f877099)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collaborationIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="queryLogStatus")
    def query_log_status(self) -> builtins.str:
        '''An indicator as to whether query logging has been enabled or disabled for the membership.'''
        return typing.cast(builtins.str, jsii.get(self, "queryLogStatus"))

    @query_log_status.setter
    def query_log_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bee80a156c452c78946d81f28dfee88d47d5702e2d1eeb7a5c7aeb167b25400e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryLogStatus", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultJobResultConfiguration")
    def default_job_result_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipProtectedJobResultConfigurationProperty"]]:
        '''The default job result configuration for the membership.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipProtectedJobResultConfigurationProperty"]], jsii.get(self, "defaultJobResultConfiguration"))

    @default_job_result_configuration.setter
    def default_job_result_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipProtectedJobResultConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fae73e4481dcc5cfeba1d7ce37a48095412d812d6a76939d24017d3e50e600fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultJobResultConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultResultConfiguration")
    def default_result_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipProtectedQueryResultConfigurationProperty"]]:
        '''The default protected query result configuration as specified by the member who can receive results.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipProtectedQueryResultConfigurationProperty"]], jsii.get(self, "defaultResultConfiguration"))

    @default_result_configuration.setter
    def default_result_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipProtectedQueryResultConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad055649202ffbf3de067877d88fa96b564e1efb0b59d9afaceb04f351ce0c65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultResultConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="jobLogStatus")
    def job_log_status(self) -> typing.Optional[builtins.str]:
        '''An indicator as to whether job logging has been enabled or disabled for the collaboration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobLogStatus"))

    @job_log_status.setter
    def job_log_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38062eee31563e49c149bef3fc9159c7dcbe0d1c37a73eb1b26fde91bcde4dd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobLogStatus", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="paymentConfiguration")
    def payment_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipPaymentConfigurationProperty"]]:
        '''The payment responsibilities accepted by the collaboration member.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipPaymentConfigurationProperty"]], jsii.get(self, "paymentConfiguration"))

    @payment_configuration.setter
    def payment_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipPaymentConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f2d4b43043fdc1c0f794c725e0fa34d3d42d2b231edc34464fcc237ea7aa6d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paymentConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efad84033de32d67e94b9ac23a8d3176e7fc904203e000dac066b28793fec68b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembership.MembershipJobComputePaymentConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"is_responsible": "isResponsible"},
    )
    class MembershipJobComputePaymentConfigProperty:
        def __init__(
            self,
            *,
            is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''An object representing the payment responsibilities accepted by the collaboration member for query and job compute costs.

            :param is_responsible: Indicates whether the collaboration member has accepted to pay for job compute costs ( ``TRUE`` ) or has not accepted to pay for query and job compute costs ( ``FALSE`` ). There is only one member who pays for queries and jobs. An error message is returned for the following reasons: - If you set the value to ``FALSE`` but you are responsible to pay for query and job compute costs. - If you set the value to ``TRUE`` but you are not responsible to pay for query and job compute costs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipjobcomputepaymentconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                membership_job_compute_payment_config_property = cleanrooms.CfnMembership.MembershipJobComputePaymentConfigProperty(
                    is_responsible=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e65ed6ced5134c54f82464bc8236090d903d3f26a591c4dc337a7344c43ce7e8)
                check_type(argname="argument is_responsible", value=is_responsible, expected_type=type_hints["is_responsible"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "is_responsible": is_responsible,
            }

        @builtins.property
        def is_responsible(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether the collaboration member has accepted to pay for job compute costs ( ``TRUE`` ) or has not accepted to pay for query and job compute costs ( ``FALSE`` ).

            There is only one member who pays for queries and jobs.

            An error message is returned for the following reasons:

            - If you set the value to ``FALSE`` but you are responsible to pay for query and job compute costs.
            - If you set the value to ``TRUE`` but you are not responsible to pay for query and job compute costs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipjobcomputepaymentconfig.html#cfn-cleanrooms-membership-membershipjobcomputepaymentconfig-isresponsible
            '''
            result = self._values.get("is_responsible")
            assert result is not None, "Required property 'is_responsible' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MembershipJobComputePaymentConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembership.MembershipMLPaymentConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "model_inference": "modelInference",
            "model_training": "modelTraining",
        },
    )
    class MembershipMLPaymentConfigProperty:
        def __init__(
            self,
            *,
            model_inference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMembership.MembershipModelInferencePaymentConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            model_training: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMembership.MembershipModelTrainingPaymentConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An object representing the collaboration member's machine learning payment responsibilities set by the collaboration creator.

            :param model_inference: The payment responsibilities accepted by the member for model inference.
            :param model_training: The payment responsibilities accepted by the member for model training.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipmlpaymentconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                membership_mLPayment_config_property = cleanrooms.CfnMembership.MembershipMLPaymentConfigProperty(
                    model_inference=cleanrooms.CfnMembership.MembershipModelInferencePaymentConfigProperty(
                        is_responsible=False
                    ),
                    model_training=cleanrooms.CfnMembership.MembershipModelTrainingPaymentConfigProperty(
                        is_responsible=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__13dd2d08b2612b2890adb3362ea4e5bebe48abd3cfb27c026a48fcd95bd347dd)
                check_type(argname="argument model_inference", value=model_inference, expected_type=type_hints["model_inference"])
                check_type(argname="argument model_training", value=model_training, expected_type=type_hints["model_training"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if model_inference is not None:
                self._values["model_inference"] = model_inference
            if model_training is not None:
                self._values["model_training"] = model_training

        @builtins.property
        def model_inference(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipModelInferencePaymentConfigProperty"]]:
            '''The payment responsibilities accepted by the member for model inference.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipmlpaymentconfig.html#cfn-cleanrooms-membership-membershipmlpaymentconfig-modelinference
            '''
            result = self._values.get("model_inference")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipModelInferencePaymentConfigProperty"]], result)

        @builtins.property
        def model_training(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipModelTrainingPaymentConfigProperty"]]:
            '''The payment responsibilities accepted by the member for model training.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipmlpaymentconfig.html#cfn-cleanrooms-membership-membershipmlpaymentconfig-modeltraining
            '''
            result = self._values.get("model_training")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipModelTrainingPaymentConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MembershipMLPaymentConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembership.MembershipModelInferencePaymentConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"is_responsible": "isResponsible"},
    )
    class MembershipModelInferencePaymentConfigProperty:
        def __init__(
            self,
            *,
            is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''An object representing the collaboration member's model inference payment responsibilities set by the collaboration creator.

            :param is_responsible: Indicates whether the collaboration member has accepted to pay for model inference costs ( ``TRUE`` ) or has not accepted to pay for model inference costs ( ``FALSE`` ). If the collaboration creator has not specified anyone to pay for model inference costs, then the member who can query is the default payer. An error message is returned for the following reasons: - If you set the value to ``FALSE`` but you are responsible to pay for model inference costs. - If you set the value to ``TRUE`` but you are not responsible to pay for model inference costs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipmodelinferencepaymentconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                membership_model_inference_payment_config_property = cleanrooms.CfnMembership.MembershipModelInferencePaymentConfigProperty(
                    is_responsible=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2b782e5294b8bba99405cc5a7ca5c775fb2010013a32d43d0fdf4a2878964aca)
                check_type(argname="argument is_responsible", value=is_responsible, expected_type=type_hints["is_responsible"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "is_responsible": is_responsible,
            }

        @builtins.property
        def is_responsible(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether the collaboration member has accepted to pay for model inference costs ( ``TRUE`` ) or has not accepted to pay for model inference costs ( ``FALSE`` ).

            If the collaboration creator has not specified anyone to pay for model inference costs, then the member who can query is the default payer.

            An error message is returned for the following reasons:

            - If you set the value to ``FALSE`` but you are responsible to pay for model inference costs.
            - If you set the value to ``TRUE`` but you are not responsible to pay for model inference costs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipmodelinferencepaymentconfig.html#cfn-cleanrooms-membership-membershipmodelinferencepaymentconfig-isresponsible
            '''
            result = self._values.get("is_responsible")
            assert result is not None, "Required property 'is_responsible' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MembershipModelInferencePaymentConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembership.MembershipModelTrainingPaymentConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"is_responsible": "isResponsible"},
    )
    class MembershipModelTrainingPaymentConfigProperty:
        def __init__(
            self,
            *,
            is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''An object representing the collaboration member's model training payment responsibilities set by the collaboration creator.

            :param is_responsible: Indicates whether the collaboration member has accepted to pay for model training costs ( ``TRUE`` ) or has not accepted to pay for model training costs ( ``FALSE`` ). If the collaboration creator has not specified anyone to pay for model training costs, then the member who can query is the default payer. An error message is returned for the following reasons: - If you set the value to ``FALSE`` but you are responsible to pay for model training costs. - If you set the value to ``TRUE`` but you are not responsible to pay for model training costs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipmodeltrainingpaymentconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                membership_model_training_payment_config_property = cleanrooms.CfnMembership.MembershipModelTrainingPaymentConfigProperty(
                    is_responsible=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8e5c7b5216c60ffcb694e1961e057ff77a03ba6ae0c1cd13b03497dc0f0df235)
                check_type(argname="argument is_responsible", value=is_responsible, expected_type=type_hints["is_responsible"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "is_responsible": is_responsible,
            }

        @builtins.property
        def is_responsible(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether the collaboration member has accepted to pay for model training costs ( ``TRUE`` ) or has not accepted to pay for model training costs ( ``FALSE`` ).

            If the collaboration creator has not specified anyone to pay for model training costs, then the member who can query is the default payer.

            An error message is returned for the following reasons:

            - If you set the value to ``FALSE`` but you are responsible to pay for model training costs.
            - If you set the value to ``TRUE`` but you are not responsible to pay for model training costs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipmodeltrainingpaymentconfig.html#cfn-cleanrooms-membership-membershipmodeltrainingpaymentconfig-isresponsible
            '''
            result = self._values.get("is_responsible")
            assert result is not None, "Required property 'is_responsible' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MembershipModelTrainingPaymentConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembership.MembershipPaymentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "query_compute": "queryCompute",
            "job_compute": "jobCompute",
            "machine_learning": "machineLearning",
        },
    )
    class MembershipPaymentConfigurationProperty:
        def __init__(
            self,
            *,
            query_compute: typing.Union[_IResolvable_da3f097b, typing.Union["CfnMembership.MembershipQueryComputePaymentConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            job_compute: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMembership.MembershipJobComputePaymentConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            machine_learning: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMembership.MembershipMLPaymentConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An object representing the payment responsibilities accepted by the collaboration member.

            :param query_compute: The payment responsibilities accepted by the collaboration member for query compute costs.
            :param job_compute: The payment responsibilities accepted by the collaboration member for job compute costs.
            :param machine_learning: The payment responsibilities accepted by the collaboration member for machine learning costs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershippaymentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                membership_payment_configuration_property = cleanrooms.CfnMembership.MembershipPaymentConfigurationProperty(
                    query_compute=cleanrooms.CfnMembership.MembershipQueryComputePaymentConfigProperty(
                        is_responsible=False
                    ),
                
                    # the properties below are optional
                    job_compute=cleanrooms.CfnMembership.MembershipJobComputePaymentConfigProperty(
                        is_responsible=False
                    ),
                    machine_learning=cleanrooms.CfnMembership.MembershipMLPaymentConfigProperty(
                        model_inference=cleanrooms.CfnMembership.MembershipModelInferencePaymentConfigProperty(
                            is_responsible=False
                        ),
                        model_training=cleanrooms.CfnMembership.MembershipModelTrainingPaymentConfigProperty(
                            is_responsible=False
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ff9b623af3a2e12d6db7063d2191f9dad178b00c5e761d332496d6065f45dfe6)
                check_type(argname="argument query_compute", value=query_compute, expected_type=type_hints["query_compute"])
                check_type(argname="argument job_compute", value=job_compute, expected_type=type_hints["job_compute"])
                check_type(argname="argument machine_learning", value=machine_learning, expected_type=type_hints["machine_learning"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "query_compute": query_compute,
            }
            if job_compute is not None:
                self._values["job_compute"] = job_compute
            if machine_learning is not None:
                self._values["machine_learning"] = machine_learning

        @builtins.property
        def query_compute(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipQueryComputePaymentConfigProperty"]:
            '''The payment responsibilities accepted by the collaboration member for query compute costs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershippaymentconfiguration.html#cfn-cleanrooms-membership-membershippaymentconfiguration-querycompute
            '''
            result = self._values.get("query_compute")
            assert result is not None, "Required property 'query_compute' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipQueryComputePaymentConfigProperty"], result)

        @builtins.property
        def job_compute(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipJobComputePaymentConfigProperty"]]:
            '''The payment responsibilities accepted by the collaboration member for job compute costs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershippaymentconfiguration.html#cfn-cleanrooms-membership-membershippaymentconfiguration-jobcompute
            '''
            result = self._values.get("job_compute")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipJobComputePaymentConfigProperty"]], result)

        @builtins.property
        def machine_learning(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipMLPaymentConfigProperty"]]:
            '''The payment responsibilities accepted by the collaboration member for machine learning costs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershippaymentconfiguration.html#cfn-cleanrooms-membership-membershippaymentconfiguration-machinelearning
            '''
            result = self._values.get("machine_learning")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipMLPaymentConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MembershipPaymentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembership.MembershipProtectedJobOutputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3": "s3"},
    )
    class MembershipProtectedJobOutputConfigurationProperty:
        def __init__(
            self,
            *,
            s3: typing.Union[_IResolvable_da3f097b, typing.Union["CfnMembership.ProtectedJobS3OutputConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Contains configurations for protected job results.

            :param s3: Contains the configuration to write the job results to S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedjoboutputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                membership_protected_job_output_configuration_property = cleanrooms.CfnMembership.MembershipProtectedJobOutputConfigurationProperty(
                    s3=cleanrooms.CfnMembership.ProtectedJobS3OutputConfigurationInputProperty(
                        bucket="bucket",
                
                        # the properties below are optional
                        key_prefix="keyPrefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__04b0307caf7eb009735af65a413fe8c877c870d384cffc49ef1a36d9699ba548)
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3": s3,
            }

        @builtins.property
        def s3(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnMembership.ProtectedJobS3OutputConfigurationInputProperty"]:
            '''Contains the configuration to write the job results to S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedjoboutputconfiguration.html#cfn-cleanrooms-membership-membershipprotectedjoboutputconfiguration-s3
            '''
            result = self._values.get("s3")
            assert result is not None, "Required property 's3' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnMembership.ProtectedJobS3OutputConfigurationInputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MembershipProtectedJobOutputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembership.MembershipProtectedJobResultConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "output_configuration": "outputConfiguration",
            "role_arn": "roleArn",
        },
    )
    class MembershipProtectedJobResultConfigurationProperty:
        def __init__(
            self,
            *,
            output_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnMembership.MembershipProtectedJobOutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            role_arn: builtins.str,
        ) -> None:
            '''Contains configurations for protected job results.

            :param output_configuration: The output configuration for a protected job result.
            :param role_arn: The unique ARN for an IAM role that is used by AWS Clean Rooms to write protected job results to the result location, given by the member who can receive results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedjobresultconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                membership_protected_job_result_configuration_property = cleanrooms.CfnMembership.MembershipProtectedJobResultConfigurationProperty(
                    output_configuration=cleanrooms.CfnMembership.MembershipProtectedJobOutputConfigurationProperty(
                        s3=cleanrooms.CfnMembership.ProtectedJobS3OutputConfigurationInputProperty(
                            bucket="bucket",
                
                            # the properties below are optional
                            key_prefix="keyPrefix"
                        )
                    ),
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b28ab623b930079e7e4df6a230e428f58f7ad919a987f38ecf686a4238ab5b47)
                check_type(argname="argument output_configuration", value=output_configuration, expected_type=type_hints["output_configuration"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "output_configuration": output_configuration,
                "role_arn": role_arn,
            }

        @builtins.property
        def output_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipProtectedJobOutputConfigurationProperty"]:
            '''The output configuration for a protected job result.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedjobresultconfiguration.html#cfn-cleanrooms-membership-membershipprotectedjobresultconfiguration-outputconfiguration
            '''
            result = self._values.get("output_configuration")
            assert result is not None, "Required property 'output_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipProtectedJobOutputConfigurationProperty"], result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The unique ARN for an IAM role that is used by AWS Clean Rooms to write protected job results to the result location, given by the member who can receive results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedjobresultconfiguration.html#cfn-cleanrooms-membership-membershipprotectedjobresultconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MembershipProtectedJobResultConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembership.MembershipProtectedQueryOutputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3": "s3"},
    )
    class MembershipProtectedQueryOutputConfigurationProperty:
        def __init__(
            self,
            *,
            s3: typing.Union[_IResolvable_da3f097b, typing.Union["CfnMembership.ProtectedQueryS3OutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Contains configurations for protected query results.

            :param s3: Required configuration for a protected query with an ``s3`` output type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedqueryoutputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                membership_protected_query_output_configuration_property = cleanrooms.CfnMembership.MembershipProtectedQueryOutputConfigurationProperty(
                    s3=cleanrooms.CfnMembership.ProtectedQueryS3OutputConfigurationProperty(
                        bucket="bucket",
                        result_format="resultFormat",
                
                        # the properties below are optional
                        key_prefix="keyPrefix",
                        single_file_output=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__95a2754aa7d946646d057afbcf1d05c839a09b522b0215f8c6ff427a564f624b)
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3": s3,
            }

        @builtins.property
        def s3(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnMembership.ProtectedQueryS3OutputConfigurationProperty"]:
            '''Required configuration for a protected query with an ``s3`` output type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedqueryoutputconfiguration.html#cfn-cleanrooms-membership-membershipprotectedqueryoutputconfiguration-s3
            '''
            result = self._values.get("s3")
            assert result is not None, "Required property 's3' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnMembership.ProtectedQueryS3OutputConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MembershipProtectedQueryOutputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembership.MembershipProtectedQueryResultConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "output_configuration": "outputConfiguration",
            "role_arn": "roleArn",
        },
    )
    class MembershipProtectedQueryResultConfigurationProperty:
        def __init__(
            self,
            *,
            output_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnMembership.MembershipProtectedQueryOutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains configurations for protected query results.

            :param output_configuration: Configuration for protected query results.
            :param role_arn: The unique ARN for an IAM role that is used by AWS Clean Rooms to write protected query results to the result location, given by the member who can receive results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedqueryresultconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                membership_protected_query_result_configuration_property = cleanrooms.CfnMembership.MembershipProtectedQueryResultConfigurationProperty(
                    output_configuration=cleanrooms.CfnMembership.MembershipProtectedQueryOutputConfigurationProperty(
                        s3=cleanrooms.CfnMembership.ProtectedQueryS3OutputConfigurationProperty(
                            bucket="bucket",
                            result_format="resultFormat",
                
                            # the properties below are optional
                            key_prefix="keyPrefix",
                            single_file_output=False
                        )
                    ),
                
                    # the properties below are optional
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5ac8c4043e48c89672053a73e33884a2912eeea08d43d7abf8e69c928dcadc65)
                check_type(argname="argument output_configuration", value=output_configuration, expected_type=type_hints["output_configuration"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "output_configuration": output_configuration,
            }
            if role_arn is not None:
                self._values["role_arn"] = role_arn

        @builtins.property
        def output_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipProtectedQueryOutputConfigurationProperty"]:
            '''Configuration for protected query results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedqueryresultconfiguration.html#cfn-cleanrooms-membership-membershipprotectedqueryresultconfiguration-outputconfiguration
            '''
            result = self._values.get("output_configuration")
            assert result is not None, "Required property 'output_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnMembership.MembershipProtectedQueryOutputConfigurationProperty"], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The unique ARN for an IAM role that is used by AWS Clean Rooms to write protected query results to the result location, given by the member who can receive results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipprotectedqueryresultconfiguration.html#cfn-cleanrooms-membership-membershipprotectedqueryresultconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MembershipProtectedQueryResultConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembership.MembershipQueryComputePaymentConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"is_responsible": "isResponsible"},
    )
    class MembershipQueryComputePaymentConfigProperty:
        def __init__(
            self,
            *,
            is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''An object representing the payment responsibilities accepted by the collaboration member for query compute costs.

            :param is_responsible: Indicates whether the collaboration member has accepted to pay for query compute costs ( ``TRUE`` ) or has not accepted to pay for query compute costs ( ``FALSE`` ). If the collaboration creator has not specified anyone to pay for query compute costs, then the member who can query is the default payer. An error message is returned for the following reasons: - If you set the value to ``FALSE`` but you are responsible to pay for query compute costs. - If you set the value to ``TRUE`` but you are not responsible to pay for query compute costs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipquerycomputepaymentconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                membership_query_compute_payment_config_property = cleanrooms.CfnMembership.MembershipQueryComputePaymentConfigProperty(
                    is_responsible=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3a0b18d278e5a5581d13248fe664b26d08f194e496fc961110d71d330026e192)
                check_type(argname="argument is_responsible", value=is_responsible, expected_type=type_hints["is_responsible"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "is_responsible": is_responsible,
            }

        @builtins.property
        def is_responsible(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether the collaboration member has accepted to pay for query compute costs ( ``TRUE`` ) or has not accepted to pay for query compute costs ( ``FALSE`` ).

            If the collaboration creator has not specified anyone to pay for query compute costs, then the member who can query is the default payer.

            An error message is returned for the following reasons:

            - If you set the value to ``FALSE`` but you are responsible to pay for query compute costs.
            - If you set the value to ``TRUE`` but you are not responsible to pay for query compute costs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-membershipquerycomputepaymentconfig.html#cfn-cleanrooms-membership-membershipquerycomputepaymentconfig-isresponsible
            '''
            result = self._values.get("is_responsible")
            assert result is not None, "Required property 'is_responsible' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MembershipQueryComputePaymentConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembership.ProtectedJobS3OutputConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key_prefix": "keyPrefix"},
    )
    class ProtectedJobS3OutputConfigurationInputProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains input information for protected jobs with an S3 output type.

            :param bucket: The S3 bucket for job output.
            :param key_prefix: The S3 prefix to unload the protected job results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-protectedjobs3outputconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                protected_job_s3_output_configuration_input_property = cleanrooms.CfnMembership.ProtectedJobS3OutputConfigurationInputProperty(
                    bucket="bucket",
                
                    # the properties below are optional
                    key_prefix="keyPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d3e8066041ab5d5ba65ac44f96738cb04449874735750f11b6331de6bf9fda0c)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key_prefix", value=key_prefix, expected_type=type_hints["key_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
            }
            if key_prefix is not None:
                self._values["key_prefix"] = key_prefix

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The S3 bucket for job output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-protectedjobs3outputconfigurationinput.html#cfn-cleanrooms-membership-protectedjobs3outputconfigurationinput-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_prefix(self) -> typing.Optional[builtins.str]:
            '''The S3 prefix to unload the protected job results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-protectedjobs3outputconfigurationinput.html#cfn-cleanrooms-membership-protectedjobs3outputconfigurationinput-keyprefix
            '''
            result = self._values.get("key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProtectedJobS3OutputConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembership.ProtectedQueryS3OutputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "result_format": "resultFormat",
            "key_prefix": "keyPrefix",
            "single_file_output": "singleFileOutput",
        },
    )
    class ProtectedQueryS3OutputConfigurationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            result_format: builtins.str,
            key_prefix: typing.Optional[builtins.str] = None,
            single_file_output: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Contains the configuration to write the query results to S3.

            :param bucket: The S3 bucket to unload the protected query results.
            :param result_format: Intended file format of the result.
            :param key_prefix: The S3 prefix to unload the protected query results.
            :param single_file_output: Indicates whether files should be output as a single file ( ``TRUE`` ) or output as multiple files ( ``FALSE`` ). This parameter is only supported for analyses with the Spark analytics engine.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                protected_query_s3_output_configuration_property = cleanrooms.CfnMembership.ProtectedQueryS3OutputConfigurationProperty(
                    bucket="bucket",
                    result_format="resultFormat",
                
                    # the properties below are optional
                    key_prefix="keyPrefix",
                    single_file_output=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a9188eb901d25d30e10ffe45a67a0477e30fc05a712c633d687872210f716c3a)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument result_format", value=result_format, expected_type=type_hints["result_format"])
                check_type(argname="argument key_prefix", value=key_prefix, expected_type=type_hints["key_prefix"])
                check_type(argname="argument single_file_output", value=single_file_output, expected_type=type_hints["single_file_output"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "result_format": result_format,
            }
            if key_prefix is not None:
                self._values["key_prefix"] = key_prefix
            if single_file_output is not None:
                self._values["single_file_output"] = single_file_output

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The S3 bucket to unload the protected query results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration.html#cfn-cleanrooms-membership-protectedquerys3outputconfiguration-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def result_format(self) -> builtins.str:
            '''Intended file format of the result.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration.html#cfn-cleanrooms-membership-protectedquerys3outputconfiguration-resultformat
            '''
            result = self._values.get("result_format")
            assert result is not None, "Required property 'result_format' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_prefix(self) -> typing.Optional[builtins.str]:
            '''The S3 prefix to unload the protected query results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration.html#cfn-cleanrooms-membership-protectedquerys3outputconfiguration-keyprefix
            '''
            result = self._values.get("key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def single_file_output(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether files should be output as a single file ( ``TRUE`` ) or output as multiple files ( ``FALSE`` ).

            This parameter is only supported for analyses with the Spark analytics engine.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-membership-protectedquerys3outputconfiguration.html#cfn-cleanrooms-membership-protectedquerys3outputconfiguration-singlefileoutput
            '''
            result = self._values.get("single_file_output")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProtectedQueryS3OutputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnMembershipProps",
    jsii_struct_bases=[],
    name_mapping={
        "collaboration_identifier": "collaborationIdentifier",
        "query_log_status": "queryLogStatus",
        "default_job_result_configuration": "defaultJobResultConfiguration",
        "default_result_configuration": "defaultResultConfiguration",
        "job_log_status": "jobLogStatus",
        "payment_configuration": "paymentConfiguration",
        "tags": "tags",
    },
)
class CfnMembershipProps:
    def __init__(
        self,
        *,
        collaboration_identifier: builtins.str,
        query_log_status: builtins.str,
        default_job_result_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipProtectedJobResultConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        default_result_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipProtectedQueryResultConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        job_log_status: typing.Optional[builtins.str] = None,
        payment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipPaymentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMembership``.

        :param collaboration_identifier: The unique ID for the associated collaboration.
        :param query_log_status: An indicator as to whether query logging has been enabled or disabled for the membership. When ``ENABLED`` , AWS Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is ``DISABLED`` .
        :param default_job_result_configuration: The default job result configuration for the membership.
        :param default_result_configuration: The default protected query result configuration as specified by the member who can receive results.
        :param job_log_status: An indicator as to whether job logging has been enabled or disabled for the collaboration. When ``ENABLED`` , AWS Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is ``DISABLED`` .
        :param payment_configuration: The payment responsibilities accepted by the collaboration member.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanrooms as cleanrooms
            
            cfn_membership_props = cleanrooms.CfnMembershipProps(
                collaboration_identifier="collaborationIdentifier",
                query_log_status="queryLogStatus",
            
                # the properties below are optional
                default_job_result_configuration=cleanrooms.CfnMembership.MembershipProtectedJobResultConfigurationProperty(
                    output_configuration=cleanrooms.CfnMembership.MembershipProtectedJobOutputConfigurationProperty(
                        s3=cleanrooms.CfnMembership.ProtectedJobS3OutputConfigurationInputProperty(
                            bucket="bucket",
            
                            # the properties below are optional
                            key_prefix="keyPrefix"
                        )
                    ),
                    role_arn="roleArn"
                ),
                default_result_configuration=cleanrooms.CfnMembership.MembershipProtectedQueryResultConfigurationProperty(
                    output_configuration=cleanrooms.CfnMembership.MembershipProtectedQueryOutputConfigurationProperty(
                        s3=cleanrooms.CfnMembership.ProtectedQueryS3OutputConfigurationProperty(
                            bucket="bucket",
                            result_format="resultFormat",
            
                            # the properties below are optional
                            key_prefix="keyPrefix",
                            single_file_output=False
                        )
                    ),
            
                    # the properties below are optional
                    role_arn="roleArn"
                ),
                job_log_status="jobLogStatus",
                payment_configuration=cleanrooms.CfnMembership.MembershipPaymentConfigurationProperty(
                    query_compute=cleanrooms.CfnMembership.MembershipQueryComputePaymentConfigProperty(
                        is_responsible=False
                    ),
            
                    # the properties below are optional
                    job_compute=cleanrooms.CfnMembership.MembershipJobComputePaymentConfigProperty(
                        is_responsible=False
                    ),
                    machine_learning=cleanrooms.CfnMembership.MembershipMLPaymentConfigProperty(
                        model_inference=cleanrooms.CfnMembership.MembershipModelInferencePaymentConfigProperty(
                            is_responsible=False
                        ),
                        model_training=cleanrooms.CfnMembership.MembershipModelTrainingPaymentConfigProperty(
                            is_responsible=False
                        )
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a7030966bdb99200cf7aff97662a2ef1e02754d2c014bc030475065ea06e0da)
            check_type(argname="argument collaboration_identifier", value=collaboration_identifier, expected_type=type_hints["collaboration_identifier"])
            check_type(argname="argument query_log_status", value=query_log_status, expected_type=type_hints["query_log_status"])
            check_type(argname="argument default_job_result_configuration", value=default_job_result_configuration, expected_type=type_hints["default_job_result_configuration"])
            check_type(argname="argument default_result_configuration", value=default_result_configuration, expected_type=type_hints["default_result_configuration"])
            check_type(argname="argument job_log_status", value=job_log_status, expected_type=type_hints["job_log_status"])
            check_type(argname="argument payment_configuration", value=payment_configuration, expected_type=type_hints["payment_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "collaboration_identifier": collaboration_identifier,
            "query_log_status": query_log_status,
        }
        if default_job_result_configuration is not None:
            self._values["default_job_result_configuration"] = default_job_result_configuration
        if default_result_configuration is not None:
            self._values["default_result_configuration"] = default_result_configuration
        if job_log_status is not None:
            self._values["job_log_status"] = job_log_status
        if payment_configuration is not None:
            self._values["payment_configuration"] = payment_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def collaboration_identifier(self) -> builtins.str:
        '''The unique ID for the associated collaboration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html#cfn-cleanrooms-membership-collaborationidentifier
        '''
        result = self._values.get("collaboration_identifier")
        assert result is not None, "Required property 'collaboration_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_log_status(self) -> builtins.str:
        '''An indicator as to whether query logging has been enabled or disabled for the membership.

        When ``ENABLED`` , AWS Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is ``DISABLED`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html#cfn-cleanrooms-membership-querylogstatus
        '''
        result = self._values.get("query_log_status")
        assert result is not None, "Required property 'query_log_status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_job_result_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMembership.MembershipProtectedJobResultConfigurationProperty]]:
        '''The default job result configuration for the membership.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html#cfn-cleanrooms-membership-defaultjobresultconfiguration
        '''
        result = self._values.get("default_job_result_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMembership.MembershipProtectedJobResultConfigurationProperty]], result)

    @builtins.property
    def default_result_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMembership.MembershipProtectedQueryResultConfigurationProperty]]:
        '''The default protected query result configuration as specified by the member who can receive results.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html#cfn-cleanrooms-membership-defaultresultconfiguration
        '''
        result = self._values.get("default_result_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMembership.MembershipProtectedQueryResultConfigurationProperty]], result)

    @builtins.property
    def job_log_status(self) -> typing.Optional[builtins.str]:
        '''An indicator as to whether job logging has been enabled or disabled for the collaboration.

        When ``ENABLED`` , AWS Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is ``DISABLED`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html#cfn-cleanrooms-membership-joblogstatus
        '''
        result = self._values.get("job_log_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def payment_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMembership.MembershipPaymentConfigurationProperty]]:
        '''The payment responsibilities accepted by the collaboration member.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html#cfn-cleanrooms-membership-paymentconfiguration
        '''
        result = self._values.get("payment_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMembership.MembershipPaymentConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.

        Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-membership.html#cfn-cleanrooms-membership-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMembershipProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnPrivacyBudgetTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnPrivacyBudgetTemplate",
):
    '''An object that defines the privacy budget template.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-privacybudgettemplate.html
    :cloudformationResource: AWS::CleanRooms::PrivacyBudgetTemplate
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cleanrooms as cleanrooms
        
        cfn_privacy_budget_template = cleanrooms.CfnPrivacyBudgetTemplate(self, "MyCfnPrivacyBudgetTemplate",
            auto_refresh="autoRefresh",
            membership_identifier="membershipIdentifier",
            parameters=cleanrooms.CfnPrivacyBudgetTemplate.ParametersProperty(
                epsilon=123,
                users_noise_per_query=123
            ),
            privacy_budget_type="privacyBudgetType",
        
            # the properties below are optional
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
        auto_refresh: builtins.str,
        membership_identifier: builtins.str,
        parameters: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPrivacyBudgetTemplate.ParametersProperty", typing.Dict[builtins.str, typing.Any]]],
        privacy_budget_type: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param auto_refresh: How often the privacy budget refreshes. .. epigraph:: If you plan to regularly bring new data into the collaboration, use ``CALENDAR_MONTH`` to automatically get a new privacy budget for the collaboration every calendar month. Choosing this option allows arbitrary amounts of information to be revealed about rows of the data when repeatedly queried across refreshes. Avoid choosing this if the same rows will be repeatedly queried between privacy budget refreshes.
        :param membership_identifier: The identifier for a membership resource.
        :param parameters: Specifies the epsilon and noise parameters for the privacy budget template.
        :param privacy_budget_type: Specifies the type of the privacy budget template.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4ef80e47afb9dceb9f249b561d13bd079011c08e3eadfd7c85afef7b15b6395)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPrivacyBudgetTemplateProps(
            auto_refresh=auto_refresh,
            membership_identifier=membership_identifier,
            parameters=parameters,
            privacy_budget_type=privacy_budget_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4105213a7d3d459c08d1525f399592909787ead616f1a795ab1b4391f1c50f74)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0bf81ecc233447257243d10c0d69e227d4821702f88ae519ba06a04eef3a6730)
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
        '''The ARN of the privacy budget template.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollaborationArn")
    def attr_collaboration_arn(self) -> builtins.str:
        '''The ARN of the collaboration that contains this privacy budget template.

        :cloudformationAttribute: CollaborationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollaborationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCollaborationIdentifier")
    def attr_collaboration_identifier(self) -> builtins.str:
        '''The unique ID of the collaboration that contains this privacy budget template.

        :cloudformationAttribute: CollaborationIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCollaborationIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrMembershipArn")
    def attr_membership_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the member who created the privacy budget template.

        :cloudformationAttribute: MembershipArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMembershipArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPrivacyBudgetTemplateIdentifier")
    def attr_privacy_budget_template_identifier(self) -> builtins.str:
        '''A unique identifier for one of your memberships for a collaboration.

        The privacy budget template is created in the collaboration that this membership belongs to. Accepts a membership ID.

        :cloudformationAttribute: PrivacyBudgetTemplateIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrivacyBudgetTemplateIdentifier"))

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
    @jsii.member(jsii_name="autoRefresh")
    def auto_refresh(self) -> builtins.str:
        '''How often the privacy budget refreshes.'''
        return typing.cast(builtins.str, jsii.get(self, "autoRefresh"))

    @auto_refresh.setter
    def auto_refresh(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aac4d267c9bad45a4e435ea568f943c0e3bf8200eb41fb580c04ae8a221cfdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoRefresh", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="membershipIdentifier")
    def membership_identifier(self) -> builtins.str:
        '''The identifier for a membership resource.'''
        return typing.cast(builtins.str, jsii.get(self, "membershipIdentifier"))

    @membership_identifier.setter
    def membership_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__451d7c98300c47ca24e57e08313a6f1c3e359f595cc6d9bd21ca7564f781be19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "membershipIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnPrivacyBudgetTemplate.ParametersProperty"]:
        '''Specifies the epsilon and noise parameters for the privacy budget template.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPrivacyBudgetTemplate.ParametersProperty"], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnPrivacyBudgetTemplate.ParametersProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f392867d1a4c1fee75cc8b48d97f801894a657d907a13d4d2a21ce8f8e5aeb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="privacyBudgetType")
    def privacy_budget_type(self) -> builtins.str:
        '''Specifies the type of the privacy budget template.'''
        return typing.cast(builtins.str, jsii.get(self, "privacyBudgetType"))

    @privacy_budget_type.setter
    def privacy_budget_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af09670bc39ec5464305b000607d6c8a229830c5ad3234b2a82e4e6004d271df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privacyBudgetType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6baec6343b79fd0bf9b81122904ed3d87c0dfb35be66cc64d471a7a08ddc00f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cleanrooms.CfnPrivacyBudgetTemplate.ParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "epsilon": "epsilon",
            "users_noise_per_query": "usersNoisePerQuery",
        },
    )
    class ParametersProperty:
        def __init__(
            self,
            *,
            epsilon: jsii.Number,
            users_noise_per_query: jsii.Number,
        ) -> None:
            '''Specifies the epsilon and noise parameters for the privacy budget template.

            :param epsilon: The epsilon value that you want to use.
            :param users_noise_per_query: Noise added per query is measured in terms of the number of users whose contributions you want to obscure. This value governs the rate at which the privacy budget is depleted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-privacybudgettemplate-parameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cleanrooms as cleanrooms
                
                parameters_property = cleanrooms.CfnPrivacyBudgetTemplate.ParametersProperty(
                    epsilon=123,
                    users_noise_per_query=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1938eceb4a5ecd53da864bdcbc38554516e8fa365c0dec957d0fe1a8bcdbe3d3)
                check_type(argname="argument epsilon", value=epsilon, expected_type=type_hints["epsilon"])
                check_type(argname="argument users_noise_per_query", value=users_noise_per_query, expected_type=type_hints["users_noise_per_query"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "epsilon": epsilon,
                "users_noise_per_query": users_noise_per_query,
            }

        @builtins.property
        def epsilon(self) -> jsii.Number:
            '''The epsilon value that you want to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-privacybudgettemplate-parameters.html#cfn-cleanrooms-privacybudgettemplate-parameters-epsilon
            '''
            result = self._values.get("epsilon")
            assert result is not None, "Required property 'epsilon' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def users_noise_per_query(self) -> jsii.Number:
            '''Noise added per query is measured in terms of the number of users whose contributions you want to obscure.

            This value governs the rate at which the privacy budget is depleted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cleanrooms-privacybudgettemplate-parameters.html#cfn-cleanrooms-privacybudgettemplate-parameters-usersnoiseperquery
            '''
            result = self._values.get("users_noise_per_query")
            assert result is not None, "Required property 'users_noise_per_query' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cleanrooms.CfnPrivacyBudgetTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "auto_refresh": "autoRefresh",
        "membership_identifier": "membershipIdentifier",
        "parameters": "parameters",
        "privacy_budget_type": "privacyBudgetType",
        "tags": "tags",
    },
)
class CfnPrivacyBudgetTemplateProps:
    def __init__(
        self,
        *,
        auto_refresh: builtins.str,
        membership_identifier: builtins.str,
        parameters: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrivacyBudgetTemplate.ParametersProperty, typing.Dict[builtins.str, typing.Any]]],
        privacy_budget_type: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPrivacyBudgetTemplate``.

        :param auto_refresh: How often the privacy budget refreshes. .. epigraph:: If you plan to regularly bring new data into the collaboration, use ``CALENDAR_MONTH`` to automatically get a new privacy budget for the collaboration every calendar month. Choosing this option allows arbitrary amounts of information to be revealed about rows of the data when repeatedly queried across refreshes. Avoid choosing this if the same rows will be repeatedly queried between privacy budget refreshes.
        :param membership_identifier: The identifier for a membership resource.
        :param parameters: Specifies the epsilon and noise parameters for the privacy budget template.
        :param privacy_budget_type: Specifies the type of the privacy budget template.
        :param tags: An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-privacybudgettemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cleanrooms as cleanrooms
            
            cfn_privacy_budget_template_props = cleanrooms.CfnPrivacyBudgetTemplateProps(
                auto_refresh="autoRefresh",
                membership_identifier="membershipIdentifier",
                parameters=cleanrooms.CfnPrivacyBudgetTemplate.ParametersProperty(
                    epsilon=123,
                    users_noise_per_query=123
                ),
                privacy_budget_type="privacyBudgetType",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7be5c898600ca696463b88a231c1311a56890ce38a77ba2a33d7a9284885c4e0)
            check_type(argname="argument auto_refresh", value=auto_refresh, expected_type=type_hints["auto_refresh"])
            check_type(argname="argument membership_identifier", value=membership_identifier, expected_type=type_hints["membership_identifier"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument privacy_budget_type", value=privacy_budget_type, expected_type=type_hints["privacy_budget_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auto_refresh": auto_refresh,
            "membership_identifier": membership_identifier,
            "parameters": parameters,
            "privacy_budget_type": privacy_budget_type,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def auto_refresh(self) -> builtins.str:
        '''How often the privacy budget refreshes.

        .. epigraph::

           If you plan to regularly bring new data into the collaboration, use ``CALENDAR_MONTH`` to automatically get a new privacy budget for the collaboration every calendar month. Choosing this option allows arbitrary amounts of information to be revealed about rows of the data when repeatedly queried across refreshes. Avoid choosing this if the same rows will be repeatedly queried between privacy budget refreshes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-privacybudgettemplate.html#cfn-cleanrooms-privacybudgettemplate-autorefresh
        '''
        result = self._values.get("auto_refresh")
        assert result is not None, "Required property 'auto_refresh' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def membership_identifier(self) -> builtins.str:
        '''The identifier for a membership resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-privacybudgettemplate.html#cfn-cleanrooms-privacybudgettemplate-membershipidentifier
        '''
        result = self._values.get("membership_identifier")
        assert result is not None, "Required property 'membership_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnPrivacyBudgetTemplate.ParametersProperty]:
        '''Specifies the epsilon and noise parameters for the privacy budget template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-privacybudgettemplate.html#cfn-cleanrooms-privacybudgettemplate-parameters
        '''
        result = self._values.get("parameters")
        assert result is not None, "Required property 'parameters' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnPrivacyBudgetTemplate.ParametersProperty], result)

    @builtins.property
    def privacy_budget_type(self) -> builtins.str:
        '''Specifies the type of the privacy budget template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-privacybudgettemplate.html#cfn-cleanrooms-privacybudgettemplate-privacybudgettype
        '''
        result = self._values.get("privacy_budget_type")
        assert result is not None, "Required property 'privacy_budget_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional label that you can assign to a resource when you create it.

        Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cleanrooms-privacybudgettemplate.html#cfn-cleanrooms-privacybudgettemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPrivacyBudgetTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAnalysisTemplate",
    "CfnAnalysisTemplateProps",
    "CfnCollaboration",
    "CfnCollaborationProps",
    "CfnConfiguredTable",
    "CfnConfiguredTableAssociation",
    "CfnConfiguredTableAssociationProps",
    "CfnConfiguredTableProps",
    "CfnIdMappingTable",
    "CfnIdMappingTableProps",
    "CfnIdNamespaceAssociation",
    "CfnIdNamespaceAssociationProps",
    "CfnMembership",
    "CfnMembershipProps",
    "CfnPrivacyBudgetTemplate",
    "CfnPrivacyBudgetTemplateProps",
]

publication.publish()

def _typecheckingstub__0e650aead4f74afeaf90193249293bee92f9a4eb687f4f9678e1a1368a887bfa(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    format: builtins.str,
    membership_identifier: builtins.str,
    name: builtins.str,
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisSourceProperty, typing.Dict[builtins.str, typing.Any]]],
    analysis_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    schema: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisSchemaProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisSourceMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__def32f8279895eaf5ae2fed796049f11e8ecc1f14c53c7a40e54f77f97722f40(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d2f63941e3ccfc02c5fd40f68748b90631da131360cf742a7aa15eb0547f5b5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a99bf5a96bec195d52c514c174a5c532136760569f0863c25b3672fb0b2a9f3c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__297b2b982e7135bfb11610ac18dcacab85dc955728c10a993db86affc23a6c85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0ca9c50ab5c0e5399ff8164eb04d12b160d7880a66ad5c75586fef748051a2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53060281bd9759f7bd4026827422f1a24050a030c7c5574430af50f44bcdc81f(
    value: typing.Union[_IResolvable_da3f097b, CfnAnalysisTemplate.AnalysisSourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1b12f58b0c5fa25bf8c085bcbec4d711cdcbcd2bcea3e5137ba027e35f34c9f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnalysisTemplate.AnalysisParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8ea0f1530d49d0cf3ea112be450d6887b42e42d18ffdc9233aac36569611c55(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b08707b577f4e2e4847fc726614c034787b0608c33e3b6db3ed058d8262f49f5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnalysisTemplate.AnalysisSchemaProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9971674aa89ce0d927eab26c4a51b41fc5fd99b53e08ed11b02d3b3b8d184899(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnalysisTemplate.AnalysisSourceMetadataProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6d8c0e267965c3e8d9449c75e721dc4e1bccb98212af3c5be762ebb7322d8e8(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f8aaf9054ec461e195e032043672bc5f9f627fd62d4544efda7b3ea2740b2d1(
    *,
    name: builtins.str,
    type: builtins.str,
    default_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f1f3d4aa401aad65536409e9f991c86250c627594c1b918fe7c42b5ac37c097(
    *,
    referenced_tables: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__142df4b782054f1f02b59fba238cf11ed294493aa487afe8597ffefc23299578(
    *,
    artifacts: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisTemplateArtifactMetadataProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbdd92f3241147ec8ad458564c84f6695d3a3e85f93b5190554663d6327c512f(
    *,
    artifacts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisTemplateArtifactsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    text: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__987e835d80cb906f68846a5d130091f8db0105378671d39598489b7cabd5fb36(
    *,
    entry_point_hash: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.HashProperty, typing.Dict[builtins.str, typing.Any]]],
    additional_artifact_hashes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.HashProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f833b582ec423809f565e96fc9ba5d49349ac881791d343e35df1673b1c9644(
    *,
    location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de78ae9ecad686157204e702611c0cf015331e3aa099f1e87ab18d5cd854abfb(
    *,
    entry_point: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisTemplateArtifactProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    additional_artifacts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisTemplateArtifactProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43be85fff22ad377febb791857a9bfd90b262e37e83d363df6adfb5783ea6cb5(
    *,
    sha256: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bb4aaebbf6530b26619974d56993c72a085bd8e9326904d3e54412c155e81e3(
    *,
    bucket: builtins.str,
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1c797e3fa5f8683aa0eb66424f00b6b29c5014d5c45e7771fe0c5b1e9a973e8(
    *,
    format: builtins.str,
    membership_identifier: builtins.str,
    name: builtins.str,
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisSourceProperty, typing.Dict[builtins.str, typing.Any]]],
    analysis_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    schema: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisSchemaProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalysisTemplate.AnalysisSourceMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8995527da9ce4212caf3c1fdf601e4947c02ff1e364e92811ac8635be534111(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    creator_display_name: builtins.str,
    description: builtins.str,
    name: builtins.str,
    query_log_status: builtins.str,
    analytics_engine: typing.Optional[builtins.str] = None,
    creator_member_abilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    creator_ml_member_abilities: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.MLMemberAbilitiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    creator_payment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.PaymentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_encryption_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.DataEncryptionMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    job_log_status: typing.Optional[builtins.str] = None,
    members: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.MemberSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43b0d208a10b53d5d7bf8e19cff7b1a7be86094960aa43579972861d563de44d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a9705b5c9f28f1d364782d5cb996ee4fe0e93dc0fbee1871bc10feeb5a547d9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9f17060755de314c6aea7e9fe1c03f18e31972fafbe5d1edf10b18250f60ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb5edb6a58e1c0f33620eadb56126089a140277fe87954ea4d3a06146b3559ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__585aa64e1eeaa11003c987d7230a1772b0683c9f8866457214d0242ba9d00d4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa852049fd80eee6c2543d7576eb0c8f60a43d90ca97006450c31d8a1ed9df20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1052deb6a86709adcf30bca5621af3b50e52d20c54f6e014b8baeaa998273732(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ee81f8b64fd681cae1a860e0339dfa0ddeb287c4e709f0b34cc3c8bcf9bc6bd(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97c0d0f6cb32a0cbf54c04b4f619c67713dd848075c944908bc62665b42284a9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCollaboration.MLMemberAbilitiesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__991360bdd6af4d5b428da7f242ab1cc46f2a619a380ffdff6e2434a3e7541e84(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCollaboration.PaymentConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a86b18a30aac6a5afc1830c4adb282d4f0f3199f7c3d3ce99ffb24dad829a6eb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCollaboration.DataEncryptionMetadataProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4417cba39dba6b058b8e9e8165e109039205858f8f1e7237cc3fa2e9f60ee5c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e816963af09a7c3bdf0ca05211222f43d66929e9fa8216fe82e8fb6e27493bdc(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCollaboration.MemberSpecificationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06877122efbe5bc41c92999ba727597f48590c383378ee73a94c91fe43305e60(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1d5c25162d0eabd19a06fd0a1ec26adcd8d8a0d12434d6ee8fbec8e27c21965(
    *,
    allow_cleartext: typing.Union[builtins.bool, _IResolvable_da3f097b],
    allow_duplicates: typing.Union[builtins.bool, _IResolvable_da3f097b],
    allow_joins_on_columns_with_different_names: typing.Union[builtins.bool, _IResolvable_da3f097b],
    preserve_nulls: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c083b467c80242022df99766953c94b800010fa09b9890251c092ef48906a8d6(
    *,
    is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d12c181790032dcf002dcacb31cb4e50bd00d2ab068f38065b4ad7d1319d80c(
    *,
    custom_ml_member_abilities: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__271514c890ff476984844077519496f6cd7107081ee5259613350b060c9bb355(
    *,
    model_inference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.ModelInferencePaymentConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    model_training: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.ModelTrainingPaymentConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c9d415168b79c297b7313d0c42362a70fed420b1dda08e496b99813fbbd3248(
    *,
    account_id: builtins.str,
    display_name: builtins.str,
    member_abilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    ml_member_abilities: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.MLMemberAbilitiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    payment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.PaymentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91778bff8fa4786b2dc1aace0c2b468463ac1eb3971264546bddcbfe95dc8a99(
    *,
    is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35cebaf540e2e0f273400ebe690d288c30c23dab0b643fcadc0b6fa47a38e5c1(
    *,
    is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bb111eda28dfc76cbd93dac49286726320cc654bfb530550f97b9ec4cf32cbf(
    *,
    query_compute: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.QueryComputePaymentConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    job_compute: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.JobComputePaymentConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    machine_learning: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.MLPaymentConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__691566df57f98e85a0cab7f982a0bb63684a2747f18e19d599214bacc63437b2(
    *,
    is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2049291a9933df94c4258b33838a3aa8100d0214a4519c3d84e6d70ed724c55d(
    *,
    creator_display_name: builtins.str,
    description: builtins.str,
    name: builtins.str,
    query_log_status: builtins.str,
    analytics_engine: typing.Optional[builtins.str] = None,
    creator_member_abilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    creator_ml_member_abilities: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.MLMemberAbilitiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    creator_payment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.PaymentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_encryption_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.DataEncryptionMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    job_log_status: typing.Optional[builtins.str] = None,
    members: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCollaboration.MemberSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6da68c3fc7e3c0674ddb5e2082cfb964074dd6f86f1df6dfcede15001d6f1259(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    allowed_columns: typing.Sequence[builtins.str],
    analysis_method: builtins.str,
    name: builtins.str,
    table_reference: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.TableReferenceProperty, typing.Dict[builtins.str, typing.Any]]],
    analysis_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AnalysisRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    selected_analysis_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fecfad26837cc2fdccacfdfb035a18dcac563292f6d300d8052bc89207ae04fe(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5c9224380ccb774fe3599e8c47969dd65412118923ba36f2fc0d722c916638e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46e6aec85126d8c2d12db0e5442b4d56c199d90e95cd9b98b1c92b7652d7c7eb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dd16c3f5e30018a39bada3627e112c5d99eea9283a9ad2de82b9790911c3169(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8743fd9932eb6c0afe523245bfc3bc611bed75b8e179806716cdbd7e1e97f817(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81f7eaa704c6766bfee1be9d2d2b0c8cc4751fd3eb996d6d9902238bdc710232(
    value: typing.Union[_IResolvable_da3f097b, CfnConfiguredTable.TableReferenceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26267c9443103a44d253b803cbd021f980a5d2b9c34ee95ca6dfc809fab0f1e0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfiguredTable.AnalysisRuleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c8634d59e391cfec8341b7e4b408bb2c2335c7e17e4ff15bc5f5d8abc23fd91(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c04ca44ac5848879bc3057033050f0e47ffad283431a7189392ca761ec64d2d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3a9395564381a20388411d14ffd2bda7a4d604b2cf7bf643f5e5bd129bdd0f0(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa417839f91cf8cc845476ca63e8e1d38ea951bbc307aaa969fdea5be7e16893(
    *,
    column_names: typing.Sequence[builtins.str],
    function: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63f1cc4359753a41914fdd91e80c9746bf76bc8ab990f1c207bf527199e05de5(
    *,
    column_name: builtins.str,
    minimum: jsii.Number,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c88de0a4314f12e0bbceae5eb6edd232a937dc4a6b95c8eb383dabc0231d87e(
    *,
    aggregate_columns: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AggregateColumnProperty, typing.Dict[builtins.str, typing.Any]]]]],
    dimension_columns: typing.Sequence[builtins.str],
    join_columns: typing.Sequence[builtins.str],
    output_constraints: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AggregationConstraintProperty, typing.Dict[builtins.str, typing.Any]]]]],
    scalar_functions: typing.Sequence[builtins.str],
    additional_analyses: typing.Optional[builtins.str] = None,
    allowed_join_operators: typing.Optional[typing.Sequence[builtins.str]] = None,
    join_required: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb34762d0bf6ed014ff8964f15e74deaeb8d3d74c070c1dc20496ef94ed7c8ec(
    *,
    allowed_analyses: typing.Sequence[builtins.str],
    additional_analyses: typing.Optional[builtins.str] = None,
    allowed_analysis_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
    differential_privacy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.DifferentialPrivacyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    disallowed_output_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0accd14fb8407350b8ede83ec532b76a492d21ad538a377f14413f98dae0fba(
    *,
    join_columns: typing.Sequence[builtins.str],
    list_columns: typing.Sequence[builtins.str],
    additional_analyses: typing.Optional[builtins.str] = None,
    allowed_join_operators: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__124c3b77588197cdbfdd27c90ac026b586926dd1d223cf478cf9815b95327095(
    *,
    policy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58a53beb1a0a90ec538b0213243c8721465a73c73f8bf745778a09f20fde15e2(
    *,
    database_name: builtins.str,
    table_name: builtins.str,
    work_group: builtins.str,
    output_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f1e3e5a795ca7258552d46676801756cc639b2cf39b0a42555fb510dee59fc1(
    *,
    v1: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.ConfiguredTableAnalysisRulePolicyV1Property, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3e07fc4df9c2eafb409dd0b417b9236aa995940875e48daa983efee06bd45fc(
    *,
    aggregation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AnalysisRuleAggregationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AnalysisRuleCustomProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AnalysisRuleListProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db51d35ba24655ba0ff827d1b1f747a981c133aa166ad14ccd1ac62c4aa28235(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25cecdbb678db7c9fecdba89215b89eba238f35861c80f5cb848f3f80ef4e9e7(
    *,
    columns: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.DifferentialPrivacyColumnProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad49810a315ae1c04064504cefbb3e0bc6fec52a1add50545955db56f0db50f9(
    *,
    database_name: builtins.str,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0bac88ed34f9327592c380e538ab50720af8f52dd5162e61df0aec6adf2833a(
    *,
    account_identifier: builtins.str,
    database_name: builtins.str,
    schema_name: builtins.str,
    secret_arn: builtins.str,
    table_name: builtins.str,
    table_schema: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.SnowflakeTableSchemaProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__239c59d3fbfbc31d3d63df05389a6d08ab60a5a59b54a1d142b38a1317d9924a(
    *,
    v1: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.SnowflakeTableSchemaV1Property, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83fba8d181362fec1a7a64673d96ded09367f372899b9e1e5eb170f94c17c13f(
    *,
    column_name: builtins.str,
    column_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48547ee47249030cb21aff2b6c33202b13d80f1552ddf62b21595c3e0bb02374(
    *,
    athena: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AthenaTableReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    glue: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.GlueTableReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snowflake: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.SnowflakeTableReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e813cbcc5b9d34191c933a4be199648c57161cd507f73f0659159b5b61777153(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configured_table_identifier: builtins.str,
    membership_identifier: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    configured_table_association_analysis_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e6d4b82c3edf32301796f14dea9ee962d5b6287982b67f53a6fce4d9e53e702(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b13025a7765c8fcc0096c7e63fe6d35197debf3b5ec554487f0710eeca7c147b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9728a7769f77a5cdfb3417c1fc58a389ba8c6ef5730bb294ef56c67c4f965bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e0b566414c7844303646de783cb99821d6132816fd82629491db143d70bc328(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bb6d6d8ed4af7ba2289b9a65f55feb240da577eb6c05a2a379ac3aa825876b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ed3a131e342f3d6715894b34f9784b7f6a4bd2257ccd5640eee2873aff3a7bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0d0ff28b0fb4873494693033feac4f811d803307eb2eaf6b27473cd93db2ef0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c12987240d2469d3de49134d97df56891e19e780c69b74115f2054f5a34a614(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab43f7456a874349f59a592b725dc266f2d215b76da6fc373e63e5999b3ce75e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__238152ae2ae96e49fa6c904bd319b8d4be8fd0916ce96bdf774850ad8ca69140(
    *,
    allowed_additional_analyses: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_result_receivers: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a7ef0cf97c0f9da19de0009ec3e6fb3ffe6b6f987fc5b6203ab290eec858c53(
    *,
    allowed_additional_analyses: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_result_receivers: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6bcf6381ae16674a7b2d769e9d709e1ae56dbd9f4c003d1b9c9c8f5d385071f(
    *,
    allowed_additional_analyses: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_result_receivers: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__281bd2c034dea5decd044a63b24891762f44992aab75ab6780e712d520ae64f2(
    *,
    v1: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyV1Property, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc559a0692caa4463a4398f86a4304afc170424b5a1434972be11d3638e5bd07(
    *,
    aggregation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleAggregationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleCustomProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleListProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__720bc84933dd2d1faf77915df0b8b69bcbb3e46b9d6c11a06d41f925485184d8(
    *,
    policy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRulePolicyProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__115dd625c37fad8a84b51d36bcabf9183ae442a7285c6ddd1efddd869faae1dc(
    *,
    configured_table_identifier: builtins.str,
    membership_identifier: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    configured_table_association_analysis_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTableAssociation.ConfiguredTableAssociationAnalysisRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__881d5bc014e7a9ce8400d21437644071526768629f4ac0f4414f60ba95930f3f(
    *,
    allowed_columns: typing.Sequence[builtins.str],
    analysis_method: builtins.str,
    name: builtins.str,
    table_reference: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.TableReferenceProperty, typing.Dict[builtins.str, typing.Any]]],
    analysis_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfiguredTable.AnalysisRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    selected_analysis_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a55eec871eed8ea740c3790e228bff6225a56f9406dd161a61af8218377c626(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    input_reference_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdMappingTable.IdMappingTableInputReferenceConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    membership_identifier: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fb4bed5d50335d140dfb97a8e1ece95e5918e41e8f333e7a21770aff551143c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acdffe9d489cfb1fd064c08c8b300b2880a9e20996d6a0e15e197844adf31b6d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80a1443fefffd729ef997de9fb9306db15cfda0ecccaa0f348c3f55a13fc2f6b(
    value: typing.Union[_IResolvable_da3f097b, CfnIdMappingTable.IdMappingTableInputReferenceConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a608278f5ac9f4b2374d49aaae1f9c846f8320a4fb6cf2c093385273f313224c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d89d3a813c07afbd9194e6ef736daf000c0d923680da83dd94897908ef16598(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fe55d535ef13a6fa856ac8e5ba601c43e7ece61a7d5ddf03730c1f1ea475767(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1390f292c37578c0a018f5c4283630c58da4fdd1848e6bfb85b87946002dc103(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d6b9b9f29a25fa84794d9a566af8e18597086eba6792ac31fe185d0f74a9ff5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e37f64c35b172103f8bfa9f0d30e75b382e86d01d38fd2e8eb28803124f2fbc(
    *,
    input_reference_arn: builtins.str,
    manage_resource_policies: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e2b496feb9017399bea5c97a77d2124b505586ff18a03d366e20cfcd893709e(
    *,
    id_mapping_table_input_source: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdMappingTable.IdMappingTableInputSourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__690a1415d215001f1d1f03e8ed0bfcd7231c35a0b31d54bd8fab7c8b51e81090(
    *,
    id_namespace_association_id: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__722f65baa0dd5025cc0e42e7e9c4015b3d215b4aa9bb587f8bb4acf1f72b6c17(
    *,
    input_reference_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdMappingTable.IdMappingTableInputReferenceConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    membership_identifier: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f52a2f7a45be837d26654b8bb3a3d0fab7fd6c5d25ec9b81d04a38689a6194fc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    input_reference_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferenceConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    membership_identifier: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id_mapping_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdNamespaceAssociation.IdMappingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a273456bd42e75067e1919d356ca738d303809279e3242770cf1909b4c53be9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c20ff570488d7e6c55252cba585a051fa87292c8341512e81f14562e1f1655f5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__314c1541c8ce4234c2ada25e682a151d92fd93edbed1b4fd9105dcda931dc8dc(
    value: typing.Union[_IResolvable_da3f097b, CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferenceConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6942bfe2fcc0b0271a549fbe0007f1450b5a3d401188d403b97a935468367b94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ae82ba9441ae418e38e9d46574ca3cf34f6664a35510b70e1232333ae528fcf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8650ed8694c75389ed6fa670c630c6fd8b2e1ada930bf70bddcc54e58397c79f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18b505cc42cf359a69612005213707ca66c0c1daa7090899390265f4b2a5aa3b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIdNamespaceAssociation.IdMappingConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb75b574b07bea6c872486b6d13e8f81b7b3304807da45e45a041c11f1b4a84d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7ab29f7c6ba8d3c436a4a92d514f1221e64c73743bc063c057464db677e1895(
    *,
    allow_use_as_dimension_column: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a0c310848e9ee828aa0877d71d6e2c6b1ece9c6d43464be34c1eea8d23e0b85(
    *,
    input_reference_arn: builtins.str,
    manage_resource_policies: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d6f96ce848c511129f57c9b34eaf0bed9c2e0367e3f29de1038e211e4797e05(
    *,
    id_mapping_workflows_supported: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
    id_namespace_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82e4c0093759d750139b85493d1dd6c9f0b65aa9075fa72356dbfcee3b0a8784(
    *,
    input_reference_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdNamespaceAssociation.IdNamespaceAssociationInputReferenceConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    membership_identifier: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    id_mapping_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdNamespaceAssociation.IdMappingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74d43efdc8d8359f9de6878ad0f2d25ff79e584d96e5ca863178e6f14312cec1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    collaboration_identifier: builtins.str,
    query_log_status: builtins.str,
    default_job_result_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipProtectedJobResultConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_result_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipProtectedQueryResultConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    job_log_status: typing.Optional[builtins.str] = None,
    payment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipPaymentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f53a7e47a69cc6ee8550050a85dd5bd1dab4134d650a0e20c9312e56ea80fc60(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78e173bbe42542972b47c21576e57269fe216eab7a86b44fadf695b6653d493d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba2cc6691bad0d4fdbfa43d453737e19bbcc1b63648ed884849a27170f877099(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bee80a156c452c78946d81f28dfee88d47d5702e2d1eeb7a5c7aeb167b25400e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fae73e4481dcc5cfeba1d7ce37a48095412d812d6a76939d24017d3e50e600fb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMembership.MembershipProtectedJobResultConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad055649202ffbf3de067877d88fa96b564e1efb0b59d9afaceb04f351ce0c65(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMembership.MembershipProtectedQueryResultConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38062eee31563e49c149bef3fc9159c7dcbe0d1c37a73eb1b26fde91bcde4dd9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f2d4b43043fdc1c0f794c725e0fa34d3d42d2b231edc34464fcc237ea7aa6d6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMembership.MembershipPaymentConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efad84033de32d67e94b9ac23a8d3176e7fc904203e000dac066b28793fec68b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e65ed6ced5134c54f82464bc8236090d903d3f26a591c4dc337a7344c43ce7e8(
    *,
    is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13dd2d08b2612b2890adb3362ea4e5bebe48abd3cfb27c026a48fcd95bd347dd(
    *,
    model_inference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipModelInferencePaymentConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    model_training: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipModelTrainingPaymentConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b782e5294b8bba99405cc5a7ca5c775fb2010013a32d43d0fdf4a2878964aca(
    *,
    is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e5c7b5216c60ffcb694e1961e057ff77a03ba6ae0c1cd13b03497dc0f0df235(
    *,
    is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff9b623af3a2e12d6db7063d2191f9dad178b00c5e761d332496d6065f45dfe6(
    *,
    query_compute: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipQueryComputePaymentConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    job_compute: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipJobComputePaymentConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    machine_learning: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipMLPaymentConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04b0307caf7eb009735af65a413fe8c877c870d384cffc49ef1a36d9699ba548(
    *,
    s3: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.ProtectedJobS3OutputConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b28ab623b930079e7e4df6a230e428f58f7ad919a987f38ecf686a4238ab5b47(
    *,
    output_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipProtectedJobOutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95a2754aa7d946646d057afbcf1d05c839a09b522b0215f8c6ff427a564f624b(
    *,
    s3: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.ProtectedQueryS3OutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ac8c4043e48c89672053a73e33884a2912eeea08d43d7abf8e69c928dcadc65(
    *,
    output_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipProtectedQueryOutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a0b18d278e5a5581d13248fe664b26d08f194e496fc961110d71d330026e192(
    *,
    is_responsible: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3e8066041ab5d5ba65ac44f96738cb04449874735750f11b6331de6bf9fda0c(
    *,
    bucket: builtins.str,
    key_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9188eb901d25d30e10ffe45a67a0477e30fc05a712c633d687872210f716c3a(
    *,
    bucket: builtins.str,
    result_format: builtins.str,
    key_prefix: typing.Optional[builtins.str] = None,
    single_file_output: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a7030966bdb99200cf7aff97662a2ef1e02754d2c014bc030475065ea06e0da(
    *,
    collaboration_identifier: builtins.str,
    query_log_status: builtins.str,
    default_job_result_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipProtectedJobResultConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_result_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipProtectedQueryResultConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    job_log_status: typing.Optional[builtins.str] = None,
    payment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMembership.MembershipPaymentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4ef80e47afb9dceb9f249b561d13bd079011c08e3eadfd7c85afef7b15b6395(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    auto_refresh: builtins.str,
    membership_identifier: builtins.str,
    parameters: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrivacyBudgetTemplate.ParametersProperty, typing.Dict[builtins.str, typing.Any]]],
    privacy_budget_type: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4105213a7d3d459c08d1525f399592909787ead616f1a795ab1b4391f1c50f74(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bf81ecc233447257243d10c0d69e227d4821702f88ae519ba06a04eef3a6730(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aac4d267c9bad45a4e435ea568f943c0e3bf8200eb41fb580c04ae8a221cfdb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__451d7c98300c47ca24e57e08313a6f1c3e359f595cc6d9bd21ca7564f781be19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f392867d1a4c1fee75cc8b48d97f801894a657d907a13d4d2a21ce8f8e5aeb9(
    value: typing.Union[_IResolvable_da3f097b, CfnPrivacyBudgetTemplate.ParametersProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af09670bc39ec5464305b000607d6c8a229830c5ad3234b2a82e4e6004d271df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6baec6343b79fd0bf9b81122904ed3d87c0dfb35be66cc64d471a7a08ddc00f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1938eceb4a5ecd53da864bdcbc38554516e8fa365c0dec957d0fe1a8bcdbe3d3(
    *,
    epsilon: jsii.Number,
    users_noise_per_query: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7be5c898600ca696463b88a231c1311a56890ce38a77ba2a33d7a9284885c4e0(
    *,
    auto_refresh: builtins.str,
    membership_identifier: builtins.str,
    parameters: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrivacyBudgetTemplate.ParametersProperty, typing.Dict[builtins.str, typing.Any]]],
    privacy_budget_type: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
