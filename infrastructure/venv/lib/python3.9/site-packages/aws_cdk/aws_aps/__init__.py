r'''
# AWS::APS Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_aps as aps
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for APS construct libraries](https://constructs.dev/search?q=aps)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::APS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_APS.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::APS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_APS.html).

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
class CfnRuleGroupsNamespace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_aps.CfnRuleGroupsNamespace",
):
    '''The definition of a rule groups namespace in an Amazon Managed Service for Prometheus workspace.

    A rule groups namespace is associated with exactly one rules file. A workspace can have multiple rule groups namespaces. For more information about rules files, see `Creating a rules file <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-rulesfile.html>`_ , in the *Amazon Managed Service for Prometheus User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html
    :cloudformationResource: AWS::APS::RuleGroupsNamespace
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_aps as aps
        
        cfn_rule_groups_namespace = aps.CfnRuleGroupsNamespace(self, "MyCfnRuleGroupsNamespace",
            data="data",
            name="name",
            workspace="workspace",
        
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
        data: builtins.str,
        name: builtins.str,
        workspace: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data: The rules file used in the namespace. For more details about the rules file, see `Creating a rules file <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-rulesfile.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .
        :param name: The name of the rule groups namespace.
        :param workspace: The ID of the workspace to add the rule groups namespace.
        :param tags: The list of tag keys and values that are associated with the rule groups namespace.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02d681a4d4a1e9d9052c98f45bf8b21257e825ee8185b30ea4b6f887fc7416b1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRuleGroupsNamespaceProps(
            data=data, name=name, workspace=workspace, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f066376b2a4b15a103f9a01bca66f252615381ddc55bd5508262712fd03eec2d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__501ad912878791d9cc1a45e52a9642fb0747f4ddf4482708286f9bfde7e036de)
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
        '''The ARN of the rule groups namespace.

        For example, ``arn:aws:aps:<region>:123456789012:rulegroupsnamespace/ws-example1-1234-abcd-5678-ef90abcd1234/rulesfile1`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="data")
    def data(self) -> builtins.str:
        '''The rules file used in the namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "data"))

    @data.setter
    def data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__327e955bc86deb15923357f0f050e077304b8dbbb2c9baba9d84a13c5d7b695d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the rule groups namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f3851e1fa5b758763dff1a85515e41a8c57e1b4da81b2e677f003890944957f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="workspace")
    def workspace(self) -> builtins.str:
        '''The ID of the workspace to add the rule groups namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "workspace"))

    @workspace.setter
    def workspace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f899db17dfa1e1837e2b90cca5f83f23f67ca015116201811ad84d044e9ebe95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspace", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of tag keys and values that are associated with the rule groups namespace.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9af819e60d52c87c9369e4854d0dfc8d4917db97219839fbc11cf2bdad55659)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_aps.CfnRuleGroupsNamespaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "data": "data",
        "name": "name",
        "workspace": "workspace",
        "tags": "tags",
    },
)
class CfnRuleGroupsNamespaceProps:
    def __init__(
        self,
        *,
        data: builtins.str,
        name: builtins.str,
        workspace: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRuleGroupsNamespace``.

        :param data: The rules file used in the namespace. For more details about the rules file, see `Creating a rules file <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-rulesfile.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .
        :param name: The name of the rule groups namespace.
        :param workspace: The ID of the workspace to add the rule groups namespace.
        :param tags: The list of tag keys and values that are associated with the rule groups namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_aps as aps
            
            cfn_rule_groups_namespace_props = aps.CfnRuleGroupsNamespaceProps(
                data="data",
                name="name",
                workspace="workspace",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ba9f13df78597d09b62adc5501ac56c5fedca3215c115e02cb7e3be9e440366)
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument workspace", value=workspace, expected_type=type_hints["workspace"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data": data,
            "name": name,
            "workspace": workspace,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data(self) -> builtins.str:
        '''The rules file used in the namespace.

        For more details about the rules file, see `Creating a rules file <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-rulesfile.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-data
        '''
        result = self._values.get("data")
        assert result is not None, "Required property 'data' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the rule groups namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace(self) -> builtins.str:
        '''The ID of the workspace to add the rule groups namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-workspace
        '''
        result = self._values.get("workspace")
        assert result is not None, "Required property 'workspace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of tag keys and values that are associated with the rule groups namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuleGroupsNamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnScraper(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_aps.CfnScraper",
):
    '''A scraper is a fully-managed agentless collector that discovers and pulls metrics automatically.

    A scraper pulls metrics from Prometheus-compatible sources within an Amazon EKS cluster, and sends them to your Amazon Managed Service for Prometheus workspace. Scrapers are flexible. You can configure the scraper to control what metrics are collected, the frequency of collection, what transformations are applied to the metrics, and more.

    An IAM role will be created for you that Amazon Managed Service for Prometheus uses to access the metrics in your cluster. You must configure this role with a policy that allows it to scrape metrics from your cluster. For more information, see `Configuring your Amazon EKS cluster <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-eks-setup>`_ in the *Amazon Managed Service for Prometheus User Guide* .

    The ``scrapeConfiguration`` parameter contains the YAML configuration for the scraper.
    .. epigraph::

       For more information about collectors, including what metrics are collected, and how to configure the scraper, see `Using an AWS managed collector <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html
    :cloudformationResource: AWS::APS::Scraper
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_aps as aps
        
        cfn_scraper = aps.CfnScraper(self, "MyCfnScraper",
            destination=aps.CfnScraper.DestinationProperty(
                amp_configuration=aps.CfnScraper.AmpConfigurationProperty(
                    workspace_arn="workspaceArn"
                )
            ),
            scrape_configuration=aps.CfnScraper.ScrapeConfigurationProperty(
                configuration_blob="configurationBlob"
            ),
            source=aps.CfnScraper.SourceProperty(
                eks_configuration=aps.CfnScraper.EksConfigurationProperty(
                    cluster_arn="clusterArn",
                    subnet_ids=["subnetIds"],
        
                    # the properties below are optional
                    security_group_ids=["securityGroupIds"]
                )
            ),
        
            # the properties below are optional
            alias="alias",
            role_configuration=aps.CfnScraper.RoleConfigurationProperty(
                source_role_arn="sourceRoleArn",
                target_role_arn="targetRoleArn"
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
        destination: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScraper.DestinationProperty", typing.Dict[builtins.str, typing.Any]]],
        scrape_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScraper.ScrapeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        source: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScraper.SourceProperty", typing.Dict[builtins.str, typing.Any]]],
        alias: typing.Optional[builtins.str] = None,
        role_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnScraper.RoleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination: The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.
        :param scrape_configuration: The configuration in use by the scraper.
        :param source: The Amazon EKS cluster from which the scraper collects metrics.
        :param alias: An optional user-assigned scraper alias.
        :param role_configuration: The role configuration in an Amazon Managed Service for Prometheus scraper.
        :param tags: (Optional) The list of tag keys and values associated with the scraper.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d4cb1653b22b80f73c5fa4972418519c1d58f8ac033d22184f1b74ee25bf2b0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScraperProps(
            destination=destination,
            scrape_configuration=scrape_configuration,
            source=source,
            alias=alias,
            role_configuration=role_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58ef0eaaf8983b897d546f9e872b3a951993e032cd8b5f5f1725e32854f8d096)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d151b530ba64dde831142e12510e32c75c01b169477c6e43bf92c26ab330e2ae)
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
        '''The Amazon Resource Name (ARN) of the scraper.

        For example, ``arn:aws:aps:<region>:123456798012:scraper/s-example1-1234-abcd-5678-ef9012abcd34`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrRoleArn")
    def attr_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that provides permissions for the scraper to discover and collect metrics on your behalf.

        For example, ``arn:aws:iam::123456789012:role/service-role/AmazonGrafanaServiceRole-12example`` .

        :cloudformationAttribute: RoleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="attrScraperId")
    def attr_scraper_id(self) -> builtins.str:
        '''The ID of the scraper.

        For example, ``s-example1-1234-abcd-5678-ef9012abcd34`` .

        :cloudformationAttribute: ScraperId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrScraperId"))

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
    @jsii.member(jsii_name="destination")
    def destination(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnScraper.DestinationProperty"]:
        '''The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScraper.DestinationProperty"], jsii.get(self, "destination"))

    @destination.setter
    def destination(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnScraper.DestinationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29d835d9e17a3614f6837476fe3d3de37c4e38685abfd4cc8e4e49236802dfc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scrapeConfiguration")
    def scrape_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnScraper.ScrapeConfigurationProperty"]:
        '''The configuration in use by the scraper.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScraper.ScrapeConfigurationProperty"], jsii.get(self, "scrapeConfiguration"))

    @scrape_configuration.setter
    def scrape_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnScraper.ScrapeConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09a91c6d3e6031af4c2e1ba10ae98234919eb5f1efa54c12c929f7141e223af9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scrapeConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnScraper.SourceProperty"]:
        '''The Amazon EKS cluster from which the scraper collects metrics.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScraper.SourceProperty"], jsii.get(self, "source"))

    @source.setter
    def source(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnScraper.SourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4baaa2665d7ddf1c8e51575f5139441f25d102954ee91a2fcbf97644019a8c48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        '''An optional user-assigned scraper alias.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36b98e11e4ea8701c0469eb24a036fb1452c2573d264405f3d5237c104fd77a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleConfiguration")
    def role_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScraper.RoleConfigurationProperty"]]:
        '''The role configuration in an Amazon Managed Service for Prometheus scraper.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScraper.RoleConfigurationProperty"]], jsii.get(self, "roleConfiguration"))

    @role_configuration.setter
    def role_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnScraper.RoleConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8492f7c00f66de3309f136730786a3ad81d27f787146130fdb2b6191464e92c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) The list of tag keys and values associated with the scraper.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__265ada3fe1d3014c11a5af4d87c8e4b691d29a917e8643b804a82b7c3223573f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.AmpConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"workspace_arn": "workspaceArn"},
    )
    class AmpConfigurationProperty:
        def __init__(self, *, workspace_arn: builtins.str) -> None:
            '''The ``AmpConfiguration`` structure defines the Amazon Managed Service for Prometheus instance a scraper should send metrics to.

            :param workspace_arn: ARN of the Amazon Managed Service for Prometheus workspace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-ampconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                amp_configuration_property = aps.CfnScraper.AmpConfigurationProperty(
                    workspace_arn="workspaceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__02c8f0a43ed30375a3d1b283c2450f310915b0f0fcff6103d168cb18a16bfc4f)
                check_type(argname="argument workspace_arn", value=workspace_arn, expected_type=type_hints["workspace_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "workspace_arn": workspace_arn,
            }

        @builtins.property
        def workspace_arn(self) -> builtins.str:
            '''ARN of the Amazon Managed Service for Prometheus workspace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-ampconfiguration.html#cfn-aps-scraper-ampconfiguration-workspacearn
            '''
            result = self._values.get("workspace_arn")
            assert result is not None, "Required property 'workspace_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmpConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.DestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"amp_configuration": "ampConfiguration"},
    )
    class DestinationProperty:
        def __init__(
            self,
            *,
            amp_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScraper.AmpConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Where to send the metrics from a scraper.

            :param amp_configuration: The Amazon Managed Service for Prometheus workspace to send metrics to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-destination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                destination_property = aps.CfnScraper.DestinationProperty(
                    amp_configuration=aps.CfnScraper.AmpConfigurationProperty(
                        workspace_arn="workspaceArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e9dfeb013903b3b566e12e34ac903da7aaad96412ee8622e798d0f4931b78c31)
                check_type(argname="argument amp_configuration", value=amp_configuration, expected_type=type_hints["amp_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "amp_configuration": amp_configuration,
            }

        @builtins.property
        def amp_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnScraper.AmpConfigurationProperty"]:
            '''The Amazon Managed Service for Prometheus workspace to send metrics to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-destination.html#cfn-aps-scraper-destination-ampconfiguration
            '''
            result = self._values.get("amp_configuration")
            assert result is not None, "Required property 'amp_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScraper.AmpConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.EksConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cluster_arn": "clusterArn",
            "subnet_ids": "subnetIds",
            "security_group_ids": "securityGroupIds",
        },
    )
    class EksConfigurationProperty:
        def __init__(
            self,
            *,
            cluster_arn: builtins.str,
            subnet_ids: typing.Sequence[builtins.str],
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The ``EksConfiguration`` structure describes the connection to the Amazon EKS cluster from which a scraper collects metrics.

            :param cluster_arn: ARN of the Amazon EKS cluster.
            :param subnet_ids: A list of subnet IDs for the Amazon EKS cluster VPC configuration.
            :param security_group_ids: A list of the security group IDs for the Amazon EKS cluster VPC configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-eksconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                eks_configuration_property = aps.CfnScraper.EksConfigurationProperty(
                    cluster_arn="clusterArn",
                    subnet_ids=["subnetIds"],
                
                    # the properties below are optional
                    security_group_ids=["securityGroupIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d84c728405d664f762d3c86aae8f989f77a50273eb74e76dce90e3e0305f06a9)
                check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cluster_arn": cluster_arn,
                "subnet_ids": subnet_ids,
            }
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids

        @builtins.property
        def cluster_arn(self) -> builtins.str:
            '''ARN of the Amazon EKS cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-eksconfiguration.html#cfn-aps-scraper-eksconfiguration-clusterarn
            '''
            result = self._values.get("cluster_arn")
            assert result is not None, "Required property 'cluster_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''A list of subnet IDs for the Amazon EKS cluster VPC configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-eksconfiguration.html#cfn-aps-scraper-eksconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of the security group IDs for the Amazon EKS cluster VPC configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-eksconfiguration.html#cfn-aps-scraper-eksconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.RoleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_role_arn": "sourceRoleArn",
            "target_role_arn": "targetRoleArn",
        },
    )
    class RoleConfigurationProperty:
        def __init__(
            self,
            *,
            source_role_arn: typing.Optional[builtins.str] = None,
            target_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The role configuration in an Amazon Managed Service for Prometheus scraper.

            :param source_role_arn: The ARN of the source role.
            :param target_role_arn: The ARN of the target role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-roleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                role_configuration_property = aps.CfnScraper.RoleConfigurationProperty(
                    source_role_arn="sourceRoleArn",
                    target_role_arn="targetRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__86bf03aa28256ae3502c8e0745b810c6f1fe11b530f463788b7c7ffd32d996d1)
                check_type(argname="argument source_role_arn", value=source_role_arn, expected_type=type_hints["source_role_arn"])
                check_type(argname="argument target_role_arn", value=target_role_arn, expected_type=type_hints["target_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source_role_arn is not None:
                self._values["source_role_arn"] = source_role_arn
            if target_role_arn is not None:
                self._values["target_role_arn"] = target_role_arn

        @builtins.property
        def source_role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the source role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-roleconfiguration.html#cfn-aps-scraper-roleconfiguration-sourcerolearn
            '''
            result = self._values.get("source_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the target role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-roleconfiguration.html#cfn-aps-scraper-roleconfiguration-targetrolearn
            '''
            result = self._values.get("target_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RoleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.ScrapeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"configuration_blob": "configurationBlob"},
    )
    class ScrapeConfigurationProperty:
        def __init__(self, *, configuration_blob: builtins.str) -> None:
            '''A scrape configuration for a scraper, base 64 encoded.

            For more information, see `Scraper configuration <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-configuration>`_ in the *Amazon Managed Service for Prometheus User Guide* .

            :param configuration_blob: The base 64 encoded scrape configuration file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-scrapeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                scrape_configuration_property = aps.CfnScraper.ScrapeConfigurationProperty(
                    configuration_blob="configurationBlob"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__61507a1463486662c27c8fec99a5cb181f22e5f346b7bb6d10823ad9b7102b72)
                check_type(argname="argument configuration_blob", value=configuration_blob, expected_type=type_hints["configuration_blob"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "configuration_blob": configuration_blob,
            }

        @builtins.property
        def configuration_blob(self) -> builtins.str:
            '''The base 64 encoded scrape configuration file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-scrapeconfiguration.html#cfn-aps-scraper-scrapeconfiguration-configurationblob
            '''
            result = self._values.get("configuration_blob")
            assert result is not None, "Required property 'configuration_blob' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScrapeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={"eks_configuration": "eksConfiguration"},
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            eks_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScraper.EksConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The source of collected metrics for a scraper.

            :param eks_configuration: The Amazon EKS cluster from which a scraper collects metrics.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-source.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                source_property = aps.CfnScraper.SourceProperty(
                    eks_configuration=aps.CfnScraper.EksConfigurationProperty(
                        cluster_arn="clusterArn",
                        subnet_ids=["subnetIds"],
                
                        # the properties below are optional
                        security_group_ids=["securityGroupIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__655e83ac40d7d6fcc3362aa2c25fcfadc0beb5744ef393de105d7d152821a330)
                check_type(argname="argument eks_configuration", value=eks_configuration, expected_type=type_hints["eks_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "eks_configuration": eks_configuration,
            }

        @builtins.property
        def eks_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnScraper.EksConfigurationProperty"]:
            '''The Amazon EKS cluster from which a scraper collects metrics.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-source.html#cfn-aps-scraper-source-eksconfiguration
            '''
            result = self._values.get("eks_configuration")
            assert result is not None, "Required property 'eks_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScraper.EksConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_aps.CfnScraperProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "scrape_configuration": "scrapeConfiguration",
        "source": "source",
        "alias": "alias",
        "role_configuration": "roleConfiguration",
        "tags": "tags",
    },
)
class CfnScraperProps:
    def __init__(
        self,
        *,
        destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.DestinationProperty, typing.Dict[builtins.str, typing.Any]]],
        scrape_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.ScrapeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
        alias: typing.Optional[builtins.str] = None,
        role_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.RoleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnScraper``.

        :param destination: The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.
        :param scrape_configuration: The configuration in use by the scraper.
        :param source: The Amazon EKS cluster from which the scraper collects metrics.
        :param alias: An optional user-assigned scraper alias.
        :param role_configuration: The role configuration in an Amazon Managed Service for Prometheus scraper.
        :param tags: (Optional) The list of tag keys and values associated with the scraper.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_aps as aps
            
            cfn_scraper_props = aps.CfnScraperProps(
                destination=aps.CfnScraper.DestinationProperty(
                    amp_configuration=aps.CfnScraper.AmpConfigurationProperty(
                        workspace_arn="workspaceArn"
                    )
                ),
                scrape_configuration=aps.CfnScraper.ScrapeConfigurationProperty(
                    configuration_blob="configurationBlob"
                ),
                source=aps.CfnScraper.SourceProperty(
                    eks_configuration=aps.CfnScraper.EksConfigurationProperty(
                        cluster_arn="clusterArn",
                        subnet_ids=["subnetIds"],
            
                        # the properties below are optional
                        security_group_ids=["securityGroupIds"]
                    )
                ),
            
                # the properties below are optional
                alias="alias",
                role_configuration=aps.CfnScraper.RoleConfigurationProperty(
                    source_role_arn="sourceRoleArn",
                    target_role_arn="targetRoleArn"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f302dfc2aa92636b313e32f5d91a0ccfd79ebde0259b977f6291d4c8329455d7)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument scrape_configuration", value=scrape_configuration, expected_type=type_hints["scrape_configuration"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument role_configuration", value=role_configuration, expected_type=type_hints["role_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
            "scrape_configuration": scrape_configuration,
            "source": source,
        }
        if alias is not None:
            self._values["alias"] = alias
        if role_configuration is not None:
            self._values["role_configuration"] = role_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def destination(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnScraper.DestinationProperty]:
        '''The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-destination
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnScraper.DestinationProperty], result)

    @builtins.property
    def scrape_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnScraper.ScrapeConfigurationProperty]:
        '''The configuration in use by the scraper.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-scrapeconfiguration
        '''
        result = self._values.get("scrape_configuration")
        assert result is not None, "Required property 'scrape_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnScraper.ScrapeConfigurationProperty], result)

    @builtins.property
    def source(self) -> typing.Union[_IResolvable_da3f097b, CfnScraper.SourceProperty]:
        '''The Amazon EKS cluster from which the scraper collects metrics.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-source
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnScraper.SourceProperty], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''An optional user-assigned scraper alias.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-alias
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScraper.RoleConfigurationProperty]]:
        '''The role configuration in an Amazon Managed Service for Prometheus scraper.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-roleconfiguration
        '''
        result = self._values.get("role_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScraper.RoleConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) The list of tag keys and values associated with the scraper.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScraperProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnWorkspace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace",
):
    '''An Amazon Managed Service for Prometheus workspace is a logical and isolated Prometheus server dedicated to ingesting, storing, and querying your Prometheus-compatible metrics.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html
    :cloudformationResource: AWS::APS::Workspace
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_aps as aps
        
        cfn_workspace = aps.CfnWorkspace(self, "MyCfnWorkspace",
            alert_manager_definition="alertManagerDefinition",
            alias="alias",
            kms_key_arn="kmsKeyArn",
            logging_configuration=aps.CfnWorkspace.LoggingConfigurationProperty(
                log_group_arn="logGroupArn"
            ),
            query_logging_configuration=aps.CfnWorkspace.QueryLoggingConfigurationProperty(
                destinations=[aps.CfnWorkspace.LoggingDestinationProperty(
                    cloud_watch_logs=aps.CfnWorkspace.CloudWatchLogDestinationProperty(
                        log_group_arn="logGroupArn"
                    ),
                    filters=aps.CfnWorkspace.LoggingFilterProperty(
                        qsp_threshold=123
                    )
                )]
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            workspace_configuration=aps.CfnWorkspace.WorkspaceConfigurationProperty(
                limits_per_label_sets=[aps.CfnWorkspace.LimitsPerLabelSetProperty(
                    label_set=[aps.CfnWorkspace.LabelProperty(
                        name="name",
                        value="value"
                    )],
                    limits=aps.CfnWorkspace.LimitsPerLabelSetEntryProperty(
                        max_series=123
                    )
                )],
                retention_period_in_days=123
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alert_manager_definition: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspace.LoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        query_logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspace.QueryLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        workspace_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspace.WorkspaceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param alert_manager_definition: The alert manager definition, a YAML configuration for the alert manager in your Amazon Managed Service for Prometheus workspace. For details about the alert manager definition, see `Creating an alert manager configuration files <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-config.html>`_ in the *Amazon Managed Service for Prometheus User Guide* . The following example shows part of a CloudFormation YAML file with an embedded alert manager definition (following the ``- |-`` ). ``Workspace: Type: AWS::APS::Workspace .... Properties: .... AlertManagerDefinition: Fn::Sub: - |- alertmanager_config: | templates: - 'default_template' route: receiver: example-sns receivers: - name: example-sns sns_configs: - topic_arn: 'arn:aws:sns:${AWS::Region}:${AWS::AccountId}:${TopicName}' -``
        :param alias: The alias that is assigned to this workspace to help identify it. It does not need to be unique.
        :param kms_key_arn: (optional) The ARN for a customer managed AWS KMS key to use for encrypting data within your workspace. For more information about using your own key in your workspace, see `Encryption at rest <https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .
        :param logging_configuration: Contains information about the current rules and alerting logging configuration for the workspace. .. epigraph:: These logging configurations are only for rules and alerting logs.
        :param query_logging_configuration: The definition of logging configuration in an Amazon Managed Service for Prometheus workspace.
        :param tags: The list of tag keys and values that are associated with the workspace.
        :param workspace_configuration: Use this structure to define label sets and the ingestion limits for time series that match label sets, and to specify the retention period of the workspace.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d7d4de6c2c3c0a6cc1f746f35f29f98344da5c5d59e48a9d1e788ab80e3ef9b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkspaceProps(
            alert_manager_definition=alert_manager_definition,
            alias=alias,
            kms_key_arn=kms_key_arn,
            logging_configuration=logging_configuration,
            query_logging_configuration=query_logging_configuration,
            tags=tags,
            workspace_configuration=workspace_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ea1a406920301232e7f737fa791c75b19a41702c2a8761c41de9163390ebcdf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__391b593ff5f1b04fd33a43b56be0c4a7f41dd147af44a0bc665b22d97e9640c8)
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
        '''The ARN of the workspace.

        For example, ``arn:aws:aps:<region>:123456789012:workspace/ws-example1-1234-abcd-5678-ef90abcd1234`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPrometheusEndpoint")
    def attr_prometheus_endpoint(self) -> builtins.str:
        '''The Prometheus endpoint available for this workspace.

        For example, ``https://aps-workspaces.<region>.amazonaws.com/workspaces/ws-example1-1234-abcd-5678-ef90abcd1234/api/v1/`` .

        :cloudformationAttribute: PrometheusEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrometheusEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkspaceId")
    def attr_workspace_id(self) -> builtins.str:
        '''The unique ID for the workspace.

        For example, ``ws-example1-1234-abcd-5678-ef90abcd1234`` .

        :cloudformationAttribute: WorkspaceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkspaceId"))

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
    @jsii.member(jsii_name="alertManagerDefinition")
    def alert_manager_definition(self) -> typing.Optional[builtins.str]:
        '''The alert manager definition, a YAML configuration for the alert manager in your Amazon Managed Service for Prometheus workspace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alertManagerDefinition"))

    @alert_manager_definition.setter
    def alert_manager_definition(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c2399f13a196d4fdd83827148d3942b4231e42e722c32b0c66a56f8425f5d1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alertManagerDefinition", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        '''The alias that is assigned to this workspace to help identify it.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69c703012a200792f370b43791a7b9e6c8ab12b196993de037a82396c6c51b3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''(optional) The ARN for a customer managed AWS KMS key to use for encrypting data within your workspace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06e1bc26d25cdad92f552b6ceb5e8a4ae6d459a5f2737ae032c5a2f069eedf68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LoggingConfigurationProperty"]]:
        '''Contains information about the current rules and alerting logging configuration for the workspace.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LoggingConfigurationProperty"]], jsii.get(self, "loggingConfiguration"))

    @logging_configuration.setter
    def logging_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LoggingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab06dccfc037b2ba3e02b4a3154224a63edcfe3fc06381ff9162c2c33a94b712)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="queryLoggingConfiguration")
    def query_logging_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.QueryLoggingConfigurationProperty"]]:
        '''The definition of logging configuration in an Amazon Managed Service for Prometheus workspace.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.QueryLoggingConfigurationProperty"]], jsii.get(self, "queryLoggingConfiguration"))

    @query_logging_configuration.setter
    def query_logging_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.QueryLoggingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6591166b06ced49bc35c6390884a7a1c30cea4102022183768ac43e25c00f9fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryLoggingConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of tag keys and values that are associated with the workspace.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb4e1977fb1f7aad47144a42af408e41c9d01794f3569a614a9ed54effb1c1e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="workspaceConfiguration")
    def workspace_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.WorkspaceConfigurationProperty"]]:
        '''Use this structure to define label sets and the ingestion limits for time series that match label sets, and to specify the retention period of the workspace.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.WorkspaceConfigurationProperty"]], jsii.get(self, "workspaceConfiguration"))

    @workspace_configuration.setter
    def workspace_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.WorkspaceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dc44ff5af32b5cdcf5234cdf89709e32cf5a9217d64f6f2b6625191085cd191)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceConfiguration", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.CloudWatchLogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_arn": "logGroupArn"},
    )
    class CloudWatchLogDestinationProperty:
        def __init__(self, *, log_group_arn: builtins.str) -> None:
            '''Configuration details for logging to CloudWatch Logs.

            :param log_group_arn: The ARN of the CloudWatch log group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-cloudwatchlogdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                cloud_watch_log_destination_property = aps.CfnWorkspace.CloudWatchLogDestinationProperty(
                    log_group_arn="logGroupArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__925c774442f9150193a5d3bfa3fb05562aec6581139c1378b5f09e1c30fb40ee)
                check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_group_arn": log_group_arn,
            }

        @builtins.property
        def log_group_arn(self) -> builtins.str:
            '''The ARN of the CloudWatch log group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-cloudwatchlogdestination.html#cfn-aps-workspace-cloudwatchlogdestination-loggrouparn
            '''
            result = self._values.get("log_group_arn")
            assert result is not None, "Required property 'log_group_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.LabelProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class LabelProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''A label is a name:value pair used to add context to ingested metrics.

            This structure defines the name and value for one label that is used in a label set. You can set ingestion limits on time series that match defined label sets, to help prevent a workspace from being overwhelmed with unexpected spikes in time series ingestion.

            :param name: The name for this label.
            :param value: The value for this label.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-label.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                label_property = aps.CfnWorkspace.LabelProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b34eb56a3257d05ed157ec9252590ce797546e9e647035e7f3e639a6629c1cd3)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name for this label.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-label.html#cfn-aps-workspace-label-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value for this label.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-label.html#cfn-aps-workspace-label-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LabelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.LimitsPerLabelSetEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"max_series": "maxSeries"},
    )
    class LimitsPerLabelSetEntryProperty:
        def __init__(self, *, max_series: typing.Optional[jsii.Number] = None) -> None:
            '''This structure contains the limits that apply to time series that match one label set.

            :param max_series: The maximum number of active series that can be ingested that match this label set. Setting this to 0 causes no label set limit to be enforced, but it does cause Amazon Managed Service for Prometheus to vend label set metrics to CloudWatch

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-limitsperlabelsetentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                limits_per_label_set_entry_property = aps.CfnWorkspace.LimitsPerLabelSetEntryProperty(
                    max_series=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__86191e69da536181f19aaae8e8a81e682e12b975b6edce1319b4d4a8b451cb95)
                check_type(argname="argument max_series", value=max_series, expected_type=type_hints["max_series"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_series is not None:
                self._values["max_series"] = max_series

        @builtins.property
        def max_series(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of active series that can be ingested that match this label set.

            Setting this to 0 causes no label set limit to be enforced, but it does cause Amazon Managed Service for Prometheus to vend label set metrics to CloudWatch

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-limitsperlabelsetentry.html#cfn-aps-workspace-limitsperlabelsetentry-maxseries
            '''
            result = self._values.get("max_series")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LimitsPerLabelSetEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.LimitsPerLabelSetProperty",
        jsii_struct_bases=[],
        name_mapping={"label_set": "labelSet", "limits": "limits"},
    )
    class LimitsPerLabelSetProperty:
        def __init__(
            self,
            *,
            label_set: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspace.LabelProperty", typing.Dict[builtins.str, typing.Any]]]]],
            limits: typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspace.LimitsPerLabelSetEntryProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''This defines a label set for the workspace, and defines the ingestion limit for active time series that match that label set.

            Each label name in a label set must be unique.

            :param label_set: This defines one label set that will have an enforced ingestion limit. You can set ingestion limits on time series that match defined label sets, to help prevent a workspace from being overwhelmed with unexpected spikes in time series ingestion. Label values accept all UTF-8 characters with one exception. If the label name is metric name label ``__ *name* __`` , then the *metric* part of the name must conform to the following pattern: ``[a-zA-Z_:][a-zA-Z0-9_:]*``
            :param limits: This structure contains the information about the limits that apply to time series that match this label set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-limitsperlabelset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                limits_per_label_set_property = aps.CfnWorkspace.LimitsPerLabelSetProperty(
                    label_set=[aps.CfnWorkspace.LabelProperty(
                        name="name",
                        value="value"
                    )],
                    limits=aps.CfnWorkspace.LimitsPerLabelSetEntryProperty(
                        max_series=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3d8045fc76bdfc4af5de994e0ebe3331fd81257f1ae53d90373a7ad960b0bca7)
                check_type(argname="argument label_set", value=label_set, expected_type=type_hints["label_set"])
                check_type(argname="argument limits", value=limits, expected_type=type_hints["limits"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "label_set": label_set,
                "limits": limits,
            }

        @builtins.property
        def label_set(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LabelProperty"]]]:
            '''This defines one label set that will have an enforced ingestion limit.

            You can set ingestion limits on time series that match defined label sets, to help prevent a workspace from being overwhelmed with unexpected spikes in time series ingestion.

            Label values accept all UTF-8 characters with one exception. If the label name is metric name label ``__ *name* __`` , then the *metric* part of the name must conform to the following pattern: ``[a-zA-Z_:][a-zA-Z0-9_:]*``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-limitsperlabelset.html#cfn-aps-workspace-limitsperlabelset-labelset
            '''
            result = self._values.get("label_set")
            assert result is not None, "Required property 'label_set' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LabelProperty"]]], result)

        @builtins.property
        def limits(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LimitsPerLabelSetEntryProperty"]:
            '''This structure contains the information about the limits that apply to time series that match this label set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-limitsperlabelset.html#cfn-aps-workspace-limitsperlabelset-limits
            '''
            result = self._values.get("limits")
            assert result is not None, "Required property 'limits' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LimitsPerLabelSetEntryProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LimitsPerLabelSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.LoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_arn": "logGroupArn"},
    )
    class LoggingConfigurationProperty:
        def __init__(
            self,
            *,
            log_group_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about the rules and alerting logging configuration for the workspace.

            .. epigraph::

               These logging configurations are only for rules and alerting logs.

            :param log_group_arn: The ARN of the CloudWatch log group to which the vended log data will be published. This log group must exist prior to calling this operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                logging_configuration_property = aps.CfnWorkspace.LoggingConfigurationProperty(
                    log_group_arn="logGroupArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa0678eca2188c6c3220d708f7d16298acecab165f03de8b400d1fada6a4b9d9)
                check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group_arn is not None:
                self._values["log_group_arn"] = log_group_arn

        @builtins.property
        def log_group_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the CloudWatch log group to which the vended log data will be published.

            This log group must exist prior to calling this operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingconfiguration.html#cfn-aps-workspace-loggingconfiguration-loggrouparn
            '''
            result = self._values.get("log_group_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.LoggingDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_watch_logs": "cloudWatchLogs", "filters": "filters"},
    )
    class LoggingDestinationProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs: typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspace.CloudWatchLogDestinationProperty", typing.Dict[builtins.str, typing.Any]]],
            filters: typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspace.LoggingFilterProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The logging destination in an Amazon Managed Service for Prometheus workspace.

            :param cloud_watch_logs: Configuration details for logging to CloudWatch Logs.
            :param filters: Filtering criteria that determine which queries are logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                logging_destination_property = aps.CfnWorkspace.LoggingDestinationProperty(
                    cloud_watch_logs=aps.CfnWorkspace.CloudWatchLogDestinationProperty(
                        log_group_arn="logGroupArn"
                    ),
                    filters=aps.CfnWorkspace.LoggingFilterProperty(
                        qsp_threshold=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cce5991812152322bf70db3d7cea0d7bb3cda26bb6b0e82d9bd091ef05995168)
                check_type(argname="argument cloud_watch_logs", value=cloud_watch_logs, expected_type=type_hints["cloud_watch_logs"])
                check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cloud_watch_logs": cloud_watch_logs,
                "filters": filters,
            }

        @builtins.property
        def cloud_watch_logs(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnWorkspace.CloudWatchLogDestinationProperty"]:
            '''Configuration details for logging to CloudWatch Logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingdestination.html#cfn-aps-workspace-loggingdestination-cloudwatchlogs
            '''
            result = self._values.get("cloud_watch_logs")
            assert result is not None, "Required property 'cloud_watch_logs' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnWorkspace.CloudWatchLogDestinationProperty"], result)

        @builtins.property
        def filters(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LoggingFilterProperty"]:
            '''Filtering criteria that determine which queries are logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingdestination.html#cfn-aps-workspace-loggingdestination-filters
            '''
            result = self._values.get("filters")
            assert result is not None, "Required property 'filters' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LoggingFilterProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.LoggingFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"qsp_threshold": "qspThreshold"},
    )
    class LoggingFilterProperty:
        def __init__(self, *, qsp_threshold: jsii.Number) -> None:
            '''Filtering criteria that determine which queries are logged.

            :param qsp_threshold: Query logs with QSP above this limit are vended.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                logging_filter_property = aps.CfnWorkspace.LoggingFilterProperty(
                    qsp_threshold=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8f1710f9a533b3c78aa9735866c9480208fe7ceb912d68581872b145d4c634fd)
                check_type(argname="argument qsp_threshold", value=qsp_threshold, expected_type=type_hints["qsp_threshold"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "qsp_threshold": qsp_threshold,
            }

        @builtins.property
        def qsp_threshold(self) -> jsii.Number:
            '''Query logs with QSP above this limit are vended.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingfilter.html#cfn-aps-workspace-loggingfilter-qspthreshold
            '''
            result = self._values.get("qsp_threshold")
            assert result is not None, "Required property 'qsp_threshold' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.QueryLoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"destinations": "destinations"},
    )
    class QueryLoggingConfigurationProperty:
        def __init__(
            self,
            *,
            destinations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspace.LoggingDestinationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The query logging configuration in an Amazon Managed Service for Prometheus workspace.

            :param destinations: Defines a destination and its associated filtering criteria for query logging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-queryloggingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                query_logging_configuration_property = aps.CfnWorkspace.QueryLoggingConfigurationProperty(
                    destinations=[aps.CfnWorkspace.LoggingDestinationProperty(
                        cloud_watch_logs=aps.CfnWorkspace.CloudWatchLogDestinationProperty(
                            log_group_arn="logGroupArn"
                        ),
                        filters=aps.CfnWorkspace.LoggingFilterProperty(
                            qsp_threshold=123
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__59e9b7a5bb1ecf6d3e6bf0c4d2f497bea98d1fe68b36d502a98c9b336781a58a)
                check_type(argname="argument destinations", value=destinations, expected_type=type_hints["destinations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destinations": destinations,
            }

        @builtins.property
        def destinations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LoggingDestinationProperty"]]]:
            '''Defines a destination and its associated filtering criteria for query logging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-queryloggingconfiguration.html#cfn-aps-workspace-queryloggingconfiguration-destinations
            '''
            result = self._values.get("destinations")
            assert result is not None, "Required property 'destinations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LoggingDestinationProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueryLoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.WorkspaceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "limits_per_label_sets": "limitsPerLabelSets",
            "retention_period_in_days": "retentionPeriodInDays",
        },
    )
    class WorkspaceConfigurationProperty:
        def __init__(
            self,
            *,
            limits_per_label_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkspace.LimitsPerLabelSetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            retention_period_in_days: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Use this structure to define label sets and the ingestion limits for time series that match label sets, and to specify the retention period of the workspace.

            :param limits_per_label_sets: This is an array of structures, where each structure defines a label set for the workspace, and defines the ingestion limit for active time series for each of those label sets. Each label name in a label set must be unique.
            :param retention_period_in_days: Specifies how many days that metrics will be retained in the workspace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-workspaceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                workspace_configuration_property = aps.CfnWorkspace.WorkspaceConfigurationProperty(
                    limits_per_label_sets=[aps.CfnWorkspace.LimitsPerLabelSetProperty(
                        label_set=[aps.CfnWorkspace.LabelProperty(
                            name="name",
                            value="value"
                        )],
                        limits=aps.CfnWorkspace.LimitsPerLabelSetEntryProperty(
                            max_series=123
                        )
                    )],
                    retention_period_in_days=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d8bd4b9a39be1594ef4681992e92f89f24816c775c0e0c40e340be13e59392a)
                check_type(argname="argument limits_per_label_sets", value=limits_per_label_sets, expected_type=type_hints["limits_per_label_sets"])
                check_type(argname="argument retention_period_in_days", value=retention_period_in_days, expected_type=type_hints["retention_period_in_days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if limits_per_label_sets is not None:
                self._values["limits_per_label_sets"] = limits_per_label_sets
            if retention_period_in_days is not None:
                self._values["retention_period_in_days"] = retention_period_in_days

        @builtins.property
        def limits_per_label_sets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LimitsPerLabelSetProperty"]]]]:
            '''This is an array of structures, where each structure defines a label set for the workspace, and defines the ingestion limit for active time series for each of those label sets.

            Each label name in a label set must be unique.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-workspaceconfiguration.html#cfn-aps-workspace-workspaceconfiguration-limitsperlabelsets
            '''
            result = self._values.get("limits_per_label_sets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkspace.LimitsPerLabelSetProperty"]]]], result)

        @builtins.property
        def retention_period_in_days(self) -> typing.Optional[jsii.Number]:
            '''Specifies how many days that metrics will be retained in the workspace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-workspaceconfiguration.html#cfn-aps-workspace-workspaceconfiguration-retentionperiodindays
            '''
            result = self._values.get("retention_period_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkspaceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_aps.CfnWorkspaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "alert_manager_definition": "alertManagerDefinition",
        "alias": "alias",
        "kms_key_arn": "kmsKeyArn",
        "logging_configuration": "loggingConfiguration",
        "query_logging_configuration": "queryLoggingConfiguration",
        "tags": "tags",
        "workspace_configuration": "workspaceConfiguration",
    },
)
class CfnWorkspaceProps:
    def __init__(
        self,
        *,
        alert_manager_definition: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        query_logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.QueryLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        workspace_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.WorkspaceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkspace``.

        :param alert_manager_definition: The alert manager definition, a YAML configuration for the alert manager in your Amazon Managed Service for Prometheus workspace. For details about the alert manager definition, see `Creating an alert manager configuration files <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-config.html>`_ in the *Amazon Managed Service for Prometheus User Guide* . The following example shows part of a CloudFormation YAML file with an embedded alert manager definition (following the ``- |-`` ). ``Workspace: Type: AWS::APS::Workspace .... Properties: .... AlertManagerDefinition: Fn::Sub: - |- alertmanager_config: | templates: - 'default_template' route: receiver: example-sns receivers: - name: example-sns sns_configs: - topic_arn: 'arn:aws:sns:${AWS::Region}:${AWS::AccountId}:${TopicName}' -``
        :param alias: The alias that is assigned to this workspace to help identify it. It does not need to be unique.
        :param kms_key_arn: (optional) The ARN for a customer managed AWS KMS key to use for encrypting data within your workspace. For more information about using your own key in your workspace, see `Encryption at rest <https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .
        :param logging_configuration: Contains information about the current rules and alerting logging configuration for the workspace. .. epigraph:: These logging configurations are only for rules and alerting logs.
        :param query_logging_configuration: The definition of logging configuration in an Amazon Managed Service for Prometheus workspace.
        :param tags: The list of tag keys and values that are associated with the workspace.
        :param workspace_configuration: Use this structure to define label sets and the ingestion limits for time series that match label sets, and to specify the retention period of the workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_aps as aps
            
            cfn_workspace_props = aps.CfnWorkspaceProps(
                alert_manager_definition="alertManagerDefinition",
                alias="alias",
                kms_key_arn="kmsKeyArn",
                logging_configuration=aps.CfnWorkspace.LoggingConfigurationProperty(
                    log_group_arn="logGroupArn"
                ),
                query_logging_configuration=aps.CfnWorkspace.QueryLoggingConfigurationProperty(
                    destinations=[aps.CfnWorkspace.LoggingDestinationProperty(
                        cloud_watch_logs=aps.CfnWorkspace.CloudWatchLogDestinationProperty(
                            log_group_arn="logGroupArn"
                        ),
                        filters=aps.CfnWorkspace.LoggingFilterProperty(
                            qsp_threshold=123
                        )
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                workspace_configuration=aps.CfnWorkspace.WorkspaceConfigurationProperty(
                    limits_per_label_sets=[aps.CfnWorkspace.LimitsPerLabelSetProperty(
                        label_set=[aps.CfnWorkspace.LabelProperty(
                            name="name",
                            value="value"
                        )],
                        limits=aps.CfnWorkspace.LimitsPerLabelSetEntryProperty(
                            max_series=123
                        )
                    )],
                    retention_period_in_days=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98e95bd874171795b8c6f6104e5fee9fa1d8f50cb6e1edc6d2cc01a77eb0f50a)
            check_type(argname="argument alert_manager_definition", value=alert_manager_definition, expected_type=type_hints["alert_manager_definition"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument logging_configuration", value=logging_configuration, expected_type=type_hints["logging_configuration"])
            check_type(argname="argument query_logging_configuration", value=query_logging_configuration, expected_type=type_hints["query_logging_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument workspace_configuration", value=workspace_configuration, expected_type=type_hints["workspace_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alert_manager_definition is not None:
            self._values["alert_manager_definition"] = alert_manager_definition
        if alias is not None:
            self._values["alias"] = alias
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if logging_configuration is not None:
            self._values["logging_configuration"] = logging_configuration
        if query_logging_configuration is not None:
            self._values["query_logging_configuration"] = query_logging_configuration
        if tags is not None:
            self._values["tags"] = tags
        if workspace_configuration is not None:
            self._values["workspace_configuration"] = workspace_configuration

    @builtins.property
    def alert_manager_definition(self) -> typing.Optional[builtins.str]:
        '''The alert manager definition, a YAML configuration for the alert manager in your Amazon Managed Service for Prometheus workspace.

        For details about the alert manager definition, see `Creating an alert manager configuration files <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-config.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .

        The following example shows part of a CloudFormation YAML file with an embedded alert manager definition (following the ``- |-`` ).

        ``Workspace: Type: AWS::APS::Workspace .... Properties: .... AlertManagerDefinition: Fn::Sub: - |- alertmanager_config: | templates: - 'default_template' route: receiver: example-sns receivers: - name: example-sns sns_configs: - topic_arn: 'arn:aws:sns:${AWS::Region}:${AWS::AccountId}:${TopicName}' -``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-alertmanagerdefinition
        '''
        result = self._values.get("alert_manager_definition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''The alias that is assigned to this workspace to help identify it.

        It does not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-alias
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''(optional) The ARN for a customer managed AWS KMS key to use for encrypting data within your workspace.

        For more information about using your own key in your workspace, see `Encryption at rest <https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.LoggingConfigurationProperty]]:
        '''Contains information about the current rules and alerting logging configuration for the workspace.

        .. epigraph::

           These logging configurations are only for rules and alerting logs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-loggingconfiguration
        '''
        result = self._values.get("logging_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.LoggingConfigurationProperty]], result)

    @builtins.property
    def query_logging_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.QueryLoggingConfigurationProperty]]:
        '''The definition of logging configuration in an Amazon Managed Service for Prometheus workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-queryloggingconfiguration
        '''
        result = self._values.get("query_logging_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.QueryLoggingConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of tag keys and values that are associated with the workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def workspace_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.WorkspaceConfigurationProperty]]:
        '''Use this structure to define label sets and the ingestion limits for time series that match label sets, and to specify the retention period of the workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-workspaceconfiguration
        '''
        result = self._values.get("workspace_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.WorkspaceConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkspaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnRuleGroupsNamespace",
    "CfnRuleGroupsNamespaceProps",
    "CfnScraper",
    "CfnScraperProps",
    "CfnWorkspace",
    "CfnWorkspaceProps",
]

publication.publish()

def _typecheckingstub__02d681a4d4a1e9d9052c98f45bf8b21257e825ee8185b30ea4b6f887fc7416b1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data: builtins.str,
    name: builtins.str,
    workspace: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f066376b2a4b15a103f9a01bca66f252615381ddc55bd5508262712fd03eec2d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__501ad912878791d9cc1a45e52a9642fb0747f4ddf4482708286f9bfde7e036de(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__327e955bc86deb15923357f0f050e077304b8dbbb2c9baba9d84a13c5d7b695d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f3851e1fa5b758763dff1a85515e41a8c57e1b4da81b2e677f003890944957f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f899db17dfa1e1837e2b90cca5f83f23f67ca015116201811ad84d044e9ebe95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9af819e60d52c87c9369e4854d0dfc8d4917db97219839fbc11cf2bdad55659(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ba9f13df78597d09b62adc5501ac56c5fedca3215c115e02cb7e3be9e440366(
    *,
    data: builtins.str,
    name: builtins.str,
    workspace: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d4cb1653b22b80f73c5fa4972418519c1d58f8ac033d22184f1b74ee25bf2b0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.DestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    scrape_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.ScrapeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
    alias: typing.Optional[builtins.str] = None,
    role_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.RoleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58ef0eaaf8983b897d546f9e872b3a951993e032cd8b5f5f1725e32854f8d096(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d151b530ba64dde831142e12510e32c75c01b169477c6e43bf92c26ab330e2ae(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29d835d9e17a3614f6837476fe3d3de37c4e38685abfd4cc8e4e49236802dfc0(
    value: typing.Union[_IResolvable_da3f097b, CfnScraper.DestinationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09a91c6d3e6031af4c2e1ba10ae98234919eb5f1efa54c12c929f7141e223af9(
    value: typing.Union[_IResolvable_da3f097b, CfnScraper.ScrapeConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4baaa2665d7ddf1c8e51575f5139441f25d102954ee91a2fcbf97644019a8c48(
    value: typing.Union[_IResolvable_da3f097b, CfnScraper.SourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36b98e11e4ea8701c0469eb24a036fb1452c2573d264405f3d5237c104fd77a0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8492f7c00f66de3309f136730786a3ad81d27f787146130fdb2b6191464e92c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScraper.RoleConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__265ada3fe1d3014c11a5af4d87c8e4b691d29a917e8643b804a82b7c3223573f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02c8f0a43ed30375a3d1b283c2450f310915b0f0fcff6103d168cb18a16bfc4f(
    *,
    workspace_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9dfeb013903b3b566e12e34ac903da7aaad96412ee8622e798d0f4931b78c31(
    *,
    amp_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.AmpConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d84c728405d664f762d3c86aae8f989f77a50273eb74e76dce90e3e0305f06a9(
    *,
    cluster_arn: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86bf03aa28256ae3502c8e0745b810c6f1fe11b530f463788b7c7ffd32d996d1(
    *,
    source_role_arn: typing.Optional[builtins.str] = None,
    target_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61507a1463486662c27c8fec99a5cb181f22e5f346b7bb6d10823ad9b7102b72(
    *,
    configuration_blob: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__655e83ac40d7d6fcc3362aa2c25fcfadc0beb5744ef393de105d7d152821a330(
    *,
    eks_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.EksConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f302dfc2aa92636b313e32f5d91a0ccfd79ebde0259b977f6291d4c8329455d7(
    *,
    destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.DestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    scrape_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.ScrapeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
    alias: typing.Optional[builtins.str] = None,
    role_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.RoleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d7d4de6c2c3c0a6cc1f746f35f29f98344da5c5d59e48a9d1e788ab80e3ef9b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alert_manager_definition: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    query_logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.QueryLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    workspace_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.WorkspaceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ea1a406920301232e7f737fa791c75b19a41702c2a8761c41de9163390ebcdf(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__391b593ff5f1b04fd33a43b56be0c4a7f41dd147af44a0bc665b22d97e9640c8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c2399f13a196d4fdd83827148d3942b4231e42e722c32b0c66a56f8425f5d1a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69c703012a200792f370b43791a7b9e6c8ab12b196993de037a82396c6c51b3d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06e1bc26d25cdad92f552b6ceb5e8a4ae6d459a5f2737ae032c5a2f069eedf68(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab06dccfc037b2ba3e02b4a3154224a63edcfe3fc06381ff9162c2c33a94b712(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.LoggingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6591166b06ced49bc35c6390884a7a1c30cea4102022183768ac43e25c00f9fc(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.QueryLoggingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb4e1977fb1f7aad47144a42af408e41c9d01794f3569a614a9ed54effb1c1e5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dc44ff5af32b5cdcf5234cdf89709e32cf5a9217d64f6f2b6625191085cd191(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.WorkspaceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__925c774442f9150193a5d3bfa3fb05562aec6581139c1378b5f09e1c30fb40ee(
    *,
    log_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b34eb56a3257d05ed157ec9252590ce797546e9e647035e7f3e639a6629c1cd3(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86191e69da536181f19aaae8e8a81e682e12b975b6edce1319b4d4a8b451cb95(
    *,
    max_series: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d8045fc76bdfc4af5de994e0ebe3331fd81257f1ae53d90373a7ad960b0bca7(
    *,
    label_set: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LabelProperty, typing.Dict[builtins.str, typing.Any]]]]],
    limits: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LimitsPerLabelSetEntryProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa0678eca2188c6c3220d708f7d16298acecab165f03de8b400d1fada6a4b9d9(
    *,
    log_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cce5991812152322bf70db3d7cea0d7bb3cda26bb6b0e82d9bd091ef05995168(
    *,
    cloud_watch_logs: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.CloudWatchLogDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    filters: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LoggingFilterProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f1710f9a533b3c78aa9735866c9480208fe7ceb912d68581872b145d4c634fd(
    *,
    qsp_threshold: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59e9b7a5bb1ecf6d3e6bf0c4d2f497bea98d1fe68b36d502a98c9b336781a58a(
    *,
    destinations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LoggingDestinationProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d8bd4b9a39be1594ef4681992e92f89f24816c775c0e0c40e340be13e59392a(
    *,
    limits_per_label_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LimitsPerLabelSetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    retention_period_in_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98e95bd874171795b8c6f6104e5fee9fa1d8f50cb6e1edc6d2cc01a77eb0f50a(
    *,
    alert_manager_definition: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    query_logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.QueryLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    workspace_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.WorkspaceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
