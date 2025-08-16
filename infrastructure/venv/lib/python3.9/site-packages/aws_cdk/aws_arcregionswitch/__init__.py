r'''
# AWS::ARCRegionSwitch Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_arcregionswitch as arcregionswitch
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ARCRegionSwitch construct libraries](https://constructs.dev/search?q=arcregionswitch)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ARCRegionSwitch resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ARCRegionSwitch.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ARCRegionSwitch](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ARCRegionSwitch.html).

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
class CfnPlan(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan",
):
    '''Represents a Region switch plan.

    A plan defines the steps required to shift traffic from one AWS Region to another.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arcregionswitch-plan.html
    :cloudformationResource: AWS::ARCRegionSwitch::Plan
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_arcregionswitch as arcregionswitch
        
        # step_property_: arcregionswitch.CfnPlan.StepProperty
        
        cfn_plan = arcregionswitch.CfnPlan(self, "MyCfnPlan",
            execution_role="executionRole",
            name="name",
            recovery_approach="recoveryApproach",
            regions=["regions"],
            workflows=[arcregionswitch.CfnPlan.WorkflowProperty(
                workflow_target_action="workflowTargetAction",
        
                # the properties below are optional
                steps=[arcregionswitch.CfnPlan.StepProperty(
                    execution_block_configuration=arcregionswitch.CfnPlan.ExecutionBlockConfigurationProperty(
                        arc_routing_control_config=arcregionswitch.CfnPlan.ArcRoutingControlConfigurationProperty(
                            region_and_routing_controls={
                                "region_and_routing_controls_key": [arcregionswitch.CfnPlan.ArcRoutingControlStateProperty(
                                    routing_control_arn="routingControlArn",
                                    state="state"
                                )]
                            },
        
                            # the properties below are optional
                            cross_account_role="crossAccountRole",
                            external_id="externalId",
                            timeout_minutes=123
                        ),
                        custom_action_lambda_config=arcregionswitch.CfnPlan.CustomActionLambdaConfigurationProperty(
                            lambdas=[arcregionswitch.CfnPlan.LambdasProperty(
                                arn="arn",
                                cross_account_role="crossAccountRole",
                                external_id="externalId"
                            )],
                            region_to_run="regionToRun",
                            retry_interval_minutes=123,
        
                            # the properties below are optional
                            timeout_minutes=123,
                            ungraceful=arcregionswitch.CfnPlan.LambdaUngracefulProperty(
                                behavior="behavior"
                            )
                        ),
                        ec2_asg_capacity_increase_config=arcregionswitch.CfnPlan.Ec2AsgCapacityIncreaseConfigurationProperty(
                            asgs=[arcregionswitch.CfnPlan.AsgProperty(
                                arn="arn",
                                cross_account_role="crossAccountRole",
                                external_id="externalId"
                            )],
        
                            # the properties below are optional
                            capacity_monitoring_approach="capacityMonitoringApproach",
                            target_percent=123,
                            timeout_minutes=123,
                            ungraceful=arcregionswitch.CfnPlan.Ec2UngracefulProperty(
                                minimum_success_percentage=123
                            )
                        ),
                        ecs_capacity_increase_config=arcregionswitch.CfnPlan.EcsCapacityIncreaseConfigurationProperty(
                            services=[arcregionswitch.CfnPlan.ServiceProperty(
                                cluster_arn="clusterArn",
                                cross_account_role="crossAccountRole",
                                external_id="externalId",
                                service_arn="serviceArn"
                            )],
        
                            # the properties below are optional
                            capacity_monitoring_approach="capacityMonitoringApproach",
                            target_percent=123,
                            timeout_minutes=123,
                            ungraceful=arcregionswitch.CfnPlan.EcsUngracefulProperty(
                                minimum_success_percentage=123
                            )
                        ),
                        eks_resource_scaling_config=arcregionswitch.CfnPlan.EksResourceScalingConfigurationProperty(
                            kubernetes_resource_type=arcregionswitch.CfnPlan.KubernetesResourceTypeProperty(
                                api_version="apiVersion",
                                kind="kind"
                            ),
        
                            # the properties below are optional
                            capacity_monitoring_approach="capacityMonitoringApproach",
                            eks_clusters=[arcregionswitch.CfnPlan.EksClusterProperty(
                                cluster_arn="clusterArn",
        
                                # the properties below are optional
                                cross_account_role="crossAccountRole",
                                external_id="externalId"
                            )],
                            scaling_resources=[{
                                "scaling_resources_key": {
                                    "scaling_resources_key": arcregionswitch.CfnPlan.KubernetesScalingResourceProperty(
                                        name="name",
                                        namespace="namespace",
        
                                        # the properties below are optional
                                        hpa_name="hpaName"
                                    )
                                }
                            }],
                            target_percent=123,
                            timeout_minutes=123,
                            ungraceful=arcregionswitch.CfnPlan.EksResourceScalingUngracefulProperty(
                                minimum_success_percentage=123
                            )
                        ),
                        execution_approval_config=arcregionswitch.CfnPlan.ExecutionApprovalConfigurationProperty(
                            approval_role="approvalRole",
        
                            # the properties below are optional
                            timeout_minutes=123
                        ),
                        global_aurora_config=arcregionswitch.CfnPlan.GlobalAuroraConfigurationProperty(
                            behavior="behavior",
                            database_cluster_arns=["databaseClusterArns"],
                            global_cluster_identifier="globalClusterIdentifier",
        
                            # the properties below are optional
                            cross_account_role="crossAccountRole",
                            external_id="externalId",
                            timeout_minutes=123,
                            ungraceful=arcregionswitch.CfnPlan.GlobalAuroraUngracefulProperty(
                                ungraceful="ungraceful"
                            )
                        ),
                        parallel_config=arcregionswitch.CfnPlan.ParallelExecutionBlockConfigurationProperty(
                            steps=[step_property_]
                        ),
                        region_switch_plan_config=arcregionswitch.CfnPlan.RegionSwitchPlanConfigurationProperty(
                            arn="arn",
        
                            # the properties below are optional
                            cross_account_role="crossAccountRole",
                            external_id="externalId"
                        ),
                        route53_health_check_config=arcregionswitch.CfnPlan.Route53HealthCheckConfigurationProperty(
                            hosted_zone_id="hostedZoneId",
                            record_name="recordName",
        
                            # the properties below are optional
                            cross_account_role="crossAccountRole",
                            external_id="externalId",
                            record_sets=[arcregionswitch.CfnPlan.Route53ResourceRecordSetProperty(
                                record_set_identifier="recordSetIdentifier",
                                region="region"
                            )],
                            timeout_minutes=123
                        )
                    ),
                    execution_block_type="executionBlockType",
                    name="name",
        
                    # the properties below are optional
                    description="description"
                )],
                workflow_description="workflowDescription",
                workflow_target_region="workflowTargetRegion"
            )],
        
            # the properties below are optional
            associated_alarms={
                "associated_alarms_key": arcregionswitch.CfnPlan.AssociatedAlarmProperty(
                    alarm_type="alarmType",
                    resource_identifier="resourceIdentifier",
        
                    # the properties below are optional
                    cross_account_role="crossAccountRole",
                    external_id="externalId"
                )
            },
            description="description",
            primary_region="primaryRegion",
            recovery_time_objective_minutes=123,
            tags={
                "tags_key": "tags"
            },
            triggers=[arcregionswitch.CfnPlan.TriggerProperty(
                action="action",
                conditions=[arcregionswitch.CfnPlan.TriggerConditionProperty(
                    associated_alarm_name="associatedAlarmName",
                    condition="condition"
                )],
                min_delay_minutes_between_executions=123,
                target_region="targetRegion",
        
                # the properties below are optional
                description="description"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        execution_role: builtins.str,
        name: builtins.str,
        recovery_approach: builtins.str,
        regions: typing.Sequence[builtins.str],
        workflows: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.WorkflowProperty", typing.Dict[builtins.str, typing.Any]]]]],
        associated_alarms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.AssociatedAlarmProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        primary_region: typing.Optional[builtins.str] = None,
        recovery_time_objective_minutes: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        triggers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.TriggerProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param execution_role: The execution role for a plan.
        :param name: The name for a plan.
        :param recovery_approach: The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).
        :param regions: The AWS Regions for a plan.
        :param workflows: The workflows for a plan.
        :param associated_alarms: The associated application health alarms for a plan.
        :param description: The description for a plan.
        :param primary_region: The primary Region for a plan.
        :param recovery_time_objective_minutes: The recovery time objective for a plan.
        :param tags: 
        :param triggers: The triggers for a plan.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__717f8fc7634107cdad75ab8dc89a21d48c1d0f596f5095c671ae6741ed5ac35c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPlanProps(
            execution_role=execution_role,
            name=name,
            recovery_approach=recovery_approach,
            regions=regions,
            workflows=workflows,
            associated_alarms=associated_alarms,
            description=description,
            primary_region=primary_region,
            recovery_time_objective_minutes=recovery_time_objective_minutes,
            tags=tags,
            triggers=triggers,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71cc46128a95cab0f86fc08911be3991a776362f808b0f24d579bc842f712f55)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5233fe9754a5f05c5abd7c2563e94e161231dbab1550036d8cb77ec7b9547432)
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
        '''The Amazon Resource Name (ARN) of the plan.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrHealthChecksForPlan")
    def attr_health_checks_for_plan(self) -> _IResolvable_da3f097b:
        '''Represents a Region switch plan.

        A plan defines the steps required to shift traffic from one AWS Region to another.

        :cloudformationAttribute: HealthChecksForPlan
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrHealthChecksForPlan"))

    @builtins.property
    @jsii.member(jsii_name="attrOwner")
    def attr_owner(self) -> builtins.str:
        '''The owner of a plan.

        :cloudformationAttribute: Owner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwner"))

    @builtins.property
    @jsii.member(jsii_name="attrVersion")
    def attr_version(self) -> builtins.str:
        '''The version for the plan.

        :cloudformationAttribute: Version
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersion"))

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
    @jsii.member(jsii_name="executionRole")
    def execution_role(self) -> builtins.str:
        '''The execution role for a plan.'''
        return typing.cast(builtins.str, jsii.get(self, "executionRole"))

    @execution_role.setter
    def execution_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f53792e88b412f34a2415fdff56351b1a54a94878ba61605061977a91e10fca2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRole", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for a plan.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbc310a1fcc73445115d9240d0eba7268997be8cac2ff2daad91277ed3174ea4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="recoveryApproach")
    def recovery_approach(self) -> builtins.str:
        '''The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).'''
        return typing.cast(builtins.str, jsii.get(self, "recoveryApproach"))

    @recovery_approach.setter
    def recovery_approach(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01b822173477d9982079c51379059a1b50ff75ad5e17af6ea27788c0b0efe0be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryApproach", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="regions")
    def regions(self) -> typing.List[builtins.str]:
        '''The AWS Regions for a plan.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regions"))

    @regions.setter
    def regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01d59248ee3d7f15f86e1af0b467749822e824bc95de98763fe13c53e695ef54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="workflows")
    def workflows(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.WorkflowProperty"]]]:
        '''The workflows for a plan.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.WorkflowProperty"]]], jsii.get(self, "workflows"))

    @workflows.setter
    def workflows(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.WorkflowProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e3eb77d0273786a3c83aa4e78160b5d7bac7f5e82e5339e9439e014d076344f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workflows", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="associatedAlarms")
    def associated_alarms(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnPlan.AssociatedAlarmProperty"]]]]:
        '''The associated application health alarms for a plan.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnPlan.AssociatedAlarmProperty"]]]], jsii.get(self, "associatedAlarms"))

    @associated_alarms.setter
    def associated_alarms(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnPlan.AssociatedAlarmProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__012a0bc7fbb902a59abbec88920455e0cd4d3ab3f0f86ab6b04d32154ed0cc71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatedAlarms", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for a plan.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__591094d49374c97cd84fa7e0eeb7a618de3dd46dd83aad681303b9ac5639e3d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="primaryRegion")
    def primary_region(self) -> typing.Optional[builtins.str]:
        '''The primary Region for a plan.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryRegion"))

    @primary_region.setter
    def primary_region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2d5c679228613d5980262152e1e6db22efda95a623c4c2113ed1dd7e09ba0a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryRegion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="recoveryTimeObjectiveMinutes")
    def recovery_time_objective_minutes(self) -> typing.Optional[jsii.Number]:
        '''The recovery time objective for a plan.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "recoveryTimeObjectiveMinutes"))

    @recovery_time_objective_minutes.setter
    def recovery_time_objective_minutes(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a158461aabcc0fceebbed61f515ca1629dd0e6cb63d8ba2e7a2f6c8e4fd5b035)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryTimeObjectiveMinutes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3c41bc2a28d77b19e855bf7c198670838a0dfb959e579501a5539e1a4eda62a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="triggers")
    def triggers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.TriggerProperty"]]]]:
        '''The triggers for a plan.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.TriggerProperty"]]]], jsii.get(self, "triggers"))

    @triggers.setter
    def triggers(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.TriggerProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__085b11c9fd7fb03e86d812a265c47665ac981e51ecdfda2e79624700d0acde6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggers", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.ArcRoutingControlConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "region_and_routing_controls": "regionAndRoutingControls",
            "cross_account_role": "crossAccountRole",
            "external_id": "externalId",
            "timeout_minutes": "timeoutMinutes",
        },
    )
    class ArcRoutingControlConfigurationProperty:
        def __init__(
            self,
            *,
            region_and_routing_controls: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.ArcRoutingControlStateProperty", typing.Dict[builtins.str, typing.Any]]]]]]],
            cross_account_role: typing.Optional[builtins.str] = None,
            external_id: typing.Optional[builtins.str] = None,
            timeout_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configuration for ARC routing controls used in a Region switch plan.

            Routing controls are simple on/off switches that you can use to shift traffic away from an impaired Region.

            :param region_and_routing_controls: The Region and ARC routing controls for the configuration.
            :param cross_account_role: The cross account role for the configuration.
            :param external_id: The external ID (secret key) for the configuration.
            :param timeout_minutes: The timeout value specified for the configuration. Default: - 60

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-arcroutingcontrolconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                arc_routing_control_configuration_property = arcregionswitch.CfnPlan.ArcRoutingControlConfigurationProperty(
                    region_and_routing_controls={
                        "region_and_routing_controls_key": [arcregionswitch.CfnPlan.ArcRoutingControlStateProperty(
                            routing_control_arn="routingControlArn",
                            state="state"
                        )]
                    },
                
                    # the properties below are optional
                    cross_account_role="crossAccountRole",
                    external_id="externalId",
                    timeout_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__57399e39635e0435be35376fd9218c629f9663afe431fd5a36d652ae3eb9873e)
                check_type(argname="argument region_and_routing_controls", value=region_and_routing_controls, expected_type=type_hints["region_and_routing_controls"])
                check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
                check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
                check_type(argname="argument timeout_minutes", value=timeout_minutes, expected_type=type_hints["timeout_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "region_and_routing_controls": region_and_routing_controls,
            }
            if cross_account_role is not None:
                self._values["cross_account_role"] = cross_account_role
            if external_id is not None:
                self._values["external_id"] = external_id
            if timeout_minutes is not None:
                self._values["timeout_minutes"] = timeout_minutes

        @builtins.property
        def region_and_routing_controls(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.ArcRoutingControlStateProperty"]]]]]:
            '''The Region and ARC routing controls for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-arcroutingcontrolconfiguration.html#cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-regionandroutingcontrols
            '''
            result = self._values.get("region_and_routing_controls")
            assert result is not None, "Required property 'region_and_routing_controls' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.ArcRoutingControlStateProperty"]]]]], result)

        @builtins.property
        def cross_account_role(self) -> typing.Optional[builtins.str]:
            '''The cross account role for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-arcroutingcontrolconfiguration.html#cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-crossaccountrole
            '''
            result = self._values.get("cross_account_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID (secret key) for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-arcroutingcontrolconfiguration.html#cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-externalid
            '''
            result = self._values.get("external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The timeout value specified for the configuration.

            :default: - 60

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-arcroutingcontrolconfiguration.html#cfn-arcregionswitch-plan-arcroutingcontrolconfiguration-timeoutminutes
            '''
            result = self._values.get("timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArcRoutingControlConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.ArcRoutingControlStateProperty",
        jsii_struct_bases=[],
        name_mapping={"routing_control_arn": "routingControlArn", "state": "state"},
    )
    class ArcRoutingControlStateProperty:
        def __init__(
            self,
            *,
            routing_control_arn: builtins.str,
            state: builtins.str,
        ) -> None:
            '''
            :param routing_control_arn: 
            :param state: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-arcroutingcontrolstate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                arc_routing_control_state_property = arcregionswitch.CfnPlan.ArcRoutingControlStateProperty(
                    routing_control_arn="routingControlArn",
                    state="state"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__55bdfafa464881d6c62e0618ec995267e3c59e4e1439ec978192672189f6b20f)
                check_type(argname="argument routing_control_arn", value=routing_control_arn, expected_type=type_hints["routing_control_arn"])
                check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "routing_control_arn": routing_control_arn,
                "state": state,
            }

        @builtins.property
        def routing_control_arn(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-arcroutingcontrolstate.html#cfn-arcregionswitch-plan-arcroutingcontrolstate-routingcontrolarn
            '''
            result = self._values.get("routing_control_arn")
            assert result is not None, "Required property 'routing_control_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def state(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-arcroutingcontrolstate.html#cfn-arcregionswitch-plan-arcroutingcontrolstate-state
            '''
            result = self._values.get("state")
            assert result is not None, "Required property 'state' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArcRoutingControlStateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.AsgProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "cross_account_role": "crossAccountRole",
            "external_id": "externalId",
        },
    )
    class AsgProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            cross_account_role: typing.Optional[builtins.str] = None,
            external_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration for an Amazon EC2 Auto Scaling group used in a Region switch plan.

            :param arn: The Amazon Resource Name (ARN) of the EC2 Auto Scaling group.
            :param cross_account_role: The cross account role for the configuration.
            :param external_id: The external ID (secret key) for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-asg.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                asg_property = arcregionswitch.CfnPlan.AsgProperty(
                    arn="arn",
                    cross_account_role="crossAccountRole",
                    external_id="externalId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1676b0ee46a93bdc080e497fe362d46ed4de4bf3d0f939d09ff3f213c7f5c637)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
                check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if cross_account_role is not None:
                self._values["cross_account_role"] = cross_account_role
            if external_id is not None:
                self._values["external_id"] = external_id

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the EC2 Auto Scaling group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-asg.html#cfn-arcregionswitch-plan-asg-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cross_account_role(self) -> typing.Optional[builtins.str]:
            '''The cross account role for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-asg.html#cfn-arcregionswitch-plan-asg-crossaccountrole
            '''
            result = self._values.get("cross_account_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID (secret key) for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-asg.html#cfn-arcregionswitch-plan-asg-externalid
            '''
            result = self._values.get("external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AsgProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.AssociatedAlarmProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alarm_type": "alarmType",
            "resource_identifier": "resourceIdentifier",
            "cross_account_role": "crossAccountRole",
            "external_id": "externalId",
        },
    )
    class AssociatedAlarmProperty:
        def __init__(
            self,
            *,
            alarm_type: builtins.str,
            resource_identifier: builtins.str,
            cross_account_role: typing.Optional[builtins.str] = None,
            external_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An Amazon CloudWatch alarm associated with a Region switch plan.

            These alarms can be used to trigger automatic execution of the plan.

            :param alarm_type: The alarm type for an associated alarm. An associated CloudWatch alarm can be an application health alarm or a trigger alarm.
            :param resource_identifier: The resource identifier for alarms that you associate with a plan.
            :param cross_account_role: The cross account role for the configuration.
            :param external_id: The external ID (secret key) for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-associatedalarm.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                associated_alarm_property = arcregionswitch.CfnPlan.AssociatedAlarmProperty(
                    alarm_type="alarmType",
                    resource_identifier="resourceIdentifier",
                
                    # the properties below are optional
                    cross_account_role="crossAccountRole",
                    external_id="externalId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__da9567b68c112553218c3dc6b107e275b5f8974694e79a06ee1f35ade040a4ff)
                check_type(argname="argument alarm_type", value=alarm_type, expected_type=type_hints["alarm_type"])
                check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
                check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
                check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "alarm_type": alarm_type,
                "resource_identifier": resource_identifier,
            }
            if cross_account_role is not None:
                self._values["cross_account_role"] = cross_account_role
            if external_id is not None:
                self._values["external_id"] = external_id

        @builtins.property
        def alarm_type(self) -> builtins.str:
            '''The alarm type for an associated alarm.

            An associated CloudWatch alarm can be an application health alarm or a trigger alarm.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-associatedalarm.html#cfn-arcregionswitch-plan-associatedalarm-alarmtype
            '''
            result = self._values.get("alarm_type")
            assert result is not None, "Required property 'alarm_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_identifier(self) -> builtins.str:
            '''The resource identifier for alarms that you associate with a plan.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-associatedalarm.html#cfn-arcregionswitch-plan-associatedalarm-resourceidentifier
            '''
            result = self._values.get("resource_identifier")
            assert result is not None, "Required property 'resource_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cross_account_role(self) -> typing.Optional[builtins.str]:
            '''The cross account role for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-associatedalarm.html#cfn-arcregionswitch-plan-associatedalarm-crossaccountrole
            '''
            result = self._values.get("cross_account_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID (secret key) for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-associatedalarm.html#cfn-arcregionswitch-plan-associatedalarm-externalid
            '''
            result = self._values.get("external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssociatedAlarmProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.CustomActionLambdaConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lambdas": "lambdas",
            "region_to_run": "regionToRun",
            "retry_interval_minutes": "retryIntervalMinutes",
            "timeout_minutes": "timeoutMinutes",
            "ungraceful": "ungraceful",
        },
    )
    class CustomActionLambdaConfigurationProperty:
        def __init__(
            self,
            *,
            lambdas: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.LambdasProperty", typing.Dict[builtins.str, typing.Any]]]]],
            region_to_run: builtins.str,
            retry_interval_minutes: jsii.Number,
            timeout_minutes: typing.Optional[jsii.Number] = None,
            ungraceful: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.LambdaUngracefulProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration for AWS Lambda functions that perform custom actions during a Region switch.

            :param lambdas: The AWS Lambda functions for the execution block.
            :param region_to_run: The AWS Region for the function to run in.
            :param retry_interval_minutes: The retry interval specified.
            :param timeout_minutes: The timeout value specified for the configuration. Default: - 60
            :param ungraceful: The settings for ungraceful execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-customactionlambdaconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                custom_action_lambda_configuration_property = arcregionswitch.CfnPlan.CustomActionLambdaConfigurationProperty(
                    lambdas=[arcregionswitch.CfnPlan.LambdasProperty(
                        arn="arn",
                        cross_account_role="crossAccountRole",
                        external_id="externalId"
                    )],
                    region_to_run="regionToRun",
                    retry_interval_minutes=123,
                
                    # the properties below are optional
                    timeout_minutes=123,
                    ungraceful=arcregionswitch.CfnPlan.LambdaUngracefulProperty(
                        behavior="behavior"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__677cc1e3776f9941a3e383511e2b156b9b18584e59ab2742e9aeb2a068d4a396)
                check_type(argname="argument lambdas", value=lambdas, expected_type=type_hints["lambdas"])
                check_type(argname="argument region_to_run", value=region_to_run, expected_type=type_hints["region_to_run"])
                check_type(argname="argument retry_interval_minutes", value=retry_interval_minutes, expected_type=type_hints["retry_interval_minutes"])
                check_type(argname="argument timeout_minutes", value=timeout_minutes, expected_type=type_hints["timeout_minutes"])
                check_type(argname="argument ungraceful", value=ungraceful, expected_type=type_hints["ungraceful"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lambdas": lambdas,
                "region_to_run": region_to_run,
                "retry_interval_minutes": retry_interval_minutes,
            }
            if timeout_minutes is not None:
                self._values["timeout_minutes"] = timeout_minutes
            if ungraceful is not None:
                self._values["ungraceful"] = ungraceful

        @builtins.property
        def lambdas(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.LambdasProperty"]]]:
            '''The AWS Lambda functions for the execution block.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-customactionlambdaconfiguration.html#cfn-arcregionswitch-plan-customactionlambdaconfiguration-lambdas
            '''
            result = self._values.get("lambdas")
            assert result is not None, "Required property 'lambdas' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.LambdasProperty"]]], result)

        @builtins.property
        def region_to_run(self) -> builtins.str:
            '''The AWS Region for the function to run in.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-customactionlambdaconfiguration.html#cfn-arcregionswitch-plan-customactionlambdaconfiguration-regiontorun
            '''
            result = self._values.get("region_to_run")
            assert result is not None, "Required property 'region_to_run' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def retry_interval_minutes(self) -> jsii.Number:
            '''The retry interval specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-customactionlambdaconfiguration.html#cfn-arcregionswitch-plan-customactionlambdaconfiguration-retryintervalminutes
            '''
            result = self._values.get("retry_interval_minutes")
            assert result is not None, "Required property 'retry_interval_minutes' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The timeout value specified for the configuration.

            :default: - 60

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-customactionlambdaconfiguration.html#cfn-arcregionswitch-plan-customactionlambdaconfiguration-timeoutminutes
            '''
            result = self._values.get("timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ungraceful(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.LambdaUngracefulProperty"]]:
            '''The settings for ungraceful execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-customactionlambdaconfiguration.html#cfn-arcregionswitch-plan-customactionlambdaconfiguration-ungraceful
            '''
            result = self._values.get("ungraceful")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.LambdaUngracefulProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomActionLambdaConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.Ec2AsgCapacityIncreaseConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "asgs": "asgs",
            "capacity_monitoring_approach": "capacityMonitoringApproach",
            "target_percent": "targetPercent",
            "timeout_minutes": "timeoutMinutes",
            "ungraceful": "ungraceful",
        },
    )
    class Ec2AsgCapacityIncreaseConfigurationProperty:
        def __init__(
            self,
            *,
            asgs: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.AsgProperty", typing.Dict[builtins.str, typing.Any]]]]],
            capacity_monitoring_approach: typing.Optional[builtins.str] = None,
            target_percent: typing.Optional[jsii.Number] = None,
            timeout_minutes: typing.Optional[jsii.Number] = None,
            ungraceful: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.Ec2UngracefulProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration for increasing the capacity of Amazon EC2 Auto Scaling groups during a Region switch.

            :param asgs: The EC2 Auto Scaling groups for the configuration.
            :param capacity_monitoring_approach: The monitoring approach that you specify EC2 Auto Scaling groups for the configuration.
            :param target_percent: The target percentage that you specify for EC2 Auto Scaling groups. Default: - 100
            :param timeout_minutes: The timeout value specified for the configuration. Default: - 60
            :param ungraceful: The settings for ungraceful execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                ec2_asg_capacity_increase_configuration_property = arcregionswitch.CfnPlan.Ec2AsgCapacityIncreaseConfigurationProperty(
                    asgs=[arcregionswitch.CfnPlan.AsgProperty(
                        arn="arn",
                        cross_account_role="crossAccountRole",
                        external_id="externalId"
                    )],
                
                    # the properties below are optional
                    capacity_monitoring_approach="capacityMonitoringApproach",
                    target_percent=123,
                    timeout_minutes=123,
                    ungraceful=arcregionswitch.CfnPlan.Ec2UngracefulProperty(
                        minimum_success_percentage=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9450c4fc5464b8ee89e44bf3f7537c88de4728278fe9d0f976e7b3a1004ee5f0)
                check_type(argname="argument asgs", value=asgs, expected_type=type_hints["asgs"])
                check_type(argname="argument capacity_monitoring_approach", value=capacity_monitoring_approach, expected_type=type_hints["capacity_monitoring_approach"])
                check_type(argname="argument target_percent", value=target_percent, expected_type=type_hints["target_percent"])
                check_type(argname="argument timeout_minutes", value=timeout_minutes, expected_type=type_hints["timeout_minutes"])
                check_type(argname="argument ungraceful", value=ungraceful, expected_type=type_hints["ungraceful"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "asgs": asgs,
            }
            if capacity_monitoring_approach is not None:
                self._values["capacity_monitoring_approach"] = capacity_monitoring_approach
            if target_percent is not None:
                self._values["target_percent"] = target_percent
            if timeout_minutes is not None:
                self._values["timeout_minutes"] = timeout_minutes
            if ungraceful is not None:
                self._values["ungraceful"] = ungraceful

        @builtins.property
        def asgs(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.AsgProperty"]]]:
            '''The EC2 Auto Scaling groups for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration.html#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-asgs
            '''
            result = self._values.get("asgs")
            assert result is not None, "Required property 'asgs' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.AsgProperty"]]], result)

        @builtins.property
        def capacity_monitoring_approach(self) -> typing.Optional[builtins.str]:
            '''The monitoring approach that you specify EC2 Auto Scaling groups for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration.html#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-capacitymonitoringapproach
            '''
            result = self._values.get("capacity_monitoring_approach")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_percent(self) -> typing.Optional[jsii.Number]:
            '''The target percentage that you specify for EC2 Auto Scaling groups.

            :default: - 100

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration.html#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-targetpercent
            '''
            result = self._values.get("target_percent")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The timeout value specified for the configuration.

            :default: - 60

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration.html#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-timeoutminutes
            '''
            result = self._values.get("timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ungraceful(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.Ec2UngracefulProperty"]]:
            '''The settings for ungraceful execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration.html#cfn-arcregionswitch-plan-ec2asgcapacityincreaseconfiguration-ungraceful
            '''
            result = self._values.get("ungraceful")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.Ec2UngracefulProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Ec2AsgCapacityIncreaseConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.Ec2UngracefulProperty",
        jsii_struct_bases=[],
        name_mapping={"minimum_success_percentage": "minimumSuccessPercentage"},
    )
    class Ec2UngracefulProperty:
        def __init__(self, *, minimum_success_percentage: jsii.Number) -> None:
            '''Configuration for handling failures when performing operations on EC2 resources.

            :param minimum_success_percentage: The minimum success percentage that you specify for EC2 Auto Scaling groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ec2ungraceful.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                ec2_ungraceful_property = arcregionswitch.CfnPlan.Ec2UngracefulProperty(
                    minimum_success_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__df83017a8027c200570884800a256e6029496bb9ce1b006656a7874327f5298d)
                check_type(argname="argument minimum_success_percentage", value=minimum_success_percentage, expected_type=type_hints["minimum_success_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "minimum_success_percentage": minimum_success_percentage,
            }

        @builtins.property
        def minimum_success_percentage(self) -> jsii.Number:
            '''The minimum success percentage that you specify for EC2 Auto Scaling groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ec2ungraceful.html#cfn-arcregionswitch-plan-ec2ungraceful-minimumsuccesspercentage
            '''
            result = self._values.get("minimum_success_percentage")
            assert result is not None, "Required property 'minimum_success_percentage' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Ec2UngracefulProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.EcsCapacityIncreaseConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "services": "services",
            "capacity_monitoring_approach": "capacityMonitoringApproach",
            "target_percent": "targetPercent",
            "timeout_minutes": "timeoutMinutes",
            "ungraceful": "ungraceful",
        },
    )
    class EcsCapacityIncreaseConfigurationProperty:
        def __init__(
            self,
            *,
            services: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.ServiceProperty", typing.Dict[builtins.str, typing.Any]]]]],
            capacity_monitoring_approach: typing.Optional[builtins.str] = None,
            target_percent: typing.Optional[jsii.Number] = None,
            timeout_minutes: typing.Optional[jsii.Number] = None,
            ungraceful: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.EcsUngracefulProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration for an AWS ECS capacity increase.

            :param services: The services specified for the configuration.
            :param capacity_monitoring_approach: The monitoring approach specified for the configuration, for example, ``Most_Recent`` .
            :param target_percent: The target percentage specified for the configuration. Default: - 100
            :param timeout_minutes: The timeout value specified for the configuration. Default: - 60
            :param ungraceful: The settings for ungraceful execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ecscapacityincreaseconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                ecs_capacity_increase_configuration_property = arcregionswitch.CfnPlan.EcsCapacityIncreaseConfigurationProperty(
                    services=[arcregionswitch.CfnPlan.ServiceProperty(
                        cluster_arn="clusterArn",
                        cross_account_role="crossAccountRole",
                        external_id="externalId",
                        service_arn="serviceArn"
                    )],
                
                    # the properties below are optional
                    capacity_monitoring_approach="capacityMonitoringApproach",
                    target_percent=123,
                    timeout_minutes=123,
                    ungraceful=arcregionswitch.CfnPlan.EcsUngracefulProperty(
                        minimum_success_percentage=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3b763afef631e7db8b2c2c3be0ade842b4b5d07005a78e029167a12daa9a0b59)
                check_type(argname="argument services", value=services, expected_type=type_hints["services"])
                check_type(argname="argument capacity_monitoring_approach", value=capacity_monitoring_approach, expected_type=type_hints["capacity_monitoring_approach"])
                check_type(argname="argument target_percent", value=target_percent, expected_type=type_hints["target_percent"])
                check_type(argname="argument timeout_minutes", value=timeout_minutes, expected_type=type_hints["timeout_minutes"])
                check_type(argname="argument ungraceful", value=ungraceful, expected_type=type_hints["ungraceful"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "services": services,
            }
            if capacity_monitoring_approach is not None:
                self._values["capacity_monitoring_approach"] = capacity_monitoring_approach
            if target_percent is not None:
                self._values["target_percent"] = target_percent
            if timeout_minutes is not None:
                self._values["timeout_minutes"] = timeout_minutes
            if ungraceful is not None:
                self._values["ungraceful"] = ungraceful

        @builtins.property
        def services(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.ServiceProperty"]]]:
            '''The services specified for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ecscapacityincreaseconfiguration.html#cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-services
            '''
            result = self._values.get("services")
            assert result is not None, "Required property 'services' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.ServiceProperty"]]], result)

        @builtins.property
        def capacity_monitoring_approach(self) -> typing.Optional[builtins.str]:
            '''The monitoring approach specified for the configuration, for example, ``Most_Recent`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ecscapacityincreaseconfiguration.html#cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-capacitymonitoringapproach
            '''
            result = self._values.get("capacity_monitoring_approach")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_percent(self) -> typing.Optional[jsii.Number]:
            '''The target percentage specified for the configuration.

            :default: - 100

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ecscapacityincreaseconfiguration.html#cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-targetpercent
            '''
            result = self._values.get("target_percent")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The timeout value specified for the configuration.

            :default: - 60

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ecscapacityincreaseconfiguration.html#cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-timeoutminutes
            '''
            result = self._values.get("timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ungraceful(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.EcsUngracefulProperty"]]:
            '''The settings for ungraceful execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ecscapacityincreaseconfiguration.html#cfn-arcregionswitch-plan-ecscapacityincreaseconfiguration-ungraceful
            '''
            result = self._values.get("ungraceful")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.EcsUngracefulProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EcsCapacityIncreaseConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.EcsUngracefulProperty",
        jsii_struct_bases=[],
        name_mapping={"minimum_success_percentage": "minimumSuccessPercentage"},
    )
    class EcsUngracefulProperty:
        def __init__(self, *, minimum_success_percentage: jsii.Number) -> None:
            '''The settings for ungraceful execution.

            :param minimum_success_percentage: The minimum success percentage specified for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ecsungraceful.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                ecs_ungraceful_property = arcregionswitch.CfnPlan.EcsUngracefulProperty(
                    minimum_success_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__deb1d009908c0c1564a0347ddbba856cd682e5fbd50557e7915c487a54d62313)
                check_type(argname="argument minimum_success_percentage", value=minimum_success_percentage, expected_type=type_hints["minimum_success_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "minimum_success_percentage": minimum_success_percentage,
            }

        @builtins.property
        def minimum_success_percentage(self) -> jsii.Number:
            '''The minimum success percentage specified for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ecsungraceful.html#cfn-arcregionswitch-plan-ecsungraceful-minimumsuccesspercentage
            '''
            result = self._values.get("minimum_success_percentage")
            assert result is not None, "Required property 'minimum_success_percentage' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EcsUngracefulProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.EksClusterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cluster_arn": "clusterArn",
            "cross_account_role": "crossAccountRole",
            "external_id": "externalId",
        },
    )
    class EksClusterProperty:
        def __init__(
            self,
            *,
            cluster_arn: builtins.str,
            cross_account_role: typing.Optional[builtins.str] = None,
            external_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The AWS EKS cluster execution block configuration.

            :param cluster_arn: The Amazon Resource Name (ARN) of an AWS EKS cluster.
            :param cross_account_role: The cross account role for the configuration.
            :param external_id: The external ID (secret key) for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ekscluster.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                eks_cluster_property = arcregionswitch.CfnPlan.EksClusterProperty(
                    cluster_arn="clusterArn",
                
                    # the properties below are optional
                    cross_account_role="crossAccountRole",
                    external_id="externalId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0d56face50d286f66c61a4649242ee9c0e4214f5a237dcc15a2a3ef5398d4405)
                check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
                check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
                check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cluster_arn": cluster_arn,
            }
            if cross_account_role is not None:
                self._values["cross_account_role"] = cross_account_role
            if external_id is not None:
                self._values["external_id"] = external_id

        @builtins.property
        def cluster_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of an AWS EKS cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ekscluster.html#cfn-arcregionswitch-plan-ekscluster-clusterarn
            '''
            result = self._values.get("cluster_arn")
            assert result is not None, "Required property 'cluster_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cross_account_role(self) -> typing.Optional[builtins.str]:
            '''The cross account role for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ekscluster.html#cfn-arcregionswitch-plan-ekscluster-crossaccountrole
            '''
            result = self._values.get("cross_account_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID (secret key) for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-ekscluster.html#cfn-arcregionswitch-plan-ekscluster-externalid
            '''
            result = self._values.get("external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksClusterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.EksResourceScalingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kubernetes_resource_type": "kubernetesResourceType",
            "capacity_monitoring_approach": "capacityMonitoringApproach",
            "eks_clusters": "eksClusters",
            "scaling_resources": "scalingResources",
            "target_percent": "targetPercent",
            "timeout_minutes": "timeoutMinutes",
            "ungraceful": "ungraceful",
        },
    )
    class EksResourceScalingConfigurationProperty:
        def __init__(
            self,
            *,
            kubernetes_resource_type: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.KubernetesResourceTypeProperty", typing.Dict[builtins.str, typing.Any]]],
            capacity_monitoring_approach: typing.Optional[builtins.str] = None,
            eks_clusters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.EksClusterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            scaling_resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.KubernetesScalingResourceProperty", typing.Dict[builtins.str, typing.Any]]]]]]]]]] = None,
            target_percent: typing.Optional[jsii.Number] = None,
            timeout_minutes: typing.Optional[jsii.Number] = None,
            ungraceful: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.EksResourceScalingUngracefulProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The AWS EKS resource scaling configuration.

            :param kubernetes_resource_type: The Kubernetes resource type for the configuration.
            :param capacity_monitoring_approach: The monitoring approach for the configuration, that is, whether it was sampled in the last 24 hours or autoscaled in the last 24 hours.
            :param eks_clusters: The clusters for the configuration.
            :param scaling_resources: The scaling resources for the configuration.
            :param target_percent: The target percentage for the configuration. Default: - 100
            :param timeout_minutes: The timeout value specified for the configuration. Default: - 60
            :param ungraceful: The settings for ungraceful execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-eksresourcescalingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                eks_resource_scaling_configuration_property = arcregionswitch.CfnPlan.EksResourceScalingConfigurationProperty(
                    kubernetes_resource_type=arcregionswitch.CfnPlan.KubernetesResourceTypeProperty(
                        api_version="apiVersion",
                        kind="kind"
                    ),
                
                    # the properties below are optional
                    capacity_monitoring_approach="capacityMonitoringApproach",
                    eks_clusters=[arcregionswitch.CfnPlan.EksClusterProperty(
                        cluster_arn="clusterArn",
                
                        # the properties below are optional
                        cross_account_role="crossAccountRole",
                        external_id="externalId"
                    )],
                    scaling_resources=[{
                        "scaling_resources_key": {
                            "scaling_resources_key": arcregionswitch.CfnPlan.KubernetesScalingResourceProperty(
                                name="name",
                                namespace="namespace",
                
                                # the properties below are optional
                                hpa_name="hpaName"
                            )
                        }
                    }],
                    target_percent=123,
                    timeout_minutes=123,
                    ungraceful=arcregionswitch.CfnPlan.EksResourceScalingUngracefulProperty(
                        minimum_success_percentage=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6a31277680fa6df426ddb8d5341e3bc1a473a20cfd357c9ab42c51d8342d45d2)
                check_type(argname="argument kubernetes_resource_type", value=kubernetes_resource_type, expected_type=type_hints["kubernetes_resource_type"])
                check_type(argname="argument capacity_monitoring_approach", value=capacity_monitoring_approach, expected_type=type_hints["capacity_monitoring_approach"])
                check_type(argname="argument eks_clusters", value=eks_clusters, expected_type=type_hints["eks_clusters"])
                check_type(argname="argument scaling_resources", value=scaling_resources, expected_type=type_hints["scaling_resources"])
                check_type(argname="argument target_percent", value=target_percent, expected_type=type_hints["target_percent"])
                check_type(argname="argument timeout_minutes", value=timeout_minutes, expected_type=type_hints["timeout_minutes"])
                check_type(argname="argument ungraceful", value=ungraceful, expected_type=type_hints["ungraceful"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "kubernetes_resource_type": kubernetes_resource_type,
            }
            if capacity_monitoring_approach is not None:
                self._values["capacity_monitoring_approach"] = capacity_monitoring_approach
            if eks_clusters is not None:
                self._values["eks_clusters"] = eks_clusters
            if scaling_resources is not None:
                self._values["scaling_resources"] = scaling_resources
            if target_percent is not None:
                self._values["target_percent"] = target_percent
            if timeout_minutes is not None:
                self._values["timeout_minutes"] = timeout_minutes
            if ungraceful is not None:
                self._values["ungraceful"] = ungraceful

        @builtins.property
        def kubernetes_resource_type(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnPlan.KubernetesResourceTypeProperty"]:
            '''The Kubernetes resource type for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-eksresourcescalingconfiguration.html#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-kubernetesresourcetype
            '''
            result = self._values.get("kubernetes_resource_type")
            assert result is not None, "Required property 'kubernetes_resource_type' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPlan.KubernetesResourceTypeProperty"], result)

        @builtins.property
        def capacity_monitoring_approach(self) -> typing.Optional[builtins.str]:
            '''The monitoring approach for the configuration, that is, whether it was sampled in the last 24 hours or autoscaled in the last 24 hours.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-eksresourcescalingconfiguration.html#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-capacitymonitoringapproach
            '''
            result = self._values.get("capacity_monitoring_approach")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def eks_clusters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.EksClusterProperty"]]]]:
            '''The clusters for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-eksresourcescalingconfiguration.html#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-eksclusters
            '''
            result = self._values.get("eks_clusters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.EksClusterProperty"]]]], result)

        @builtins.property
        def scaling_resources(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnPlan.KubernetesScalingResourceProperty"]]]]]]]]:
            '''The scaling resources for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-eksresourcescalingconfiguration.html#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-scalingresources
            '''
            result = self._values.get("scaling_resources")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnPlan.KubernetesScalingResourceProperty"]]]]]]]], result)

        @builtins.property
        def target_percent(self) -> typing.Optional[jsii.Number]:
            '''The target percentage for the configuration.

            :default: - 100

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-eksresourcescalingconfiguration.html#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-targetpercent
            '''
            result = self._values.get("target_percent")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The timeout value specified for the configuration.

            :default: - 60

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-eksresourcescalingconfiguration.html#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-timeoutminutes
            '''
            result = self._values.get("timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ungraceful(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.EksResourceScalingUngracefulProperty"]]:
            '''The settings for ungraceful execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-eksresourcescalingconfiguration.html#cfn-arcregionswitch-plan-eksresourcescalingconfiguration-ungraceful
            '''
            result = self._values.get("ungraceful")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.EksResourceScalingUngracefulProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksResourceScalingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.EksResourceScalingUngracefulProperty",
        jsii_struct_bases=[],
        name_mapping={"minimum_success_percentage": "minimumSuccessPercentage"},
    )
    class EksResourceScalingUngracefulProperty:
        def __init__(self, *, minimum_success_percentage: jsii.Number) -> None:
            '''The ungraceful settings for AWS EKS resource scaling.

            :param minimum_success_percentage: The minimum success percentage for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-eksresourcescalingungraceful.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                eks_resource_scaling_ungraceful_property = arcregionswitch.CfnPlan.EksResourceScalingUngracefulProperty(
                    minimum_success_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5f9e5d7d28df64aed085e7fff7c951fac8c798f2930bd6f677766f09bf9022cb)
                check_type(argname="argument minimum_success_percentage", value=minimum_success_percentage, expected_type=type_hints["minimum_success_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "minimum_success_percentage": minimum_success_percentage,
            }

        @builtins.property
        def minimum_success_percentage(self) -> jsii.Number:
            '''The minimum success percentage for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-eksresourcescalingungraceful.html#cfn-arcregionswitch-plan-eksresourcescalingungraceful-minimumsuccesspercentage
            '''
            result = self._values.get("minimum_success_percentage")
            assert result is not None, "Required property 'minimum_success_percentage' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksResourceScalingUngracefulProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.ExecutionApprovalConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "approval_role": "approvalRole",
            "timeout_minutes": "timeoutMinutes",
        },
    )
    class ExecutionApprovalConfigurationProperty:
        def __init__(
            self,
            *,
            approval_role: builtins.str,
            timeout_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configuration for approval steps in a Region switch plan execution.

            Approval steps require manual intervention before the execution can proceed.

            :param approval_role: The IAM approval role for the configuration.
            :param timeout_minutes: The timeout value specified for the configuration. Default: - 60

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-executionapprovalconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                execution_approval_configuration_property = arcregionswitch.CfnPlan.ExecutionApprovalConfigurationProperty(
                    approval_role="approvalRole",
                
                    # the properties below are optional
                    timeout_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__332cd445173cd90befd93793d12cf56d6b9d0cf5f0f950d8f1c8da40b41112d7)
                check_type(argname="argument approval_role", value=approval_role, expected_type=type_hints["approval_role"])
                check_type(argname="argument timeout_minutes", value=timeout_minutes, expected_type=type_hints["timeout_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "approval_role": approval_role,
            }
            if timeout_minutes is not None:
                self._values["timeout_minutes"] = timeout_minutes

        @builtins.property
        def approval_role(self) -> builtins.str:
            '''The IAM approval role for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-executionapprovalconfiguration.html#cfn-arcregionswitch-plan-executionapprovalconfiguration-approvalrole
            '''
            result = self._values.get("approval_role")
            assert result is not None, "Required property 'approval_role' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The timeout value specified for the configuration.

            :default: - 60

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-executionapprovalconfiguration.html#cfn-arcregionswitch-plan-executionapprovalconfiguration-timeoutminutes
            '''
            result = self._values.get("timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExecutionApprovalConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.ExecutionBlockConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arc_routing_control_config": "arcRoutingControlConfig",
            "custom_action_lambda_config": "customActionLambdaConfig",
            "ec2_asg_capacity_increase_config": "ec2AsgCapacityIncreaseConfig",
            "ecs_capacity_increase_config": "ecsCapacityIncreaseConfig",
            "eks_resource_scaling_config": "eksResourceScalingConfig",
            "execution_approval_config": "executionApprovalConfig",
            "global_aurora_config": "globalAuroraConfig",
            "parallel_config": "parallelConfig",
            "region_switch_plan_config": "regionSwitchPlanConfig",
            "route53_health_check_config": "route53HealthCheckConfig",
        },
    )
    class ExecutionBlockConfigurationProperty:
        def __init__(
            self,
            *,
            arc_routing_control_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.ArcRoutingControlConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            custom_action_lambda_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.CustomActionLambdaConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ec2_asg_capacity_increase_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.Ec2AsgCapacityIncreaseConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ecs_capacity_increase_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.EcsCapacityIncreaseConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            eks_resource_scaling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.EksResourceScalingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            execution_approval_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.ExecutionApprovalConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            global_aurora_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.GlobalAuroraConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            parallel_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.ParallelExecutionBlockConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            region_switch_plan_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.RegionSwitchPlanConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            route53_health_check_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.Route53HealthCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Execution block configurations for a workflow in a Region switch plan.

            An execution block represents a specific type of action to perform during a Region switch.

            :param arc_routing_control_config: An ARC routing control execution block.
            :param custom_action_lambda_config: An AWS Lambda execution block.
            :param ec2_asg_capacity_increase_config: An EC2 Auto Scaling group execution block.
            :param ecs_capacity_increase_config: The capacity increase specified for the configuration.
            :param eks_resource_scaling_config: An AWS EKS resource scaling execution block.
            :param execution_approval_config: A manual approval execution block.
            :param global_aurora_config: An Aurora Global Database execution block.
            :param parallel_config: A parallel configuration execution block.
            :param region_switch_plan_config: A Region switch plan execution block.
            :param route53_health_check_config: The Amazon Route 53 health check configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-executionblockconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                # execution_block_configuration_property_: arcregionswitch.CfnPlan.ExecutionBlockConfigurationProperty
                
                execution_block_configuration_property = arcregionswitch.CfnPlan.ExecutionBlockConfigurationProperty(
                    arc_routing_control_config=arcregionswitch.CfnPlan.ArcRoutingControlConfigurationProperty(
                        region_and_routing_controls={
                            "region_and_routing_controls_key": [arcregionswitch.CfnPlan.ArcRoutingControlStateProperty(
                                routing_control_arn="routingControlArn",
                                state="state"
                            )]
                        },
                
                        # the properties below are optional
                        cross_account_role="crossAccountRole",
                        external_id="externalId",
                        timeout_minutes=123
                    ),
                    custom_action_lambda_config=arcregionswitch.CfnPlan.CustomActionLambdaConfigurationProperty(
                        lambdas=[arcregionswitch.CfnPlan.LambdasProperty(
                            arn="arn",
                            cross_account_role="crossAccountRole",
                            external_id="externalId"
                        )],
                        region_to_run="regionToRun",
                        retry_interval_minutes=123,
                
                        # the properties below are optional
                        timeout_minutes=123,
                        ungraceful=arcregionswitch.CfnPlan.LambdaUngracefulProperty(
                            behavior="behavior"
                        )
                    ),
                    ec2_asg_capacity_increase_config=arcregionswitch.CfnPlan.Ec2AsgCapacityIncreaseConfigurationProperty(
                        asgs=[arcregionswitch.CfnPlan.AsgProperty(
                            arn="arn",
                            cross_account_role="crossAccountRole",
                            external_id="externalId"
                        )],
                
                        # the properties below are optional
                        capacity_monitoring_approach="capacityMonitoringApproach",
                        target_percent=123,
                        timeout_minutes=123,
                        ungraceful=arcregionswitch.CfnPlan.Ec2UngracefulProperty(
                            minimum_success_percentage=123
                        )
                    ),
                    ecs_capacity_increase_config=arcregionswitch.CfnPlan.EcsCapacityIncreaseConfigurationProperty(
                        services=[arcregionswitch.CfnPlan.ServiceProperty(
                            cluster_arn="clusterArn",
                            cross_account_role="crossAccountRole",
                            external_id="externalId",
                            service_arn="serviceArn"
                        )],
                
                        # the properties below are optional
                        capacity_monitoring_approach="capacityMonitoringApproach",
                        target_percent=123,
                        timeout_minutes=123,
                        ungraceful=arcregionswitch.CfnPlan.EcsUngracefulProperty(
                            minimum_success_percentage=123
                        )
                    ),
                    eks_resource_scaling_config=arcregionswitch.CfnPlan.EksResourceScalingConfigurationProperty(
                        kubernetes_resource_type=arcregionswitch.CfnPlan.KubernetesResourceTypeProperty(
                            api_version="apiVersion",
                            kind="kind"
                        ),
                
                        # the properties below are optional
                        capacity_monitoring_approach="capacityMonitoringApproach",
                        eks_clusters=[arcregionswitch.CfnPlan.EksClusterProperty(
                            cluster_arn="clusterArn",
                
                            # the properties below are optional
                            cross_account_role="crossAccountRole",
                            external_id="externalId"
                        )],
                        scaling_resources=[{
                            "scaling_resources_key": {
                                "scaling_resources_key": arcregionswitch.CfnPlan.KubernetesScalingResourceProperty(
                                    name="name",
                                    namespace="namespace",
                
                                    # the properties below are optional
                                    hpa_name="hpaName"
                                )
                            }
                        }],
                        target_percent=123,
                        timeout_minutes=123,
                        ungraceful=arcregionswitch.CfnPlan.EksResourceScalingUngracefulProperty(
                            minimum_success_percentage=123
                        )
                    ),
                    execution_approval_config=arcregionswitch.CfnPlan.ExecutionApprovalConfigurationProperty(
                        approval_role="approvalRole",
                
                        # the properties below are optional
                        timeout_minutes=123
                    ),
                    global_aurora_config=arcregionswitch.CfnPlan.GlobalAuroraConfigurationProperty(
                        behavior="behavior",
                        database_cluster_arns=["databaseClusterArns"],
                        global_cluster_identifier="globalClusterIdentifier",
                
                        # the properties below are optional
                        cross_account_role="crossAccountRole",
                        external_id="externalId",
                        timeout_minutes=123,
                        ungraceful=arcregionswitch.CfnPlan.GlobalAuroraUngracefulProperty(
                            ungraceful="ungraceful"
                        )
                    ),
                    parallel_config=arcregionswitch.CfnPlan.ParallelExecutionBlockConfigurationProperty(
                        steps=[arcregionswitch.CfnPlan.StepProperty(
                            execution_block_configuration=execution_block_configuration_property_,
                            execution_block_type="executionBlockType",
                            name="name",
                
                            # the properties below are optional
                            description="description"
                        )]
                    ),
                    region_switch_plan_config=arcregionswitch.CfnPlan.RegionSwitchPlanConfigurationProperty(
                        arn="arn",
                
                        # the properties below are optional
                        cross_account_role="crossAccountRole",
                        external_id="externalId"
                    ),
                    route53_health_check_config=arcregionswitch.CfnPlan.Route53HealthCheckConfigurationProperty(
                        hosted_zone_id="hostedZoneId",
                        record_name="recordName",
                
                        # the properties below are optional
                        cross_account_role="crossAccountRole",
                        external_id="externalId",
                        record_sets=[arcregionswitch.CfnPlan.Route53ResourceRecordSetProperty(
                            record_set_identifier="recordSetIdentifier",
                            region="region"
                        )],
                        timeout_minutes=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf03412277ce24dfa861d02429118a5e512a97579dd1c299024e646c98c02098)
                check_type(argname="argument arc_routing_control_config", value=arc_routing_control_config, expected_type=type_hints["arc_routing_control_config"])
                check_type(argname="argument custom_action_lambda_config", value=custom_action_lambda_config, expected_type=type_hints["custom_action_lambda_config"])
                check_type(argname="argument ec2_asg_capacity_increase_config", value=ec2_asg_capacity_increase_config, expected_type=type_hints["ec2_asg_capacity_increase_config"])
                check_type(argname="argument ecs_capacity_increase_config", value=ecs_capacity_increase_config, expected_type=type_hints["ecs_capacity_increase_config"])
                check_type(argname="argument eks_resource_scaling_config", value=eks_resource_scaling_config, expected_type=type_hints["eks_resource_scaling_config"])
                check_type(argname="argument execution_approval_config", value=execution_approval_config, expected_type=type_hints["execution_approval_config"])
                check_type(argname="argument global_aurora_config", value=global_aurora_config, expected_type=type_hints["global_aurora_config"])
                check_type(argname="argument parallel_config", value=parallel_config, expected_type=type_hints["parallel_config"])
                check_type(argname="argument region_switch_plan_config", value=region_switch_plan_config, expected_type=type_hints["region_switch_plan_config"])
                check_type(argname="argument route53_health_check_config", value=route53_health_check_config, expected_type=type_hints["route53_health_check_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arc_routing_control_config is not None:
                self._values["arc_routing_control_config"] = arc_routing_control_config
            if custom_action_lambda_config is not None:
                self._values["custom_action_lambda_config"] = custom_action_lambda_config
            if ec2_asg_capacity_increase_config is not None:
                self._values["ec2_asg_capacity_increase_config"] = ec2_asg_capacity_increase_config
            if ecs_capacity_increase_config is not None:
                self._values["ecs_capacity_increase_config"] = ecs_capacity_increase_config
            if eks_resource_scaling_config is not None:
                self._values["eks_resource_scaling_config"] = eks_resource_scaling_config
            if execution_approval_config is not None:
                self._values["execution_approval_config"] = execution_approval_config
            if global_aurora_config is not None:
                self._values["global_aurora_config"] = global_aurora_config
            if parallel_config is not None:
                self._values["parallel_config"] = parallel_config
            if region_switch_plan_config is not None:
                self._values["region_switch_plan_config"] = region_switch_plan_config
            if route53_health_check_config is not None:
                self._values["route53_health_check_config"] = route53_health_check_config

        @builtins.property
        def arc_routing_control_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.ArcRoutingControlConfigurationProperty"]]:
            '''An ARC routing control execution block.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-executionblockconfiguration.html#cfn-arcregionswitch-plan-executionblockconfiguration-arcroutingcontrolconfig
            '''
            result = self._values.get("arc_routing_control_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.ArcRoutingControlConfigurationProperty"]], result)

        @builtins.property
        def custom_action_lambda_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.CustomActionLambdaConfigurationProperty"]]:
            '''An AWS Lambda execution block.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-executionblockconfiguration.html#cfn-arcregionswitch-plan-executionblockconfiguration-customactionlambdaconfig
            '''
            result = self._values.get("custom_action_lambda_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.CustomActionLambdaConfigurationProperty"]], result)

        @builtins.property
        def ec2_asg_capacity_increase_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.Ec2AsgCapacityIncreaseConfigurationProperty"]]:
            '''An EC2 Auto Scaling group execution block.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-executionblockconfiguration.html#cfn-arcregionswitch-plan-executionblockconfiguration-ec2asgcapacityincreaseconfig
            '''
            result = self._values.get("ec2_asg_capacity_increase_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.Ec2AsgCapacityIncreaseConfigurationProperty"]], result)

        @builtins.property
        def ecs_capacity_increase_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.EcsCapacityIncreaseConfigurationProperty"]]:
            '''The capacity increase specified for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-executionblockconfiguration.html#cfn-arcregionswitch-plan-executionblockconfiguration-ecscapacityincreaseconfig
            '''
            result = self._values.get("ecs_capacity_increase_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.EcsCapacityIncreaseConfigurationProperty"]], result)

        @builtins.property
        def eks_resource_scaling_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.EksResourceScalingConfigurationProperty"]]:
            '''An AWS EKS resource scaling execution block.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-executionblockconfiguration.html#cfn-arcregionswitch-plan-executionblockconfiguration-eksresourcescalingconfig
            '''
            result = self._values.get("eks_resource_scaling_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.EksResourceScalingConfigurationProperty"]], result)

        @builtins.property
        def execution_approval_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.ExecutionApprovalConfigurationProperty"]]:
            '''A manual approval execution block.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-executionblockconfiguration.html#cfn-arcregionswitch-plan-executionblockconfiguration-executionapprovalconfig
            '''
            result = self._values.get("execution_approval_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.ExecutionApprovalConfigurationProperty"]], result)

        @builtins.property
        def global_aurora_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.GlobalAuroraConfigurationProperty"]]:
            '''An Aurora Global Database execution block.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-executionblockconfiguration.html#cfn-arcregionswitch-plan-executionblockconfiguration-globalauroraconfig
            '''
            result = self._values.get("global_aurora_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.GlobalAuroraConfigurationProperty"]], result)

        @builtins.property
        def parallel_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.ParallelExecutionBlockConfigurationProperty"]]:
            '''A parallel configuration execution block.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-executionblockconfiguration.html#cfn-arcregionswitch-plan-executionblockconfiguration-parallelconfig
            '''
            result = self._values.get("parallel_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.ParallelExecutionBlockConfigurationProperty"]], result)

        @builtins.property
        def region_switch_plan_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.RegionSwitchPlanConfigurationProperty"]]:
            '''A Region switch plan execution block.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-executionblockconfiguration.html#cfn-arcregionswitch-plan-executionblockconfiguration-regionswitchplanconfig
            '''
            result = self._values.get("region_switch_plan_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.RegionSwitchPlanConfigurationProperty"]], result)

        @builtins.property
        def route53_health_check_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.Route53HealthCheckConfigurationProperty"]]:
            '''The Amazon Route 53 health check configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-executionblockconfiguration.html#cfn-arcregionswitch-plan-executionblockconfiguration-route53healthcheckconfig
            '''
            result = self._values.get("route53_health_check_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.Route53HealthCheckConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExecutionBlockConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.GlobalAuroraConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "behavior": "behavior",
            "database_cluster_arns": "databaseClusterArns",
            "global_cluster_identifier": "globalClusterIdentifier",
            "cross_account_role": "crossAccountRole",
            "external_id": "externalId",
            "timeout_minutes": "timeoutMinutes",
            "ungraceful": "ungraceful",
        },
    )
    class GlobalAuroraConfigurationProperty:
        def __init__(
            self,
            *,
            behavior: builtins.str,
            database_cluster_arns: typing.Sequence[builtins.str],
            global_cluster_identifier: builtins.str,
            cross_account_role: typing.Optional[builtins.str] = None,
            external_id: typing.Optional[builtins.str] = None,
            timeout_minutes: typing.Optional[jsii.Number] = None,
            ungraceful: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.GlobalAuroraUngracefulProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration for Amazon Aurora global databases used in a Region switch plan.

            :param behavior: The behavior for a global database, that is, only allow switchover or also allow failover.
            :param database_cluster_arns: The database cluster Amazon Resource Names (ARNs) for a global database.
            :param global_cluster_identifier: The global cluster identifier for a global database.
            :param cross_account_role: The cross account role for the configuration.
            :param external_id: The external ID (secret key) for the configuration.
            :param timeout_minutes: The timeout value specified for the configuration. Default: - 60
            :param ungraceful: The settings for ungraceful execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-globalauroraconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                global_aurora_configuration_property = arcregionswitch.CfnPlan.GlobalAuroraConfigurationProperty(
                    behavior="behavior",
                    database_cluster_arns=["databaseClusterArns"],
                    global_cluster_identifier="globalClusterIdentifier",
                
                    # the properties below are optional
                    cross_account_role="crossAccountRole",
                    external_id="externalId",
                    timeout_minutes=123,
                    ungraceful=arcregionswitch.CfnPlan.GlobalAuroraUngracefulProperty(
                        ungraceful="ungraceful"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e60aa2a866c67f15aa41619ecd129adf197a423c592e6f605c7713f6b5591f97)
                check_type(argname="argument behavior", value=behavior, expected_type=type_hints["behavior"])
                check_type(argname="argument database_cluster_arns", value=database_cluster_arns, expected_type=type_hints["database_cluster_arns"])
                check_type(argname="argument global_cluster_identifier", value=global_cluster_identifier, expected_type=type_hints["global_cluster_identifier"])
                check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
                check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
                check_type(argname="argument timeout_minutes", value=timeout_minutes, expected_type=type_hints["timeout_minutes"])
                check_type(argname="argument ungraceful", value=ungraceful, expected_type=type_hints["ungraceful"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "behavior": behavior,
                "database_cluster_arns": database_cluster_arns,
                "global_cluster_identifier": global_cluster_identifier,
            }
            if cross_account_role is not None:
                self._values["cross_account_role"] = cross_account_role
            if external_id is not None:
                self._values["external_id"] = external_id
            if timeout_minutes is not None:
                self._values["timeout_minutes"] = timeout_minutes
            if ungraceful is not None:
                self._values["ungraceful"] = ungraceful

        @builtins.property
        def behavior(self) -> builtins.str:
            '''The behavior for a global database, that is, only allow switchover or also allow failover.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-globalauroraconfiguration.html#cfn-arcregionswitch-plan-globalauroraconfiguration-behavior
            '''
            result = self._values.get("behavior")
            assert result is not None, "Required property 'behavior' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_cluster_arns(self) -> typing.List[builtins.str]:
            '''The database cluster Amazon Resource Names (ARNs) for a global database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-globalauroraconfiguration.html#cfn-arcregionswitch-plan-globalauroraconfiguration-databaseclusterarns
            '''
            result = self._values.get("database_cluster_arns")
            assert result is not None, "Required property 'database_cluster_arns' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def global_cluster_identifier(self) -> builtins.str:
            '''The global cluster identifier for a global database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-globalauroraconfiguration.html#cfn-arcregionswitch-plan-globalauroraconfiguration-globalclusteridentifier
            '''
            result = self._values.get("global_cluster_identifier")
            assert result is not None, "Required property 'global_cluster_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cross_account_role(self) -> typing.Optional[builtins.str]:
            '''The cross account role for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-globalauroraconfiguration.html#cfn-arcregionswitch-plan-globalauroraconfiguration-crossaccountrole
            '''
            result = self._values.get("cross_account_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID (secret key) for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-globalauroraconfiguration.html#cfn-arcregionswitch-plan-globalauroraconfiguration-externalid
            '''
            result = self._values.get("external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The timeout value specified for the configuration.

            :default: - 60

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-globalauroraconfiguration.html#cfn-arcregionswitch-plan-globalauroraconfiguration-timeoutminutes
            '''
            result = self._values.get("timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ungraceful(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.GlobalAuroraUngracefulProperty"]]:
            '''The settings for ungraceful execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-globalauroraconfiguration.html#cfn-arcregionswitch-plan-globalauroraconfiguration-ungraceful
            '''
            result = self._values.get("ungraceful")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPlan.GlobalAuroraUngracefulProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlobalAuroraConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.GlobalAuroraUngracefulProperty",
        jsii_struct_bases=[],
        name_mapping={"ungraceful": "ungraceful"},
    )
    class GlobalAuroraUngracefulProperty:
        def __init__(self, *, ungraceful: typing.Optional[builtins.str] = None) -> None:
            '''Configuration for handling failures when performing operations on Aurora global databases.

            :param ungraceful: The settings for ungraceful execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-globalauroraungraceful.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                global_aurora_ungraceful_property = arcregionswitch.CfnPlan.GlobalAuroraUngracefulProperty(
                    ungraceful="ungraceful"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8e95bf120b9c7191be2a0d5f0c8b6dc1fc6f89952abe27811996d58bf93ece46)
                check_type(argname="argument ungraceful", value=ungraceful, expected_type=type_hints["ungraceful"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ungraceful is not None:
                self._values["ungraceful"] = ungraceful

        @builtins.property
        def ungraceful(self) -> typing.Optional[builtins.str]:
            '''The settings for ungraceful execution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-globalauroraungraceful.html#cfn-arcregionswitch-plan-globalauroraungraceful-ungraceful
            '''
            result = self._values.get("ungraceful")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlobalAuroraUngracefulProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.HealthCheckStateProperty",
        jsii_struct_bases=[],
        name_mapping={"health_check_id": "healthCheckId", "region": "region"},
    )
    class HealthCheckStateProperty:
        def __init__(
            self,
            *,
            health_check_id: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param health_check_id: 
            :param region: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-healthcheckstate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                health_check_state_property = arcregionswitch.CfnPlan.HealthCheckStateProperty(
                    health_check_id="healthCheckId",
                    region="region"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7f6f9eab294a354253a8235a964459afdc89f8904dc974eac694bcd815c8a40c)
                check_type(argname="argument health_check_id", value=health_check_id, expected_type=type_hints["health_check_id"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if health_check_id is not None:
                self._values["health_check_id"] = health_check_id
            if region is not None:
                self._values["region"] = region

        @builtins.property
        def health_check_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-healthcheckstate.html#cfn-arcregionswitch-plan-healthcheckstate-healthcheckid
            '''
            result = self._values.get("health_check_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-healthcheckstate.html#cfn-arcregionswitch-plan-healthcheckstate-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HealthCheckStateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.KubernetesResourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={"api_version": "apiVersion", "kind": "kind"},
    )
    class KubernetesResourceTypeProperty:
        def __init__(self, *, api_version: builtins.str, kind: builtins.str) -> None:
            '''Defines the type of Kubernetes resource to scale in an Amazon EKS cluster.

            :param api_version: The API version type for the Kubernetes resource.
            :param kind: The kind for the Kubernetes resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-kubernetesresourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                kubernetes_resource_type_property = arcregionswitch.CfnPlan.KubernetesResourceTypeProperty(
                    api_version="apiVersion",
                    kind="kind"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c232ba08af7c15b406e994864bd91ccf5d92d9076e59f172c6103cf5e3ca4b41)
                check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
                check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "api_version": api_version,
                "kind": kind,
            }

        @builtins.property
        def api_version(self) -> builtins.str:
            '''The API version type for the Kubernetes resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-kubernetesresourcetype.html#cfn-arcregionswitch-plan-kubernetesresourcetype-apiversion
            '''
            result = self._values.get("api_version")
            assert result is not None, "Required property 'api_version' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kind(self) -> builtins.str:
            '''The kind for the Kubernetes resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-kubernetesresourcetype.html#cfn-arcregionswitch-plan-kubernetesresourcetype-kind
            '''
            result = self._values.get("kind")
            assert result is not None, "Required property 'kind' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KubernetesResourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.KubernetesScalingResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "namespace": "namespace", "hpa_name": "hpaName"},
    )
    class KubernetesScalingResourceProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            namespace: builtins.str,
            hpa_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines a Kubernetes resource to scale in an Amazon EKS cluster.

            :param name: The name for the Kubernetes resource.
            :param namespace: The namespace for the Kubernetes resource.
            :param hpa_name: The hpaname for the Kubernetes resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-kubernetesscalingresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                kubernetes_scaling_resource_property = arcregionswitch.CfnPlan.KubernetesScalingResourceProperty(
                    name="name",
                    namespace="namespace",
                
                    # the properties below are optional
                    hpa_name="hpaName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__57d18eef9bff8e63ac0c26d15b57916fe933491b47893043399d20a15098730f)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
                check_type(argname="argument hpa_name", value=hpa_name, expected_type=type_hints["hpa_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "namespace": namespace,
            }
            if hpa_name is not None:
                self._values["hpa_name"] = hpa_name

        @builtins.property
        def name(self) -> builtins.str:
            '''The name for the Kubernetes resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-kubernetesscalingresource.html#cfn-arcregionswitch-plan-kubernetesscalingresource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def namespace(self) -> builtins.str:
            '''The namespace for the Kubernetes resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-kubernetesscalingresource.html#cfn-arcregionswitch-plan-kubernetesscalingresource-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hpa_name(self) -> typing.Optional[builtins.str]:
            '''The hpaname for the Kubernetes resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-kubernetesscalingresource.html#cfn-arcregionswitch-plan-kubernetesscalingresource-hpaname
            '''
            result = self._values.get("hpa_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KubernetesScalingResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.LambdaUngracefulProperty",
        jsii_struct_bases=[],
        name_mapping={"behavior": "behavior"},
    )
    class LambdaUngracefulProperty:
        def __init__(self, *, behavior: typing.Optional[builtins.str] = None) -> None:
            '''Configuration for handling failures when invoking Lambda functions.

            :param behavior: The ungraceful behavior for a Lambda function, which must be set to ``skip`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-lambdaungraceful.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                lambda_ungraceful_property = arcregionswitch.CfnPlan.LambdaUngracefulProperty(
                    behavior="behavior"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f24eea14fa20d551f2fa4c3eb9c17bb8bd884082806add21df6612279fc0da30)
                check_type(argname="argument behavior", value=behavior, expected_type=type_hints["behavior"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if behavior is not None:
                self._values["behavior"] = behavior

        @builtins.property
        def behavior(self) -> typing.Optional[builtins.str]:
            '''The ungraceful behavior for a Lambda function, which must be set to ``skip`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-lambdaungraceful.html#cfn-arcregionswitch-plan-lambdaungraceful-behavior
            '''
            result = self._values.get("behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaUngracefulProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.LambdasProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "cross_account_role": "crossAccountRole",
            "external_id": "externalId",
        },
    )
    class LambdasProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            cross_account_role: typing.Optional[builtins.str] = None,
            external_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration for AWS Lambda functions used in a Region switch plan.

            :param arn: The Amazon Resource Name (ARN) of the Lambda function.
            :param cross_account_role: The cross account role for the configuration.
            :param external_id: The external ID (secret key) for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-lambdas.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                lambdas_property = arcregionswitch.CfnPlan.LambdasProperty(
                    arn="arn",
                    cross_account_role="crossAccountRole",
                    external_id="externalId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__382b21febb492930836b8663cd8745c59e5e805caa04c745c3509c5beda2a1ac)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
                check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if cross_account_role is not None:
                self._values["cross_account_role"] = cross_account_role
            if external_id is not None:
                self._values["external_id"] = external_id

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-lambdas.html#cfn-arcregionswitch-plan-lambdas-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cross_account_role(self) -> typing.Optional[builtins.str]:
            '''The cross account role for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-lambdas.html#cfn-arcregionswitch-plan-lambdas-crossaccountrole
            '''
            result = self._values.get("cross_account_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID (secret key) for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-lambdas.html#cfn-arcregionswitch-plan-lambdas-externalid
            '''
            result = self._values.get("external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdasProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.ParallelExecutionBlockConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"steps": "steps"},
    )
    class ParallelExecutionBlockConfigurationProperty:
        def __init__(
            self,
            *,
            steps: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.StepProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Configuration for steps that should be executed in parallel during a Region switch.

            :param steps: The steps for a parallel execution block.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-parallelexecutionblockconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                # parallel_execution_block_configuration_property_: arcregionswitch.CfnPlan.ParallelExecutionBlockConfigurationProperty
                
                parallel_execution_block_configuration_property = arcregionswitch.CfnPlan.ParallelExecutionBlockConfigurationProperty(
                    steps=[arcregionswitch.CfnPlan.StepProperty(
                        execution_block_configuration=arcregionswitch.CfnPlan.ExecutionBlockConfigurationProperty(
                            arc_routing_control_config=arcregionswitch.CfnPlan.ArcRoutingControlConfigurationProperty(
                                region_and_routing_controls={
                                    "region_and_routing_controls_key": [arcregionswitch.CfnPlan.ArcRoutingControlStateProperty(
                                        routing_control_arn="routingControlArn",
                                        state="state"
                                    )]
                                },
                
                                # the properties below are optional
                                cross_account_role="crossAccountRole",
                                external_id="externalId",
                                timeout_minutes=123
                            ),
                            custom_action_lambda_config=arcregionswitch.CfnPlan.CustomActionLambdaConfigurationProperty(
                                lambdas=[arcregionswitch.CfnPlan.LambdasProperty(
                                    arn="arn",
                                    cross_account_role="crossAccountRole",
                                    external_id="externalId"
                                )],
                                region_to_run="regionToRun",
                                retry_interval_minutes=123,
                
                                # the properties below are optional
                                timeout_minutes=123,
                                ungraceful=arcregionswitch.CfnPlan.LambdaUngracefulProperty(
                                    behavior="behavior"
                                )
                            ),
                            ec2_asg_capacity_increase_config=arcregionswitch.CfnPlan.Ec2AsgCapacityIncreaseConfigurationProperty(
                                asgs=[arcregionswitch.CfnPlan.AsgProperty(
                                    arn="arn",
                                    cross_account_role="crossAccountRole",
                                    external_id="externalId"
                                )],
                
                                # the properties below are optional
                                capacity_monitoring_approach="capacityMonitoringApproach",
                                target_percent=123,
                                timeout_minutes=123,
                                ungraceful=arcregionswitch.CfnPlan.Ec2UngracefulProperty(
                                    minimum_success_percentage=123
                                )
                            ),
                            ecs_capacity_increase_config=arcregionswitch.CfnPlan.EcsCapacityIncreaseConfigurationProperty(
                                services=[arcregionswitch.CfnPlan.ServiceProperty(
                                    cluster_arn="clusterArn",
                                    cross_account_role="crossAccountRole",
                                    external_id="externalId",
                                    service_arn="serviceArn"
                                )],
                
                                # the properties below are optional
                                capacity_monitoring_approach="capacityMonitoringApproach",
                                target_percent=123,
                                timeout_minutes=123,
                                ungraceful=arcregionswitch.CfnPlan.EcsUngracefulProperty(
                                    minimum_success_percentage=123
                                )
                            ),
                            eks_resource_scaling_config=arcregionswitch.CfnPlan.EksResourceScalingConfigurationProperty(
                                kubernetes_resource_type=arcregionswitch.CfnPlan.KubernetesResourceTypeProperty(
                                    api_version="apiVersion",
                                    kind="kind"
                                ),
                
                                # the properties below are optional
                                capacity_monitoring_approach="capacityMonitoringApproach",
                                eks_clusters=[arcregionswitch.CfnPlan.EksClusterProperty(
                                    cluster_arn="clusterArn",
                
                                    # the properties below are optional
                                    cross_account_role="crossAccountRole",
                                    external_id="externalId"
                                )],
                                scaling_resources=[{
                                    "scaling_resources_key": {
                                        "scaling_resources_key": arcregionswitch.CfnPlan.KubernetesScalingResourceProperty(
                                            name="name",
                                            namespace="namespace",
                
                                            # the properties below are optional
                                            hpa_name="hpaName"
                                        )
                                    }
                                }],
                                target_percent=123,
                                timeout_minutes=123,
                                ungraceful=arcregionswitch.CfnPlan.EksResourceScalingUngracefulProperty(
                                    minimum_success_percentage=123
                                )
                            ),
                            execution_approval_config=arcregionswitch.CfnPlan.ExecutionApprovalConfigurationProperty(
                                approval_role="approvalRole",
                
                                # the properties below are optional
                                timeout_minutes=123
                            ),
                            global_aurora_config=arcregionswitch.CfnPlan.GlobalAuroraConfigurationProperty(
                                behavior="behavior",
                                database_cluster_arns=["databaseClusterArns"],
                                global_cluster_identifier="globalClusterIdentifier",
                
                                # the properties below are optional
                                cross_account_role="crossAccountRole",
                                external_id="externalId",
                                timeout_minutes=123,
                                ungraceful=arcregionswitch.CfnPlan.GlobalAuroraUngracefulProperty(
                                    ungraceful="ungraceful"
                                )
                            ),
                            parallel_config=parallel_execution_block_configuration_property_,
                            region_switch_plan_config=arcregionswitch.CfnPlan.RegionSwitchPlanConfigurationProperty(
                                arn="arn",
                
                                # the properties below are optional
                                cross_account_role="crossAccountRole",
                                external_id="externalId"
                            ),
                            route53_health_check_config=arcregionswitch.CfnPlan.Route53HealthCheckConfigurationProperty(
                                hosted_zone_id="hostedZoneId",
                                record_name="recordName",
                
                                # the properties below are optional
                                cross_account_role="crossAccountRole",
                                external_id="externalId",
                                record_sets=[arcregionswitch.CfnPlan.Route53ResourceRecordSetProperty(
                                    record_set_identifier="recordSetIdentifier",
                                    region="region"
                                )],
                                timeout_minutes=123
                            )
                        ),
                        execution_block_type="executionBlockType",
                        name="name",
                
                        # the properties below are optional
                        description="description"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__15563430da8134fdc062f2fae765097f644a784a2fe1b26fc67f62716996ef69)
                check_type(argname="argument steps", value=steps, expected_type=type_hints["steps"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "steps": steps,
            }

        @builtins.property
        def steps(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.StepProperty"]]]:
            '''The steps for a parallel execution block.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-parallelexecutionblockconfiguration.html#cfn-arcregionswitch-plan-parallelexecutionblockconfiguration-steps
            '''
            result = self._values.get("steps")
            assert result is not None, "Required property 'steps' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.StepProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParallelExecutionBlockConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.RegionSwitchPlanConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "cross_account_role": "crossAccountRole",
            "external_id": "externalId",
        },
    )
    class RegionSwitchPlanConfigurationProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            cross_account_role: typing.Optional[builtins.str] = None,
            external_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration for nested Region switch plans.

            This allows one Region switch plan to trigger another plan as part of its execution.

            :param arn: The Amazon Resource Name (ARN) of the plan configuration.
            :param cross_account_role: The cross account role for the configuration.
            :param external_id: The external ID (secret key) for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-regionswitchplanconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                region_switch_plan_configuration_property = arcregionswitch.CfnPlan.RegionSwitchPlanConfigurationProperty(
                    arn="arn",
                
                    # the properties below are optional
                    cross_account_role="crossAccountRole",
                    external_id="externalId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c7f4d6ccde8e09198d4b7a9cf491066654de4ce1eae2ba3efd23e437a7c7b59a)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
                check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "arn": arn,
            }
            if cross_account_role is not None:
                self._values["cross_account_role"] = cross_account_role
            if external_id is not None:
                self._values["external_id"] = external_id

        @builtins.property
        def arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the plan configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-regionswitchplanconfiguration.html#cfn-arcregionswitch-plan-regionswitchplanconfiguration-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cross_account_role(self) -> typing.Optional[builtins.str]:
            '''The cross account role for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-regionswitchplanconfiguration.html#cfn-arcregionswitch-plan-regionswitchplanconfiguration-crossaccountrole
            '''
            result = self._values.get("cross_account_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID (secret key) for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-regionswitchplanconfiguration.html#cfn-arcregionswitch-plan-regionswitchplanconfiguration-externalid
            '''
            result = self._values.get("external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegionSwitchPlanConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.Route53HealthCheckConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hosted_zone_id": "hostedZoneId",
            "record_name": "recordName",
            "cross_account_role": "crossAccountRole",
            "external_id": "externalId",
            "record_sets": "recordSets",
            "timeout_minutes": "timeoutMinutes",
        },
    )
    class Route53HealthCheckConfigurationProperty:
        def __init__(
            self,
            *,
            hosted_zone_id: builtins.str,
            record_name: builtins.str,
            cross_account_role: typing.Optional[builtins.str] = None,
            external_id: typing.Optional[builtins.str] = None,
            record_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.Route53ResourceRecordSetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            timeout_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The Amazon Route 53 health check configuration.

            :param hosted_zone_id: The Amazon Route 53 health check configuration hosted zone ID.
            :param record_name: The Amazon Route 53 health check configuration record name.
            :param cross_account_role: The cross account role for the configuration.
            :param external_id: The external ID (secret key) for the configuration.
            :param record_sets: The Amazon Route 53 health check configuration record sets.
            :param timeout_minutes: The Amazon Route 53 health check configuration time out (in minutes). Default: - 60

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-route53healthcheckconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                route53_health_check_configuration_property = arcregionswitch.CfnPlan.Route53HealthCheckConfigurationProperty(
                    hosted_zone_id="hostedZoneId",
                    record_name="recordName",
                
                    # the properties below are optional
                    cross_account_role="crossAccountRole",
                    external_id="externalId",
                    record_sets=[arcregionswitch.CfnPlan.Route53ResourceRecordSetProperty(
                        record_set_identifier="recordSetIdentifier",
                        region="region"
                    )],
                    timeout_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dafd3d15027013dc86ea477c0cc06ceb95b9df4585b699565ae5446c3cbc6845)
                check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
                check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
                check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
                check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
                check_type(argname="argument record_sets", value=record_sets, expected_type=type_hints["record_sets"])
                check_type(argname="argument timeout_minutes", value=timeout_minutes, expected_type=type_hints["timeout_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "hosted_zone_id": hosted_zone_id,
                "record_name": record_name,
            }
            if cross_account_role is not None:
                self._values["cross_account_role"] = cross_account_role
            if external_id is not None:
                self._values["external_id"] = external_id
            if record_sets is not None:
                self._values["record_sets"] = record_sets
            if timeout_minutes is not None:
                self._values["timeout_minutes"] = timeout_minutes

        @builtins.property
        def hosted_zone_id(self) -> builtins.str:
            '''The Amazon Route 53 health check configuration hosted zone ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-route53healthcheckconfiguration.html#cfn-arcregionswitch-plan-route53healthcheckconfiguration-hostedzoneid
            '''
            result = self._values.get("hosted_zone_id")
            assert result is not None, "Required property 'hosted_zone_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def record_name(self) -> builtins.str:
            '''The Amazon Route 53 health check configuration record name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-route53healthcheckconfiguration.html#cfn-arcregionswitch-plan-route53healthcheckconfiguration-recordname
            '''
            result = self._values.get("record_name")
            assert result is not None, "Required property 'record_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cross_account_role(self) -> typing.Optional[builtins.str]:
            '''The cross account role for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-route53healthcheckconfiguration.html#cfn-arcregionswitch-plan-route53healthcheckconfiguration-crossaccountrole
            '''
            result = self._values.get("cross_account_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID (secret key) for the configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-route53healthcheckconfiguration.html#cfn-arcregionswitch-plan-route53healthcheckconfiguration-externalid
            '''
            result = self._values.get("external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def record_sets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.Route53ResourceRecordSetProperty"]]]]:
            '''The Amazon Route 53 health check configuration record sets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-route53healthcheckconfiguration.html#cfn-arcregionswitch-plan-route53healthcheckconfiguration-recordsets
            '''
            result = self._values.get("record_sets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.Route53ResourceRecordSetProperty"]]]], result)

        @builtins.property
        def timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The Amazon Route 53 health check configuration time out (in minutes).

            :default: - 60

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-route53healthcheckconfiguration.html#cfn-arcregionswitch-plan-route53healthcheckconfiguration-timeoutminutes
            '''
            result = self._values.get("timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Route53HealthCheckConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.Route53ResourceRecordSetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "record_set_identifier": "recordSetIdentifier",
            "region": "region",
        },
    )
    class Route53ResourceRecordSetProperty:
        def __init__(
            self,
            *,
            record_set_identifier: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Amazon Route 53 record set.

            :param record_set_identifier: The Amazon Route 53 record set identifier.
            :param region: The Amazon Route 53 record set Region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-route53resourcerecordset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                route53_resource_record_set_property = arcregionswitch.CfnPlan.Route53ResourceRecordSetProperty(
                    record_set_identifier="recordSetIdentifier",
                    region="region"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0e8634f5bf0466b7e8441b8a091ba90aa68f8785fca863c7422c0f356bcd7c6f)
                check_type(argname="argument record_set_identifier", value=record_set_identifier, expected_type=type_hints["record_set_identifier"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if record_set_identifier is not None:
                self._values["record_set_identifier"] = record_set_identifier
            if region is not None:
                self._values["region"] = region

        @builtins.property
        def record_set_identifier(self) -> typing.Optional[builtins.str]:
            '''The Amazon Route 53 record set identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-route53resourcerecordset.html#cfn-arcregionswitch-plan-route53resourcerecordset-recordsetidentifier
            '''
            result = self._values.get("record_set_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''The Amazon Route 53 record set Region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-route53resourcerecordset.html#cfn-arcregionswitch-plan-route53resourcerecordset-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Route53ResourceRecordSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.ServiceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cluster_arn": "clusterArn",
            "cross_account_role": "crossAccountRole",
            "external_id": "externalId",
            "service_arn": "serviceArn",
        },
    )
    class ServiceProperty:
        def __init__(
            self,
            *,
            cluster_arn: typing.Optional[builtins.str] = None,
            cross_account_role: typing.Optional[builtins.str] = None,
            external_id: typing.Optional[builtins.str] = None,
            service_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The service for a cross account role.

            :param cluster_arn: The cluster Amazon Resource Name (ARN) for a service.
            :param cross_account_role: The cross account role for a service.
            :param external_id: The external ID (secret key) for the service.
            :param service_arn: The Amazon Resource Name (ARN) for a service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-service.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                service_property = arcregionswitch.CfnPlan.ServiceProperty(
                    cluster_arn="clusterArn",
                    cross_account_role="crossAccountRole",
                    external_id="externalId",
                    service_arn="serviceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__66163b57e8e8c71356b0aea432dd64d08666ca8cad746cff30bddd456c91458e)
                check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
                check_type(argname="argument cross_account_role", value=cross_account_role, expected_type=type_hints["cross_account_role"])
                check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
                check_type(argname="argument service_arn", value=service_arn, expected_type=type_hints["service_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cluster_arn is not None:
                self._values["cluster_arn"] = cluster_arn
            if cross_account_role is not None:
                self._values["cross_account_role"] = cross_account_role
            if external_id is not None:
                self._values["external_id"] = external_id
            if service_arn is not None:
                self._values["service_arn"] = service_arn

        @builtins.property
        def cluster_arn(self) -> typing.Optional[builtins.str]:
            '''The cluster Amazon Resource Name (ARN) for a service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-service.html#cfn-arcregionswitch-plan-service-clusterarn
            '''
            result = self._values.get("cluster_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cross_account_role(self) -> typing.Optional[builtins.str]:
            '''The cross account role for a service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-service.html#cfn-arcregionswitch-plan-service-crossaccountrole
            '''
            result = self._values.get("cross_account_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def external_id(self) -> typing.Optional[builtins.str]:
            '''The external ID (secret key) for the service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-service.html#cfn-arcregionswitch-plan-service-externalid
            '''
            result = self._values.get("external_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for a service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-service.html#cfn-arcregionswitch-plan-service-servicearn
            '''
            result = self._values.get("service_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.StepProperty",
        jsii_struct_bases=[],
        name_mapping={
            "execution_block_configuration": "executionBlockConfiguration",
            "execution_block_type": "executionBlockType",
            "name": "name",
            "description": "description",
        },
    )
    class StepProperty:
        def __init__(
            self,
            *,
            execution_block_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.ExecutionBlockConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            execution_block_type: builtins.str,
            name: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents a step in a Region switch plan workflow.

            Each step performs a specific action during the Region switch process.

            :param execution_block_configuration: The configuration for an execution block in a workflow.
            :param execution_block_type: The type of an execution block in a workflow.
            :param name: The name of a step in a workflow.
            :param description: The description of a step in a workflow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-step.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                # step_property_: arcregionswitch.CfnPlan.StepProperty
                
                step_property = arcregionswitch.CfnPlan.StepProperty(
                    execution_block_configuration=arcregionswitch.CfnPlan.ExecutionBlockConfigurationProperty(
                        arc_routing_control_config=arcregionswitch.CfnPlan.ArcRoutingControlConfigurationProperty(
                            region_and_routing_controls={
                                "region_and_routing_controls_key": [arcregionswitch.CfnPlan.ArcRoutingControlStateProperty(
                                    routing_control_arn="routingControlArn",
                                    state="state"
                                )]
                            },
                
                            # the properties below are optional
                            cross_account_role="crossAccountRole",
                            external_id="externalId",
                            timeout_minutes=123
                        ),
                        custom_action_lambda_config=arcregionswitch.CfnPlan.CustomActionLambdaConfigurationProperty(
                            lambdas=[arcregionswitch.CfnPlan.LambdasProperty(
                                arn="arn",
                                cross_account_role="crossAccountRole",
                                external_id="externalId"
                            )],
                            region_to_run="regionToRun",
                            retry_interval_minutes=123,
                
                            # the properties below are optional
                            timeout_minutes=123,
                            ungraceful=arcregionswitch.CfnPlan.LambdaUngracefulProperty(
                                behavior="behavior"
                            )
                        ),
                        ec2_asg_capacity_increase_config=arcregionswitch.CfnPlan.Ec2AsgCapacityIncreaseConfigurationProperty(
                            asgs=[arcregionswitch.CfnPlan.AsgProperty(
                                arn="arn",
                                cross_account_role="crossAccountRole",
                                external_id="externalId"
                            )],
                
                            # the properties below are optional
                            capacity_monitoring_approach="capacityMonitoringApproach",
                            target_percent=123,
                            timeout_minutes=123,
                            ungraceful=arcregionswitch.CfnPlan.Ec2UngracefulProperty(
                                minimum_success_percentage=123
                            )
                        ),
                        ecs_capacity_increase_config=arcregionswitch.CfnPlan.EcsCapacityIncreaseConfigurationProperty(
                            services=[arcregionswitch.CfnPlan.ServiceProperty(
                                cluster_arn="clusterArn",
                                cross_account_role="crossAccountRole",
                                external_id="externalId",
                                service_arn="serviceArn"
                            )],
                
                            # the properties below are optional
                            capacity_monitoring_approach="capacityMonitoringApproach",
                            target_percent=123,
                            timeout_minutes=123,
                            ungraceful=arcregionswitch.CfnPlan.EcsUngracefulProperty(
                                minimum_success_percentage=123
                            )
                        ),
                        eks_resource_scaling_config=arcregionswitch.CfnPlan.EksResourceScalingConfigurationProperty(
                            kubernetes_resource_type=arcregionswitch.CfnPlan.KubernetesResourceTypeProperty(
                                api_version="apiVersion",
                                kind="kind"
                            ),
                
                            # the properties below are optional
                            capacity_monitoring_approach="capacityMonitoringApproach",
                            eks_clusters=[arcregionswitch.CfnPlan.EksClusterProperty(
                                cluster_arn="clusterArn",
                
                                # the properties below are optional
                                cross_account_role="crossAccountRole",
                                external_id="externalId"
                            )],
                            scaling_resources=[{
                                "scaling_resources_key": {
                                    "scaling_resources_key": arcregionswitch.CfnPlan.KubernetesScalingResourceProperty(
                                        name="name",
                                        namespace="namespace",
                
                                        # the properties below are optional
                                        hpa_name="hpaName"
                                    )
                                }
                            }],
                            target_percent=123,
                            timeout_minutes=123,
                            ungraceful=arcregionswitch.CfnPlan.EksResourceScalingUngracefulProperty(
                                minimum_success_percentage=123
                            )
                        ),
                        execution_approval_config=arcregionswitch.CfnPlan.ExecutionApprovalConfigurationProperty(
                            approval_role="approvalRole",
                
                            # the properties below are optional
                            timeout_minutes=123
                        ),
                        global_aurora_config=arcregionswitch.CfnPlan.GlobalAuroraConfigurationProperty(
                            behavior="behavior",
                            database_cluster_arns=["databaseClusterArns"],
                            global_cluster_identifier="globalClusterIdentifier",
                
                            # the properties below are optional
                            cross_account_role="crossAccountRole",
                            external_id="externalId",
                            timeout_minutes=123,
                            ungraceful=arcregionswitch.CfnPlan.GlobalAuroraUngracefulProperty(
                                ungraceful="ungraceful"
                            )
                        ),
                        parallel_config=arcregionswitch.CfnPlan.ParallelExecutionBlockConfigurationProperty(
                            steps=[step_property_]
                        ),
                        region_switch_plan_config=arcregionswitch.CfnPlan.RegionSwitchPlanConfigurationProperty(
                            arn="arn",
                
                            # the properties below are optional
                            cross_account_role="crossAccountRole",
                            external_id="externalId"
                        ),
                        route53_health_check_config=arcregionswitch.CfnPlan.Route53HealthCheckConfigurationProperty(
                            hosted_zone_id="hostedZoneId",
                            record_name="recordName",
                
                            # the properties below are optional
                            cross_account_role="crossAccountRole",
                            external_id="externalId",
                            record_sets=[arcregionswitch.CfnPlan.Route53ResourceRecordSetProperty(
                                record_set_identifier="recordSetIdentifier",
                                region="region"
                            )],
                            timeout_minutes=123
                        )
                    ),
                    execution_block_type="executionBlockType",
                    name="name",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__66452e7d3703fa7367742b516ac3b5d497cf9255f69c7e6fe3f2f69ac8e95139)
                check_type(argname="argument execution_block_configuration", value=execution_block_configuration, expected_type=type_hints["execution_block_configuration"])
                check_type(argname="argument execution_block_type", value=execution_block_type, expected_type=type_hints["execution_block_type"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "execution_block_configuration": execution_block_configuration,
                "execution_block_type": execution_block_type,
                "name": name,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def execution_block_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnPlan.ExecutionBlockConfigurationProperty"]:
            '''The configuration for an execution block in a workflow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-step.html#cfn-arcregionswitch-plan-step-executionblockconfiguration
            '''
            result = self._values.get("execution_block_configuration")
            assert result is not None, "Required property 'execution_block_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPlan.ExecutionBlockConfigurationProperty"], result)

        @builtins.property
        def execution_block_type(self) -> builtins.str:
            '''The type of an execution block in a workflow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-step.html#cfn-arcregionswitch-plan-step-executionblocktype
            '''
            result = self._values.get("execution_block_type")
            assert result is not None, "Required property 'execution_block_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of a step in a workflow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-step.html#cfn-arcregionswitch-plan-step-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of a step in a workflow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-step.html#cfn-arcregionswitch-plan-step-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StepProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.TriggerConditionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "associated_alarm_name": "associatedAlarmName",
            "condition": "condition",
        },
    )
    class TriggerConditionProperty:
        def __init__(
            self,
            *,
            associated_alarm_name: builtins.str,
            condition: builtins.str,
        ) -> None:
            '''Defines a condition that must be met for a trigger to fire.

            :param associated_alarm_name: The name of the CloudWatch alarm associated with the condition.
            :param condition: The condition that must be met. Valid values include ALARM and OK.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-triggercondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                trigger_condition_property = arcregionswitch.CfnPlan.TriggerConditionProperty(
                    associated_alarm_name="associatedAlarmName",
                    condition="condition"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d58de4e5ff54abd141b94ef01a4e2b8cf9048e2704fc1718134ab6d7ac32e19d)
                check_type(argname="argument associated_alarm_name", value=associated_alarm_name, expected_type=type_hints["associated_alarm_name"])
                check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "associated_alarm_name": associated_alarm_name,
                "condition": condition,
            }

        @builtins.property
        def associated_alarm_name(self) -> builtins.str:
            '''The name of the CloudWatch alarm associated with the condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-triggercondition.html#cfn-arcregionswitch-plan-triggercondition-associatedalarmname
            '''
            result = self._values.get("associated_alarm_name")
            assert result is not None, "Required property 'associated_alarm_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def condition(self) -> builtins.str:
            '''The condition that must be met.

            Valid values include ALARM and OK.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-triggercondition.html#cfn-arcregionswitch-plan-triggercondition-condition
            '''
            result = self._values.get("condition")
            assert result is not None, "Required property 'condition' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggerConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.TriggerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "conditions": "conditions",
            "min_delay_minutes_between_executions": "minDelayMinutesBetweenExecutions",
            "target_region": "targetRegion",
            "description": "description",
        },
    )
    class TriggerProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            conditions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.TriggerConditionProperty", typing.Dict[builtins.str, typing.Any]]]]],
            min_delay_minutes_between_executions: jsii.Number,
            target_region: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines a condition that can automatically trigger the execution of a Region switch plan.

            :param action: The action to perform when the trigger fires. Valid values include ACTIVATE and DEACTIVATE.
            :param conditions: The conditions that must be met for the trigger to fire.
            :param min_delay_minutes_between_executions: The minimum time, in minutes, that must elapse between automatic executions of the plan.
            :param target_region: The AWS Region for a trigger.
            :param description: The description for a trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-trigger.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                trigger_property = arcregionswitch.CfnPlan.TriggerProperty(
                    action="action",
                    conditions=[arcregionswitch.CfnPlan.TriggerConditionProperty(
                        associated_alarm_name="associatedAlarmName",
                        condition="condition"
                    )],
                    min_delay_minutes_between_executions=123,
                    target_region="targetRegion",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9bf5e3ac00f2b2ce74567b08c3450d613dd5d1b8ff69e8e715177408109021fb)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
                check_type(argname="argument min_delay_minutes_between_executions", value=min_delay_minutes_between_executions, expected_type=type_hints["min_delay_minutes_between_executions"])
                check_type(argname="argument target_region", value=target_region, expected_type=type_hints["target_region"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "conditions": conditions,
                "min_delay_minutes_between_executions": min_delay_minutes_between_executions,
                "target_region": target_region,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def action(self) -> builtins.str:
            '''The action to perform when the trigger fires.

            Valid values include ACTIVATE and DEACTIVATE.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-trigger.html#cfn-arcregionswitch-plan-trigger-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def conditions(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.TriggerConditionProperty"]]]:
            '''The conditions that must be met for the trigger to fire.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-trigger.html#cfn-arcregionswitch-plan-trigger-conditions
            '''
            result = self._values.get("conditions")
            assert result is not None, "Required property 'conditions' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.TriggerConditionProperty"]]], result)

        @builtins.property
        def min_delay_minutes_between_executions(self) -> jsii.Number:
            '''The minimum time, in minutes, that must elapse between automatic executions of the plan.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-trigger.html#cfn-arcregionswitch-plan-trigger-mindelayminutesbetweenexecutions
            '''
            result = self._values.get("min_delay_minutes_between_executions")
            assert result is not None, "Required property 'min_delay_minutes_between_executions' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def target_region(self) -> builtins.str:
            '''The AWS Region for a trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-trigger.html#cfn-arcregionswitch-plan-trigger-targetregion
            '''
            result = self._values.get("target_region")
            assert result is not None, "Required property 'target_region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description for a trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-trigger.html#cfn-arcregionswitch-plan-trigger-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlan.WorkflowProperty",
        jsii_struct_bases=[],
        name_mapping={
            "workflow_target_action": "workflowTargetAction",
            "steps": "steps",
            "workflow_description": "workflowDescription",
            "workflow_target_region": "workflowTargetRegion",
        },
    )
    class WorkflowProperty:
        def __init__(
            self,
            *,
            workflow_target_action: builtins.str,
            steps: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPlan.StepProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            workflow_description: typing.Optional[builtins.str] = None,
            workflow_target_region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents a workflow in a Region switch plan.

            A workflow defines a sequence of steps to execute during a Region switch.

            :param workflow_target_action: The action that the workflow performs. Valid values include ACTIVATE and DEACTIVATE.
            :param steps: The steps that make up the workflow.
            :param workflow_description: The description of the workflow.
            :param workflow_target_region: The AWS Region that the workflow targets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-workflow.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arcregionswitch as arcregionswitch
                
                # step_property_: arcregionswitch.CfnPlan.StepProperty
                
                workflow_property = arcregionswitch.CfnPlan.WorkflowProperty(
                    workflow_target_action="workflowTargetAction",
                
                    # the properties below are optional
                    steps=[arcregionswitch.CfnPlan.StepProperty(
                        execution_block_configuration=arcregionswitch.CfnPlan.ExecutionBlockConfigurationProperty(
                            arc_routing_control_config=arcregionswitch.CfnPlan.ArcRoutingControlConfigurationProperty(
                                region_and_routing_controls={
                                    "region_and_routing_controls_key": [arcregionswitch.CfnPlan.ArcRoutingControlStateProperty(
                                        routing_control_arn="routingControlArn",
                                        state="state"
                                    )]
                                },
                
                                # the properties below are optional
                                cross_account_role="crossAccountRole",
                                external_id="externalId",
                                timeout_minutes=123
                            ),
                            custom_action_lambda_config=arcregionswitch.CfnPlan.CustomActionLambdaConfigurationProperty(
                                lambdas=[arcregionswitch.CfnPlan.LambdasProperty(
                                    arn="arn",
                                    cross_account_role="crossAccountRole",
                                    external_id="externalId"
                                )],
                                region_to_run="regionToRun",
                                retry_interval_minutes=123,
                
                                # the properties below are optional
                                timeout_minutes=123,
                                ungraceful=arcregionswitch.CfnPlan.LambdaUngracefulProperty(
                                    behavior="behavior"
                                )
                            ),
                            ec2_asg_capacity_increase_config=arcregionswitch.CfnPlan.Ec2AsgCapacityIncreaseConfigurationProperty(
                                asgs=[arcregionswitch.CfnPlan.AsgProperty(
                                    arn="arn",
                                    cross_account_role="crossAccountRole",
                                    external_id="externalId"
                                )],
                
                                # the properties below are optional
                                capacity_monitoring_approach="capacityMonitoringApproach",
                                target_percent=123,
                                timeout_minutes=123,
                                ungraceful=arcregionswitch.CfnPlan.Ec2UngracefulProperty(
                                    minimum_success_percentage=123
                                )
                            ),
                            ecs_capacity_increase_config=arcregionswitch.CfnPlan.EcsCapacityIncreaseConfigurationProperty(
                                services=[arcregionswitch.CfnPlan.ServiceProperty(
                                    cluster_arn="clusterArn",
                                    cross_account_role="crossAccountRole",
                                    external_id="externalId",
                                    service_arn="serviceArn"
                                )],
                
                                # the properties below are optional
                                capacity_monitoring_approach="capacityMonitoringApproach",
                                target_percent=123,
                                timeout_minutes=123,
                                ungraceful=arcregionswitch.CfnPlan.EcsUngracefulProperty(
                                    minimum_success_percentage=123
                                )
                            ),
                            eks_resource_scaling_config=arcregionswitch.CfnPlan.EksResourceScalingConfigurationProperty(
                                kubernetes_resource_type=arcregionswitch.CfnPlan.KubernetesResourceTypeProperty(
                                    api_version="apiVersion",
                                    kind="kind"
                                ),
                
                                # the properties below are optional
                                capacity_monitoring_approach="capacityMonitoringApproach",
                                eks_clusters=[arcregionswitch.CfnPlan.EksClusterProperty(
                                    cluster_arn="clusterArn",
                
                                    # the properties below are optional
                                    cross_account_role="crossAccountRole",
                                    external_id="externalId"
                                )],
                                scaling_resources=[{
                                    "scaling_resources_key": {
                                        "scaling_resources_key": arcregionswitch.CfnPlan.KubernetesScalingResourceProperty(
                                            name="name",
                                            namespace="namespace",
                
                                            # the properties below are optional
                                            hpa_name="hpaName"
                                        )
                                    }
                                }],
                                target_percent=123,
                                timeout_minutes=123,
                                ungraceful=arcregionswitch.CfnPlan.EksResourceScalingUngracefulProperty(
                                    minimum_success_percentage=123
                                )
                            ),
                            execution_approval_config=arcregionswitch.CfnPlan.ExecutionApprovalConfigurationProperty(
                                approval_role="approvalRole",
                
                                # the properties below are optional
                                timeout_minutes=123
                            ),
                            global_aurora_config=arcregionswitch.CfnPlan.GlobalAuroraConfigurationProperty(
                                behavior="behavior",
                                database_cluster_arns=["databaseClusterArns"],
                                global_cluster_identifier="globalClusterIdentifier",
                
                                # the properties below are optional
                                cross_account_role="crossAccountRole",
                                external_id="externalId",
                                timeout_minutes=123,
                                ungraceful=arcregionswitch.CfnPlan.GlobalAuroraUngracefulProperty(
                                    ungraceful="ungraceful"
                                )
                            ),
                            parallel_config=arcregionswitch.CfnPlan.ParallelExecutionBlockConfigurationProperty(
                                steps=[step_property_]
                            ),
                            region_switch_plan_config=arcregionswitch.CfnPlan.RegionSwitchPlanConfigurationProperty(
                                arn="arn",
                
                                # the properties below are optional
                                cross_account_role="crossAccountRole",
                                external_id="externalId"
                            ),
                            route53_health_check_config=arcregionswitch.CfnPlan.Route53HealthCheckConfigurationProperty(
                                hosted_zone_id="hostedZoneId",
                                record_name="recordName",
                
                                # the properties below are optional
                                cross_account_role="crossAccountRole",
                                external_id="externalId",
                                record_sets=[arcregionswitch.CfnPlan.Route53ResourceRecordSetProperty(
                                    record_set_identifier="recordSetIdentifier",
                                    region="region"
                                )],
                                timeout_minutes=123
                            )
                        ),
                        execution_block_type="executionBlockType",
                        name="name",
                
                        # the properties below are optional
                        description="description"
                    )],
                    workflow_description="workflowDescription",
                    workflow_target_region="workflowTargetRegion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__20a30ca206bf2a7483e5517778a6e2e160f345026b4773019a9189cc9fd4a8fd)
                check_type(argname="argument workflow_target_action", value=workflow_target_action, expected_type=type_hints["workflow_target_action"])
                check_type(argname="argument steps", value=steps, expected_type=type_hints["steps"])
                check_type(argname="argument workflow_description", value=workflow_description, expected_type=type_hints["workflow_description"])
                check_type(argname="argument workflow_target_region", value=workflow_target_region, expected_type=type_hints["workflow_target_region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "workflow_target_action": workflow_target_action,
            }
            if steps is not None:
                self._values["steps"] = steps
            if workflow_description is not None:
                self._values["workflow_description"] = workflow_description
            if workflow_target_region is not None:
                self._values["workflow_target_region"] = workflow_target_region

        @builtins.property
        def workflow_target_action(self) -> builtins.str:
            '''The action that the workflow performs.

            Valid values include ACTIVATE and DEACTIVATE.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-workflow.html#cfn-arcregionswitch-plan-workflow-workflowtargetaction
            '''
            result = self._values.get("workflow_target_action")
            assert result is not None, "Required property 'workflow_target_action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def steps(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.StepProperty"]]]]:
            '''The steps that make up the workflow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-workflow.html#cfn-arcregionswitch-plan-workflow-steps
            '''
            result = self._values.get("steps")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPlan.StepProperty"]]]], result)

        @builtins.property
        def workflow_description(self) -> typing.Optional[builtins.str]:
            '''The description of the workflow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-workflow.html#cfn-arcregionswitch-plan-workflow-workflowdescription
            '''
            result = self._values.get("workflow_description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def workflow_target_region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region that the workflow targets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arcregionswitch-plan-workflow.html#cfn-arcregionswitch-plan-workflow-workflowtargetregion
            '''
            result = self._values.get("workflow_target_region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_arcregionswitch.CfnPlanProps",
    jsii_struct_bases=[],
    name_mapping={
        "execution_role": "executionRole",
        "name": "name",
        "recovery_approach": "recoveryApproach",
        "regions": "regions",
        "workflows": "workflows",
        "associated_alarms": "associatedAlarms",
        "description": "description",
        "primary_region": "primaryRegion",
        "recovery_time_objective_minutes": "recoveryTimeObjectiveMinutes",
        "tags": "tags",
        "triggers": "triggers",
    },
)
class CfnPlanProps:
    def __init__(
        self,
        *,
        execution_role: builtins.str,
        name: builtins.str,
        recovery_approach: builtins.str,
        regions: typing.Sequence[builtins.str],
        workflows: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.WorkflowProperty, typing.Dict[builtins.str, typing.Any]]]]],
        associated_alarms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.AssociatedAlarmProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        primary_region: typing.Optional[builtins.str] = None,
        recovery_time_objective_minutes: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        triggers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.TriggerProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPlan``.

        :param execution_role: The execution role for a plan.
        :param name: The name for a plan.
        :param recovery_approach: The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).
        :param regions: The AWS Regions for a plan.
        :param workflows: The workflows for a plan.
        :param associated_alarms: The associated application health alarms for a plan.
        :param description: The description for a plan.
        :param primary_region: The primary Region for a plan.
        :param recovery_time_objective_minutes: The recovery time objective for a plan.
        :param tags: 
        :param triggers: The triggers for a plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arcregionswitch-plan.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_arcregionswitch as arcregionswitch
            
            # step_property_: arcregionswitch.CfnPlan.StepProperty
            
            cfn_plan_props = arcregionswitch.CfnPlanProps(
                execution_role="executionRole",
                name="name",
                recovery_approach="recoveryApproach",
                regions=["regions"],
                workflows=[arcregionswitch.CfnPlan.WorkflowProperty(
                    workflow_target_action="workflowTargetAction",
            
                    # the properties below are optional
                    steps=[arcregionswitch.CfnPlan.StepProperty(
                        execution_block_configuration=arcregionswitch.CfnPlan.ExecutionBlockConfigurationProperty(
                            arc_routing_control_config=arcregionswitch.CfnPlan.ArcRoutingControlConfigurationProperty(
                                region_and_routing_controls={
                                    "region_and_routing_controls_key": [arcregionswitch.CfnPlan.ArcRoutingControlStateProperty(
                                        routing_control_arn="routingControlArn",
                                        state="state"
                                    )]
                                },
            
                                # the properties below are optional
                                cross_account_role="crossAccountRole",
                                external_id="externalId",
                                timeout_minutes=123
                            ),
                            custom_action_lambda_config=arcregionswitch.CfnPlan.CustomActionLambdaConfigurationProperty(
                                lambdas=[arcregionswitch.CfnPlan.LambdasProperty(
                                    arn="arn",
                                    cross_account_role="crossAccountRole",
                                    external_id="externalId"
                                )],
                                region_to_run="regionToRun",
                                retry_interval_minutes=123,
            
                                # the properties below are optional
                                timeout_minutes=123,
                                ungraceful=arcregionswitch.CfnPlan.LambdaUngracefulProperty(
                                    behavior="behavior"
                                )
                            ),
                            ec2_asg_capacity_increase_config=arcregionswitch.CfnPlan.Ec2AsgCapacityIncreaseConfigurationProperty(
                                asgs=[arcregionswitch.CfnPlan.AsgProperty(
                                    arn="arn",
                                    cross_account_role="crossAccountRole",
                                    external_id="externalId"
                                )],
            
                                # the properties below are optional
                                capacity_monitoring_approach="capacityMonitoringApproach",
                                target_percent=123,
                                timeout_minutes=123,
                                ungraceful=arcregionswitch.CfnPlan.Ec2UngracefulProperty(
                                    minimum_success_percentage=123
                                )
                            ),
                            ecs_capacity_increase_config=arcregionswitch.CfnPlan.EcsCapacityIncreaseConfigurationProperty(
                                services=[arcregionswitch.CfnPlan.ServiceProperty(
                                    cluster_arn="clusterArn",
                                    cross_account_role="crossAccountRole",
                                    external_id="externalId",
                                    service_arn="serviceArn"
                                )],
            
                                # the properties below are optional
                                capacity_monitoring_approach="capacityMonitoringApproach",
                                target_percent=123,
                                timeout_minutes=123,
                                ungraceful=arcregionswitch.CfnPlan.EcsUngracefulProperty(
                                    minimum_success_percentage=123
                                )
                            ),
                            eks_resource_scaling_config=arcregionswitch.CfnPlan.EksResourceScalingConfigurationProperty(
                                kubernetes_resource_type=arcregionswitch.CfnPlan.KubernetesResourceTypeProperty(
                                    api_version="apiVersion",
                                    kind="kind"
                                ),
            
                                # the properties below are optional
                                capacity_monitoring_approach="capacityMonitoringApproach",
                                eks_clusters=[arcregionswitch.CfnPlan.EksClusterProperty(
                                    cluster_arn="clusterArn",
            
                                    # the properties below are optional
                                    cross_account_role="crossAccountRole",
                                    external_id="externalId"
                                )],
                                scaling_resources=[{
                                    "scaling_resources_key": {
                                        "scaling_resources_key": arcregionswitch.CfnPlan.KubernetesScalingResourceProperty(
                                            name="name",
                                            namespace="namespace",
            
                                            # the properties below are optional
                                            hpa_name="hpaName"
                                        )
                                    }
                                }],
                                target_percent=123,
                                timeout_minutes=123,
                                ungraceful=arcregionswitch.CfnPlan.EksResourceScalingUngracefulProperty(
                                    minimum_success_percentage=123
                                )
                            ),
                            execution_approval_config=arcregionswitch.CfnPlan.ExecutionApprovalConfigurationProperty(
                                approval_role="approvalRole",
            
                                # the properties below are optional
                                timeout_minutes=123
                            ),
                            global_aurora_config=arcregionswitch.CfnPlan.GlobalAuroraConfigurationProperty(
                                behavior="behavior",
                                database_cluster_arns=["databaseClusterArns"],
                                global_cluster_identifier="globalClusterIdentifier",
            
                                # the properties below are optional
                                cross_account_role="crossAccountRole",
                                external_id="externalId",
                                timeout_minutes=123,
                                ungraceful=arcregionswitch.CfnPlan.GlobalAuroraUngracefulProperty(
                                    ungraceful="ungraceful"
                                )
                            ),
                            parallel_config=arcregionswitch.CfnPlan.ParallelExecutionBlockConfigurationProperty(
                                steps=[step_property_]
                            ),
                            region_switch_plan_config=arcregionswitch.CfnPlan.RegionSwitchPlanConfigurationProperty(
                                arn="arn",
            
                                # the properties below are optional
                                cross_account_role="crossAccountRole",
                                external_id="externalId"
                            ),
                            route53_health_check_config=arcregionswitch.CfnPlan.Route53HealthCheckConfigurationProperty(
                                hosted_zone_id="hostedZoneId",
                                record_name="recordName",
            
                                # the properties below are optional
                                cross_account_role="crossAccountRole",
                                external_id="externalId",
                                record_sets=[arcregionswitch.CfnPlan.Route53ResourceRecordSetProperty(
                                    record_set_identifier="recordSetIdentifier",
                                    region="region"
                                )],
                                timeout_minutes=123
                            )
                        ),
                        execution_block_type="executionBlockType",
                        name="name",
            
                        # the properties below are optional
                        description="description"
                    )],
                    workflow_description="workflowDescription",
                    workflow_target_region="workflowTargetRegion"
                )],
            
                # the properties below are optional
                associated_alarms={
                    "associated_alarms_key": arcregionswitch.CfnPlan.AssociatedAlarmProperty(
                        alarm_type="alarmType",
                        resource_identifier="resourceIdentifier",
            
                        # the properties below are optional
                        cross_account_role="crossAccountRole",
                        external_id="externalId"
                    )
                },
                description="description",
                primary_region="primaryRegion",
                recovery_time_objective_minutes=123,
                tags={
                    "tags_key": "tags"
                },
                triggers=[arcregionswitch.CfnPlan.TriggerProperty(
                    action="action",
                    conditions=[arcregionswitch.CfnPlan.TriggerConditionProperty(
                        associated_alarm_name="associatedAlarmName",
                        condition="condition"
                    )],
                    min_delay_minutes_between_executions=123,
                    target_region="targetRegion",
            
                    # the properties below are optional
                    description="description"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3769ac000838fbbf6a0de25911d7b60b6ec569d30dc6c0baa361105df2e6c141)
            check_type(argname="argument execution_role", value=execution_role, expected_type=type_hints["execution_role"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument recovery_approach", value=recovery_approach, expected_type=type_hints["recovery_approach"])
            check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
            check_type(argname="argument workflows", value=workflows, expected_type=type_hints["workflows"])
            check_type(argname="argument associated_alarms", value=associated_alarms, expected_type=type_hints["associated_alarms"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument primary_region", value=primary_region, expected_type=type_hints["primary_region"])
            check_type(argname="argument recovery_time_objective_minutes", value=recovery_time_objective_minutes, expected_type=type_hints["recovery_time_objective_minutes"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument triggers", value=triggers, expected_type=type_hints["triggers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "execution_role": execution_role,
            "name": name,
            "recovery_approach": recovery_approach,
            "regions": regions,
            "workflows": workflows,
        }
        if associated_alarms is not None:
            self._values["associated_alarms"] = associated_alarms
        if description is not None:
            self._values["description"] = description
        if primary_region is not None:
            self._values["primary_region"] = primary_region
        if recovery_time_objective_minutes is not None:
            self._values["recovery_time_objective_minutes"] = recovery_time_objective_minutes
        if tags is not None:
            self._values["tags"] = tags
        if triggers is not None:
            self._values["triggers"] = triggers

    @builtins.property
    def execution_role(self) -> builtins.str:
        '''The execution role for a plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arcregionswitch-plan.html#cfn-arcregionswitch-plan-executionrole
        '''
        result = self._values.get("execution_role")
        assert result is not None, "Required property 'execution_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for a plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arcregionswitch-plan.html#cfn-arcregionswitch-plan-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recovery_approach(self) -> builtins.str:
        '''The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arcregionswitch-plan.html#cfn-arcregionswitch-plan-recoveryapproach
        '''
        result = self._values.get("recovery_approach")
        assert result is not None, "Required property 'recovery_approach' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regions(self) -> typing.List[builtins.str]:
        '''The AWS Regions for a plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arcregionswitch-plan.html#cfn-arcregionswitch-plan-regions
        '''
        result = self._values.get("regions")
        assert result is not None, "Required property 'regions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def workflows(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPlan.WorkflowProperty]]]:
        '''The workflows for a plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arcregionswitch-plan.html#cfn-arcregionswitch-plan-workflows
        '''
        result = self._values.get("workflows")
        assert result is not None, "Required property 'workflows' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPlan.WorkflowProperty]]], result)

    @builtins.property
    def associated_alarms(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnPlan.AssociatedAlarmProperty]]]]:
        '''The associated application health alarms for a plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arcregionswitch-plan.html#cfn-arcregionswitch-plan-associatedalarms
        '''
        result = self._values.get("associated_alarms")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnPlan.AssociatedAlarmProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for a plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arcregionswitch-plan.html#cfn-arcregionswitch-plan-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_region(self) -> typing.Optional[builtins.str]:
        '''The primary Region for a plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arcregionswitch-plan.html#cfn-arcregionswitch-plan-primaryregion
        '''
        result = self._values.get("primary_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recovery_time_objective_minutes(self) -> typing.Optional[jsii.Number]:
        '''The recovery time objective for a plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arcregionswitch-plan.html#cfn-arcregionswitch-plan-recoverytimeobjectiveminutes
        '''
        result = self._values.get("recovery_time_objective_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arcregionswitch-plan.html#cfn-arcregionswitch-plan-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def triggers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPlan.TriggerProperty]]]]:
        '''The triggers for a plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arcregionswitch-plan.html#cfn-arcregionswitch-plan-triggers
        '''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPlan.TriggerProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnPlan",
    "CfnPlanProps",
]

publication.publish()

def _typecheckingstub__717f8fc7634107cdad75ab8dc89a21d48c1d0f596f5095c671ae6741ed5ac35c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    execution_role: builtins.str,
    name: builtins.str,
    recovery_approach: builtins.str,
    regions: typing.Sequence[builtins.str],
    workflows: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.WorkflowProperty, typing.Dict[builtins.str, typing.Any]]]]],
    associated_alarms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.AssociatedAlarmProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    primary_region: typing.Optional[builtins.str] = None,
    recovery_time_objective_minutes: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    triggers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.TriggerProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71cc46128a95cab0f86fc08911be3991a776362f808b0f24d579bc842f712f55(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5233fe9754a5f05c5abd7c2563e94e161231dbab1550036d8cb77ec7b9547432(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f53792e88b412f34a2415fdff56351b1a54a94878ba61605061977a91e10fca2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbc310a1fcc73445115d9240d0eba7268997be8cac2ff2daad91277ed3174ea4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01b822173477d9982079c51379059a1b50ff75ad5e17af6ea27788c0b0efe0be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01d59248ee3d7f15f86e1af0b467749822e824bc95de98763fe13c53e695ef54(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e3eb77d0273786a3c83aa4e78160b5d7bac7f5e82e5339e9439e014d076344f(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPlan.WorkflowProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__012a0bc7fbb902a59abbec88920455e0cd4d3ab3f0f86ab6b04d32154ed0cc71(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnPlan.AssociatedAlarmProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__591094d49374c97cd84fa7e0eeb7a618de3dd46dd83aad681303b9ac5639e3d9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2d5c679228613d5980262152e1e6db22efda95a623c4c2113ed1dd7e09ba0a1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a158461aabcc0fceebbed61f515ca1629dd0e6cb63d8ba2e7a2f6c8e4fd5b035(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3c41bc2a28d77b19e855bf7c198670838a0dfb959e579501a5539e1a4eda62a(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__085b11c9fd7fb03e86d812a265c47665ac981e51ecdfda2e79624700d0acde6d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPlan.TriggerProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57399e39635e0435be35376fd9218c629f9663afe431fd5a36d652ae3eb9873e(
    *,
    region_and_routing_controls: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.ArcRoutingControlStateProperty, typing.Dict[builtins.str, typing.Any]]]]]]],
    cross_account_role: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
    timeout_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55bdfafa464881d6c62e0618ec995267e3c59e4e1439ec978192672189f6b20f(
    *,
    routing_control_arn: builtins.str,
    state: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1676b0ee46a93bdc080e497fe362d46ed4de4bf3d0f939d09ff3f213c7f5c637(
    *,
    arn: typing.Optional[builtins.str] = None,
    cross_account_role: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da9567b68c112553218c3dc6b107e275b5f8974694e79a06ee1f35ade040a4ff(
    *,
    alarm_type: builtins.str,
    resource_identifier: builtins.str,
    cross_account_role: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__677cc1e3776f9941a3e383511e2b156b9b18584e59ab2742e9aeb2a068d4a396(
    *,
    lambdas: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.LambdasProperty, typing.Dict[builtins.str, typing.Any]]]]],
    region_to_run: builtins.str,
    retry_interval_minutes: jsii.Number,
    timeout_minutes: typing.Optional[jsii.Number] = None,
    ungraceful: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.LambdaUngracefulProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9450c4fc5464b8ee89e44bf3f7537c88de4728278fe9d0f976e7b3a1004ee5f0(
    *,
    asgs: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.AsgProperty, typing.Dict[builtins.str, typing.Any]]]]],
    capacity_monitoring_approach: typing.Optional[builtins.str] = None,
    target_percent: typing.Optional[jsii.Number] = None,
    timeout_minutes: typing.Optional[jsii.Number] = None,
    ungraceful: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.Ec2UngracefulProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df83017a8027c200570884800a256e6029496bb9ce1b006656a7874327f5298d(
    *,
    minimum_success_percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b763afef631e7db8b2c2c3be0ade842b4b5d07005a78e029167a12daa9a0b59(
    *,
    services: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.ServiceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    capacity_monitoring_approach: typing.Optional[builtins.str] = None,
    target_percent: typing.Optional[jsii.Number] = None,
    timeout_minutes: typing.Optional[jsii.Number] = None,
    ungraceful: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.EcsUngracefulProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deb1d009908c0c1564a0347ddbba856cd682e5fbd50557e7915c487a54d62313(
    *,
    minimum_success_percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d56face50d286f66c61a4649242ee9c0e4214f5a237dcc15a2a3ef5398d4405(
    *,
    cluster_arn: builtins.str,
    cross_account_role: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a31277680fa6df426ddb8d5341e3bc1a473a20cfd357c9ab42c51d8342d45d2(
    *,
    kubernetes_resource_type: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.KubernetesResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    capacity_monitoring_approach: typing.Optional[builtins.str] = None,
    eks_clusters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.EksClusterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    scaling_resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.KubernetesScalingResourceProperty, typing.Dict[builtins.str, typing.Any]]]]]]]]]] = None,
    target_percent: typing.Optional[jsii.Number] = None,
    timeout_minutes: typing.Optional[jsii.Number] = None,
    ungraceful: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.EksResourceScalingUngracefulProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f9e5d7d28df64aed085e7fff7c951fac8c798f2930bd6f677766f09bf9022cb(
    *,
    minimum_success_percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__332cd445173cd90befd93793d12cf56d6b9d0cf5f0f950d8f1c8da40b41112d7(
    *,
    approval_role: builtins.str,
    timeout_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf03412277ce24dfa861d02429118a5e512a97579dd1c299024e646c98c02098(
    *,
    arc_routing_control_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.ArcRoutingControlConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_action_lambda_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.CustomActionLambdaConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ec2_asg_capacity_increase_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.Ec2AsgCapacityIncreaseConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ecs_capacity_increase_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.EcsCapacityIncreaseConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    eks_resource_scaling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.EksResourceScalingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    execution_approval_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.ExecutionApprovalConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    global_aurora_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.GlobalAuroraConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parallel_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.ParallelExecutionBlockConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    region_switch_plan_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.RegionSwitchPlanConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    route53_health_check_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.Route53HealthCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e60aa2a866c67f15aa41619ecd129adf197a423c592e6f605c7713f6b5591f97(
    *,
    behavior: builtins.str,
    database_cluster_arns: typing.Sequence[builtins.str],
    global_cluster_identifier: builtins.str,
    cross_account_role: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
    timeout_minutes: typing.Optional[jsii.Number] = None,
    ungraceful: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.GlobalAuroraUngracefulProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e95bf120b9c7191be2a0d5f0c8b6dc1fc6f89952abe27811996d58bf93ece46(
    *,
    ungraceful: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f6f9eab294a354253a8235a964459afdc89f8904dc974eac694bcd815c8a40c(
    *,
    health_check_id: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c232ba08af7c15b406e994864bd91ccf5d92d9076e59f172c6103cf5e3ca4b41(
    *,
    api_version: builtins.str,
    kind: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57d18eef9bff8e63ac0c26d15b57916fe933491b47893043399d20a15098730f(
    *,
    name: builtins.str,
    namespace: builtins.str,
    hpa_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f24eea14fa20d551f2fa4c3eb9c17bb8bd884082806add21df6612279fc0da30(
    *,
    behavior: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__382b21febb492930836b8663cd8745c59e5e805caa04c745c3509c5beda2a1ac(
    *,
    arn: typing.Optional[builtins.str] = None,
    cross_account_role: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15563430da8134fdc062f2fae765097f644a784a2fe1b26fc67f62716996ef69(
    *,
    steps: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.StepProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7f4d6ccde8e09198d4b7a9cf491066654de4ce1eae2ba3efd23e437a7c7b59a(
    *,
    arn: builtins.str,
    cross_account_role: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dafd3d15027013dc86ea477c0cc06ceb95b9df4585b699565ae5446c3cbc6845(
    *,
    hosted_zone_id: builtins.str,
    record_name: builtins.str,
    cross_account_role: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
    record_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.Route53ResourceRecordSetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    timeout_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e8634f5bf0466b7e8441b8a091ba90aa68f8785fca863c7422c0f356bcd7c6f(
    *,
    record_set_identifier: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66163b57e8e8c71356b0aea432dd64d08666ca8cad746cff30bddd456c91458e(
    *,
    cluster_arn: typing.Optional[builtins.str] = None,
    cross_account_role: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
    service_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66452e7d3703fa7367742b516ac3b5d497cf9255f69c7e6fe3f2f69ac8e95139(
    *,
    execution_block_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.ExecutionBlockConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    execution_block_type: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d58de4e5ff54abd141b94ef01a4e2b8cf9048e2704fc1718134ab6d7ac32e19d(
    *,
    associated_alarm_name: builtins.str,
    condition: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bf5e3ac00f2b2ce74567b08c3450d613dd5d1b8ff69e8e715177408109021fb(
    *,
    action: builtins.str,
    conditions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.TriggerConditionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    min_delay_minutes_between_executions: jsii.Number,
    target_region: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a30ca206bf2a7483e5517778a6e2e160f345026b4773019a9189cc9fd4a8fd(
    *,
    workflow_target_action: builtins.str,
    steps: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.StepProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    workflow_description: typing.Optional[builtins.str] = None,
    workflow_target_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3769ac000838fbbf6a0de25911d7b60b6ec569d30dc6c0baa361105df2e6c141(
    *,
    execution_role: builtins.str,
    name: builtins.str,
    recovery_approach: builtins.str,
    regions: typing.Sequence[builtins.str],
    workflows: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.WorkflowProperty, typing.Dict[builtins.str, typing.Any]]]]],
    associated_alarms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.AssociatedAlarmProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    primary_region: typing.Optional[builtins.str] = None,
    recovery_time_objective_minutes: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    triggers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPlan.TriggerProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
