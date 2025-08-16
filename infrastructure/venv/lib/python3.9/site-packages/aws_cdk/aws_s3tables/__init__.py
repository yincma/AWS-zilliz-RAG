r'''
# AWS::S3Tables Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_s3tables as s3tables
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for S3Tables construct libraries](https://constructs.dev/search?q=s3tables)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::S3Tables resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3Tables.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::S3Tables](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3Tables.html).

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
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnNamespace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3tables.CfnNamespace",
):
    '''Creates a namespace.

    A namespace is a logical grouping of tables within your table bucket, which you can use to organize tables. For more information, see `Create a namespace <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-namespace-create.html>`_ in the *Amazon Simple Storage Service User Guide* .

    - **Permissions** - You must have the ``s3tables:CreateNamespace`` permission to use this operation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-namespace.html
    :cloudformationResource: AWS::S3Tables::Namespace
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3tables as s3tables
        
        cfn_namespace = s3tables.CfnNamespace(self, "MyCfnNamespace",
            namespace="namespace",
            table_bucket_arn="tableBucketArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        namespace: builtins.str,
        table_bucket_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param namespace: The name of the namespace.
        :param table_bucket_arn: The Amazon Resource Name (ARN) of the specified table bucket.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd79dcff4893fe1cd3464c1f48689d2a01ad4a5eed6acfd35e21266683ab1f1c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNamespaceProps(
            namespace=namespace, table_bucket_arn=table_bucket_arn
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dae368df5e118b03066ac5fbad3765e81aa23b31a7288aa2bb824379578614f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c772aad560ab6b4e840f54665ca3a18a9fcbf362512eb78423617db138b70b0)
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
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        '''The name of the namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__083038783d9a592008992f105965913f4b10d8bc23252afb9a929c22e7cebd06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tableBucketArn")
    def table_bucket_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the specified table bucket.'''
        return typing.cast(builtins.str, jsii.get(self, "tableBucketArn"))

    @table_bucket_arn.setter
    def table_bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8560b7f29623bc1f753b1cf34442c874c6958096b39accf37244c9341879fd81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableBucketArn", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3tables.CfnNamespaceProps",
    jsii_struct_bases=[],
    name_mapping={"namespace": "namespace", "table_bucket_arn": "tableBucketArn"},
)
class CfnNamespaceProps:
    def __init__(
        self,
        *,
        namespace: builtins.str,
        table_bucket_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnNamespace``.

        :param namespace: The name of the namespace.
        :param table_bucket_arn: The Amazon Resource Name (ARN) of the specified table bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-namespace.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3tables as s3tables
            
            cfn_namespace_props = s3tables.CfnNamespaceProps(
                namespace="namespace",
                table_bucket_arn="tableBucketArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fdadc8758c9f96fac22200567c0d51cfd3e36c943cb9fa46e50cbf9abf25faf)
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument table_bucket_arn", value=table_bucket_arn, expected_type=type_hints["table_bucket_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "namespace": namespace,
            "table_bucket_arn": table_bucket_arn,
        }

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The name of the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-namespace.html#cfn-s3tables-namespace-namespace
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_bucket_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the specified table bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-namespace.html#cfn-s3tables-namespace-tablebucketarn
        '''
        result = self._values.get("table_bucket_arn")
        assert result is not None, "Required property 'table_bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTable(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3tables.CfnTable",
):
    '''Creates a new table associated with the given namespace in a table bucket.

    For more information, see `Creating an Amazon S3 table <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-create.html>`_ in the *Amazon Simple Storage Service User Guide* .

    - **Permissions** - - You must have the ``s3tables:CreateTable`` permission to use this operation.
    - If you use this operation with the optional ``metadata`` request parameter you must have the ``s3tables:PutTableData`` permission.
    - If you use this operation with the optional ``encryptionConfiguration`` request parameter you must have the ``s3tables:PutTableEncryption`` permission.

    .. epigraph::

       Additionally, If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see `Permissions requirements for S3 Tables SSE-KMS encryption <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-table.html
    :cloudformationResource: AWS::S3Tables::Table
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3tables as s3tables
        
        cfn_table = s3tables.CfnTable(self, "MyCfnTable",
            namespace="namespace",
            open_table_format="openTableFormat",
            table_bucket_arn="tableBucketArn",
            table_name="tableName",
        
            # the properties below are optional
            compaction=s3tables.CfnTable.CompactionProperty(
                status="status",
                target_file_size_mb=123
            ),
            iceberg_metadata=s3tables.CfnTable.IcebergMetadataProperty(
                iceberg_schema=s3tables.CfnTable.IcebergSchemaProperty(
                    schema_field_list=[s3tables.CfnTable.SchemaFieldProperty(
                        name="name",
                        type="type",
        
                        # the properties below are optional
                        required=False
                    )]
                )
            ),
            snapshot_management=s3tables.CfnTable.SnapshotManagementProperty(
                max_snapshot_age_hours=123,
                min_snapshots_to_keep=123,
                status="status"
            ),
            without_metadata="withoutMetadata"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        namespace: builtins.str,
        open_table_format: builtins.str,
        table_bucket_arn: builtins.str,
        table_name: builtins.str,
        compaction: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.CompactionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        iceberg_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.IcebergMetadataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        snapshot_management: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.SnapshotManagementProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        without_metadata: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param namespace: The name of the namespace.
        :param open_table_format: Format of the table.
        :param table_bucket_arn: The Amazon Resource Name (ARN) of the specified table bucket.
        :param table_name: The name for the table.
        :param compaction: Settings governing the Compaction maintenance action. Contains details about the compaction settings for an Iceberg table.
        :param iceberg_metadata: Contains details about the metadata for an Iceberg table.
        :param snapshot_management: Contains details about the snapshot management settings for an Iceberg table. A snapshot is expired when it exceeds MinSnapshotsToKeep and MaxSnapshotAgeHours.
        :param without_metadata: Indicates that you don't want to specify a schema for the table. This property is mutually exclusive to 'IcebergMetadata', and its only possible value is 'Yes'.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cb6d8b27037c33c46017d3b0b00b52a14bbd8c0a922c03aca7fff9e327b1420)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTableProps(
            namespace=namespace,
            open_table_format=open_table_format,
            table_bucket_arn=table_bucket_arn,
            table_name=table_name,
            compaction=compaction,
            iceberg_metadata=iceberg_metadata,
            snapshot_management=snapshot_management,
            without_metadata=without_metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e9f0a1074447de044514c7c1b5b2cca167912d3e02c228b501f3cc4c1b09a6f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a82da714fe9043c593e17c8af3ba9310ce4d043a6843c815aa933a3f004a6d5a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrTableArn")
    def attr_table_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the table.

        :cloudformationAttribute: TableARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTableArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionToken")
    def attr_version_token(self) -> builtins.str:
        '''The version token of the table.

        :cloudformationAttribute: VersionToken
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersionToken"))

    @builtins.property
    @jsii.member(jsii_name="attrWarehouseLocation")
    def attr_warehouse_location(self) -> builtins.str:
        '''The warehouse location of the table.

        :cloudformationAttribute: WarehouseLocation
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWarehouseLocation"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        '''The name of the namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb40731dfd6256164661895ce0f48c78b8e18c58fb7f27fbb73a3ce7c916c1df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="openTableFormat")
    def open_table_format(self) -> builtins.str:
        '''Format of the table.'''
        return typing.cast(builtins.str, jsii.get(self, "openTableFormat"))

    @open_table_format.setter
    def open_table_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5892a05d87447cee97d5ab4f41ddb7d6837df87a8b4e6b9d577c79cfe927180a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openTableFormat", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tableBucketArn")
    def table_bucket_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the specified table bucket.'''
        return typing.cast(builtins.str, jsii.get(self, "tableBucketArn"))

    @table_bucket_arn.setter
    def table_bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ad6ac8e43e44c04006a5ef80e152c8effbbdb7bf127bd063a6b732c4ee1f9a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableBucketArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        '''The name for the table.'''
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f410c91375a77f7ed3b5736522dbfb254643b931cd30ea49af6d7d51d9c5ddc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="compaction")
    def compaction(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.CompactionProperty"]]:
        '''Settings governing the Compaction maintenance action.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.CompactionProperty"]], jsii.get(self, "compaction"))

    @compaction.setter
    def compaction(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.CompactionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ff6f95f778b64c53b87dfe6f8a117fa9d1583584d475eef7586c75859dcb219)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compaction", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="icebergMetadata")
    def iceberg_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.IcebergMetadataProperty"]]:
        '''Contains details about the metadata for an Iceberg table.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.IcebergMetadataProperty"]], jsii.get(self, "icebergMetadata"))

    @iceberg_metadata.setter
    def iceberg_metadata(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.IcebergMetadataProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f0509a656c9927b41c3ead9b58d6c83257863d2b8d1104c542e1a8435be4160)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icebergMetadata", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="snapshotManagement")
    def snapshot_management(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.SnapshotManagementProperty"]]:
        '''Contains details about the snapshot management settings for an Iceberg table.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.SnapshotManagementProperty"]], jsii.get(self, "snapshotManagement"))

    @snapshot_management.setter
    def snapshot_management(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTable.SnapshotManagementProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6c432f4785ee47d59f072204756d42650b9fc3dd3e85a79139ab4f11fb72a43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotManagement", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="withoutMetadata")
    def without_metadata(self) -> typing.Optional[builtins.str]:
        '''Indicates that you don't want to specify a schema for the table.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "withoutMetadata"))

    @without_metadata.setter
    def without_metadata(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5d21acaabd2bab58c6f59f334d1b06b0962eb6541244a042a933b5ce009a061)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withoutMetadata", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3tables.CfnTable.CompactionProperty",
        jsii_struct_bases=[],
        name_mapping={"status": "status", "target_file_size_mb": "targetFileSizeMb"},
    )
    class CompactionProperty:
        def __init__(
            self,
            *,
            status: typing.Optional[builtins.str] = None,
            target_file_size_mb: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Settings governing the Compaction maintenance action.

            Contains details about the compaction settings for an Iceberg table.

            :param status: Indicates whether the Compaction maintenance action is enabled.
            :param target_file_size_mb: The target file size for the table in MB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-table-compaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3tables as s3tables
                
                compaction_property = s3tables.CfnTable.CompactionProperty(
                    status="status",
                    target_file_size_mb=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f49118bb06f06baf9f7618e6cd633803a2486d06b541e59cab8801a6a0983fcc)
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument target_file_size_mb", value=target_file_size_mb, expected_type=type_hints["target_file_size_mb"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if status is not None:
                self._values["status"] = status
            if target_file_size_mb is not None:
                self._values["target_file_size_mb"] = target_file_size_mb

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''Indicates whether the Compaction maintenance action is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-table-compaction.html#cfn-s3tables-table-compaction-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_file_size_mb(self) -> typing.Optional[jsii.Number]:
            '''The target file size for the table in MB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-table-compaction.html#cfn-s3tables-table-compaction-targetfilesizemb
            '''
            result = self._values.get("target_file_size_mb")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CompactionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3tables.CfnTable.IcebergMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={"iceberg_schema": "icebergSchema"},
    )
    class IcebergMetadataProperty:
        def __init__(
            self,
            *,
            iceberg_schema: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.IcebergSchemaProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Contains details about the metadata for an Iceberg table.

            :param iceberg_schema: Contains details about the schema for an Iceberg table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-table-icebergmetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3tables as s3tables
                
                iceberg_metadata_property = s3tables.CfnTable.IcebergMetadataProperty(
                    iceberg_schema=s3tables.CfnTable.IcebergSchemaProperty(
                        schema_field_list=[s3tables.CfnTable.SchemaFieldProperty(
                            name="name",
                            type="type",
                
                            # the properties below are optional
                            required=False
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1e5dc7085346ad722ba37251e910871affc6e3d90d9251cc9d43941978d7cb0a)
                check_type(argname="argument iceberg_schema", value=iceberg_schema, expected_type=type_hints["iceberg_schema"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "iceberg_schema": iceberg_schema,
            }

        @builtins.property
        def iceberg_schema(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTable.IcebergSchemaProperty"]:
            '''Contains details about the schema for an Iceberg table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-table-icebergmetadata.html#cfn-s3tables-table-icebergmetadata-icebergschema
            '''
            result = self._values.get("iceberg_schema")
            assert result is not None, "Required property 'iceberg_schema' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTable.IcebergSchemaProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IcebergMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3tables.CfnTable.IcebergSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={"schema_field_list": "schemaFieldList"},
    )
    class IcebergSchemaProperty:
        def __init__(
            self,
            *,
            schema_field_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTable.SchemaFieldProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Contains details about the schema for an Iceberg table.

            :param schema_field_list: Contains details about the schema for an Iceberg table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-table-icebergschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3tables as s3tables
                
                iceberg_schema_property = s3tables.CfnTable.IcebergSchemaProperty(
                    schema_field_list=[s3tables.CfnTable.SchemaFieldProperty(
                        name="name",
                        type="type",
                
                        # the properties below are optional
                        required=False
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3613cb002c55c4baeb2517f3445ed9e71396e5ee393d230544d3f1302b471205)
                check_type(argname="argument schema_field_list", value=schema_field_list, expected_type=type_hints["schema_field_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "schema_field_list": schema_field_list,
            }

        @builtins.property
        def schema_field_list(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.SchemaFieldProperty"]]]:
            '''Contains details about the schema for an Iceberg table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-table-icebergschema.html#cfn-s3tables-table-icebergschema-schemafieldlist
            '''
            result = self._values.get("schema_field_list")
            assert result is not None, "Required property 'schema_field_list' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTable.SchemaFieldProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IcebergSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3tables.CfnTable.SchemaFieldProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "type": "type", "required": "required"},
    )
    class SchemaFieldProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            type: builtins.str,
            required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Contains details about a schema field.

            :param name: The name of the field.
            :param type: The field type. S3 Tables supports all Apache Iceberg primitive types. For more information, see the `Apache Iceberg documentation <https://docs.aws.amazon.com/https://iceberg.apache.org/spec/#primitive-types>`_ .
            :param required: A Boolean value that specifies whether values are required for each row in this field. By default, this is ``false`` and null values are allowed in the field. If this is ``true`` the field does not allow null values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-table-schemafield.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3tables as s3tables
                
                schema_field_property = s3tables.CfnTable.SchemaFieldProperty(
                    name="name",
                    type="type",
                
                    # the properties below are optional
                    required=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b3f6368f6b334e97c5c50a43ab04d5e784e18fdb0e687d1684b9ad01ad6c1a29)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "type": type,
            }
            if required is not None:
                self._values["required"] = required

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-table-schemafield.html#cfn-s3tables-table-schemafield-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The field type.

            S3 Tables supports all Apache Iceberg primitive types. For more information, see the `Apache Iceberg documentation <https://docs.aws.amazon.com/https://iceberg.apache.org/spec/#primitive-types>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-table-schemafield.html#cfn-s3tables-table-schemafield-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def required(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean value that specifies whether values are required for each row in this field.

            By default, this is ``false`` and null values are allowed in the field. If this is ``true`` the field does not allow null values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-table-schemafield.html#cfn-s3tables-table-schemafield-required
            '''
            result = self._values.get("required")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaFieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3tables.CfnTable.SnapshotManagementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_snapshot_age_hours": "maxSnapshotAgeHours",
            "min_snapshots_to_keep": "minSnapshotsToKeep",
            "status": "status",
        },
    )
    class SnapshotManagementProperty:
        def __init__(
            self,
            *,
            max_snapshot_age_hours: typing.Optional[jsii.Number] = None,
            min_snapshots_to_keep: typing.Optional[jsii.Number] = None,
            status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains details about the snapshot management settings for an Iceberg table.

            A snapshot is expired when it exceeds MinSnapshotsToKeep and MaxSnapshotAgeHours.

            :param max_snapshot_age_hours: The maximum age of a snapshot before it can be expired.
            :param min_snapshots_to_keep: The minimum number of snapshots to keep.
            :param status: Indicates whether the SnapshotManagement maintenance action is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-table-snapshotmanagement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3tables as s3tables
                
                snapshot_management_property = s3tables.CfnTable.SnapshotManagementProperty(
                    max_snapshot_age_hours=123,
                    min_snapshots_to_keep=123,
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa9c2ac7b8956daecf8522166700dd475625d08f131913fda8e01475215f3656)
                check_type(argname="argument max_snapshot_age_hours", value=max_snapshot_age_hours, expected_type=type_hints["max_snapshot_age_hours"])
                check_type(argname="argument min_snapshots_to_keep", value=min_snapshots_to_keep, expected_type=type_hints["min_snapshots_to_keep"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_snapshot_age_hours is not None:
                self._values["max_snapshot_age_hours"] = max_snapshot_age_hours
            if min_snapshots_to_keep is not None:
                self._values["min_snapshots_to_keep"] = min_snapshots_to_keep
            if status is not None:
                self._values["status"] = status

        @builtins.property
        def max_snapshot_age_hours(self) -> typing.Optional[jsii.Number]:
            '''The maximum age of a snapshot before it can be expired.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-table-snapshotmanagement.html#cfn-s3tables-table-snapshotmanagement-maxsnapshotagehours
            '''
            result = self._values.get("max_snapshot_age_hours")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_snapshots_to_keep(self) -> typing.Optional[jsii.Number]:
            '''The minimum number of snapshots to keep.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-table-snapshotmanagement.html#cfn-s3tables-table-snapshotmanagement-minsnapshotstokeep
            '''
            result = self._values.get("min_snapshots_to_keep")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''Indicates whether the SnapshotManagement maintenance action is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-table-snapshotmanagement.html#cfn-s3tables-table-snapshotmanagement-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnapshotManagementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnTableBucket(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3tables.CfnTableBucket",
):
    '''Creates a table bucket.

    For more information, see `Creating a table bucket <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-create.html>`_ in the *Amazon Simple Storage Service User Guide* .

    - **Permissions** - - You must have the ``s3tables:CreateTableBucket`` permission to use this operation.
    - If you use this operation with the optional ``encryptionConfiguration`` parameter you must have the ``s3tables:PutTableBucketEncryption`` permission.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucket.html
    :cloudformationResource: AWS::S3Tables::TableBucket
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3tables as s3tables
        
        cfn_table_bucket = s3tables.CfnTableBucket(self, "MyCfnTableBucket",
            table_bucket_name="tableBucketName",
        
            # the properties below are optional
            encryption_configuration=s3tables.CfnTableBucket.EncryptionConfigurationProperty(
                kms_key_arn="kmsKeyArn",
                sse_algorithm="sseAlgorithm"
            ),
            unreferenced_file_removal=s3tables.CfnTableBucket.UnreferencedFileRemovalProperty(
                noncurrent_days=123,
                status="status",
                unreferenced_days=123
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        table_bucket_name: builtins.str,
        encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTableBucket.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        unreferenced_file_removal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTableBucket.UnreferencedFileRemovalProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param table_bucket_name: The name for the table bucket.
        :param encryption_configuration: Configuration specifying how data should be encrypted. This structure defines the encryption algorithm and optional KMS key to be used for server-side encryption.
        :param unreferenced_file_removal: The unreferenced file removal settings for your table bucket. Unreferenced file removal identifies and deletes all objects that are not referenced by any table snapshots. For more information, see the `*Amazon S3 User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de433918cd34eecbcaab0e81b6a287f71a48dd308c2f4d42e07a0e19ce5af0e2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTableBucketProps(
            table_bucket_name=table_bucket_name,
            encryption_configuration=encryption_configuration,
            unreferenced_file_removal=unreferenced_file_removal,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40da426af74874eef485654394ab5db25ba5f82e8490b96bd68d9f6318b6654e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e15cdb1ab81b354e389c0debd6b2b9d760245945e38c20d735044cde53c3979)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrTableBucketArn")
    def attr_table_bucket_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the table bucket.

        :cloudformationAttribute: TableBucketARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTableBucketArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tableBucketName")
    def table_bucket_name(self) -> builtins.str:
        '''The name for the table bucket.'''
        return typing.cast(builtins.str, jsii.get(self, "tableBucketName"))

    @table_bucket_name.setter
    def table_bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42ef5079e6a92822a2e6ccbb91b02661f493a7d44dc79dfba0916840dbe44863)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableBucketName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTableBucket.EncryptionConfigurationProperty"]]:
        '''Configuration specifying how data should be encrypted.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTableBucket.EncryptionConfigurationProperty"]], jsii.get(self, "encryptionConfiguration"))

    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTableBucket.EncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61499f569b4e5dc20b99defd26e29c6e9b7761b6630e1adec9c20e97e099dd4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="unreferencedFileRemoval")
    def unreferenced_file_removal(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTableBucket.UnreferencedFileRemovalProperty"]]:
        '''The unreferenced file removal settings for your table bucket.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTableBucket.UnreferencedFileRemovalProperty"]], jsii.get(self, "unreferencedFileRemoval"))

    @unreferenced_file_removal.setter
    def unreferenced_file_removal(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTableBucket.UnreferencedFileRemovalProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02bf42691243dcbc8ea49c2499d3414260e70a80c4e38a371b64664c49f17e6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unreferencedFileRemoval", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3tables.CfnTableBucket.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_arn": "kmsKeyArn", "sse_algorithm": "sseAlgorithm"},
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            kms_key_arn: typing.Optional[builtins.str] = None,
            sse_algorithm: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration specifying how data should be encrypted.

            This structure defines the encryption algorithm and optional KMS key to be used for server-side encryption.

            :param kms_key_arn: The Amazon Resource Name (ARN) of the KMS key to use for encryption. This field is required only when ``sseAlgorithm`` is set to ``aws:kms`` .
            :param sse_algorithm: The server-side encryption algorithm to use. Valid values are ``AES256`` for S3-managed encryption keys, or ``aws:kms`` for AWS KMS-managed encryption keys. If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see `Permissions requirements for S3 Tables SSE-KMS encryption <https://docs.aws.amazon.com//AmazonS3/latest/userguide/s3-tables-kms-permissions.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-tablebucket-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3tables as s3tables
                
                encryption_configuration_property = s3tables.CfnTableBucket.EncryptionConfigurationProperty(
                    kms_key_arn="kmsKeyArn",
                    sse_algorithm="sseAlgorithm"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__659e946ab1ee4bc0eb13a519adc57d2cb4431347d47a9e6cb4d4086a87be1b2a)
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
                check_type(argname="argument sse_algorithm", value=sse_algorithm, expected_type=type_hints["sse_algorithm"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn
            if sse_algorithm is not None:
                self._values["sse_algorithm"] = sse_algorithm

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the KMS key to use for encryption.

            This field is required only when ``sseAlgorithm`` is set to ``aws:kms`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-tablebucket-encryptionconfiguration.html#cfn-s3tables-tablebucket-encryptionconfiguration-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sse_algorithm(self) -> typing.Optional[builtins.str]:
            '''The server-side encryption algorithm to use.

            Valid values are ``AES256`` for S3-managed encryption keys, or ``aws:kms`` for AWS KMS-managed encryption keys. If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see `Permissions requirements for S3 Tables SSE-KMS encryption <https://docs.aws.amazon.com//AmazonS3/latest/userguide/s3-tables-kms-permissions.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-tablebucket-encryptionconfiguration.html#cfn-s3tables-tablebucket-encryptionconfiguration-ssealgorithm
            '''
            result = self._values.get("sse_algorithm")
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
        jsii_type="aws-cdk-lib.aws_s3tables.CfnTableBucket.UnreferencedFileRemovalProperty",
        jsii_struct_bases=[],
        name_mapping={
            "noncurrent_days": "noncurrentDays",
            "status": "status",
            "unreferenced_days": "unreferencedDays",
        },
    )
    class UnreferencedFileRemovalProperty:
        def __init__(
            self,
            *,
            noncurrent_days: typing.Optional[jsii.Number] = None,
            status: typing.Optional[builtins.str] = None,
            unreferenced_days: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The unreferenced file removal settings for your table bucket.

            Unreferenced file removal identifies and deletes all objects that are not referenced by any table snapshots. For more information, see the `*Amazon S3 User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html>`_ .

            :param noncurrent_days: The number of days an object can be noncurrent before Amazon S3 deletes it.
            :param status: The status of the unreferenced file removal configuration for your table bucket.
            :param unreferenced_days: The number of days an object must be unreferenced by your table before Amazon S3 marks the object as noncurrent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-tablebucket-unreferencedfileremoval.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3tables as s3tables
                
                unreferenced_file_removal_property = s3tables.CfnTableBucket.UnreferencedFileRemovalProperty(
                    noncurrent_days=123,
                    status="status",
                    unreferenced_days=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e5a5e0b11a3cbe8be01a72f3ac6efc85af9472104c94585d26f630d3354c816b)
                check_type(argname="argument noncurrent_days", value=noncurrent_days, expected_type=type_hints["noncurrent_days"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument unreferenced_days", value=unreferenced_days, expected_type=type_hints["unreferenced_days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if noncurrent_days is not None:
                self._values["noncurrent_days"] = noncurrent_days
            if status is not None:
                self._values["status"] = status
            if unreferenced_days is not None:
                self._values["unreferenced_days"] = unreferenced_days

        @builtins.property
        def noncurrent_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days an object can be noncurrent before Amazon S3 deletes it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-tablebucket-unreferencedfileremoval.html#cfn-s3tables-tablebucket-unreferencedfileremoval-noncurrentdays
            '''
            result = self._values.get("noncurrent_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The status of the unreferenced file removal configuration for your table bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-tablebucket-unreferencedfileremoval.html#cfn-s3tables-tablebucket-unreferencedfileremoval-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unreferenced_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days an object must be unreferenced by your table before Amazon S3 marks the object as noncurrent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3tables-tablebucket-unreferencedfileremoval.html#cfn-s3tables-tablebucket-unreferencedfileremoval-unreferenceddays
            '''
            result = self._values.get("unreferenced_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UnreferencedFileRemovalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnTableBucketPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3tables.CfnTableBucketPolicy",
):
    '''Creates a new maintenance configuration or replaces an existing table bucket policy for a table bucket.

    For more information, see `Adding a table bucket policy <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-bucket-policy.html#table-bucket-policy-add>`_ in the *Amazon Simple Storage Service User Guide* .

    - **Permissions** - You must have the ``s3tables:PutTableBucketPolicy`` permission to use this operation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucketpolicy.html
    :cloudformationResource: AWS::S3Tables::TableBucketPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3tables as s3tables
        
        # resource_policy: Any
        
        cfn_table_bucket_policy = s3tables.CfnTableBucketPolicy(self, "MyCfnTableBucketPolicy",
            resource_policy=resource_policy,
            table_bucket_arn="tableBucketArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resource_policy: typing.Any,
        table_bucket_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resource_policy: The bucket policy JSON for the table bucket.
        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e41d1f33249c074a27c8db71a0d74f7ec78216836901a699d5ff7dbdcfdcf89a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTableBucketPolicyProps(
            resource_policy=resource_policy, table_bucket_arn=table_bucket_arn
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a8346fde6b51dff587833e7cd68ccdd12e4f80b4b07e756c507ac9d8b81cfdb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__32d2b3e7f152d93640c11f17b345fb2a9bf95efe6dd3c1235a1d9ca148caae1a)
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
    @jsii.member(jsii_name="resourcePolicy")
    def resource_policy(self) -> typing.Any:
        '''The bucket policy JSON for the table bucket.'''
        return typing.cast(typing.Any, jsii.get(self, "resourcePolicy"))

    @resource_policy.setter
    def resource_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60d686568fe0e9bc1be86d3585b33d6e6dcf5d8ec00b2b4b4ba9c5e48ea4cd82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourcePolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tableBucketArn")
    def table_bucket_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the table bucket.'''
        return typing.cast(builtins.str, jsii.get(self, "tableBucketArn"))

    @table_bucket_arn.setter
    def table_bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9db770e8febae7602179359c1a5975b5ae8be6270348474fc3a1cca79c47ad2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableBucketArn", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3tables.CfnTableBucketPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "resource_policy": "resourcePolicy",
        "table_bucket_arn": "tableBucketArn",
    },
)
class CfnTableBucketPolicyProps:
    def __init__(
        self,
        *,
        resource_policy: typing.Any,
        table_bucket_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnTableBucketPolicy``.

        :param resource_policy: The bucket policy JSON for the table bucket.
        :param table_bucket_arn: The Amazon Resource Name (ARN) of the table bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucketpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3tables as s3tables
            
            # resource_policy: Any
            
            cfn_table_bucket_policy_props = s3tables.CfnTableBucketPolicyProps(
                resource_policy=resource_policy,
                table_bucket_arn="tableBucketArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df8972559ed3d0ff90d01d70d1cf8f77869398b91f03a408d49a7b5bee0615a0)
            check_type(argname="argument resource_policy", value=resource_policy, expected_type=type_hints["resource_policy"])
            check_type(argname="argument table_bucket_arn", value=table_bucket_arn, expected_type=type_hints["table_bucket_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_policy": resource_policy,
            "table_bucket_arn": table_bucket_arn,
        }

    @builtins.property
    def resource_policy(self) -> typing.Any:
        '''The bucket policy JSON for the table bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucketpolicy.html#cfn-s3tables-tablebucketpolicy-resourcepolicy
        '''
        result = self._values.get("resource_policy")
        assert result is not None, "Required property 'resource_policy' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def table_bucket_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the table bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucketpolicy.html#cfn-s3tables-tablebucketpolicy-tablebucketarn
        '''
        result = self._values.get("table_bucket_arn")
        assert result is not None, "Required property 'table_bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTableBucketPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3tables.CfnTableBucketProps",
    jsii_struct_bases=[],
    name_mapping={
        "table_bucket_name": "tableBucketName",
        "encryption_configuration": "encryptionConfiguration",
        "unreferenced_file_removal": "unreferencedFileRemoval",
    },
)
class CfnTableBucketProps:
    def __init__(
        self,
        *,
        table_bucket_name: builtins.str,
        encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTableBucket.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        unreferenced_file_removal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTableBucket.UnreferencedFileRemovalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTableBucket``.

        :param table_bucket_name: The name for the table bucket.
        :param encryption_configuration: Configuration specifying how data should be encrypted. This structure defines the encryption algorithm and optional KMS key to be used for server-side encryption.
        :param unreferenced_file_removal: The unreferenced file removal settings for your table bucket. Unreferenced file removal identifies and deletes all objects that are not referenced by any table snapshots. For more information, see the `*Amazon S3 User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucket.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3tables as s3tables
            
            cfn_table_bucket_props = s3tables.CfnTableBucketProps(
                table_bucket_name="tableBucketName",
            
                # the properties below are optional
                encryption_configuration=s3tables.CfnTableBucket.EncryptionConfigurationProperty(
                    kms_key_arn="kmsKeyArn",
                    sse_algorithm="sseAlgorithm"
                ),
                unreferenced_file_removal=s3tables.CfnTableBucket.UnreferencedFileRemovalProperty(
                    noncurrent_days=123,
                    status="status",
                    unreferenced_days=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fb9342a13c0e9f7b21679814e793d7ccc0964ccfe53bc5e0916676b628d20f3)
            check_type(argname="argument table_bucket_name", value=table_bucket_name, expected_type=type_hints["table_bucket_name"])
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument unreferenced_file_removal", value=unreferenced_file_removal, expected_type=type_hints["unreferenced_file_removal"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table_bucket_name": table_bucket_name,
        }
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if unreferenced_file_removal is not None:
            self._values["unreferenced_file_removal"] = unreferenced_file_removal

    @builtins.property
    def table_bucket_name(self) -> builtins.str:
        '''The name for the table bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucket.html#cfn-s3tables-tablebucket-tablebucketname
        '''
        result = self._values.get("table_bucket_name")
        assert result is not None, "Required property 'table_bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTableBucket.EncryptionConfigurationProperty]]:
        '''Configuration specifying how data should be encrypted.

        This structure defines the encryption algorithm and optional KMS key to be used for server-side encryption.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucket.html#cfn-s3tables-tablebucket-encryptionconfiguration
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTableBucket.EncryptionConfigurationProperty]], result)

    @builtins.property
    def unreferenced_file_removal(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTableBucket.UnreferencedFileRemovalProperty]]:
        '''The unreferenced file removal settings for your table bucket.

        Unreferenced file removal identifies and deletes all objects that are not referenced by any table snapshots. For more information, see the `*Amazon S3 User Guide* <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucket.html#cfn-s3tables-tablebucket-unreferencedfileremoval
        '''
        result = self._values.get("unreferenced_file_removal")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTableBucket.UnreferencedFileRemovalProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTableBucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTablePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3tables.CfnTablePolicy",
):
    '''Creates a new maintenance configuration or replaces an existing table policy for a table.

    For more information, see `Adding a table policy <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-table-policy.html#table-policy-add>`_ in the *Amazon Simple Storage Service User Guide* .

    - **Permissions** - You must have the ``s3tables:PutTablePolicy`` permission to use this operation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablepolicy.html
    :cloudformationResource: AWS::S3Tables::TablePolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3tables as s3tables
        
        # resource_policy: Any
        
        cfn_table_policy = s3tables.CfnTablePolicy(self, "MyCfnTablePolicy",
            resource_policy=resource_policy,
            table_arn="tableArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resource_policy: typing.Any,
        table_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resource_policy: 
        :param table_arn: The Amazon Resource Name (ARN) of the specified table.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a411c2784ec9f97ff20ac6b524d48b9d66affbbc6dde8cf88f11829983b62656)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTablePolicyProps(
            resource_policy=resource_policy, table_arn=table_arn
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0a3947da1bdccb78be78c5e73ba6a761b9581cfdb6fde618a0c2e2cc24e62e6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__79081d3da496e49f8054cf224d3c19c14084df9686495715d7c13deb2b01f4e5)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespace")
    def attr_namespace(self) -> builtins.str:
        '''The namespace that the table belongs to.

        :cloudformationAttribute: Namespace
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespace"))

    @builtins.property
    @jsii.member(jsii_name="attrTableBucketArn")
    def attr_table_bucket_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the specified table bucket.

        :cloudformationAttribute: TableBucketARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTableBucketArn"))

    @builtins.property
    @jsii.member(jsii_name="attrTableName")
    def attr_table_name(self) -> builtins.str:
        '''The name for the table.

        :cloudformationAttribute: TableName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTableName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="resourcePolicy")
    def resource_policy(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "resourcePolicy"))

    @resource_policy.setter
    def resource_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5ff64cf2723b6c321a7dae00772c6657abff46b53f326cb7ef2461494ecaead)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourcePolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tableArn")
    def table_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the specified table.'''
        return typing.cast(builtins.str, jsii.get(self, "tableArn"))

    @table_arn.setter
    def table_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87d38159ba1fcdcd6a78891e84e79fef3b2492c5066559f8f91cd5cc6191efe4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableArn", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3tables.CfnTablePolicyProps",
    jsii_struct_bases=[],
    name_mapping={"resource_policy": "resourcePolicy", "table_arn": "tableArn"},
)
class CfnTablePolicyProps:
    def __init__(self, *, resource_policy: typing.Any, table_arn: builtins.str) -> None:
        '''Properties for defining a ``CfnTablePolicy``.

        :param resource_policy: 
        :param table_arn: The Amazon Resource Name (ARN) of the specified table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3tables as s3tables
            
            # resource_policy: Any
            
            cfn_table_policy_props = s3tables.CfnTablePolicyProps(
                resource_policy=resource_policy,
                table_arn="tableArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e4efe8d2b5f3164478497385240c6eecce420e07f634572b7fac929a357ad5f)
            check_type(argname="argument resource_policy", value=resource_policy, expected_type=type_hints["resource_policy"])
            check_type(argname="argument table_arn", value=table_arn, expected_type=type_hints["table_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_policy": resource_policy,
            "table_arn": table_arn,
        }

    @builtins.property
    def resource_policy(self) -> typing.Any:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablepolicy.html#cfn-s3tables-tablepolicy-resourcepolicy
        '''
        result = self._values.get("resource_policy")
        assert result is not None, "Required property 'resource_policy' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def table_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the specified table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablepolicy.html#cfn-s3tables-tablepolicy-tablearn
        '''
        result = self._values.get("table_arn")
        assert result is not None, "Required property 'table_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTablePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3tables.CfnTableProps",
    jsii_struct_bases=[],
    name_mapping={
        "namespace": "namespace",
        "open_table_format": "openTableFormat",
        "table_bucket_arn": "tableBucketArn",
        "table_name": "tableName",
        "compaction": "compaction",
        "iceberg_metadata": "icebergMetadata",
        "snapshot_management": "snapshotManagement",
        "without_metadata": "withoutMetadata",
    },
)
class CfnTableProps:
    def __init__(
        self,
        *,
        namespace: builtins.str,
        open_table_format: builtins.str,
        table_bucket_arn: builtins.str,
        table_name: builtins.str,
        compaction: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.CompactionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        iceberg_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.IcebergMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        snapshot_management: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.SnapshotManagementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        without_metadata: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnTable``.

        :param namespace: The name of the namespace.
        :param open_table_format: Format of the table.
        :param table_bucket_arn: The Amazon Resource Name (ARN) of the specified table bucket.
        :param table_name: The name for the table.
        :param compaction: Settings governing the Compaction maintenance action. Contains details about the compaction settings for an Iceberg table.
        :param iceberg_metadata: Contains details about the metadata for an Iceberg table.
        :param snapshot_management: Contains details about the snapshot management settings for an Iceberg table. A snapshot is expired when it exceeds MinSnapshotsToKeep and MaxSnapshotAgeHours.
        :param without_metadata: Indicates that you don't want to specify a schema for the table. This property is mutually exclusive to 'IcebergMetadata', and its only possible value is 'Yes'.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-table.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3tables as s3tables
            
            cfn_table_props = s3tables.CfnTableProps(
                namespace="namespace",
                open_table_format="openTableFormat",
                table_bucket_arn="tableBucketArn",
                table_name="tableName",
            
                # the properties below are optional
                compaction=s3tables.CfnTable.CompactionProperty(
                    status="status",
                    target_file_size_mb=123
                ),
                iceberg_metadata=s3tables.CfnTable.IcebergMetadataProperty(
                    iceberg_schema=s3tables.CfnTable.IcebergSchemaProperty(
                        schema_field_list=[s3tables.CfnTable.SchemaFieldProperty(
                            name="name",
                            type="type",
            
                            # the properties below are optional
                            required=False
                        )]
                    )
                ),
                snapshot_management=s3tables.CfnTable.SnapshotManagementProperty(
                    max_snapshot_age_hours=123,
                    min_snapshots_to_keep=123,
                    status="status"
                ),
                without_metadata="withoutMetadata"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6346a05fb3e021dceca566705037999fa06de23c2e117b37dcdd3e46838b7bc6)
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument open_table_format", value=open_table_format, expected_type=type_hints["open_table_format"])
            check_type(argname="argument table_bucket_arn", value=table_bucket_arn, expected_type=type_hints["table_bucket_arn"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument compaction", value=compaction, expected_type=type_hints["compaction"])
            check_type(argname="argument iceberg_metadata", value=iceberg_metadata, expected_type=type_hints["iceberg_metadata"])
            check_type(argname="argument snapshot_management", value=snapshot_management, expected_type=type_hints["snapshot_management"])
            check_type(argname="argument without_metadata", value=without_metadata, expected_type=type_hints["without_metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "namespace": namespace,
            "open_table_format": open_table_format,
            "table_bucket_arn": table_bucket_arn,
            "table_name": table_name,
        }
        if compaction is not None:
            self._values["compaction"] = compaction
        if iceberg_metadata is not None:
            self._values["iceberg_metadata"] = iceberg_metadata
        if snapshot_management is not None:
            self._values["snapshot_management"] = snapshot_management
        if without_metadata is not None:
            self._values["without_metadata"] = without_metadata

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The name of the namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-table.html#cfn-s3tables-table-namespace
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def open_table_format(self) -> builtins.str:
        '''Format of the table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-table.html#cfn-s3tables-table-opentableformat
        '''
        result = self._values.get("open_table_format")
        assert result is not None, "Required property 'open_table_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_bucket_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the specified table bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-table.html#cfn-s3tables-table-tablebucketarn
        '''
        result = self._values.get("table_bucket_arn")
        assert result is not None, "Required property 'table_bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''The name for the table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-table.html#cfn-s3tables-table-tablename
        '''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compaction(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTable.CompactionProperty]]:
        '''Settings governing the Compaction maintenance action.

        Contains details about the compaction settings for an Iceberg table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-table.html#cfn-s3tables-table-compaction
        '''
        result = self._values.get("compaction")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTable.CompactionProperty]], result)

    @builtins.property
    def iceberg_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTable.IcebergMetadataProperty]]:
        '''Contains details about the metadata for an Iceberg table.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-table.html#cfn-s3tables-table-icebergmetadata
        '''
        result = self._values.get("iceberg_metadata")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTable.IcebergMetadataProperty]], result)

    @builtins.property
    def snapshot_management(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTable.SnapshotManagementProperty]]:
        '''Contains details about the snapshot management settings for an Iceberg table.

        A snapshot is expired when it exceeds MinSnapshotsToKeep and MaxSnapshotAgeHours.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-table.html#cfn-s3tables-table-snapshotmanagement
        '''
        result = self._values.get("snapshot_management")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTable.SnapshotManagementProperty]], result)

    @builtins.property
    def without_metadata(self) -> typing.Optional[builtins.str]:
        '''Indicates that you don't want to specify a schema for the table.

        This property is mutually exclusive to 'IcebergMetadata', and its only possible value is 'Yes'.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-table.html#cfn-s3tables-table-withoutmetadata
        '''
        result = self._values.get("without_metadata")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnNamespace",
    "CfnNamespaceProps",
    "CfnTable",
    "CfnTableBucket",
    "CfnTableBucketPolicy",
    "CfnTableBucketPolicyProps",
    "CfnTableBucketProps",
    "CfnTablePolicy",
    "CfnTablePolicyProps",
    "CfnTableProps",
]

publication.publish()

def _typecheckingstub__fd79dcff4893fe1cd3464c1f48689d2a01ad4a5eed6acfd35e21266683ab1f1c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    namespace: builtins.str,
    table_bucket_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dae368df5e118b03066ac5fbad3765e81aa23b31a7288aa2bb824379578614f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c772aad560ab6b4e840f54665ca3a18a9fcbf362512eb78423617db138b70b0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__083038783d9a592008992f105965913f4b10d8bc23252afb9a929c22e7cebd06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8560b7f29623bc1f753b1cf34442c874c6958096b39accf37244c9341879fd81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fdadc8758c9f96fac22200567c0d51cfd3e36c943cb9fa46e50cbf9abf25faf(
    *,
    namespace: builtins.str,
    table_bucket_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cb6d8b27037c33c46017d3b0b00b52a14bbd8c0a922c03aca7fff9e327b1420(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    namespace: builtins.str,
    open_table_format: builtins.str,
    table_bucket_arn: builtins.str,
    table_name: builtins.str,
    compaction: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.CompactionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iceberg_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.IcebergMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snapshot_management: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.SnapshotManagementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    without_metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e9f0a1074447de044514c7c1b5b2cca167912d3e02c228b501f3cc4c1b09a6f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a82da714fe9043c593e17c8af3ba9310ce4d043a6843c815aa933a3f004a6d5a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb40731dfd6256164661895ce0f48c78b8e18c58fb7f27fbb73a3ce7c916c1df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5892a05d87447cee97d5ab4f41ddb7d6837df87a8b4e6b9d577c79cfe927180a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ad6ac8e43e44c04006a5ef80e152c8effbbdb7bf127bd063a6b732c4ee1f9a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f410c91375a77f7ed3b5736522dbfb254643b931cd30ea49af6d7d51d9c5ddc5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ff6f95f778b64c53b87dfe6f8a117fa9d1583584d475eef7586c75859dcb219(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTable.CompactionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f0509a656c9927b41c3ead9b58d6c83257863d2b8d1104c542e1a8435be4160(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTable.IcebergMetadataProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6c432f4785ee47d59f072204756d42650b9fc3dd3e85a79139ab4f11fb72a43(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTable.SnapshotManagementProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5d21acaabd2bab58c6f59f334d1b06b0962eb6541244a042a933b5ce009a061(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f49118bb06f06baf9f7618e6cd633803a2486d06b541e59cab8801a6a0983fcc(
    *,
    status: typing.Optional[builtins.str] = None,
    target_file_size_mb: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e5dc7085346ad722ba37251e910871affc6e3d90d9251cc9d43941978d7cb0a(
    *,
    iceberg_schema: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.IcebergSchemaProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3613cb002c55c4baeb2517f3445ed9e71396e5ee393d230544d3f1302b471205(
    *,
    schema_field_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.SchemaFieldProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3f6368f6b334e97c5c50a43ab04d5e784e18fdb0e687d1684b9ad01ad6c1a29(
    *,
    name: builtins.str,
    type: builtins.str,
    required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa9c2ac7b8956daecf8522166700dd475625d08f131913fda8e01475215f3656(
    *,
    max_snapshot_age_hours: typing.Optional[jsii.Number] = None,
    min_snapshots_to_keep: typing.Optional[jsii.Number] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de433918cd34eecbcaab0e81b6a287f71a48dd308c2f4d42e07a0e19ce5af0e2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    table_bucket_name: builtins.str,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTableBucket.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    unreferenced_file_removal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTableBucket.UnreferencedFileRemovalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40da426af74874eef485654394ab5db25ba5f82e8490b96bd68d9f6318b6654e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e15cdb1ab81b354e389c0debd6b2b9d760245945e38c20d735044cde53c3979(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42ef5079e6a92822a2e6ccbb91b02661f493a7d44dc79dfba0916840dbe44863(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61499f569b4e5dc20b99defd26e29c6e9b7761b6630e1adec9c20e97e099dd4a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTableBucket.EncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02bf42691243dcbc8ea49c2499d3414260e70a80c4e38a371b64664c49f17e6e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTableBucket.UnreferencedFileRemovalProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__659e946ab1ee4bc0eb13a519adc57d2cb4431347d47a9e6cb4d4086a87be1b2a(
    *,
    kms_key_arn: typing.Optional[builtins.str] = None,
    sse_algorithm: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5a5e0b11a3cbe8be01a72f3ac6efc85af9472104c94585d26f630d3354c816b(
    *,
    noncurrent_days: typing.Optional[jsii.Number] = None,
    status: typing.Optional[builtins.str] = None,
    unreferenced_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e41d1f33249c074a27c8db71a0d74f7ec78216836901a699d5ff7dbdcfdcf89a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resource_policy: typing.Any,
    table_bucket_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a8346fde6b51dff587833e7cd68ccdd12e4f80b4b07e756c507ac9d8b81cfdb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32d2b3e7f152d93640c11f17b345fb2a9bf95efe6dd3c1235a1d9ca148caae1a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60d686568fe0e9bc1be86d3585b33d6e6dcf5d8ec00b2b4b4ba9c5e48ea4cd82(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9db770e8febae7602179359c1a5975b5ae8be6270348474fc3a1cca79c47ad2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df8972559ed3d0ff90d01d70d1cf8f77869398b91f03a408d49a7b5bee0615a0(
    *,
    resource_policy: typing.Any,
    table_bucket_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fb9342a13c0e9f7b21679814e793d7ccc0964ccfe53bc5e0916676b628d20f3(
    *,
    table_bucket_name: builtins.str,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTableBucket.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    unreferenced_file_removal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTableBucket.UnreferencedFileRemovalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a411c2784ec9f97ff20ac6b524d48b9d66affbbc6dde8cf88f11829983b62656(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resource_policy: typing.Any,
    table_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0a3947da1bdccb78be78c5e73ba6a761b9581cfdb6fde618a0c2e2cc24e62e6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79081d3da496e49f8054cf224d3c19c14084df9686495715d7c13deb2b01f4e5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5ff64cf2723b6c321a7dae00772c6657abff46b53f326cb7ef2461494ecaead(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87d38159ba1fcdcd6a78891e84e79fef3b2492c5066559f8f91cd5cc6191efe4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e4efe8d2b5f3164478497385240c6eecce420e07f634572b7fac929a357ad5f(
    *,
    resource_policy: typing.Any,
    table_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6346a05fb3e021dceca566705037999fa06de23c2e117b37dcdd3e46838b7bc6(
    *,
    namespace: builtins.str,
    open_table_format: builtins.str,
    table_bucket_arn: builtins.str,
    table_name: builtins.str,
    compaction: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.CompactionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iceberg_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.IcebergMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snapshot_management: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTable.SnapshotManagementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    without_metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
