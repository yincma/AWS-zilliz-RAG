r'''
# AWS::WorkspacesInstances Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_workspacesinstances as workspacesinstances
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for WorkspacesInstances construct libraries](https://constructs.dev/search?q=workspacesinstances)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::WorkspacesInstances resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WorkspacesInstances.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::WorkspacesInstances](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WorkspacesInstances.html).

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


@jsii.implements(_IInspectable_c2943556)
class CfnVolume(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnVolume",
):
    '''Resource Type definition for AWS::WorkspacesInstances::Volume - Manages WorkSpaces Volume resources.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volume.html
    :cloudformationResource: AWS::WorkspacesInstances::Volume
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_workspacesinstances as workspacesinstances
        
        cfn_volume = workspacesinstances.CfnVolume(self, "MyCfnVolume",
            availability_zone="availabilityZone",
        
            # the properties below are optional
            encrypted=False,
            iops=123,
            kms_key_id="kmsKeyId",
            size_in_gb=123,
            snapshot_id="snapshotId",
            tag_specifications=[workspacesinstances.CfnVolume.TagSpecificationProperty(
                resource_type="resourceType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )],
            throughput=123,
            volume_type="volumeType"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        availability_zone: builtins.str,
        encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        size_in_gb: typing.Optional[jsii.Number] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        tag_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnVolume.TagSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param availability_zone: The Availability Zone in which to create the volume.
        :param encrypted: Indicates whether the volume should be encrypted.
        :param iops: The number of I/O operations per second (IOPS).
        :param kms_key_id: The identifier of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use for Amazon EBS encryption.
        :param size_in_gb: The size of the volume, in GiBs.
        :param snapshot_id: The snapshot from which to create the volume.
        :param tag_specifications: The tags passed to EBS volume.
        :param throughput: The throughput to provision for a volume, with a maximum of 1,000 MiB/s.
        :param volume_type: The volume type.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f8f538e7b445e64dae7c3f3fa5cbf03f73a9175df0c28d38e372410d7a38644)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVolumeProps(
            availability_zone=availability_zone,
            encrypted=encrypted,
            iops=iops,
            kms_key_id=kms_key_id,
            size_in_gb=size_in_gb,
            snapshot_id=snapshot_id,
            tag_specifications=tag_specifications,
            throughput=throughput,
            volume_type=volume_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__685ee3c99d00c4a98137add5e1954d76422417da17f64b863cea2c0824dea902)
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
            type_hints = typing.get_type_hints(_typecheckingstub__50ddfbc291d3e556ace0dc6e9d82cfedb078a4a3cbb9ef9e8eac039d0e82d9e6)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrVolumeId")
    def attr_volume_id(self) -> builtins.str:
        '''Unique identifier for the volume.

        :cloudformationAttribute: VolumeId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVolumeId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> builtins.str:
        '''The Availability Zone in which to create the volume.'''
        return typing.cast(builtins.str, jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9f5f1fdafc059b4dc0f72801057c79e690b2878e7ac2fdf540ab305cb1db5b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="encrypted")
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the volume should be encrypted.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "encrypted"))

    @encrypted.setter
    def encrypted(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2545bcf2397b591eeb5bc2020672daea19e4969515b96c2982ba337dfe90a159)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypted", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> typing.Optional[jsii.Number]:
        '''The number of I/O operations per second (IOPS).'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed1876d81e0f42a3b54883c4648bf7cf155fa880a498cacc96a0945d5032084c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use for Amazon EBS encryption.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__395b2ede7d0057a6fa453fc8de076050bcc1806edcbaeecc76c37f56b5befabc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sizeInGb")
    def size_in_gb(self) -> typing.Optional[jsii.Number]:
        '''The size of the volume, in GiBs.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInGb"))

    @size_in_gb.setter
    def size_in_gb(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac8bac9f32006bab210d99c61fa194ffe0daa28445242538135f5024937fed35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeInGb", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="snapshotId")
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''The snapshot from which to create the volume.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotId"))

    @snapshot_id.setter
    def snapshot_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d59cb75f780fcc1524e9d8f2469747f8c6f2bbfc350d8662efddf91bcec54be4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagSpecifications")
    def tag_specifications(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnVolume.TagSpecificationProperty"]]]]:
        '''The tags passed to EBS volume.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnVolume.TagSpecificationProperty"]]]], jsii.get(self, "tagSpecifications"))

    @tag_specifications.setter
    def tag_specifications(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnVolume.TagSpecificationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7afbacaf7f3ea12aff8077fba424159c4a78dabec81d0e15c2cf21552d0eca48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagSpecifications", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''The throughput to provision for a volume, with a maximum of 1,000 MiB/s.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd4dae6ee80b4f1583ff940c92723ae5abc6127d8abd48ca72184266298e68d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''The volume type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ce69be7eab4b12a5677916d7b89ed00c676fbd7d9858d3c8fd894ed8a963d70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnVolume.TagSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_type": "resourceType", "tags": "tags"},
    )
    class TagSpecificationProperty:
        def __init__(
            self,
            *,
            resource_type: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param resource_type: 
            :param tags: The tags to apply to the resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-volume-tagspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                tag_specification_property = workspacesinstances.CfnVolume.TagSpecificationProperty(
                    resource_type="resourceType",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0902e5172f6b16ac0cad62cbc3b7188ce843a8d38d90dcc5c86591e6acf47988)
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if resource_type is not None:
                self._values["resource_type"] = resource_type
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def resource_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-volume-tagspecification.html#cfn-workspacesinstances-volume-tagspecification-resourcetype
            '''
            result = self._values.get("resource_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''The tags to apply to the resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-volume-tagspecification.html#cfn-workspacesinstances-volume-tagspecification-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnVolumeAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnVolumeAssociation",
):
    '''Resource Type definition for AWS::WorkspacesInstances::VolumeAssociation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volumeassociation.html
    :cloudformationResource: AWS::WorkspacesInstances::VolumeAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_workspacesinstances as workspacesinstances
        
        cfn_volume_association = workspacesinstances.CfnVolumeAssociation(self, "MyCfnVolumeAssociation",
            device="device",
            volume_id="volumeId",
            workspace_instance_id="workspaceInstanceId",
        
            # the properties below are optional
            disassociate_mode="disassociateMode"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        device: builtins.str,
        volume_id: builtins.str,
        workspace_instance_id: builtins.str,
        disassociate_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param device: The device name for the volume attachment.
        :param volume_id: ID of the volume to attach to the workspace instance.
        :param workspace_instance_id: ID of the workspace instance to associate with the volume.
        :param disassociate_mode: Mode to use when disassociating the volume.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7eec0daa83c1024898d2dd124cb4f461e56903d8a98401eb4d02742f55a5ba8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVolumeAssociationProps(
            device=device,
            volume_id=volume_id,
            workspace_instance_id=workspace_instance_id,
            disassociate_mode=disassociate_mode,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fd0989a57e9649b7a4d590f7c91b99524c0760e7a9573d04c9a0651e66ba9b4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9edb2ba816767d7bd7866452c6fad9e22e451376ace13728983cb1007430d513)
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
    @jsii.member(jsii_name="device")
    def device(self) -> builtins.str:
        '''The device name for the volume attachment.'''
        return typing.cast(builtins.str, jsii.get(self, "device"))

    @device.setter
    def device(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2c067e418598328cb19e2ca662460d196bbf4f0edd016a89d56ca6b09b96ae9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "device", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        '''ID of the volume to attach to the workspace instance.'''
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @volume_id.setter
    def volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c66f015cf8f3049bd728d95ffef2a32c21bd81393c29537303adaf4e86d6829)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="workspaceInstanceId")
    def workspace_instance_id(self) -> builtins.str:
        '''ID of the workspace instance to associate with the volume.'''
        return typing.cast(builtins.str, jsii.get(self, "workspaceInstanceId"))

    @workspace_instance_id.setter
    def workspace_instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb0e90de13632397d9f05ecf786f58d468973d0cf21a6f5c435c070b2c03b819)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceInstanceId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="disassociateMode")
    def disassociate_mode(self) -> typing.Optional[builtins.str]:
        '''Mode to use when disassociating the volume.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "disassociateMode"))

    @disassociate_mode.setter
    def disassociate_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1139240ee9e52471c21751caa541f36622002b63b2edb0a487ae73612ae098a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disassociateMode", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnVolumeAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "device": "device",
        "volume_id": "volumeId",
        "workspace_instance_id": "workspaceInstanceId",
        "disassociate_mode": "disassociateMode",
    },
)
class CfnVolumeAssociationProps:
    def __init__(
        self,
        *,
        device: builtins.str,
        volume_id: builtins.str,
        workspace_instance_id: builtins.str,
        disassociate_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnVolumeAssociation``.

        :param device: The device name for the volume attachment.
        :param volume_id: ID of the volume to attach to the workspace instance.
        :param workspace_instance_id: ID of the workspace instance to associate with the volume.
        :param disassociate_mode: Mode to use when disassociating the volume.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volumeassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_workspacesinstances as workspacesinstances
            
            cfn_volume_association_props = workspacesinstances.CfnVolumeAssociationProps(
                device="device",
                volume_id="volumeId",
                workspace_instance_id="workspaceInstanceId",
            
                # the properties below are optional
                disassociate_mode="disassociateMode"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f051309343f88ebe1cc3dc3f2fff77a39c42174a07969dff75f195781a41fbf)
            check_type(argname="argument device", value=device, expected_type=type_hints["device"])
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument workspace_instance_id", value=workspace_instance_id, expected_type=type_hints["workspace_instance_id"])
            check_type(argname="argument disassociate_mode", value=disassociate_mode, expected_type=type_hints["disassociate_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device": device,
            "volume_id": volume_id,
            "workspace_instance_id": workspace_instance_id,
        }
        if disassociate_mode is not None:
            self._values["disassociate_mode"] = disassociate_mode

    @builtins.property
    def device(self) -> builtins.str:
        '''The device name for the volume attachment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volumeassociation.html#cfn-workspacesinstances-volumeassociation-device
        '''
        result = self._values.get("device")
        assert result is not None, "Required property 'device' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''ID of the volume to attach to the workspace instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volumeassociation.html#cfn-workspacesinstances-volumeassociation-volumeid
        '''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_instance_id(self) -> builtins.str:
        '''ID of the workspace instance to associate with the volume.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volumeassociation.html#cfn-workspacesinstances-volumeassociation-workspaceinstanceid
        '''
        result = self._values.get("workspace_instance_id")
        assert result is not None, "Required property 'workspace_instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disassociate_mode(self) -> typing.Optional[builtins.str]:
        '''Mode to use when disassociating the volume.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volumeassociation.html#cfn-workspacesinstances-volumeassociation-disassociatemode
        '''
        result = self._values.get("disassociate_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVolumeAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnVolumeProps",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zone": "availabilityZone",
        "encrypted": "encrypted",
        "iops": "iops",
        "kms_key_id": "kmsKeyId",
        "size_in_gb": "sizeInGb",
        "snapshot_id": "snapshotId",
        "tag_specifications": "tagSpecifications",
        "throughput": "throughput",
        "volume_type": "volumeType",
    },
)
class CfnVolumeProps:
    def __init__(
        self,
        *,
        availability_zone: builtins.str,
        encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        iops: typing.Optional[jsii.Number] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        size_in_gb: typing.Optional[jsii.Number] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        tag_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVolume.TagSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnVolume``.

        :param availability_zone: The Availability Zone in which to create the volume.
        :param encrypted: Indicates whether the volume should be encrypted.
        :param iops: The number of I/O operations per second (IOPS).
        :param kms_key_id: The identifier of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use for Amazon EBS encryption.
        :param size_in_gb: The size of the volume, in GiBs.
        :param snapshot_id: The snapshot from which to create the volume.
        :param tag_specifications: The tags passed to EBS volume.
        :param throughput: The throughput to provision for a volume, with a maximum of 1,000 MiB/s.
        :param volume_type: The volume type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volume.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_workspacesinstances as workspacesinstances
            
            cfn_volume_props = workspacesinstances.CfnVolumeProps(
                availability_zone="availabilityZone",
            
                # the properties below are optional
                encrypted=False,
                iops=123,
                kms_key_id="kmsKeyId",
                size_in_gb=123,
                snapshot_id="snapshotId",
                tag_specifications=[workspacesinstances.CfnVolume.TagSpecificationProperty(
                    resource_type="resourceType",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )],
                throughput=123,
                volume_type="volumeType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86994d3c65438656f95433a2d79f0f9f2640fb4eb23141adf1234d9d1e1d53cd)
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument size_in_gb", value=size_in_gb, expected_type=type_hints["size_in_gb"])
            check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
            check_type(argname="argument tag_specifications", value=tag_specifications, expected_type=type_hints["tag_specifications"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "availability_zone": availability_zone,
        }
        if encrypted is not None:
            self._values["encrypted"] = encrypted
        if iops is not None:
            self._values["iops"] = iops
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if size_in_gb is not None:
            self._values["size_in_gb"] = size_in_gb
        if snapshot_id is not None:
            self._values["snapshot_id"] = snapshot_id
        if tag_specifications is not None:
            self._values["tag_specifications"] = tag_specifications
        if throughput is not None:
            self._values["throughput"] = throughput
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def availability_zone(self) -> builtins.str:
        '''The Availability Zone in which to create the volume.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volume.html#cfn-workspacesinstances-volume-availabilityzone
        '''
        result = self._values.get("availability_zone")
        assert result is not None, "Required property 'availability_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the volume should be encrypted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volume.html#cfn-workspacesinstances-volume-encrypted
        '''
        result = self._values.get("encrypted")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''The number of I/O operations per second (IOPS).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volume.html#cfn-workspacesinstances-volume-iops
        '''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use for Amazon EBS encryption.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volume.html#cfn-workspacesinstances-volume-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size_in_gb(self) -> typing.Optional[jsii.Number]:
        '''The size of the volume, in GiBs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volume.html#cfn-workspacesinstances-volume-sizeingb
        '''
        result = self._values.get("size_in_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''The snapshot from which to create the volume.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volume.html#cfn-workspacesinstances-volume-snapshotid
        '''
        result = self._values.get("snapshot_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_specifications(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnVolume.TagSpecificationProperty]]]]:
        '''The tags passed to EBS volume.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volume.html#cfn-workspacesinstances-volume-tagspecifications
        '''
        result = self._values.get("tag_specifications")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnVolume.TagSpecificationProperty]]]], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''The throughput to provision for a volume, with a maximum of 1,000 MiB/s.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volume.html#cfn-workspacesinstances-volume-throughput
        '''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''The volume type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-volume.html#cfn-workspacesinstances-volume-volumetype
        '''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVolumeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnWorkspaceInstance(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance",
):
    '''Resource Type definition for AWS::WorkspacesInstances::WorkspaceInstance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-workspaceinstance.html
    :cloudformationResource: AWS::WorkspacesInstances::WorkspaceInstance
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_workspacesinstances as workspacesinstances
        
        cfn_workspace_instance = workspacesinstances.CfnWorkspaceInstance(self, "MyCfnWorkspaceInstance",
            managed_instance=workspacesinstances.CfnWorkspaceInstance.ManagedInstanceProperty(
                image_id="imageId",
                instance_type="instanceType",
        
                # the properties below are optional
                block_device_mappings=[workspacesinstances.CfnWorkspaceInstance.BlockDeviceMappingProperty(
                    device_name="deviceName",
                    ebs=workspacesinstances.CfnWorkspaceInstance.EbsBlockDeviceProperty(
                        encrypted=False,
                        iops=123,
                        kms_key_id="kmsKeyId",
                        throughput=123,
                        volume_size=123,
                        volume_type="volumeType"
                    ),
                    no_device="noDevice",
                    virtual_name="virtualName"
                )],
                cpu_options=workspacesinstances.CfnWorkspaceInstance.CpuOptionsRequestProperty(
                    core_count=123,
                    threads_per_core=123
                ),
                credit_specification=workspacesinstances.CfnWorkspaceInstance.CreditSpecificationRequestProperty(
                    cpu_credits="cpuCredits"
                ),
                disable_api_stop=False,
                ebs_optimized=False,
                enclave_options=workspacesinstances.CfnWorkspaceInstance.EnclaveOptionsRequestProperty(
                    enabled=False
                ),
                hibernation_options=workspacesinstances.CfnWorkspaceInstance.HibernationOptionsRequestProperty(
                    configured=False
                ),
                iam_instance_profile=workspacesinstances.CfnWorkspaceInstance.IamInstanceProfileSpecificationProperty(
                    name="name"
                ),
                key_name="keyName",
                maintenance_options=workspacesinstances.CfnWorkspaceInstance.InstanceMaintenanceOptionsRequestProperty(
                    auto_recovery="autoRecovery"
                ),
                metadata_options=workspacesinstances.CfnWorkspaceInstance.InstanceMetadataOptionsRequestProperty(
                    http_endpoint="httpEndpoint",
                    http_protocol_ipv6="httpProtocolIpv6",
                    http_put_response_hop_limit=123,
                    http_tokens="httpTokens",
                    instance_metadata_tags="instanceMetadataTags"
                ),
                monitoring=workspacesinstances.CfnWorkspaceInstance.RunInstancesMonitoringEnabledProperty(
                    enabled=False
                ),
                network_interfaces=[workspacesinstances.CfnWorkspaceInstance.InstanceNetworkInterfaceSpecificationProperty(
                    description="description",
                    device_index=123,
                    groups=["groups"],
                    subnet_id="subnetId"
                )],
                network_performance_options=workspacesinstances.CfnWorkspaceInstance.InstanceNetworkPerformanceOptionsRequestProperty(
                    bandwidth_weighting="bandwidthWeighting"
                ),
                placement=workspacesinstances.CfnWorkspaceInstance.PlacementProperty(
                    availability_zone="availabilityZone",
                    group_name="groupName",
                    tenancy="tenancy"
                ),
                private_dns_name_options=workspacesinstances.CfnWorkspaceInstance.PrivateDnsNameOptionsRequestProperty(
                    enable_resource_name_dns_aaaa_record=False,
                    enable_resource_name_dns_aRecord=False,
                    hostname_type="hostnameType"
                ),
                tag_specifications=[workspacesinstances.CfnWorkspaceInstance.TagSpecificationProperty(
                    resource_type="resourceType",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )],
                user_data="userData"
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
        managed_instance: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.ManagedInstanceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param managed_instance: 
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe297a4f0279d14c1f9c904fa95a44f828762333773f7e3a7c9943d3b9b3e3b3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkspaceInstanceProps(managed_instance=managed_instance, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bdc42635ac5557f3eb11885f29e281607cfb0594c2e299de906f90030a10deb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ec3702eceaf9b2e99eb781959d3fbe14573ce56bb19f427daba893407569847)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEc2ManagedInstance")
    def attr_ec2_managed_instance(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: EC2ManagedInstance
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrEc2ManagedInstance"))

    @builtins.property
    @jsii.member(jsii_name="attrEc2ManagedInstanceInstanceId")
    def attr_ec2_managed_instance_instance_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: EC2ManagedInstance.InstanceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEc2ManagedInstanceInstanceId"))

    @builtins.property
    @jsii.member(jsii_name="attrProvisionState")
    def attr_provision_state(self) -> builtins.str:
        '''The current state of the workspace instance.

        :cloudformationAttribute: ProvisionState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProvisionState"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkspaceInstanceId")
    def attr_workspace_instance_id(self) -> builtins.str:
        '''Unique identifier for the workspace instance.

        :cloudformationAttribute: WorkspaceInstanceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkspaceInstanceId"))

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
    @jsii.member(jsii_name="managedInstance")
    def managed_instance(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.ManagedInstanceProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.ManagedInstanceProperty"]], jsii.get(self, "managedInstance"))

    @managed_instance.setter
    def managed_instance(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.ManagedInstanceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6fb81328f4cb605751ce72d14049d2c7dbe8255e2141c4d01d4204ed9b4adf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedInstance", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58b2c86c1c3f77e59470dc4f588d2e8033f028f5127ba91d829c8c6add4de38a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.BlockDeviceMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "device_name": "deviceName",
            "ebs": "ebs",
            "no_device": "noDevice",
            "virtual_name": "virtualName",
        },
    )
    class BlockDeviceMappingProperty:
        def __init__(
            self,
            *,
            device_name: typing.Optional[builtins.str] = None,
            ebs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.EbsBlockDeviceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            no_device: typing.Optional[builtins.str] = None,
            virtual_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param device_name: 
            :param ebs: 
            :param no_device: 
            :param virtual_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-blockdevicemapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                block_device_mapping_property = workspacesinstances.CfnWorkspaceInstance.BlockDeviceMappingProperty(
                    device_name="deviceName",
                    ebs=workspacesinstances.CfnWorkspaceInstance.EbsBlockDeviceProperty(
                        encrypted=False,
                        iops=123,
                        kms_key_id="kmsKeyId",
                        throughput=123,
                        volume_size=123,
                        volume_type="volumeType"
                    ),
                    no_device="noDevice",
                    virtual_name="virtualName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6f2d2dc4f023dfee96411ef0d53c3f207f589b520679a75d9c4a2ca0843d3994)
                check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
                check_type(argname="argument ebs", value=ebs, expected_type=type_hints["ebs"])
                check_type(argname="argument no_device", value=no_device, expected_type=type_hints["no_device"])
                check_type(argname="argument virtual_name", value=virtual_name, expected_type=type_hints["virtual_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if device_name is not None:
                self._values["device_name"] = device_name
            if ebs is not None:
                self._values["ebs"] = ebs
            if no_device is not None:
                self._values["no_device"] = no_device
            if virtual_name is not None:
                self._values["virtual_name"] = virtual_name

        @builtins.property
        def device_name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-blockdevicemapping.html#cfn-workspacesinstances-workspaceinstance-blockdevicemapping-devicename
            '''
            result = self._values.get("device_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ebs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.EbsBlockDeviceProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-blockdevicemapping.html#cfn-workspacesinstances-workspaceinstance-blockdevicemapping-ebs
            '''
            result = self._values.get("ebs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.EbsBlockDeviceProperty"]], result)

        @builtins.property
        def no_device(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-blockdevicemapping.html#cfn-workspacesinstances-workspaceinstance-blockdevicemapping-nodevice
            '''
            result = self._values.get("no_device")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def virtual_name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-blockdevicemapping.html#cfn-workspacesinstances-workspaceinstance-blockdevicemapping-virtualname
            '''
            result = self._values.get("virtual_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BlockDeviceMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.CpuOptionsRequestProperty",
        jsii_struct_bases=[],
        name_mapping={"core_count": "coreCount", "threads_per_core": "threadsPerCore"},
    )
    class CpuOptionsRequestProperty:
        def __init__(
            self,
            *,
            core_count: typing.Optional[jsii.Number] = None,
            threads_per_core: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param core_count: 
            :param threads_per_core: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-cpuoptionsrequest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                cpu_options_request_property = workspacesinstances.CfnWorkspaceInstance.CpuOptionsRequestProperty(
                    core_count=123,
                    threads_per_core=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__baf2483b6c10091ca1060d8ca8cb538b6f9eb1223193ab69470e79d02ae05c0f)
                check_type(argname="argument core_count", value=core_count, expected_type=type_hints["core_count"])
                check_type(argname="argument threads_per_core", value=threads_per_core, expected_type=type_hints["threads_per_core"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if core_count is not None:
                self._values["core_count"] = core_count
            if threads_per_core is not None:
                self._values["threads_per_core"] = threads_per_core

        @builtins.property
        def core_count(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-cpuoptionsrequest.html#cfn-workspacesinstances-workspaceinstance-cpuoptionsrequest-corecount
            '''
            result = self._values.get("core_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def threads_per_core(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-cpuoptionsrequest.html#cfn-workspacesinstances-workspaceinstance-cpuoptionsrequest-threadspercore
            '''
            result = self._values.get("threads_per_core")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CpuOptionsRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.CreditSpecificationRequestProperty",
        jsii_struct_bases=[],
        name_mapping={"cpu_credits": "cpuCredits"},
    )
    class CreditSpecificationRequestProperty:
        def __init__(
            self,
            *,
            cpu_credits: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param cpu_credits: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-creditspecificationrequest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                credit_specification_request_property = workspacesinstances.CfnWorkspaceInstance.CreditSpecificationRequestProperty(
                    cpu_credits="cpuCredits"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be827443f2405057687f0e728dd6b714e64976c6b7fdb53616ba22f38fe684f7)
                check_type(argname="argument cpu_credits", value=cpu_credits, expected_type=type_hints["cpu_credits"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cpu_credits is not None:
                self._values["cpu_credits"] = cpu_credits

        @builtins.property
        def cpu_credits(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-creditspecificationrequest.html#cfn-workspacesinstances-workspaceinstance-creditspecificationrequest-cpucredits
            '''
            result = self._values.get("cpu_credits")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CreditSpecificationRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.EC2ManagedInstanceProperty",
        jsii_struct_bases=[],
        name_mapping={"instance_id": "instanceId"},
    )
    class EC2ManagedInstanceProperty:
        def __init__(
            self,
            *,
            instance_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param instance_id: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-ec2managedinstance.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                e_c2_managed_instance_property = workspacesinstances.CfnWorkspaceInstance.EC2ManagedInstanceProperty(
                    instance_id="instanceId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fdf6ee9b22498f38a18bcb3d582068ef8ccfe59145f98269dc66087bebceba31)
                check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if instance_id is not None:
                self._values["instance_id"] = instance_id

        @builtins.property
        def instance_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-ec2managedinstance.html#cfn-workspacesinstances-workspaceinstance-ec2managedinstance-instanceid
            '''
            result = self._values.get("instance_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EC2ManagedInstanceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.EbsBlockDeviceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encrypted": "encrypted",
            "iops": "iops",
            "kms_key_id": "kmsKeyId",
            "throughput": "throughput",
            "volume_size": "volumeSize",
            "volume_type": "volumeType",
        },
    )
    class EbsBlockDeviceProperty:
        def __init__(
            self,
            *,
            encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            iops: typing.Optional[jsii.Number] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
            throughput: typing.Optional[jsii.Number] = None,
            volume_size: typing.Optional[jsii.Number] = None,
            volume_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param encrypted: 
            :param iops: 
            :param kms_key_id: 
            :param throughput: 
            :param volume_size: 
            :param volume_type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-ebsblockdevice.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                ebs_block_device_property = workspacesinstances.CfnWorkspaceInstance.EbsBlockDeviceProperty(
                    encrypted=False,
                    iops=123,
                    kms_key_id="kmsKeyId",
                    throughput=123,
                    volume_size=123,
                    volume_type="volumeType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__afafa3f2614378531f34f7c44be3d52735de40c84c8eb108e258a8bf3eb50e61)
                check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
                check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
                check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
                check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encrypted is not None:
                self._values["encrypted"] = encrypted
            if iops is not None:
                self._values["iops"] = iops
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if throughput is not None:
                self._values["throughput"] = throughput
            if volume_size is not None:
                self._values["volume_size"] = volume_size
            if volume_type is not None:
                self._values["volume_type"] = volume_type

        @builtins.property
        def encrypted(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-ebsblockdevice.html#cfn-workspacesinstances-workspaceinstance-ebsblockdevice-encrypted
            '''
            result = self._values.get("encrypted")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-ebsblockdevice.html#cfn-workspacesinstances-workspaceinstance-ebsblockdevice-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-ebsblockdevice.html#cfn-workspacesinstances-workspaceinstance-ebsblockdevice-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def throughput(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-ebsblockdevice.html#cfn-workspacesinstances-workspaceinstance-ebsblockdevice-throughput
            '''
            result = self._values.get("throughput")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-ebsblockdevice.html#cfn-workspacesinstances-workspaceinstance-ebsblockdevice-volumesize
            '''
            result = self._values.get("volume_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-ebsblockdevice.html#cfn-workspacesinstances-workspaceinstance-ebsblockdevice-volumetype
            '''
            result = self._values.get("volume_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsBlockDeviceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.EnclaveOptionsRequestProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class EnclaveOptionsRequestProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param enabled: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-enclaveoptionsrequest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                enclave_options_request_property = workspacesinstances.CfnWorkspaceInstance.EnclaveOptionsRequestProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5aaf83d8222c97044bf3b1051a0f48a71d78afefae567af0ee4fd1946ba8b25b)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-enclaveoptionsrequest.html#cfn-workspacesinstances-workspaceinstance-enclaveoptionsrequest-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnclaveOptionsRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.HibernationOptionsRequestProperty",
        jsii_struct_bases=[],
        name_mapping={"configured": "configured"},
    )
    class HibernationOptionsRequestProperty:
        def __init__(
            self,
            *,
            configured: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param configured: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-hibernationoptionsrequest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                hibernation_options_request_property = workspacesinstances.CfnWorkspaceInstance.HibernationOptionsRequestProperty(
                    configured=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6c8991a0b12bd7048f141f964633e62a1f4e02c6996cbf5ff8a1bf1656d2254d)
                check_type(argname="argument configured", value=configured, expected_type=type_hints["configured"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if configured is not None:
                self._values["configured"] = configured

        @builtins.property
        def configured(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-hibernationoptionsrequest.html#cfn-workspacesinstances-workspaceinstance-hibernationoptionsrequest-configured
            '''
            result = self._values.get("configured")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HibernationOptionsRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.IamInstanceProfileSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class IamInstanceProfileSpecificationProperty:
        def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
            '''
            :param name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-iaminstanceprofilespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                iam_instance_profile_specification_property = workspacesinstances.CfnWorkspaceInstance.IamInstanceProfileSpecificationProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__46446ab38acd11b881b5c7aac1c73f790aba6f0b8215d39325f4bb1081daf531)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-iaminstanceprofilespecification.html#cfn-workspacesinstances-workspaceinstance-iaminstanceprofilespecification-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamInstanceProfileSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.InstanceMaintenanceOptionsRequestProperty",
        jsii_struct_bases=[],
        name_mapping={"auto_recovery": "autoRecovery"},
    )
    class InstanceMaintenanceOptionsRequestProperty:
        def __init__(
            self,
            *,
            auto_recovery: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param auto_recovery: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-instancemaintenanceoptionsrequest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                instance_maintenance_options_request_property = workspacesinstances.CfnWorkspaceInstance.InstanceMaintenanceOptionsRequestProperty(
                    auto_recovery="autoRecovery"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5785155bdccebc0d8fada1620d3c62726134a88a6a448d54e8ea0f622a0cfe50)
                check_type(argname="argument auto_recovery", value=auto_recovery, expected_type=type_hints["auto_recovery"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auto_recovery is not None:
                self._values["auto_recovery"] = auto_recovery

        @builtins.property
        def auto_recovery(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-instancemaintenanceoptionsrequest.html#cfn-workspacesinstances-workspaceinstance-instancemaintenanceoptionsrequest-autorecovery
            '''
            result = self._values.get("auto_recovery")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceMaintenanceOptionsRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.InstanceMetadataOptionsRequestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "http_endpoint": "httpEndpoint",
            "http_protocol_ipv6": "httpProtocolIpv6",
            "http_put_response_hop_limit": "httpPutResponseHopLimit",
            "http_tokens": "httpTokens",
            "instance_metadata_tags": "instanceMetadataTags",
        },
    )
    class InstanceMetadataOptionsRequestProperty:
        def __init__(
            self,
            *,
            http_endpoint: typing.Optional[builtins.str] = None,
            http_protocol_ipv6: typing.Optional[builtins.str] = None,
            http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
            http_tokens: typing.Optional[builtins.str] = None,
            instance_metadata_tags: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param http_endpoint: 
            :param http_protocol_ipv6: 
            :param http_put_response_hop_limit: 
            :param http_tokens: 
            :param instance_metadata_tags: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-instancemetadataoptionsrequest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                instance_metadata_options_request_property = workspacesinstances.CfnWorkspaceInstance.InstanceMetadataOptionsRequestProperty(
                    http_endpoint="httpEndpoint",
                    http_protocol_ipv6="httpProtocolIpv6",
                    http_put_response_hop_limit=123,
                    http_tokens="httpTokens",
                    instance_metadata_tags="instanceMetadataTags"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d879a9a1ea939eed5a5bf31a9e53a33bef78538d965c45115d7750157f87c88b)
                check_type(argname="argument http_endpoint", value=http_endpoint, expected_type=type_hints["http_endpoint"])
                check_type(argname="argument http_protocol_ipv6", value=http_protocol_ipv6, expected_type=type_hints["http_protocol_ipv6"])
                check_type(argname="argument http_put_response_hop_limit", value=http_put_response_hop_limit, expected_type=type_hints["http_put_response_hop_limit"])
                check_type(argname="argument http_tokens", value=http_tokens, expected_type=type_hints["http_tokens"])
                check_type(argname="argument instance_metadata_tags", value=instance_metadata_tags, expected_type=type_hints["instance_metadata_tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if http_endpoint is not None:
                self._values["http_endpoint"] = http_endpoint
            if http_protocol_ipv6 is not None:
                self._values["http_protocol_ipv6"] = http_protocol_ipv6
            if http_put_response_hop_limit is not None:
                self._values["http_put_response_hop_limit"] = http_put_response_hop_limit
            if http_tokens is not None:
                self._values["http_tokens"] = http_tokens
            if instance_metadata_tags is not None:
                self._values["instance_metadata_tags"] = instance_metadata_tags

        @builtins.property
        def http_endpoint(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-instancemetadataoptionsrequest.html#cfn-workspacesinstances-workspaceinstance-instancemetadataoptionsrequest-httpendpoint
            '''
            result = self._values.get("http_endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def http_protocol_ipv6(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-instancemetadataoptionsrequest.html#cfn-workspacesinstances-workspaceinstance-instancemetadataoptionsrequest-httpprotocolipv6
            '''
            result = self._values.get("http_protocol_ipv6")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def http_put_response_hop_limit(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-instancemetadataoptionsrequest.html#cfn-workspacesinstances-workspaceinstance-instancemetadataoptionsrequest-httpputresponsehoplimit
            '''
            result = self._values.get("http_put_response_hop_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def http_tokens(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-instancemetadataoptionsrequest.html#cfn-workspacesinstances-workspaceinstance-instancemetadataoptionsrequest-httptokens
            '''
            result = self._values.get("http_tokens")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def instance_metadata_tags(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-instancemetadataoptionsrequest.html#cfn-workspacesinstances-workspaceinstance-instancemetadataoptionsrequest-instancemetadatatags
            '''
            result = self._values.get("instance_metadata_tags")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceMetadataOptionsRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.InstanceNetworkInterfaceSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "description": "description",
            "device_index": "deviceIndex",
            "groups": "groups",
            "subnet_id": "subnetId",
        },
    )
    class InstanceNetworkInterfaceSpecificationProperty:
        def __init__(
            self,
            *,
            description: typing.Optional[builtins.str] = None,
            device_index: typing.Optional[jsii.Number] = None,
            groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param description: 
            :param device_index: 
            :param groups: 
            :param subnet_id: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-instancenetworkinterfacespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                instance_network_interface_specification_property = workspacesinstances.CfnWorkspaceInstance.InstanceNetworkInterfaceSpecificationProperty(
                    description="description",
                    device_index=123,
                    groups=["groups"],
                    subnet_id="subnetId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7c88a37359de0c57531f563cc84d1109a289e345ba61e892cf12f1611a31662d)
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument device_index", value=device_index, expected_type=type_hints["device_index"])
                check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
                check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if description is not None:
                self._values["description"] = description
            if device_index is not None:
                self._values["device_index"] = device_index
            if groups is not None:
                self._values["groups"] = groups
            if subnet_id is not None:
                self._values["subnet_id"] = subnet_id

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-instancenetworkinterfacespecification.html#cfn-workspacesinstances-workspaceinstance-instancenetworkinterfacespecification-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_index(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-instancenetworkinterfacespecification.html#cfn-workspacesinstances-workspaceinstance-instancenetworkinterfacespecification-deviceindex
            '''
            result = self._values.get("device_index")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-instancenetworkinterfacespecification.html#cfn-workspacesinstances-workspaceinstance-instancenetworkinterfacespecification-groups
            '''
            result = self._values.get("groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-instancenetworkinterfacespecification.html#cfn-workspacesinstances-workspaceinstance-instancenetworkinterfacespecification-subnetid
            '''
            result = self._values.get("subnet_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceNetworkInterfaceSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.InstanceNetworkPerformanceOptionsRequestProperty",
        jsii_struct_bases=[],
        name_mapping={"bandwidth_weighting": "bandwidthWeighting"},
    )
    class InstanceNetworkPerformanceOptionsRequestProperty:
        def __init__(
            self,
            *,
            bandwidth_weighting: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bandwidth_weighting: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-instancenetworkperformanceoptionsrequest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                instance_network_performance_options_request_property = workspacesinstances.CfnWorkspaceInstance.InstanceNetworkPerformanceOptionsRequestProperty(
                    bandwidth_weighting="bandwidthWeighting"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8457689e343afe3fd18713b744f081cee9dcd43310c6b6befb13b25b56685b35)
                check_type(argname="argument bandwidth_weighting", value=bandwidth_weighting, expected_type=type_hints["bandwidth_weighting"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bandwidth_weighting is not None:
                self._values["bandwidth_weighting"] = bandwidth_weighting

        @builtins.property
        def bandwidth_weighting(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-instancenetworkperformanceoptionsrequest.html#cfn-workspacesinstances-workspaceinstance-instancenetworkperformanceoptionsrequest-bandwidthweighting
            '''
            result = self._values.get("bandwidth_weighting")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceNetworkPerformanceOptionsRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.ManagedInstanceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_id": "imageId",
            "instance_type": "instanceType",
            "block_device_mappings": "blockDeviceMappings",
            "cpu_options": "cpuOptions",
            "credit_specification": "creditSpecification",
            "disable_api_stop": "disableApiStop",
            "ebs_optimized": "ebsOptimized",
            "enclave_options": "enclaveOptions",
            "hibernation_options": "hibernationOptions",
            "iam_instance_profile": "iamInstanceProfile",
            "key_name": "keyName",
            "maintenance_options": "maintenanceOptions",
            "metadata_options": "metadataOptions",
            "monitoring": "monitoring",
            "network_interfaces": "networkInterfaces",
            "network_performance_options": "networkPerformanceOptions",
            "placement": "placement",
            "private_dns_name_options": "privateDnsNameOptions",
            "tag_specifications": "tagSpecifications",
            "user_data": "userData",
        },
    )
    class ManagedInstanceProperty:
        def __init__(
            self,
            *,
            image_id: builtins.str,
            instance_type: builtins.str,
            block_device_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.BlockDeviceMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            cpu_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.CpuOptionsRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            credit_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.CreditSpecificationRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            disable_api_stop: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            ebs_optimized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            enclave_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.EnclaveOptionsRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            hibernation_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.HibernationOptionsRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            iam_instance_profile: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.IamInstanceProfileSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            key_name: typing.Optional[builtins.str] = None,
            maintenance_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.InstanceMaintenanceOptionsRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            metadata_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.InstanceMetadataOptionsRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            monitoring: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.RunInstancesMonitoringEnabledProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.InstanceNetworkInterfaceSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            network_performance_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.InstanceNetworkPerformanceOptionsRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            placement: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.PlacementProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            private_dns_name_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.PrivateDnsNameOptionsRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            tag_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspaceInstance.TagSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            user_data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param image_id: 
            :param instance_type: 
            :param block_device_mappings: 
            :param cpu_options: 
            :param credit_specification: 
            :param disable_api_stop: 
            :param ebs_optimized: 
            :param enclave_options: 
            :param hibernation_options: 
            :param iam_instance_profile: 
            :param key_name: 
            :param maintenance_options: 
            :param metadata_options: 
            :param monitoring: 
            :param network_interfaces: 
            :param network_performance_options: 
            :param placement: 
            :param private_dns_name_options: 
            :param tag_specifications: 
            :param user_data: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                managed_instance_property = workspacesinstances.CfnWorkspaceInstance.ManagedInstanceProperty(
                    image_id="imageId",
                    instance_type="instanceType",
                
                    # the properties below are optional
                    block_device_mappings=[workspacesinstances.CfnWorkspaceInstance.BlockDeviceMappingProperty(
                        device_name="deviceName",
                        ebs=workspacesinstances.CfnWorkspaceInstance.EbsBlockDeviceProperty(
                            encrypted=False,
                            iops=123,
                            kms_key_id="kmsKeyId",
                            throughput=123,
                            volume_size=123,
                            volume_type="volumeType"
                        ),
                        no_device="noDevice",
                        virtual_name="virtualName"
                    )],
                    cpu_options=workspacesinstances.CfnWorkspaceInstance.CpuOptionsRequestProperty(
                        core_count=123,
                        threads_per_core=123
                    ),
                    credit_specification=workspacesinstances.CfnWorkspaceInstance.CreditSpecificationRequestProperty(
                        cpu_credits="cpuCredits"
                    ),
                    disable_api_stop=False,
                    ebs_optimized=False,
                    enclave_options=workspacesinstances.CfnWorkspaceInstance.EnclaveOptionsRequestProperty(
                        enabled=False
                    ),
                    hibernation_options=workspacesinstances.CfnWorkspaceInstance.HibernationOptionsRequestProperty(
                        configured=False
                    ),
                    iam_instance_profile=workspacesinstances.CfnWorkspaceInstance.IamInstanceProfileSpecificationProperty(
                        name="name"
                    ),
                    key_name="keyName",
                    maintenance_options=workspacesinstances.CfnWorkspaceInstance.InstanceMaintenanceOptionsRequestProperty(
                        auto_recovery="autoRecovery"
                    ),
                    metadata_options=workspacesinstances.CfnWorkspaceInstance.InstanceMetadataOptionsRequestProperty(
                        http_endpoint="httpEndpoint",
                        http_protocol_ipv6="httpProtocolIpv6",
                        http_put_response_hop_limit=123,
                        http_tokens="httpTokens",
                        instance_metadata_tags="instanceMetadataTags"
                    ),
                    monitoring=workspacesinstances.CfnWorkspaceInstance.RunInstancesMonitoringEnabledProperty(
                        enabled=False
                    ),
                    network_interfaces=[workspacesinstances.CfnWorkspaceInstance.InstanceNetworkInterfaceSpecificationProperty(
                        description="description",
                        device_index=123,
                        groups=["groups"],
                        subnet_id="subnetId"
                    )],
                    network_performance_options=workspacesinstances.CfnWorkspaceInstance.InstanceNetworkPerformanceOptionsRequestProperty(
                        bandwidth_weighting="bandwidthWeighting"
                    ),
                    placement=workspacesinstances.CfnWorkspaceInstance.PlacementProperty(
                        availability_zone="availabilityZone",
                        group_name="groupName",
                        tenancy="tenancy"
                    ),
                    private_dns_name_options=workspacesinstances.CfnWorkspaceInstance.PrivateDnsNameOptionsRequestProperty(
                        enable_resource_name_dns_aaaa_record=False,
                        enable_resource_name_dns_aRecord=False,
                        hostname_type="hostnameType"
                    ),
                    tag_specifications=[workspacesinstances.CfnWorkspaceInstance.TagSpecificationProperty(
                        resource_type="resourceType",
                        tags=[CfnTag(
                            key="key",
                            value="value"
                        )]
                    )],
                    user_data="userData"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__122edb12e6993ba3ae146e0faaf65a6eef7a6651e2293cb5479f0afe37198259)
                check_type(argname="argument image_id", value=image_id, expected_type=type_hints["image_id"])
                check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
                check_type(argname="argument block_device_mappings", value=block_device_mappings, expected_type=type_hints["block_device_mappings"])
                check_type(argname="argument cpu_options", value=cpu_options, expected_type=type_hints["cpu_options"])
                check_type(argname="argument credit_specification", value=credit_specification, expected_type=type_hints["credit_specification"])
                check_type(argname="argument disable_api_stop", value=disable_api_stop, expected_type=type_hints["disable_api_stop"])
                check_type(argname="argument ebs_optimized", value=ebs_optimized, expected_type=type_hints["ebs_optimized"])
                check_type(argname="argument enclave_options", value=enclave_options, expected_type=type_hints["enclave_options"])
                check_type(argname="argument hibernation_options", value=hibernation_options, expected_type=type_hints["hibernation_options"])
                check_type(argname="argument iam_instance_profile", value=iam_instance_profile, expected_type=type_hints["iam_instance_profile"])
                check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
                check_type(argname="argument maintenance_options", value=maintenance_options, expected_type=type_hints["maintenance_options"])
                check_type(argname="argument metadata_options", value=metadata_options, expected_type=type_hints["metadata_options"])
                check_type(argname="argument monitoring", value=monitoring, expected_type=type_hints["monitoring"])
                check_type(argname="argument network_interfaces", value=network_interfaces, expected_type=type_hints["network_interfaces"])
                check_type(argname="argument network_performance_options", value=network_performance_options, expected_type=type_hints["network_performance_options"])
                check_type(argname="argument placement", value=placement, expected_type=type_hints["placement"])
                check_type(argname="argument private_dns_name_options", value=private_dns_name_options, expected_type=type_hints["private_dns_name_options"])
                check_type(argname="argument tag_specifications", value=tag_specifications, expected_type=type_hints["tag_specifications"])
                check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "image_id": image_id,
                "instance_type": instance_type,
            }
            if block_device_mappings is not None:
                self._values["block_device_mappings"] = block_device_mappings
            if cpu_options is not None:
                self._values["cpu_options"] = cpu_options
            if credit_specification is not None:
                self._values["credit_specification"] = credit_specification
            if disable_api_stop is not None:
                self._values["disable_api_stop"] = disable_api_stop
            if ebs_optimized is not None:
                self._values["ebs_optimized"] = ebs_optimized
            if enclave_options is not None:
                self._values["enclave_options"] = enclave_options
            if hibernation_options is not None:
                self._values["hibernation_options"] = hibernation_options
            if iam_instance_profile is not None:
                self._values["iam_instance_profile"] = iam_instance_profile
            if key_name is not None:
                self._values["key_name"] = key_name
            if maintenance_options is not None:
                self._values["maintenance_options"] = maintenance_options
            if metadata_options is not None:
                self._values["metadata_options"] = metadata_options
            if monitoring is not None:
                self._values["monitoring"] = monitoring
            if network_interfaces is not None:
                self._values["network_interfaces"] = network_interfaces
            if network_performance_options is not None:
                self._values["network_performance_options"] = network_performance_options
            if placement is not None:
                self._values["placement"] = placement
            if private_dns_name_options is not None:
                self._values["private_dns_name_options"] = private_dns_name_options
            if tag_specifications is not None:
                self._values["tag_specifications"] = tag_specifications
            if user_data is not None:
                self._values["user_data"] = user_data

        @builtins.property
        def image_id(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-imageid
            '''
            result = self._values.get("image_id")
            assert result is not None, "Required property 'image_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def block_device_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.BlockDeviceMappingProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-blockdevicemappings
            '''
            result = self._values.get("block_device_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.BlockDeviceMappingProperty"]]]], result)

        @builtins.property
        def cpu_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.CpuOptionsRequestProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-cpuoptions
            '''
            result = self._values.get("cpu_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.CpuOptionsRequestProperty"]], result)

        @builtins.property
        def credit_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.CreditSpecificationRequestProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-creditspecification
            '''
            result = self._values.get("credit_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.CreditSpecificationRequestProperty"]], result)

        @builtins.property
        def disable_api_stop(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-disableapistop
            '''
            result = self._values.get("disable_api_stop")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def ebs_optimized(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-ebsoptimized
            '''
            result = self._values.get("ebs_optimized")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def enclave_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.EnclaveOptionsRequestProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-enclaveoptions
            '''
            result = self._values.get("enclave_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.EnclaveOptionsRequestProperty"]], result)

        @builtins.property
        def hibernation_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.HibernationOptionsRequestProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-hibernationoptions
            '''
            result = self._values.get("hibernation_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.HibernationOptionsRequestProperty"]], result)

        @builtins.property
        def iam_instance_profile(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.IamInstanceProfileSpecificationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-iaminstanceprofile
            '''
            result = self._values.get("iam_instance_profile")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.IamInstanceProfileSpecificationProperty"]], result)

        @builtins.property
        def key_name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-keyname
            '''
            result = self._values.get("key_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def maintenance_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.InstanceMaintenanceOptionsRequestProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-maintenanceoptions
            '''
            result = self._values.get("maintenance_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.InstanceMaintenanceOptionsRequestProperty"]], result)

        @builtins.property
        def metadata_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.InstanceMetadataOptionsRequestProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-metadataoptions
            '''
            result = self._values.get("metadata_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.InstanceMetadataOptionsRequestProperty"]], result)

        @builtins.property
        def monitoring(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.RunInstancesMonitoringEnabledProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-monitoring
            '''
            result = self._values.get("monitoring")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.RunInstancesMonitoringEnabledProperty"]], result)

        @builtins.property
        def network_interfaces(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.InstanceNetworkInterfaceSpecificationProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-networkinterfaces
            '''
            result = self._values.get("network_interfaces")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.InstanceNetworkInterfaceSpecificationProperty"]]]], result)

        @builtins.property
        def network_performance_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.InstanceNetworkPerformanceOptionsRequestProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-networkperformanceoptions
            '''
            result = self._values.get("network_performance_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.InstanceNetworkPerformanceOptionsRequestProperty"]], result)

        @builtins.property
        def placement(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.PlacementProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-placement
            '''
            result = self._values.get("placement")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.PlacementProperty"]], result)

        @builtins.property
        def private_dns_name_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.PrivateDnsNameOptionsRequestProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-privatednsnameoptions
            '''
            result = self._values.get("private_dns_name_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.PrivateDnsNameOptionsRequestProperty"]], result)

        @builtins.property
        def tag_specifications(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.TagSpecificationProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-tagspecifications
            '''
            result = self._values.get("tag_specifications")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkspaceInstance.TagSpecificationProperty"]]]], result)

        @builtins.property
        def user_data(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-managedinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance-userdata
            '''
            result = self._values.get("user_data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManagedInstanceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.PlacementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "availability_zone": "availabilityZone",
            "group_name": "groupName",
            "tenancy": "tenancy",
        },
    )
    class PlacementProperty:
        def __init__(
            self,
            *,
            availability_zone: typing.Optional[builtins.str] = None,
            group_name: typing.Optional[builtins.str] = None,
            tenancy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param availability_zone: 
            :param group_name: 
            :param tenancy: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-placement.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                placement_property = workspacesinstances.CfnWorkspaceInstance.PlacementProperty(
                    availability_zone="availabilityZone",
                    group_name="groupName",
                    tenancy="tenancy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__74aaa065dbb77262ecab6552e5fde4ac2723c645be4dde2327c06e281386c1f8)
                check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
                check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
                check_type(argname="argument tenancy", value=tenancy, expected_type=type_hints["tenancy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if availability_zone is not None:
                self._values["availability_zone"] = availability_zone
            if group_name is not None:
                self._values["group_name"] = group_name
            if tenancy is not None:
                self._values["tenancy"] = tenancy

        @builtins.property
        def availability_zone(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-placement.html#cfn-workspacesinstances-workspaceinstance-placement-availabilityzone
            '''
            result = self._values.get("availability_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def group_name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-placement.html#cfn-workspacesinstances-workspaceinstance-placement-groupname
            '''
            result = self._values.get("group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tenancy(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-placement.html#cfn-workspacesinstances-workspaceinstance-placement-tenancy
            '''
            result = self._values.get("tenancy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PlacementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.PrivateDnsNameOptionsRequestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_resource_name_dns_aaaa_record": "enableResourceNameDnsAaaaRecord",
            "enable_resource_name_dns_a_record": "enableResourceNameDnsARecord",
            "hostname_type": "hostnameType",
        },
    )
    class PrivateDnsNameOptionsRequestProperty:
        def __init__(
            self,
            *,
            enable_resource_name_dns_aaaa_record: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            enable_resource_name_dns_a_record: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            hostname_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param enable_resource_name_dns_aaaa_record: 
            :param enable_resource_name_dns_a_record: 
            :param hostname_type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-privatednsnameoptionsrequest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                private_dns_name_options_request_property = workspacesinstances.CfnWorkspaceInstance.PrivateDnsNameOptionsRequestProperty(
                    enable_resource_name_dns_aaaa_record=False,
                    enable_resource_name_dns_aRecord=False,
                    hostname_type="hostnameType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5bcd696ce9417cfc6075ca9f9d64535711403bc6dc26a7e1e325bcb0b416dccc)
                check_type(argname="argument enable_resource_name_dns_aaaa_record", value=enable_resource_name_dns_aaaa_record, expected_type=type_hints["enable_resource_name_dns_aaaa_record"])
                check_type(argname="argument enable_resource_name_dns_a_record", value=enable_resource_name_dns_a_record, expected_type=type_hints["enable_resource_name_dns_a_record"])
                check_type(argname="argument hostname_type", value=hostname_type, expected_type=type_hints["hostname_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable_resource_name_dns_aaaa_record is not None:
                self._values["enable_resource_name_dns_aaaa_record"] = enable_resource_name_dns_aaaa_record
            if enable_resource_name_dns_a_record is not None:
                self._values["enable_resource_name_dns_a_record"] = enable_resource_name_dns_a_record
            if hostname_type is not None:
                self._values["hostname_type"] = hostname_type

        @builtins.property
        def enable_resource_name_dns_aaaa_record(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-privatednsnameoptionsrequest.html#cfn-workspacesinstances-workspaceinstance-privatednsnameoptionsrequest-enableresourcenamednsaaaarecord
            '''
            result = self._values.get("enable_resource_name_dns_aaaa_record")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def enable_resource_name_dns_a_record(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-privatednsnameoptionsrequest.html#cfn-workspacesinstances-workspaceinstance-privatednsnameoptionsrequest-enableresourcenamednsarecord
            '''
            result = self._values.get("enable_resource_name_dns_a_record")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def hostname_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-privatednsnameoptionsrequest.html#cfn-workspacesinstances-workspaceinstance-privatednsnameoptionsrequest-hostnametype
            '''
            result = self._values.get("hostname_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrivateDnsNameOptionsRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.RunInstancesMonitoringEnabledProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class RunInstancesMonitoringEnabledProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param enabled: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-runinstancesmonitoringenabled.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                run_instances_monitoring_enabled_property = workspacesinstances.CfnWorkspaceInstance.RunInstancesMonitoringEnabledProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6fcd9d05f58e0d776ba7b11b076d5a7c565bc9ea5ce223eab03cdac46e660811)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-runinstancesmonitoringenabled.html#cfn-workspacesinstances-workspaceinstance-runinstancesmonitoringenabled-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RunInstancesMonitoringEnabledProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstance.TagSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_type": "resourceType", "tags": "tags"},
    )
    class TagSpecificationProperty:
        def __init__(
            self,
            *,
            resource_type: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param resource_type: 
            :param tags: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-tagspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesinstances as workspacesinstances
                
                tag_specification_property = workspacesinstances.CfnWorkspaceInstance.TagSpecificationProperty(
                    resource_type="resourceType",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a80a115a0fb3e43ec2f01b3395420a80cbdd00bb61da5e1c9176167d6eb9bbf0)
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if resource_type is not None:
                self._values["resource_type"] = resource_type
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def resource_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-tagspecification.html#cfn-workspacesinstances-workspaceinstance-tagspecification-resourcetype
            '''
            result = self._values.get("resource_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesinstances-workspaceinstance-tagspecification.html#cfn-workspacesinstances-workspaceinstance-tagspecification-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_workspacesinstances.CfnWorkspaceInstanceProps",
    jsii_struct_bases=[],
    name_mapping={"managed_instance": "managedInstance", "tags": "tags"},
)
class CfnWorkspaceInstanceProps:
    def __init__(
        self,
        *,
        managed_instance: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.ManagedInstanceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkspaceInstance``.

        :param managed_instance: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-workspaceinstance.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_workspacesinstances as workspacesinstances
            
            cfn_workspace_instance_props = workspacesinstances.CfnWorkspaceInstanceProps(
                managed_instance=workspacesinstances.CfnWorkspaceInstance.ManagedInstanceProperty(
                    image_id="imageId",
                    instance_type="instanceType",
            
                    # the properties below are optional
                    block_device_mappings=[workspacesinstances.CfnWorkspaceInstance.BlockDeviceMappingProperty(
                        device_name="deviceName",
                        ebs=workspacesinstances.CfnWorkspaceInstance.EbsBlockDeviceProperty(
                            encrypted=False,
                            iops=123,
                            kms_key_id="kmsKeyId",
                            throughput=123,
                            volume_size=123,
                            volume_type="volumeType"
                        ),
                        no_device="noDevice",
                        virtual_name="virtualName"
                    )],
                    cpu_options=workspacesinstances.CfnWorkspaceInstance.CpuOptionsRequestProperty(
                        core_count=123,
                        threads_per_core=123
                    ),
                    credit_specification=workspacesinstances.CfnWorkspaceInstance.CreditSpecificationRequestProperty(
                        cpu_credits="cpuCredits"
                    ),
                    disable_api_stop=False,
                    ebs_optimized=False,
                    enclave_options=workspacesinstances.CfnWorkspaceInstance.EnclaveOptionsRequestProperty(
                        enabled=False
                    ),
                    hibernation_options=workspacesinstances.CfnWorkspaceInstance.HibernationOptionsRequestProperty(
                        configured=False
                    ),
                    iam_instance_profile=workspacesinstances.CfnWorkspaceInstance.IamInstanceProfileSpecificationProperty(
                        name="name"
                    ),
                    key_name="keyName",
                    maintenance_options=workspacesinstances.CfnWorkspaceInstance.InstanceMaintenanceOptionsRequestProperty(
                        auto_recovery="autoRecovery"
                    ),
                    metadata_options=workspacesinstances.CfnWorkspaceInstance.InstanceMetadataOptionsRequestProperty(
                        http_endpoint="httpEndpoint",
                        http_protocol_ipv6="httpProtocolIpv6",
                        http_put_response_hop_limit=123,
                        http_tokens="httpTokens",
                        instance_metadata_tags="instanceMetadataTags"
                    ),
                    monitoring=workspacesinstances.CfnWorkspaceInstance.RunInstancesMonitoringEnabledProperty(
                        enabled=False
                    ),
                    network_interfaces=[workspacesinstances.CfnWorkspaceInstance.InstanceNetworkInterfaceSpecificationProperty(
                        description="description",
                        device_index=123,
                        groups=["groups"],
                        subnet_id="subnetId"
                    )],
                    network_performance_options=workspacesinstances.CfnWorkspaceInstance.InstanceNetworkPerformanceOptionsRequestProperty(
                        bandwidth_weighting="bandwidthWeighting"
                    ),
                    placement=workspacesinstances.CfnWorkspaceInstance.PlacementProperty(
                        availability_zone="availabilityZone",
                        group_name="groupName",
                        tenancy="tenancy"
                    ),
                    private_dns_name_options=workspacesinstances.CfnWorkspaceInstance.PrivateDnsNameOptionsRequestProperty(
                        enable_resource_name_dns_aaaa_record=False,
                        enable_resource_name_dns_aRecord=False,
                        hostname_type="hostnameType"
                    ),
                    tag_specifications=[workspacesinstances.CfnWorkspaceInstance.TagSpecificationProperty(
                        resource_type="resourceType",
                        tags=[CfnTag(
                            key="key",
                            value="value"
                        )]
                    )],
                    user_data="userData"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d4292dcb083e5a048440cd4455e31dfc65f5b3dd4c844b99e38e6c3941cca08)
            check_type(argname="argument managed_instance", value=managed_instance, expected_type=type_hints["managed_instance"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if managed_instance is not None:
            self._values["managed_instance"] = managed_instance
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def managed_instance(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspaceInstance.ManagedInstanceProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-workspaceinstance.html#cfn-workspacesinstances-workspaceinstance-managedinstance
        '''
        result = self._values.get("managed_instance")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspaceInstance.ManagedInstanceProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesinstances-workspaceinstance.html#cfn-workspacesinstances-workspaceinstance-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkspaceInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnVolume",
    "CfnVolumeAssociation",
    "CfnVolumeAssociationProps",
    "CfnVolumeProps",
    "CfnWorkspaceInstance",
    "CfnWorkspaceInstanceProps",
]

publication.publish()

def _typecheckingstub__6f8f538e7b445e64dae7c3f3fa5cbf03f73a9175df0c28d38e372410d7a38644(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    availability_zone: builtins.str,
    encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    iops: typing.Optional[jsii.Number] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    size_in_gb: typing.Optional[jsii.Number] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    tag_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVolume.TagSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__685ee3c99d00c4a98137add5e1954d76422417da17f64b863cea2c0824dea902(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50ddfbc291d3e556ace0dc6e9d82cfedb078a4a3cbb9ef9e8eac039d0e82d9e6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9f5f1fdafc059b4dc0f72801057c79e690b2878e7ac2fdf540ab305cb1db5b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2545bcf2397b591eeb5bc2020672daea19e4969515b96c2982ba337dfe90a159(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed1876d81e0f42a3b54883c4648bf7cf155fa880a498cacc96a0945d5032084c(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__395b2ede7d0057a6fa453fc8de076050bcc1806edcbaeecc76c37f56b5befabc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac8bac9f32006bab210d99c61fa194ffe0daa28445242538135f5024937fed35(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d59cb75f780fcc1524e9d8f2469747f8c6f2bbfc350d8662efddf91bcec54be4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7afbacaf7f3ea12aff8077fba424159c4a78dabec81d0e15c2cf21552d0eca48(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnVolume.TagSpecificationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd4dae6ee80b4f1583ff940c92723ae5abc6127d8abd48ca72184266298e68d5(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ce69be7eab4b12a5677916d7b89ed00c676fbd7d9858d3c8fd894ed8a963d70(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0902e5172f6b16ac0cad62cbc3b7188ce843a8d38d90dcc5c86591e6acf47988(
    *,
    resource_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7eec0daa83c1024898d2dd124cb4f461e56903d8a98401eb4d02742f55a5ba8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    device: builtins.str,
    volume_id: builtins.str,
    workspace_instance_id: builtins.str,
    disassociate_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fd0989a57e9649b7a4d590f7c91b99524c0760e7a9573d04c9a0651e66ba9b4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9edb2ba816767d7bd7866452c6fad9e22e451376ace13728983cb1007430d513(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2c067e418598328cb19e2ca662460d196bbf4f0edd016a89d56ca6b09b96ae9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c66f015cf8f3049bd728d95ffef2a32c21bd81393c29537303adaf4e86d6829(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb0e90de13632397d9f05ecf786f58d468973d0cf21a6f5c435c070b2c03b819(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1139240ee9e52471c21751caa541f36622002b63b2edb0a487ae73612ae098a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f051309343f88ebe1cc3dc3f2fff77a39c42174a07969dff75f195781a41fbf(
    *,
    device: builtins.str,
    volume_id: builtins.str,
    workspace_instance_id: builtins.str,
    disassociate_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86994d3c65438656f95433a2d79f0f9f2640fb4eb23141adf1234d9d1e1d53cd(
    *,
    availability_zone: builtins.str,
    encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    iops: typing.Optional[jsii.Number] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    size_in_gb: typing.Optional[jsii.Number] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    tag_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVolume.TagSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe297a4f0279d14c1f9c904fa95a44f828762333773f7e3a7c9943d3b9b3e3b3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    managed_instance: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.ManagedInstanceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bdc42635ac5557f3eb11885f29e281607cfb0594c2e299de906f90030a10deb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ec3702eceaf9b2e99eb781959d3fbe14573ce56bb19f427daba893407569847(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6fb81328f4cb605751ce72d14049d2c7dbe8255e2141c4d01d4204ed9b4adf0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspaceInstance.ManagedInstanceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58b2c86c1c3f77e59470dc4f588d2e8033f028f5127ba91d829c8c6add4de38a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f2d2dc4f023dfee96411ef0d53c3f207f589b520679a75d9c4a2ca0843d3994(
    *,
    device_name: typing.Optional[builtins.str] = None,
    ebs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.EbsBlockDeviceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    no_device: typing.Optional[builtins.str] = None,
    virtual_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baf2483b6c10091ca1060d8ca8cb538b6f9eb1223193ab69470e79d02ae05c0f(
    *,
    core_count: typing.Optional[jsii.Number] = None,
    threads_per_core: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be827443f2405057687f0e728dd6b714e64976c6b7fdb53616ba22f38fe684f7(
    *,
    cpu_credits: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdf6ee9b22498f38a18bcb3d582068ef8ccfe59145f98269dc66087bebceba31(
    *,
    instance_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afafa3f2614378531f34f7c44be3d52735de40c84c8eb108e258a8bf3eb50e61(
    *,
    encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    iops: typing.Optional[jsii.Number] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aaf83d8222c97044bf3b1051a0f48a71d78afefae567af0ee4fd1946ba8b25b(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c8991a0b12bd7048f141f964633e62a1f4e02c6996cbf5ff8a1bf1656d2254d(
    *,
    configured: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46446ab38acd11b881b5c7aac1c73f790aba6f0b8215d39325f4bb1081daf531(
    *,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5785155bdccebc0d8fada1620d3c62726134a88a6a448d54e8ea0f622a0cfe50(
    *,
    auto_recovery: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d879a9a1ea939eed5a5bf31a9e53a33bef78538d965c45115d7750157f87c88b(
    *,
    http_endpoint: typing.Optional[builtins.str] = None,
    http_protocol_ipv6: typing.Optional[builtins.str] = None,
    http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
    http_tokens: typing.Optional[builtins.str] = None,
    instance_metadata_tags: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c88a37359de0c57531f563cc84d1109a289e345ba61e892cf12f1611a31662d(
    *,
    description: typing.Optional[builtins.str] = None,
    device_index: typing.Optional[jsii.Number] = None,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8457689e343afe3fd18713b744f081cee9dcd43310c6b6befb13b25b56685b35(
    *,
    bandwidth_weighting: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__122edb12e6993ba3ae146e0faaf65a6eef7a6651e2293cb5479f0afe37198259(
    *,
    image_id: builtins.str,
    instance_type: builtins.str,
    block_device_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.BlockDeviceMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    cpu_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.CpuOptionsRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    credit_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.CreditSpecificationRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    disable_api_stop: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ebs_optimized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enclave_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.EnclaveOptionsRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hibernation_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.HibernationOptionsRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iam_instance_profile: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.IamInstanceProfileSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    key_name: typing.Optional[builtins.str] = None,
    maintenance_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.InstanceMaintenanceOptionsRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    metadata_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.InstanceMetadataOptionsRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    monitoring: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.RunInstancesMonitoringEnabledProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.InstanceNetworkInterfaceSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_performance_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.InstanceNetworkPerformanceOptionsRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    placement: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.PlacementProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    private_dns_name_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.PrivateDnsNameOptionsRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tag_specifications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.TagSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    user_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74aaa065dbb77262ecab6552e5fde4ac2723c645be4dde2327c06e281386c1f8(
    *,
    availability_zone: typing.Optional[builtins.str] = None,
    group_name: typing.Optional[builtins.str] = None,
    tenancy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bcd696ce9417cfc6075ca9f9d64535711403bc6dc26a7e1e325bcb0b416dccc(
    *,
    enable_resource_name_dns_aaaa_record: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_resource_name_dns_a_record: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    hostname_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fcd9d05f58e0d776ba7b11b076d5a7c565bc9ea5ce223eab03cdac46e660811(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a80a115a0fb3e43ec2f01b3395420a80cbdd00bb61da5e1c9176167d6eb9bbf0(
    *,
    resource_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d4292dcb083e5a048440cd4455e31dfc65f5b3dd4c844b99e38e6c3941cca08(
    *,
    managed_instance: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspaceInstance.ManagedInstanceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
