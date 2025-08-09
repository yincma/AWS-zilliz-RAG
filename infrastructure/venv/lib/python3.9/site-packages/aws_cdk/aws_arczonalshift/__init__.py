r'''
# AWS::ARCZonalShift Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_arczonalshift as arczonalshift
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ARCZonalShift construct libraries](https://constructs.dev/search?q=arczonalshift)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ARCZonalShift resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ARCZonalShift.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ARCZonalShift](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ARCZonalShift.html).

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
class CfnAutoshiftObserverNotificationStatus(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_arczonalshift.CfnAutoshiftObserverNotificationStatus",
):
    '''Definition of AWS::ARCZonalShift::AutoshiftObserverNotificationStatus Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arczonalshift-autoshiftobservernotificationstatus.html
    :cloudformationResource: AWS::ARCZonalShift::AutoshiftObserverNotificationStatus
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_arczonalshift as arczonalshift
        
        cfn_autoshift_observer_notification_status = arczonalshift.CfnAutoshiftObserverNotificationStatus(self, "MyCfnAutoshiftObserverNotificationStatus",
            status="status"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        status: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param status: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a641c95b7291cd74504f21deec131b94f9a4820ca9da19c12dcb74b342b75c5f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAutoshiftObserverNotificationStatusProps(status=status)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__367a58f6c0a1e21e312519427c6e0c9dec1c77bae6f15f5e3bb87efaf051de75)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f50aa9c339197b955491d70b247d392f25ffabeb5671525df666d3ee91a733a0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAccountId")
    def attr_account_id(self) -> builtins.str:
        '''User account id, used as part of the primary identifier for the resource.

        :cloudformationAttribute: AccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrRegion")
    def attr_region(self) -> builtins.str:
        '''Region, used as part of the primary identifier for the resource.

        :cloudformationAttribute: Region
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegion"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef429db68210cb2d5549e51165dc50e2f32e0d65575831ef012354037d1bcfd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_arczonalshift.CfnAutoshiftObserverNotificationStatusProps",
    jsii_struct_bases=[],
    name_mapping={"status": "status"},
)
class CfnAutoshiftObserverNotificationStatusProps:
    def __init__(self, *, status: builtins.str) -> None:
        '''Properties for defining a ``CfnAutoshiftObserverNotificationStatus``.

        :param status: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arczonalshift-autoshiftobservernotificationstatus.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_arczonalshift as arczonalshift
            
            cfn_autoshift_observer_notification_status_props = arczonalshift.CfnAutoshiftObserverNotificationStatusProps(
                status="status"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02982b02d19d6396959a28b523ecc10a35db9ead5858b9c048a1ff36123d13d7)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "status": status,
        }

    @builtins.property
    def status(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arczonalshift-autoshiftobservernotificationstatus.html#cfn-arczonalshift-autoshiftobservernotificationstatus-status
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAutoshiftObserverNotificationStatusProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnZonalAutoshiftConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_arczonalshift.CfnZonalAutoshiftConfiguration",
):
    '''The zonal autoshift configuration for a resource includes the practice run configuration and the status for running autoshifts, zonal autoshift status.

    When a resource has a practice run configuation, ARC starts weekly zonal shifts for the resource, to shift traffic away from an Availability Zone. Weekly practice runs help you to make sure that your application can continue to operate normally with the loss of one Availability Zone.

    You can update the zonal autoshift autoshift status to enable or disable zonal autoshift. When zonal autoshift is ``ENABLED`` , you authorize AWS to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery. Traffic is also shifted away for the required weekly practice runs.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arczonalshift-zonalautoshiftconfiguration.html
    :cloudformationResource: AWS::ARCZonalShift::ZonalAutoshiftConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_arczonalshift as arczonalshift
        
        cfn_zonal_autoshift_configuration = arczonalshift.CfnZonalAutoshiftConfiguration(self, "MyCfnZonalAutoshiftConfiguration",
            resource_identifier="resourceIdentifier",
        
            # the properties below are optional
            practice_run_configuration=arczonalshift.CfnZonalAutoshiftConfiguration.PracticeRunConfigurationProperty(
                outcome_alarms=[arczonalshift.CfnZonalAutoshiftConfiguration.ControlConditionProperty(
                    alarm_identifier="alarmIdentifier",
                    type="type"
                )],
        
                # the properties below are optional
                blocked_dates=["blockedDates"],
                blocked_windows=["blockedWindows"],
                blocking_alarms=[arczonalshift.CfnZonalAutoshiftConfiguration.ControlConditionProperty(
                    alarm_identifier="alarmIdentifier",
                    type="type"
                )]
            ),
            zonal_autoshift_status="zonalAutoshiftStatus"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resource_identifier: builtins.str,
        practice_run_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnZonalAutoshiftConfiguration.PracticeRunConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        zonal_autoshift_status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resource_identifier: The identifier for the resource that AWS shifts traffic for. The identifier is the Amazon Resource Name (ARN) for the resource. At this time, supported resources are Network Load Balancers and Application Load Balancers.
        :param practice_run_configuration: A practice run configuration for a resource includes the Amazon CloudWatch alarms that you've specified for a practice run, as well as any blocked dates or blocked windows for the practice run. When a resource has a practice run configuration, ARC shifts traffic for the resource weekly for practice runs. Practice runs are required for zonal autoshift. The zonal shifts that ARC starts for practice runs help you to ensure that shifting away traffic from an Availability Zone during an autoshift is safe for your application. You can update or delete a practice run configuration. Before you delete a practice run configuration, you must disable zonal autoshift for the resource. A practice run configuration is required when zonal autoshift is enabled.
        :param zonal_autoshift_status: When zonal autoshift is ``ENABLED`` , you authorize AWS to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery. Traffic is also shifted away for the required weekly practice runs.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c7357d3884cea81f1166de2f6ac59cb16a8663a471270d73a743eb77c875eb9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnZonalAutoshiftConfigurationProps(
            resource_identifier=resource_identifier,
            practice_run_configuration=practice_run_configuration,
            zonal_autoshift_status=zonal_autoshift_status,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b99ba79946576f2cdb58feb7c9f7c2ee461960d1efbc1c1a5fd3abdceea0643)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6cd5c905f39dc6d9cfcdb3f49d58c5ca237eb10b38e48744425b3c2c5ebdbbd)
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
    @jsii.member(jsii_name="resourceIdentifier")
    def resource_identifier(self) -> builtins.str:
        '''The identifier for the resource that AWS shifts traffic for.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceIdentifier"))

    @resource_identifier.setter
    def resource_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0172f855e8c8e45fb028b84c5b6c061a5bab422e24d02655056a950949eb68fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="practiceRunConfiguration")
    def practice_run_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnZonalAutoshiftConfiguration.PracticeRunConfigurationProperty"]]:
        '''A practice run configuration for a resource includes the Amazon CloudWatch alarms that you've specified for a practice run, as well as any blocked dates or blocked windows for the practice run.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnZonalAutoshiftConfiguration.PracticeRunConfigurationProperty"]], jsii.get(self, "practiceRunConfiguration"))

    @practice_run_configuration.setter
    def practice_run_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnZonalAutoshiftConfiguration.PracticeRunConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deabf71a3e0015b91f35f23b96354f1d2feeb19a3f783edd9e6c4be281a4d00a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "practiceRunConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="zonalAutoshiftStatus")
    def zonal_autoshift_status(self) -> typing.Optional[builtins.str]:
        '''When zonal autoshift is ``ENABLED`` , you authorize AWS to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zonalAutoshiftStatus"))

    @zonal_autoshift_status.setter
    def zonal_autoshift_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38043ab0659274c5d49e518db7e7a8d1c6e2ecac6e3e25ff03a10aec470be875)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zonalAutoshiftStatus", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arczonalshift.CfnZonalAutoshiftConfiguration.ControlConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"alarm_identifier": "alarmIdentifier", "type": "type"},
    )
    class ControlConditionProperty:
        def __init__(
            self,
            *,
            alarm_identifier: builtins.str,
            type: builtins.str,
        ) -> None:
            '''A control condition is an alarm that you specify for a practice run.

            When you configure practice runs with zonal autoshift for a resource, you specify Amazon CloudWatch alarms, which you create in CloudWatch to use with the practice run. The alarms that you specify are an *outcome alarm* , to monitor application health during practice runs and, optionally, a *blocking alarm* , to block practice runs from starting or to interrupt a practice run in progress.

            Control condition alarms do not apply for autoshifts.

            For more information, see `Considerations when you configure zonal autoshift <https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.considerations.html>`_ in the ARC Developer Guide.

            :param alarm_identifier: The Amazon Resource Name (ARN) for an Amazon CloudWatch alarm that you specify as a control condition for a practice run.
            :param type: The type of alarm specified for a practice run. You can only specify Amazon CloudWatch alarms for practice runs, so the only valid value is ``CLOUDWATCH`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arczonalshift as arczonalshift
                
                control_condition_property = arczonalshift.CfnZonalAutoshiftConfiguration.ControlConditionProperty(
                    alarm_identifier="alarmIdentifier",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__32c87263351229051c702b913e012d54d6a7dde2b0ae1f0bdfd4035559222feb)
                check_type(argname="argument alarm_identifier", value=alarm_identifier, expected_type=type_hints["alarm_identifier"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "alarm_identifier": alarm_identifier,
                "type": type,
            }

        @builtins.property
        def alarm_identifier(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) for an Amazon CloudWatch alarm that you specify as a control condition for a practice run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition.html#cfn-arczonalshift-zonalautoshiftconfiguration-controlcondition-alarmidentifier
            '''
            result = self._values.get("alarm_identifier")
            assert result is not None, "Required property 'alarm_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of alarm specified for a practice run.

            You can only specify Amazon CloudWatch alarms for practice runs, so the only valid value is ``CLOUDWATCH`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-controlcondition.html#cfn-arczonalshift-zonalautoshiftconfiguration-controlcondition-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ControlConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_arczonalshift.CfnZonalAutoshiftConfiguration.PracticeRunConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "outcome_alarms": "outcomeAlarms",
            "blocked_dates": "blockedDates",
            "blocked_windows": "blockedWindows",
            "blocking_alarms": "blockingAlarms",
        },
    )
    class PracticeRunConfigurationProperty:
        def __init__(
            self,
            *,
            outcome_alarms: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnZonalAutoshiftConfiguration.ControlConditionProperty", typing.Dict[builtins.str, typing.Any]]]]],
            blocked_dates: typing.Optional[typing.Sequence[builtins.str]] = None,
            blocked_windows: typing.Optional[typing.Sequence[builtins.str]] = None,
            blocking_alarms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnZonalAutoshiftConfiguration.ControlConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''A practice run configuration for a resource includes the Amazon CloudWatch alarms that you've specified for a practice run, as well as any blocked dates or blocked windows for the practice run.

            When a resource has a practice run configuation, ARC starts weekly zonal shifts for the resource, to shift traffic away from an Availability Zone. Weekly practice runs help you to make sure that your application can continue to operate normally with the loss of one Availability Zone.

            You can update or delete a practice run configuration. When you delete a practice run configuration, zonal autoshift is disabled for the resource. A practice run configuration is required when zonal autoshift is enabled.

            :param outcome_alarms: The alarm that you specify to monitor the health of your application during practice runs. When the outcome alarm goes into an ``ALARM`` state, the practice run is ended and the outcome is set to ``FAILED`` .
            :param blocked_dates: An array of one or more dates that you can specify when AWS does not start practice runs for a resource. Dates are in UTC. Specify blocked dates in the format ``YYYY-MM-DD`` , separated by spaces.
            :param blocked_windows: An array of one or more days and times that you can specify when ARC does not start practice runs for a resource. Days and times are in UTC. Specify blocked windows in the format ``DAY:HH:MM-DAY:HH:MM`` , separated by spaces. For example, ``MON:18:30-MON:19:30 TUE:18:30-TUE:19:30`` . .. epigraph:: Blocked windows have to start and end on the same day. Windows that span multiple days aren't supported.
            :param blocking_alarms: An optional alarm that you can specify that blocks practice runs when the alarm is in an ``ALARM`` state. When a blocking alarm goes into an ``ALARM`` state, it prevents practice runs from being started, and ends practice runs that are in progress.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_arczonalshift as arczonalshift
                
                practice_run_configuration_property = arczonalshift.CfnZonalAutoshiftConfiguration.PracticeRunConfigurationProperty(
                    outcome_alarms=[arczonalshift.CfnZonalAutoshiftConfiguration.ControlConditionProperty(
                        alarm_identifier="alarmIdentifier",
                        type="type"
                    )],
                
                    # the properties below are optional
                    blocked_dates=["blockedDates"],
                    blocked_windows=["blockedWindows"],
                    blocking_alarms=[arczonalshift.CfnZonalAutoshiftConfiguration.ControlConditionProperty(
                        alarm_identifier="alarmIdentifier",
                        type="type"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__09d714a4c978f7c2d70e24869d7ce300d549509a8b35174736a9571be8aa5750)
                check_type(argname="argument outcome_alarms", value=outcome_alarms, expected_type=type_hints["outcome_alarms"])
                check_type(argname="argument blocked_dates", value=blocked_dates, expected_type=type_hints["blocked_dates"])
                check_type(argname="argument blocked_windows", value=blocked_windows, expected_type=type_hints["blocked_windows"])
                check_type(argname="argument blocking_alarms", value=blocking_alarms, expected_type=type_hints["blocking_alarms"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "outcome_alarms": outcome_alarms,
            }
            if blocked_dates is not None:
                self._values["blocked_dates"] = blocked_dates
            if blocked_windows is not None:
                self._values["blocked_windows"] = blocked_windows
            if blocking_alarms is not None:
                self._values["blocking_alarms"] = blocking_alarms

        @builtins.property
        def outcome_alarms(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnZonalAutoshiftConfiguration.ControlConditionProperty"]]]:
            '''The alarm that you specify to monitor the health of your application during practice runs.

            When the outcome alarm goes into an ``ALARM`` state, the practice run is ended and the outcome is set to ``FAILED`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration.html#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-outcomealarms
            '''
            result = self._values.get("outcome_alarms")
            assert result is not None, "Required property 'outcome_alarms' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnZonalAutoshiftConfiguration.ControlConditionProperty"]]], result)

        @builtins.property
        def blocked_dates(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of one or more dates that you can specify when AWS does not start practice runs for a resource.

            Dates are in UTC.

            Specify blocked dates in the format ``YYYY-MM-DD`` , separated by spaces.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration.html#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-blockeddates
            '''
            result = self._values.get("blocked_dates")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def blocked_windows(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of one or more days and times that you can specify when ARC does not start practice runs for a resource.

            Days and times are in UTC.

            Specify blocked windows in the format ``DAY:HH:MM-DAY:HH:MM`` , separated by spaces. For example, ``MON:18:30-MON:19:30 TUE:18:30-TUE:19:30`` .
            .. epigraph::

               Blocked windows have to start and end on the same day. Windows that span multiple days aren't supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration.html#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-blockedwindows
            '''
            result = self._values.get("blocked_windows")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def blocking_alarms(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnZonalAutoshiftConfiguration.ControlConditionProperty"]]]]:
            '''An optional alarm that you can specify that blocks practice runs when the alarm is in an ``ALARM`` state.

            When a blocking alarm goes into an ``ALARM`` state, it prevents practice runs from being started, and ends practice runs that are in progress.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration.html#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration-blockingalarms
            '''
            result = self._values.get("blocking_alarms")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnZonalAutoshiftConfiguration.ControlConditionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PracticeRunConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_arczonalshift.CfnZonalAutoshiftConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "resource_identifier": "resourceIdentifier",
        "practice_run_configuration": "practiceRunConfiguration",
        "zonal_autoshift_status": "zonalAutoshiftStatus",
    },
)
class CfnZonalAutoshiftConfigurationProps:
    def __init__(
        self,
        *,
        resource_identifier: builtins.str,
        practice_run_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnZonalAutoshiftConfiguration.PracticeRunConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        zonal_autoshift_status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnZonalAutoshiftConfiguration``.

        :param resource_identifier: The identifier for the resource that AWS shifts traffic for. The identifier is the Amazon Resource Name (ARN) for the resource. At this time, supported resources are Network Load Balancers and Application Load Balancers.
        :param practice_run_configuration: A practice run configuration for a resource includes the Amazon CloudWatch alarms that you've specified for a practice run, as well as any blocked dates or blocked windows for the practice run. When a resource has a practice run configuration, ARC shifts traffic for the resource weekly for practice runs. Practice runs are required for zonal autoshift. The zonal shifts that ARC starts for practice runs help you to ensure that shifting away traffic from an Availability Zone during an autoshift is safe for your application. You can update or delete a practice run configuration. Before you delete a practice run configuration, you must disable zonal autoshift for the resource. A practice run configuration is required when zonal autoshift is enabled.
        :param zonal_autoshift_status: When zonal autoshift is ``ENABLED`` , you authorize AWS to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery. Traffic is also shifted away for the required weekly practice runs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arczonalshift-zonalautoshiftconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_arczonalshift as arczonalshift
            
            cfn_zonal_autoshift_configuration_props = arczonalshift.CfnZonalAutoshiftConfigurationProps(
                resource_identifier="resourceIdentifier",
            
                # the properties below are optional
                practice_run_configuration=arczonalshift.CfnZonalAutoshiftConfiguration.PracticeRunConfigurationProperty(
                    outcome_alarms=[arczonalshift.CfnZonalAutoshiftConfiguration.ControlConditionProperty(
                        alarm_identifier="alarmIdentifier",
                        type="type"
                    )],
            
                    # the properties below are optional
                    blocked_dates=["blockedDates"],
                    blocked_windows=["blockedWindows"],
                    blocking_alarms=[arczonalshift.CfnZonalAutoshiftConfiguration.ControlConditionProperty(
                        alarm_identifier="alarmIdentifier",
                        type="type"
                    )]
                ),
                zonal_autoshift_status="zonalAutoshiftStatus"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df846ffeb392d27b90c69c753d2f5defce1421dd94b678654bb7fe32434590d0)
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
            check_type(argname="argument practice_run_configuration", value=practice_run_configuration, expected_type=type_hints["practice_run_configuration"])
            check_type(argname="argument zonal_autoshift_status", value=zonal_autoshift_status, expected_type=type_hints["zonal_autoshift_status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_identifier": resource_identifier,
        }
        if practice_run_configuration is not None:
            self._values["practice_run_configuration"] = practice_run_configuration
        if zonal_autoshift_status is not None:
            self._values["zonal_autoshift_status"] = zonal_autoshift_status

    @builtins.property
    def resource_identifier(self) -> builtins.str:
        '''The identifier for the resource that AWS shifts traffic for.

        The identifier is the Amazon Resource Name (ARN) for the resource.

        At this time, supported resources are Network Load Balancers and Application Load Balancers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arczonalshift-zonalautoshiftconfiguration.html#cfn-arczonalshift-zonalautoshiftconfiguration-resourceidentifier
        '''
        result = self._values.get("resource_identifier")
        assert result is not None, "Required property 'resource_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def practice_run_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnZonalAutoshiftConfiguration.PracticeRunConfigurationProperty]]:
        '''A practice run configuration for a resource includes the Amazon CloudWatch alarms that you've specified for a practice run, as well as any blocked dates or blocked windows for the practice run.

        When a resource has a practice run configuration, ARC shifts traffic for the resource weekly for practice runs.

        Practice runs are required for zonal autoshift. The zonal shifts that ARC starts for practice runs help you to ensure that shifting away traffic from an Availability Zone during an autoshift is safe for your application.

        You can update or delete a practice run configuration. Before you delete a practice run configuration, you must disable zonal autoshift for the resource. A practice run configuration is required when zonal autoshift is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arczonalshift-zonalautoshiftconfiguration.html#cfn-arczonalshift-zonalautoshiftconfiguration-practicerunconfiguration
        '''
        result = self._values.get("practice_run_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnZonalAutoshiftConfiguration.PracticeRunConfigurationProperty]], result)

    @builtins.property
    def zonal_autoshift_status(self) -> typing.Optional[builtins.str]:
        '''When zonal autoshift is ``ENABLED`` , you authorize AWS to shift away resource traffic for an application from an Availability Zone during events, on your behalf, to help reduce time to recovery.

        Traffic is also shifted away for the required weekly practice runs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-arczonalshift-zonalautoshiftconfiguration.html#cfn-arczonalshift-zonalautoshiftconfiguration-zonalautoshiftstatus
        '''
        result = self._values.get("zonal_autoshift_status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnZonalAutoshiftConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAutoshiftObserverNotificationStatus",
    "CfnAutoshiftObserverNotificationStatusProps",
    "CfnZonalAutoshiftConfiguration",
    "CfnZonalAutoshiftConfigurationProps",
]

publication.publish()

def _typecheckingstub__a641c95b7291cd74504f21deec131b94f9a4820ca9da19c12dcb74b342b75c5f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__367a58f6c0a1e21e312519427c6e0c9dec1c77bae6f15f5e3bb87efaf051de75(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f50aa9c339197b955491d70b247d392f25ffabeb5671525df666d3ee91a733a0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef429db68210cb2d5549e51165dc50e2f32e0d65575831ef012354037d1bcfd0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02982b02d19d6396959a28b523ecc10a35db9ead5858b9c048a1ff36123d13d7(
    *,
    status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c7357d3884cea81f1166de2f6ac59cb16a8663a471270d73a743eb77c875eb9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resource_identifier: builtins.str,
    practice_run_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnZonalAutoshiftConfiguration.PracticeRunConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    zonal_autoshift_status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b99ba79946576f2cdb58feb7c9f7c2ee461960d1efbc1c1a5fd3abdceea0643(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6cd5c905f39dc6d9cfcdb3f49d58c5ca237eb10b38e48744425b3c2c5ebdbbd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0172f855e8c8e45fb028b84c5b6c061a5bab422e24d02655056a950949eb68fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deabf71a3e0015b91f35f23b96354f1d2feeb19a3f783edd9e6c4be281a4d00a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnZonalAutoshiftConfiguration.PracticeRunConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38043ab0659274c5d49e518db7e7a8d1c6e2ecac6e3e25ff03a10aec470be875(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32c87263351229051c702b913e012d54d6a7dde2b0ae1f0bdfd4035559222feb(
    *,
    alarm_identifier: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09d714a4c978f7c2d70e24869d7ce300d549509a8b35174736a9571be8aa5750(
    *,
    outcome_alarms: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnZonalAutoshiftConfiguration.ControlConditionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    blocked_dates: typing.Optional[typing.Sequence[builtins.str]] = None,
    blocked_windows: typing.Optional[typing.Sequence[builtins.str]] = None,
    blocking_alarms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnZonalAutoshiftConfiguration.ControlConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df846ffeb392d27b90c69c753d2f5defce1421dd94b678654bb7fe32434590d0(
    *,
    resource_identifier: builtins.str,
    practice_run_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnZonalAutoshiftConfiguration.PracticeRunConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    zonal_autoshift_status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
