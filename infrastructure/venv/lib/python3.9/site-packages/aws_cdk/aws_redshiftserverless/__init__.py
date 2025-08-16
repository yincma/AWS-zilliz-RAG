r'''
# AWS::RedshiftServerless Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_redshiftserverless as redshiftserverless
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for RedshiftServerless construct libraries](https://constructs.dev/search?q=redshiftserverless)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::RedshiftServerless resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RedshiftServerless.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::RedshiftServerless](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RedshiftServerless.html).

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


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnNamespace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnNamespace",
):
    '''A collection of database objects and users.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html
    :cloudformationResource: AWS::RedshiftServerless::Namespace
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshiftserverless as redshiftserverless
        
        # namespace_resource_policy: Any
        
        cfn_namespace = redshiftserverless.CfnNamespace(self, "MyCfnNamespace",
            namespace_name="namespaceName",
        
            # the properties below are optional
            admin_password_secret_kms_key_id="adminPasswordSecretKmsKeyId",
            admin_username="adminUsername",
            admin_user_password="adminUserPassword",
            db_name="dbName",
            default_iam_role_arn="defaultIamRoleArn",
            final_snapshot_name="finalSnapshotName",
            final_snapshot_retention_period=123,
            iam_roles=["iamRoles"],
            kms_key_id="kmsKeyId",
            log_exports=["logExports"],
            manage_admin_password=False,
            namespace_resource_policy=namespace_resource_policy,
            redshift_idc_application_arn="redshiftIdcApplicationArn",
            snapshot_copy_configurations=[redshiftserverless.CfnNamespace.SnapshotCopyConfigurationProperty(
                destination_region="destinationRegion",
        
                # the properties below are optional
                destination_kms_key_id="destinationKmsKeyId",
                snapshot_retention_period=123
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
        namespace_name: builtins.str,
        admin_password_secret_kms_key_id: typing.Optional[builtins.str] = None,
        admin_username: typing.Optional[builtins.str] = None,
        admin_user_password: typing.Optional[builtins.str] = None,
        db_name: typing.Optional[builtins.str] = None,
        default_iam_role_arn: typing.Optional[builtins.str] = None,
        final_snapshot_name: typing.Optional[builtins.str] = None,
        final_snapshot_retention_period: typing.Optional[jsii.Number] = None,
        iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        manage_admin_password: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        namespace_resource_policy: typing.Any = None,
        redshift_idc_application_arn: typing.Optional[builtins.str] = None,
        snapshot_copy_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnNamespace.SnapshotCopyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param namespace_name: The name of the namespace. Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.
        :param admin_password_secret_kms_key_id: The ID of the AWS Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if ``ManageAdminPassword`` is ``true`` .
        :param admin_username: The username of the administrator for the primary database created in the namespace.
        :param admin_user_password: The password of the administrator for the primary database created in the namespace.
        :param db_name: The name of the primary database created in the namespace.
        :param default_iam_role_arn: The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.
        :param final_snapshot_name: The name of the snapshot to be created before the namespace is deleted.
        :param final_snapshot_retention_period: How long to retain the final snapshot.
        :param iam_roles: A list of IAM roles to associate with the namespace.
        :param kms_key_id: The ID of the AWS Key Management Service key used to encrypt your data.
        :param log_exports: The types of logs the namespace can export. Available export types are ``userlog`` , ``connectionlog`` , and ``useractivitylog`` .
        :param manage_admin_password: If true, Amazon Redshift uses AWS Secrets Manager to manage the namespace's admin credentials. You can't use ``AdminUserPassword`` if ``ManageAdminPassword`` is true. If ``ManageAdminPassword`` is ``false`` or not set, Amazon Redshift uses ``AdminUserPassword`` for the admin user account's password.
        :param namespace_resource_policy: The resource policy that will be attached to the namespace.
        :param redshift_idc_application_arn: The ARN for the Redshift application that integrates with IAM Identity Center.
        :param snapshot_copy_configurations: The snapshot copy configurations for the namespace.
        :param tags: The map of the key-value pairs used to tag the namespace.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e517382d9f55a518348d7299a7ce6c5be66bae2202f4223bf3c891a7dd669682)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNamespaceProps(
            namespace_name=namespace_name,
            admin_password_secret_kms_key_id=admin_password_secret_kms_key_id,
            admin_username=admin_username,
            admin_user_password=admin_user_password,
            db_name=db_name,
            default_iam_role_arn=default_iam_role_arn,
            final_snapshot_name=final_snapshot_name,
            final_snapshot_retention_period=final_snapshot_retention_period,
            iam_roles=iam_roles,
            kms_key_id=kms_key_id,
            log_exports=log_exports,
            manage_admin_password=manage_admin_password,
            namespace_resource_policy=namespace_resource_policy,
            redshift_idc_application_arn=redshift_idc_application_arn,
            snapshot_copy_configurations=snapshot_copy_configurations,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2df0038e9ec3a1b73ddb07c3b803a742204804b2ccd2aab0d7df9fbb8521f86)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d877d23369c8f10ea1630884d7e7c879ab22a49fc05986834857785664c640ca)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespace")
    def attr_namespace(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Namespace
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrNamespace"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceAdminUsername")
    def attr_namespace_admin_username(self) -> builtins.str:
        '''The username of the administrator for the first database created in the namespace.

        :cloudformationAttribute: Namespace.AdminUsername
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceAdminUsername"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceCreationDate")
    def attr_namespace_creation_date(self) -> builtins.str:
        '''The date of when the namespace was created.

        :cloudformationAttribute: Namespace.CreationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceCreationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceDbName")
    def attr_namespace_db_name(self) -> builtins.str:
        '''The name of the first database created in the namespace.

        :cloudformationAttribute: Namespace.DbName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceDbName"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceDefaultIamRoleArn")
    def attr_namespace_default_iam_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.

        :cloudformationAttribute: Namespace.DefaultIamRoleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceDefaultIamRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceIamRoles")
    def attr_namespace_iam_roles(self) -> typing.List[builtins.str]:
        '''A list of IAM roles to associate with the namespace.

        :cloudformationAttribute: Namespace.IamRoles
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrNamespaceIamRoles"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceKmsKeyId")
    def attr_namespace_kms_key_id(self) -> builtins.str:
        '''The ID of the AWS Key Management Service key used to encrypt your data.

        :cloudformationAttribute: Namespace.KmsKeyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceKmsKeyId"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceLogExports")
    def attr_namespace_log_exports(self) -> typing.List[builtins.str]:
        '''The types of logs the namespace can export.

        Available export types are ``User log`` , ``Connection log`` , and ``User activity log`` .

        :cloudformationAttribute: Namespace.LogExports
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrNamespaceLogExports"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceNamespaceArn")
    def attr_namespace_namespace_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) associated with a namespace.

        :cloudformationAttribute: Namespace.NamespaceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceNamespaceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceNamespaceId")
    def attr_namespace_namespace_id(self) -> builtins.str:
        '''The unique identifier of a namespace.

        :cloudformationAttribute: Namespace.NamespaceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceNamespaceId"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceNamespaceName")
    def attr_namespace_namespace_name(self) -> builtins.str:
        '''The name of the namespace.

        Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.

        :cloudformationAttribute: Namespace.NamespaceName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceNamespaceName"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespaceStatus")
    def attr_namespace_status(self) -> builtins.str:
        '''The status of the namespace.

        :cloudformationAttribute: Namespace.Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespaceStatus"))

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
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> builtins.str:
        '''The name of the namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "namespaceName"))

    @namespace_name.setter
    def namespace_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fe15d8ff16345a3e36d8c090d48eea89c8cd559ac4218facdfd95b67e49140c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="adminPasswordSecretKmsKeyId")
    def admin_password_secret_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminPasswordSecretKmsKeyId"))

    @admin_password_secret_kms_key_id.setter
    def admin_password_secret_kms_key_id(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ad26fc5262e682a19af3392d1855021d70d396b74b82cb73cc9022919f97e63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminPasswordSecretKmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> typing.Optional[builtins.str]:
        '''The username of the administrator for the primary database created in the namespace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e95b6bb908e50903825c7cbfdb447ab3aceb27b3a93be8aa57fe8923f432493)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUsername", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="adminUserPassword")
    def admin_user_password(self) -> typing.Optional[builtins.str]:
        '''The password of the administrator for the primary database created in the namespace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUserPassword"))

    @admin_user_password.setter
    def admin_user_password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b50aae57ce0c503e5aed7528570d1ab32511eacbfe2dcac51d410dd4bb1991ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUserPassword", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dbName")
    def db_name(self) -> typing.Optional[builtins.str]:
        '''The name of the primary database created in the namespace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbName"))

    @db_name.setter
    def db_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8947213c316180fbcdb1956ca9a54febcb6a874110724c51c1db8705f8186d0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultIamRoleArn"))

    @default_iam_role_arn.setter
    def default_iam_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a992711b01695733a564873ba440d2806a3692e807afc16701507c986201edd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultIamRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="finalSnapshotName")
    def final_snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The name of the snapshot to be created before the namespace is deleted.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "finalSnapshotName"))

    @final_snapshot_name.setter
    def final_snapshot_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de06e0fc02a451c4e9e47c3f839f6289f8f8e9d4dbc0867eb263e09672990c7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finalSnapshotName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="finalSnapshotRetentionPeriod")
    def final_snapshot_retention_period(self) -> typing.Optional[jsii.Number]:
        '''How long to retain the final snapshot.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "finalSnapshotRetentionPeriod"))

    @final_snapshot_retention_period.setter
    def final_snapshot_retention_period(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ae56ba94c395d18dd103368c4ca09a505763b47324b4820065925d61c84adaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "finalSnapshotRetentionPeriod", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iamRoles")
    def iam_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of IAM roles to associate with the namespace.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "iamRoles"))

    @iam_roles.setter
    def iam_roles(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9111ebc5ef107cd5d00c7617518664163ccd1b1d99fb0ec53548dd04073b0e77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoles", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS Key Management Service key used to encrypt your data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bc1c937667ef895444beeaaacfd8af398b90be0a42f50184325fdb96072b5ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logExports")
    def log_exports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The types of logs the namespace can export.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "logExports"))

    @log_exports.setter
    def log_exports(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1526e0cedff0515a6bb96570f366670e82fb4d0cc597e2d7a8b0a091f0420dea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logExports", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="manageAdminPassword")
    def manage_admin_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If true, Amazon Redshift uses AWS Secrets Manager to manage the namespace's admin credentials.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "manageAdminPassword"))

    @manage_admin_password.setter
    def manage_admin_password(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fee9e13028e66f79f12c6ed7063cc442fd9b8a5aa18d9a39ced55fd585d8f0d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageAdminPassword", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="namespaceResourcePolicy")
    def namespace_resource_policy(self) -> typing.Any:
        '''The resource policy that will be attached to the namespace.'''
        return typing.cast(typing.Any, jsii.get(self, "namespaceResourcePolicy"))

    @namespace_resource_policy.setter
    def namespace_resource_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43a289d7dca3804ca980a93314a4c0b2949e95448b9e91aef20d960cd1facef7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceResourcePolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="redshiftIdcApplicationArn")
    def redshift_idc_application_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the Redshift application that integrates with IAM Identity Center.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redshiftIdcApplicationArn"))

    @redshift_idc_application_arn.setter
    def redshift_idc_application_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51136c4f6d62ea1ed8116bbb890860f45a983131873ecd0a7b407595037600cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftIdcApplicationArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="snapshotCopyConfigurations")
    def snapshot_copy_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnNamespace.SnapshotCopyConfigurationProperty"]]]]:
        '''The snapshot copy configurations for the namespace.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnNamespace.SnapshotCopyConfigurationProperty"]]]], jsii.get(self, "snapshotCopyConfigurations"))

    @snapshot_copy_configurations.setter
    def snapshot_copy_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnNamespace.SnapshotCopyConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7336d2da1a6ceace7b9ad8afbae65968e0c9440d9a2bcf4cd5e62d531da1693)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotCopyConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The map of the key-value pairs used to tag the namespace.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e2da7bae4bc39426d05dc2f307e08d5246472ad626b032ef4c2ea7b7d1bd33f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnNamespace.NamespaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "admin_password_secret_arn": "adminPasswordSecretArn",
            "admin_password_secret_kms_key_id": "adminPasswordSecretKmsKeyId",
            "admin_username": "adminUsername",
            "creation_date": "creationDate",
            "db_name": "dbName",
            "default_iam_role_arn": "defaultIamRoleArn",
            "iam_roles": "iamRoles",
            "kms_key_id": "kmsKeyId",
            "log_exports": "logExports",
            "namespace_arn": "namespaceArn",
            "namespace_id": "namespaceId",
            "namespace_name": "namespaceName",
            "status": "status",
        },
    )
    class NamespaceProperty:
        def __init__(
            self,
            *,
            admin_password_secret_arn: typing.Optional[builtins.str] = None,
            admin_password_secret_kms_key_id: typing.Optional[builtins.str] = None,
            admin_username: typing.Optional[builtins.str] = None,
            creation_date: typing.Optional[builtins.str] = None,
            db_name: typing.Optional[builtins.str] = None,
            default_iam_role_arn: typing.Optional[builtins.str] = None,
            iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
            log_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
            namespace_arn: typing.Optional[builtins.str] = None,
            namespace_id: typing.Optional[builtins.str] = None,
            namespace_name: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A collection of database objects and users.

            :param admin_password_secret_arn: The Amazon Resource Name (ARN) for the namespace's admin user credentials secret.
            :param admin_password_secret_kms_key_id: The ID of the AWS Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.
            :param admin_username: The username of the administrator for the first database created in the namespace.
            :param creation_date: The date of when the namespace was created.
            :param db_name: The name of the first database created in the namespace.
            :param default_iam_role_arn: The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.
            :param iam_roles: A list of IAM roles to associate with the namespace.
            :param kms_key_id: The ID of the AWS Key Management Service key used to encrypt your data.
            :param log_exports: The types of logs the namespace can export. Available export types are User log, Connection log, and User activity log.
            :param namespace_arn: The Amazon Resource Name (ARN) associated with a namespace.
            :param namespace_id: The unique identifier of a namespace.
            :param namespace_name: The name of the namespace. Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.
            :param status: The status of the namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                namespace_property = redshiftserverless.CfnNamespace.NamespaceProperty(
                    admin_password_secret_arn="adminPasswordSecretArn",
                    admin_password_secret_kms_key_id="adminPasswordSecretKmsKeyId",
                    admin_username="adminUsername",
                    creation_date="creationDate",
                    db_name="dbName",
                    default_iam_role_arn="defaultIamRoleArn",
                    iam_roles=["iamRoles"],
                    kms_key_id="kmsKeyId",
                    log_exports=["logExports"],
                    namespace_arn="namespaceArn",
                    namespace_id="namespaceId",
                    namespace_name="namespaceName",
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6bcbea65acb7d2a3cef7455cfbb52c832d3da01cd5e02df21a06cdb2b4822e35)
                check_type(argname="argument admin_password_secret_arn", value=admin_password_secret_arn, expected_type=type_hints["admin_password_secret_arn"])
                check_type(argname="argument admin_password_secret_kms_key_id", value=admin_password_secret_kms_key_id, expected_type=type_hints["admin_password_secret_kms_key_id"])
                check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
                check_type(argname="argument creation_date", value=creation_date, expected_type=type_hints["creation_date"])
                check_type(argname="argument db_name", value=db_name, expected_type=type_hints["db_name"])
                check_type(argname="argument default_iam_role_arn", value=default_iam_role_arn, expected_type=type_hints["default_iam_role_arn"])
                check_type(argname="argument iam_roles", value=iam_roles, expected_type=type_hints["iam_roles"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
                check_type(argname="argument log_exports", value=log_exports, expected_type=type_hints["log_exports"])
                check_type(argname="argument namespace_arn", value=namespace_arn, expected_type=type_hints["namespace_arn"])
                check_type(argname="argument namespace_id", value=namespace_id, expected_type=type_hints["namespace_id"])
                check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if admin_password_secret_arn is not None:
                self._values["admin_password_secret_arn"] = admin_password_secret_arn
            if admin_password_secret_kms_key_id is not None:
                self._values["admin_password_secret_kms_key_id"] = admin_password_secret_kms_key_id
            if admin_username is not None:
                self._values["admin_username"] = admin_username
            if creation_date is not None:
                self._values["creation_date"] = creation_date
            if db_name is not None:
                self._values["db_name"] = db_name
            if default_iam_role_arn is not None:
                self._values["default_iam_role_arn"] = default_iam_role_arn
            if iam_roles is not None:
                self._values["iam_roles"] = iam_roles
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if log_exports is not None:
                self._values["log_exports"] = log_exports
            if namespace_arn is not None:
                self._values["namespace_arn"] = namespace_arn
            if namespace_id is not None:
                self._values["namespace_id"] = namespace_id
            if namespace_name is not None:
                self._values["namespace_name"] = namespace_name
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def admin_password_secret_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the namespace's admin user credentials secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-adminpasswordsecretarn
            '''
            result = self._values.get("admin_password_secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def admin_password_secret_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the AWS Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-adminpasswordsecretkmskeyid
            '''
            result = self._values.get("admin_password_secret_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def admin_username(self) -> typing.Optional[builtins.str]:
            '''The username of the administrator for the first database created in the namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-adminusername
            '''
            result = self._values.get("admin_username")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def creation_date(self) -> typing.Optional[builtins.str]:
            '''The date of when the namespace was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-creationdate
            '''
            result = self._values.get("creation_date")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def db_name(self) -> typing.Optional[builtins.str]:
            '''The name of the first database created in the namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-dbname
            '''
            result = self._values.get("db_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def default_iam_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-defaultiamrolearn
            '''
            result = self._values.get("default_iam_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def iam_roles(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of IAM roles to associate with the namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-iamroles
            '''
            result = self._values.get("iam_roles")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the AWS Key Management Service key used to encrypt your data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_exports(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The types of logs the namespace can export.

            Available export types are User log, Connection log, and User activity log.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-logexports
            '''
            result = self._values.get("log_exports")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def namespace_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) associated with a namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-namespacearn
            '''
            result = self._values.get("namespace_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespace_id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of a namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-namespaceid
            '''
            result = self._values.get("namespace_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespace_name(self) -> typing.Optional[builtins.str]:
            '''The name of the namespace.

            Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-namespacename
            '''
            result = self._values.get("namespace_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-namespace.html#cfn-redshiftserverless-namespace-namespace-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NamespaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnNamespace.SnapshotCopyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_region": "destinationRegion",
            "destination_kms_key_id": "destinationKmsKeyId",
            "snapshot_retention_period": "snapshotRetentionPeriod",
        },
    )
    class SnapshotCopyConfigurationProperty:
        def __init__(
            self,
            *,
            destination_region: builtins.str,
            destination_kms_key_id: typing.Optional[builtins.str] = None,
            snapshot_retention_period: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The object that you configure to copy snapshots from one namespace to a namespace in another AWS Region .

            :param destination_region: The destination AWS Region to copy snapshots to.
            :param destination_kms_key_id: The ID of the KMS key to use to encrypt your snapshots in the destination AWS Region .
            :param snapshot_retention_period: The retention period of snapshots that are copied to the destination AWS Region .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-snapshotcopyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                snapshot_copy_configuration_property = redshiftserverless.CfnNamespace.SnapshotCopyConfigurationProperty(
                    destination_region="destinationRegion",
                
                    # the properties below are optional
                    destination_kms_key_id="destinationKmsKeyId",
                    snapshot_retention_period=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4f726a14406204ec2ead254e53f2cdca3d4ac96a2d835e99da9cbbb58c02dccd)
                check_type(argname="argument destination_region", value=destination_region, expected_type=type_hints["destination_region"])
                check_type(argname="argument destination_kms_key_id", value=destination_kms_key_id, expected_type=type_hints["destination_kms_key_id"])
                check_type(argname="argument snapshot_retention_period", value=snapshot_retention_period, expected_type=type_hints["snapshot_retention_period"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_region": destination_region,
            }
            if destination_kms_key_id is not None:
                self._values["destination_kms_key_id"] = destination_kms_key_id
            if snapshot_retention_period is not None:
                self._values["snapshot_retention_period"] = snapshot_retention_period

        @builtins.property
        def destination_region(self) -> builtins.str:
            '''The destination AWS Region to copy snapshots to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-snapshotcopyconfiguration.html#cfn-redshiftserverless-namespace-snapshotcopyconfiguration-destinationregion
            '''
            result = self._values.get("destination_region")
            assert result is not None, "Required property 'destination_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the KMS key to use to encrypt your snapshots in the destination AWS Region .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-snapshotcopyconfiguration.html#cfn-redshiftserverless-namespace-snapshotcopyconfiguration-destinationkmskeyid
            '''
            result = self._values.get("destination_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def snapshot_retention_period(self) -> typing.Optional[jsii.Number]:
            '''The retention period of snapshots that are copied to the destination AWS Region .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-namespace-snapshotcopyconfiguration.html#cfn-redshiftserverless-namespace-snapshotcopyconfiguration-snapshotretentionperiod
            '''
            result = self._values.get("snapshot_retention_period")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnapshotCopyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnNamespaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "namespace_name": "namespaceName",
        "admin_password_secret_kms_key_id": "adminPasswordSecretKmsKeyId",
        "admin_username": "adminUsername",
        "admin_user_password": "adminUserPassword",
        "db_name": "dbName",
        "default_iam_role_arn": "defaultIamRoleArn",
        "final_snapshot_name": "finalSnapshotName",
        "final_snapshot_retention_period": "finalSnapshotRetentionPeriod",
        "iam_roles": "iamRoles",
        "kms_key_id": "kmsKeyId",
        "log_exports": "logExports",
        "manage_admin_password": "manageAdminPassword",
        "namespace_resource_policy": "namespaceResourcePolicy",
        "redshift_idc_application_arn": "redshiftIdcApplicationArn",
        "snapshot_copy_configurations": "snapshotCopyConfigurations",
        "tags": "tags",
    },
)
class CfnNamespaceProps:
    def __init__(
        self,
        *,
        namespace_name: builtins.str,
        admin_password_secret_kms_key_id: typing.Optional[builtins.str] = None,
        admin_username: typing.Optional[builtins.str] = None,
        admin_user_password: typing.Optional[builtins.str] = None,
        db_name: typing.Optional[builtins.str] = None,
        default_iam_role_arn: typing.Optional[builtins.str] = None,
        final_snapshot_name: typing.Optional[builtins.str] = None,
        final_snapshot_retention_period: typing.Optional[jsii.Number] = None,
        iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        log_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
        manage_admin_password: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        namespace_resource_policy: typing.Any = None,
        redshift_idc_application_arn: typing.Optional[builtins.str] = None,
        snapshot_copy_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnNamespace.SnapshotCopyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnNamespace``.

        :param namespace_name: The name of the namespace. Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.
        :param admin_password_secret_kms_key_id: The ID of the AWS Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret. You can only use this parameter if ``ManageAdminPassword`` is ``true`` .
        :param admin_username: The username of the administrator for the primary database created in the namespace.
        :param admin_user_password: The password of the administrator for the primary database created in the namespace.
        :param db_name: The name of the primary database created in the namespace.
        :param default_iam_role_arn: The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.
        :param final_snapshot_name: The name of the snapshot to be created before the namespace is deleted.
        :param final_snapshot_retention_period: How long to retain the final snapshot.
        :param iam_roles: A list of IAM roles to associate with the namespace.
        :param kms_key_id: The ID of the AWS Key Management Service key used to encrypt your data.
        :param log_exports: The types of logs the namespace can export. Available export types are ``userlog`` , ``connectionlog`` , and ``useractivitylog`` .
        :param manage_admin_password: If true, Amazon Redshift uses AWS Secrets Manager to manage the namespace's admin credentials. You can't use ``AdminUserPassword`` if ``ManageAdminPassword`` is true. If ``ManageAdminPassword`` is ``false`` or not set, Amazon Redshift uses ``AdminUserPassword`` for the admin user account's password.
        :param namespace_resource_policy: The resource policy that will be attached to the namespace.
        :param redshift_idc_application_arn: The ARN for the Redshift application that integrates with IAM Identity Center.
        :param snapshot_copy_configurations: The snapshot copy configurations for the namespace.
        :param tags: The map of the key-value pairs used to tag the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshiftserverless as redshiftserverless
            
            # namespace_resource_policy: Any
            
            cfn_namespace_props = redshiftserverless.CfnNamespaceProps(
                namespace_name="namespaceName",
            
                # the properties below are optional
                admin_password_secret_kms_key_id="adminPasswordSecretKmsKeyId",
                admin_username="adminUsername",
                admin_user_password="adminUserPassword",
                db_name="dbName",
                default_iam_role_arn="defaultIamRoleArn",
                final_snapshot_name="finalSnapshotName",
                final_snapshot_retention_period=123,
                iam_roles=["iamRoles"],
                kms_key_id="kmsKeyId",
                log_exports=["logExports"],
                manage_admin_password=False,
                namespace_resource_policy=namespace_resource_policy,
                redshift_idc_application_arn="redshiftIdcApplicationArn",
                snapshot_copy_configurations=[redshiftserverless.CfnNamespace.SnapshotCopyConfigurationProperty(
                    destination_region="destinationRegion",
            
                    # the properties below are optional
                    destination_kms_key_id="destinationKmsKeyId",
                    snapshot_retention_period=123
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5964a5da555f62a5d9615a6e07cd0d1128cdf904fd5aa3c5be9fd5e53dc30bd9)
            check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
            check_type(argname="argument admin_password_secret_kms_key_id", value=admin_password_secret_kms_key_id, expected_type=type_hints["admin_password_secret_kms_key_id"])
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument admin_user_password", value=admin_user_password, expected_type=type_hints["admin_user_password"])
            check_type(argname="argument db_name", value=db_name, expected_type=type_hints["db_name"])
            check_type(argname="argument default_iam_role_arn", value=default_iam_role_arn, expected_type=type_hints["default_iam_role_arn"])
            check_type(argname="argument final_snapshot_name", value=final_snapshot_name, expected_type=type_hints["final_snapshot_name"])
            check_type(argname="argument final_snapshot_retention_period", value=final_snapshot_retention_period, expected_type=type_hints["final_snapshot_retention_period"])
            check_type(argname="argument iam_roles", value=iam_roles, expected_type=type_hints["iam_roles"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument log_exports", value=log_exports, expected_type=type_hints["log_exports"])
            check_type(argname="argument manage_admin_password", value=manage_admin_password, expected_type=type_hints["manage_admin_password"])
            check_type(argname="argument namespace_resource_policy", value=namespace_resource_policy, expected_type=type_hints["namespace_resource_policy"])
            check_type(argname="argument redshift_idc_application_arn", value=redshift_idc_application_arn, expected_type=type_hints["redshift_idc_application_arn"])
            check_type(argname="argument snapshot_copy_configurations", value=snapshot_copy_configurations, expected_type=type_hints["snapshot_copy_configurations"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "namespace_name": namespace_name,
        }
        if admin_password_secret_kms_key_id is not None:
            self._values["admin_password_secret_kms_key_id"] = admin_password_secret_kms_key_id
        if admin_username is not None:
            self._values["admin_username"] = admin_username
        if admin_user_password is not None:
            self._values["admin_user_password"] = admin_user_password
        if db_name is not None:
            self._values["db_name"] = db_name
        if default_iam_role_arn is not None:
            self._values["default_iam_role_arn"] = default_iam_role_arn
        if final_snapshot_name is not None:
            self._values["final_snapshot_name"] = final_snapshot_name
        if final_snapshot_retention_period is not None:
            self._values["final_snapshot_retention_period"] = final_snapshot_retention_period
        if iam_roles is not None:
            self._values["iam_roles"] = iam_roles
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if log_exports is not None:
            self._values["log_exports"] = log_exports
        if manage_admin_password is not None:
            self._values["manage_admin_password"] = manage_admin_password
        if namespace_resource_policy is not None:
            self._values["namespace_resource_policy"] = namespace_resource_policy
        if redshift_idc_application_arn is not None:
            self._values["redshift_idc_application_arn"] = redshift_idc_application_arn
        if snapshot_copy_configurations is not None:
            self._values["snapshot_copy_configurations"] = snapshot_copy_configurations
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def namespace_name(self) -> builtins.str:
        '''The name of the namespace.

        Must be between 3-64 alphanumeric characters in lowercase, and it cannot be a reserved word. A list of reserved words can be found in `Reserved Words <https://docs.aws.amazon.com//redshift/latest/dg/r_pg_keywords.html>`_ in the Amazon Redshift Database Developer Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-namespacename
        '''
        result = self._values.get("namespace_name")
        assert result is not None, "Required property 'namespace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_password_secret_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.

        You can only use this parameter if ``ManageAdminPassword`` is ``true`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-adminpasswordsecretkmskeyid
        '''
        result = self._values.get("admin_password_secret_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def admin_username(self) -> typing.Optional[builtins.str]:
        '''The username of the administrator for the primary database created in the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-adminusername
        '''
        result = self._values.get("admin_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def admin_user_password(self) -> typing.Optional[builtins.str]:
        '''The password of the administrator for the primary database created in the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-adminuserpassword
        '''
        result = self._values.get("admin_user_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_name(self) -> typing.Optional[builtins.str]:
        '''The name of the primary database created in the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-dbname
        '''
        result = self._values.get("db_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM role to set as a default in the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-defaultiamrolearn
        '''
        result = self._values.get("default_iam_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def final_snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The name of the snapshot to be created before the namespace is deleted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-finalsnapshotname
        '''
        result = self._values.get("final_snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def final_snapshot_retention_period(self) -> typing.Optional[jsii.Number]:
        '''How long to retain the final snapshot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-finalsnapshotretentionperiod
        '''
        result = self._values.get("final_snapshot_retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def iam_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of IAM roles to associate with the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-iamroles
        '''
        result = self._values.get("iam_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS Key Management Service key used to encrypt your data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_exports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The types of logs the namespace can export.

        Available export types are ``userlog`` , ``connectionlog`` , and ``useractivitylog`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-logexports
        '''
        result = self._values.get("log_exports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def manage_admin_password(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''If true, Amazon Redshift uses AWS Secrets Manager to manage the namespace's admin credentials.

        You can't use ``AdminUserPassword`` if ``ManageAdminPassword`` is true. If ``ManageAdminPassword`` is ``false`` or not set, Amazon Redshift uses ``AdminUserPassword`` for the admin user account's password.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-manageadminpassword
        '''
        result = self._values.get("manage_admin_password")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def namespace_resource_policy(self) -> typing.Any:
        '''The resource policy that will be attached to the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-namespaceresourcepolicy
        '''
        result = self._values.get("namespace_resource_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def redshift_idc_application_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN for the Redshift application that integrates with IAM Identity Center.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-redshiftidcapplicationarn
        '''
        result = self._values.get("redshift_idc_application_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_copy_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnNamespace.SnapshotCopyConfigurationProperty]]]]:
        '''The snapshot copy configurations for the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-snapshotcopyconfigurations
        '''
        result = self._values.get("snapshot_copy_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnNamespace.SnapshotCopyConfigurationProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The map of the key-value pairs used to tag the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-namespace.html#cfn-redshiftserverless-namespace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnSnapshot(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnSnapshot",
):
    '''A snapshot object that contains databases.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-snapshot.html
    :cloudformationResource: AWS::RedshiftServerless::Snapshot
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshiftserverless as redshiftserverless
        
        cfn_snapshot = redshiftserverless.CfnSnapshot(self, "MyCfnSnapshot",
            snapshot_name="snapshotName",
        
            # the properties below are optional
            namespace_name="namespaceName",
            retention_period=123,
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
        snapshot_name: builtins.str,
        namespace_name: typing.Optional[builtins.str] = None,
        retention_period: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param snapshot_name: The name of the snapshot.
        :param namespace_name: The name of the namepsace.
        :param retention_period: The retention period of the snapshot created by the scheduled action.
        :param tags: An array of `Tag objects <https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html>`_ to associate with the snapshot.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1e2b5eeadcf14eaf0be75cda550b6bcef2aa009af0fe87d6f5e9e856ad0ef43)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSnapshotProps(
            snapshot_name=snapshot_name,
            namespace_name=namespace_name,
            retention_period=retention_period,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ddc470fc115016c807de39b9ff4325d249ff8657e32f92eefbcb4bac9e79eb0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4bdbe6940b32b0a05793c97cd18c6f2009d35937c086b1b342b276e310c97129)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerAccount")
    def attr_owner_account(self) -> builtins.str:
        '''The owner AWS ;

        account of the snapshot.

        :cloudformationAttribute: OwnerAccount
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerAccount"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshot")
    def attr_snapshot(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Snapshot
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrSnapshot"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotAdminUsername")
    def attr_snapshot_admin_username(self) -> builtins.str:
        '''The username of the database within a snapshot.

        :cloudformationAttribute: Snapshot.AdminUsername
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSnapshotAdminUsername"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotKmsKeyId")
    def attr_snapshot_kms_key_id(self) -> builtins.str:
        '''The unique identifier of the KMS key used to encrypt the snapshot.

        :cloudformationAttribute: Snapshot.KmsKeyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSnapshotKmsKeyId"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotNamespaceArn")
    def attr_snapshot_namespace_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the namespace the snapshot was created from.

        :cloudformationAttribute: Snapshot.NamespaceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSnapshotNamespaceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotNamespaceName")
    def attr_snapshot_namespace_name(self) -> builtins.str:
        '''The name of the namepsace.

        :cloudformationAttribute: Snapshot.NamespaceName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSnapshotNamespaceName"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotOwnerAccount")
    def attr_snapshot_owner_account(self) -> builtins.str:
        '''The owner AWS ;

        account of the snapshot.

        :cloudformationAttribute: Snapshot.OwnerAccount
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSnapshotOwnerAccount"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotRetentionPeriod")
    def attr_snapshot_retention_period(self) -> jsii.Number:
        '''The retention period of the snapshot created by the scheduled action.

        :cloudformationAttribute: Snapshot.RetentionPeriod
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrSnapshotRetentionPeriod"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotSnapshotArn")
    def attr_snapshot_snapshot_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the snapshot.

        :cloudformationAttribute: Snapshot.SnapshotArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSnapshotSnapshotArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotSnapshotCreateTime")
    def attr_snapshot_snapshot_create_time(self) -> builtins.str:
        '''The timestamp of when the snapshot was created.

        :cloudformationAttribute: Snapshot.SnapshotCreateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSnapshotSnapshotCreateTime"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotSnapshotName")
    def attr_snapshot_snapshot_name(self) -> builtins.str:
        '''The name of the snapshot.

        :cloudformationAttribute: Snapshot.SnapshotName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSnapshotSnapshotName"))

    @builtins.property
    @jsii.member(jsii_name="attrSnapshotStatus")
    def attr_snapshot_status(self) -> builtins.str:
        '''The status of the snapshot.

        :cloudformationAttribute: Snapshot.Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSnapshotStatus"))

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
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> builtins.str:
        '''The name of the snapshot.'''
        return typing.cast(builtins.str, jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f64f97556142b340a4fd0b74522c68b85e2157f2a27ece8203bd18185cfe3ce6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> typing.Optional[builtins.str]:
        '''The name of the namepsace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceName"))

    @namespace_name.setter
    def namespace_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f6a30dd9c5c0b8045b8d36ef14977ccb4361c843f7dcb8ac7322f8fa349468d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="retentionPeriod")
    def retention_period(self) -> typing.Optional[jsii.Number]:
        '''The retention period of the snapshot created by the scheduled action.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionPeriod"))

    @retention_period.setter
    def retention_period(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__521c1c8ca437327e56c1b9a24896fa19595912e045202fbf656a893304dd3c04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPeriod", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of `Tag objects <https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html>`_ to associate with the snapshot.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77534803a2fb41b5883d0c89334777e664cec59572dd7a376bbe5dbc41ff64ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnSnapshot.SnapshotProperty",
        jsii_struct_bases=[],
        name_mapping={
            "admin_username": "adminUsername",
            "kms_key_id": "kmsKeyId",
            "namespace_arn": "namespaceArn",
            "namespace_name": "namespaceName",
            "owner_account": "ownerAccount",
            "retention_period": "retentionPeriod",
            "snapshot_arn": "snapshotArn",
            "snapshot_create_time": "snapshotCreateTime",
            "snapshot_name": "snapshotName",
            "status": "status",
        },
    )
    class SnapshotProperty:
        def __init__(
            self,
            *,
            admin_username: typing.Optional[builtins.str] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
            namespace_arn: typing.Optional[builtins.str] = None,
            namespace_name: typing.Optional[builtins.str] = None,
            owner_account: typing.Optional[builtins.str] = None,
            retention_period: typing.Optional[jsii.Number] = None,
            snapshot_arn: typing.Optional[builtins.str] = None,
            snapshot_create_time: typing.Optional[builtins.str] = None,
            snapshot_name: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A snapshot object that contains databases.

            :param admin_username: The username of the database within a snapshot.
            :param kms_key_id: The unique identifier of the KMS key used to encrypt the snapshot.
            :param namespace_arn: The Amazon Resource Name (ARN) of the namespace the snapshot was created from.
            :param namespace_name: The name of the namepsace.
            :param owner_account: The owner AWS ; account of the snapshot.
            :param retention_period: The retention period of the snapshot created by the scheduled action.
            :param snapshot_arn: The Amazon Resource Name (ARN) of the snapshot.
            :param snapshot_create_time: The timestamp of when the snapshot was created.
            :param snapshot_name: The name of the snapshot.
            :param status: The status of the snapshot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-snapshot-snapshot.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                snapshot_property = redshiftserverless.CfnSnapshot.SnapshotProperty(
                    admin_username="adminUsername",
                    kms_key_id="kmsKeyId",
                    namespace_arn="namespaceArn",
                    namespace_name="namespaceName",
                    owner_account="ownerAccount",
                    retention_period=123,
                    snapshot_arn="snapshotArn",
                    snapshot_create_time="snapshotCreateTime",
                    snapshot_name="snapshotName",
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d32a77292254bff347197e3bdcc04e2fea309ebb7baea20e5fee3f5714159ffa)
                check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
                check_type(argname="argument namespace_arn", value=namespace_arn, expected_type=type_hints["namespace_arn"])
                check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
                check_type(argname="argument owner_account", value=owner_account, expected_type=type_hints["owner_account"])
                check_type(argname="argument retention_period", value=retention_period, expected_type=type_hints["retention_period"])
                check_type(argname="argument snapshot_arn", value=snapshot_arn, expected_type=type_hints["snapshot_arn"])
                check_type(argname="argument snapshot_create_time", value=snapshot_create_time, expected_type=type_hints["snapshot_create_time"])
                check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if admin_username is not None:
                self._values["admin_username"] = admin_username
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if namespace_arn is not None:
                self._values["namespace_arn"] = namespace_arn
            if namespace_name is not None:
                self._values["namespace_name"] = namespace_name
            if owner_account is not None:
                self._values["owner_account"] = owner_account
            if retention_period is not None:
                self._values["retention_period"] = retention_period
            if snapshot_arn is not None:
                self._values["snapshot_arn"] = snapshot_arn
            if snapshot_create_time is not None:
                self._values["snapshot_create_time"] = snapshot_create_time
            if snapshot_name is not None:
                self._values["snapshot_name"] = snapshot_name
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def admin_username(self) -> typing.Optional[builtins.str]:
            '''The username of the database within a snapshot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-snapshot-snapshot.html#cfn-redshiftserverless-snapshot-snapshot-adminusername
            '''
            result = self._values.get("admin_username")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of the KMS key used to encrypt the snapshot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-snapshot-snapshot.html#cfn-redshiftserverless-snapshot-snapshot-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespace_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the namespace the snapshot was created from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-snapshot-snapshot.html#cfn-redshiftserverless-snapshot-snapshot-namespacearn
            '''
            result = self._values.get("namespace_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespace_name(self) -> typing.Optional[builtins.str]:
            '''The name of the namepsace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-snapshot-snapshot.html#cfn-redshiftserverless-snapshot-snapshot-namespacename
            '''
            result = self._values.get("namespace_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def owner_account(self) -> typing.Optional[builtins.str]:
            '''The owner AWS ;

            account of the snapshot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-snapshot-snapshot.html#cfn-redshiftserverless-snapshot-snapshot-owneraccount
            '''
            result = self._values.get("owner_account")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def retention_period(self) -> typing.Optional[jsii.Number]:
            '''The retention period of the snapshot created by the scheduled action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-snapshot-snapshot.html#cfn-redshiftserverless-snapshot-snapshot-retentionperiod
            '''
            result = self._values.get("retention_period")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def snapshot_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the snapshot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-snapshot-snapshot.html#cfn-redshiftserverless-snapshot-snapshot-snapshotarn
            '''
            result = self._values.get("snapshot_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def snapshot_create_time(self) -> typing.Optional[builtins.str]:
            '''The timestamp of when the snapshot was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-snapshot-snapshot.html#cfn-redshiftserverless-snapshot-snapshot-snapshotcreatetime
            '''
            result = self._values.get("snapshot_create_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def snapshot_name(self) -> typing.Optional[builtins.str]:
            '''The name of the snapshot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-snapshot-snapshot.html#cfn-redshiftserverless-snapshot-snapshot-snapshotname
            '''
            result = self._values.get("snapshot_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the snapshot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-snapshot-snapshot.html#cfn-redshiftserverless-snapshot-snapshot-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnapshotProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnSnapshotProps",
    jsii_struct_bases=[],
    name_mapping={
        "snapshot_name": "snapshotName",
        "namespace_name": "namespaceName",
        "retention_period": "retentionPeriod",
        "tags": "tags",
    },
)
class CfnSnapshotProps:
    def __init__(
        self,
        *,
        snapshot_name: builtins.str,
        namespace_name: typing.Optional[builtins.str] = None,
        retention_period: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSnapshot``.

        :param snapshot_name: The name of the snapshot.
        :param namespace_name: The name of the namepsace.
        :param retention_period: The retention period of the snapshot created by the scheduled action.
        :param tags: An array of `Tag objects <https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html>`_ to associate with the snapshot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-snapshot.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshiftserverless as redshiftserverless
            
            cfn_snapshot_props = redshiftserverless.CfnSnapshotProps(
                snapshot_name="snapshotName",
            
                # the properties below are optional
                namespace_name="namespaceName",
                retention_period=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38cd0d09fc150d83197b13fb0e10ea82ffa589e88452cdfecbd53994ae2ced5b)
            check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
            check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
            check_type(argname="argument retention_period", value=retention_period, expected_type=type_hints["retention_period"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "snapshot_name": snapshot_name,
        }
        if namespace_name is not None:
            self._values["namespace_name"] = namespace_name
        if retention_period is not None:
            self._values["retention_period"] = retention_period
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def snapshot_name(self) -> builtins.str:
        '''The name of the snapshot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-snapshot.html#cfn-redshiftserverless-snapshot-snapshotname
        '''
        result = self._values.get("snapshot_name")
        assert result is not None, "Required property 'snapshot_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace_name(self) -> typing.Optional[builtins.str]:
        '''The name of the namepsace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-snapshot.html#cfn-redshiftserverless-snapshot-namespacename
        '''
        result = self._values.get("namespace_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retention_period(self) -> typing.Optional[jsii.Number]:
        '''The retention period of the snapshot created by the scheduled action.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-snapshot.html#cfn-redshiftserverless-snapshot-retentionperiod
        '''
        result = self._values.get("retention_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of `Tag objects <https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Tag.html>`_ to associate with the snapshot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-snapshot.html#cfn-redshiftserverless-snapshot-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSnapshotProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnWorkgroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroup",
):
    '''The collection of compute resources in Amazon Redshift Serverless.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html
    :cloudformationResource: AWS::RedshiftServerless::Workgroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_redshiftserverless as redshiftserverless
        
        cfn_workgroup = redshiftserverless.CfnWorkgroup(self, "MyCfnWorkgroup",
            workgroup_name="workgroupName",
        
            # the properties below are optional
            base_capacity=123,
            config_parameters=[redshiftserverless.CfnWorkgroup.ConfigParameterProperty(
                parameter_key="parameterKey",
                parameter_value="parameterValue"
            )],
            enhanced_vpc_routing=False,
            max_capacity=123,
            namespace_name="namespaceName",
            port=123,
            price_performance_target=redshiftserverless.CfnWorkgroup.PerformanceTargetProperty(
                level=123,
                status="status"
            ),
            publicly_accessible=False,
            recovery_point_id="recoveryPointId",
            security_group_ids=["securityGroupIds"],
            snapshot_arn="snapshotArn",
            snapshot_name="snapshotName",
            snapshot_owner_account="snapshotOwnerAccount",
            subnet_ids=["subnetIds"],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            track_name="trackName",
            workgroup=redshiftserverless.CfnWorkgroup.WorkgroupProperty(
                base_capacity=123,
                config_parameters=[redshiftserverless.CfnWorkgroup.ConfigParameterProperty(
                    parameter_key="parameterKey",
                    parameter_value="parameterValue"
                )],
                creation_date="creationDate",
                endpoint=redshiftserverless.CfnWorkgroup.EndpointProperty(
                    address="address",
                    port=123,
                    vpc_endpoints=[redshiftserverless.CfnWorkgroup.VpcEndpointProperty(
                        network_interfaces=[redshiftserverless.CfnWorkgroup.NetworkInterfaceProperty(
                            availability_zone="availabilityZone",
                            network_interface_id="networkInterfaceId",
                            private_ip_address="privateIpAddress",
                            subnet_id="subnetId"
                        )],
                        vpc_endpoint_id="vpcEndpointId",
                        vpc_id="vpcId"
                    )]
                ),
                enhanced_vpc_routing=False,
                max_capacity=123,
                namespace_name="namespaceName",
                price_performance_target=redshiftserverless.CfnWorkgroup.PerformanceTargetProperty(
                    level=123,
                    status="status"
                ),
                publicly_accessible=False,
                security_group_ids=["securityGroupIds"],
                status="status",
                subnet_ids=["subnetIds"],
                track_name="trackName",
                workgroup_arn="workgroupArn",
                workgroup_id="workgroupId",
                workgroup_name="workgroupName"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        workgroup_name: builtins.str,
        base_capacity: typing.Optional[jsii.Number] = None,
        config_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkgroup.ConfigParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        namespace_name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        price_performance_target: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkgroup.PerformanceTargetProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        recovery_point_id: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_arn: typing.Optional[builtins.str] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        snapshot_owner_account: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        track_name: typing.Optional[builtins.str] = None,
        workgroup: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkgroup.WorkgroupProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param workgroup_name: The name of the workgroup.
        :param base_capacity: The base compute capacity of the workgroup in Redshift Processing Units (RPUs).
        :param config_parameters: The key of the parameter. The options are ``auto_mv`` , ``datestyle`` , ``enable_case_sensitive_identifier`` , ``enable_user_activity_logging`` , ``query_group`` , ``search_path`` , ``require_ssl`` , ``use_fips_ssl`` , and query monitoring metrics that let you define performance boundaries. For more information about query monitoring rules and available metrics, see `Query monitoring metrics for Amazon Redshift Serverless <https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless>`_ .
        :param enhanced_vpc_routing: The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC. Default: - false
        :param max_capacity: The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.
        :param namespace_name: The namespace the workgroup is associated with.
        :param port: The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.
        :param price_performance_target: An object that represents the price performance target settings for the workgroup.
        :param publicly_accessible: A value that specifies whether the workgroup can be accessible from a public network. Default: - false
        :param recovery_point_id: The recovery point id to restore from.
        :param security_group_ids: A list of security group IDs to associate with the workgroup.
        :param snapshot_arn: The Amazon Resource Name (ARN) of the snapshot to restore from.
        :param snapshot_name: The snapshot name to restore from.
        :param snapshot_owner_account: The Amazon Web Services account that owns the snapshot.
        :param subnet_ids: A list of subnet IDs the workgroup is associated with.
        :param tags: The map of the key-value pairs used to tag the workgroup.
        :param track_name: An optional parameter for the name of the track for the workgroup. If you don't provide a track name, the workgroup is assigned to the current track.
        :param workgroup: The collection of computing resources from which an endpoint is created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61a1b6ebbdacc577619f4e17ddabdaa553ffe5fe072b72e14ddf7d9c3f7e1a04)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkgroupProps(
            workgroup_name=workgroup_name,
            base_capacity=base_capacity,
            config_parameters=config_parameters,
            enhanced_vpc_routing=enhanced_vpc_routing,
            max_capacity=max_capacity,
            namespace_name=namespace_name,
            port=port,
            price_performance_target=price_performance_target,
            publicly_accessible=publicly_accessible,
            recovery_point_id=recovery_point_id,
            security_group_ids=security_group_ids,
            snapshot_arn=snapshot_arn,
            snapshot_name=snapshot_name,
            snapshot_owner_account=snapshot_owner_account,
            subnet_ids=subnet_ids,
            tags=tags,
            track_name=track_name,
            workgroup=workgroup,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__986feaaa3c97c38d5a5c4414a977741007338bd588a8ebc981d89e63b28c9c38)
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
            type_hints = typing.get_type_hints(_typecheckingstub__575b09c3449f3d47af302b94ec8c88b82387f8f428024e134c076d5600122345)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroup")
    def attr_workgroup(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Workgroup
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrWorkgroup"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupBaseCapacity")
    def attr_workgroup_base_capacity(self) -> jsii.Number:
        '''The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).

        :cloudformationAttribute: Workgroup.BaseCapacity
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrWorkgroupBaseCapacity"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupConfigParameters")
    def attr_workgroup_config_parameters(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Workgroup.ConfigParameters
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrWorkgroupConfigParameters"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupCreationDate")
    def attr_workgroup_creation_date(self) -> builtins.str:
        '''The creation date of the workgroup.

        :cloudformationAttribute: Workgroup.CreationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkgroupCreationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupEndpoint")
    def attr_workgroup_endpoint(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Workgroup.Endpoint
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrWorkgroupEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupEndpointAddress")
    def attr_workgroup_endpoint_address(self) -> builtins.str:
        '''The DNS address of the VPC endpoint.

        :cloudformationAttribute: Workgroup.Endpoint.Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkgroupEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupEndpointPort")
    def attr_workgroup_endpoint_port(self) -> jsii.Number:
        '''The custom port to use when connecting to a workgroup.

        Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.

        :cloudformationAttribute: Workgroup.Endpoint.Port
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrWorkgroupEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupEndpointVpcEndpoints")
    def attr_workgroup_endpoint_vpc_endpoints(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Workgroup.Endpoint.VpcEndpoints
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrWorkgroupEndpointVpcEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupEnhancedVpcRouting")
    def attr_workgroup_enhanced_vpc_routing(self) -> _IResolvable_da3f097b:
        '''The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.

        :cloudformationAttribute: Workgroup.EnhancedVpcRouting
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrWorkgroupEnhancedVpcRouting"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupMaxCapacity")
    def attr_workgroup_max_capacity(self) -> jsii.Number:
        '''The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries.

        The max capacity is specified in RPUs.

        :cloudformationAttribute: Workgroup.MaxCapacity
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrWorkgroupMaxCapacity"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupNamespaceName")
    def attr_workgroup_namespace_name(self) -> builtins.str:
        '''The namespace the workgroup is associated with.

        :cloudformationAttribute: Workgroup.NamespaceName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkgroupNamespaceName"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupPubliclyAccessible")
    def attr_workgroup_publicly_accessible(self) -> _IResolvable_da3f097b:
        '''A value that specifies whether the workgroup can be accessible from a public network.

        :cloudformationAttribute: Workgroup.PubliclyAccessible
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrWorkgroupPubliclyAccessible"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupSecurityGroupIds")
    def attr_workgroup_security_group_ids(self) -> typing.List[builtins.str]:
        '''An array of security group IDs to associate with the workgroup.

        :cloudformationAttribute: Workgroup.SecurityGroupIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrWorkgroupSecurityGroupIds"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupStatus")
    def attr_workgroup_status(self) -> builtins.str:
        '''The status of the workgroup.

        :cloudformationAttribute: Workgroup.Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkgroupStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupSubnetIds")
    def attr_workgroup_subnet_ids(self) -> typing.List[builtins.str]:
        '''An array of subnet IDs the workgroup is associated with.

        :cloudformationAttribute: Workgroup.SubnetIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrWorkgroupSubnetIds"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupTrackName")
    def attr_workgroup_track_name(self) -> builtins.str:
        '''The name of the track for the workgroup.

        :cloudformationAttribute: Workgroup.TrackName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkgroupTrackName"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupWorkgroupArn")
    def attr_workgroup_workgroup_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) that links to the workgroup.

        :cloudformationAttribute: Workgroup.WorkgroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkgroupWorkgroupArn"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupWorkgroupId")
    def attr_workgroup_workgroup_id(self) -> builtins.str:
        '''The unique identifier of the workgroup.

        :cloudformationAttribute: Workgroup.WorkgroupId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkgroupWorkgroupId"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkgroupWorkgroupName")
    def attr_workgroup_workgroup_name(self) -> builtins.str:
        '''The name of the workgroup.

        :cloudformationAttribute: Workgroup.WorkgroupName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkgroupWorkgroupName"))

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
    @jsii.member(jsii_name="workgroupName")
    def workgroup_name(self) -> builtins.str:
        '''The name of the workgroup.'''
        return typing.cast(builtins.str, jsii.get(self, "workgroupName"))

    @workgroup_name.setter
    def workgroup_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44b001bba04c1f96a7169e528d056ccd8d9035fee30af63b1f339873bf7e3ea7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workgroupName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="baseCapacity")
    def base_capacity(self) -> typing.Optional[jsii.Number]:
        '''The base compute capacity of the workgroup in Redshift Processing Units (RPUs).'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "baseCapacity"))

    @base_capacity.setter
    def base_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d35b55423f49c0c42ee449a11852238ff7a68ae5e2e78f2da58bcb94c221a85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseCapacity", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="configParameters")
    def config_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.ConfigParameterProperty"]]]]:
        '''The key of the parameter.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.ConfigParameterProperty"]]]], jsii.get(self, "configParameters"))

    @config_parameters.setter
    def config_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.ConfigParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00339df2c3d04a43ab10d867748f8678b0423745badc0e14afa8bb128d473607)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configParameters", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enhancedVpcRouting")
    def enhanced_vpc_routing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enhancedVpcRouting"))

    @enhanced_vpc_routing.setter
    def enhanced_vpc_routing(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b06db2b227debd7cc917f51bf7c4c0bb700bca075b329af61a43f37521feba71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enhancedVpcRouting", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCapacity"))

    @max_capacity.setter
    def max_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ceab2fa028856954a409378fab7e1382a9cf79f0bf83fa7f082c0d6996e02e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCapacity", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> typing.Optional[builtins.str]:
        '''The namespace the workgroup is associated with.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceName"))

    @namespace_name.setter
    def namespace_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a009fb86999f55de110193d15ea127b35ea379a1d840ddd42a0406b02f3a997a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''The custom port to use when connecting to a workgroup.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e3a61acfcbbe3b107c15ebd1c1248f3bd150ad58cf876908da7870de9fd6fde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="pricePerformanceTarget")
    def price_performance_target(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.PerformanceTargetProperty"]]:
        '''An object that represents the price performance target settings for the workgroup.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.PerformanceTargetProperty"]], jsii.get(self, "pricePerformanceTarget"))

    @price_performance_target.setter
    def price_performance_target(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.PerformanceTargetProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__971a4fc1559ba6fa762249206f240d83ab3e607f325e8eeed9b9122b529c78e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pricePerformanceTarget", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A value that specifies whether the workgroup can be accessible from a public network.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__974542b0d8aa6c1847dd536dcf795ef2c4719aed798ea365b0767f6ad3234ca0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAccessible", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="recoveryPointId")
    def recovery_point_id(self) -> typing.Optional[builtins.str]:
        '''The recovery point id to restore from.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryPointId"))

    @recovery_point_id.setter
    def recovery_point_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__330f25021814c2fb98578117b6d4b45cb103383dd78a1ec221ad5ee1da1af776)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryPointId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group IDs to associate with the workgroup.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2864d0fac41ac305963b5532a731665cbc0d93a810a41ea2d2fe98a5285e8aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="snapshotArn")
    def snapshot_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the snapshot to restore from.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotArn"))

    @snapshot_arn.setter
    def snapshot_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22c9552850e931e5526d6b100685f6e372509370d50247f9134b09b667c31905)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="snapshotName")
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The snapshot name to restore from.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotName"))

    @snapshot_name.setter
    def snapshot_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9001e412e7a006803ae5b51d6b1ec1486aa95db2939acfaa5b88a397dfaf1e7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="snapshotOwnerAccount")
    def snapshot_owner_account(self) -> typing.Optional[builtins.str]:
        '''The Amazon Web Services account that owns the snapshot.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotOwnerAccount"))

    @snapshot_owner_account.setter
    def snapshot_owner_account(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e20f0edef13cea8274ed0af3c59774d9e6b1dc49c1c6cd25ad2a5807f42500fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotOwnerAccount", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of subnet IDs the workgroup is associated with.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67e139cef151f144f2bb04082850da469be0ab0515cff591edf9fc1e44df78a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The map of the key-value pairs used to tag the workgroup.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3104c5d5a81618ce7738aabf06bbd67fea6c82cd5abea01e1b03c71c5065efc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="trackName")
    def track_name(self) -> typing.Optional[builtins.str]:
        '''An optional parameter for the name of the track for the workgroup.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trackName"))

    @track_name.setter
    def track_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ae0d98fb213b87bdf0bef05c29f3608e64d5cab8c142baeef1f930bb88523bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trackName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="workgroup")
    def workgroup(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.WorkgroupProperty"]]:
        '''The collection of computing resources from which an endpoint is created.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.WorkgroupProperty"]], jsii.get(self, "workgroup"))

    @workgroup.setter
    def workgroup(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.WorkgroupProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb73897901d98002fc8e5d2e00c5ffffec6d6ffc0d70be41b21317bd200b87a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workgroup", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroup.ConfigParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_key": "parameterKey",
            "parameter_value": "parameterValue",
        },
    )
    class ConfigParameterProperty:
        def __init__(
            self,
            *,
            parameter_key: typing.Optional[builtins.str] = None,
            parameter_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A array of parameters to set for more control over a serverless database.

            :param parameter_key: The key of the parameter. The options are ``auto_mv`` , ``datestyle`` , ``enable_case_sensitive_identifier`` , ``enable_user_activity_logging`` , ``query_group`` , ``search_path`` , ``require_ssl`` , ``use_fips_ssl`` , and query monitoring metrics that let you define performance boundaries. For more information about query monitoring rules and available metrics, see `Query monitoring metrics for Amazon Redshift Serverless <https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless>`_ .
            :param parameter_value: The value of the parameter to set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-configparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                config_parameter_property = redshiftserverless.CfnWorkgroup.ConfigParameterProperty(
                    parameter_key="parameterKey",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__322e3a40a90a7ebca9e3ef09024360dddede638badc33eeda64eccd556f3dc5f)
                check_type(argname="argument parameter_key", value=parameter_key, expected_type=type_hints["parameter_key"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if parameter_key is not None:
                self._values["parameter_key"] = parameter_key
            if parameter_value is not None:
                self._values["parameter_value"] = parameter_value

        @builtins.property
        def parameter_key(self) -> typing.Optional[builtins.str]:
            '''The key of the parameter.

            The options are ``auto_mv`` , ``datestyle`` , ``enable_case_sensitive_identifier`` , ``enable_user_activity_logging`` , ``query_group`` , ``search_path`` , ``require_ssl`` , ``use_fips_ssl`` , and query monitoring metrics that let you define performance boundaries. For more information about query monitoring rules and available metrics, see `Query monitoring metrics for Amazon Redshift Serverless <https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-configparameter.html#cfn-redshiftserverless-workgroup-configparameter-parameterkey
            '''
            result = self._values.get("parameter_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameter_value(self) -> typing.Optional[builtins.str]:
            '''The value of the parameter to set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-configparameter.html#cfn-redshiftserverless-workgroup-configparameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroup.EndpointProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address": "address",
            "port": "port",
            "vpc_endpoints": "vpcEndpoints",
        },
    )
    class EndpointProperty:
        def __init__(
            self,
            *,
            address: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
            vpc_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkgroup.VpcEndpointProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The VPC endpoint object.

            :param address: The DNS address of the VPC endpoint.
            :param port: The port that Amazon Redshift Serverless listens on.
            :param vpc_endpoints: An array of ``VpcEndpoint`` objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-endpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                endpoint_property = redshiftserverless.CfnWorkgroup.EndpointProperty(
                    address="address",
                    port=123,
                    vpc_endpoints=[redshiftserverless.CfnWorkgroup.VpcEndpointProperty(
                        network_interfaces=[redshiftserverless.CfnWorkgroup.NetworkInterfaceProperty(
                            availability_zone="availabilityZone",
                            network_interface_id="networkInterfaceId",
                            private_ip_address="privateIpAddress",
                            subnet_id="subnetId"
                        )],
                        vpc_endpoint_id="vpcEndpointId",
                        vpc_id="vpcId"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1064dbbc6e1afc7fbd36b9ac721b89fc24382d0930f8f41542644b48bc6c07bf)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument vpc_endpoints", value=vpc_endpoints, expected_type=type_hints["vpc_endpoints"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address
            if port is not None:
                self._values["port"] = port
            if vpc_endpoints is not None:
                self._values["vpc_endpoints"] = vpc_endpoints

        @builtins.property
        def address(self) -> typing.Optional[builtins.str]:
            '''The DNS address of the VPC endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-endpoint.html#cfn-redshiftserverless-workgroup-endpoint-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''The port that Amazon Redshift Serverless listens on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-endpoint.html#cfn-redshiftserverless-workgroup-endpoint-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def vpc_endpoints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.VpcEndpointProperty"]]]]:
            '''An array of ``VpcEndpoint`` objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-endpoint.html#cfn-redshiftserverless-workgroup-endpoint-vpcendpoints
            '''
            result = self._values.get("vpc_endpoints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.VpcEndpointProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroup.NetworkInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "availability_zone": "availabilityZone",
            "network_interface_id": "networkInterfaceId",
            "private_ip_address": "privateIpAddress",
            "subnet_id": "subnetId",
        },
    )
    class NetworkInterfaceProperty:
        def __init__(
            self,
            *,
            availability_zone: typing.Optional[builtins.str] = None,
            network_interface_id: typing.Optional[builtins.str] = None,
            private_ip_address: typing.Optional[builtins.str] = None,
            subnet_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about a network interface in an Amazon Redshift Serverless managed VPC endpoint.

            :param availability_zone: The availability Zone.
            :param network_interface_id: The unique identifier of the network interface.
            :param private_ip_address: The IPv4 address of the network interface within the subnet.
            :param subnet_id: The unique identifier of the subnet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                network_interface_property = redshiftserverless.CfnWorkgroup.NetworkInterfaceProperty(
                    availability_zone="availabilityZone",
                    network_interface_id="networkInterfaceId",
                    private_ip_address="privateIpAddress",
                    subnet_id="subnetId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c27a8032aaa250691e1e68b2e75ce65c47142ac6b83ad22f01b09ec293f841b8)
                check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
                check_type(argname="argument network_interface_id", value=network_interface_id, expected_type=type_hints["network_interface_id"])
                check_type(argname="argument private_ip_address", value=private_ip_address, expected_type=type_hints["private_ip_address"])
                check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if availability_zone is not None:
                self._values["availability_zone"] = availability_zone
            if network_interface_id is not None:
                self._values["network_interface_id"] = network_interface_id
            if private_ip_address is not None:
                self._values["private_ip_address"] = private_ip_address
            if subnet_id is not None:
                self._values["subnet_id"] = subnet_id

        @builtins.property
        def availability_zone(self) -> typing.Optional[builtins.str]:
            '''The availability Zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html#cfn-redshiftserverless-workgroup-networkinterface-availabilityzone
            '''
            result = self._values.get("availability_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def network_interface_id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of the network interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html#cfn-redshiftserverless-workgroup-networkinterface-networkinterfaceid
            '''
            result = self._values.get("network_interface_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def private_ip_address(self) -> typing.Optional[builtins.str]:
            '''The IPv4 address of the network interface within the subnet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html#cfn-redshiftserverless-workgroup-networkinterface-privateipaddress
            '''
            result = self._values.get("private_ip_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subnet_id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of the subnet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-networkinterface.html#cfn-redshiftserverless-workgroup-networkinterface-subnetid
            '''
            result = self._values.get("subnet_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroup.PerformanceTargetProperty",
        jsii_struct_bases=[],
        name_mapping={"level": "level", "status": "status"},
    )
    class PerformanceTargetProperty:
        def __init__(
            self,
            *,
            level: typing.Optional[jsii.Number] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that represents the price performance target settings for the workgroup.

            :param level: The target price performance level for the workgroup. Valid values include 1, 25, 50, 75, and 100. These correspond to the price performance levels LOW_COST, ECONOMICAL, BALANCED, RESOURCEFUL, and HIGH_PERFORMANCE.
            :param status: Whether the price performance target is enabled for the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-performancetarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                performance_target_property = redshiftserverless.CfnWorkgroup.PerformanceTargetProperty(
                    level=123,
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e7166282347ab806de45e7f23d02833af860bdd81c72c593cfef563b261c272f)
                check_type(argname="argument level", value=level, expected_type=type_hints["level"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if level is not None:
                self._values["level"] = level
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def level(self) -> typing.Optional[jsii.Number]:
            '''The target price performance level for the workgroup.

            Valid values include 1, 25, 50, 75, and 100. These correspond to the price performance levels LOW_COST, ECONOMICAL, BALANCED, RESOURCEFUL, and HIGH_PERFORMANCE.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-performancetarget.html#cfn-redshiftserverless-workgroup-performancetarget-level
            '''
            result = self._values.get("level")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''Whether the price performance target is enabled for the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-performancetarget.html#cfn-redshiftserverless-workgroup-performancetarget-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PerformanceTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroup.VpcEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={
            "network_interfaces": "networkInterfaces",
            "vpc_endpoint_id": "vpcEndpointId",
            "vpc_id": "vpcId",
        },
    )
    class VpcEndpointProperty:
        def __init__(
            self,
            *,
            network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkgroup.NetworkInterfaceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            vpc_endpoint_id: typing.Optional[builtins.str] = None,
            vpc_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The connection endpoint for connecting to Amazon Redshift Serverless through the proxy.

            :param network_interfaces: One or more network interfaces of the endpoint. Also known as an interface endpoint.
            :param vpc_endpoint_id: The connection endpoint ID for connecting to Amazon Redshift Serverless.
            :param vpc_id: The VPC identifier that the endpoint is associated with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-vpcendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                vpc_endpoint_property = redshiftserverless.CfnWorkgroup.VpcEndpointProperty(
                    network_interfaces=[redshiftserverless.CfnWorkgroup.NetworkInterfaceProperty(
                        availability_zone="availabilityZone",
                        network_interface_id="networkInterfaceId",
                        private_ip_address="privateIpAddress",
                        subnet_id="subnetId"
                    )],
                    vpc_endpoint_id="vpcEndpointId",
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__200b427a09281b666ef25deaac2b6bf3abeeda64d77ffa3f7903dbe300b6606d)
                check_type(argname="argument network_interfaces", value=network_interfaces, expected_type=type_hints["network_interfaces"])
                check_type(argname="argument vpc_endpoint_id", value=vpc_endpoint_id, expected_type=type_hints["vpc_endpoint_id"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if network_interfaces is not None:
                self._values["network_interfaces"] = network_interfaces
            if vpc_endpoint_id is not None:
                self._values["vpc_endpoint_id"] = vpc_endpoint_id
            if vpc_id is not None:
                self._values["vpc_id"] = vpc_id

        @builtins.property
        def network_interfaces(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.NetworkInterfaceProperty"]]]]:
            '''One or more network interfaces of the endpoint.

            Also known as an interface endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-vpcendpoint.html#cfn-redshiftserverless-workgroup-vpcendpoint-networkinterfaces
            '''
            result = self._values.get("network_interfaces")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.NetworkInterfaceProperty"]]]], result)

        @builtins.property
        def vpc_endpoint_id(self) -> typing.Optional[builtins.str]:
            '''The connection endpoint ID for connecting to Amazon Redshift Serverless.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-vpcendpoint.html#cfn-redshiftserverless-workgroup-vpcendpoint-vpcendpointid
            '''
            result = self._values.get("vpc_endpoint_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> typing.Optional[builtins.str]:
            '''The VPC identifier that the endpoint is associated with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-vpcendpoint.html#cfn-redshiftserverless-workgroup-vpcendpoint-vpcid
            '''
            result = self._values.get("vpc_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroup.WorkgroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "base_capacity": "baseCapacity",
            "config_parameters": "configParameters",
            "creation_date": "creationDate",
            "endpoint": "endpoint",
            "enhanced_vpc_routing": "enhancedVpcRouting",
            "max_capacity": "maxCapacity",
            "namespace_name": "namespaceName",
            "price_performance_target": "pricePerformanceTarget",
            "publicly_accessible": "publiclyAccessible",
            "security_group_ids": "securityGroupIds",
            "status": "status",
            "subnet_ids": "subnetIds",
            "track_name": "trackName",
            "workgroup_arn": "workgroupArn",
            "workgroup_id": "workgroupId",
            "workgroup_name": "workgroupName",
        },
    )
    class WorkgroupProperty:
        def __init__(
            self,
            *,
            base_capacity: typing.Optional[jsii.Number] = None,
            config_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkgroup.ConfigParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            creation_date: typing.Optional[builtins.str] = None,
            endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkgroup.EndpointProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            max_capacity: typing.Optional[jsii.Number] = None,
            namespace_name: typing.Optional[builtins.str] = None,
            price_performance_target: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkgroup.PerformanceTargetProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            status: typing.Optional[builtins.str] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            track_name: typing.Optional[builtins.str] = None,
            workgroup_arn: typing.Optional[builtins.str] = None,
            workgroup_id: typing.Optional[builtins.str] = None,
            workgroup_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The collection of computing resources from which an endpoint is created.

            :param base_capacity: The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).
            :param config_parameters: An array of parameters to set for advanced control over a database. The options are ``auto_mv`` , ``datestyle`` , ``enable_case_sensitive_identifier`` , ``enable_user_activity_logging`` , ``query_group`` , ``search_path`` , ``require_ssl`` , ``use_fips_ssl`` , and query monitoring metrics that let you define performance boundaries. For more information about query monitoring rules and available metrics, see `Query monitoring metrics for Amazon Redshift Serverless <https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless>`_ .
            :param creation_date: The creation date of the workgroup.
            :param endpoint: The endpoint that is created from the workgroup.
            :param enhanced_vpc_routing: The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.
            :param max_capacity: The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.
            :param namespace_name: The namespace the workgroup is associated with.
            :param price_performance_target: An object that represents the price performance target settings for the workgroup.
            :param publicly_accessible: A value that specifies whether the workgroup can be accessible from a public network.
            :param security_group_ids: An array of security group IDs to associate with the workgroup.
            :param status: The status of the workgroup.
            :param subnet_ids: An array of subnet IDs the workgroup is associated with.
            :param track_name: The name of the track for the workgroup.
            :param workgroup_arn: The Amazon Resource Name (ARN) that links to the workgroup.
            :param workgroup_id: The unique identifier of the workgroup.
            :param workgroup_name: The name of the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_redshiftserverless as redshiftserverless
                
                workgroup_property = redshiftserverless.CfnWorkgroup.WorkgroupProperty(
                    base_capacity=123,
                    config_parameters=[redshiftserverless.CfnWorkgroup.ConfigParameterProperty(
                        parameter_key="parameterKey",
                        parameter_value="parameterValue"
                    )],
                    creation_date="creationDate",
                    endpoint=redshiftserverless.CfnWorkgroup.EndpointProperty(
                        address="address",
                        port=123,
                        vpc_endpoints=[redshiftserverless.CfnWorkgroup.VpcEndpointProperty(
                            network_interfaces=[redshiftserverless.CfnWorkgroup.NetworkInterfaceProperty(
                                availability_zone="availabilityZone",
                                network_interface_id="networkInterfaceId",
                                private_ip_address="privateIpAddress",
                                subnet_id="subnetId"
                            )],
                            vpc_endpoint_id="vpcEndpointId",
                            vpc_id="vpcId"
                        )]
                    ),
                    enhanced_vpc_routing=False,
                    max_capacity=123,
                    namespace_name="namespaceName",
                    price_performance_target=redshiftserverless.CfnWorkgroup.PerformanceTargetProperty(
                        level=123,
                        status="status"
                    ),
                    publicly_accessible=False,
                    security_group_ids=["securityGroupIds"],
                    status="status",
                    subnet_ids=["subnetIds"],
                    track_name="trackName",
                    workgroup_arn="workgroupArn",
                    workgroup_id="workgroupId",
                    workgroup_name="workgroupName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b7cad236eecd67272da075e88f17a1dbdae4ee5083553d6443dcc19b3a333780)
                check_type(argname="argument base_capacity", value=base_capacity, expected_type=type_hints["base_capacity"])
                check_type(argname="argument config_parameters", value=config_parameters, expected_type=type_hints["config_parameters"])
                check_type(argname="argument creation_date", value=creation_date, expected_type=type_hints["creation_date"])
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument enhanced_vpc_routing", value=enhanced_vpc_routing, expected_type=type_hints["enhanced_vpc_routing"])
                check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
                check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
                check_type(argname="argument price_performance_target", value=price_performance_target, expected_type=type_hints["price_performance_target"])
                check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument track_name", value=track_name, expected_type=type_hints["track_name"])
                check_type(argname="argument workgroup_arn", value=workgroup_arn, expected_type=type_hints["workgroup_arn"])
                check_type(argname="argument workgroup_id", value=workgroup_id, expected_type=type_hints["workgroup_id"])
                check_type(argname="argument workgroup_name", value=workgroup_name, expected_type=type_hints["workgroup_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if base_capacity is not None:
                self._values["base_capacity"] = base_capacity
            if config_parameters is not None:
                self._values["config_parameters"] = config_parameters
            if creation_date is not None:
                self._values["creation_date"] = creation_date
            if endpoint is not None:
                self._values["endpoint"] = endpoint
            if enhanced_vpc_routing is not None:
                self._values["enhanced_vpc_routing"] = enhanced_vpc_routing
            if max_capacity is not None:
                self._values["max_capacity"] = max_capacity
            if namespace_name is not None:
                self._values["namespace_name"] = namespace_name
            if price_performance_target is not None:
                self._values["price_performance_target"] = price_performance_target
            if publicly_accessible is not None:
                self._values["publicly_accessible"] = publicly_accessible
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if status is not None:
                self._values["status"] = status
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids
            if track_name is not None:
                self._values["track_name"] = track_name
            if workgroup_arn is not None:
                self._values["workgroup_arn"] = workgroup_arn
            if workgroup_id is not None:
                self._values["workgroup_id"] = workgroup_id
            if workgroup_name is not None:
                self._values["workgroup_name"] = workgroup_name

        @builtins.property
        def base_capacity(self) -> typing.Optional[jsii.Number]:
            '''The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-basecapacity
            '''
            result = self._values.get("base_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def config_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.ConfigParameterProperty"]]]]:
            '''An array of parameters to set for advanced control over a database.

            The options are ``auto_mv`` , ``datestyle`` , ``enable_case_sensitive_identifier`` , ``enable_user_activity_logging`` , ``query_group`` , ``search_path`` , ``require_ssl`` , ``use_fips_ssl`` , and query monitoring metrics that let you define performance boundaries. For more information about query monitoring rules and available metrics, see `Query monitoring metrics for Amazon Redshift Serverless <https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-configparameters
            '''
            result = self._values.get("config_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.ConfigParameterProperty"]]]], result)

        @builtins.property
        def creation_date(self) -> typing.Optional[builtins.str]:
            '''The creation date of the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-creationdate
            '''
            result = self._values.get("creation_date")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def endpoint(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.EndpointProperty"]]:
            '''The endpoint that is created from the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-endpoint
            '''
            result = self._values.get("endpoint")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.EndpointProperty"]], result)

        @builtins.property
        def enhanced_vpc_routing(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-enhancedvpcrouting
            '''
            result = self._values.get("enhanced_vpc_routing")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def max_capacity(self) -> typing.Optional[jsii.Number]:
            '''The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries.

            The max capacity is specified in RPUs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-maxcapacity
            '''
            result = self._values.get("max_capacity")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def namespace_name(self) -> typing.Optional[builtins.str]:
            '''The namespace the workgroup is associated with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-namespacename
            '''
            result = self._values.get("namespace_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def price_performance_target(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.PerformanceTargetProperty"]]:
            '''An object that represents the price performance target settings for the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-priceperformancetarget
            '''
            result = self._values.get("price_performance_target")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkgroup.PerformanceTargetProperty"]], result)

        @builtins.property
        def publicly_accessible(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that specifies whether the workgroup can be accessible from a public network.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-publiclyaccessible
            '''
            result = self._values.get("publicly_accessible")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of security group IDs to associate with the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of subnet IDs the workgroup is associated with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def track_name(self) -> typing.Optional[builtins.str]:
            '''The name of the track for the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-trackname
            '''
            result = self._values.get("track_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def workgroup_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) that links to the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-workgrouparn
            '''
            result = self._values.get("workgroup_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def workgroup_id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-workgroupid
            '''
            result = self._values.get("workgroup_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def workgroup_name(self) -> typing.Optional[builtins.str]:
            '''The name of the workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-redshiftserverless-workgroup-workgroup.html#cfn-redshiftserverless-workgroup-workgroup-workgroupname
            '''
            result = self._values.get("workgroup_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkgroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_redshiftserverless.CfnWorkgroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "workgroup_name": "workgroupName",
        "base_capacity": "baseCapacity",
        "config_parameters": "configParameters",
        "enhanced_vpc_routing": "enhancedVpcRouting",
        "max_capacity": "maxCapacity",
        "namespace_name": "namespaceName",
        "port": "port",
        "price_performance_target": "pricePerformanceTarget",
        "publicly_accessible": "publiclyAccessible",
        "recovery_point_id": "recoveryPointId",
        "security_group_ids": "securityGroupIds",
        "snapshot_arn": "snapshotArn",
        "snapshot_name": "snapshotName",
        "snapshot_owner_account": "snapshotOwnerAccount",
        "subnet_ids": "subnetIds",
        "tags": "tags",
        "track_name": "trackName",
        "workgroup": "workgroup",
    },
)
class CfnWorkgroupProps:
    def __init__(
        self,
        *,
        workgroup_name: builtins.str,
        base_capacity: typing.Optional[jsii.Number] = None,
        config_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.ConfigParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        max_capacity: typing.Optional[jsii.Number] = None,
        namespace_name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        price_performance_target: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.PerformanceTargetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        recovery_point_id: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        snapshot_arn: typing.Optional[builtins.str] = None,
        snapshot_name: typing.Optional[builtins.str] = None,
        snapshot_owner_account: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        track_name: typing.Optional[builtins.str] = None,
        workgroup: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.WorkgroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkgroup``.

        :param workgroup_name: The name of the workgroup.
        :param base_capacity: The base compute capacity of the workgroup in Redshift Processing Units (RPUs).
        :param config_parameters: The key of the parameter. The options are ``auto_mv`` , ``datestyle`` , ``enable_case_sensitive_identifier`` , ``enable_user_activity_logging`` , ``query_group`` , ``search_path`` , ``require_ssl`` , ``use_fips_ssl`` , and query monitoring metrics that let you define performance boundaries. For more information about query monitoring rules and available metrics, see `Query monitoring metrics for Amazon Redshift Serverless <https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless>`_ .
        :param enhanced_vpc_routing: The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC. Default: - false
        :param max_capacity: The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.
        :param namespace_name: The namespace the workgroup is associated with.
        :param port: The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.
        :param price_performance_target: An object that represents the price performance target settings for the workgroup.
        :param publicly_accessible: A value that specifies whether the workgroup can be accessible from a public network. Default: - false
        :param recovery_point_id: The recovery point id to restore from.
        :param security_group_ids: A list of security group IDs to associate with the workgroup.
        :param snapshot_arn: The Amazon Resource Name (ARN) of the snapshot to restore from.
        :param snapshot_name: The snapshot name to restore from.
        :param snapshot_owner_account: The Amazon Web Services account that owns the snapshot.
        :param subnet_ids: A list of subnet IDs the workgroup is associated with.
        :param tags: The map of the key-value pairs used to tag the workgroup.
        :param track_name: An optional parameter for the name of the track for the workgroup. If you don't provide a track name, the workgroup is assigned to the current track.
        :param workgroup: The collection of computing resources from which an endpoint is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_redshiftserverless as redshiftserverless
            
            cfn_workgroup_props = redshiftserverless.CfnWorkgroupProps(
                workgroup_name="workgroupName",
            
                # the properties below are optional
                base_capacity=123,
                config_parameters=[redshiftserverless.CfnWorkgroup.ConfigParameterProperty(
                    parameter_key="parameterKey",
                    parameter_value="parameterValue"
                )],
                enhanced_vpc_routing=False,
                max_capacity=123,
                namespace_name="namespaceName",
                port=123,
                price_performance_target=redshiftserverless.CfnWorkgroup.PerformanceTargetProperty(
                    level=123,
                    status="status"
                ),
                publicly_accessible=False,
                recovery_point_id="recoveryPointId",
                security_group_ids=["securityGroupIds"],
                snapshot_arn="snapshotArn",
                snapshot_name="snapshotName",
                snapshot_owner_account="snapshotOwnerAccount",
                subnet_ids=["subnetIds"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                track_name="trackName",
                workgroup=redshiftserverless.CfnWorkgroup.WorkgroupProperty(
                    base_capacity=123,
                    config_parameters=[redshiftserverless.CfnWorkgroup.ConfigParameterProperty(
                        parameter_key="parameterKey",
                        parameter_value="parameterValue"
                    )],
                    creation_date="creationDate",
                    endpoint=redshiftserverless.CfnWorkgroup.EndpointProperty(
                        address="address",
                        port=123,
                        vpc_endpoints=[redshiftserverless.CfnWorkgroup.VpcEndpointProperty(
                            network_interfaces=[redshiftserverless.CfnWorkgroup.NetworkInterfaceProperty(
                                availability_zone="availabilityZone",
                                network_interface_id="networkInterfaceId",
                                private_ip_address="privateIpAddress",
                                subnet_id="subnetId"
                            )],
                            vpc_endpoint_id="vpcEndpointId",
                            vpc_id="vpcId"
                        )]
                    ),
                    enhanced_vpc_routing=False,
                    max_capacity=123,
                    namespace_name="namespaceName",
                    price_performance_target=redshiftserverless.CfnWorkgroup.PerformanceTargetProperty(
                        level=123,
                        status="status"
                    ),
                    publicly_accessible=False,
                    security_group_ids=["securityGroupIds"],
                    status="status",
                    subnet_ids=["subnetIds"],
                    track_name="trackName",
                    workgroup_arn="workgroupArn",
                    workgroup_id="workgroupId",
                    workgroup_name="workgroupName"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ee3941005026bdab05d38183c12cc7cf5ff218e6db3877161b60d823e21a136)
            check_type(argname="argument workgroup_name", value=workgroup_name, expected_type=type_hints["workgroup_name"])
            check_type(argname="argument base_capacity", value=base_capacity, expected_type=type_hints["base_capacity"])
            check_type(argname="argument config_parameters", value=config_parameters, expected_type=type_hints["config_parameters"])
            check_type(argname="argument enhanced_vpc_routing", value=enhanced_vpc_routing, expected_type=type_hints["enhanced_vpc_routing"])
            check_type(argname="argument max_capacity", value=max_capacity, expected_type=type_hints["max_capacity"])
            check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument price_performance_target", value=price_performance_target, expected_type=type_hints["price_performance_target"])
            check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
            check_type(argname="argument recovery_point_id", value=recovery_point_id, expected_type=type_hints["recovery_point_id"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument snapshot_arn", value=snapshot_arn, expected_type=type_hints["snapshot_arn"])
            check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
            check_type(argname="argument snapshot_owner_account", value=snapshot_owner_account, expected_type=type_hints["snapshot_owner_account"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument track_name", value=track_name, expected_type=type_hints["track_name"])
            check_type(argname="argument workgroup", value=workgroup, expected_type=type_hints["workgroup"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workgroup_name": workgroup_name,
        }
        if base_capacity is not None:
            self._values["base_capacity"] = base_capacity
        if config_parameters is not None:
            self._values["config_parameters"] = config_parameters
        if enhanced_vpc_routing is not None:
            self._values["enhanced_vpc_routing"] = enhanced_vpc_routing
        if max_capacity is not None:
            self._values["max_capacity"] = max_capacity
        if namespace_name is not None:
            self._values["namespace_name"] = namespace_name
        if port is not None:
            self._values["port"] = port
        if price_performance_target is not None:
            self._values["price_performance_target"] = price_performance_target
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if recovery_point_id is not None:
            self._values["recovery_point_id"] = recovery_point_id
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if snapshot_arn is not None:
            self._values["snapshot_arn"] = snapshot_arn
        if snapshot_name is not None:
            self._values["snapshot_name"] = snapshot_name
        if snapshot_owner_account is not None:
            self._values["snapshot_owner_account"] = snapshot_owner_account
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if tags is not None:
            self._values["tags"] = tags
        if track_name is not None:
            self._values["track_name"] = track_name
        if workgroup is not None:
            self._values["workgroup"] = workgroup

    @builtins.property
    def workgroup_name(self) -> builtins.str:
        '''The name of the workgroup.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-workgroupname
        '''
        result = self._values.get("workgroup_name")
        assert result is not None, "Required property 'workgroup_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base_capacity(self) -> typing.Optional[jsii.Number]:
        '''The base compute capacity of the workgroup in Redshift Processing Units (RPUs).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-basecapacity
        '''
        result = self._values.get("base_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def config_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnWorkgroup.ConfigParameterProperty]]]]:
        '''The key of the parameter.

        The options are ``auto_mv`` , ``datestyle`` , ``enable_case_sensitive_identifier`` , ``enable_user_activity_logging`` , ``query_group`` , ``search_path`` , ``require_ssl`` , ``use_fips_ssl`` , and query monitoring metrics that let you define performance boundaries. For more information about query monitoring rules and available metrics, see `Query monitoring metrics for Amazon Redshift Serverless <https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-configparameters
        '''
        result = self._values.get("config_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnWorkgroup.ConfigParameterProperty]]]], result)

    @builtins.property
    def enhanced_vpc_routing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-enhancedvpcrouting
        '''
        result = self._values.get("enhanced_vpc_routing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def max_capacity(self) -> typing.Optional[jsii.Number]:
        '''The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries.

        The max capacity is specified in RPUs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-maxcapacity
        '''
        result = self._values.get("max_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def namespace_name(self) -> typing.Optional[builtins.str]:
        '''The namespace the workgroup is associated with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-namespacename
        '''
        result = self._values.get("namespace_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The custom port to use when connecting to a workgroup.

        Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def price_performance_target(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkgroup.PerformanceTargetProperty]]:
        '''An object that represents the price performance target settings for the workgroup.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-priceperformancetarget
        '''
        result = self._values.get("price_performance_target")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkgroup.PerformanceTargetProperty]], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A value that specifies whether the workgroup can be accessible from a public network.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-publiclyaccessible
        '''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def recovery_point_id(self) -> typing.Optional[builtins.str]:
        '''The recovery point id to restore from.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-recoverypointid
        '''
        result = self._values.get("recovery_point_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group IDs to associate with the workgroup.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def snapshot_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the snapshot to restore from.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-snapshotarn
        '''
        result = self._values.get("snapshot_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_name(self) -> typing.Optional[builtins.str]:
        '''The snapshot name to restore from.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-snapshotname
        '''
        result = self._values.get("snapshot_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_owner_account(self) -> typing.Optional[builtins.str]:
        '''The Amazon Web Services account that owns the snapshot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-snapshotowneraccount
        '''
        result = self._values.get("snapshot_owner_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of subnet IDs the workgroup is associated with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-subnetids
        '''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The map of the key-value pairs used to tag the workgroup.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def track_name(self) -> typing.Optional[builtins.str]:
        '''An optional parameter for the name of the track for the workgroup.

        If you don't provide a track name, the workgroup is assigned to the current track.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-trackname
        '''
        result = self._values.get("track_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workgroup(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkgroup.WorkgroupProperty]]:
        '''The collection of computing resources from which an endpoint is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshiftserverless-workgroup.html#cfn-redshiftserverless-workgroup-workgroup
        '''
        result = self._values.get("workgroup")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkgroup.WorkgroupProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkgroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnNamespace",
    "CfnNamespaceProps",
    "CfnSnapshot",
    "CfnSnapshotProps",
    "CfnWorkgroup",
    "CfnWorkgroupProps",
]

publication.publish()

def _typecheckingstub__e517382d9f55a518348d7299a7ce6c5be66bae2202f4223bf3c891a7dd669682(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    namespace_name: builtins.str,
    admin_password_secret_kms_key_id: typing.Optional[builtins.str] = None,
    admin_username: typing.Optional[builtins.str] = None,
    admin_user_password: typing.Optional[builtins.str] = None,
    db_name: typing.Optional[builtins.str] = None,
    default_iam_role_arn: typing.Optional[builtins.str] = None,
    final_snapshot_name: typing.Optional[builtins.str] = None,
    final_snapshot_retention_period: typing.Optional[jsii.Number] = None,
    iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
    manage_admin_password: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    namespace_resource_policy: typing.Any = None,
    redshift_idc_application_arn: typing.Optional[builtins.str] = None,
    snapshot_copy_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnNamespace.SnapshotCopyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2df0038e9ec3a1b73ddb07c3b803a742204804b2ccd2aab0d7df9fbb8521f86(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d877d23369c8f10ea1630884d7e7c879ab22a49fc05986834857785664c640ca(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fe15d8ff16345a3e36d8c090d48eea89c8cd559ac4218facdfd95b67e49140c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ad26fc5262e682a19af3392d1855021d70d396b74b82cb73cc9022919f97e63(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e95b6bb908e50903825c7cbfdb447ab3aceb27b3a93be8aa57fe8923f432493(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b50aae57ce0c503e5aed7528570d1ab32511eacbfe2dcac51d410dd4bb1991ec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8947213c316180fbcdb1956ca9a54febcb6a874110724c51c1db8705f8186d0a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a992711b01695733a564873ba440d2806a3692e807afc16701507c986201edd9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de06e0fc02a451c4e9e47c3f839f6289f8f8e9d4dbc0867eb263e09672990c7e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ae56ba94c395d18dd103368c4ca09a505763b47324b4820065925d61c84adaf(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9111ebc5ef107cd5d00c7617518664163ccd1b1d99fb0ec53548dd04073b0e77(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bc1c937667ef895444beeaaacfd8af398b90be0a42f50184325fdb96072b5ba(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1526e0cedff0515a6bb96570f366670e82fb4d0cc597e2d7a8b0a091f0420dea(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fee9e13028e66f79f12c6ed7063cc442fd9b8a5aa18d9a39ced55fd585d8f0d4(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43a289d7dca3804ca980a93314a4c0b2949e95448b9e91aef20d960cd1facef7(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51136c4f6d62ea1ed8116bbb890860f45a983131873ecd0a7b407595037600cc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7336d2da1a6ceace7b9ad8afbae65968e0c9440d9a2bcf4cd5e62d531da1693(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnNamespace.SnapshotCopyConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e2da7bae4bc39426d05dc2f307e08d5246472ad626b032ef4c2ea7b7d1bd33f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bcbea65acb7d2a3cef7455cfbb52c832d3da01cd5e02df21a06cdb2b4822e35(
    *,
    admin_password_secret_arn: typing.Optional[builtins.str] = None,
    admin_password_secret_kms_key_id: typing.Optional[builtins.str] = None,
    admin_username: typing.Optional[builtins.str] = None,
    creation_date: typing.Optional[builtins.str] = None,
    db_name: typing.Optional[builtins.str] = None,
    default_iam_role_arn: typing.Optional[builtins.str] = None,
    iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
    namespace_arn: typing.Optional[builtins.str] = None,
    namespace_id: typing.Optional[builtins.str] = None,
    namespace_name: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f726a14406204ec2ead254e53f2cdca3d4ac96a2d835e99da9cbbb58c02dccd(
    *,
    destination_region: builtins.str,
    destination_kms_key_id: typing.Optional[builtins.str] = None,
    snapshot_retention_period: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5964a5da555f62a5d9615a6e07cd0d1128cdf904fd5aa3c5be9fd5e53dc30bd9(
    *,
    namespace_name: builtins.str,
    admin_password_secret_kms_key_id: typing.Optional[builtins.str] = None,
    admin_username: typing.Optional[builtins.str] = None,
    admin_user_password: typing.Optional[builtins.str] = None,
    db_name: typing.Optional[builtins.str] = None,
    default_iam_role_arn: typing.Optional[builtins.str] = None,
    final_snapshot_name: typing.Optional[builtins.str] = None,
    final_snapshot_retention_period: typing.Optional[jsii.Number] = None,
    iam_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    log_exports: typing.Optional[typing.Sequence[builtins.str]] = None,
    manage_admin_password: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    namespace_resource_policy: typing.Any = None,
    redshift_idc_application_arn: typing.Optional[builtins.str] = None,
    snapshot_copy_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnNamespace.SnapshotCopyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1e2b5eeadcf14eaf0be75cda550b6bcef2aa009af0fe87d6f5e9e856ad0ef43(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    snapshot_name: builtins.str,
    namespace_name: typing.Optional[builtins.str] = None,
    retention_period: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ddc470fc115016c807de39b9ff4325d249ff8657e32f92eefbcb4bac9e79eb0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bdbe6940b32b0a05793c97cd18c6f2009d35937c086b1b342b276e310c97129(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f64f97556142b340a4fd0b74522c68b85e2157f2a27ece8203bd18185cfe3ce6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f6a30dd9c5c0b8045b8d36ef14977ccb4361c843f7dcb8ac7322f8fa349468d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__521c1c8ca437327e56c1b9a24896fa19595912e045202fbf656a893304dd3c04(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77534803a2fb41b5883d0c89334777e664cec59572dd7a376bbe5dbc41ff64ef(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d32a77292254bff347197e3bdcc04e2fea309ebb7baea20e5fee3f5714159ffa(
    *,
    admin_username: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    namespace_arn: typing.Optional[builtins.str] = None,
    namespace_name: typing.Optional[builtins.str] = None,
    owner_account: typing.Optional[builtins.str] = None,
    retention_period: typing.Optional[jsii.Number] = None,
    snapshot_arn: typing.Optional[builtins.str] = None,
    snapshot_create_time: typing.Optional[builtins.str] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38cd0d09fc150d83197b13fb0e10ea82ffa589e88452cdfecbd53994ae2ced5b(
    *,
    snapshot_name: builtins.str,
    namespace_name: typing.Optional[builtins.str] = None,
    retention_period: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61a1b6ebbdacc577619f4e17ddabdaa553ffe5fe072b72e14ddf7d9c3f7e1a04(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    workgroup_name: builtins.str,
    base_capacity: typing.Optional[jsii.Number] = None,
    config_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.ConfigParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    max_capacity: typing.Optional[jsii.Number] = None,
    namespace_name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    price_performance_target: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.PerformanceTargetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    recovery_point_id: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_arn: typing.Optional[builtins.str] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
    snapshot_owner_account: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    track_name: typing.Optional[builtins.str] = None,
    workgroup: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.WorkgroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__986feaaa3c97c38d5a5c4414a977741007338bd588a8ebc981d89e63b28c9c38(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__575b09c3449f3d47af302b94ec8c88b82387f8f428024e134c076d5600122345(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b001bba04c1f96a7169e528d056ccd8d9035fee30af63b1f339873bf7e3ea7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d35b55423f49c0c42ee449a11852238ff7a68ae5e2e78f2da58bcb94c221a85(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00339df2c3d04a43ab10d867748f8678b0423745badc0e14afa8bb128d473607(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnWorkgroup.ConfigParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b06db2b227debd7cc917f51bf7c4c0bb700bca075b329af61a43f37521feba71(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ceab2fa028856954a409378fab7e1382a9cf79f0bf83fa7f082c0d6996e02e9(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a009fb86999f55de110193d15ea127b35ea379a1d840ddd42a0406b02f3a997a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e3a61acfcbbe3b107c15ebd1c1248f3bd150ad58cf876908da7870de9fd6fde(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__971a4fc1559ba6fa762249206f240d83ab3e607f325e8eeed9b9122b529c78e0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkgroup.PerformanceTargetProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__974542b0d8aa6c1847dd536dcf795ef2c4719aed798ea365b0767f6ad3234ca0(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__330f25021814c2fb98578117b6d4b45cb103383dd78a1ec221ad5ee1da1af776(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2864d0fac41ac305963b5532a731665cbc0d93a810a41ea2d2fe98a5285e8aa(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22c9552850e931e5526d6b100685f6e372509370d50247f9134b09b667c31905(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9001e412e7a006803ae5b51d6b1ec1486aa95db2939acfaa5b88a397dfaf1e7b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e20f0edef13cea8274ed0af3c59774d9e6b1dc49c1c6cd25ad2a5807f42500fe(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67e139cef151f144f2bb04082850da469be0ab0515cff591edf9fc1e44df78a9(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3104c5d5a81618ce7738aabf06bbd67fea6c82cd5abea01e1b03c71c5065efc(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ae0d98fb213b87bdf0bef05c29f3608e64d5cab8c142baeef1f930bb88523bd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb73897901d98002fc8e5d2e00c5ffffec6d6ffc0d70be41b21317bd200b87a5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkgroup.WorkgroupProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__322e3a40a90a7ebca9e3ef09024360dddede638badc33eeda64eccd556f3dc5f(
    *,
    parameter_key: typing.Optional[builtins.str] = None,
    parameter_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1064dbbc6e1afc7fbd36b9ac721b89fc24382d0930f8f41542644b48bc6c07bf(
    *,
    address: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    vpc_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.VpcEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c27a8032aaa250691e1e68b2e75ce65c47142ac6b83ad22f01b09ec293f841b8(
    *,
    availability_zone: typing.Optional[builtins.str] = None,
    network_interface_id: typing.Optional[builtins.str] = None,
    private_ip_address: typing.Optional[builtins.str] = None,
    subnet_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7166282347ab806de45e7f23d02833af860bdd81c72c593cfef563b261c272f(
    *,
    level: typing.Optional[jsii.Number] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__200b427a09281b666ef25deaac2b6bf3abeeda64d77ffa3f7903dbe300b6606d(
    *,
    network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.NetworkInterfaceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    vpc_endpoint_id: typing.Optional[builtins.str] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7cad236eecd67272da075e88f17a1dbdae4ee5083553d6443dcc19b3a333780(
    *,
    base_capacity: typing.Optional[jsii.Number] = None,
    config_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.ConfigParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    creation_date: typing.Optional[builtins.str] = None,
    endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.EndpointProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    max_capacity: typing.Optional[jsii.Number] = None,
    namespace_name: typing.Optional[builtins.str] = None,
    price_performance_target: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.PerformanceTargetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    track_name: typing.Optional[builtins.str] = None,
    workgroup_arn: typing.Optional[builtins.str] = None,
    workgroup_id: typing.Optional[builtins.str] = None,
    workgroup_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ee3941005026bdab05d38183c12cc7cf5ff218e6db3877161b60d823e21a136(
    *,
    workgroup_name: builtins.str,
    base_capacity: typing.Optional[jsii.Number] = None,
    config_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.ConfigParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    enhanced_vpc_routing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    max_capacity: typing.Optional[jsii.Number] = None,
    namespace_name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    price_performance_target: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.PerformanceTargetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    recovery_point_id: typing.Optional[builtins.str] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    snapshot_arn: typing.Optional[builtins.str] = None,
    snapshot_name: typing.Optional[builtins.str] = None,
    snapshot_owner_account: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    track_name: typing.Optional[builtins.str] = None,
    workgroup: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkgroup.WorkgroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
