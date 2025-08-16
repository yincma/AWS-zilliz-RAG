r'''
# AWS::DSQL Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_dsql as dsql
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DSQL construct libraries](https://constructs.dev/search?q=dsql)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DSQL resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DSQL.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DSQL](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DSQL.html).

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
class CfnCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dsql.CfnCluster",
):
    '''The ``AWS::DSQL::Cluster`` resource specifies an cluster. You can use this resource to create, modify, and manage clusters.

    This resource supports both single-Region clusters and multi-Region clusters through the ``MultiRegionProperties`` parameter.
    .. epigraph::

       Creating multi-Region clusters requires additional IAM permissions beyond those needed for single-Region clusters. > - The witness Region specified in ``multiRegionProperties.witnessRegion`` cannot be the same as the cluster's Region.

    *Required permissions*

    - **dsql:CreateCluster** - Required to create a cluster.

    Resources: ``arn:aws:dsql:region:account-id:cluster/*``

    - **dsql:TagResource** - Permission to add tags to a resource.

    Resources: ``arn:aws:dsql:region:account-id:cluster/*``

    - **dsql:PutMultiRegionProperties** - Permission to configure multi-Region properties for a cluster.

    Resources: ``arn:aws:dsql:region:account-id:cluster/*``

    - **dsql:AddPeerCluster** - When specifying ``multiRegionProperties.clusters`` , permission to add peer clusters.

    Resources:

    - Local cluster: ``arn:aws:dsql:region:account-id:cluster/*``
    - Each peer cluster: exact ARN of each specified peer cluster
    - **dsql:PutWitnessRegion** - When specifying ``multiRegionProperties.witnessRegion`` , permission to set a witness Region. This permission is checked both in the cluster Region and in the witness Region.

    Resources: ``arn:aws:dsql:region:account-id:cluster/*``

    Condition Keys: ``dsql:WitnessRegion`` (matching the specified witness region)

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dsql-cluster.html
    :cloudformationResource: AWS::DSQL::Cluster
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dsql as dsql
        
        cfn_cluster = dsql.CfnCluster(self, "MyCfnCluster",
            deletion_protection_enabled=False,
            kms_encryption_key="kmsEncryptionKey",
            multi_region_properties=dsql.CfnCluster.MultiRegionPropertiesProperty(
                clusters=["clusters"],
                witness_region="witnessRegion"
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
        deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        kms_encryption_key: typing.Optional[builtins.str] = None,
        multi_region_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.MultiRegionPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param deletion_protection_enabled: Whether deletion protection is enabled on this cluster.
        :param kms_encryption_key: The KMS key that encrypts data on the cluster.
        :param multi_region_properties: Defines the structure for multi-Region cluster configurations, containing the witness Region and peered cluster settings.
        :param tags: A map of key and value pairs this cluster is tagged with.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b82b76673b1942e60f823768c857e13a61b0491cdd1ca21c1f2a574e980d253e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(
            deletion_protection_enabled=deletion_protection_enabled,
            kms_encryption_key=kms_encryption_key,
            multi_region_properties=multi_region_properties,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b05414cc6a0a47d76a5604395b89b41d7f04f08f9b28ec25471d8d9dfd914483)
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
            type_hints = typing.get_type_hints(_typecheckingstub__89daa5d24060578a1ef99b50292d70f5dc9e43d808d9f1f6ce09b7a3dac27778)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The timestamp when the cluster was created, in ISO 8601 format.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrEncryptionDetails")
    def attr_encryption_details(self) -> _IResolvable_da3f097b:
        '''The encryption configuration details for the cluster.

        :cloudformationAttribute: EncryptionDetails
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrEncryptionDetails"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentifier")
    def attr_identifier(self) -> builtins.str:
        '''The unique identifier assigned to the cluster upon creation.

        :cloudformationAttribute: Identifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceArn")
    def attr_resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the cluster.

        Used for IAM permissions and resource identification.

        :cloudformationAttribute: ResourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current status of the cluster. Possible values include: CREATING, ACTIVE, DELETING, FAILED.

        The cluster can have two additional status values when working with multi-Region clusters:

        ``PENDING_SETUP`` —Indicates the cluster is being configured

        ``PENDING_DELETE`` —Indicates the cluster is being deleted

        *Note:* These status values only appear for multi-Region cluster operations.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcEndpointServiceName")
    def attr_vpc_endpoint_service_name(self) -> builtins.str:
        '''The VPC Endpoint Service name for the cluster.

        This can be used to create a VPC endpoint to connect to the cluster from within a VPC.

        :cloudformationAttribute: VpcEndpointServiceName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVpcEndpointServiceName"))

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
    @jsii.member(jsii_name="deletionProtectionEnabled")
    def deletion_protection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether deletion protection is enabled on this cluster.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "deletionProtectionEnabled"))

    @deletion_protection_enabled.setter
    def deletion_protection_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__393f500a888707295be5db6ececab65a69f1c1889e02c7043d1d8ad0ec5e7636)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtectionEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsEncryptionKey")
    def kms_encryption_key(self) -> typing.Optional[builtins.str]:
        '''The KMS key that encrypts data on the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsEncryptionKey"))

    @kms_encryption_key.setter
    def kms_encryption_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ae716ffcdd031c28de520d863a21a8cc04056fe6c3c1a6e658dd02ea3bae8eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsEncryptionKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="multiRegionProperties")
    def multi_region_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.MultiRegionPropertiesProperty"]]:
        '''Defines the structure for multi-Region cluster configurations, containing the witness Region and peered cluster settings.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.MultiRegionPropertiesProperty"]], jsii.get(self, "multiRegionProperties"))

    @multi_region_properties.setter
    def multi_region_properties(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.MultiRegionPropertiesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1cd42de6387e3057eda85830c6674c4cac74a5be160e21869cc4c1b3274381c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiRegionProperties", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map of key and value pairs this cluster is tagged with.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9eb2f89b2e4104fba43d8d14808715e2f3435951317df69258fecf9b606d598)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dsql.CfnCluster.EncryptionDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_status": "encryptionStatus",
            "encryption_type": "encryptionType",
            "kms_key_arn": "kmsKeyArn",
        },
    )
    class EncryptionDetailsProperty:
        def __init__(
            self,
            *,
            encryption_status: typing.Optional[builtins.str] = None,
            encryption_type: typing.Optional[builtins.str] = None,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration details about encryption for the cluster including the AWS KMS key ARN, encryption type, and encryption status.

            :param encryption_status: The status of encryption for the cluster.
            :param encryption_type: The type of encryption that protects the data on your cluster.
            :param kms_key_arn: The ARN of the AWS KMS key that encrypts data in the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dsql-cluster-encryptiondetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dsql as dsql
                
                encryption_details_property = dsql.CfnCluster.EncryptionDetailsProperty(
                    encryption_status="encryptionStatus",
                    encryption_type="encryptionType",
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dd4156a8f1ca33d4dc585a1af5623fff8b945e08734aa29b92ad1fc93a6bccd0)
                check_type(argname="argument encryption_status", value=encryption_status, expected_type=type_hints["encryption_status"])
                check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encryption_status is not None:
                self._values["encryption_status"] = encryption_status
            if encryption_type is not None:
                self._values["encryption_type"] = encryption_type
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def encryption_status(self) -> typing.Optional[builtins.str]:
            '''The status of encryption for the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dsql-cluster-encryptiondetails.html#cfn-dsql-cluster-encryptiondetails-encryptionstatus
            '''
            result = self._values.get("encryption_status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_type(self) -> typing.Optional[builtins.str]:
            '''The type of encryption that protects the data on your cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dsql-cluster-encryptiondetails.html#cfn-dsql-cluster-encryptiondetails-encryptiontype
            '''
            result = self._values.get("encryption_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the AWS KMS key that encrypts data in the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dsql-cluster-encryptiondetails.html#cfn-dsql-cluster-encryptiondetails-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dsql.CfnCluster.MultiRegionPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"clusters": "clusters", "witness_region": "witnessRegion"},
    )
    class MultiRegionPropertiesProperty:
        def __init__(
            self,
            *,
            clusters: typing.Optional[typing.Sequence[builtins.str]] = None,
            witness_region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines the structure for multi-Region cluster configurations, containing the witness Region and peered cluster settings.

            :param clusters: The set of peered clusters that form the multi-Region cluster configuration. Each peered cluster represents a database instance in a different Region.
            :param witness_region: The Region that serves as the witness Region for a multi-Region cluster. The witness Region helps maintain cluster consistency and quorum.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dsql-cluster-multiregionproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dsql as dsql
                
                multi_region_properties_property = dsql.CfnCluster.MultiRegionPropertiesProperty(
                    clusters=["clusters"],
                    witness_region="witnessRegion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b9a11b947e8fa036630c80e949e1619ff609036ee5de58658c8157988d8c212f)
                check_type(argname="argument clusters", value=clusters, expected_type=type_hints["clusters"])
                check_type(argname="argument witness_region", value=witness_region, expected_type=type_hints["witness_region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if clusters is not None:
                self._values["clusters"] = clusters
            if witness_region is not None:
                self._values["witness_region"] = witness_region

        @builtins.property
        def clusters(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The set of peered clusters that form the multi-Region cluster configuration.

            Each peered cluster represents a database instance in a different Region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dsql-cluster-multiregionproperties.html#cfn-dsql-cluster-multiregionproperties-clusters
            '''
            result = self._values.get("clusters")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def witness_region(self) -> typing.Optional[builtins.str]:
            '''The Region that serves as the witness Region for a multi-Region cluster.

            The witness Region helps maintain cluster consistency and quorum.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dsql-cluster-multiregionproperties.html#cfn-dsql-cluster-multiregionproperties-witnessregion
            '''
            result = self._values.get("witness_region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MultiRegionPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dsql.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "deletion_protection_enabled": "deletionProtectionEnabled",
        "kms_encryption_key": "kmsEncryptionKey",
        "multi_region_properties": "multiRegionProperties",
        "tags": "tags",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        kms_encryption_key: typing.Optional[builtins.str] = None,
        multi_region_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.MultiRegionPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCluster``.

        :param deletion_protection_enabled: Whether deletion protection is enabled on this cluster.
        :param kms_encryption_key: The KMS key that encrypts data on the cluster.
        :param multi_region_properties: Defines the structure for multi-Region cluster configurations, containing the witness Region and peered cluster settings.
        :param tags: A map of key and value pairs this cluster is tagged with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dsql-cluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dsql as dsql
            
            cfn_cluster_props = dsql.CfnClusterProps(
                deletion_protection_enabled=False,
                kms_encryption_key="kmsEncryptionKey",
                multi_region_properties=dsql.CfnCluster.MultiRegionPropertiesProperty(
                    clusters=["clusters"],
                    witness_region="witnessRegion"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c99b78beafe41f2e25cbcc0b8a8aff58ff66a77464bef06dbf9128ff75ebd08c)
            check_type(argname="argument deletion_protection_enabled", value=deletion_protection_enabled, expected_type=type_hints["deletion_protection_enabled"])
            check_type(argname="argument kms_encryption_key", value=kms_encryption_key, expected_type=type_hints["kms_encryption_key"])
            check_type(argname="argument multi_region_properties", value=multi_region_properties, expected_type=type_hints["multi_region_properties"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if deletion_protection_enabled is not None:
            self._values["deletion_protection_enabled"] = deletion_protection_enabled
        if kms_encryption_key is not None:
            self._values["kms_encryption_key"] = kms_encryption_key
        if multi_region_properties is not None:
            self._values["multi_region_properties"] = multi_region_properties
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def deletion_protection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether deletion protection is enabled on this cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dsql-cluster.html#cfn-dsql-cluster-deletionprotectionenabled
        '''
        result = self._values.get("deletion_protection_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def kms_encryption_key(self) -> typing.Optional[builtins.str]:
        '''The KMS key that encrypts data on the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dsql-cluster.html#cfn-dsql-cluster-kmsencryptionkey
        '''
        result = self._values.get("kms_encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multi_region_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.MultiRegionPropertiesProperty]]:
        '''Defines the structure for multi-Region cluster configurations, containing the witness Region and peered cluster settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dsql-cluster.html#cfn-dsql-cluster-multiregionproperties
        '''
        result = self._values.get("multi_region_properties")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.MultiRegionPropertiesProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map of key and value pairs this cluster is tagged with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dsql-cluster.html#cfn-dsql-cluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCluster",
    "CfnClusterProps",
]

publication.publish()

def _typecheckingstub__b82b76673b1942e60f823768c857e13a61b0491cdd1ca21c1f2a574e980d253e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kms_encryption_key: typing.Optional[builtins.str] = None,
    multi_region_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.MultiRegionPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b05414cc6a0a47d76a5604395b89b41d7f04f08f9b28ec25471d8d9dfd914483(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89daa5d24060578a1ef99b50292d70f5dc9e43d808d9f1f6ce09b7a3dac27778(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__393f500a888707295be5db6ececab65a69f1c1889e02c7043d1d8ad0ec5e7636(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ae716ffcdd031c28de520d863a21a8cc04056fe6c3c1a6e658dd02ea3bae8eb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1cd42de6387e3057eda85830c6674c4cac74a5be160e21869cc4c1b3274381c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.MultiRegionPropertiesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9eb2f89b2e4104fba43d8d14808715e2f3435951317df69258fecf9b606d598(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd4156a8f1ca33d4dc585a1af5623fff8b945e08734aa29b92ad1fc93a6bccd0(
    *,
    encryption_status: typing.Optional[builtins.str] = None,
    encryption_type: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9a11b947e8fa036630c80e949e1619ff609036ee5de58658c8157988d8c212f(
    *,
    clusters: typing.Optional[typing.Sequence[builtins.str]] = None,
    witness_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c99b78beafe41f2e25cbcc0b8a8aff58ff66a77464bef06dbf9128ff75ebd08c(
    *,
    deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kms_encryption_key: typing.Optional[builtins.str] = None,
    multi_region_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.MultiRegionPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
