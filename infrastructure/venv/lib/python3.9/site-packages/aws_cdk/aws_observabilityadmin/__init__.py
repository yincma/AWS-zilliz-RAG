r'''
# AWS::ObservabilityAdmin Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_observabilityadmin as observabilityadmin
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ObservabilityAdmin construct libraries](https://constructs.dev/search?q=observabilityadmin)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ObservabilityAdmin resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ObservabilityAdmin.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ObservabilityAdmin](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ObservabilityAdmin.html).

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
class CfnOrganizationTelemetryRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule",
):
    '''The AWS::ObservabilityAdmin::OrganizationTelemetryRule resource defines a CloudWatch Observability Admin Organization Telemetry Rule.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationtelemetryrule.html
    :cloudformationResource: AWS::ObservabilityAdmin::OrganizationTelemetryRule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_observabilityadmin as observabilityadmin
        
        cfn_organization_telemetry_rule = observabilityadmin.CfnOrganizationTelemetryRule(self, "MyCfnOrganizationTelemetryRule",
            rule=observabilityadmin.CfnOrganizationTelemetryRule.TelemetryRuleProperty(
                resource_type="resourceType",
                telemetry_type="telemetryType",
        
                # the properties below are optional
                destination_configuration=observabilityadmin.CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty(
                    destination_pattern="destinationPattern",
                    destination_type="destinationType",
                    retention_in_days=123,
                    vpc_flow_log_parameters=observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty(
                        log_format="logFormat",
                        max_aggregation_interval=123,
                        traffic_type="trafficType"
                    )
                ),
                scope="scope",
                selection_criteria="selectionCriteria"
            ),
            rule_name="ruleName",
        
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
        rule: typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationTelemetryRule.TelemetryRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param rule: The telemetry rule.
        :param rule_name: The name of the organization telemetry rule.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a67d6a9dd82924a413b7d3435faeb8efa735048df0244b926e672def8c2d5f75)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOrganizationTelemetryRuleProps(
            rule=rule, rule_name=rule_name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cb893813673a29ee1f384593916d34bdcc440b816dfc54ad27097692c5a64e9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c809c768027da00df4018694393faf5d77af9754b12923bf684ada119faecfc7)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleArn")
    def attr_rule_arn(self) -> builtins.str:
        '''The arn of the organization telemetry rule.

        :cloudformationAttribute: RuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleArn"))

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
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.TelemetryRuleProperty"]:
        '''The telemetry rule.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.TelemetryRuleProperty"], jsii.get(self, "rule"))

    @rule.setter
    def rule(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.TelemetryRuleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97cf84910a3c46b94c3e90ddf73c07b304a029e413bebd1b7c5e7b2bbe5cd411)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> builtins.str:
        '''The name of the organization telemetry rule.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84099afcf940dd46614099ecc03e181396a6d202813d1517bd79414c5aa2f5ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d494e45ec3f03fbc2168c2e374f689615e98524c832aa6247ad243fabe01ffe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_pattern": "destinationPattern",
            "destination_type": "destinationType",
            "retention_in_days": "retentionInDays",
            "vpc_flow_log_parameters": "vpcFlowLogParameters",
        },
    )
    class TelemetryDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            destination_pattern: typing.Optional[builtins.str] = None,
            destination_type: typing.Optional[builtins.str] = None,
            retention_in_days: typing.Optional[jsii.Number] = None,
            vpc_flow_log_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The destination configuration for telemetry data.

            :param destination_pattern: Pattern for telemetry data destination.
            :param destination_type: Type of telemetry destination.
            :param retention_in_days: Number of days to retain the telemetry data in the specified destination.
            :param vpc_flow_log_parameters: Telemetry parameters for VPC Flow logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                telemetry_destination_configuration_property = observabilityadmin.CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty(
                    destination_pattern="destinationPattern",
                    destination_type="destinationType",
                    retention_in_days=123,
                    vpc_flow_log_parameters=observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty(
                        log_format="logFormat",
                        max_aggregation_interval=123,
                        traffic_type="trafficType"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36b4168c57b4555036ca598e8299a36985c9aab7a1eb6b84357df4454b340171)
                check_type(argname="argument destination_pattern", value=destination_pattern, expected_type=type_hints["destination_pattern"])
                check_type(argname="argument destination_type", value=destination_type, expected_type=type_hints["destination_type"])
                check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
                check_type(argname="argument vpc_flow_log_parameters", value=vpc_flow_log_parameters, expected_type=type_hints["vpc_flow_log_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_pattern is not None:
                self._values["destination_pattern"] = destination_pattern
            if destination_type is not None:
                self._values["destination_type"] = destination_type
            if retention_in_days is not None:
                self._values["retention_in_days"] = retention_in_days
            if vpc_flow_log_parameters is not None:
                self._values["vpc_flow_log_parameters"] = vpc_flow_log_parameters

        @builtins.property
        def destination_pattern(self) -> typing.Optional[builtins.str]:
            '''Pattern for telemetry data destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration-destinationpattern
            '''
            result = self._values.get("destination_pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def destination_type(self) -> typing.Optional[builtins.str]:
            '''Type of telemetry destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration-destinationtype
            '''
            result = self._values.get("destination_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def retention_in_days(self) -> typing.Optional[jsii.Number]:
            '''Number of days to retain the telemetry data in the specified destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration-retentionindays
            '''
            result = self._values.get("retention_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def vpc_flow_log_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty"]]:
            '''Telemetry parameters for VPC Flow logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration-vpcflowlogparameters
            '''
            result = self._values.get("vpc_flow_log_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelemetryDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.TelemetryRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resource_type": "resourceType",
            "telemetry_type": "telemetryType",
            "destination_configuration": "destinationConfiguration",
            "scope": "scope",
            "selection_criteria": "selectionCriteria",
        },
    )
    class TelemetryRuleProperty:
        def __init__(
            self,
            *,
            resource_type: builtins.str,
            telemetry_type: builtins.str,
            destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            scope: typing.Optional[builtins.str] = None,
            selection_criteria: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The telemetry rule.

            :param resource_type: Resource Type associated with the Organization Telemetry Rule.
            :param telemetry_type: Telemetry Type associated with the Organization Telemetry Rule.
            :param destination_configuration: The destination configuration for telemetry data.
            :param scope: Selection Criteria on scope level for rule application.
            :param selection_criteria: Selection Criteria on resource level for rule application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                telemetry_rule_property = observabilityadmin.CfnOrganizationTelemetryRule.TelemetryRuleProperty(
                    resource_type="resourceType",
                    telemetry_type="telemetryType",
                
                    # the properties below are optional
                    destination_configuration=observabilityadmin.CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty(
                        destination_pattern="destinationPattern",
                        destination_type="destinationType",
                        retention_in_days=123,
                        vpc_flow_log_parameters=observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty(
                            log_format="logFormat",
                            max_aggregation_interval=123,
                            traffic_type="trafficType"
                        )
                    ),
                    scope="scope",
                    selection_criteria="selectionCriteria"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8febf24ebcbc00029972152d874df5e847a9f5cd45e05abb26e69f7a2cabc5bf)
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
                check_type(argname="argument telemetry_type", value=telemetry_type, expected_type=type_hints["telemetry_type"])
                check_type(argname="argument destination_configuration", value=destination_configuration, expected_type=type_hints["destination_configuration"])
                check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
                check_type(argname="argument selection_criteria", value=selection_criteria, expected_type=type_hints["selection_criteria"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_type": resource_type,
                "telemetry_type": telemetry_type,
            }
            if destination_configuration is not None:
                self._values["destination_configuration"] = destination_configuration
            if scope is not None:
                self._values["scope"] = scope
            if selection_criteria is not None:
                self._values["selection_criteria"] = selection_criteria

        @builtins.property
        def resource_type(self) -> builtins.str:
            '''Resource Type associated with the Organization Telemetry Rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-resourcetype
            '''
            result = self._values.get("resource_type")
            assert result is not None, "Required property 'resource_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def telemetry_type(self) -> builtins.str:
            '''Telemetry Type associated with the Organization Telemetry Rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-telemetrytype
            '''
            result = self._values.get("telemetry_type")
            assert result is not None, "Required property 'telemetry_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty"]]:
            '''The destination configuration for telemetry data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-destinationconfiguration
            '''
            result = self._values.get("destination_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty"]], result)

        @builtins.property
        def scope(self) -> typing.Optional[builtins.str]:
            '''Selection Criteria on scope level for rule application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-scope
            '''
            result = self._values.get("scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def selection_criteria(self) -> typing.Optional[builtins.str]:
            '''Selection Criteria on resource level for rule application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-selectioncriteria
            '''
            result = self._values.get("selection_criteria")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelemetryRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_format": "logFormat",
            "max_aggregation_interval": "maxAggregationInterval",
            "traffic_type": "trafficType",
        },
    )
    class VPCFlowLogParametersProperty:
        def __init__(
            self,
            *,
            log_format: typing.Optional[builtins.str] = None,
            max_aggregation_interval: typing.Optional[jsii.Number] = None,
            traffic_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Telemetry parameters for VPC Flow logs.

            :param log_format: The fields to include in the flow log record. If you omit this parameter, the flow log is created using the default format.
            :param max_aggregation_interval: The maximum interval of time, in seconds, during which a flow of packets is captured and aggregated into a flow log record. Default is 600s.
            :param traffic_type: The type of traffic captured for the flow log. Default is ALL

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                v_pCFlow_log_parameters_property = observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty(
                    log_format="logFormat",
                    max_aggregation_interval=123,
                    traffic_type="trafficType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__945b01222f6573dfd9bd365335b34de4d056db844b2fe9ffa6c9d40371eaff6e)
                check_type(argname="argument log_format", value=log_format, expected_type=type_hints["log_format"])
                check_type(argname="argument max_aggregation_interval", value=max_aggregation_interval, expected_type=type_hints["max_aggregation_interval"])
                check_type(argname="argument traffic_type", value=traffic_type, expected_type=type_hints["traffic_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_format is not None:
                self._values["log_format"] = log_format
            if max_aggregation_interval is not None:
                self._values["max_aggregation_interval"] = max_aggregation_interval
            if traffic_type is not None:
                self._values["traffic_type"] = traffic_type

        @builtins.property
        def log_format(self) -> typing.Optional[builtins.str]:
            '''The fields to include in the flow log record.

            If you omit this parameter, the flow log is created using the default format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-logformat
            '''
            result = self._values.get("log_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_aggregation_interval(self) -> typing.Optional[jsii.Number]:
            '''The maximum interval of time, in seconds, during which a flow of packets is captured and aggregated into a flow log record.

            Default is 600s.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-maxaggregationinterval
            '''
            result = self._values.get("max_aggregation_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def traffic_type(self) -> typing.Optional[builtins.str]:
            '''The type of traffic captured for the flow log.

            Default is ALL

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-traffictype
            '''
            result = self._values.get("traffic_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VPCFlowLogParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRuleProps",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "rule_name": "ruleName", "tags": "tags"},
)
class CfnOrganizationTelemetryRuleProps:
    def __init__(
        self,
        *,
        rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.TelemetryRuleProperty, typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOrganizationTelemetryRule``.

        :param rule: The telemetry rule.
        :param rule_name: The name of the organization telemetry rule.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationtelemetryrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_observabilityadmin as observabilityadmin
            
            cfn_organization_telemetry_rule_props = observabilityadmin.CfnOrganizationTelemetryRuleProps(
                rule=observabilityadmin.CfnOrganizationTelemetryRule.TelemetryRuleProperty(
                    resource_type="resourceType",
                    telemetry_type="telemetryType",
            
                    # the properties below are optional
                    destination_configuration=observabilityadmin.CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty(
                        destination_pattern="destinationPattern",
                        destination_type="destinationType",
                        retention_in_days=123,
                        vpc_flow_log_parameters=observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty(
                            log_format="logFormat",
                            max_aggregation_interval=123,
                            traffic_type="trafficType"
                        )
                    ),
                    scope="scope",
                    selection_criteria="selectionCriteria"
                ),
                rule_name="ruleName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45c94381428dd096d5bd5b31c1a78b0ec6c66b125c46a889f389e957dbf9f76b)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
            "rule_name": rule_name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnOrganizationTelemetryRule.TelemetryRuleProperty]:
        '''The telemetry rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationtelemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-rule
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnOrganizationTelemetryRule.TelemetryRuleProperty], result)

    @builtins.property
    def rule_name(self) -> builtins.str:
        '''The name of the organization telemetry rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationtelemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-rulename
        '''
        result = self._values.get("rule_name")
        assert result is not None, "Required property 'rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationtelemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOrganizationTelemetryRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnTelemetryRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule",
):
    '''The AWS::ObservabilityAdmin::TelemetryRule resource defines a CloudWatch Observability Admin Telemetry Rule.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetryrule.html
    :cloudformationResource: AWS::ObservabilityAdmin::TelemetryRule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_observabilityadmin as observabilityadmin
        
        cfn_telemetry_rule = observabilityadmin.CfnTelemetryRule(self, "MyCfnTelemetryRule",
            rule=observabilityadmin.CfnTelemetryRule.TelemetryRuleProperty(
                resource_type="resourceType",
                telemetry_type="telemetryType",
        
                # the properties below are optional
                destination_configuration=observabilityadmin.CfnTelemetryRule.TelemetryDestinationConfigurationProperty(
                    destination_pattern="destinationPattern",
                    destination_type="destinationType",
                    retention_in_days=123,
                    vpc_flow_log_parameters=observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty(
                        log_format="logFormat",
                        max_aggregation_interval=123,
                        traffic_type="trafficType"
                    )
                ),
                selection_criteria="selectionCriteria"
            ),
            rule_name="ruleName",
        
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
        rule: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTelemetryRule.TelemetryRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param rule: The telemetry rule.
        :param rule_name: The name of the telemetry rule.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cb28d06ef60815f8488b771b64aca8e3671a315a3f6676ad80a414dcd296224)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTelemetryRuleProps(rule=rule, rule_name=rule_name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c971c1c4e8e03d4140674a22f18490c0a14f143dab5c9b15a801d0e69e908b92)
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
            type_hints = typing.get_type_hints(_typecheckingstub__adf48e055c256d6f5cb987ba3921807e211a303c3d38be6a02b6932f52a739fe)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleArn")
    def attr_rule_arn(self) -> builtins.str:
        '''The arn of the telemetry rule.

        :cloudformationAttribute: RuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleArn"))

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
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.TelemetryRuleProperty"]:
        '''The telemetry rule.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.TelemetryRuleProperty"], jsii.get(self, "rule"))

    @rule.setter
    def rule(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.TelemetryRuleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__253115d76ca17e48e13df2aa679666bb12581680b457a45a7743f6a80d6dbfa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> builtins.str:
        '''The name of the telemetry rule.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c59aae5f9c690d805a52b4e5949569db025239eb21172f781673428651a87d80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec4f4991901119d1b8ec2bf2b1d23daff9627e5f20b555f27ec8fd5bc58890b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.TelemetryDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_pattern": "destinationPattern",
            "destination_type": "destinationType",
            "retention_in_days": "retentionInDays",
            "vpc_flow_log_parameters": "vpcFlowLogParameters",
        },
    )
    class TelemetryDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            destination_pattern: typing.Optional[builtins.str] = None,
            destination_type: typing.Optional[builtins.str] = None,
            retention_in_days: typing.Optional[jsii.Number] = None,
            vpc_flow_log_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTelemetryRule.VPCFlowLogParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The destination configuration for telemetry data.

            :param destination_pattern: Pattern for telemetry data destination.
            :param destination_type: Type of telemetry destination.
            :param retention_in_days: Number of days to retain the telemetry data in the specified destination.
            :param vpc_flow_log_parameters: Telemetry parameters for VPC Flow logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                telemetry_destination_configuration_property = observabilityadmin.CfnTelemetryRule.TelemetryDestinationConfigurationProperty(
                    destination_pattern="destinationPattern",
                    destination_type="destinationType",
                    retention_in_days=123,
                    vpc_flow_log_parameters=observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty(
                        log_format="logFormat",
                        max_aggregation_interval=123,
                        traffic_type="trafficType"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__01ec7a824466c4f6343ec939656046b6c12a168edd9bbf6ebca41e4b5d1554d5)
                check_type(argname="argument destination_pattern", value=destination_pattern, expected_type=type_hints["destination_pattern"])
                check_type(argname="argument destination_type", value=destination_type, expected_type=type_hints["destination_type"])
                check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
                check_type(argname="argument vpc_flow_log_parameters", value=vpc_flow_log_parameters, expected_type=type_hints["vpc_flow_log_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_pattern is not None:
                self._values["destination_pattern"] = destination_pattern
            if destination_type is not None:
                self._values["destination_type"] = destination_type
            if retention_in_days is not None:
                self._values["retention_in_days"] = retention_in_days
            if vpc_flow_log_parameters is not None:
                self._values["vpc_flow_log_parameters"] = vpc_flow_log_parameters

        @builtins.property
        def destination_pattern(self) -> typing.Optional[builtins.str]:
            '''Pattern for telemetry data destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-destinationpattern
            '''
            result = self._values.get("destination_pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def destination_type(self) -> typing.Optional[builtins.str]:
            '''Type of telemetry destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-destinationtype
            '''
            result = self._values.get("destination_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def retention_in_days(self) -> typing.Optional[jsii.Number]:
            '''Number of days to retain the telemetry data in the specified destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-retentionindays
            '''
            result = self._values.get("retention_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def vpc_flow_log_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.VPCFlowLogParametersProperty"]]:
            '''Telemetry parameters for VPC Flow logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-vpcflowlogparameters
            '''
            result = self._values.get("vpc_flow_log_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.VPCFlowLogParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelemetryDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.TelemetryRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resource_type": "resourceType",
            "telemetry_type": "telemetryType",
            "destination_configuration": "destinationConfiguration",
            "selection_criteria": "selectionCriteria",
        },
    )
    class TelemetryRuleProperty:
        def __init__(
            self,
            *,
            resource_type: builtins.str,
            telemetry_type: builtins.str,
            destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTelemetryRule.TelemetryDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            selection_criteria: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The telemetry rule.

            :param resource_type: Resource Type associated with the Telemetry Rule.
            :param telemetry_type: Telemetry Type associated with the Telemetry Rule.
            :param destination_configuration: The destination configuration for telemetry data.
            :param selection_criteria: Selection Criteria on resource level for rule application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                telemetry_rule_property = observabilityadmin.CfnTelemetryRule.TelemetryRuleProperty(
                    resource_type="resourceType",
                    telemetry_type="telemetryType",
                
                    # the properties below are optional
                    destination_configuration=observabilityadmin.CfnTelemetryRule.TelemetryDestinationConfigurationProperty(
                        destination_pattern="destinationPattern",
                        destination_type="destinationType",
                        retention_in_days=123,
                        vpc_flow_log_parameters=observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty(
                            log_format="logFormat",
                            max_aggregation_interval=123,
                            traffic_type="trafficType"
                        )
                    ),
                    selection_criteria="selectionCriteria"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__25d1c19a045d927560ccf78552c0595fbd7db1322a4e66f60e4d9cb5393b81c3)
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
                check_type(argname="argument telemetry_type", value=telemetry_type, expected_type=type_hints["telemetry_type"])
                check_type(argname="argument destination_configuration", value=destination_configuration, expected_type=type_hints["destination_configuration"])
                check_type(argname="argument selection_criteria", value=selection_criteria, expected_type=type_hints["selection_criteria"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_type": resource_type,
                "telemetry_type": telemetry_type,
            }
            if destination_configuration is not None:
                self._values["destination_configuration"] = destination_configuration
            if selection_criteria is not None:
                self._values["selection_criteria"] = selection_criteria

        @builtins.property
        def resource_type(self) -> builtins.str:
            '''Resource Type associated with the Telemetry Rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html#cfn-observabilityadmin-telemetryrule-telemetryrule-resourcetype
            '''
            result = self._values.get("resource_type")
            assert result is not None, "Required property 'resource_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def telemetry_type(self) -> builtins.str:
            '''Telemetry Type associated with the Telemetry Rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html#cfn-observabilityadmin-telemetryrule-telemetryrule-telemetrytype
            '''
            result = self._values.get("telemetry_type")
            assert result is not None, "Required property 'telemetry_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.TelemetryDestinationConfigurationProperty"]]:
            '''The destination configuration for telemetry data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html#cfn-observabilityadmin-telemetryrule-telemetryrule-destinationconfiguration
            '''
            result = self._values.get("destination_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTelemetryRule.TelemetryDestinationConfigurationProperty"]], result)

        @builtins.property
        def selection_criteria(self) -> typing.Optional[builtins.str]:
            '''Selection Criteria on resource level for rule application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html#cfn-observabilityadmin-telemetryrule-telemetryrule-selectioncriteria
            '''
            result = self._values.get("selection_criteria")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelemetryRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_format": "logFormat",
            "max_aggregation_interval": "maxAggregationInterval",
            "traffic_type": "trafficType",
        },
    )
    class VPCFlowLogParametersProperty:
        def __init__(
            self,
            *,
            log_format: typing.Optional[builtins.str] = None,
            max_aggregation_interval: typing.Optional[jsii.Number] = None,
            traffic_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Telemetry parameters for VPC Flow logs.

            :param log_format: The fields to include in the flow log record. If you omit this parameter, the flow log is created using the default format.
            :param max_aggregation_interval: The maximum interval of time, in seconds, during which a flow of packets is captured and aggregated into a flow log record. Default is 600s.
            :param traffic_type: The type of traffic captured for the flow log. Default is ALL

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                v_pCFlow_log_parameters_property = observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty(
                    log_format="logFormat",
                    max_aggregation_interval=123,
                    traffic_type="trafficType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb426e63d8ddff6bc9e58865c89c023dbf7b61ef2e21b2f9ff902df9db830681)
                check_type(argname="argument log_format", value=log_format, expected_type=type_hints["log_format"])
                check_type(argname="argument max_aggregation_interval", value=max_aggregation_interval, expected_type=type_hints["max_aggregation_interval"])
                check_type(argname="argument traffic_type", value=traffic_type, expected_type=type_hints["traffic_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_format is not None:
                self._values["log_format"] = log_format
            if max_aggregation_interval is not None:
                self._values["max_aggregation_interval"] = max_aggregation_interval
            if traffic_type is not None:
                self._values["traffic_type"] = traffic_type

        @builtins.property
        def log_format(self) -> typing.Optional[builtins.str]:
            '''The fields to include in the flow log record.

            If you omit this parameter, the flow log is created using the default format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-logformat
            '''
            result = self._values.get("log_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_aggregation_interval(self) -> typing.Optional[jsii.Number]:
            '''The maximum interval of time, in seconds, during which a flow of packets is captured and aggregated into a flow log record.

            Default is 600s.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-maxaggregationinterval
            '''
            result = self._values.get("max_aggregation_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def traffic_type(self) -> typing.Optional[builtins.str]:
            '''The type of traffic captured for the flow log.

            Default is ALL

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-traffictype
            '''
            result = self._values.get("traffic_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VPCFlowLogParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRuleProps",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "rule_name": "ruleName", "tags": "tags"},
)
class CfnTelemetryRuleProps:
    def __init__(
        self,
        *,
        rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.TelemetryRuleProperty, typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTelemetryRule``.

        :param rule: The telemetry rule.
        :param rule_name: The name of the telemetry rule.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetryrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_observabilityadmin as observabilityadmin
            
            cfn_telemetry_rule_props = observabilityadmin.CfnTelemetryRuleProps(
                rule=observabilityadmin.CfnTelemetryRule.TelemetryRuleProperty(
                    resource_type="resourceType",
                    telemetry_type="telemetryType",
            
                    # the properties below are optional
                    destination_configuration=observabilityadmin.CfnTelemetryRule.TelemetryDestinationConfigurationProperty(
                        destination_pattern="destinationPattern",
                        destination_type="destinationType",
                        retention_in_days=123,
                        vpc_flow_log_parameters=observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty(
                            log_format="logFormat",
                            max_aggregation_interval=123,
                            traffic_type="trafficType"
                        )
                    ),
                    selection_criteria="selectionCriteria"
                ),
                rule_name="ruleName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7455cb845b044ed569a8ec8407abf811920062f00d1e54ad191e90dc9b7e2811)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
            "rule_name": rule_name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnTelemetryRule.TelemetryRuleProperty]:
        '''The telemetry rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetryrule.html#cfn-observabilityadmin-telemetryrule-rule
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnTelemetryRule.TelemetryRuleProperty], result)

    @builtins.property
    def rule_name(self) -> builtins.str:
        '''The name of the telemetry rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetryrule.html#cfn-observabilityadmin-telemetryrule-rulename
        '''
        result = self._values.get("rule_name")
        assert result is not None, "Required property 'rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetryrule.html#cfn-observabilityadmin-telemetryrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTelemetryRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnOrganizationTelemetryRule",
    "CfnOrganizationTelemetryRuleProps",
    "CfnTelemetryRule",
    "CfnTelemetryRuleProps",
]

publication.publish()

def _typecheckingstub__a67d6a9dd82924a413b7d3435faeb8efa735048df0244b926e672def8c2d5f75(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.TelemetryRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cb893813673a29ee1f384593916d34bdcc440b816dfc54ad27097692c5a64e9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c809c768027da00df4018694393faf5d77af9754b12923bf684ada119faecfc7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97cf84910a3c46b94c3e90ddf73c07b304a029e413bebd1b7c5e7b2bbe5cd411(
    value: typing.Union[_IResolvable_da3f097b, CfnOrganizationTelemetryRule.TelemetryRuleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84099afcf940dd46614099ecc03e181396a6d202813d1517bd79414c5aa2f5ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d494e45ec3f03fbc2168c2e374f689615e98524c832aa6247ad243fabe01ffe7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36b4168c57b4555036ca598e8299a36985c9aab7a1eb6b84357df4454b340171(
    *,
    destination_pattern: typing.Optional[builtins.str] = None,
    destination_type: typing.Optional[builtins.str] = None,
    retention_in_days: typing.Optional[jsii.Number] = None,
    vpc_flow_log_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8febf24ebcbc00029972152d874df5e847a9f5cd45e05abb26e69f7a2cabc5bf(
    *,
    resource_type: builtins.str,
    telemetry_type: builtins.str,
    destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scope: typing.Optional[builtins.str] = None,
    selection_criteria: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__945b01222f6573dfd9bd365335b34de4d056db844b2fe9ffa6c9d40371eaff6e(
    *,
    log_format: typing.Optional[builtins.str] = None,
    max_aggregation_interval: typing.Optional[jsii.Number] = None,
    traffic_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45c94381428dd096d5bd5b31c1a78b0ec6c66b125c46a889f389e957dbf9f76b(
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.TelemetryRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cb28d06ef60815f8488b771b64aca8e3671a315a3f6676ad80a414dcd296224(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.TelemetryRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c971c1c4e8e03d4140674a22f18490c0a14f143dab5c9b15a801d0e69e908b92(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adf48e055c256d6f5cb987ba3921807e211a303c3d38be6a02b6932f52a739fe(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__253115d76ca17e48e13df2aa679666bb12581680b457a45a7743f6a80d6dbfa1(
    value: typing.Union[_IResolvable_da3f097b, CfnTelemetryRule.TelemetryRuleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c59aae5f9c690d805a52b4e5949569db025239eb21172f781673428651a87d80(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec4f4991901119d1b8ec2bf2b1d23daff9627e5f20b555f27ec8fd5bc58890b7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01ec7a824466c4f6343ec939656046b6c12a168edd9bbf6ebca41e4b5d1554d5(
    *,
    destination_pattern: typing.Optional[builtins.str] = None,
    destination_type: typing.Optional[builtins.str] = None,
    retention_in_days: typing.Optional[jsii.Number] = None,
    vpc_flow_log_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.VPCFlowLogParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d1c19a045d927560ccf78552c0595fbd7db1322a4e66f60e4d9cb5393b81c3(
    *,
    resource_type: builtins.str,
    telemetry_type: builtins.str,
    destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.TelemetryDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    selection_criteria: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb426e63d8ddff6bc9e58865c89c023dbf7b61ef2e21b2f9ff902df9db830681(
    *,
    log_format: typing.Optional[builtins.str] = None,
    max_aggregation_interval: typing.Optional[jsii.Number] = None,
    traffic_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7455cb845b044ed569a8ec8407abf811920062f00d1e54ad191e90dc9b7e2811(
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.TelemetryRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
