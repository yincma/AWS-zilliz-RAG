r'''
# AWS::Rbin Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_rbin as rbin
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Rbin construct libraries](https://constructs.dev/search?q=rbin)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Rbin resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Rbin.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Rbin](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Rbin.html).

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
class CfnRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_rbin.CfnRule",
):
    '''Creates a Recycle Bin retention rule. You can create two types of retention rules:.

    - *Tag-level retention rules* - These retention rules use resource tags to identify the resources to protect. For each retention rule, you specify one or more tag key and value pairs. Resources (of the specified type) that have at least one of these tag key and value pairs are automatically retained in the Recycle Bin upon deletion. Use this type of retention rule to protect specific resources in your account based on their tags.
    - *Region-level retention rules* - These retention rules, by default, apply to all of the resources (of the specified type) in the Region, even if the resources are not tagged. However, you can specify exclusion tags to exclude resources that have specific tags. Use this type of retention rule to protect all resources of a specific type in a Region.

    For more information, see `Create Recycle Bin retention rules <https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin.html>`_ in the *Amazon EBS User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rbin-rule.html
    :cloudformationResource: AWS::Rbin::Rule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_rbin as rbin
        
        cfn_rule = rbin.CfnRule(self, "MyCfnRule",
            resource_type="resourceType",
            retention_period=rbin.CfnRule.RetentionPeriodProperty(
                retention_period_unit="retentionPeriodUnit",
                retention_period_value=123
            ),
        
            # the properties below are optional
            description="description",
            exclude_resource_tags=[rbin.CfnRule.ResourceTagProperty(
                resource_tag_key="resourceTagKey",
                resource_tag_value="resourceTagValue"
            )],
            lock_configuration=rbin.CfnRule.UnlockDelayProperty(
                unlock_delay_unit="unlockDelayUnit",
                unlock_delay_value=123
            ),
            resource_tags=[rbin.CfnRule.ResourceTagProperty(
                resource_tag_key="resourceTagKey",
                resource_tag_value="resourceTagValue"
            )],
            status="status",
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
        resource_type: builtins.str,
        retention_period: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.RetentionPeriodProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        exclude_resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.ResourceTagProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        lock_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.UnlockDelayProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.ResourceTagProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resource_type: The resource type to be retained by the retention rule. Currently, only Amazon EBS snapshots and EBS-backed AMIs are supported. To retain snapshots, specify ``EBS_SNAPSHOT`` . To retain EBS-backed AMIs, specify ``EC2_IMAGE`` .
        :param retention_period: Information about the retention period for which the retention rule is to retain resources.
        :param description: The retention rule description.
        :param exclude_resource_tags: [Region-level retention rules only] Specifies the exclusion tags to use to identify resources that are to be excluded, or ignored, by a Region-level retention rule. Resources that have any of these tags are not retained by the retention rule upon deletion. You can't specify exclusion tags for tag-level retention rules.
        :param lock_configuration: Information about the retention rule lock configuration.
        :param resource_tags: [Tag-level retention rules only] Specifies the resource tags to use to identify resources that are to be retained by a tag-level retention rule. For tag-level retention rules, only deleted resources, of the specified resource type, that have one or more of the specified tag key and value pairs are retained. If a resource is deleted, but it does not have any of the specified tag key and value pairs, it is immediately deleted without being retained by the retention rule. You can add the same tag key and value pair to a maximum or five retention rules. To create a Region-level retention rule, omit this parameter. A Region-level retention rule does not have any resource tags specified. It retains all deleted resources of the specified resource type in the Region in which the rule is created, even if the resources are not tagged.
        :param status: The state of the retention rule. Only retention rules that are in the ``available`` state retain resources.
        :param tags: Information about the tags to assign to the retention rule.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38111a34066818ca2f172524180ec7dec02ce564c681ac0c87097b02350ebe17)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRuleProps(
            resource_type=resource_type,
            retention_period=retention_period,
            description=description,
            exclude_resource_tags=exclude_resource_tags,
            lock_configuration=lock_configuration,
            resource_tags=resource_tags,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5e2d558e79cd4c1853664243affb2788ae164a541fe9173013893487ad12468)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f8034d4fc6a3ab8d042623ec8857f056b79c1bd97f0d82b66729845c9f14fa5)
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
        '''The Amazon Resource Name (ARN) of the retention rule.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentifier")
    def attr_identifier(self) -> builtins.str:
        '''The unique ID of the retention rule.

        :cloudformationAttribute: Identifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrLockState")
    def attr_lock_state(self) -> builtins.str:
        '''[Region-level retention rules only] The lock state for the retention rule.

        - ``locked`` - The retention rule is locked and can't be modified or deleted.
        - ``pending_unlock`` - The retention rule has been unlocked but it is still within the unlock delay period. The retention rule can be modified or deleted only after the unlock delay period has expired.
        - ``unlocked`` - The retention rule is unlocked and it can be modified or deleted by any user with the required permissions.
        - ``null`` - The retention rule has never been locked. Once a retention rule has been locked, it can transition between the ``locked`` and ``unlocked`` states only; it can never transition back to ``null`` .

        :cloudformationAttribute: LockState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLockState"))

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
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The resource type to be retained by the retention rule.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c74a6102cda767f81d08a2ce4a9f380c01bef76688ed3f2426a6abc2f6878bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="retentionPeriod")
    def retention_period(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRule.RetentionPeriodProperty"]:
        '''Information about the retention period for which the retention rule is to retain resources.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRule.RetentionPeriodProperty"], jsii.get(self, "retentionPeriod"))

    @retention_period.setter
    def retention_period(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnRule.RetentionPeriodProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0d27934aff5d763d4a0cff90f748b18d817167613cec2de784a19e0980a2fe4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPeriod", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The retention rule description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3d64ebf98762cb6f5e840690eeebd382523d8cea931da2c8618a90f770698c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="excludeResourceTags")
    def exclude_resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.ResourceTagProperty"]]]]:
        '''[Region-level retention rules only] Specifies the exclusion tags to use to identify resources that are to be excluded, or ignored, by a Region-level retention rule.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.ResourceTagProperty"]]]], jsii.get(self, "excludeResourceTags"))

    @exclude_resource_tags.setter
    def exclude_resource_tags(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.ResourceTagProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20704aef7f8bc3c60046956bdcd1dc4e858b35b183e74b90587dae29d670872b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludeResourceTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lockConfiguration")
    def lock_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRule.UnlockDelayProperty"]]:
        '''Information about the retention rule lock configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRule.UnlockDelayProperty"]], jsii.get(self, "lockConfiguration"))

    @lock_configuration.setter
    def lock_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRule.UnlockDelayProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f565c87c44cc6deeef0351aeb8e4b8ead6860f0e90c735ebf7826cdbc04ae0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lockConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.ResourceTagProperty"]]]]:
        '''[Tag-level retention rules only] Specifies the resource tags to use to identify resources that are to be retained by a tag-level retention rule.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.ResourceTagProperty"]]]], jsii.get(self, "resourceTags"))

    @resource_tags.setter
    def resource_tags(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.ResourceTagProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e0b94a905f0a4a1448048e0ead85a45b5b5aa837fc74feedc20218875209250)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The state of the retention rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb14fdab3dd71774cb9bab4038b816ff578268a68dda7042fda45b88adf4a647)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Information about the tags to assign to the retention rule.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce724038f2c5f6b081624628cfc2e8ecba465376fcb9fc6a115d81b322693c72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rbin.CfnRule.ResourceTagProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resource_tag_key": "resourceTagKey",
            "resource_tag_value": "resourceTagValue",
        },
    )
    class ResourceTagProperty:
        def __init__(
            self,
            *,
            resource_tag_key: builtins.str,
            resource_tag_value: builtins.str,
        ) -> None:
            '''[Tag-level retention rules only] Information about the resource tags used to identify resources that are retained by the retention rule.

            :param resource_tag_key: The tag key.
            :param resource_tag_value: The tag value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rbin-rule-resourcetag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rbin as rbin
                
                resource_tag_property = rbin.CfnRule.ResourceTagProperty(
                    resource_tag_key="resourceTagKey",
                    resource_tag_value="resourceTagValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__86dbca3d8e90ed21aab495dd4465cd65c5600b932f6947382977ac6049cfdc9b)
                check_type(argname="argument resource_tag_key", value=resource_tag_key, expected_type=type_hints["resource_tag_key"])
                check_type(argname="argument resource_tag_value", value=resource_tag_value, expected_type=type_hints["resource_tag_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_tag_key": resource_tag_key,
                "resource_tag_value": resource_tag_value,
            }

        @builtins.property
        def resource_tag_key(self) -> builtins.str:
            '''The tag key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rbin-rule-resourcetag.html#cfn-rbin-rule-resourcetag-resourcetagkey
            '''
            result = self._values.get("resource_tag_key")
            assert result is not None, "Required property 'resource_tag_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_tag_value(self) -> builtins.str:
            '''The tag value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rbin-rule-resourcetag.html#cfn-rbin-rule-resourcetag-resourcetagvalue
            '''
            result = self._values.get("resource_tag_value")
            assert result is not None, "Required property 'resource_tag_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rbin.CfnRule.RetentionPeriodProperty",
        jsii_struct_bases=[],
        name_mapping={
            "retention_period_unit": "retentionPeriodUnit",
            "retention_period_value": "retentionPeriodValue",
        },
    )
    class RetentionPeriodProperty:
        def __init__(
            self,
            *,
            retention_period_unit: builtins.str,
            retention_period_value: jsii.Number,
        ) -> None:
            '''Information about the retention period for which the retention rule is to retain resources.

            :param retention_period_unit: The unit of time in which the retention period is measured. Currently, only ``DAYS`` is supported.
            :param retention_period_value: The period value for which the retention rule is to retain resources. The period is measured using the unit specified for *RetentionPeriodUnit* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rbin-rule-retentionperiod.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rbin as rbin
                
                retention_period_property = rbin.CfnRule.RetentionPeriodProperty(
                    retention_period_unit="retentionPeriodUnit",
                    retention_period_value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8c623c23074f8bcff0ea21ef370a8648f359985c15fca05e00e93100e4fc5254)
                check_type(argname="argument retention_period_unit", value=retention_period_unit, expected_type=type_hints["retention_period_unit"])
                check_type(argname="argument retention_period_value", value=retention_period_value, expected_type=type_hints["retention_period_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "retention_period_unit": retention_period_unit,
                "retention_period_value": retention_period_value,
            }

        @builtins.property
        def retention_period_unit(self) -> builtins.str:
            '''The unit of time in which the retention period is measured.

            Currently, only ``DAYS`` is supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rbin-rule-retentionperiod.html#cfn-rbin-rule-retentionperiod-retentionperiodunit
            '''
            result = self._values.get("retention_period_unit")
            assert result is not None, "Required property 'retention_period_unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def retention_period_value(self) -> jsii.Number:
            '''The period value for which the retention rule is to retain resources.

            The period is measured using the unit specified for *RetentionPeriodUnit* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rbin-rule-retentionperiod.html#cfn-rbin-rule-retentionperiod-retentionperiodvalue
            '''
            result = self._values.get("retention_period_value")
            assert result is not None, "Required property 'retention_period_value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetentionPeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rbin.CfnRule.UnlockDelayProperty",
        jsii_struct_bases=[],
        name_mapping={
            "unlock_delay_unit": "unlockDelayUnit",
            "unlock_delay_value": "unlockDelayValue",
        },
    )
    class UnlockDelayProperty:
        def __init__(
            self,
            *,
            unlock_delay_unit: typing.Optional[builtins.str] = None,
            unlock_delay_value: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Information about the retention rule unlock delay.

            The unlock delay is the period after which a retention rule can be modified or edited after it has been unlocked by a user with the required permissions. The retention rule can't be modified or deleted during the unlock delay.

            :param unlock_delay_unit: The unit of time in which to measure the unlock delay. Currently, the unlock delay can be measure only in days.
            :param unlock_delay_value: The unlock delay period, measured in the unit specified for *UnlockDelayUnit* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rbin-rule-unlockdelay.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rbin as rbin
                
                unlock_delay_property = rbin.CfnRule.UnlockDelayProperty(
                    unlock_delay_unit="unlockDelayUnit",
                    unlock_delay_value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d5cb70d54df5cb782865dd65947c16d9455e200989ec0b11ea250d28107e4894)
                check_type(argname="argument unlock_delay_unit", value=unlock_delay_unit, expected_type=type_hints["unlock_delay_unit"])
                check_type(argname="argument unlock_delay_value", value=unlock_delay_value, expected_type=type_hints["unlock_delay_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if unlock_delay_unit is not None:
                self._values["unlock_delay_unit"] = unlock_delay_unit
            if unlock_delay_value is not None:
                self._values["unlock_delay_value"] = unlock_delay_value

        @builtins.property
        def unlock_delay_unit(self) -> typing.Optional[builtins.str]:
            '''The unit of time in which to measure the unlock delay.

            Currently, the unlock delay can be measure only in days.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rbin-rule-unlockdelay.html#cfn-rbin-rule-unlockdelay-unlockdelayunit
            '''
            result = self._values.get("unlock_delay_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unlock_delay_value(self) -> typing.Optional[jsii.Number]:
            '''The unlock delay period, measured in the unit specified for *UnlockDelayUnit* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rbin-rule-unlockdelay.html#cfn-rbin-rule-unlockdelay-unlockdelayvalue
            '''
            result = self._values.get("unlock_delay_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UnlockDelayProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_rbin.CfnRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "resource_type": "resourceType",
        "retention_period": "retentionPeriod",
        "description": "description",
        "exclude_resource_tags": "excludeResourceTags",
        "lock_configuration": "lockConfiguration",
        "resource_tags": "resourceTags",
        "status": "status",
        "tags": "tags",
    },
)
class CfnRuleProps:
    def __init__(
        self,
        *,
        resource_type: builtins.str,
        retention_period: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.RetentionPeriodProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        exclude_resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        lock_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.UnlockDelayProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRule``.

        :param resource_type: The resource type to be retained by the retention rule. Currently, only Amazon EBS snapshots and EBS-backed AMIs are supported. To retain snapshots, specify ``EBS_SNAPSHOT`` . To retain EBS-backed AMIs, specify ``EC2_IMAGE`` .
        :param retention_period: Information about the retention period for which the retention rule is to retain resources.
        :param description: The retention rule description.
        :param exclude_resource_tags: [Region-level retention rules only] Specifies the exclusion tags to use to identify resources that are to be excluded, or ignored, by a Region-level retention rule. Resources that have any of these tags are not retained by the retention rule upon deletion. You can't specify exclusion tags for tag-level retention rules.
        :param lock_configuration: Information about the retention rule lock configuration.
        :param resource_tags: [Tag-level retention rules only] Specifies the resource tags to use to identify resources that are to be retained by a tag-level retention rule. For tag-level retention rules, only deleted resources, of the specified resource type, that have one or more of the specified tag key and value pairs are retained. If a resource is deleted, but it does not have any of the specified tag key and value pairs, it is immediately deleted without being retained by the retention rule. You can add the same tag key and value pair to a maximum or five retention rules. To create a Region-level retention rule, omit this parameter. A Region-level retention rule does not have any resource tags specified. It retains all deleted resources of the specified resource type in the Region in which the rule is created, even if the resources are not tagged.
        :param status: The state of the retention rule. Only retention rules that are in the ``available`` state retain resources.
        :param tags: Information about the tags to assign to the retention rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rbin-rule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_rbin as rbin
            
            cfn_rule_props = rbin.CfnRuleProps(
                resource_type="resourceType",
                retention_period=rbin.CfnRule.RetentionPeriodProperty(
                    retention_period_unit="retentionPeriodUnit",
                    retention_period_value=123
                ),
            
                # the properties below are optional
                description="description",
                exclude_resource_tags=[rbin.CfnRule.ResourceTagProperty(
                    resource_tag_key="resourceTagKey",
                    resource_tag_value="resourceTagValue"
                )],
                lock_configuration=rbin.CfnRule.UnlockDelayProperty(
                    unlock_delay_unit="unlockDelayUnit",
                    unlock_delay_value=123
                ),
                resource_tags=[rbin.CfnRule.ResourceTagProperty(
                    resource_tag_key="resourceTagKey",
                    resource_tag_value="resourceTagValue"
                )],
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f246c80846d7b6504b1f19f501c0aca8aa64ad2d5daf1c0f3c805f6f96d87faa)
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument retention_period", value=retention_period, expected_type=type_hints["retention_period"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument exclude_resource_tags", value=exclude_resource_tags, expected_type=type_hints["exclude_resource_tags"])
            check_type(argname="argument lock_configuration", value=lock_configuration, expected_type=type_hints["lock_configuration"])
            check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_type": resource_type,
            "retention_period": retention_period,
        }
        if description is not None:
            self._values["description"] = description
        if exclude_resource_tags is not None:
            self._values["exclude_resource_tags"] = exclude_resource_tags
        if lock_configuration is not None:
            self._values["lock_configuration"] = lock_configuration
        if resource_tags is not None:
            self._values["resource_tags"] = resource_tags
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''The resource type to be retained by the retention rule.

        Currently, only Amazon EBS snapshots and EBS-backed AMIs are supported. To retain snapshots, specify ``EBS_SNAPSHOT`` . To retain EBS-backed AMIs, specify ``EC2_IMAGE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rbin-rule.html#cfn-rbin-rule-resourcetype
        '''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention_period(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnRule.RetentionPeriodProperty]:
        '''Information about the retention period for which the retention rule is to retain resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rbin-rule.html#cfn-rbin-rule-retentionperiod
        '''
        result = self._values.get("retention_period")
        assert result is not None, "Required property 'retention_period' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnRule.RetentionPeriodProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The retention rule description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rbin-rule.html#cfn-rbin-rule-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclude_resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRule.ResourceTagProperty]]]]:
        '''[Region-level retention rules only] Specifies the exclusion tags to use to identify resources that are to be excluded, or ignored, by a Region-level retention rule.

        Resources that have any of these tags are not retained by the retention rule upon deletion.

        You can't specify exclusion tags for tag-level retention rules.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rbin-rule.html#cfn-rbin-rule-excluderesourcetags
        '''
        result = self._values.get("exclude_resource_tags")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRule.ResourceTagProperty]]]], result)

    @builtins.property
    def lock_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRule.UnlockDelayProperty]]:
        '''Information about the retention rule lock configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rbin-rule.html#cfn-rbin-rule-lockconfiguration
        '''
        result = self._values.get("lock_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRule.UnlockDelayProperty]], result)

    @builtins.property
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRule.ResourceTagProperty]]]]:
        '''[Tag-level retention rules only] Specifies the resource tags to use to identify resources that are to be retained by a tag-level retention rule.

        For tag-level retention rules, only deleted resources, of the specified resource type, that have one or more of the specified tag key and value pairs are retained. If a resource is deleted, but it does not have any of the specified tag key and value pairs, it is immediately deleted without being retained by the retention rule.

        You can add the same tag key and value pair to a maximum or five retention rules.

        To create a Region-level retention rule, omit this parameter. A Region-level retention rule does not have any resource tags specified. It retains all deleted resources of the specified resource type in the Region in which the rule is created, even if the resources are not tagged.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rbin-rule.html#cfn-rbin-rule-resourcetags
        '''
        result = self._values.get("resource_tags")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRule.ResourceTagProperty]]]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The state of the retention rule.

        Only retention rules that are in the ``available`` state retain resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rbin-rule.html#cfn-rbin-rule-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Information about the tags to assign to the retention rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rbin-rule.html#cfn-rbin-rule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnRule",
    "CfnRuleProps",
]

publication.publish()

def _typecheckingstub__38111a34066818ca2f172524180ec7dec02ce564c681ac0c87097b02350ebe17(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resource_type: builtins.str,
    retention_period: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.RetentionPeriodProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    exclude_resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    lock_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.UnlockDelayProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5e2d558e79cd4c1853664243affb2788ae164a541fe9173013893487ad12468(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f8034d4fc6a3ab8d042623ec8857f056b79c1bd97f0d82b66729845c9f14fa5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c74a6102cda767f81d08a2ce4a9f380c01bef76688ed3f2426a6abc2f6878bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0d27934aff5d763d4a0cff90f748b18d817167613cec2de784a19e0980a2fe4(
    value: typing.Union[_IResolvable_da3f097b, CfnRule.RetentionPeriodProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3d64ebf98762cb6f5e840690eeebd382523d8cea931da2c8618a90f770698c9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20704aef7f8bc3c60046956bdcd1dc4e858b35b183e74b90587dae29d670872b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRule.ResourceTagProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f565c87c44cc6deeef0351aeb8e4b8ead6860f0e90c735ebf7826cdbc04ae0a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRule.UnlockDelayProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e0b94a905f0a4a1448048e0ead85a45b5b5aa837fc74feedc20218875209250(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRule.ResourceTagProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb14fdab3dd71774cb9bab4038b816ff578268a68dda7042fda45b88adf4a647(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce724038f2c5f6b081624628cfc2e8ecba465376fcb9fc6a115d81b322693c72(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86dbca3d8e90ed21aab495dd4465cd65c5600b932f6947382977ac6049cfdc9b(
    *,
    resource_tag_key: builtins.str,
    resource_tag_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c623c23074f8bcff0ea21ef370a8648f359985c15fca05e00e93100e4fc5254(
    *,
    retention_period_unit: builtins.str,
    retention_period_value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5cb70d54df5cb782865dd65947c16d9455e200989ec0b11ea250d28107e4894(
    *,
    unlock_delay_unit: typing.Optional[builtins.str] = None,
    unlock_delay_value: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f246c80846d7b6504b1f19f501c0aca8aa64ad2d5daf1c0f3c805f6f96d87faa(
    *,
    resource_type: builtins.str,
    retention_period: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.RetentionPeriodProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    exclude_resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    lock_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.UnlockDelayProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
