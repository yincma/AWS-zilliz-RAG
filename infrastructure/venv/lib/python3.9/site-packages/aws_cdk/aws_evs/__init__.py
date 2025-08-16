r'''
# AWS::EVS Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_evs as evs
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for EVS construct libraries](https://constructs.dev/search?q=evs)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::EVS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EVS.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::EVS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EVS.html).

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
class CfnEnvironment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_evs.CfnEnvironment",
):
    '''Creates an Amazon EVS environment that runs VCF software, such as SDDC Manager, NSX Manager, and vCenter Server.

    During environment creation, Amazon EVS performs validations on DNS settings, provisions VLAN subnets and hosts, and deploys the supplied version of VCF.

    It can take several hours to create an environment. After the deployment completes, you can configure VCF in the vSphere user interface according to your needs.
    .. epigraph::

       You cannot use the ``dedicatedHostId`` and ``placementGroupId`` parameters together in the same ``CreateEnvironment`` action. This results in a ``ValidationException`` response.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html
    :cloudformationResource: AWS::EVS::Environment
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_evs as evs
        
        cfn_environment = evs.CfnEnvironment(self, "MyCfnEnvironment",
            connectivity_info=evs.CfnEnvironment.ConnectivityInfoProperty(
                private_route_server_peerings=["privateRouteServerPeerings"]
            ),
            license_info=evs.CfnEnvironment.LicenseInfoProperty(
                solution_key="solutionKey",
                vsan_key="vsanKey"
            ),
            service_access_subnet_id="serviceAccessSubnetId",
            site_id="siteId",
            terms_accepted=False,
            vcf_hostnames=evs.CfnEnvironment.VcfHostnamesProperty(
                cloud_builder="cloudBuilder",
                nsx="nsx",
                nsx_edge1="nsxEdge1",
                nsx_edge2="nsxEdge2",
                nsx_manager1="nsxManager1",
                nsx_manager2="nsxManager2",
                nsx_manager3="nsxManager3",
                sddc_manager="sddcManager",
                v_center="vCenter"
            ),
            vcf_version="vcfVersion",
            vpc_id="vpcId",
        
            # the properties below are optional
            environment_name="environmentName",
            hosts=[evs.CfnEnvironment.HostInfoForCreateProperty(
                host_name="hostName",
                instance_type="instanceType",
                key_name="keyName",
        
                # the properties below are optional
                dedicated_host_id="dedicatedHostId",
                placement_group_id="placementGroupId"
            )],
            initial_vlans=evs.CfnEnvironment.InitialVlansProperty(
                edge_vTep=evs.CfnEnvironment.InitialVlanInfoProperty(
                    cidr="cidr"
                ),
                expansion_vlan1=evs.CfnEnvironment.InitialVlanInfoProperty(
                    cidr="cidr"
                ),
                expansion_vlan2=evs.CfnEnvironment.InitialVlanInfoProperty(
                    cidr="cidr"
                ),
                hcx=evs.CfnEnvironment.InitialVlanInfoProperty(
                    cidr="cidr"
                ),
                nsx_up_link=evs.CfnEnvironment.InitialVlanInfoProperty(
                    cidr="cidr"
                ),
                vmk_management=evs.CfnEnvironment.InitialVlanInfoProperty(
                    cidr="cidr"
                ),
                vm_management=evs.CfnEnvironment.InitialVlanInfoProperty(
                    cidr="cidr"
                ),
                v_motion=evs.CfnEnvironment.InitialVlanInfoProperty(
                    cidr="cidr"
                ),
                v_san=evs.CfnEnvironment.InitialVlanInfoProperty(
                    cidr="cidr"
                ),
                v_tep=evs.CfnEnvironment.InitialVlanInfoProperty(
                    cidr="cidr"
                )
            ),
            kms_key_id="kmsKeyId",
            service_access_security_groups=evs.CfnEnvironment.ServiceAccessSecurityGroupsProperty(
                security_groups=["securityGroups"]
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
        connectivity_info: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.ConnectivityInfoProperty", typing.Dict[builtins.str, typing.Any]]],
        license_info: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.LicenseInfoProperty", typing.Dict[builtins.str, typing.Any]]],
        service_access_subnet_id: builtins.str,
        site_id: builtins.str,
        terms_accepted: typing.Union[builtins.bool, _IResolvable_da3f097b],
        vcf_hostnames: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.VcfHostnamesProperty", typing.Dict[builtins.str, typing.Any]]],
        vcf_version: builtins.str,
        vpc_id: builtins.str,
        environment_name: typing.Optional[builtins.str] = None,
        hosts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.HostInfoForCreateProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        initial_vlans: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.InitialVlansProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        service_access_security_groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.ServiceAccessSecurityGroupsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param connectivity_info: The connectivity configuration for the environment. Amazon EVS requires that you specify two route server peer IDs. During environment creation, the route server endpoints peer with the NSX uplink VLAN for connectivity to the NSX overlay network.
        :param license_info: The license information that Amazon EVS requires to create an environment. Amazon EVS requires two license keys: a VCF solution key and a vSAN license key. The VCF solution key must cover a minimum of 256 cores. The vSAN license key must provide at least 110 TiB of vSAN capacity.
        :param service_access_subnet_id: The subnet that is used to establish connectivity between the Amazon EVS control plane and VPC. Amazon EVS uses this subnet to perform validations and create the environment.
        :param site_id: The Broadcom Site ID that is associated with your Amazon EVS environment. Amazon EVS uses the Broadcom Site ID that you provide to meet Broadcom VCF license usage reporting requirements for Amazon EVS.
        :param terms_accepted: Customer confirmation that the customer has purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment. Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance. Amazon EVS does not validate license keys. To validate license keys, visit the Broadcom support portal.
        :param vcf_hostnames: The DNS hostnames to be used by the VCF management appliances in your environment. For environment creation to be successful, each hostname entry must resolve to a domain name that you've registered in your DNS service of choice and configured in the DHCP option set of your VPC. DNS hostnames cannot be changed after environment creation has started.
        :param vcf_version: The VCF version of the environment.
        :param vpc_id: The VPC associated with the environment.
        :param environment_name: The name of the environment.
        :param hosts: Required for environment resource creation.
        :param initial_vlans: .. epigraph:: Amazon EVS is in public preview release and is subject to change. The initial VLAN subnets for the environment. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24. Amazon EVS VLAN subnet CIDR blocks must not overlap with other subnets in the VPC. Required for environment resource creation.
        :param kms_key_id: The AWS KMS key ID that AWS Secrets Manager uses to encrypt secrets that are associated with the environment. These secrets contain the VCF credentials that are needed to install vCenter Server, NSX, and SDDC Manager. By default, Amazon EVS use the AWS Secrets Manager managed key ``aws/secretsmanager`` . You can also specify a customer managed key.
        :param service_access_security_groups: The security groups that allow traffic between the Amazon EVS control plane and your VPC for service access. If a security group is not specified, Amazon EVS uses the default security group in your account for service access.
        :param tags: Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fd5abd7fe71e306d7b1cc2c3ef834eb9af874a0b9fed902c6923bbc07b00b63)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentProps(
            connectivity_info=connectivity_info,
            license_info=license_info,
            service_access_subnet_id=service_access_subnet_id,
            site_id=site_id,
            terms_accepted=terms_accepted,
            vcf_hostnames=vcf_hostnames,
            vcf_version=vcf_version,
            vpc_id=vpc_id,
            environment_name=environment_name,
            hosts=hosts,
            initial_vlans=initial_vlans,
            kms_key_id=kms_key_id,
            service_access_security_groups=service_access_security_groups,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97c8e6ce05b681569d057e41cd3b8f77e1403e7a3da8aebf629d5b36513ac407)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5933d5785ec1ac628e3fd45b05b1c5bc9e333cb80c6d102fb738934f3f5c15da)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrChecks")
    def attr_checks(self) -> _IResolvable_da3f097b:
        '''A check on the environment to identify instance health and VMware VCF licensing issues. For example:.

        ``{ "checks": [ { "type": "KEY_REUSE", "result": "PASSED" }, { "type": "KEY_COVERAGE", "result": "PASSED" }, { "type": "REACHABILITY", "result": "PASSED" }, { "type": "HOST_COUNT", "result": "PASSED" } ] }``

        :cloudformationAttribute: Checks
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrChecks"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time that the environment was created.

        For example: ``1749081600.000`` .

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCredentials")
    def attr_credentials(self) -> _IResolvable_da3f097b:
        '''The VCF credentials that are stored as Amazon EVS managed secrets in AWS Secrets Manager.

        Amazon EVS stores credentials that are needed to install vCenter Server, NSX, and SDDC Manager. For example:

        ``{ [ { "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_vCenterAdmin-MnTMEi" }, { "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_vCenterRoot-87VyCF" }, { "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_NSXRoot-SR3k43" }, { "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_NSXAdmin-L5LUiD" }, { "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_NSXAudit-Q2oW46" }, { "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_SDDCManagerRoot-bFulOq" }, { "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_SDDCManagerVCF-Ec3gES" }, { "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_SDDCManagerAdmin-JMTAAb" } ] }``

        :cloudformationAttribute: Credentials
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrCredentials"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentArn")
    def attr_environment_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) that is associated with the environment.

        For example: ``arn:aws:evs:us-east-1:000000000000:environment/env-1234567890`` .

        :cloudformationAttribute: EnvironmentArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentId")
    def attr_environment_id(self) -> builtins.str:
        '''The unique ID for the environment.

        For example: ``env-1234567890`` .

        :cloudformationAttribute: EnvironmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentState")
    def attr_environment_state(self) -> builtins.str:
        '''The state of an environment.

        For example: ``CREATED`` .

        :cloudformationAttribute: EnvironmentState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentState"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''The date and time that the environment was modified.

        For example: ``1749081600.000`` .

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStateDetails")
    def attr_state_details(self) -> builtins.str:
        '''A detailed description of the ``environmentState`` of an environment.

        For example: ``Environment successfully created`` .

        :cloudformationAttribute: StateDetails
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStateDetails"))

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
    @jsii.member(jsii_name="connectivityInfo")
    def connectivity_info(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ConnectivityInfoProperty"]:
        '''The connectivity configuration for the environment.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ConnectivityInfoProperty"], jsii.get(self, "connectivityInfo"))

    @connectivity_info.setter
    def connectivity_info(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ConnectivityInfoProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf81c76587f8aaaaa50fc18d1384cc1e8ff44f1cd0d764c0355340e0f0839c21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectivityInfo", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="licenseInfo")
    def license_info(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnEnvironment.LicenseInfoProperty"]:
        '''The license information that Amazon EVS requires to create an environment.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEnvironment.LicenseInfoProperty"], jsii.get(self, "licenseInfo"))

    @license_info.setter
    def license_info(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnEnvironment.LicenseInfoProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb6e498dbb5d87feb34dfe26b3466fa6383016c37a4ea21caecc26f60b5ce901)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseInfo", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serviceAccessSubnetId")
    def service_access_subnet_id(self) -> builtins.str:
        '''The subnet that is used to establish connectivity between the Amazon EVS control plane and VPC.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessSubnetId"))

    @service_access_subnet_id.setter
    def service_access_subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f01a5018beaa28fab7b0d068a7a6fe45dbeee0ab15ecdf25462887288ace66cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessSubnetId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="siteId")
    def site_id(self) -> builtins.str:
        '''The Broadcom Site ID that is associated with your Amazon EVS environment.'''
        return typing.cast(builtins.str, jsii.get(self, "siteId"))

    @site_id.setter
    def site_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dc69ff9904f782ce993fe0884901782c11a2214109cfd4cf83020946119b99f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="termsAccepted")
    def terms_accepted(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Customer confirmation that the customer has purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "termsAccepted"))

    @terms_accepted.setter
    def terms_accepted(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93808d5eb28c6837a5047d6d1811bd832bd6250809b9c84a0b609bb88989d45e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "termsAccepted", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vcfHostnames")
    def vcf_hostnames(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnEnvironment.VcfHostnamesProperty"]:
        '''The DNS hostnames to be used by the VCF management appliances in your environment.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEnvironment.VcfHostnamesProperty"], jsii.get(self, "vcfHostnames"))

    @vcf_hostnames.setter
    def vcf_hostnames(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnEnvironment.VcfHostnamesProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98651cf572ae807d1eccd57a45d3ecc81f79063879b068927b5130df235e0b0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vcfHostnames", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vcfVersion")
    def vcf_version(self) -> builtins.str:
        '''The VCF version of the environment.'''
        return typing.cast(builtins.str, jsii.get(self, "vcfVersion"))

    @vcf_version.setter
    def vcf_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77294c8299a96e3407af4323a38741fc1be8bdc06d14be597ecf158dcf011c14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vcfVersion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''The VPC associated with the environment.'''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60ce2bd3161be4b835be56a05bdccfd9639c58eea7d09baeab4884c9a906852e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentName")
    def environment_name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentName"))

    @environment_name.setter
    def environment_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16c81b6578fa573cefa89abf7b2fbcfcf6b8db97f8f8b8e2a8c44d8009af03ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hosts")
    def hosts(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.HostInfoForCreateProperty"]]]]:
        '''Required for environment resource creation.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.HostInfoForCreateProperty"]]]], jsii.get(self, "hosts"))

    @hosts.setter
    def hosts(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.HostInfoForCreateProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18c17b2a1d9ccb9d1cd534e31c376d097f1d59794abd3093f8587758af40bc2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hosts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="initialVlans")
    def initial_vlans(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlansProperty"]]:
        '''.. epigraph::

   Amazon EVS is in public preview release and is subject to change.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlansProperty"]], jsii.get(self, "initialVlans"))

    @initial_vlans.setter
    def initial_vlans(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlansProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15ccc5cc405553a6a5463668babc67ef1dc4049150ba7dddfc07bee61251bcfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialVlans", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The AWS KMS key ID that AWS Secrets Manager uses to encrypt secrets that are associated with the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5b585f35cde6963f33953b58455872fcf621844d2b3fa8f7f85b96542463156)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serviceAccessSecurityGroups")
    def service_access_security_groups(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ServiceAccessSecurityGroupsProperty"]]:
        '''The security groups that allow traffic between the Amazon EVS control plane and your VPC for service access.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ServiceAccessSecurityGroupsProperty"]], jsii.get(self, "serviceAccessSecurityGroups"))

    @service_access_security_groups.setter
    def service_access_security_groups(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.ServiceAccessSecurityGroupsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df95c894cd990c7a318fa3e3397c915f2a30df40bd79003673d83a2d1016e1b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessSecurityGroups", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata that assists with categorization and organization.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c420c54db733392f5b59d4f5a9ded1bfdc781dbe1df45ec2312e16a4c3655efd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evs.CfnEnvironment.CheckProperty",
        jsii_struct_bases=[],
        name_mapping={
            "result": "result",
            "type": "type",
            "impaired_since": "impairedSince",
        },
    )
    class CheckProperty:
        def __init__(
            self,
            *,
            result: builtins.str,
            type: builtins.str,
            impaired_since: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A check on the environment to identify environment health and validate VMware VCF licensing compliance.

            :param result: The check result.
            :param type: The check type. Amazon EVS performs the following checks. - ``KEY_REUSE`` : checks that the VCF license key is not used by another Amazon EVS environment. This check fails if a used license is added to the environment. - ``KEY_COVERAGE`` : checks that your VCF license key allocates sufficient vCPU cores for all deployed hosts. The check fails when any assigned hosts in the EVS environment are not covered by license keys, or when any unassigned hosts cannot be covered by available vCPU cores in keys. - ``REACHABILITY`` : checks that the Amazon EVS control plane has a persistent connection to SDDC Manager. If Amazon EVS cannot reach the environment, this check fails. - ``HOST_COUNT`` : Checks that your environment has a minimum of 4 hosts, which is a requirement for VCF 5.2.1. If this check fails, you will need to add hosts so that your environment meets this minimum requirement. Amazon EVS only supports environments with 4-16 hosts.
            :param impaired_since: The time when environment health began to be impaired.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-check.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evs as evs
                
                check_property = evs.CfnEnvironment.CheckProperty(
                    result="result",
                    type="type",
                
                    # the properties below are optional
                    impaired_since="impairedSince"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fab870dfa28349d9079dfaa9f8d7d27975ec4da1aec540075bef6f41926da444)
                check_type(argname="argument result", value=result, expected_type=type_hints["result"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument impaired_since", value=impaired_since, expected_type=type_hints["impaired_since"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "result": result,
                "type": type,
            }
            if impaired_since is not None:
                self._values["impaired_since"] = impaired_since

        @builtins.property
        def result(self) -> builtins.str:
            '''The check result.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-check.html#cfn-evs-environment-check-result
            '''
            result = self._values.get("result")
            assert result is not None, "Required property 'result' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The check type. Amazon EVS performs the following checks.

            - ``KEY_REUSE`` : checks that the VCF license key is not used by another Amazon EVS environment. This check fails if a used license is added to the environment.
            - ``KEY_COVERAGE`` : checks that your VCF license key allocates sufficient vCPU cores for all deployed hosts. The check fails when any assigned hosts in the EVS environment are not covered by license keys, or when any unassigned hosts cannot be covered by available vCPU cores in keys.
            - ``REACHABILITY`` : checks that the Amazon EVS control plane has a persistent connection to SDDC Manager. If Amazon EVS cannot reach the environment, this check fails.
            - ``HOST_COUNT`` : Checks that your environment has a minimum of 4 hosts, which is a requirement for VCF 5.2.1.

            If this check fails, you will need to add hosts so that your environment meets this minimum requirement. Amazon EVS only supports environments with 4-16 hosts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-check.html#cfn-evs-environment-check-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def impaired_since(self) -> typing.Optional[builtins.str]:
            '''The time when environment health began to be impaired.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-check.html#cfn-evs-environment-check-impairedsince
            '''
            result = self._values.get("impaired_since")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CheckProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evs.CfnEnvironment.ConnectivityInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"private_route_server_peerings": "privateRouteServerPeerings"},
    )
    class ConnectivityInfoProperty:
        def __init__(
            self,
            *,
            private_route_server_peerings: typing.Sequence[builtins.str],
        ) -> None:
            '''The connectivity configuration for the environment.

            Amazon EVS requires that you specify two route server peer IDs. During environment creation, the route server endpoints peer with the NSX uplink VLAN for connectivity to the NSX overlay network.

            :param private_route_server_peerings: The unique IDs for private route server peers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-connectivityinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evs as evs
                
                connectivity_info_property = evs.CfnEnvironment.ConnectivityInfoProperty(
                    private_route_server_peerings=["privateRouteServerPeerings"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2cb3d22ab966fb57bf85a281b91db18f25f2e9b843fa76b2414f9c1ca1285629)
                check_type(argname="argument private_route_server_peerings", value=private_route_server_peerings, expected_type=type_hints["private_route_server_peerings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "private_route_server_peerings": private_route_server_peerings,
            }

        @builtins.property
        def private_route_server_peerings(self) -> typing.List[builtins.str]:
            '''The unique IDs for private route server peers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-connectivityinfo.html#cfn-evs-environment-connectivityinfo-privaterouteserverpeerings
            '''
            result = self._values.get("private_route_server_peerings")
            assert result is not None, "Required property 'private_route_server_peerings' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectivityInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evs.CfnEnvironment.HostInfoForCreateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "host_name": "hostName",
            "instance_type": "instanceType",
            "key_name": "keyName",
            "dedicated_host_id": "dedicatedHostId",
            "placement_group_id": "placementGroupId",
        },
    )
    class HostInfoForCreateProperty:
        def __init__(
            self,
            *,
            host_name: builtins.str,
            instance_type: builtins.str,
            key_name: builtins.str,
            dedicated_host_id: typing.Optional[builtins.str] = None,
            placement_group_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that represents a host.

            .. epigraph::

               You cannot use ``dedicatedHostId`` and ``placementGroupId`` together in the same ``HostInfoForCreate`` object. This results in a ``ValidationException`` response.

            :param host_name: The DNS hostname of the host. DNS hostnames for hosts must be unique across Amazon EVS environments and within VCF.
            :param instance_type: The EC2 instance type that represents the host.
            :param key_name: The name of the SSH key that is used to access the host.
            :param dedicated_host_id: The unique ID of the Amazon EC2 Dedicated Host.
            :param placement_group_id: The unique ID of the placement group where the host is placed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-hostinfoforcreate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evs as evs
                
                host_info_for_create_property = evs.CfnEnvironment.HostInfoForCreateProperty(
                    host_name="hostName",
                    instance_type="instanceType",
                    key_name="keyName",
                
                    # the properties below are optional
                    dedicated_host_id="dedicatedHostId",
                    placement_group_id="placementGroupId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3b92e04ba9146f120cc657bac8562ffe8ba1683c2cda51e8edf7837916efbff4)
                check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
                check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
                check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
                check_type(argname="argument dedicated_host_id", value=dedicated_host_id, expected_type=type_hints["dedicated_host_id"])
                check_type(argname="argument placement_group_id", value=placement_group_id, expected_type=type_hints["placement_group_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "host_name": host_name,
                "instance_type": instance_type,
                "key_name": key_name,
            }
            if dedicated_host_id is not None:
                self._values["dedicated_host_id"] = dedicated_host_id
            if placement_group_id is not None:
                self._values["placement_group_id"] = placement_group_id

        @builtins.property
        def host_name(self) -> builtins.str:
            '''The DNS hostname of the host.

            DNS hostnames for hosts must be unique across Amazon EVS environments and within VCF.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-hostinfoforcreate.html#cfn-evs-environment-hostinfoforcreate-hostname
            '''
            result = self._values.get("host_name")
            assert result is not None, "Required property 'host_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''The EC2 instance type that represents the host.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-hostinfoforcreate.html#cfn-evs-environment-hostinfoforcreate-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_name(self) -> builtins.str:
            '''The name of the SSH key that is used to access the host.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-hostinfoforcreate.html#cfn-evs-environment-hostinfoforcreate-keyname
            '''
            result = self._values.get("key_name")
            assert result is not None, "Required property 'key_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dedicated_host_id(self) -> typing.Optional[builtins.str]:
            '''The unique ID of the Amazon EC2 Dedicated Host.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-hostinfoforcreate.html#cfn-evs-environment-hostinfoforcreate-dedicatedhostid
            '''
            result = self._values.get("dedicated_host_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def placement_group_id(self) -> typing.Optional[builtins.str]:
            '''The unique ID of the placement group where the host is placed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-hostinfoforcreate.html#cfn-evs-environment-hostinfoforcreate-placementgroupid
            '''
            result = self._values.get("placement_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HostInfoForCreateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evs.CfnEnvironment.InitialVlanInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"cidr": "cidr"},
    )
    class InitialVlanInfoProperty:
        def __init__(self, *, cidr: builtins.str) -> None:
            '''An object that represents an initial VLAN subnet for the Amazon EVS environment.

            Amazon EVS creates initial VLAN subnets when you first create the environment. Amazon EVS creates the following 10 VLAN subnets: host management VLAN, vMotion VLAN, vSAN VLAN, VTEP VLAN, Edge VTEP VLAN, Management VM VLAN, HCX uplink VLAN, NSX uplink VLAN, expansion VLAN 1, expansion VLAN 2.
            .. epigraph::

               For each Amazon EVS VLAN subnet, you must specify a non-overlapping CIDR block. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24.

            :param cidr: The CIDR block that you provide to create an Amazon EVS VLAN subnet. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24. Amazon EVS VLAN subnet CIDR blocks must not overlap with other subnets in the VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-initialvlaninfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evs as evs
                
                initial_vlan_info_property = evs.CfnEnvironment.InitialVlanInfoProperty(
                    cidr="cidr"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__620167df6fd78af7ecffe1762889e66c6a24ac02786c4e7ca2d324fab050513a)
                check_type(argname="argument cidr", value=cidr, expected_type=type_hints["cidr"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cidr": cidr,
            }

        @builtins.property
        def cidr(self) -> builtins.str:
            '''The CIDR block that you provide to create an Amazon EVS VLAN subnet.

            Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24. Amazon EVS VLAN subnet CIDR blocks must not overlap with other subnets in the VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-initialvlaninfo.html#cfn-evs-environment-initialvlaninfo-cidr
            '''
            result = self._values.get("cidr")
            assert result is not None, "Required property 'cidr' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InitialVlanInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evs.CfnEnvironment.InitialVlansProperty",
        jsii_struct_bases=[],
        name_mapping={
            "edge_v_tep": "edgeVTep",
            "expansion_vlan1": "expansionVlan1",
            "expansion_vlan2": "expansionVlan2",
            "hcx": "hcx",
            "nsx_up_link": "nsxUpLink",
            "vmk_management": "vmkManagement",
            "vm_management": "vmManagement",
            "v_motion": "vMotion",
            "v_san": "vSan",
            "v_tep": "vTep",
        },
    )
    class InitialVlansProperty:
        def __init__(
            self,
            *,
            edge_v_tep: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.InitialVlanInfoProperty", typing.Dict[builtins.str, typing.Any]]],
            expansion_vlan1: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.InitialVlanInfoProperty", typing.Dict[builtins.str, typing.Any]]],
            expansion_vlan2: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.InitialVlanInfoProperty", typing.Dict[builtins.str, typing.Any]]],
            hcx: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.InitialVlanInfoProperty", typing.Dict[builtins.str, typing.Any]]],
            nsx_up_link: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.InitialVlanInfoProperty", typing.Dict[builtins.str, typing.Any]]],
            vmk_management: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.InitialVlanInfoProperty", typing.Dict[builtins.str, typing.Any]]],
            vm_management: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.InitialVlanInfoProperty", typing.Dict[builtins.str, typing.Any]]],
            v_motion: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.InitialVlanInfoProperty", typing.Dict[builtins.str, typing.Any]]],
            v_san: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.InitialVlanInfoProperty", typing.Dict[builtins.str, typing.Any]]],
            v_tep: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.InitialVlanInfoProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The initial VLAN subnets for the environment.

            Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24. Amazon EVS VLAN subnet CIDR blocks must not overlap with other subnets in the VPC.

            :param edge_v_tep: The edge VTEP VLAN subnet. This VLAN subnet manages traffic flowing between the internal network and external networks, including internet access and other site connections.
            :param expansion_vlan1: An additional VLAN subnet that can be used to extend VCF capabilities once configured. For example, you can configure an expansion VLAN subnet to use NSX Federation for centralized management and synchronization of multiple NSX deployments across different locations.
            :param expansion_vlan2: An additional VLAN subnet that can be used to extend VCF capabilities once configured. For example, you can configure an expansion VLAN subnet to use NSX Federation for centralized management and synchronization of multiple NSX deployments across different locations.
            :param hcx: The HCX VLAN subnet. This VLAN subnet allows the HCX Interconnnect (IX) and HCX Network Extension (NE) to reach their peers and enable HCX Service Mesh creation.
            :param nsx_up_link: The NSX uplink VLAN subnet. This VLAN subnet allows connectivity to the NSX overlay network.
            :param vmk_management: The host VMkernel management VLAN subnet. This VLAN subnet carries traffic for managing ESXi hosts and communicating with VMware vCenter Server.
            :param vm_management: The VM management VLAN subnet. This VLAN subnet carries traffic for vSphere virtual machines.
            :param v_motion: The vMotion VLAN subnet. This VLAN subnet carries traffic for vSphere vMotion.
            :param v_san: The vSAN VLAN subnet. This VLAN subnet carries the communication between ESXi hosts to implement a vSAN shared storage pool.
            :param v_tep: The VTEP VLAN subnet. This VLAN subnet handles internal network traffic between virtual machines within a VCF instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-initialvlans.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evs as evs
                
                initial_vlans_property = evs.CfnEnvironment.InitialVlansProperty(
                    edge_vTep=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    expansion_vlan1=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    expansion_vlan2=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    hcx=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    nsx_up_link=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    vmk_management=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    vm_management=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    v_motion=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    v_san=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    v_tep=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a70b9547ba64740f8b44168dbcdcd80e75a75a1dc2ed733c834ad336fe27001d)
                check_type(argname="argument edge_v_tep", value=edge_v_tep, expected_type=type_hints["edge_v_tep"])
                check_type(argname="argument expansion_vlan1", value=expansion_vlan1, expected_type=type_hints["expansion_vlan1"])
                check_type(argname="argument expansion_vlan2", value=expansion_vlan2, expected_type=type_hints["expansion_vlan2"])
                check_type(argname="argument hcx", value=hcx, expected_type=type_hints["hcx"])
                check_type(argname="argument nsx_up_link", value=nsx_up_link, expected_type=type_hints["nsx_up_link"])
                check_type(argname="argument vmk_management", value=vmk_management, expected_type=type_hints["vmk_management"])
                check_type(argname="argument vm_management", value=vm_management, expected_type=type_hints["vm_management"])
                check_type(argname="argument v_motion", value=v_motion, expected_type=type_hints["v_motion"])
                check_type(argname="argument v_san", value=v_san, expected_type=type_hints["v_san"])
                check_type(argname="argument v_tep", value=v_tep, expected_type=type_hints["v_tep"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "edge_v_tep": edge_v_tep,
                "expansion_vlan1": expansion_vlan1,
                "expansion_vlan2": expansion_vlan2,
                "hcx": hcx,
                "nsx_up_link": nsx_up_link,
                "vmk_management": vmk_management,
                "vm_management": vm_management,
                "v_motion": v_motion,
                "v_san": v_san,
                "v_tep": v_tep,
            }

        @builtins.property
        def edge_v_tep(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"]:
            '''The edge VTEP VLAN subnet.

            This VLAN subnet manages traffic flowing between the internal network and external networks, including internet access and other site connections.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-initialvlans.html#cfn-evs-environment-initialvlans-edgevtep
            '''
            result = self._values.get("edge_v_tep")
            assert result is not None, "Required property 'edge_v_tep' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"], result)

        @builtins.property
        def expansion_vlan1(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"]:
            '''An additional VLAN subnet that can be used to extend VCF capabilities once configured.

            For example, you can configure an expansion VLAN subnet to use NSX Federation for centralized management and synchronization of multiple NSX deployments across different locations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-initialvlans.html#cfn-evs-environment-initialvlans-expansionvlan1
            '''
            result = self._values.get("expansion_vlan1")
            assert result is not None, "Required property 'expansion_vlan1' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"], result)

        @builtins.property
        def expansion_vlan2(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"]:
            '''An additional VLAN subnet that can be used to extend VCF capabilities once configured.

            For example, you can configure an expansion VLAN subnet to use NSX Federation for centralized management and synchronization of multiple NSX deployments across different locations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-initialvlans.html#cfn-evs-environment-initialvlans-expansionvlan2
            '''
            result = self._values.get("expansion_vlan2")
            assert result is not None, "Required property 'expansion_vlan2' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"], result)

        @builtins.property
        def hcx(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"]:
            '''The HCX VLAN subnet.

            This VLAN subnet allows the HCX Interconnnect (IX) and HCX Network Extension (NE) to reach their peers and enable HCX Service Mesh creation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-initialvlans.html#cfn-evs-environment-initialvlans-hcx
            '''
            result = self._values.get("hcx")
            assert result is not None, "Required property 'hcx' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"], result)

        @builtins.property
        def nsx_up_link(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"]:
            '''The NSX uplink VLAN subnet.

            This VLAN subnet allows connectivity to the NSX overlay network.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-initialvlans.html#cfn-evs-environment-initialvlans-nsxuplink
            '''
            result = self._values.get("nsx_up_link")
            assert result is not None, "Required property 'nsx_up_link' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"], result)

        @builtins.property
        def vmk_management(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"]:
            '''The host VMkernel management VLAN subnet.

            This VLAN subnet carries traffic for managing ESXi hosts and communicating with VMware vCenter Server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-initialvlans.html#cfn-evs-environment-initialvlans-vmkmanagement
            '''
            result = self._values.get("vmk_management")
            assert result is not None, "Required property 'vmk_management' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"], result)

        @builtins.property
        def vm_management(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"]:
            '''The VM management VLAN subnet.

            This VLAN subnet carries traffic for vSphere virtual machines.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-initialvlans.html#cfn-evs-environment-initialvlans-vmmanagement
            '''
            result = self._values.get("vm_management")
            assert result is not None, "Required property 'vm_management' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"], result)

        @builtins.property
        def v_motion(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"]:
            '''The vMotion VLAN subnet.

            This VLAN subnet carries traffic for vSphere vMotion.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-initialvlans.html#cfn-evs-environment-initialvlans-vmotion
            '''
            result = self._values.get("v_motion")
            assert result is not None, "Required property 'v_motion' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"], result)

        @builtins.property
        def v_san(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"]:
            '''The vSAN VLAN subnet.

            This VLAN subnet carries the communication between ESXi hosts to implement a vSAN shared storage pool.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-initialvlans.html#cfn-evs-environment-initialvlans-vsan
            '''
            result = self._values.get("v_san")
            assert result is not None, "Required property 'v_san' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"], result)

        @builtins.property
        def v_tep(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"]:
            '''The VTEP VLAN subnet.

            This VLAN subnet handles internal network traffic between virtual machines within a VCF instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-initialvlans.html#cfn-evs-environment-initialvlans-vtep
            '''
            result = self._values.get("v_tep")
            assert result is not None, "Required property 'v_tep' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEnvironment.InitialVlanInfoProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InitialVlansProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evs.CfnEnvironment.LicenseInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"solution_key": "solutionKey", "vsan_key": "vsanKey"},
    )
    class LicenseInfoProperty:
        def __init__(
            self,
            *,
            solution_key: builtins.str,
            vsan_key: builtins.str,
        ) -> None:
            '''The license information that Amazon EVS requires to create an environment.

            Amazon EVS requires two license keys: a VCF solution key and a vSAN license key.

            :param solution_key: The VCF solution key. This license unlocks VMware VCF product features, including vSphere, NSX, SDDC Manager, and vCenter Server. The VCF solution key must cover a minimum of 256 cores.
            :param vsan_key: The VSAN license key. This license unlocks vSAN features. The vSAN license key must provide at least 110 TiB of vSAN capacity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-licenseinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evs as evs
                
                license_info_property = evs.CfnEnvironment.LicenseInfoProperty(
                    solution_key="solutionKey",
                    vsan_key="vsanKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6bb631c066ce7fa55edfeac94e8c8a5337b818eed4292c5b3aced9cad6d1cad3)
                check_type(argname="argument solution_key", value=solution_key, expected_type=type_hints["solution_key"])
                check_type(argname="argument vsan_key", value=vsan_key, expected_type=type_hints["vsan_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "solution_key": solution_key,
                "vsan_key": vsan_key,
            }

        @builtins.property
        def solution_key(self) -> builtins.str:
            '''The VCF solution key.

            This license unlocks VMware VCF product features, including vSphere, NSX, SDDC Manager, and vCenter Server. The VCF solution key must cover a minimum of 256 cores.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-licenseinfo.html#cfn-evs-environment-licenseinfo-solutionkey
            '''
            result = self._values.get("solution_key")
            assert result is not None, "Required property 'solution_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vsan_key(self) -> builtins.str:
            '''The VSAN license key.

            This license unlocks vSAN features. The vSAN license key must provide at least 110 TiB of vSAN capacity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-licenseinfo.html#cfn-evs-environment-licenseinfo-vsankey
            '''
            result = self._values.get("vsan_key")
            assert result is not None, "Required property 'vsan_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LicenseInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evs.CfnEnvironment.SecretProperty",
        jsii_struct_bases=[],
        name_mapping={"secret_arn": "secretArn"},
    )
    class SecretProperty:
        def __init__(self, *, secret_arn: typing.Optional[builtins.str] = None) -> None:
            '''A managed secret that contains the credentials for installing vCenter Server, NSX, and SDDC Manager.

            During environment creation, the Amazon EVS control plane uses AWS Secrets Manager to create, encrypt, validate, and store secrets. If you choose to delete your environment, Amazon EVS also deletes the secrets that are associated with your environment. Amazon EVS does not provide managed rotation of secrets. We recommend that you rotate secrets regularly to ensure that secrets are not long-lived.

            :param secret_arn: The Amazon Resource Name (ARN) of the secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-secret.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evs as evs
                
                secret_property = evs.CfnEnvironment.SecretProperty(
                    secret_arn="secretArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__33967b6ef3400afc32ce0af5c9e428f01559afa67ae04decfe8e700e94b87a50)
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-secret.html#cfn-evs-environment-secret-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecretProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evs.CfnEnvironment.ServiceAccessSecurityGroupsProperty",
        jsii_struct_bases=[],
        name_mapping={"security_groups": "securityGroups"},
    )
    class ServiceAccessSecurityGroupsProperty:
        def __init__(
            self,
            *,
            security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The security groups that allow traffic between the Amazon EVS control plane and your VPC for Amazon EVS service access.

            If a security group is not specified, Amazon EVS uses the default security group in your account for service access.

            :param security_groups: The security groups that allow service access.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-serviceaccesssecuritygroups.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evs as evs
                
                service_access_security_groups_property = evs.CfnEnvironment.ServiceAccessSecurityGroupsProperty(
                    security_groups=["securityGroups"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__35c3da17a2fce469ae79744d181a61b0265e29008e2b55604fbe06fb54b01d0d)
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_groups is not None:
                self._values["security_groups"] = security_groups

        @builtins.property
        def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The security groups that allow service access.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-serviceaccesssecuritygroups.html#cfn-evs-environment-serviceaccesssecuritygroups-securitygroups
            '''
            result = self._values.get("security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceAccessSecurityGroupsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evs.CfnEnvironment.VcfHostnamesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_builder": "cloudBuilder",
            "nsx": "nsx",
            "nsx_edge1": "nsxEdge1",
            "nsx_edge2": "nsxEdge2",
            "nsx_manager1": "nsxManager1",
            "nsx_manager2": "nsxManager2",
            "nsx_manager3": "nsxManager3",
            "sddc_manager": "sddcManager",
            "v_center": "vCenter",
        },
    )
    class VcfHostnamesProperty:
        def __init__(
            self,
            *,
            cloud_builder: builtins.str,
            nsx: builtins.str,
            nsx_edge1: builtins.str,
            nsx_edge2: builtins.str,
            nsx_manager1: builtins.str,
            nsx_manager2: builtins.str,
            nsx_manager3: builtins.str,
            sddc_manager: builtins.str,
            v_center: builtins.str,
        ) -> None:
            '''The DNS hostnames that Amazon EVS uses to install VMware vCenter Server, NSX, SDDC Manager, and Cloud Builder.

            Each hostname must be unique, and resolve to a domain name that you've registered in your DNS service of choice. Hostnames cannot be changed.

            VMware VCF requires the deployment of two NSX Edge nodes, and three NSX Manager virtual machines.

            :param cloud_builder: The hostname for VMware Cloud Builder.
            :param nsx: The VMware NSX hostname.
            :param nsx_edge1: The hostname for the first NSX Edge node.
            :param nsx_edge2: The hostname for the second NSX Edge node.
            :param nsx_manager1: The hostname for the first VMware NSX Manager virtual machine (VM).
            :param nsx_manager2: The hostname for the second VMware NSX Manager virtual machine (VM).
            :param nsx_manager3: The hostname for the third VMware NSX Manager virtual machine (VM).
            :param sddc_manager: The hostname for SDDC Manager.
            :param v_center: The VMware vCenter hostname.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-vcfhostnames.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evs as evs
                
                vcf_hostnames_property = evs.CfnEnvironment.VcfHostnamesProperty(
                    cloud_builder="cloudBuilder",
                    nsx="nsx",
                    nsx_edge1="nsxEdge1",
                    nsx_edge2="nsxEdge2",
                    nsx_manager1="nsxManager1",
                    nsx_manager2="nsxManager2",
                    nsx_manager3="nsxManager3",
                    sddc_manager="sddcManager",
                    v_center="vCenter"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1ba5fd1a9e5e7dc84687933a99fd65aef3da8840e139b66bfd40a66914e4a834)
                check_type(argname="argument cloud_builder", value=cloud_builder, expected_type=type_hints["cloud_builder"])
                check_type(argname="argument nsx", value=nsx, expected_type=type_hints["nsx"])
                check_type(argname="argument nsx_edge1", value=nsx_edge1, expected_type=type_hints["nsx_edge1"])
                check_type(argname="argument nsx_edge2", value=nsx_edge2, expected_type=type_hints["nsx_edge2"])
                check_type(argname="argument nsx_manager1", value=nsx_manager1, expected_type=type_hints["nsx_manager1"])
                check_type(argname="argument nsx_manager2", value=nsx_manager2, expected_type=type_hints["nsx_manager2"])
                check_type(argname="argument nsx_manager3", value=nsx_manager3, expected_type=type_hints["nsx_manager3"])
                check_type(argname="argument sddc_manager", value=sddc_manager, expected_type=type_hints["sddc_manager"])
                check_type(argname="argument v_center", value=v_center, expected_type=type_hints["v_center"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cloud_builder": cloud_builder,
                "nsx": nsx,
                "nsx_edge1": nsx_edge1,
                "nsx_edge2": nsx_edge2,
                "nsx_manager1": nsx_manager1,
                "nsx_manager2": nsx_manager2,
                "nsx_manager3": nsx_manager3,
                "sddc_manager": sddc_manager,
                "v_center": v_center,
            }

        @builtins.property
        def cloud_builder(self) -> builtins.str:
            '''The hostname for VMware Cloud Builder.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-vcfhostnames.html#cfn-evs-environment-vcfhostnames-cloudbuilder
            '''
            result = self._values.get("cloud_builder")
            assert result is not None, "Required property 'cloud_builder' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nsx(self) -> builtins.str:
            '''The VMware NSX hostname.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-vcfhostnames.html#cfn-evs-environment-vcfhostnames-nsx
            '''
            result = self._values.get("nsx")
            assert result is not None, "Required property 'nsx' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nsx_edge1(self) -> builtins.str:
            '''The hostname for the first NSX Edge node.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-vcfhostnames.html#cfn-evs-environment-vcfhostnames-nsxedge1
            '''
            result = self._values.get("nsx_edge1")
            assert result is not None, "Required property 'nsx_edge1' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nsx_edge2(self) -> builtins.str:
            '''The hostname for the second NSX Edge node.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-vcfhostnames.html#cfn-evs-environment-vcfhostnames-nsxedge2
            '''
            result = self._values.get("nsx_edge2")
            assert result is not None, "Required property 'nsx_edge2' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nsx_manager1(self) -> builtins.str:
            '''The hostname for the first VMware NSX Manager virtual machine (VM).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-vcfhostnames.html#cfn-evs-environment-vcfhostnames-nsxmanager1
            '''
            result = self._values.get("nsx_manager1")
            assert result is not None, "Required property 'nsx_manager1' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nsx_manager2(self) -> builtins.str:
            '''The hostname for the second VMware NSX Manager virtual machine (VM).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-vcfhostnames.html#cfn-evs-environment-vcfhostnames-nsxmanager2
            '''
            result = self._values.get("nsx_manager2")
            assert result is not None, "Required property 'nsx_manager2' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nsx_manager3(self) -> builtins.str:
            '''The hostname for the third VMware NSX Manager virtual machine (VM).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-vcfhostnames.html#cfn-evs-environment-vcfhostnames-nsxmanager3
            '''
            result = self._values.get("nsx_manager3")
            assert result is not None, "Required property 'nsx_manager3' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sddc_manager(self) -> builtins.str:
            '''The hostname for SDDC Manager.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-vcfhostnames.html#cfn-evs-environment-vcfhostnames-sddcmanager
            '''
            result = self._values.get("sddc_manager")
            assert result is not None, "Required property 'sddc_manager' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def v_center(self) -> builtins.str:
            '''The VMware vCenter hostname.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evs-environment-vcfhostnames.html#cfn-evs-environment-vcfhostnames-vcenter
            '''
            result = self._values.get("v_center")
            assert result is not None, "Required property 'v_center' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VcfHostnamesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_evs.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "connectivity_info": "connectivityInfo",
        "license_info": "licenseInfo",
        "service_access_subnet_id": "serviceAccessSubnetId",
        "site_id": "siteId",
        "terms_accepted": "termsAccepted",
        "vcf_hostnames": "vcfHostnames",
        "vcf_version": "vcfVersion",
        "vpc_id": "vpcId",
        "environment_name": "environmentName",
        "hosts": "hosts",
        "initial_vlans": "initialVlans",
        "kms_key_id": "kmsKeyId",
        "service_access_security_groups": "serviceAccessSecurityGroups",
        "tags": "tags",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        connectivity_info: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.ConnectivityInfoProperty, typing.Dict[builtins.str, typing.Any]]],
        license_info: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.LicenseInfoProperty, typing.Dict[builtins.str, typing.Any]]],
        service_access_subnet_id: builtins.str,
        site_id: builtins.str,
        terms_accepted: typing.Union[builtins.bool, _IResolvable_da3f097b],
        vcf_hostnames: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.VcfHostnamesProperty, typing.Dict[builtins.str, typing.Any]]],
        vcf_version: builtins.str,
        vpc_id: builtins.str,
        environment_name: typing.Optional[builtins.str] = None,
        hosts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.HostInfoForCreateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        initial_vlans: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.InitialVlansProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        service_access_security_groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.ServiceAccessSecurityGroupsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironment``.

        :param connectivity_info: The connectivity configuration for the environment. Amazon EVS requires that you specify two route server peer IDs. During environment creation, the route server endpoints peer with the NSX uplink VLAN for connectivity to the NSX overlay network.
        :param license_info: The license information that Amazon EVS requires to create an environment. Amazon EVS requires two license keys: a VCF solution key and a vSAN license key. The VCF solution key must cover a minimum of 256 cores. The vSAN license key must provide at least 110 TiB of vSAN capacity.
        :param service_access_subnet_id: The subnet that is used to establish connectivity between the Amazon EVS control plane and VPC. Amazon EVS uses this subnet to perform validations and create the environment.
        :param site_id: The Broadcom Site ID that is associated with your Amazon EVS environment. Amazon EVS uses the Broadcom Site ID that you provide to meet Broadcom VCF license usage reporting requirements for Amazon EVS.
        :param terms_accepted: Customer confirmation that the customer has purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment. Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance. Amazon EVS does not validate license keys. To validate license keys, visit the Broadcom support portal.
        :param vcf_hostnames: The DNS hostnames to be used by the VCF management appliances in your environment. For environment creation to be successful, each hostname entry must resolve to a domain name that you've registered in your DNS service of choice and configured in the DHCP option set of your VPC. DNS hostnames cannot be changed after environment creation has started.
        :param vcf_version: The VCF version of the environment.
        :param vpc_id: The VPC associated with the environment.
        :param environment_name: The name of the environment.
        :param hosts: Required for environment resource creation.
        :param initial_vlans: .. epigraph:: Amazon EVS is in public preview release and is subject to change. The initial VLAN subnets for the environment. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24. Amazon EVS VLAN subnet CIDR blocks must not overlap with other subnets in the VPC. Required for environment resource creation.
        :param kms_key_id: The AWS KMS key ID that AWS Secrets Manager uses to encrypt secrets that are associated with the environment. These secrets contain the VCF credentials that are needed to install vCenter Server, NSX, and SDDC Manager. By default, Amazon EVS use the AWS Secrets Manager managed key ``aws/secretsmanager`` . You can also specify a customer managed key.
        :param service_access_security_groups: The security groups that allow traffic between the Amazon EVS control plane and your VPC for service access. If a security group is not specified, Amazon EVS uses the default security group in your account for service access.
        :param tags: Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_evs as evs
            
            cfn_environment_props = evs.CfnEnvironmentProps(
                connectivity_info=evs.CfnEnvironment.ConnectivityInfoProperty(
                    private_route_server_peerings=["privateRouteServerPeerings"]
                ),
                license_info=evs.CfnEnvironment.LicenseInfoProperty(
                    solution_key="solutionKey",
                    vsan_key="vsanKey"
                ),
                service_access_subnet_id="serviceAccessSubnetId",
                site_id="siteId",
                terms_accepted=False,
                vcf_hostnames=evs.CfnEnvironment.VcfHostnamesProperty(
                    cloud_builder="cloudBuilder",
                    nsx="nsx",
                    nsx_edge1="nsxEdge1",
                    nsx_edge2="nsxEdge2",
                    nsx_manager1="nsxManager1",
                    nsx_manager2="nsxManager2",
                    nsx_manager3="nsxManager3",
                    sddc_manager="sddcManager",
                    v_center="vCenter"
                ),
                vcf_version="vcfVersion",
                vpc_id="vpcId",
            
                # the properties below are optional
                environment_name="environmentName",
                hosts=[evs.CfnEnvironment.HostInfoForCreateProperty(
                    host_name="hostName",
                    instance_type="instanceType",
                    key_name="keyName",
            
                    # the properties below are optional
                    dedicated_host_id="dedicatedHostId",
                    placement_group_id="placementGroupId"
                )],
                initial_vlans=evs.CfnEnvironment.InitialVlansProperty(
                    edge_vTep=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    expansion_vlan1=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    expansion_vlan2=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    hcx=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    nsx_up_link=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    vmk_management=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    vm_management=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    v_motion=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    v_san=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    ),
                    v_tep=evs.CfnEnvironment.InitialVlanInfoProperty(
                        cidr="cidr"
                    )
                ),
                kms_key_id="kmsKeyId",
                service_access_security_groups=evs.CfnEnvironment.ServiceAccessSecurityGroupsProperty(
                    security_groups=["securityGroups"]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13a1fb4e59a516dd42610d3a93252ed2060e4948f1e22e6ac66a5c31e9d3fb06)
            check_type(argname="argument connectivity_info", value=connectivity_info, expected_type=type_hints["connectivity_info"])
            check_type(argname="argument license_info", value=license_info, expected_type=type_hints["license_info"])
            check_type(argname="argument service_access_subnet_id", value=service_access_subnet_id, expected_type=type_hints["service_access_subnet_id"])
            check_type(argname="argument site_id", value=site_id, expected_type=type_hints["site_id"])
            check_type(argname="argument terms_accepted", value=terms_accepted, expected_type=type_hints["terms_accepted"])
            check_type(argname="argument vcf_hostnames", value=vcf_hostnames, expected_type=type_hints["vcf_hostnames"])
            check_type(argname="argument vcf_version", value=vcf_version, expected_type=type_hints["vcf_version"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument environment_name", value=environment_name, expected_type=type_hints["environment_name"])
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument initial_vlans", value=initial_vlans, expected_type=type_hints["initial_vlans"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument service_access_security_groups", value=service_access_security_groups, expected_type=type_hints["service_access_security_groups"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connectivity_info": connectivity_info,
            "license_info": license_info,
            "service_access_subnet_id": service_access_subnet_id,
            "site_id": site_id,
            "terms_accepted": terms_accepted,
            "vcf_hostnames": vcf_hostnames,
            "vcf_version": vcf_version,
            "vpc_id": vpc_id,
        }
        if environment_name is not None:
            self._values["environment_name"] = environment_name
        if hosts is not None:
            self._values["hosts"] = hosts
        if initial_vlans is not None:
            self._values["initial_vlans"] = initial_vlans
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if service_access_security_groups is not None:
            self._values["service_access_security_groups"] = service_access_security_groups
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def connectivity_info(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnEnvironment.ConnectivityInfoProperty]:
        '''The connectivity configuration for the environment.

        Amazon EVS requires that you specify two route server peer IDs. During environment creation, the route server endpoints peer with the NSX uplink VLAN for connectivity to the NSX overlay network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html#cfn-evs-environment-connectivityinfo
        '''
        result = self._values.get("connectivity_info")
        assert result is not None, "Required property 'connectivity_info' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnEnvironment.ConnectivityInfoProperty], result)

    @builtins.property
    def license_info(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnEnvironment.LicenseInfoProperty]:
        '''The license information that Amazon EVS requires to create an environment.

        Amazon EVS requires two license keys: a VCF solution key and a vSAN license key. The VCF solution key must cover a minimum of 256 cores. The vSAN license key must provide at least 110 TiB of vSAN capacity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html#cfn-evs-environment-licenseinfo
        '''
        result = self._values.get("license_info")
        assert result is not None, "Required property 'license_info' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnEnvironment.LicenseInfoProperty], result)

    @builtins.property
    def service_access_subnet_id(self) -> builtins.str:
        '''The subnet that is used to establish connectivity between the Amazon EVS control plane and VPC.

        Amazon EVS uses this subnet to perform validations and create the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html#cfn-evs-environment-serviceaccesssubnetid
        '''
        result = self._values.get("service_access_subnet_id")
        assert result is not None, "Required property 'service_access_subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def site_id(self) -> builtins.str:
        '''The Broadcom Site ID that is associated with your Amazon EVS environment.

        Amazon EVS uses the Broadcom Site ID that you provide to meet Broadcom VCF license usage reporting requirements for Amazon EVS.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html#cfn-evs-environment-siteid
        '''
        result = self._values.get("site_id")
        assert result is not None, "Required property 'site_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def terms_accepted(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Customer confirmation that the customer has purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment.

        Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance. Amazon EVS does not validate license keys. To validate license keys, visit the Broadcom support portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html#cfn-evs-environment-termsaccepted
        '''
        result = self._values.get("terms_accepted")
        assert result is not None, "Required property 'terms_accepted' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def vcf_hostnames(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnEnvironment.VcfHostnamesProperty]:
        '''The DNS hostnames to be used by the VCF management appliances in your environment.

        For environment creation to be successful, each hostname entry must resolve to a domain name that you've registered in your DNS service of choice and configured in the DHCP option set of your VPC. DNS hostnames cannot be changed after environment creation has started.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html#cfn-evs-environment-vcfhostnames
        '''
        result = self._values.get("vcf_hostnames")
        assert result is not None, "Required property 'vcf_hostnames' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnEnvironment.VcfHostnamesProperty], result)

    @builtins.property
    def vcf_version(self) -> builtins.str:
        '''The VCF version of the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html#cfn-evs-environment-vcfversion
        '''
        result = self._values.get("vcf_version")
        assert result is not None, "Required property 'vcf_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The VPC associated with the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html#cfn-evs-environment-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html#cfn-evs-environment-environmentname
        '''
        result = self._values.get("environment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hosts(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.HostInfoForCreateProperty]]]]:
        '''Required for environment resource creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html#cfn-evs-environment-hosts
        '''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.HostInfoForCreateProperty]]]], result)

    @builtins.property
    def initial_vlans(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.InitialVlansProperty]]:
        '''.. epigraph::

   Amazon EVS is in public preview release and is subject to change.

        The initial VLAN subnets for the environment. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24. Amazon EVS VLAN subnet CIDR blocks must not overlap with other subnets in the VPC.

        Required for environment resource creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html#cfn-evs-environment-initialvlans
        '''
        result = self._values.get("initial_vlans")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.InitialVlansProperty]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The AWS KMS key ID that AWS Secrets Manager uses to encrypt secrets that are associated with the environment.

        These secrets contain the VCF credentials that are needed to install vCenter Server, NSX, and SDDC Manager.

        By default, Amazon EVS use the AWS Secrets Manager managed key ``aws/secretsmanager`` . You can also specify a customer managed key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html#cfn-evs-environment-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_access_security_groups(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.ServiceAccessSecurityGroupsProperty]]:
        '''The security groups that allow traffic between the Amazon EVS control plane and your VPC for service access.

        If a security group is not specified, Amazon EVS uses the default security group in your account for service access.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html#cfn-evs-environment-serviceaccesssecuritygroups
        '''
        result = self._values.get("service_access_security_groups")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.ServiceAccessSecurityGroupsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata that assists with categorization and organization.

        Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evs-environment.html#cfn-evs-environment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEnvironment",
    "CfnEnvironmentProps",
]

publication.publish()

def _typecheckingstub__0fd5abd7fe71e306d7b1cc2c3ef834eb9af874a0b9fed902c6923bbc07b00b63(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connectivity_info: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.ConnectivityInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    license_info: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.LicenseInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    service_access_subnet_id: builtins.str,
    site_id: builtins.str,
    terms_accepted: typing.Union[builtins.bool, _IResolvable_da3f097b],
    vcf_hostnames: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.VcfHostnamesProperty, typing.Dict[builtins.str, typing.Any]]],
    vcf_version: builtins.str,
    vpc_id: builtins.str,
    environment_name: typing.Optional[builtins.str] = None,
    hosts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.HostInfoForCreateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    initial_vlans: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.InitialVlansProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    service_access_security_groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.ServiceAccessSecurityGroupsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97c8e6ce05b681569d057e41cd3b8f77e1403e7a3da8aebf629d5b36513ac407(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5933d5785ec1ac628e3fd45b05b1c5bc9e333cb80c6d102fb738934f3f5c15da(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf81c76587f8aaaaa50fc18d1384cc1e8ff44f1cd0d764c0355340e0f0839c21(
    value: typing.Union[_IResolvable_da3f097b, CfnEnvironment.ConnectivityInfoProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb6e498dbb5d87feb34dfe26b3466fa6383016c37a4ea21caecc26f60b5ce901(
    value: typing.Union[_IResolvable_da3f097b, CfnEnvironment.LicenseInfoProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f01a5018beaa28fab7b0d068a7a6fe45dbeee0ab15ecdf25462887288ace66cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dc69ff9904f782ce993fe0884901782c11a2214109cfd4cf83020946119b99f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93808d5eb28c6837a5047d6d1811bd832bd6250809b9c84a0b609bb88989d45e(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98651cf572ae807d1eccd57a45d3ecc81f79063879b068927b5130df235e0b0c(
    value: typing.Union[_IResolvable_da3f097b, CfnEnvironment.VcfHostnamesProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77294c8299a96e3407af4323a38741fc1be8bdc06d14be597ecf158dcf011c14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60ce2bd3161be4b835be56a05bdccfd9639c58eea7d09baeab4884c9a906852e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16c81b6578fa573cefa89abf7b2fbcfcf6b8db97f8f8b8e2a8c44d8009af03ed(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18c17b2a1d9ccb9d1cd534e31c376d097f1d59794abd3093f8587758af40bc2e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnvironment.HostInfoForCreateProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15ccc5cc405553a6a5463668babc67ef1dc4049150ba7dddfc07bee61251bcfe(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.InitialVlansProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5b585f35cde6963f33953b58455872fcf621844d2b3fa8f7f85b96542463156(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df95c894cd990c7a318fa3e3397c915f2a30df40bd79003673d83a2d1016e1b9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.ServiceAccessSecurityGroupsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c420c54db733392f5b59d4f5a9ded1bfdc781dbe1df45ec2312e16a4c3655efd(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fab870dfa28349d9079dfaa9f8d7d27975ec4da1aec540075bef6f41926da444(
    *,
    result: builtins.str,
    type: builtins.str,
    impaired_since: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cb3d22ab966fb57bf85a281b91db18f25f2e9b843fa76b2414f9c1ca1285629(
    *,
    private_route_server_peerings: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b92e04ba9146f120cc657bac8562ffe8ba1683c2cda51e8edf7837916efbff4(
    *,
    host_name: builtins.str,
    instance_type: builtins.str,
    key_name: builtins.str,
    dedicated_host_id: typing.Optional[builtins.str] = None,
    placement_group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__620167df6fd78af7ecffe1762889e66c6a24ac02786c4e7ca2d324fab050513a(
    *,
    cidr: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a70b9547ba64740f8b44168dbcdcd80e75a75a1dc2ed733c834ad336fe27001d(
    *,
    edge_v_tep: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.InitialVlanInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    expansion_vlan1: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.InitialVlanInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    expansion_vlan2: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.InitialVlanInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    hcx: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.InitialVlanInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    nsx_up_link: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.InitialVlanInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    vmk_management: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.InitialVlanInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    vm_management: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.InitialVlanInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    v_motion: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.InitialVlanInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    v_san: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.InitialVlanInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    v_tep: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.InitialVlanInfoProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bb631c066ce7fa55edfeac94e8c8a5337b818eed4292c5b3aced9cad6d1cad3(
    *,
    solution_key: builtins.str,
    vsan_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33967b6ef3400afc32ce0af5c9e428f01559afa67ae04decfe8e700e94b87a50(
    *,
    secret_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35c3da17a2fce469ae79744d181a61b0265e29008e2b55604fbe06fb54b01d0d(
    *,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ba5fd1a9e5e7dc84687933a99fd65aef3da8840e139b66bfd40a66914e4a834(
    *,
    cloud_builder: builtins.str,
    nsx: builtins.str,
    nsx_edge1: builtins.str,
    nsx_edge2: builtins.str,
    nsx_manager1: builtins.str,
    nsx_manager2: builtins.str,
    nsx_manager3: builtins.str,
    sddc_manager: builtins.str,
    v_center: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13a1fb4e59a516dd42610d3a93252ed2060e4948f1e22e6ac66a5c31e9d3fb06(
    *,
    connectivity_info: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.ConnectivityInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    license_info: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.LicenseInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    service_access_subnet_id: builtins.str,
    site_id: builtins.str,
    terms_accepted: typing.Union[builtins.bool, _IResolvable_da3f097b],
    vcf_hostnames: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.VcfHostnamesProperty, typing.Dict[builtins.str, typing.Any]]],
    vcf_version: builtins.str,
    vpc_id: builtins.str,
    environment_name: typing.Optional[builtins.str] = None,
    hosts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.HostInfoForCreateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    initial_vlans: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.InitialVlansProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    service_access_security_groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.ServiceAccessSecurityGroupsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
