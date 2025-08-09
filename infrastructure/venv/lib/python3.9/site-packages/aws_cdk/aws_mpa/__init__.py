r'''
# AWS::MPA Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_mpa as mpa
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for MPA construct libraries](https://constructs.dev/search?q=mpa)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::MPA resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MPA.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::MPA](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MPA.html).

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
class CfnApprovalTeam(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mpa.CfnApprovalTeam",
):
    '''Creates a new approval team.

    For more information, see `Approval team <https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html>`_ in the *Multi-party approval User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mpa-approvalteam.html
    :cloudformationResource: AWS::MPA::ApprovalTeam
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mpa as mpa
        
        cfn_approval_team = mpa.CfnApprovalTeam(self, "MyCfnApprovalTeam",
            approval_strategy=mpa.CfnApprovalTeam.ApprovalStrategyProperty(
                mof_n=mpa.CfnApprovalTeam.MofNApprovalStrategyProperty(
                    min_approvals_required=123
                )
            ),
            approvers=[mpa.CfnApprovalTeam.ApproverProperty(
                primary_identity_id="primaryIdentityId",
                primary_identity_source_arn="primaryIdentitySourceArn",
        
                # the properties below are optional
                approver_id="approverId",
                primary_identity_status="primaryIdentityStatus",
                response_time="responseTime"
            )],
            description="description",
            name="name",
            policies=[mpa.CfnApprovalTeam.PolicyProperty(
                policy_arn="policyArn"
            )],
        
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
        approval_strategy: typing.Union[_IResolvable_da3f097b, typing.Union["CfnApprovalTeam.ApprovalStrategyProperty", typing.Dict[builtins.str, typing.Any]]],
        approvers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApprovalTeam.ApproverProperty", typing.Dict[builtins.str, typing.Any]]]]],
        description: builtins.str,
        name: builtins.str,
        policies: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApprovalTeam.PolicyProperty", typing.Dict[builtins.str, typing.Any]]]]],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param approval_strategy: Contains details for how an approval team grants approval.
        :param approvers: Contains details for an approver.
        :param description: Description for the team.
        :param name: Name of the team.
        :param policies: Contains details for a policy. Policies define what operations a team that define the permissions for team resources.
        :param tags: Tags that you have added to the specified resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__386990d7f44b867156b4ae1be61f59dcf68b732d47a10262382c529e91f18365)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApprovalTeamProps(
            approval_strategy=approval_strategy,
            approvers=approvers,
            description=description,
            name=name,
            policies=policies,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dba069c00d1a308983f1858c860837ee043b1a2f961d8a9723e5b6ab33cc7f30)
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
            type_hints = typing.get_type_hints(_typecheckingstub__75ba9035ba86d7cbf51b44474da24ea7dc3325fb3d54c692b9f7bd885fa89138)
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
        '''Amazon Resource Name (ARN) for the team.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''Timestamp when the team was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdateTime")
    def attr_last_update_time(self) -> builtins.str:
        '''Timestamp when the team was last updated.

        :cloudformationAttribute: LastUpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdateTime"))

    @builtins.property
    @jsii.member(jsii_name="attrNumberOfApprovers")
    def attr_number_of_approvers(self) -> jsii.Number:
        '''Total number of approvers in the team.

        :cloudformationAttribute: NumberOfApprovers
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrNumberOfApprovers"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Status for the team.

        For more information, see `Team health <https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html>`_ in the *Multi-party approval User Guide* .

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusCode")
    def attr_status_code(self) -> builtins.str:
        '''Status code for the team.

        For more information, see `Team health <https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html>`_ in the *Multi-party approval User Guide* .

        :cloudformationAttribute: StatusCode
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusCode"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''Message describing the status for the team.

        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdateSessionArn")
    def attr_update_session_arn(self) -> builtins.str:
        '''Timestamp when the team was last updated.

        :cloudformationAttribute: UpdateSessionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateSessionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionId")
    def attr_version_id(self) -> builtins.str:
        '''Version ID for the team.

        :cloudformationAttribute: VersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersionId"))

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
    @jsii.member(jsii_name="approvalStrategy")
    def approval_strategy(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnApprovalTeam.ApprovalStrategyProperty"]:
        '''Contains details for how an approval team grants approval.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnApprovalTeam.ApprovalStrategyProperty"], jsii.get(self, "approvalStrategy"))

    @approval_strategy.setter
    def approval_strategy(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnApprovalTeam.ApprovalStrategyProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ec22b692d714a3a436a85095d2cb14c5395173e9390a7d17279d7b92a0e5186)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvalStrategy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="approvers")
    def approvers(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApprovalTeam.ApproverProperty"]]]:
        '''Contains details for an approver.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApprovalTeam.ApproverProperty"]]], jsii.get(self, "approvers"))

    @approvers.setter
    def approvers(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApprovalTeam.ApproverProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0eaf16236f7ec9b60a4b70a3f4b6ec8d4c38b2a19b3bcfd2b71bc112aa84697)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvers", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''Description for the team.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5329ac4998f7b59d7d1e54592bf7342bbee963874c6616e24205a5f906bb7c8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Name of the team.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e39f33a9d3b76bbe323d54d7d73234df05c9a544c11e71f2803cfa2ba185bfde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApprovalTeam.PolicyProperty"]]]:
        '''Contains details for a policy.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApprovalTeam.PolicyProperty"]]], jsii.get(self, "policies"))

    @policies.setter
    def policies(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnApprovalTeam.PolicyProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3a7c415cd8a7816dfb413751381ef0ef0d82b8795bc1c9d3776bc7988dc32fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policies", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags that you have added to the specified resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d31b1fab5555e70c4496aadbffef5ef28d65db31b88ab4e99ebb5030f3b22bad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mpa.CfnApprovalTeam.ApprovalStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={"mof_n": "mofN"},
    )
    class ApprovalStrategyProperty:
        def __init__(
            self,
            *,
            mof_n: typing.Union[_IResolvable_da3f097b, typing.Union["CfnApprovalTeam.MofNApprovalStrategyProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Strategy for how an approval team grants approval.

            :param mof_n: Minimum number of approvals (M) required for a total number of approvers (N).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-approvalteam-approvalstrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mpa as mpa
                
                approval_strategy_property = mpa.CfnApprovalTeam.ApprovalStrategyProperty(
                    mof_n=mpa.CfnApprovalTeam.MofNApprovalStrategyProperty(
                        min_approvals_required=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cace1306ec287bf286eedec7b306e0183888aef06e1e0a1d74cc4532b3ae145b)
                check_type(argname="argument mof_n", value=mof_n, expected_type=type_hints["mof_n"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mof_n": mof_n,
            }

        @builtins.property
        def mof_n(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnApprovalTeam.MofNApprovalStrategyProperty"]:
            '''Minimum number of approvals (M) required for a total number of approvers (N).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-approvalteam-approvalstrategy.html#cfn-mpa-approvalteam-approvalstrategy-mofn
            '''
            result = self._values.get("mof_n")
            assert result is not None, "Required property 'mof_n' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnApprovalTeam.MofNApprovalStrategyProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApprovalStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mpa.CfnApprovalTeam.ApproverProperty",
        jsii_struct_bases=[],
        name_mapping={
            "primary_identity_id": "primaryIdentityId",
            "primary_identity_source_arn": "primaryIdentitySourceArn",
            "approver_id": "approverId",
            "primary_identity_status": "primaryIdentityStatus",
            "response_time": "responseTime",
        },
    )
    class ApproverProperty:
        def __init__(
            self,
            *,
            primary_identity_id: builtins.str,
            primary_identity_source_arn: builtins.str,
            approver_id: typing.Optional[builtins.str] = None,
            primary_identity_status: typing.Optional[builtins.str] = None,
            response_time: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains details for an approver.

            :param primary_identity_id: ID for the user.
            :param primary_identity_source_arn: Amazon Resource Name (ARN) for the identity source. The identity source manages the user authentication for approvers.
            :param approver_id: ID for the approver.
            :param primary_identity_status: Status for the identity source. For example, if an approver has accepted a team invitation with a user authentication method managed by the identity source.
            :param response_time: Timestamp when the approver responded to an approval team invitation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-approvalteam-approver.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mpa as mpa
                
                approver_property = mpa.CfnApprovalTeam.ApproverProperty(
                    primary_identity_id="primaryIdentityId",
                    primary_identity_source_arn="primaryIdentitySourceArn",
                
                    # the properties below are optional
                    approver_id="approverId",
                    primary_identity_status="primaryIdentityStatus",
                    response_time="responseTime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36558bdfdc85f3fc5feb84a058bedb6b2533db65993cd67119e308af416d59bd)
                check_type(argname="argument primary_identity_id", value=primary_identity_id, expected_type=type_hints["primary_identity_id"])
                check_type(argname="argument primary_identity_source_arn", value=primary_identity_source_arn, expected_type=type_hints["primary_identity_source_arn"])
                check_type(argname="argument approver_id", value=approver_id, expected_type=type_hints["approver_id"])
                check_type(argname="argument primary_identity_status", value=primary_identity_status, expected_type=type_hints["primary_identity_status"])
                check_type(argname="argument response_time", value=response_time, expected_type=type_hints["response_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "primary_identity_id": primary_identity_id,
                "primary_identity_source_arn": primary_identity_source_arn,
            }
            if approver_id is not None:
                self._values["approver_id"] = approver_id
            if primary_identity_status is not None:
                self._values["primary_identity_status"] = primary_identity_status
            if response_time is not None:
                self._values["response_time"] = response_time

        @builtins.property
        def primary_identity_id(self) -> builtins.str:
            '''ID for the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-approvalteam-approver.html#cfn-mpa-approvalteam-approver-primaryidentityid
            '''
            result = self._values.get("primary_identity_id")
            assert result is not None, "Required property 'primary_identity_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def primary_identity_source_arn(self) -> builtins.str:
            '''Amazon Resource Name (ARN) for the identity source.

            The identity source manages the user authentication for approvers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-approvalteam-approver.html#cfn-mpa-approvalteam-approver-primaryidentitysourcearn
            '''
            result = self._values.get("primary_identity_source_arn")
            assert result is not None, "Required property 'primary_identity_source_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def approver_id(self) -> typing.Optional[builtins.str]:
            '''ID for the approver.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-approvalteam-approver.html#cfn-mpa-approvalteam-approver-approverid
            '''
            result = self._values.get("approver_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def primary_identity_status(self) -> typing.Optional[builtins.str]:
            '''Status for the identity source.

            For example, if an approver has accepted a team invitation with a user authentication method managed by the identity source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-approvalteam-approver.html#cfn-mpa-approvalteam-approver-primaryidentitystatus
            '''
            result = self._values.get("primary_identity_status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def response_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp when the approver responded to an approval team invitation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-approvalteam-approver.html#cfn-mpa-approvalteam-approver-responsetime
            '''
            result = self._values.get("response_time")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApproverProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mpa.CfnApprovalTeam.MofNApprovalStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={"min_approvals_required": "minApprovalsRequired"},
    )
    class MofNApprovalStrategyProperty:
        def __init__(self, *, min_approvals_required: jsii.Number) -> None:
            '''Strategy for how an approval team grants approval.

            :param min_approvals_required: Minimum number of approvals (M) required for a total number of approvers (N).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-approvalteam-mofnapprovalstrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mpa as mpa
                
                mof_nApproval_strategy_property = mpa.CfnApprovalTeam.MofNApprovalStrategyProperty(
                    min_approvals_required=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c9128fe21a2ecc0edffaa444518ee4e665f9c001202934e3a6ce10274d631042)
                check_type(argname="argument min_approvals_required", value=min_approvals_required, expected_type=type_hints["min_approvals_required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "min_approvals_required": min_approvals_required,
            }

        @builtins.property
        def min_approvals_required(self) -> jsii.Number:
            '''Minimum number of approvals (M) required for a total number of approvers (N).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-approvalteam-mofnapprovalstrategy.html#cfn-mpa-approvalteam-mofnapprovalstrategy-minapprovalsrequired
            '''
            result = self._values.get("min_approvals_required")
            assert result is not None, "Required property 'min_approvals_required' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MofNApprovalStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mpa.CfnApprovalTeam.PolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"policy_arn": "policyArn"},
    )
    class PolicyProperty:
        def __init__(self, *, policy_arn: builtins.str) -> None:
            '''Contains details for a policy.

            Policies define what operations a team that define the permissions for team resources.

            :param policy_arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-approvalteam-policy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mpa as mpa
                
                policy_property = mpa.CfnApprovalTeam.PolicyProperty(
                    policy_arn="policyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__75ccc78545af23823b4f234ee8de6d1d0e7b956206086f97f9aa04f82d00b6f1)
                check_type(argname="argument policy_arn", value=policy_arn, expected_type=type_hints["policy_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "policy_arn": policy_arn,
            }

        @builtins.property
        def policy_arn(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-approvalteam-policy.html#cfn-mpa-approvalteam-policy-policyarn
            '''
            result = self._values.get("policy_arn")
            assert result is not None, "Required property 'policy_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mpa.CfnApprovalTeamProps",
    jsii_struct_bases=[],
    name_mapping={
        "approval_strategy": "approvalStrategy",
        "approvers": "approvers",
        "description": "description",
        "name": "name",
        "policies": "policies",
        "tags": "tags",
    },
)
class CfnApprovalTeamProps:
    def __init__(
        self,
        *,
        approval_strategy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApprovalTeam.ApprovalStrategyProperty, typing.Dict[builtins.str, typing.Any]]],
        approvers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApprovalTeam.ApproverProperty, typing.Dict[builtins.str, typing.Any]]]]],
        description: builtins.str,
        name: builtins.str,
        policies: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApprovalTeam.PolicyProperty, typing.Dict[builtins.str, typing.Any]]]]],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApprovalTeam``.

        :param approval_strategy: Contains details for how an approval team grants approval.
        :param approvers: Contains details for an approver.
        :param description: Description for the team.
        :param name: Name of the team.
        :param policies: Contains details for a policy. Policies define what operations a team that define the permissions for team resources.
        :param tags: Tags that you have added to the specified resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mpa-approvalteam.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mpa as mpa
            
            cfn_approval_team_props = mpa.CfnApprovalTeamProps(
                approval_strategy=mpa.CfnApprovalTeam.ApprovalStrategyProperty(
                    mof_n=mpa.CfnApprovalTeam.MofNApprovalStrategyProperty(
                        min_approvals_required=123
                    )
                ),
                approvers=[mpa.CfnApprovalTeam.ApproverProperty(
                    primary_identity_id="primaryIdentityId",
                    primary_identity_source_arn="primaryIdentitySourceArn",
            
                    # the properties below are optional
                    approver_id="approverId",
                    primary_identity_status="primaryIdentityStatus",
                    response_time="responseTime"
                )],
                description="description",
                name="name",
                policies=[mpa.CfnApprovalTeam.PolicyProperty(
                    policy_arn="policyArn"
                )],
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23c8b69a9c24f10b33222467e81cbea79a3fbb6feb302fe9dea7e9fc448dae98)
            check_type(argname="argument approval_strategy", value=approval_strategy, expected_type=type_hints["approval_strategy"])
            check_type(argname="argument approvers", value=approvers, expected_type=type_hints["approvers"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "approval_strategy": approval_strategy,
            "approvers": approvers,
            "description": description,
            "name": name,
            "policies": policies,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def approval_strategy(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnApprovalTeam.ApprovalStrategyProperty]:
        '''Contains details for how an approval team grants approval.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mpa-approvalteam.html#cfn-mpa-approvalteam-approvalstrategy
        '''
        result = self._values.get("approval_strategy")
        assert result is not None, "Required property 'approval_strategy' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnApprovalTeam.ApprovalStrategyProperty], result)

    @builtins.property
    def approvers(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApprovalTeam.ApproverProperty]]]:
        '''Contains details for an approver.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mpa-approvalteam.html#cfn-mpa-approvalteam-approvers
        '''
        result = self._values.get("approvers")
        assert result is not None, "Required property 'approvers' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApprovalTeam.ApproverProperty]]], result)

    @builtins.property
    def description(self) -> builtins.str:
        '''Description for the team.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mpa-approvalteam.html#cfn-mpa-approvalteam-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the team.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mpa-approvalteam.html#cfn-mpa-approvalteam-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policies(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApprovalTeam.PolicyProperty]]]:
        '''Contains details for a policy.

        Policies define what operations a team that define the permissions for team resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mpa-approvalteam.html#cfn-mpa-approvalteam-policies
        '''
        result = self._values.get("policies")
        assert result is not None, "Required property 'policies' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApprovalTeam.PolicyProperty]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags that you have added to the specified resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mpa-approvalteam.html#cfn-mpa-approvalteam-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApprovalTeamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnIdentitySource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mpa.CfnIdentitySource",
):
    '''Creates a new identity source.

    For more information, see `Identity Source <https://docs.aws.amazon.com/mpa/latest/userguide/mpa-concepts.html>`_ in the *Multi-party approval User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mpa-identitysource.html
    :cloudformationResource: AWS::MPA::IdentitySource
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mpa as mpa
        
        cfn_identity_source = mpa.CfnIdentitySource(self, "MyCfnIdentitySource",
            identity_source_parameters=mpa.CfnIdentitySource.IdentitySourceParametersProperty(
                iam_identity_center=mpa.CfnIdentitySource.IamIdentityCenterProperty(
                    instance_arn="instanceArn",
                    region="region",
        
                    # the properties below are optional
                    approval_portal_url="approvalPortalUrl"
                )
            ),
        
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
        identity_source_parameters: typing.Union[_IResolvable_da3f097b, typing.Union["CfnIdentitySource.IdentitySourceParametersProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param identity_source_parameters: A ``IdentitySourceParameters`` object. Contains details for the resource that provides identities to the identity source. For example, an IAM Identity Center instance.
        :param tags: Tags that you have added to the specified resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ccadabc10958f9b34637bf63683a7ae402b738916eaae8b4554005edd9a7f4e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIdentitySourceProps(
            identity_source_parameters=identity_source_parameters, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__958a95f31b67e8f309896314f9522aadfa2c69a0264848ce97b3ad043e59f942)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c387c3be49c9c1559f9200673f4589cb8729c2ec8c7770beb57a1e5e35378256)
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
        '''Timestamp when the identity source was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentitySourceArn")
    def attr_identity_source_arn(self) -> builtins.str:
        '''Amazon Resource Name (ARN) for the identity source.

        :cloudformationAttribute: IdentitySourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentitySourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentitySourceParametersIamIdentityCenterApprovalPortalUrl")
    def attr_identity_source_parameters_iam_identity_center_approval_portal_url(
        self,
    ) -> builtins.str:
        '''URL for the approval portal associated with the IAM Identity Center instance.

        :cloudformationAttribute: IdentitySourceParameters.IamIdentityCenter.ApprovalPortalUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentitySourceParametersIamIdentityCenterApprovalPortalUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentitySourceType")
    def attr_identity_source_type(self) -> builtins.str:
        '''The type of resource that provided identities to the identity source.

        For example, an IAM Identity Center instance.

        :cloudformationAttribute: IdentitySourceType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentitySourceType"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Status for the identity source.

        For example, if the identity source is ``ACTIVE`` .

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusCode")
    def attr_status_code(self) -> builtins.str:
        '''Status code of the identity source.

        :cloudformationAttribute: StatusCode
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusCode"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''Message describing the status for the identity source.

        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

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
    @jsii.member(jsii_name="identitySourceParameters")
    def identity_source_parameters(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnIdentitySource.IdentitySourceParametersProperty"]:
        '''A ``IdentitySourceParameters`` object.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnIdentitySource.IdentitySourceParametersProperty"], jsii.get(self, "identitySourceParameters"))

    @identity_source_parameters.setter
    def identity_source_parameters(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnIdentitySource.IdentitySourceParametersProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edf6a9866153061ef7d7e82b292ccb765e9c0faa36bd2f2b5fbe62010c82e44f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identitySourceParameters", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags that you have added to the specified resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2348313ff968eefe1739ee64d5e35820f3cb200528d000a5072b402def990d94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mpa.CfnIdentitySource.IamIdentityCenterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_arn": "instanceArn",
            "region": "region",
            "approval_portal_url": "approvalPortalUrl",
        },
    )
    class IamIdentityCenterProperty:
        def __init__(
            self,
            *,
            instance_arn: builtins.str,
            region: builtins.str,
            approval_portal_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''AWS IAM Identity Center credentials.

            For more information see, `AWS IAM Identity Center <https://docs.aws.amazon.com/identity-center/>`_ .

            :param instance_arn: Amazon Resource Name (ARN) for the IAM Identity Center instance.
            :param region: AWS Region where the IAM Identity Center instance is located.
            :param approval_portal_url: URL for the approval portal associated with the IAM Identity Center instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-identitysource-iamidentitycenter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mpa as mpa
                
                iam_identity_center_property = mpa.CfnIdentitySource.IamIdentityCenterProperty(
                    instance_arn="instanceArn",
                    region="region",
                
                    # the properties below are optional
                    approval_portal_url="approvalPortalUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ad03e7c03292e16adba0239cd21aae5665927b223a3d024fb5b1e7a0e5d618f0)
                check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument approval_portal_url", value=approval_portal_url, expected_type=type_hints["approval_portal_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_arn": instance_arn,
                "region": region,
            }
            if approval_portal_url is not None:
                self._values["approval_portal_url"] = approval_portal_url

        @builtins.property
        def instance_arn(self) -> builtins.str:
            '''Amazon Resource Name (ARN) for the IAM Identity Center instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-identitysource-iamidentitycenter.html#cfn-mpa-identitysource-iamidentitycenter-instancearn
            '''
            result = self._values.get("instance_arn")
            assert result is not None, "Required property 'instance_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def region(self) -> builtins.str:
            '''AWS Region where the IAM Identity Center instance is located.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-identitysource-iamidentitycenter.html#cfn-mpa-identitysource-iamidentitycenter-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def approval_portal_url(self) -> typing.Optional[builtins.str]:
            '''URL for the approval portal associated with the IAM Identity Center instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-identitysource-iamidentitycenter.html#cfn-mpa-identitysource-iamidentitycenter-approvalportalurl
            '''
            result = self._values.get("approval_portal_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamIdentityCenterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mpa.CfnIdentitySource.IdentitySourceParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"iam_identity_center": "iamIdentityCenter"},
    )
    class IdentitySourceParametersProperty:
        def __init__(
            self,
            *,
            iam_identity_center: typing.Union[_IResolvable_da3f097b, typing.Union["CfnIdentitySource.IamIdentityCenterProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Contains details for the resource that provides identities to the identity source.

            For example, an IAM Identity Center instance.

            :param iam_identity_center: AWS IAM Identity Center credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-identitysource-identitysourceparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mpa as mpa
                
                identity_source_parameters_property = mpa.CfnIdentitySource.IdentitySourceParametersProperty(
                    iam_identity_center=mpa.CfnIdentitySource.IamIdentityCenterProperty(
                        instance_arn="instanceArn",
                        region="region",
                
                        # the properties below are optional
                        approval_portal_url="approvalPortalUrl"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cdb131b4f18fdc2f28197cd3ec3c8e53cc57a860dfad6d92280cc24753500fc2)
                check_type(argname="argument iam_identity_center", value=iam_identity_center, expected_type=type_hints["iam_identity_center"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "iam_identity_center": iam_identity_center,
            }

        @builtins.property
        def iam_identity_center(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnIdentitySource.IamIdentityCenterProperty"]:
            '''AWS IAM Identity Center credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mpa-identitysource-identitysourceparameters.html#cfn-mpa-identitysource-identitysourceparameters-iamidentitycenter
            '''
            result = self._values.get("iam_identity_center")
            assert result is not None, "Required property 'iam_identity_center' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnIdentitySource.IamIdentityCenterProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentitySourceParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mpa.CfnIdentitySourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "identity_source_parameters": "identitySourceParameters",
        "tags": "tags",
    },
)
class CfnIdentitySourceProps:
    def __init__(
        self,
        *,
        identity_source_parameters: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdentitySource.IdentitySourceParametersProperty, typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnIdentitySource``.

        :param identity_source_parameters: A ``IdentitySourceParameters`` object. Contains details for the resource that provides identities to the identity source. For example, an IAM Identity Center instance.
        :param tags: Tags that you have added to the specified resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mpa-identitysource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mpa as mpa
            
            cfn_identity_source_props = mpa.CfnIdentitySourceProps(
                identity_source_parameters=mpa.CfnIdentitySource.IdentitySourceParametersProperty(
                    iam_identity_center=mpa.CfnIdentitySource.IamIdentityCenterProperty(
                        instance_arn="instanceArn",
                        region="region",
            
                        # the properties below are optional
                        approval_portal_url="approvalPortalUrl"
                    )
                ),
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acb62a986f58f3a0fe81121a9d10976dc06320f2f60c079b3562b20316f0e79b)
            check_type(argname="argument identity_source_parameters", value=identity_source_parameters, expected_type=type_hints["identity_source_parameters"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_source_parameters": identity_source_parameters,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def identity_source_parameters(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnIdentitySource.IdentitySourceParametersProperty]:
        '''A ``IdentitySourceParameters`` object.

        Contains details for the resource that provides identities to the identity source. For example, an IAM Identity Center instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mpa-identitysource.html#cfn-mpa-identitysource-identitysourceparameters
        '''
        result = self._values.get("identity_source_parameters")
        assert result is not None, "Required property 'identity_source_parameters' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnIdentitySource.IdentitySourceParametersProperty], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags that you have added to the specified resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mpa-identitysource.html#cfn-mpa-identitysource-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIdentitySourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApprovalTeam",
    "CfnApprovalTeamProps",
    "CfnIdentitySource",
    "CfnIdentitySourceProps",
]

publication.publish()

def _typecheckingstub__386990d7f44b867156b4ae1be61f59dcf68b732d47a10262382c529e91f18365(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    approval_strategy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApprovalTeam.ApprovalStrategyProperty, typing.Dict[builtins.str, typing.Any]]],
    approvers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApprovalTeam.ApproverProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: builtins.str,
    name: builtins.str,
    policies: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApprovalTeam.PolicyProperty, typing.Dict[builtins.str, typing.Any]]]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dba069c00d1a308983f1858c860837ee043b1a2f961d8a9723e5b6ab33cc7f30(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75ba9035ba86d7cbf51b44474da24ea7dc3325fb3d54c692b9f7bd885fa89138(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ec22b692d714a3a436a85095d2cb14c5395173e9390a7d17279d7b92a0e5186(
    value: typing.Union[_IResolvable_da3f097b, CfnApprovalTeam.ApprovalStrategyProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0eaf16236f7ec9b60a4b70a3f4b6ec8d4c38b2a19b3bcfd2b71bc112aa84697(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApprovalTeam.ApproverProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5329ac4998f7b59d7d1e54592bf7342bbee963874c6616e24205a5f906bb7c8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e39f33a9d3b76bbe323d54d7d73234df05c9a544c11e71f2803cfa2ba185bfde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3a7c415cd8a7816dfb413751381ef0ef0d82b8795bc1c9d3776bc7988dc32fe(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnApprovalTeam.PolicyProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d31b1fab5555e70c4496aadbffef5ef28d65db31b88ab4e99ebb5030f3b22bad(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cace1306ec287bf286eedec7b306e0183888aef06e1e0a1d74cc4532b3ae145b(
    *,
    mof_n: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApprovalTeam.MofNApprovalStrategyProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36558bdfdc85f3fc5feb84a058bedb6b2533db65993cd67119e308af416d59bd(
    *,
    primary_identity_id: builtins.str,
    primary_identity_source_arn: builtins.str,
    approver_id: typing.Optional[builtins.str] = None,
    primary_identity_status: typing.Optional[builtins.str] = None,
    response_time: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9128fe21a2ecc0edffaa444518ee4e665f9c001202934e3a6ce10274d631042(
    *,
    min_approvals_required: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75ccc78545af23823b4f234ee8de6d1d0e7b956206086f97f9aa04f82d00b6f1(
    *,
    policy_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23c8b69a9c24f10b33222467e81cbea79a3fbb6feb302fe9dea7e9fc448dae98(
    *,
    approval_strategy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApprovalTeam.ApprovalStrategyProperty, typing.Dict[builtins.str, typing.Any]]],
    approvers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApprovalTeam.ApproverProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: builtins.str,
    name: builtins.str,
    policies: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApprovalTeam.PolicyProperty, typing.Dict[builtins.str, typing.Any]]]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ccadabc10958f9b34637bf63683a7ae402b738916eaae8b4554005edd9a7f4e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    identity_source_parameters: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdentitySource.IdentitySourceParametersProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__958a95f31b67e8f309896314f9522aadfa2c69a0264848ce97b3ad043e59f942(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c387c3be49c9c1559f9200673f4589cb8729c2ec8c7770beb57a1e5e35378256(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edf6a9866153061ef7d7e82b292ccb765e9c0faa36bd2f2b5fbe62010c82e44f(
    value: typing.Union[_IResolvable_da3f097b, CfnIdentitySource.IdentitySourceParametersProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2348313ff968eefe1739ee64d5e35820f3cb200528d000a5072b402def990d94(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad03e7c03292e16adba0239cd21aae5665927b223a3d024fb5b1e7a0e5d618f0(
    *,
    instance_arn: builtins.str,
    region: builtins.str,
    approval_portal_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdb131b4f18fdc2f28197cd3ec3c8e53cc57a860dfad6d92280cc24753500fc2(
    *,
    iam_identity_center: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdentitySource.IamIdentityCenterProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acb62a986f58f3a0fe81121a9d10976dc06320f2f60c079b3562b20316f0e79b(
    *,
    identity_source_parameters: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdentitySource.IdentitySourceParametersProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
