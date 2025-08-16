r'''
# AWS::CustomerProfiles Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_customerprofiles as customerprofiles
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for CustomerProfiles construct libraries](https://constructs.dev/search?q=customerprofiles)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::CustomerProfiles resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CustomerProfiles.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::CustomerProfiles](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CustomerProfiles.html).

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


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnCalculatedAttributeDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinition",
):
    '''A calculated attribute definition for Customer Profiles.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html
    :cloudformationResource: AWS::CustomerProfiles::CalculatedAttributeDefinition
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_customerprofiles as customerprofiles
        
        cfn_calculated_attribute_definition = customerprofiles.CfnCalculatedAttributeDefinition(self, "MyCfnCalculatedAttributeDefinition",
            attribute_details=customerprofiles.CfnCalculatedAttributeDefinition.AttributeDetailsProperty(
                attributes=[customerprofiles.CfnCalculatedAttributeDefinition.AttributeItemProperty(
                    name="name"
                )],
                expression="expression"
            ),
            calculated_attribute_name="calculatedAttributeName",
            domain_name="domainName",
            statistic="statistic",
        
            # the properties below are optional
            conditions=customerprofiles.CfnCalculatedAttributeDefinition.ConditionsProperty(
                object_count=123,
                range=customerprofiles.CfnCalculatedAttributeDefinition.RangeProperty(
                    unit="unit",
        
                    # the properties below are optional
                    timestamp_format="timestampFormat",
                    timestamp_source="timestampSource",
                    value=123,
                    value_range=customerprofiles.CfnCalculatedAttributeDefinition.ValueRangeProperty(
                        end=123,
                        start=123
                    )
                ),
                threshold=customerprofiles.CfnCalculatedAttributeDefinition.ThresholdProperty(
                    operator="operator",
                    value="value"
                )
            ),
            description="description",
            display_name="displayName",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            use_historical_data=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        attribute_details: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCalculatedAttributeDefinition.AttributeDetailsProperty", typing.Dict[builtins.str, typing.Any]]],
        calculated_attribute_name: builtins.str,
        domain_name: builtins.str,
        statistic: builtins.str,
        conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCalculatedAttributeDefinition.ConditionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        use_historical_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param attribute_details: Mathematical expression and a list of attribute items specified in that expression.
        :param calculated_attribute_name: The name of an attribute defined in a profile object type.
        :param domain_name: The unique name of the domain.
        :param statistic: The aggregation operation to perform for the calculated attribute.
        :param conditions: The conditions including range, object count, and threshold for the calculated attribute.
        :param description: The description of the calculated attribute.
        :param display_name: The display name of the calculated attribute.
        :param tags: An array of key-value pairs to apply to this resource.
        :param use_historical_data: Whether historical data ingested before the Calculated Attribute was created should be included in calculations.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a09ab96caa4db6cfa4ebb0207c025a7f976cac18f814d69b882506cf2971669)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCalculatedAttributeDefinitionProps(
            attribute_details=attribute_details,
            calculated_attribute_name=calculated_attribute_name,
            domain_name=domain_name,
            statistic=statistic,
            conditions=conditions,
            description=description,
            display_name=display_name,
            tags=tags,
            use_historical_data=use_historical_data,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8c355c3b327941e1e80c87b111beedb797243265da934cbe14cb40a04def39b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ff2e7320eba6c67e11b5108c4174e965091aab4bf1ed72835487ea46d7bd228)
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
        '''The timestamp of when the calculated attribute definition was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The timestamp of when the calculated attribute definition was most recently edited.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrReadiness")
    def attr_readiness(self) -> _IResolvable_da3f097b:
        '''The readiness status of the calculated attribute.

        :cloudformationAttribute: Readiness
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrReadiness"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Status of the Calculated Attribute creation (whether all historical data has been indexed.).

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
    @jsii.member(jsii_name="attributeDetails")
    def attribute_details(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.AttributeDetailsProperty"]:
        '''Mathematical expression and a list of attribute items specified in that expression.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.AttributeDetailsProperty"], jsii.get(self, "attributeDetails"))

    @attribute_details.setter
    def attribute_details(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.AttributeDetailsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc094b8898d98fbc0a232ed05081d6ffd11e6092cf72d062c7ab6a1a118b2655)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeDetails", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="calculatedAttributeName")
    def calculated_attribute_name(self) -> builtins.str:
        '''The name of an attribute defined in a profile object type.'''
        return typing.cast(builtins.str, jsii.get(self, "calculatedAttributeName"))

    @calculated_attribute_name.setter
    def calculated_attribute_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1874ab73c6c7fb500a83379a356ae12dde9d52f47b68d1b2dfe7fb7772ae682)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "calculatedAttributeName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__806572f2b3c6f3d60619dab1026866577ec43486c44775df8e7f00f9ec946cc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="statistic")
    def statistic(self) -> builtins.str:
        '''The aggregation operation to perform for the calculated attribute.'''
        return typing.cast(builtins.str, jsii.get(self, "statistic"))

    @statistic.setter
    def statistic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24137af23c238e226876684e3ad841c56564bd3e9f7c488415d38fbd9560440e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statistic", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="conditions")
    def conditions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.ConditionsProperty"]]:
        '''The conditions including range, object count, and threshold for the calculated attribute.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.ConditionsProperty"]], jsii.get(self, "conditions"))

    @conditions.setter
    def conditions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.ConditionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d9f165d8e8dde422309619ae01ce8e4f77e67c1d8707134c0f7c2a25fd53ebc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conditions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the calculated attribute.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e94c935ac0604ce2b84a26b87f764d32bfa425eb59416e0935dca9d2a010ce58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the calculated attribute.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64a1f1d0da7758807d6fc0184c03cfdc7c695677f2dd2cfeb300cb009b6e9d69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66b41ae1f61b2d451c01e8a6b3eabc1ef1fe6f0e51c71a264d46a9df8ec0ad14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="useHistoricalData")
    def use_historical_data(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether historical data ingested before the Calculated Attribute was created should be included in calculations.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "useHistoricalData"))

    @use_historical_data.setter
    def use_historical_data(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ab1072a749050ba2fecfbba8cc52cbc745e52869b7164a97ab6eb2dcdf582c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useHistoricalData", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinition.AttributeDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"attributes": "attributes", "expression": "expression"},
    )
    class AttributeDetailsProperty:
        def __init__(
            self,
            *,
            attributes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCalculatedAttributeDefinition.AttributeItemProperty", typing.Dict[builtins.str, typing.Any]]]]],
            expression: builtins.str,
        ) -> None:
            '''Mathematical expression and a list of attribute items specified in that expression.

            :param attributes: Mathematical expression and a list of attribute items specified in that expression.
            :param expression: Mathematical expression that is performed on attribute items provided in the attribute list. Each element in the expression should follow the structure of "{ObjectTypeName.AttributeName}".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                attribute_details_property = customerprofiles.CfnCalculatedAttributeDefinition.AttributeDetailsProperty(
                    attributes=[customerprofiles.CfnCalculatedAttributeDefinition.AttributeItemProperty(
                        name="name"
                    )],
                    expression="expression"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6241b1471123a742a03d1b24e69021bc3c2c3b4a805094f7a6176be6f76da07a)
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attributes": attributes,
                "expression": expression,
            }

        @builtins.property
        def attributes(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.AttributeItemProperty"]]]:
            '''Mathematical expression and a list of attribute items specified in that expression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributedetails.html#cfn-customerprofiles-calculatedattributedefinition-attributedetails-attributes
            '''
            result = self._values.get("attributes")
            assert result is not None, "Required property 'attributes' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.AttributeItemProperty"]]], result)

        @builtins.property
        def expression(self) -> builtins.str:
            '''Mathematical expression that is performed on attribute items provided in the attribute list.

            Each element in the expression should follow the structure of "{ObjectTypeName.AttributeName}".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributedetails.html#cfn-customerprofiles-calculatedattributedefinition-attributedetails-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinition.AttributeItemProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class AttributeItemProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''The details of a single attribute item specified in the mathematical expression.

            :param name: The unique name of the calculated attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributeitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                attribute_item_property = customerprofiles.CfnCalculatedAttributeDefinition.AttributeItemProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2af823a61c3449f36ffaa48661361e9de02280cffeeefa5a3d5990a5035cd43b)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The unique name of the calculated attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-attributeitem.html#cfn-customerprofiles-calculatedattributedefinition-attributeitem-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinition.ConditionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "object_count": "objectCount",
            "range": "range",
            "threshold": "threshold",
        },
    )
    class ConditionsProperty:
        def __init__(
            self,
            *,
            object_count: typing.Optional[jsii.Number] = None,
            range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCalculatedAttributeDefinition.RangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            threshold: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCalculatedAttributeDefinition.ThresholdProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The conditions including range, object count, and threshold for the calculated attribute.

            :param object_count: The number of profile objects used for the calculated attribute.
            :param range: The relative time period over which data is included in the aggregation.
            :param threshold: The threshold for the calculated attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-conditions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                conditions_property = customerprofiles.CfnCalculatedAttributeDefinition.ConditionsProperty(
                    object_count=123,
                    range=customerprofiles.CfnCalculatedAttributeDefinition.RangeProperty(
                        unit="unit",
                
                        # the properties below are optional
                        timestamp_format="timestampFormat",
                        timestamp_source="timestampSource",
                        value=123,
                        value_range=customerprofiles.CfnCalculatedAttributeDefinition.ValueRangeProperty(
                            end=123,
                            start=123
                        )
                    ),
                    threshold=customerprofiles.CfnCalculatedAttributeDefinition.ThresholdProperty(
                        operator="operator",
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d5d5606a68f168622e019935c1cfd2eb8821e95f36c66313b2a6f7a38cc4e472)
                check_type(argname="argument object_count", value=object_count, expected_type=type_hints["object_count"])
                check_type(argname="argument range", value=range, expected_type=type_hints["range"])
                check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if object_count is not None:
                self._values["object_count"] = object_count
            if range is not None:
                self._values["range"] = range
            if threshold is not None:
                self._values["threshold"] = threshold

        @builtins.property
        def object_count(self) -> typing.Optional[jsii.Number]:
            '''The number of profile objects used for the calculated attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-conditions.html#cfn-customerprofiles-calculatedattributedefinition-conditions-objectcount
            '''
            result = self._values.get("object_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def range(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.RangeProperty"]]:
            '''The relative time period over which data is included in the aggregation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-conditions.html#cfn-customerprofiles-calculatedattributedefinition-conditions-range
            '''
            result = self._values.get("range")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.RangeProperty"]], result)

        @builtins.property
        def threshold(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.ThresholdProperty"]]:
            '''The threshold for the calculated attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-conditions.html#cfn-customerprofiles-calculatedattributedefinition-conditions-threshold
            '''
            result = self._values.get("threshold")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.ThresholdProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinition.RangeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "unit": "unit",
            "timestamp_format": "timestampFormat",
            "timestamp_source": "timestampSource",
            "value": "value",
            "value_range": "valueRange",
        },
    )
    class RangeProperty:
        def __init__(
            self,
            *,
            unit: builtins.str,
            timestamp_format: typing.Optional[builtins.str] = None,
            timestamp_source: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
            value_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCalculatedAttributeDefinition.ValueRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The relative time period over which data is included in the aggregation.

            :param unit: The unit of time.
            :param timestamp_format: The format the timestamp field in your JSON object is specified. This value should be one of EPOCHMILLI (for Unix epoch timestamps with second/millisecond level precision) or ISO_8601 (following ISO_8601 format with second/millisecond level precision, with an optional offset of Z or in the format HH:MM or HHMM.). E.g. if your object type is MyType and source JSON is {"generatedAt": {"timestamp": "2001-07-04T12:08:56.235-0700"}}, then TimestampFormat should be "ISO_8601"
            :param timestamp_source: An expression specifying the field in your JSON object from which the date should be parsed. The expression should follow the structure of "{ObjectTypeName.}". E.g. if your object type is MyType and source JSON is {"generatedAt": {"timestamp": "1737587945945"}}, then TimestampSource should be "{MyType.generatedAt.timestamp}"
            :param value: The amount of time of the specified unit.
            :param value_range: A structure letting customers specify a relative time window over which over which data is included in the Calculated Attribute. Use positive numbers to indicate that the endpoint is in the past, and negative numbers to indicate it is in the future. ValueRange overrides Value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-range.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                range_property = customerprofiles.CfnCalculatedAttributeDefinition.RangeProperty(
                    unit="unit",
                
                    # the properties below are optional
                    timestamp_format="timestampFormat",
                    timestamp_source="timestampSource",
                    value=123,
                    value_range=customerprofiles.CfnCalculatedAttributeDefinition.ValueRangeProperty(
                        end=123,
                        start=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4567eb83ac5620aa6be36cbd0e38cdba257d259743e1017616dbc2252fc66f9d)
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
                check_type(argname="argument timestamp_format", value=timestamp_format, expected_type=type_hints["timestamp_format"])
                check_type(argname="argument timestamp_source", value=timestamp_source, expected_type=type_hints["timestamp_source"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument value_range", value=value_range, expected_type=type_hints["value_range"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "unit": unit,
            }
            if timestamp_format is not None:
                self._values["timestamp_format"] = timestamp_format
            if timestamp_source is not None:
                self._values["timestamp_source"] = timestamp_source
            if value is not None:
                self._values["value"] = value
            if value_range is not None:
                self._values["value_range"] = value_range

        @builtins.property
        def unit(self) -> builtins.str:
            '''The unit of time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-range.html#cfn-customerprofiles-calculatedattributedefinition-range-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def timestamp_format(self) -> typing.Optional[builtins.str]:
            '''The format the timestamp field in your JSON object is specified.

            This value should be one of EPOCHMILLI (for Unix epoch timestamps with second/millisecond level precision) or ISO_8601 (following ISO_8601 format with second/millisecond level precision, with an optional offset of Z or in the format HH:MM or HHMM.). E.g. if your object type is MyType and source JSON is {"generatedAt": {"timestamp": "2001-07-04T12:08:56.235-0700"}}, then TimestampFormat should be "ISO_8601"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-range.html#cfn-customerprofiles-calculatedattributedefinition-range-timestampformat
            '''
            result = self._values.get("timestamp_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timestamp_source(self) -> typing.Optional[builtins.str]:
            '''An expression specifying the field in your JSON object from which the date should be parsed.

            The expression should follow the structure of "{ObjectTypeName.}". E.g. if your object type is MyType and source JSON is {"generatedAt": {"timestamp": "1737587945945"}}, then TimestampSource should be "{MyType.generatedAt.timestamp}"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-range.html#cfn-customerprofiles-calculatedattributedefinition-range-timestampsource
            '''
            result = self._values.get("timestamp_source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            '''The amount of time of the specified unit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-range.html#cfn-customerprofiles-calculatedattributedefinition-range-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def value_range(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.ValueRangeProperty"]]:
            '''A structure letting customers specify a relative time window over which over which data is included in the Calculated Attribute.

            Use positive numbers to indicate that the endpoint is in the past, and negative numbers to indicate it is in the future. ValueRange overrides Value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-range.html#cfn-customerprofiles-calculatedattributedefinition-range-valuerange
            '''
            result = self._values.get("value_range")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCalculatedAttributeDefinition.ValueRangeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinition.ReadinessProperty",
        jsii_struct_bases=[],
        name_mapping={
            "message": "message",
            "progress_percentage": "progressPercentage",
        },
    )
    class ReadinessProperty:
        def __init__(
            self,
            *,
            message: typing.Optional[builtins.str] = None,
            progress_percentage: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Information indicating if the Calculated Attribute is ready for use by confirming all historical data has been processed and reflected.

            :param message: Any customer messaging.
            :param progress_percentage: Approximately how far the Calculated Attribute creation is from completion.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-readiness.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                readiness_property = customerprofiles.CfnCalculatedAttributeDefinition.ReadinessProperty(
                    message="message",
                    progress_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0bc0a3c3468a435a5677e162145a9ef5e062a4e72fd921895d645bd1056af4e3)
                check_type(argname="argument message", value=message, expected_type=type_hints["message"])
                check_type(argname="argument progress_percentage", value=progress_percentage, expected_type=type_hints["progress_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if message is not None:
                self._values["message"] = message
            if progress_percentage is not None:
                self._values["progress_percentage"] = progress_percentage

        @builtins.property
        def message(self) -> typing.Optional[builtins.str]:
            '''Any customer messaging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-readiness.html#cfn-customerprofiles-calculatedattributedefinition-readiness-message
            '''
            result = self._values.get("message")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def progress_percentage(self) -> typing.Optional[jsii.Number]:
            '''Approximately how far the Calculated Attribute creation is from completion.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-readiness.html#cfn-customerprofiles-calculatedattributedefinition-readiness-progresspercentage
            '''
            result = self._values.get("progress_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReadinessProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinition.ThresholdProperty",
        jsii_struct_bases=[],
        name_mapping={"operator": "operator", "value": "value"},
    )
    class ThresholdProperty:
        def __init__(self, *, operator: builtins.str, value: builtins.str) -> None:
            '''The threshold for the calculated attribute.

            :param operator: The operator of the threshold.
            :param value: The value of the threshold.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-threshold.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                threshold_property = customerprofiles.CfnCalculatedAttributeDefinition.ThresholdProperty(
                    operator="operator",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dcc19afa2a314e3392b1f8004f5ce5593298e226e89f8bb3424dc57cefbb2646)
                check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "operator": operator,
                "value": value,
            }

        @builtins.property
        def operator(self) -> builtins.str:
            '''The operator of the threshold.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-threshold.html#cfn-customerprofiles-calculatedattributedefinition-threshold-operator
            '''
            result = self._values.get("operator")
            assert result is not None, "Required property 'operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value of the threshold.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-threshold.html#cfn-customerprofiles-calculatedattributedefinition-threshold-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ThresholdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinition.ValueRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"end": "end", "start": "start"},
    )
    class ValueRangeProperty:
        def __init__(self, *, end: jsii.Number, start: jsii.Number) -> None:
            '''A structure letting customers specify a relative time window over which over which data is included in the Calculated Attribute.

            Use positive numbers to indicate that the endpoint is in the past, and negative numbers to indicate it is in the future. ValueRange overrides Value.

            :param end: The ending point for this overridden range. Positive numbers indicate how many days in the past data should be included, and negative numbers indicate how many days in the future.
            :param start: The starting point for this overridden range. Positive numbers indicate how many days in the past data should be included, and negative numbers indicate how many days in the future.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-valuerange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                value_range_property = customerprofiles.CfnCalculatedAttributeDefinition.ValueRangeProperty(
                    end=123,
                    start=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d18b8118549ce586fc14b0cc15f51e9a520330684bb4d883bbf10b82b000c5a)
                check_type(argname="argument end", value=end, expected_type=type_hints["end"])
                check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "end": end,
                "start": start,
            }

        @builtins.property
        def end(self) -> jsii.Number:
            '''The ending point for this overridden range.

            Positive numbers indicate how many days in the past data should be included, and negative numbers indicate how many days in the future.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-valuerange.html#cfn-customerprofiles-calculatedattributedefinition-valuerange-end
            '''
            result = self._values.get("end")
            assert result is not None, "Required property 'end' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def start(self) -> jsii.Number:
            '''The starting point for this overridden range.

            Positive numbers indicate how many days in the past data should be included, and negative numbers indicate how many days in the future.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-calculatedattributedefinition-valuerange.html#cfn-customerprofiles-calculatedattributedefinition-valuerange-start
            '''
            result = self._values.get("start")
            assert result is not None, "Required property 'start' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValueRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnCalculatedAttributeDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_details": "attributeDetails",
        "calculated_attribute_name": "calculatedAttributeName",
        "domain_name": "domainName",
        "statistic": "statistic",
        "conditions": "conditions",
        "description": "description",
        "display_name": "displayName",
        "tags": "tags",
        "use_historical_data": "useHistoricalData",
    },
)
class CfnCalculatedAttributeDefinitionProps:
    def __init__(
        self,
        *,
        attribute_details: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.AttributeDetailsProperty, typing.Dict[builtins.str, typing.Any]]],
        calculated_attribute_name: builtins.str,
        domain_name: builtins.str,
        statistic: builtins.str,
        conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.ConditionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        use_historical_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCalculatedAttributeDefinition``.

        :param attribute_details: Mathematical expression and a list of attribute items specified in that expression.
        :param calculated_attribute_name: The name of an attribute defined in a profile object type.
        :param domain_name: The unique name of the domain.
        :param statistic: The aggregation operation to perform for the calculated attribute.
        :param conditions: The conditions including range, object count, and threshold for the calculated attribute.
        :param description: The description of the calculated attribute.
        :param display_name: The display name of the calculated attribute.
        :param tags: An array of key-value pairs to apply to this resource.
        :param use_historical_data: Whether historical data ingested before the Calculated Attribute was created should be included in calculations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_customerprofiles as customerprofiles
            
            cfn_calculated_attribute_definition_props = customerprofiles.CfnCalculatedAttributeDefinitionProps(
                attribute_details=customerprofiles.CfnCalculatedAttributeDefinition.AttributeDetailsProperty(
                    attributes=[customerprofiles.CfnCalculatedAttributeDefinition.AttributeItemProperty(
                        name="name"
                    )],
                    expression="expression"
                ),
                calculated_attribute_name="calculatedAttributeName",
                domain_name="domainName",
                statistic="statistic",
            
                # the properties below are optional
                conditions=customerprofiles.CfnCalculatedAttributeDefinition.ConditionsProperty(
                    object_count=123,
                    range=customerprofiles.CfnCalculatedAttributeDefinition.RangeProperty(
                        unit="unit",
            
                        # the properties below are optional
                        timestamp_format="timestampFormat",
                        timestamp_source="timestampSource",
                        value=123,
                        value_range=customerprofiles.CfnCalculatedAttributeDefinition.ValueRangeProperty(
                            end=123,
                            start=123
                        )
                    ),
                    threshold=customerprofiles.CfnCalculatedAttributeDefinition.ThresholdProperty(
                        operator="operator",
                        value="value"
                    )
                ),
                description="description",
                display_name="displayName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                use_historical_data=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b490cf412d8b10ddc1ddbf98b6d852a5446deca7e9befe3439df8de5169c37dd)
            check_type(argname="argument attribute_details", value=attribute_details, expected_type=type_hints["attribute_details"])
            check_type(argname="argument calculated_attribute_name", value=calculated_attribute_name, expected_type=type_hints["calculated_attribute_name"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument use_historical_data", value=use_historical_data, expected_type=type_hints["use_historical_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attribute_details": attribute_details,
            "calculated_attribute_name": calculated_attribute_name,
            "domain_name": domain_name,
            "statistic": statistic,
        }
        if conditions is not None:
            self._values["conditions"] = conditions
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if tags is not None:
            self._values["tags"] = tags
        if use_historical_data is not None:
            self._values["use_historical_data"] = use_historical_data

    @builtins.property
    def attribute_details(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCalculatedAttributeDefinition.AttributeDetailsProperty]:
        '''Mathematical expression and a list of attribute items specified in that expression.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-attributedetails
        '''
        result = self._values.get("attribute_details")
        assert result is not None, "Required property 'attribute_details' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCalculatedAttributeDefinition.AttributeDetailsProperty], result)

    @builtins.property
    def calculated_attribute_name(self) -> builtins.str:
        '''The name of an attribute defined in a profile object type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-calculatedattributename
        '''
        result = self._values.get("calculated_attribute_name")
        assert result is not None, "Required property 'calculated_attribute_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statistic(self) -> builtins.str:
        '''The aggregation operation to perform for the calculated attribute.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-statistic
        '''
        result = self._values.get("statistic")
        assert result is not None, "Required property 'statistic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conditions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCalculatedAttributeDefinition.ConditionsProperty]]:
        '''The conditions including range, object count, and threshold for the calculated attribute.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-conditions
        '''
        result = self._values.get("conditions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCalculatedAttributeDefinition.ConditionsProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the calculated attribute.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the calculated attribute.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def use_historical_data(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether historical data ingested before the Calculated Attribute was created should be included in calculations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-calculatedattributedefinition.html#cfn-customerprofiles-calculatedattributedefinition-usehistoricaldata
        '''
        result = self._values.get("use_historical_data")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCalculatedAttributeDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDomain(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnDomain",
):
    '''Specifies an Amazon Connect Customer Profiles Domain.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html
    :cloudformationResource: AWS::CustomerProfiles::Domain
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_customerprofiles as customerprofiles
        
        cfn_domain = customerprofiles.CfnDomain(self, "MyCfnDomain",
            default_expiration_days=123,
            domain_name="domainName",
        
            # the properties below are optional
            dead_letter_queue_url="deadLetterQueueUrl",
            default_encryption_key="defaultEncryptionKey",
            matching=customerprofiles.CfnDomain.MatchingProperty(
                enabled=False,
        
                # the properties below are optional
                auto_merging=customerprofiles.CfnDomain.AutoMergingProperty(
                    enabled=False,
        
                    # the properties below are optional
                    conflict_resolution=customerprofiles.CfnDomain.ConflictResolutionProperty(
                        conflict_resolving_model="conflictResolvingModel",
        
                        # the properties below are optional
                        source_name="sourceName"
                    ),
                    consolidation=customerprofiles.CfnDomain.ConsolidationProperty(
                        matching_attributes_list=[["matchingAttributesList"]]
                    ),
                    min_allowed_confidence_score_for_merging=123
                ),
                exporting_config=customerprofiles.CfnDomain.ExportingConfigProperty(
                    s3_exporting=customerprofiles.CfnDomain.S3ExportingConfigProperty(
                        s3_bucket_name="s3BucketName",
        
                        # the properties below are optional
                        s3_key_name="s3KeyName"
                    )
                ),
                job_schedule=customerprofiles.CfnDomain.JobScheduleProperty(
                    day_of_the_week="dayOfTheWeek",
                    time="time"
                )
            ),
            rule_based_matching=customerprofiles.CfnDomain.RuleBasedMatchingProperty(
                enabled=False,
        
                # the properties below are optional
                attribute_types_selector=customerprofiles.CfnDomain.AttributeTypesSelectorProperty(
                    attribute_matching_model="attributeMatchingModel",
        
                    # the properties below are optional
                    address=["address"],
                    email_address=["emailAddress"],
                    phone_number=["phoneNumber"]
                ),
                conflict_resolution=customerprofiles.CfnDomain.ConflictResolutionProperty(
                    conflict_resolving_model="conflictResolvingModel",
        
                    # the properties below are optional
                    source_name="sourceName"
                ),
                exporting_config=customerprofiles.CfnDomain.ExportingConfigProperty(
                    s3_exporting=customerprofiles.CfnDomain.S3ExportingConfigProperty(
                        s3_bucket_name="s3BucketName",
        
                        # the properties below are optional
                        s3_key_name="s3KeyName"
                    )
                ),
                matching_rules=[customerprofiles.CfnDomain.MatchingRuleProperty(
                    rule=["rule"]
                )],
                max_allowed_rule_level_for_matching=123,
                max_allowed_rule_level_for_merging=123,
                status="status"
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
        default_expiration_days: jsii.Number,
        domain_name: builtins.str,
        dead_letter_queue_url: typing.Optional[builtins.str] = None,
        default_encryption_key: typing.Optional[builtins.str] = None,
        matching: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.MatchingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        rule_based_matching: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.RuleBasedMatchingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param default_expiration_days: The default number of days until the data within the domain expires.
        :param domain_name: The unique name of the domain.
        :param dead_letter_queue_url: The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications. You must set up a policy on the ``DeadLetterQueue`` for the ``SendMessage`` operation to enable Amazon Connect Customer Profiles to send messages to the ``DeadLetterQueue`` .
        :param default_encryption_key: The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified. It is used to encrypt all data before it is placed in permanent or semi-permanent storage.
        :param matching: The process of matching duplicate profiles.
        :param rule_based_matching: The process of matching duplicate profiles using Rule-Based matching.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cc1e612474254ea8edde86de3e08226c0c50e450782b3a99c92e87c31b99bad)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainProps(
            default_expiration_days=default_expiration_days,
            domain_name=domain_name,
            dead_letter_queue_url=dead_letter_queue_url,
            default_encryption_key=default_encryption_key,
            matching=matching,
            rule_based_matching=rule_based_matching,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bd90568f369097b5d7a19088e675226c1257ad9e9ac30f3a478e941435aaaf5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__88e553e446de50b16b878a912bc0a5f6f8763a19282b8d9da5099d68ef82e5b6)
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
        '''The timestamp of when the domain was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The timestamp of when the domain was most recently edited.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleBasedMatchingStatus")
    def attr_rule_based_matching_status(self) -> builtins.str:
        '''The status of rule-based matching rule.

        :cloudformationAttribute: RuleBasedMatching.Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleBasedMatchingStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStats")
    def attr_stats(self) -> _IResolvable_da3f097b:
        '''Usage-specific statistics about the domain.

        :cloudformationAttribute: Stats
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrStats"))

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
    @jsii.member(jsii_name="defaultExpirationDays")
    def default_expiration_days(self) -> jsii.Number:
        '''The default number of days until the data within the domain expires.'''
        return typing.cast(jsii.Number, jsii.get(self, "defaultExpirationDays"))

    @default_expiration_days.setter
    def default_expiration_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d16654417fe9cbdb9f2b4f0145b59b3328699684a9b2c7ae7f2a3ad9b271e93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultExpirationDays", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5155d94ec0a92f02d3b08cff5971632f213635d3dd2577433bbe328e9fac1d90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deadLetterQueueUrl")
    def dead_letter_queue_url(self) -> typing.Optional[builtins.str]:
        '''The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deadLetterQueueUrl"))

    @dead_letter_queue_url.setter
    def dead_letter_queue_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39213ab6c2161d29ce1bafee3ec589effa27e2d24da755fd856339bb486e25a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deadLetterQueueUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultEncryptionKey")
    def default_encryption_key(self) -> typing.Optional[builtins.str]:
        '''The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultEncryptionKey"))

    @default_encryption_key.setter
    def default_encryption_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed9ea79eb70814ff005e2ba351fe52042bea41d55509db4f24fbbf0d33cfb9a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultEncryptionKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="matching")
    def matching(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.MatchingProperty"]]:
        '''The process of matching duplicate profiles.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.MatchingProperty"]], jsii.get(self, "matching"))

    @matching.setter
    def matching(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.MatchingProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38b62853e21632f695b18d1a2df674dd4f9112b5fa5e1f684278017a8ed38588)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matching", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ruleBasedMatching")
    def rule_based_matching(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.RuleBasedMatchingProperty"]]:
        '''The process of matching duplicate profiles using Rule-Based matching.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.RuleBasedMatchingProperty"]], jsii.get(self, "ruleBasedMatching"))

    @rule_based_matching.setter
    def rule_based_matching(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.RuleBasedMatchingProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__868f26d6f7d5d3991c71c5dd31b8053c3dab74afec8faa28dab5dc89621ca137)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleBasedMatching", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cc3d01d93fe80a75ec77ac1c37d929543f51e4a47feb47e25ebd0afa5fee06a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnDomain.AttributeTypesSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute_matching_model": "attributeMatchingModel",
            "address": "address",
            "email_address": "emailAddress",
            "phone_number": "phoneNumber",
        },
    )
    class AttributeTypesSelectorProperty:
        def __init__(
            self,
            *,
            attribute_matching_model: builtins.str,
            address: typing.Optional[typing.Sequence[builtins.str]] = None,
            email_address: typing.Optional[typing.Sequence[builtins.str]] = None,
            phone_number: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Configures information about the ``AttributeTypesSelector`` which rule-based identity resolution uses to match profiles.

            :param attribute_matching_model: Configures the ``AttributeMatchingModel`` , you can either choose ``ONE_TO_ONE`` or ``MANY_TO_MANY`` .
            :param address: The ``Address`` type. You can choose from ``Address`` , ``BusinessAddress`` , ``MaillingAddress`` , and ``ShippingAddress`` . You only can use the ``Address`` type in the ``MatchingRule`` . For example, if you want to match a profile based on ``BusinessAddress.City`` or ``MaillingAddress.City`` , you can choose the ``BusinessAddress`` and the ``MaillingAddress`` to represent the ``Address`` type and specify the ``Address.City`` on the matching rule.
            :param email_address: The Email type. You can choose from ``EmailAddress`` , ``BusinessEmailAddress`` and ``PersonalEmailAddress`` . You only can use the ``EmailAddress`` type in the ``MatchingRule`` . For example, if you want to match profile based on ``PersonalEmailAddress`` or ``BusinessEmailAddress`` , you can choose the ``PersonalEmailAddress`` and the ``BusinessEmailAddress`` to represent the ``EmailAddress`` type and only specify the ``EmailAddress`` on the matching rule.
            :param phone_number: The ``PhoneNumber`` type. You can choose from ``PhoneNumber`` , ``HomePhoneNumber`` , and ``MobilePhoneNumber`` . You only can use the ``PhoneNumber`` type in the ``MatchingRule`` . For example, if you want to match a profile based on ``Phone`` or ``HomePhone`` , you can choose the ``Phone`` and the ``HomePhone`` to represent the ``PhoneNumber`` type and only specify the ``PhoneNumber`` on the matching rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-attributetypesselector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                attribute_types_selector_property = customerprofiles.CfnDomain.AttributeTypesSelectorProperty(
                    attribute_matching_model="attributeMatchingModel",
                
                    # the properties below are optional
                    address=["address"],
                    email_address=["emailAddress"],
                    phone_number=["phoneNumber"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a3428c7ec5300f42cab23342316a084605547b5a853b619d629d81f5d7cfafd8)
                check_type(argname="argument attribute_matching_model", value=attribute_matching_model, expected_type=type_hints["attribute_matching_model"])
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
                check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attribute_matching_model": attribute_matching_model,
            }
            if address is not None:
                self._values["address"] = address
            if email_address is not None:
                self._values["email_address"] = email_address
            if phone_number is not None:
                self._values["phone_number"] = phone_number

        @builtins.property
        def attribute_matching_model(self) -> builtins.str:
            '''Configures the ``AttributeMatchingModel`` , you can either choose ``ONE_TO_ONE`` or ``MANY_TO_MANY`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-attributetypesselector.html#cfn-customerprofiles-domain-attributetypesselector-attributematchingmodel
            '''
            result = self._values.get("attribute_matching_model")
            assert result is not None, "Required property 'attribute_matching_model' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def address(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The ``Address`` type.

            You can choose from ``Address`` , ``BusinessAddress`` , ``MaillingAddress`` , and ``ShippingAddress`` . You only can use the ``Address`` type in the ``MatchingRule`` . For example, if you want to match a profile based on ``BusinessAddress.City`` or ``MaillingAddress.City`` , you can choose the ``BusinessAddress`` and the ``MaillingAddress`` to represent the ``Address`` type and specify the ``Address.City`` on the matching rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-attributetypesselector.html#cfn-customerprofiles-domain-attributetypesselector-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def email_address(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The Email type.

            You can choose from ``EmailAddress`` , ``BusinessEmailAddress`` and ``PersonalEmailAddress`` . You only can use the ``EmailAddress`` type in the ``MatchingRule`` . For example, if you want to match profile based on ``PersonalEmailAddress`` or ``BusinessEmailAddress`` , you can choose the ``PersonalEmailAddress`` and the ``BusinessEmailAddress`` to represent the ``EmailAddress`` type and only specify the ``EmailAddress`` on the matching rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-attributetypesselector.html#cfn-customerprofiles-domain-attributetypesselector-emailaddress
            '''
            result = self._values.get("email_address")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def phone_number(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The ``PhoneNumber`` type.

            You can choose from ``PhoneNumber`` , ``HomePhoneNumber`` , and ``MobilePhoneNumber`` . You only can use the ``PhoneNumber`` type in the ``MatchingRule`` . For example, if you want to match a profile based on ``Phone`` or ``HomePhone`` , you can choose the ``Phone`` and the ``HomePhone`` to represent the ``PhoneNumber`` type and only specify the ``PhoneNumber`` on the matching rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-attributetypesselector.html#cfn-customerprofiles-domain-attributetypesselector-phonenumber
            '''
            result = self._values.get("phone_number")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeTypesSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnDomain.AutoMergingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "conflict_resolution": "conflictResolution",
            "consolidation": "consolidation",
            "min_allowed_confidence_score_for_merging": "minAllowedConfidenceScoreForMerging",
        },
    )
    class AutoMergingProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            conflict_resolution: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.ConflictResolutionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            consolidation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.ConsolidationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            min_allowed_confidence_score_for_merging: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configuration information about the auto-merging process.

            :param enabled: The flag that enables the auto-merging of duplicate profiles.
            :param conflict_resolution: Determines how the auto-merging process should resolve conflicts between different profiles. For example, if Profile A and Profile B have the same ``FirstName`` and ``LastName`` , ``ConflictResolution`` specifies which ``EmailAddress`` should be used.
            :param consolidation: A list of matching attributes that represent matching criteria. If two profiles meet at least one of the requirements in the matching attributes list, they will be merged.
            :param min_allowed_confidence_score_for_merging: A number between 0 and 1 that represents the minimum confidence score required for profiles within a matching group to be merged during the auto-merge process. A higher score means that a higher similarity is required to merge profiles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-automerging.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                auto_merging_property = customerprofiles.CfnDomain.AutoMergingProperty(
                    enabled=False,
                
                    # the properties below are optional
                    conflict_resolution=customerprofiles.CfnDomain.ConflictResolutionProperty(
                        conflict_resolving_model="conflictResolvingModel",
                
                        # the properties below are optional
                        source_name="sourceName"
                    ),
                    consolidation=customerprofiles.CfnDomain.ConsolidationProperty(
                        matching_attributes_list=[["matchingAttributesList"]]
                    ),
                    min_allowed_confidence_score_for_merging=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5b35edae469251b1731680dae49e6588a5a064bbfac0f2f75b83135106bb693f)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument conflict_resolution", value=conflict_resolution, expected_type=type_hints["conflict_resolution"])
                check_type(argname="argument consolidation", value=consolidation, expected_type=type_hints["consolidation"])
                check_type(argname="argument min_allowed_confidence_score_for_merging", value=min_allowed_confidence_score_for_merging, expected_type=type_hints["min_allowed_confidence_score_for_merging"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }
            if conflict_resolution is not None:
                self._values["conflict_resolution"] = conflict_resolution
            if consolidation is not None:
                self._values["consolidation"] = consolidation
            if min_allowed_confidence_score_for_merging is not None:
                self._values["min_allowed_confidence_score_for_merging"] = min_allowed_confidence_score_for_merging

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''The flag that enables the auto-merging of duplicate profiles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-automerging.html#cfn-customerprofiles-domain-automerging-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def conflict_resolution(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ConflictResolutionProperty"]]:
            '''Determines how the auto-merging process should resolve conflicts between different profiles.

            For example, if Profile A and Profile B have the same ``FirstName`` and ``LastName`` , ``ConflictResolution`` specifies which ``EmailAddress`` should be used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-automerging.html#cfn-customerprofiles-domain-automerging-conflictresolution
            '''
            result = self._values.get("conflict_resolution")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ConflictResolutionProperty"]], result)

        @builtins.property
        def consolidation(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ConsolidationProperty"]]:
            '''A list of matching attributes that represent matching criteria.

            If two profiles meet at least one of the requirements in the matching attributes list, they will be merged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-automerging.html#cfn-customerprofiles-domain-automerging-consolidation
            '''
            result = self._values.get("consolidation")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ConsolidationProperty"]], result)

        @builtins.property
        def min_allowed_confidence_score_for_merging(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''A number between 0 and 1 that represents the minimum confidence score required for profiles within a matching group to be merged during the auto-merge process.

            A higher score means that a higher similarity is required to merge profiles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-automerging.html#cfn-customerprofiles-domain-automerging-minallowedconfidencescoreformerging
            '''
            result = self._values.get("min_allowed_confidence_score_for_merging")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoMergingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnDomain.ConflictResolutionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "conflict_resolving_model": "conflictResolvingModel",
            "source_name": "sourceName",
        },
    )
    class ConflictResolutionProperty:
        def __init__(
            self,
            *,
            conflict_resolving_model: builtins.str,
            source_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Determines how the auto-merging process should resolve conflicts between different profiles.

            For example, if Profile A and Profile B have the same ``FirstName`` and ``LastName`` , ``ConflictResolution`` specifies which ``EmailAddress`` should be used.

            :param conflict_resolving_model: How the auto-merging process should resolve conflicts between different profiles.
            :param source_name: The ``ObjectType`` name that is used to resolve profile merging conflicts when choosing ``SOURCE`` as the ``ConflictResolvingModel`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-conflictresolution.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                conflict_resolution_property = customerprofiles.CfnDomain.ConflictResolutionProperty(
                    conflict_resolving_model="conflictResolvingModel",
                
                    # the properties below are optional
                    source_name="sourceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__39a5c699e09d6961f3eed32cb756eca983664193f4a0cdfbac7965404e3b40d1)
                check_type(argname="argument conflict_resolving_model", value=conflict_resolving_model, expected_type=type_hints["conflict_resolving_model"])
                check_type(argname="argument source_name", value=source_name, expected_type=type_hints["source_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "conflict_resolving_model": conflict_resolving_model,
            }
            if source_name is not None:
                self._values["source_name"] = source_name

        @builtins.property
        def conflict_resolving_model(self) -> builtins.str:
            '''How the auto-merging process should resolve conflicts between different profiles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-conflictresolution.html#cfn-customerprofiles-domain-conflictresolution-conflictresolvingmodel
            '''
            result = self._values.get("conflict_resolving_model")
            assert result is not None, "Required property 'conflict_resolving_model' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_name(self) -> typing.Optional[builtins.str]:
            '''The ``ObjectType`` name that is used to resolve profile merging conflicts when choosing ``SOURCE`` as the ``ConflictResolvingModel`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-conflictresolution.html#cfn-customerprofiles-domain-conflictresolution-sourcename
            '''
            result = self._values.get("source_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConflictResolutionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnDomain.ConsolidationProperty",
        jsii_struct_bases=[],
        name_mapping={"matching_attributes_list": "matchingAttributesList"},
    )
    class ConsolidationProperty:
        def __init__(
            self,
            *,
            matching_attributes_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Sequence[builtins.str]]],
        ) -> None:
            '''A list of matching attributes that represent matching criteria.

            If two profiles meet at least one of the requirements in the matching attributes list, they will be merged.

            :param matching_attributes_list: A list of matching criteria.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-consolidation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                consolidation_property = customerprofiles.CfnDomain.ConsolidationProperty(
                    matching_attributes_list=[["matchingAttributesList"]]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2f3fee71d236ee85937168636cf44627d0e12e7714908fdcc02548a6e6baa537)
                check_type(argname="argument matching_attributes_list", value=matching_attributes_list, expected_type=type_hints["matching_attributes_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "matching_attributes_list": matching_attributes_list,
            }

        @builtins.property
        def matching_attributes_list(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.List[builtins.str]]]:
            '''A list of matching criteria.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-consolidation.html#cfn-customerprofiles-domain-consolidation-matchingattributeslist
            '''
            result = self._values.get("matching_attributes_list")
            assert result is not None, "Required property 'matching_attributes_list' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.List[builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConsolidationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnDomain.DomainStatsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metering_profile_count": "meteringProfileCount",
            "object_count": "objectCount",
            "profile_count": "profileCount",
            "total_size": "totalSize",
        },
    )
    class DomainStatsProperty:
        def __init__(
            self,
            *,
            metering_profile_count: typing.Optional[jsii.Number] = None,
            object_count: typing.Optional[jsii.Number] = None,
            profile_count: typing.Optional[jsii.Number] = None,
            total_size: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Usage-specific statistics about the domain.

            :param metering_profile_count: The number of profiles that you are currently paying for in the domain. If you have more than 100 objects associated with a single profile, that profile counts as two profiles. If you have more than 200 objects, that profile counts as three, and so on.
            :param object_count: The total number of objects in domain.
            :param profile_count: The total number of profiles currently in the domain.
            :param total_size: The total size, in bytes, of all objects in the domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-domainstats.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                domain_stats_property = customerprofiles.CfnDomain.DomainStatsProperty(
                    metering_profile_count=123,
                    object_count=123,
                    profile_count=123,
                    total_size=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ed7393f6287227101f4cad4938dff729de652d2fea3653b0c4f8ef82477058e4)
                check_type(argname="argument metering_profile_count", value=metering_profile_count, expected_type=type_hints["metering_profile_count"])
                check_type(argname="argument object_count", value=object_count, expected_type=type_hints["object_count"])
                check_type(argname="argument profile_count", value=profile_count, expected_type=type_hints["profile_count"])
                check_type(argname="argument total_size", value=total_size, expected_type=type_hints["total_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if metering_profile_count is not None:
                self._values["metering_profile_count"] = metering_profile_count
            if object_count is not None:
                self._values["object_count"] = object_count
            if profile_count is not None:
                self._values["profile_count"] = profile_count
            if total_size is not None:
                self._values["total_size"] = total_size

        @builtins.property
        def metering_profile_count(self) -> typing.Optional[jsii.Number]:
            '''The number of profiles that you are currently paying for in the domain.

            If you have more than 100 objects associated with a single profile, that profile counts as two profiles. If you have more than 200 objects, that profile counts as three, and so on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-domainstats.html#cfn-customerprofiles-domain-domainstats-meteringprofilecount
            '''
            result = self._values.get("metering_profile_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def object_count(self) -> typing.Optional[jsii.Number]:
            '''The total number of objects in domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-domainstats.html#cfn-customerprofiles-domain-domainstats-objectcount
            '''
            result = self._values.get("object_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def profile_count(self) -> typing.Optional[jsii.Number]:
            '''The total number of profiles currently in the domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-domainstats.html#cfn-customerprofiles-domain-domainstats-profilecount
            '''
            result = self._values.get("profile_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total_size(self) -> typing.Optional[jsii.Number]:
            '''The total size, in bytes, of all objects in the domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-domainstats.html#cfn-customerprofiles-domain-domainstats-totalsize
            '''
            result = self._values.get("total_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DomainStatsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnDomain.ExportingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_exporting": "s3Exporting"},
    )
    class ExportingConfigProperty:
        def __init__(
            self,
            *,
            s3_exporting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.S3ExportingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration information for exporting Identity Resolution results, for example, to an S3 bucket.

            :param s3_exporting: The S3 location where Identity Resolution Jobs write result files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-exportingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                exporting_config_property = customerprofiles.CfnDomain.ExportingConfigProperty(
                    s3_exporting=customerprofiles.CfnDomain.S3ExportingConfigProperty(
                        s3_bucket_name="s3BucketName",
                
                        # the properties below are optional
                        s3_key_name="s3KeyName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fb96a013617382e2d069cda664f0c892dede8cafdff896ba1efefecbd051b998)
                check_type(argname="argument s3_exporting", value=s3_exporting, expected_type=type_hints["s3_exporting"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_exporting is not None:
                self._values["s3_exporting"] = s3_exporting

        @builtins.property
        def s3_exporting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.S3ExportingConfigProperty"]]:
            '''The S3 location where Identity Resolution Jobs write result files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-exportingconfig.html#cfn-customerprofiles-domain-exportingconfig-s3exporting
            '''
            result = self._values.get("s3_exporting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.S3ExportingConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExportingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnDomain.JobScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={"day_of_the_week": "dayOfTheWeek", "time": "time"},
    )
    class JobScheduleProperty:
        def __init__(
            self,
            *,
            day_of_the_week: builtins.str,
            time: builtins.str,
        ) -> None:
            '''The day and time when do you want to start the Identity Resolution Job every week.

            :param day_of_the_week: The day when the Identity Resolution Job should run every week.
            :param time: The time when the Identity Resolution Job should run every week.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-jobschedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                job_schedule_property = customerprofiles.CfnDomain.JobScheduleProperty(
                    day_of_the_week="dayOfTheWeek",
                    time="time"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f904c449e943e8aaee42f71a3d0a53319d006582bc12e5658661832c9424bd99)
                check_type(argname="argument day_of_the_week", value=day_of_the_week, expected_type=type_hints["day_of_the_week"])
                check_type(argname="argument time", value=time, expected_type=type_hints["time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "day_of_the_week": day_of_the_week,
                "time": time,
            }

        @builtins.property
        def day_of_the_week(self) -> builtins.str:
            '''The day when the Identity Resolution Job should run every week.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-jobschedule.html#cfn-customerprofiles-domain-jobschedule-dayoftheweek
            '''
            result = self._values.get("day_of_the_week")
            assert result is not None, "Required property 'day_of_the_week' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def time(self) -> builtins.str:
            '''The time when the Identity Resolution Job should run every week.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-jobschedule.html#cfn-customerprofiles-domain-jobschedule-time
            '''
            result = self._values.get("time")
            assert result is not None, "Required property 'time' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JobScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnDomain.MatchingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "auto_merging": "autoMerging",
            "exporting_config": "exportingConfig",
            "job_schedule": "jobSchedule",
        },
    )
    class MatchingProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            auto_merging: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.AutoMergingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            exporting_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.ExportingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            job_schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.JobScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The process of matching duplicate profiles.

            If ``Matching = true`` , Amazon Connect Customer Profiles starts a weekly batch process called *Identity Resolution Job* . If you do not specify a date and time for the *Identity Resolution Job* to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains. After the *Identity Resolution Job* completes, use the ``GetMatches`` API to return and review the results. Or, if you have configured ``ExportingConfig`` in the ``MatchingRequest`` , you can download the results from S3.

            :param enabled: The flag that enables the matching process of duplicate profiles.
            :param auto_merging: Configuration information about the auto-merging process.
            :param exporting_config: The S3 location where Identity Resolution Jobs write result files.
            :param job_schedule: The day and time when do you want to start the Identity Resolution Job every week.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matching.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                matching_property = customerprofiles.CfnDomain.MatchingProperty(
                    enabled=False,
                
                    # the properties below are optional
                    auto_merging=customerprofiles.CfnDomain.AutoMergingProperty(
                        enabled=False,
                
                        # the properties below are optional
                        conflict_resolution=customerprofiles.CfnDomain.ConflictResolutionProperty(
                            conflict_resolving_model="conflictResolvingModel",
                
                            # the properties below are optional
                            source_name="sourceName"
                        ),
                        consolidation=customerprofiles.CfnDomain.ConsolidationProperty(
                            matching_attributes_list=[["matchingAttributesList"]]
                        ),
                        min_allowed_confidence_score_for_merging=123
                    ),
                    exporting_config=customerprofiles.CfnDomain.ExportingConfigProperty(
                        s3_exporting=customerprofiles.CfnDomain.S3ExportingConfigProperty(
                            s3_bucket_name="s3BucketName",
                
                            # the properties below are optional
                            s3_key_name="s3KeyName"
                        )
                    ),
                    job_schedule=customerprofiles.CfnDomain.JobScheduleProperty(
                        day_of_the_week="dayOfTheWeek",
                        time="time"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1f66676b221bc8ebb46140fe93d616e4dde0b38406203efe2203ad295a0605a4)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument auto_merging", value=auto_merging, expected_type=type_hints["auto_merging"])
                check_type(argname="argument exporting_config", value=exporting_config, expected_type=type_hints["exporting_config"])
                check_type(argname="argument job_schedule", value=job_schedule, expected_type=type_hints["job_schedule"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }
            if auto_merging is not None:
                self._values["auto_merging"] = auto_merging
            if exporting_config is not None:
                self._values["exporting_config"] = exporting_config
            if job_schedule is not None:
                self._values["job_schedule"] = job_schedule

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''The flag that enables the matching process of duplicate profiles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matching.html#cfn-customerprofiles-domain-matching-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def auto_merging(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.AutoMergingProperty"]]:
            '''Configuration information about the auto-merging process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matching.html#cfn-customerprofiles-domain-matching-automerging
            '''
            result = self._values.get("auto_merging")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.AutoMergingProperty"]], result)

        @builtins.property
        def exporting_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ExportingConfigProperty"]]:
            '''The S3 location where Identity Resolution Jobs write result files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matching.html#cfn-customerprofiles-domain-matching-exportingconfig
            '''
            result = self._values.get("exporting_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ExportingConfigProperty"]], result)

        @builtins.property
        def job_schedule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.JobScheduleProperty"]]:
            '''The day and time when do you want to start the Identity Resolution Job every week.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matching.html#cfn-customerprofiles-domain-matching-jobschedule
            '''
            result = self._values.get("job_schedule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.JobScheduleProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MatchingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnDomain.MatchingRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"rule": "rule"},
    )
    class MatchingRuleProperty:
        def __init__(self, *, rule: typing.Sequence[builtins.str]) -> None:
            '''Specifies how the rule-based matching process should match profiles.

            :param rule: A single rule level of the ``MatchRules`` . Configures how the rule-based matching process should match profiles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matchingrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                matching_rule_property = customerprofiles.CfnDomain.MatchingRuleProperty(
                    rule=["rule"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0d978c61e1b04215bb349c7460583b8296f0fc2a1f64e575731bf7ab355b1b9e)
                check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rule": rule,
            }

        @builtins.property
        def rule(self) -> typing.List[builtins.str]:
            '''A single rule level of the ``MatchRules`` .

            Configures how the rule-based matching process should match profiles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-matchingrule.html#cfn-customerprofiles-domain-matchingrule-rule
            '''
            result = self._values.get("rule")
            assert result is not None, "Required property 'rule' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MatchingRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnDomain.RuleBasedMatchingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "attribute_types_selector": "attributeTypesSelector",
            "conflict_resolution": "conflictResolution",
            "exporting_config": "exportingConfig",
            "matching_rules": "matchingRules",
            "max_allowed_rule_level_for_matching": "maxAllowedRuleLevelForMatching",
            "max_allowed_rule_level_for_merging": "maxAllowedRuleLevelForMerging",
            "status": "status",
        },
    )
    class RuleBasedMatchingProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            attribute_types_selector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.AttributeTypesSelectorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            conflict_resolution: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.ConflictResolutionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            exporting_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.ExportingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            matching_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomain.MatchingRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            max_allowed_rule_level_for_matching: typing.Optional[jsii.Number] = None,
            max_allowed_rule_level_for_merging: typing.Optional[jsii.Number] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The process of matching duplicate profiles using Rule-Based matching.

            If ``RuleBasedMatching = true`` , Amazon Connect Customer Profiles will start to match and merge your profiles according to your configuration in the ``RuleBasedMatchingRequest`` . You can use the ``ListRuleBasedMatches`` and ``GetSimilarProfiles`` API to return and review the results. Also, if you have configured ``ExportingConfig`` in the ``RuleBasedMatchingRequest`` , you can download the results from S3.

            :param enabled: The flag that enables the matching process of duplicate profiles.
            :param attribute_types_selector: Configures information about the ``AttributeTypesSelector`` where the rule-based identity resolution uses to match profiles.
            :param conflict_resolution: Determines how the auto-merging process should resolve conflicts between different profiles. For example, if Profile A and Profile B have the same ``FirstName`` and ``LastName`` , ``ConflictResolution`` specifies which ``EmailAddress`` should be used.
            :param exporting_config: The S3 location where Identity Resolution Jobs write result files.
            :param matching_rules: Configures how the rule-based matching process should match profiles. You can have up to 15 ``MatchingRule`` in the ``MatchingRules`` .
            :param max_allowed_rule_level_for_matching: Indicates the maximum allowed rule level for matching.
            :param max_allowed_rule_level_for_merging: Indicates the maximum allowed rule level for merging.
            :param status: The status of rule-based matching rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                rule_based_matching_property = customerprofiles.CfnDomain.RuleBasedMatchingProperty(
                    enabled=False,
                
                    # the properties below are optional
                    attribute_types_selector=customerprofiles.CfnDomain.AttributeTypesSelectorProperty(
                        attribute_matching_model="attributeMatchingModel",
                
                        # the properties below are optional
                        address=["address"],
                        email_address=["emailAddress"],
                        phone_number=["phoneNumber"]
                    ),
                    conflict_resolution=customerprofiles.CfnDomain.ConflictResolutionProperty(
                        conflict_resolving_model="conflictResolvingModel",
                
                        # the properties below are optional
                        source_name="sourceName"
                    ),
                    exporting_config=customerprofiles.CfnDomain.ExportingConfigProperty(
                        s3_exporting=customerprofiles.CfnDomain.S3ExportingConfigProperty(
                            s3_bucket_name="s3BucketName",
                
                            # the properties below are optional
                            s3_key_name="s3KeyName"
                        )
                    ),
                    matching_rules=[customerprofiles.CfnDomain.MatchingRuleProperty(
                        rule=["rule"]
                    )],
                    max_allowed_rule_level_for_matching=123,
                    max_allowed_rule_level_for_merging=123,
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63470bb7c476b2fc82a2f0bc6e61f9a94630928b1d8427c1ec5400fd3523d282)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument attribute_types_selector", value=attribute_types_selector, expected_type=type_hints["attribute_types_selector"])
                check_type(argname="argument conflict_resolution", value=conflict_resolution, expected_type=type_hints["conflict_resolution"])
                check_type(argname="argument exporting_config", value=exporting_config, expected_type=type_hints["exporting_config"])
                check_type(argname="argument matching_rules", value=matching_rules, expected_type=type_hints["matching_rules"])
                check_type(argname="argument max_allowed_rule_level_for_matching", value=max_allowed_rule_level_for_matching, expected_type=type_hints["max_allowed_rule_level_for_matching"])
                check_type(argname="argument max_allowed_rule_level_for_merging", value=max_allowed_rule_level_for_merging, expected_type=type_hints["max_allowed_rule_level_for_merging"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }
            if attribute_types_selector is not None:
                self._values["attribute_types_selector"] = attribute_types_selector
            if conflict_resolution is not None:
                self._values["conflict_resolution"] = conflict_resolution
            if exporting_config is not None:
                self._values["exporting_config"] = exporting_config
            if matching_rules is not None:
                self._values["matching_rules"] = matching_rules
            if max_allowed_rule_level_for_matching is not None:
                self._values["max_allowed_rule_level_for_matching"] = max_allowed_rule_level_for_matching
            if max_allowed_rule_level_for_merging is not None:
                self._values["max_allowed_rule_level_for_merging"] = max_allowed_rule_level_for_merging
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''The flag that enables the matching process of duplicate profiles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def attribute_types_selector(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.AttributeTypesSelectorProperty"]]:
            '''Configures information about the ``AttributeTypesSelector`` where the rule-based identity resolution uses to match profiles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-attributetypesselector
            '''
            result = self._values.get("attribute_types_selector")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.AttributeTypesSelectorProperty"]], result)

        @builtins.property
        def conflict_resolution(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ConflictResolutionProperty"]]:
            '''Determines how the auto-merging process should resolve conflicts between different profiles.

            For example, if Profile A and Profile B have the same ``FirstName`` and ``LastName`` , ``ConflictResolution`` specifies which ``EmailAddress`` should be used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-conflictresolution
            '''
            result = self._values.get("conflict_resolution")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ConflictResolutionProperty"]], result)

        @builtins.property
        def exporting_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ExportingConfigProperty"]]:
            '''The S3 location where Identity Resolution Jobs write result files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-exportingconfig
            '''
            result = self._values.get("exporting_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomain.ExportingConfigProperty"]], result)

        @builtins.property
        def matching_rules(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDomain.MatchingRuleProperty"]]]]:
            '''Configures how the rule-based matching process should match profiles.

            You can have up to 15 ``MatchingRule`` in the ``MatchingRules`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-matchingrules
            '''
            result = self._values.get("matching_rules")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDomain.MatchingRuleProperty"]]]], result)

        @builtins.property
        def max_allowed_rule_level_for_matching(self) -> typing.Optional[jsii.Number]:
            '''Indicates the maximum allowed rule level for matching.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-maxallowedrulelevelformatching
            '''
            result = self._values.get("max_allowed_rule_level_for_matching")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_allowed_rule_level_for_merging(self) -> typing.Optional[jsii.Number]:
            '''Indicates the maximum allowed rule level for merging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-maxallowedrulelevelformerging
            '''
            result = self._values.get("max_allowed_rule_level_for_merging")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of rule-based matching rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-rulebasedmatching.html#cfn-customerprofiles-domain-rulebasedmatching-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleBasedMatchingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnDomain.S3ExportingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_bucket_name": "s3BucketName", "s3_key_name": "s3KeyName"},
    )
    class S3ExportingConfigProperty:
        def __init__(
            self,
            *,
            s3_bucket_name: builtins.str,
            s3_key_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The S3 location where Identity Resolution Jobs write result files.

            :param s3_bucket_name: The name of the S3 bucket where Identity Resolution Jobs write result files.
            :param s3_key_name: The S3 key name of the location where Identity Resolution Jobs write result files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-s3exportingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                s3_exporting_config_property = customerprofiles.CfnDomain.S3ExportingConfigProperty(
                    s3_bucket_name="s3BucketName",
                
                    # the properties below are optional
                    s3_key_name="s3KeyName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__67d29e593ac1f40be9594826daeee9e088ed90a7a1c973d30de0a10f42a70cb6)
                check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
                check_type(argname="argument s3_key_name", value=s3_key_name, expected_type=type_hints["s3_key_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_bucket_name": s3_bucket_name,
            }
            if s3_key_name is not None:
                self._values["s3_key_name"] = s3_key_name

        @builtins.property
        def s3_bucket_name(self) -> builtins.str:
            '''The name of the S3 bucket where Identity Resolution Jobs write result files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-s3exportingconfig.html#cfn-customerprofiles-domain-s3exportingconfig-s3bucketname
            '''
            result = self._values.get("s3_bucket_name")
            assert result is not None, "Required property 's3_bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_key_name(self) -> typing.Optional[builtins.str]:
            '''The S3 key name of the location where Identity Resolution Jobs write result files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-domain-s3exportingconfig.html#cfn-customerprofiles-domain-s3exportingconfig-s3keyname
            '''
            result = self._values.get("s3_key_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ExportingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnDomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "default_expiration_days": "defaultExpirationDays",
        "domain_name": "domainName",
        "dead_letter_queue_url": "deadLetterQueueUrl",
        "default_encryption_key": "defaultEncryptionKey",
        "matching": "matching",
        "rule_based_matching": "ruleBasedMatching",
        "tags": "tags",
    },
)
class CfnDomainProps:
    def __init__(
        self,
        *,
        default_expiration_days: jsii.Number,
        domain_name: builtins.str,
        dead_letter_queue_url: typing.Optional[builtins.str] = None,
        default_encryption_key: typing.Optional[builtins.str] = None,
        matching: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.MatchingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        rule_based_matching: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.RuleBasedMatchingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDomain``.

        :param default_expiration_days: The default number of days until the data within the domain expires.
        :param domain_name: The unique name of the domain.
        :param dead_letter_queue_url: The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications. You must set up a policy on the ``DeadLetterQueue`` for the ``SendMessage`` operation to enable Amazon Connect Customer Profiles to send messages to the ``DeadLetterQueue`` .
        :param default_encryption_key: The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified. It is used to encrypt all data before it is placed in permanent or semi-permanent storage.
        :param matching: The process of matching duplicate profiles.
        :param rule_based_matching: The process of matching duplicate profiles using Rule-Based matching.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_customerprofiles as customerprofiles
            
            cfn_domain_props = customerprofiles.CfnDomainProps(
                default_expiration_days=123,
                domain_name="domainName",
            
                # the properties below are optional
                dead_letter_queue_url="deadLetterQueueUrl",
                default_encryption_key="defaultEncryptionKey",
                matching=customerprofiles.CfnDomain.MatchingProperty(
                    enabled=False,
            
                    # the properties below are optional
                    auto_merging=customerprofiles.CfnDomain.AutoMergingProperty(
                        enabled=False,
            
                        # the properties below are optional
                        conflict_resolution=customerprofiles.CfnDomain.ConflictResolutionProperty(
                            conflict_resolving_model="conflictResolvingModel",
            
                            # the properties below are optional
                            source_name="sourceName"
                        ),
                        consolidation=customerprofiles.CfnDomain.ConsolidationProperty(
                            matching_attributes_list=[["matchingAttributesList"]]
                        ),
                        min_allowed_confidence_score_for_merging=123
                    ),
                    exporting_config=customerprofiles.CfnDomain.ExportingConfigProperty(
                        s3_exporting=customerprofiles.CfnDomain.S3ExportingConfigProperty(
                            s3_bucket_name="s3BucketName",
            
                            # the properties below are optional
                            s3_key_name="s3KeyName"
                        )
                    ),
                    job_schedule=customerprofiles.CfnDomain.JobScheduleProperty(
                        day_of_the_week="dayOfTheWeek",
                        time="time"
                    )
                ),
                rule_based_matching=customerprofiles.CfnDomain.RuleBasedMatchingProperty(
                    enabled=False,
            
                    # the properties below are optional
                    attribute_types_selector=customerprofiles.CfnDomain.AttributeTypesSelectorProperty(
                        attribute_matching_model="attributeMatchingModel",
            
                        # the properties below are optional
                        address=["address"],
                        email_address=["emailAddress"],
                        phone_number=["phoneNumber"]
                    ),
                    conflict_resolution=customerprofiles.CfnDomain.ConflictResolutionProperty(
                        conflict_resolving_model="conflictResolvingModel",
            
                        # the properties below are optional
                        source_name="sourceName"
                    ),
                    exporting_config=customerprofiles.CfnDomain.ExportingConfigProperty(
                        s3_exporting=customerprofiles.CfnDomain.S3ExportingConfigProperty(
                            s3_bucket_name="s3BucketName",
            
                            # the properties below are optional
                            s3_key_name="s3KeyName"
                        )
                    ),
                    matching_rules=[customerprofiles.CfnDomain.MatchingRuleProperty(
                        rule=["rule"]
                    )],
                    max_allowed_rule_level_for_matching=123,
                    max_allowed_rule_level_for_merging=123,
                    status="status"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03a55eb0b8d16e4b2b2589908d65475847a28870949386381667b6572e627f96)
            check_type(argname="argument default_expiration_days", value=default_expiration_days, expected_type=type_hints["default_expiration_days"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument dead_letter_queue_url", value=dead_letter_queue_url, expected_type=type_hints["dead_letter_queue_url"])
            check_type(argname="argument default_encryption_key", value=default_encryption_key, expected_type=type_hints["default_encryption_key"])
            check_type(argname="argument matching", value=matching, expected_type=type_hints["matching"])
            check_type(argname="argument rule_based_matching", value=rule_based_matching, expected_type=type_hints["rule_based_matching"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_expiration_days": default_expiration_days,
            "domain_name": domain_name,
        }
        if dead_letter_queue_url is not None:
            self._values["dead_letter_queue_url"] = dead_letter_queue_url
        if default_encryption_key is not None:
            self._values["default_encryption_key"] = default_encryption_key
        if matching is not None:
            self._values["matching"] = matching
        if rule_based_matching is not None:
            self._values["rule_based_matching"] = rule_based_matching
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def default_expiration_days(self) -> jsii.Number:
        '''The default number of days until the data within the domain expires.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultexpirationdays
        '''
        result = self._values.get("default_expiration_days")
        assert result is not None, "Required property 'default_expiration_days' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dead_letter_queue_url(self) -> typing.Optional[builtins.str]:
        '''The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications.

        You must set up a policy on the ``DeadLetterQueue`` for the ``SendMessage`` operation to enable Amazon Connect Customer Profiles to send messages to the ``DeadLetterQueue`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-deadletterqueueurl
        '''
        result = self._values.get("dead_letter_queue_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_encryption_key(self) -> typing.Optional[builtins.str]:
        '''The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified.

        It is used to encrypt all data before it is placed in permanent or semi-permanent storage.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-defaultencryptionkey
        '''
        result = self._values.get("default_encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def matching(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.MatchingProperty]]:
        '''The process of matching duplicate profiles.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-matching
        '''
        result = self._values.get("matching")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.MatchingProperty]], result)

    @builtins.property
    def rule_based_matching(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.RuleBasedMatchingProperty]]:
        '''The process of matching duplicate profiles using Rule-Based matching.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-rulebasedmatching
        '''
        result = self._values.get("rule_based_matching")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.RuleBasedMatchingProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-domain.html#cfn-customerprofiles-domain-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnEventStream(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnEventStream",
):
    '''An Event Stream resource of Amazon Connect Customer Profiles.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html
    :cloudformationResource: AWS::CustomerProfiles::EventStream
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_customerprofiles as customerprofiles
        
        cfn_event_stream = customerprofiles.CfnEventStream(self, "MyCfnEventStream",
            domain_name="domainName",
            event_stream_name="eventStreamName",
            uri="uri",
        
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
        domain_name: builtins.str,
        event_stream_name: builtins.str,
        uri: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_name: The unique name of the domain.
        :param event_stream_name: The name of the event stream.
        :param uri: The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab29d0d747428994b84491cb3989a05a67bcb4cf0b84ebeba8fd19114b7cd61d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventStreamProps(
            domain_name=domain_name,
            event_stream_name=event_stream_name,
            uri=uri,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d37a000675ecf626a3348ff78d7f60db4441f2bb16c208d8dea0d1a4ecbd88f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__897cf1ba007446204846a7b757f800cd045b6bea2153894c6a8efdade633eaca)
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
        '''The timestamp of when the export was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDestinationDetails")
    def attr_destination_details(self) -> _IResolvable_da3f097b:
        '''Details regarding the Kinesis stream.

        :cloudformationAttribute: DestinationDetails
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrDestinationDetails"))

    @builtins.property
    @jsii.member(jsii_name="attrDestinationDetailsStatus")
    def attr_destination_details_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: DestinationDetails.Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDestinationDetailsStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrDestinationDetailsUri")
    def attr_destination_details_uri(self) -> builtins.str:
        '''
        :cloudformationAttribute: DestinationDetails.Uri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDestinationDetailsUri"))

    @builtins.property
    @jsii.member(jsii_name="attrEventStreamArn")
    def attr_event_stream_arn(self) -> builtins.str:
        '''A unique identifier for the event stream.

        :cloudformationAttribute: EventStreamArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEventStreamArn"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The operational state of destination stream for export.

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

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
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e40edb2a552aa50e0d65e685a232d9e8b469877491c9fd016aaf025966b9a1b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="eventStreamName")
    def event_stream_name(self) -> builtins.str:
        '''The name of the event stream.'''
        return typing.cast(builtins.str, jsii.get(self, "eventStreamName"))

    @event_stream_name.setter
    def event_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87ecaa8f57744bab81313074352cbc2f82cf8f797e78ce582ff548aa6251c330)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventStreamName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        '''The StreamARN of the destination to deliver profile events to.'''
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d80288203f7d0782baca6858266d8c740f3fda90b2d6ef328306f3e966d5ee4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dcffaefd3d051ab25e983d551d4abe7f28bcc0ccc2cc0f00dfbe9151cc9bd64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnEventStream.DestinationDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"status": "status", "uri": "uri"},
    )
    class DestinationDetailsProperty:
        def __init__(self, *, status: builtins.str, uri: builtins.str) -> None:
            '''Details regarding the Kinesis stream.

            :param status: The status of enabling the Kinesis stream as a destination for export.
            :param uri: The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventstream-destinationdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                destination_details_property = customerprofiles.CfnEventStream.DestinationDetailsProperty(
                    status="status",
                    uri="uri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__14be2a6e46acdc39b98267227ca646cdeba3edce7277e1499527949bda68cd54)
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "status": status,
                "uri": uri,
            }

        @builtins.property
        def status(self) -> builtins.str:
            '''The status of enabling the Kinesis stream as a destination for export.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventstream-destinationdetails.html#cfn-customerprofiles-eventstream-destinationdetails-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def uri(self) -> builtins.str:
            '''The StreamARN of the destination to deliver profile events to.

            For example, arn:aws:kinesis:region:account-id:stream/stream-name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventstream-destinationdetails.html#cfn-customerprofiles-eventstream-destinationdetails-uri
            '''
            result = self._values.get("uri")
            assert result is not None, "Required property 'uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnEventStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "event_stream_name": "eventStreamName",
        "uri": "uri",
        "tags": "tags",
    },
)
class CfnEventStreamProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        event_stream_name: builtins.str,
        uri: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEventStream``.

        :param domain_name: The unique name of the domain.
        :param event_stream_name: The name of the event stream.
        :param uri: The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_customerprofiles as customerprofiles
            
            cfn_event_stream_props = customerprofiles.CfnEventStreamProps(
                domain_name="domainName",
                event_stream_name="eventStreamName",
                uri="uri",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__813f95ba6287d3dc18d43b5b2ff35fbde17184e556360b280e3386143cfc00f0)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument event_stream_name", value=event_stream_name, expected_type=type_hints["event_stream_name"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "event_stream_name": event_stream_name,
            "uri": uri,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html#cfn-customerprofiles-eventstream-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_stream_name(self) -> builtins.str:
        '''The name of the event stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html#cfn-customerprofiles-eventstream-eventstreamname
        '''
        result = self._values.get("event_stream_name")
        assert result is not None, "Required property 'event_stream_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def uri(self) -> builtins.str:
        '''The StreamARN of the destination to deliver profile events to.

        For example, arn:aws:kinesis:region:account-id:stream/stream-name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html#cfn-customerprofiles-eventstream-uri
        '''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventstream.html#cfn-customerprofiles-eventstream-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnEventTrigger(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnEventTrigger",
):
    '''Specifies the rules to perform an action based on customer ingested data.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventtrigger.html
    :cloudformationResource: AWS::CustomerProfiles::EventTrigger
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_customerprofiles as customerprofiles
        
        cfn_event_trigger = customerprofiles.CfnEventTrigger(self, "MyCfnEventTrigger",
            domain_name="domainName",
            event_trigger_conditions=[customerprofiles.CfnEventTrigger.EventTriggerConditionProperty(
                event_trigger_dimensions=[customerprofiles.CfnEventTrigger.EventTriggerDimensionProperty(
                    object_attributes=[customerprofiles.CfnEventTrigger.ObjectAttributeProperty(
                        comparison_operator="comparisonOperator",
                        values=["values"],
        
                        # the properties below are optional
                        field_name="fieldName",
                        source="source"
                    )]
                )],
                logical_operator="logicalOperator"
            )],
            event_trigger_name="eventTriggerName",
            object_type_name="objectTypeName",
        
            # the properties below are optional
            description="description",
            event_trigger_limits=customerprofiles.CfnEventTrigger.EventTriggerLimitsProperty(
                event_expiration=123,
                periods=[customerprofiles.CfnEventTrigger.PeriodProperty(
                    unit="unit",
                    value=123,
        
                    # the properties below are optional
                    max_invocations_per_profile=123,
                    unlimited=False
                )]
            ),
            segment_filter="segmentFilter",
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
        domain_name: builtins.str,
        event_trigger_conditions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEventTrigger.EventTriggerConditionProperty", typing.Dict[builtins.str, typing.Any]]]]],
        event_trigger_name: builtins.str,
        object_type_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        event_trigger_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEventTrigger.EventTriggerLimitsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        segment_filter: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_name: The unique name of the domain.
        :param event_trigger_conditions: A list of conditions that determine when an event should trigger the destination.
        :param event_trigger_name: The unique name of the event trigger.
        :param object_type_name: The unique name of the object type.
        :param description: The description of the event trigger.
        :param event_trigger_limits: Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.
        :param segment_filter: The destination is triggered only for profiles that meet the criteria of a segment definition.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3238d15e8be30353d06e9f7813fb0d93d105339df1e3008dc6d5d889128103a4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventTriggerProps(
            domain_name=domain_name,
            event_trigger_conditions=event_trigger_conditions,
            event_trigger_name=event_trigger_name,
            object_type_name=object_type_name,
            description=description,
            event_trigger_limits=event_trigger_limits,
            segment_filter=segment_filter,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e272d39f5f3a739ab199e698c49cb32366cbc41b54a8e3cc306be93e625b409)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9d0fbc1a083288ddd09e30a938f56be084f6444e4f3ee741d96ffda16a72c037)
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
        '''The timestamp of when the event trigger was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The timestamp of when the event trigger was most recently updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

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
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46f0ca81a5f8cee1e0a4c4f9b3d38652326a6ebce5ed8f5ee45cd3300bc09d21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="eventTriggerConditions")
    def event_trigger_conditions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventTrigger.EventTriggerConditionProperty"]]]:
        '''A list of conditions that determine when an event should trigger the destination.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventTrigger.EventTriggerConditionProperty"]]], jsii.get(self, "eventTriggerConditions"))

    @event_trigger_conditions.setter
    def event_trigger_conditions(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventTrigger.EventTriggerConditionProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c4c9a1ce30ec03f18e86da98746e17633bdcc9de1f9657feb330288a5703464)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventTriggerConditions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="eventTriggerName")
    def event_trigger_name(self) -> builtins.str:
        '''The unique name of the event trigger.'''
        return typing.cast(builtins.str, jsii.get(self, "eventTriggerName"))

    @event_trigger_name.setter
    def event_trigger_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9a32cfee1a68445fea2fa917fb431b02536069883dc6c492094b36c48158d6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventTriggerName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="objectTypeName")
    def object_type_name(self) -> builtins.str:
        '''The unique name of the object type.'''
        return typing.cast(builtins.str, jsii.get(self, "objectTypeName"))

    @object_type_name.setter
    def object_type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26f048d7d34ef17a451ca6afc9c754cf23e5448d0fa70d08e95941b41a53e15b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectTypeName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the event trigger.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14f8e2b14eb300ec5bb3dbffd9fda2b1b3fa26a8ccb24220faf205a2c9252b16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="eventTriggerLimits")
    def event_trigger_limits(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEventTrigger.EventTriggerLimitsProperty"]]:
        '''Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEventTrigger.EventTriggerLimitsProperty"]], jsii.get(self, "eventTriggerLimits"))

    @event_trigger_limits.setter
    def event_trigger_limits(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEventTrigger.EventTriggerLimitsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8577e6b11fafc0b473494e772f42df4b3a275f14decae7f35bf35c8ceca6efbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventTriggerLimits", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="segmentFilter")
    def segment_filter(self) -> typing.Optional[builtins.str]:
        '''The destination is triggered only for profiles that meet the criteria of a segment definition.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "segmentFilter"))

    @segment_filter.setter
    def segment_filter(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ed3d132124c95676f8283662330dfc6f234432d197bcdb1846aeb9b55d6b31d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "segmentFilter", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0431604b79fa9f08ecdffc28b119f0c684057eb139cb8d0fcc9e51cc364ff34a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnEventTrigger.EventTriggerConditionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "event_trigger_dimensions": "eventTriggerDimensions",
            "logical_operator": "logicalOperator",
        },
    )
    class EventTriggerConditionProperty:
        def __init__(
            self,
            *,
            event_trigger_dimensions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEventTrigger.EventTriggerDimensionProperty", typing.Dict[builtins.str, typing.Any]]]]],
            logical_operator: builtins.str,
        ) -> None:
            '''Specifies the circumstances under which the event should trigger the destination.

            :param event_trigger_dimensions: A list of dimensions to be evaluated for the event.
            :param logical_operator: The operator used to combine multiple dimensions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-eventtriggercondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                event_trigger_condition_property = customerprofiles.CfnEventTrigger.EventTriggerConditionProperty(
                    event_trigger_dimensions=[customerprofiles.CfnEventTrigger.EventTriggerDimensionProperty(
                        object_attributes=[customerprofiles.CfnEventTrigger.ObjectAttributeProperty(
                            comparison_operator="comparisonOperator",
                            values=["values"],
                
                            # the properties below are optional
                            field_name="fieldName",
                            source="source"
                        )]
                    )],
                    logical_operator="logicalOperator"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__01622abde91c4f131120bde889e115bd6740e17b0e7e060628263c9607cf01d4)
                check_type(argname="argument event_trigger_dimensions", value=event_trigger_dimensions, expected_type=type_hints["event_trigger_dimensions"])
                check_type(argname="argument logical_operator", value=logical_operator, expected_type=type_hints["logical_operator"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "event_trigger_dimensions": event_trigger_dimensions,
                "logical_operator": logical_operator,
            }

        @builtins.property
        def event_trigger_dimensions(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventTrigger.EventTriggerDimensionProperty"]]]:
            '''A list of dimensions to be evaluated for the event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-eventtriggercondition.html#cfn-customerprofiles-eventtrigger-eventtriggercondition-eventtriggerdimensions
            '''
            result = self._values.get("event_trigger_dimensions")
            assert result is not None, "Required property 'event_trigger_dimensions' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventTrigger.EventTriggerDimensionProperty"]]], result)

        @builtins.property
        def logical_operator(self) -> builtins.str:
            '''The operator used to combine multiple dimensions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-eventtriggercondition.html#cfn-customerprofiles-eventtrigger-eventtriggercondition-logicaloperator
            '''
            result = self._values.get("logical_operator")
            assert result is not None, "Required property 'logical_operator' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventTriggerConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnEventTrigger.EventTriggerDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"object_attributes": "objectAttributes"},
    )
    class EventTriggerDimensionProperty:
        def __init__(
            self,
            *,
            object_attributes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEventTrigger.ObjectAttributeProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''A specific event dimension to be assessed.

            :param object_attributes: A list of object attributes to be evaluated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-eventtriggerdimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                event_trigger_dimension_property = customerprofiles.CfnEventTrigger.EventTriggerDimensionProperty(
                    object_attributes=[customerprofiles.CfnEventTrigger.ObjectAttributeProperty(
                        comparison_operator="comparisonOperator",
                        values=["values"],
                
                        # the properties below are optional
                        field_name="fieldName",
                        source="source"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__936befd5e0ecb3c45c2c47843a0cfa5dfc87acecf21c037978def245f15c99ff)
                check_type(argname="argument object_attributes", value=object_attributes, expected_type=type_hints["object_attributes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object_attributes": object_attributes,
            }

        @builtins.property
        def object_attributes(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventTrigger.ObjectAttributeProperty"]]]:
            '''A list of object attributes to be evaluated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-eventtriggerdimension.html#cfn-customerprofiles-eventtrigger-eventtriggerdimension-objectattributes
            '''
            result = self._values.get("object_attributes")
            assert result is not None, "Required property 'object_attributes' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventTrigger.ObjectAttributeProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventTriggerDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnEventTrigger.EventTriggerLimitsProperty",
        jsii_struct_bases=[],
        name_mapping={"event_expiration": "eventExpiration", "periods": "periods"},
    )
    class EventTriggerLimitsProperty:
        def __init__(
            self,
            *,
            event_expiration: typing.Optional[jsii.Number] = None,
            periods: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEventTrigger.PeriodProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.

            :param event_expiration: Specifies that an event will only trigger the destination if it is processed within a certain latency period.
            :param periods: A list of time periods during which the limits apply.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-eventtriggerlimits.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                event_trigger_limits_property = customerprofiles.CfnEventTrigger.EventTriggerLimitsProperty(
                    event_expiration=123,
                    periods=[customerprofiles.CfnEventTrigger.PeriodProperty(
                        unit="unit",
                        value=123,
                
                        # the properties below are optional
                        max_invocations_per_profile=123,
                        unlimited=False
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c21f9960dce43c4cfe6a915ec34c75b13089631bea9d3de70a87e7098384cb1d)
                check_type(argname="argument event_expiration", value=event_expiration, expected_type=type_hints["event_expiration"])
                check_type(argname="argument periods", value=periods, expected_type=type_hints["periods"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if event_expiration is not None:
                self._values["event_expiration"] = event_expiration
            if periods is not None:
                self._values["periods"] = periods

        @builtins.property
        def event_expiration(self) -> typing.Optional[jsii.Number]:
            '''Specifies that an event will only trigger the destination if it is processed within a certain latency period.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-eventtriggerlimits.html#cfn-customerprofiles-eventtrigger-eventtriggerlimits-eventexpiration
            '''
            result = self._values.get("event_expiration")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def periods(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventTrigger.PeriodProperty"]]]]:
            '''A list of time periods during which the limits apply.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-eventtriggerlimits.html#cfn-customerprofiles-eventtrigger-eventtriggerlimits-periods
            '''
            result = self._values.get("periods")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventTrigger.PeriodProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventTriggerLimitsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnEventTrigger.ObjectAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "values": "values",
            "field_name": "fieldName",
            "source": "source",
        },
    )
    class ObjectAttributeProperty:
        def __init__(
            self,
            *,
            comparison_operator: builtins.str,
            values: typing.Sequence[builtins.str],
            field_name: typing.Optional[builtins.str] = None,
            source: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The criteria that a specific object attribute must meet to trigger the destination.

            :param comparison_operator: The operator used to compare an attribute against a list of values.
            :param values: The amount of time of the specified unit.
            :param field_name: A field defined within an object type.
            :param source: An attribute contained within a source object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-objectattribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                object_attribute_property = customerprofiles.CfnEventTrigger.ObjectAttributeProperty(
                    comparison_operator="comparisonOperator",
                    values=["values"],
                
                    # the properties below are optional
                    field_name="fieldName",
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0a90a9f34cbabcbef830e52f532688120b085cb48e257f24a4658b7c9bbbcec)
                check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
                check_type(argname="argument field_name", value=field_name, expected_type=type_hints["field_name"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "comparison_operator": comparison_operator,
                "values": values,
            }
            if field_name is not None:
                self._values["field_name"] = field_name
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def comparison_operator(self) -> builtins.str:
            '''The operator used to compare an attribute against a list of values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-objectattribute.html#cfn-customerprofiles-eventtrigger-objectattribute-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            assert result is not None, "Required property 'comparison_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''The amount of time of the specified unit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-objectattribute.html#cfn-customerprofiles-eventtrigger-objectattribute-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def field_name(self) -> typing.Optional[builtins.str]:
            '''A field defined within an object type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-objectattribute.html#cfn-customerprofiles-eventtrigger-objectattribute-fieldname
            '''
            result = self._values.get("field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''An attribute contained within a source object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-objectattribute.html#cfn-customerprofiles-eventtrigger-objectattribute-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObjectAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnEventTrigger.PeriodProperty",
        jsii_struct_bases=[],
        name_mapping={
            "unit": "unit",
            "value": "value",
            "max_invocations_per_profile": "maxInvocationsPerProfile",
            "unlimited": "unlimited",
        },
    )
    class PeriodProperty:
        def __init__(
            self,
            *,
            unit: builtins.str,
            value: jsii.Number,
            max_invocations_per_profile: typing.Optional[jsii.Number] = None,
            unlimited: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Defines a limit and the time period during which it is enforced.

            :param unit: The unit of time.
            :param value: The amount of time of the specified unit.
            :param max_invocations_per_profile: The maximum allowed number of destination invocations per profile.
            :param unlimited: If set to true, there is no limit on the number of destination invocations per profile. The default is false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-period.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                period_property = customerprofiles.CfnEventTrigger.PeriodProperty(
                    unit="unit",
                    value=123,
                
                    # the properties below are optional
                    max_invocations_per_profile=123,
                    unlimited=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__779555dd66a387de3220544cdb9e3846de45bce3e7a1615f8f0ecb0e783adbe9)
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument max_invocations_per_profile", value=max_invocations_per_profile, expected_type=type_hints["max_invocations_per_profile"])
                check_type(argname="argument unlimited", value=unlimited, expected_type=type_hints["unlimited"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "unit": unit,
                "value": value,
            }
            if max_invocations_per_profile is not None:
                self._values["max_invocations_per_profile"] = max_invocations_per_profile
            if unlimited is not None:
                self._values["unlimited"] = unlimited

        @builtins.property
        def unit(self) -> builtins.str:
            '''The unit of time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-period.html#cfn-customerprofiles-eventtrigger-period-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''The amount of time of the specified unit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-period.html#cfn-customerprofiles-eventtrigger-period-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max_invocations_per_profile(self) -> typing.Optional[jsii.Number]:
            '''The maximum allowed number of destination invocations per profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-period.html#cfn-customerprofiles-eventtrigger-period-maxinvocationsperprofile
            '''
            result = self._values.get("max_invocations_per_profile")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unlimited(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If set to true, there is no limit on the number of destination invocations per profile.

            The default is false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-eventtrigger-period.html#cfn-customerprofiles-eventtrigger-period-unlimited
            '''
            result = self._values.get("unlimited")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnEventTriggerProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "event_trigger_conditions": "eventTriggerConditions",
        "event_trigger_name": "eventTriggerName",
        "object_type_name": "objectTypeName",
        "description": "description",
        "event_trigger_limits": "eventTriggerLimits",
        "segment_filter": "segmentFilter",
        "tags": "tags",
    },
)
class CfnEventTriggerProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        event_trigger_conditions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventTrigger.EventTriggerConditionProperty, typing.Dict[builtins.str, typing.Any]]]]],
        event_trigger_name: builtins.str,
        object_type_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        event_trigger_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventTrigger.EventTriggerLimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        segment_filter: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEventTrigger``.

        :param domain_name: The unique name of the domain.
        :param event_trigger_conditions: A list of conditions that determine when an event should trigger the destination.
        :param event_trigger_name: The unique name of the event trigger.
        :param object_type_name: The unique name of the object type.
        :param description: The description of the event trigger.
        :param event_trigger_limits: Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.
        :param segment_filter: The destination is triggered only for profiles that meet the criteria of a segment definition.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventtrigger.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_customerprofiles as customerprofiles
            
            cfn_event_trigger_props = customerprofiles.CfnEventTriggerProps(
                domain_name="domainName",
                event_trigger_conditions=[customerprofiles.CfnEventTrigger.EventTriggerConditionProperty(
                    event_trigger_dimensions=[customerprofiles.CfnEventTrigger.EventTriggerDimensionProperty(
                        object_attributes=[customerprofiles.CfnEventTrigger.ObjectAttributeProperty(
                            comparison_operator="comparisonOperator",
                            values=["values"],
            
                            # the properties below are optional
                            field_name="fieldName",
                            source="source"
                        )]
                    )],
                    logical_operator="logicalOperator"
                )],
                event_trigger_name="eventTriggerName",
                object_type_name="objectTypeName",
            
                # the properties below are optional
                description="description",
                event_trigger_limits=customerprofiles.CfnEventTrigger.EventTriggerLimitsProperty(
                    event_expiration=123,
                    periods=[customerprofiles.CfnEventTrigger.PeriodProperty(
                        unit="unit",
                        value=123,
            
                        # the properties below are optional
                        max_invocations_per_profile=123,
                        unlimited=False
                    )]
                ),
                segment_filter="segmentFilter",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9d2b6147273c603d09e90db3d8372049e484840bcff7a8dc8031fd2f0e0e756)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument event_trigger_conditions", value=event_trigger_conditions, expected_type=type_hints["event_trigger_conditions"])
            check_type(argname="argument event_trigger_name", value=event_trigger_name, expected_type=type_hints["event_trigger_name"])
            check_type(argname="argument object_type_name", value=object_type_name, expected_type=type_hints["object_type_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument event_trigger_limits", value=event_trigger_limits, expected_type=type_hints["event_trigger_limits"])
            check_type(argname="argument segment_filter", value=segment_filter, expected_type=type_hints["segment_filter"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "event_trigger_conditions": event_trigger_conditions,
            "event_trigger_name": event_trigger_name,
            "object_type_name": object_type_name,
        }
        if description is not None:
            self._values["description"] = description
        if event_trigger_limits is not None:
            self._values["event_trigger_limits"] = event_trigger_limits
        if segment_filter is not None:
            self._values["segment_filter"] = segment_filter
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventtrigger.html#cfn-customerprofiles-eventtrigger-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_trigger_conditions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventTrigger.EventTriggerConditionProperty]]]:
        '''A list of conditions that determine when an event should trigger the destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventtrigger.html#cfn-customerprofiles-eventtrigger-eventtriggerconditions
        '''
        result = self._values.get("event_trigger_conditions")
        assert result is not None, "Required property 'event_trigger_conditions' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventTrigger.EventTriggerConditionProperty]]], result)

    @builtins.property
    def event_trigger_name(self) -> builtins.str:
        '''The unique name of the event trigger.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventtrigger.html#cfn-customerprofiles-eventtrigger-eventtriggername
        '''
        result = self._values.get("event_trigger_name")
        assert result is not None, "Required property 'event_trigger_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_type_name(self) -> builtins.str:
        '''The unique name of the object type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventtrigger.html#cfn-customerprofiles-eventtrigger-objecttypename
        '''
        result = self._values.get("object_type_name")
        assert result is not None, "Required property 'object_type_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the event trigger.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventtrigger.html#cfn-customerprofiles-eventtrigger-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_trigger_limits(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEventTrigger.EventTriggerLimitsProperty]]:
        '''Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventtrigger.html#cfn-customerprofiles-eventtrigger-eventtriggerlimits
        '''
        result = self._values.get("event_trigger_limits")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEventTrigger.EventTriggerLimitsProperty]], result)

    @builtins.property
    def segment_filter(self) -> typing.Optional[builtins.str]:
        '''The destination is triggered only for profiles that meet the criteria of a segment definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventtrigger.html#cfn-customerprofiles-eventtrigger-segmentfilter
        '''
        result = self._values.get("segment_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-eventtrigger.html#cfn-customerprofiles-eventtrigger-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventTriggerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnIntegration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration",
):
    '''Specifies an Amazon Connect Customer Profiles Integration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html
    :cloudformationResource: AWS::CustomerProfiles::Integration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_customerprofiles as customerprofiles
        
        cfn_integration = customerprofiles.CfnIntegration(self, "MyCfnIntegration",
            domain_name="domainName",
        
            # the properties below are optional
            event_trigger_names=["eventTriggerNames"],
            flow_definition=customerprofiles.CfnIntegration.FlowDefinitionProperty(
                flow_name="flowName",
                kms_arn="kmsArn",
                source_flow_config=customerprofiles.CfnIntegration.SourceFlowConfigProperty(
                    connector_type="connectorType",
                    source_connector_properties=customerprofiles.CfnIntegration.SourceConnectorPropertiesProperty(
                        marketo=customerprofiles.CfnIntegration.MarketoSourcePropertiesProperty(
                            object="object"
                        ),
                        s3=customerprofiles.CfnIntegration.S3SourcePropertiesProperty(
                            bucket_name="bucketName",
        
                            # the properties below are optional
                            bucket_prefix="bucketPrefix"
                        ),
                        salesforce=customerprofiles.CfnIntegration.SalesforceSourcePropertiesProperty(
                            object="object",
        
                            # the properties below are optional
                            enable_dynamic_field_update=False,
                            include_deleted_records=False
                        ),
                        service_now=customerprofiles.CfnIntegration.ServiceNowSourcePropertiesProperty(
                            object="object"
                        ),
                        zendesk=customerprofiles.CfnIntegration.ZendeskSourcePropertiesProperty(
                            object="object"
                        )
                    ),
        
                    # the properties below are optional
                    connector_profile_name="connectorProfileName",
                    incremental_pull_config=customerprofiles.CfnIntegration.IncrementalPullConfigProperty(
                        datetime_type_field_name="datetimeTypeFieldName"
                    )
                ),
                tasks=[customerprofiles.CfnIntegration.TaskProperty(
                    source_fields=["sourceFields"],
                    task_type="taskType",
        
                    # the properties below are optional
                    connector_operator=customerprofiles.CfnIntegration.ConnectorOperatorProperty(
                        marketo="marketo",
                        s3="s3",
                        salesforce="salesforce",
                        service_now="serviceNow",
                        zendesk="zendesk"
                    ),
                    destination_field="destinationField",
                    task_properties=[customerprofiles.CfnIntegration.TaskPropertiesMapProperty(
                        operator_property_key="operatorPropertyKey",
                        property="property"
                    )]
                )],
                trigger_config=customerprofiles.CfnIntegration.TriggerConfigProperty(
                    trigger_type="triggerType",
        
                    # the properties below are optional
                    trigger_properties=customerprofiles.CfnIntegration.TriggerPropertiesProperty(
                        scheduled=customerprofiles.CfnIntegration.ScheduledTriggerPropertiesProperty(
                            schedule_expression="scheduleExpression",
        
                            # the properties below are optional
                            data_pull_mode="dataPullMode",
                            first_execution_from=123,
                            schedule_end_time=123,
                            schedule_offset=123,
                            schedule_start_time=123,
                            timezone="timezone"
                        )
                    )
                ),
        
                # the properties below are optional
                description="description"
            ),
            object_type_name="objectTypeName",
            object_type_names=[customerprofiles.CfnIntegration.ObjectTypeMappingProperty(
                key="key",
                value="value"
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            uri="uri"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        event_trigger_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        flow_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.FlowDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        object_type_name: typing.Optional[builtins.str] = None,
        object_type_names: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.ObjectTypeMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_name: The unique name of the domain.
        :param event_trigger_names: A list of unique names for active event triggers associated with the integration.
        :param flow_definition: The configuration that controls how Customer Profiles retrieves data from the source.
        :param object_type_name: The name of the profile object type mapping to use.
        :param object_type_names: The object type mapping.
        :param tags: The tags used to organize, track, or control access for this resource.
        :param uri: The URI of the S3 bucket or any other type of data source.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8211c08b95eabfe008b27ab5b3b74bab34f671b7bd9761e15cdb090da9d3d95)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIntegrationProps(
            domain_name=domain_name,
            event_trigger_names=event_trigger_names,
            flow_definition=flow_definition,
            object_type_name=object_type_name,
            object_type_names=object_type_names,
            tags=tags,
            uri=uri,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85eb075da84dc570034fe72854e5f377beb9454784461fb242856b2b0d6db071)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a02b200ac7ef42474d61bef0afc23d2047a43211308a0f0f346c8804318a953d)
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
        '''The timestamp of when the integration was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The timestamp of when the integration was most recently edited.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

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
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d13bac4a06b95e4fadaf50aaed39e2383120484f2d6e868a652119e3c0741a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="eventTriggerNames")
    def event_trigger_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of unique names for active event triggers associated with the integration.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventTriggerNames"))

    @event_trigger_names.setter
    def event_trigger_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2353defad4ed0b7f19993fda09b6c2619751d1fb77397c9b4957634b704a6fba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventTriggerNames", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowDefinition")
    def flow_definition(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.FlowDefinitionProperty"]]:
        '''The configuration that controls how Customer Profiles retrieves data from the source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.FlowDefinitionProperty"]], jsii.get(self, "flowDefinition"))

    @flow_definition.setter
    def flow_definition(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.FlowDefinitionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eda84696baed289de5f577073d9697fd7b0969af55567086ad86e6466b533e14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowDefinition", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="objectTypeName")
    def object_type_name(self) -> typing.Optional[builtins.str]:
        '''The name of the profile object type mapping to use.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectTypeName"))

    @object_type_name.setter
    def object_type_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ac4be2e5060d6806d086adb14efc1af2df364f07423ea56e6af2958c23fc2b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectTypeName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="objectTypeNames")
    def object_type_names(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ObjectTypeMappingProperty"]]]]:
        '''The object type mapping.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ObjectTypeMappingProperty"]]]], jsii.get(self, "objectTypeNames"))

    @object_type_names.setter
    def object_type_names(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ObjectTypeMappingProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d19e3d184d030db553288fb9b5bf060b201c3b429358e9c4818b39453b44a060)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectTypeNames", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55efe13391c8b01dcc8a4fc8cdb64b30e0590e3c2de5fbdfaf88656f9ad1a18e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> typing.Optional[builtins.str]:
        '''The URI of the S3 bucket or any other type of data source.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02e9de6347e213a96d6d3dc4870b6c07c7e7db9b8044cff9f9952e0192a795c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.ConnectorOperatorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "marketo": "marketo",
            "s3": "s3",
            "salesforce": "salesforce",
            "service_now": "serviceNow",
            "zendesk": "zendesk",
        },
    )
    class ConnectorOperatorProperty:
        def __init__(
            self,
            *,
            marketo: typing.Optional[builtins.str] = None,
            s3: typing.Optional[builtins.str] = None,
            salesforce: typing.Optional[builtins.str] = None,
            service_now: typing.Optional[builtins.str] = None,
            zendesk: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The operation to be performed on the provided source fields.

            :param marketo: The operation to be performed on the provided Marketo source fields.
            :param s3: The operation to be performed on the provided Amazon S3 source fields.
            :param salesforce: The operation to be performed on the provided Salesforce source fields.
            :param service_now: The operation to be performed on the provided ServiceNow source fields.
            :param zendesk: The operation to be performed on the provided Zendesk source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                connector_operator_property = customerprofiles.CfnIntegration.ConnectorOperatorProperty(
                    marketo="marketo",
                    s3="s3",
                    salesforce="salesforce",
                    service_now="serviceNow",
                    zendesk="zendesk"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d8ff575fc6d67c92e33f52c9a2a9924dd1914b3ec97eb67ea19a5f83109dfe09)
                check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
                check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
                check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
                check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if marketo is not None:
                self._values["marketo"] = marketo
            if s3 is not None:
                self._values["s3"] = s3
            if salesforce is not None:
                self._values["salesforce"] = salesforce
            if service_now is not None:
                self._values["service_now"] = service_now
            if zendesk is not None:
                self._values["zendesk"] = zendesk

        @builtins.property
        def marketo(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Marketo source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-marketo
            '''
            result = self._values.get("marketo")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Amazon S3 source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def salesforce(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Salesforce source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-salesforce
            '''
            result = self._values.get("salesforce")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_now(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided ServiceNow source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-servicenow
            '''
            result = self._values.get("service_now")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def zendesk(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Zendesk source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-connectoroperator.html#cfn-customerprofiles-integration-connectoroperator-zendesk
            '''
            result = self._values.get("zendesk")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectorOperatorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.FlowDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "flow_name": "flowName",
            "kms_arn": "kmsArn",
            "source_flow_config": "sourceFlowConfig",
            "tasks": "tasks",
            "trigger_config": "triggerConfig",
            "description": "description",
        },
    )
    class FlowDefinitionProperty:
        def __init__(
            self,
            *,
            flow_name: builtins.str,
            kms_arn: builtins.str,
            source_flow_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.SourceFlowConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            tasks: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.TaskProperty", typing.Dict[builtins.str, typing.Any]]]]],
            trigger_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.TriggerConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configurations that control how Customer Profiles retrieves data from the source, Amazon AppFlow.

            Customer Profiles uses this information to create an AppFlow flow on behalf of customers.

            :param flow_name: The specified name of the flow. Use underscores (_) or hyphens (-) only. Spaces are not allowed.
            :param kms_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key you provide for encryption.
            :param source_flow_config: The configuration that controls how Customer Profiles retrieves data from the source.
            :param tasks: A list of tasks that Customer Profiles performs while transferring the data in the flow run.
            :param trigger_config: The trigger settings that determine how and when the flow runs.
            :param description: A description of the flow you want to create.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                flow_definition_property = customerprofiles.CfnIntegration.FlowDefinitionProperty(
                    flow_name="flowName",
                    kms_arn="kmsArn",
                    source_flow_config=customerprofiles.CfnIntegration.SourceFlowConfigProperty(
                        connector_type="connectorType",
                        source_connector_properties=customerprofiles.CfnIntegration.SourceConnectorPropertiesProperty(
                            marketo=customerprofiles.CfnIntegration.MarketoSourcePropertiesProperty(
                                object="object"
                            ),
                            s3=customerprofiles.CfnIntegration.S3SourcePropertiesProperty(
                                bucket_name="bucketName",
                
                                # the properties below are optional
                                bucket_prefix="bucketPrefix"
                            ),
                            salesforce=customerprofiles.CfnIntegration.SalesforceSourcePropertiesProperty(
                                object="object",
                
                                # the properties below are optional
                                enable_dynamic_field_update=False,
                                include_deleted_records=False
                            ),
                            service_now=customerprofiles.CfnIntegration.ServiceNowSourcePropertiesProperty(
                                object="object"
                            ),
                            zendesk=customerprofiles.CfnIntegration.ZendeskSourcePropertiesProperty(
                                object="object"
                            )
                        ),
                
                        # the properties below are optional
                        connector_profile_name="connectorProfileName",
                        incremental_pull_config=customerprofiles.CfnIntegration.IncrementalPullConfigProperty(
                            datetime_type_field_name="datetimeTypeFieldName"
                        )
                    ),
                    tasks=[customerprofiles.CfnIntegration.TaskProperty(
                        source_fields=["sourceFields"],
                        task_type="taskType",
                
                        # the properties below are optional
                        connector_operator=customerprofiles.CfnIntegration.ConnectorOperatorProperty(
                            marketo="marketo",
                            s3="s3",
                            salesforce="salesforce",
                            service_now="serviceNow",
                            zendesk="zendesk"
                        ),
                        destination_field="destinationField",
                        task_properties=[customerprofiles.CfnIntegration.TaskPropertiesMapProperty(
                            operator_property_key="operatorPropertyKey",
                            property="property"
                        )]
                    )],
                    trigger_config=customerprofiles.CfnIntegration.TriggerConfigProperty(
                        trigger_type="triggerType",
                
                        # the properties below are optional
                        trigger_properties=customerprofiles.CfnIntegration.TriggerPropertiesProperty(
                            scheduled=customerprofiles.CfnIntegration.ScheduledTriggerPropertiesProperty(
                                schedule_expression="scheduleExpression",
                
                                # the properties below are optional
                                data_pull_mode="dataPullMode",
                                first_execution_from=123,
                                schedule_end_time=123,
                                schedule_offset=123,
                                schedule_start_time=123,
                                timezone="timezone"
                            )
                        )
                    ),
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__684e26c18461ba90c60337c4f41ecfe0fff4d6e92e5f5ccc4fca2dbb9cb7fe58)
                check_type(argname="argument flow_name", value=flow_name, expected_type=type_hints["flow_name"])
                check_type(argname="argument kms_arn", value=kms_arn, expected_type=type_hints["kms_arn"])
                check_type(argname="argument source_flow_config", value=source_flow_config, expected_type=type_hints["source_flow_config"])
                check_type(argname="argument tasks", value=tasks, expected_type=type_hints["tasks"])
                check_type(argname="argument trigger_config", value=trigger_config, expected_type=type_hints["trigger_config"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "flow_name": flow_name,
                "kms_arn": kms_arn,
                "source_flow_config": source_flow_config,
                "tasks": tasks,
                "trigger_config": trigger_config,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def flow_name(self) -> builtins.str:
            '''The specified name of the flow.

            Use underscores (_) or hyphens (-) only. Spaces are not allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-flowname
            '''
            result = self._values.get("flow_name")
            assert result is not None, "Required property 'flow_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key you provide for encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-kmsarn
            '''
            result = self._values.get("kms_arn")
            assert result is not None, "Required property 'kms_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_flow_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnIntegration.SourceFlowConfigProperty"]:
            '''The configuration that controls how Customer Profiles retrieves data from the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-sourceflowconfig
            '''
            result = self._values.get("source_flow_config")
            assert result is not None, "Required property 'source_flow_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnIntegration.SourceFlowConfigProperty"], result)

        @builtins.property
        def tasks(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.TaskProperty"]]]:
            '''A list of tasks that Customer Profiles performs while transferring the data in the flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-tasks
            '''
            result = self._values.get("tasks")
            assert result is not None, "Required property 'tasks' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.TaskProperty"]]], result)

        @builtins.property
        def trigger_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnIntegration.TriggerConfigProperty"]:
            '''The trigger settings that determine how and when the flow runs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-triggerconfig
            '''
            result = self._values.get("trigger_config")
            assert result is not None, "Required property 'trigger_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnIntegration.TriggerConfigProperty"], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of the flow you want to create.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-flowdefinition.html#cfn-customerprofiles-integration-flowdefinition-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlowDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.IncrementalPullConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"datetime_type_field_name": "datetimeTypeFieldName"},
    )
    class IncrementalPullConfigProperty:
        def __init__(
            self,
            *,
            datetime_type_field_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the configuration used when importing incremental records from the source.

            :param datetime_type_field_name: A field that specifies the date time or timestamp field as the criteria to use when importing incremental records from the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-incrementalpullconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                incremental_pull_config_property = customerprofiles.CfnIntegration.IncrementalPullConfigProperty(
                    datetime_type_field_name="datetimeTypeFieldName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b30373edbc1fc87d87c0305c0d579d9085e768165db2968c37ebc100141fc94c)
                check_type(argname="argument datetime_type_field_name", value=datetime_type_field_name, expected_type=type_hints["datetime_type_field_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if datetime_type_field_name is not None:
                self._values["datetime_type_field_name"] = datetime_type_field_name

        @builtins.property
        def datetime_type_field_name(self) -> typing.Optional[builtins.str]:
            '''A field that specifies the date time or timestamp field as the criteria to use when importing incremental records from the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-incrementalpullconfig.html#cfn-customerprofiles-integration-incrementalpullconfig-datetimetypefieldname
            '''
            result = self._values.get("datetime_type_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IncrementalPullConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.MarketoSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class MarketoSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when Marketo is being used as a source.

            :param object: The object specified in the Marketo flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-marketosourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                marketo_source_properties_property = customerprofiles.CfnIntegration.MarketoSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3a60c86877c43b5afd59790a18d6019039ccc87b2d8b8b5c9299157eda159890)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Marketo flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-marketosourceproperties.html#cfn-customerprofiles-integration-marketosourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MarketoSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.ObjectTypeMappingProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ObjectTypeMappingProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''A map in which each key is an event type from an external application such as Segment or Shopify, and each value is an ``ObjectTypeName`` (template) used to ingest the event.

            :param key: The key.
            :param value: The value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-objecttypemapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                object_type_mapping_property = customerprofiles.CfnIntegration.ObjectTypeMappingProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d9afb6e6e9868c0b8b44a3a96fec8e43830e8a548405844dbf1d5a8d81ced10d)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-objecttypemapping.html#cfn-customerprofiles-integration-objecttypemapping-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-objecttypemapping.html#cfn-customerprofiles-integration-objecttypemapping-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObjectTypeMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.S3SourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName", "bucket_prefix": "bucketPrefix"},
    )
    class S3SourcePropertiesProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            bucket_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The properties that are applied when Amazon S3 is being used as the flow source.

            :param bucket_name: The Amazon S3 bucket name where the source files are stored.
            :param bucket_prefix: The object key for the Amazon S3 bucket in which the source files are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                s3_source_properties_property = customerprofiles.CfnIntegration.S3SourcePropertiesProperty(
                    bucket_name="bucketName",
                
                    # the properties below are optional
                    bucket_prefix="bucketPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a79daf2a1599613c0d4820e23ade3e1ab729e048f4f33e5e1ca2c56d56a3757b)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
            }
            if bucket_prefix is not None:
                self._values["bucket_prefix"] = bucket_prefix

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The Amazon S3 bucket name where the source files are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html#cfn-customerprofiles-integration-s3sourceproperties-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_prefix(self) -> typing.Optional[builtins.str]:
            '''The object key for the Amazon S3 bucket in which the source files are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-s3sourceproperties.html#cfn-customerprofiles-integration-s3sourceproperties-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3SourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.SalesforceSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "object": "object",
            "enable_dynamic_field_update": "enableDynamicFieldUpdate",
            "include_deleted_records": "includeDeletedRecords",
        },
    )
    class SalesforceSourcePropertiesProperty:
        def __init__(
            self,
            *,
            object: builtins.str,
            enable_dynamic_field_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_deleted_records: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The properties that are applied when Salesforce is being used as a source.

            :param object: The object specified in the Salesforce flow source.
            :param enable_dynamic_field_update: The flag that enables dynamic fetching of new (recently added) fields in the Salesforce objects while running a flow.
            :param include_deleted_records: Indicates whether Amazon AppFlow includes deleted files in the flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                salesforce_source_properties_property = customerprofiles.CfnIntegration.SalesforceSourcePropertiesProperty(
                    object="object",
                
                    # the properties below are optional
                    enable_dynamic_field_update=False,
                    include_deleted_records=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__48d96167457187d54618dd4839b1f9086125a2307ec481de96e070635baf5c77)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
                check_type(argname="argument enable_dynamic_field_update", value=enable_dynamic_field_update, expected_type=type_hints["enable_dynamic_field_update"])
                check_type(argname="argument include_deleted_records", value=include_deleted_records, expected_type=type_hints["include_deleted_records"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }
            if enable_dynamic_field_update is not None:
                self._values["enable_dynamic_field_update"] = enable_dynamic_field_update
            if include_deleted_records is not None:
                self._values["include_deleted_records"] = include_deleted_records

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Salesforce flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def enable_dynamic_field_update(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The flag that enables dynamic fetching of new (recently added) fields in the Salesforce objects while running a flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-enabledynamicfieldupdate
            '''
            result = self._values.get("enable_dynamic_field_update")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_deleted_records(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether Amazon AppFlow includes deleted files in the flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-salesforcesourceproperties.html#cfn-customerprofiles-integration-salesforcesourceproperties-includedeletedrecords
            '''
            result = self._values.get("include_deleted_records")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.ScheduledTriggerPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "schedule_expression": "scheduleExpression",
            "data_pull_mode": "dataPullMode",
            "first_execution_from": "firstExecutionFrom",
            "schedule_end_time": "scheduleEndTime",
            "schedule_offset": "scheduleOffset",
            "schedule_start_time": "scheduleStartTime",
            "timezone": "timezone",
        },
    )
    class ScheduledTriggerPropertiesProperty:
        def __init__(
            self,
            *,
            schedule_expression: builtins.str,
            data_pull_mode: typing.Optional[builtins.str] = None,
            first_execution_from: typing.Optional[jsii.Number] = None,
            schedule_end_time: typing.Optional[jsii.Number] = None,
            schedule_offset: typing.Optional[jsii.Number] = None,
            schedule_start_time: typing.Optional[jsii.Number] = None,
            timezone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the configuration details of a scheduled-trigger flow that you define.

            Currently, these settings only apply to the scheduled-trigger type.

            :param schedule_expression: The scheduling expression that determines the rate at which the schedule will run, for example rate (5 minutes).
            :param data_pull_mode: Specifies whether a scheduled flow has an incremental data transfer or a complete data transfer for each flow run.
            :param first_execution_from: Specifies the date range for the records to import from the connector in the first flow run.
            :param schedule_end_time: Specifies the scheduled end time for a scheduled-trigger flow.
            :param schedule_offset: Specifies the optional offset that is added to the time interval for a schedule-triggered flow.
            :param schedule_start_time: Specifies the scheduled start time for a scheduled-trigger flow. The value must be a date/time value in EPOCH format.
            :param timezone: Specifies the time zone used when referring to the date and time of a scheduled-triggered flow, such as America/New_York.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                scheduled_trigger_properties_property = customerprofiles.CfnIntegration.ScheduledTriggerPropertiesProperty(
                    schedule_expression="scheduleExpression",
                
                    # the properties below are optional
                    data_pull_mode="dataPullMode",
                    first_execution_from=123,
                    schedule_end_time=123,
                    schedule_offset=123,
                    schedule_start_time=123,
                    timezone="timezone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0e5944d396eaa65c18b0b184d20b092353bd232b3071af67d1f4668a3a6cb830)
                check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
                check_type(argname="argument data_pull_mode", value=data_pull_mode, expected_type=type_hints["data_pull_mode"])
                check_type(argname="argument first_execution_from", value=first_execution_from, expected_type=type_hints["first_execution_from"])
                check_type(argname="argument schedule_end_time", value=schedule_end_time, expected_type=type_hints["schedule_end_time"])
                check_type(argname="argument schedule_offset", value=schedule_offset, expected_type=type_hints["schedule_offset"])
                check_type(argname="argument schedule_start_time", value=schedule_start_time, expected_type=type_hints["schedule_start_time"])
                check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "schedule_expression": schedule_expression,
            }
            if data_pull_mode is not None:
                self._values["data_pull_mode"] = data_pull_mode
            if first_execution_from is not None:
                self._values["first_execution_from"] = first_execution_from
            if schedule_end_time is not None:
                self._values["schedule_end_time"] = schedule_end_time
            if schedule_offset is not None:
                self._values["schedule_offset"] = schedule_offset
            if schedule_start_time is not None:
                self._values["schedule_start_time"] = schedule_start_time
            if timezone is not None:
                self._values["timezone"] = timezone

        @builtins.property
        def schedule_expression(self) -> builtins.str:
            '''The scheduling expression that determines the rate at which the schedule will run, for example rate (5 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            assert result is not None, "Required property 'schedule_expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data_pull_mode(self) -> typing.Optional[builtins.str]:
            '''Specifies whether a scheduled flow has an incremental data transfer or a complete data transfer for each flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-datapullmode
            '''
            result = self._values.get("data_pull_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def first_execution_from(self) -> typing.Optional[jsii.Number]:
            '''Specifies the date range for the records to import from the connector in the first flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-firstexecutionfrom
            '''
            result = self._values.get("first_execution_from")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def schedule_end_time(self) -> typing.Optional[jsii.Number]:
            '''Specifies the scheduled end time for a scheduled-trigger flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleendtime
            '''
            result = self._values.get("schedule_end_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def schedule_offset(self) -> typing.Optional[jsii.Number]:
            '''Specifies the optional offset that is added to the time interval for a schedule-triggered flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-scheduleoffset
            '''
            result = self._values.get("schedule_offset")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def schedule_start_time(self) -> typing.Optional[jsii.Number]:
            '''Specifies the scheduled start time for a scheduled-trigger flow.

            The value must be a date/time value in EPOCH format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-schedulestarttime
            '''
            result = self._values.get("schedule_start_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timezone(self) -> typing.Optional[builtins.str]:
            '''Specifies the time zone used when referring to the date and time of a scheduled-triggered flow, such as America/New_York.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-scheduledtriggerproperties.html#cfn-customerprofiles-integration-scheduledtriggerproperties-timezone
            '''
            result = self._values.get("timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduledTriggerPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.ServiceNowSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class ServiceNowSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when ServiceNow is being used as a source.

            :param object: The object specified in the ServiceNow flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-servicenowsourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                service_now_source_properties_property = customerprofiles.CfnIntegration.ServiceNowSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0e39d4ec6bb5656a7c82bcb644c1e71ed86635052e302daedb141f92c9338d5e)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the ServiceNow flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-servicenowsourceproperties.html#cfn-customerprofiles-integration-servicenowsourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceNowSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.SourceConnectorPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "marketo": "marketo",
            "s3": "s3",
            "salesforce": "salesforce",
            "service_now": "serviceNow",
            "zendesk": "zendesk",
        },
    )
    class SourceConnectorPropertiesProperty:
        def __init__(
            self,
            *,
            marketo: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.MarketoSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.S3SourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            salesforce: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.SalesforceSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_now: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.ServiceNowSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            zendesk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.ZendeskSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the information that is required to query a particular Amazon AppFlow connector.

            Customer Profiles supports Salesforce, Zendesk, Marketo, ServiceNow and Amazon S3.

            :param marketo: The properties that are applied when Marketo is being used as a source.
            :param s3: The properties that are applied when Amazon S3 is being used as the flow source.
            :param salesforce: The properties that are applied when Salesforce is being used as a source.
            :param service_now: The properties that are applied when ServiceNow is being used as a source.
            :param zendesk: The properties that are applied when using Zendesk as a flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                source_connector_properties_property = customerprofiles.CfnIntegration.SourceConnectorPropertiesProperty(
                    marketo=customerprofiles.CfnIntegration.MarketoSourcePropertiesProperty(
                        object="object"
                    ),
                    s3=customerprofiles.CfnIntegration.S3SourcePropertiesProperty(
                        bucket_name="bucketName",
                
                        # the properties below are optional
                        bucket_prefix="bucketPrefix"
                    ),
                    salesforce=customerprofiles.CfnIntegration.SalesforceSourcePropertiesProperty(
                        object="object",
                
                        # the properties below are optional
                        enable_dynamic_field_update=False,
                        include_deleted_records=False
                    ),
                    service_now=customerprofiles.CfnIntegration.ServiceNowSourcePropertiesProperty(
                        object="object"
                    ),
                    zendesk=customerprofiles.CfnIntegration.ZendeskSourcePropertiesProperty(
                        object="object"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__886a4a6c1d593aa53fe13ccd79b82bf91be008e3952bb987ac48d2b64b7a6ac9)
                check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
                check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
                check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
                check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if marketo is not None:
                self._values["marketo"] = marketo
            if s3 is not None:
                self._values["s3"] = s3
            if salesforce is not None:
                self._values["salesforce"] = salesforce
            if service_now is not None:
                self._values["service_now"] = service_now
            if zendesk is not None:
                self._values["zendesk"] = zendesk

        @builtins.property
        def marketo(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.MarketoSourcePropertiesProperty"]]:
            '''The properties that are applied when Marketo is being used as a source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-marketo
            '''
            result = self._values.get("marketo")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.MarketoSourcePropertiesProperty"]], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.S3SourcePropertiesProperty"]]:
            '''The properties that are applied when Amazon S3 is being used as the flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.S3SourcePropertiesProperty"]], result)

        @builtins.property
        def salesforce(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.SalesforceSourcePropertiesProperty"]]:
            '''The properties that are applied when Salesforce is being used as a source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-salesforce
            '''
            result = self._values.get("salesforce")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.SalesforceSourcePropertiesProperty"]], result)

        @builtins.property
        def service_now(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ServiceNowSourcePropertiesProperty"]]:
            '''The properties that are applied when ServiceNow is being used as a source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-servicenow
            '''
            result = self._values.get("service_now")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ServiceNowSourcePropertiesProperty"]], result)

        @builtins.property
        def zendesk(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ZendeskSourcePropertiesProperty"]]:
            '''The properties that are applied when using Zendesk as a flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceconnectorproperties.html#cfn-customerprofiles-integration-sourceconnectorproperties-zendesk
            '''
            result = self._values.get("zendesk")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ZendeskSourcePropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceConnectorPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.SourceFlowConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connector_type": "connectorType",
            "source_connector_properties": "sourceConnectorProperties",
            "connector_profile_name": "connectorProfileName",
            "incremental_pull_config": "incrementalPullConfig",
        },
    )
    class SourceFlowConfigProperty:
        def __init__(
            self,
            *,
            connector_type: builtins.str,
            source_connector_properties: typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.SourceConnectorPropertiesProperty", typing.Dict[builtins.str, typing.Any]]],
            connector_profile_name: typing.Optional[builtins.str] = None,
            incremental_pull_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.IncrementalPullConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration that controls how Customer Profiles retrieves data from the source.

            :param connector_type: The type of connector, such as Salesforce, Marketo, and so on.
            :param source_connector_properties: Specifies the information that is required to query a particular source connector.
            :param connector_profile_name: The name of the Amazon AppFlow connector profile. This name must be unique for each connector profile in the AWS account .
            :param incremental_pull_config: Defines the configuration for a scheduled incremental data pull. If a valid configuration is provided, the fields specified in the configuration are used when querying for the incremental data pull.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                source_flow_config_property = customerprofiles.CfnIntegration.SourceFlowConfigProperty(
                    connector_type="connectorType",
                    source_connector_properties=customerprofiles.CfnIntegration.SourceConnectorPropertiesProperty(
                        marketo=customerprofiles.CfnIntegration.MarketoSourcePropertiesProperty(
                            object="object"
                        ),
                        s3=customerprofiles.CfnIntegration.S3SourcePropertiesProperty(
                            bucket_name="bucketName",
                
                            # the properties below are optional
                            bucket_prefix="bucketPrefix"
                        ),
                        salesforce=customerprofiles.CfnIntegration.SalesforceSourcePropertiesProperty(
                            object="object",
                
                            # the properties below are optional
                            enable_dynamic_field_update=False,
                            include_deleted_records=False
                        ),
                        service_now=customerprofiles.CfnIntegration.ServiceNowSourcePropertiesProperty(
                            object="object"
                        ),
                        zendesk=customerprofiles.CfnIntegration.ZendeskSourcePropertiesProperty(
                            object="object"
                        )
                    ),
                
                    # the properties below are optional
                    connector_profile_name="connectorProfileName",
                    incremental_pull_config=customerprofiles.CfnIntegration.IncrementalPullConfigProperty(
                        datetime_type_field_name="datetimeTypeFieldName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__55d9871f7bd0e95109d517268a1cdd0da37965b7b7acd24cb1bfd91cacda7d2f)
                check_type(argname="argument connector_type", value=connector_type, expected_type=type_hints["connector_type"])
                check_type(argname="argument source_connector_properties", value=source_connector_properties, expected_type=type_hints["source_connector_properties"])
                check_type(argname="argument connector_profile_name", value=connector_profile_name, expected_type=type_hints["connector_profile_name"])
                check_type(argname="argument incremental_pull_config", value=incremental_pull_config, expected_type=type_hints["incremental_pull_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connector_type": connector_type,
                "source_connector_properties": source_connector_properties,
            }
            if connector_profile_name is not None:
                self._values["connector_profile_name"] = connector_profile_name
            if incremental_pull_config is not None:
                self._values["incremental_pull_config"] = incremental_pull_config

        @builtins.property
        def connector_type(self) -> builtins.str:
            '''The type of connector, such as Salesforce, Marketo, and so on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-connectortype
            '''
            result = self._values.get("connector_type")
            assert result is not None, "Required property 'connector_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_connector_properties(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnIntegration.SourceConnectorPropertiesProperty"]:
            '''Specifies the information that is required to query a particular source connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-sourceconnectorproperties
            '''
            result = self._values.get("source_connector_properties")
            assert result is not None, "Required property 'source_connector_properties' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnIntegration.SourceConnectorPropertiesProperty"], result)

        @builtins.property
        def connector_profile_name(self) -> typing.Optional[builtins.str]:
            '''The name of the Amazon AppFlow connector profile.

            This name must be unique for each connector profile in the AWS account .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-connectorprofilename
            '''
            result = self._values.get("connector_profile_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def incremental_pull_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.IncrementalPullConfigProperty"]]:
            '''Defines the configuration for a scheduled incremental data pull.

            If a valid configuration is provided, the fields specified in the configuration are used when querying for the incremental data pull.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-sourceflowconfig.html#cfn-customerprofiles-integration-sourceflowconfig-incrementalpullconfig
            '''
            result = self._values.get("incremental_pull_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.IncrementalPullConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceFlowConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.TaskPropertiesMapProperty",
        jsii_struct_bases=[],
        name_mapping={
            "operator_property_key": "operatorPropertyKey",
            "property": "property",
        },
    )
    class TaskPropertiesMapProperty:
        def __init__(
            self,
            *,
            operator_property_key: builtins.str,
            property: builtins.str,
        ) -> None:
            '''A map used to store task-related information.

            The execution service looks for particular information based on the ``TaskType`` .

            :param operator_property_key: The task property key.
            :param property: The task property value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                task_properties_map_property = customerprofiles.CfnIntegration.TaskPropertiesMapProperty(
                    operator_property_key="operatorPropertyKey",
                    property="property"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a8a6d70493dcc8d57205e11e51993268d52dac180561f2ae05a6aa7eba5fab11)
                check_type(argname="argument operator_property_key", value=operator_property_key, expected_type=type_hints["operator_property_key"])
                check_type(argname="argument property", value=property, expected_type=type_hints["property"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "operator_property_key": operator_property_key,
                "property": property,
            }

        @builtins.property
        def operator_property_key(self) -> builtins.str:
            '''The task property key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html#cfn-customerprofiles-integration-taskpropertiesmap-operatorpropertykey
            '''
            result = self._values.get("operator_property_key")
            assert result is not None, "Required property 'operator_property_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def property(self) -> builtins.str:
            '''The task property value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-taskpropertiesmap.html#cfn-customerprofiles-integration-taskpropertiesmap-property
            '''
            result = self._values.get("property")
            assert result is not None, "Required property 'property' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskPropertiesMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.TaskProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_fields": "sourceFields",
            "task_type": "taskType",
            "connector_operator": "connectorOperator",
            "destination_field": "destinationField",
            "task_properties": "taskProperties",
        },
    )
    class TaskProperty:
        def __init__(
            self,
            *,
            source_fields: typing.Sequence[builtins.str],
            task_type: builtins.str,
            connector_operator: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.ConnectorOperatorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            destination_field: typing.Optional[builtins.str] = None,
            task_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.TaskPropertiesMapProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``Task`` property type specifies the class for modeling different type of tasks.

            Task implementation varies based on the TaskType.

            :param source_fields: The source fields to which a particular task is applied.
            :param task_type: Specifies the particular task implementation that Amazon AppFlow performs.
            :param connector_operator: The operation to be performed on the provided source fields.
            :param destination_field: A field in a destination connector, or a field value against which Amazon AppFlow validates a source field.
            :param task_properties: A map used to store task-related information. The service looks for particular information based on the TaskType.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                task_property = customerprofiles.CfnIntegration.TaskProperty(
                    source_fields=["sourceFields"],
                    task_type="taskType",
                
                    # the properties below are optional
                    connector_operator=customerprofiles.CfnIntegration.ConnectorOperatorProperty(
                        marketo="marketo",
                        s3="s3",
                        salesforce="salesforce",
                        service_now="serviceNow",
                        zendesk="zendesk"
                    ),
                    destination_field="destinationField",
                    task_properties=[customerprofiles.CfnIntegration.TaskPropertiesMapProperty(
                        operator_property_key="operatorPropertyKey",
                        property="property"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8c97356b1cf286df38ebed38c9f4ce8135e5160a1254e87e74e1baaba8f2149f)
                check_type(argname="argument source_fields", value=source_fields, expected_type=type_hints["source_fields"])
                check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
                check_type(argname="argument connector_operator", value=connector_operator, expected_type=type_hints["connector_operator"])
                check_type(argname="argument destination_field", value=destination_field, expected_type=type_hints["destination_field"])
                check_type(argname="argument task_properties", value=task_properties, expected_type=type_hints["task_properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source_fields": source_fields,
                "task_type": task_type,
            }
            if connector_operator is not None:
                self._values["connector_operator"] = connector_operator
            if destination_field is not None:
                self._values["destination_field"] = destination_field
            if task_properties is not None:
                self._values["task_properties"] = task_properties

        @builtins.property
        def source_fields(self) -> typing.List[builtins.str]:
            '''The source fields to which a particular task is applied.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-sourcefields
            '''
            result = self._values.get("source_fields")
            assert result is not None, "Required property 'source_fields' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def task_type(self) -> builtins.str:
            '''Specifies the particular task implementation that Amazon AppFlow performs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-tasktype
            '''
            result = self._values.get("task_type")
            assert result is not None, "Required property 'task_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def connector_operator(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ConnectorOperatorProperty"]]:
            '''The operation to be performed on the provided source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-connectoroperator
            '''
            result = self._values.get("connector_operator")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ConnectorOperatorProperty"]], result)

        @builtins.property
        def destination_field(self) -> typing.Optional[builtins.str]:
            '''A field in a destination connector, or a field value against which Amazon AppFlow validates a source field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-destinationfield
            '''
            result = self._values.get("destination_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def task_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.TaskPropertiesMapProperty"]]]]:
            '''A map used to store task-related information.

            The service looks for particular information based on the TaskType.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-task.html#cfn-customerprofiles-integration-task-taskproperties
            '''
            result = self._values.get("task_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.TaskPropertiesMapProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.TriggerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "trigger_type": "triggerType",
            "trigger_properties": "triggerProperties",
        },
    )
    class TriggerConfigProperty:
        def __init__(
            self,
            *,
            trigger_type: builtins.str,
            trigger_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.TriggerPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The trigger settings that determine how and when Amazon AppFlow runs the specified flow.

            :param trigger_type: Specifies the type of flow trigger. It can be OnDemand, Scheduled, or Event.
            :param trigger_properties: Specifies the configuration details of a schedule-triggered flow that you define. Currently, these settings only apply to the Scheduled trigger type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                trigger_config_property = customerprofiles.CfnIntegration.TriggerConfigProperty(
                    trigger_type="triggerType",
                
                    # the properties below are optional
                    trigger_properties=customerprofiles.CfnIntegration.TriggerPropertiesProperty(
                        scheduled=customerprofiles.CfnIntegration.ScheduledTriggerPropertiesProperty(
                            schedule_expression="scheduleExpression",
                
                            # the properties below are optional
                            data_pull_mode="dataPullMode",
                            first_execution_from=123,
                            schedule_end_time=123,
                            schedule_offset=123,
                            schedule_start_time=123,
                            timezone="timezone"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__43314febd76ccf4bc3946158640fcdb8e8e2b2e8aa92fe065358b557e5787cdc)
                check_type(argname="argument trigger_type", value=trigger_type, expected_type=type_hints["trigger_type"])
                check_type(argname="argument trigger_properties", value=trigger_properties, expected_type=type_hints["trigger_properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "trigger_type": trigger_type,
            }
            if trigger_properties is not None:
                self._values["trigger_properties"] = trigger_properties

        @builtins.property
        def trigger_type(self) -> builtins.str:
            '''Specifies the type of flow trigger.

            It can be OnDemand, Scheduled, or Event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html#cfn-customerprofiles-integration-triggerconfig-triggertype
            '''
            result = self._values.get("trigger_type")
            assert result is not None, "Required property 'trigger_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def trigger_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.TriggerPropertiesProperty"]]:
            '''Specifies the configuration details of a schedule-triggered flow that you define.

            Currently, these settings only apply to the Scheduled trigger type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerconfig.html#cfn-customerprofiles-integration-triggerconfig-triggerproperties
            '''
            result = self._values.get("trigger_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.TriggerPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.TriggerPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"scheduled": "scheduled"},
    )
    class TriggerPropertiesProperty:
        def __init__(
            self,
            *,
            scheduled: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.ScheduledTriggerPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the configuration details that control the trigger for a flow.

            Currently, these settings only apply to the Scheduled trigger type.

            :param scheduled: Specifies the configuration details of a schedule-triggered flow that you define.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                trigger_properties_property = customerprofiles.CfnIntegration.TriggerPropertiesProperty(
                    scheduled=customerprofiles.CfnIntegration.ScheduledTriggerPropertiesProperty(
                        schedule_expression="scheduleExpression",
                
                        # the properties below are optional
                        data_pull_mode="dataPullMode",
                        first_execution_from=123,
                        schedule_end_time=123,
                        schedule_offset=123,
                        schedule_start_time=123,
                        timezone="timezone"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3d95880464ba4d79437e95620f7b099ab48173665d71b3b3e9925b31023ae79a)
                check_type(argname="argument scheduled", value=scheduled, expected_type=type_hints["scheduled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if scheduled is not None:
                self._values["scheduled"] = scheduled

        @builtins.property
        def scheduled(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ScheduledTriggerPropertiesProperty"]]:
            '''Specifies the configuration details of a schedule-triggered flow that you define.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-triggerproperties.html#cfn-customerprofiles-integration-triggerproperties-scheduled
            '''
            result = self._values.get("scheduled")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ScheduledTriggerPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggerPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegration.ZendeskSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class ZendeskSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when using Zendesk as a flow source.

            :param object: The object specified in the Zendesk flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-zendesksourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                zendesk_source_properties_property = customerprofiles.CfnIntegration.ZendeskSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6fec16a3ec50ec7d597e7573ae1e24e531163b732505e322d5ef39e9267351db)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Zendesk flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-integration-zendesksourceproperties.html#cfn-customerprofiles-integration-zendesksourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ZendeskSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "event_trigger_names": "eventTriggerNames",
        "flow_definition": "flowDefinition",
        "object_type_name": "objectTypeName",
        "object_type_names": "objectTypeNames",
        "tags": "tags",
        "uri": "uri",
    },
)
class CfnIntegrationProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        event_trigger_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        flow_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.FlowDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        object_type_name: typing.Optional[builtins.str] = None,
        object_type_names: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ObjectTypeMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnIntegration``.

        :param domain_name: The unique name of the domain.
        :param event_trigger_names: A list of unique names for active event triggers associated with the integration.
        :param flow_definition: The configuration that controls how Customer Profiles retrieves data from the source.
        :param object_type_name: The name of the profile object type mapping to use.
        :param object_type_names: The object type mapping.
        :param tags: The tags used to organize, track, or control access for this resource.
        :param uri: The URI of the S3 bucket or any other type of data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_customerprofiles as customerprofiles
            
            cfn_integration_props = customerprofiles.CfnIntegrationProps(
                domain_name="domainName",
            
                # the properties below are optional
                event_trigger_names=["eventTriggerNames"],
                flow_definition=customerprofiles.CfnIntegration.FlowDefinitionProperty(
                    flow_name="flowName",
                    kms_arn="kmsArn",
                    source_flow_config=customerprofiles.CfnIntegration.SourceFlowConfigProperty(
                        connector_type="connectorType",
                        source_connector_properties=customerprofiles.CfnIntegration.SourceConnectorPropertiesProperty(
                            marketo=customerprofiles.CfnIntegration.MarketoSourcePropertiesProperty(
                                object="object"
                            ),
                            s3=customerprofiles.CfnIntegration.S3SourcePropertiesProperty(
                                bucket_name="bucketName",
            
                                # the properties below are optional
                                bucket_prefix="bucketPrefix"
                            ),
                            salesforce=customerprofiles.CfnIntegration.SalesforceSourcePropertiesProperty(
                                object="object",
            
                                # the properties below are optional
                                enable_dynamic_field_update=False,
                                include_deleted_records=False
                            ),
                            service_now=customerprofiles.CfnIntegration.ServiceNowSourcePropertiesProperty(
                                object="object"
                            ),
                            zendesk=customerprofiles.CfnIntegration.ZendeskSourcePropertiesProperty(
                                object="object"
                            )
                        ),
            
                        # the properties below are optional
                        connector_profile_name="connectorProfileName",
                        incremental_pull_config=customerprofiles.CfnIntegration.IncrementalPullConfigProperty(
                            datetime_type_field_name="datetimeTypeFieldName"
                        )
                    ),
                    tasks=[customerprofiles.CfnIntegration.TaskProperty(
                        source_fields=["sourceFields"],
                        task_type="taskType",
            
                        # the properties below are optional
                        connector_operator=customerprofiles.CfnIntegration.ConnectorOperatorProperty(
                            marketo="marketo",
                            s3="s3",
                            salesforce="salesforce",
                            service_now="serviceNow",
                            zendesk="zendesk"
                        ),
                        destination_field="destinationField",
                        task_properties=[customerprofiles.CfnIntegration.TaskPropertiesMapProperty(
                            operator_property_key="operatorPropertyKey",
                            property="property"
                        )]
                    )],
                    trigger_config=customerprofiles.CfnIntegration.TriggerConfigProperty(
                        trigger_type="triggerType",
            
                        # the properties below are optional
                        trigger_properties=customerprofiles.CfnIntegration.TriggerPropertiesProperty(
                            scheduled=customerprofiles.CfnIntegration.ScheduledTriggerPropertiesProperty(
                                schedule_expression="scheduleExpression",
            
                                # the properties below are optional
                                data_pull_mode="dataPullMode",
                                first_execution_from=123,
                                schedule_end_time=123,
                                schedule_offset=123,
                                schedule_start_time=123,
                                timezone="timezone"
                            )
                        )
                    ),
            
                    # the properties below are optional
                    description="description"
                ),
                object_type_name="objectTypeName",
                object_type_names=[customerprofiles.CfnIntegration.ObjectTypeMappingProperty(
                    key="key",
                    value="value"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                uri="uri"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52bfebce0bd12cb9d9ed6354b0627c3f2946899ecf1ba8120aa70c1e1e22428d)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument event_trigger_names", value=event_trigger_names, expected_type=type_hints["event_trigger_names"])
            check_type(argname="argument flow_definition", value=flow_definition, expected_type=type_hints["flow_definition"])
            check_type(argname="argument object_type_name", value=object_type_name, expected_type=type_hints["object_type_name"])
            check_type(argname="argument object_type_names", value=object_type_names, expected_type=type_hints["object_type_names"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
        }
        if event_trigger_names is not None:
            self._values["event_trigger_names"] = event_trigger_names
        if flow_definition is not None:
            self._values["flow_definition"] = flow_definition
        if object_type_name is not None:
            self._values["object_type_name"] = object_type_name
        if object_type_names is not None:
            self._values["object_type_names"] = object_type_names
        if tags is not None:
            self._values["tags"] = tags
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_trigger_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of unique names for active event triggers associated with the integration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-eventtriggernames
        '''
        result = self._values.get("event_trigger_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def flow_definition(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIntegration.FlowDefinitionProperty]]:
        '''The configuration that controls how Customer Profiles retrieves data from the source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-flowdefinition
        '''
        result = self._values.get("flow_definition")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIntegration.FlowDefinitionProperty]], result)

    @builtins.property
    def object_type_name(self) -> typing.Optional[builtins.str]:
        '''The name of the profile object type mapping to use.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-objecttypename
        '''
        result = self._values.get("object_type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_type_names(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnIntegration.ObjectTypeMappingProperty]]]]:
        '''The object type mapping.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-objecttypenames
        '''
        result = self._values.get("object_type_names")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnIntegration.ObjectTypeMappingProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''The URI of the S3 bucket or any other type of data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-integration.html#cfn-customerprofiles-integration-uri
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnObjectType(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnObjectType",
):
    '''Specifies an Amazon Connect Customer Profiles Object Type Mapping.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html
    :cloudformationResource: AWS::CustomerProfiles::ObjectType
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_customerprofiles as customerprofiles
        
        cfn_object_type = customerprofiles.CfnObjectType(self, "MyCfnObjectType",
            description="description",
            domain_name="domainName",
            object_type_name="objectTypeName",
        
            # the properties below are optional
            allow_profile_creation=False,
            encryption_key="encryptionKey",
            expiration_days=123,
            fields=[customerprofiles.CfnObjectType.FieldMapProperty(
                name="name",
                object_type_field=customerprofiles.CfnObjectType.ObjectTypeFieldProperty(
                    content_type="contentType",
                    source="source",
                    target="target"
                )
            )],
            keys=[customerprofiles.CfnObjectType.KeyMapProperty(
                name="name",
                object_type_key_list=[customerprofiles.CfnObjectType.ObjectTypeKeyProperty(
                    field_names=["fieldNames"],
                    standard_identifiers=["standardIdentifiers"]
                )]
            )],
            max_profile_object_count=123,
            source_last_updated_timestamp_format="sourceLastUpdatedTimestampFormat",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            template_id="templateId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        domain_name: builtins.str,
        object_type_name: builtins.str,
        allow_profile_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        expiration_days: typing.Optional[jsii.Number] = None,
        fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnObjectType.FieldMapProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnObjectType.KeyMapProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        max_profile_object_count: typing.Optional[jsii.Number] = None,
        source_last_updated_timestamp_format: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        template_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: The description of the profile object type mapping.
        :param domain_name: The unique name of the domain.
        :param object_type_name: The name of the profile object type.
        :param allow_profile_creation: Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type. The default is ``FALSE`` . If the AllowProfileCreation flag is set to ``FALSE`` , then the service tries to fetch a standard profile and associate this object with the profile. If it is set to ``TRUE`` , and if no match is found, then the service creates a new standard profile.
        :param encryption_key: The customer-provided key to encrypt the profile object that will be created in this profile object type mapping. If not specified the system will use the encryption key of the domain.
        :param expiration_days: The number of days until the data of this type expires.
        :param fields: A list of field definitions for the object type mapping.
        :param keys: A list of keys that can be used to map data to the profile or search for the profile.
        :param max_profile_object_count: The amount of profile object max count assigned to the object type.
        :param source_last_updated_timestamp_format: The format of your sourceLastUpdatedTimestamp that was previously set up.
        :param tags: The tags used to organize, track, or control access for this resource.
        :param template_id: A unique identifier for the template mapping. This can be used instead of specifying the Keys and Fields properties directly.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e58419cb0a7694b5c554275a8721df95dc40489e742a23c76f7830ca5210127a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnObjectTypeProps(
            description=description,
            domain_name=domain_name,
            object_type_name=object_type_name,
            allow_profile_creation=allow_profile_creation,
            encryption_key=encryption_key,
            expiration_days=expiration_days,
            fields=fields,
            keys=keys,
            max_profile_object_count=max_profile_object_count,
            source_last_updated_timestamp_format=source_last_updated_timestamp_format,
            tags=tags,
            template_id=template_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__091e212a123e3a0cfb8577aebb7068432007378feb06e4af48a00036957ea470)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0769bdf04f2e44acf0d6aa58be6958449e3ed7487344183891e249f5aefe6bea)
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
        '''The timestamp of when the object type was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The timestamp of when the object type was most recently edited.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrMaxAvailableProfileObjectCount")
    def attr_max_available_profile_object_count(self) -> jsii.Number:
        '''The amount of provisioned profile object max count available.

        :cloudformationAttribute: MaxAvailableProfileObjectCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrMaxAvailableProfileObjectCount"))

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
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the profile object type mapping.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aba990030ebf284cb51fc495ba3f894a3828072faa9f459784674e3467c4e696)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b24cea9cf31f287c3b3c148ba0586506624f0432fe276fdb1ec08d552833ef32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="objectTypeName")
    def object_type_name(self) -> builtins.str:
        '''The name of the profile object type.'''
        return typing.cast(builtins.str, jsii.get(self, "objectTypeName"))

    @object_type_name.setter
    def object_type_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19dbd5a494e7060e32b7c4cc781d4cee2093bd041be3baf6d8b03e5f66d76985)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectTypeName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="allowProfileCreation")
    def allow_profile_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "allowProfileCreation"))

    @allow_profile_creation.setter
    def allow_profile_creation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b0f4dc9c396c634c5fa55ab6032956c1c94c0dec83e089c60d92fb58640061c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowProfileCreation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''The customer-provided key to encrypt the profile object that will be created in this profile object type mapping.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKey"))

    @encryption_key.setter
    def encryption_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ca3be4f6e2ca6127ac1ca1adcf9552041402fd0c44217f1d4f13a4e14bf2b40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="expirationDays")
    def expiration_days(self) -> typing.Optional[jsii.Number]:
        '''The number of days until the data of this type expires.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expirationDays"))

    @expiration_days.setter
    def expiration_days(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64d57ec4a44e9d66c50a3e82cedcef4d73b7c54672341cb6bdc26bb43d5048de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationDays", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fields")
    def fields(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.FieldMapProperty"]]]]:
        '''A list of field definitions for the object type mapping.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.FieldMapProperty"]]]], jsii.get(self, "fields"))

    @fields.setter
    def fields(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.FieldMapProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eccf30ab38ee3158514f0243fca4f8f7f38ae86489a3784a2fee01eb15f10f58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fields", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="keys")
    def keys(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.KeyMapProperty"]]]]:
        '''A list of keys that can be used to map data to the profile or search for the profile.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.KeyMapProperty"]]]], jsii.get(self, "keys"))

    @keys.setter
    def keys(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.KeyMapProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__521c1a4bfa097c3b1f3951ecd6980736e1de35a3bfe50227b262534c59370624)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keys", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxProfileObjectCount")
    def max_profile_object_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of profile object max count assigned to the object type.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxProfileObjectCount"))

    @max_profile_object_count.setter
    def max_profile_object_count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edf9f4ddaedd0b5a755b294f08376889d206a0ce1a397886e2483e9471c6b184)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxProfileObjectCount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceLastUpdatedTimestampFormat")
    def source_last_updated_timestamp_format(self) -> typing.Optional[builtins.str]:
        '''The format of your sourceLastUpdatedTimestamp that was previously set up.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceLastUpdatedTimestampFormat"))

    @source_last_updated_timestamp_format.setter
    def source_last_updated_timestamp_format(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc577e5c0fd1bd47194e04599a6df995f066e809b7c98cb3b2e9ef839eaca0bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceLastUpdatedTimestampFormat", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__034fbef34b9c45ddeef371cddf129b147eb3c6d5cb089d2a874dec871d849617)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="templateId")
    def template_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the template mapping.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateId"))

    @template_id.setter
    def template_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c3516f296b116ed334a16a7f280bc13da509b7cc1b2d0f53992808db2bf0433)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateId", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnObjectType.FieldMapProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "object_type_field": "objectTypeField"},
    )
    class FieldMapProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            object_type_field: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnObjectType.ObjectTypeFieldProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A map of the name and ObjectType field.

            :param name: Name of the field.
            :param object_type_field: Represents a field in a ProfileObjectType.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                field_map_property = customerprofiles.CfnObjectType.FieldMapProperty(
                    name="name",
                    object_type_field=customerprofiles.CfnObjectType.ObjectTypeFieldProperty(
                        content_type="contentType",
                        source="source",
                        target="target"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ed4b9fc776f1c6cc0260e8e465d5e13c160ba26b2ed598c73a7b95e98cf61c94)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument object_type_field", value=object_type_field, expected_type=type_hints["object_type_field"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if object_type_field is not None:
                self._values["object_type_field"] = object_type_field

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''Name of the field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html#cfn-customerprofiles-objecttype-fieldmap-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_type_field(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnObjectType.ObjectTypeFieldProperty"]]:
            '''Represents a field in a ProfileObjectType.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-fieldmap.html#cfn-customerprofiles-objecttype-fieldmap-objecttypefield
            '''
            result = self._values.get("object_type_field")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnObjectType.ObjectTypeFieldProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnObjectType.KeyMapProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "object_type_key_list": "objectTypeKeyList"},
    )
    class KeyMapProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            object_type_key_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnObjectType.ObjectTypeKeyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''A unique key map that can be used to map data to the profile.

            :param name: Name of the key.
            :param object_type_key_list: A list of ObjectTypeKey.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                key_map_property = customerprofiles.CfnObjectType.KeyMapProperty(
                    name="name",
                    object_type_key_list=[customerprofiles.CfnObjectType.ObjectTypeKeyProperty(
                        field_names=["fieldNames"],
                        standard_identifiers=["standardIdentifiers"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7ea3cec6c8d04e9528d2f478540e3895caf69bc8db4178642b943b32ed3f9261)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument object_type_key_list", value=object_type_key_list, expected_type=type_hints["object_type_key_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if object_type_key_list is not None:
                self._values["object_type_key_list"] = object_type_key_list

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''Name of the key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html#cfn-customerprofiles-objecttype-keymap-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_type_key_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.ObjectTypeKeyProperty"]]]]:
            '''A list of ObjectTypeKey.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-keymap.html#cfn-customerprofiles-objecttype-keymap-objecttypekeylist
            '''
            result = self._values.get("object_type_key_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnObjectType.ObjectTypeKeyProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnObjectType.ObjectTypeFieldProperty",
        jsii_struct_bases=[],
        name_mapping={
            "content_type": "contentType",
            "source": "source",
            "target": "target",
        },
    )
    class ObjectTypeFieldProperty:
        def __init__(
            self,
            *,
            content_type: typing.Optional[builtins.str] = None,
            source: typing.Optional[builtins.str] = None,
            target: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents a field in a ProfileObjectType.

            :param content_type: The content type of the field. Used for determining equality when searching.
            :param source: A field of a ProfileObject. For example: _source.FirstName, where “_source” is a ProfileObjectType of a Zendesk user and “FirstName” is a field in that ObjectType.
            :param target: The location of the data in the standard ProfileObject model. For example: _profile.Address.PostalCode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                object_type_field_property = customerprofiles.CfnObjectType.ObjectTypeFieldProperty(
                    content_type="contentType",
                    source="source",
                    target="target"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b178f0d9e90930c4a4fd81ab392ed9c808bb1ea28f32cdd69c558694300980b)
                check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if content_type is not None:
                self._values["content_type"] = content_type
            if source is not None:
                self._values["source"] = source
            if target is not None:
                self._values["target"] = target

        @builtins.property
        def content_type(self) -> typing.Optional[builtins.str]:
            '''The content type of the field.

            Used for determining equality when searching.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-contenttype
            '''
            result = self._values.get("content_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source(self) -> typing.Optional[builtins.str]:
            '''A field of a ProfileObject.

            For example: _source.FirstName, where “_source” is a ProfileObjectType of a Zendesk user and “FirstName” is a field in that ObjectType.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target(self) -> typing.Optional[builtins.str]:
            '''The location of the data in the standard ProfileObject model.

            For example: _profile.Address.PostalCode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypefield.html#cfn-customerprofiles-objecttype-objecttypefield-target
            '''
            result = self._values.get("target")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObjectTypeFieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnObjectType.ObjectTypeKeyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_names": "fieldNames",
            "standard_identifiers": "standardIdentifiers",
        },
    )
    class ObjectTypeKeyProperty:
        def __init__(
            self,
            *,
            field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            standard_identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''An object that defines the Key element of a ProfileObject.

            A Key is a special element that can be used to search for a customer profile.

            :param field_names: The reference for the key name of the fields map.
            :param standard_identifiers: The types of keys that a ProfileObject can have. Each ProfileObject can have only 1 UNIQUE key but multiple PROFILE keys. PROFILE means that this key can be used to tie an object to a PROFILE. UNIQUE means that it can be used to uniquely identify an object. If a key a is marked as SECONDARY, it will be used to search for profiles after all other PROFILE keys have been searched. A LOOKUP_ONLY key is only used to match a profile but is not persisted to be used for searching of the profile. A NEW_ONLY key is only used if the profile does not already exist before the object is ingested, otherwise it is only used for matching objects to profiles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                object_type_key_property = customerprofiles.CfnObjectType.ObjectTypeKeyProperty(
                    field_names=["fieldNames"],
                    standard_identifiers=["standardIdentifiers"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7448ca799e207118d55f0019b3c6c35b6416f32804761112746d00e405772897)
                check_type(argname="argument field_names", value=field_names, expected_type=type_hints["field_names"])
                check_type(argname="argument standard_identifiers", value=standard_identifiers, expected_type=type_hints["standard_identifiers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if field_names is not None:
                self._values["field_names"] = field_names
            if standard_identifiers is not None:
                self._values["standard_identifiers"] = standard_identifiers

        @builtins.property
        def field_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The reference for the key name of the fields map.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html#cfn-customerprofiles-objecttype-objecttypekey-fieldnames
            '''
            result = self._values.get("field_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def standard_identifiers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The types of keys that a ProfileObject can have.

            Each ProfileObject can have only 1 UNIQUE key but multiple PROFILE keys. PROFILE means that this key can be used to tie an object to a PROFILE. UNIQUE means that it can be used to uniquely identify an object. If a key a is marked as SECONDARY, it will be used to search for profiles after all other PROFILE keys have been searched. A LOOKUP_ONLY key is only used to match a profile but is not persisted to be used for searching of the profile. A NEW_ONLY key is only used if the profile does not already exist before the object is ingested, otherwise it is only used for matching objects to profiles.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-objecttype-objecttypekey.html#cfn-customerprofiles-objecttype-objecttypekey-standardidentifiers
            '''
            result = self._values.get("standard_identifiers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObjectTypeKeyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnObjectTypeProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "domain_name": "domainName",
        "object_type_name": "objectTypeName",
        "allow_profile_creation": "allowProfileCreation",
        "encryption_key": "encryptionKey",
        "expiration_days": "expirationDays",
        "fields": "fields",
        "keys": "keys",
        "max_profile_object_count": "maxProfileObjectCount",
        "source_last_updated_timestamp_format": "sourceLastUpdatedTimestampFormat",
        "tags": "tags",
        "template_id": "templateId",
    },
)
class CfnObjectTypeProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        domain_name: builtins.str,
        object_type_name: builtins.str,
        allow_profile_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        expiration_days: typing.Optional[jsii.Number] = None,
        fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.FieldMapProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.KeyMapProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        max_profile_object_count: typing.Optional[jsii.Number] = None,
        source_last_updated_timestamp_format: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        template_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnObjectType``.

        :param description: The description of the profile object type mapping.
        :param domain_name: The unique name of the domain.
        :param object_type_name: The name of the profile object type.
        :param allow_profile_creation: Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type. The default is ``FALSE`` . If the AllowProfileCreation flag is set to ``FALSE`` , then the service tries to fetch a standard profile and associate this object with the profile. If it is set to ``TRUE`` , and if no match is found, then the service creates a new standard profile.
        :param encryption_key: The customer-provided key to encrypt the profile object that will be created in this profile object type mapping. If not specified the system will use the encryption key of the domain.
        :param expiration_days: The number of days until the data of this type expires.
        :param fields: A list of field definitions for the object type mapping.
        :param keys: A list of keys that can be used to map data to the profile or search for the profile.
        :param max_profile_object_count: The amount of profile object max count assigned to the object type.
        :param source_last_updated_timestamp_format: The format of your sourceLastUpdatedTimestamp that was previously set up.
        :param tags: The tags used to organize, track, or control access for this resource.
        :param template_id: A unique identifier for the template mapping. This can be used instead of specifying the Keys and Fields properties directly.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_customerprofiles as customerprofiles
            
            cfn_object_type_props = customerprofiles.CfnObjectTypeProps(
                description="description",
                domain_name="domainName",
                object_type_name="objectTypeName",
            
                # the properties below are optional
                allow_profile_creation=False,
                encryption_key="encryptionKey",
                expiration_days=123,
                fields=[customerprofiles.CfnObjectType.FieldMapProperty(
                    name="name",
                    object_type_field=customerprofiles.CfnObjectType.ObjectTypeFieldProperty(
                        content_type="contentType",
                        source="source",
                        target="target"
                    )
                )],
                keys=[customerprofiles.CfnObjectType.KeyMapProperty(
                    name="name",
                    object_type_key_list=[customerprofiles.CfnObjectType.ObjectTypeKeyProperty(
                        field_names=["fieldNames"],
                        standard_identifiers=["standardIdentifiers"]
                    )]
                )],
                max_profile_object_count=123,
                source_last_updated_timestamp_format="sourceLastUpdatedTimestampFormat",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                template_id="templateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__674aff1f8e16a6059ac0e56bfd831b21c20b3b3358878f53ea82ff2eea85954e)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument object_type_name", value=object_type_name, expected_type=type_hints["object_type_name"])
            check_type(argname="argument allow_profile_creation", value=allow_profile_creation, expected_type=type_hints["allow_profile_creation"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument expiration_days", value=expiration_days, expected_type=type_hints["expiration_days"])
            check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
            check_type(argname="argument keys", value=keys, expected_type=type_hints["keys"])
            check_type(argname="argument max_profile_object_count", value=max_profile_object_count, expected_type=type_hints["max_profile_object_count"])
            check_type(argname="argument source_last_updated_timestamp_format", value=source_last_updated_timestamp_format, expected_type=type_hints["source_last_updated_timestamp_format"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template_id", value=template_id, expected_type=type_hints["template_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "domain_name": domain_name,
            "object_type_name": object_type_name,
        }
        if allow_profile_creation is not None:
            self._values["allow_profile_creation"] = allow_profile_creation
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if expiration_days is not None:
            self._values["expiration_days"] = expiration_days
        if fields is not None:
            self._values["fields"] = fields
        if keys is not None:
            self._values["keys"] = keys
        if max_profile_object_count is not None:
            self._values["max_profile_object_count"] = max_profile_object_count
        if source_last_updated_timestamp_format is not None:
            self._values["source_last_updated_timestamp_format"] = source_last_updated_timestamp_format
        if tags is not None:
            self._values["tags"] = tags
        if template_id is not None:
            self._values["template_id"] = template_id

    @builtins.property
    def description(self) -> builtins.str:
        '''The description of the profile object type mapping.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The unique name of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_type_name(self) -> builtins.str:
        '''The name of the profile object type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-objecttypename
        '''
        result = self._values.get("object_type_name")
        assert result is not None, "Required property 'object_type_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_profile_creation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type.

        The default is ``FALSE`` . If the AllowProfileCreation flag is set to ``FALSE`` , then the service tries to fetch a standard profile and associate this object with the profile. If it is set to ``TRUE`` , and if no match is found, then the service creates a new standard profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-allowprofilecreation
        '''
        result = self._values.get("allow_profile_creation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''The customer-provided key to encrypt the profile object that will be created in this profile object type mapping.

        If not specified the system will use the encryption key of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-encryptionkey
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiration_days(self) -> typing.Optional[jsii.Number]:
        '''The number of days until the data of this type expires.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-expirationdays
        '''
        result = self._values.get("expiration_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fields(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnObjectType.FieldMapProperty]]]]:
        '''A list of field definitions for the object type mapping.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-fields
        '''
        result = self._values.get("fields")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnObjectType.FieldMapProperty]]]], result)

    @builtins.property
    def keys(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnObjectType.KeyMapProperty]]]]:
        '''A list of keys that can be used to map data to the profile or search for the profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-keys
        '''
        result = self._values.get("keys")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnObjectType.KeyMapProperty]]]], result)

    @builtins.property
    def max_profile_object_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of profile object max count assigned to the object type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-maxprofileobjectcount
        '''
        result = self._values.get("max_profile_object_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def source_last_updated_timestamp_format(self) -> typing.Optional[builtins.str]:
        '''The format of your sourceLastUpdatedTimestamp that was previously set up.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-sourcelastupdatedtimestampformat
        '''
        result = self._values.get("source_last_updated_timestamp_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def template_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the template mapping.

        This can be used instead of specifying the Keys and Fields properties directly.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-objecttype.html#cfn-customerprofiles-objecttype-templateid
        '''
        result = self._values.get("template_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnObjectTypeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnSegmentDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinition",
):
    '''A segment definition resource of Amazon Connect Customer Profiles.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-segmentdefinition.html
    :cloudformationResource: AWS::CustomerProfiles::SegmentDefinition
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_customerprofiles as customerprofiles
        
        cfn_segment_definition = customerprofiles.CfnSegmentDefinition(self, "MyCfnSegmentDefinition",
            display_name="displayName",
            domain_name="domainName",
            segment_definition_name="segmentDefinitionName",
            segment_groups=customerprofiles.CfnSegmentDefinition.SegmentGroupProperty(
                groups=[customerprofiles.CfnSegmentDefinition.GroupProperty(
                    dimensions=[customerprofiles.CfnSegmentDefinition.DimensionProperty(
                        calculated_attributes={
                            "calculated_attributes_key": customerprofiles.CfnSegmentDefinition.CalculatedAttributeDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"],
        
                                # the properties below are optional
                                condition_overrides=customerprofiles.CfnSegmentDefinition.ConditionOverridesProperty(
                                    range=customerprofiles.CfnSegmentDefinition.RangeOverrideProperty(
                                        start=123,
                                        unit="unit",
        
                                        # the properties below are optional
                                        end=123
                                    )
                                )
                            )
                        },
                        profile_attributes=customerprofiles.CfnSegmentDefinition.ProfileAttributesProperty(
                            account_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            additional_information=customerprofiles.CfnSegmentDefinition.ExtraLengthValueProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                )
                            ),
                            attributes={
                                "attributes_key": customerprofiles.CfnSegmentDefinition.AttributeDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                )
                            },
                            billing_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                )
                            ),
                            birth_date=customerprofiles.CfnSegmentDefinition.DateDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            business_email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            business_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            business_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            first_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            gender_string=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            home_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            last_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            mailing_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                )
                            ),
                            middle_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            mobile_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            party_type_string=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            personal_email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            profile_type=customerprofiles.CfnSegmentDefinition.ProfileTypeDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            shipping_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                )
                            )
                        )
                    )],
                    source_segments=[customerprofiles.CfnSegmentDefinition.SourceSegmentProperty(
                        segment_definition_name="segmentDefinitionName"
                    )],
                    source_type="sourceType",
                    type="type"
                )],
                include="include"
            ),
        
            # the properties below are optional
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
        display_name: builtins.str,
        domain_name: builtins.str,
        segment_definition_name: builtins.str,
        segment_groups: typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.SegmentGroupProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param display_name: Display name of the segment definition.
        :param domain_name: The name of the domain.
        :param segment_definition_name: Name of the segment definition.
        :param segment_groups: Contains all groups of the segment definition.
        :param description: The description of the segment definition.
        :param tags: The tags belonging to the segment definition.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__350e170fd13ca6586a78a39785ca961e3b7fa8982a5b03ff0799f34c2f12ea50)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSegmentDefinitionProps(
            display_name=display_name,
            domain_name=domain_name,
            segment_definition_name=segment_definition_name,
            segment_groups=segment_groups,
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
            type_hints = typing.get_type_hints(_typecheckingstub__43053ca51dec7fe64d769d488c3ff627584d6d29c926079a5503cd0fa5fcb6ca)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c93dc972ce2f528b294beb14fd064d6205569b6d0b68a9397a753547674ae198)
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
        '''When the segment definition was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrSegmentDefinitionArn")
    def attr_segment_definition_arn(self) -> builtins.str:
        '''The arn of the segment definition.

        :cloudformationAttribute: SegmentDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSegmentDefinitionArn"))

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
        '''Display name of the segment definition.'''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05d7eb6c9916e03c3799e9d2016d81426c2f6d43e95689ce0af12bfe09e6549f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The name of the domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26ba965f3f83218ff70b8ea34f99b1d05bab7433a8807b2fbcdaf115b08b6ae9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="segmentDefinitionName")
    def segment_definition_name(self) -> builtins.str:
        '''Name of the segment definition.'''
        return typing.cast(builtins.str, jsii.get(self, "segmentDefinitionName"))

    @segment_definition_name.setter
    def segment_definition_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bc5bbfa19f04ef37dd74fe0dab060cbd192ee5bb1b47e5b1508f67f27be5aa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "segmentDefinitionName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="segmentGroups")
    def segment_groups(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.SegmentGroupProperty"]:
        '''Contains all groups of the segment definition.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.SegmentGroupProperty"], jsii.get(self, "segmentGroups"))

    @segment_groups.setter
    def segment_groups(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.SegmentGroupProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__744689fb47e84da608e8ce7c410f0a6489728b4132c9e51efab1802d01b77340)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "segmentGroups", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the segment definition.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__223f2ad9551b0ca745b7b727aa69f874d90c37d42f2d71a6e2b2fb44e7ade212)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags belonging to the segment definition.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__238b83e5f2661e205fa241820b4292d8a4cb4f60bf75be3b31f1b17711318539)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinition.AddressDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "city": "city",
            "country": "country",
            "county": "county",
            "postal_code": "postalCode",
            "province": "province",
            "state": "state",
        },
    )
    class AddressDimensionProperty:
        def __init__(
            self,
            *,
            city: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            country: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            county: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            postal_code: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            province: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Object that segments on Customer Profile's address object.

            :param city: The city belonging to the address.
            :param country: The country belonging to the address.
            :param county: The county belonging to the address.
            :param postal_code: The postal code belonging to the address.
            :param province: The province belonging to the address.
            :param state: The state belonging to the address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-addressdimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                address_dimension_property = customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                    city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6a0bc2d171c7abf0d09aef2749bfbe17beb9e940d0184742ad750455e61d50e9)
                check_type(argname="argument city", value=city, expected_type=type_hints["city"])
                check_type(argname="argument country", value=country, expected_type=type_hints["country"])
                check_type(argname="argument county", value=county, expected_type=type_hints["county"])
                check_type(argname="argument postal_code", value=postal_code, expected_type=type_hints["postal_code"])
                check_type(argname="argument province", value=province, expected_type=type_hints["province"])
                check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if city is not None:
                self._values["city"] = city
            if country is not None:
                self._values["country"] = country
            if county is not None:
                self._values["county"] = county
            if postal_code is not None:
                self._values["postal_code"] = postal_code
            if province is not None:
                self._values["province"] = province
            if state is not None:
                self._values["state"] = state

        @builtins.property
        def city(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''The city belonging to the address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-addressdimension.html#cfn-customerprofiles-segmentdefinition-addressdimension-city
            '''
            result = self._values.get("city")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def country(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''The country belonging to the address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-addressdimension.html#cfn-customerprofiles-segmentdefinition-addressdimension-country
            '''
            result = self._values.get("country")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def county(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''The county belonging to the address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-addressdimension.html#cfn-customerprofiles-segmentdefinition-addressdimension-county
            '''
            result = self._values.get("county")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def postal_code(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''The postal code belonging to the address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-addressdimension.html#cfn-customerprofiles-segmentdefinition-addressdimension-postalcode
            '''
            result = self._values.get("postal_code")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def province(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''The province belonging to the address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-addressdimension.html#cfn-customerprofiles-segmentdefinition-addressdimension-province
            '''
            result = self._values.get("province")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def state(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''The state belonging to the address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-addressdimension.html#cfn-customerprofiles-segmentdefinition-addressdimension-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddressDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinition.AttributeDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_type": "dimensionType", "values": "values"},
    )
    class AttributeDimensionProperty:
        def __init__(
            self,
            *,
            dimension_type: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''Object that defines how to filter the incoming objects for the calculated attribute.

            :param dimension_type: The action to segment with.
            :param values: The values to apply the DimensionType on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-attributedimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                attribute_dimension_property = customerprofiles.CfnSegmentDefinition.AttributeDimensionProperty(
                    dimension_type="dimensionType",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bb318635b9a0dfe69f39d22e3b143ff47d00d73e95ba7e6119cb5a713fe732dd)
                check_type(argname="argument dimension_type", value=dimension_type, expected_type=type_hints["dimension_type"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dimension_type": dimension_type,
                "values": values,
            }

        @builtins.property
        def dimension_type(self) -> builtins.str:
            '''The action to segment with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-attributedimension.html#cfn-customerprofiles-segmentdefinition-attributedimension-dimensiontype
            '''
            result = self._values.get("dimension_type")
            assert result is not None, "Required property 'dimension_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''The values to apply the DimensionType on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-attributedimension.html#cfn-customerprofiles-segmentdefinition-attributedimension-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinition.CalculatedAttributeDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dimension_type": "dimensionType",
            "values": "values",
            "condition_overrides": "conditionOverrides",
        },
    )
    class CalculatedAttributeDimensionProperty:
        def __init__(
            self,
            *,
            dimension_type: builtins.str,
            values: typing.Sequence[builtins.str],
            condition_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ConditionOverridesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Object that segments on Customer Profile's Calculated Attributes.

            :param dimension_type: The action to segment with.
            :param values: The values to apply the DimensionType with.
            :param condition_overrides: Applies the given condition over the initial Calculated Attribute's definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-calculatedattributedimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                calculated_attribute_dimension_property = customerprofiles.CfnSegmentDefinition.CalculatedAttributeDimensionProperty(
                    dimension_type="dimensionType",
                    values=["values"],
                
                    # the properties below are optional
                    condition_overrides=customerprofiles.CfnSegmentDefinition.ConditionOverridesProperty(
                        range=customerprofiles.CfnSegmentDefinition.RangeOverrideProperty(
                            start=123,
                            unit="unit",
                
                            # the properties below are optional
                            end=123
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a86c277d8f43a78bd0246d26e28cb0a8e84b0a5c96f8046b7d644735eb70d256)
                check_type(argname="argument dimension_type", value=dimension_type, expected_type=type_hints["dimension_type"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
                check_type(argname="argument condition_overrides", value=condition_overrides, expected_type=type_hints["condition_overrides"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dimension_type": dimension_type,
                "values": values,
            }
            if condition_overrides is not None:
                self._values["condition_overrides"] = condition_overrides

        @builtins.property
        def dimension_type(self) -> builtins.str:
            '''The action to segment with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-calculatedattributedimension.html#cfn-customerprofiles-segmentdefinition-calculatedattributedimension-dimensiontype
            '''
            result = self._values.get("dimension_type")
            assert result is not None, "Required property 'dimension_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''The values to apply the DimensionType with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-calculatedattributedimension.html#cfn-customerprofiles-segmentdefinition-calculatedattributedimension-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def condition_overrides(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ConditionOverridesProperty"]]:
            '''Applies the given condition over the initial Calculated Attribute's definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-calculatedattributedimension.html#cfn-customerprofiles-segmentdefinition-calculatedattributedimension-conditionoverrides
            '''
            result = self._values.get("condition_overrides")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ConditionOverridesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CalculatedAttributeDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinition.ConditionOverridesProperty",
        jsii_struct_bases=[],
        name_mapping={"range": "range"},
    )
    class ConditionOverridesProperty:
        def __init__(
            self,
            *,
            range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.RangeOverrideProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An object to override the original condition block of a calculated attribute.

            :param range: The relative time period over which data is included in the aggregation for this override.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-conditionoverrides.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                condition_overrides_property = customerprofiles.CfnSegmentDefinition.ConditionOverridesProperty(
                    range=customerprofiles.CfnSegmentDefinition.RangeOverrideProperty(
                        start=123,
                        unit="unit",
                
                        # the properties below are optional
                        end=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__805f367b5025255b85dff70d74ab17cdb3209b82d5159f03785caf2e4ea38c27)
                check_type(argname="argument range", value=range, expected_type=type_hints["range"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if range is not None:
                self._values["range"] = range

        @builtins.property
        def range(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.RangeOverrideProperty"]]:
            '''The relative time period over which data is included in the aggregation for this override.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-conditionoverrides.html#cfn-customerprofiles-segmentdefinition-conditionoverrides-range
            '''
            result = self._values.get("range")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.RangeOverrideProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionOverridesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinition.DateDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_type": "dimensionType", "values": "values"},
    )
    class DateDimensionProperty:
        def __init__(
            self,
            *,
            dimension_type: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''Object that segments on various Customer Profile's date fields.

            :param dimension_type: The action to segment on.
            :param values: The values to apply the DimensionType on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-datedimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                date_dimension_property = customerprofiles.CfnSegmentDefinition.DateDimensionProperty(
                    dimension_type="dimensionType",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__321aa9ea2ffbe9c71ff0392adca1a155f2414f845fd6c463f7a0ea3785f7c270)
                check_type(argname="argument dimension_type", value=dimension_type, expected_type=type_hints["dimension_type"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dimension_type": dimension_type,
                "values": values,
            }

        @builtins.property
        def dimension_type(self) -> builtins.str:
            '''The action to segment on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-datedimension.html#cfn-customerprofiles-segmentdefinition-datedimension-dimensiontype
            '''
            result = self._values.get("dimension_type")
            assert result is not None, "Required property 'dimension_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''The values to apply the DimensionType on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-datedimension.html#cfn-customerprofiles-segmentdefinition-datedimension-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DateDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinition.DimensionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "calculated_attributes": "calculatedAttributes",
            "profile_attributes": "profileAttributes",
        },
    )
    class DimensionProperty:
        def __init__(
            self,
            *,
            calculated_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.CalculatedAttributeDimensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            profile_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Defines the attribute to segment on.

            :param calculated_attributes: Object that holds the calculated attributes to segment on.
            :param profile_attributes: Object that holds the profile attributes to segment on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-dimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                dimension_property = customerprofiles.CfnSegmentDefinition.DimensionProperty(
                    calculated_attributes={
                        "calculated_attributes_key": customerprofiles.CfnSegmentDefinition.CalculatedAttributeDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"],
                
                            # the properties below are optional
                            condition_overrides=customerprofiles.CfnSegmentDefinition.ConditionOverridesProperty(
                                range=customerprofiles.CfnSegmentDefinition.RangeOverrideProperty(
                                    start=123,
                                    unit="unit",
                
                                    # the properties below are optional
                                    end=123
                                )
                            )
                        )
                    },
                    profile_attributes=customerprofiles.CfnSegmentDefinition.ProfileAttributesProperty(
                        account_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        additional_information=customerprofiles.CfnSegmentDefinition.ExtraLengthValueProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                            city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            )
                        ),
                        attributes={
                            "attributes_key": customerprofiles.CfnSegmentDefinition.AttributeDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            )
                        },
                        billing_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                            city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            )
                        ),
                        birth_date=customerprofiles.CfnSegmentDefinition.DateDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        business_email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        business_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        business_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        first_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        gender_string=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        home_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        last_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        mailing_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                            city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            )
                        ),
                        middle_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        mobile_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        party_type_string=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        personal_email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        profile_type=customerprofiles.CfnSegmentDefinition.ProfileTypeDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        shipping_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                            city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__afcd95200751df2b6ea6aaaaadf0dca0e852f0fef263eeab7100a5c95ae82fc2)
                check_type(argname="argument calculated_attributes", value=calculated_attributes, expected_type=type_hints["calculated_attributes"])
                check_type(argname="argument profile_attributes", value=profile_attributes, expected_type=type_hints["profile_attributes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if calculated_attributes is not None:
                self._values["calculated_attributes"] = calculated_attributes
            if profile_attributes is not None:
                self._values["profile_attributes"] = profile_attributes

        @builtins.property
        def calculated_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.CalculatedAttributeDimensionProperty"]]]]:
            '''Object that holds the calculated attributes to segment on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-dimension.html#cfn-customerprofiles-segmentdefinition-dimension-calculatedattributes
            '''
            result = self._values.get("calculated_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.CalculatedAttributeDimensionProperty"]]]], result)

        @builtins.property
        def profile_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileAttributesProperty"]]:
            '''Object that holds the profile attributes to segment on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-dimension.html#cfn-customerprofiles-segmentdefinition-dimension-profileattributes
            '''
            result = self._values.get("profile_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileAttributesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinition.ExtraLengthValueProfileDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_type": "dimensionType", "values": "values"},
    )
    class ExtraLengthValueProfileDimensionProperty:
        def __init__(
            self,
            *,
            dimension_type: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''Object that segments on various Customer profile's fields that are larger than normal.

            :param dimension_type: The action to segment with.
            :param values: The values to apply the DimensionType on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-extralengthvalueprofiledimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                extra_length_value_profile_dimension_property = customerprofiles.CfnSegmentDefinition.ExtraLengthValueProfileDimensionProperty(
                    dimension_type="dimensionType",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b7820cd9f215f422bb2ed34ea399f9c5252453574cd926e31a73fd9a12c28498)
                check_type(argname="argument dimension_type", value=dimension_type, expected_type=type_hints["dimension_type"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dimension_type": dimension_type,
                "values": values,
            }

        @builtins.property
        def dimension_type(self) -> builtins.str:
            '''The action to segment with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-extralengthvalueprofiledimension.html#cfn-customerprofiles-segmentdefinition-extralengthvalueprofiledimension-dimensiontype
            '''
            result = self._values.get("dimension_type")
            assert result is not None, "Required property 'dimension_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''The values to apply the DimensionType on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-extralengthvalueprofiledimension.html#cfn-customerprofiles-segmentdefinition-extralengthvalueprofiledimension-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExtraLengthValueProfileDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinition.GroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dimensions": "dimensions",
            "source_segments": "sourceSegments",
            "source_type": "sourceType",
            "type": "type",
        },
    )
    class GroupProperty:
        def __init__(
            self,
            *,
            dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.DimensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            source_segments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.SourceSegmentProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            source_type: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains dimensions that determine what to segment on.

            :param dimensions: Defines the attributes to segment on.
            :param source_segments: Defines the starting source of data.
            :param source_type: Defines how to interact with the source data.
            :param type: Defines how to interact with the profiles found in the current filtering.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-group.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                group_property = customerprofiles.CfnSegmentDefinition.GroupProperty(
                    dimensions=[customerprofiles.CfnSegmentDefinition.DimensionProperty(
                        calculated_attributes={
                            "calculated_attributes_key": customerprofiles.CfnSegmentDefinition.CalculatedAttributeDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"],
                
                                # the properties below are optional
                                condition_overrides=customerprofiles.CfnSegmentDefinition.ConditionOverridesProperty(
                                    range=customerprofiles.CfnSegmentDefinition.RangeOverrideProperty(
                                        start=123,
                                        unit="unit",
                
                                        # the properties below are optional
                                        end=123
                                    )
                                )
                            )
                        },
                        profile_attributes=customerprofiles.CfnSegmentDefinition.ProfileAttributesProperty(
                            account_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            additional_information=customerprofiles.CfnSegmentDefinition.ExtraLengthValueProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                )
                            ),
                            attributes={
                                "attributes_key": customerprofiles.CfnSegmentDefinition.AttributeDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                )
                            },
                            billing_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                )
                            ),
                            birth_date=customerprofiles.CfnSegmentDefinition.DateDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            business_email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            business_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            business_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            first_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            gender_string=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            home_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            last_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            mailing_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                )
                            ),
                            middle_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            mobile_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            party_type_string=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            personal_email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            profile_type=customerprofiles.CfnSegmentDefinition.ProfileTypeDimensionProperty(
                                dimension_type="dimensionType",
                                values=["values"]
                            ),
                            shipping_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                )
                            )
                        )
                    )],
                    source_segments=[customerprofiles.CfnSegmentDefinition.SourceSegmentProperty(
                        segment_definition_name="segmentDefinitionName"
                    )],
                    source_type="sourceType",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d94bcaeaf726b09dbd09e1e48f12c042d531e9d0b092770695cebc3d52b5f5d)
                check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
                check_type(argname="argument source_segments", value=source_segments, expected_type=type_hints["source_segments"])
                check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if source_segments is not None:
                self._values["source_segments"] = source_segments
            if source_type is not None:
                self._values["source_type"] = source_type
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.DimensionProperty"]]]]:
            '''Defines the attributes to segment on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-group.html#cfn-customerprofiles-segmentdefinition-group-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.DimensionProperty"]]]], result)

        @builtins.property
        def source_segments(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.SourceSegmentProperty"]]]]:
            '''Defines the starting source of data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-group.html#cfn-customerprofiles-segmentdefinition-group-sourcesegments
            '''
            result = self._values.get("source_segments")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.SourceSegmentProperty"]]]], result)

        @builtins.property
        def source_type(self) -> typing.Optional[builtins.str]:
            '''Defines how to interact with the source data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-group.html#cfn-customerprofiles-segmentdefinition-group-sourcetype
            '''
            result = self._values.get("source_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''Defines how to interact with the profiles found in the current filtering.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-group.html#cfn-customerprofiles-segmentdefinition-group-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinition.ProfileAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_number": "accountNumber",
            "additional_information": "additionalInformation",
            "address": "address",
            "attributes": "attributes",
            "billing_address": "billingAddress",
            "birth_date": "birthDate",
            "business_email_address": "businessEmailAddress",
            "business_name": "businessName",
            "business_phone_number": "businessPhoneNumber",
            "email_address": "emailAddress",
            "first_name": "firstName",
            "gender_string": "genderString",
            "home_phone_number": "homePhoneNumber",
            "last_name": "lastName",
            "mailing_address": "mailingAddress",
            "middle_name": "middleName",
            "mobile_phone_number": "mobilePhoneNumber",
            "party_type_string": "partyTypeString",
            "personal_email_address": "personalEmailAddress",
            "phone_number": "phoneNumber",
            "profile_type": "profileType",
            "shipping_address": "shippingAddress",
        },
    )
    class ProfileAttributesProperty:
        def __init__(
            self,
            *,
            account_number: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            additional_information: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ExtraLengthValueProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.AddressDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.AttributeDimensionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            billing_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.AddressDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            birth_date: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.DateDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            business_email_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            business_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            business_phone_number: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            email_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            first_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            gender_string: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            home_phone_number: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            last_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mailing_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.AddressDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            middle_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mobile_phone_number: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            party_type_string: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            personal_email_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            phone_number: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            profile_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.ProfileTypeDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            shipping_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.AddressDimensionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The object used to segment on attributes within the customer profile.

            :param account_number: A field to describe values to segment on within account number.
            :param additional_information: A field to describe values to segment on within additional information.
            :param address: A field to describe values to segment on within address.
            :param attributes: A field to describe values to segment on within attributes.
            :param billing_address: A field to describe values to segment on within billing address.
            :param birth_date: A field to describe values to segment on within birthDate.
            :param business_email_address: A field to describe values to segment on within business email address.
            :param business_name: A field to describe values to segment on within business name.
            :param business_phone_number: A field to describe values to segment on within business phone number.
            :param email_address: A field to describe values to segment on within email address.
            :param first_name: A field to describe values to segment on within first name.
            :param gender_string: A field to describe values to segment on within genderString.
            :param home_phone_number: A field to describe values to segment on within home phone number.
            :param last_name: A field to describe values to segment on within last name.
            :param mailing_address: A field to describe values to segment on within mailing address.
            :param middle_name: A field to describe values to segment on within middle name.
            :param mobile_phone_number: A field to describe values to segment on within mobile phone number.
            :param party_type_string: A field to describe values to segment on within partyTypeString.
            :param personal_email_address: A field to describe values to segment on within personal email address.
            :param phone_number: A field to describe values to segment on within phone number.
            :param profile_type: The type of profile.
            :param shipping_address: A field to describe values to segment on within shipping address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                profile_attributes_property = customerprofiles.CfnSegmentDefinition.ProfileAttributesProperty(
                    account_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    additional_information=customerprofiles.CfnSegmentDefinition.ExtraLengthValueProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                        city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        )
                    ),
                    attributes={
                        "attributes_key": customerprofiles.CfnSegmentDefinition.AttributeDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        )
                    },
                    billing_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                        city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        )
                    ),
                    birth_date=customerprofiles.CfnSegmentDefinition.DateDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    business_email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    business_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    business_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    first_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    gender_string=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    home_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    last_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    mailing_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                        city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        )
                    ),
                    middle_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    mobile_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    party_type_string=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    personal_email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    profile_type=customerprofiles.CfnSegmentDefinition.ProfileTypeDimensionProperty(
                        dimension_type="dimensionType",
                        values=["values"]
                    ),
                    shipping_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                        city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        ),
                        state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                            dimension_type="dimensionType",
                            values=["values"]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2d3744d80b787b304270031bc1ba903495b3abb0c8edddf7fdffa36031caf48f)
                check_type(argname="argument account_number", value=account_number, expected_type=type_hints["account_number"])
                check_type(argname="argument additional_information", value=additional_information, expected_type=type_hints["additional_information"])
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
                check_type(argname="argument billing_address", value=billing_address, expected_type=type_hints["billing_address"])
                check_type(argname="argument birth_date", value=birth_date, expected_type=type_hints["birth_date"])
                check_type(argname="argument business_email_address", value=business_email_address, expected_type=type_hints["business_email_address"])
                check_type(argname="argument business_name", value=business_name, expected_type=type_hints["business_name"])
                check_type(argname="argument business_phone_number", value=business_phone_number, expected_type=type_hints["business_phone_number"])
                check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
                check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
                check_type(argname="argument gender_string", value=gender_string, expected_type=type_hints["gender_string"])
                check_type(argname="argument home_phone_number", value=home_phone_number, expected_type=type_hints["home_phone_number"])
                check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
                check_type(argname="argument mailing_address", value=mailing_address, expected_type=type_hints["mailing_address"])
                check_type(argname="argument middle_name", value=middle_name, expected_type=type_hints["middle_name"])
                check_type(argname="argument mobile_phone_number", value=mobile_phone_number, expected_type=type_hints["mobile_phone_number"])
                check_type(argname="argument party_type_string", value=party_type_string, expected_type=type_hints["party_type_string"])
                check_type(argname="argument personal_email_address", value=personal_email_address, expected_type=type_hints["personal_email_address"])
                check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
                check_type(argname="argument profile_type", value=profile_type, expected_type=type_hints["profile_type"])
                check_type(argname="argument shipping_address", value=shipping_address, expected_type=type_hints["shipping_address"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if account_number is not None:
                self._values["account_number"] = account_number
            if additional_information is not None:
                self._values["additional_information"] = additional_information
            if address is not None:
                self._values["address"] = address
            if attributes is not None:
                self._values["attributes"] = attributes
            if billing_address is not None:
                self._values["billing_address"] = billing_address
            if birth_date is not None:
                self._values["birth_date"] = birth_date
            if business_email_address is not None:
                self._values["business_email_address"] = business_email_address
            if business_name is not None:
                self._values["business_name"] = business_name
            if business_phone_number is not None:
                self._values["business_phone_number"] = business_phone_number
            if email_address is not None:
                self._values["email_address"] = email_address
            if first_name is not None:
                self._values["first_name"] = first_name
            if gender_string is not None:
                self._values["gender_string"] = gender_string
            if home_phone_number is not None:
                self._values["home_phone_number"] = home_phone_number
            if last_name is not None:
                self._values["last_name"] = last_name
            if mailing_address is not None:
                self._values["mailing_address"] = mailing_address
            if middle_name is not None:
                self._values["middle_name"] = middle_name
            if mobile_phone_number is not None:
                self._values["mobile_phone_number"] = mobile_phone_number
            if party_type_string is not None:
                self._values["party_type_string"] = party_type_string
            if personal_email_address is not None:
                self._values["personal_email_address"] = personal_email_address
            if phone_number is not None:
                self._values["phone_number"] = phone_number
            if profile_type is not None:
                self._values["profile_type"] = profile_type
            if shipping_address is not None:
                self._values["shipping_address"] = shipping_address

        @builtins.property
        def account_number(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''A field to describe values to segment on within account number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-accountnumber
            '''
            result = self._values.get("account_number")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def additional_information(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ExtraLengthValueProfileDimensionProperty"]]:
            '''A field to describe values to segment on within additional information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-additionalinformation
            '''
            result = self._values.get("additional_information")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ExtraLengthValueProfileDimensionProperty"]], result)

        @builtins.property
        def address(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.AddressDimensionProperty"]]:
            '''A field to describe values to segment on within address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.AddressDimensionProperty"]], result)

        @builtins.property
        def attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.AttributeDimensionProperty"]]]]:
            '''A field to describe values to segment on within attributes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.AttributeDimensionProperty"]]]], result)

        @builtins.property
        def billing_address(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.AddressDimensionProperty"]]:
            '''A field to describe values to segment on within billing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-billingaddress
            '''
            result = self._values.get("billing_address")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.AddressDimensionProperty"]], result)

        @builtins.property
        def birth_date(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.DateDimensionProperty"]]:
            '''A field to describe values to segment on within birthDate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-birthdate
            '''
            result = self._values.get("birth_date")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.DateDimensionProperty"]], result)

        @builtins.property
        def business_email_address(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''A field to describe values to segment on within business email address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-businessemailaddress
            '''
            result = self._values.get("business_email_address")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def business_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''A field to describe values to segment on within business name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-businessname
            '''
            result = self._values.get("business_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def business_phone_number(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''A field to describe values to segment on within business phone number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-businessphonenumber
            '''
            result = self._values.get("business_phone_number")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def email_address(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''A field to describe values to segment on within email address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-emailaddress
            '''
            result = self._values.get("email_address")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def first_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''A field to describe values to segment on within first name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-firstname
            '''
            result = self._values.get("first_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def gender_string(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''A field to describe values to segment on within genderString.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-genderstring
            '''
            result = self._values.get("gender_string")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def home_phone_number(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''A field to describe values to segment on within home phone number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-homephonenumber
            '''
            result = self._values.get("home_phone_number")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def last_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''A field to describe values to segment on within last name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-lastname
            '''
            result = self._values.get("last_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def mailing_address(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.AddressDimensionProperty"]]:
            '''A field to describe values to segment on within mailing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-mailingaddress
            '''
            result = self._values.get("mailing_address")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.AddressDimensionProperty"]], result)

        @builtins.property
        def middle_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''A field to describe values to segment on within middle name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-middlename
            '''
            result = self._values.get("middle_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def mobile_phone_number(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''A field to describe values to segment on within mobile phone number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-mobilephonenumber
            '''
            result = self._values.get("mobile_phone_number")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def party_type_string(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''A field to describe values to segment on within partyTypeString.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-partytypestring
            '''
            result = self._values.get("party_type_string")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def personal_email_address(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''A field to describe values to segment on within personal email address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-personalemailaddress
            '''
            result = self._values.get("personal_email_address")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def phone_number(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]]:
            '''A field to describe values to segment on within phone number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-phonenumber
            '''
            result = self._values.get("phone_number")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileDimensionProperty"]], result)

        @builtins.property
        def profile_type(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileTypeDimensionProperty"]]:
            '''The type of profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-profiletype
            '''
            result = self._values.get("profile_type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.ProfileTypeDimensionProperty"]], result)

        @builtins.property
        def shipping_address(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.AddressDimensionProperty"]]:
            '''A field to describe values to segment on within shipping address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profileattributes.html#cfn-customerprofiles-segmentdefinition-profileattributes-shippingaddress
            '''
            result = self._values.get("shipping_address")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.AddressDimensionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProfileAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_type": "dimensionType", "values": "values"},
    )
    class ProfileDimensionProperty:
        def __init__(
            self,
            *,
            dimension_type: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''Object that segments on various Customer profile's fields that are larger than normal.

            :param dimension_type: The action to segment on.
            :param values: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profiledimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                profile_dimension_property = customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                    dimension_type="dimensionType",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__007e452519747d631a7d676cfec00290dff2452d6eaac4a54fc80925aca3d685)
                check_type(argname="argument dimension_type", value=dimension_type, expected_type=type_hints["dimension_type"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dimension_type": dimension_type,
                "values": values,
            }

        @builtins.property
        def dimension_type(self) -> builtins.str:
            '''The action to segment on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profiledimension.html#cfn-customerprofiles-segmentdefinition-profiledimension-dimensiontype
            '''
            result = self._values.get("dimension_type")
            assert result is not None, "Required property 'dimension_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profiledimension.html#cfn-customerprofiles-segmentdefinition-profiledimension-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProfileDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinition.ProfileTypeDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_type": "dimensionType", "values": "values"},
    )
    class ProfileTypeDimensionProperty:
        def __init__(
            self,
            *,
            dimension_type: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''Specifies profile type based criteria for a segment.

            :param dimension_type: The action to segment on.
            :param values: The values to apply the DimensionType on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profiletypedimension.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                profile_type_dimension_property = customerprofiles.CfnSegmentDefinition.ProfileTypeDimensionProperty(
                    dimension_type="dimensionType",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__054d82d45b080caa1018b194962cae1c565d1648b07a9d3eb9b751a54d3c2b39)
                check_type(argname="argument dimension_type", value=dimension_type, expected_type=type_hints["dimension_type"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dimension_type": dimension_type,
                "values": values,
            }

        @builtins.property
        def dimension_type(self) -> builtins.str:
            '''The action to segment on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profiletypedimension.html#cfn-customerprofiles-segmentdefinition-profiletypedimension-dimensiontype
            '''
            result = self._values.get("dimension_type")
            assert result is not None, "Required property 'dimension_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''The values to apply the DimensionType on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-profiletypedimension.html#cfn-customerprofiles-segmentdefinition-profiletypedimension-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProfileTypeDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinition.RangeOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={"start": "start", "unit": "unit", "end": "end"},
    )
    class RangeOverrideProperty:
        def __init__(
            self,
            *,
            start: jsii.Number,
            unit: builtins.str,
            end: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Overrides the original range on a calculated attribute definition.

            :param start: The start time of when to include objects.
            :param unit: The unit for start and end.
            :param end: The end time of when to include objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-rangeoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                range_override_property = customerprofiles.CfnSegmentDefinition.RangeOverrideProperty(
                    start=123,
                    unit="unit",
                
                    # the properties below are optional
                    end=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ca238704a173f3c1cf142a9086e33976f93d4c9bf252b6a1aac82208186ef3e5)
                check_type(argname="argument start", value=start, expected_type=type_hints["start"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
                check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "start": start,
                "unit": unit,
            }
            if end is not None:
                self._values["end"] = end

        @builtins.property
        def start(self) -> jsii.Number:
            '''The start time of when to include objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-rangeoverride.html#cfn-customerprofiles-segmentdefinition-rangeoverride-start
            '''
            result = self._values.get("start")
            assert result is not None, "Required property 'start' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def unit(self) -> builtins.str:
            '''The unit for start and end.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-rangeoverride.html#cfn-customerprofiles-segmentdefinition-rangeoverride-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end(self) -> typing.Optional[jsii.Number]:
            '''The end time of when to include objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-rangeoverride.html#cfn-customerprofiles-segmentdefinition-rangeoverride-end
            '''
            result = self._values.get("end")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RangeOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinition.SegmentGroupProperty",
        jsii_struct_bases=[],
        name_mapping={"groups": "groups", "include": "include"},
    )
    class SegmentGroupProperty:
        def __init__(
            self,
            *,
            groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSegmentDefinition.GroupProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            include: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains all groups of the segment definition.

            :param groups: Holds the list of groups within the segment definition.
            :param include: Defines whether to include or exclude the profiles that fit the segment criteria.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-segmentgroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                segment_group_property = customerprofiles.CfnSegmentDefinition.SegmentGroupProperty(
                    groups=[customerprofiles.CfnSegmentDefinition.GroupProperty(
                        dimensions=[customerprofiles.CfnSegmentDefinition.DimensionProperty(
                            calculated_attributes={
                                "calculated_attributes_key": customerprofiles.CfnSegmentDefinition.CalculatedAttributeDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"],
                
                                    # the properties below are optional
                                    condition_overrides=customerprofiles.CfnSegmentDefinition.ConditionOverridesProperty(
                                        range=customerprofiles.CfnSegmentDefinition.RangeOverrideProperty(
                                            start=123,
                                            unit="unit",
                
                                            # the properties below are optional
                                            end=123
                                        )
                                    )
                                )
                            },
                            profile_attributes=customerprofiles.CfnSegmentDefinition.ProfileAttributesProperty(
                                account_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                additional_information=customerprofiles.CfnSegmentDefinition.ExtraLengthValueProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                    city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    )
                                ),
                                attributes={
                                    "attributes_key": customerprofiles.CfnSegmentDefinition.AttributeDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    )
                                },
                                billing_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                    city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    )
                                ),
                                birth_date=customerprofiles.CfnSegmentDefinition.DateDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                business_email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                business_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                business_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                first_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                gender_string=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                home_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                last_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                mailing_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                    city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    )
                                ),
                                middle_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                mobile_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                party_type_string=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                personal_email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                profile_type=customerprofiles.CfnSegmentDefinition.ProfileTypeDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                shipping_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                    city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    )
                                )
                            )
                        )],
                        source_segments=[customerprofiles.CfnSegmentDefinition.SourceSegmentProperty(
                            segment_definition_name="segmentDefinitionName"
                        )],
                        source_type="sourceType",
                        type="type"
                    )],
                    include="include"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__49a789743f5ac4162a8c53d6f5aae978c5989a590155f77804b52b37938d7672)
                check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
                check_type(argname="argument include", value=include, expected_type=type_hints["include"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if groups is not None:
                self._values["groups"] = groups
            if include is not None:
                self._values["include"] = include

        @builtins.property
        def groups(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.GroupProperty"]]]]:
            '''Holds the list of groups within the segment definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-segmentgroup.html#cfn-customerprofiles-segmentdefinition-segmentgroup-groups
            '''
            result = self._values.get("groups")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSegmentDefinition.GroupProperty"]]]], result)

        @builtins.property
        def include(self) -> typing.Optional[builtins.str]:
            '''Defines whether to include or exclude the profiles that fit the segment criteria.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-segmentgroup.html#cfn-customerprofiles-segmentdefinition-segmentgroup-include
            '''
            result = self._values.get("include")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SegmentGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinition.SourceSegmentProperty",
        jsii_struct_bases=[],
        name_mapping={"segment_definition_name": "segmentDefinitionName"},
    )
    class SourceSegmentProperty:
        def __init__(
            self,
            *,
            segment_definition_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The source segments to build off of.

            :param segment_definition_name: The name of the source segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-sourcesegment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_customerprofiles as customerprofiles
                
                source_segment_property = customerprofiles.CfnSegmentDefinition.SourceSegmentProperty(
                    segment_definition_name="segmentDefinitionName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__002c938fccce270fc597ae5653583b8a9910031239e0daaf523e0c4431d75ed7)
                check_type(argname="argument segment_definition_name", value=segment_definition_name, expected_type=type_hints["segment_definition_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if segment_definition_name is not None:
                self._values["segment_definition_name"] = segment_definition_name

        @builtins.property
        def segment_definition_name(self) -> typing.Optional[builtins.str]:
            '''The name of the source segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-customerprofiles-segmentdefinition-sourcesegment.html#cfn-customerprofiles-segmentdefinition-sourcesegment-segmentdefinitionname
            '''
            result = self._values.get("segment_definition_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceSegmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_customerprofiles.CfnSegmentDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "domain_name": "domainName",
        "segment_definition_name": "segmentDefinitionName",
        "segment_groups": "segmentGroups",
        "description": "description",
        "tags": "tags",
    },
)
class CfnSegmentDefinitionProps:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        domain_name: builtins.str,
        segment_definition_name: builtins.str,
        segment_groups: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.SegmentGroupProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSegmentDefinition``.

        :param display_name: Display name of the segment definition.
        :param domain_name: The name of the domain.
        :param segment_definition_name: Name of the segment definition.
        :param segment_groups: Contains all groups of the segment definition.
        :param description: The description of the segment definition.
        :param tags: The tags belonging to the segment definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-segmentdefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_customerprofiles as customerprofiles
            
            cfn_segment_definition_props = customerprofiles.CfnSegmentDefinitionProps(
                display_name="displayName",
                domain_name="domainName",
                segment_definition_name="segmentDefinitionName",
                segment_groups=customerprofiles.CfnSegmentDefinition.SegmentGroupProperty(
                    groups=[customerprofiles.CfnSegmentDefinition.GroupProperty(
                        dimensions=[customerprofiles.CfnSegmentDefinition.DimensionProperty(
                            calculated_attributes={
                                "calculated_attributes_key": customerprofiles.CfnSegmentDefinition.CalculatedAttributeDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"],
            
                                    # the properties below are optional
                                    condition_overrides=customerprofiles.CfnSegmentDefinition.ConditionOverridesProperty(
                                        range=customerprofiles.CfnSegmentDefinition.RangeOverrideProperty(
                                            start=123,
                                            unit="unit",
            
                                            # the properties below are optional
                                            end=123
                                        )
                                    )
                                )
                            },
                            profile_attributes=customerprofiles.CfnSegmentDefinition.ProfileAttributesProperty(
                                account_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                additional_information=customerprofiles.CfnSegmentDefinition.ExtraLengthValueProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                    city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    )
                                ),
                                attributes={
                                    "attributes_key": customerprofiles.CfnSegmentDefinition.AttributeDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    )
                                },
                                billing_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                    city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    )
                                ),
                                birth_date=customerprofiles.CfnSegmentDefinition.DateDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                business_email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                business_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                business_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                first_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                gender_string=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                home_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                last_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                mailing_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                    city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    )
                                ),
                                middle_name=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                mobile_phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                party_type_string=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                personal_email_address=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                phone_number=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                profile_type=customerprofiles.CfnSegmentDefinition.ProfileTypeDimensionProperty(
                                    dimension_type="dimensionType",
                                    values=["values"]
                                ),
                                shipping_address=customerprofiles.CfnSegmentDefinition.AddressDimensionProperty(
                                    city=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    country=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    county=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    postal_code=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    province=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    ),
                                    state=customerprofiles.CfnSegmentDefinition.ProfileDimensionProperty(
                                        dimension_type="dimensionType",
                                        values=["values"]
                                    )
                                )
                            )
                        )],
                        source_segments=[customerprofiles.CfnSegmentDefinition.SourceSegmentProperty(
                            segment_definition_name="segmentDefinitionName"
                        )],
                        source_type="sourceType",
                        type="type"
                    )],
                    include="include"
                ),
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfe3927b013a59f4b37e001ce8d373fe3d8d8bc374ee6c206d37e74f69369348)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument segment_definition_name", value=segment_definition_name, expected_type=type_hints["segment_definition_name"])
            check_type(argname="argument segment_groups", value=segment_groups, expected_type=type_hints["segment_groups"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "display_name": display_name,
            "domain_name": domain_name,
            "segment_definition_name": segment_definition_name,
            "segment_groups": segment_groups,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def display_name(self) -> builtins.str:
        '''Display name of the segment definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-segmentdefinition.html#cfn-customerprofiles-segmentdefinition-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The name of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-segmentdefinition.html#cfn-customerprofiles-segmentdefinition-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def segment_definition_name(self) -> builtins.str:
        '''Name of the segment definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-segmentdefinition.html#cfn-customerprofiles-segmentdefinition-segmentdefinitionname
        '''
        result = self._values.get("segment_definition_name")
        assert result is not None, "Required property 'segment_definition_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def segment_groups(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnSegmentDefinition.SegmentGroupProperty]:
        '''Contains all groups of the segment definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-segmentdefinition.html#cfn-customerprofiles-segmentdefinition-segmentgroups
        '''
        result = self._values.get("segment_groups")
        assert result is not None, "Required property 'segment_groups' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnSegmentDefinition.SegmentGroupProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the segment definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-segmentdefinition.html#cfn-customerprofiles-segmentdefinition-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags belonging to the segment definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-customerprofiles-segmentdefinition.html#cfn-customerprofiles-segmentdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSegmentDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCalculatedAttributeDefinition",
    "CfnCalculatedAttributeDefinitionProps",
    "CfnDomain",
    "CfnDomainProps",
    "CfnEventStream",
    "CfnEventStreamProps",
    "CfnEventTrigger",
    "CfnEventTriggerProps",
    "CfnIntegration",
    "CfnIntegrationProps",
    "CfnObjectType",
    "CfnObjectTypeProps",
    "CfnSegmentDefinition",
    "CfnSegmentDefinitionProps",
]

publication.publish()

def _typecheckingstub__3a09ab96caa4db6cfa4ebb0207c025a7f976cac18f814d69b882506cf2971669(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    attribute_details: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.AttributeDetailsProperty, typing.Dict[builtins.str, typing.Any]]],
    calculated_attribute_name: builtins.str,
    domain_name: builtins.str,
    statistic: builtins.str,
    conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.ConditionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_historical_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8c355c3b327941e1e80c87b111beedb797243265da934cbe14cb40a04def39b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ff2e7320eba6c67e11b5108c4174e965091aab4bf1ed72835487ea46d7bd228(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc094b8898d98fbc0a232ed05081d6ffd11e6092cf72d062c7ab6a1a118b2655(
    value: typing.Union[_IResolvable_da3f097b, CfnCalculatedAttributeDefinition.AttributeDetailsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1874ab73c6c7fb500a83379a356ae12dde9d52f47b68d1b2dfe7fb7772ae682(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__806572f2b3c6f3d60619dab1026866577ec43486c44775df8e7f00f9ec946cc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24137af23c238e226876684e3ad841c56564bd3e9f7c488415d38fbd9560440e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d9f165d8e8dde422309619ae01ce8e4f77e67c1d8707134c0f7c2a25fd53ebc(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCalculatedAttributeDefinition.ConditionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e94c935ac0604ce2b84a26b87f764d32bfa425eb59416e0935dca9d2a010ce58(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64a1f1d0da7758807d6fc0184c03cfdc7c695677f2dd2cfeb300cb009b6e9d69(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66b41ae1f61b2d451c01e8a6b3eabc1ef1fe6f0e51c71a264d46a9df8ec0ad14(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ab1072a749050ba2fecfbba8cc52cbc745e52869b7164a97ab6eb2dcdf582c4(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6241b1471123a742a03d1b24e69021bc3c2c3b4a805094f7a6176be6f76da07a(
    *,
    attributes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.AttributeItemProperty, typing.Dict[builtins.str, typing.Any]]]]],
    expression: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2af823a61c3449f36ffaa48661361e9de02280cffeeefa5a3d5990a5035cd43b(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d5606a68f168622e019935c1cfd2eb8821e95f36c66313b2a6f7a38cc4e472(
    *,
    object_count: typing.Optional[jsii.Number] = None,
    range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.RangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    threshold: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.ThresholdProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4567eb83ac5620aa6be36cbd0e38cdba257d259743e1017616dbc2252fc66f9d(
    *,
    unit: builtins.str,
    timestamp_format: typing.Optional[builtins.str] = None,
    timestamp_source: typing.Optional[builtins.str] = None,
    value: typing.Optional[jsii.Number] = None,
    value_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.ValueRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bc0a3c3468a435a5677e162145a9ef5e062a4e72fd921895d645bd1056af4e3(
    *,
    message: typing.Optional[builtins.str] = None,
    progress_percentage: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcc19afa2a314e3392b1f8004f5ce5593298e226e89f8bb3424dc57cefbb2646(
    *,
    operator: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d18b8118549ce586fc14b0cc15f51e9a520330684bb4d883bbf10b82b000c5a(
    *,
    end: jsii.Number,
    start: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b490cf412d8b10ddc1ddbf98b6d852a5446deca7e9befe3439df8de5169c37dd(
    *,
    attribute_details: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.AttributeDetailsProperty, typing.Dict[builtins.str, typing.Any]]],
    calculated_attribute_name: builtins.str,
    domain_name: builtins.str,
    statistic: builtins.str,
    conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCalculatedAttributeDefinition.ConditionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_historical_data: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cc1e612474254ea8edde86de3e08226c0c50e450782b3a99c92e87c31b99bad(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    default_expiration_days: jsii.Number,
    domain_name: builtins.str,
    dead_letter_queue_url: typing.Optional[builtins.str] = None,
    default_encryption_key: typing.Optional[builtins.str] = None,
    matching: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.MatchingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rule_based_matching: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.RuleBasedMatchingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd90568f369097b5d7a19088e675226c1257ad9e9ac30f3a478e941435aaaf5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88e553e446de50b16b878a912bc0a5f6f8763a19282b8d9da5099d68ef82e5b6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d16654417fe9cbdb9f2b4f0145b59b3328699684a9b2c7ae7f2a3ad9b271e93(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5155d94ec0a92f02d3b08cff5971632f213635d3dd2577433bbe328e9fac1d90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39213ab6c2161d29ce1bafee3ec589effa27e2d24da755fd856339bb486e25a2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed9ea79eb70814ff005e2ba351fe52042bea41d55509db4f24fbbf0d33cfb9a7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38b62853e21632f695b18d1a2df674dd4f9112b5fa5e1f684278017a8ed38588(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.MatchingProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__868f26d6f7d5d3991c71c5dd31b8053c3dab74afec8faa28dab5dc89621ca137(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomain.RuleBasedMatchingProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cc3d01d93fe80a75ec77ac1c37d929543f51e4a47feb47e25ebd0afa5fee06a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3428c7ec5300f42cab23342316a084605547b5a853b619d629d81f5d7cfafd8(
    *,
    attribute_matching_model: builtins.str,
    address: typing.Optional[typing.Sequence[builtins.str]] = None,
    email_address: typing.Optional[typing.Sequence[builtins.str]] = None,
    phone_number: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b35edae469251b1731680dae49e6588a5a064bbfac0f2f75b83135106bb693f(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    conflict_resolution: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.ConflictResolutionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    consolidation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.ConsolidationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    min_allowed_confidence_score_for_merging: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39a5c699e09d6961f3eed32cb756eca983664193f4a0cdfbac7965404e3b40d1(
    *,
    conflict_resolving_model: builtins.str,
    source_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f3fee71d236ee85937168636cf44627d0e12e7714908fdcc02548a6e6baa537(
    *,
    matching_attributes_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Sequence[builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed7393f6287227101f4cad4938dff729de652d2fea3653b0c4f8ef82477058e4(
    *,
    metering_profile_count: typing.Optional[jsii.Number] = None,
    object_count: typing.Optional[jsii.Number] = None,
    profile_count: typing.Optional[jsii.Number] = None,
    total_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb96a013617382e2d069cda664f0c892dede8cafdff896ba1efefecbd051b998(
    *,
    s3_exporting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.S3ExportingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f904c449e943e8aaee42f71a3d0a53319d006582bc12e5658661832c9424bd99(
    *,
    day_of_the_week: builtins.str,
    time: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f66676b221bc8ebb46140fe93d616e4dde0b38406203efe2203ad295a0605a4(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    auto_merging: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.AutoMergingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    exporting_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.ExportingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    job_schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.JobScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d978c61e1b04215bb349c7460583b8296f0fc2a1f64e575731bf7ab355b1b9e(
    *,
    rule: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63470bb7c476b2fc82a2f0bc6e61f9a94630928b1d8427c1ec5400fd3523d282(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    attribute_types_selector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.AttributeTypesSelectorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    conflict_resolution: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.ConflictResolutionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    exporting_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.ExportingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    matching_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.MatchingRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    max_allowed_rule_level_for_matching: typing.Optional[jsii.Number] = None,
    max_allowed_rule_level_for_merging: typing.Optional[jsii.Number] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67d29e593ac1f40be9594826daeee9e088ed90a7a1c973d30de0a10f42a70cb6(
    *,
    s3_bucket_name: builtins.str,
    s3_key_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03a55eb0b8d16e4b2b2589908d65475847a28870949386381667b6572e627f96(
    *,
    default_expiration_days: jsii.Number,
    domain_name: builtins.str,
    dead_letter_queue_url: typing.Optional[builtins.str] = None,
    default_encryption_key: typing.Optional[builtins.str] = None,
    matching: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.MatchingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rule_based_matching: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomain.RuleBasedMatchingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab29d0d747428994b84491cb3989a05a67bcb4cf0b84ebeba8fd19114b7cd61d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    event_stream_name: builtins.str,
    uri: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d37a000675ecf626a3348ff78d7f60db4441f2bb16c208d8dea0d1a4ecbd88f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__897cf1ba007446204846a7b757f800cd045b6bea2153894c6a8efdade633eaca(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e40edb2a552aa50e0d65e685a232d9e8b469877491c9fd016aaf025966b9a1b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87ecaa8f57744bab81313074352cbc2f82cf8f797e78ce582ff548aa6251c330(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d80288203f7d0782baca6858266d8c740f3fda90b2d6ef328306f3e966d5ee4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dcffaefd3d051ab25e983d551d4abe7f28bcc0ccc2cc0f00dfbe9151cc9bd64(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14be2a6e46acdc39b98267227ca646cdeba3edce7277e1499527949bda68cd54(
    *,
    status: builtins.str,
    uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__813f95ba6287d3dc18d43b5b2ff35fbde17184e556360b280e3386143cfc00f0(
    *,
    domain_name: builtins.str,
    event_stream_name: builtins.str,
    uri: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3238d15e8be30353d06e9f7813fb0d93d105339df1e3008dc6d5d889128103a4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    event_trigger_conditions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventTrigger.EventTriggerConditionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    event_trigger_name: builtins.str,
    object_type_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    event_trigger_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventTrigger.EventTriggerLimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    segment_filter: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e272d39f5f3a739ab199e698c49cb32366cbc41b54a8e3cc306be93e625b409(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d0fbc1a083288ddd09e30a938f56be084f6444e4f3ee741d96ffda16a72c037(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46f0ca81a5f8cee1e0a4c4f9b3d38652326a6ebce5ed8f5ee45cd3300bc09d21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c4c9a1ce30ec03f18e86da98746e17633bdcc9de1f9657feb330288a5703464(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventTrigger.EventTriggerConditionProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9a32cfee1a68445fea2fa917fb431b02536069883dc6c492094b36c48158d6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26f048d7d34ef17a451ca6afc9c754cf23e5448d0fa70d08e95941b41a53e15b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14f8e2b14eb300ec5bb3dbffd9fda2b1b3fa26a8ccb24220faf205a2c9252b16(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8577e6b11fafc0b473494e772f42df4b3a275f14decae7f35bf35c8ceca6efbb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEventTrigger.EventTriggerLimitsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ed3d132124c95676f8283662330dfc6f234432d197bcdb1846aeb9b55d6b31d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0431604b79fa9f08ecdffc28b119f0c684057eb139cb8d0fcc9e51cc364ff34a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01622abde91c4f131120bde889e115bd6740e17b0e7e060628263c9607cf01d4(
    *,
    event_trigger_dimensions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventTrigger.EventTriggerDimensionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    logical_operator: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__936befd5e0ecb3c45c2c47843a0cfa5dfc87acecf21c037978def245f15c99ff(
    *,
    object_attributes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventTrigger.ObjectAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c21f9960dce43c4cfe6a915ec34c75b13089631bea9d3de70a87e7098384cb1d(
    *,
    event_expiration: typing.Optional[jsii.Number] = None,
    periods: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventTrigger.PeriodProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0a90a9f34cbabcbef830e52f532688120b085cb48e257f24a4658b7c9bbbcec(
    *,
    comparison_operator: builtins.str,
    values: typing.Sequence[builtins.str],
    field_name: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__779555dd66a387de3220544cdb9e3846de45bce3e7a1615f8f0ecb0e783adbe9(
    *,
    unit: builtins.str,
    value: jsii.Number,
    max_invocations_per_profile: typing.Optional[jsii.Number] = None,
    unlimited: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9d2b6147273c603d09e90db3d8372049e484840bcff7a8dc8031fd2f0e0e756(
    *,
    domain_name: builtins.str,
    event_trigger_conditions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventTrigger.EventTriggerConditionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    event_trigger_name: builtins.str,
    object_type_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    event_trigger_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventTrigger.EventTriggerLimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    segment_filter: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8211c08b95eabfe008b27ab5b3b74bab34f671b7bd9761e15cdb090da9d3d95(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    event_trigger_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    flow_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.FlowDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    object_type_name: typing.Optional[builtins.str] = None,
    object_type_names: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ObjectTypeMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85eb075da84dc570034fe72854e5f377beb9454784461fb242856b2b0d6db071(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a02b200ac7ef42474d61bef0afc23d2047a43211308a0f0f346c8804318a953d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d13bac4a06b95e4fadaf50aaed39e2383120484f2d6e868a652119e3c0741a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2353defad4ed0b7f19993fda09b6c2619751d1fb77397c9b4957634b704a6fba(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eda84696baed289de5f577073d9697fd7b0969af55567086ad86e6466b533e14(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIntegration.FlowDefinitionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ac4be2e5060d6806d086adb14efc1af2df364f07423ea56e6af2958c23fc2b1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d19e3d184d030db553288fb9b5bf060b201c3b429358e9c4818b39453b44a060(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnIntegration.ObjectTypeMappingProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55efe13391c8b01dcc8a4fc8cdb64b30e0590e3c2de5fbdfaf88656f9ad1a18e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02e9de6347e213a96d6d3dc4870b6c07c7e7db9b8044cff9f9952e0192a795c2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8ff575fc6d67c92e33f52c9a2a9924dd1914b3ec97eb67ea19a5f83109dfe09(
    *,
    marketo: typing.Optional[builtins.str] = None,
    s3: typing.Optional[builtins.str] = None,
    salesforce: typing.Optional[builtins.str] = None,
    service_now: typing.Optional[builtins.str] = None,
    zendesk: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__684e26c18461ba90c60337c4f41ecfe0fff4d6e92e5f5ccc4fca2dbb9cb7fe58(
    *,
    flow_name: builtins.str,
    kms_arn: builtins.str,
    source_flow_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.SourceFlowConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    tasks: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.TaskProperty, typing.Dict[builtins.str, typing.Any]]]]],
    trigger_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.TriggerConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b30373edbc1fc87d87c0305c0d579d9085e768165db2968c37ebc100141fc94c(
    *,
    datetime_type_field_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a60c86877c43b5afd59790a18d6019039ccc87b2d8b8b5c9299157eda159890(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9afb6e6e9868c0b8b44a3a96fec8e43830e8a548405844dbf1d5a8d81ced10d(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a79daf2a1599613c0d4820e23ade3e1ab729e048f4f33e5e1ca2c56d56a3757b(
    *,
    bucket_name: builtins.str,
    bucket_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48d96167457187d54618dd4839b1f9086125a2307ec481de96e070635baf5c77(
    *,
    object: builtins.str,
    enable_dynamic_field_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_deleted_records: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e5944d396eaa65c18b0b184d20b092353bd232b3071af67d1f4668a3a6cb830(
    *,
    schedule_expression: builtins.str,
    data_pull_mode: typing.Optional[builtins.str] = None,
    first_execution_from: typing.Optional[jsii.Number] = None,
    schedule_end_time: typing.Optional[jsii.Number] = None,
    schedule_offset: typing.Optional[jsii.Number] = None,
    schedule_start_time: typing.Optional[jsii.Number] = None,
    timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e39d4ec6bb5656a7c82bcb644c1e71ed86635052e302daedb141f92c9338d5e(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__886a4a6c1d593aa53fe13ccd79b82bf91be008e3952bb987ac48d2b64b7a6ac9(
    *,
    marketo: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.MarketoSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.S3SourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    salesforce: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.SalesforceSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_now: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ServiceNowSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    zendesk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ZendeskSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55d9871f7bd0e95109d517268a1cdd0da37965b7b7acd24cb1bfd91cacda7d2f(
    *,
    connector_type: builtins.str,
    source_connector_properties: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.SourceConnectorPropertiesProperty, typing.Dict[builtins.str, typing.Any]]],
    connector_profile_name: typing.Optional[builtins.str] = None,
    incremental_pull_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.IncrementalPullConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8a6d70493dcc8d57205e11e51993268d52dac180561f2ae05a6aa7eba5fab11(
    *,
    operator_property_key: builtins.str,
    property: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c97356b1cf286df38ebed38c9f4ce8135e5160a1254e87e74e1baaba8f2149f(
    *,
    source_fields: typing.Sequence[builtins.str],
    task_type: builtins.str,
    connector_operator: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ConnectorOperatorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    destination_field: typing.Optional[builtins.str] = None,
    task_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.TaskPropertiesMapProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43314febd76ccf4bc3946158640fcdb8e8e2b2e8aa92fe065358b557e5787cdc(
    *,
    trigger_type: builtins.str,
    trigger_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.TriggerPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d95880464ba4d79437e95620f7b099ab48173665d71b3b3e9925b31023ae79a(
    *,
    scheduled: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ScheduledTriggerPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fec16a3ec50ec7d597e7573ae1e24e531163b732505e322d5ef39e9267351db(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52bfebce0bd12cb9d9ed6354b0627c3f2946899ecf1ba8120aa70c1e1e22428d(
    *,
    domain_name: builtins.str,
    event_trigger_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    flow_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.FlowDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    object_type_name: typing.Optional[builtins.str] = None,
    object_type_names: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ObjectTypeMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e58419cb0a7694b5c554275a8721df95dc40489e742a23c76f7830ca5210127a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: builtins.str,
    domain_name: builtins.str,
    object_type_name: builtins.str,
    allow_profile_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    encryption_key: typing.Optional[builtins.str] = None,
    expiration_days: typing.Optional[jsii.Number] = None,
    fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.FieldMapProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.KeyMapProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    max_profile_object_count: typing.Optional[jsii.Number] = None,
    source_last_updated_timestamp_format: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__091e212a123e3a0cfb8577aebb7068432007378feb06e4af48a00036957ea470(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0769bdf04f2e44acf0d6aa58be6958449e3ed7487344183891e249f5aefe6bea(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aba990030ebf284cb51fc495ba3f894a3828072faa9f459784674e3467c4e696(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b24cea9cf31f287c3b3c148ba0586506624f0432fe276fdb1ec08d552833ef32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19dbd5a494e7060e32b7c4cc781d4cee2093bd041be3baf6d8b03e5f66d76985(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b0f4dc9c396c634c5fa55ab6032956c1c94c0dec83e089c60d92fb58640061c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ca3be4f6e2ca6127ac1ca1adcf9552041402fd0c44217f1d4f13a4e14bf2b40(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64d57ec4a44e9d66c50a3e82cedcef4d73b7c54672341cb6bdc26bb43d5048de(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eccf30ab38ee3158514f0243fca4f8f7f38ae86489a3784a2fee01eb15f10f58(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnObjectType.FieldMapProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__521c1a4bfa097c3b1f3951ecd6980736e1de35a3bfe50227b262534c59370624(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnObjectType.KeyMapProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edf9f4ddaedd0b5a755b294f08376889d206a0ce1a397886e2483e9471c6b184(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc577e5c0fd1bd47194e04599a6df995f066e809b7c98cb3b2e9ef839eaca0bc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__034fbef34b9c45ddeef371cddf129b147eb3c6d5cb089d2a874dec871d849617(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c3516f296b116ed334a16a7f280bc13da509b7cc1b2d0f53992808db2bf0433(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed4b9fc776f1c6cc0260e8e465d5e13c160ba26b2ed598c73a7b95e98cf61c94(
    *,
    name: typing.Optional[builtins.str] = None,
    object_type_field: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.ObjectTypeFieldProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea3cec6c8d04e9528d2f478540e3895caf69bc8db4178642b943b32ed3f9261(
    *,
    name: typing.Optional[builtins.str] = None,
    object_type_key_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.ObjectTypeKeyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b178f0d9e90930c4a4fd81ab392ed9c808bb1ea28f32cdd69c558694300980b(
    *,
    content_type: typing.Optional[builtins.str] = None,
    source: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7448ca799e207118d55f0019b3c6c35b6416f32804761112746d00e405772897(
    *,
    field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    standard_identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__674aff1f8e16a6059ac0e56bfd831b21c20b3b3358878f53ea82ff2eea85954e(
    *,
    description: builtins.str,
    domain_name: builtins.str,
    object_type_name: builtins.str,
    allow_profile_creation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    encryption_key: typing.Optional[builtins.str] = None,
    expiration_days: typing.Optional[jsii.Number] = None,
    fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.FieldMapProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    keys: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObjectType.KeyMapProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    max_profile_object_count: typing.Optional[jsii.Number] = None,
    source_last_updated_timestamp_format: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__350e170fd13ca6586a78a39785ca961e3b7fa8982a5b03ff0799f34c2f12ea50(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    display_name: builtins.str,
    domain_name: builtins.str,
    segment_definition_name: builtins.str,
    segment_groups: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.SegmentGroupProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43053ca51dec7fe64d769d488c3ff627584d6d29c926079a5503cd0fa5fcb6ca(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c93dc972ce2f528b294beb14fd064d6205569b6d0b68a9397a753547674ae198(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05d7eb6c9916e03c3799e9d2016d81426c2f6d43e95689ce0af12bfe09e6549f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26ba965f3f83218ff70b8ea34f99b1d05bab7433a8807b2fbcdaf115b08b6ae9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bc5bbfa19f04ef37dd74fe0dab060cbd192ee5bb1b47e5b1508f67f27be5aa3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__744689fb47e84da608e8ce7c410f0a6489728b4132c9e51efab1802d01b77340(
    value: typing.Union[_IResolvable_da3f097b, CfnSegmentDefinition.SegmentGroupProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__223f2ad9551b0ca745b7b727aa69f874d90c37d42f2d71a6e2b2fb44e7ade212(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__238b83e5f2661e205fa241820b4292d8a4cb4f60bf75be3b31f1b17711318539(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a0bc2d171c7abf0d09aef2749bfbe17beb9e940d0184742ad750455e61d50e9(
    *,
    city: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    country: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    county: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    postal_code: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    province: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb318635b9a0dfe69f39d22e3b143ff47d00d73e95ba7e6119cb5a713fe732dd(
    *,
    dimension_type: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a86c277d8f43a78bd0246d26e28cb0a8e84b0a5c96f8046b7d644735eb70d256(
    *,
    dimension_type: builtins.str,
    values: typing.Sequence[builtins.str],
    condition_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ConditionOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__805f367b5025255b85dff70d74ab17cdb3209b82d5159f03785caf2e4ea38c27(
    *,
    range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.RangeOverrideProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__321aa9ea2ffbe9c71ff0392adca1a155f2414f845fd6c463f7a0ea3785f7c270(
    *,
    dimension_type: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afcd95200751df2b6ea6aaaaadf0dca0e852f0fef263eeab7100a5c95ae82fc2(
    *,
    calculated_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.CalculatedAttributeDimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    profile_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7820cd9f215f422bb2ed34ea399f9c5252453574cd926e31a73fd9a12c28498(
    *,
    dimension_type: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d94bcaeaf726b09dbd09e1e48f12c042d531e9d0b092770695cebc3d52b5f5d(
    *,
    dimensions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.DimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_segments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.SourceSegmentProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_type: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3744d80b787b304270031bc1ba903495b3abb0c8edddf7fdffa36031caf48f(
    *,
    account_number: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    additional_information: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ExtraLengthValueProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.AddressDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.AttributeDimensionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    billing_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.AddressDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    birth_date: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.DateDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    business_email_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    business_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    business_phone_number: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    email_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    first_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    gender_string: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    home_phone_number: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    last_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mailing_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.AddressDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    middle_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mobile_phone_number: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    party_type_string: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    personal_email_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    phone_number: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    profile_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.ProfileTypeDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    shipping_address: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.AddressDimensionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__007e452519747d631a7d676cfec00290dff2452d6eaac4a54fc80925aca3d685(
    *,
    dimension_type: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__054d82d45b080caa1018b194962cae1c565d1648b07a9d3eb9b751a54d3c2b39(
    *,
    dimension_type: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca238704a173f3c1cf142a9086e33976f93d4c9bf252b6a1aac82208186ef3e5(
    *,
    start: jsii.Number,
    unit: builtins.str,
    end: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49a789743f5ac4162a8c53d6f5aae978c5989a590155f77804b52b37938d7672(
    *,
    groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.GroupProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    include: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__002c938fccce270fc597ae5653583b8a9910031239e0daaf523e0c4431d75ed7(
    *,
    segment_definition_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfe3927b013a59f4b37e001ce8d373fe3d8d8bc374ee6c206d37e74f69369348(
    *,
    display_name: builtins.str,
    domain_name: builtins.str,
    segment_definition_name: builtins.str,
    segment_groups: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSegmentDefinition.SegmentGroupProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
