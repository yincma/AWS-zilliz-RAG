r'''
# AWS::IoTSiteWise Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_iotsitewise as iotsitewise
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IoTSiteWise construct libraries](https://constructs.dev/search?q=iotsitewise)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IoTSiteWise resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTSiteWise.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IoTSiteWise](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTSiteWise.html).

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
class CfnAccessPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAccessPolicy",
):
    '''Creates an access policy that grants the specified identity (IAM Identity Center user, IAM Identity Center group, or IAM user) access to the specified AWS IoT SiteWise Monitor portal or project resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html
    :cloudformationResource: AWS::IoTSiteWise::AccessPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotsitewise as iotsitewise
        
        cfn_access_policy = iotsitewise.CfnAccessPolicy(self, "MyCfnAccessPolicy",
            access_policy_identity=iotsitewise.CfnAccessPolicy.AccessPolicyIdentityProperty(
                iam_role=iotsitewise.CfnAccessPolicy.IamRoleProperty(
                    arn="arn"
                ),
                iam_user=iotsitewise.CfnAccessPolicy.IamUserProperty(
                    arn="arn"
                ),
                user=iotsitewise.CfnAccessPolicy.UserProperty(
                    id="id"
                )
            ),
            access_policy_permission="accessPolicyPermission",
            access_policy_resource=iotsitewise.CfnAccessPolicy.AccessPolicyResourceProperty(
                portal=iotsitewise.CfnAccessPolicy.PortalProperty(
                    id="id"
                ),
                project=iotsitewise.CfnAccessPolicy.ProjectProperty(
                    id="id"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_policy_identity: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAccessPolicy.AccessPolicyIdentityProperty", typing.Dict[builtins.str, typing.Any]]],
        access_policy_permission: builtins.str,
        access_policy_resource: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAccessPolicy.AccessPolicyResourceProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param access_policy_identity: The identity for this access policy. Choose an IAM Identity Center user, an IAM Identity Center group, or an IAM user.
        :param access_policy_permission: The permission level for this access policy. Note that a project ``ADMINISTRATOR`` is also known as a project owner.
        :param access_policy_resource: The AWS IoT SiteWise Monitor resource for this access policy. Choose either a portal or a project.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__531aa21f3bed6dedfd9fce9d7bb67acf86efe74ca96cafedea1800e8112b281b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccessPolicyProps(
            access_policy_identity=access_policy_identity,
            access_policy_permission=access_policy_permission,
            access_policy_resource=access_policy_resource,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7c314721c2fd001464c0deebc3b8d42528f0226fb07963546a560eee048707a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d01f88f7fe294002e36ddfd24dba681b851b96f9e5b026a4da2d13fe47035504)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAccessPolicyArn")
    def attr_access_policy_arn(self) -> builtins.str:
        '''The `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ of the access policy, which has the following format.

        ``arn:${Partition}:iotsitewise:${Region}:${Account}:access-policy/${AccessPolicyId}``

        :cloudformationAttribute: AccessPolicyArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccessPolicyArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAccessPolicyId")
    def attr_access_policy_id(self) -> builtins.str:
        '''The ID of the access policy.

        :cloudformationAttribute: AccessPolicyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccessPolicyId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="accessPolicyIdentity")
    def access_policy_identity(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.AccessPolicyIdentityProperty"]:
        '''The identity for this access policy.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.AccessPolicyIdentityProperty"], jsii.get(self, "accessPolicyIdentity"))

    @access_policy_identity.setter
    def access_policy_identity(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.AccessPolicyIdentityProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2415091a9e2f73b7c84f270a46cb74a20cbda551668c1888f3deca22ef17375a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessPolicyIdentity", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="accessPolicyPermission")
    def access_policy_permission(self) -> builtins.str:
        '''The permission level for this access policy.'''
        return typing.cast(builtins.str, jsii.get(self, "accessPolicyPermission"))

    @access_policy_permission.setter
    def access_policy_permission(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__818cb88e831e00c87bc949084acafc61e7b103360b6efa353d0949058b3af434)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessPolicyPermission", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="accessPolicyResource")
    def access_policy_resource(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.AccessPolicyResourceProperty"]:
        '''The AWS IoT SiteWise Monitor resource for this access policy.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.AccessPolicyResourceProperty"], jsii.get(self, "accessPolicyResource"))

    @access_policy_resource.setter
    def access_policy_resource(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.AccessPolicyResourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__411d422b3be028b917aa7b3dbac61d64724f4eade2fcacd4bcf9431699d87cda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessPolicyResource", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAccessPolicy.AccessPolicyIdentityProperty",
        jsii_struct_bases=[],
        name_mapping={"iam_role": "iamRole", "iam_user": "iamUser", "user": "user"},
    )
    class AccessPolicyIdentityProperty:
        def __init__(
            self,
            *,
            iam_role: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAccessPolicy.IamRoleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            iam_user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAccessPolicy.IamUserProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAccessPolicy.UserProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The identity (IAM Identity Center user, IAM Identity Center group, or IAM user) to which this access policy applies.

            :param iam_role: An IAM role identity.
            :param iam_user: An IAM user identity.
            :param user: An IAM Identity Center user identity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                access_policy_identity_property = iotsitewise.CfnAccessPolicy.AccessPolicyIdentityProperty(
                    iam_role=iotsitewise.CfnAccessPolicy.IamRoleProperty(
                        arn="arn"
                    ),
                    iam_user=iotsitewise.CfnAccessPolicy.IamUserProperty(
                        arn="arn"
                    ),
                    user=iotsitewise.CfnAccessPolicy.UserProperty(
                        id="id"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e2d486ca8cf2592ca8b37c9d0e3cb26ad139033da3d5cef4d0958898a1f3e228)
                check_type(argname="argument iam_role", value=iam_role, expected_type=type_hints["iam_role"])
                check_type(argname="argument iam_user", value=iam_user, expected_type=type_hints["iam_user"])
                check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if iam_role is not None:
                self._values["iam_role"] = iam_role
            if iam_user is not None:
                self._values["iam_user"] = iam_user
            if user is not None:
                self._values["user"] = user

        @builtins.property
        def iam_role(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.IamRoleProperty"]]:
            '''An IAM role identity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity-iamrole
            '''
            result = self._values.get("iam_role")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.IamRoleProperty"]], result)

        @builtins.property
        def iam_user(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.IamUserProperty"]]:
            '''An IAM user identity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity-iamuser
            '''
            result = self._values.get("iam_user")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.IamUserProperty"]], result)

        @builtins.property
        def user(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.UserProperty"]]:
            '''An IAM Identity Center user identity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyidentity.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity-user
            '''
            result = self._values.get("user")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.UserProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessPolicyIdentityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAccessPolicy.AccessPolicyResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"portal": "portal", "project": "project"},
    )
    class AccessPolicyResourceProperty:
        def __init__(
            self,
            *,
            portal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAccessPolicy.PortalProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            project: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAccessPolicy.ProjectProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The AWS IoT SiteWise Monitor resource for this access policy.

            Choose either a portal or a project.

            :param portal: Identifies an AWS IoT SiteWise Monitor portal.
            :param project: Identifies a specific AWS IoT SiteWise Monitor project.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                access_policy_resource_property = iotsitewise.CfnAccessPolicy.AccessPolicyResourceProperty(
                    portal=iotsitewise.CfnAccessPolicy.PortalProperty(
                        id="id"
                    ),
                    project=iotsitewise.CfnAccessPolicy.ProjectProperty(
                        id="id"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__765b4d883deb51ec44680a76cffbd0a2ab68fee759c8b28c86b9f59498c31af2)
                check_type(argname="argument portal", value=portal, expected_type=type_hints["portal"])
                check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if portal is not None:
                self._values["portal"] = portal
            if project is not None:
                self._values["project"] = project

        @builtins.property
        def portal(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.PortalProperty"]]:
            '''Identifies an AWS IoT SiteWise Monitor portal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyresource.html#cfn-iotsitewise-accesspolicy-accesspolicyresource-portal
            '''
            result = self._values.get("portal")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.PortalProperty"]], result)

        @builtins.property
        def project(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.ProjectProperty"]]:
            '''Identifies a specific AWS IoT SiteWise Monitor project.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-accesspolicyresource.html#cfn-iotsitewise-accesspolicy-accesspolicyresource-project
            '''
            result = self._values.get("project")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAccessPolicy.ProjectProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessPolicyResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAccessPolicy.IamRoleProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class IamRoleProperty:
        def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
            '''Contains information about an AWS Identity and Access Management role.

            For more information, see `IAM roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`_ in the *IAM User Guide* .

            :param arn: The ARN of the IAM role. For more information, see `IAM ARNs <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`_ in the *IAM User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamrole.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                iam_role_property = iotsitewise.CfnAccessPolicy.IamRoleProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1f5cf7bcba5c6d5ceddf0ec6c4ef4ac1e8f801d29e104b8acac16b1b29340586)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the IAM role.

            For more information, see `IAM ARNs <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`_ in the *IAM User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamrole.html#cfn-iotsitewise-accesspolicy-iamrole-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamRoleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAccessPolicy.IamUserProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class IamUserProperty:
        def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
            '''Contains information about an AWS Identity and Access Management user.

            :param arn: The ARN of the IAM user. For more information, see `IAM ARNs <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`_ in the *IAM User Guide* . .. epigraph:: If you delete the IAM user, access policies that contain this identity include an empty ``arn`` . You can delete the access policy for the IAM user that no longer exists.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamuser.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                iam_user_property = iotsitewise.CfnAccessPolicy.IamUserProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__432609e44b579a8a90c10739f068d0000939943a6fe45469f4f1ae467aa2f163)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the IAM user. For more information, see `IAM ARNs <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`_ in the *IAM User Guide* .

            .. epigraph::

               If you delete the IAM user, access policies that contain this identity include an empty ``arn`` . You can delete the access policy for the IAM user that no longer exists.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-iamuser.html#cfn-iotsitewise-accesspolicy-iamuser-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamUserProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAccessPolicy.PortalProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id"},
    )
    class PortalProperty:
        def __init__(self, *, id: typing.Optional[builtins.str] = None) -> None:
            '''Identifies an AWS IoT SiteWise Monitor portal.

            :param id: The ID of the portal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-portal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                portal_property = iotsitewise.CfnAccessPolicy.PortalProperty(
                    id="id"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__143d119625b35bf1029bcedc015ee7c97453389b6fd03e0a75c41d6e12e704b9)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The ID of the portal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-portal.html#cfn-iotsitewise-accesspolicy-portal-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAccessPolicy.ProjectProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id"},
    )
    class ProjectProperty:
        def __init__(self, *, id: typing.Optional[builtins.str] = None) -> None:
            '''Identifies a specific AWS IoT SiteWise Monitor project.

            :param id: The ID of the project.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-project.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                project_property = iotsitewise.CfnAccessPolicy.ProjectProperty(
                    id="id"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__13bff317a735a1083b2976369b994f0f31c739c79d78584197a9a73729daef99)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The ID of the project.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-project.html#cfn-iotsitewise-accesspolicy-project-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAccessPolicy.UserProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id"},
    )
    class UserProperty:
        def __init__(self, *, id: typing.Optional[builtins.str] = None) -> None:
            '''Contains information for a user identity in an access policy.

            :param id: The IAM Identity Center ID of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-user.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                user_property = iotsitewise.CfnAccessPolicy.UserProperty(
                    id="id"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f363729f07f015fc23f72b53be5071c8dc7624eb969069e23f064b035b2c023c)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The IAM Identity Center ID of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-accesspolicy-user.html#cfn-iotsitewise-accesspolicy-user-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAccessPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_policy_identity": "accessPolicyIdentity",
        "access_policy_permission": "accessPolicyPermission",
        "access_policy_resource": "accessPolicyResource",
    },
)
class CfnAccessPolicyProps:
    def __init__(
        self,
        *,
        access_policy_identity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPolicy.AccessPolicyIdentityProperty, typing.Dict[builtins.str, typing.Any]]],
        access_policy_permission: builtins.str,
        access_policy_resource: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPolicy.AccessPolicyResourceProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnAccessPolicy``.

        :param access_policy_identity: The identity for this access policy. Choose an IAM Identity Center user, an IAM Identity Center group, or an IAM user.
        :param access_policy_permission: The permission level for this access policy. Note that a project ``ADMINISTRATOR`` is also known as a project owner.
        :param access_policy_resource: The AWS IoT SiteWise Monitor resource for this access policy. Choose either a portal or a project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotsitewise as iotsitewise
            
            cfn_access_policy_props = iotsitewise.CfnAccessPolicyProps(
                access_policy_identity=iotsitewise.CfnAccessPolicy.AccessPolicyIdentityProperty(
                    iam_role=iotsitewise.CfnAccessPolicy.IamRoleProperty(
                        arn="arn"
                    ),
                    iam_user=iotsitewise.CfnAccessPolicy.IamUserProperty(
                        arn="arn"
                    ),
                    user=iotsitewise.CfnAccessPolicy.UserProperty(
                        id="id"
                    )
                ),
                access_policy_permission="accessPolicyPermission",
                access_policy_resource=iotsitewise.CfnAccessPolicy.AccessPolicyResourceProperty(
                    portal=iotsitewise.CfnAccessPolicy.PortalProperty(
                        id="id"
                    ),
                    project=iotsitewise.CfnAccessPolicy.ProjectProperty(
                        id="id"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__395192fc212cfba19ac0d48ac6224771ee93f01bee507a5e9571a735a417decd)
            check_type(argname="argument access_policy_identity", value=access_policy_identity, expected_type=type_hints["access_policy_identity"])
            check_type(argname="argument access_policy_permission", value=access_policy_permission, expected_type=type_hints["access_policy_permission"])
            check_type(argname="argument access_policy_resource", value=access_policy_resource, expected_type=type_hints["access_policy_resource"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_policy_identity": access_policy_identity,
            "access_policy_permission": access_policy_permission,
            "access_policy_resource": access_policy_resource,
        }

    @builtins.property
    def access_policy_identity(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAccessPolicy.AccessPolicyIdentityProperty]:
        '''The identity for this access policy.

        Choose an IAM Identity Center user, an IAM Identity Center group, or an IAM user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicyidentity
        '''
        result = self._values.get("access_policy_identity")
        assert result is not None, "Required property 'access_policy_identity' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAccessPolicy.AccessPolicyIdentityProperty], result)

    @builtins.property
    def access_policy_permission(self) -> builtins.str:
        '''The permission level for this access policy.

        Note that a project ``ADMINISTRATOR`` is also known as a project owner.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicypermission
        '''
        result = self._values.get("access_policy_permission")
        assert result is not None, "Required property 'access_policy_permission' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_policy_resource(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAccessPolicy.AccessPolicyResourceProperty]:
        '''The AWS IoT SiteWise Monitor resource for this access policy.

        Choose either a portal or a project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-accesspolicy.html#cfn-iotsitewise-accesspolicy-accesspolicyresource
        '''
        result = self._values.get("access_policy_resource")
        assert result is not None, "Required property 'access_policy_resource' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAccessPolicy.AccessPolicyResourceProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccessPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnAsset(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAsset",
):
    '''Creates an asset from an existing asset model.

    For more information, see `Creating assets <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-assets.html>`_ in the *AWS IoT SiteWise User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html
    :cloudformationResource: AWS::IoTSiteWise::Asset
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotsitewise as iotsitewise
        
        cfn_asset = iotsitewise.CfnAsset(self, "MyCfnAsset",
            asset_model_id="assetModelId",
            asset_name="assetName",
        
            # the properties below are optional
            asset_description="assetDescription",
            asset_external_id="assetExternalId",
            asset_hierarchies=[iotsitewise.CfnAsset.AssetHierarchyProperty(
                child_asset_id="childAssetId",
        
                # the properties below are optional
                external_id="externalId",
                id="id",
                logical_id="logicalId"
            )],
            asset_properties=[iotsitewise.CfnAsset.AssetPropertyProperty(
                alias="alias",
                external_id="externalId",
                id="id",
                logical_id="logicalId",
                notification_state="notificationState",
                unit="unit"
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
        asset_model_id: builtins.str,
        asset_name: builtins.str,
        asset_description: typing.Optional[builtins.str] = None,
        asset_external_id: typing.Optional[builtins.str] = None,
        asset_hierarchies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAsset.AssetHierarchyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        asset_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAsset.AssetPropertyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param asset_model_id: The ID of the asset model from which to create the asset. This can be either the actual ID in UUID format, or else ``externalId:`` followed by the external ID, if it has one. For more information, see `Referencing objects with external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references>`_ in the *AWS IoT SiteWise User Guide* .
        :param asset_name: A friendly name for the asset.
        :param asset_description: The ID of the asset, in UUID format.
        :param asset_external_id: The external ID of the asset model composite model. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .
        :param asset_hierarchies: A list of asset hierarchies that each contain a ``hierarchyId`` . A hierarchy specifies allowed parent/child asset relationships.
        :param asset_properties: The list of asset properties for the asset. This object doesn't include properties that you define in composite models. You can find composite model properties in the ``assetCompositeModels`` object.
        :param tags: A list of key-value pairs that contain metadata for the asset. For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23b484c08f8b327d7857c955867af231fc3193cc5df788160c4e1c6e326075b1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssetProps(
            asset_model_id=asset_model_id,
            asset_name=asset_name,
            asset_description=asset_description,
            asset_external_id=asset_external_id,
            asset_hierarchies=asset_hierarchies,
            asset_properties=asset_properties,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__102e5bd91193367af65b5d5491e5dd31e20ce7e2d4a10294b8a904b2294f035c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8036de54cbe0f29f20898cb6faa8d078fdb3b445a95f607b80032b1561c7fef2)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssetArn")
    def attr_asset_arn(self) -> builtins.str:
        '''The ARN of the asset.

        :cloudformationAttribute: AssetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssetArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssetId")
    def attr_asset_id(self) -> builtins.str:
        '''The ID of the asset.

        :cloudformationAttribute: AssetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssetId"))

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
    @jsii.member(jsii_name="assetModelId")
    def asset_model_id(self) -> builtins.str:
        '''The ID of the asset model from which to create the asset.'''
        return typing.cast(builtins.str, jsii.get(self, "assetModelId"))

    @asset_model_id.setter
    def asset_model_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e944261c39c832f5a26bb7510ff2565f5b578ad73aa1c03c10b468a125df4e0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetModelId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assetName")
    def asset_name(self) -> builtins.str:
        '''A friendly name for the asset.'''
        return typing.cast(builtins.str, jsii.get(self, "assetName"))

    @asset_name.setter
    def asset_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2dc507f393cf1c06a074a018c9e9db507f543807826f4e8fa45ee4df4d527e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assetDescription")
    def asset_description(self) -> typing.Optional[builtins.str]:
        '''The ID of the asset, in UUID format.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assetDescription"))

    @asset_description.setter
    def asset_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__846aec2a49e7d9368d2d62f013b975b4b8e383e34d606cf26025fa1e9c1f080e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetDescription", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assetExternalId")
    def asset_external_id(self) -> typing.Optional[builtins.str]:
        '''The external ID of the asset model composite model.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assetExternalId"))

    @asset_external_id.setter
    def asset_external_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__774f36beafbc5ecee60ee64670d06a55e1d63cae97a7bf37614ae9a5662e5bb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetExternalId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assetHierarchies")
    def asset_hierarchies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAsset.AssetHierarchyProperty"]]]]:
        '''A list of asset hierarchies that each contain a ``hierarchyId`` .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAsset.AssetHierarchyProperty"]]]], jsii.get(self, "assetHierarchies"))

    @asset_hierarchies.setter
    def asset_hierarchies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAsset.AssetHierarchyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54fdb5abb9d6b9f05e9d300d7d933adae0aed3f34ae2309c30c6ed3f6d1d6517)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetHierarchies", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assetProperties")
    def asset_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAsset.AssetPropertyProperty"]]]]:
        '''The list of asset properties for the asset.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAsset.AssetPropertyProperty"]]]], jsii.get(self, "assetProperties"))

    @asset_properties.setter
    def asset_properties(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAsset.AssetPropertyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba341fa6fbf95a16923570d24a7123b2633590b82a24b510405c0e43e73829bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetProperties", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the asset.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95733b024c1a6ce8bc474f669fc60c5ec6406e7dd1eb8029bb8e07049a3ce2a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAsset.AssetHierarchyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "child_asset_id": "childAssetId",
            "external_id": "externalId",
            "id": "id",
            "logical_id": "logicalId",
        },
    )
    class AssetHierarchyProperty:
        def __init__(
            self,
            *,
            child_asset_id: builtins.str,
            external_id: typing.Optional[builtins.str] = None,
            id: typing.Optional[builtins.str] = None,
            logical_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an asset hierarchy that contains a hierarchy's name and ID.

            :param child_asset_id: The Id of the child asset.
            :param external_id: The external ID of the hierarchy, if it has one. When you update an asset hierarchy, you may assign an external ID if it doesn't already have one. You can't change the external ID of an asset hierarchy that already has one. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .
            :param id: The ID of the hierarchy. This ID is a ``hierarchyId`` . .. epigraph:: This is a return value and can't be set.
            :param logical_id: The ID of the hierarchy. This ID is a ``hierarchyId`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assethierarchy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                asset_hierarchy_property = iotsitewise.CfnAsset.AssetHierarchyProperty(
                    child_asset_id="childAssetId",
                
                    # the properties below are optional
                    external_id="externalId",
                    id="id",
                    logical_id="logicalId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b6404a33020d845fe84e2cc02f1ce61855b1caee959bf2437d88b3669ceecf46)
                check_type(argname="argument child_asset_id", value=child_asset_id, expected_type=type_hints["child_asset_id"])
                check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "child_asset_id": child_asset_id,
            }
            if external_id is not None:
                self._values["external_id"] = external_id
            if id is not None:
                self._values["id"] = id
            if logical_id is not None:
                self._values["logical_id"] = logical_id

        @builtins.property
        def child_asset_id(self) -> builtins.str:
            '''The Id of the child asset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assethierarchy.html#cfn-iotsitewise-asset-assethierarchy-childassetid
            '''
            result = self._values.get("child_asset_id")
            assert result is not None, "Required property 'child_asset_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID of the hierarchy, if it has one.

            When you update an asset hierarchy, you may assign an external ID if it doesn't already have one. You can't change the external ID of an asset hierarchy that already has one. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assethierarchy.html#cfn-iotsitewise-asset-assethierarchy-externalid
            '''
            result = self._values.get("external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The ID of the hierarchy. This ID is a ``hierarchyId`` .

            .. epigraph::

               This is a return value and can't be set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assethierarchy.html#cfn-iotsitewise-asset-assethierarchy-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def logical_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the hierarchy.

            This ID is a ``hierarchyId`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assethierarchy.html#cfn-iotsitewise-asset-assethierarchy-logicalid
            '''
            result = self._values.get("logical_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetHierarchyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAsset.AssetPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alias": "alias",
            "external_id": "externalId",
            "id": "id",
            "logical_id": "logicalId",
            "notification_state": "notificationState",
            "unit": "unit",
        },
    )
    class AssetPropertyProperty:
        def __init__(
            self,
            *,
            alias: typing.Optional[builtins.str] = None,
            external_id: typing.Optional[builtins.str] = None,
            id: typing.Optional[builtins.str] = None,
            logical_id: typing.Optional[builtins.str] = None,
            notification_state: typing.Optional[builtins.str] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains asset property information.

            :param alias: The alias that identifies the property, such as an OPC-UA server data stream path (for example, ``/company/windfarm/3/turbine/7/temperature`` ). For more information, see `Mapping industrial data streams to asset properties <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html>`_ in the *AWS IoT SiteWise User Guide* .
            :param external_id: The external ID of the property. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .
            :param id: The ID of the asset property. .. epigraph:: This is a return value and can't be set.
            :param logical_id: The ``LogicalID`` of the asset property.
            :param notification_state: The MQTT notification state (enabled or disabled) for this asset property. When the notification state is enabled, AWS IoT SiteWise publishes property value updates to a unique MQTT topic. For more information, see `Interacting with other services <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interact-with-other-services.html>`_ in the *AWS IoT SiteWise User Guide* . If you omit this parameter, the notification state is set to ``DISABLED`` .
            :param unit: The unit (such as ``Newtons`` or ``RPM`` ) of the asset property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                asset_property_property = iotsitewise.CfnAsset.AssetPropertyProperty(
                    alias="alias",
                    external_id="externalId",
                    id="id",
                    logical_id="logicalId",
                    notification_state="notificationState",
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c0a542963124a747730cbbfebfb49e3e50b517a00196aa1b2e31a5db31322e3e)
                check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
                check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
                check_type(argname="argument notification_state", value=notification_state, expected_type=type_hints["notification_state"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if alias is not None:
                self._values["alias"] = alias
            if external_id is not None:
                self._values["external_id"] = external_id
            if id is not None:
                self._values["id"] = id
            if logical_id is not None:
                self._values["logical_id"] = logical_id
            if notification_state is not None:
                self._values["notification_state"] = notification_state
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def alias(self) -> typing.Optional[builtins.str]:
            '''The alias that identifies the property, such as an OPC-UA server data stream path (for example, ``/company/windfarm/3/turbine/7/temperature`` ).

            For more information, see `Mapping industrial data streams to asset properties <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html#cfn-iotsitewise-asset-assetproperty-alias
            '''
            result = self._values.get("alias")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID of the property.

            For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html#cfn-iotsitewise-asset-assetproperty-externalid
            '''
            result = self._values.get("external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The ID of the asset property.

            .. epigraph::

               This is a return value and can't be set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html#cfn-iotsitewise-asset-assetproperty-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def logical_id(self) -> typing.Optional[builtins.str]:
            '''The ``LogicalID`` of the asset property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html#cfn-iotsitewise-asset-assetproperty-logicalid
            '''
            result = self._values.get("logical_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def notification_state(self) -> typing.Optional[builtins.str]:
            '''The MQTT notification state (enabled or disabled) for this asset property.

            When the notification state is enabled, AWS IoT SiteWise publishes property value updates to a unique MQTT topic. For more information, see `Interacting with other services <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interact-with-other-services.html>`_ in the *AWS IoT SiteWise User Guide* .

            If you omit this parameter, the notification state is set to ``DISABLED`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html#cfn-iotsitewise-asset-assetproperty-notificationstate
            '''
            result = self._values.get("notification_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''The unit (such as ``Newtons`` or ``RPM`` ) of the asset property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-asset-assetproperty.html#cfn-iotsitewise-asset-assetproperty-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnAssetModel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModel",
):
    '''Creates an asset model from specified property and hierarchy definitions.

    You create assets from asset models. With asset models, you can easily create assets of the same type that have standardized definitions. Each asset created from a model inherits the asset model's property and hierarchy definitions. For more information, see `Defining asset models <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/define-models.html>`_ in the *AWS IoT SiteWise User Guide* .

    You can create three types of asset models, ``ASSET_MODEL`` , ``COMPONENT_MODEL`` , or an ``INTERFACE`` .

    - *ASSET_MODEL* – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.
    - *COMPONENT_MODEL* – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model.
    - *INTERFACE* – An interface is a type of model that defines a standard structure that can be applied to different asset models.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html
    :cloudformationResource: AWS::IoTSiteWise::AssetModel
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotsitewise as iotsitewise
        
        cfn_asset_model = iotsitewise.CfnAssetModel(self, "MyCfnAssetModel",
            asset_model_name="assetModelName",
        
            # the properties below are optional
            asset_model_composite_models=[iotsitewise.CfnAssetModel.AssetModelCompositeModelProperty(
                name="name",
                type="type",
        
                # the properties below are optional
                composed_asset_model_id="composedAssetModelId",
                composite_model_properties=[iotsitewise.CfnAssetModel.AssetModelPropertyProperty(
                    data_type="dataType",
                    name="name",
                    type=iotsitewise.CfnAssetModel.PropertyTypeProperty(
                        type_name="typeName",
        
                        # the properties below are optional
                        attribute=iotsitewise.CfnAssetModel.AttributeProperty(
                            default_value="defaultValue"
                        ),
                        metric=iotsitewise.CfnAssetModel.MetricProperty(
                            expression="expression",
                            variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                                name="name",
                                value=iotsitewise.CfnAssetModel.VariableValueProperty(
                                    hierarchy_external_id="hierarchyExternalId",
                                    hierarchy_id="hierarchyId",
                                    hierarchy_logical_id="hierarchyLogicalId",
                                    property_external_id="propertyExternalId",
                                    property_id="propertyId",
                                    property_logical_id="propertyLogicalId",
                                    property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                        name="name"
                                    )]
                                )
                            )],
                            window=iotsitewise.CfnAssetModel.MetricWindowProperty(
                                tumbling=iotsitewise.CfnAssetModel.TumblingWindowProperty(
                                    interval="interval",
        
                                    # the properties below are optional
                                    offset="offset"
                                )
                            )
                        ),
                        transform=iotsitewise.CfnAssetModel.TransformProperty(
                            expression="expression",
                            variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                                name="name",
                                value=iotsitewise.CfnAssetModel.VariableValueProperty(
                                    hierarchy_external_id="hierarchyExternalId",
                                    hierarchy_id="hierarchyId",
                                    hierarchy_logical_id="hierarchyLogicalId",
                                    property_external_id="propertyExternalId",
                                    property_id="propertyId",
                                    property_logical_id="propertyLogicalId",
                                    property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                        name="name"
                                    )]
                                )
                            )]
                        )
                    ),
        
                    # the properties below are optional
                    data_type_spec="dataTypeSpec",
                    external_id="externalId",
                    id="id",
                    logical_id="logicalId",
                    unit="unit"
                )],
                description="description",
                external_id="externalId",
                id="id",
                parent_asset_model_composite_model_external_id="parentAssetModelCompositeModelExternalId",
                path=["path"]
            )],
            asset_model_description="assetModelDescription",
            asset_model_external_id="assetModelExternalId",
            asset_model_hierarchies=[iotsitewise.CfnAssetModel.AssetModelHierarchyProperty(
                child_asset_model_id="childAssetModelId",
                name="name",
        
                # the properties below are optional
                external_id="externalId",
                id="id",
                logical_id="logicalId"
            )],
            asset_model_properties=[iotsitewise.CfnAssetModel.AssetModelPropertyProperty(
                data_type="dataType",
                name="name",
                type=iotsitewise.CfnAssetModel.PropertyTypeProperty(
                    type_name="typeName",
        
                    # the properties below are optional
                    attribute=iotsitewise.CfnAssetModel.AttributeProperty(
                        default_value="defaultValue"
                    ),
                    metric=iotsitewise.CfnAssetModel.MetricProperty(
                        expression="expression",
                        variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                            name="name",
                            value=iotsitewise.CfnAssetModel.VariableValueProperty(
                                hierarchy_external_id="hierarchyExternalId",
                                hierarchy_id="hierarchyId",
                                hierarchy_logical_id="hierarchyLogicalId",
                                property_external_id="propertyExternalId",
                                property_id="propertyId",
                                property_logical_id="propertyLogicalId",
                                property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                    name="name"
                                )]
                            )
                        )],
                        window=iotsitewise.CfnAssetModel.MetricWindowProperty(
                            tumbling=iotsitewise.CfnAssetModel.TumblingWindowProperty(
                                interval="interval",
        
                                # the properties below are optional
                                offset="offset"
                            )
                        )
                    ),
                    transform=iotsitewise.CfnAssetModel.TransformProperty(
                        expression="expression",
                        variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                            name="name",
                            value=iotsitewise.CfnAssetModel.VariableValueProperty(
                                hierarchy_external_id="hierarchyExternalId",
                                hierarchy_id="hierarchyId",
                                hierarchy_logical_id="hierarchyLogicalId",
                                property_external_id="propertyExternalId",
                                property_id="propertyId",
                                property_logical_id="propertyLogicalId",
                                property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                    name="name"
                                )]
                            )
                        )]
                    )
                ),
        
                # the properties below are optional
                data_type_spec="dataTypeSpec",
                external_id="externalId",
                id="id",
                logical_id="logicalId",
                unit="unit"
            )],
            asset_model_type="assetModelType",
            enforced_asset_model_interface_relationships=[iotsitewise.CfnAssetModel.EnforcedAssetModelInterfaceRelationshipProperty(
                interface_asset_model_id="interfaceAssetModelId",
                property_mappings=[iotsitewise.CfnAssetModel.EnforcedAssetModelInterfacePropertyMappingProperty(
                    interface_asset_model_property_external_id="interfaceAssetModelPropertyExternalId",
        
                    # the properties below are optional
                    asset_model_property_external_id="assetModelPropertyExternalId",
                    asset_model_property_logical_id="assetModelPropertyLogicalId"
                )]
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
        asset_model_name: builtins.str,
        asset_model_composite_models: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.AssetModelCompositeModelProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        asset_model_description: typing.Optional[builtins.str] = None,
        asset_model_external_id: typing.Optional[builtins.str] = None,
        asset_model_hierarchies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.AssetModelHierarchyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        asset_model_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.AssetModelPropertyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        asset_model_type: typing.Optional[builtins.str] = None,
        enforced_asset_model_interface_relationships: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.EnforcedAssetModelInterfaceRelationshipProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param asset_model_name: A unique name for the asset model.
        :param asset_model_composite_models: The composite models that are part of this asset model. It groups properties (such as attributes, measurements, transforms, and metrics) and child composite models that model parts of your industrial equipment. Each composite model has a type that defines the properties that the composite model supports. Use composite models to define alarms on this asset model. .. epigraph:: When creating custom composite models, you need to use `CreateAssetModelCompositeModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html>`_ . For more information, see `Creating custom composite models (Components) <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-custom-composite-models.html>`_ in the *AWS IoT SiteWise User Guide* .
        :param asset_model_description: A description for the asset model.
        :param asset_model_external_id: The external ID of the asset model. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .
        :param asset_model_hierarchies: The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. For more information, see `Asset hierarchies <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html>`_ in the *AWS IoT SiteWise User Guide* . You can specify up to 10 hierarchies per asset model. For more information, see `Quotas <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html>`_ in the *AWS IoT SiteWise User Guide* .
        :param asset_model_properties: The property definitions of the asset model. For more information, see `Asset properties <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html>`_ in the *AWS IoT SiteWise User Guide* . You can specify up to 200 properties per asset model. For more information, see `Quotas <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html>`_ in the *AWS IoT SiteWise User Guide* .
        :param asset_model_type: The type of asset model. - *ASSET_MODEL* – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model. - *COMPONENT_MODEL* – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model.
        :param enforced_asset_model_interface_relationships: a list of asset model and interface relationships.
        :param tags: A list of key-value pairs that contain metadata for the asset. For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64edf231bb465b8f44da5cbed11fe0e7614208f47a50131d6c645ff0d3644608)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssetModelProps(
            asset_model_name=asset_model_name,
            asset_model_composite_models=asset_model_composite_models,
            asset_model_description=asset_model_description,
            asset_model_external_id=asset_model_external_id,
            asset_model_hierarchies=asset_model_hierarchies,
            asset_model_properties=asset_model_properties,
            asset_model_type=asset_model_type,
            enforced_asset_model_interface_relationships=enforced_asset_model_interface_relationships,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbed60408dd1c2873bc70f9dc7fe48d0d621e09df06498a80d6afdcb1504aadc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__57999804e9c09aa4d1dbca31b8d2a972cc93fa6fe7fe6e2b6a7b43ea236693de)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssetModelArn")
    def attr_asset_model_arn(self) -> builtins.str:
        '''The ARN of the asset model, which has the following format.

        :cloudformationAttribute: AssetModelArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssetModelArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssetModelId")
    def attr_asset_model_id(self) -> builtins.str:
        '''The ID of the asset model.

        :cloudformationAttribute: AssetModelId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssetModelId"))

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
    @jsii.member(jsii_name="assetModelName")
    def asset_model_name(self) -> builtins.str:
        '''A unique name for the asset model.'''
        return typing.cast(builtins.str, jsii.get(self, "assetModelName"))

    @asset_model_name.setter
    def asset_model_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4071e2eabdee1916b99a1a251c710b2b59e2c130de77e066817d7a99c8cbc84e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetModelName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assetModelCompositeModels")
    def asset_model_composite_models(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.AssetModelCompositeModelProperty"]]]]:
        '''The composite models that are part of this asset model.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.AssetModelCompositeModelProperty"]]]], jsii.get(self, "assetModelCompositeModels"))

    @asset_model_composite_models.setter
    def asset_model_composite_models(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.AssetModelCompositeModelProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75654fb8879a906466b416abbe028fcaa8a196e113d1b36c2586e69cf2304cf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetModelCompositeModels", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assetModelDescription")
    def asset_model_description(self) -> typing.Optional[builtins.str]:
        '''A description for the asset model.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assetModelDescription"))

    @asset_model_description.setter
    def asset_model_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d490d061673fe6f1c9ad9df9a8647b42dd857e63b1146d02ad13d08528d7ec58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetModelDescription", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assetModelExternalId")
    def asset_model_external_id(self) -> typing.Optional[builtins.str]:
        '''The external ID of the asset model.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assetModelExternalId"))

    @asset_model_external_id.setter
    def asset_model_external_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b11e9b7de389bdacb96aca69368f81f0023b01a9984dd10d8410bc081120813a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetModelExternalId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assetModelHierarchies")
    def asset_model_hierarchies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.AssetModelHierarchyProperty"]]]]:
        '''The hierarchy definitions of the asset model.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.AssetModelHierarchyProperty"]]]], jsii.get(self, "assetModelHierarchies"))

    @asset_model_hierarchies.setter
    def asset_model_hierarchies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.AssetModelHierarchyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfff308bea7d00a1626ce55b090f5843c55f7c818902bb4d4533293210c8b379)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetModelHierarchies", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assetModelProperties")
    def asset_model_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.AssetModelPropertyProperty"]]]]:
        '''The property definitions of the asset model.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.AssetModelPropertyProperty"]]]], jsii.get(self, "assetModelProperties"))

    @asset_model_properties.setter
    def asset_model_properties(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.AssetModelPropertyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62970d87191bab84b19cdf16fe635ae56be3bca14dce3de8ddbcb4ebe56e2e34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetModelProperties", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assetModelType")
    def asset_model_type(self) -> typing.Optional[builtins.str]:
        '''The type of asset model.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assetModelType"))

    @asset_model_type.setter
    def asset_model_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33747ea8b68fd7ca1298da79a238d24533fca030571c5c5f494b793812c77e2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetModelType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enforcedAssetModelInterfaceRelationships")
    def enforced_asset_model_interface_relationships(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.EnforcedAssetModelInterfaceRelationshipProperty"]]]]:
        '''a list of asset model and interface relationships.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.EnforcedAssetModelInterfaceRelationshipProperty"]]]], jsii.get(self, "enforcedAssetModelInterfaceRelationships"))

    @enforced_asset_model_interface_relationships.setter
    def enforced_asset_model_interface_relationships(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.EnforcedAssetModelInterfaceRelationshipProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8585343b0b44aebb25048a1408ef7b098cbb2e611b50c8ec2cbecceb8582d081)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforcedAssetModelInterfaceRelationships", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the asset.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__087e71db10fe7e46cfbe736951d8b93342a08c50afea582cbddc2eaa71151a64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModel.AssetModelCompositeModelProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "type": "type",
            "composed_asset_model_id": "composedAssetModelId",
            "composite_model_properties": "compositeModelProperties",
            "description": "description",
            "external_id": "externalId",
            "id": "id",
            "parent_asset_model_composite_model_external_id": "parentAssetModelCompositeModelExternalId",
            "path": "path",
        },
    )
    class AssetModelCompositeModelProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            type: builtins.str,
            composed_asset_model_id: typing.Optional[builtins.str] = None,
            composite_model_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.AssetModelPropertyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            description: typing.Optional[builtins.str] = None,
            external_id: typing.Optional[builtins.str] = None,
            id: typing.Optional[builtins.str] = None,
            parent_asset_model_composite_model_external_id: typing.Optional[builtins.str] = None,
            path: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Contains information about a composite model in an asset model.

            This object contains the asset property definitions that you define in the composite model.

            :param name: The name of the composite model.
            :param type: The type of the composite model. For alarm composite models, this type is ``AWS/ALARM`` .
            :param composed_asset_model_id: The ID of a component model which is reused to create this composite model.
            :param composite_model_properties: The asset property definitions for this composite model.
            :param description: The description of the composite model. .. epigraph:: If the composite model is a ``component-model-based`` composite model, the description is inherited from the ``COMPONENT_MODEL`` asset model and cannot be changed.
            :param external_id: The external ID of a composite model on this asset model. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* . .. epigraph:: One of ``ExternalId`` or ``Path`` must be specified.
            :param id: The ID of the asset model composite model. .. epigraph:: This is a return value and can't be set.
            :param parent_asset_model_composite_model_external_id: The external ID of the parent composite model. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .
            :param path: The structured path to the property from the root of the asset using property names. Path is used as the ID if the asset model is a derived composite model. .. epigraph:: One of ``ExternalId`` or ``Path`` must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                asset_model_composite_model_property = iotsitewise.CfnAssetModel.AssetModelCompositeModelProperty(
                    name="name",
                    type="type",
                
                    # the properties below are optional
                    composed_asset_model_id="composedAssetModelId",
                    composite_model_properties=[iotsitewise.CfnAssetModel.AssetModelPropertyProperty(
                        data_type="dataType",
                        name="name",
                        type=iotsitewise.CfnAssetModel.PropertyTypeProperty(
                            type_name="typeName",
                
                            # the properties below are optional
                            attribute=iotsitewise.CfnAssetModel.AttributeProperty(
                                default_value="defaultValue"
                            ),
                            metric=iotsitewise.CfnAssetModel.MetricProperty(
                                expression="expression",
                                variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                                    name="name",
                                    value=iotsitewise.CfnAssetModel.VariableValueProperty(
                                        hierarchy_external_id="hierarchyExternalId",
                                        hierarchy_id="hierarchyId",
                                        hierarchy_logical_id="hierarchyLogicalId",
                                        property_external_id="propertyExternalId",
                                        property_id="propertyId",
                                        property_logical_id="propertyLogicalId",
                                        property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                            name="name"
                                        )]
                                    )
                                )],
                                window=iotsitewise.CfnAssetModel.MetricWindowProperty(
                                    tumbling=iotsitewise.CfnAssetModel.TumblingWindowProperty(
                                        interval="interval",
                
                                        # the properties below are optional
                                        offset="offset"
                                    )
                                )
                            ),
                            transform=iotsitewise.CfnAssetModel.TransformProperty(
                                expression="expression",
                                variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                                    name="name",
                                    value=iotsitewise.CfnAssetModel.VariableValueProperty(
                                        hierarchy_external_id="hierarchyExternalId",
                                        hierarchy_id="hierarchyId",
                                        hierarchy_logical_id="hierarchyLogicalId",
                                        property_external_id="propertyExternalId",
                                        property_id="propertyId",
                                        property_logical_id="propertyLogicalId",
                                        property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                            name="name"
                                        )]
                                    )
                                )]
                            )
                        ),
                
                        # the properties below are optional
                        data_type_spec="dataTypeSpec",
                        external_id="externalId",
                        id="id",
                        logical_id="logicalId",
                        unit="unit"
                    )],
                    description="description",
                    external_id="externalId",
                    id="id",
                    parent_asset_model_composite_model_external_id="parentAssetModelCompositeModelExternalId",
                    path=["path"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9032bb49134101399c5b628c8911fa6a32ba8f4082d1d7ce6034344be92c8edb)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument composed_asset_model_id", value=composed_asset_model_id, expected_type=type_hints["composed_asset_model_id"])
                check_type(argname="argument composite_model_properties", value=composite_model_properties, expected_type=type_hints["composite_model_properties"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument parent_asset_model_composite_model_external_id", value=parent_asset_model_composite_model_external_id, expected_type=type_hints["parent_asset_model_composite_model_external_id"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "type": type,
            }
            if composed_asset_model_id is not None:
                self._values["composed_asset_model_id"] = composed_asset_model_id
            if composite_model_properties is not None:
                self._values["composite_model_properties"] = composite_model_properties
            if description is not None:
                self._values["description"] = description
            if external_id is not None:
                self._values["external_id"] = external_id
            if id is not None:
                self._values["id"] = id
            if parent_asset_model_composite_model_external_id is not None:
                self._values["parent_asset_model_composite_model_external_id"] = parent_asset_model_composite_model_external_id
            if path is not None:
                self._values["path"] = path

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the composite model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the composite model.

            For alarm composite models, this type is ``AWS/ALARM`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def composed_asset_model_id(self) -> typing.Optional[builtins.str]:
            '''The ID of a component model which is reused to create this composite model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-composedassetmodelid
            '''
            result = self._values.get("composed_asset_model_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def composite_model_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.AssetModelPropertyProperty"]]]]:
            '''The asset property definitions for this composite model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-compositemodelproperties
            '''
            result = self._values.get("composite_model_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.AssetModelPropertyProperty"]]]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the composite model.

            .. epigraph::

               If the composite model is a ``component-model-based`` composite model, the description is inherited from the ``COMPONENT_MODEL`` asset model and cannot be changed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID of a composite model on this asset model.

            For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .
            .. epigraph::

               One of ``ExternalId`` or ``Path`` must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-externalid
            '''
            result = self._values.get("external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The ID of the asset model composite model.

            .. epigraph::

               This is a return value and can't be set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parent_asset_model_composite_model_external_id(
            self,
        ) -> typing.Optional[builtins.str]:
            '''The external ID of the parent composite model.

            For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-parentassetmodelcompositemodelexternalid
            '''
            result = self._values.get("parent_asset_model_composite_model_external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def path(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The structured path to the property from the root of the asset using property names.

            Path is used as the ID if the asset model is a derived composite model.
            .. epigraph::

               One of ``ExternalId`` or ``Path`` must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelcompositemodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodel-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetModelCompositeModelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModel.AssetModelHierarchyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "child_asset_model_id": "childAssetModelId",
            "name": "name",
            "external_id": "externalId",
            "id": "id",
            "logical_id": "logicalId",
        },
    )
    class AssetModelHierarchyProperty:
        def __init__(
            self,
            *,
            child_asset_model_id: builtins.str,
            name: builtins.str,
            external_id: typing.Optional[builtins.str] = None,
            id: typing.Optional[builtins.str] = None,
            logical_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes an asset hierarchy that contains a hierarchy's name, ID, and child asset model ID that specifies the type of asset that can be in this hierarchy.

            :param child_asset_model_id: The ID of the asset model, in UUID format. All assets in this hierarchy must be instances of the ``childAssetModelId`` asset model. AWS IoT SiteWise will always return the actual asset model ID for this value. However, when you are specifying this value as part of a call to `UpdateAssetModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html>`_ , you may provide either the asset model ID or else ``externalId:`` followed by the asset model's external ID. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .
            :param name: The name of the asset model hierarchy that you specify by using the `CreateAssetModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html>`_ or `UpdateAssetModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html>`_ API operation.
            :param external_id: The external ID (if any) provided in the `CreateAssetModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html>`_ or `UpdateAssetModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html>`_ operation. You can assign an external ID by specifying this value as part of a call to `UpdateAssetModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html>`_ . However, you can't change the external ID if one is already assigned. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* . .. epigraph:: One of ``ExternalId`` or ``LogicalId`` must be specified.
            :param id: The ID of the asset model hierarchy. This ID is a ``hierarchyId`` . .. epigraph:: This is a return value and can't be set. - If you are callling `UpdateAssetModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html>`_ to create a *new* hierarchy: You can specify its ID here, if desired. AWS IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique. - If you are calling UpdateAssetModel to modify an *existing* hierarchy: This can be either the actual ID in UUID format, or else ``externalId:`` followed by the external ID, if it has one. For more information, see `Referencing objects with external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references>`_ in the *AWS IoT SiteWise User Guide* .
            :param logical_id: The ``LogicalID`` of the asset model hierarchy. This ID is a ``hierarchyLogicalId`` . .. epigraph:: One of ``ExternalId`` or ``LogicalId`` must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                asset_model_hierarchy_property = iotsitewise.CfnAssetModel.AssetModelHierarchyProperty(
                    child_asset_model_id="childAssetModelId",
                    name="name",
                
                    # the properties below are optional
                    external_id="externalId",
                    id="id",
                    logical_id="logicalId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b8bdd9b09999ded14aeb0bb460a6a5e4983c049cd1fedb5aaca40a2cd4b07f26)
                check_type(argname="argument child_asset_model_id", value=child_asset_model_id, expected_type=type_hints["child_asset_model_id"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "child_asset_model_id": child_asset_model_id,
                "name": name,
            }
            if external_id is not None:
                self._values["external_id"] = external_id
            if id is not None:
                self._values["id"] = id
            if logical_id is not None:
                self._values["logical_id"] = logical_id

        @builtins.property
        def child_asset_model_id(self) -> builtins.str:
            '''The ID of the asset model, in UUID format.

            All assets in this hierarchy must be instances of the ``childAssetModelId`` asset model. AWS IoT SiteWise will always return the actual asset model ID for this value. However, when you are specifying this value as part of a call to `UpdateAssetModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html>`_ , you may provide either the asset model ID or else ``externalId:`` followed by the asset model's external ID. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html#cfn-iotsitewise-assetmodel-assetmodelhierarchy-childassetmodelid
            '''
            result = self._values.get("child_asset_model_id")
            assert result is not None, "Required property 'child_asset_model_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the asset model hierarchy that you specify by using the `CreateAssetModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html>`_ or `UpdateAssetModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html>`_ API operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html#cfn-iotsitewise-assetmodel-assetmodelhierarchy-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID (if any) provided in the `CreateAssetModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html>`_ or `UpdateAssetModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html>`_ operation. You can assign an external ID by specifying this value as part of a call to `UpdateAssetModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html>`_ . However, you can't change the external ID if one is already assigned. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .

            .. epigraph::

               One of ``ExternalId`` or ``LogicalId`` must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html#cfn-iotsitewise-assetmodel-assetmodelhierarchy-externalid
            '''
            result = self._values.get("external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The ID of the asset model hierarchy. This ID is a ``hierarchyId`` .

            .. epigraph::

               This is a return value and can't be set.

            - If you are callling `UpdateAssetModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html>`_ to create a *new* hierarchy: You can specify its ID here, if desired. AWS IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.
            - If you are calling UpdateAssetModel to modify an *existing* hierarchy: This can be either the actual ID in UUID format, or else ``externalId:`` followed by the external ID, if it has one. For more information, see `Referencing objects with external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html#cfn-iotsitewise-assetmodel-assetmodelhierarchy-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def logical_id(self) -> typing.Optional[builtins.str]:
            '''The ``LogicalID`` of the asset model hierarchy. This ID is a ``hierarchyLogicalId`` .

            .. epigraph::

               One of ``ExternalId`` or ``LogicalId`` must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelhierarchy.html#cfn-iotsitewise-assetmodel-assetmodelhierarchy-logicalid
            '''
            result = self._values.get("logical_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetModelHierarchyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModel.AssetModelPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_type": "dataType",
            "name": "name",
            "type": "type",
            "data_type_spec": "dataTypeSpec",
            "external_id": "externalId",
            "id": "id",
            "logical_id": "logicalId",
            "unit": "unit",
        },
    )
    class AssetModelPropertyProperty:
        def __init__(
            self,
            *,
            data_type: builtins.str,
            name: builtins.str,
            type: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.PropertyTypeProperty", typing.Dict[builtins.str, typing.Any]]],
            data_type_spec: typing.Optional[builtins.str] = None,
            external_id: typing.Optional[builtins.str] = None,
            id: typing.Optional[builtins.str] = None,
            logical_id: typing.Optional[builtins.str] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about an asset model property.

            :param data_type: The data type of the asset model property. If you specify ``STRUCT`` , you must also specify ``dataTypeSpec`` to identify the type of the structure for this property.
            :param name: The name of the asset model property.
            :param type: Contains a property type, which can be one of ``attribute`` , ``measurement`` , ``metric`` , or ``transform`` .
            :param data_type_spec: The data type of the structure for this property. This parameter exists on properties that have the ``STRUCT`` data type.
            :param external_id: The external ID of the asset property. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* . .. epigraph:: One of ``ExternalId`` or ``LogicalId`` must be specified.
            :param id: The ID of the property. .. epigraph:: This is a return value and can't be set.
            :param logical_id: The ``LogicalID`` of the asset model property. .. epigraph:: One of ``ExternalId`` or ``LogicalId`` must be specified.
            :param unit: The unit of the asset model property, such as ``Newtons`` or ``RPM`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                asset_model_property_property = iotsitewise.CfnAssetModel.AssetModelPropertyProperty(
                    data_type="dataType",
                    name="name",
                    type=iotsitewise.CfnAssetModel.PropertyTypeProperty(
                        type_name="typeName",
                
                        # the properties below are optional
                        attribute=iotsitewise.CfnAssetModel.AttributeProperty(
                            default_value="defaultValue"
                        ),
                        metric=iotsitewise.CfnAssetModel.MetricProperty(
                            expression="expression",
                            variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                                name="name",
                                value=iotsitewise.CfnAssetModel.VariableValueProperty(
                                    hierarchy_external_id="hierarchyExternalId",
                                    hierarchy_id="hierarchyId",
                                    hierarchy_logical_id="hierarchyLogicalId",
                                    property_external_id="propertyExternalId",
                                    property_id="propertyId",
                                    property_logical_id="propertyLogicalId",
                                    property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                        name="name"
                                    )]
                                )
                            )],
                            window=iotsitewise.CfnAssetModel.MetricWindowProperty(
                                tumbling=iotsitewise.CfnAssetModel.TumblingWindowProperty(
                                    interval="interval",
                
                                    # the properties below are optional
                                    offset="offset"
                                )
                            )
                        ),
                        transform=iotsitewise.CfnAssetModel.TransformProperty(
                            expression="expression",
                            variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                                name="name",
                                value=iotsitewise.CfnAssetModel.VariableValueProperty(
                                    hierarchy_external_id="hierarchyExternalId",
                                    hierarchy_id="hierarchyId",
                                    hierarchy_logical_id="hierarchyLogicalId",
                                    property_external_id="propertyExternalId",
                                    property_id="propertyId",
                                    property_logical_id="propertyLogicalId",
                                    property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                        name="name"
                                    )]
                                )
                            )]
                        )
                    ),
                
                    # the properties below are optional
                    data_type_spec="dataTypeSpec",
                    external_id="externalId",
                    id="id",
                    logical_id="logicalId",
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__df059a45516e286dd4ae84860f6454c3be02b47df42355ea284b5bd8c3c97590)
                check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument data_type_spec", value=data_type_spec, expected_type=type_hints["data_type_spec"])
                check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_type": data_type,
                "name": name,
                "type": type,
            }
            if data_type_spec is not None:
                self._values["data_type_spec"] = data_type_spec
            if external_id is not None:
                self._values["external_id"] = external_id
            if id is not None:
                self._values["id"] = id
            if logical_id is not None:
                self._values["logical_id"] = logical_id
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def data_type(self) -> builtins.str:
            '''The data type of the asset model property.

            If you specify ``STRUCT`` , you must also specify ``dataTypeSpec`` to identify the type of the structure for this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-datatype
            '''
            result = self._values.get("data_type")
            assert result is not None, "Required property 'data_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the asset model property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAssetModel.PropertyTypeProperty"]:
            '''Contains a property type, which can be one of ``attribute`` , ``measurement`` , ``metric`` , or ``transform`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAssetModel.PropertyTypeProperty"], result)

        @builtins.property
        def data_type_spec(self) -> typing.Optional[builtins.str]:
            '''The data type of the structure for this property.

            This parameter exists on properties that have the ``STRUCT`` data type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-datatypespec
            '''
            result = self._values.get("data_type_spec")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID of the asset property.

            For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .
            .. epigraph::

               One of ``ExternalId`` or ``LogicalId`` must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-externalid
            '''
            result = self._values.get("external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''The ID of the property.

            .. epigraph::

               This is a return value and can't be set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def logical_id(self) -> typing.Optional[builtins.str]:
            '''The ``LogicalID`` of the asset model property.

            .. epigraph::

               One of ``ExternalId`` or ``LogicalId`` must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-logicalid
            '''
            result = self._values.get("logical_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''The unit of the asset model property, such as ``Newtons`` or ``RPM`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-assetmodelproperty.html#cfn-iotsitewise-assetmodel-assetmodelproperty-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetModelPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModel.AttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"default_value": "defaultValue"},
    )
    class AttributeProperty:
        def __init__(
            self,
            *,
            default_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains an asset attribute property.

            For more information, see `Attributes <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html#attributes>`_ in the *AWS IoT SiteWise User Guide* .

            :param default_value: The default value of the asset model property attribute. All assets that you create from the asset model contain this attribute value. You can update an attribute's value after you create an asset. For more information, see `Updating attribute values <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-attribute-values.html>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-attribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                attribute_property = iotsitewise.CfnAssetModel.AttributeProperty(
                    default_value="defaultValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3172068ecee12a11a997c0f7922e1b5c5f5b9e44979e3f39af0c9f9974d4cbc0)
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if default_value is not None:
                self._values["default_value"] = default_value

        @builtins.property
        def default_value(self) -> typing.Optional[builtins.str]:
            '''The default value of the asset model property attribute.

            All assets that you create from the asset model contain this attribute value. You can update an attribute's value after you create an asset. For more information, see `Updating attribute values <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-attribute-values.html>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-attribute.html#cfn-iotsitewise-assetmodel-attribute-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModel.EnforcedAssetModelInterfacePropertyMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interface_asset_model_property_external_id": "interfaceAssetModelPropertyExternalId",
            "asset_model_property_external_id": "assetModelPropertyExternalId",
            "asset_model_property_logical_id": "assetModelPropertyLogicalId",
        },
    )
    class EnforcedAssetModelInterfacePropertyMappingProperty:
        def __init__(
            self,
            *,
            interface_asset_model_property_external_id: builtins.str,
            asset_model_property_external_id: typing.Optional[builtins.str] = None,
            asset_model_property_logical_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about enforced interface property and asset model property.

            :param interface_asset_model_property_external_id: The external ID of the enforced interface property.
            :param asset_model_property_external_id: The external ID of the enforced asset model property.
            :param asset_model_property_logical_id: The logical ID of the enforced asset model property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                enforced_asset_model_interface_property_mapping_property = iotsitewise.CfnAssetModel.EnforcedAssetModelInterfacePropertyMappingProperty(
                    interface_asset_model_property_external_id="interfaceAssetModelPropertyExternalId",
                
                    # the properties below are optional
                    asset_model_property_external_id="assetModelPropertyExternalId",
                    asset_model_property_logical_id="assetModelPropertyLogicalId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__602edbd4a6db7058c0a2d97bafdee4ac831e8e9cefa95964c590f9009304858f)
                check_type(argname="argument interface_asset_model_property_external_id", value=interface_asset_model_property_external_id, expected_type=type_hints["interface_asset_model_property_external_id"])
                check_type(argname="argument asset_model_property_external_id", value=asset_model_property_external_id, expected_type=type_hints["asset_model_property_external_id"])
                check_type(argname="argument asset_model_property_logical_id", value=asset_model_property_logical_id, expected_type=type_hints["asset_model_property_logical_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "interface_asset_model_property_external_id": interface_asset_model_property_external_id,
            }
            if asset_model_property_external_id is not None:
                self._values["asset_model_property_external_id"] = asset_model_property_external_id
            if asset_model_property_logical_id is not None:
                self._values["asset_model_property_logical_id"] = asset_model_property_logical_id

        @builtins.property
        def interface_asset_model_property_external_id(self) -> builtins.str:
            '''The external ID of the enforced interface property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping.html#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-interfaceassetmodelpropertyexternalid
            '''
            result = self._values.get("interface_asset_model_property_external_id")
            assert result is not None, "Required property 'interface_asset_model_property_external_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def asset_model_property_external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID of the enforced asset model property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping.html#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-assetmodelpropertyexternalid
            '''
            result = self._values.get("asset_model_property_external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def asset_model_property_logical_id(self) -> typing.Optional[builtins.str]:
            '''The logical ID of the enforced asset model property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping.html#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacepropertymapping-assetmodelpropertylogicalid
            '''
            result = self._values.get("asset_model_property_logical_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnforcedAssetModelInterfacePropertyMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModel.EnforcedAssetModelInterfaceRelationshipProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interface_asset_model_id": "interfaceAssetModelId",
            "property_mappings": "propertyMappings",
        },
    )
    class EnforcedAssetModelInterfaceRelationshipProperty:
        def __init__(
            self,
            *,
            interface_asset_model_id: typing.Optional[builtins.str] = None,
            property_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.EnforcedAssetModelInterfacePropertyMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Contains information about enforced interface hierarchy and asset model hierarchy.

            :param interface_asset_model_id: The ID of the interface that is enforced to the asset model.
            :param property_mappings: Contains information about enforced interface property and asset model property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                enforced_asset_model_interface_relationship_property = iotsitewise.CfnAssetModel.EnforcedAssetModelInterfaceRelationshipProperty(
                    interface_asset_model_id="interfaceAssetModelId",
                    property_mappings=[iotsitewise.CfnAssetModel.EnforcedAssetModelInterfacePropertyMappingProperty(
                        interface_asset_model_property_external_id="interfaceAssetModelPropertyExternalId",
                
                        # the properties below are optional
                        asset_model_property_external_id="assetModelPropertyExternalId",
                        asset_model_property_logical_id="assetModelPropertyLogicalId"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1fe8dfe5b5064a1ee03d773eb65966bf8eb13cf514900f6647f677f88f271459)
                check_type(argname="argument interface_asset_model_id", value=interface_asset_model_id, expected_type=type_hints["interface_asset_model_id"])
                check_type(argname="argument property_mappings", value=property_mappings, expected_type=type_hints["property_mappings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if interface_asset_model_id is not None:
                self._values["interface_asset_model_id"] = interface_asset_model_id
            if property_mappings is not None:
                self._values["property_mappings"] = property_mappings

        @builtins.property
        def interface_asset_model_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the interface that is enforced to the asset model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship.html#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship-interfaceassetmodelid
            '''
            result = self._values.get("interface_asset_model_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.EnforcedAssetModelInterfacePropertyMappingProperty"]]]]:
            '''Contains information about enforced interface property and asset model property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship.html#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationship-propertymappings
            '''
            result = self._values.get("property_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.EnforcedAssetModelInterfacePropertyMappingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnforcedAssetModelInterfaceRelationshipProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModel.ExpressionVariableProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class ExpressionVariableProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            value: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.VariableValueProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Contains expression variable information.

            :param name: The friendly name of the variable to be used in the expression.
            :param value: The variable that identifies an asset property from which to use values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-expressionvariable.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                expression_variable_property = iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                    name="name",
                    value=iotsitewise.CfnAssetModel.VariableValueProperty(
                        hierarchy_external_id="hierarchyExternalId",
                        hierarchy_id="hierarchyId",
                        hierarchy_logical_id="hierarchyLogicalId",
                        property_external_id="propertyExternalId",
                        property_id="propertyId",
                        property_logical_id="propertyLogicalId",
                        property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                            name="name"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__47d40674b47217f8eb75acf1060336f44b9e0583e395a98550f44b5a4681f3db)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The friendly name of the variable to be used in the expression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-expressionvariable.html#cfn-iotsitewise-assetmodel-expressionvariable-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAssetModel.VariableValueProperty"]:
            '''The variable that identifies an asset property from which to use values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-expressionvariable.html#cfn-iotsitewise-assetmodel-expressionvariable-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAssetModel.VariableValueProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExpressionVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModel.MetricProperty",
        jsii_struct_bases=[],
        name_mapping={
            "expression": "expression",
            "variables": "variables",
            "window": "window",
        },
    )
    class MetricProperty:
        def __init__(
            self,
            *,
            expression: builtins.str,
            variables: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.ExpressionVariableProperty", typing.Dict[builtins.str, typing.Any]]]]],
            window: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.MetricWindowProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Contains an asset metric property.

            With metrics, you can calculate aggregate functions, such as an average, maximum, or minimum, as specified through an expression. A metric maps several values to a single value (such as a sum).

            The maximum number of dependent/cascading variables used in any one metric calculation is 10. Therefore, a *root* metric can have up to 10 cascading metrics in its computational dependency tree. Additionally, a metric can only have a data type of ``DOUBLE`` and consume properties with data types of ``INTEGER`` or ``DOUBLE`` .

            For more information, see `Metrics <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html#metrics>`_ in the *AWS IoT SiteWise User Guide* .

            :param expression: The mathematical expression that defines the metric aggregation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression. For more information, see `Quotas <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html>`_ in the *AWS IoT SiteWise User Guide* .
            :param variables: The list of variables used in the expression.
            :param window: The window (time interval) over which AWS IoT SiteWise computes the metric's aggregation expression. AWS IoT SiteWise computes one data point per ``window`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metric.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                metric_property = iotsitewise.CfnAssetModel.MetricProperty(
                    expression="expression",
                    variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                        name="name",
                        value=iotsitewise.CfnAssetModel.VariableValueProperty(
                            hierarchy_external_id="hierarchyExternalId",
                            hierarchy_id="hierarchyId",
                            hierarchy_logical_id="hierarchyLogicalId",
                            property_external_id="propertyExternalId",
                            property_id="propertyId",
                            property_logical_id="propertyLogicalId",
                            property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                name="name"
                            )]
                        )
                    )],
                    window=iotsitewise.CfnAssetModel.MetricWindowProperty(
                        tumbling=iotsitewise.CfnAssetModel.TumblingWindowProperty(
                            interval="interval",
                
                            # the properties below are optional
                            offset="offset"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__018f0992b00dd2aa0891d7049deb5b9e6a376d61ee7e9524a2dc1a04b2d1de89)
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
                check_type(argname="argument window", value=window, expected_type=type_hints["window"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "expression": expression,
                "variables": variables,
                "window": window,
            }

        @builtins.property
        def expression(self) -> builtins.str:
            '''The mathematical expression that defines the metric aggregation function.

            You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.

            For more information, see `Quotas <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metric.html#cfn-iotsitewise-assetmodel-metric-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def variables(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.ExpressionVariableProperty"]]]:
            '''The list of variables used in the expression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metric.html#cfn-iotsitewise-assetmodel-metric-variables
            '''
            result = self._values.get("variables")
            assert result is not None, "Required property 'variables' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.ExpressionVariableProperty"]]], result)

        @builtins.property
        def window(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAssetModel.MetricWindowProperty"]:
            '''The window (time interval) over which AWS IoT SiteWise computes the metric's aggregation expression.

            AWS IoT SiteWise computes one data point per ``window`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metric.html#cfn-iotsitewise-assetmodel-metric-window
            '''
            result = self._values.get("window")
            assert result is not None, "Required property 'window' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAssetModel.MetricWindowProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModel.MetricWindowProperty",
        jsii_struct_bases=[],
        name_mapping={"tumbling": "tumbling"},
    )
    class MetricWindowProperty:
        def __init__(
            self,
            *,
            tumbling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.TumblingWindowProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains a time interval window used for data aggregate computations (for example, average, sum, count, and so on).

            :param tumbling: The tumbling time interval window.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metricwindow.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                metric_window_property = iotsitewise.CfnAssetModel.MetricWindowProperty(
                    tumbling=iotsitewise.CfnAssetModel.TumblingWindowProperty(
                        interval="interval",
                
                        # the properties below are optional
                        offset="offset"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36161b8e17b90887f361ce990f098e579673e8c26bf5974d4d53d888312a8a4b)
                check_type(argname="argument tumbling", value=tumbling, expected_type=type_hints["tumbling"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if tumbling is not None:
                self._values["tumbling"] = tumbling

        @builtins.property
        def tumbling(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.TumblingWindowProperty"]]:
            '''The tumbling time interval window.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-metricwindow.html#cfn-iotsitewise-assetmodel-metricwindow-tumbling
            '''
            result = self._values.get("tumbling")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.TumblingWindowProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricWindowProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class PropertyPathDefinitionProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''Represents one level between a composite model and the root of the asset model.

            :param name: The name of the path segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertypathdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                property_path_definition_property = iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1359481022b13ca49cc9baa669a2ecc9adec5ca26699f485a60965403d6b134e)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the path segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertypathdefinition.html#cfn-iotsitewise-assetmodel-propertypathdefinition-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PropertyPathDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModel.PropertyTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type_name": "typeName",
            "attribute": "attribute",
            "metric": "metric",
            "transform": "transform",
        },
    )
    class PropertyTypeProperty:
        def __init__(
            self,
            *,
            type_name: builtins.str,
            attribute: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.AttributeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            metric: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.MetricProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            transform: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.TransformProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains a property type, which can be one of ``attribute`` , ``measurement`` , ``metric`` , or ``transform`` .

            :param type_name: The type of property type, which can be one of ``Attribute`` , ``Measurement`` , ``Metric`` , or ``Transform`` .
            :param attribute: Specifies an asset attribute property. An attribute generally contains static information, such as the serial number of an `IIoT <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Internet_of_things#Industrial_applications>`_ wind turbine.
            :param metric: Specifies an asset metric property. A metric contains a mathematical expression that uses aggregate functions to process all input data points over a time interval and output a single data point, such as to calculate the average hourly temperature.
            :param transform: Specifies an asset transform property. A transform contains a mathematical expression that maps a property's data points from one form to another, such as a unit conversion from Celsius to Fahrenheit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                property_type_property = iotsitewise.CfnAssetModel.PropertyTypeProperty(
                    type_name="typeName",
                
                    # the properties below are optional
                    attribute=iotsitewise.CfnAssetModel.AttributeProperty(
                        default_value="defaultValue"
                    ),
                    metric=iotsitewise.CfnAssetModel.MetricProperty(
                        expression="expression",
                        variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                            name="name",
                            value=iotsitewise.CfnAssetModel.VariableValueProperty(
                                hierarchy_external_id="hierarchyExternalId",
                                hierarchy_id="hierarchyId",
                                hierarchy_logical_id="hierarchyLogicalId",
                                property_external_id="propertyExternalId",
                                property_id="propertyId",
                                property_logical_id="propertyLogicalId",
                                property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                    name="name"
                                )]
                            )
                        )],
                        window=iotsitewise.CfnAssetModel.MetricWindowProperty(
                            tumbling=iotsitewise.CfnAssetModel.TumblingWindowProperty(
                                interval="interval",
                
                                # the properties below are optional
                                offset="offset"
                            )
                        )
                    ),
                    transform=iotsitewise.CfnAssetModel.TransformProperty(
                        expression="expression",
                        variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                            name="name",
                            value=iotsitewise.CfnAssetModel.VariableValueProperty(
                                hierarchy_external_id="hierarchyExternalId",
                                hierarchy_id="hierarchyId",
                                hierarchy_logical_id="hierarchyLogicalId",
                                property_external_id="propertyExternalId",
                                property_id="propertyId",
                                property_logical_id="propertyLogicalId",
                                property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                    name="name"
                                )]
                            )
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__88ab1ab9be5266b8374e7737561a2ceef629d83bcca6a5f65325e207910a86e3)
                check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
                check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
                check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
                check_type(argname="argument transform", value=transform, expected_type=type_hints["transform"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type_name": type_name,
            }
            if attribute is not None:
                self._values["attribute"] = attribute
            if metric is not None:
                self._values["metric"] = metric
            if transform is not None:
                self._values["transform"] = transform

        @builtins.property
        def type_name(self) -> builtins.str:
            '''The type of property type, which can be one of ``Attribute`` , ``Measurement`` , ``Metric`` , or ``Transform`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html#cfn-iotsitewise-assetmodel-propertytype-typename
            '''
            result = self._values.get("type_name")
            assert result is not None, "Required property 'type_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attribute(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.AttributeProperty"]]:
            '''Specifies an asset attribute property.

            An attribute generally contains static information, such as the serial number of an `IIoT <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/Internet_of_things#Industrial_applications>`_ wind turbine.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html#cfn-iotsitewise-assetmodel-propertytype-attribute
            '''
            result = self._values.get("attribute")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.AttributeProperty"]], result)

        @builtins.property
        def metric(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.MetricProperty"]]:
            '''Specifies an asset metric property.

            A metric contains a mathematical expression that uses aggregate functions to process all input data points over a time interval and output a single data point, such as to calculate the average hourly temperature.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html#cfn-iotsitewise-assetmodel-propertytype-metric
            '''
            result = self._values.get("metric")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.MetricProperty"]], result)

        @builtins.property
        def transform(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.TransformProperty"]]:
            '''Specifies an asset transform property.

            A transform contains a mathematical expression that maps a property's data points from one form to another, such as a unit conversion from Celsius to Fahrenheit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-propertytype.html#cfn-iotsitewise-assetmodel-propertytype-transform
            '''
            result = self._values.get("transform")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.TransformProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PropertyTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModel.TransformProperty",
        jsii_struct_bases=[],
        name_mapping={"expression": "expression", "variables": "variables"},
    )
    class TransformProperty:
        def __init__(
            self,
            *,
            expression: builtins.str,
            variables: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.ExpressionVariableProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Contains an asset transform property.

            A transform is a one-to-one mapping of a property's data points from one form to another. For example, you can use a transform to convert a Celsius data stream to Fahrenheit by applying the transformation expression to each data point of the Celsius stream. A transform can only have a data type of ``DOUBLE`` and consume properties with data types of ``INTEGER`` or ``DOUBLE`` .

            For more information, see `Transforms <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html#transforms>`_ in the *AWS IoT SiteWise User Guide* .

            :param expression: The mathematical expression that defines the transformation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression. For more information, see `Quotas <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html>`_ in the *AWS IoT SiteWise User Guide* .
            :param variables: The list of variables used in the expression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-transform.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                transform_property = iotsitewise.CfnAssetModel.TransformProperty(
                    expression="expression",
                    variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                        name="name",
                        value=iotsitewise.CfnAssetModel.VariableValueProperty(
                            hierarchy_external_id="hierarchyExternalId",
                            hierarchy_id="hierarchyId",
                            hierarchy_logical_id="hierarchyLogicalId",
                            property_external_id="propertyExternalId",
                            property_id="propertyId",
                            property_logical_id="propertyLogicalId",
                            property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                name="name"
                            )]
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b165b40ea43e6f49e8b83fad3f0774b1c777b4df0881816c6666f80def04b51)
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "expression": expression,
                "variables": variables,
            }

        @builtins.property
        def expression(self) -> builtins.str:
            '''The mathematical expression that defines the transformation function.

            You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.

            For more information, see `Quotas <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-transform.html#cfn-iotsitewise-assetmodel-transform-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def variables(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.ExpressionVariableProperty"]]]:
            '''The list of variables used in the expression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-transform.html#cfn-iotsitewise-assetmodel-transform-variables
            '''
            result = self._values.get("variables")
            assert result is not None, "Required property 'variables' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.ExpressionVariableProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TransformProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModel.TumblingWindowProperty",
        jsii_struct_bases=[],
        name_mapping={"interval": "interval", "offset": "offset"},
    )
    class TumblingWindowProperty:
        def __init__(
            self,
            *,
            interval: builtins.str,
            offset: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains a tumbling window, which is a repeating fixed-sized, non-overlapping, and contiguous time window.

            You can use this window in metrics to aggregate data from properties and other assets.

            You can use ``m`` , ``h`` , ``d`` , and ``w`` when you specify an interval or offset. Note that ``m`` represents minutes, ``h`` represents hours, ``d`` represents days, and ``w`` represents weeks. You can also use ``s`` to represent seconds in ``offset`` .

            The ``interval`` and ``offset`` parameters support the `ISO 8601 format <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/ISO_8601>`_ . For example, ``PT5S`` represents 5 seconds, ``PT5M`` represents 5 minutes, and ``PT5H`` represents 5 hours.

            :param interval: The time interval for the tumbling window. The interval time must be between 1 minute and 1 week. AWS IoT SiteWise computes the ``1w`` interval the end of Sunday at midnight each week (UTC), the ``1d`` interval at the end of each day at midnight (UTC), the ``1h`` interval at the end of each hour, and so on. When AWS IoT SiteWise aggregates data points for metric computations, the start of each interval is exclusive and the end of each interval is inclusive. AWS IoT SiteWise places the computed data point at the end of the interval.
            :param offset: The offset for the tumbling window. The ``offset`` parameter accepts the following:. - The offset time. For example, if you specify ``18h`` for ``offset`` and ``1d`` for ``interval`` , AWS IoT SiteWise aggregates data in one of the following ways: - If you create the metric before or at 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) on the day when you create the metric. - If you create the metric after 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) the next day. - The ISO 8601 format. For example, if you specify ``PT18H`` for ``offset`` and ``1d`` for ``interval`` , AWS IoT SiteWise aggregates data in one of the following ways: - If you create the metric before or at 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) on the day when you create the metric. - If you create the metric after 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) the next day. - The 24-hour clock. For example, if you specify ``00:03:00`` for ``offset`` , ``5m`` for ``interval`` , and you create the metric at 2 PM (UTC), you get the first aggregation result at 2:03 PM (UTC). You get the second aggregation result at 2:08 PM (UTC). - The offset time zone. For example, if you specify ``2021-07-23T18:00-08`` for ``offset`` and ``1d`` for ``interval`` , AWS IoT SiteWise aggregates data in one of the following ways: - If you create the metric before or at 6 PM (PST), you get the first aggregation result at 6 PM (PST) on the day when you create the metric. - If you create the metric after 6 PM (PST), you get the first aggregation result at 6 PM (PST) the next day.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-tumblingwindow.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                tumbling_window_property = iotsitewise.CfnAssetModel.TumblingWindowProperty(
                    interval="interval",
                
                    # the properties below are optional
                    offset="offset"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__167b1f3f100fbd3792343a3af0f3185dfbaf01430ea8af4870144df021de021f)
                check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
                check_type(argname="argument offset", value=offset, expected_type=type_hints["offset"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "interval": interval,
            }
            if offset is not None:
                self._values["offset"] = offset

        @builtins.property
        def interval(self) -> builtins.str:
            '''The time interval for the tumbling window. The interval time must be between 1 minute and 1 week.

            AWS IoT SiteWise computes the ``1w`` interval the end of Sunday at midnight each week (UTC), the ``1d`` interval at the end of each day at midnight (UTC), the ``1h`` interval at the end of each hour, and so on.

            When AWS IoT SiteWise aggregates data points for metric computations, the start of each interval is exclusive and the end of each interval is inclusive. AWS IoT SiteWise places the computed data point at the end of the interval.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-tumblingwindow.html#cfn-iotsitewise-assetmodel-tumblingwindow-interval
            '''
            result = self._values.get("interval")
            assert result is not None, "Required property 'interval' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def offset(self) -> typing.Optional[builtins.str]:
            '''The offset for the tumbling window. The ``offset`` parameter accepts the following:.

            - The offset time.

            For example, if you specify ``18h`` for ``offset`` and ``1d`` for ``interval`` , AWS IoT SiteWise aggregates data in one of the following ways:

            - If you create the metric before or at 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) on the day when you create the metric.
            - If you create the metric after 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) the next day.
            - The ISO 8601 format.

            For example, if you specify ``PT18H`` for ``offset`` and ``1d`` for ``interval`` , AWS IoT SiteWise aggregates data in one of the following ways:

            - If you create the metric before or at 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) on the day when you create the metric.
            - If you create the metric after 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) the next day.
            - The 24-hour clock.

            For example, if you specify ``00:03:00`` for ``offset`` , ``5m`` for ``interval`` , and you create the metric at 2 PM (UTC), you get the first aggregation result at 2:03 PM (UTC). You get the second aggregation result at 2:08 PM (UTC).

            - The offset time zone.

            For example, if you specify ``2021-07-23T18:00-08`` for ``offset`` and ``1d`` for ``interval`` , AWS IoT SiteWise aggregates data in one of the following ways:

            - If you create the metric before or at 6 PM (PST), you get the first aggregation result at 6 PM (PST) on the day when you create the metric.
            - If you create the metric after 6 PM (PST), you get the first aggregation result at 6 PM (PST) the next day.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-tumblingwindow.html#cfn-iotsitewise-assetmodel-tumblingwindow-offset
            '''
            result = self._values.get("offset")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TumblingWindowProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModel.VariableValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hierarchy_external_id": "hierarchyExternalId",
            "hierarchy_id": "hierarchyId",
            "hierarchy_logical_id": "hierarchyLogicalId",
            "property_external_id": "propertyExternalId",
            "property_id": "propertyId",
            "property_logical_id": "propertyLogicalId",
            "property_path": "propertyPath",
        },
    )
    class VariableValueProperty:
        def __init__(
            self,
            *,
            hierarchy_external_id: typing.Optional[builtins.str] = None,
            hierarchy_id: typing.Optional[builtins.str] = None,
            hierarchy_logical_id: typing.Optional[builtins.str] = None,
            property_external_id: typing.Optional[builtins.str] = None,
            property_id: typing.Optional[builtins.str] = None,
            property_logical_id: typing.Optional[builtins.str] = None,
            property_path: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssetModel.PropertyPathDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Identifies a property value used in an expression.

            :param hierarchy_external_id: The external ID of the hierarchy being referenced. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .
            :param hierarchy_id: The ID of the hierarchy to query for the property ID. You can use the hierarchy's name instead of the hierarchy's ID. If the hierarchy has an external ID, you can specify ``externalId:`` followed by the external ID. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* . You use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same ``propertyId`` . For example, you might have separately grouped assets that come from the same asset model. For more information, see `Asset hierarchies <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html>`_ in the *AWS IoT SiteWise User Guide* .
            :param hierarchy_logical_id: The ``LogicalID`` of the hierarchy to query for the ``PropertyLogicalID`` . You use a ``hierarchyLogicalID`` instead of a model ID because you can have several hierarchies using the same model and therefore the same property. For example, you might have separately grouped assets that come from the same asset model. For more information, see `Defining relationships between asset models (hierarchies) <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html>`_ in the *AWS IoT SiteWise User Guide* .
            :param property_external_id: The external ID of the property being referenced. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .
            :param property_id: The ID of the property to use as the variable. You can use the property ``name`` if it's from the same asset model. If the property has an external ID, you can specify ``externalId:`` followed by the external ID. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* . .. epigraph:: This is a return value and can't be set.
            :param property_logical_id: The ``LogicalID`` of the property that is being referenced.
            :param property_path: The path of the property. Each step of the path is the name of the step. See the following example: ``PropertyPath: Name: AssetModelName Name: Composite1 Name: NestedComposite``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                variable_value_property = iotsitewise.CfnAssetModel.VariableValueProperty(
                    hierarchy_external_id="hierarchyExternalId",
                    hierarchy_id="hierarchyId",
                    hierarchy_logical_id="hierarchyLogicalId",
                    property_external_id="propertyExternalId",
                    property_id="propertyId",
                    property_logical_id="propertyLogicalId",
                    property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                        name="name"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dfc8a5f6be8f2396701edaddb5e852d356262a49103549dbc6de3a39b491f9b4)
                check_type(argname="argument hierarchy_external_id", value=hierarchy_external_id, expected_type=type_hints["hierarchy_external_id"])
                check_type(argname="argument hierarchy_id", value=hierarchy_id, expected_type=type_hints["hierarchy_id"])
                check_type(argname="argument hierarchy_logical_id", value=hierarchy_logical_id, expected_type=type_hints["hierarchy_logical_id"])
                check_type(argname="argument property_external_id", value=property_external_id, expected_type=type_hints["property_external_id"])
                check_type(argname="argument property_id", value=property_id, expected_type=type_hints["property_id"])
                check_type(argname="argument property_logical_id", value=property_logical_id, expected_type=type_hints["property_logical_id"])
                check_type(argname="argument property_path", value=property_path, expected_type=type_hints["property_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if hierarchy_external_id is not None:
                self._values["hierarchy_external_id"] = hierarchy_external_id
            if hierarchy_id is not None:
                self._values["hierarchy_id"] = hierarchy_id
            if hierarchy_logical_id is not None:
                self._values["hierarchy_logical_id"] = hierarchy_logical_id
            if property_external_id is not None:
                self._values["property_external_id"] = property_external_id
            if property_id is not None:
                self._values["property_id"] = property_id
            if property_logical_id is not None:
                self._values["property_logical_id"] = property_logical_id
            if property_path is not None:
                self._values["property_path"] = property_path

        @builtins.property
        def hierarchy_external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID of the hierarchy being referenced.

            For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html#cfn-iotsitewise-assetmodel-variablevalue-hierarchyexternalid
            '''
            result = self._values.get("hierarchy_external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def hierarchy_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the hierarchy to query for the property ID.

            You can use the hierarchy's name instead of the hierarchy's ID. If the hierarchy has an external ID, you can specify ``externalId:`` followed by the external ID. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .

            You use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same ``propertyId`` . For example, you might have separately grouped assets that come from the same asset model. For more information, see `Asset hierarchies <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html#cfn-iotsitewise-assetmodel-variablevalue-hierarchyid
            '''
            result = self._values.get("hierarchy_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def hierarchy_logical_id(self) -> typing.Optional[builtins.str]:
            '''The ``LogicalID`` of the hierarchy to query for the ``PropertyLogicalID`` .

            You use a ``hierarchyLogicalID`` instead of a model ID because you can have several hierarchies using the same model and therefore the same property. For example, you might have separately grouped assets that come from the same asset model. For more information, see `Defining relationships between asset models (hierarchies) <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html#cfn-iotsitewise-assetmodel-variablevalue-hierarchylogicalid
            '''
            result = self._values.get("hierarchy_logical_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID of the property being referenced.

            For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html#cfn-iotsitewise-assetmodel-variablevalue-propertyexternalid
            '''
            result = self._values.get("property_external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the property to use as the variable.

            You can use the property ``name`` if it's from the same asset model. If the property has an external ID, you can specify ``externalId:`` followed by the external ID. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .
            .. epigraph::

               This is a return value and can't be set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html#cfn-iotsitewise-assetmodel-variablevalue-propertyid
            '''
            result = self._values.get("property_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_logical_id(self) -> typing.Optional[builtins.str]:
            '''The ``LogicalID`` of the property that is being referenced.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html#cfn-iotsitewise-assetmodel-variablevalue-propertylogicalid
            '''
            result = self._values.get("property_logical_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_path(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.PropertyPathDefinitionProperty"]]]]:
            '''The path of the property.

            Each step of the path is the name of the step. See the following example:

            ``PropertyPath: Name: AssetModelName Name: Composite1 Name: NestedComposite``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-assetmodel-variablevalue.html#cfn-iotsitewise-assetmodel-variablevalue-propertypath
            '''
            result = self._values.get("property_path")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAssetModel.PropertyPathDefinitionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VariableValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetModelProps",
    jsii_struct_bases=[],
    name_mapping={
        "asset_model_name": "assetModelName",
        "asset_model_composite_models": "assetModelCompositeModels",
        "asset_model_description": "assetModelDescription",
        "asset_model_external_id": "assetModelExternalId",
        "asset_model_hierarchies": "assetModelHierarchies",
        "asset_model_properties": "assetModelProperties",
        "asset_model_type": "assetModelType",
        "enforced_asset_model_interface_relationships": "enforcedAssetModelInterfaceRelationships",
        "tags": "tags",
    },
)
class CfnAssetModelProps:
    def __init__(
        self,
        *,
        asset_model_name: builtins.str,
        asset_model_composite_models: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.AssetModelCompositeModelProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        asset_model_description: typing.Optional[builtins.str] = None,
        asset_model_external_id: typing.Optional[builtins.str] = None,
        asset_model_hierarchies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.AssetModelHierarchyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        asset_model_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.AssetModelPropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        asset_model_type: typing.Optional[builtins.str] = None,
        enforced_asset_model_interface_relationships: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.EnforcedAssetModelInterfaceRelationshipProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAssetModel``.

        :param asset_model_name: A unique name for the asset model.
        :param asset_model_composite_models: The composite models that are part of this asset model. It groups properties (such as attributes, measurements, transforms, and metrics) and child composite models that model parts of your industrial equipment. Each composite model has a type that defines the properties that the composite model supports. Use composite models to define alarms on this asset model. .. epigraph:: When creating custom composite models, you need to use `CreateAssetModelCompositeModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html>`_ . For more information, see `Creating custom composite models (Components) <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-custom-composite-models.html>`_ in the *AWS IoT SiteWise User Guide* .
        :param asset_model_description: A description for the asset model.
        :param asset_model_external_id: The external ID of the asset model. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .
        :param asset_model_hierarchies: The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. For more information, see `Asset hierarchies <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html>`_ in the *AWS IoT SiteWise User Guide* . You can specify up to 10 hierarchies per asset model. For more information, see `Quotas <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html>`_ in the *AWS IoT SiteWise User Guide* .
        :param asset_model_properties: The property definitions of the asset model. For more information, see `Asset properties <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html>`_ in the *AWS IoT SiteWise User Guide* . You can specify up to 200 properties per asset model. For more information, see `Quotas <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html>`_ in the *AWS IoT SiteWise User Guide* .
        :param asset_model_type: The type of asset model. - *ASSET_MODEL* – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model. - *COMPONENT_MODEL* – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model.
        :param enforced_asset_model_interface_relationships: a list of asset model and interface relationships.
        :param tags: A list of key-value pairs that contain metadata for the asset. For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotsitewise as iotsitewise
            
            cfn_asset_model_props = iotsitewise.CfnAssetModelProps(
                asset_model_name="assetModelName",
            
                # the properties below are optional
                asset_model_composite_models=[iotsitewise.CfnAssetModel.AssetModelCompositeModelProperty(
                    name="name",
                    type="type",
            
                    # the properties below are optional
                    composed_asset_model_id="composedAssetModelId",
                    composite_model_properties=[iotsitewise.CfnAssetModel.AssetModelPropertyProperty(
                        data_type="dataType",
                        name="name",
                        type=iotsitewise.CfnAssetModel.PropertyTypeProperty(
                            type_name="typeName",
            
                            # the properties below are optional
                            attribute=iotsitewise.CfnAssetModel.AttributeProperty(
                                default_value="defaultValue"
                            ),
                            metric=iotsitewise.CfnAssetModel.MetricProperty(
                                expression="expression",
                                variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                                    name="name",
                                    value=iotsitewise.CfnAssetModel.VariableValueProperty(
                                        hierarchy_external_id="hierarchyExternalId",
                                        hierarchy_id="hierarchyId",
                                        hierarchy_logical_id="hierarchyLogicalId",
                                        property_external_id="propertyExternalId",
                                        property_id="propertyId",
                                        property_logical_id="propertyLogicalId",
                                        property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                            name="name"
                                        )]
                                    )
                                )],
                                window=iotsitewise.CfnAssetModel.MetricWindowProperty(
                                    tumbling=iotsitewise.CfnAssetModel.TumblingWindowProperty(
                                        interval="interval",
            
                                        # the properties below are optional
                                        offset="offset"
                                    )
                                )
                            ),
                            transform=iotsitewise.CfnAssetModel.TransformProperty(
                                expression="expression",
                                variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                                    name="name",
                                    value=iotsitewise.CfnAssetModel.VariableValueProperty(
                                        hierarchy_external_id="hierarchyExternalId",
                                        hierarchy_id="hierarchyId",
                                        hierarchy_logical_id="hierarchyLogicalId",
                                        property_external_id="propertyExternalId",
                                        property_id="propertyId",
                                        property_logical_id="propertyLogicalId",
                                        property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                            name="name"
                                        )]
                                    )
                                )]
                            )
                        ),
            
                        # the properties below are optional
                        data_type_spec="dataTypeSpec",
                        external_id="externalId",
                        id="id",
                        logical_id="logicalId",
                        unit="unit"
                    )],
                    description="description",
                    external_id="externalId",
                    id="id",
                    parent_asset_model_composite_model_external_id="parentAssetModelCompositeModelExternalId",
                    path=["path"]
                )],
                asset_model_description="assetModelDescription",
                asset_model_external_id="assetModelExternalId",
                asset_model_hierarchies=[iotsitewise.CfnAssetModel.AssetModelHierarchyProperty(
                    child_asset_model_id="childAssetModelId",
                    name="name",
            
                    # the properties below are optional
                    external_id="externalId",
                    id="id",
                    logical_id="logicalId"
                )],
                asset_model_properties=[iotsitewise.CfnAssetModel.AssetModelPropertyProperty(
                    data_type="dataType",
                    name="name",
                    type=iotsitewise.CfnAssetModel.PropertyTypeProperty(
                        type_name="typeName",
            
                        # the properties below are optional
                        attribute=iotsitewise.CfnAssetModel.AttributeProperty(
                            default_value="defaultValue"
                        ),
                        metric=iotsitewise.CfnAssetModel.MetricProperty(
                            expression="expression",
                            variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                                name="name",
                                value=iotsitewise.CfnAssetModel.VariableValueProperty(
                                    hierarchy_external_id="hierarchyExternalId",
                                    hierarchy_id="hierarchyId",
                                    hierarchy_logical_id="hierarchyLogicalId",
                                    property_external_id="propertyExternalId",
                                    property_id="propertyId",
                                    property_logical_id="propertyLogicalId",
                                    property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                        name="name"
                                    )]
                                )
                            )],
                            window=iotsitewise.CfnAssetModel.MetricWindowProperty(
                                tumbling=iotsitewise.CfnAssetModel.TumblingWindowProperty(
                                    interval="interval",
            
                                    # the properties below are optional
                                    offset="offset"
                                )
                            )
                        ),
                        transform=iotsitewise.CfnAssetModel.TransformProperty(
                            expression="expression",
                            variables=[iotsitewise.CfnAssetModel.ExpressionVariableProperty(
                                name="name",
                                value=iotsitewise.CfnAssetModel.VariableValueProperty(
                                    hierarchy_external_id="hierarchyExternalId",
                                    hierarchy_id="hierarchyId",
                                    hierarchy_logical_id="hierarchyLogicalId",
                                    property_external_id="propertyExternalId",
                                    property_id="propertyId",
                                    property_logical_id="propertyLogicalId",
                                    property_path=[iotsitewise.CfnAssetModel.PropertyPathDefinitionProperty(
                                        name="name"
                                    )]
                                )
                            )]
                        )
                    ),
            
                    # the properties below are optional
                    data_type_spec="dataTypeSpec",
                    external_id="externalId",
                    id="id",
                    logical_id="logicalId",
                    unit="unit"
                )],
                asset_model_type="assetModelType",
                enforced_asset_model_interface_relationships=[iotsitewise.CfnAssetModel.EnforcedAssetModelInterfaceRelationshipProperty(
                    interface_asset_model_id="interfaceAssetModelId",
                    property_mappings=[iotsitewise.CfnAssetModel.EnforcedAssetModelInterfacePropertyMappingProperty(
                        interface_asset_model_property_external_id="interfaceAssetModelPropertyExternalId",
            
                        # the properties below are optional
                        asset_model_property_external_id="assetModelPropertyExternalId",
                        asset_model_property_logical_id="assetModelPropertyLogicalId"
                    )]
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4c397ea0e26142735f716b5c92fe1c51048d94b5142d035ce8dc4cb1df79380)
            check_type(argname="argument asset_model_name", value=asset_model_name, expected_type=type_hints["asset_model_name"])
            check_type(argname="argument asset_model_composite_models", value=asset_model_composite_models, expected_type=type_hints["asset_model_composite_models"])
            check_type(argname="argument asset_model_description", value=asset_model_description, expected_type=type_hints["asset_model_description"])
            check_type(argname="argument asset_model_external_id", value=asset_model_external_id, expected_type=type_hints["asset_model_external_id"])
            check_type(argname="argument asset_model_hierarchies", value=asset_model_hierarchies, expected_type=type_hints["asset_model_hierarchies"])
            check_type(argname="argument asset_model_properties", value=asset_model_properties, expected_type=type_hints["asset_model_properties"])
            check_type(argname="argument asset_model_type", value=asset_model_type, expected_type=type_hints["asset_model_type"])
            check_type(argname="argument enforced_asset_model_interface_relationships", value=enforced_asset_model_interface_relationships, expected_type=type_hints["enforced_asset_model_interface_relationships"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "asset_model_name": asset_model_name,
        }
        if asset_model_composite_models is not None:
            self._values["asset_model_composite_models"] = asset_model_composite_models
        if asset_model_description is not None:
            self._values["asset_model_description"] = asset_model_description
        if asset_model_external_id is not None:
            self._values["asset_model_external_id"] = asset_model_external_id
        if asset_model_hierarchies is not None:
            self._values["asset_model_hierarchies"] = asset_model_hierarchies
        if asset_model_properties is not None:
            self._values["asset_model_properties"] = asset_model_properties
        if asset_model_type is not None:
            self._values["asset_model_type"] = asset_model_type
        if enforced_asset_model_interface_relationships is not None:
            self._values["enforced_asset_model_interface_relationships"] = enforced_asset_model_interface_relationships
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def asset_model_name(self) -> builtins.str:
        '''A unique name for the asset model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelname
        '''
        result = self._values.get("asset_model_name")
        assert result is not None, "Required property 'asset_model_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_model_composite_models(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAssetModel.AssetModelCompositeModelProperty]]]]:
        '''The composite models that are part of this asset model.

        It groups properties (such as attributes, measurements, transforms, and metrics) and child composite models that model parts of your industrial equipment. Each composite model has a type that defines the properties that the composite model supports. Use composite models to define alarms on this asset model.
        .. epigraph::

           When creating custom composite models, you need to use `CreateAssetModelCompositeModel <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html>`_ . For more information, see `Creating custom composite models (Components) <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-custom-composite-models.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelcompositemodels
        '''
        result = self._values.get("asset_model_composite_models")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAssetModel.AssetModelCompositeModelProperty]]]], result)

    @builtins.property
    def asset_model_description(self) -> typing.Optional[builtins.str]:
        '''A description for the asset model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodeldescription
        '''
        result = self._values.get("asset_model_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_model_external_id(self) -> typing.Optional[builtins.str]:
        '''The external ID of the asset model.

        For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelexternalid
        '''
        result = self._values.get("asset_model_external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_model_hierarchies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAssetModel.AssetModelHierarchyProperty]]]]:
        '''The hierarchy definitions of the asset model.

        Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. For more information, see `Asset hierarchies <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html>`_ in the *AWS IoT SiteWise User Guide* .

        You can specify up to 10 hierarchies per asset model. For more information, see `Quotas <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelhierarchies
        '''
        result = self._values.get("asset_model_hierarchies")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAssetModel.AssetModelHierarchyProperty]]]], result)

    @builtins.property
    def asset_model_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAssetModel.AssetModelPropertyProperty]]]]:
        '''The property definitions of the asset model.

        For more information, see `Asset properties <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html>`_ in the *AWS IoT SiteWise User Guide* .

        You can specify up to 200 properties per asset model. For more information, see `Quotas <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodelproperties
        '''
        result = self._values.get("asset_model_properties")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAssetModel.AssetModelPropertyProperty]]]], result)

    @builtins.property
    def asset_model_type(self) -> typing.Optional[builtins.str]:
        '''The type of asset model.

        - *ASSET_MODEL* – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.
        - *COMPONENT_MODEL* – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-assetmodeltype
        '''
        result = self._values.get("asset_model_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enforced_asset_model_interface_relationships(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAssetModel.EnforcedAssetModelInterfaceRelationshipProperty]]]]:
        '''a list of asset model and interface relationships.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-enforcedassetmodelinterfacerelationships
        '''
        result = self._values.get("enforced_asset_model_interface_relationships")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAssetModel.EnforcedAssetModelInterfaceRelationshipProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the asset.

        For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-assetmodel.html#cfn-iotsitewise-assetmodel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssetModelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnAssetProps",
    jsii_struct_bases=[],
    name_mapping={
        "asset_model_id": "assetModelId",
        "asset_name": "assetName",
        "asset_description": "assetDescription",
        "asset_external_id": "assetExternalId",
        "asset_hierarchies": "assetHierarchies",
        "asset_properties": "assetProperties",
        "tags": "tags",
    },
)
class CfnAssetProps:
    def __init__(
        self,
        *,
        asset_model_id: builtins.str,
        asset_name: builtins.str,
        asset_description: typing.Optional[builtins.str] = None,
        asset_external_id: typing.Optional[builtins.str] = None,
        asset_hierarchies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAsset.AssetHierarchyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        asset_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAsset.AssetPropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAsset``.

        :param asset_model_id: The ID of the asset model from which to create the asset. This can be either the actual ID in UUID format, or else ``externalId:`` followed by the external ID, if it has one. For more information, see `Referencing objects with external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references>`_ in the *AWS IoT SiteWise User Guide* .
        :param asset_name: A friendly name for the asset.
        :param asset_description: The ID of the asset, in UUID format.
        :param asset_external_id: The external ID of the asset model composite model. For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .
        :param asset_hierarchies: A list of asset hierarchies that each contain a ``hierarchyId`` . A hierarchy specifies allowed parent/child asset relationships.
        :param asset_properties: The list of asset properties for the asset. This object doesn't include properties that you define in composite models. You can find composite model properties in the ``assetCompositeModels`` object.
        :param tags: A list of key-value pairs that contain metadata for the asset. For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotsitewise as iotsitewise
            
            cfn_asset_props = iotsitewise.CfnAssetProps(
                asset_model_id="assetModelId",
                asset_name="assetName",
            
                # the properties below are optional
                asset_description="assetDescription",
                asset_external_id="assetExternalId",
                asset_hierarchies=[iotsitewise.CfnAsset.AssetHierarchyProperty(
                    child_asset_id="childAssetId",
            
                    # the properties below are optional
                    external_id="externalId",
                    id="id",
                    logical_id="logicalId"
                )],
                asset_properties=[iotsitewise.CfnAsset.AssetPropertyProperty(
                    alias="alias",
                    external_id="externalId",
                    id="id",
                    logical_id="logicalId",
                    notification_state="notificationState",
                    unit="unit"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__306f4833ce13fd25ec4269f2a96d0ee80f11a34f43885f5b4b372569dc9f7931)
            check_type(argname="argument asset_model_id", value=asset_model_id, expected_type=type_hints["asset_model_id"])
            check_type(argname="argument asset_name", value=asset_name, expected_type=type_hints["asset_name"])
            check_type(argname="argument asset_description", value=asset_description, expected_type=type_hints["asset_description"])
            check_type(argname="argument asset_external_id", value=asset_external_id, expected_type=type_hints["asset_external_id"])
            check_type(argname="argument asset_hierarchies", value=asset_hierarchies, expected_type=type_hints["asset_hierarchies"])
            check_type(argname="argument asset_properties", value=asset_properties, expected_type=type_hints["asset_properties"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "asset_model_id": asset_model_id,
            "asset_name": asset_name,
        }
        if asset_description is not None:
            self._values["asset_description"] = asset_description
        if asset_external_id is not None:
            self._values["asset_external_id"] = asset_external_id
        if asset_hierarchies is not None:
            self._values["asset_hierarchies"] = asset_hierarchies
        if asset_properties is not None:
            self._values["asset_properties"] = asset_properties
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def asset_model_id(self) -> builtins.str:
        '''The ID of the asset model from which to create the asset.

        This can be either the actual ID in UUID format, or else ``externalId:`` followed by the external ID, if it has one. For more information, see `Referencing objects with external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetmodelid
        '''
        result = self._values.get("asset_model_id")
        assert result is not None, "Required property 'asset_model_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_name(self) -> builtins.str:
        '''A friendly name for the asset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetname
        '''
        result = self._values.get("asset_name")
        assert result is not None, "Required property 'asset_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_description(self) -> typing.Optional[builtins.str]:
        '''The ID of the asset, in UUID format.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetdescription
        '''
        result = self._values.get("asset_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_external_id(self) -> typing.Optional[builtins.str]:
        '''The external ID of the asset model composite model.

        For more information, see `Using external IDs <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetexternalid
        '''
        result = self._values.get("asset_external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_hierarchies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAsset.AssetHierarchyProperty]]]]:
        '''A list of asset hierarchies that each contain a ``hierarchyId`` .

        A hierarchy specifies allowed parent/child asset relationships.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assethierarchies
        '''
        result = self._values.get("asset_hierarchies")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAsset.AssetHierarchyProperty]]]], result)

    @builtins.property
    def asset_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAsset.AssetPropertyProperty]]]]:
        '''The list of asset properties for the asset.

        This object doesn't include properties that you define in composite models. You can find composite model properties in the ``assetCompositeModels`` object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-assetproperties
        '''
        result = self._values.get("asset_properties")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAsset.AssetPropertyProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the asset.

        For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-asset.html#cfn-iotsitewise-asset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnComputationModel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnComputationModel",
):
    '''Resource schema for AWS::IoTSiteWise::ComputationModel.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-computationmodel.html
    :cloudformationResource: AWS::IoTSiteWise::ComputationModel
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotsitewise as iotsitewise
        
        # computation_model_data_binding_value_property_: iotsitewise.CfnComputationModel.ComputationModelDataBindingValueProperty
        
        cfn_computation_model = iotsitewise.CfnComputationModel(self, "MyCfnComputationModel",
            computation_model_configuration=iotsitewise.CfnComputationModel.ComputationModelConfigurationProperty(
                anomaly_detection=iotsitewise.CfnComputationModel.AnomalyDetectionComputationModelConfigurationProperty(
                    input_properties="inputProperties",
                    result_property="resultProperty"
                )
            ),
            computation_model_data_binding={
                "computation_model_data_binding_key": iotsitewise.CfnComputationModel.ComputationModelDataBindingValueProperty(
                    asset_model_property=iotsitewise.CfnComputationModel.AssetModelPropertyBindingValueProperty(
                        asset_model_id="assetModelId",
                        property_id="propertyId"
                    ),
                    asset_property=iotsitewise.CfnComputationModel.AssetPropertyBindingValueProperty(
                        asset_id="assetId",
                        property_id="propertyId"
                    ),
                    list=[computation_model_data_binding_value_property_]
                )
            },
            computation_model_name="computationModelName",
        
            # the properties below are optional
            computation_model_description="computationModelDescription",
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
        computation_model_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputationModel.ComputationModelConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        computation_model_data_binding: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputationModel.ComputationModelDataBindingValueProperty", typing.Dict[builtins.str, typing.Any]]]]],
        computation_model_name: builtins.str,
        computation_model_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param computation_model_configuration: 
        :param computation_model_data_binding: 
        :param computation_model_name: The name of the computation model.
        :param computation_model_description: A description about the computation model.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__566bf1711c9dcacb9cb88add46c2c4e157208bdce4a774ccb256a7d21c68de89)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnComputationModelProps(
            computation_model_configuration=computation_model_configuration,
            computation_model_data_binding=computation_model_data_binding,
            computation_model_name=computation_model_name,
            computation_model_description=computation_model_description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__137e70d4839513d333c73d5f02909172ab78f14b28c52c7f13f6f52ff398e870)
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
            type_hints = typing.get_type_hints(_typecheckingstub__27af8e5f561e3e573b9a04774edf0c0c6cf2f3e31d385b4ffe28873a39dc7e48)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrComputationModelArn")
    def attr_computation_model_arn(self) -> builtins.str:
        '''The ARN of the computation model.

        :cloudformationAttribute: ComputationModelArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrComputationModelArn"))

    @builtins.property
    @jsii.member(jsii_name="attrComputationModelId")
    def attr_computation_model_id(self) -> builtins.str:
        '''The ID of the computation model.

        :cloudformationAttribute: ComputationModelId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrComputationModelId"))

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
    @jsii.member(jsii_name="computationModelConfiguration")
    def computation_model_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnComputationModel.ComputationModelConfigurationProperty"]:
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnComputationModel.ComputationModelConfigurationProperty"], jsii.get(self, "computationModelConfiguration"))

    @computation_model_configuration.setter
    def computation_model_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnComputationModel.ComputationModelConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fa195f1583c09a0caa02fa5c50ed928dbf5232ca80e6affc9fa715d83e57cd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computationModelConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="computationModelDataBinding")
    def computation_model_data_binding(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnComputationModel.ComputationModelDataBindingValueProperty"]]]:
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnComputationModel.ComputationModelDataBindingValueProperty"]]], jsii.get(self, "computationModelDataBinding"))

    @computation_model_data_binding.setter
    def computation_model_data_binding(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnComputationModel.ComputationModelDataBindingValueProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be967ec7617c0ed0efa50fb8a3519a87b8800751beb73a6449a1637314931d2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computationModelDataBinding", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="computationModelName")
    def computation_model_name(self) -> builtins.str:
        '''The name of the computation model.'''
        return typing.cast(builtins.str, jsii.get(self, "computationModelName"))

    @computation_model_name.setter
    def computation_model_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a009db7b645690134b3878ea2c7cdee53682cf297919e1b3f54b712539f8b0de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computationModelName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="computationModelDescription")
    def computation_model_description(self) -> typing.Optional[builtins.str]:
        '''A description about the computation model.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computationModelDescription"))

    @computation_model_description.setter
    def computation_model_description(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d577131789cc578cee733460d23165debfb49d0d90b94e3e10d38d4d0d44a79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computationModelDescription", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a82834353206c4a7be4a8ed40665c48481769bb21be0214fd279c598a8007929)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnComputationModel.AnomalyDetectionComputationModelConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_properties": "inputProperties",
            "result_property": "resultProperty",
        },
    )
    class AnomalyDetectionComputationModelConfigurationProperty:
        def __init__(
            self,
            *,
            input_properties: builtins.str,
            result_property: builtins.str,
        ) -> None:
            '''
            :param input_properties: Input properties for anomaly detection.
            :param result_property: Result property for anomaly detection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                anomaly_detection_computation_model_configuration_property = iotsitewise.CfnComputationModel.AnomalyDetectionComputationModelConfigurationProperty(
                    input_properties="inputProperties",
                    result_property="resultProperty"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__69d1839ca00b91b9b1180620638bc2ec0b687463e3828b79ad3dd49ef5189aa7)
                check_type(argname="argument input_properties", value=input_properties, expected_type=type_hints["input_properties"])
                check_type(argname="argument result_property", value=result_property, expected_type=type_hints["result_property"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_properties": input_properties,
                "result_property": result_property,
            }

        @builtins.property
        def input_properties(self) -> builtins.str:
            '''Input properties for anomaly detection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration.html#cfn-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration-inputproperties
            '''
            result = self._values.get("input_properties")
            assert result is not None, "Required property 'input_properties' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def result_property(self) -> builtins.str:
            '''Result property for anomaly detection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration.html#cfn-iotsitewise-computationmodel-anomalydetectioncomputationmodelconfiguration-resultproperty
            '''
            result = self._values.get("result_property")
            assert result is not None, "Required property 'result_property' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnomalyDetectionComputationModelConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnComputationModel.AssetModelPropertyBindingValueProperty",
        jsii_struct_bases=[],
        name_mapping={"asset_model_id": "assetModelId", "property_id": "propertyId"},
    )
    class AssetModelPropertyBindingValueProperty:
        def __init__(
            self,
            *,
            asset_model_id: builtins.str,
            property_id: builtins.str,
        ) -> None:
            '''
            :param asset_model_id: The ID of the asset model.
            :param property_id: The ID of the asset model property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-computationmodel-assetmodelpropertybindingvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                asset_model_property_binding_value_property = iotsitewise.CfnComputationModel.AssetModelPropertyBindingValueProperty(
                    asset_model_id="assetModelId",
                    property_id="propertyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__949067d8ab294bdc850ab646091006fd0e748f018285b21dcc99fb980c1a0f5e)
                check_type(argname="argument asset_model_id", value=asset_model_id, expected_type=type_hints["asset_model_id"])
                check_type(argname="argument property_id", value=property_id, expected_type=type_hints["property_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "asset_model_id": asset_model_id,
                "property_id": property_id,
            }

        @builtins.property
        def asset_model_id(self) -> builtins.str:
            '''The ID of the asset model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-computationmodel-assetmodelpropertybindingvalue.html#cfn-iotsitewise-computationmodel-assetmodelpropertybindingvalue-assetmodelid
            '''
            result = self._values.get("asset_model_id")
            assert result is not None, "Required property 'asset_model_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def property_id(self) -> builtins.str:
            '''The ID of the asset model property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-computationmodel-assetmodelpropertybindingvalue.html#cfn-iotsitewise-computationmodel-assetmodelpropertybindingvalue-propertyid
            '''
            result = self._values.get("property_id")
            assert result is not None, "Required property 'property_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetModelPropertyBindingValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnComputationModel.AssetPropertyBindingValueProperty",
        jsii_struct_bases=[],
        name_mapping={"asset_id": "assetId", "property_id": "propertyId"},
    )
    class AssetPropertyBindingValueProperty:
        def __init__(
            self,
            *,
            asset_id: builtins.str,
            property_id: builtins.str,
        ) -> None:
            '''
            :param asset_id: The ID of the asset.
            :param property_id: The ID of the asset property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-computationmodel-assetpropertybindingvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                asset_property_binding_value_property = iotsitewise.CfnComputationModel.AssetPropertyBindingValueProperty(
                    asset_id="assetId",
                    property_id="propertyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e4a3ae5efabf3788291f9b7ef194e309cc061d66db8346fea04452f02980728d)
                check_type(argname="argument asset_id", value=asset_id, expected_type=type_hints["asset_id"])
                check_type(argname="argument property_id", value=property_id, expected_type=type_hints["property_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "asset_id": asset_id,
                "property_id": property_id,
            }

        @builtins.property
        def asset_id(self) -> builtins.str:
            '''The ID of the asset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-computationmodel-assetpropertybindingvalue.html#cfn-iotsitewise-computationmodel-assetpropertybindingvalue-assetid
            '''
            result = self._values.get("asset_id")
            assert result is not None, "Required property 'asset_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def property_id(self) -> builtins.str:
            '''The ID of the asset property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-computationmodel-assetpropertybindingvalue.html#cfn-iotsitewise-computationmodel-assetpropertybindingvalue-propertyid
            '''
            result = self._values.get("property_id")
            assert result is not None, "Required property 'property_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyBindingValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnComputationModel.ComputationModelConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"anomaly_detection": "anomalyDetection"},
    )
    class ComputationModelConfigurationProperty:
        def __init__(
            self,
            *,
            anomaly_detection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputationModel.AnomalyDetectionComputationModelConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param anomaly_detection: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-computationmodel-computationmodelconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                computation_model_configuration_property = iotsitewise.CfnComputationModel.ComputationModelConfigurationProperty(
                    anomaly_detection=iotsitewise.CfnComputationModel.AnomalyDetectionComputationModelConfigurationProperty(
                        input_properties="inputProperties",
                        result_property="resultProperty"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7b33f062481ddc382b1fb7a44ec3672f2844ad5a2ee31f5ede04b108b279328e)
                check_type(argname="argument anomaly_detection", value=anomaly_detection, expected_type=type_hints["anomaly_detection"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if anomaly_detection is not None:
                self._values["anomaly_detection"] = anomaly_detection

        @builtins.property
        def anomaly_detection(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputationModel.AnomalyDetectionComputationModelConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-computationmodel-computationmodelconfiguration.html#cfn-iotsitewise-computationmodel-computationmodelconfiguration-anomalydetection
            '''
            result = self._values.get("anomaly_detection")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputationModel.AnomalyDetectionComputationModelConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComputationModelConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnComputationModel.ComputationModelDataBindingValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "asset_model_property": "assetModelProperty",
            "asset_property": "assetProperty",
            "list": "list",
        },
    )
    class ComputationModelDataBindingValueProperty:
        def __init__(
            self,
            *,
            asset_model_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputationModel.AssetModelPropertyBindingValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            asset_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputationModel.AssetPropertyBindingValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputationModel.ComputationModelDataBindingValueProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''
            :param asset_model_property: 
            :param asset_property: 
            :param list: Defines a list of computation model binding values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-computationmodel-computationmodeldatabindingvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                # computation_model_data_binding_value_property_: iotsitewise.CfnComputationModel.ComputationModelDataBindingValueProperty
                
                computation_model_data_binding_value_property = iotsitewise.CfnComputationModel.ComputationModelDataBindingValueProperty(
                    asset_model_property=iotsitewise.CfnComputationModel.AssetModelPropertyBindingValueProperty(
                        asset_model_id="assetModelId",
                        property_id="propertyId"
                    ),
                    asset_property=iotsitewise.CfnComputationModel.AssetPropertyBindingValueProperty(
                        asset_id="assetId",
                        property_id="propertyId"
                    ),
                    list=[computation_model_data_binding_value_property_]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__30609777f6bb1d4c3fb4232f9af93dc24089504c669f64d1de9edd24a9e6d0df)
                check_type(argname="argument asset_model_property", value=asset_model_property, expected_type=type_hints["asset_model_property"])
                check_type(argname="argument asset_property", value=asset_property, expected_type=type_hints["asset_property"])
                check_type(argname="argument list", value=list, expected_type=type_hints["list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if asset_model_property is not None:
                self._values["asset_model_property"] = asset_model_property
            if asset_property is not None:
                self._values["asset_property"] = asset_property
            if list is not None:
                self._values["list"] = list

        @builtins.property
        def asset_model_property(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputationModel.AssetModelPropertyBindingValueProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-computationmodel-computationmodeldatabindingvalue.html#cfn-iotsitewise-computationmodel-computationmodeldatabindingvalue-assetmodelproperty
            '''
            result = self._values.get("asset_model_property")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputationModel.AssetModelPropertyBindingValueProperty"]], result)

        @builtins.property
        def asset_property(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputationModel.AssetPropertyBindingValueProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-computationmodel-computationmodeldatabindingvalue.html#cfn-iotsitewise-computationmodel-computationmodeldatabindingvalue-assetproperty
            '''
            result = self._values.get("asset_property")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputationModel.AssetPropertyBindingValueProperty"]], result)

        @builtins.property
        def list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComputationModel.ComputationModelDataBindingValueProperty"]]]]:
            '''Defines a list of computation model binding values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-computationmodel-computationmodeldatabindingvalue.html#cfn-iotsitewise-computationmodel-computationmodeldatabindingvalue-list
            '''
            result = self._values.get("list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComputationModel.ComputationModelDataBindingValueProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComputationModelDataBindingValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnComputationModelProps",
    jsii_struct_bases=[],
    name_mapping={
        "computation_model_configuration": "computationModelConfiguration",
        "computation_model_data_binding": "computationModelDataBinding",
        "computation_model_name": "computationModelName",
        "computation_model_description": "computationModelDescription",
        "tags": "tags",
    },
)
class CfnComputationModelProps:
    def __init__(
        self,
        *,
        computation_model_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputationModel.ComputationModelConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        computation_model_data_binding: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputationModel.ComputationModelDataBindingValueProperty, typing.Dict[builtins.str, typing.Any]]]]],
        computation_model_name: builtins.str,
        computation_model_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnComputationModel``.

        :param computation_model_configuration: 
        :param computation_model_data_binding: 
        :param computation_model_name: The name of the computation model.
        :param computation_model_description: A description about the computation model.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-computationmodel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotsitewise as iotsitewise
            
            # computation_model_data_binding_value_property_: iotsitewise.CfnComputationModel.ComputationModelDataBindingValueProperty
            
            cfn_computation_model_props = iotsitewise.CfnComputationModelProps(
                computation_model_configuration=iotsitewise.CfnComputationModel.ComputationModelConfigurationProperty(
                    anomaly_detection=iotsitewise.CfnComputationModel.AnomalyDetectionComputationModelConfigurationProperty(
                        input_properties="inputProperties",
                        result_property="resultProperty"
                    )
                ),
                computation_model_data_binding={
                    "computation_model_data_binding_key": iotsitewise.CfnComputationModel.ComputationModelDataBindingValueProperty(
                        asset_model_property=iotsitewise.CfnComputationModel.AssetModelPropertyBindingValueProperty(
                            asset_model_id="assetModelId",
                            property_id="propertyId"
                        ),
                        asset_property=iotsitewise.CfnComputationModel.AssetPropertyBindingValueProperty(
                            asset_id="assetId",
                            property_id="propertyId"
                        ),
                        list=[computation_model_data_binding_value_property_]
                    )
                },
                computation_model_name="computationModelName",
            
                # the properties below are optional
                computation_model_description="computationModelDescription",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed97b2e804664b4c2090fb09c1141fc63e60c4fbaee41661ef227778c1ed7dd3)
            check_type(argname="argument computation_model_configuration", value=computation_model_configuration, expected_type=type_hints["computation_model_configuration"])
            check_type(argname="argument computation_model_data_binding", value=computation_model_data_binding, expected_type=type_hints["computation_model_data_binding"])
            check_type(argname="argument computation_model_name", value=computation_model_name, expected_type=type_hints["computation_model_name"])
            check_type(argname="argument computation_model_description", value=computation_model_description, expected_type=type_hints["computation_model_description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "computation_model_configuration": computation_model_configuration,
            "computation_model_data_binding": computation_model_data_binding,
            "computation_model_name": computation_model_name,
        }
        if computation_model_description is not None:
            self._values["computation_model_description"] = computation_model_description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def computation_model_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnComputationModel.ComputationModelConfigurationProperty]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-computationmodel.html#cfn-iotsitewise-computationmodel-computationmodelconfiguration
        '''
        result = self._values.get("computation_model_configuration")
        assert result is not None, "Required property 'computation_model_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnComputationModel.ComputationModelConfigurationProperty], result)

    @builtins.property
    def computation_model_data_binding(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnComputationModel.ComputationModelDataBindingValueProperty]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-computationmodel.html#cfn-iotsitewise-computationmodel-computationmodeldatabinding
        '''
        result = self._values.get("computation_model_data_binding")
        assert result is not None, "Required property 'computation_model_data_binding' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnComputationModel.ComputationModelDataBindingValueProperty]]], result)

    @builtins.property
    def computation_model_name(self) -> builtins.str:
        '''The name of the computation model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-computationmodel.html#cfn-iotsitewise-computationmodel-computationmodelname
        '''
        result = self._values.get("computation_model_name")
        assert result is not None, "Required property 'computation_model_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def computation_model_description(self) -> typing.Optional[builtins.str]:
        '''A description about the computation model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-computationmodel.html#cfn-iotsitewise-computationmodel-computationmodeldescription
        '''
        result = self._values.get("computation_model_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-computationmodel.html#cfn-iotsitewise-computationmodel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnComputationModelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDashboard(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnDashboard",
):
    '''Creates a dashboard in an AWS IoT SiteWise Monitor project.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html
    :cloudformationResource: AWS::IoTSiteWise::Dashboard
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotsitewise as iotsitewise
        
        cfn_dashboard = iotsitewise.CfnDashboard(self, "MyCfnDashboard",
            dashboard_definition="dashboardDefinition",
            dashboard_description="dashboardDescription",
            dashboard_name="dashboardName",
        
            # the properties below are optional
            project_id="projectId",
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
        dashboard_definition: builtins.str,
        dashboard_description: builtins.str,
        dashboard_name: builtins.str,
        project_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param dashboard_definition: The dashboard definition specified in a JSON literal. - AWS IoT SiteWise Monitor (Classic) see `Create dashboards ( AWS CLI ) <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html>`_ - AWS IoT SiteWise Monitor (AI-aware) see `Create dashboards ( AWS CLI ) <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-ai-dashboard-cli.html>`_ in the *AWS IoT SiteWise User Guide*
        :param dashboard_description: A description for the dashboard.
        :param dashboard_name: A friendly name for the dashboard.
        :param project_id: The ID of the project in which to create the dashboard.
        :param tags: A list of key-value pairs that contain metadata for the dashboard. For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7408e63e7ba97e630e06dc4a383d275da9719808da2d750b179e27c09b363329)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDashboardProps(
            dashboard_definition=dashboard_definition,
            dashboard_description=dashboard_description,
            dashboard_name=dashboard_name,
            project_id=project_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b472ad5fec8e10a47deb9d29be81c0539f4b5be2ab95923bc43842cace7b7859)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c575a08895bd58ff6950d32eea6f2d29ac539b1a8ea16ab5a6815a167a66a53)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDashboardArn")
    def attr_dashboard_arn(self) -> builtins.str:
        '''The `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ of the dashboard, which has the following format.

        ``arn:${Partition}:iotsitewise:${Region}:${Account}:dashboard/${DashboardId}``

        :cloudformationAttribute: DashboardArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDashboardArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDashboardId")
    def attr_dashboard_id(self) -> builtins.str:
        '''The ID of the dashboard.

        :cloudformationAttribute: DashboardId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDashboardId"))

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
    @jsii.member(jsii_name="dashboardDefinition")
    def dashboard_definition(self) -> builtins.str:
        '''The dashboard definition specified in a JSON literal.'''
        return typing.cast(builtins.str, jsii.get(self, "dashboardDefinition"))

    @dashboard_definition.setter
    def dashboard_definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dff968d51e506fdd3d98d6169f84765246ff8d86876d701729950862efbcb07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashboardDefinition", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dashboardDescription")
    def dashboard_description(self) -> builtins.str:
        '''A description for the dashboard.'''
        return typing.cast(builtins.str, jsii.get(self, "dashboardDescription"))

    @dashboard_description.setter
    def dashboard_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2e71c5b9cc6130bf794aba4fc07bef70a290bd69088f6d2e772d1c018383a99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashboardDescription", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dashboardName")
    def dashboard_name(self) -> builtins.str:
        '''A friendly name for the dashboard.'''
        return typing.cast(builtins.str, jsii.get(self, "dashboardName"))

    @dashboard_name.setter
    def dashboard_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44f37a7656daf53d7fabe76785ece45b5c2bc6eb84289aacfae174ffe2497a56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashboardName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which to create the dashboard.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d621f50afe555c434794e30d38d7e134a8c91ebdac9f42da18c26db60e90e079)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the dashboard.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c685ecf3c21151b25cdde509c49bdd7b2812d894f5dab8c2fd028d7ea55b28c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnDashboardProps",
    jsii_struct_bases=[],
    name_mapping={
        "dashboard_definition": "dashboardDefinition",
        "dashboard_description": "dashboardDescription",
        "dashboard_name": "dashboardName",
        "project_id": "projectId",
        "tags": "tags",
    },
)
class CfnDashboardProps:
    def __init__(
        self,
        *,
        dashboard_definition: builtins.str,
        dashboard_description: builtins.str,
        dashboard_name: builtins.str,
        project_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDashboard``.

        :param dashboard_definition: The dashboard definition specified in a JSON literal. - AWS IoT SiteWise Monitor (Classic) see `Create dashboards ( AWS CLI ) <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html>`_ - AWS IoT SiteWise Monitor (AI-aware) see `Create dashboards ( AWS CLI ) <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-ai-dashboard-cli.html>`_ in the *AWS IoT SiteWise User Guide*
        :param dashboard_description: A description for the dashboard.
        :param dashboard_name: A friendly name for the dashboard.
        :param project_id: The ID of the project in which to create the dashboard.
        :param tags: A list of key-value pairs that contain metadata for the dashboard. For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotsitewise as iotsitewise
            
            cfn_dashboard_props = iotsitewise.CfnDashboardProps(
                dashboard_definition="dashboardDefinition",
                dashboard_description="dashboardDescription",
                dashboard_name="dashboardName",
            
                # the properties below are optional
                project_id="projectId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e87db1e2d08493321e273557f52f1665d6e8b066bd235aa15fbe6b372c969da)
            check_type(argname="argument dashboard_definition", value=dashboard_definition, expected_type=type_hints["dashboard_definition"])
            check_type(argname="argument dashboard_description", value=dashboard_description, expected_type=type_hints["dashboard_description"])
            check_type(argname="argument dashboard_name", value=dashboard_name, expected_type=type_hints["dashboard_name"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dashboard_definition": dashboard_definition,
            "dashboard_description": dashboard_description,
            "dashboard_name": dashboard_name,
        }
        if project_id is not None:
            self._values["project_id"] = project_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def dashboard_definition(self) -> builtins.str:
        '''The dashboard definition specified in a JSON literal.

        - AWS IoT SiteWise Monitor (Classic) see `Create dashboards ( AWS CLI ) <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html>`_
        - AWS IoT SiteWise Monitor (AI-aware) see `Create dashboards ( AWS CLI ) <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-ai-dashboard-cli.html>`_

        in the *AWS IoT SiteWise User Guide*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-dashboarddefinition
        '''
        result = self._values.get("dashboard_definition")
        assert result is not None, "Required property 'dashboard_definition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_description(self) -> builtins.str:
        '''A description for the dashboard.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-dashboarddescription
        '''
        result = self._values.get("dashboard_description")
        assert result is not None, "Required property 'dashboard_description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_name(self) -> builtins.str:
        '''A friendly name for the dashboard.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-dashboardname
        '''
        result = self._values.get("dashboard_name")
        assert result is not None, "Required property 'dashboard_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which to create the dashboard.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-projectid
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the dashboard.

        For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dashboard.html#cfn-iotsitewise-dashboard-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDashboardProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnDataset(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnDataset",
):
    '''Resource schema for AWS::IoTSiteWise::Dataset.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dataset.html
    :cloudformationResource: AWS::IoTSiteWise::Dataset
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotsitewise as iotsitewise
        
        cfn_dataset = iotsitewise.CfnDataset(self, "MyCfnDataset",
            dataset_name="datasetName",
            dataset_source=iotsitewise.CfnDataset.DatasetSourceProperty(
                source_format="sourceFormat",
                source_type="sourceType",
        
                # the properties below are optional
                source_detail=iotsitewise.CfnDataset.SourceDetailProperty(
                    kendra=iotsitewise.CfnDataset.KendraSourceDetailProperty(
                        knowledge_base_arn="knowledgeBaseArn",
                        role_arn="roleArn"
                    )
                )
            ),
        
            # the properties below are optional
            dataset_description="datasetDescription",
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
        dataset_name: builtins.str,
        dataset_source: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.DatasetSourceProperty", typing.Dict[builtins.str, typing.Any]]],
        dataset_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param dataset_name: The name of the dataset.
        :param dataset_source: 
        :param dataset_description: A description about the dataset, and its functionality.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44369ff07e07f1dbb28102a65eb5a8e6317f5b2e832b326cf3fc0bef13d7e1cc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatasetProps(
            dataset_name=dataset_name,
            dataset_source=dataset_source,
            dataset_description=dataset_description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c537b447cd6a1f193bb6937137b32d81fb8fc58b3637f501b722c0a287eff25e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__052a04636940cb669719f99afdd8ce7ebf71823f5bd4fc4a56e8e06e962e930e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDatasetArn")
    def attr_dataset_arn(self) -> builtins.str:
        '''The ARN of the dataset.

        :cloudformationAttribute: DatasetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatasetArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDatasetId")
    def attr_dataset_id(self) -> builtins.str:
        '''The ID of the dataset.

        :cloudformationAttribute: DatasetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatasetId"))

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
    @jsii.member(jsii_name="datasetName")
    def dataset_name(self) -> builtins.str:
        '''The name of the dataset.'''
        return typing.cast(builtins.str, jsii.get(self, "datasetName"))

    @dataset_name.setter
    def dataset_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b47777cde433184527816fbc94a5e50f4751f14ba951445e4260fbf75e5f9ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="datasetSource")
    def dataset_source(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnDataset.DatasetSourceProperty"]:
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDataset.DatasetSourceProperty"], jsii.get(self, "datasetSource"))

    @dataset_source.setter
    def dataset_source(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnDataset.DatasetSourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ee08c36e5cc935e5be89b5ecc51c303d15d2f3f60f818632c78e21d65cc0e19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetSource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="datasetDescription")
    def dataset_description(self) -> typing.Optional[builtins.str]:
        '''A description about the dataset, and its functionality.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetDescription"))

    @dataset_description.setter
    def dataset_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb27e9e2c5f0a4b58c2867084de6a19d127db8e56f71ceb33ecb4c038c5aeba9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetDescription", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc32716df823dcb28cde4279865e5af2ea0ed286db7d62b848f8ebbc49079037)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnDataset.DatasetSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_format": "sourceFormat",
            "source_type": "sourceType",
            "source_detail": "sourceDetail",
        },
    )
    class DatasetSourceProperty:
        def __init__(
            self,
            *,
            source_format: builtins.str,
            source_type: builtins.str,
            source_detail: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.SourceDetailProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param source_format: The format of the dataset source associated with the dataset.
            :param source_type: The type of data source for the dataset.
            :param source_detail: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-dataset-datasetsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                dataset_source_property = iotsitewise.CfnDataset.DatasetSourceProperty(
                    source_format="sourceFormat",
                    source_type="sourceType",
                
                    # the properties below are optional
                    source_detail=iotsitewise.CfnDataset.SourceDetailProperty(
                        kendra=iotsitewise.CfnDataset.KendraSourceDetailProperty(
                            knowledge_base_arn="knowledgeBaseArn",
                            role_arn="roleArn"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f58345f56b93936a864a7b8b77051f0ab53f3948caa6107fb0e0b5e918839970)
                check_type(argname="argument source_format", value=source_format, expected_type=type_hints["source_format"])
                check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
                check_type(argname="argument source_detail", value=source_detail, expected_type=type_hints["source_detail"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source_format": source_format,
                "source_type": source_type,
            }
            if source_detail is not None:
                self._values["source_detail"] = source_detail

        @builtins.property
        def source_format(self) -> builtins.str:
            '''The format of the dataset source associated with the dataset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-dataset-datasetsource.html#cfn-iotsitewise-dataset-datasetsource-sourceformat
            '''
            result = self._values.get("source_format")
            assert result is not None, "Required property 'source_format' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_type(self) -> builtins.str:
            '''The type of data source for the dataset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-dataset-datasetsource.html#cfn-iotsitewise-dataset-datasetsource-sourcetype
            '''
            result = self._values.get("source_type")
            assert result is not None, "Required property 'source_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_detail(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.SourceDetailProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-dataset-datasetsource.html#cfn-iotsitewise-dataset-datasetsource-sourcedetail
            '''
            result = self._values.get("source_detail")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.SourceDetailProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnDataset.KendraSourceDetailProperty",
        jsii_struct_bases=[],
        name_mapping={"knowledge_base_arn": "knowledgeBaseArn", "role_arn": "roleArn"},
    )
    class KendraSourceDetailProperty:
        def __init__(
            self,
            *,
            knowledge_base_arn: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''
            :param knowledge_base_arn: The knowledgeBaseArn details for the Kendra dataset source.
            :param role_arn: The roleARN details for the Kendra dataset source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-dataset-kendrasourcedetail.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                kendra_source_detail_property = iotsitewise.CfnDataset.KendraSourceDetailProperty(
                    knowledge_base_arn="knowledgeBaseArn",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5d827c7c36898f2d8c24814838df150d16db4b05143943eaff03575fc4152bf9)
                check_type(argname="argument knowledge_base_arn", value=knowledge_base_arn, expected_type=type_hints["knowledge_base_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "knowledge_base_arn": knowledge_base_arn,
                "role_arn": role_arn,
            }

        @builtins.property
        def knowledge_base_arn(self) -> builtins.str:
            '''The knowledgeBaseArn details for the Kendra dataset source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-dataset-kendrasourcedetail.html#cfn-iotsitewise-dataset-kendrasourcedetail-knowledgebasearn
            '''
            result = self._values.get("knowledge_base_arn")
            assert result is not None, "Required property 'knowledge_base_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The roleARN details for the Kendra dataset source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-dataset-kendrasourcedetail.html#cfn-iotsitewise-dataset-kendrasourcedetail-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KendraSourceDetailProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnDataset.SourceDetailProperty",
        jsii_struct_bases=[],
        name_mapping={"kendra": "kendra"},
    )
    class SourceDetailProperty:
        def __init__(
            self,
            *,
            kendra: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.KendraSourceDetailProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param kendra: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-dataset-sourcedetail.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                source_detail_property = iotsitewise.CfnDataset.SourceDetailProperty(
                    kendra=iotsitewise.CfnDataset.KendraSourceDetailProperty(
                        knowledge_base_arn="knowledgeBaseArn",
                        role_arn="roleArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7a598d81c202f610ae61fa753a459c38aa834bd6a34e5b7a54eb9f63914b22c7)
                check_type(argname="argument kendra", value=kendra, expected_type=type_hints["kendra"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kendra is not None:
                self._values["kendra"] = kendra

        @builtins.property
        def kendra(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.KendraSourceDetailProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-dataset-sourcedetail.html#cfn-iotsitewise-dataset-sourcedetail-kendra
            '''
            result = self._values.get("kendra")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.KendraSourceDetailProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceDetailProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnDatasetProps",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_name": "datasetName",
        "dataset_source": "datasetSource",
        "dataset_description": "datasetDescription",
        "tags": "tags",
    },
)
class CfnDatasetProps:
    def __init__(
        self,
        *,
        dataset_name: builtins.str,
        dataset_source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.DatasetSourceProperty, typing.Dict[builtins.str, typing.Any]]],
        dataset_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataset``.

        :param dataset_name: The name of the dataset.
        :param dataset_source: 
        :param dataset_description: A description about the dataset, and its functionality.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dataset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotsitewise as iotsitewise
            
            cfn_dataset_props = iotsitewise.CfnDatasetProps(
                dataset_name="datasetName",
                dataset_source=iotsitewise.CfnDataset.DatasetSourceProperty(
                    source_format="sourceFormat",
                    source_type="sourceType",
            
                    # the properties below are optional
                    source_detail=iotsitewise.CfnDataset.SourceDetailProperty(
                        kendra=iotsitewise.CfnDataset.KendraSourceDetailProperty(
                            knowledge_base_arn="knowledgeBaseArn",
                            role_arn="roleArn"
                        )
                    )
                ),
            
                # the properties below are optional
                dataset_description="datasetDescription",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ecfd46cd288d1fcedea054d9db52e78eed5b596789d023c110fcfb9e1e41ff8)
            check_type(argname="argument dataset_name", value=dataset_name, expected_type=type_hints["dataset_name"])
            check_type(argname="argument dataset_source", value=dataset_source, expected_type=type_hints["dataset_source"])
            check_type(argname="argument dataset_description", value=dataset_description, expected_type=type_hints["dataset_description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_name": dataset_name,
            "dataset_source": dataset_source,
        }
        if dataset_description is not None:
            self._values["dataset_description"] = dataset_description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def dataset_name(self) -> builtins.str:
        '''The name of the dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dataset.html#cfn-iotsitewise-dataset-datasetname
        '''
        result = self._values.get("dataset_name")
        assert result is not None, "Required property 'dataset_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_source(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnDataset.DatasetSourceProperty]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dataset.html#cfn-iotsitewise-dataset-datasetsource
        '''
        result = self._values.get("dataset_source")
        assert result is not None, "Required property 'dataset_source' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnDataset.DatasetSourceProperty], result)

    @builtins.property
    def dataset_description(self) -> typing.Optional[builtins.str]:
        '''A description about the dataset, and its functionality.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dataset.html#cfn-iotsitewise-dataset-datasetdescription
        '''
        result = self._values.get("dataset_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-dataset.html#cfn-iotsitewise-dataset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatasetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnGateway(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnGateway",
):
    '''Creates a gateway, which is a virtual or edge device that delivers industrial data streams from local servers to AWS IoT SiteWise .

    For more information, see `Ingesting data using a gateway <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-connector.html>`_ in the *AWS IoT SiteWise User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html
    :cloudformationResource: AWS::IoTSiteWise::Gateway
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotsitewise as iotsitewise
        
        cfn_gateway = iotsitewise.CfnGateway(self, "MyCfnGateway",
            gateway_name="gatewayName",
            gateway_platform=iotsitewise.CfnGateway.GatewayPlatformProperty(
                greengrass=iotsitewise.CfnGateway.GreengrassProperty(
                    group_arn="groupArn"
                ),
                greengrass_v2=iotsitewise.CfnGateway.GreengrassV2Property(
                    core_device_thing_name="coreDeviceThingName",
        
                    # the properties below are optional
                    core_device_operating_system="coreDeviceOperatingSystem"
                ),
                siemens_ie=iotsitewise.CfnGateway.SiemensIEProperty(
                    iot_core_thing_name="iotCoreThingName"
                )
            ),
        
            # the properties below are optional
            gateway_capability_summaries=[iotsitewise.CfnGateway.GatewayCapabilitySummaryProperty(
                capability_namespace="capabilityNamespace",
        
                # the properties below are optional
                capability_configuration="capabilityConfiguration"
            )],
            gateway_version="gatewayVersion",
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
        gateway_name: builtins.str,
        gateway_platform: typing.Union[_IResolvable_da3f097b, typing.Union["CfnGateway.GatewayPlatformProperty", typing.Dict[builtins.str, typing.Any]]],
        gateway_capability_summaries: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGateway.GatewayCapabilitySummaryProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        gateway_version: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param gateway_name: A unique name for the gateway.
        :param gateway_platform: The gateway's platform. You can only specify one platform in a gateway.
        :param gateway_capability_summaries: A list of gateway capability summaries that each contain a namespace and status. Each gateway capability defines data sources for the gateway. To retrieve a capability configuration's definition, use `DescribeGatewayCapabilityConfiguration <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGatewayCapabilityConfiguration.html>`_ .
        :param gateway_version: The version of the gateway. A value of ``3`` indicates an MQTT-enabled, V3 gateway, while ``2`` indicates a Classic streams, V2 gateway.
        :param tags: A list of key-value pairs that contain metadata for the gateway. For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4e7aa58e6088e2cbee0005ea5a43b4c9db3b6647e2ff56a2b30310e7b1a75db)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGatewayProps(
            gateway_name=gateway_name,
            gateway_platform=gateway_platform,
            gateway_capability_summaries=gateway_capability_summaries,
            gateway_version=gateway_version,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32d18496c19dcd70d3e2bfdd8e37ae7c14e763732057eeb476d73309d3c982b7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e487f6fea4e7332025180df4bf127d8e2f634a79a13359046159c2b43bf6acd1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrGatewayId")
    def attr_gateway_id(self) -> builtins.str:
        '''The ID for the gateway.

        :cloudformationAttribute: GatewayId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayId"))

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
    @jsii.member(jsii_name="gatewayName")
    def gateway_name(self) -> builtins.str:
        '''A unique name for the gateway.'''
        return typing.cast(builtins.str, jsii.get(self, "gatewayName"))

    @gateway_name.setter
    def gateway_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b71cb9978b1b17c72ceab4f152568de72d45008677395cf39abe54f3af29d6d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gatewayPlatform")
    def gateway_platform(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnGateway.GatewayPlatformProperty"]:
        '''The gateway's platform.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnGateway.GatewayPlatformProperty"], jsii.get(self, "gatewayPlatform"))

    @gateway_platform.setter
    def gateway_platform(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnGateway.GatewayPlatformProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b804b846f70fe7670a1f8b651e7e17d1fb4055204c26a834d8529aa9d4f27ca9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayPlatform", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gatewayCapabilitySummaries")
    def gateway_capability_summaries(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGateway.GatewayCapabilitySummaryProperty"]]]]:
        '''A list of gateway capability summaries that each contain a namespace and status.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGateway.GatewayCapabilitySummaryProperty"]]]], jsii.get(self, "gatewayCapabilitySummaries"))

    @gateway_capability_summaries.setter
    def gateway_capability_summaries(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGateway.GatewayCapabilitySummaryProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0575717a55b787485944fbb94729c238b3cf9e112e2d0d439edfd4f8dd27b9b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayCapabilitySummaries", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gatewayVersion")
    def gateway_version(self) -> typing.Optional[builtins.str]:
        '''The version of the gateway.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayVersion"))

    @gateway_version.setter
    def gateway_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9914b4c24d20de7b662b3040cb09c4bae39421cef7517509a76b470a8687bc9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayVersion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the gateway.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26fcdcade7dc164a37aa04c5ee368b075236804669ba2be2553ac47ed59284da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnGateway.GatewayCapabilitySummaryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "capability_namespace": "capabilityNamespace",
            "capability_configuration": "capabilityConfiguration",
        },
    )
    class GatewayCapabilitySummaryProperty:
        def __init__(
            self,
            *,
            capability_namespace: builtins.str,
            capability_configuration: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains a summary of a gateway capability configuration.

            :param capability_namespace: The namespace of the capability configuration. For example, if you configure OPC UA sources for an MQTT-enabled gateway, your OPC-UA capability configuration has the namespace ``iotsitewise:opcuacollector:3`` .
            :param capability_configuration: The JSON document that defines the configuration for the gateway capability. For more information, see `Configuring data sources (CLI) <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-sources.html#configure-source-cli>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewaycapabilitysummary.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                gateway_capability_summary_property = iotsitewise.CfnGateway.GatewayCapabilitySummaryProperty(
                    capability_namespace="capabilityNamespace",
                
                    # the properties below are optional
                    capability_configuration="capabilityConfiguration"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ee1ae3477d1c1b70d9b9edb2163592393d56e767842107ae7939132c13ce358)
                check_type(argname="argument capability_namespace", value=capability_namespace, expected_type=type_hints["capability_namespace"])
                check_type(argname="argument capability_configuration", value=capability_configuration, expected_type=type_hints["capability_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "capability_namespace": capability_namespace,
            }
            if capability_configuration is not None:
                self._values["capability_configuration"] = capability_configuration

        @builtins.property
        def capability_namespace(self) -> builtins.str:
            '''The namespace of the capability configuration.

            For example, if you configure OPC UA sources for an MQTT-enabled gateway, your OPC-UA capability configuration has the namespace ``iotsitewise:opcuacollector:3`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewaycapabilitysummary.html#cfn-iotsitewise-gateway-gatewaycapabilitysummary-capabilitynamespace
            '''
            result = self._values.get("capability_namespace")
            assert result is not None, "Required property 'capability_namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def capability_configuration(self) -> typing.Optional[builtins.str]:
            '''The JSON document that defines the configuration for the gateway capability.

            For more information, see `Configuring data sources (CLI) <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-sources.html#configure-source-cli>`_ in the *AWS IoT SiteWise User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewaycapabilitysummary.html#cfn-iotsitewise-gateway-gatewaycapabilitysummary-capabilityconfiguration
            '''
            result = self._values.get("capability_configuration")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayCapabilitySummaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnGateway.GatewayPlatformProperty",
        jsii_struct_bases=[],
        name_mapping={
            "greengrass": "greengrass",
            "greengrass_v2": "greengrassV2",
            "siemens_ie": "siemensIe",
        },
    )
    class GatewayPlatformProperty:
        def __init__(
            self,
            *,
            greengrass: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGateway.GreengrassProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            greengrass_v2: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGateway.GreengrassV2Property", typing.Dict[builtins.str, typing.Any]]]] = None,
            siemens_ie: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGateway.SiemensIEProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The gateway's platform configuration. You can only specify one platform type in a gateway.

            (Legacy only) For Greengrass V1 gateways, specify the ``greengrass`` parameter with a valid Greengrass group ARN.

            For Greengrass V2 gateways, specify the ``greengrassV2`` parameter with a valid core device thing name. If creating a V3 gateway ( ``gatewayVersion=3`` ), you must also specify the ``coreDeviceOperatingSystem`` .

            For Siemens Industrial Edge gateways, specify the ``siemensIE`` parameter with a valid IoT Core thing name.

            :param greengrass: 
            :param greengrass_v2: A gateway that runs on AWS IoT Greengrass V2 .
            :param siemens_ie: An AWS IoT SiteWise Edge gateway that runs on a Siemens Industrial Edge Device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewayplatform.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                gateway_platform_property = iotsitewise.CfnGateway.GatewayPlatformProperty(
                    greengrass=iotsitewise.CfnGateway.GreengrassProperty(
                        group_arn="groupArn"
                    ),
                    greengrass_v2=iotsitewise.CfnGateway.GreengrassV2Property(
                        core_device_thing_name="coreDeviceThingName",
                
                        # the properties below are optional
                        core_device_operating_system="coreDeviceOperatingSystem"
                    ),
                    siemens_ie=iotsitewise.CfnGateway.SiemensIEProperty(
                        iot_core_thing_name="iotCoreThingName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d661bcb76cb5472e741e4e4c43ddf5d8a0dc76895775f2d9c80eb435edf5fc23)
                check_type(argname="argument greengrass", value=greengrass, expected_type=type_hints["greengrass"])
                check_type(argname="argument greengrass_v2", value=greengrass_v2, expected_type=type_hints["greengrass_v2"])
                check_type(argname="argument siemens_ie", value=siemens_ie, expected_type=type_hints["siemens_ie"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if greengrass is not None:
                self._values["greengrass"] = greengrass
            if greengrass_v2 is not None:
                self._values["greengrass_v2"] = greengrass_v2
            if siemens_ie is not None:
                self._values["siemens_ie"] = siemens_ie

        @builtins.property
        def greengrass(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.GreengrassProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewayplatform.html#cfn-iotsitewise-gateway-gatewayplatform-greengrass
            '''
            result = self._values.get("greengrass")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.GreengrassProperty"]], result)

        @builtins.property
        def greengrass_v2(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.GreengrassV2Property"]]:
            '''A gateway that runs on AWS IoT Greengrass V2 .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewayplatform.html#cfn-iotsitewise-gateway-gatewayplatform-greengrassv2
            '''
            result = self._values.get("greengrass_v2")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.GreengrassV2Property"]], result)

        @builtins.property
        def siemens_ie(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.SiemensIEProperty"]]:
            '''An AWS IoT SiteWise Edge gateway that runs on a Siemens Industrial Edge Device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-gatewayplatform.html#cfn-iotsitewise-gateway-gatewayplatform-siemensie
            '''
            result = self._values.get("siemens_ie")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGateway.SiemensIEProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayPlatformProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnGateway.GreengrassProperty",
        jsii_struct_bases=[],
        name_mapping={"group_arn": "groupArn"},
    )
    class GreengrassProperty:
        def __init__(self, *, group_arn: builtins.str) -> None:
            '''
            :param group_arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrass.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                greengrass_property = iotsitewise.CfnGateway.GreengrassProperty(
                    group_arn="groupArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__869d2e480b38a0e2376044c367d2367e64287fbb827bbca68d53b1515c75fbed)
                check_type(argname="argument group_arn", value=group_arn, expected_type=type_hints["group_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "group_arn": group_arn,
            }

        @builtins.property
        def group_arn(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrass.html#cfn-iotsitewise-gateway-greengrass-grouparn
            '''
            result = self._values.get("group_arn")
            assert result is not None, "Required property 'group_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GreengrassProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnGateway.GreengrassV2Property",
        jsii_struct_bases=[],
        name_mapping={
            "core_device_thing_name": "coreDeviceThingName",
            "core_device_operating_system": "coreDeviceOperatingSystem",
        },
    )
    class GreengrassV2Property:
        def __init__(
            self,
            *,
            core_device_thing_name: builtins.str,
            core_device_operating_system: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains details for a gateway that runs on AWS IoT Greengrass V2 .

            To create a gateway that runs on AWS IoT Greengrass V2 , you must deploy the IoT SiteWise Edge component to your gateway device. Your `Greengrass device role <https://docs.aws.amazon.com/greengrass/v2/developerguide/device-service-role.html>`_ must use the ``AWSIoTSiteWiseEdgeAccess`` policy. For more information, see `Using AWS IoT SiteWise at the edge <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sw-gateways.html>`_ in the *AWS IoT SiteWise User Guide* .

            :param core_device_thing_name: The name of the AWS IoT thing for your AWS IoT Greengrass V2 core device.
            :param core_device_operating_system: The operating system of the core device in AWS IoT Greengrass V2.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrassv2.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                greengrass_v2_property = iotsitewise.CfnGateway.GreengrassV2Property(
                    core_device_thing_name="coreDeviceThingName",
                
                    # the properties below are optional
                    core_device_operating_system="coreDeviceOperatingSystem"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aaa34ef3ffa417e0d8477bdf5fd83220079621fb80b75a881ad5c04a9c485841)
                check_type(argname="argument core_device_thing_name", value=core_device_thing_name, expected_type=type_hints["core_device_thing_name"])
                check_type(argname="argument core_device_operating_system", value=core_device_operating_system, expected_type=type_hints["core_device_operating_system"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "core_device_thing_name": core_device_thing_name,
            }
            if core_device_operating_system is not None:
                self._values["core_device_operating_system"] = core_device_operating_system

        @builtins.property
        def core_device_thing_name(self) -> builtins.str:
            '''The name of the AWS IoT thing for your AWS IoT Greengrass V2 core device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrassv2.html#cfn-iotsitewise-gateway-greengrassv2-coredevicethingname
            '''
            result = self._values.get("core_device_thing_name")
            assert result is not None, "Required property 'core_device_thing_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def core_device_operating_system(self) -> typing.Optional[builtins.str]:
            '''The operating system of the core device in AWS IoT Greengrass V2.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-greengrassv2.html#cfn-iotsitewise-gateway-greengrassv2-coredeviceoperatingsystem
            '''
            result = self._values.get("core_device_operating_system")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GreengrassV2Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnGateway.SiemensIEProperty",
        jsii_struct_bases=[],
        name_mapping={"iot_core_thing_name": "iotCoreThingName"},
    )
    class SiemensIEProperty:
        def __init__(self, *, iot_core_thing_name: builtins.str) -> None:
            '''Contains details for a AWS IoT SiteWise Edge gateway that runs on a Siemens Industrial Edge Device.

            :param iot_core_thing_name: The name of the AWS IoT Thing for your AWS IoT SiteWise Edge gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-siemensie.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                siemens_iEProperty = iotsitewise.CfnGateway.SiemensIEProperty(
                    iot_core_thing_name="iotCoreThingName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c5c36e991ce3543e0259817d60bf936941834dcd087997082364d6b61a83223f)
                check_type(argname="argument iot_core_thing_name", value=iot_core_thing_name, expected_type=type_hints["iot_core_thing_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "iot_core_thing_name": iot_core_thing_name,
            }

        @builtins.property
        def iot_core_thing_name(self) -> builtins.str:
            '''The name of the AWS IoT Thing for your AWS IoT SiteWise Edge gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-gateway-siemensie.html#cfn-iotsitewise-gateway-siemensie-iotcorethingname
            '''
            result = self._values.get("iot_core_thing_name")
            assert result is not None, "Required property 'iot_core_thing_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SiemensIEProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnGatewayProps",
    jsii_struct_bases=[],
    name_mapping={
        "gateway_name": "gatewayName",
        "gateway_platform": "gatewayPlatform",
        "gateway_capability_summaries": "gatewayCapabilitySummaries",
        "gateway_version": "gatewayVersion",
        "tags": "tags",
    },
)
class CfnGatewayProps:
    def __init__(
        self,
        *,
        gateway_name: builtins.str,
        gateway_platform: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayPlatformProperty, typing.Dict[builtins.str, typing.Any]]],
        gateway_capability_summaries: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayCapabilitySummaryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        gateway_version: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGateway``.

        :param gateway_name: A unique name for the gateway.
        :param gateway_platform: The gateway's platform. You can only specify one platform in a gateway.
        :param gateway_capability_summaries: A list of gateway capability summaries that each contain a namespace and status. Each gateway capability defines data sources for the gateway. To retrieve a capability configuration's definition, use `DescribeGatewayCapabilityConfiguration <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGatewayCapabilityConfiguration.html>`_ .
        :param gateway_version: The version of the gateway. A value of ``3`` indicates an MQTT-enabled, V3 gateway, while ``2`` indicates a Classic streams, V2 gateway.
        :param tags: A list of key-value pairs that contain metadata for the gateway. For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotsitewise as iotsitewise
            
            cfn_gateway_props = iotsitewise.CfnGatewayProps(
                gateway_name="gatewayName",
                gateway_platform=iotsitewise.CfnGateway.GatewayPlatformProperty(
                    greengrass=iotsitewise.CfnGateway.GreengrassProperty(
                        group_arn="groupArn"
                    ),
                    greengrass_v2=iotsitewise.CfnGateway.GreengrassV2Property(
                        core_device_thing_name="coreDeviceThingName",
            
                        # the properties below are optional
                        core_device_operating_system="coreDeviceOperatingSystem"
                    ),
                    siemens_ie=iotsitewise.CfnGateway.SiemensIEProperty(
                        iot_core_thing_name="iotCoreThingName"
                    )
                ),
            
                # the properties below are optional
                gateway_capability_summaries=[iotsitewise.CfnGateway.GatewayCapabilitySummaryProperty(
                    capability_namespace="capabilityNamespace",
            
                    # the properties below are optional
                    capability_configuration="capabilityConfiguration"
                )],
                gateway_version="gatewayVersion",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96b726a7f6953ced23491d12afc63dd3960b8d44e1734397f1db9d45a0cf6793)
            check_type(argname="argument gateway_name", value=gateway_name, expected_type=type_hints["gateway_name"])
            check_type(argname="argument gateway_platform", value=gateway_platform, expected_type=type_hints["gateway_platform"])
            check_type(argname="argument gateway_capability_summaries", value=gateway_capability_summaries, expected_type=type_hints["gateway_capability_summaries"])
            check_type(argname="argument gateway_version", value=gateway_version, expected_type=type_hints["gateway_version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_name": gateway_name,
            "gateway_platform": gateway_platform,
        }
        if gateway_capability_summaries is not None:
            self._values["gateway_capability_summaries"] = gateway_capability_summaries
        if gateway_version is not None:
            self._values["gateway_version"] = gateway_version
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def gateway_name(self) -> builtins.str:
        '''A unique name for the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayname
        '''
        result = self._values.get("gateway_name")
        assert result is not None, "Required property 'gateway_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def gateway_platform(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnGateway.GatewayPlatformProperty]:
        '''The gateway's platform.

        You can only specify one platform in a gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayplatform
        '''
        result = self._values.get("gateway_platform")
        assert result is not None, "Required property 'gateway_platform' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnGateway.GatewayPlatformProperty], result)

    @builtins.property
    def gateway_capability_summaries(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGateway.GatewayCapabilitySummaryProperty]]]]:
        '''A list of gateway capability summaries that each contain a namespace and status.

        Each gateway capability defines data sources for the gateway. To retrieve a capability configuration's definition, use `DescribeGatewayCapabilityConfiguration <https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGatewayCapabilityConfiguration.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewaycapabilitysummaries
        '''
        result = self._values.get("gateway_capability_summaries")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGateway.GatewayCapabilitySummaryProperty]]]], result)

    @builtins.property
    def gateway_version(self) -> typing.Optional[builtins.str]:
        '''The version of the gateway.

        A value of ``3`` indicates an MQTT-enabled, V3 gateway, while ``2`` indicates a Classic streams, V2 gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-gatewayversion
        '''
        result = self._values.get("gateway_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the gateway.

        For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-gateway.html#cfn-iotsitewise-gateway-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPortal(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnPortal",
):
    '''Creates a portal, which can contain projects and dashboards.

    AWS IoT SiteWise Monitor uses IAM Identity Center or IAM to authenticate portal users and manage user permissions.
    .. epigraph::

       Before you can sign in to a new portal, you must add at least one identity to that portal. For more information, see `Adding or removing portal administrators <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html#portal-change-admins>`_ in the *AWS IoT SiteWise User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html
    :cloudformationResource: AWS::IoTSiteWise::Portal
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotsitewise as iotsitewise
        
        # alarms: Any
        
        cfn_portal = iotsitewise.CfnPortal(self, "MyCfnPortal",
            portal_contact_email="portalContactEmail",
            portal_name="portalName",
            role_arn="roleArn",
        
            # the properties below are optional
            alarms=alarms,
            notification_sender_email="notificationSenderEmail",
            portal_auth_mode="portalAuthMode",
            portal_description="portalDescription",
            portal_type="portalType",
            portal_type_configuration={
                "portal_type_configuration_key": iotsitewise.CfnPortal.PortalTypeEntryProperty(
                    portal_tools=["portalTools"]
                )
            },
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
        portal_contact_email: builtins.str,
        portal_name: builtins.str,
        role_arn: builtins.str,
        alarms: typing.Any = None,
        notification_sender_email: typing.Optional[builtins.str] = None,
        portal_auth_mode: typing.Optional[builtins.str] = None,
        portal_description: typing.Optional[builtins.str] = None,
        portal_type: typing.Optional[builtins.str] = None,
        portal_type_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnPortal.PortalTypeEntryProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param portal_contact_email: The AWS administrator's contact email address.
        :param portal_name: A friendly name for the portal.
        :param role_arn: The `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ of a service role that allows the portal's users to access your AWS IoT SiteWise resources on your behalf. For more information, see `Using service roles for AWS IoT SiteWise Monitor <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html>`_ in the *AWS IoT SiteWise User Guide* .
        :param alarms: Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range. For more information, see `Monitoring with alarms <https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html>`_ in the *AWS IoT SiteWise Application Guide* .
        :param notification_sender_email: The email address that sends alarm notifications. .. epigraph:: If you use the `AWS IoT Events managed Lambda function <https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html>`_ to manage your emails, you must `verify the sender email address in Amazon SES <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html>`_ .
        :param portal_auth_mode: The service to use to authenticate users to the portal. Choose from the following options:. - ``SSO`` – The portal uses AWS IAM Identity Center to authenticate users and manage user permissions. Before you can create a portal that uses IAM Identity Center, you must enable IAM Identity Center. For more information, see `Enabling IAM Identity Center <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-get-started.html#mon-gs-sso>`_ in the *AWS IoT SiteWise User Guide* . This option is only available in AWS Regions other than the China Regions. - ``IAM`` – The portal uses AWS Identity and Access Management to authenticate users and manage user permissions. You can't change this value after you create a portal. Default: ``SSO``
        :param portal_description: A description for the portal.
        :param portal_type: Define the type of portal. The value for AWS IoT SiteWise Monitor (Classic) is ``SITEWISE_PORTAL_V1`` . The value for AWS IoT SiteWise Monitor (AI-aware) is ``SITEWISE_PORTAL_V2`` .
        :param portal_type_configuration: Map to associate detail of configuration related with a PortalType.
        :param tags: A list of key-value pairs that contain metadata for the portal. For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbc23e7f8ea9f23ecedfbb8e22cd39fad67b5932c9e8eb1d5d50975c13a3c5e8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPortalProps(
            portal_contact_email=portal_contact_email,
            portal_name=portal_name,
            role_arn=role_arn,
            alarms=alarms,
            notification_sender_email=notification_sender_email,
            portal_auth_mode=portal_auth_mode,
            portal_description=portal_description,
            portal_type=portal_type,
            portal_type_configuration=portal_type_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e35d29c0f35bd7b72ba87b37ebcc981c82f95575036b8a5527137363bcb6ec6d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c7d41561b5ff568159d53d88d8901853afd0b84ccc6b789aee97627ac22af3b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPortalArn")
    def attr_portal_arn(self) -> builtins.str:
        '''The `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ of the portal, which has the following format.

        ``arn:${Partition}:iotsitewise:${Region}:${Account}:portal/${PortalId}``

        :cloudformationAttribute: PortalArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPortalArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPortalClientId")
    def attr_portal_client_id(self) -> builtins.str:
        '''The IAM Identity Center application generated client ID (used with IAM Identity Center APIs).

        :cloudformationAttribute: PortalClientId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPortalClientId"))

    @builtins.property
    @jsii.member(jsii_name="attrPortalId")
    def attr_portal_id(self) -> builtins.str:
        '''The ID of the created portal.

        :cloudformationAttribute: PortalId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPortalId"))

    @builtins.property
    @jsii.member(jsii_name="attrPortalStartUrl")
    def attr_portal_start_url(self) -> builtins.str:
        '''The public URL for the AWS IoT SiteWise Monitor portal.

        :cloudformationAttribute: PortalStartUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPortalStartUrl"))

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
    @jsii.member(jsii_name="portalContactEmail")
    def portal_contact_email(self) -> builtins.str:
        '''The AWS administrator's contact email address.'''
        return typing.cast(builtins.str, jsii.get(self, "portalContactEmail"))

    @portal_contact_email.setter
    def portal_contact_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76cc7d18d9cdc2c0262648281c53cc8a8880f76962fd416b38bc00d5e2e4d807)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portalContactEmail", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="portalName")
    def portal_name(self) -> builtins.str:
        '''A friendly name for the portal.'''
        return typing.cast(builtins.str, jsii.get(self, "portalName"))

    @portal_name.setter
    def portal_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e09665f12ada311bc3e92f26c950c3b352054729e545455c7ab822ebd2ba0d74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portalName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ of a service role that allows the portal's users to access your AWS IoT SiteWise resources on your behalf. For more information, see `Using service roles for AWS IoT SiteWise Monitor <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html>`_ in the *AWS IoT SiteWise User Guide* .'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__801da38b8b0799f806382f6db4934f5cde8b7b5856a63457bf47a3c3d721e0ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="alarms")
    def alarms(self) -> typing.Any:
        '''Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal.'''
        return typing.cast(typing.Any, jsii.get(self, "alarms"))

    @alarms.setter
    def alarms(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a07bf890e264d76055c18252e2d1882abb53a19982220ec6c89215096dedb5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarms", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="notificationSenderEmail")
    def notification_sender_email(self) -> typing.Optional[builtins.str]:
        '''The email address that sends alarm notifications.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationSenderEmail"))

    @notification_sender_email.setter
    def notification_sender_email(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__450baca4a5d4d44597d00571c99f952263e5c4dcc79c06e175ed7758a5e5dc07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationSenderEmail", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="portalAuthMode")
    def portal_auth_mode(self) -> typing.Optional[builtins.str]:
        '''The service to use to authenticate users to the portal.

        Choose from the following options:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portalAuthMode"))

    @portal_auth_mode.setter
    def portal_auth_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41cc3527d6f0a3c056b662b09636e8487fe6b2cd4d2a86f883aad8fa1e852b4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portalAuthMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="portalDescription")
    def portal_description(self) -> typing.Optional[builtins.str]:
        '''A description for the portal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portalDescription"))

    @portal_description.setter
    def portal_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aef69531546e69c52fb621d608894b8a13ea5ce64a0e713b24aacd2b912457dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portalDescription", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="portalType")
    def portal_type(self) -> typing.Optional[builtins.str]:
        '''Define the type of portal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portalType"))

    @portal_type.setter
    def portal_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e30e6480af8bf6c9156f76afcfbc51187c15ffe199e8b2a284dae86baaccb878)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portalType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="portalTypeConfiguration")
    def portal_type_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnPortal.PortalTypeEntryProperty"]]]]:
        '''Map to associate detail of configuration related with a PortalType.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnPortal.PortalTypeEntryProperty"]]]], jsii.get(self, "portalTypeConfiguration"))

    @portal_type_configuration.setter
    def portal_type_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnPortal.PortalTypeEntryProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d9d6a7fc128e24a5796b5247e692bea000e44c1afd3fed96b4e4cb15f279f74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portalTypeConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the portal.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__094008154aa9c2ed7f23db7b3bd3bbad9f03aa4bbdaba95af7958b252ddd4bc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnPortal.AlarmsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alarm_role_arn": "alarmRoleArn",
            "notification_lambda_arn": "notificationLambdaArn",
        },
    )
    class AlarmsProperty:
        def __init__(
            self,
            *,
            alarm_role_arn: typing.Optional[builtins.str] = None,
            notification_lambda_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal.

            You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range. For more information, see `Monitoring with alarms <https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html>`_ in the *AWS IoT SiteWise Application Guide* .

            :param alarm_role_arn: The `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ of the IAM role that allows the alarm to perform actions and access AWS resources and services, such as AWS IoT Events .
            :param notification_lambda_arn: The `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ of the Lambda function that manages alarm notifications. For more information, see `Managing alarm notifications <https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html>`_ in the *AWS IoT Events Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-portal-alarms.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                alarms_property = iotsitewise.CfnPortal.AlarmsProperty(
                    alarm_role_arn="alarmRoleArn",
                    notification_lambda_arn="notificationLambdaArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3a766409f9773f0cd5cb3dd5c49ce92586c7cc4f8233f8f908d042bfd8359991)
                check_type(argname="argument alarm_role_arn", value=alarm_role_arn, expected_type=type_hints["alarm_role_arn"])
                check_type(argname="argument notification_lambda_arn", value=notification_lambda_arn, expected_type=type_hints["notification_lambda_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if alarm_role_arn is not None:
                self._values["alarm_role_arn"] = alarm_role_arn
            if notification_lambda_arn is not None:
                self._values["notification_lambda_arn"] = notification_lambda_arn

        @builtins.property
        def alarm_role_arn(self) -> typing.Optional[builtins.str]:
            '''The `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ of the IAM role that allows the alarm to perform actions and access AWS resources and services, such as AWS IoT Events .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-portal-alarms.html#cfn-iotsitewise-portal-alarms-alarmrolearn
            '''
            result = self._values.get("alarm_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def notification_lambda_arn(self) -> typing.Optional[builtins.str]:
            '''The `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ of the Lambda function that manages alarm notifications. For more information, see `Managing alarm notifications <https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html>`_ in the *AWS IoT Events Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-portal-alarms.html#cfn-iotsitewise-portal-alarms-notificationlambdaarn
            '''
            result = self._values.get("notification_lambda_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotsitewise.CfnPortal.PortalTypeEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"portal_tools": "portalTools"},
    )
    class PortalTypeEntryProperty:
        def __init__(self, *, portal_tools: typing.Sequence[builtins.str]) -> None:
            '''Container associated a certain PortalType.

            :param portal_tools: The array of tools associated with the specified portal type. The possible values are ``ASSISTANT`` and ``DASHBOARD`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-portal-portaltypeentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotsitewise as iotsitewise
                
                portal_type_entry_property = iotsitewise.CfnPortal.PortalTypeEntryProperty(
                    portal_tools=["portalTools"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__159de1986a281fe75049e969ee02d9509ce935b8bef35eb415647d6e66e0feab)
                check_type(argname="argument portal_tools", value=portal_tools, expected_type=type_hints["portal_tools"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "portal_tools": portal_tools,
            }

        @builtins.property
        def portal_tools(self) -> typing.List[builtins.str]:
            '''The array of tools associated with the specified portal type.

            The possible values are ``ASSISTANT`` and ``DASHBOARD`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotsitewise-portal-portaltypeentry.html#cfn-iotsitewise-portal-portaltypeentry-portaltools
            '''
            result = self._values.get("portal_tools")
            assert result is not None, "Required property 'portal_tools' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortalTypeEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnPortalProps",
    jsii_struct_bases=[],
    name_mapping={
        "portal_contact_email": "portalContactEmail",
        "portal_name": "portalName",
        "role_arn": "roleArn",
        "alarms": "alarms",
        "notification_sender_email": "notificationSenderEmail",
        "portal_auth_mode": "portalAuthMode",
        "portal_description": "portalDescription",
        "portal_type": "portalType",
        "portal_type_configuration": "portalTypeConfiguration",
        "tags": "tags",
    },
)
class CfnPortalProps:
    def __init__(
        self,
        *,
        portal_contact_email: builtins.str,
        portal_name: builtins.str,
        role_arn: builtins.str,
        alarms: typing.Any = None,
        notification_sender_email: typing.Optional[builtins.str] = None,
        portal_auth_mode: typing.Optional[builtins.str] = None,
        portal_description: typing.Optional[builtins.str] = None,
        portal_type: typing.Optional[builtins.str] = None,
        portal_type_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnPortal.PortalTypeEntryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPortal``.

        :param portal_contact_email: The AWS administrator's contact email address.
        :param portal_name: A friendly name for the portal.
        :param role_arn: The `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ of a service role that allows the portal's users to access your AWS IoT SiteWise resources on your behalf. For more information, see `Using service roles for AWS IoT SiteWise Monitor <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html>`_ in the *AWS IoT SiteWise User Guide* .
        :param alarms: Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range. For more information, see `Monitoring with alarms <https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html>`_ in the *AWS IoT SiteWise Application Guide* .
        :param notification_sender_email: The email address that sends alarm notifications. .. epigraph:: If you use the `AWS IoT Events managed Lambda function <https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html>`_ to manage your emails, you must `verify the sender email address in Amazon SES <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html>`_ .
        :param portal_auth_mode: The service to use to authenticate users to the portal. Choose from the following options:. - ``SSO`` – The portal uses AWS IAM Identity Center to authenticate users and manage user permissions. Before you can create a portal that uses IAM Identity Center, you must enable IAM Identity Center. For more information, see `Enabling IAM Identity Center <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-get-started.html#mon-gs-sso>`_ in the *AWS IoT SiteWise User Guide* . This option is only available in AWS Regions other than the China Regions. - ``IAM`` – The portal uses AWS Identity and Access Management to authenticate users and manage user permissions. You can't change this value after you create a portal. Default: ``SSO``
        :param portal_description: A description for the portal.
        :param portal_type: Define the type of portal. The value for AWS IoT SiteWise Monitor (Classic) is ``SITEWISE_PORTAL_V1`` . The value for AWS IoT SiteWise Monitor (AI-aware) is ``SITEWISE_PORTAL_V2`` .
        :param portal_type_configuration: Map to associate detail of configuration related with a PortalType.
        :param tags: A list of key-value pairs that contain metadata for the portal. For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotsitewise as iotsitewise
            
            # alarms: Any
            
            cfn_portal_props = iotsitewise.CfnPortalProps(
                portal_contact_email="portalContactEmail",
                portal_name="portalName",
                role_arn="roleArn",
            
                # the properties below are optional
                alarms=alarms,
                notification_sender_email="notificationSenderEmail",
                portal_auth_mode="portalAuthMode",
                portal_description="portalDescription",
                portal_type="portalType",
                portal_type_configuration={
                    "portal_type_configuration_key": iotsitewise.CfnPortal.PortalTypeEntryProperty(
                        portal_tools=["portalTools"]
                    )
                },
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db927eff8866e7afa967752c7f48d5d8ab1bd58489a78569b13cac34c81ba650)
            check_type(argname="argument portal_contact_email", value=portal_contact_email, expected_type=type_hints["portal_contact_email"])
            check_type(argname="argument portal_name", value=portal_name, expected_type=type_hints["portal_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument alarms", value=alarms, expected_type=type_hints["alarms"])
            check_type(argname="argument notification_sender_email", value=notification_sender_email, expected_type=type_hints["notification_sender_email"])
            check_type(argname="argument portal_auth_mode", value=portal_auth_mode, expected_type=type_hints["portal_auth_mode"])
            check_type(argname="argument portal_description", value=portal_description, expected_type=type_hints["portal_description"])
            check_type(argname="argument portal_type", value=portal_type, expected_type=type_hints["portal_type"])
            check_type(argname="argument portal_type_configuration", value=portal_type_configuration, expected_type=type_hints["portal_type_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "portal_contact_email": portal_contact_email,
            "portal_name": portal_name,
            "role_arn": role_arn,
        }
        if alarms is not None:
            self._values["alarms"] = alarms
        if notification_sender_email is not None:
            self._values["notification_sender_email"] = notification_sender_email
        if portal_auth_mode is not None:
            self._values["portal_auth_mode"] = portal_auth_mode
        if portal_description is not None:
            self._values["portal_description"] = portal_description
        if portal_type is not None:
            self._values["portal_type"] = portal_type
        if portal_type_configuration is not None:
            self._values["portal_type_configuration"] = portal_type_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def portal_contact_email(self) -> builtins.str:
        '''The AWS administrator's contact email address.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portalcontactemail
        '''
        result = self._values.get("portal_contact_email")
        assert result is not None, "Required property 'portal_contact_email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def portal_name(self) -> builtins.str:
        '''A friendly name for the portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portalname
        '''
        result = self._values.get("portal_name")
        assert result is not None, "Required property 'portal_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ of a service role that allows the portal's users to access your AWS IoT SiteWise resources on your behalf. For more information, see `Using service roles for AWS IoT SiteWise Monitor <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alarms(self) -> typing.Any:
        '''Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal.

        You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range. For more information, see `Monitoring with alarms <https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html>`_ in the *AWS IoT SiteWise Application Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-alarms
        '''
        result = self._values.get("alarms")
        return typing.cast(typing.Any, result)

    @builtins.property
    def notification_sender_email(self) -> typing.Optional[builtins.str]:
        '''The email address that sends alarm notifications.

        .. epigraph::

           If you use the `AWS IoT Events managed Lambda function <https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html>`_ to manage your emails, you must `verify the sender email address in Amazon SES <https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-notificationsenderemail
        '''
        result = self._values.get("notification_sender_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def portal_auth_mode(self) -> typing.Optional[builtins.str]:
        '''The service to use to authenticate users to the portal. Choose from the following options:.

        - ``SSO`` – The portal uses AWS IAM Identity Center to authenticate users and manage user permissions. Before you can create a portal that uses IAM Identity Center, you must enable IAM Identity Center. For more information, see `Enabling IAM Identity Center <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-get-started.html#mon-gs-sso>`_ in the *AWS IoT SiteWise User Guide* . This option is only available in AWS Regions other than the China Regions.
        - ``IAM`` – The portal uses AWS Identity and Access Management to authenticate users and manage user permissions.

        You can't change this value after you create a portal.

        Default: ``SSO``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portalauthmode
        '''
        result = self._values.get("portal_auth_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def portal_description(self) -> typing.Optional[builtins.str]:
        '''A description for the portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portaldescription
        '''
        result = self._values.get("portal_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def portal_type(self) -> typing.Optional[builtins.str]:
        '''Define the type of portal.

        The value for AWS IoT SiteWise Monitor (Classic) is ``SITEWISE_PORTAL_V1`` . The value for AWS IoT SiteWise Monitor (AI-aware) is ``SITEWISE_PORTAL_V2`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portaltype
        '''
        result = self._values.get("portal_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def portal_type_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnPortal.PortalTypeEntryProperty]]]]:
        '''Map to associate detail of configuration related with a PortalType.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-portaltypeconfiguration
        '''
        result = self._values.get("portal_type_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnPortal.PortalTypeEntryProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the portal.

        For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-portal.html#cfn-iotsitewise-portal-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPortalProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnProject(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnProject",
):
    '''Creates a project in the specified portal.

    .. epigraph::

       Make sure that the project name and description don't contain confidential information.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html
    :cloudformationResource: AWS::IoTSiteWise::Project
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotsitewise as iotsitewise
        
        cfn_project = iotsitewise.CfnProject(self, "MyCfnProject",
            portal_id="portalId",
            project_name="projectName",
        
            # the properties below are optional
            asset_ids=["assetIds"],
            project_description="projectDescription",
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
        portal_id: builtins.str,
        project_name: builtins.str,
        asset_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        project_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param portal_id: The ID of the portal in which to create the project.
        :param project_name: A friendly name for the project.
        :param asset_ids: A list that contains the IDs of each asset associated with the project.
        :param project_description: A description for the project.
        :param tags: A list of key-value pairs that contain metadata for the project. For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ca003aa6daa3e15044d74469428b378e883b1a517620f59fc80331c1a383f15)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectProps(
            portal_id=portal_id,
            project_name=project_name,
            asset_ids=asset_ids,
            project_description=project_description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a16b8d5ebb2cc95753d1c1a1a523d80ae58e829ae8ce8450719faca461b1b1c8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__453b9d09035594771c3821a921bed5d09e9b261f5293c2fdd845898471727f84)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrProjectArn")
    def attr_project_arn(self) -> builtins.str:
        '''The `ARN <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ of the project, which has the following format.

        ``arn:${Partition}:iotsitewise:${Region}:${Account}:project/${ProjectId}``

        :cloudformationAttribute: ProjectArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectArn"))

    @builtins.property
    @jsii.member(jsii_name="attrProjectId")
    def attr_project_id(self) -> builtins.str:
        '''The ID of the project.

        :cloudformationAttribute: ProjectId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectId"))

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
    @jsii.member(jsii_name="portalId")
    def portal_id(self) -> builtins.str:
        '''The ID of the portal in which to create the project.'''
        return typing.cast(builtins.str, jsii.get(self, "portalId"))

    @portal_id.setter
    def portal_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f26f3f5573e85a97b08157df77b5856c58817b81405637e615727b3cb10e7e0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portalId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="projectName")
    def project_name(self) -> builtins.str:
        '''A friendly name for the project.'''
        return typing.cast(builtins.str, jsii.get(self, "projectName"))

    @project_name.setter
    def project_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d035e8224bbba25abe29c7e7ff3e91e74da8b89504dfa0422128a6b9dd419fce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assetIds")
    def asset_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list that contains the IDs of each asset associated with the project.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "assetIds"))

    @asset_ids.setter
    def asset_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2efb7789fd61ffe146d6ef68fdc319d09b3f1b9c49d567dd16971f31010169b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assetIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="projectDescription")
    def project_description(self) -> typing.Optional[builtins.str]:
        '''A description for the project.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectDescription"))

    @project_description.setter
    def project_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80b733624c751f502aeb54f4ab221ff7e5ae55f6bd1e87090cac18105f6c4a70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectDescription", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the project.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcb700fa41df1dfaa6c4cfad19b3a4f56b9aa96ef4b6e315d990eb0a286b2cdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotsitewise.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "portal_id": "portalId",
        "project_name": "projectName",
        "asset_ids": "assetIds",
        "project_description": "projectDescription",
        "tags": "tags",
    },
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        portal_id: builtins.str,
        project_name: builtins.str,
        asset_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        project_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProject``.

        :param portal_id: The ID of the portal in which to create the project.
        :param project_name: A friendly name for the project.
        :param asset_ids: A list that contains the IDs of each asset associated with the project.
        :param project_description: A description for the project.
        :param tags: A list of key-value pairs that contain metadata for the project. For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotsitewise as iotsitewise
            
            cfn_project_props = iotsitewise.CfnProjectProps(
                portal_id="portalId",
                project_name="projectName",
            
                # the properties below are optional
                asset_ids=["assetIds"],
                project_description="projectDescription",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7af827083026086703d7567e7e4a27cf6d5bb590317461231a2e997d42b85e1b)
            check_type(argname="argument portal_id", value=portal_id, expected_type=type_hints["portal_id"])
            check_type(argname="argument project_name", value=project_name, expected_type=type_hints["project_name"])
            check_type(argname="argument asset_ids", value=asset_ids, expected_type=type_hints["asset_ids"])
            check_type(argname="argument project_description", value=project_description, expected_type=type_hints["project_description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "portal_id": portal_id,
            "project_name": project_name,
        }
        if asset_ids is not None:
            self._values["asset_ids"] = asset_ids
        if project_description is not None:
            self._values["project_description"] = project_description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def portal_id(self) -> builtins.str:
        '''The ID of the portal in which to create the project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-portalid
        '''
        result = self._values.get("portal_id")
        assert result is not None, "Required property 'portal_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_name(self) -> builtins.str:
        '''A friendly name for the project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-projectname
        '''
        result = self._values.get("project_name")
        assert result is not None, "Required property 'project_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list that contains the IDs of each asset associated with the project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-assetids
        '''
        result = self._values.get("asset_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def project_description(self) -> typing.Optional[builtins.str]:
        '''A description for the project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-projectdescription
        '''
        result = self._values.get("project_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of key-value pairs that contain metadata for the project.

        For more information, see `Tagging your AWS IoT SiteWise resources <https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html>`_ in the *AWS IoT SiteWise User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotsitewise-project.html#cfn-iotsitewise-project-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAccessPolicy",
    "CfnAccessPolicyProps",
    "CfnAsset",
    "CfnAssetModel",
    "CfnAssetModelProps",
    "CfnAssetProps",
    "CfnComputationModel",
    "CfnComputationModelProps",
    "CfnDashboard",
    "CfnDashboardProps",
    "CfnDataset",
    "CfnDatasetProps",
    "CfnGateway",
    "CfnGatewayProps",
    "CfnPortal",
    "CfnPortalProps",
    "CfnProject",
    "CfnProjectProps",
]

publication.publish()

def _typecheckingstub__531aa21f3bed6dedfd9fce9d7bb67acf86efe74ca96cafedea1800e8112b281b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_policy_identity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPolicy.AccessPolicyIdentityProperty, typing.Dict[builtins.str, typing.Any]]],
    access_policy_permission: builtins.str,
    access_policy_resource: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPolicy.AccessPolicyResourceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7c314721c2fd001464c0deebc3b8d42528f0226fb07963546a560eee048707a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d01f88f7fe294002e36ddfd24dba681b851b96f9e5b026a4da2d13fe47035504(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2415091a9e2f73b7c84f270a46cb74a20cbda551668c1888f3deca22ef17375a(
    value: typing.Union[_IResolvable_da3f097b, CfnAccessPolicy.AccessPolicyIdentityProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__818cb88e831e00c87bc949084acafc61e7b103360b6efa353d0949058b3af434(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__411d422b3be028b917aa7b3dbac61d64724f4eade2fcacd4bcf9431699d87cda(
    value: typing.Union[_IResolvable_da3f097b, CfnAccessPolicy.AccessPolicyResourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2d486ca8cf2592ca8b37c9d0e3cb26ad139033da3d5cef4d0958898a1f3e228(
    *,
    iam_role: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPolicy.IamRoleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iam_user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPolicy.IamUserProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    user: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPolicy.UserProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__765b4d883deb51ec44680a76cffbd0a2ab68fee759c8b28c86b9f59498c31af2(
    *,
    portal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPolicy.PortalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    project: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPolicy.ProjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f5cf7bcba5c6d5ceddf0ec6c4ef4ac1e8f801d29e104b8acac16b1b29340586(
    *,
    arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__432609e44b579a8a90c10739f068d0000939943a6fe45469f4f1ae467aa2f163(
    *,
    arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__143d119625b35bf1029bcedc015ee7c97453389b6fd03e0a75c41d6e12e704b9(
    *,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13bff317a735a1083b2976369b994f0f31c739c79d78584197a9a73729daef99(
    *,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f363729f07f015fc23f72b53be5071c8dc7624eb969069e23f064b035b2c023c(
    *,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__395192fc212cfba19ac0d48ac6224771ee93f01bee507a5e9571a735a417decd(
    *,
    access_policy_identity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPolicy.AccessPolicyIdentityProperty, typing.Dict[builtins.str, typing.Any]]],
    access_policy_permission: builtins.str,
    access_policy_resource: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccessPolicy.AccessPolicyResourceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23b484c08f8b327d7857c955867af231fc3193cc5df788160c4e1c6e326075b1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    asset_model_id: builtins.str,
    asset_name: builtins.str,
    asset_description: typing.Optional[builtins.str] = None,
    asset_external_id: typing.Optional[builtins.str] = None,
    asset_hierarchies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAsset.AssetHierarchyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    asset_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAsset.AssetPropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__102e5bd91193367af65b5d5491e5dd31e20ce7e2d4a10294b8a904b2294f035c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8036de54cbe0f29f20898cb6faa8d078fdb3b445a95f607b80032b1561c7fef2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e944261c39c832f5a26bb7510ff2565f5b578ad73aa1c03c10b468a125df4e0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2dc507f393cf1c06a074a018c9e9db507f543807826f4e8fa45ee4df4d527e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__846aec2a49e7d9368d2d62f013b975b4b8e383e34d606cf26025fa1e9c1f080e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__774f36beafbc5ecee60ee64670d06a55e1d63cae97a7bf37614ae9a5662e5bb5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54fdb5abb9d6b9f05e9d300d7d933adae0aed3f34ae2309c30c6ed3f6d1d6517(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAsset.AssetHierarchyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba341fa6fbf95a16923570d24a7123b2633590b82a24b510405c0e43e73829bb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAsset.AssetPropertyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95733b024c1a6ce8bc474f669fc60c5ec6406e7dd1eb8029bb8e07049a3ce2a4(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6404a33020d845fe84e2cc02f1ce61855b1caee959bf2437d88b3669ceecf46(
    *,
    child_asset_id: builtins.str,
    external_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    logical_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0a542963124a747730cbbfebfb49e3e50b517a00196aa1b2e31a5db31322e3e(
    *,
    alias: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    logical_id: typing.Optional[builtins.str] = None,
    notification_state: typing.Optional[builtins.str] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64edf231bb465b8f44da5cbed11fe0e7614208f47a50131d6c645ff0d3644608(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    asset_model_name: builtins.str,
    asset_model_composite_models: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.AssetModelCompositeModelProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    asset_model_description: typing.Optional[builtins.str] = None,
    asset_model_external_id: typing.Optional[builtins.str] = None,
    asset_model_hierarchies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.AssetModelHierarchyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    asset_model_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.AssetModelPropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    asset_model_type: typing.Optional[builtins.str] = None,
    enforced_asset_model_interface_relationships: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.EnforcedAssetModelInterfaceRelationshipProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbed60408dd1c2873bc70f9dc7fe48d0d621e09df06498a80d6afdcb1504aadc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57999804e9c09aa4d1dbca31b8d2a972cc93fa6fe7fe6e2b6a7b43ea236693de(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4071e2eabdee1916b99a1a251c710b2b59e2c130de77e066817d7a99c8cbc84e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75654fb8879a906466b416abbe028fcaa8a196e113d1b36c2586e69cf2304cf4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAssetModel.AssetModelCompositeModelProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d490d061673fe6f1c9ad9df9a8647b42dd857e63b1146d02ad13d08528d7ec58(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b11e9b7de389bdacb96aca69368f81f0023b01a9984dd10d8410bc081120813a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfff308bea7d00a1626ce55b090f5843c55f7c818902bb4d4533293210c8b379(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAssetModel.AssetModelHierarchyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62970d87191bab84b19cdf16fe635ae56be3bca14dce3de8ddbcb4ebe56e2e34(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAssetModel.AssetModelPropertyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33747ea8b68fd7ca1298da79a238d24533fca030571c5c5f494b793812c77e2a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8585343b0b44aebb25048a1408ef7b098cbb2e611b50c8ec2cbecceb8582d081(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAssetModel.EnforcedAssetModelInterfaceRelationshipProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__087e71db10fe7e46cfbe736951d8b93342a08c50afea582cbddc2eaa71151a64(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9032bb49134101399c5b628c8911fa6a32ba8f4082d1d7ce6034344be92c8edb(
    *,
    name: builtins.str,
    type: builtins.str,
    composed_asset_model_id: typing.Optional[builtins.str] = None,
    composite_model_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.AssetModelPropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    parent_asset_model_composite_model_external_id: typing.Optional[builtins.str] = None,
    path: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8bdd9b09999ded14aeb0bb460a6a5e4983c049cd1fedb5aaca40a2cd4b07f26(
    *,
    child_asset_model_id: builtins.str,
    name: builtins.str,
    external_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    logical_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df059a45516e286dd4ae84860f6454c3be02b47df42355ea284b5bd8c3c97590(
    *,
    data_type: builtins.str,
    name: builtins.str,
    type: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.PropertyTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    data_type_spec: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    logical_id: typing.Optional[builtins.str] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3172068ecee12a11a997c0f7922e1b5c5f5b9e44979e3f39af0c9f9974d4cbc0(
    *,
    default_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__602edbd4a6db7058c0a2d97bafdee4ac831e8e9cefa95964c590f9009304858f(
    *,
    interface_asset_model_property_external_id: builtins.str,
    asset_model_property_external_id: typing.Optional[builtins.str] = None,
    asset_model_property_logical_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fe8dfe5b5064a1ee03d773eb65966bf8eb13cf514900f6647f677f88f271459(
    *,
    interface_asset_model_id: typing.Optional[builtins.str] = None,
    property_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.EnforcedAssetModelInterfacePropertyMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47d40674b47217f8eb75acf1060336f44b9e0583e395a98550f44b5a4681f3db(
    *,
    name: builtins.str,
    value: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.VariableValueProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__018f0992b00dd2aa0891d7049deb5b9e6a376d61ee7e9524a2dc1a04b2d1de89(
    *,
    expression: builtins.str,
    variables: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.ExpressionVariableProperty, typing.Dict[builtins.str, typing.Any]]]]],
    window: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.MetricWindowProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36161b8e17b90887f361ce990f098e579673e8c26bf5974d4d53d888312a8a4b(
    *,
    tumbling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.TumblingWindowProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1359481022b13ca49cc9baa669a2ecc9adec5ca26699f485a60965403d6b134e(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88ab1ab9be5266b8374e7737561a2ceef629d83bcca6a5f65325e207910a86e3(
    *,
    type_name: builtins.str,
    attribute: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.AttributeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    metric: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.MetricProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    transform: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.TransformProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b165b40ea43e6f49e8b83fad3f0774b1c777b4df0881816c6666f80def04b51(
    *,
    expression: builtins.str,
    variables: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.ExpressionVariableProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__167b1f3f100fbd3792343a3af0f3185dfbaf01430ea8af4870144df021de021f(
    *,
    interval: builtins.str,
    offset: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfc8a5f6be8f2396701edaddb5e852d356262a49103549dbc6de3a39b491f9b4(
    *,
    hierarchy_external_id: typing.Optional[builtins.str] = None,
    hierarchy_id: typing.Optional[builtins.str] = None,
    hierarchy_logical_id: typing.Optional[builtins.str] = None,
    property_external_id: typing.Optional[builtins.str] = None,
    property_id: typing.Optional[builtins.str] = None,
    property_logical_id: typing.Optional[builtins.str] = None,
    property_path: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.PropertyPathDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4c397ea0e26142735f716b5c92fe1c51048d94b5142d035ce8dc4cb1df79380(
    *,
    asset_model_name: builtins.str,
    asset_model_composite_models: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.AssetModelCompositeModelProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    asset_model_description: typing.Optional[builtins.str] = None,
    asset_model_external_id: typing.Optional[builtins.str] = None,
    asset_model_hierarchies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.AssetModelHierarchyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    asset_model_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.AssetModelPropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    asset_model_type: typing.Optional[builtins.str] = None,
    enforced_asset_model_interface_relationships: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssetModel.EnforcedAssetModelInterfaceRelationshipProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__306f4833ce13fd25ec4269f2a96d0ee80f11a34f43885f5b4b372569dc9f7931(
    *,
    asset_model_id: builtins.str,
    asset_name: builtins.str,
    asset_description: typing.Optional[builtins.str] = None,
    asset_external_id: typing.Optional[builtins.str] = None,
    asset_hierarchies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAsset.AssetHierarchyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    asset_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAsset.AssetPropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__566bf1711c9dcacb9cb88add46c2c4e157208bdce4a774ccb256a7d21c68de89(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    computation_model_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputationModel.ComputationModelConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    computation_model_data_binding: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputationModel.ComputationModelDataBindingValueProperty, typing.Dict[builtins.str, typing.Any]]]]],
    computation_model_name: builtins.str,
    computation_model_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__137e70d4839513d333c73d5f02909172ab78f14b28c52c7f13f6f52ff398e870(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27af8e5f561e3e573b9a04774edf0c0c6cf2f3e31d385b4ffe28873a39dc7e48(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fa195f1583c09a0caa02fa5c50ed928dbf5232ca80e6affc9fa715d83e57cd1(
    value: typing.Union[_IResolvable_da3f097b, CfnComputationModel.ComputationModelConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be967ec7617c0ed0efa50fb8a3519a87b8800751beb73a6449a1637314931d2c(
    value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnComputationModel.ComputationModelDataBindingValueProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a009db7b645690134b3878ea2c7cdee53682cf297919e1b3f54b712539f8b0de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d577131789cc578cee733460d23165debfb49d0d90b94e3e10d38d4d0d44a79(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a82834353206c4a7be4a8ed40665c48481769bb21be0214fd279c598a8007929(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69d1839ca00b91b9b1180620638bc2ec0b687463e3828b79ad3dd49ef5189aa7(
    *,
    input_properties: builtins.str,
    result_property: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__949067d8ab294bdc850ab646091006fd0e748f018285b21dcc99fb980c1a0f5e(
    *,
    asset_model_id: builtins.str,
    property_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4a3ae5efabf3788291f9b7ef194e309cc061d66db8346fea04452f02980728d(
    *,
    asset_id: builtins.str,
    property_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b33f062481ddc382b1fb7a44ec3672f2844ad5a2ee31f5ede04b108b279328e(
    *,
    anomaly_detection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputationModel.AnomalyDetectionComputationModelConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30609777f6bb1d4c3fb4232f9af93dc24089504c669f64d1de9edd24a9e6d0df(
    *,
    asset_model_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputationModel.AssetModelPropertyBindingValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    asset_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputationModel.AssetPropertyBindingValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputationModel.ComputationModelDataBindingValueProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed97b2e804664b4c2090fb09c1141fc63e60c4fbaee41661ef227778c1ed7dd3(
    *,
    computation_model_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputationModel.ComputationModelConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    computation_model_data_binding: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputationModel.ComputationModelDataBindingValueProperty, typing.Dict[builtins.str, typing.Any]]]]],
    computation_model_name: builtins.str,
    computation_model_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7408e63e7ba97e630e06dc4a383d275da9719808da2d750b179e27c09b363329(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    dashboard_definition: builtins.str,
    dashboard_description: builtins.str,
    dashboard_name: builtins.str,
    project_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b472ad5fec8e10a47deb9d29be81c0539f4b5be2ab95923bc43842cace7b7859(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c575a08895bd58ff6950d32eea6f2d29ac539b1a8ea16ab5a6815a167a66a53(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dff968d51e506fdd3d98d6169f84765246ff8d86876d701729950862efbcb07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2e71c5b9cc6130bf794aba4fc07bef70a290bd69088f6d2e772d1c018383a99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44f37a7656daf53d7fabe76785ece45b5c2bc6eb84289aacfae174ffe2497a56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d621f50afe555c434794e30d38d7e134a8c91ebdac9f42da18c26db60e90e079(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c685ecf3c21151b25cdde509c49bdd7b2812d894f5dab8c2fd028d7ea55b28c2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e87db1e2d08493321e273557f52f1665d6e8b066bd235aa15fbe6b372c969da(
    *,
    dashboard_definition: builtins.str,
    dashboard_description: builtins.str,
    dashboard_name: builtins.str,
    project_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44369ff07e07f1dbb28102a65eb5a8e6317f5b2e832b326cf3fc0bef13d7e1cc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    dataset_name: builtins.str,
    dataset_source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.DatasetSourceProperty, typing.Dict[builtins.str, typing.Any]]],
    dataset_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c537b447cd6a1f193bb6937137b32d81fb8fc58b3637f501b722c0a287eff25e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__052a04636940cb669719f99afdd8ce7ebf71823f5bd4fc4a56e8e06e962e930e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b47777cde433184527816fbc94a5e50f4751f14ba951445e4260fbf75e5f9ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ee08c36e5cc935e5be89b5ecc51c303d15d2f3f60f818632c78e21d65cc0e19(
    value: typing.Union[_IResolvable_da3f097b, CfnDataset.DatasetSourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb27e9e2c5f0a4b58c2867084de6a19d127db8e56f71ceb33ecb4c038c5aeba9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc32716df823dcb28cde4279865e5af2ea0ed286db7d62b848f8ebbc49079037(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f58345f56b93936a864a7b8b77051f0ab53f3948caa6107fb0e0b5e918839970(
    *,
    source_format: builtins.str,
    source_type: builtins.str,
    source_detail: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.SourceDetailProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d827c7c36898f2d8c24814838df150d16db4b05143943eaff03575fc4152bf9(
    *,
    knowledge_base_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a598d81c202f610ae61fa753a459c38aa834bd6a34e5b7a54eb9f63914b22c7(
    *,
    kendra: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.KendraSourceDetailProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ecfd46cd288d1fcedea054d9db52e78eed5b596789d023c110fcfb9e1e41ff8(
    *,
    dataset_name: builtins.str,
    dataset_source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.DatasetSourceProperty, typing.Dict[builtins.str, typing.Any]]],
    dataset_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4e7aa58e6088e2cbee0005ea5a43b4c9db3b6647e2ff56a2b30310e7b1a75db(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    gateway_name: builtins.str,
    gateway_platform: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayPlatformProperty, typing.Dict[builtins.str, typing.Any]]],
    gateway_capability_summaries: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayCapabilitySummaryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    gateway_version: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32d18496c19dcd70d3e2bfdd8e37ae7c14e763732057eeb476d73309d3c982b7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e487f6fea4e7332025180df4bf127d8e2f634a79a13359046159c2b43bf6acd1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b71cb9978b1b17c72ceab4f152568de72d45008677395cf39abe54f3af29d6d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b804b846f70fe7670a1f8b651e7e17d1fb4055204c26a834d8529aa9d4f27ca9(
    value: typing.Union[_IResolvable_da3f097b, CfnGateway.GatewayPlatformProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0575717a55b787485944fbb94729c238b3cf9e112e2d0d439edfd4f8dd27b9b8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGateway.GatewayCapabilitySummaryProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9914b4c24d20de7b662b3040cb09c4bae39421cef7517509a76b470a8687bc9a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26fcdcade7dc164a37aa04c5ee368b075236804669ba2be2553ac47ed59284da(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ee1ae3477d1c1b70d9b9edb2163592393d56e767842107ae7939132c13ce358(
    *,
    capability_namespace: builtins.str,
    capability_configuration: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d661bcb76cb5472e741e4e4c43ddf5d8a0dc76895775f2d9c80eb435edf5fc23(
    *,
    greengrass: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GreengrassProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    greengrass_v2: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GreengrassV2Property, typing.Dict[builtins.str, typing.Any]]]] = None,
    siemens_ie: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.SiemensIEProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__869d2e480b38a0e2376044c367d2367e64287fbb827bbca68d53b1515c75fbed(
    *,
    group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaa34ef3ffa417e0d8477bdf5fd83220079621fb80b75a881ad5c04a9c485841(
    *,
    core_device_thing_name: builtins.str,
    core_device_operating_system: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5c36e991ce3543e0259817d60bf936941834dcd087997082364d6b61a83223f(
    *,
    iot_core_thing_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96b726a7f6953ced23491d12afc63dd3960b8d44e1734397f1db9d45a0cf6793(
    *,
    gateway_name: builtins.str,
    gateway_platform: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayPlatformProperty, typing.Dict[builtins.str, typing.Any]]],
    gateway_capability_summaries: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayCapabilitySummaryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    gateway_version: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbc23e7f8ea9f23ecedfbb8e22cd39fad67b5932c9e8eb1d5d50975c13a3c5e8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    portal_contact_email: builtins.str,
    portal_name: builtins.str,
    role_arn: builtins.str,
    alarms: typing.Any = None,
    notification_sender_email: typing.Optional[builtins.str] = None,
    portal_auth_mode: typing.Optional[builtins.str] = None,
    portal_description: typing.Optional[builtins.str] = None,
    portal_type: typing.Optional[builtins.str] = None,
    portal_type_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnPortal.PortalTypeEntryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e35d29c0f35bd7b72ba87b37ebcc981c82f95575036b8a5527137363bcb6ec6d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c7d41561b5ff568159d53d88d8901853afd0b84ccc6b789aee97627ac22af3b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76cc7d18d9cdc2c0262648281c53cc8a8880f76962fd416b38bc00d5e2e4d807(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e09665f12ada311bc3e92f26c950c3b352054729e545455c7ab822ebd2ba0d74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__801da38b8b0799f806382f6db4934f5cde8b7b5856a63457bf47a3c3d721e0ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a07bf890e264d76055c18252e2d1882abb53a19982220ec6c89215096dedb5a(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__450baca4a5d4d44597d00571c99f952263e5c4dcc79c06e175ed7758a5e5dc07(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41cc3527d6f0a3c056b662b09636e8487fe6b2cd4d2a86f883aad8fa1e852b4b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aef69531546e69c52fb621d608894b8a13ea5ce64a0e713b24aacd2b912457dd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e30e6480af8bf6c9156f76afcfbc51187c15ffe199e8b2a284dae86baaccb878(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d9d6a7fc128e24a5796b5247e692bea000e44c1afd3fed96b4e4cb15f279f74(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnPortal.PortalTypeEntryProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__094008154aa9c2ed7f23db7b3bd3bbad9f03aa4bbdaba95af7958b252ddd4bc2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a766409f9773f0cd5cb3dd5c49ce92586c7cc4f8233f8f908d042bfd8359991(
    *,
    alarm_role_arn: typing.Optional[builtins.str] = None,
    notification_lambda_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__159de1986a281fe75049e969ee02d9509ce935b8bef35eb415647d6e66e0feab(
    *,
    portal_tools: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db927eff8866e7afa967752c7f48d5d8ab1bd58489a78569b13cac34c81ba650(
    *,
    portal_contact_email: builtins.str,
    portal_name: builtins.str,
    role_arn: builtins.str,
    alarms: typing.Any = None,
    notification_sender_email: typing.Optional[builtins.str] = None,
    portal_auth_mode: typing.Optional[builtins.str] = None,
    portal_description: typing.Optional[builtins.str] = None,
    portal_type: typing.Optional[builtins.str] = None,
    portal_type_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnPortal.PortalTypeEntryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ca003aa6daa3e15044d74469428b378e883b1a517620f59fc80331c1a383f15(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    portal_id: builtins.str,
    project_name: builtins.str,
    asset_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    project_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a16b8d5ebb2cc95753d1c1a1a523d80ae58e829ae8ce8450719faca461b1b1c8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__453b9d09035594771c3821a921bed5d09e9b261f5293c2fdd845898471727f84(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f26f3f5573e85a97b08157df77b5856c58817b81405637e615727b3cb10e7e0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d035e8224bbba25abe29c7e7ff3e91e74da8b89504dfa0422128a6b9dd419fce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2efb7789fd61ffe146d6ef68fdc319d09b3f1b9c49d567dd16971f31010169b4(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80b733624c751f502aeb54f4ab221ff7e5ae55f6bd1e87090cac18105f6c4a70(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcb700fa41df1dfaa6c4cfad19b3a4f56b9aa96ef4b6e315d990eb0a286b2cdc(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7af827083026086703d7567e7e4a27cf6d5bb590317461231a2e997d42b85e1b(
    *,
    portal_id: builtins.str,
    project_name: builtins.str,
    asset_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    project_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
