r'''
# AWS::NotificationsContacts Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_notificationscontacts as notificationscontacts
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for NotificationsContacts construct libraries](https://constructs.dev/search?q=notificationscontacts)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::NotificationsContacts resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NotificationsContacts.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::NotificationsContacts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NotificationsContacts.html).

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
class CfnEmailContact(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_notificationscontacts.CfnEmailContact",
):
    '''Configures email contacts for AWS User Notifications .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notificationscontacts-emailcontact.html
    :cloudformationResource: AWS::NotificationsContacts::EmailContact
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_notificationscontacts as notificationscontacts
        
        cfn_email_contact = notificationscontacts.CfnEmailContact(self, "MyCfnEmailContact",
            email_address="emailAddress",
            name="name",
        
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
        email_address: builtins.str,
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param email_address: The email address of the contact. The activation and notification emails are sent here.
        :param name: The name of the contact.
        :param tags: A list of tags to apply to the email contact.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1de25815cbc5e561d0f90c0eee8ffe57e0f8551698ba5a811da29f445a3d211b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEmailContactProps(email_address=email_address, name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6bae88336d9a51f69c3fc86da9d85ddead25993d2bc29fd415fa7b87726d0e7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__49a0a2d04984c43f3c80eb33fad944cd8b49b1fb73b667140e24f4f9a81d76ae)
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
        '''Returns the ARN of the contact.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEmailContact")
    def attr_email_contact(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: EmailContact
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrEmailContact"))

    @builtins.property
    @jsii.member(jsii_name="attrEmailContactAddress")
    def attr_email_contact_address(self) -> builtins.str:
        '''The email address of the contact.

        :cloudformationAttribute: EmailContact.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEmailContactAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrEmailContactArn")
    def attr_email_contact_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the contact.

        :cloudformationAttribute: EmailContact.Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEmailContactArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEmailContactCreationTime")
    def attr_email_contact_creation_time(self) -> builtins.str:
        '''The creation time of the ``EmailContact`` .

        :cloudformationAttribute: EmailContact.CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEmailContactCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrEmailContactName")
    def attr_email_contact_name(self) -> builtins.str:
        '''The name of the contact.

        :cloudformationAttribute: EmailContact.Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEmailContactName"))

    @builtins.property
    @jsii.member(jsii_name="attrEmailContactStatus")
    def attr_email_contact_status(self) -> builtins.str:
        '''The status of the contact.

        Only activated contacts receive emails.

        :cloudformationAttribute: EmailContact.Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEmailContactStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrEmailContactUpdateTime")
    def attr_email_contact_update_time(self) -> builtins.str:
        '''The time the ``EmailContact`` was last updated.

        :cloudformationAttribute: EmailContact.UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEmailContactUpdateTime"))

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
    @jsii.member(jsii_name="emailAddress")
    def email_address(self) -> builtins.str:
        '''The email address of the contact.'''
        return typing.cast(builtins.str, jsii.get(self, "emailAddress"))

    @email_address.setter
    def email_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad40c0465cbabf41bb2abf49dcce2989a3b42139c67d0d593acc1d1d67028e58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailAddress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the contact.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71ded19921304e3a6ee545520c16e2621065bcf6a576b5305f984c994ac9fe5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to apply to the email contact.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6155552227ec0ef011be7e784ffc90ecfddac06545f4d44a087256c3ef2ee22b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_notificationscontacts.CfnEmailContact.EmailContactProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address": "address",
            "arn": "arn",
            "creation_time": "creationTime",
            "name": "name",
            "status": "status",
            "update_time": "updateTime",
        },
    )
    class EmailContactProperty:
        def __init__(
            self,
            *,
            address: builtins.str,
            arn: builtins.str,
            creation_time: builtins.str,
            name: builtins.str,
            status: builtins.str,
            update_time: builtins.str,
        ) -> None:
            '''Configures email contacts for AWS User Notifications .

            You must activate the email contact using the activation token that you will receive when the email contact is set up.

            :param address: The email address of the contact.
            :param arn: The Amazon Resource Name (ARN) of the contact.
            :param creation_time: The creation time of the ``EmailContact`` .
            :param name: The name of the contact.
            :param status: The status of the contact. Only activated contacts receive emails.
            :param update_time: The time the ``EmailContact`` was last updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-notificationscontacts-emailcontact-emailcontact.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_notificationscontacts as notificationscontacts
                
                email_contact_property = notificationscontacts.CfnEmailContact.EmailContactProperty(
                    address="address",
                    arn="arn",
                    creation_time="creationTime",
                    name="name",
                    status="status",
                    update_time="updateTime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__48f41a7ff86bdb3f6536168c36c8ddd6876c1a2bfcd36169b53af9ce364e0eff)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument creation_time", value=creation_time, expected_type=type_hints["creation_time"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument update_time", value=update_time, expected_type=type_hints["update_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "address": address,
                "arn": arn,
                "creation_time": creation_time,
                "name": name,
                "status": status,
                "update_time": update_time,
            }

        @builtins.property
        def address(self) -> builtins.str:
            '''The email address of the contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-notificationscontacts-emailcontact-emailcontact.html#cfn-notificationscontacts-emailcontact-emailcontact-address
            '''
            result = self._values.get("address")
            assert result is not None, "Required property 'address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-notificationscontacts-emailcontact-emailcontact.html#cfn-notificationscontacts-emailcontact-emailcontact-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def creation_time(self) -> builtins.str:
            '''The creation time of the ``EmailContact`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-notificationscontacts-emailcontact-emailcontact.html#cfn-notificationscontacts-emailcontact-emailcontact-creationtime
            '''
            result = self._values.get("creation_time")
            assert result is not None, "Required property 'creation_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-notificationscontacts-emailcontact-emailcontact.html#cfn-notificationscontacts-emailcontact-emailcontact-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def status(self) -> builtins.str:
            '''The status of the contact.

            Only activated contacts receive emails.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-notificationscontacts-emailcontact-emailcontact.html#cfn-notificationscontacts-emailcontact-emailcontact-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def update_time(self) -> builtins.str:
            '''The time the ``EmailContact`` was last updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-notificationscontacts-emailcontact-emailcontact.html#cfn-notificationscontacts-emailcontact-emailcontact-updatetime
            '''
            result = self._values.get("update_time")
            assert result is not None, "Required property 'update_time' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmailContactProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_notificationscontacts.CfnEmailContactProps",
    jsii_struct_bases=[],
    name_mapping={"email_address": "emailAddress", "name": "name", "tags": "tags"},
)
class CfnEmailContactProps:
    def __init__(
        self,
        *,
        email_address: builtins.str,
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEmailContact``.

        :param email_address: The email address of the contact. The activation and notification emails are sent here.
        :param name: The name of the contact.
        :param tags: A list of tags to apply to the email contact.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notificationscontacts-emailcontact.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_notificationscontacts as notificationscontacts
            
            cfn_email_contact_props = notificationscontacts.CfnEmailContactProps(
                email_address="emailAddress",
                name="name",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7543e8bd10495fcc6c9e64b34fe84fba884f90162406e82ddba641f72f545e8)
            check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "email_address": email_address,
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def email_address(self) -> builtins.str:
        '''The email address of the contact.

        The activation and notification emails are sent here.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notificationscontacts-emailcontact.html#cfn-notificationscontacts-emailcontact-emailaddress
        '''
        result = self._values.get("email_address")
        assert result is not None, "Required property 'email_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the contact.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notificationscontacts-emailcontact.html#cfn-notificationscontacts-emailcontact-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to apply to the email contact.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-notificationscontacts-emailcontact.html#cfn-notificationscontacts-emailcontact-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEmailContactProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEmailContact",
    "CfnEmailContactProps",
]

publication.publish()

def _typecheckingstub__1de25815cbc5e561d0f90c0eee8ffe57e0f8551698ba5a811da29f445a3d211b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    email_address: builtins.str,
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6bae88336d9a51f69c3fc86da9d85ddead25993d2bc29fd415fa7b87726d0e7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49a0a2d04984c43f3c80eb33fad944cd8b49b1fb73b667140e24f4f9a81d76ae(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad40c0465cbabf41bb2abf49dcce2989a3b42139c67d0d593acc1d1d67028e58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71ded19921304e3a6ee545520c16e2621065bcf6a576b5305f984c994ac9fe5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6155552227ec0ef011be7e784ffc90ecfddac06545f4d44a087256c3ef2ee22b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48f41a7ff86bdb3f6536168c36c8ddd6876c1a2bfcd36169b53af9ce364e0eff(
    *,
    address: builtins.str,
    arn: builtins.str,
    creation_time: builtins.str,
    name: builtins.str,
    status: builtins.str,
    update_time: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7543e8bd10495fcc6c9e64b34fe84fba884f90162406e82ddba641f72f545e8(
    *,
    email_address: builtins.str,
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
