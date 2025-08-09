r'''
# AWS::LaunchWizard Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_launchwizard as launchwizard
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for LaunchWizard construct libraries](https://constructs.dev/search?q=launchwizard)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::LaunchWizard resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LaunchWizard.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::LaunchWizard](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LaunchWizard.html).

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
class CfnDeployment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_launchwizard.CfnDeployment",
):
    '''Creates a deployment for the given workload.

    Deployments created by this operation are not available in the Launch Wizard console to use the ``Clone deployment`` action on.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html
    :cloudformationResource: AWS::LaunchWizard::Deployment
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_launchwizard as launchwizard
        
        cfn_deployment = launchwizard.CfnDeployment(self, "MyCfnDeployment",
            deployment_pattern_name="deploymentPatternName",
            name="name",
            workload_name="workloadName",
        
            # the properties below are optional
            specifications={
                "specifications_key": "specifications"
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
        deployment_pattern_name: builtins.str,
        name: builtins.str,
        workload_name: builtins.str,
        specifications: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param deployment_pattern_name: The name of the deployment pattern.
        :param name: The name of the deployment.
        :param workload_name: The name of the workload.
        :param specifications: The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see `SAP deployment specifications <https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html>`_ . To retrieve the specifications required to create a deployment for other workloads, use the ```GetWorkloadDeploymentPattern`` <https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html>`_ operation.
        :param tags: Information about the tags attached to a deployment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe77ed4e81ab71d948f0b03ed5f8780bcc2f324a23805bc45e7eef5f9137ded1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeploymentProps(
            deployment_pattern_name=deployment_pattern_name,
            name=name,
            workload_name=workload_name,
            specifications=specifications,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7f3e6794e1a2bf9096acd5b62e08b5fc91decb983d7f694ca0d44580c781e51)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fcfcdfea35cf6cb8ac79e3e1ec3fcf3c8fe447be5f525eff497dbc69d38de67b)
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
        '''The Amazon Resource Name (ARN) of the deployment.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time the deployment was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDeletedAt")
    def attr_deleted_at(self) -> builtins.str:
        '''The time the deployment was deleted.

        :cloudformationAttribute: DeletedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeletedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDeploymentId")
    def attr_deployment_id(self) -> builtins.str:
        '''The ID of the deployment.

        :cloudformationAttribute: DeploymentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeploymentId"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceGroup")
    def attr_resource_group(self) -> builtins.str:
        '''The resource group of the deployment.

        :cloudformationAttribute: ResourceGroup
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceGroup"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the deployment.

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
    @jsii.member(jsii_name="deploymentPatternName")
    def deployment_pattern_name(self) -> builtins.str:
        '''The name of the deployment pattern.'''
        return typing.cast(builtins.str, jsii.get(self, "deploymentPatternName"))

    @deployment_pattern_name.setter
    def deployment_pattern_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04c6045841669ffb1a4272a23741926c40913ef41f644914958b8ffb8b0820be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentPatternName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the deployment.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0094e37b81e5d8f0b6e42001fe8da7cf6d149317e4ef32b73e5cef5a82aee61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="workloadName")
    def workload_name(self) -> builtins.str:
        '''The name of the workload.'''
        return typing.cast(builtins.str, jsii.get(self, "workloadName"))

    @workload_name.setter
    def workload_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ddbc17d8abf4c6daba412028f139c421c42d9da86f2e5b12d5b5a149a84c309)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workloadName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="specifications")
    def specifications(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
        '''The settings specified for the deployment.'''
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], jsii.get(self, "specifications"))

    @specifications.setter
    def specifications(
        self,
        value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6343321573b3c3c84666431fb123811dbd97cb11a86c65d6c6d7d4c669c25d86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "specifications", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Information about the tags attached to a deployment.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__057665c8ffa5f5cdaedcf0301e727d15ee8b0244807853f59c72aadbb741357d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_launchwizard.CfnDeploymentProps",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_pattern_name": "deploymentPatternName",
        "name": "name",
        "workload_name": "workloadName",
        "specifications": "specifications",
        "tags": "tags",
    },
)
class CfnDeploymentProps:
    def __init__(
        self,
        *,
        deployment_pattern_name: builtins.str,
        name: builtins.str,
        workload_name: builtins.str,
        specifications: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeployment``.

        :param deployment_pattern_name: The name of the deployment pattern.
        :param name: The name of the deployment.
        :param workload_name: The name of the workload.
        :param specifications: The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see `SAP deployment specifications <https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html>`_ . To retrieve the specifications required to create a deployment for other workloads, use the ```GetWorkloadDeploymentPattern`` <https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html>`_ operation.
        :param tags: Information about the tags attached to a deployment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_launchwizard as launchwizard
            
            cfn_deployment_props = launchwizard.CfnDeploymentProps(
                deployment_pattern_name="deploymentPatternName",
                name="name",
                workload_name="workloadName",
            
                # the properties below are optional
                specifications={
                    "specifications_key": "specifications"
                },
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6e25238aa51033c6bfd52d31380bf8d8789e604e540fcfff33c0df8b15dcdcf)
            check_type(argname="argument deployment_pattern_name", value=deployment_pattern_name, expected_type=type_hints["deployment_pattern_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument workload_name", value=workload_name, expected_type=type_hints["workload_name"])
            check_type(argname="argument specifications", value=specifications, expected_type=type_hints["specifications"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deployment_pattern_name": deployment_pattern_name,
            "name": name,
            "workload_name": workload_name,
        }
        if specifications is not None:
            self._values["specifications"] = specifications
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def deployment_pattern_name(self) -> builtins.str:
        '''The name of the deployment pattern.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html#cfn-launchwizard-deployment-deploymentpatternname
        '''
        result = self._values.get("deployment_pattern_name")
        assert result is not None, "Required property 'deployment_pattern_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the deployment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html#cfn-launchwizard-deployment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workload_name(self) -> builtins.str:
        '''The name of the workload.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html#cfn-launchwizard-deployment-workloadname
        '''
        result = self._values.get("workload_name")
        assert result is not None, "Required property 'workload_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def specifications(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
        '''The settings specified for the deployment.

        These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see `SAP deployment specifications <https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html>`_ . To retrieve the specifications required to create a deployment for other workloads, use the ```GetWorkloadDeploymentPattern`` <https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html>`_ operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html#cfn-launchwizard-deployment-specifications
        '''
        result = self._values.get("specifications")
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Information about the tags attached to a deployment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-launchwizard-deployment.html#cfn-launchwizard-deployment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeploymentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDeployment",
    "CfnDeploymentProps",
]

publication.publish()

def _typecheckingstub__fe77ed4e81ab71d948f0b03ed5f8780bcc2f324a23805bc45e7eef5f9137ded1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    deployment_pattern_name: builtins.str,
    name: builtins.str,
    workload_name: builtins.str,
    specifications: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7f3e6794e1a2bf9096acd5b62e08b5fc91decb983d7f694ca0d44580c781e51(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcfcdfea35cf6cb8ac79e3e1ec3fcf3c8fe447be5f525eff497dbc69d38de67b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04c6045841669ffb1a4272a23741926c40913ef41f644914958b8ffb8b0820be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0094e37b81e5d8f0b6e42001fe8da7cf6d149317e4ef32b73e5cef5a82aee61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ddbc17d8abf4c6daba412028f139c421c42d9da86f2e5b12d5b5a149a84c309(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6343321573b3c3c84666431fb123811dbd97cb11a86c65d6c6d7d4c669c25d86(
    value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__057665c8ffa5f5cdaedcf0301e727d15ee8b0244807853f59c72aadbb741357d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6e25238aa51033c6bfd52d31380bf8d8789e604e540fcfff33c0df8b15dcdcf(
    *,
    deployment_pattern_name: builtins.str,
    name: builtins.str,
    workload_name: builtins.str,
    specifications: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
