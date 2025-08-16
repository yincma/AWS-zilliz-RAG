r'''
# AWS::AccessAnalyzer Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_accessanalyzer as accessanalyzer
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AccessAnalyzer construct libraries](https://constructs.dev/search?q=accessanalyzer)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AccessAnalyzer resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AccessAnalyzer.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AccessAnalyzer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AccessAnalyzer.html).

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
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnAnalyzer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_accessanalyzer.CfnAnalyzer",
):
    '''The ``AWS::AccessAnalyzer::Analyzer`` resource specifies a new analyzer.

    The analyzer is an object that represents the IAM Access Analyzer feature. An analyzer is required for Access Analyzer to become operational.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html
    :cloudformationResource: AWS::AccessAnalyzer::Analyzer
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_accessanalyzer as accessanalyzer
        
        cfn_analyzer = accessanalyzer.CfnAnalyzer(self, "MyCfnAnalyzer",
            type="type",
        
            # the properties below are optional
            analyzer_configuration=accessanalyzer.CfnAnalyzer.AnalyzerConfigurationProperty(
                internal_access_configuration=accessanalyzer.CfnAnalyzer.InternalAccessConfigurationProperty(
                    internal_access_analysis_rule=accessanalyzer.CfnAnalyzer.InternalAccessAnalysisRuleProperty(
                        inclusions=[accessanalyzer.CfnAnalyzer.InternalAccessAnalysisRuleCriteriaProperty(
                            account_ids=["accountIds"],
                            resource_arns=["resourceArns"],
                            resource_types=["resourceTypes"]
                        )]
                    )
                ),
                unused_access_configuration=accessanalyzer.CfnAnalyzer.UnusedAccessConfigurationProperty(
                    analysis_rule=accessanalyzer.CfnAnalyzer.AnalysisRuleProperty(
                        exclusions=[accessanalyzer.CfnAnalyzer.AnalysisRuleCriteriaProperty(
                            account_ids=["accountIds"],
                            resource_tags=[[CfnTag(
                                key="key",
                                value="value"
                            )]]
                        )]
                    ),
                    unused_access_age=123
                )
            ),
            analyzer_name="analyzerName",
            archive_rules=[accessanalyzer.CfnAnalyzer.ArchiveRuleProperty(
                filter=[accessanalyzer.CfnAnalyzer.FilterProperty(
                    property="property",
        
                    # the properties below are optional
                    contains=["contains"],
                    eq=["eq"],
                    exists=False,
                    neq=["neq"]
                )],
                rule_name="ruleName"
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
        type: builtins.str,
        analyzer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalyzer.AnalyzerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        analyzer_name: typing.Optional[builtins.str] = None,
        archive_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalyzer.ArchiveRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param type: The type represents the zone of trust for the analyzer. *Allowed Values* : ACCOUNT | ORGANIZATION | ACCOUNT_UNUSED_ACCESS | ACCOUNT_INTERNAL_ACCESS | ORGANIZATION_INTERNAL_ACCESS | ORGANIZATION_UNUSED_ACCESS
        :param analyzer_configuration: Contains information about the configuration of an analyzer for an AWS organization or account.
        :param analyzer_name: The name of the analyzer.
        :param archive_rules: Specifies the archive rules to add for the analyzer. Archive rules automatically archive findings that meet the criteria you define for the rule.
        :param tags: An array of key-value pairs to apply to the analyzer. You can use the set of Unicode letters, digits, whitespace, ``_`` , ``.`` , ``/`` , ``=`` , ``+`` , and ``-`` . For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with ``aws:`` . For the tag value, you can specify a value that is 0 to 256 characters in length.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d078d0b17e4dff80691cd25737bc9c648722f68955725da002d3ab5d4df9b21)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAnalyzerProps(
            type=type,
            analyzer_configuration=analyzer_configuration,
            analyzer_name=analyzer_name,
            archive_rules=archive_rules,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a366b020d431b9e8e5d2ed8e3b287179b77a059bb9e4407de61c18f8bafea93)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b4a15c19694e0f2a4c59bffdc30147a3fd55610e77c34007676071a6a1cee74)
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
        '''The ARN of the analyzer that was created.

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
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type represents the zone of trust for the analyzer.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae0ebe072220649d8253f3011fe641bc781e24d2bbf9d9a1cc55fdf1fb9124cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="analyzerConfiguration")
    def analyzer_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.AnalyzerConfigurationProperty"]]:
        '''Contains information about the configuration of an analyzer for an AWS organization or account.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.AnalyzerConfigurationProperty"]], jsii.get(self, "analyzerConfiguration"))

    @analyzer_configuration.setter
    def analyzer_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.AnalyzerConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b65a5d08bf50e1911863b6e4854f804654921017c34f668f95a5081f5c25b8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "analyzerConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="analyzerName")
    def analyzer_name(self) -> typing.Optional[builtins.str]:
        '''The name of the analyzer.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "analyzerName"))

    @analyzer_name.setter
    def analyzer_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f49c019c0256461aaf3c1e401ec662652b0851ed050ba88de78bf16d1886d0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "analyzerName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="archiveRules")
    def archive_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.ArchiveRuleProperty"]]]]:
        '''Specifies the archive rules to add for the analyzer.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.ArchiveRuleProperty"]]]], jsii.get(self, "archiveRules"))

    @archive_rules.setter
    def archive_rules(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.ArchiveRuleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6e8df0db0833319fd0b7c019964ba2ec4f399928538e323239bc668cacd0434)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archiveRules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the analyzer.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a60563761f5e2faa4dde6d3c0daa593ac20d10acf23bf72fc62050810a7b3e48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_accessanalyzer.CfnAnalyzer.AnalysisRuleCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={"account_ids": "accountIds", "resource_tags": "resourceTags"},
    )
    class AnalysisRuleCriteriaProperty:
        def __init__(
            self,
            *,
            account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]]]] = None,
        ) -> None:
            '''The criteria for an analysis rule for an analyzer.

            The criteria determine which entities will generate findings.

            :param account_ids: A list of AWS account IDs to apply to the analysis rule criteria. The accounts cannot include the organization analyzer owner account. Account IDs can only be applied to the analysis rule criteria for organization-level analyzers. The list cannot include more than 2,000 account IDs.
            :param resource_tags: An array of key-value pairs to match for your resources. You can use the set of Unicode letters, digits, whitespace, ``_`` , ``.`` , ``/`` , ``=`` , ``+`` , and ``-`` . For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with ``aws:`` . For the tag value, you can specify a value that is 0 to 256 characters in length. If the specified tag value is 0 characters, the rule is applied to all principals with the specified tag key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-analysisrulecriteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_accessanalyzer as accessanalyzer
                
                analysis_rule_criteria_property = accessanalyzer.CfnAnalyzer.AnalysisRuleCriteriaProperty(
                    account_ids=["accountIds"],
                    resource_tags=[[CfnTag(
                        key="key",
                        value="value"
                    )]]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36c3b122854545155d3943e2cf1f8f001f347b0db4e3b0e61e5562d5c4418440)
                check_type(argname="argument account_ids", value=account_ids, expected_type=type_hints["account_ids"])
                check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if account_ids is not None:
                self._values["account_ids"] = account_ids
            if resource_tags is not None:
                self._values["resource_tags"] = resource_tags

        @builtins.property
        def account_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of AWS account IDs to apply to the analysis rule criteria.

            The accounts cannot include the organization analyzer owner account. Account IDs can only be applied to the analysis rule criteria for organization-level analyzers. The list cannot include more than 2,000 account IDs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-analysisrulecriteria.html#cfn-accessanalyzer-analyzer-analysisrulecriteria-accountids
            '''
            result = self._values.get("account_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def resource_tags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]]]:
            '''An array of key-value pairs to match for your resources.

            You can use the set of Unicode letters, digits, whitespace, ``_`` , ``.`` , ``/`` , ``=`` , ``+`` , and ``-`` .

            For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with ``aws:`` .

            For the tag value, you can specify a value that is 0 to 256 characters in length. If the specified tag value is 0 characters, the rule is applied to all principals with the specified tag key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-analysisrulecriteria.html#cfn-accessanalyzer-analyzer-analysisrulecriteria-resourcetags
            '''
            result = self._values.get("resource_tags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisRuleCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_accessanalyzer.CfnAnalyzer.AnalysisRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"exclusions": "exclusions"},
    )
    class AnalysisRuleProperty:
        def __init__(
            self,
            *,
            exclusions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalyzer.AnalysisRuleCriteriaProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Contains information about analysis rules for the analyzer.

            Analysis rules determine which entities will generate findings based on the criteria you define when you create the rule.

            :param exclusions: A list of rules for the analyzer containing criteria to exclude from analysis. Entities that meet the rule criteria will not generate findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-analysisrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_accessanalyzer as accessanalyzer
                
                analysis_rule_property = accessanalyzer.CfnAnalyzer.AnalysisRuleProperty(
                    exclusions=[accessanalyzer.CfnAnalyzer.AnalysisRuleCriteriaProperty(
                        account_ids=["accountIds"],
                        resource_tags=[[CfnTag(
                            key="key",
                            value="value"
                        )]]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__17edc274e7f0852c4514c56018aaea9d25296dab4aaadab463eab14602e93887)
                check_type(argname="argument exclusions", value=exclusions, expected_type=type_hints["exclusions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if exclusions is not None:
                self._values["exclusions"] = exclusions

        @builtins.property
        def exclusions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.AnalysisRuleCriteriaProperty"]]]]:
            '''A list of rules for the analyzer containing criteria to exclude from analysis.

            Entities that meet the rule criteria will not generate findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-analysisrule.html#cfn-accessanalyzer-analyzer-analysisrule-exclusions
            '''
            result = self._values.get("exclusions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.AnalysisRuleCriteriaProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalysisRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_accessanalyzer.CfnAnalyzer.AnalyzerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "internal_access_configuration": "internalAccessConfiguration",
            "unused_access_configuration": "unusedAccessConfiguration",
        },
    )
    class AnalyzerConfigurationProperty:
        def __init__(
            self,
            *,
            internal_access_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalyzer.InternalAccessConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            unused_access_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalyzer.UnusedAccessConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about the configuration of an analyzer for an AWS organization or account.

            :param internal_access_configuration: Specifies the configuration of an internal access analyzer for an AWS organization or account. This configuration determines how the analyzer evaluates access within your AWS environment.
            :param unused_access_configuration: Specifies the configuration of an unused access analyzer for an AWS organization or account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-analyzerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_accessanalyzer as accessanalyzer
                
                analyzer_configuration_property = accessanalyzer.CfnAnalyzer.AnalyzerConfigurationProperty(
                    internal_access_configuration=accessanalyzer.CfnAnalyzer.InternalAccessConfigurationProperty(
                        internal_access_analysis_rule=accessanalyzer.CfnAnalyzer.InternalAccessAnalysisRuleProperty(
                            inclusions=[accessanalyzer.CfnAnalyzer.InternalAccessAnalysisRuleCriteriaProperty(
                                account_ids=["accountIds"],
                                resource_arns=["resourceArns"],
                                resource_types=["resourceTypes"]
                            )]
                        )
                    ),
                    unused_access_configuration=accessanalyzer.CfnAnalyzer.UnusedAccessConfigurationProperty(
                        analysis_rule=accessanalyzer.CfnAnalyzer.AnalysisRuleProperty(
                            exclusions=[accessanalyzer.CfnAnalyzer.AnalysisRuleCriteriaProperty(
                                account_ids=["accountIds"],
                                resource_tags=[[CfnTag(
                                    key="key",
                                    value="value"
                                )]]
                            )]
                        ),
                        unused_access_age=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__31c56409583b90336517d4c07b7b7849a386335199a589eff293943ed3b54e61)
                check_type(argname="argument internal_access_configuration", value=internal_access_configuration, expected_type=type_hints["internal_access_configuration"])
                check_type(argname="argument unused_access_configuration", value=unused_access_configuration, expected_type=type_hints["unused_access_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if internal_access_configuration is not None:
                self._values["internal_access_configuration"] = internal_access_configuration
            if unused_access_configuration is not None:
                self._values["unused_access_configuration"] = unused_access_configuration

        @builtins.property
        def internal_access_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.InternalAccessConfigurationProperty"]]:
            '''Specifies the configuration of an internal access analyzer for an AWS organization or account.

            This configuration determines how the analyzer evaluates access within your AWS environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-analyzerconfiguration.html#cfn-accessanalyzer-analyzer-analyzerconfiguration-internalaccessconfiguration
            '''
            result = self._values.get("internal_access_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.InternalAccessConfigurationProperty"]], result)

        @builtins.property
        def unused_access_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.UnusedAccessConfigurationProperty"]]:
            '''Specifies the configuration of an unused access analyzer for an AWS organization or account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-analyzerconfiguration.html#cfn-accessanalyzer-analyzer-analyzerconfiguration-unusedaccessconfiguration
            '''
            result = self._values.get("unused_access_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.UnusedAccessConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnalyzerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_accessanalyzer.CfnAnalyzer.ArchiveRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"filter": "filter", "rule_name": "ruleName"},
    )
    class ArchiveRuleProperty:
        def __init__(
            self,
            *,
            filter: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalyzer.FilterProperty", typing.Dict[builtins.str, typing.Any]]]]],
            rule_name: builtins.str,
        ) -> None:
            '''Contains information about an archive rule.

            Archive rules automatically archive new findings that meet the criteria you define when you create the rule.

            :param filter: The criteria for the rule.
            :param rule_name: The name of the rule to create.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_accessanalyzer as accessanalyzer
                
                archive_rule_property = accessanalyzer.CfnAnalyzer.ArchiveRuleProperty(
                    filter=[accessanalyzer.CfnAnalyzer.FilterProperty(
                        property="property",
                
                        # the properties below are optional
                        contains=["contains"],
                        eq=["eq"],
                        exists=False,
                        neq=["neq"]
                    )],
                    rule_name="ruleName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__00f4155e4f1585786ae6a8e164d5eede38f79d223d8918b08f56f012e2ced7ed)
                check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
                check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "filter": filter,
                "rule_name": rule_name,
            }

        @builtins.property
        def filter(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.FilterProperty"]]]:
            '''The criteria for the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html#cfn-accessanalyzer-analyzer-archiverule-filter
            '''
            result = self._values.get("filter")
            assert result is not None, "Required property 'filter' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.FilterProperty"]]], result)

        @builtins.property
        def rule_name(self) -> builtins.str:
            '''The name of the rule to create.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html#cfn-accessanalyzer-analyzer-archiverule-rulename
            '''
            result = self._values.get("rule_name")
            assert result is not None, "Required property 'rule_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArchiveRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_accessanalyzer.CfnAnalyzer.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "property": "property",
            "contains": "contains",
            "eq": "eq",
            "exists": "exists",
            "neq": "neq",
        },
    )
    class FilterProperty:
        def __init__(
            self,
            *,
            property: builtins.str,
            contains: typing.Optional[typing.Sequence[builtins.str]] = None,
            eq: typing.Optional[typing.Sequence[builtins.str]] = None,
            exists: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            neq: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The criteria that defines the archive rule.

            To learn about filter keys that you can use to create an archive rule, see `filter keys <https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html>`_ in the *User Guide* .

            :param property: The property used to define the criteria in the filter for the rule.
            :param contains: A "contains" condition to match for the rule.
            :param eq: An "equals" condition to match for the rule.
            :param exists: An "exists" condition to match for the rule.
            :param neq: A "not equal" condition to match for the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_accessanalyzer as accessanalyzer
                
                filter_property = accessanalyzer.CfnAnalyzer.FilterProperty(
                    property="property",
                
                    # the properties below are optional
                    contains=["contains"],
                    eq=["eq"],
                    exists=False,
                    neq=["neq"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a277539f2c67c28a2a9fc67270fd81239b1346785d9508df320b963a25eb1e3a)
                check_type(argname="argument property", value=property, expected_type=type_hints["property"])
                check_type(argname="argument contains", value=contains, expected_type=type_hints["contains"])
                check_type(argname="argument eq", value=eq, expected_type=type_hints["eq"])
                check_type(argname="argument exists", value=exists, expected_type=type_hints["exists"])
                check_type(argname="argument neq", value=neq, expected_type=type_hints["neq"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "property": property,
            }
            if contains is not None:
                self._values["contains"] = contains
            if eq is not None:
                self._values["eq"] = eq
            if exists is not None:
                self._values["exists"] = exists
            if neq is not None:
                self._values["neq"] = neq

        @builtins.property
        def property(self) -> builtins.str:
            '''The property used to define the criteria in the filter for the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-property
            '''
            result = self._values.get("property")
            assert result is not None, "Required property 'property' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def contains(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A "contains" condition to match for the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-contains
            '''
            result = self._values.get("contains")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def eq(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An "equals" condition to match for the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-eq
            '''
            result = self._values.get("eq")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def exists(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''An "exists" condition to match for the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-exists
            '''
            result = self._values.get("exists")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def neq(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A "not equal" condition to match for the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-neq
            '''
            result = self._values.get("neq")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_accessanalyzer.CfnAnalyzer.InternalAccessAnalysisRuleCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_ids": "accountIds",
            "resource_arns": "resourceArns",
            "resource_types": "resourceTypes",
        },
    )
    class InternalAccessAnalysisRuleCriteriaProperty:
        def __init__(
            self,
            *,
            account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The criteria for an analysis rule for an internal access analyzer.

            :param account_ids: A list of AWS account IDs to apply to the internal access analysis rule criteria. Account IDs can only be applied to the analysis rule criteria for organization-level analyzers.
            :param resource_arns: A list of resource ARNs to apply to the internal access analysis rule criteria. The analyzer will only generate findings for resources that match these ARNs.
            :param resource_types: A list of resource types to apply to the internal access analysis rule criteria. The analyzer will only generate findings for resources of these types. These resource types are currently supported for internal access analyzers: - ``AWS::S3::Bucket`` - ``AWS::RDS::DBSnapshot`` - ``AWS::RDS::DBClusterSnapshot`` - ``AWS::S3Express::DirectoryBucket`` - ``AWS::DynamoDB::Table`` - ``AWS::DynamoDB::Stream``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-internalaccessanalysisrulecriteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_accessanalyzer as accessanalyzer
                
                internal_access_analysis_rule_criteria_property = accessanalyzer.CfnAnalyzer.InternalAccessAnalysisRuleCriteriaProperty(
                    account_ids=["accountIds"],
                    resource_arns=["resourceArns"],
                    resource_types=["resourceTypes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__df58106489755d92b5cc9d51d8ac254dfccee65f0ca7f4d03d3a9002659d6a9f)
                check_type(argname="argument account_ids", value=account_ids, expected_type=type_hints["account_ids"])
                check_type(argname="argument resource_arns", value=resource_arns, expected_type=type_hints["resource_arns"])
                check_type(argname="argument resource_types", value=resource_types, expected_type=type_hints["resource_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if account_ids is not None:
                self._values["account_ids"] = account_ids
            if resource_arns is not None:
                self._values["resource_arns"] = resource_arns
            if resource_types is not None:
                self._values["resource_types"] = resource_types

        @builtins.property
        def account_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of AWS account IDs to apply to the internal access analysis rule criteria.

            Account IDs can only be applied to the analysis rule criteria for organization-level analyzers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-internalaccessanalysisrulecriteria.html#cfn-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-accountids
            '''
            result = self._values.get("account_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def resource_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of resource ARNs to apply to the internal access analysis rule criteria.

            The analyzer will only generate findings for resources that match these ARNs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-internalaccessanalysisrulecriteria.html#cfn-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-resourcearns
            '''
            result = self._values.get("resource_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def resource_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of resource types to apply to the internal access analysis rule criteria.

            The analyzer will only generate findings for resources of these types. These resource types are currently supported for internal access analyzers:

            - ``AWS::S3::Bucket``
            - ``AWS::RDS::DBSnapshot``
            - ``AWS::RDS::DBClusterSnapshot``
            - ``AWS::S3Express::DirectoryBucket``
            - ``AWS::DynamoDB::Table``
            - ``AWS::DynamoDB::Stream``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-internalaccessanalysisrulecriteria.html#cfn-accessanalyzer-analyzer-internalaccessanalysisrulecriteria-resourcetypes
            '''
            result = self._values.get("resource_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InternalAccessAnalysisRuleCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_accessanalyzer.CfnAnalyzer.InternalAccessAnalysisRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"inclusions": "inclusions"},
    )
    class InternalAccessAnalysisRuleProperty:
        def __init__(
            self,
            *,
            inclusions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalyzer.InternalAccessAnalysisRuleCriteriaProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Contains information about analysis rules for the internal access analyzer.

            Analysis rules determine which entities will generate findings based on the criteria you define when you create the rule.

            :param inclusions: A list of rules for the internal access analyzer containing criteria to include in analysis. Only resources that meet the rule criteria will generate findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-internalaccessanalysisrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_accessanalyzer as accessanalyzer
                
                internal_access_analysis_rule_property = accessanalyzer.CfnAnalyzer.InternalAccessAnalysisRuleProperty(
                    inclusions=[accessanalyzer.CfnAnalyzer.InternalAccessAnalysisRuleCriteriaProperty(
                        account_ids=["accountIds"],
                        resource_arns=["resourceArns"],
                        resource_types=["resourceTypes"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b551cb53f4f7a1a38a9a57f1445115d565b843fa07c255e6ae31333c89b019a7)
                check_type(argname="argument inclusions", value=inclusions, expected_type=type_hints["inclusions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if inclusions is not None:
                self._values["inclusions"] = inclusions

        @builtins.property
        def inclusions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.InternalAccessAnalysisRuleCriteriaProperty"]]]]:
            '''A list of rules for the internal access analyzer containing criteria to include in analysis.

            Only resources that meet the rule criteria will generate findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-internalaccessanalysisrule.html#cfn-accessanalyzer-analyzer-internalaccessanalysisrule-inclusions
            '''
            result = self._values.get("inclusions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.InternalAccessAnalysisRuleCriteriaProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InternalAccessAnalysisRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_accessanalyzer.CfnAnalyzer.InternalAccessConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"internal_access_analysis_rule": "internalAccessAnalysisRule"},
    )
    class InternalAccessConfigurationProperty:
        def __init__(
            self,
            *,
            internal_access_analysis_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalyzer.InternalAccessAnalysisRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the configuration of an internal access analyzer for an AWS organization or account.

            This configuration determines how the analyzer evaluates internal access within your AWS environment.

            :param internal_access_analysis_rule: Contains information about analysis rules for the internal access analyzer. These rules determine which resources and access patterns will be analyzed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-internalaccessconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_accessanalyzer as accessanalyzer
                
                internal_access_configuration_property = accessanalyzer.CfnAnalyzer.InternalAccessConfigurationProperty(
                    internal_access_analysis_rule=accessanalyzer.CfnAnalyzer.InternalAccessAnalysisRuleProperty(
                        inclusions=[accessanalyzer.CfnAnalyzer.InternalAccessAnalysisRuleCriteriaProperty(
                            account_ids=["accountIds"],
                            resource_arns=["resourceArns"],
                            resource_types=["resourceTypes"]
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0a796d008592c4cc4b9ffe7a696b2a26db99022fdab61d5695cf9465c2e2ecff)
                check_type(argname="argument internal_access_analysis_rule", value=internal_access_analysis_rule, expected_type=type_hints["internal_access_analysis_rule"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if internal_access_analysis_rule is not None:
                self._values["internal_access_analysis_rule"] = internal_access_analysis_rule

        @builtins.property
        def internal_access_analysis_rule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.InternalAccessAnalysisRuleProperty"]]:
            '''Contains information about analysis rules for the internal access analyzer.

            These rules determine which resources and access patterns will be analyzed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-internalaccessconfiguration.html#cfn-accessanalyzer-analyzer-internalaccessconfiguration-internalaccessanalysisrule
            '''
            result = self._values.get("internal_access_analysis_rule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.InternalAccessAnalysisRuleProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InternalAccessConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_accessanalyzer.CfnAnalyzer.UnusedAccessConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "analysis_rule": "analysisRule",
            "unused_access_age": "unusedAccessAge",
        },
    )
    class UnusedAccessConfigurationProperty:
        def __init__(
            self,
            *,
            analysis_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnalyzer.AnalysisRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            unused_access_age: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Contains information about an unused access analyzer.

            :param analysis_rule: Contains information about analysis rules for the analyzer. Analysis rules determine which entities will generate findings based on the criteria you define when you create the rule.
            :param unused_access_age: The specified access age in days for which to generate findings for unused access. For example, if you specify 90 days, the analyzer will generate findings for IAM entities within the accounts of the selected organization for any access that hasn't been used in 90 or more days since the analyzer's last scan. You can choose a value between 1 and 365 days.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-unusedaccessconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_accessanalyzer as accessanalyzer
                
                unused_access_configuration_property = accessanalyzer.CfnAnalyzer.UnusedAccessConfigurationProperty(
                    analysis_rule=accessanalyzer.CfnAnalyzer.AnalysisRuleProperty(
                        exclusions=[accessanalyzer.CfnAnalyzer.AnalysisRuleCriteriaProperty(
                            account_ids=["accountIds"],
                            resource_tags=[[CfnTag(
                                key="key",
                                value="value"
                            )]]
                        )]
                    ),
                    unused_access_age=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b15bc1bfb223a199dc73f744cc56dfec8d77e91fcae9e8e5b3520484a497aba7)
                check_type(argname="argument analysis_rule", value=analysis_rule, expected_type=type_hints["analysis_rule"])
                check_type(argname="argument unused_access_age", value=unused_access_age, expected_type=type_hints["unused_access_age"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if analysis_rule is not None:
                self._values["analysis_rule"] = analysis_rule
            if unused_access_age is not None:
                self._values["unused_access_age"] = unused_access_age

        @builtins.property
        def analysis_rule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.AnalysisRuleProperty"]]:
            '''Contains information about analysis rules for the analyzer.

            Analysis rules determine which entities will generate findings based on the criteria you define when you create the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-unusedaccessconfiguration.html#cfn-accessanalyzer-analyzer-unusedaccessconfiguration-analysisrule
            '''
            result = self._values.get("analysis_rule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnalyzer.AnalysisRuleProperty"]], result)

        @builtins.property
        def unused_access_age(self) -> typing.Optional[jsii.Number]:
            '''The specified access age in days for which to generate findings for unused access.

            For example, if you specify 90 days, the analyzer will generate findings for IAM entities within the accounts of the selected organization for any access that hasn't been used in 90 or more days since the analyzer's last scan. You can choose a value between 1 and 365 days.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-unusedaccessconfiguration.html#cfn-accessanalyzer-analyzer-unusedaccessconfiguration-unusedaccessage
            '''
            result = self._values.get("unused_access_age")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UnusedAccessConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_accessanalyzer.CfnAnalyzerProps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "analyzer_configuration": "analyzerConfiguration",
        "analyzer_name": "analyzerName",
        "archive_rules": "archiveRules",
        "tags": "tags",
    },
)
class CfnAnalyzerProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        analyzer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalyzer.AnalyzerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        analyzer_name: typing.Optional[builtins.str] = None,
        archive_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalyzer.ArchiveRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAnalyzer``.

        :param type: The type represents the zone of trust for the analyzer. *Allowed Values* : ACCOUNT | ORGANIZATION | ACCOUNT_UNUSED_ACCESS | ACCOUNT_INTERNAL_ACCESS | ORGANIZATION_INTERNAL_ACCESS | ORGANIZATION_UNUSED_ACCESS
        :param analyzer_configuration: Contains information about the configuration of an analyzer for an AWS organization or account.
        :param analyzer_name: The name of the analyzer.
        :param archive_rules: Specifies the archive rules to add for the analyzer. Archive rules automatically archive findings that meet the criteria you define for the rule.
        :param tags: An array of key-value pairs to apply to the analyzer. You can use the set of Unicode letters, digits, whitespace, ``_`` , ``.`` , ``/`` , ``=`` , ``+`` , and ``-`` . For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with ``aws:`` . For the tag value, you can specify a value that is 0 to 256 characters in length.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_accessanalyzer as accessanalyzer
            
            cfn_analyzer_props = accessanalyzer.CfnAnalyzerProps(
                type="type",
            
                # the properties below are optional
                analyzer_configuration=accessanalyzer.CfnAnalyzer.AnalyzerConfigurationProperty(
                    internal_access_configuration=accessanalyzer.CfnAnalyzer.InternalAccessConfigurationProperty(
                        internal_access_analysis_rule=accessanalyzer.CfnAnalyzer.InternalAccessAnalysisRuleProperty(
                            inclusions=[accessanalyzer.CfnAnalyzer.InternalAccessAnalysisRuleCriteriaProperty(
                                account_ids=["accountIds"],
                                resource_arns=["resourceArns"],
                                resource_types=["resourceTypes"]
                            )]
                        )
                    ),
                    unused_access_configuration=accessanalyzer.CfnAnalyzer.UnusedAccessConfigurationProperty(
                        analysis_rule=accessanalyzer.CfnAnalyzer.AnalysisRuleProperty(
                            exclusions=[accessanalyzer.CfnAnalyzer.AnalysisRuleCriteriaProperty(
                                account_ids=["accountIds"],
                                resource_tags=[[CfnTag(
                                    key="key",
                                    value="value"
                                )]]
                            )]
                        ),
                        unused_access_age=123
                    )
                ),
                analyzer_name="analyzerName",
                archive_rules=[accessanalyzer.CfnAnalyzer.ArchiveRuleProperty(
                    filter=[accessanalyzer.CfnAnalyzer.FilterProperty(
                        property="property",
            
                        # the properties below are optional
                        contains=["contains"],
                        eq=["eq"],
                        exists=False,
                        neq=["neq"]
                    )],
                    rule_name="ruleName"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d178159df606ae35bc43e8f369c7f3f27d01795dcec5d3d6824e97919c0e7f83)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument analyzer_configuration", value=analyzer_configuration, expected_type=type_hints["analyzer_configuration"])
            check_type(argname="argument analyzer_name", value=analyzer_name, expected_type=type_hints["analyzer_name"])
            check_type(argname="argument archive_rules", value=archive_rules, expected_type=type_hints["archive_rules"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if analyzer_configuration is not None:
            self._values["analyzer_configuration"] = analyzer_configuration
        if analyzer_name is not None:
            self._values["analyzer_name"] = analyzer_name
        if archive_rules is not None:
            self._values["archive_rules"] = archive_rules
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def type(self) -> builtins.str:
        '''The type represents the zone of trust for the analyzer.

        *Allowed Values* : ACCOUNT | ORGANIZATION | ACCOUNT_UNUSED_ACCESS | ACCOUNT_INTERNAL_ACCESS | ORGANIZATION_INTERNAL_ACCESS | ORGANIZATION_UNUSED_ACCESS

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def analyzer_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnalyzer.AnalyzerConfigurationProperty]]:
        '''Contains information about the configuration of an analyzer for an AWS organization or account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-analyzerconfiguration
        '''
        result = self._values.get("analyzer_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnalyzer.AnalyzerConfigurationProperty]], result)

    @builtins.property
    def analyzer_name(self) -> typing.Optional[builtins.str]:
        '''The name of the analyzer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-analyzername
        '''
        result = self._values.get("analyzer_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def archive_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnalyzer.ArchiveRuleProperty]]]]:
        '''Specifies the archive rules to add for the analyzer.

        Archive rules automatically archive findings that meet the criteria you define for the rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-archiverules
        '''
        result = self._values.get("archive_rules")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnalyzer.ArchiveRuleProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to the analyzer.

        You can use the set of Unicode letters, digits, whitespace, ``_`` , ``.`` , ``/`` , ``=`` , ``+`` , and ``-`` .

        For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with ``aws:`` .

        For the tag value, you can specify a value that is 0 to 256 characters in length.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAnalyzerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAnalyzer",
    "CfnAnalyzerProps",
]

publication.publish()

def _typecheckingstub__4d078d0b17e4dff80691cd25737bc9c648722f68955725da002d3ab5d4df9b21(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    type: builtins.str,
    analyzer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalyzer.AnalyzerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    analyzer_name: typing.Optional[builtins.str] = None,
    archive_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalyzer.ArchiveRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a366b020d431b9e8e5d2ed8e3b287179b77a059bb9e4407de61c18f8bafea93(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b4a15c19694e0f2a4c59bffdc30147a3fd55610e77c34007676071a6a1cee74(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae0ebe072220649d8253f3011fe641bc781e24d2bbf9d9a1cc55fdf1fb9124cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b65a5d08bf50e1911863b6e4854f804654921017c34f668f95a5081f5c25b8c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnalyzer.AnalyzerConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f49c019c0256461aaf3c1e401ec662652b0851ed050ba88de78bf16d1886d0d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6e8df0db0833319fd0b7c019964ba2ec4f399928538e323239bc668cacd0434(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnalyzer.ArchiveRuleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a60563761f5e2faa4dde6d3c0daa593ac20d10acf23bf72fc62050810a7b3e48(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36c3b122854545155d3943e2cf1f8f001f347b0db4e3b0e61e5562d5c4418440(
    *,
    account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17edc274e7f0852c4514c56018aaea9d25296dab4aaadab463eab14602e93887(
    *,
    exclusions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalyzer.AnalysisRuleCriteriaProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31c56409583b90336517d4c07b7b7849a386335199a589eff293943ed3b54e61(
    *,
    internal_access_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalyzer.InternalAccessConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    unused_access_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalyzer.UnusedAccessConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00f4155e4f1585786ae6a8e164d5eede38f79d223d8918b08f56f012e2ced7ed(
    *,
    filter: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalyzer.FilterProperty, typing.Dict[builtins.str, typing.Any]]]]],
    rule_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a277539f2c67c28a2a9fc67270fd81239b1346785d9508df320b963a25eb1e3a(
    *,
    property: builtins.str,
    contains: typing.Optional[typing.Sequence[builtins.str]] = None,
    eq: typing.Optional[typing.Sequence[builtins.str]] = None,
    exists: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    neq: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df58106489755d92b5cc9d51d8ac254dfccee65f0ca7f4d03d3a9002659d6a9f(
    *,
    account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b551cb53f4f7a1a38a9a57f1445115d565b843fa07c255e6ae31333c89b019a7(
    *,
    inclusions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalyzer.InternalAccessAnalysisRuleCriteriaProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a796d008592c4cc4b9ffe7a696b2a26db99022fdab61d5695cf9465c2e2ecff(
    *,
    internal_access_analysis_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalyzer.InternalAccessAnalysisRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b15bc1bfb223a199dc73f744cc56dfec8d77e91fcae9e8e5b3520484a497aba7(
    *,
    analysis_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalyzer.AnalysisRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    unused_access_age: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d178159df606ae35bc43e8f369c7f3f27d01795dcec5d3d6824e97919c0e7f83(
    *,
    type: builtins.str,
    analyzer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalyzer.AnalyzerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    analyzer_name: typing.Optional[builtins.str] = None,
    archive_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnalyzer.ArchiveRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
