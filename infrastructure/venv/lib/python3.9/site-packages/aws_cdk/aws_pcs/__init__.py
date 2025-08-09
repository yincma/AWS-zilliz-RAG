r'''
# AWS::PCS Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_pcs as pcs
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for PCS construct libraries](https://constructs.dev/search?q=pcs)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::PCS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_PCS.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::PCS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_PCS.html).

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
class CfnCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pcs.CfnCluster",
):
    '''The ``AWS::PCS::Cluster`` resource creates an AWS PCS cluster.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-cluster.html
    :cloudformationResource: AWS::PCS::Cluster
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pcs as pcs
        
        cfn_cluster = pcs.CfnCluster(self, "MyCfnCluster",
            networking=pcs.CfnCluster.NetworkingProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"]
            ),
            scheduler=pcs.CfnCluster.SchedulerProperty(
                type="type",
                version="version"
            ),
            size="size",
        
            # the properties below are optional
            name="name",
            slurm_configuration=pcs.CfnCluster.SlurmConfigurationProperty(
                accounting=pcs.CfnCluster.AccountingProperty(
                    mode="mode",
        
                    # the properties below are optional
                    default_purge_time_in_days=123
                ),
                auth_key=pcs.CfnCluster.AuthKeyProperty(
                    secret_arn="secretArn",
                    secret_version="secretVersion"
                ),
                scale_down_idle_time_in_seconds=123,
                slurm_custom_settings=[pcs.CfnCluster.SlurmCustomSettingProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )]
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        networking: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.NetworkingProperty", typing.Dict[builtins.str, typing.Any]]],
        scheduler: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.SchedulerProperty", typing.Dict[builtins.str, typing.Any]]],
        size: builtins.str,
        name: typing.Optional[builtins.str] = None,
        slurm_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.SlurmConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param networking: The networking configuration for the cluster's control plane.
        :param scheduler: The cluster management and job scheduling software associated with the cluster.
        :param size: The size of the cluster.
        :param name: The name that identifies the cluster.
        :param slurm_configuration: Additional options related to the Slurm scheduler.
        :param tags: 1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3eeeaf566612baca2013a4f6d5c60484ee36ebc0edd307d32ef21991c170b65)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(
            networking=networking,
            scheduler=scheduler,
            size=size,
            name=name,
            slurm_configuration=slurm_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad41b9587f0f8c306a5663de2a8a6102111fcb7fc8d0e9a53a589055d6beaedc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6de5406d3a652bc9f44810e2ec4b074eabc97b2d888228c1ef6aa15a9be62dd7)
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
        '''The unique Amazon Resource Name (ARN) of the cluster.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEndpoints")
    def attr_endpoints(self) -> _IResolvable_da3f097b:
        '''The list of endpoints available for interaction with the scheduler.

        :cloudformationAttribute: Endpoints
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="attrErrorInfo")
    def attr_error_info(self) -> _IResolvable_da3f097b:
        '''The list of errors that occurred during cluster provisioning.

        :cloudformationAttribute: ErrorInfo
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrErrorInfo"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The generated unique ID of the cluster.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The provisioning status of the cluster.

        The provisioning status doesn't indicate the overall health of the cluster.

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
    @jsii.member(jsii_name="networking")
    def networking(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCluster.NetworkingProperty"]:
        '''The networking configuration for the cluster's control plane.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCluster.NetworkingProperty"], jsii.get(self, "networking"))

    @networking.setter
    def networking(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCluster.NetworkingProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55c1ec55aa513ac3501a36d2ae996a234035f2352cdef00bfd71db7d9a57e50c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networking", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scheduler")
    def scheduler(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCluster.SchedulerProperty"]:
        '''The cluster management and job scheduling software associated with the cluster.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCluster.SchedulerProperty"], jsii.get(self, "scheduler"))

    @scheduler.setter
    def scheduler(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCluster.SchedulerProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d56c39b86f5541062b8866fd13a6f0b7c91e0e765586d45abea04f33cc267998)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduler", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        '''The size of the cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__991109fd44c9cf1840f37fe27f8e8d0dd425a7d35c40957d93e9cd3eda6960f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name that identifies the cluster.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02af9af912d0a7aca1a803881152b3dd95a43c257523e7b9af7a7e20581e9a9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="slurmConfiguration")
    def slurm_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.SlurmConfigurationProperty"]]:
        '''Additional options related to the Slurm scheduler.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.SlurmConfigurationProperty"]], jsii.get(self, "slurmConfiguration"))

    @slurm_configuration.setter
    def slurm_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.SlurmConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d87e1a23a15695700ae0058f31b0dfa9d42571eb71c777bac50f89be58cf34fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slurmConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''1 or more tags added to the resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b386ea2d0b46e98dda569b5edccc0da74b6c12d09181731c93163fcad15cefbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnCluster.AccountingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "mode": "mode",
            "default_purge_time_in_days": "defaultPurgeTimeInDays",
        },
    )
    class AccountingProperty:
        def __init__(
            self,
            *,
            mode: builtins.str,
            default_purge_time_in_days: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The accounting configuration includes configurable settings for Slurm accounting.

            It's a property of the ``ClusterSlurmConfiguration`` object.

            :param mode: The default value for ``mode`` is ``STANDARD`` . A value of ``STANDARD`` means Slurm accounting is enabled. Default: - "NONE"
            :param default_purge_time_in_days: The default value for all purge settings for ``slurmdbd.conf`` . For more information, see the `slurmdbd.conf documentation at SchedMD <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurmdbd.conf.html>`_ . The default value ``-1`` means there is no purge time and records persist as long as the cluster exists. .. epigraph:: ``0`` isn't a valid value. Default: - -1

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-accounting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                accounting_property = pcs.CfnCluster.AccountingProperty(
                    mode="mode",
                
                    # the properties below are optional
                    default_purge_time_in_days=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1371c6dd1b40632a0c832b301d232842e616e6e2e20240f16e1a18c257dec328)
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
                check_type(argname="argument default_purge_time_in_days", value=default_purge_time_in_days, expected_type=type_hints["default_purge_time_in_days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mode": mode,
            }
            if default_purge_time_in_days is not None:
                self._values["default_purge_time_in_days"] = default_purge_time_in_days

        @builtins.property
        def mode(self) -> builtins.str:
            '''The default value for ``mode`` is ``STANDARD`` .

            A value of ``STANDARD`` means Slurm accounting is enabled.

            :default: - "NONE"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-accounting.html#cfn-pcs-cluster-accounting-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def default_purge_time_in_days(self) -> typing.Optional[jsii.Number]:
            '''The default value for all purge settings for ``slurmdbd.conf`` . For more information, see the `slurmdbd.conf documentation at SchedMD <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurmdbd.conf.html>`_ .

            The default value ``-1`` means there is no purge time and records persist as long as the cluster exists.
            .. epigraph::

               ``0`` isn't a valid value.

            :default: - -1

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-accounting.html#cfn-pcs-cluster-accounting-defaultpurgetimeindays
            '''
            result = self._values.get("default_purge_time_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccountingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnCluster.AuthKeyProperty",
        jsii_struct_bases=[],
        name_mapping={"secret_arn": "secretArn", "secret_version": "secretVersion"},
    )
    class AuthKeyProperty:
        def __init__(
            self,
            *,
            secret_arn: builtins.str,
            secret_version: builtins.str,
        ) -> None:
            '''The shared Slurm key for authentication, also known as the *cluster secret* .

            :param secret_arn: The Amazon Resource Name (ARN) of the shared Slurm key.
            :param secret_version: The version of the shared Slurm key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-authkey.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                auth_key_property = pcs.CfnCluster.AuthKeyProperty(
                    secret_arn="secretArn",
                    secret_version="secretVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1864f71bcded956851b861671a045d1c7d6402331c1d756c5ac88d21e9fe823c)
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument secret_version", value=secret_version, expected_type=type_hints["secret_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "secret_arn": secret_arn,
                "secret_version": secret_version,
            }

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the shared Slurm key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-authkey.html#cfn-pcs-cluster-authkey-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_version(self) -> builtins.str:
            '''The version of the shared Slurm key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-authkey.html#cfn-pcs-cluster-authkey-secretversion
            '''
            result = self._values.get("secret_version")
            assert result is not None, "Required property 'secret_version' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthKeyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnCluster.EndpointProperty",
        jsii_struct_bases=[],
        name_mapping={
            "port": "port",
            "private_ip_address": "privateIpAddress",
            "type": "type",
            "public_ip_address": "publicIpAddress",
        },
    )
    class EndpointProperty:
        def __init__(
            self,
            *,
            port: builtins.str,
            private_ip_address: builtins.str,
            type: builtins.str,
            public_ip_address: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An endpoint available for interaction with the scheduler.

            :param port: The endpoint's connection port number.
            :param private_ip_address: The endpoint's private IP address.
            :param type: Indicates the type of endpoint running at the specific IP address.
            :param public_ip_address: The endpoint's public IP address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-endpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                endpoint_property = pcs.CfnCluster.EndpointProperty(
                    port="port",
                    private_ip_address="privateIpAddress",
                    type="type",
                
                    # the properties below are optional
                    public_ip_address="publicIpAddress"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fb46faa4736fd5bede060ea1460c35898193ef49ace1726974a1db8958312929)
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument private_ip_address", value=private_ip_address, expected_type=type_hints["private_ip_address"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument public_ip_address", value=public_ip_address, expected_type=type_hints["public_ip_address"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "port": port,
                "private_ip_address": private_ip_address,
                "type": type,
            }
            if public_ip_address is not None:
                self._values["public_ip_address"] = public_ip_address

        @builtins.property
        def port(self) -> builtins.str:
            '''The endpoint's connection port number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-endpoint.html#cfn-pcs-cluster-endpoint-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def private_ip_address(self) -> builtins.str:
            '''The endpoint's private IP address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-endpoint.html#cfn-pcs-cluster-endpoint-privateipaddress
            '''
            result = self._values.get("private_ip_address")
            assert result is not None, "Required property 'private_ip_address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''Indicates the type of endpoint running at the specific IP address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-endpoint.html#cfn-pcs-cluster-endpoint-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def public_ip_address(self) -> typing.Optional[builtins.str]:
            '''The endpoint's public IP address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-endpoint.html#cfn-pcs-cluster-endpoint-publicipaddress
            '''
            result = self._values.get("public_ip_address")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnCluster.ErrorInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"code": "code", "message": "message"},
    )
    class ErrorInfoProperty:
        def __init__(
            self,
            *,
            code: typing.Optional[builtins.str] = None,
            message: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An error that occurred during resource provisioning.

            :param code: The short-form error code.
            :param message: The detailed error information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-errorinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                error_info_property = pcs.CfnCluster.ErrorInfoProperty(
                    code="code",
                    message="message"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b9e127e61b0ea75f45a99bba1dcc51875a9ecf36ea91f697889ebe4cb4a8e301)
                check_type(argname="argument code", value=code, expected_type=type_hints["code"])
                check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if code is not None:
                self._values["code"] = code
            if message is not None:
                self._values["message"] = message

        @builtins.property
        def code(self) -> typing.Optional[builtins.str]:
            '''The short-form error code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-errorinfo.html#cfn-pcs-cluster-errorinfo-code
            '''
            result = self._values.get("code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def message(self) -> typing.Optional[builtins.str]:
            '''The detailed error information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-errorinfo.html#cfn-pcs-cluster-errorinfo-message
            '''
            result = self._values.get("message")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ErrorInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnCluster.NetworkingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class NetworkingProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''TThe networking configuration for the cluster's control plane.

            :param security_group_ids: The list of security group IDs associated with the Elastic Network Interface (ENI) created in subnets.
            :param subnet_ids: The list of subnet IDs where AWS PCS creates an Elastic Network Interface (ENI) to enable communication between managed controllers and AWS PCS resources. The subnet must have an available IP address, cannot reside in AWS Outposts, AWS Wavelength, or an AWS Local Zone. AWS PCS currently supports only 1 subnet in this list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-networking.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                networking_property = pcs.CfnCluster.NetworkingProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__82c7f3d28e2ed0d063467ea787c6cfc31c28d4c5f26ef1ddf71940887dea9d1f)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of security group IDs associated with the Elastic Network Interface (ENI) created in subnets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-networking.html#cfn-pcs-cluster-networking-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of subnet IDs where AWS PCS creates an Elastic Network Interface (ENI) to enable communication between managed controllers and AWS PCS resources.

            The subnet must have an available IP address, cannot reside in AWS Outposts, AWS Wavelength, or an AWS Local Zone. AWS PCS currently supports only 1 subnet in this list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-networking.html#cfn-pcs-cluster-networking-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnCluster.SchedulerProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "version": "version"},
    )
    class SchedulerProperty:
        def __init__(self, *, type: builtins.str, version: builtins.str) -> None:
            '''The cluster management and job scheduling software associated with the cluster.

            :param type: The software AWS PCS uses to manage cluster scaling and job scheduling.
            :param version: The version of the specified scheduling software that AWS PCS uses to manage cluster scaling and job scheduling.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-scheduler.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                scheduler_property = pcs.CfnCluster.SchedulerProperty(
                    type="type",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fe24d9f1c44d1db4489549227b033216d5b6490b74f43ce9c2871e34c4d886ce)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
                "version": version,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''The software AWS PCS uses to manage cluster scaling and job scheduling.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-scheduler.html#cfn-pcs-cluster-scheduler-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> builtins.str:
            '''The version of the specified scheduling software that AWS PCS uses to manage cluster scaling and job scheduling.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-scheduler.html#cfn-pcs-cluster-scheduler-version
            '''
            result = self._values.get("version")
            assert result is not None, "Required property 'version' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchedulerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnCluster.SlurmConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "accounting": "accounting",
            "auth_key": "authKey",
            "scale_down_idle_time_in_seconds": "scaleDownIdleTimeInSeconds",
            "slurm_custom_settings": "slurmCustomSettings",
        },
    )
    class SlurmConfigurationProperty:
        def __init__(
            self,
            *,
            accounting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.AccountingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            auth_key: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.AuthKeyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            scale_down_idle_time_in_seconds: typing.Optional[jsii.Number] = None,
            slurm_custom_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCluster.SlurmCustomSettingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Additional options related to the Slurm scheduler.

            :param accounting: The accounting configuration includes configurable settings for Slurm accounting.
            :param auth_key: The shared Slurm key for authentication, also known as the cluster secret.
            :param scale_down_idle_time_in_seconds: The time before an idle node is scaled down.
            :param slurm_custom_settings: Additional Slurm-specific configuration that directly maps to Slurm settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-slurmconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                slurm_configuration_property = pcs.CfnCluster.SlurmConfigurationProperty(
                    accounting=pcs.CfnCluster.AccountingProperty(
                        mode="mode",
                
                        # the properties below are optional
                        default_purge_time_in_days=123
                    ),
                    auth_key=pcs.CfnCluster.AuthKeyProperty(
                        secret_arn="secretArn",
                        secret_version="secretVersion"
                    ),
                    scale_down_idle_time_in_seconds=123,
                    slurm_custom_settings=[pcs.CfnCluster.SlurmCustomSettingProperty(
                        parameter_name="parameterName",
                        parameter_value="parameterValue"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e6bb8855a5cf237041c92e56f09fd1b1d2d40c49f363bfde280100fbfd6f137f)
                check_type(argname="argument accounting", value=accounting, expected_type=type_hints["accounting"])
                check_type(argname="argument auth_key", value=auth_key, expected_type=type_hints["auth_key"])
                check_type(argname="argument scale_down_idle_time_in_seconds", value=scale_down_idle_time_in_seconds, expected_type=type_hints["scale_down_idle_time_in_seconds"])
                check_type(argname="argument slurm_custom_settings", value=slurm_custom_settings, expected_type=type_hints["slurm_custom_settings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if accounting is not None:
                self._values["accounting"] = accounting
            if auth_key is not None:
                self._values["auth_key"] = auth_key
            if scale_down_idle_time_in_seconds is not None:
                self._values["scale_down_idle_time_in_seconds"] = scale_down_idle_time_in_seconds
            if slurm_custom_settings is not None:
                self._values["slurm_custom_settings"] = slurm_custom_settings

        @builtins.property
        def accounting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.AccountingProperty"]]:
            '''The accounting configuration includes configurable settings for Slurm accounting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-slurmconfiguration.html#cfn-pcs-cluster-slurmconfiguration-accounting
            '''
            result = self._values.get("accounting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.AccountingProperty"]], result)

        @builtins.property
        def auth_key(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.AuthKeyProperty"]]:
            '''The shared Slurm key for authentication, also known as the cluster secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-slurmconfiguration.html#cfn-pcs-cluster-slurmconfiguration-authkey
            '''
            result = self._values.get("auth_key")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCluster.AuthKeyProperty"]], result)

        @builtins.property
        def scale_down_idle_time_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The time before an idle node is scaled down.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-slurmconfiguration.html#cfn-pcs-cluster-slurmconfiguration-scaledownidletimeinseconds
            '''
            result = self._values.get("scale_down_idle_time_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def slurm_custom_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.SlurmCustomSettingProperty"]]]]:
            '''Additional Slurm-specific configuration that directly maps to Slurm settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-slurmconfiguration.html#cfn-pcs-cluster-slurmconfiguration-slurmcustomsettings
            '''
            result = self._values.get("slurm_custom_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCluster.SlurmCustomSettingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlurmConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnCluster.SlurmCustomSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class SlurmCustomSettingProperty:
        def __init__(
            self,
            *,
            parameter_name: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''Additional settings that directly map to Slurm settings.

            :param parameter_name: AWS PCS supports configuration of the following Slurm parameters:. - For *clusters* - ```Prolog`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Prolog_1>`_ - ```Epilog`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Epilog_1>`_ - ```SelectTypeParameters`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_SelectTypeParameters>`_ - For *compute node groups* - ```Weight`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Weight>`_ - ```RealMemory`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Weight>`_
            :param parameter_value: The values for the configured Slurm settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-slurmcustomsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                slurm_custom_setting_property = pcs.CfnCluster.SlurmCustomSettingProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b9d168abcd7adc19d99485fc5db81c30bba87bb255608ac3a4487d1a1028fd33)
                check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parameter_name": parameter_name,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_name(self) -> builtins.str:
            '''AWS PCS supports configuration of the following Slurm parameters:.

            - For *clusters*
            - ```Prolog`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Prolog_1>`_
            - ```Epilog`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Epilog_1>`_
            - ```SelectTypeParameters`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_SelectTypeParameters>`_
            - For *compute node groups*
            - ```Weight`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Weight>`_
            - ```RealMemory`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Weight>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-slurmcustomsetting.html#cfn-pcs-cluster-slurmcustomsetting-parametername
            '''
            result = self._values.get("parameter_name")
            assert result is not None, "Required property 'parameter_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''The values for the configured Slurm settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-slurmcustomsetting.html#cfn-pcs-cluster-slurmcustomsetting-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlurmCustomSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pcs.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "networking": "networking",
        "scheduler": "scheduler",
        "size": "size",
        "name": "name",
        "slurm_configuration": "slurmConfiguration",
        "tags": "tags",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        networking: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.NetworkingProperty, typing.Dict[builtins.str, typing.Any]]],
        scheduler: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.SchedulerProperty, typing.Dict[builtins.str, typing.Any]]],
        size: builtins.str,
        name: typing.Optional[builtins.str] = None,
        slurm_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.SlurmConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCluster``.

        :param networking: The networking configuration for the cluster's control plane.
        :param scheduler: The cluster management and job scheduling software associated with the cluster.
        :param size: The size of the cluster.
        :param name: The name that identifies the cluster.
        :param slurm_configuration: Additional options related to the Slurm scheduler.
        :param tags: 1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-cluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pcs as pcs
            
            cfn_cluster_props = pcs.CfnClusterProps(
                networking=pcs.CfnCluster.NetworkingProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                ),
                scheduler=pcs.CfnCluster.SchedulerProperty(
                    type="type",
                    version="version"
                ),
                size="size",
            
                # the properties below are optional
                name="name",
                slurm_configuration=pcs.CfnCluster.SlurmConfigurationProperty(
                    accounting=pcs.CfnCluster.AccountingProperty(
                        mode="mode",
            
                        # the properties below are optional
                        default_purge_time_in_days=123
                    ),
                    auth_key=pcs.CfnCluster.AuthKeyProperty(
                        secret_arn="secretArn",
                        secret_version="secretVersion"
                    ),
                    scale_down_idle_time_in_seconds=123,
                    slurm_custom_settings=[pcs.CfnCluster.SlurmCustomSettingProperty(
                        parameter_name="parameterName",
                        parameter_value="parameterValue"
                    )]
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1acc8d7c41893eaa3f211b6514471817eb607a349cab301161899ae592f0bdf0)
            check_type(argname="argument networking", value=networking, expected_type=type_hints["networking"])
            check_type(argname="argument scheduler", value=scheduler, expected_type=type_hints["scheduler"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument slurm_configuration", value=slurm_configuration, expected_type=type_hints["slurm_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "networking": networking,
            "scheduler": scheduler,
            "size": size,
        }
        if name is not None:
            self._values["name"] = name
        if slurm_configuration is not None:
            self._values["slurm_configuration"] = slurm_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def networking(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCluster.NetworkingProperty]:
        '''The networking configuration for the cluster's control plane.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-cluster.html#cfn-pcs-cluster-networking
        '''
        result = self._values.get("networking")
        assert result is not None, "Required property 'networking' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCluster.NetworkingProperty], result)

    @builtins.property
    def scheduler(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCluster.SchedulerProperty]:
        '''The cluster management and job scheduling software associated with the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-cluster.html#cfn-pcs-cluster-scheduler
        '''
        result = self._values.get("scheduler")
        assert result is not None, "Required property 'scheduler' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCluster.SchedulerProperty], result)

    @builtins.property
    def size(self) -> builtins.str:
        '''The size of the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-cluster.html#cfn-pcs-cluster-size
        '''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name that identifies the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-cluster.html#cfn-pcs-cluster-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slurm_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.SlurmConfigurationProperty]]:
        '''Additional options related to the Slurm scheduler.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-cluster.html#cfn-pcs-cluster-slurmconfiguration
        '''
        result = self._values.get("slurm_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.SlurmConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''1 or more tags added to the resource.

        Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-cluster.html#cfn-pcs-cluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnComputeNodeGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pcs.CfnComputeNodeGroup",
):
    '''The ``AWS::PCS::ComputeNodeGroup`` resource creates an AWS PCS compute node group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-computenodegroup.html
    :cloudformationResource: AWS::PCS::ComputeNodeGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pcs as pcs
        
        cfn_compute_node_group = pcs.CfnComputeNodeGroup(self, "MyCfnComputeNodeGroup",
            cluster_id="clusterId",
            custom_launch_template=pcs.CfnComputeNodeGroup.CustomLaunchTemplateProperty(
                version="version",
        
                # the properties below are optional
                template_id="templateId"
            ),
            iam_instance_profile_arn="iamInstanceProfileArn",
            instance_configs=[pcs.CfnComputeNodeGroup.InstanceConfigProperty(
                instance_type="instanceType"
            )],
            scaling_configuration=pcs.CfnComputeNodeGroup.ScalingConfigurationProperty(
                max_instance_count=123,
                min_instance_count=123
            ),
            subnet_ids=["subnetIds"],
        
            # the properties below are optional
            ami_id="amiId",
            name="name",
            purchase_option="purchaseOption",
            slurm_configuration=pcs.CfnComputeNodeGroup.SlurmConfigurationProperty(
                slurm_custom_settings=[pcs.CfnComputeNodeGroup.SlurmCustomSettingProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )]
            ),
            spot_options=pcs.CfnComputeNodeGroup.SpotOptionsProperty(
                allocation_strategy="allocationStrategy"
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_id: builtins.str,
        custom_launch_template: typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputeNodeGroup.CustomLaunchTemplateProperty", typing.Dict[builtins.str, typing.Any]]],
        iam_instance_profile_arn: builtins.str,
        instance_configs: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputeNodeGroup.InstanceConfigProperty", typing.Dict[builtins.str, typing.Any]]]]],
        scaling_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputeNodeGroup.ScalingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        subnet_ids: typing.Sequence[builtins.str],
        ami_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        purchase_option: typing.Optional[builtins.str] = None,
        slurm_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputeNodeGroup.SlurmConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        spot_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputeNodeGroup.SpotOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cluster_id: The ID of the cluster of the compute node group.
        :param custom_launch_template: An Amazon EC2 launch template AWS PCS uses to launch compute nodes.
        :param iam_instance_profile_arn: The Amazon Resource Name (ARN) of the IAM instance profile used to pass an IAM role when launching EC2 instances. The role contained in your instance profile must have pcs:RegisterComputeNodeGroupInstance permissions attached to provision instances correctly.
        :param instance_configs: A list of EC2 instance configurations that AWS PCS can provision in the compute node group.
        :param scaling_configuration: Specifies the boundaries of the compute node group auto scaling.
        :param subnet_ids: The list of subnet IDs where instances are provisioned by the compute node group. The subnets must be in the same VPC as the cluster.
        :param ami_id: The ID of the Amazon Machine Image (AMI) that AWS PCS uses to launch instances. If not provided, AWS PCS uses the AMI ID specified in the custom launch template.
        :param name: The name that identifies the compute node group.
        :param purchase_option: Specifies how EC2 instances are purchased on your behalf. AWS PCS supports On-Demand and Spot instances. For more information, see Instance purchasing options in the Amazon Elastic Compute Cloud User Guide. If you don't provide this option, it defaults to On-Demand.
        :param slurm_configuration: Additional options related to the Slurm scheduler.
        :param spot_options: Additional configuration when you specify ``SPOT`` as the ``purchaseOption`` .
        :param tags: 1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d74625cecbce8d2048b29b24f3148123fb31c64b330ed51fd45d2b2c42d1c20)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnComputeNodeGroupProps(
            cluster_id=cluster_id,
            custom_launch_template=custom_launch_template,
            iam_instance_profile_arn=iam_instance_profile_arn,
            instance_configs=instance_configs,
            scaling_configuration=scaling_configuration,
            subnet_ids=subnet_ids,
            ami_id=ami_id,
            name=name,
            purchase_option=purchase_option,
            slurm_configuration=slurm_configuration,
            spot_options=spot_options,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d833050301c35ecc35d9e2cf88fc748a8f8174e49289d0e2719e757def93e83c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__571860de08b34398201b8498268e8b69422d6e17de99d62fd83b52005d26a6b5)
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
        '''The unique Amazon Resource Name (ARN) of the compute node group.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrErrorInfo")
    def attr_error_info(self) -> _IResolvable_da3f097b:
        '''The list of errors that occurred during compute node group provisioning.

        :cloudformationAttribute: ErrorInfo
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrErrorInfo"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The generated unique ID of the compute node group.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The provisioning status of the compute node group.

        The provisioning status doesn't indicate the overall health of the compute node group.

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
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        '''The ID of the cluster of the compute node group.'''
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27a33200e9f918661858505e376a9533b97ee45f0f14cd2c479bb9e61b1effc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="customLaunchTemplate")
    def custom_launch_template(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.CustomLaunchTemplateProperty"]:
        '''An Amazon EC2 launch template AWS PCS uses to launch compute nodes.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.CustomLaunchTemplateProperty"], jsii.get(self, "customLaunchTemplate"))

    @custom_launch_template.setter
    def custom_launch_template(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.CustomLaunchTemplateProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf4a47490919e9b97683082d58e0ccf8649fd09ec2c5f621c3f8467d84363706)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customLaunchTemplate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iamInstanceProfileArn")
    def iam_instance_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM instance profile used to pass an IAM role when launching EC2 instances.'''
        return typing.cast(builtins.str, jsii.get(self, "iamInstanceProfileArn"))

    @iam_instance_profile_arn.setter
    def iam_instance_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77021f3115c7344dc9b7365b13a661fa578c34c1997a99dd619003646b7e460a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamInstanceProfileArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="instanceConfigs")
    def instance_configs(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.InstanceConfigProperty"]]]:
        '''A list of EC2 instance configurations that AWS PCS can provision in the compute node group.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.InstanceConfigProperty"]]], jsii.get(self, "instanceConfigs"))

    @instance_configs.setter
    def instance_configs(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.InstanceConfigProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd2f09e3d9b4cca4eab96f7862d7a047649e41118beecac43ed36e424625aa02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceConfigs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scalingConfiguration")
    def scaling_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.ScalingConfigurationProperty"]:
        '''Specifies the boundaries of the compute node group auto scaling.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.ScalingConfigurationProperty"], jsii.get(self, "scalingConfiguration"))

    @scaling_configuration.setter
    def scaling_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.ScalingConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faa6826218f9909223a7fac326f705e3e75a1469e1ec902fe056022fd0a6adf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalingConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''The list of subnet IDs where instances are provisioned by the compute node group.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6c11a7ef6bbf97645d89e780e4819e5c51eacccbab5c6e46497a3e31accf32e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="amiId")
    def ami_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the Amazon Machine Image (AMI) that AWS PCS uses to launch instances.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amiId"))

    @ami_id.setter
    def ami_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce6f7916bab348203539e21c424ed76ed039fc805a1e3d704cca40baffc97318)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amiId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name that identifies the compute node group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__621c25d891dcaffc1e388ad783cc5d71aeffd2776b0166c92fce41e6d992d2d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="purchaseOption")
    def purchase_option(self) -> typing.Optional[builtins.str]:
        '''Specifies how EC2 instances are purchased on your behalf.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "purchaseOption"))

    @purchase_option.setter
    def purchase_option(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abf0b129d8eff2b9d98cc25ed6c3cbfebb7f706aa5948692e942f1a485c29a79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "purchaseOption", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="slurmConfiguration")
    def slurm_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.SlurmConfigurationProperty"]]:
        '''Additional options related to the Slurm scheduler.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.SlurmConfigurationProperty"]], jsii.get(self, "slurmConfiguration"))

    @slurm_configuration.setter
    def slurm_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.SlurmConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d5c6af28cfa6220ac6fe417a830b4b39cfb3320cd91ef31f4ef71aa5f6d934b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slurmConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="spotOptions")
    def spot_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.SpotOptionsProperty"]]:
        '''Additional configuration when you specify ``SPOT`` as the ``purchaseOption`` .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.SpotOptionsProperty"]], jsii.get(self, "spotOptions"))

    @spot_options.setter
    def spot_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.SpotOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25d7dc8c33129932f54cb9e69a7f2e96a79caaf423f50891bd309efbb2cf8a56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spotOptions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''1 or more tags added to the resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f9d940f011938958eb70282b41c84f70c7f86093c1788ec73b310de39dd817d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnComputeNodeGroup.CustomLaunchTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={"version": "version", "template_id": "templateId"},
    )
    class CustomLaunchTemplateProperty:
        def __init__(
            self,
            *,
            version: builtins.str,
            template_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An Amazon EC2 launch template AWS PCS uses to launch compute nodes.

            :param version: The version of the EC2 launch template to use to provision instances.
            :param template_id: The ID of the EC2 launch template to use to provision instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-customlaunchtemplate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                custom_launch_template_property = pcs.CfnComputeNodeGroup.CustomLaunchTemplateProperty(
                    version="version",
                
                    # the properties below are optional
                    template_id="templateId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f5e18d4eaf127cbbf203643daa28b5c0a8105f4a3d48ce6e2c896d6f851d7911)
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
                check_type(argname="argument template_id", value=template_id, expected_type=type_hints["template_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "version": version,
            }
            if template_id is not None:
                self._values["template_id"] = template_id

        @builtins.property
        def version(self) -> builtins.str:
            '''The version of the EC2 launch template to use to provision instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-customlaunchtemplate.html#cfn-pcs-computenodegroup-customlaunchtemplate-version
            '''
            result = self._values.get("version")
            assert result is not None, "Required property 'version' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def template_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the EC2 launch template to use to provision instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-customlaunchtemplate.html#cfn-pcs-computenodegroup-customlaunchtemplate-templateid
            '''
            result = self._values.get("template_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomLaunchTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnComputeNodeGroup.ErrorInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"code": "code", "message": "message"},
    )
    class ErrorInfoProperty:
        def __init__(
            self,
            *,
            code: typing.Optional[builtins.str] = None,
            message: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The list of errors that occurred during compute node group provisioning.

            :param code: The short-form error code.
            :param message: The detailed error information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-errorinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                error_info_property = pcs.CfnComputeNodeGroup.ErrorInfoProperty(
                    code="code",
                    message="message"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__88387b075e6eeff950872537e019e72d8c0543b07c44cb6fd37f6a6580892efe)
                check_type(argname="argument code", value=code, expected_type=type_hints["code"])
                check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if code is not None:
                self._values["code"] = code
            if message is not None:
                self._values["message"] = message

        @builtins.property
        def code(self) -> typing.Optional[builtins.str]:
            '''The short-form error code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-errorinfo.html#cfn-pcs-computenodegroup-errorinfo-code
            '''
            result = self._values.get("code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def message(self) -> typing.Optional[builtins.str]:
            '''The detailed error information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-errorinfo.html#cfn-pcs-computenodegroup-errorinfo-message
            '''
            result = self._values.get("message")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ErrorInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnComputeNodeGroup.InstanceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"instance_type": "instanceType"},
    )
    class InstanceConfigProperty:
        def __init__(
            self,
            *,
            instance_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An EC2 instance configuration AWS PCS uses to launch compute nodes.

            :param instance_type: The EC2 instance type that AWS PCS can provision in the compute node group. Example: ``t2.xlarge``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-instanceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                instance_config_property = pcs.CfnComputeNodeGroup.InstanceConfigProperty(
                    instance_type="instanceType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e94b232b9d47b7a1d244e32e3a5dc754392f55d51698be51f1a5de8260de9a0b)
                check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if instance_type is not None:
                self._values["instance_type"] = instance_type

        @builtins.property
        def instance_type(self) -> typing.Optional[builtins.str]:
            '''The EC2 instance type that AWS PCS can provision in the compute node group.

            Example: ``t2.xlarge``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-instanceconfig.html#cfn-pcs-computenodegroup-instanceconfig-instancetype
            '''
            result = self._values.get("instance_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnComputeNodeGroup.ScalingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_instance_count": "maxInstanceCount",
            "min_instance_count": "minInstanceCount",
        },
    )
    class ScalingConfigurationProperty:
        def __init__(
            self,
            *,
            max_instance_count: jsii.Number,
            min_instance_count: jsii.Number,
        ) -> None:
            '''Specifies the boundaries of the compute node group auto scaling.

            :param max_instance_count: The upper bound of the number of instances allowed in the compute fleet.
            :param min_instance_count: The lower bound of the number of instances allowed in the compute fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-scalingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                scaling_configuration_property = pcs.CfnComputeNodeGroup.ScalingConfigurationProperty(
                    max_instance_count=123,
                    min_instance_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c591f6ad958f29b5e6c332ca3927c8ba0e76bc075461fbecdd513918b5d0bbcd)
                check_type(argname="argument max_instance_count", value=max_instance_count, expected_type=type_hints["max_instance_count"])
                check_type(argname="argument min_instance_count", value=min_instance_count, expected_type=type_hints["min_instance_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_instance_count": max_instance_count,
                "min_instance_count": min_instance_count,
            }

        @builtins.property
        def max_instance_count(self) -> jsii.Number:
            '''The upper bound of the number of instances allowed in the compute fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-scalingconfiguration.html#cfn-pcs-computenodegroup-scalingconfiguration-maxinstancecount
            '''
            result = self._values.get("max_instance_count")
            assert result is not None, "Required property 'max_instance_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def min_instance_count(self) -> jsii.Number:
            '''The lower bound of the number of instances allowed in the compute fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-scalingconfiguration.html#cfn-pcs-computenodegroup-scalingconfiguration-mininstancecount
            '''
            result = self._values.get("min_instance_count")
            assert result is not None, "Required property 'min_instance_count' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnComputeNodeGroup.SlurmConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"slurm_custom_settings": "slurmCustomSettings"},
    )
    class SlurmConfigurationProperty:
        def __init__(
            self,
            *,
            slurm_custom_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnComputeNodeGroup.SlurmCustomSettingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Additional options related to the Slurm scheduler.

            :param slurm_custom_settings: Additional Slurm-specific configuration that directly maps to Slurm settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-slurmconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                slurm_configuration_property = pcs.CfnComputeNodeGroup.SlurmConfigurationProperty(
                    slurm_custom_settings=[pcs.CfnComputeNodeGroup.SlurmCustomSettingProperty(
                        parameter_name="parameterName",
                        parameter_value="parameterValue"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__33800b7dfb5193bcd6bf17beca91a47b148b0349a0de5c1a62f72612ea620096)
                check_type(argname="argument slurm_custom_settings", value=slurm_custom_settings, expected_type=type_hints["slurm_custom_settings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if slurm_custom_settings is not None:
                self._values["slurm_custom_settings"] = slurm_custom_settings

        @builtins.property
        def slurm_custom_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.SlurmCustomSettingProperty"]]]]:
            '''Additional Slurm-specific configuration that directly maps to Slurm settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-slurmconfiguration.html#cfn-pcs-computenodegroup-slurmconfiguration-slurmcustomsettings
            '''
            result = self._values.get("slurm_custom_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnComputeNodeGroup.SlurmCustomSettingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlurmConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnComputeNodeGroup.SlurmCustomSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class SlurmCustomSettingProperty:
        def __init__(
            self,
            *,
            parameter_name: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''Additional settings that directly map to Slurm settings.

            :param parameter_name: AWS PCS supports configuration of the following Slurm parameters:. - For *clusters* - ```Prolog`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Prolog_1>`_ - ```Epilog`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Epilog_1>`_ - ```SelectTypeParameters`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_SelectTypeParameters>`_ - For *compute node groups* - ```Weight`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Weight>`_ - ```RealMemory`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Weight>`_
            :param parameter_value: The values for the configured Slurm settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-slurmcustomsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                slurm_custom_setting_property = pcs.CfnComputeNodeGroup.SlurmCustomSettingProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__95bf383e09d59731c7b8cdac63a717d5a44f4c4d44a291a247b4ebda5f004d3c)
                check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parameter_name": parameter_name,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_name(self) -> builtins.str:
            '''AWS PCS supports configuration of the following Slurm parameters:.

            - For *clusters*
            - ```Prolog`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Prolog_1>`_
            - ```Epilog`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Epilog_1>`_
            - ```SelectTypeParameters`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_SelectTypeParameters>`_
            - For *compute node groups*
            - ```Weight`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Weight>`_
            - ```RealMemory`` <https://docs.aws.amazon.com/https://slurm.schedmd.com/slurm.conf.html#OPT_Weight>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-slurmcustomsetting.html#cfn-pcs-computenodegroup-slurmcustomsetting-parametername
            '''
            result = self._values.get("parameter_name")
            assert result is not None, "Required property 'parameter_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''The values for the configured Slurm settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-slurmcustomsetting.html#cfn-pcs-computenodegroup-slurmcustomsetting-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlurmCustomSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnComputeNodeGroup.SpotOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"allocation_strategy": "allocationStrategy"},
    )
    class SpotOptionsProperty:
        def __init__(
            self,
            *,
            allocation_strategy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Additional configuration when you specify ``SPOT`` as the ``purchaseOption`` .

            :param allocation_strategy: The Amazon EC2 allocation strategy AWS PCS uses to provision EC2 instances. AWS PCS supports lowest price, capacity optimized, and price capacity optimized. If you don't provide this option, it defaults to price capacity optimized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-spotoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                spot_options_property = pcs.CfnComputeNodeGroup.SpotOptionsProperty(
                    allocation_strategy="allocationStrategy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__adf4042ef194d53ff84c49fd66b8d9e370cc1fb06ce3e5dfca9c196a9102c196)
                check_type(argname="argument allocation_strategy", value=allocation_strategy, expected_type=type_hints["allocation_strategy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allocation_strategy is not None:
                self._values["allocation_strategy"] = allocation_strategy

        @builtins.property
        def allocation_strategy(self) -> typing.Optional[builtins.str]:
            '''The Amazon EC2 allocation strategy AWS PCS uses to provision EC2 instances.

            AWS PCS supports lowest price, capacity optimized, and price capacity optimized. If you don't provide this option, it defaults to price capacity optimized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-computenodegroup-spotoptions.html#cfn-pcs-computenodegroup-spotoptions-allocationstrategy
            '''
            result = self._values.get("allocation_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpotOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pcs.CfnComputeNodeGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_id": "clusterId",
        "custom_launch_template": "customLaunchTemplate",
        "iam_instance_profile_arn": "iamInstanceProfileArn",
        "instance_configs": "instanceConfigs",
        "scaling_configuration": "scalingConfiguration",
        "subnet_ids": "subnetIds",
        "ami_id": "amiId",
        "name": "name",
        "purchase_option": "purchaseOption",
        "slurm_configuration": "slurmConfiguration",
        "spot_options": "spotOptions",
        "tags": "tags",
    },
)
class CfnComputeNodeGroupProps:
    def __init__(
        self,
        *,
        cluster_id: builtins.str,
        custom_launch_template: typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.CustomLaunchTemplateProperty, typing.Dict[builtins.str, typing.Any]]],
        iam_instance_profile_arn: builtins.str,
        instance_configs: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.InstanceConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
        scaling_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.ScalingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        subnet_ids: typing.Sequence[builtins.str],
        ami_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        purchase_option: typing.Optional[builtins.str] = None,
        slurm_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.SlurmConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        spot_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.SpotOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnComputeNodeGroup``.

        :param cluster_id: The ID of the cluster of the compute node group.
        :param custom_launch_template: An Amazon EC2 launch template AWS PCS uses to launch compute nodes.
        :param iam_instance_profile_arn: The Amazon Resource Name (ARN) of the IAM instance profile used to pass an IAM role when launching EC2 instances. The role contained in your instance profile must have pcs:RegisterComputeNodeGroupInstance permissions attached to provision instances correctly.
        :param instance_configs: A list of EC2 instance configurations that AWS PCS can provision in the compute node group.
        :param scaling_configuration: Specifies the boundaries of the compute node group auto scaling.
        :param subnet_ids: The list of subnet IDs where instances are provisioned by the compute node group. The subnets must be in the same VPC as the cluster.
        :param ami_id: The ID of the Amazon Machine Image (AMI) that AWS PCS uses to launch instances. If not provided, AWS PCS uses the AMI ID specified in the custom launch template.
        :param name: The name that identifies the compute node group.
        :param purchase_option: Specifies how EC2 instances are purchased on your behalf. AWS PCS supports On-Demand and Spot instances. For more information, see Instance purchasing options in the Amazon Elastic Compute Cloud User Guide. If you don't provide this option, it defaults to On-Demand.
        :param slurm_configuration: Additional options related to the Slurm scheduler.
        :param spot_options: Additional configuration when you specify ``SPOT`` as the ``purchaseOption`` .
        :param tags: 1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-computenodegroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pcs as pcs
            
            cfn_compute_node_group_props = pcs.CfnComputeNodeGroupProps(
                cluster_id="clusterId",
                custom_launch_template=pcs.CfnComputeNodeGroup.CustomLaunchTemplateProperty(
                    version="version",
            
                    # the properties below are optional
                    template_id="templateId"
                ),
                iam_instance_profile_arn="iamInstanceProfileArn",
                instance_configs=[pcs.CfnComputeNodeGroup.InstanceConfigProperty(
                    instance_type="instanceType"
                )],
                scaling_configuration=pcs.CfnComputeNodeGroup.ScalingConfigurationProperty(
                    max_instance_count=123,
                    min_instance_count=123
                ),
                subnet_ids=["subnetIds"],
            
                # the properties below are optional
                ami_id="amiId",
                name="name",
                purchase_option="purchaseOption",
                slurm_configuration=pcs.CfnComputeNodeGroup.SlurmConfigurationProperty(
                    slurm_custom_settings=[pcs.CfnComputeNodeGroup.SlurmCustomSettingProperty(
                        parameter_name="parameterName",
                        parameter_value="parameterValue"
                    )]
                ),
                spot_options=pcs.CfnComputeNodeGroup.SpotOptionsProperty(
                    allocation_strategy="allocationStrategy"
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b89ff3536491b7ea531bd9d6ca00d7d32a25ce4c02b926c6d677abde115a012d)
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument custom_launch_template", value=custom_launch_template, expected_type=type_hints["custom_launch_template"])
            check_type(argname="argument iam_instance_profile_arn", value=iam_instance_profile_arn, expected_type=type_hints["iam_instance_profile_arn"])
            check_type(argname="argument instance_configs", value=instance_configs, expected_type=type_hints["instance_configs"])
            check_type(argname="argument scaling_configuration", value=scaling_configuration, expected_type=type_hints["scaling_configuration"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument ami_id", value=ami_id, expected_type=type_hints["ami_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument purchase_option", value=purchase_option, expected_type=type_hints["purchase_option"])
            check_type(argname="argument slurm_configuration", value=slurm_configuration, expected_type=type_hints["slurm_configuration"])
            check_type(argname="argument spot_options", value=spot_options, expected_type=type_hints["spot_options"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_id": cluster_id,
            "custom_launch_template": custom_launch_template,
            "iam_instance_profile_arn": iam_instance_profile_arn,
            "instance_configs": instance_configs,
            "scaling_configuration": scaling_configuration,
            "subnet_ids": subnet_ids,
        }
        if ami_id is not None:
            self._values["ami_id"] = ami_id
        if name is not None:
            self._values["name"] = name
        if purchase_option is not None:
            self._values["purchase_option"] = purchase_option
        if slurm_configuration is not None:
            self._values["slurm_configuration"] = slurm_configuration
        if spot_options is not None:
            self._values["spot_options"] = spot_options
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cluster_id(self) -> builtins.str:
        '''The ID of the cluster of the compute node group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-computenodegroup.html#cfn-pcs-computenodegroup-clusterid
        '''
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_launch_template(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnComputeNodeGroup.CustomLaunchTemplateProperty]:
        '''An Amazon EC2 launch template AWS PCS uses to launch compute nodes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-computenodegroup.html#cfn-pcs-computenodegroup-customlaunchtemplate
        '''
        result = self._values.get("custom_launch_template")
        assert result is not None, "Required property 'custom_launch_template' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnComputeNodeGroup.CustomLaunchTemplateProperty], result)

    @builtins.property
    def iam_instance_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM instance profile used to pass an IAM role when launching EC2 instances.

        The role contained in your instance profile must have pcs:RegisterComputeNodeGroupInstance permissions attached to provision instances correctly.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-computenodegroup.html#cfn-pcs-computenodegroup-iaminstanceprofilearn
        '''
        result = self._values.get("iam_instance_profile_arn")
        assert result is not None, "Required property 'iam_instance_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_configs(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnComputeNodeGroup.InstanceConfigProperty]]]:
        '''A list of EC2 instance configurations that AWS PCS can provision in the compute node group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-computenodegroup.html#cfn-pcs-computenodegroup-instanceconfigs
        '''
        result = self._values.get("instance_configs")
        assert result is not None, "Required property 'instance_configs' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnComputeNodeGroup.InstanceConfigProperty]]], result)

    @builtins.property
    def scaling_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnComputeNodeGroup.ScalingConfigurationProperty]:
        '''Specifies the boundaries of the compute node group auto scaling.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-computenodegroup.html#cfn-pcs-computenodegroup-scalingconfiguration
        '''
        result = self._values.get("scaling_configuration")
        assert result is not None, "Required property 'scaling_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnComputeNodeGroup.ScalingConfigurationProperty], result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''The list of subnet IDs where instances are provisioned by the compute node group.

        The subnets must be in the same VPC as the cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-computenodegroup.html#cfn-pcs-computenodegroup-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def ami_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the Amazon Machine Image (AMI) that AWS PCS uses to launch instances.

        If not provided, AWS PCS uses the AMI ID specified in the custom launch template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-computenodegroup.html#cfn-pcs-computenodegroup-amiid
        '''
        result = self._values.get("ami_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name that identifies the compute node group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-computenodegroup.html#cfn-pcs-computenodegroup-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def purchase_option(self) -> typing.Optional[builtins.str]:
        '''Specifies how EC2 instances are purchased on your behalf.

        AWS PCS supports On-Demand and Spot instances. For more information, see Instance purchasing options in the Amazon Elastic Compute Cloud User Guide. If you don't provide this option, it defaults to On-Demand.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-computenodegroup.html#cfn-pcs-computenodegroup-purchaseoption
        '''
        result = self._values.get("purchase_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slurm_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComputeNodeGroup.SlurmConfigurationProperty]]:
        '''Additional options related to the Slurm scheduler.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-computenodegroup.html#cfn-pcs-computenodegroup-slurmconfiguration
        '''
        result = self._values.get("slurm_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComputeNodeGroup.SlurmConfigurationProperty]], result)

    @builtins.property
    def spot_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComputeNodeGroup.SpotOptionsProperty]]:
        '''Additional configuration when you specify ``SPOT`` as the ``purchaseOption`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-computenodegroup.html#cfn-pcs-computenodegroup-spotoptions
        '''
        result = self._values.get("spot_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComputeNodeGroup.SpotOptionsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''1 or more tags added to the resource.

        Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-computenodegroup.html#cfn-pcs-computenodegroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnComputeNodeGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnQueue(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pcs.CfnQueue",
):
    '''The ``AWS::PCS::Queue`` resource creates an AWS PCS queue.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-queue.html
    :cloudformationResource: AWS::PCS::Queue
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pcs as pcs
        
        cfn_queue = pcs.CfnQueue(self, "MyCfnQueue",
            cluster_id="clusterId",
        
            # the properties below are optional
            compute_node_group_configurations=[pcs.CfnQueue.ComputeNodeGroupConfigurationProperty(
                compute_node_group_id="computeNodeGroupId"
            )],
            name="name",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        cluster_id: builtins.str,
        compute_node_group_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnQueue.ComputeNodeGroupConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param cluster_id: The ID of the cluster of the queue.
        :param compute_node_group_configurations: The list of compute node group configurations associated with the queue. Queues assign jobs to associated compute node groups.
        :param name: The name that identifies the queue.
        :param tags: 1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__456edeb02414f262683a35f15a1fae223f92feec590d98024478f680e3249bdd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnQueueProps(
            cluster_id=cluster_id,
            compute_node_group_configurations=compute_node_group_configurations,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e91ae15ffe542b6e139af845f0fd58e29e3eb1de94ad2d790169a1ef4226536)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fedb84fc44c9a0375a3b3b2a4753f07a788f5775a01c39a2a16ef0736b04f3b1)
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
        '''The unique Amazon Resource Name (ARN) of the queue.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrErrorInfo")
    def attr_error_info(self) -> _IResolvable_da3f097b:
        '''The list of errors that occurred during queue provisioning.

        :cloudformationAttribute: ErrorInfo
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrErrorInfo"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The generated unique ID of the queue.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The provisioning status of the queue.

        The provisioning status doesn't indicate the overall health of the queue.

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
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        '''The ID of the cluster of the queue.'''
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dd96bf4d965aac7a933a9b0af29542239baf57d893776c7333dd76d3bff2ca8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="computeNodeGroupConfigurations")
    def compute_node_group_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnQueue.ComputeNodeGroupConfigurationProperty"]]]]:
        '''The list of compute node group configurations associated with the queue.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnQueue.ComputeNodeGroupConfigurationProperty"]]]], jsii.get(self, "computeNodeGroupConfigurations"))

    @compute_node_group_configurations.setter
    def compute_node_group_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnQueue.ComputeNodeGroupConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fa120ad7f68494c28ccc4186d82ee7a8ff23a8eb4615bb87e7c325c61e1a497)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeNodeGroupConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name that identifies the queue.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e4f1e9c61fd11b4d3ed4834db791c7064b5408b742dfa6c4a00a242858ad868)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''1 or more tags added to the resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31674031b3f2a49a29efb9edfdb5a54431db3db7616989edd3617113cd6b9afd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnQueue.ComputeNodeGroupConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"compute_node_group_id": "computeNodeGroupId"},
    )
    class ComputeNodeGroupConfigurationProperty:
        def __init__(
            self,
            *,
            compute_node_group_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The compute node group configuration for a queue.

            :param compute_node_group_id: The compute node group ID for the compute node group configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-queue-computenodegroupconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                compute_node_group_configuration_property = pcs.CfnQueue.ComputeNodeGroupConfigurationProperty(
                    compute_node_group_id="computeNodeGroupId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9cc981d8d2dee6d007be19b192d33155162e657cf0ddef3c82ac69bf13b0c34a)
                check_type(argname="argument compute_node_group_id", value=compute_node_group_id, expected_type=type_hints["compute_node_group_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if compute_node_group_id is not None:
                self._values["compute_node_group_id"] = compute_node_group_id

        @builtins.property
        def compute_node_group_id(self) -> typing.Optional[builtins.str]:
            '''The compute node group ID for the compute node group configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-queue-computenodegroupconfiguration.html#cfn-pcs-queue-computenodegroupconfiguration-computenodegroupid
            '''
            result = self._values.get("compute_node_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComputeNodeGroupConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcs.CfnQueue.ErrorInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"code": "code", "message": "message"},
    )
    class ErrorInfoProperty:
        def __init__(
            self,
            *,
            code: typing.Optional[builtins.str] = None,
            message: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An error that occurred during resource provisioning.

            :param code: The short-form error code.
            :param message: TBDThe detailed error information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-queue-errorinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcs as pcs
                
                error_info_property = pcs.CfnQueue.ErrorInfoProperty(
                    code="code",
                    message="message"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5e51eb0cec81203da74b9b3c33259135afec8fef04327498ab79338af5a9df34)
                check_type(argname="argument code", value=code, expected_type=type_hints["code"])
                check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if code is not None:
                self._values["code"] = code
            if message is not None:
                self._values["message"] = message

        @builtins.property
        def code(self) -> typing.Optional[builtins.str]:
            '''The short-form error code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-queue-errorinfo.html#cfn-pcs-queue-errorinfo-code
            '''
            result = self._values.get("code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def message(self) -> typing.Optional[builtins.str]:
            '''TBDThe detailed error information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-queue-errorinfo.html#cfn-pcs-queue-errorinfo-message
            '''
            result = self._values.get("message")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ErrorInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pcs.CfnQueueProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_id": "clusterId",
        "compute_node_group_configurations": "computeNodeGroupConfigurations",
        "name": "name",
        "tags": "tags",
    },
)
class CfnQueueProps:
    def __init__(
        self,
        *,
        cluster_id: builtins.str,
        compute_node_group_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQueue.ComputeNodeGroupConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnQueue``.

        :param cluster_id: The ID of the cluster of the queue.
        :param compute_node_group_configurations: The list of compute node group configurations associated with the queue. Queues assign jobs to associated compute node groups.
        :param name: The name that identifies the queue.
        :param tags: 1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-queue.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pcs as pcs
            
            cfn_queue_props = pcs.CfnQueueProps(
                cluster_id="clusterId",
            
                # the properties below are optional
                compute_node_group_configurations=[pcs.CfnQueue.ComputeNodeGroupConfigurationProperty(
                    compute_node_group_id="computeNodeGroupId"
                )],
                name="name",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4211e23057aa9883cd55dc7f797abf7f4ad0554424bd2d7d7cfce123004b8557)
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument compute_node_group_configurations", value=compute_node_group_configurations, expected_type=type_hints["compute_node_group_configurations"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_id": cluster_id,
        }
        if compute_node_group_configurations is not None:
            self._values["compute_node_group_configurations"] = compute_node_group_configurations
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def cluster_id(self) -> builtins.str:
        '''The ID of the cluster of the queue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-queue.html#cfn-pcs-queue-clusterid
        '''
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compute_node_group_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnQueue.ComputeNodeGroupConfigurationProperty]]]]:
        '''The list of compute node group configurations associated with the queue.

        Queues assign jobs to associated compute node groups.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-queue.html#cfn-pcs-queue-computenodegroupconfigurations
        '''
        result = self._values.get("compute_node_group_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnQueue.ComputeNodeGroupConfigurationProperty]]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name that identifies the queue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-queue.html#cfn-pcs-queue-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''1 or more tags added to the resource.

        Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-queue.html#cfn-pcs-queue-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQueueProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCluster",
    "CfnClusterProps",
    "CfnComputeNodeGroup",
    "CfnComputeNodeGroupProps",
    "CfnQueue",
    "CfnQueueProps",
]

publication.publish()

def _typecheckingstub__f3eeeaf566612baca2013a4f6d5c60484ee36ebc0edd307d32ef21991c170b65(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    networking: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.NetworkingProperty, typing.Dict[builtins.str, typing.Any]]],
    scheduler: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.SchedulerProperty, typing.Dict[builtins.str, typing.Any]]],
    size: builtins.str,
    name: typing.Optional[builtins.str] = None,
    slurm_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.SlurmConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad41b9587f0f8c306a5663de2a8a6102111fcb7fc8d0e9a53a589055d6beaedc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6de5406d3a652bc9f44810e2ec4b074eabc97b2d888228c1ef6aa15a9be62dd7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55c1ec55aa513ac3501a36d2ae996a234035f2352cdef00bfd71db7d9a57e50c(
    value: typing.Union[_IResolvable_da3f097b, CfnCluster.NetworkingProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d56c39b86f5541062b8866fd13a6f0b7c91e0e765586d45abea04f33cc267998(
    value: typing.Union[_IResolvable_da3f097b, CfnCluster.SchedulerProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__991109fd44c9cf1840f37fe27f8e8d0dd425a7d35c40957d93e9cd3eda6960f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02af9af912d0a7aca1a803881152b3dd95a43c257523e7b9af7a7e20581e9a9e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d87e1a23a15695700ae0058f31b0dfa9d42571eb71c777bac50f89be58cf34fe(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCluster.SlurmConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b386ea2d0b46e98dda569b5edccc0da74b6c12d09181731c93163fcad15cefbf(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1371c6dd1b40632a0c832b301d232842e616e6e2e20240f16e1a18c257dec328(
    *,
    mode: builtins.str,
    default_purge_time_in_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1864f71bcded956851b861671a045d1c7d6402331c1d756c5ac88d21e9fe823c(
    *,
    secret_arn: builtins.str,
    secret_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb46faa4736fd5bede060ea1460c35898193ef49ace1726974a1db8958312929(
    *,
    port: builtins.str,
    private_ip_address: builtins.str,
    type: builtins.str,
    public_ip_address: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9e127e61b0ea75f45a99bba1dcc51875a9ecf36ea91f697889ebe4cb4a8e301(
    *,
    code: typing.Optional[builtins.str] = None,
    message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82c7f3d28e2ed0d063467ea787c6cfc31c28d4c5f26ef1ddf71940887dea9d1f(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe24d9f1c44d1db4489549227b033216d5b6490b74f43ce9c2871e34c4d886ce(
    *,
    type: builtins.str,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6bb8855a5cf237041c92e56f09fd1b1d2d40c49f363bfde280100fbfd6f137f(
    *,
    accounting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.AccountingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    auth_key: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.AuthKeyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scale_down_idle_time_in_seconds: typing.Optional[jsii.Number] = None,
    slurm_custom_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.SlurmCustomSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9d168abcd7adc19d99485fc5db81c30bba87bb255608ac3a4487d1a1028fd33(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1acc8d7c41893eaa3f211b6514471817eb607a349cab301161899ae592f0bdf0(
    *,
    networking: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.NetworkingProperty, typing.Dict[builtins.str, typing.Any]]],
    scheduler: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.SchedulerProperty, typing.Dict[builtins.str, typing.Any]]],
    size: builtins.str,
    name: typing.Optional[builtins.str] = None,
    slurm_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCluster.SlurmConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d74625cecbce8d2048b29b24f3148123fb31c64b330ed51fd45d2b2c42d1c20(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_id: builtins.str,
    custom_launch_template: typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.CustomLaunchTemplateProperty, typing.Dict[builtins.str, typing.Any]]],
    iam_instance_profile_arn: builtins.str,
    instance_configs: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.InstanceConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
    scaling_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.ScalingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    subnet_ids: typing.Sequence[builtins.str],
    ami_id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    purchase_option: typing.Optional[builtins.str] = None,
    slurm_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.SlurmConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    spot_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.SpotOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d833050301c35ecc35d9e2cf88fc748a8f8174e49289d0e2719e757def93e83c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__571860de08b34398201b8498268e8b69422d6e17de99d62fd83b52005d26a6b5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27a33200e9f918661858505e376a9533b97ee45f0f14cd2c479bb9e61b1effc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf4a47490919e9b97683082d58e0ccf8649fd09ec2c5f621c3f8467d84363706(
    value: typing.Union[_IResolvable_da3f097b, CfnComputeNodeGroup.CustomLaunchTemplateProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77021f3115c7344dc9b7365b13a661fa578c34c1997a99dd619003646b7e460a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd2f09e3d9b4cca4eab96f7862d7a047649e41118beecac43ed36e424625aa02(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnComputeNodeGroup.InstanceConfigProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faa6826218f9909223a7fac326f705e3e75a1469e1ec902fe056022fd0a6adf1(
    value: typing.Union[_IResolvable_da3f097b, CfnComputeNodeGroup.ScalingConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6c11a7ef6bbf97645d89e780e4819e5c51eacccbab5c6e46497a3e31accf32e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce6f7916bab348203539e21c424ed76ed039fc805a1e3d704cca40baffc97318(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__621c25d891dcaffc1e388ad783cc5d71aeffd2776b0166c92fce41e6d992d2d7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abf0b129d8eff2b9d98cc25ed6c3cbfebb7f706aa5948692e942f1a485c29a79(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d5c6af28cfa6220ac6fe417a830b4b39cfb3320cd91ef31f4ef71aa5f6d934b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComputeNodeGroup.SlurmConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d7dc8c33129932f54cb9e69a7f2e96a79caaf423f50891bd309efbb2cf8a56(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnComputeNodeGroup.SpotOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f9d940f011938958eb70282b41c84f70c7f86093c1788ec73b310de39dd817d(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5e18d4eaf127cbbf203643daa28b5c0a8105f4a3d48ce6e2c896d6f851d7911(
    *,
    version: builtins.str,
    template_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88387b075e6eeff950872537e019e72d8c0543b07c44cb6fd37f6a6580892efe(
    *,
    code: typing.Optional[builtins.str] = None,
    message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e94b232b9d47b7a1d244e32e3a5dc754392f55d51698be51f1a5de8260de9a0b(
    *,
    instance_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c591f6ad958f29b5e6c332ca3927c8ba0e76bc075461fbecdd513918b5d0bbcd(
    *,
    max_instance_count: jsii.Number,
    min_instance_count: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33800b7dfb5193bcd6bf17beca91a47b148b0349a0de5c1a62f72612ea620096(
    *,
    slurm_custom_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.SlurmCustomSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95bf383e09d59731c7b8cdac63a717d5a44f4c4d44a291a247b4ebda5f004d3c(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adf4042ef194d53ff84c49fd66b8d9e370cc1fb06ce3e5dfca9c196a9102c196(
    *,
    allocation_strategy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b89ff3536491b7ea531bd9d6ca00d7d32a25ce4c02b926c6d677abde115a012d(
    *,
    cluster_id: builtins.str,
    custom_launch_template: typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.CustomLaunchTemplateProperty, typing.Dict[builtins.str, typing.Any]]],
    iam_instance_profile_arn: builtins.str,
    instance_configs: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.InstanceConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
    scaling_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.ScalingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    subnet_ids: typing.Sequence[builtins.str],
    ami_id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    purchase_option: typing.Optional[builtins.str] = None,
    slurm_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.SlurmConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    spot_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnComputeNodeGroup.SpotOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__456edeb02414f262683a35f15a1fae223f92feec590d98024478f680e3249bdd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    cluster_id: builtins.str,
    compute_node_group_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQueue.ComputeNodeGroupConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e91ae15ffe542b6e139af845f0fd58e29e3eb1de94ad2d790169a1ef4226536(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fedb84fc44c9a0375a3b3b2a4753f07a788f5775a01c39a2a16ef0736b04f3b1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dd96bf4d965aac7a933a9b0af29542239baf57d893776c7333dd76d3bff2ca8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fa120ad7f68494c28ccc4186d82ee7a8ff23a8eb4615bb87e7c325c61e1a497(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnQueue.ComputeNodeGroupConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e4f1e9c61fd11b4d3ed4834db791c7064b5408b742dfa6c4a00a242858ad868(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31674031b3f2a49a29efb9edfdb5a54431db3db7616989edd3617113cd6b9afd(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cc981d8d2dee6d007be19b192d33155162e657cf0ddef3c82ac69bf13b0c34a(
    *,
    compute_node_group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e51eb0cec81203da74b9b3c33259135afec8fef04327498ab79338af5a9df34(
    *,
    code: typing.Optional[builtins.str] = None,
    message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4211e23057aa9883cd55dc7f797abf7f4ad0554424bd2d7d7cfce123004b8557(
    *,
    cluster_id: builtins.str,
    compute_node_group_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQueue.ComputeNodeGroupConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
