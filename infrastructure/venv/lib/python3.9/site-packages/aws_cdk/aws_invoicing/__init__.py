r'''
# AWS::Invoicing Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_invoicing as invoicing
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Invoicing construct libraries](https://constructs.dev/search?q=invoicing)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Invoicing resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Invoicing.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Invoicing](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Invoicing.html).

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
class CfnInvoiceUnit(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_invoicing.CfnInvoiceUnit",
):
    '''An invoice unit is a set of mutually exclusive account that correspond to your business entity.

    Invoice units allow you separate AWS account costs and configures your invoice for each business entity going forward.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html
    :cloudformationResource: AWS::Invoicing::InvoiceUnit
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_invoicing as invoicing
        
        cfn_invoice_unit = invoicing.CfnInvoiceUnit(self, "MyCfnInvoiceUnit",
            invoice_receiver="invoiceReceiver",
            name="name",
            rule=invoicing.CfnInvoiceUnit.RuleProperty(
                linked_accounts=["linkedAccounts"]
            ),
        
            # the properties below are optional
            description="description",
            resource_tags=[invoicing.CfnInvoiceUnit.ResourceTagProperty(
                key="key",
                value="value"
            )],
            tax_inheritance_disabled=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        invoice_receiver: builtins.str,
        name: builtins.str,
        rule: typing.Union[_IResolvable_da3f097b, typing.Union["CfnInvoiceUnit.RuleProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        resource_tags: typing.Optional[typing.Sequence[typing.Union["CfnInvoiceUnit.ResourceTagProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tax_inheritance_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param invoice_receiver: The account that receives invoices related to the invoice unit.
        :param name: A unique name that is distinctive within your AWS .
        :param rule: An ``InvoiceUnitRule`` object used the categorize invoice units.
        :param description: The assigned description for an invoice unit. This information can't be modified or deleted.
        :param resource_tags: The tag structure that contains a tag key and value.
        :param tax_inheritance_disabled: Whether the invoice unit based tax inheritance is/ should be enabled or disabled.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec21d6093b38a709121aa7ff8c0297fdced84c912861970ec02e3bc317566bc6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInvoiceUnitProps(
            invoice_receiver=invoice_receiver,
            name=name,
            rule=rule,
            description=description,
            resource_tags=resource_tags,
            tax_inheritance_disabled=tax_inheritance_disabled,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adc114041b1663662392e373664cbecf8821f20a78009df2b54077dc4acd4a4f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__107a105e04f9f1089e314bd557a043d7c27143f765a9e1ea9ee1881882b1c045)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrInvoiceUnitArn")
    def attr_invoice_unit_arn(self) -> builtins.str:
        '''The ARN to identify an invoice unit.

        This information can't be modified or deleted.

        :cloudformationAttribute: InvoiceUnitArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrInvoiceUnitArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModified")
    def attr_last_modified(self) -> _IResolvable_da3f097b:
        '''The last time the invoice unit was updated.

        This is important to determine the version of invoice unit configuration used to create the invoices. Any invoice created after this modified time will use this invoice unit configuration.

        :cloudformationAttribute: LastModified
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLastModified"))

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
    @jsii.member(jsii_name="invoiceReceiver")
    def invoice_receiver(self) -> builtins.str:
        '''The account that receives invoices related to the invoice unit.'''
        return typing.cast(builtins.str, jsii.get(self, "invoiceReceiver"))

    @invoice_receiver.setter
    def invoice_receiver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__696a83d1411656063bc2e9712df3268ed2ef2248e55f5547394f8f5e78942d54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invoiceReceiver", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A unique name that is distinctive within your AWS .'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3aae9f9b97db34c63c2be162b2b82f9e0ec45cb8225187a2e441c3d9df5fc6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnInvoiceUnit.RuleProperty"]:
        '''An ``InvoiceUnitRule`` object used the categorize invoice units.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnInvoiceUnit.RuleProperty"], jsii.get(self, "rule"))

    @rule.setter
    def rule(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnInvoiceUnit.RuleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11bd3886ac3007b56aa51fb96bae09bccc9e9cc9c0abd45264540df233a478a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The assigned description for an invoice unit.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__076923c02da9e54ceab543bf61c811c9f8f6d99b2e479b043a782db5a4b4fa76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(
        self,
    ) -> typing.Optional[typing.List["CfnInvoiceUnit.ResourceTagProperty"]]:
        '''The tag structure that contains a tag key and value.'''
        return typing.cast(typing.Optional[typing.List["CfnInvoiceUnit.ResourceTagProperty"]], jsii.get(self, "resourceTags"))

    @resource_tags.setter
    def resource_tags(
        self,
        value: typing.Optional[typing.List["CfnInvoiceUnit.ResourceTagProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3778014062d8d17e79b38d529c3fb3bb66de99f01976014103eaa0ec3100ef9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="taxInheritanceDisabled")
    def tax_inheritance_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the invoice unit based tax inheritance is/ should be enabled or disabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "taxInheritanceDisabled"))

    @tax_inheritance_disabled.setter
    def tax_inheritance_disabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42f1928e769bc3f0a10f5fa89984b4cfd7df0a60a619ce30e6135776c65ea23b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taxInheritanceDisabled", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_invoicing.CfnInvoiceUnit.ResourceTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ResourceTagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''The tag structure that contains a tag key and value.

            :param key: The object key of your of your resource tag.
            :param value: The specific value of the resource tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-invoiceunit-resourcetag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_invoicing as invoicing
                
                resource_tag_property = invoicing.CfnInvoiceUnit.ResourceTagProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__859a6df074320cbe1a9099b42236f7d3759a4ce5419adf8bb3c001155a98ed4f)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The object key of your of your resource tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-invoiceunit-resourcetag.html#cfn-invoicing-invoiceunit-resourcetag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The specific value of the resource tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-invoiceunit-resourcetag.html#cfn-invoicing-invoiceunit-resourcetag-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
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
        jsii_type="aws-cdk-lib.aws_invoicing.CfnInvoiceUnit.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={"linked_accounts": "linkedAccounts"},
    )
    class RuleProperty:
        def __init__(self, *, linked_accounts: typing.Sequence[builtins.str]) -> None:
            '''The ``InvoiceUnitRule`` object used to update invoice units.

            :param linked_accounts: The list of ``LINKED_ACCOUNT`` IDs where charges are included within the invoice unit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-invoiceunit-rule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_invoicing as invoicing
                
                rule_property = invoicing.CfnInvoiceUnit.RuleProperty(
                    linked_accounts=["linkedAccounts"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8558be1d7f9b75065f54979d9fa00436e977578b77550f4c1d3e32a6b46a4bea)
                check_type(argname="argument linked_accounts", value=linked_accounts, expected_type=type_hints["linked_accounts"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "linked_accounts": linked_accounts,
            }

        @builtins.property
        def linked_accounts(self) -> typing.List[builtins.str]:
            '''The list of ``LINKED_ACCOUNT`` IDs where charges are included within the invoice unit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-invoicing-invoiceunit-rule.html#cfn-invoicing-invoiceunit-rule-linkedaccounts
            '''
            result = self._values.get("linked_accounts")
            assert result is not None, "Required property 'linked_accounts' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_invoicing.CfnInvoiceUnitProps",
    jsii_struct_bases=[],
    name_mapping={
        "invoice_receiver": "invoiceReceiver",
        "name": "name",
        "rule": "rule",
        "description": "description",
        "resource_tags": "resourceTags",
        "tax_inheritance_disabled": "taxInheritanceDisabled",
    },
)
class CfnInvoiceUnitProps:
    def __init__(
        self,
        *,
        invoice_receiver: builtins.str,
        name: builtins.str,
        rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInvoiceUnit.RuleProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        resource_tags: typing.Optional[typing.Sequence[typing.Union[CfnInvoiceUnit.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tax_inheritance_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInvoiceUnit``.

        :param invoice_receiver: The account that receives invoices related to the invoice unit.
        :param name: A unique name that is distinctive within your AWS .
        :param rule: An ``InvoiceUnitRule`` object used the categorize invoice units.
        :param description: The assigned description for an invoice unit. This information can't be modified or deleted.
        :param resource_tags: The tag structure that contains a tag key and value.
        :param tax_inheritance_disabled: Whether the invoice unit based tax inheritance is/ should be enabled or disabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_invoicing as invoicing
            
            cfn_invoice_unit_props = invoicing.CfnInvoiceUnitProps(
                invoice_receiver="invoiceReceiver",
                name="name",
                rule=invoicing.CfnInvoiceUnit.RuleProperty(
                    linked_accounts=["linkedAccounts"]
                ),
            
                # the properties below are optional
                description="description",
                resource_tags=[invoicing.CfnInvoiceUnit.ResourceTagProperty(
                    key="key",
                    value="value"
                )],
                tax_inheritance_disabled=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4fdf29b8c64b38c209320f998b71b0ce2601c2ac744bde28886f66b3cefdce6)
            check_type(argname="argument invoice_receiver", value=invoice_receiver, expected_type=type_hints["invoice_receiver"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
            check_type(argname="argument tax_inheritance_disabled", value=tax_inheritance_disabled, expected_type=type_hints["tax_inheritance_disabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "invoice_receiver": invoice_receiver,
            "name": name,
            "rule": rule,
        }
        if description is not None:
            self._values["description"] = description
        if resource_tags is not None:
            self._values["resource_tags"] = resource_tags
        if tax_inheritance_disabled is not None:
            self._values["tax_inheritance_disabled"] = tax_inheritance_disabled

    @builtins.property
    def invoice_receiver(self) -> builtins.str:
        '''The account that receives invoices related to the invoice unit.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html#cfn-invoicing-invoiceunit-invoicereceiver
        '''
        result = self._values.get("invoice_receiver")
        assert result is not None, "Required property 'invoice_receiver' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A unique name that is distinctive within your AWS .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html#cfn-invoicing-invoiceunit-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(self) -> typing.Union[_IResolvable_da3f097b, CfnInvoiceUnit.RuleProperty]:
        '''An ``InvoiceUnitRule`` object used the categorize invoice units.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html#cfn-invoicing-invoiceunit-rule
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnInvoiceUnit.RuleProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The assigned description for an invoice unit.

        This information can't be modified or deleted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html#cfn-invoicing-invoiceunit-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_tags(
        self,
    ) -> typing.Optional[typing.List[CfnInvoiceUnit.ResourceTagProperty]]:
        '''The tag structure that contains a tag key and value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html#cfn-invoicing-invoiceunit-resourcetags
        '''
        result = self._values.get("resource_tags")
        return typing.cast(typing.Optional[typing.List[CfnInvoiceUnit.ResourceTagProperty]], result)

    @builtins.property
    def tax_inheritance_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the invoice unit based tax inheritance is/ should be enabled or disabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-invoicing-invoiceunit.html#cfn-invoicing-invoiceunit-taxinheritancedisabled
        '''
        result = self._values.get("tax_inheritance_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInvoiceUnitProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnInvoiceUnit",
    "CfnInvoiceUnitProps",
]

publication.publish()

def _typecheckingstub__ec21d6093b38a709121aa7ff8c0297fdced84c912861970ec02e3bc317566bc6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    invoice_receiver: builtins.str,
    name: builtins.str,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInvoiceUnit.RuleProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    resource_tags: typing.Optional[typing.Sequence[typing.Union[CfnInvoiceUnit.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tax_inheritance_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adc114041b1663662392e373664cbecf8821f20a78009df2b54077dc4acd4a4f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__107a105e04f9f1089e314bd557a043d7c27143f765a9e1ea9ee1881882b1c045(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__696a83d1411656063bc2e9712df3268ed2ef2248e55f5547394f8f5e78942d54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3aae9f9b97db34c63c2be162b2b82f9e0ec45cb8225187a2e441c3d9df5fc6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11bd3886ac3007b56aa51fb96bae09bccc9e9cc9c0abd45264540df233a478a8(
    value: typing.Union[_IResolvable_da3f097b, CfnInvoiceUnit.RuleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__076923c02da9e54ceab543bf61c811c9f8f6d99b2e479b043a782db5a4b4fa76(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3778014062d8d17e79b38d529c3fb3bb66de99f01976014103eaa0ec3100ef9a(
    value: typing.Optional[typing.List[CfnInvoiceUnit.ResourceTagProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42f1928e769bc3f0a10f5fa89984b4cfd7df0a60a619ce30e6135776c65ea23b(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__859a6df074320cbe1a9099b42236f7d3759a4ce5419adf8bb3c001155a98ed4f(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8558be1d7f9b75065f54979d9fa00436e977578b77550f4c1d3e32a6b46a4bea(
    *,
    linked_accounts: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4fdf29b8c64b38c209320f998b71b0ce2601c2ac744bde28886f66b3cefdce6(
    *,
    invoice_receiver: builtins.str,
    name: builtins.str,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInvoiceUnit.RuleProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    resource_tags: typing.Optional[typing.Sequence[typing.Union[CfnInvoiceUnit.ResourceTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tax_inheritance_disabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass
