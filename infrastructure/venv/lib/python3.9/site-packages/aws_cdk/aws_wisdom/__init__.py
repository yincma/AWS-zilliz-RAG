r'''
# AWS::Wisdom Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_wisdom as wisdom
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Wisdom construct libraries](https://constructs.dev/search?q=wisdom)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Wisdom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Wisdom.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Wisdom](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Wisdom.html).

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


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnAIAgent(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent",
):
    '''Creates an Amazon Q in Connect AI Agent.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html
    :cloudformationResource: AWS::Wisdom::AIAgent
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_aIAgent = wisdom.CfnAIAgent(self, "MyCfnAIAgent",
            assistant_id="assistantId",
            configuration=wisdom.CfnAIAgent.AIAgentConfigurationProperty(
                answer_recommendation_ai_agent_configuration=wisdom.CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty(
                    answer_generation_ai_guardrail_id="answerGenerationAiGuardrailId",
                    answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                    association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                        association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                            knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
        
                                        # the properties below are optional
                                        value="value"
                                    )],
                                    or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
        
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
        
                                            # the properties below are optional
                                            value="value"
                                        )
                                    )],
                                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
        
                                        # the properties below are optional
                                        value="value"
                                    )
                                ),
                                max_results=123,
                                override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                            )
                        ),
                        association_id="associationId",
                        association_type="associationType"
                    )],
                    intent_labeling_generation_ai_prompt_id="intentLabelingGenerationAiPromptId",
                    locale="locale",
                    query_reformulation_ai_prompt_id="queryReformulationAiPromptId"
                ),
                manual_search_ai_agent_configuration=wisdom.CfnAIAgent.ManualSearchAIAgentConfigurationProperty(
                    answer_generation_ai_guardrail_id="answerGenerationAiGuardrailId",
                    answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                    association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                        association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                            knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
        
                                        # the properties below are optional
                                        value="value"
                                    )],
                                    or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
        
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
        
                                            # the properties below are optional
                                            value="value"
                                        )
                                    )],
                                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
        
                                        # the properties below are optional
                                        value="value"
                                    )
                                ),
                                max_results=123,
                                override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                            )
                        ),
                        association_id="associationId",
                        association_type="associationType"
                    )],
                    locale="locale"
                ),
                self_service_ai_agent_configuration=wisdom.CfnAIAgent.SelfServiceAIAgentConfigurationProperty(
                    association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                        association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                            knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
        
                                        # the properties below are optional
                                        value="value"
                                    )],
                                    or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
        
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
        
                                            # the properties below are optional
                                            value="value"
                                        )
                                    )],
                                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
        
                                        # the properties below are optional
                                        value="value"
                                    )
                                ),
                                max_results=123,
                                override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                            )
                        ),
                        association_id="associationId",
                        association_type="associationType"
                    )],
                    self_service_ai_guardrail_id="selfServiceAiGuardrailId",
                    self_service_answer_generation_ai_prompt_id="selfServiceAnswerGenerationAiPromptId",
                    self_service_pre_processing_ai_prompt_id="selfServicePreProcessingAiPromptId"
                )
            ),
            type="type",
        
            # the properties below are optional
            description="description",
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
        assistant_id: builtins.str,
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.AIAgentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param assistant_id: The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
        :param configuration: Configuration for the AI Agent.
        :param type: The type of the AI Agent.
        :param description: The description of the AI Agent.
        :param name: The name of the AI Agent.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4d43de9ccaeb31eba5b0b613ecac25531a87bb9137652388e6196070f4622ab)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAIAgentProps(
            assistant_id=assistant_id,
            configuration=configuration,
            type=type,
            description=description,
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
            type_hints = typing.get_type_hints(_typecheckingstub__daf9bd162ab4eaa6b11972bcaf8372498a47b4ad8cf111130cabfae3f675d2b4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__569f9e85834b9b380045c7e9789b3ac0684022e3b37642b34e232ba9b451ade6)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAiAgentArn")
    def attr_ai_agent_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AI agent.

        :cloudformationAttribute: AIAgentArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiAgentArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAiAgentId")
    def attr_ai_agent_id(self) -> builtins.str:
        '''The identifier of the AI Agent.

        :cloudformationAttribute: AIAgentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiAgentId"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.

        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedTimeSeconds")
    def attr_modified_time_seconds(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: ModifiedTimeSeconds
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrModifiedTimeSeconds"))

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
    @jsii.member(jsii_name="assistantId")
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect assistant.'''
        return typing.cast(builtins.str, jsii.get(self, "assistantId"))

    @assistant_id.setter
    def assistant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3d8fd38839efd97edc463e08adcbeb6d1b964aa278b19d07017fb40c806bb19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assistantId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AIAgentConfigurationProperty"]:
        '''Configuration for the AI Agent.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AIAgentConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AIAgentConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d07c289ddb2abe8b14c5f581386f3377fb7266b5b099c89c1b142b4bbd9d769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the AI Agent.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b90fdd18e60e92e1589e2bf61b55c6cd7758b9da5e26d00525cb08a2ad13830)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the AI Agent.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6380f3badbada0c208691bd5242dfabe1122f10b446d77f1ae5ad0c9da456ae8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the AI Agent.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__982490f39ff188d23898421a1623ad1489db32be592625d58e01c368c7568247)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e3ed01afbf4aa2c01303d467dcbf5c5cd3fb267902b917f3c4f5fdd0d83ccdc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.AIAgentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "answer_recommendation_ai_agent_configuration": "answerRecommendationAiAgentConfiguration",
            "manual_search_ai_agent_configuration": "manualSearchAiAgentConfiguration",
            "self_service_ai_agent_configuration": "selfServiceAiAgentConfiguration",
        },
    )
    class AIAgentConfigurationProperty:
        def __init__(
            self,
            *,
            answer_recommendation_ai_agent_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            manual_search_ai_agent_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.ManualSearchAIAgentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            self_service_ai_agent_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.SelfServiceAIAgentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A typed union that specifies the configuration based on the type of AI Agent.

            :param answer_recommendation_ai_agent_configuration: The configuration for AI Agents of type ``ANSWER_RECOMMENDATION`` .
            :param manual_search_ai_agent_configuration: The configuration for AI Agents of type ``MANUAL_SEARCH`` .
            :param self_service_ai_agent_configuration: The self-service AI agent configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-aiagentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                a_iAgent_configuration_property = wisdom.CfnAIAgent.AIAgentConfigurationProperty(
                    answer_recommendation_ai_agent_configuration=wisdom.CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty(
                        answer_generation_ai_guardrail_id="answerGenerationAiGuardrailId",
                        answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                        association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                            association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                                knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                    content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                            and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
                
                                                # the properties below are optional
                                                value="value"
                                            )],
                                            tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
                
                                                # the properties below are optional
                                                value="value"
                                            )
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )
                                    ),
                                    max_results=123,
                                    override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                                )
                            ),
                            association_id="associationId",
                            association_type="associationType"
                        )],
                        intent_labeling_generation_ai_prompt_id="intentLabelingGenerationAiPromptId",
                        locale="locale",
                        query_reformulation_ai_prompt_id="queryReformulationAiPromptId"
                    ),
                    manual_search_ai_agent_configuration=wisdom.CfnAIAgent.ManualSearchAIAgentConfigurationProperty(
                        answer_generation_ai_guardrail_id="answerGenerationAiGuardrailId",
                        answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                        association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                            association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                                knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                    content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                            and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
                
                                                # the properties below are optional
                                                value="value"
                                            )],
                                            tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
                
                                                # the properties below are optional
                                                value="value"
                                            )
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )
                                    ),
                                    max_results=123,
                                    override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                                )
                            ),
                            association_id="associationId",
                            association_type="associationType"
                        )],
                        locale="locale"
                    ),
                    self_service_ai_agent_configuration=wisdom.CfnAIAgent.SelfServiceAIAgentConfigurationProperty(
                        association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                            association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                                knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                    content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                            and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
                
                                                # the properties below are optional
                                                value="value"
                                            )],
                                            tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
                
                                                # the properties below are optional
                                                value="value"
                                            )
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )
                                    ),
                                    max_results=123,
                                    override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                                )
                            ),
                            association_id="associationId",
                            association_type="associationType"
                        )],
                        self_service_ai_guardrail_id="selfServiceAiGuardrailId",
                        self_service_answer_generation_ai_prompt_id="selfServiceAnswerGenerationAiPromptId",
                        self_service_pre_processing_ai_prompt_id="selfServicePreProcessingAiPromptId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8cb84ad0dc27ffdae65e4e739c98ea6a4e7c36340f15c21ae83a2225ff763ba3)
                check_type(argname="argument answer_recommendation_ai_agent_configuration", value=answer_recommendation_ai_agent_configuration, expected_type=type_hints["answer_recommendation_ai_agent_configuration"])
                check_type(argname="argument manual_search_ai_agent_configuration", value=manual_search_ai_agent_configuration, expected_type=type_hints["manual_search_ai_agent_configuration"])
                check_type(argname="argument self_service_ai_agent_configuration", value=self_service_ai_agent_configuration, expected_type=type_hints["self_service_ai_agent_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if answer_recommendation_ai_agent_configuration is not None:
                self._values["answer_recommendation_ai_agent_configuration"] = answer_recommendation_ai_agent_configuration
            if manual_search_ai_agent_configuration is not None:
                self._values["manual_search_ai_agent_configuration"] = manual_search_ai_agent_configuration
            if self_service_ai_agent_configuration is not None:
                self._values["self_service_ai_agent_configuration"] = self_service_ai_agent_configuration

        @builtins.property
        def answer_recommendation_ai_agent_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty"]]:
            '''The configuration for AI Agents of type ``ANSWER_RECOMMENDATION`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-aiagentconfiguration.html#cfn-wisdom-aiagent-aiagentconfiguration-answerrecommendationaiagentconfiguration
            '''
            result = self._values.get("answer_recommendation_ai_agent_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty"]], result)

        @builtins.property
        def manual_search_ai_agent_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.ManualSearchAIAgentConfigurationProperty"]]:
            '''The configuration for AI Agents of type ``MANUAL_SEARCH`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-aiagentconfiguration.html#cfn-wisdom-aiagent-aiagentconfiguration-manualsearchaiagentconfiguration
            '''
            result = self._values.get("manual_search_ai_agent_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.ManualSearchAIAgentConfigurationProperty"]], result)

        @builtins.property
        def self_service_ai_agent_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.SelfServiceAIAgentConfigurationProperty"]]:
            '''The self-service AI agent configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-aiagentconfiguration.html#cfn-wisdom-aiagent-aiagentconfiguration-selfserviceaiagentconfiguration
            '''
            result = self._values.get("self_service_ai_agent_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.SelfServiceAIAgentConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AIAgentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "answer_generation_ai_guardrail_id": "answerGenerationAiGuardrailId",
            "answer_generation_ai_prompt_id": "answerGenerationAiPromptId",
            "association_configurations": "associationConfigurations",
            "intent_labeling_generation_ai_prompt_id": "intentLabelingGenerationAiPromptId",
            "locale": "locale",
            "query_reformulation_ai_prompt_id": "queryReformulationAiPromptId",
        },
    )
    class AnswerRecommendationAIAgentConfigurationProperty:
        def __init__(
            self,
            *,
            answer_generation_ai_guardrail_id: typing.Optional[builtins.str] = None,
            answer_generation_ai_prompt_id: typing.Optional[builtins.str] = None,
            association_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.AssociationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            intent_labeling_generation_ai_prompt_id: typing.Optional[builtins.str] = None,
            locale: typing.Optional[builtins.str] = None,
            query_reformulation_ai_prompt_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for AI Agents of type ``ANSWER_RECOMMENDATION`` .

            :param answer_generation_ai_guardrail_id: The ID of the answer generation AI guardrail.
            :param answer_generation_ai_prompt_id: The AI Prompt identifier for the Answer Generation prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.
            :param association_configurations: The association configurations for overriding behavior on this AI Agent.
            :param intent_labeling_generation_ai_prompt_id: The AI Prompt identifier for the Intent Labeling prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.
            :param locale: The locale to which specifies the language and region settings that determine the response language for `QueryAssistant <https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html>`_ .
            :param query_reformulation_ai_prompt_id: The AI Prompt identifier for the Query Reformulation prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                answer_recommendation_aIAgent_configuration_property = wisdom.CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty(
                    answer_generation_ai_guardrail_id="answerGenerationAiGuardrailId",
                    answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                    association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                        association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                            knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
                
                                        # the properties below are optional
                                        value="value"
                                    )],
                                    or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )
                                    )],
                                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
                
                                        # the properties below are optional
                                        value="value"
                                    )
                                ),
                                max_results=123,
                                override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                            )
                        ),
                        association_id="associationId",
                        association_type="associationType"
                    )],
                    intent_labeling_generation_ai_prompt_id="intentLabelingGenerationAiPromptId",
                    locale="locale",
                    query_reformulation_ai_prompt_id="queryReformulationAiPromptId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6847cf788b7def362d576a512b579b2a08c25837003298b7c57254d1dfb45112)
                check_type(argname="argument answer_generation_ai_guardrail_id", value=answer_generation_ai_guardrail_id, expected_type=type_hints["answer_generation_ai_guardrail_id"])
                check_type(argname="argument answer_generation_ai_prompt_id", value=answer_generation_ai_prompt_id, expected_type=type_hints["answer_generation_ai_prompt_id"])
                check_type(argname="argument association_configurations", value=association_configurations, expected_type=type_hints["association_configurations"])
                check_type(argname="argument intent_labeling_generation_ai_prompt_id", value=intent_labeling_generation_ai_prompt_id, expected_type=type_hints["intent_labeling_generation_ai_prompt_id"])
                check_type(argname="argument locale", value=locale, expected_type=type_hints["locale"])
                check_type(argname="argument query_reformulation_ai_prompt_id", value=query_reformulation_ai_prompt_id, expected_type=type_hints["query_reformulation_ai_prompt_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if answer_generation_ai_guardrail_id is not None:
                self._values["answer_generation_ai_guardrail_id"] = answer_generation_ai_guardrail_id
            if answer_generation_ai_prompt_id is not None:
                self._values["answer_generation_ai_prompt_id"] = answer_generation_ai_prompt_id
            if association_configurations is not None:
                self._values["association_configurations"] = association_configurations
            if intent_labeling_generation_ai_prompt_id is not None:
                self._values["intent_labeling_generation_ai_prompt_id"] = intent_labeling_generation_ai_prompt_id
            if locale is not None:
                self._values["locale"] = locale
            if query_reformulation_ai_prompt_id is not None:
                self._values["query_reformulation_ai_prompt_id"] = query_reformulation_ai_prompt_id

        @builtins.property
        def answer_generation_ai_guardrail_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the answer generation AI guardrail.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration.html#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-answergenerationaiguardrailid
            '''
            result = self._values.get("answer_generation_ai_guardrail_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def answer_generation_ai_prompt_id(self) -> typing.Optional[builtins.str]:
            '''The AI Prompt identifier for the Answer Generation prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration.html#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-answergenerationaipromptid
            '''
            result = self._values.get("answer_generation_ai_prompt_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def association_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AssociationConfigurationProperty"]]]]:
            '''The association configurations for overriding behavior on this AI Agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration.html#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-associationconfigurations
            '''
            result = self._values.get("association_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AssociationConfigurationProperty"]]]], result)

        @builtins.property
        def intent_labeling_generation_ai_prompt_id(
            self,
        ) -> typing.Optional[builtins.str]:
            '''The AI Prompt identifier for the Intent Labeling prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration.html#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-intentlabelinggenerationaipromptid
            '''
            result = self._values.get("intent_labeling_generation_ai_prompt_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def locale(self) -> typing.Optional[builtins.str]:
            '''The locale to which specifies the language and region settings that determine the response language for `QueryAssistant <https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration.html#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-locale
            '''
            result = self._values.get("locale")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def query_reformulation_ai_prompt_id(self) -> typing.Optional[builtins.str]:
            '''The AI Prompt identifier for the Query Reformulation prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-answerrecommendationaiagentconfiguration.html#cfn-wisdom-aiagent-answerrecommendationaiagentconfiguration-queryreformulationaipromptid
            '''
            result = self._values.get("query_reformulation_ai_prompt_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnswerRecommendationAIAgentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.AssociationConfigurationDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "knowledge_base_association_configuration_data": "knowledgeBaseAssociationConfigurationData",
        },
    )
    class AssociationConfigurationDataProperty:
        def __init__(
            self,
            *,
            knowledge_base_association_configuration_data: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A typed union of the data of the configuration for an Amazon Q in Connect Assistant Association.

            :param knowledge_base_association_configuration_data: The data of the configuration for a ``KNOWLEDGE_BASE`` type Amazon Q in Connect Assistant Association.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-associationconfigurationdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                association_configuration_data_property = wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                    knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                        content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                            and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                key="key",
                
                                # the properties below are optional
                                value="value"
                            )],
                            or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                    key="key",
                
                                    # the properties below are optional
                                    value="value"
                                )],
                                tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                    key="key",
                
                                    # the properties below are optional
                                    value="value"
                                )
                            )],
                            tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                key="key",
                
                                # the properties below are optional
                                value="value"
                            )
                        ),
                        max_results=123,
                        override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c351d3e3386a19a82d6920c115ac6f8c911a12da4a117a9c0676a8ff0038fd41)
                check_type(argname="argument knowledge_base_association_configuration_data", value=knowledge_base_association_configuration_data, expected_type=type_hints["knowledge_base_association_configuration_data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "knowledge_base_association_configuration_data": knowledge_base_association_configuration_data,
            }

        @builtins.property
        def knowledge_base_association_configuration_data(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty"]:
            '''The data of the configuration for a ``KNOWLEDGE_BASE`` type Amazon Q in Connect Assistant Association.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-associationconfigurationdata.html#cfn-wisdom-aiagent-associationconfigurationdata-knowledgebaseassociationconfigurationdata
            '''
            result = self._values.get("knowledge_base_association_configuration_data")
            assert result is not None, "Required property 'knowledge_base_association_configuration_data' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssociationConfigurationDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.AssociationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "association_configuration_data": "associationConfigurationData",
            "association_id": "associationId",
            "association_type": "associationType",
        },
    )
    class AssociationConfigurationProperty:
        def __init__(
            self,
            *,
            association_configuration_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.AssociationConfigurationDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            association_id: typing.Optional[builtins.str] = None,
            association_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for an Amazon Q in Connect Assistant Association.

            :param association_configuration_data: A typed union of the data of the configuration for an Amazon Q in Connect Assistant Association.
            :param association_id: The identifier of the association for this Association Configuration.
            :param association_type: The type of the association for this Association Configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-associationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                association_configuration_property = wisdom.CfnAIAgent.AssociationConfigurationProperty(
                    association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                        knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                            content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                    key="key",
                
                                    # the properties below are optional
                                    value="value"
                                )],
                                or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
                
                                        # the properties below are optional
                                        value="value"
                                    )],
                                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
                
                                        # the properties below are optional
                                        value="value"
                                    )
                                )],
                                tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                    key="key",
                
                                    # the properties below are optional
                                    value="value"
                                )
                            ),
                            max_results=123,
                            override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                        )
                    ),
                    association_id="associationId",
                    association_type="associationType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2df56062b7b8c55a883d0469e63c3aad05d8079bf21171f13f4e68d2f26fea44)
                check_type(argname="argument association_configuration_data", value=association_configuration_data, expected_type=type_hints["association_configuration_data"])
                check_type(argname="argument association_id", value=association_id, expected_type=type_hints["association_id"])
                check_type(argname="argument association_type", value=association_type, expected_type=type_hints["association_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if association_configuration_data is not None:
                self._values["association_configuration_data"] = association_configuration_data
            if association_id is not None:
                self._values["association_id"] = association_id
            if association_type is not None:
                self._values["association_type"] = association_type

        @builtins.property
        def association_configuration_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AssociationConfigurationDataProperty"]]:
            '''A typed union of the data of the configuration for an Amazon Q in Connect Assistant Association.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-associationconfiguration.html#cfn-wisdom-aiagent-associationconfiguration-associationconfigurationdata
            '''
            result = self._values.get("association_configuration_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AssociationConfigurationDataProperty"]], result)

        @builtins.property
        def association_id(self) -> typing.Optional[builtins.str]:
            '''The identifier of the association for this Association Configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-associationconfiguration.html#cfn-wisdom-aiagent-associationconfiguration-associationid
            '''
            result = self._values.get("association_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def association_type(self) -> typing.Optional[builtins.str]:
            '''The type of the association for this Association Configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-associationconfiguration.html#cfn-wisdom-aiagent-associationconfiguration-associationtype
            '''
            result = self._values.get("association_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssociationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "content_tag_filter": "contentTagFilter",
            "max_results": "maxResults",
            "override_knowledge_base_search_type": "overrideKnowledgeBaseSearchType",
        },
    )
    class KnowledgeBaseAssociationConfigurationDataProperty:
        def __init__(
            self,
            *,
            content_tag_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.TagFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            max_results: typing.Optional[jsii.Number] = None,
            override_knowledge_base_search_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The data of the configuration for a ``KNOWLEDGE_BASE`` type Amazon Q in Connect Assistant Association.

            :param content_tag_filter: An object that can be used to specify Tag conditions.
            :param max_results: The maximum number of results to return per page.
            :param override_knowledge_base_search_type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                knowledge_base_association_configuration_data_property = wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                    content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                            key="key",
                
                            # the properties below are optional
                            value="value"
                        )],
                        or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                            and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                key="key",
                
                                # the properties below are optional
                                value="value"
                            )],
                            tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                key="key",
                
                                # the properties below are optional
                                value="value"
                            )
                        )],
                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                            key="key",
                
                            # the properties below are optional
                            value="value"
                        )
                    ),
                    max_results=123,
                    override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__af25ecdf7592033a618b9a411d145fb2bd7b10ae3e9b0a04a4502e0dee139e27)
                check_type(argname="argument content_tag_filter", value=content_tag_filter, expected_type=type_hints["content_tag_filter"])
                check_type(argname="argument max_results", value=max_results, expected_type=type_hints["max_results"])
                check_type(argname="argument override_knowledge_base_search_type", value=override_knowledge_base_search_type, expected_type=type_hints["override_knowledge_base_search_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if content_tag_filter is not None:
                self._values["content_tag_filter"] = content_tag_filter
            if max_results is not None:
                self._values["max_results"] = max_results
            if override_knowledge_base_search_type is not None:
                self._values["override_knowledge_base_search_type"] = override_knowledge_base_search_type

        @builtins.property
        def content_tag_filter(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagFilterProperty"]]:
            '''An object that can be used to specify Tag conditions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata.html#cfn-wisdom-aiagent-knowledgebaseassociationconfigurationdata-contenttagfilter
            '''
            result = self._values.get("content_tag_filter")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagFilterProperty"]], result)

        @builtins.property
        def max_results(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of results to return per page.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata.html#cfn-wisdom-aiagent-knowledgebaseassociationconfigurationdata-maxresults
            '''
            result = self._values.get("max_results")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def override_knowledge_base_search_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-knowledgebaseassociationconfigurationdata.html#cfn-wisdom-aiagent-knowledgebaseassociationconfigurationdata-overrideknowledgebasesearchtype
            '''
            result = self._values.get("override_knowledge_base_search_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KnowledgeBaseAssociationConfigurationDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.ManualSearchAIAgentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "answer_generation_ai_guardrail_id": "answerGenerationAiGuardrailId",
            "answer_generation_ai_prompt_id": "answerGenerationAiPromptId",
            "association_configurations": "associationConfigurations",
            "locale": "locale",
        },
    )
    class ManualSearchAIAgentConfigurationProperty:
        def __init__(
            self,
            *,
            answer_generation_ai_guardrail_id: typing.Optional[builtins.str] = None,
            answer_generation_ai_prompt_id: typing.Optional[builtins.str] = None,
            association_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.AssociationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            locale: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for AI Agents of type ``MANUAL_SEARCH`` .

            :param answer_generation_ai_guardrail_id: The ID of the answer generation AI guardrail.
            :param answer_generation_ai_prompt_id: The AI Prompt identifier for the Answer Generation prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.
            :param association_configurations: The association configurations for overriding behavior on this AI Agent.
            :param locale: The locale to which specifies the language and region settings that determine the response language for `QueryAssistant <https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                manual_search_aIAgent_configuration_property = wisdom.CfnAIAgent.ManualSearchAIAgentConfigurationProperty(
                    answer_generation_ai_guardrail_id="answerGenerationAiGuardrailId",
                    answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                    association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                        association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                            knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
                
                                        # the properties below are optional
                                        value="value"
                                    )],
                                    or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )
                                    )],
                                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
                
                                        # the properties below are optional
                                        value="value"
                                    )
                                ),
                                max_results=123,
                                override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                            )
                        ),
                        association_id="associationId",
                        association_type="associationType"
                    )],
                    locale="locale"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3346eba3a05ad4b31350bf2c54edbb6063a18cfea8a25ebbab80c402438f039a)
                check_type(argname="argument answer_generation_ai_guardrail_id", value=answer_generation_ai_guardrail_id, expected_type=type_hints["answer_generation_ai_guardrail_id"])
                check_type(argname="argument answer_generation_ai_prompt_id", value=answer_generation_ai_prompt_id, expected_type=type_hints["answer_generation_ai_prompt_id"])
                check_type(argname="argument association_configurations", value=association_configurations, expected_type=type_hints["association_configurations"])
                check_type(argname="argument locale", value=locale, expected_type=type_hints["locale"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if answer_generation_ai_guardrail_id is not None:
                self._values["answer_generation_ai_guardrail_id"] = answer_generation_ai_guardrail_id
            if answer_generation_ai_prompt_id is not None:
                self._values["answer_generation_ai_prompt_id"] = answer_generation_ai_prompt_id
            if association_configurations is not None:
                self._values["association_configurations"] = association_configurations
            if locale is not None:
                self._values["locale"] = locale

        @builtins.property
        def answer_generation_ai_guardrail_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the answer generation AI guardrail.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration.html#cfn-wisdom-aiagent-manualsearchaiagentconfiguration-answergenerationaiguardrailid
            '''
            result = self._values.get("answer_generation_ai_guardrail_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def answer_generation_ai_prompt_id(self) -> typing.Optional[builtins.str]:
            '''The AI Prompt identifier for the Answer Generation prompt used by the ``ANSWER_RECOMMENDATION`` AI Agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration.html#cfn-wisdom-aiagent-manualsearchaiagentconfiguration-answergenerationaipromptid
            '''
            result = self._values.get("answer_generation_ai_prompt_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def association_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AssociationConfigurationProperty"]]]]:
            '''The association configurations for overriding behavior on this AI Agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration.html#cfn-wisdom-aiagent-manualsearchaiagentconfiguration-associationconfigurations
            '''
            result = self._values.get("association_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AssociationConfigurationProperty"]]]], result)

        @builtins.property
        def locale(self) -> typing.Optional[builtins.str]:
            '''The locale to which specifies the language and region settings that determine the response language for `QueryAssistant <https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QueryAssistant.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-manualsearchaiagentconfiguration.html#cfn-wisdom-aiagent-manualsearchaiagentconfiguration-locale
            '''
            result = self._values.get("locale")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManualSearchAIAgentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.OrConditionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "and_conditions": "andConditions",
            "tag_condition": "tagCondition",
        },
    )
    class OrConditionProperty:
        def __init__(
            self,
            *,
            and_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.TagConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            tag_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.TagConditionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param and_conditions: 
            :param tag_condition: A leaf node condition which can be used to specify a tag condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-orcondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                or_condition_property = wisdom.CfnAIAgent.OrConditionProperty(
                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                        key="key",
                
                        # the properties below are optional
                        value="value"
                    )],
                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                        key="key",
                
                        # the properties below are optional
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf2bbad68aea63c5546563872782e30b131382ddae5fbabf04602b928494d4d4)
                check_type(argname="argument and_conditions", value=and_conditions, expected_type=type_hints["and_conditions"])
                check_type(argname="argument tag_condition", value=tag_condition, expected_type=type_hints["tag_condition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if and_conditions is not None:
                self._values["and_conditions"] = and_conditions
            if tag_condition is not None:
                self._values["tag_condition"] = tag_condition

        @builtins.property
        def and_conditions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-orcondition.html#cfn-wisdom-aiagent-orcondition-andconditions
            '''
            result = self._values.get("and_conditions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]]]], result)

        @builtins.property
        def tag_condition(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]]:
            '''A leaf node condition which can be used to specify a tag condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-orcondition.html#cfn-wisdom-aiagent-orcondition-tagcondition
            '''
            result = self._values.get("tag_condition")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.SelfServiceAIAgentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "association_configurations": "associationConfigurations",
            "self_service_ai_guardrail_id": "selfServiceAiGuardrailId",
            "self_service_answer_generation_ai_prompt_id": "selfServiceAnswerGenerationAiPromptId",
            "self_service_pre_processing_ai_prompt_id": "selfServicePreProcessingAiPromptId",
        },
    )
    class SelfServiceAIAgentConfigurationProperty:
        def __init__(
            self,
            *,
            association_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.AssociationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            self_service_ai_guardrail_id: typing.Optional[builtins.str] = None,
            self_service_answer_generation_ai_prompt_id: typing.Optional[builtins.str] = None,
            self_service_pre_processing_ai_prompt_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration of the self-service AI agent.

            :param association_configurations: The association configuration of the self-service AI agent.
            :param self_service_ai_guardrail_id: The ID of the self-service AI guardrail.
            :param self_service_answer_generation_ai_prompt_id: The ID of the self-service answer generation AI prompt.
            :param self_service_pre_processing_ai_prompt_id: The ID of the self-service preprocessing AI prompt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-selfserviceaiagentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                self_service_aIAgent_configuration_property = wisdom.CfnAIAgent.SelfServiceAIAgentConfigurationProperty(
                    association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                        association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                            knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
                
                                        # the properties below are optional
                                        value="value"
                                    )],
                                    or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
                
                                            # the properties below are optional
                                            value="value"
                                        )
                                    )],
                                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                        key="key",
                
                                        # the properties below are optional
                                        value="value"
                                    )
                                ),
                                max_results=123,
                                override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                            )
                        ),
                        association_id="associationId",
                        association_type="associationType"
                    )],
                    self_service_ai_guardrail_id="selfServiceAiGuardrailId",
                    self_service_answer_generation_ai_prompt_id="selfServiceAnswerGenerationAiPromptId",
                    self_service_pre_processing_ai_prompt_id="selfServicePreProcessingAiPromptId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c0833e248a2b0215b05dd66ce2879efe35c5180b459e725cf02acb524808c7ec)
                check_type(argname="argument association_configurations", value=association_configurations, expected_type=type_hints["association_configurations"])
                check_type(argname="argument self_service_ai_guardrail_id", value=self_service_ai_guardrail_id, expected_type=type_hints["self_service_ai_guardrail_id"])
                check_type(argname="argument self_service_answer_generation_ai_prompt_id", value=self_service_answer_generation_ai_prompt_id, expected_type=type_hints["self_service_answer_generation_ai_prompt_id"])
                check_type(argname="argument self_service_pre_processing_ai_prompt_id", value=self_service_pre_processing_ai_prompt_id, expected_type=type_hints["self_service_pre_processing_ai_prompt_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if association_configurations is not None:
                self._values["association_configurations"] = association_configurations
            if self_service_ai_guardrail_id is not None:
                self._values["self_service_ai_guardrail_id"] = self_service_ai_guardrail_id
            if self_service_answer_generation_ai_prompt_id is not None:
                self._values["self_service_answer_generation_ai_prompt_id"] = self_service_answer_generation_ai_prompt_id
            if self_service_pre_processing_ai_prompt_id is not None:
                self._values["self_service_pre_processing_ai_prompt_id"] = self_service_pre_processing_ai_prompt_id

        @builtins.property
        def association_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AssociationConfigurationProperty"]]]]:
            '''The association configuration of the self-service AI agent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-selfserviceaiagentconfiguration.html#cfn-wisdom-aiagent-selfserviceaiagentconfiguration-associationconfigurations
            '''
            result = self._values.get("association_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.AssociationConfigurationProperty"]]]], result)

        @builtins.property
        def self_service_ai_guardrail_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the self-service AI guardrail.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-selfserviceaiagentconfiguration.html#cfn-wisdom-aiagent-selfserviceaiagentconfiguration-selfserviceaiguardrailid
            '''
            result = self._values.get("self_service_ai_guardrail_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def self_service_answer_generation_ai_prompt_id(
            self,
        ) -> typing.Optional[builtins.str]:
            '''The ID of the self-service answer generation AI prompt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-selfserviceaiagentconfiguration.html#cfn-wisdom-aiagent-selfserviceaiagentconfiguration-selfserviceanswergenerationaipromptid
            '''
            result = self._values.get("self_service_answer_generation_ai_prompt_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def self_service_pre_processing_ai_prompt_id(
            self,
        ) -> typing.Optional[builtins.str]:
            '''The ID of the self-service preprocessing AI prompt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-selfserviceaiagentconfiguration.html#cfn-wisdom-aiagent-selfserviceaiagentconfiguration-selfservicepreprocessingaipromptid
            '''
            result = self._values.get("self_service_pre_processing_ai_prompt_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SelfServiceAIAgentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.TagConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagConditionProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that can be used to specify tag conditions.

            :param key: The tag key in the tag condition.
            :param value: The tag value in the tag condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagcondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                tag_condition_property = wisdom.CfnAIAgent.TagConditionProperty(
                    key="key",
                
                    # the properties below are optional
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__76535774a57202e416fb208d73c095c91408f65fd8a1b99f6b568fd994b915e9)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
            }
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> builtins.str:
            '''The tag key in the tag condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagcondition.html#cfn-wisdom-aiagent-tagcondition-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The tag value in the tag condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagcondition.html#cfn-wisdom-aiagent-tagcondition-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgent.TagFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "and_conditions": "andConditions",
            "or_conditions": "orConditions",
            "tag_condition": "tagCondition",
        },
    )
    class TagFilterProperty:
        def __init__(
            self,
            *,
            and_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.TagConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            or_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.OrConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            tag_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIAgent.TagConditionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An object that can be used to specify tag conditions.

            :param and_conditions: A list of conditions which would be applied together with an ``AND`` condition.
            :param or_conditions: A list of conditions which would be applied together with an ``OR`` condition.
            :param tag_condition: A leaf node condition which can be used to specify a tag condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                tag_filter_property = wisdom.CfnAIAgent.TagFilterProperty(
                    and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                        key="key",
                
                        # the properties below are optional
                        value="value"
                    )],
                    or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                            key="key",
                
                            # the properties below are optional
                            value="value"
                        )],
                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                            key="key",
                
                            # the properties below are optional
                            value="value"
                        )
                    )],
                    tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                        key="key",
                
                        # the properties below are optional
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__47961a691b994d09a0537dc7d655a0aab653585a5e8bd78b30c4bc84ec243c19)
                check_type(argname="argument and_conditions", value=and_conditions, expected_type=type_hints["and_conditions"])
                check_type(argname="argument or_conditions", value=or_conditions, expected_type=type_hints["or_conditions"])
                check_type(argname="argument tag_condition", value=tag_condition, expected_type=type_hints["tag_condition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if and_conditions is not None:
                self._values["and_conditions"] = and_conditions
            if or_conditions is not None:
                self._values["or_conditions"] = or_conditions
            if tag_condition is not None:
                self._values["tag_condition"] = tag_condition

        @builtins.property
        def and_conditions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]]]]:
            '''A list of conditions which would be applied together with an ``AND`` condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagfilter.html#cfn-wisdom-aiagent-tagfilter-andconditions
            '''
            result = self._values.get("and_conditions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]]]], result)

        @builtins.property
        def or_conditions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.OrConditionProperty"]]]]:
            '''A list of conditions which would be applied together with an ``OR`` condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagfilter.html#cfn-wisdom-aiagent-tagfilter-orconditions
            '''
            result = self._values.get("or_conditions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.OrConditionProperty"]]]], result)

        @builtins.property
        def tag_condition(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]]:
            '''A leaf node condition which can be used to specify a tag condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiagent-tagfilter.html#cfn-wisdom-aiagent-tagfilter-tagcondition
            '''
            result = self._values.get("tag_condition")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIAgent.TagConditionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgentProps",
    jsii_struct_bases=[],
    name_mapping={
        "assistant_id": "assistantId",
        "configuration": "configuration",
        "type": "type",
        "description": "description",
        "name": "name",
        "tags": "tags",
    },
)
class CfnAIAgentProps:
    def __init__(
        self,
        *,
        assistant_id: builtins.str,
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.AIAgentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAIAgent``.

        :param assistant_id: The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
        :param configuration: Configuration for the AI Agent.
        :param type: The type of the AI Agent.
        :param description: The description of the AI Agent.
        :param name: The name of the AI Agent.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_aIAgent_props = wisdom.CfnAIAgentProps(
                assistant_id="assistantId",
                configuration=wisdom.CfnAIAgent.AIAgentConfigurationProperty(
                    answer_recommendation_ai_agent_configuration=wisdom.CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty(
                        answer_generation_ai_guardrail_id="answerGenerationAiGuardrailId",
                        answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                        association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                            association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                                knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                    content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
            
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                            and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
            
                                                # the properties below are optional
                                                value="value"
                                            )],
                                            tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
            
                                                # the properties below are optional
                                                value="value"
                                            )
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
            
                                            # the properties below are optional
                                            value="value"
                                        )
                                    ),
                                    max_results=123,
                                    override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                                )
                            ),
                            association_id="associationId",
                            association_type="associationType"
                        )],
                        intent_labeling_generation_ai_prompt_id="intentLabelingGenerationAiPromptId",
                        locale="locale",
                        query_reformulation_ai_prompt_id="queryReformulationAiPromptId"
                    ),
                    manual_search_ai_agent_configuration=wisdom.CfnAIAgent.ManualSearchAIAgentConfigurationProperty(
                        answer_generation_ai_guardrail_id="answerGenerationAiGuardrailId",
                        answer_generation_ai_prompt_id="answerGenerationAiPromptId",
                        association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                            association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                                knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                    content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
            
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                            and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
            
                                                # the properties below are optional
                                                value="value"
                                            )],
                                            tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
            
                                                # the properties below are optional
                                                value="value"
                                            )
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
            
                                            # the properties below are optional
                                            value="value"
                                        )
                                    ),
                                    max_results=123,
                                    override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                                )
                            ),
                            association_id="associationId",
                            association_type="associationType"
                        )],
                        locale="locale"
                    ),
                    self_service_ai_agent_configuration=wisdom.CfnAIAgent.SelfServiceAIAgentConfigurationProperty(
                        association_configurations=[wisdom.CfnAIAgent.AssociationConfigurationProperty(
                            association_configuration_data=wisdom.CfnAIAgent.AssociationConfigurationDataProperty(
                                knowledge_base_association_configuration_data=wisdom.CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty(
                                    content_tag_filter=wisdom.CfnAIAgent.TagFilterProperty(
                                        and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
            
                                            # the properties below are optional
                                            value="value"
                                        )],
                                        or_conditions=[wisdom.CfnAIAgent.OrConditionProperty(
                                            and_conditions=[wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
            
                                                # the properties below are optional
                                                value="value"
                                            )],
                                            tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                                key="key",
            
                                                # the properties below are optional
                                                value="value"
                                            )
                                        )],
                                        tag_condition=wisdom.CfnAIAgent.TagConditionProperty(
                                            key="key",
            
                                            # the properties below are optional
                                            value="value"
                                        )
                                    ),
                                    max_results=123,
                                    override_knowledge_base_search_type="overrideKnowledgeBaseSearchType"
                                )
                            ),
                            association_id="associationId",
                            association_type="associationType"
                        )],
                        self_service_ai_guardrail_id="selfServiceAiGuardrailId",
                        self_service_answer_generation_ai_prompt_id="selfServiceAnswerGenerationAiPromptId",
                        self_service_pre_processing_ai_prompt_id="selfServicePreProcessingAiPromptId"
                    )
                ),
                type="type",
            
                # the properties below are optional
                description="description",
                name="name",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1cda9a6282ec07c28c0ef49efdf8da8f079052d26edd32bbe15324644982756)
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "assistant_id": assistant_id,
            "configuration": configuration,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect assistant.

        Can be either the ID or the ARN. URLs cannot contain the ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html#cfn-wisdom-aiagent-assistantid
        '''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAIAgent.AIAgentConfigurationProperty]:
        '''Configuration for the AI Agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html#cfn-wisdom-aiagent-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAIAgent.AIAgentConfigurationProperty], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the AI Agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html#cfn-wisdom-aiagent-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the AI Agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html#cfn-wisdom-aiagent-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the AI Agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html#cfn-wisdom-aiagent-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html#cfn-wisdom-aiagent-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAIAgentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAIAgentVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgentVersion",
):
    '''Creates and Amazon Q in Connect AI Agent version.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagentversion.html
    :cloudformationResource: AWS::Wisdom::AIAgentVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_aIAgent_version = wisdom.CfnAIAgentVersion(self, "MyCfnAIAgentVersion",
            ai_agent_id="aiAgentId",
            assistant_id="assistantId",
        
            # the properties below are optional
            modified_time_seconds=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        ai_agent_id: builtins.str,
        assistant_id: builtins.str,
        modified_time_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param ai_agent_id: The identifier of the AI Agent.
        :param assistant_id: 
        :param modified_time_seconds: The time the AI Agent version was last modified in seconds.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa5a166c3d658d9410f80c3ff44a4aee88b29cb4def5f6c7d811c5b47f5ffb68)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAIAgentVersionProps(
            ai_agent_id=ai_agent_id,
            assistant_id=assistant_id,
            modified_time_seconds=modified_time_seconds,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eec3c0a8aee757b615051ab77f3708fef64acd48758d58f7b8801c7073f3ea55)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1eec2d46406b6deb09ae2fc5f30e9bb5223c8f293091f02f7d13f928906953a1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAiAgentArn")
    def attr_ai_agent_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AIAgentArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiAgentArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAiAgentVersionId")
    def attr_ai_agent_version_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AIAgentVersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiAgentVersionId"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionNumber")
    def attr_version_number(self) -> _IResolvable_da3f097b:
        '''The version number for this AI Agent version.

        :cloudformationAttribute: VersionNumber
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrVersionNumber"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="aiAgentId")
    def ai_agent_id(self) -> builtins.str:
        '''The identifier of the AI Agent.'''
        return typing.cast(builtins.str, jsii.get(self, "aiAgentId"))

    @ai_agent_id.setter
    def ai_agent_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df356486e6fdad853cdc4c3aa5d62a5febffd1441d8e82f3a672bf4aef6e809d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aiAgentId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assistantId")
    def assistant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "assistantId"))

    @assistant_id.setter
    def assistant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3c00eedc618755e116ec4cf13129b9ecab51c03e0aa3285aa6c4eca0e7c9311)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assistantId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="modifiedTimeSeconds")
    def modified_time_seconds(self) -> typing.Optional[jsii.Number]:
        '''The time the AI Agent version was last modified in seconds.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "modifiedTimeSeconds"))

    @modified_time_seconds.setter
    def modified_time_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cbb04d6951221f1cfd98bc4ebed42ba72b9f79a3ef0707bfcea622572f06cd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modifiedTimeSeconds", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIAgentVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "ai_agent_id": "aiAgentId",
        "assistant_id": "assistantId",
        "modified_time_seconds": "modifiedTimeSeconds",
    },
)
class CfnAIAgentVersionProps:
    def __init__(
        self,
        *,
        ai_agent_id: builtins.str,
        assistant_id: builtins.str,
        modified_time_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnAIAgentVersion``.

        :param ai_agent_id: The identifier of the AI Agent.
        :param assistant_id: 
        :param modified_time_seconds: The time the AI Agent version was last modified in seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagentversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_aIAgent_version_props = wisdom.CfnAIAgentVersionProps(
                ai_agent_id="aiAgentId",
                assistant_id="assistantId",
            
                # the properties below are optional
                modified_time_seconds=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ce55b0c69b9bc58cfcaeadaff04d7986170a5f73af9f6157ba1fe19c79b250e)
            check_type(argname="argument ai_agent_id", value=ai_agent_id, expected_type=type_hints["ai_agent_id"])
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument modified_time_seconds", value=modified_time_seconds, expected_type=type_hints["modified_time_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ai_agent_id": ai_agent_id,
            "assistant_id": assistant_id,
        }
        if modified_time_seconds is not None:
            self._values["modified_time_seconds"] = modified_time_seconds

    @builtins.property
    def ai_agent_id(self) -> builtins.str:
        '''The identifier of the AI Agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagentversion.html#cfn-wisdom-aiagentversion-aiagentid
        '''
        result = self._values.get("ai_agent_id")
        assert result is not None, "Required property 'ai_agent_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagentversion.html#cfn-wisdom-aiagentversion-assistantid
        '''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def modified_time_seconds(self) -> typing.Optional[jsii.Number]:
        '''The time the AI Agent version was last modified in seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagentversion.html#cfn-wisdom-aiagentversion-modifiedtimeseconds
        '''
        result = self._values.get("modified_time_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAIAgentVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnAIGuardrail(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrail",
):
    '''Creates an Amazon Q in Connect AI Guardrail.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrail.html
    :cloudformationResource: AWS::Wisdom::AIGuardrail
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_aIGuardrail = wisdom.CfnAIGuardrail(self, "MyCfnAIGuardrail",
            assistant_id="assistantId",
            blocked_input_messaging="blockedInputMessaging",
            blocked_outputs_messaging="blockedOutputsMessaging",
        
            # the properties below are optional
            content_policy_config=wisdom.CfnAIGuardrail.AIGuardrailContentPolicyConfigProperty(
                filters_config=[wisdom.CfnAIGuardrail.GuardrailContentFilterConfigProperty(
                    input_strength="inputStrength",
                    output_strength="outputStrength",
                    type="type"
                )]
            ),
            contextual_grounding_policy_config=wisdom.CfnAIGuardrail.AIGuardrailContextualGroundingPolicyConfigProperty(
                filters_config=[wisdom.CfnAIGuardrail.GuardrailContextualGroundingFilterConfigProperty(
                    threshold=123,
                    type="type"
                )]
            ),
            description="description",
            name="name",
            sensitive_information_policy_config=wisdom.CfnAIGuardrail.AIGuardrailSensitiveInformationPolicyConfigProperty(
                pii_entities_config=[wisdom.CfnAIGuardrail.GuardrailPiiEntityConfigProperty(
                    action="action",
                    type="type"
                )],
                regexes_config=[wisdom.CfnAIGuardrail.GuardrailRegexConfigProperty(
                    action="action",
                    name="name",
                    pattern="pattern",
        
                    # the properties below are optional
                    description="description"
                )]
            ),
            tags={
                "tags_key": "tags"
            },
            topic_policy_config=wisdom.CfnAIGuardrail.AIGuardrailTopicPolicyConfigProperty(
                topics_config=[wisdom.CfnAIGuardrail.GuardrailTopicConfigProperty(
                    definition="definition",
                    name="name",
                    type="type",
        
                    # the properties below are optional
                    examples=["examples"]
                )]
            ),
            word_policy_config=wisdom.CfnAIGuardrail.AIGuardrailWordPolicyConfigProperty(
                managed_word_lists_config=[wisdom.CfnAIGuardrail.GuardrailManagedWordsConfigProperty(
                    type="type"
                )],
                words_config=[wisdom.CfnAIGuardrail.GuardrailWordConfigProperty(
                    text="text"
                )]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        assistant_id: builtins.str,
        blocked_input_messaging: builtins.str,
        blocked_outputs_messaging: builtins.str,
        content_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIGuardrail.AIGuardrailContentPolicyConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        contextual_grounding_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIGuardrail.AIGuardrailContextualGroundingPolicyConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        sensitive_information_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIGuardrail.AIGuardrailSensitiveInformationPolicyConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        topic_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIGuardrail.AIGuardrailTopicPolicyConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        word_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIGuardrail.AIGuardrailWordPolicyConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param assistant_id: The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
        :param blocked_input_messaging: The message to return when the AI Guardrail blocks a prompt.
        :param blocked_outputs_messaging: The message to return when the AI Guardrail blocks a model response.
        :param content_policy_config: Contains details about how to handle harmful content.
        :param contextual_grounding_policy_config: The policy configuration details for the AI Guardrail's contextual grounding policy.
        :param description: A description of the AI Guardrail.
        :param name: The name of the AI Guardrail.
        :param sensitive_information_policy_config: Contains details about PII entities and regular expressions to configure for the AI Guardrail.
        :param tags: The tags used to organize, track, or control access for this resource.
        :param topic_policy_config: Contains details about topics that the AI Guardrail should identify and deny.
        :param word_policy_config: Contains details about the word policy to configured for the AI Guardrail.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76ea8e26c58eaed3d156b1860dd33693ef608e81ac9c96aa849d3236df58330b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAIGuardrailProps(
            assistant_id=assistant_id,
            blocked_input_messaging=blocked_input_messaging,
            blocked_outputs_messaging=blocked_outputs_messaging,
            content_policy_config=content_policy_config,
            contextual_grounding_policy_config=contextual_grounding_policy_config,
            description=description,
            name=name,
            sensitive_information_policy_config=sensitive_information_policy_config,
            tags=tags,
            topic_policy_config=topic_policy_config,
            word_policy_config=word_policy_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fbdc5de28d3c991f79f98e3c345ade75e45ce50bdb72f64634f0031d019b3e0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__71dcd22a9ef76aa3a7c280a922b91cc6f9cd7b114a93623bb44dbc112e60ec54)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAiGuardrailArn")
    def attr_ai_guardrail_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AI Guardrail.

        :cloudformationAttribute: AIGuardrailArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiGuardrailArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAiGuardrailId")
    def attr_ai_guardrail_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect AI Guardrail.

        :cloudformationAttribute: AIGuardrailId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiGuardrailId"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.

        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

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
    @jsii.member(jsii_name="assistantId")
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect assistant.'''
        return typing.cast(builtins.str, jsii.get(self, "assistantId"))

    @assistant_id.setter
    def assistant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24f61192b3941f9e6c1d63e119a6d1f1ac8e4e31bfb9beda991736af85ba7edc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assistantId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="blockedInputMessaging")
    def blocked_input_messaging(self) -> builtins.str:
        '''The message to return when the AI Guardrail blocks a prompt.'''
        return typing.cast(builtins.str, jsii.get(self, "blockedInputMessaging"))

    @blocked_input_messaging.setter
    def blocked_input_messaging(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a3f10e3678233e9583c04468dd2fa9082d1099e59298bafe2cbef0c5d3a0a58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockedInputMessaging", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="blockedOutputsMessaging")
    def blocked_outputs_messaging(self) -> builtins.str:
        '''The message to return when the AI Guardrail blocks a model response.'''
        return typing.cast(builtins.str, jsii.get(self, "blockedOutputsMessaging"))

    @blocked_outputs_messaging.setter
    def blocked_outputs_messaging(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab881749cd994050fdfe9190c2ad83d2d5995d553667532d5b3046c5784f3a46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockedOutputsMessaging", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="contentPolicyConfig")
    def content_policy_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.AIGuardrailContentPolicyConfigProperty"]]:
        '''Contains details about how to handle harmful content.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.AIGuardrailContentPolicyConfigProperty"]], jsii.get(self, "contentPolicyConfig"))

    @content_policy_config.setter
    def content_policy_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.AIGuardrailContentPolicyConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af0b681055aef2365d977a2adefd9d9d8538dd4e7497bed81a040c4d3e6d1013)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentPolicyConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="contextualGroundingPolicyConfig")
    def contextual_grounding_policy_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.AIGuardrailContextualGroundingPolicyConfigProperty"]]:
        '''The policy configuration details for the AI Guardrail's contextual grounding policy.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.AIGuardrailContextualGroundingPolicyConfigProperty"]], jsii.get(self, "contextualGroundingPolicyConfig"))

    @contextual_grounding_policy_config.setter
    def contextual_grounding_policy_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.AIGuardrailContextualGroundingPolicyConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6f963ab8c2eace9b626eca75747edc1eef5302cb2ca185e3c17ef190404aa68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contextualGroundingPolicyConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the AI Guardrail.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13bc08d099c391203a59ca71c4b7738f433a55e9dce1b3ec45bc792ea35be252)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the AI Guardrail.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5074d801992ea9ab774216aab1356ca4243d514bdf42abc16be1a957239bdca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sensitiveInformationPolicyConfig")
    def sensitive_information_policy_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.AIGuardrailSensitiveInformationPolicyConfigProperty"]]:
        '''Contains details about PII entities and regular expressions to configure for the AI Guardrail.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.AIGuardrailSensitiveInformationPolicyConfigProperty"]], jsii.get(self, "sensitiveInformationPolicyConfig"))

    @sensitive_information_policy_config.setter
    def sensitive_information_policy_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.AIGuardrailSensitiveInformationPolicyConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e94179fb829e66c40130c72071c91ec85dbd64f5e3e9cbe35c4966a40c3fefda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sensitiveInformationPolicyConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c295406d2cf871f486448002b556c3b63d9432e2114674011371326c1ba7c1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="topicPolicyConfig")
    def topic_policy_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.AIGuardrailTopicPolicyConfigProperty"]]:
        '''Contains details about topics that the AI Guardrail should identify and deny.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.AIGuardrailTopicPolicyConfigProperty"]], jsii.get(self, "topicPolicyConfig"))

    @topic_policy_config.setter
    def topic_policy_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.AIGuardrailTopicPolicyConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8bb338f6da5f73bdb4820c73ee887f612953bf85b2d8bd54e7541ea081f4f53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topicPolicyConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wordPolicyConfig")
    def word_policy_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.AIGuardrailWordPolicyConfigProperty"]]:
        '''Contains details about the word policy to configured for the AI Guardrail.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.AIGuardrailWordPolicyConfigProperty"]], jsii.get(self, "wordPolicyConfig"))

    @word_policy_config.setter
    def word_policy_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.AIGuardrailWordPolicyConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f41825c818a79784ab378059125875eeee0524136b34267aa4caca170457da14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wordPolicyConfig", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrail.AIGuardrailContentPolicyConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"filters_config": "filtersConfig"},
    )
    class AIGuardrailContentPolicyConfigProperty:
        def __init__(
            self,
            *,
            filters_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIGuardrail.GuardrailContentFilterConfigProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Content policy config for a guardrail.

            :param filters_config: List of content filter configurations in a content policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailcontentpolicyconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                a_iGuardrail_content_policy_config_property = wisdom.CfnAIGuardrail.AIGuardrailContentPolicyConfigProperty(
                    filters_config=[wisdom.CfnAIGuardrail.GuardrailContentFilterConfigProperty(
                        input_strength="inputStrength",
                        output_strength="outputStrength",
                        type="type"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3b7764340b5366a000b7609f9e6c1b7857f2afd9dca723fd492a1e331b82b32)
                check_type(argname="argument filters_config", value=filters_config, expected_type=type_hints["filters_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "filters_config": filters_config,
            }

        @builtins.property
        def filters_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.GuardrailContentFilterConfigProperty"]]]:
            '''List of content filter configurations in a content policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailcontentpolicyconfig.html#cfn-wisdom-aiguardrail-aiguardrailcontentpolicyconfig-filtersconfig
            '''
            result = self._values.get("filters_config")
            assert result is not None, "Required property 'filters_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.GuardrailContentFilterConfigProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AIGuardrailContentPolicyConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrail.AIGuardrailContextualGroundingPolicyConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"filters_config": "filtersConfig"},
    )
    class AIGuardrailContextualGroundingPolicyConfigProperty:
        def __init__(
            self,
            *,
            filters_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIGuardrail.GuardrailContextualGroundingFilterConfigProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Contextual grounding policy config for a guardrail.

            :param filters_config: List of contextual grounding filter configs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailcontextualgroundingpolicyconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                a_iGuardrail_contextual_grounding_policy_config_property = wisdom.CfnAIGuardrail.AIGuardrailContextualGroundingPolicyConfigProperty(
                    filters_config=[wisdom.CfnAIGuardrail.GuardrailContextualGroundingFilterConfigProperty(
                        threshold=123,
                        type="type"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b8b3e67068f407c2f3042d1380119651fa9edd8b97c312dbce41168ba5036ce3)
                check_type(argname="argument filters_config", value=filters_config, expected_type=type_hints["filters_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "filters_config": filters_config,
            }

        @builtins.property
        def filters_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.GuardrailContextualGroundingFilterConfigProperty"]]]:
            '''List of contextual grounding filter configs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailcontextualgroundingpolicyconfig.html#cfn-wisdom-aiguardrail-aiguardrailcontextualgroundingpolicyconfig-filtersconfig
            '''
            result = self._values.get("filters_config")
            assert result is not None, "Required property 'filters_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.GuardrailContextualGroundingFilterConfigProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AIGuardrailContextualGroundingPolicyConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrail.AIGuardrailSensitiveInformationPolicyConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "pii_entities_config": "piiEntitiesConfig",
            "regexes_config": "regexesConfig",
        },
    )
    class AIGuardrailSensitiveInformationPolicyConfigProperty:
        def __init__(
            self,
            *,
            pii_entities_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIGuardrail.GuardrailPiiEntityConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            regexes_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIGuardrail.GuardrailRegexConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Sensitive information policy configuration for a guardrail.

            :param pii_entities_config: List of entities.
            :param regexes_config: List of regex.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                a_iGuardrail_sensitive_information_policy_config_property = wisdom.CfnAIGuardrail.AIGuardrailSensitiveInformationPolicyConfigProperty(
                    pii_entities_config=[wisdom.CfnAIGuardrail.GuardrailPiiEntityConfigProperty(
                        action="action",
                        type="type"
                    )],
                    regexes_config=[wisdom.CfnAIGuardrail.GuardrailRegexConfigProperty(
                        action="action",
                        name="name",
                        pattern="pattern",
                
                        # the properties below are optional
                        description="description"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b1019f2767cdb75a66ac9e6dbb808d33ced4e1d098b227029ca4e8aaace98331)
                check_type(argname="argument pii_entities_config", value=pii_entities_config, expected_type=type_hints["pii_entities_config"])
                check_type(argname="argument regexes_config", value=regexes_config, expected_type=type_hints["regexes_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if pii_entities_config is not None:
                self._values["pii_entities_config"] = pii_entities_config
            if regexes_config is not None:
                self._values["regexes_config"] = regexes_config

        @builtins.property
        def pii_entities_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.GuardrailPiiEntityConfigProperty"]]]]:
            '''List of entities.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig.html#cfn-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig-piientitiesconfig
            '''
            result = self._values.get("pii_entities_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.GuardrailPiiEntityConfigProperty"]]]], result)

        @builtins.property
        def regexes_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.GuardrailRegexConfigProperty"]]]]:
            '''List of regex.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig.html#cfn-wisdom-aiguardrail-aiguardrailsensitiveinformationpolicyconfig-regexesconfig
            '''
            result = self._values.get("regexes_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.GuardrailRegexConfigProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AIGuardrailSensitiveInformationPolicyConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrail.AIGuardrailTopicPolicyConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"topics_config": "topicsConfig"},
    )
    class AIGuardrailTopicPolicyConfigProperty:
        def __init__(
            self,
            *,
            topics_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIGuardrail.GuardrailTopicConfigProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Topic policy configuration for a guardrail.

            :param topics_config: List of topic configs in topic policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailtopicpolicyconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                a_iGuardrail_topic_policy_config_property = wisdom.CfnAIGuardrail.AIGuardrailTopicPolicyConfigProperty(
                    topics_config=[wisdom.CfnAIGuardrail.GuardrailTopicConfigProperty(
                        definition="definition",
                        name="name",
                        type="type",
                
                        # the properties below are optional
                        examples=["examples"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c9fd7602104f512891874b785e4236b2dd9131ea684d5c3e16792b3e5f9a3767)
                check_type(argname="argument topics_config", value=topics_config, expected_type=type_hints["topics_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "topics_config": topics_config,
            }

        @builtins.property
        def topics_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.GuardrailTopicConfigProperty"]]]:
            '''List of topic configs in topic policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailtopicpolicyconfig.html#cfn-wisdom-aiguardrail-aiguardrailtopicpolicyconfig-topicsconfig
            '''
            result = self._values.get("topics_config")
            assert result is not None, "Required property 'topics_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.GuardrailTopicConfigProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AIGuardrailTopicPolicyConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrail.AIGuardrailWordPolicyConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "managed_word_lists_config": "managedWordListsConfig",
            "words_config": "wordsConfig",
        },
    )
    class AIGuardrailWordPolicyConfigProperty:
        def __init__(
            self,
            *,
            managed_word_lists_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIGuardrail.GuardrailManagedWordsConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            words_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIGuardrail.GuardrailWordConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Word policy config for a guardrail.

            :param managed_word_lists_config: A config for the list of managed words.
            :param words_config: List of custom word configurations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailwordpolicyconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                a_iGuardrail_word_policy_config_property = wisdom.CfnAIGuardrail.AIGuardrailWordPolicyConfigProperty(
                    managed_word_lists_config=[wisdom.CfnAIGuardrail.GuardrailManagedWordsConfigProperty(
                        type="type"
                    )],
                    words_config=[wisdom.CfnAIGuardrail.GuardrailWordConfigProperty(
                        text="text"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ddb251dfe6c0ff4b7a273bddeb253f5fc859e92197286c2d46566bdebdb6837d)
                check_type(argname="argument managed_word_lists_config", value=managed_word_lists_config, expected_type=type_hints["managed_word_lists_config"])
                check_type(argname="argument words_config", value=words_config, expected_type=type_hints["words_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if managed_word_lists_config is not None:
                self._values["managed_word_lists_config"] = managed_word_lists_config
            if words_config is not None:
                self._values["words_config"] = words_config

        @builtins.property
        def managed_word_lists_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.GuardrailManagedWordsConfigProperty"]]]]:
            '''A config for the list of managed words.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailwordpolicyconfig.html#cfn-wisdom-aiguardrail-aiguardrailwordpolicyconfig-managedwordlistsconfig
            '''
            result = self._values.get("managed_word_lists_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.GuardrailManagedWordsConfigProperty"]]]], result)

        @builtins.property
        def words_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.GuardrailWordConfigProperty"]]]]:
            '''List of custom word configurations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-aiguardrailwordpolicyconfig.html#cfn-wisdom-aiguardrail-aiguardrailwordpolicyconfig-wordsconfig
            '''
            result = self._values.get("words_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAIGuardrail.GuardrailWordConfigProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AIGuardrailWordPolicyConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrail.GuardrailContentFilterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_strength": "inputStrength",
            "output_strength": "outputStrength",
            "type": "type",
        },
    )
    class GuardrailContentFilterConfigProperty:
        def __init__(
            self,
            *,
            input_strength: builtins.str,
            output_strength: builtins.str,
            type: builtins.str,
        ) -> None:
            '''Content filter configuration in content policy.

            :param input_strength: The strength of the input for the guardrail content filter.
            :param output_strength: The output strength of the guardrail content filter.
            :param type: The type of the guardrail content filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailcontentfilterconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                guardrail_content_filter_config_property = wisdom.CfnAIGuardrail.GuardrailContentFilterConfigProperty(
                    input_strength="inputStrength",
                    output_strength="outputStrength",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e47d1e764075659f79a8e65f93d2613f269a815edddfaa5255b97587dc9f2a91)
                check_type(argname="argument input_strength", value=input_strength, expected_type=type_hints["input_strength"])
                check_type(argname="argument output_strength", value=output_strength, expected_type=type_hints["output_strength"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_strength": input_strength,
                "output_strength": output_strength,
                "type": type,
            }

        @builtins.property
        def input_strength(self) -> builtins.str:
            '''The strength of the input for the guardrail content filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailcontentfilterconfig.html#cfn-wisdom-aiguardrail-guardrailcontentfilterconfig-inputstrength
            '''
            result = self._values.get("input_strength")
            assert result is not None, "Required property 'input_strength' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def output_strength(self) -> builtins.str:
            '''The output strength of the guardrail content filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailcontentfilterconfig.html#cfn-wisdom-aiguardrail-guardrailcontentfilterconfig-outputstrength
            '''
            result = self._values.get("output_strength")
            assert result is not None, "Required property 'output_strength' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the guardrail content filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailcontentfilterconfig.html#cfn-wisdom-aiguardrail-guardrailcontentfilterconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GuardrailContentFilterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrail.GuardrailContextualGroundingFilterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"threshold": "threshold", "type": "type"},
    )
    class GuardrailContextualGroundingFilterConfigProperty:
        def __init__(self, *, threshold: jsii.Number, type: builtins.str) -> None:
            '''A configuration for grounding filter.

            :param threshold: The threshold for this filter. Default: - 0
            :param type: The type of this filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailcontextualgroundingfilterconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                guardrail_contextual_grounding_filter_config_property = wisdom.CfnAIGuardrail.GuardrailContextualGroundingFilterConfigProperty(
                    threshold=123,
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__57e4e4233989e39271f6f5b1254ba49184eaf97a79f1df28337cd59a6a5ce09f)
                check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "threshold": threshold,
                "type": type,
            }

        @builtins.property
        def threshold(self) -> jsii.Number:
            '''The threshold for this filter.

            :default: - 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailcontextualgroundingfilterconfig.html#cfn-wisdom-aiguardrail-guardrailcontextualgroundingfilterconfig-threshold
            '''
            result = self._values.get("threshold")
            assert result is not None, "Required property 'threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of this filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailcontextualgroundingfilterconfig.html#cfn-wisdom-aiguardrail-guardrailcontextualgroundingfilterconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GuardrailContextualGroundingFilterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrail.GuardrailManagedWordsConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type"},
    )
    class GuardrailManagedWordsConfigProperty:
        def __init__(self, *, type: builtins.str) -> None:
            '''A managed words config.

            :param type: The type of guardrail managed words.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailmanagedwordsconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                guardrail_managed_words_config_property = wisdom.CfnAIGuardrail.GuardrailManagedWordsConfigProperty(
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dfc19deb6dd371180a4bb8d9f0990f6132afb22d46b71ae1e32e4ffdbe4ef567)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of guardrail managed words.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailmanagedwordsconfig.html#cfn-wisdom-aiguardrail-guardrailmanagedwordsconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GuardrailManagedWordsConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrail.GuardrailPiiEntityConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action", "type": "type"},
    )
    class GuardrailPiiEntityConfigProperty:
        def __init__(self, *, action: builtins.str, type: builtins.str) -> None:
            '''PII entity configuration.

            :param action: The action of guardrail PII entity configuration.
            :param type: The currently supported PII entities.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailpiientityconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                guardrail_pii_entity_config_property = wisdom.CfnAIGuardrail.GuardrailPiiEntityConfigProperty(
                    action="action",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c764d4acc62cb140dda0e1c7dbd2f6738df34c8fb43ef4cf0d9a9941f03af4c1)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "type": type,
            }

        @builtins.property
        def action(self) -> builtins.str:
            '''The action of guardrail PII entity configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailpiientityconfig.html#cfn-wisdom-aiguardrail-guardrailpiientityconfig-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The currently supported PII entities.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailpiientityconfig.html#cfn-wisdom-aiguardrail-guardrailpiientityconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GuardrailPiiEntityConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrail.GuardrailRegexConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "name": "name",
            "pattern": "pattern",
            "description": "description",
        },
    )
    class GuardrailRegexConfigProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            name: builtins.str,
            pattern: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A regex configuration.

            :param action: The action of the guardrail regex configuration.
            :param name: A regex configuration.
            :param pattern: The regex pattern.
            :param description: The regex description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailregexconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                guardrail_regex_config_property = wisdom.CfnAIGuardrail.GuardrailRegexConfigProperty(
                    action="action",
                    name="name",
                    pattern="pattern",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5a28c8495c26410e3b614188ff183453c712c882484a101d2d68ce3d2a925385)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "name": name,
                "pattern": pattern,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def action(self) -> builtins.str:
            '''The action of the guardrail regex configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailregexconfig.html#cfn-wisdom-aiguardrail-guardrailregexconfig-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''A regex configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailregexconfig.html#cfn-wisdom-aiguardrail-guardrailregexconfig-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def pattern(self) -> builtins.str:
            '''The regex pattern.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailregexconfig.html#cfn-wisdom-aiguardrail-guardrailregexconfig-pattern
            '''
            result = self._values.get("pattern")
            assert result is not None, "Required property 'pattern' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The regex description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailregexconfig.html#cfn-wisdom-aiguardrail-guardrailregexconfig-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GuardrailRegexConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrail.GuardrailTopicConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "definition": "definition",
            "name": "name",
            "type": "type",
            "examples": "examples",
        },
    )
    class GuardrailTopicConfigProperty:
        def __init__(
            self,
            *,
            definition: builtins.str,
            name: builtins.str,
            type: builtins.str,
            examples: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Topic configuration in topic policy.

            :param definition: Definition of topic in topic policy.
            :param name: Name of topic in topic policy.
            :param type: Type of topic in a policy.
            :param examples: Text example in topic policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailtopicconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                guardrail_topic_config_property = wisdom.CfnAIGuardrail.GuardrailTopicConfigProperty(
                    definition="definition",
                    name="name",
                    type="type",
                
                    # the properties below are optional
                    examples=["examples"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__925705bff59beafe6b6eee70065213b10cb0a6047a45adbdaf25fa9a8b0ee5cf)
                check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument examples", value=examples, expected_type=type_hints["examples"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "definition": definition,
                "name": name,
                "type": type,
            }
            if examples is not None:
                self._values["examples"] = examples

        @builtins.property
        def definition(self) -> builtins.str:
            '''Definition of topic in topic policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailtopicconfig.html#cfn-wisdom-aiguardrail-guardrailtopicconfig-definition
            '''
            result = self._values.get("definition")
            assert result is not None, "Required property 'definition' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''Name of topic in topic policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailtopicconfig.html#cfn-wisdom-aiguardrail-guardrailtopicconfig-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''Type of topic in a policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailtopicconfig.html#cfn-wisdom-aiguardrail-guardrailtopicconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def examples(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Text example in topic policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailtopicconfig.html#cfn-wisdom-aiguardrail-guardrailtopicconfig-examples
            '''
            result = self._values.get("examples")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GuardrailTopicConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrail.GuardrailWordConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"text": "text"},
    )
    class GuardrailWordConfigProperty:
        def __init__(self, *, text: builtins.str) -> None:
            '''A custom word config.

            :param text: The custom word text.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailwordconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                guardrail_word_config_property = wisdom.CfnAIGuardrail.GuardrailWordConfigProperty(
                    text="text"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__606553234f4510e4e970f7df37efccc44b1516de671a981777f6102615e8243d)
                check_type(argname="argument text", value=text, expected_type=type_hints["text"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "text": text,
            }

        @builtins.property
        def text(self) -> builtins.str:
            '''The custom word text.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiguardrail-guardrailwordconfig.html#cfn-wisdom-aiguardrail-guardrailwordconfig-text
            '''
            result = self._values.get("text")
            assert result is not None, "Required property 'text' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GuardrailWordConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrailProps",
    jsii_struct_bases=[],
    name_mapping={
        "assistant_id": "assistantId",
        "blocked_input_messaging": "blockedInputMessaging",
        "blocked_outputs_messaging": "blockedOutputsMessaging",
        "content_policy_config": "contentPolicyConfig",
        "contextual_grounding_policy_config": "contextualGroundingPolicyConfig",
        "description": "description",
        "name": "name",
        "sensitive_information_policy_config": "sensitiveInformationPolicyConfig",
        "tags": "tags",
        "topic_policy_config": "topicPolicyConfig",
        "word_policy_config": "wordPolicyConfig",
    },
)
class CfnAIGuardrailProps:
    def __init__(
        self,
        *,
        assistant_id: builtins.str,
        blocked_input_messaging: builtins.str,
        blocked_outputs_messaging: builtins.str,
        content_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.AIGuardrailContentPolicyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        contextual_grounding_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.AIGuardrailContextualGroundingPolicyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        sensitive_information_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.AIGuardrailSensitiveInformationPolicyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        topic_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.AIGuardrailTopicPolicyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        word_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.AIGuardrailWordPolicyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAIGuardrail``.

        :param assistant_id: The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
        :param blocked_input_messaging: The message to return when the AI Guardrail blocks a prompt.
        :param blocked_outputs_messaging: The message to return when the AI Guardrail blocks a model response.
        :param content_policy_config: Contains details about how to handle harmful content.
        :param contextual_grounding_policy_config: The policy configuration details for the AI Guardrail's contextual grounding policy.
        :param description: A description of the AI Guardrail.
        :param name: The name of the AI Guardrail.
        :param sensitive_information_policy_config: Contains details about PII entities and regular expressions to configure for the AI Guardrail.
        :param tags: The tags used to organize, track, or control access for this resource.
        :param topic_policy_config: Contains details about topics that the AI Guardrail should identify and deny.
        :param word_policy_config: Contains details about the word policy to configured for the AI Guardrail.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrail.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_aIGuardrail_props = wisdom.CfnAIGuardrailProps(
                assistant_id="assistantId",
                blocked_input_messaging="blockedInputMessaging",
                blocked_outputs_messaging="blockedOutputsMessaging",
            
                # the properties below are optional
                content_policy_config=wisdom.CfnAIGuardrail.AIGuardrailContentPolicyConfigProperty(
                    filters_config=[wisdom.CfnAIGuardrail.GuardrailContentFilterConfigProperty(
                        input_strength="inputStrength",
                        output_strength="outputStrength",
                        type="type"
                    )]
                ),
                contextual_grounding_policy_config=wisdom.CfnAIGuardrail.AIGuardrailContextualGroundingPolicyConfigProperty(
                    filters_config=[wisdom.CfnAIGuardrail.GuardrailContextualGroundingFilterConfigProperty(
                        threshold=123,
                        type="type"
                    )]
                ),
                description="description",
                name="name",
                sensitive_information_policy_config=wisdom.CfnAIGuardrail.AIGuardrailSensitiveInformationPolicyConfigProperty(
                    pii_entities_config=[wisdom.CfnAIGuardrail.GuardrailPiiEntityConfigProperty(
                        action="action",
                        type="type"
                    )],
                    regexes_config=[wisdom.CfnAIGuardrail.GuardrailRegexConfigProperty(
                        action="action",
                        name="name",
                        pattern="pattern",
            
                        # the properties below are optional
                        description="description"
                    )]
                ),
                tags={
                    "tags_key": "tags"
                },
                topic_policy_config=wisdom.CfnAIGuardrail.AIGuardrailTopicPolicyConfigProperty(
                    topics_config=[wisdom.CfnAIGuardrail.GuardrailTopicConfigProperty(
                        definition="definition",
                        name="name",
                        type="type",
            
                        # the properties below are optional
                        examples=["examples"]
                    )]
                ),
                word_policy_config=wisdom.CfnAIGuardrail.AIGuardrailWordPolicyConfigProperty(
                    managed_word_lists_config=[wisdom.CfnAIGuardrail.GuardrailManagedWordsConfigProperty(
                        type="type"
                    )],
                    words_config=[wisdom.CfnAIGuardrail.GuardrailWordConfigProperty(
                        text="text"
                    )]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__272934bdd57f29fc5c93ba393c351f7b04e959a7a6be0e13591e187bd90df3aa)
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument blocked_input_messaging", value=blocked_input_messaging, expected_type=type_hints["blocked_input_messaging"])
            check_type(argname="argument blocked_outputs_messaging", value=blocked_outputs_messaging, expected_type=type_hints["blocked_outputs_messaging"])
            check_type(argname="argument content_policy_config", value=content_policy_config, expected_type=type_hints["content_policy_config"])
            check_type(argname="argument contextual_grounding_policy_config", value=contextual_grounding_policy_config, expected_type=type_hints["contextual_grounding_policy_config"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sensitive_information_policy_config", value=sensitive_information_policy_config, expected_type=type_hints["sensitive_information_policy_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument topic_policy_config", value=topic_policy_config, expected_type=type_hints["topic_policy_config"])
            check_type(argname="argument word_policy_config", value=word_policy_config, expected_type=type_hints["word_policy_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "assistant_id": assistant_id,
            "blocked_input_messaging": blocked_input_messaging,
            "blocked_outputs_messaging": blocked_outputs_messaging,
        }
        if content_policy_config is not None:
            self._values["content_policy_config"] = content_policy_config
        if contextual_grounding_policy_config is not None:
            self._values["contextual_grounding_policy_config"] = contextual_grounding_policy_config
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if sensitive_information_policy_config is not None:
            self._values["sensitive_information_policy_config"] = sensitive_information_policy_config
        if tags is not None:
            self._values["tags"] = tags
        if topic_policy_config is not None:
            self._values["topic_policy_config"] = topic_policy_config
        if word_policy_config is not None:
            self._values["word_policy_config"] = word_policy_config

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect assistant.

        Can be either the ID or the ARN. URLs cannot contain the ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrail.html#cfn-wisdom-aiguardrail-assistantid
        '''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def blocked_input_messaging(self) -> builtins.str:
        '''The message to return when the AI Guardrail blocks a prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrail.html#cfn-wisdom-aiguardrail-blockedinputmessaging
        '''
        result = self._values.get("blocked_input_messaging")
        assert result is not None, "Required property 'blocked_input_messaging' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def blocked_outputs_messaging(self) -> builtins.str:
        '''The message to return when the AI Guardrail blocks a model response.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrail.html#cfn-wisdom-aiguardrail-blockedoutputsmessaging
        '''
        result = self._values.get("blocked_outputs_messaging")
        assert result is not None, "Required property 'blocked_outputs_messaging' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_policy_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAIGuardrail.AIGuardrailContentPolicyConfigProperty]]:
        '''Contains details about how to handle harmful content.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrail.html#cfn-wisdom-aiguardrail-contentpolicyconfig
        '''
        result = self._values.get("content_policy_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAIGuardrail.AIGuardrailContentPolicyConfigProperty]], result)

    @builtins.property
    def contextual_grounding_policy_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAIGuardrail.AIGuardrailContextualGroundingPolicyConfigProperty]]:
        '''The policy configuration details for the AI Guardrail's contextual grounding policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrail.html#cfn-wisdom-aiguardrail-contextualgroundingpolicyconfig
        '''
        result = self._values.get("contextual_grounding_policy_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAIGuardrail.AIGuardrailContextualGroundingPolicyConfigProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the AI Guardrail.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrail.html#cfn-wisdom-aiguardrail-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the AI Guardrail.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrail.html#cfn-wisdom-aiguardrail-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sensitive_information_policy_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAIGuardrail.AIGuardrailSensitiveInformationPolicyConfigProperty]]:
        '''Contains details about PII entities and regular expressions to configure for the AI Guardrail.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrail.html#cfn-wisdom-aiguardrail-sensitiveinformationpolicyconfig
        '''
        result = self._values.get("sensitive_information_policy_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAIGuardrail.AIGuardrailSensitiveInformationPolicyConfigProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrail.html#cfn-wisdom-aiguardrail-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def topic_policy_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAIGuardrail.AIGuardrailTopicPolicyConfigProperty]]:
        '''Contains details about topics that the AI Guardrail should identify and deny.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrail.html#cfn-wisdom-aiguardrail-topicpolicyconfig
        '''
        result = self._values.get("topic_policy_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAIGuardrail.AIGuardrailTopicPolicyConfigProperty]], result)

    @builtins.property
    def word_policy_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAIGuardrail.AIGuardrailWordPolicyConfigProperty]]:
        '''Contains details about the word policy to configured for the AI Guardrail.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrail.html#cfn-wisdom-aiguardrail-wordpolicyconfig
        '''
        result = self._values.get("word_policy_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAIGuardrail.AIGuardrailWordPolicyConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAIGuardrailProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAIGuardrailVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrailVersion",
):
    '''Creates an Amazon Q in Connect AI Guardrail version.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrailversion.html
    :cloudformationResource: AWS::Wisdom::AIGuardrailVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_aIGuardrail_version = wisdom.CfnAIGuardrailVersion(self, "MyCfnAIGuardrailVersion",
            ai_guardrail_id="aiGuardrailId",
            assistant_id="assistantId",
        
            # the properties below are optional
            modified_time_seconds=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        ai_guardrail_id: builtins.str,
        assistant_id: builtins.str,
        modified_time_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param ai_guardrail_id: The ID of the AI guardrail version.
        :param assistant_id: The ID of the AI guardrail version assistant.
        :param modified_time_seconds: The modified time of the AI guardrail version in seconds.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a9a92a95cf92d95c08e9a7abc4202740081918bf2082c415b59e8a388ed1ceb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAIGuardrailVersionProps(
            ai_guardrail_id=ai_guardrail_id,
            assistant_id=assistant_id,
            modified_time_seconds=modified_time_seconds,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce87f6cc038ae50940e8317ea6eb15fb4755952543358f516cfb8178eb844887)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb4398a8c6a20907582fa6297d25cfd57e7cd74c3d99a7d32fa8f1476c4ba7f4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAiGuardrailArn")
    def attr_ai_guardrail_arn(self) -> builtins.str:
        '''The ARN of the AI guardrail version.

        :cloudformationAttribute: AIGuardrailArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiGuardrailArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAiGuardrailVersionId")
    def attr_ai_guardrail_version_id(self) -> builtins.str:
        '''The ID of the AI guardrail version.

        :cloudformationAttribute: AIGuardrailVersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiGuardrailVersionId"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''The ARN of the AI guardrail version assistant.

        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionNumber")
    def attr_version_number(self) -> _IResolvable_da3f097b:
        '''The version number for this AI Guardrail version.

        :cloudformationAttribute: VersionNumber
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrVersionNumber"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="aiGuardrailId")
    def ai_guardrail_id(self) -> builtins.str:
        '''The ID of the AI guardrail version.'''
        return typing.cast(builtins.str, jsii.get(self, "aiGuardrailId"))

    @ai_guardrail_id.setter
    def ai_guardrail_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a553f580b0f104a026581e9450d365d429441d11d53e610beb7a35a5229aedf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aiGuardrailId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assistantId")
    def assistant_id(self) -> builtins.str:
        '''The ID of the AI guardrail version assistant.'''
        return typing.cast(builtins.str, jsii.get(self, "assistantId"))

    @assistant_id.setter
    def assistant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad42f08834e2762e6f546d5167e6c7dccf9f639bbf36d9596aa7a154f6898e41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assistantId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="modifiedTimeSeconds")
    def modified_time_seconds(self) -> typing.Optional[jsii.Number]:
        '''The modified time of the AI guardrail version in seconds.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "modifiedTimeSeconds"))

    @modified_time_seconds.setter
    def modified_time_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94c07d3aa9bfd5fbb498b3a8c9f38b60219be42b9521625f0f8d680e6206d6ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modifiedTimeSeconds", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIGuardrailVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "ai_guardrail_id": "aiGuardrailId",
        "assistant_id": "assistantId",
        "modified_time_seconds": "modifiedTimeSeconds",
    },
)
class CfnAIGuardrailVersionProps:
    def __init__(
        self,
        *,
        ai_guardrail_id: builtins.str,
        assistant_id: builtins.str,
        modified_time_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnAIGuardrailVersion``.

        :param ai_guardrail_id: The ID of the AI guardrail version.
        :param assistant_id: The ID of the AI guardrail version assistant.
        :param modified_time_seconds: The modified time of the AI guardrail version in seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrailversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_aIGuardrail_version_props = wisdom.CfnAIGuardrailVersionProps(
                ai_guardrail_id="aiGuardrailId",
                assistant_id="assistantId",
            
                # the properties below are optional
                modified_time_seconds=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a99128fc6202c08bbbe787b73cc8f6fe79376afb6a408a1c3b9f1d86295794b)
            check_type(argname="argument ai_guardrail_id", value=ai_guardrail_id, expected_type=type_hints["ai_guardrail_id"])
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument modified_time_seconds", value=modified_time_seconds, expected_type=type_hints["modified_time_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ai_guardrail_id": ai_guardrail_id,
            "assistant_id": assistant_id,
        }
        if modified_time_seconds is not None:
            self._values["modified_time_seconds"] = modified_time_seconds

    @builtins.property
    def ai_guardrail_id(self) -> builtins.str:
        '''The ID of the AI guardrail version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrailversion.html#cfn-wisdom-aiguardrailversion-aiguardrailid
        '''
        result = self._values.get("ai_guardrail_id")
        assert result is not None, "Required property 'ai_guardrail_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The ID of the AI guardrail version assistant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrailversion.html#cfn-wisdom-aiguardrailversion-assistantid
        '''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def modified_time_seconds(self) -> typing.Optional[jsii.Number]:
        '''The modified time of the AI guardrail version in seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiguardrailversion.html#cfn-wisdom-aiguardrailversion-modifiedtimeseconds
        '''
        result = self._values.get("modified_time_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAIGuardrailVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnAIPrompt(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIPrompt",
):
    '''Creates an Amazon Q in Connect AI Prompt.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html
    :cloudformationResource: AWS::Wisdom::AIPrompt
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_aIPrompt = wisdom.CfnAIPrompt(self, "MyCfnAIPrompt",
            api_format="apiFormat",
            model_id="modelId",
            template_configuration=wisdom.CfnAIPrompt.AIPromptTemplateConfigurationProperty(
                text_full_ai_prompt_edit_template_configuration=wisdom.CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty(
                    text="text"
                )
            ),
            template_type="templateType",
            type="type",
        
            # the properties below are optional
            assistant_id="assistantId",
            description="description",
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
        api_format: builtins.str,
        model_id: builtins.str,
        template_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIPrompt.AIPromptTemplateConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        template_type: builtins.str,
        type: builtins.str,
        assistant_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_format: The API format used for this AI Prompt.
        :param model_id: The identifier of the model used for this AI Prompt. The following model Ids are supported:. - ``anthropic.claude-3-haiku--v1:0`` - ``apac.amazon.nova-lite-v1:0`` - ``apac.amazon.nova-micro-v1:0`` - ``apac.amazon.nova-pro-v1:0`` - ``apac.anthropic.claude-3-5-sonnet--v2:0`` - ``apac.anthropic.claude-3-haiku-20240307-v1:0`` - ``eu.amazon.nova-lite-v1:0`` - ``eu.amazon.nova-micro-v1:0`` - ``eu.amazon.nova-pro-v1:0`` - ``eu.anthropic.claude-3-7-sonnet-20250219-v1:0`` - ``eu.anthropic.claude-3-haiku-20240307-v1:0`` - ``us.amazon.nova-lite-v1:0`` - ``us.amazon.nova-micro-v1:0`` - ``us.amazon.nova-pro-v1:0`` - ``us.anthropic.claude-3-5-haiku-20241022-v1:0`` - ``us.anthropic.claude-3-7-sonnet-20250219-v1:0`` - ``us.anthropic.claude-3-haiku-20240307-v1:0``
        :param template_configuration: The configuration of the prompt template for this AI Prompt.
        :param template_type: The type of the prompt template for this AI Prompt.
        :param type: The type of this AI Prompt.
        :param assistant_id: The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
        :param description: The description of the AI Prompt.
        :param name: The name of the AI Prompt.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48a265f7ec519ced4028dd8e69d5a1fe8ef89d36b11d693c968f74c8be6bb9df)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAIPromptProps(
            api_format=api_format,
            model_id=model_id,
            template_configuration=template_configuration,
            template_type=template_type,
            type=type,
            assistant_id=assistant_id,
            description=description,
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
            type_hints = typing.get_type_hints(_typecheckingstub__7567e2bb6113fabf7ae624801bcdbbfa2507650c0fcedb4572ac328601553fcc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8c65608208361b5449f96e9e897202e481d956b960bbccf8366c60dac3e4bd70)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAiPromptArn")
    def attr_ai_prompt_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AI Prompt.

        :cloudformationAttribute: AIPromptArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiPromptArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAiPromptId")
    def attr_ai_prompt_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect AI prompt.

        :cloudformationAttribute: AIPromptId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiPromptId"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.

        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedTimeSeconds")
    def attr_modified_time_seconds(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: ModifiedTimeSeconds
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrModifiedTimeSeconds"))

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
    @jsii.member(jsii_name="apiFormat")
    def api_format(self) -> builtins.str:
        '''The API format used for this AI Prompt.'''
        return typing.cast(builtins.str, jsii.get(self, "apiFormat"))

    @api_format.setter
    def api_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6643cec138a765effc7d182e3db5b09b1ddb19205b800c1f517cbed5e73488b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiFormat", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="modelId")
    def model_id(self) -> builtins.str:
        '''The identifier of the model used for this AI Prompt.

        The following model Ids are supported:.
        '''
        return typing.cast(builtins.str, jsii.get(self, "modelId"))

    @model_id.setter
    def model_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be2ea2c4f381a43b0574cf9f6fdcace2ba70655e5f3ebd78fd5e8c4541b05982)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="templateConfiguration")
    def template_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAIPrompt.AIPromptTemplateConfigurationProperty"]:
        '''The configuration of the prompt template for this AI Prompt.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAIPrompt.AIPromptTemplateConfigurationProperty"], jsii.get(self, "templateConfiguration"))

    @template_configuration.setter
    def template_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAIPrompt.AIPromptTemplateConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5419aa0c5422844ff34f9fc9a194021532fa6ada449722bb2aa4b846530445ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="templateType")
    def template_type(self) -> builtins.str:
        '''The type of the prompt template for this AI Prompt.'''
        return typing.cast(builtins.str, jsii.get(self, "templateType"))

    @template_type.setter
    def template_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e4b3aeb8d77c711927acf1f94798cc7b4e483f8fc8bc95ae0b322f2c18a51f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of this AI Prompt.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3f45400801eabea6672075f9e78a389daf48244d79b0b5601339aad9840939b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assistantId")
    def assistant_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the Amazon Q in Connect assistant.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assistantId"))

    @assistant_id.setter
    def assistant_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5634dda4bc6094fc31dbde0ffceab32283f49a381e6e026ed12c76738e89fe5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assistantId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the AI Prompt.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aab971aeb8e18c48f506a9f2350fb427745d11ff1d792a38763843c7c52200b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the AI Prompt.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c8237463d9724c409122f49c9b69b5a1e0f429714ecc37326da2fb2d24ac916)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebc135e5b323c7d3a33dd614d94d6bb8425982f46dc4aafee23df90fac59a460)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIPrompt.AIPromptTemplateConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "text_full_ai_prompt_edit_template_configuration": "textFullAiPromptEditTemplateConfiguration",
        },
    )
    class AIPromptTemplateConfigurationProperty:
        def __init__(
            self,
            *,
            text_full_ai_prompt_edit_template_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A typed union that specifies the configuration for a prompt template based on its type.

            :param text_full_ai_prompt_edit_template_configuration: The configuration for a prompt template that supports full textual prompt configuration using a YAML prompt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiprompt-aiprompttemplateconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                a_iPrompt_template_configuration_property = wisdom.CfnAIPrompt.AIPromptTemplateConfigurationProperty(
                    text_full_ai_prompt_edit_template_configuration=wisdom.CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty(
                        text="text"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5c009da191a8948caab2f589b801cb2b5b6bd6f17d15c830bfcc3eac735974e)
                check_type(argname="argument text_full_ai_prompt_edit_template_configuration", value=text_full_ai_prompt_edit_template_configuration, expected_type=type_hints["text_full_ai_prompt_edit_template_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "text_full_ai_prompt_edit_template_configuration": text_full_ai_prompt_edit_template_configuration,
            }

        @builtins.property
        def text_full_ai_prompt_edit_template_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty"]:
            '''The configuration for a prompt template that supports full textual prompt configuration using a YAML prompt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiprompt-aiprompttemplateconfiguration.html#cfn-wisdom-aiprompt-aiprompttemplateconfiguration-textfullaipromptedittemplateconfiguration
            '''
            result = self._values.get("text_full_ai_prompt_edit_template_configuration")
            assert result is not None, "Required property 'text_full_ai_prompt_edit_template_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AIPromptTemplateConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"text": "text"},
    )
    class TextFullAIPromptEditTemplateConfigurationProperty:
        def __init__(self, *, text: builtins.str) -> None:
            '''The configuration for a prompt template that supports full textual prompt configuration using a YAML prompt.

            :param text: The YAML text for the AI Prompt template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiprompt-textfullaipromptedittemplateconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                text_full_aIPrompt_edit_template_configuration_property = wisdom.CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty(
                    text="text"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aab519c6a13d7d17f031944b9ddc67f7d24074f5ba48e4816f1ba2dfd7883ffc)
                check_type(argname="argument text", value=text, expected_type=type_hints["text"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "text": text,
            }

        @builtins.property
        def text(self) -> builtins.str:
            '''The YAML text for the AI Prompt template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-aiprompt-textfullaipromptedittemplateconfiguration.html#cfn-wisdom-aiprompt-textfullaipromptedittemplateconfiguration-text
            '''
            result = self._values.get("text")
            assert result is not None, "Required property 'text' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TextFullAIPromptEditTemplateConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIPromptProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_format": "apiFormat",
        "model_id": "modelId",
        "template_configuration": "templateConfiguration",
        "template_type": "templateType",
        "type": "type",
        "assistant_id": "assistantId",
        "description": "description",
        "name": "name",
        "tags": "tags",
    },
)
class CfnAIPromptProps:
    def __init__(
        self,
        *,
        api_format: builtins.str,
        model_id: builtins.str,
        template_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIPrompt.AIPromptTemplateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        template_type: builtins.str,
        type: builtins.str,
        assistant_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAIPrompt``.

        :param api_format: The API format used for this AI Prompt.
        :param model_id: The identifier of the model used for this AI Prompt. The following model Ids are supported:. - ``anthropic.claude-3-haiku--v1:0`` - ``apac.amazon.nova-lite-v1:0`` - ``apac.amazon.nova-micro-v1:0`` - ``apac.amazon.nova-pro-v1:0`` - ``apac.anthropic.claude-3-5-sonnet--v2:0`` - ``apac.anthropic.claude-3-haiku-20240307-v1:0`` - ``eu.amazon.nova-lite-v1:0`` - ``eu.amazon.nova-micro-v1:0`` - ``eu.amazon.nova-pro-v1:0`` - ``eu.anthropic.claude-3-7-sonnet-20250219-v1:0`` - ``eu.anthropic.claude-3-haiku-20240307-v1:0`` - ``us.amazon.nova-lite-v1:0`` - ``us.amazon.nova-micro-v1:0`` - ``us.amazon.nova-pro-v1:0`` - ``us.anthropic.claude-3-5-haiku-20241022-v1:0`` - ``us.anthropic.claude-3-7-sonnet-20250219-v1:0`` - ``us.anthropic.claude-3-haiku-20240307-v1:0``
        :param template_configuration: The configuration of the prompt template for this AI Prompt.
        :param template_type: The type of the prompt template for this AI Prompt.
        :param type: The type of this AI Prompt.
        :param assistant_id: The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
        :param description: The description of the AI Prompt.
        :param name: The name of the AI Prompt.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_aIPrompt_props = wisdom.CfnAIPromptProps(
                api_format="apiFormat",
                model_id="modelId",
                template_configuration=wisdom.CfnAIPrompt.AIPromptTemplateConfigurationProperty(
                    text_full_ai_prompt_edit_template_configuration=wisdom.CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty(
                        text="text"
                    )
                ),
                template_type="templateType",
                type="type",
            
                # the properties below are optional
                assistant_id="assistantId",
                description="description",
                name="name",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a55de2153828f44950073a28af3416601dc1f09105d3fa9d8f1ec243b3822d3)
            check_type(argname="argument api_format", value=api_format, expected_type=type_hints["api_format"])
            check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            check_type(argname="argument template_configuration", value=template_configuration, expected_type=type_hints["template_configuration"])
            check_type(argname="argument template_type", value=template_type, expected_type=type_hints["template_type"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_format": api_format,
            "model_id": model_id,
            "template_configuration": template_configuration,
            "template_type": template_type,
            "type": type,
        }
        if assistant_id is not None:
            self._values["assistant_id"] = assistant_id
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def api_format(self) -> builtins.str:
        '''The API format used for this AI Prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-apiformat
        '''
        result = self._values.get("api_format")
        assert result is not None, "Required property 'api_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model_id(self) -> builtins.str:
        '''The identifier of the model used for this AI Prompt. The following model Ids are supported:.

        - ``anthropic.claude-3-haiku--v1:0``
        - ``apac.amazon.nova-lite-v1:0``
        - ``apac.amazon.nova-micro-v1:0``
        - ``apac.amazon.nova-pro-v1:0``
        - ``apac.anthropic.claude-3-5-sonnet--v2:0``
        - ``apac.anthropic.claude-3-haiku-20240307-v1:0``
        - ``eu.amazon.nova-lite-v1:0``
        - ``eu.amazon.nova-micro-v1:0``
        - ``eu.amazon.nova-pro-v1:0``
        - ``eu.anthropic.claude-3-7-sonnet-20250219-v1:0``
        - ``eu.anthropic.claude-3-haiku-20240307-v1:0``
        - ``us.amazon.nova-lite-v1:0``
        - ``us.amazon.nova-micro-v1:0``
        - ``us.amazon.nova-pro-v1:0``
        - ``us.anthropic.claude-3-5-haiku-20241022-v1:0``
        - ``us.anthropic.claude-3-7-sonnet-20250219-v1:0``
        - ``us.anthropic.claude-3-haiku-20240307-v1:0``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-modelid
        '''
        result = self._values.get("model_id")
        assert result is not None, "Required property 'model_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAIPrompt.AIPromptTemplateConfigurationProperty]:
        '''The configuration of the prompt template for this AI Prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-templateconfiguration
        '''
        result = self._values.get("template_configuration")
        assert result is not None, "Required property 'template_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAIPrompt.AIPromptTemplateConfigurationProperty], result)

    @builtins.property
    def template_type(self) -> builtins.str:
        '''The type of the prompt template for this AI Prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-templatetype
        '''
        result = self._values.get("template_type")
        assert result is not None, "Required property 'template_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of this AI Prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the Amazon Q in Connect assistant.

        Can be either the ID or the ARN. URLs cannot contain the ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-assistantid
        '''
        result = self._values.get("assistant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the AI Prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the AI Prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiprompt.html#cfn-wisdom-aiprompt-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAIPromptProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAIPromptVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIPromptVersion",
):
    '''Creates an Amazon Q in Connect AI Prompt version.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aipromptversion.html
    :cloudformationResource: AWS::Wisdom::AIPromptVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_aIPrompt_version = wisdom.CfnAIPromptVersion(self, "MyCfnAIPromptVersion",
            ai_prompt_id="aiPromptId",
            assistant_id="assistantId",
        
            # the properties below are optional
            modified_time_seconds=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        ai_prompt_id: builtins.str,
        assistant_id: builtins.str,
        modified_time_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param ai_prompt_id: The identifier of the Amazon Q in Connect AI prompt.
        :param assistant_id: The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
        :param modified_time_seconds: The time the AI Prompt version was last modified in seconds.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__729db38c828e5e73ae0386aea45298b479e1a069777600fadadd338035a13e5d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAIPromptVersionProps(
            ai_prompt_id=ai_prompt_id,
            assistant_id=assistant_id,
            modified_time_seconds=modified_time_seconds,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb551060d0407b951291352d04af15e21651dd34a52774e39a2d2da6e4df3220)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b234db791908c37519c8ae3284494dc43affe3bad0ab4eadab6407ef7ccc7627)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAiPromptArn")
    def attr_ai_prompt_arn(self) -> builtins.str:
        '''The ARN of the AI prompt.

        :cloudformationAttribute: AIPromptArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiPromptArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAiPromptVersionId")
    def attr_ai_prompt_version_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AIPromptVersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAiPromptVersionId"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionNumber")
    def attr_version_number(self) -> _IResolvable_da3f097b:
        '''The version number for this AI Prompt version.

        :cloudformationAttribute: VersionNumber
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrVersionNumber"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="aiPromptId")
    def ai_prompt_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect AI prompt.'''
        return typing.cast(builtins.str, jsii.get(self, "aiPromptId"))

    @ai_prompt_id.setter
    def ai_prompt_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad29e2ee6fad75de44645890c2c623b9ccb35a02f6e75d7ed98fa3b7337272ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aiPromptId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="assistantId")
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect assistant.'''
        return typing.cast(builtins.str, jsii.get(self, "assistantId"))

    @assistant_id.setter
    def assistant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b6982f0f13d49bf234e47082e4a9783bc461e6dc18d68737a370a3682f93b48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assistantId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="modifiedTimeSeconds")
    def modified_time_seconds(self) -> typing.Optional[jsii.Number]:
        '''The time the AI Prompt version was last modified in seconds.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "modifiedTimeSeconds"))

    @modified_time_seconds.setter
    def modified_time_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1f64ffa51639af07e9712d95780a238db8bd368a440a159ead5f0364951dcd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modifiedTimeSeconds", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAIPromptVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "ai_prompt_id": "aiPromptId",
        "assistant_id": "assistantId",
        "modified_time_seconds": "modifiedTimeSeconds",
    },
)
class CfnAIPromptVersionProps:
    def __init__(
        self,
        *,
        ai_prompt_id: builtins.str,
        assistant_id: builtins.str,
        modified_time_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnAIPromptVersion``.

        :param ai_prompt_id: The identifier of the Amazon Q in Connect AI prompt.
        :param assistant_id: The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
        :param modified_time_seconds: The time the AI Prompt version was last modified in seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aipromptversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_aIPrompt_version_props = wisdom.CfnAIPromptVersionProps(
                ai_prompt_id="aiPromptId",
                assistant_id="assistantId",
            
                # the properties below are optional
                modified_time_seconds=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39068faf047cdd2f1dce0d86adaff6f71058bba08c161da563b36647959f2add)
            check_type(argname="argument ai_prompt_id", value=ai_prompt_id, expected_type=type_hints["ai_prompt_id"])
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument modified_time_seconds", value=modified_time_seconds, expected_type=type_hints["modified_time_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ai_prompt_id": ai_prompt_id,
            "assistant_id": assistant_id,
        }
        if modified_time_seconds is not None:
            self._values["modified_time_seconds"] = modified_time_seconds

    @builtins.property
    def ai_prompt_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect AI prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aipromptversion.html#cfn-wisdom-aipromptversion-aipromptid
        '''
        result = self._values.get("ai_prompt_id")
        assert result is not None, "Required property 'ai_prompt_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Amazon Q in Connect assistant.

        Can be either the ID or the ARN. URLs cannot contain the ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aipromptversion.html#cfn-wisdom-aipromptversion-assistantid
        '''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def modified_time_seconds(self) -> typing.Optional[jsii.Number]:
        '''The time the AI Prompt version was last modified in seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aipromptversion.html#cfn-wisdom-aipromptversion-modifiedtimeseconds
        '''
        result = self._values.get("modified_time_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAIPromptVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnAssistant(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistant",
):
    '''Specifies an Amazon Connect Wisdom assistant.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html
    :cloudformationResource: AWS::Wisdom::Assistant
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_assistant = wisdom.CfnAssistant(self, "MyCfnAssistant",
            name="name",
            type="type",
        
            # the properties below are optional
            description="description",
            server_side_encryption_configuration=wisdom.CfnAssistant.ServerSideEncryptionConfigurationProperty(
                kms_key_id="kmsKeyId"
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
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssistant.ServerSideEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the assistant.
        :param type: The type of assistant.
        :param description: The description of the assistant.
        :param server_side_encryption_configuration: The configuration information for the customer managed key used for encryption. The customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow ``kms:Decrypt`` , ``kms:GenerateDataKey*`` , and ``kms:DescribeKey`` permissions to the ``connect.amazonaws.com`` service principal. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ .
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8078b7e28a17a68ab6f3d362e7de3af6b6867207690b2b344e35797cd6569746)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssistantProps(
            name=name,
            type=type,
            description=description,
            server_side_encryption_configuration=server_side_encryption_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67a0860b53a1867e3124a155db57aa1ab8bbb2d50c48a1553f8766101996d0b8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a17095196842a083c7a71c961443f89f6d1dd766154e06248d10cdee66b0113)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the assistant.

        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantId")
    def attr_assistant_id(self) -> builtins.str:
        '''The ID of the Wisdom assistant.

        :cloudformationAttribute: AssistantId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantId"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the assistant.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ded25c09bd072cbcb02cdfdf40580d154663664980378f96c5210edc137dd8c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of assistant.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c131b16ef6a21690f65d4e643bc0f04ea3e1fa9afd2bbf0e89a9bd4b96032657)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the assistant.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17115c2ceb35036c54e25dfa13fd4465303e5a759aae943761c84163427b74ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssistant.ServerSideEncryptionConfigurationProperty"]]:
        '''The configuration information for the customer managed key used for encryption.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssistant.ServerSideEncryptionConfigurationProperty"]], jsii.get(self, "serverSideEncryptionConfiguration"))

    @server_side_encryption_configuration.setter
    def server_side_encryption_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssistant.ServerSideEncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb8470e364668ea9060baa4a3306507e0ded02773f75cc435d33474d30577d1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideEncryptionConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a82c89946835215b7304a7033eacc23c202ee6ae8e17e73d0ba34f1dbaf1416)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistant.ServerSideEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_id": "kmsKeyId"},
    )
    class ServerSideEncryptionConfigurationProperty:
        def __init__(self, *, kms_key_id: typing.Optional[builtins.str] = None) -> None:
            '''The configuration information for the customer managed key used for encryption.

            :param kms_key_id: The customer managed key used for encryption. The customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow ``kms:Decrypt`` , ``kms:GenerateDataKey*`` , and ``kms:DescribeKey`` permissions to the ``connect.amazonaws.com`` service principal. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistant-serversideencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                server_side_encryption_configuration_property = wisdom.CfnAssistant.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa78e1cc313485ba353b8f1dc8b01c69bcdd1c5bcecd204b9778596de1e4a07d)
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The customer managed key used for encryption.

            The customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow ``kms:Decrypt`` , ``kms:GenerateDataKey*`` , and ``kms:DescribeKey`` permissions to the ``connect.amazonaws.com`` service principal. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistant-serversideencryptionconfiguration.html#cfn-wisdom-assistant-serversideencryptionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerSideEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnAssistantAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistantAssociation",
):
    '''Specifies an association between an Amazon Connect Wisdom assistant and another resource.

    Currently, the only supported association is with a knowledge base. An assistant can have only a single association.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html
    :cloudformationResource: AWS::Wisdom::AssistantAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_assistant_association = wisdom.CfnAssistantAssociation(self, "MyCfnAssistantAssociation",
            assistant_id="assistantId",
            association=wisdom.CfnAssistantAssociation.AssociationDataProperty(
                knowledge_base_id="knowledgeBaseId"
            ),
            association_type="associationType",
        
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
        assistant_id: builtins.str,
        association: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssistantAssociation.AssociationDataProperty", typing.Dict[builtins.str, typing.Any]]],
        association_type: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param assistant_id: The identifier of the Wisdom assistant.
        :param association: The identifier of the associated resource.
        :param association_type: The type of association.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17f6f8491bb7be7dab63c57bf64b65f643c4fece381b02f49002f796c7a8f0f9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssistantAssociationProps(
            assistant_id=assistant_id,
            association=association,
            association_type=association_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a96af34ce4ed10cd5d626bf5df7799b86ca3023d4f6b302c0cdb51a0bdd1274)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e84fe37792368fc9821204b49ed0d6e13642f35bcdc7bb2676de0ee949767075)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Wisdom assistant.

        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantAssociationArn")
    def attr_assistant_association_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the assistant association.

        :cloudformationAttribute: AssistantAssociationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantAssociationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantAssociationId")
    def attr_assistant_association_id(self) -> builtins.str:
        '''The ID of the association.

        :cloudformationAttribute: AssistantAssociationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantAssociationId"))

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
    @jsii.member(jsii_name="assistantId")
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Wisdom assistant.'''
        return typing.cast(builtins.str, jsii.get(self, "assistantId"))

    @assistant_id.setter
    def assistant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c72c215a467df1527e01f95d41dc85287728a80fa94729b3ff14b2b1312fb30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assistantId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="association")
    def association(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAssistantAssociation.AssociationDataProperty"]:
        '''The identifier of the associated resource.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAssistantAssociation.AssociationDataProperty"], jsii.get(self, "association"))

    @association.setter
    def association(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAssistantAssociation.AssociationDataProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e46eeb6364ccf0b8f92618927437f56df6248417cb401c056b83fe5692feb0f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "association", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="associationType")
    def association_type(self) -> builtins.str:
        '''The type of association.'''
        return typing.cast(builtins.str, jsii.get(self, "associationType"))

    @association_type.setter
    def association_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48fcb269f8dde8b147d1a0d7681e40817cb35b599f00a24aff263a84df4cea90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associationType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea3d3cb4fe1048c256fc8719ac3d18f47cb21ef29730dd9d1f53a9304ccd4030)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistantAssociation.AssociationDataProperty",
        jsii_struct_bases=[],
        name_mapping={"knowledge_base_id": "knowledgeBaseId"},
    )
    class AssociationDataProperty:
        def __init__(self, *, knowledge_base_id: builtins.str) -> None:
            '''A union type that currently has a single argument, which is the knowledge base ID.

            :param knowledge_base_id: The identifier of the knowledge base.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistantassociation-associationdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                association_data_property = wisdom.CfnAssistantAssociation.AssociationDataProperty(
                    knowledge_base_id="knowledgeBaseId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f6ecf0cfb2eb97624a8ec4ab51e16f75cfa1a5397890274252a2621ff5ad378d)
                check_type(argname="argument knowledge_base_id", value=knowledge_base_id, expected_type=type_hints["knowledge_base_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "knowledge_base_id": knowledge_base_id,
            }

        @builtins.property
        def knowledge_base_id(self) -> builtins.str:
            '''The identifier of the knowledge base.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistantassociation-associationdata.html#cfn-wisdom-assistantassociation-associationdata-knowledgebaseid
            '''
            result = self._values.get("knowledge_base_id")
            assert result is not None, "Required property 'knowledge_base_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssociationDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistantAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "assistant_id": "assistantId",
        "association": "association",
        "association_type": "associationType",
        "tags": "tags",
    },
)
class CfnAssistantAssociationProps:
    def __init__(
        self,
        *,
        assistant_id: builtins.str,
        association: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistantAssociation.AssociationDataProperty, typing.Dict[builtins.str, typing.Any]]],
        association_type: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAssistantAssociation``.

        :param assistant_id: The identifier of the Wisdom assistant.
        :param association: The identifier of the associated resource.
        :param association_type: The type of association.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_assistant_association_props = wisdom.CfnAssistantAssociationProps(
                assistant_id="assistantId",
                association=wisdom.CfnAssistantAssociation.AssociationDataProperty(
                    knowledge_base_id="knowledgeBaseId"
                ),
                association_type="associationType",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__419e70156a249f4fa2bea77a71d532fe9a351e3d150b5939dc8455b174375514)
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument association", value=association, expected_type=type_hints["association"])
            check_type(argname="argument association_type", value=association_type, expected_type=type_hints["association_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "assistant_id": assistant_id,
            "association": association,
            "association_type": association_type,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Wisdom assistant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-assistantid
        '''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def association(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAssistantAssociation.AssociationDataProperty]:
        '''The identifier of the associated resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-association
        '''
        result = self._values.get("association")
        assert result is not None, "Required property 'association' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAssistantAssociation.AssociationDataProperty], result)

    @builtins.property
    def association_type(self) -> builtins.str:
        '''The type of association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-associationtype
        '''
        result = self._values.get("association_type")
        assert result is not None, "Required property 'association_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssistantAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistantProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "description": "description",
        "server_side_encryption_configuration": "serverSideEncryptionConfiguration",
        "tags": "tags",
    },
)
class CfnAssistantProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistant.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAssistant``.

        :param name: The name of the assistant.
        :param type: The type of assistant.
        :param description: The description of the assistant.
        :param server_side_encryption_configuration: The configuration information for the customer managed key used for encryption. The customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow ``kms:Decrypt`` , ``kms:GenerateDataKey*`` , and ``kms:DescribeKey`` permissions to the ``connect.amazonaws.com`` service principal. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ .
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_assistant_props = wisdom.CfnAssistantProps(
                name="name",
                type="type",
            
                # the properties below are optional
                description="description",
                server_side_encryption_configuration=wisdom.CfnAssistant.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2f6978729a0bccb7cc077df26ee5d379812791b9fe7ec0622251ed958562e07)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument server_side_encryption_configuration", value=server_side_encryption_configuration, expected_type=type_hints["server_side_encryption_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if server_side_encryption_configuration is not None:
            self._values["server_side_encryption_configuration"] = server_side_encryption_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the assistant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of assistant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the assistant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAssistant.ServerSideEncryptionConfigurationProperty]]:
        '''The configuration information for the customer managed key used for encryption.

        The customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow ``kms:Decrypt`` , ``kms:GenerateDataKey*`` , and ``kms:DescribeKey`` permissions to the ``connect.amazonaws.com`` service principal. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-serversideencryptionconfiguration
        '''
        result = self._values.get("server_side_encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAssistant.ServerSideEncryptionConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssistantProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnKnowledgeBase(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase",
):
    '''Specifies a knowledge base.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html
    :cloudformationResource: AWS::Wisdom::KnowledgeBase
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_knowledge_base = wisdom.CfnKnowledgeBase(self, "MyCfnKnowledgeBase",
            knowledge_base_type="knowledgeBaseType",
            name="name",
        
            # the properties below are optional
            description="description",
            rendering_configuration=wisdom.CfnKnowledgeBase.RenderingConfigurationProperty(
                template_uri="templateUri"
            ),
            server_side_encryption_configuration=wisdom.CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty(
                kms_key_id="kmsKeyId"
            ),
            source_configuration=wisdom.CfnKnowledgeBase.SourceConfigurationProperty(
                app_integrations=wisdom.CfnKnowledgeBase.AppIntegrationsConfigurationProperty(
                    app_integration_arn="appIntegrationArn",
        
                    # the properties below are optional
                    object_fields=["objectFields"]
                ),
                managed_source_configuration=wisdom.CfnKnowledgeBase.ManagedSourceConfigurationProperty(
                    web_crawler_configuration=wisdom.CfnKnowledgeBase.WebCrawlerConfigurationProperty(
                        url_configuration=wisdom.CfnKnowledgeBase.UrlConfigurationProperty(
                            seed_urls=[wisdom.CfnKnowledgeBase.SeedUrlProperty(
                                url="url"
                            )]
                        ),
        
                        # the properties below are optional
                        crawler_limits=wisdom.CfnKnowledgeBase.CrawlerLimitsProperty(
                            rate_limit=123
                        ),
                        exclusion_filters=["exclusionFilters"],
                        inclusion_filters=["inclusionFilters"],
                        scope="scope"
                    )
                )
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vector_ingestion_configuration=wisdom.CfnKnowledgeBase.VectorIngestionConfigurationProperty(
                chunking_configuration=wisdom.CfnKnowledgeBase.ChunkingConfigurationProperty(
                    chunking_strategy="chunkingStrategy",
        
                    # the properties below are optional
                    fixed_size_chunking_configuration=wisdom.CfnKnowledgeBase.FixedSizeChunkingConfigurationProperty(
                        max_tokens=123,
                        overlap_percentage=123
                    ),
                    hierarchical_chunking_configuration=wisdom.CfnKnowledgeBase.HierarchicalChunkingConfigurationProperty(
                        level_configurations=[wisdom.CfnKnowledgeBase.HierarchicalChunkingLevelConfigurationProperty(
                            max_tokens=123
                        )],
                        overlap_tokens=123
                    ),
                    semantic_chunking_configuration=wisdom.CfnKnowledgeBase.SemanticChunkingConfigurationProperty(
                        breakpoint_percentile_threshold=123,
                        buffer_size=123,
                        max_tokens=123
                    )
                ),
                parsing_configuration=wisdom.CfnKnowledgeBase.ParsingConfigurationProperty(
                    parsing_strategy="parsingStrategy",
        
                    # the properties below are optional
                    bedrock_foundation_model_configuration=wisdom.CfnKnowledgeBase.BedrockFoundationModelConfigurationProperty(
                        model_arn="modelArn",
        
                        # the properties below are optional
                        parsing_prompt=wisdom.CfnKnowledgeBase.ParsingPromptProperty(
                            parsing_prompt_text="parsingPromptText"
                        )
                    )
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        knowledge_base_type: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        rendering_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.RenderingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.SourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vector_ingestion_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.VectorIngestionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param knowledge_base_type: The type of knowledge base. Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically.
        :param name: The name of the knowledge base.
        :param description: The description.
        :param rendering_configuration: Information about how to render the content.
        :param server_side_encryption_configuration: This customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .
        :param source_configuration: The source of the knowledge base content. Only set this argument for EXTERNAL or Managed knowledge bases.
        :param tags: The tags used to organize, track, or control access for this resource.
        :param vector_ingestion_configuration: Contains details about how to ingest the documents in a data source.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99512a2eb8a3e47802b889aac668fc94bdc0534ee683313dac712b20006ea6ed)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnKnowledgeBaseProps(
            knowledge_base_type=knowledge_base_type,
            name=name,
            description=description,
            rendering_configuration=rendering_configuration,
            server_side_encryption_configuration=server_side_encryption_configuration,
            source_configuration=source_configuration,
            tags=tags,
            vector_ingestion_configuration=vector_ingestion_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e12fde615d3c7854b4e97326fea29e89d837485efe274039378606ee08a4be76)
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
            type_hints = typing.get_type_hints(_typecheckingstub__198b767f5d7e7dce9b330a5c5c43441fed236182c59b06b0be2da034b14ce256)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrKnowledgeBaseArn")
    def attr_knowledge_base_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the knowledge base.

        :cloudformationAttribute: KnowledgeBaseArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKnowledgeBaseArn"))

    @builtins.property
    @jsii.member(jsii_name="attrKnowledgeBaseId")
    def attr_knowledge_base_id(self) -> builtins.str:
        '''The ID of the knowledge base.

        :cloudformationAttribute: KnowledgeBaseId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKnowledgeBaseId"))

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
    @jsii.member(jsii_name="knowledgeBaseType")
    def knowledge_base_type(self) -> builtins.str:
        '''The type of knowledge base.'''
        return typing.cast(builtins.str, jsii.get(self, "knowledgeBaseType"))

    @knowledge_base_type.setter
    def knowledge_base_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93bc0b75027c2aaed7afea32df7bbe9ea25daf054d032e869d4b65d3c73427e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "knowledgeBaseType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the knowledge base.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06da4251d33a92a96fd91655710caf394cf4fa6fe728e86b20be47c80f50c450)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8e87e39918fdfb349935e6c5b5b76307ecd838c21583fab217f7d88ca3ea67c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="renderingConfiguration")
    def rendering_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.RenderingConfigurationProperty"]]:
        '''Information about how to render the content.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.RenderingConfigurationProperty"]], jsii.get(self, "renderingConfiguration"))

    @rendering_configuration.setter
    def rendering_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.RenderingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dbfe6a279891a574d7128da28db41ca74ec109e76fb61b5b9db27b1ee815fba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renderingConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty"]]:
        '''This customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty"]], jsii.get(self, "serverSideEncryptionConfiguration"))

    @server_side_encryption_configuration.setter
    def server_side_encryption_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__221e4b62cf601d8c0e6300aceb9f7a7bfe38ac19093345137be6abb3f22756d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideEncryptionConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.SourceConfigurationProperty"]]:
        '''The source of the knowledge base content.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.SourceConfigurationProperty"]], jsii.get(self, "sourceConfiguration"))

    @source_configuration.setter
    def source_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.SourceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ab7292e64b294c529dec00a33cfb2da96ff80581b3e1376c67027a944849691)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b654968450798e9434ae157e80b0efdde965d3d9cf517c41c4fcdcfa66e910f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vectorIngestionConfiguration")
    def vector_ingestion_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.VectorIngestionConfigurationProperty"]]:
        '''Contains details about how to ingest the documents in a data source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.VectorIngestionConfigurationProperty"]], jsii.get(self, "vectorIngestionConfiguration"))

    @vector_ingestion_configuration.setter
    def vector_ingestion_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.VectorIngestionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__841ed99c710bd0f2748a34efe9978e0d2cadafde4697b94a4cfbf0d401c23ee2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vectorIngestionConfiguration", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.AppIntegrationsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_integration_arn": "appIntegrationArn",
            "object_fields": "objectFields",
        },
    )
    class AppIntegrationsConfigurationProperty:
        def __init__(
            self,
            *,
            app_integration_arn: builtins.str,
            object_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Configuration information for Amazon AppIntegrations to automatically ingest content.

            :param app_integration_arn: The Amazon Resource Name (ARN) of the AppIntegrations DataIntegration to use for ingesting content. - For `Salesforce <https://docs.aws.amazon.com/https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , and ``IsDeleted`` as source fields. - For `ServiceNow <https://docs.aws.amazon.com/https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , and ``active`` as source fields. - For `Zendesk <https://docs.aws.amazon.com/https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if ``objectFields`` is not provided, including at least ``id`` , ``title`` , ``updated_at`` , and ``draft`` as source fields. - For `SharePoint <https://docs.aws.amazon.com/https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/sharepoint-net-server-csom-jsom-and-rest-api-index>`_ , your AppIntegrations DataIntegration must have a FileConfiguration, including only file extensions that are among ``docx`` , ``pdf`` , ``html`` , ``htm`` , and ``txt`` . - For `Amazon S3 <https://docs.aws.amazon.com/s3/>`_ , the ObjectConfiguration and FileConfiguration of your AppIntegrations DataIntegration must be null. The ``SourceURI`` of your DataIntegration must use the following format: ``s3://your_s3_bucket_name`` . .. epigraph:: The bucket policy of the corresponding S3 bucket must allow the AWS principal ``app-integrations.amazonaws.com`` to perform ``s3:ListBucket`` , ``s3:GetObject`` , and ``s3:GetBucketLocation`` against the bucket.
            :param object_fields: The fields from the source that are made available to your agents in Amazon Q in Connect. Optional if ObjectConfiguration is included in the provided DataIntegration. - For `Salesforce <https://docs.aws.amazon.com/https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm>`_ , you must include at least ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , and ``IsDeleted`` . - For `ServiceNow <https://docs.aws.amazon.com/https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api>`_ , you must include at least ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , and ``active`` . - For `Zendesk <https://docs.aws.amazon.com/https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/>`_ , you must include at least ``id`` , ``title`` , ``updated_at`` , and ``draft`` . Make sure to include additional fields. These fields are indexed and used to source recommendations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                app_integrations_configuration_property = wisdom.CfnKnowledgeBase.AppIntegrationsConfigurationProperty(
                    app_integration_arn="appIntegrationArn",
                
                    # the properties below are optional
                    object_fields=["objectFields"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fb5af4edc537ecd6b5dab081c90708156852ccef10f7a6228ff445f6dc0e509c)
                check_type(argname="argument app_integration_arn", value=app_integration_arn, expected_type=type_hints["app_integration_arn"])
                check_type(argname="argument object_fields", value=object_fields, expected_type=type_hints["object_fields"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "app_integration_arn": app_integration_arn,
            }
            if object_fields is not None:
                self._values["object_fields"] = object_fields

        @builtins.property
        def app_integration_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AppIntegrations DataIntegration to use for ingesting content.

            - For `Salesforce <https://docs.aws.amazon.com/https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , and ``IsDeleted`` as source fields.
            - For `ServiceNow <https://docs.aws.amazon.com/https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , and ``active`` as source fields.
            - For `Zendesk <https://docs.aws.amazon.com/https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if ``objectFields`` is not provided, including at least ``id`` , ``title`` , ``updated_at`` , and ``draft`` as source fields.
            - For `SharePoint <https://docs.aws.amazon.com/https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/sharepoint-net-server-csom-jsom-and-rest-api-index>`_ , your AppIntegrations DataIntegration must have a FileConfiguration, including only file extensions that are among ``docx`` , ``pdf`` , ``html`` , ``htm`` , and ``txt`` .
            - For `Amazon S3 <https://docs.aws.amazon.com/s3/>`_ , the ObjectConfiguration and FileConfiguration of your AppIntegrations DataIntegration must be null. The ``SourceURI`` of your DataIntegration must use the following format: ``s3://your_s3_bucket_name`` .

            .. epigraph::

               The bucket policy of the corresponding S3 bucket must allow the AWS principal ``app-integrations.amazonaws.com`` to perform ``s3:ListBucket`` , ``s3:GetObject`` , and ``s3:GetBucketLocation`` against the bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html#cfn-wisdom-knowledgebase-appintegrationsconfiguration-appintegrationarn
            '''
            result = self._values.get("app_integration_arn")
            assert result is not None, "Required property 'app_integration_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_fields(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The fields from the source that are made available to your agents in Amazon Q in Connect.

            Optional if ObjectConfiguration is included in the provided DataIntegration.

            - For `Salesforce <https://docs.aws.amazon.com/https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm>`_ , you must include at least ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , and ``IsDeleted`` .
            - For `ServiceNow <https://docs.aws.amazon.com/https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api>`_ , you must include at least ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , and ``active`` .
            - For `Zendesk <https://docs.aws.amazon.com/https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/>`_ , you must include at least ``id`` , ``title`` , ``updated_at`` , and ``draft`` .

            Make sure to include additional fields. These fields are indexed and used to source recommendations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html#cfn-wisdom-knowledgebase-appintegrationsconfiguration-objectfields
            '''
            result = self._values.get("object_fields")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AppIntegrationsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.BedrockFoundationModelConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"model_arn": "modelArn", "parsing_prompt": "parsingPrompt"},
    )
    class BedrockFoundationModelConfigurationProperty:
        def __init__(
            self,
            *,
            model_arn: builtins.str,
            parsing_prompt: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.ParsingPromptProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration of the Bedrock foundation model.

            :param model_arn: The model ARN of the Bedrock foundation model.
            :param parsing_prompt: The parsing prompt of the Bedrock foundation model configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-bedrockfoundationmodelconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                bedrock_foundation_model_configuration_property = wisdom.CfnKnowledgeBase.BedrockFoundationModelConfigurationProperty(
                    model_arn="modelArn",
                
                    # the properties below are optional
                    parsing_prompt=wisdom.CfnKnowledgeBase.ParsingPromptProperty(
                        parsing_prompt_text="parsingPromptText"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3357d1d4f3808129b0987d8a651abe6fce2d6e99ac83ee764b51bcb69af90bfa)
                check_type(argname="argument model_arn", value=model_arn, expected_type=type_hints["model_arn"])
                check_type(argname="argument parsing_prompt", value=parsing_prompt, expected_type=type_hints["parsing_prompt"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "model_arn": model_arn,
            }
            if parsing_prompt is not None:
                self._values["parsing_prompt"] = parsing_prompt

        @builtins.property
        def model_arn(self) -> builtins.str:
            '''The model ARN of the Bedrock foundation model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-bedrockfoundationmodelconfiguration.html#cfn-wisdom-knowledgebase-bedrockfoundationmodelconfiguration-modelarn
            '''
            result = self._values.get("model_arn")
            assert result is not None, "Required property 'model_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parsing_prompt(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ParsingPromptProperty"]]:
            '''The parsing prompt of the Bedrock foundation model configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-bedrockfoundationmodelconfiguration.html#cfn-wisdom-knowledgebase-bedrockfoundationmodelconfiguration-parsingprompt
            '''
            result = self._values.get("parsing_prompt")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ParsingPromptProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BedrockFoundationModelConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.ChunkingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "chunking_strategy": "chunkingStrategy",
            "fixed_size_chunking_configuration": "fixedSizeChunkingConfiguration",
            "hierarchical_chunking_configuration": "hierarchicalChunkingConfiguration",
            "semantic_chunking_configuration": "semanticChunkingConfiguration",
        },
    )
    class ChunkingConfigurationProperty:
        def __init__(
            self,
            *,
            chunking_strategy: builtins.str,
            fixed_size_chunking_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.FixedSizeChunkingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            hierarchical_chunking_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.HierarchicalChunkingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            semantic_chunking_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.SemanticChunkingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Details about how to chunk the documents in the data source.

            A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.

            :param chunking_strategy: Knowledge base can split your source data into chunks. A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried. You have the following options for chunking your data. If you opt for ``NONE`` , then you may want to pre-process your files by splitting them up such that each file corresponds to a chunk.
            :param fixed_size_chunking_configuration: Configurations for when you choose fixed-size chunking. If you set the ``chunkingStrategy`` as ``NONE`` , exclude this field.
            :param hierarchical_chunking_configuration: Settings for hierarchical document chunking for a data source. Hierarchical chunking splits documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.
            :param semantic_chunking_configuration: Settings for semantic document chunking for a data source. Semantic chunking splits a document into smaller documents based on groups of similar content derived from the text with natural language processing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-chunkingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                chunking_configuration_property = wisdom.CfnKnowledgeBase.ChunkingConfigurationProperty(
                    chunking_strategy="chunkingStrategy",
                
                    # the properties below are optional
                    fixed_size_chunking_configuration=wisdom.CfnKnowledgeBase.FixedSizeChunkingConfigurationProperty(
                        max_tokens=123,
                        overlap_percentage=123
                    ),
                    hierarchical_chunking_configuration=wisdom.CfnKnowledgeBase.HierarchicalChunkingConfigurationProperty(
                        level_configurations=[wisdom.CfnKnowledgeBase.HierarchicalChunkingLevelConfigurationProperty(
                            max_tokens=123
                        )],
                        overlap_tokens=123
                    ),
                    semantic_chunking_configuration=wisdom.CfnKnowledgeBase.SemanticChunkingConfigurationProperty(
                        breakpoint_percentile_threshold=123,
                        buffer_size=123,
                        max_tokens=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d95119d30e49d5bd11aadde5636c2dcecbffe3cd3f2559414b0a1fc6d4a6af3)
                check_type(argname="argument chunking_strategy", value=chunking_strategy, expected_type=type_hints["chunking_strategy"])
                check_type(argname="argument fixed_size_chunking_configuration", value=fixed_size_chunking_configuration, expected_type=type_hints["fixed_size_chunking_configuration"])
                check_type(argname="argument hierarchical_chunking_configuration", value=hierarchical_chunking_configuration, expected_type=type_hints["hierarchical_chunking_configuration"])
                check_type(argname="argument semantic_chunking_configuration", value=semantic_chunking_configuration, expected_type=type_hints["semantic_chunking_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "chunking_strategy": chunking_strategy,
            }
            if fixed_size_chunking_configuration is not None:
                self._values["fixed_size_chunking_configuration"] = fixed_size_chunking_configuration
            if hierarchical_chunking_configuration is not None:
                self._values["hierarchical_chunking_configuration"] = hierarchical_chunking_configuration
            if semantic_chunking_configuration is not None:
                self._values["semantic_chunking_configuration"] = semantic_chunking_configuration

        @builtins.property
        def chunking_strategy(self) -> builtins.str:
            '''Knowledge base can split your source data into chunks.

            A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried. You have the following options for chunking your data. If you opt for ``NONE`` , then you may want to pre-process your files by splitting them up such that each file corresponds to a chunk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-chunkingconfiguration.html#cfn-wisdom-knowledgebase-chunkingconfiguration-chunkingstrategy
            '''
            result = self._values.get("chunking_strategy")
            assert result is not None, "Required property 'chunking_strategy' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def fixed_size_chunking_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.FixedSizeChunkingConfigurationProperty"]]:
            '''Configurations for when you choose fixed-size chunking.

            If you set the ``chunkingStrategy`` as ``NONE`` , exclude this field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-chunkingconfiguration.html#cfn-wisdom-knowledgebase-chunkingconfiguration-fixedsizechunkingconfiguration
            '''
            result = self._values.get("fixed_size_chunking_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.FixedSizeChunkingConfigurationProperty"]], result)

        @builtins.property
        def hierarchical_chunking_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.HierarchicalChunkingConfigurationProperty"]]:
            '''Settings for hierarchical document chunking for a data source.

            Hierarchical chunking splits documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-chunkingconfiguration.html#cfn-wisdom-knowledgebase-chunkingconfiguration-hierarchicalchunkingconfiguration
            '''
            result = self._values.get("hierarchical_chunking_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.HierarchicalChunkingConfigurationProperty"]], result)

        @builtins.property
        def semantic_chunking_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.SemanticChunkingConfigurationProperty"]]:
            '''Settings for semantic document chunking for a data source.

            Semantic chunking splits a document into smaller documents based on groups of similar content derived from the text with natural language processing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-chunkingconfiguration.html#cfn-wisdom-knowledgebase-chunkingconfiguration-semanticchunkingconfiguration
            '''
            result = self._values.get("semantic_chunking_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.SemanticChunkingConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ChunkingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.CrawlerLimitsProperty",
        jsii_struct_bases=[],
        name_mapping={"rate_limit": "rateLimit"},
    )
    class CrawlerLimitsProperty:
        def __init__(self, *, rate_limit: typing.Optional[jsii.Number] = None) -> None:
            '''The limits of the crawler.

            :param rate_limit: The limit rate at which the crawler is configured.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-crawlerlimits.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                crawler_limits_property = wisdom.CfnKnowledgeBase.CrawlerLimitsProperty(
                    rate_limit=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1e3c61c31746c21216c5087b3b9c0ff8b6a3720c51cb749cc9b8ac907b6269dc)
                check_type(argname="argument rate_limit", value=rate_limit, expected_type=type_hints["rate_limit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if rate_limit is not None:
                self._values["rate_limit"] = rate_limit

        @builtins.property
        def rate_limit(self) -> typing.Optional[jsii.Number]:
            '''The limit rate at which the crawler is configured.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-crawlerlimits.html#cfn-wisdom-knowledgebase-crawlerlimits-ratelimit
            '''
            result = self._values.get("rate_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CrawlerLimitsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.FixedSizeChunkingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_tokens": "maxTokens",
            "overlap_percentage": "overlapPercentage",
        },
    )
    class FixedSizeChunkingConfigurationProperty:
        def __init__(
            self,
            *,
            max_tokens: jsii.Number,
            overlap_percentage: jsii.Number,
        ) -> None:
            '''Configurations for when you choose fixed-size chunking.

            If you set the ``chunkingStrategy`` as ``NONE`` , exclude this field.

            :param max_tokens: The maximum number of tokens to include in a chunk.
            :param overlap_percentage: The percentage of overlap between adjacent chunks of a data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-fixedsizechunkingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                fixed_size_chunking_configuration_property = wisdom.CfnKnowledgeBase.FixedSizeChunkingConfigurationProperty(
                    max_tokens=123,
                    overlap_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e64775237b79e7f336be4b1d76a0ab710432dde63badb3a5752cee09b6d6fcae)
                check_type(argname="argument max_tokens", value=max_tokens, expected_type=type_hints["max_tokens"])
                check_type(argname="argument overlap_percentage", value=overlap_percentage, expected_type=type_hints["overlap_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_tokens": max_tokens,
                "overlap_percentage": overlap_percentage,
            }

        @builtins.property
        def max_tokens(self) -> jsii.Number:
            '''The maximum number of tokens to include in a chunk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-fixedsizechunkingconfiguration.html#cfn-wisdom-knowledgebase-fixedsizechunkingconfiguration-maxtokens
            '''
            result = self._values.get("max_tokens")
            assert result is not None, "Required property 'max_tokens' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def overlap_percentage(self) -> jsii.Number:
            '''The percentage of overlap between adjacent chunks of a data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-fixedsizechunkingconfiguration.html#cfn-wisdom-knowledgebase-fixedsizechunkingconfiguration-overlappercentage
            '''
            result = self._values.get("overlap_percentage")
            assert result is not None, "Required property 'overlap_percentage' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FixedSizeChunkingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.HierarchicalChunkingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "level_configurations": "levelConfigurations",
            "overlap_tokens": "overlapTokens",
        },
    )
    class HierarchicalChunkingConfigurationProperty:
        def __init__(
            self,
            *,
            level_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.HierarchicalChunkingLevelConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
            overlap_tokens: jsii.Number,
        ) -> None:
            '''Settings for hierarchical document chunking for a data source.

            Hierarchical chunking splits documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.

            :param level_configurations: Token settings for each layer.
            :param overlap_tokens: The number of tokens to repeat across chunks in the same layer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-hierarchicalchunkingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                hierarchical_chunking_configuration_property = wisdom.CfnKnowledgeBase.HierarchicalChunkingConfigurationProperty(
                    level_configurations=[wisdom.CfnKnowledgeBase.HierarchicalChunkingLevelConfigurationProperty(
                        max_tokens=123
                    )],
                    overlap_tokens=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e2e75b2aebff3c68af11b908941d1e187a79a951b58f0a33b152f1ab00053e49)
                check_type(argname="argument level_configurations", value=level_configurations, expected_type=type_hints["level_configurations"])
                check_type(argname="argument overlap_tokens", value=overlap_tokens, expected_type=type_hints["overlap_tokens"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "level_configurations": level_configurations,
                "overlap_tokens": overlap_tokens,
            }

        @builtins.property
        def level_configurations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.HierarchicalChunkingLevelConfigurationProperty"]]]:
            '''Token settings for each layer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-hierarchicalchunkingconfiguration.html#cfn-wisdom-knowledgebase-hierarchicalchunkingconfiguration-levelconfigurations
            '''
            result = self._values.get("level_configurations")
            assert result is not None, "Required property 'level_configurations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.HierarchicalChunkingLevelConfigurationProperty"]]], result)

        @builtins.property
        def overlap_tokens(self) -> jsii.Number:
            '''The number of tokens to repeat across chunks in the same layer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-hierarchicalchunkingconfiguration.html#cfn-wisdom-knowledgebase-hierarchicalchunkingconfiguration-overlaptokens
            '''
            result = self._values.get("overlap_tokens")
            assert result is not None, "Required property 'overlap_tokens' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HierarchicalChunkingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.HierarchicalChunkingLevelConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"max_tokens": "maxTokens"},
    )
    class HierarchicalChunkingLevelConfigurationProperty:
        def __init__(self, *, max_tokens: jsii.Number) -> None:
            '''Token settings for each layer.

            :param max_tokens: The maximum number of tokens that a chunk can contain in this layer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-hierarchicalchunkinglevelconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                hierarchical_chunking_level_configuration_property = wisdom.CfnKnowledgeBase.HierarchicalChunkingLevelConfigurationProperty(
                    max_tokens=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b80446f3a787de6c7b48fad975fa7ee10b8ee51af79a599756b923e9991e203f)
                check_type(argname="argument max_tokens", value=max_tokens, expected_type=type_hints["max_tokens"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_tokens": max_tokens,
            }

        @builtins.property
        def max_tokens(self) -> jsii.Number:
            '''The maximum number of tokens that a chunk can contain in this layer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-hierarchicalchunkinglevelconfiguration.html#cfn-wisdom-knowledgebase-hierarchicalchunkinglevelconfiguration-maxtokens
            '''
            result = self._values.get("max_tokens")
            assert result is not None, "Required property 'max_tokens' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HierarchicalChunkingLevelConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.ManagedSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"web_crawler_configuration": "webCrawlerConfiguration"},
    )
    class ManagedSourceConfigurationProperty:
        def __init__(
            self,
            *,
            web_crawler_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.WebCrawlerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Source configuration for managed resources.

            :param web_crawler_configuration: Configuration data for web crawler data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-managedsourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                managed_source_configuration_property = wisdom.CfnKnowledgeBase.ManagedSourceConfigurationProperty(
                    web_crawler_configuration=wisdom.CfnKnowledgeBase.WebCrawlerConfigurationProperty(
                        url_configuration=wisdom.CfnKnowledgeBase.UrlConfigurationProperty(
                            seed_urls=[wisdom.CfnKnowledgeBase.SeedUrlProperty(
                                url="url"
                            )]
                        ),
                
                        # the properties below are optional
                        crawler_limits=wisdom.CfnKnowledgeBase.CrawlerLimitsProperty(
                            rate_limit=123
                        ),
                        exclusion_filters=["exclusionFilters"],
                        inclusion_filters=["inclusionFilters"],
                        scope="scope"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__01b279dc3cda96328b8095cb5a3f31cb31404d26a7e228390580d93bf073de89)
                check_type(argname="argument web_crawler_configuration", value=web_crawler_configuration, expected_type=type_hints["web_crawler_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "web_crawler_configuration": web_crawler_configuration,
            }

        @builtins.property
        def web_crawler_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.WebCrawlerConfigurationProperty"]:
            '''Configuration data for web crawler data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-managedsourceconfiguration.html#cfn-wisdom-knowledgebase-managedsourceconfiguration-webcrawlerconfiguration
            '''
            result = self._values.get("web_crawler_configuration")
            assert result is not None, "Required property 'web_crawler_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.WebCrawlerConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManagedSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.ParsingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parsing_strategy": "parsingStrategy",
            "bedrock_foundation_model_configuration": "bedrockFoundationModelConfiguration",
        },
    )
    class ParsingConfigurationProperty:
        def __init__(
            self,
            *,
            parsing_strategy: builtins.str,
            bedrock_foundation_model_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.BedrockFoundationModelConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Settings for parsing document contents.

            By default, the service converts the contents of each document into text before splitting it into chunks. To improve processing of PDF files with tables and images, you can configure the data source to convert the pages of text into images and use a model to describe the contents of each page.

            :param parsing_strategy: The parsing strategy for the data source.
            :param bedrock_foundation_model_configuration: Settings for a foundation model used to parse documents for a data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-parsingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                parsing_configuration_property = wisdom.CfnKnowledgeBase.ParsingConfigurationProperty(
                    parsing_strategy="parsingStrategy",
                
                    # the properties below are optional
                    bedrock_foundation_model_configuration=wisdom.CfnKnowledgeBase.BedrockFoundationModelConfigurationProperty(
                        model_arn="modelArn",
                
                        # the properties below are optional
                        parsing_prompt=wisdom.CfnKnowledgeBase.ParsingPromptProperty(
                            parsing_prompt_text="parsingPromptText"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fc6bf4b7f99a7762951f3f88a8d67827d0e4117b574284c21f89ea4ed59edb2f)
                check_type(argname="argument parsing_strategy", value=parsing_strategy, expected_type=type_hints["parsing_strategy"])
                check_type(argname="argument bedrock_foundation_model_configuration", value=bedrock_foundation_model_configuration, expected_type=type_hints["bedrock_foundation_model_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parsing_strategy": parsing_strategy,
            }
            if bedrock_foundation_model_configuration is not None:
                self._values["bedrock_foundation_model_configuration"] = bedrock_foundation_model_configuration

        @builtins.property
        def parsing_strategy(self) -> builtins.str:
            '''The parsing strategy for the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-parsingconfiguration.html#cfn-wisdom-knowledgebase-parsingconfiguration-parsingstrategy
            '''
            result = self._values.get("parsing_strategy")
            assert result is not None, "Required property 'parsing_strategy' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bedrock_foundation_model_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.BedrockFoundationModelConfigurationProperty"]]:
            '''Settings for a foundation model used to parse documents for a data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-parsingconfiguration.html#cfn-wisdom-knowledgebase-parsingconfiguration-bedrockfoundationmodelconfiguration
            '''
            result = self._values.get("bedrock_foundation_model_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.BedrockFoundationModelConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParsingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.ParsingPromptProperty",
        jsii_struct_bases=[],
        name_mapping={"parsing_prompt_text": "parsingPromptText"},
    )
    class ParsingPromptProperty:
        def __init__(self, *, parsing_prompt_text: builtins.str) -> None:
            '''Instructions for interpreting the contents of a document.

            :param parsing_prompt_text: Instructions for interpreting the contents of a document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-parsingprompt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                parsing_prompt_property = wisdom.CfnKnowledgeBase.ParsingPromptProperty(
                    parsing_prompt_text="parsingPromptText"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__05d68dd54deb469c741ebfe8562286929c13c3a79aeac89ec4266aac6399b98e)
                check_type(argname="argument parsing_prompt_text", value=parsing_prompt_text, expected_type=type_hints["parsing_prompt_text"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parsing_prompt_text": parsing_prompt_text,
            }

        @builtins.property
        def parsing_prompt_text(self) -> builtins.str:
            '''Instructions for interpreting the contents of a document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-parsingprompt.html#cfn-wisdom-knowledgebase-parsingprompt-parsingprompttext
            '''
            result = self._values.get("parsing_prompt_text")
            assert result is not None, "Required property 'parsing_prompt_text' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParsingPromptProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.RenderingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"template_uri": "templateUri"},
    )
    class RenderingConfigurationProperty:
        def __init__(
            self,
            *,
            template_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about how to render the content.

            :param template_uri: A URI template containing exactly one variable in ``${variableName}`` format. This can only be set for ``EXTERNAL`` knowledge bases. For Salesforce, ServiceNow, and Zendesk, the variable must be one of the following: - Salesforce: ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , or ``IsDeleted`` - ServiceNow: ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , or ``active`` - Zendesk: ``id`` , ``title`` , ``updated_at`` , or ``draft`` The variable is replaced with the actual value for a piece of content when calling `GetContent <https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetContent.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-renderingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                rendering_configuration_property = wisdom.CfnKnowledgeBase.RenderingConfigurationProperty(
                    template_uri="templateUri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc0b3350c030b63153dd14a7ab6b7c686549027289e97b41678c46c5c9bce0d1)
                check_type(argname="argument template_uri", value=template_uri, expected_type=type_hints["template_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if template_uri is not None:
                self._values["template_uri"] = template_uri

        @builtins.property
        def template_uri(self) -> typing.Optional[builtins.str]:
            '''A URI template containing exactly one variable in ``${variableName}`` format.

            This can only be set for ``EXTERNAL`` knowledge bases. For Salesforce, ServiceNow, and Zendesk, the variable must be one of the following:

            - Salesforce: ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , or ``IsDeleted``
            - ServiceNow: ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , or ``active``
            - Zendesk: ``id`` , ``title`` , ``updated_at`` , or ``draft``

            The variable is replaced with the actual value for a piece of content when calling `GetContent <https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetContent.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-renderingconfiguration.html#cfn-wisdom-knowledgebase-renderingconfiguration-templateuri
            '''
            result = self._values.get("template_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RenderingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.SeedUrlProperty",
        jsii_struct_bases=[],
        name_mapping={"url": "url"},
    )
    class SeedUrlProperty:
        def __init__(self, *, url: typing.Optional[builtins.str] = None) -> None:
            '''A URL for crawling.

            :param url: URL for crawling.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-seedurl.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                seed_url_property = wisdom.CfnKnowledgeBase.SeedUrlProperty(
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8f5d22aa2f115decf996bdbc44327658efeadecefcf31ed94de1f632c99c4226)
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''URL for crawling.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-seedurl.html#cfn-wisdom-knowledgebase-seedurl-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SeedUrlProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.SemanticChunkingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "breakpoint_percentile_threshold": "breakpointPercentileThreshold",
            "buffer_size": "bufferSize",
            "max_tokens": "maxTokens",
        },
    )
    class SemanticChunkingConfigurationProperty:
        def __init__(
            self,
            *,
            breakpoint_percentile_threshold: jsii.Number,
            buffer_size: jsii.Number,
            max_tokens: jsii.Number,
        ) -> None:
            '''Settings for semantic document chunking for a data source.

            Semantic chunking splits a document into smaller documents based on groups of similar content derived from the text with natural language processing.

            :param breakpoint_percentile_threshold: The dissimilarity threshold for splitting chunks.
            :param buffer_size: The buffer size.
            :param max_tokens: The maximum number of tokens that a chunk can contain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-semanticchunkingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                semantic_chunking_configuration_property = wisdom.CfnKnowledgeBase.SemanticChunkingConfigurationProperty(
                    breakpoint_percentile_threshold=123,
                    buffer_size=123,
                    max_tokens=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__37473100b67c3634da11f7c1327c6358310e63403f4bba0df82c4eabeeae71df)
                check_type(argname="argument breakpoint_percentile_threshold", value=breakpoint_percentile_threshold, expected_type=type_hints["breakpoint_percentile_threshold"])
                check_type(argname="argument buffer_size", value=buffer_size, expected_type=type_hints["buffer_size"])
                check_type(argname="argument max_tokens", value=max_tokens, expected_type=type_hints["max_tokens"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "breakpoint_percentile_threshold": breakpoint_percentile_threshold,
                "buffer_size": buffer_size,
                "max_tokens": max_tokens,
            }

        @builtins.property
        def breakpoint_percentile_threshold(self) -> jsii.Number:
            '''The dissimilarity threshold for splitting chunks.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-semanticchunkingconfiguration.html#cfn-wisdom-knowledgebase-semanticchunkingconfiguration-breakpointpercentilethreshold
            '''
            result = self._values.get("breakpoint_percentile_threshold")
            assert result is not None, "Required property 'breakpoint_percentile_threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def buffer_size(self) -> jsii.Number:
            '''The buffer size.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-semanticchunkingconfiguration.html#cfn-wisdom-knowledgebase-semanticchunkingconfiguration-buffersize
            '''
            result = self._values.get("buffer_size")
            assert result is not None, "Required property 'buffer_size' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max_tokens(self) -> jsii.Number:
            '''The maximum number of tokens that a chunk can contain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-semanticchunkingconfiguration.html#cfn-wisdom-knowledgebase-semanticchunkingconfiguration-maxtokens
            '''
            result = self._values.get("max_tokens")
            assert result is not None, "Required property 'max_tokens' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SemanticChunkingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_id": "kmsKeyId"},
    )
    class ServerSideEncryptionConfigurationProperty:
        def __init__(self, *, kms_key_id: typing.Optional[builtins.str] = None) -> None:
            '''The configuration information for the customer managed key used for encryption.

            :param kms_key_id: The customer managed key used for encryption. This customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                server_side_encryption_configuration_property = wisdom.CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0cd7e6721b8c282e7e8effcea12ef5d59096c2d9eb9611a2269ac2deff0e697)
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The customer managed key used for encryption.

            This customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom.

            For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration.html#cfn-wisdom-knowledgebase-serversideencryptionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerSideEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.SourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_integrations": "appIntegrations",
            "managed_source_configuration": "managedSourceConfiguration",
        },
    )
    class SourceConfigurationProperty:
        def __init__(
            self,
            *,
            app_integrations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.AppIntegrationsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            managed_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.ManagedSourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration information about the external data source.

            :param app_integrations: Configuration information for Amazon AppIntegrations to automatically ingest content.
            :param managed_source_configuration: Source configuration for managed resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-sourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                source_configuration_property = wisdom.CfnKnowledgeBase.SourceConfigurationProperty(
                    app_integrations=wisdom.CfnKnowledgeBase.AppIntegrationsConfigurationProperty(
                        app_integration_arn="appIntegrationArn",
                
                        # the properties below are optional
                        object_fields=["objectFields"]
                    ),
                    managed_source_configuration=wisdom.CfnKnowledgeBase.ManagedSourceConfigurationProperty(
                        web_crawler_configuration=wisdom.CfnKnowledgeBase.WebCrawlerConfigurationProperty(
                            url_configuration=wisdom.CfnKnowledgeBase.UrlConfigurationProperty(
                                seed_urls=[wisdom.CfnKnowledgeBase.SeedUrlProperty(
                                    url="url"
                                )]
                            ),
                
                            # the properties below are optional
                            crawler_limits=wisdom.CfnKnowledgeBase.CrawlerLimitsProperty(
                                rate_limit=123
                            ),
                            exclusion_filters=["exclusionFilters"],
                            inclusion_filters=["inclusionFilters"],
                            scope="scope"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__169c34939e73e3c8ce81d921898915b159d4e29ad0c3757e50950775728d0aa0)
                check_type(argname="argument app_integrations", value=app_integrations, expected_type=type_hints["app_integrations"])
                check_type(argname="argument managed_source_configuration", value=managed_source_configuration, expected_type=type_hints["managed_source_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if app_integrations is not None:
                self._values["app_integrations"] = app_integrations
            if managed_source_configuration is not None:
                self._values["managed_source_configuration"] = managed_source_configuration

        @builtins.property
        def app_integrations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.AppIntegrationsConfigurationProperty"]]:
            '''Configuration information for Amazon AppIntegrations to automatically ingest content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-sourceconfiguration.html#cfn-wisdom-knowledgebase-sourceconfiguration-appintegrations
            '''
            result = self._values.get("app_integrations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.AppIntegrationsConfigurationProperty"]], result)

        @builtins.property
        def managed_source_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ManagedSourceConfigurationProperty"]]:
            '''Source configuration for managed resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-sourceconfiguration.html#cfn-wisdom-knowledgebase-sourceconfiguration-managedsourceconfiguration
            '''
            result = self._values.get("managed_source_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ManagedSourceConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.UrlConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"seed_urls": "seedUrls"},
    )
    class UrlConfigurationProperty:
        def __init__(
            self,
            *,
            seed_urls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.SeedUrlProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The configuration of the URL/URLs for the web content that you want to crawl.

            You should be authorized to crawl the URLs.

            :param seed_urls: List of URLs for crawling.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-urlconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                url_configuration_property = wisdom.CfnKnowledgeBase.UrlConfigurationProperty(
                    seed_urls=[wisdom.CfnKnowledgeBase.SeedUrlProperty(
                        url="url"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__71e0a652750aa86f6181cd7e7b6bae1e590e2b69e5632dac0497da6c702900f9)
                check_type(argname="argument seed_urls", value=seed_urls, expected_type=type_hints["seed_urls"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if seed_urls is not None:
                self._values["seed_urls"] = seed_urls

        @builtins.property
        def seed_urls(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.SeedUrlProperty"]]]]:
            '''List of URLs for crawling.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-urlconfiguration.html#cfn-wisdom-knowledgebase-urlconfiguration-seedurls
            '''
            result = self._values.get("seed_urls")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.SeedUrlProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UrlConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.VectorIngestionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "chunking_configuration": "chunkingConfiguration",
            "parsing_configuration": "parsingConfiguration",
        },
    )
    class VectorIngestionConfigurationProperty:
        def __init__(
            self,
            *,
            chunking_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.ChunkingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            parsing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.ParsingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains details about how to ingest the documents in a data source.

            :param chunking_configuration: Details about how to chunk the documents in the data source. A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.
            :param parsing_configuration: A custom parser for data source documents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-vectoringestionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                vector_ingestion_configuration_property = wisdom.CfnKnowledgeBase.VectorIngestionConfigurationProperty(
                    chunking_configuration=wisdom.CfnKnowledgeBase.ChunkingConfigurationProperty(
                        chunking_strategy="chunkingStrategy",
                
                        # the properties below are optional
                        fixed_size_chunking_configuration=wisdom.CfnKnowledgeBase.FixedSizeChunkingConfigurationProperty(
                            max_tokens=123,
                            overlap_percentage=123
                        ),
                        hierarchical_chunking_configuration=wisdom.CfnKnowledgeBase.HierarchicalChunkingConfigurationProperty(
                            level_configurations=[wisdom.CfnKnowledgeBase.HierarchicalChunkingLevelConfigurationProperty(
                                max_tokens=123
                            )],
                            overlap_tokens=123
                        ),
                        semantic_chunking_configuration=wisdom.CfnKnowledgeBase.SemanticChunkingConfigurationProperty(
                            breakpoint_percentile_threshold=123,
                            buffer_size=123,
                            max_tokens=123
                        )
                    ),
                    parsing_configuration=wisdom.CfnKnowledgeBase.ParsingConfigurationProperty(
                        parsing_strategy="parsingStrategy",
                
                        # the properties below are optional
                        bedrock_foundation_model_configuration=wisdom.CfnKnowledgeBase.BedrockFoundationModelConfigurationProperty(
                            model_arn="modelArn",
                
                            # the properties below are optional
                            parsing_prompt=wisdom.CfnKnowledgeBase.ParsingPromptProperty(
                                parsing_prompt_text="parsingPromptText"
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d8cf77ffdab289f4029f153e2fd852680c5cf76c8d875df505957acb18dd433b)
                check_type(argname="argument chunking_configuration", value=chunking_configuration, expected_type=type_hints["chunking_configuration"])
                check_type(argname="argument parsing_configuration", value=parsing_configuration, expected_type=type_hints["parsing_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if chunking_configuration is not None:
                self._values["chunking_configuration"] = chunking_configuration
            if parsing_configuration is not None:
                self._values["parsing_configuration"] = parsing_configuration

        @builtins.property
        def chunking_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ChunkingConfigurationProperty"]]:
            '''Details about how to chunk the documents in the data source.

            A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-vectoringestionconfiguration.html#cfn-wisdom-knowledgebase-vectoringestionconfiguration-chunkingconfiguration
            '''
            result = self._values.get("chunking_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ChunkingConfigurationProperty"]], result)

        @builtins.property
        def parsing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ParsingConfigurationProperty"]]:
            '''A custom parser for data source documents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-vectoringestionconfiguration.html#cfn-wisdom-knowledgebase-vectoringestionconfiguration-parsingconfiguration
            '''
            result = self._values.get("parsing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ParsingConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VectorIngestionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.WebCrawlerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "url_configuration": "urlConfiguration",
            "crawler_limits": "crawlerLimits",
            "exclusion_filters": "exclusionFilters",
            "inclusion_filters": "inclusionFilters",
            "scope": "scope",
        },
    )
    class WebCrawlerConfigurationProperty:
        def __init__(
            self,
            *,
            url_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.UrlConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            crawler_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.CrawlerLimitsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            exclusion_filters: typing.Optional[typing.Sequence[builtins.str]] = None,
            inclusion_filters: typing.Optional[typing.Sequence[builtins.str]] = None,
            scope: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration details for the web data source.

            :param url_configuration: The configuration of the URL/URLs for the web content that you want to crawl. You should be authorized to crawl the URLs.
            :param crawler_limits: The configuration of crawl limits for the web URLs.
            :param exclusion_filters: A list of one or more exclusion regular expression patterns to exclude certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.
            :param inclusion_filters: A list of one or more inclusion regular expression patterns to include certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.
            :param scope: The scope of what is crawled for your URLs. You can choose to crawl only web pages that belong to the same host or primary domain. For example, only web pages that contain the seed URL ``https://docs.aws.amazon.com/bedrock/latest/userguide/`` and no other domains. You can choose to include sub domains in addition to the host or primary domain. For example, web pages that contain ``aws.amazon.com`` can also include sub domain ``docs.aws.amazon.com`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-webcrawlerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                web_crawler_configuration_property = wisdom.CfnKnowledgeBase.WebCrawlerConfigurationProperty(
                    url_configuration=wisdom.CfnKnowledgeBase.UrlConfigurationProperty(
                        seed_urls=[wisdom.CfnKnowledgeBase.SeedUrlProperty(
                            url="url"
                        )]
                    ),
                
                    # the properties below are optional
                    crawler_limits=wisdom.CfnKnowledgeBase.CrawlerLimitsProperty(
                        rate_limit=123
                    ),
                    exclusion_filters=["exclusionFilters"],
                    inclusion_filters=["inclusionFilters"],
                    scope="scope"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b62d94eb7bc7c732098a29bd2a5de83daa71f6616ea1433becc1240c16c3e6a)
                check_type(argname="argument url_configuration", value=url_configuration, expected_type=type_hints["url_configuration"])
                check_type(argname="argument crawler_limits", value=crawler_limits, expected_type=type_hints["crawler_limits"])
                check_type(argname="argument exclusion_filters", value=exclusion_filters, expected_type=type_hints["exclusion_filters"])
                check_type(argname="argument inclusion_filters", value=inclusion_filters, expected_type=type_hints["inclusion_filters"])
                check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "url_configuration": url_configuration,
            }
            if crawler_limits is not None:
                self._values["crawler_limits"] = crawler_limits
            if exclusion_filters is not None:
                self._values["exclusion_filters"] = exclusion_filters
            if inclusion_filters is not None:
                self._values["inclusion_filters"] = inclusion_filters
            if scope is not None:
                self._values["scope"] = scope

        @builtins.property
        def url_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.UrlConfigurationProperty"]:
            '''The configuration of the URL/URLs for the web content that you want to crawl.

            You should be authorized to crawl the URLs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-webcrawlerconfiguration.html#cfn-wisdom-knowledgebase-webcrawlerconfiguration-urlconfiguration
            '''
            result = self._values.get("url_configuration")
            assert result is not None, "Required property 'url_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.UrlConfigurationProperty"], result)

        @builtins.property
        def crawler_limits(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.CrawlerLimitsProperty"]]:
            '''The configuration of crawl limits for the web URLs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-webcrawlerconfiguration.html#cfn-wisdom-knowledgebase-webcrawlerconfiguration-crawlerlimits
            '''
            result = self._values.get("crawler_limits")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.CrawlerLimitsProperty"]], result)

        @builtins.property
        def exclusion_filters(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of one or more exclusion regular expression patterns to exclude certain URLs.

            If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-webcrawlerconfiguration.html#cfn-wisdom-knowledgebase-webcrawlerconfiguration-exclusionfilters
            '''
            result = self._values.get("exclusion_filters")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def inclusion_filters(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of one or more inclusion regular expression patterns to include certain URLs.

            If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isn’t crawled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-webcrawlerconfiguration.html#cfn-wisdom-knowledgebase-webcrawlerconfiguration-inclusionfilters
            '''
            result = self._values.get("inclusion_filters")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def scope(self) -> typing.Optional[builtins.str]:
            '''The scope of what is crawled for your URLs.

            You can choose to crawl only web pages that belong to the same host or primary domain. For example, only web pages that contain the seed URL ``https://docs.aws.amazon.com/bedrock/latest/userguide/`` and no other domains. You can choose to include sub domains in addition to the host or primary domain. For example, web pages that contain ``aws.amazon.com`` can also include sub domain ``docs.aws.amazon.com`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-webcrawlerconfiguration.html#cfn-wisdom-knowledgebase-webcrawlerconfiguration-scope
            '''
            result = self._values.get("scope")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WebCrawlerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "knowledge_base_type": "knowledgeBaseType",
        "name": "name",
        "description": "description",
        "rendering_configuration": "renderingConfiguration",
        "server_side_encryption_configuration": "serverSideEncryptionConfiguration",
        "source_configuration": "sourceConfiguration",
        "tags": "tags",
        "vector_ingestion_configuration": "vectorIngestionConfiguration",
    },
)
class CfnKnowledgeBaseProps:
    def __init__(
        self,
        *,
        knowledge_base_type: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        rendering_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.RenderingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vector_ingestion_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.VectorIngestionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnKnowledgeBase``.

        :param knowledge_base_type: The type of knowledge base. Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically.
        :param name: The name of the knowledge base.
        :param description: The description.
        :param rendering_configuration: Information about how to render the content.
        :param server_side_encryption_configuration: This customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom. For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .
        :param source_configuration: The source of the knowledge base content. Only set this argument for EXTERNAL or Managed knowledge bases.
        :param tags: The tags used to organize, track, or control access for this resource.
        :param vector_ingestion_configuration: Contains details about how to ingest the documents in a data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_knowledge_base_props = wisdom.CfnKnowledgeBaseProps(
                knowledge_base_type="knowledgeBaseType",
                name="name",
            
                # the properties below are optional
                description="description",
                rendering_configuration=wisdom.CfnKnowledgeBase.RenderingConfigurationProperty(
                    template_uri="templateUri"
                ),
                server_side_encryption_configuration=wisdom.CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                ),
                source_configuration=wisdom.CfnKnowledgeBase.SourceConfigurationProperty(
                    app_integrations=wisdom.CfnKnowledgeBase.AppIntegrationsConfigurationProperty(
                        app_integration_arn="appIntegrationArn",
            
                        # the properties below are optional
                        object_fields=["objectFields"]
                    ),
                    managed_source_configuration=wisdom.CfnKnowledgeBase.ManagedSourceConfigurationProperty(
                        web_crawler_configuration=wisdom.CfnKnowledgeBase.WebCrawlerConfigurationProperty(
                            url_configuration=wisdom.CfnKnowledgeBase.UrlConfigurationProperty(
                                seed_urls=[wisdom.CfnKnowledgeBase.SeedUrlProperty(
                                    url="url"
                                )]
                            ),
            
                            # the properties below are optional
                            crawler_limits=wisdom.CfnKnowledgeBase.CrawlerLimitsProperty(
                                rate_limit=123
                            ),
                            exclusion_filters=["exclusionFilters"],
                            inclusion_filters=["inclusionFilters"],
                            scope="scope"
                        )
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vector_ingestion_configuration=wisdom.CfnKnowledgeBase.VectorIngestionConfigurationProperty(
                    chunking_configuration=wisdom.CfnKnowledgeBase.ChunkingConfigurationProperty(
                        chunking_strategy="chunkingStrategy",
            
                        # the properties below are optional
                        fixed_size_chunking_configuration=wisdom.CfnKnowledgeBase.FixedSizeChunkingConfigurationProperty(
                            max_tokens=123,
                            overlap_percentage=123
                        ),
                        hierarchical_chunking_configuration=wisdom.CfnKnowledgeBase.HierarchicalChunkingConfigurationProperty(
                            level_configurations=[wisdom.CfnKnowledgeBase.HierarchicalChunkingLevelConfigurationProperty(
                                max_tokens=123
                            )],
                            overlap_tokens=123
                        ),
                        semantic_chunking_configuration=wisdom.CfnKnowledgeBase.SemanticChunkingConfigurationProperty(
                            breakpoint_percentile_threshold=123,
                            buffer_size=123,
                            max_tokens=123
                        )
                    ),
                    parsing_configuration=wisdom.CfnKnowledgeBase.ParsingConfigurationProperty(
                        parsing_strategy="parsingStrategy",
            
                        # the properties below are optional
                        bedrock_foundation_model_configuration=wisdom.CfnKnowledgeBase.BedrockFoundationModelConfigurationProperty(
                            model_arn="modelArn",
            
                            # the properties below are optional
                            parsing_prompt=wisdom.CfnKnowledgeBase.ParsingPromptProperty(
                                parsing_prompt_text="parsingPromptText"
                            )
                        )
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b2c89f78d66a3c10ed4851c5bc420028f69cc91ddabbe2ac038dd7332ea1edd)
            check_type(argname="argument knowledge_base_type", value=knowledge_base_type, expected_type=type_hints["knowledge_base_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument rendering_configuration", value=rendering_configuration, expected_type=type_hints["rendering_configuration"])
            check_type(argname="argument server_side_encryption_configuration", value=server_side_encryption_configuration, expected_type=type_hints["server_side_encryption_configuration"])
            check_type(argname="argument source_configuration", value=source_configuration, expected_type=type_hints["source_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vector_ingestion_configuration", value=vector_ingestion_configuration, expected_type=type_hints["vector_ingestion_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "knowledge_base_type": knowledge_base_type,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if rendering_configuration is not None:
            self._values["rendering_configuration"] = rendering_configuration
        if server_side_encryption_configuration is not None:
            self._values["server_side_encryption_configuration"] = server_side_encryption_configuration
        if source_configuration is not None:
            self._values["source_configuration"] = source_configuration
        if tags is not None:
            self._values["tags"] = tags
        if vector_ingestion_configuration is not None:
            self._values["vector_ingestion_configuration"] = vector_ingestion_configuration

    @builtins.property
    def knowledge_base_type(self) -> builtins.str:
        '''The type of knowledge base.

        Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-knowledgebasetype
        '''
        result = self._values.get("knowledge_base_type")
        assert result is not None, "Required property 'knowledge_base_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the knowledge base.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rendering_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.RenderingConfigurationProperty]]:
        '''Information about how to render the content.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-renderingconfiguration
        '''
        result = self._values.get("rendering_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.RenderingConfigurationProperty]], result)

    @builtins.property
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty]]:
        '''This customer managed key must have a policy that allows ``kms:CreateGrant`` and ``kms:DescribeKey`` permissions to the IAM identity using the key to invoke Wisdom.

        For more information about setting up a customer managed key for Wisdom, see `Enable Amazon Connect Wisdom for your instance <https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html>`_ . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-serversideencryptionconfiguration
        '''
        result = self._values.get("server_side_encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty]], result)

    @builtins.property
    def source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.SourceConfigurationProperty]]:
        '''The source of the knowledge base content.

        Only set this argument for EXTERNAL or Managed knowledge bases.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-sourceconfiguration
        '''
        result = self._values.get("source_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.SourceConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vector_ingestion_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.VectorIngestionConfigurationProperty]]:
        '''Contains details about how to ingest the documents in a data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-vectoringestionconfiguration
        '''
        result = self._values.get("vector_ingestion_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.VectorIngestionConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKnowledgeBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnMessageTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplate",
):
    '''Creates an Amazon Q in Connect message template.

    The name of the message template has to be unique for each knowledge base. The channel subtype of the message template is immutable and cannot be modified after creation. After the message template is created, you can use the ``$LATEST`` qualifier to reference the created message template.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplate.html
    :cloudformationResource: AWS::Wisdom::MessageTemplate
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_message_template = wisdom.CfnMessageTemplate(self, "MyCfnMessageTemplate",
            channel_subtype="channelSubtype",
            content=wisdom.CfnMessageTemplate.ContentProperty(
                email_message_template_content=wisdom.CfnMessageTemplate.EmailMessageTemplateContentProperty(
                    body=wisdom.CfnMessageTemplate.EmailMessageTemplateContentBodyProperty(
                        html=wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                            content="content"
                        ),
                        plain_text=wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                            content="content"
                        )
                    ),
                    headers=[wisdom.CfnMessageTemplate.EmailMessageTemplateHeaderProperty(
                        name="name",
                        value="value"
                    )],
                    subject="subject"
                ),
                sms_message_template_content=wisdom.CfnMessageTemplate.SmsMessageTemplateContentProperty(
                    body=wisdom.CfnMessageTemplate.SmsMessageTemplateContentBodyProperty(
                        plain_text=wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                            content="content"
                        )
                    )
                )
            ),
            knowledge_base_arn="knowledgeBaseArn",
            name="name",
        
            # the properties below are optional
            default_attributes=wisdom.CfnMessageTemplate.MessageTemplateAttributesProperty(
                agent_attributes=wisdom.CfnMessageTemplate.AgentAttributesProperty(
                    first_name="firstName",
                    last_name="lastName"
                ),
                custom_attributes={
                    "custom_attributes_key": "customAttributes"
                },
                customer_profile_attributes=wisdom.CfnMessageTemplate.CustomerProfileAttributesProperty(
                    account_number="accountNumber",
                    additional_information="additionalInformation",
                    address1="address1",
                    address2="address2",
                    address3="address3",
                    address4="address4",
                    billing_address1="billingAddress1",
                    billing_address2="billingAddress2",
                    billing_address3="billingAddress3",
                    billing_address4="billingAddress4",
                    billing_city="billingCity",
                    billing_country="billingCountry",
                    billing_county="billingCounty",
                    billing_postal_code="billingPostalCode",
                    billing_province="billingProvince",
                    billing_state="billingState",
                    birth_date="birthDate",
                    business_email_address="businessEmailAddress",
                    business_name="businessName",
                    business_phone_number="businessPhoneNumber",
                    city="city",
                    country="country",
                    county="county",
                    custom={
                        "custom_key": "custom"
                    },
                    email_address="emailAddress",
                    first_name="firstName",
                    gender="gender",
                    home_phone_number="homePhoneNumber",
                    last_name="lastName",
                    mailing_address1="mailingAddress1",
                    mailing_address2="mailingAddress2",
                    mailing_address3="mailingAddress3",
                    mailing_address4="mailingAddress4",
                    mailing_city="mailingCity",
                    mailing_country="mailingCountry",
                    mailing_county="mailingCounty",
                    mailing_postal_code="mailingPostalCode",
                    mailing_province="mailingProvince",
                    mailing_state="mailingState",
                    middle_name="middleName",
                    mobile_phone_number="mobilePhoneNumber",
                    party_type="partyType",
                    phone_number="phoneNumber",
                    postal_code="postalCode",
                    profile_arn="profileArn",
                    profile_id="profileId",
                    province="province",
                    shipping_address1="shippingAddress1",
                    shipping_address2="shippingAddress2",
                    shipping_address3="shippingAddress3",
                    shipping_address4="shippingAddress4",
                    shipping_city="shippingCity",
                    shipping_country="shippingCountry",
                    shipping_county="shippingCounty",
                    shipping_postal_code="shippingPostalCode",
                    shipping_province="shippingProvince",
                    shipping_state="shippingState",
                    state="state"
                ),
                system_attributes=wisdom.CfnMessageTemplate.SystemAttributesProperty(
                    customer_endpoint=wisdom.CfnMessageTemplate.SystemEndpointAttributesProperty(
                        address="address"
                    ),
                    name="name",
                    system_endpoint=wisdom.CfnMessageTemplate.SystemEndpointAttributesProperty(
                        address="address"
                    )
                )
            ),
            description="description",
            grouping_configuration=wisdom.CfnMessageTemplate.GroupingConfigurationProperty(
                criteria="criteria",
                values=["values"]
            ),
            language="language",
            message_template_attachments=[wisdom.CfnMessageTemplate.MessageTemplateAttachmentProperty(
                attachment_name="attachmentName",
                s3_presigned_url="s3PresignedUrl",
        
                # the properties below are optional
                attachment_id="attachmentId"
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
        channel_subtype: builtins.str,
        content: typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.ContentProperty", typing.Dict[builtins.str, typing.Any]]],
        knowledge_base_arn: builtins.str,
        name: builtins.str,
        default_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.MessageTemplateAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        grouping_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.GroupingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        language: typing.Optional[builtins.str] = None,
        message_template_attachments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.MessageTemplateAttachmentProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param channel_subtype: The channel subtype this message template applies to.
        :param content: The content of the message template.
        :param knowledge_base_arn: The Amazon Resource Name (ARN) of the knowledge base.
        :param name: The name of the message template.
        :param default_attributes: An object that specifies the default values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.
        :param description: The description of the message template.
        :param grouping_configuration: The configuration information of the external data source.
        :param language: The language code value for the language in which the quick response is written. The supported language codes include ``de_DE`` , ``en_US`` , ``es_ES`` , ``fr_FR`` , ``id_ID`` , ``it_IT`` , ``ja_JP`` , ``ko_KR`` , ``pt_BR`` , ``zh_CN`` , ``zh_TW``
        :param message_template_attachments: List of message template attachments.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d99067595817364fbb03fa017437b616b3c32bdfb38c386a909328ac78d1053)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMessageTemplateProps(
            channel_subtype=channel_subtype,
            content=content,
            knowledge_base_arn=knowledge_base_arn,
            name=name,
            default_attributes=default_attributes,
            description=description,
            grouping_configuration=grouping_configuration,
            language=language,
            message_template_attachments=message_template_attachments,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bd3a69fd8e8039386e9bb281e08fdde1b7575eb0f4584620df31d2602466d2b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__51e5807f3469c5509115f0174d0a4a4e94bf8231cc93e8f0094c9c6a9a4b8671)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrMessageTemplateArn")
    def attr_message_template_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the message template.

        :cloudformationAttribute: MessageTemplateArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMessageTemplateArn"))

    @builtins.property
    @jsii.member(jsii_name="attrMessageTemplateContentSha256")
    def attr_message_template_content_sha256(self) -> builtins.str:
        '''The checksum value of the message template content that is referenced by the ``$LATEST`` qualifier.

        It can be returned in ``MessageTemplateData`` or ``ExtendedMessageTemplateData`` . It’s calculated by content, language, ``defaultAttributes`` and ``Attachments`` of the message template.

        :cloudformationAttribute: MessageTemplateContentSha256
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMessageTemplateContentSha256"))

    @builtins.property
    @jsii.member(jsii_name="attrMessageTemplateId")
    def attr_message_template_id(self) -> builtins.str:
        '''The identifier of the message template.

        :cloudformationAttribute: MessageTemplateId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMessageTemplateId"))

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
    @jsii.member(jsii_name="channelSubtype")
    def channel_subtype(self) -> builtins.str:
        '''The channel subtype this message template applies to.'''
        return typing.cast(builtins.str, jsii.get(self, "channelSubtype"))

    @channel_subtype.setter
    def channel_subtype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9a491239929796de387804b5ffabbcc9d2d80c46187061bad6dbd69cb644824)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelSubtype", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.ContentProperty"]:
        '''The content of the message template.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.ContentProperty"], jsii.get(self, "content"))

    @content.setter
    def content(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.ContentProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ee7a5f3ae13619e783db2bde4848cd5e3d84a6c38e5cf0e040a3d6810a2b619)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="knowledgeBaseArn")
    def knowledge_base_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the knowledge base.'''
        return typing.cast(builtins.str, jsii.get(self, "knowledgeBaseArn"))

    @knowledge_base_arn.setter
    def knowledge_base_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1089af8f7f43591721a256e0bcbb3a3e75172ab965d8e37a20d563d96fea6c7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "knowledgeBaseArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the message template.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d2ebd98b6a5c07a0bfd2e4c013c178b5a1cdc3388149770a1a36251b5b6e6e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultAttributes")
    def default_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.MessageTemplateAttributesProperty"]]:
        '''An object that specifies the default values to use for variables in the message template.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.MessageTemplateAttributesProperty"]], jsii.get(self, "defaultAttributes"))

    @default_attributes.setter
    def default_attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.MessageTemplateAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c90c4e95d1b7bc695fb4935b1c99d447bbd24e9da4bc0367c93bcfe1269fbe2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAttributes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the message template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f18337bd9aa5b9f46e3c5167353a0544735c7f2633460e6e48392e441c4c1ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="groupingConfiguration")
    def grouping_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.GroupingConfigurationProperty"]]:
        '''The configuration information of the external data source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.GroupingConfigurationProperty"]], jsii.get(self, "groupingConfiguration"))

    @grouping_configuration.setter
    def grouping_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.GroupingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a293700b704f958a326ada96bec14e09605f0a2af76a1972e28306ecd1c0bea9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupingConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="language")
    def language(self) -> typing.Optional[builtins.str]:
        '''The language code value for the language in which the quick response is written.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "language"))

    @language.setter
    def language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4bfbbc60d2eb951b3081015f23b57de459d734cb6ca7e17db3b5ea28887251d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "language", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="messageTemplateAttachments")
    def message_template_attachments(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.MessageTemplateAttachmentProperty"]]]]:
        '''List of message template attachments.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.MessageTemplateAttachmentProperty"]]]], jsii.get(self, "messageTemplateAttachments"))

    @message_template_attachments.setter
    def message_template_attachments(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.MessageTemplateAttachmentProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99e58f577d070d3c392b7519e6ec169337ff707d8d0fbec1d5b147b3eb27b11a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageTemplateAttachments", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a8749d4385c7e2fd758f8b86ee5b36af0b25c3e531a4c7936791aa080a35421)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplate.AgentAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"first_name": "firstName", "last_name": "lastName"},
    )
    class AgentAttributesProperty:
        def __init__(
            self,
            *,
            first_name: typing.Optional[builtins.str] = None,
            last_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about an agent.

            :param first_name: The agent’s first name as entered in their Amazon Connect user account.
            :param last_name: The agent’s last name as entered in their Amazon Connect user account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-agentattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                agent_attributes_property = wisdom.CfnMessageTemplate.AgentAttributesProperty(
                    first_name="firstName",
                    last_name="lastName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__19e932a438b8adf98a2f01a0c01e6402cbbcee9d65521d2cf7fd141793378561)
                check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
                check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if first_name is not None:
                self._values["first_name"] = first_name
            if last_name is not None:
                self._values["last_name"] = last_name

        @builtins.property
        def first_name(self) -> typing.Optional[builtins.str]:
            '''The agent’s first name as entered in their Amazon Connect user account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-agentattributes.html#cfn-wisdom-messagetemplate-agentattributes-firstname
            '''
            result = self._values.get("first_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def last_name(self) -> typing.Optional[builtins.str]:
            '''The agent’s last name as entered in their Amazon Connect user account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-agentattributes.html#cfn-wisdom-messagetemplate-agentattributes-lastname
            '''
            result = self._values.get("last_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AgentAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplate.ContentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "email_message_template_content": "emailMessageTemplateContent",
            "sms_message_template_content": "smsMessageTemplateContent",
        },
    )
    class ContentProperty:
        def __init__(
            self,
            *,
            email_message_template_content: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.EmailMessageTemplateContentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sms_message_template_content: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.SmsMessageTemplateContentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The content of the message template.

            :param email_message_template_content: The content of the message template that applies to the email channel subtype.
            :param sms_message_template_content: The content of message template that applies to SMS channel subtype.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-content.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                content_property = wisdom.CfnMessageTemplate.ContentProperty(
                    email_message_template_content=wisdom.CfnMessageTemplate.EmailMessageTemplateContentProperty(
                        body=wisdom.CfnMessageTemplate.EmailMessageTemplateContentBodyProperty(
                            html=wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                                content="content"
                            ),
                            plain_text=wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                                content="content"
                            )
                        ),
                        headers=[wisdom.CfnMessageTemplate.EmailMessageTemplateHeaderProperty(
                            name="name",
                            value="value"
                        )],
                        subject="subject"
                    ),
                    sms_message_template_content=wisdom.CfnMessageTemplate.SmsMessageTemplateContentProperty(
                        body=wisdom.CfnMessageTemplate.SmsMessageTemplateContentBodyProperty(
                            plain_text=wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                                content="content"
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0d47d957dda4da1971b35706dec828b7fec81d445218ea14dbd7300f581ac052)
                check_type(argname="argument email_message_template_content", value=email_message_template_content, expected_type=type_hints["email_message_template_content"])
                check_type(argname="argument sms_message_template_content", value=sms_message_template_content, expected_type=type_hints["sms_message_template_content"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if email_message_template_content is not None:
                self._values["email_message_template_content"] = email_message_template_content
            if sms_message_template_content is not None:
                self._values["sms_message_template_content"] = sms_message_template_content

        @builtins.property
        def email_message_template_content(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.EmailMessageTemplateContentProperty"]]:
            '''The content of the message template that applies to the email channel subtype.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-content.html#cfn-wisdom-messagetemplate-content-emailmessagetemplatecontent
            '''
            result = self._values.get("email_message_template_content")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.EmailMessageTemplateContentProperty"]], result)

        @builtins.property
        def sms_message_template_content(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.SmsMessageTemplateContentProperty"]]:
            '''The content of message template that applies to SMS channel subtype.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-content.html#cfn-wisdom-messagetemplate-content-smsmessagetemplatecontent
            '''
            result = self._values.get("sms_message_template_content")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.SmsMessageTemplateContentProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplate.CustomerProfileAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_number": "accountNumber",
            "additional_information": "additionalInformation",
            "address1": "address1",
            "address2": "address2",
            "address3": "address3",
            "address4": "address4",
            "billing_address1": "billingAddress1",
            "billing_address2": "billingAddress2",
            "billing_address3": "billingAddress3",
            "billing_address4": "billingAddress4",
            "billing_city": "billingCity",
            "billing_country": "billingCountry",
            "billing_county": "billingCounty",
            "billing_postal_code": "billingPostalCode",
            "billing_province": "billingProvince",
            "billing_state": "billingState",
            "birth_date": "birthDate",
            "business_email_address": "businessEmailAddress",
            "business_name": "businessName",
            "business_phone_number": "businessPhoneNumber",
            "city": "city",
            "country": "country",
            "county": "county",
            "custom": "custom",
            "email_address": "emailAddress",
            "first_name": "firstName",
            "gender": "gender",
            "home_phone_number": "homePhoneNumber",
            "last_name": "lastName",
            "mailing_address1": "mailingAddress1",
            "mailing_address2": "mailingAddress2",
            "mailing_address3": "mailingAddress3",
            "mailing_address4": "mailingAddress4",
            "mailing_city": "mailingCity",
            "mailing_country": "mailingCountry",
            "mailing_county": "mailingCounty",
            "mailing_postal_code": "mailingPostalCode",
            "mailing_province": "mailingProvince",
            "mailing_state": "mailingState",
            "middle_name": "middleName",
            "mobile_phone_number": "mobilePhoneNumber",
            "party_type": "partyType",
            "phone_number": "phoneNumber",
            "postal_code": "postalCode",
            "profile_arn": "profileArn",
            "profile_id": "profileId",
            "province": "province",
            "shipping_address1": "shippingAddress1",
            "shipping_address2": "shippingAddress2",
            "shipping_address3": "shippingAddress3",
            "shipping_address4": "shippingAddress4",
            "shipping_city": "shippingCity",
            "shipping_country": "shippingCountry",
            "shipping_county": "shippingCounty",
            "shipping_postal_code": "shippingPostalCode",
            "shipping_province": "shippingProvince",
            "shipping_state": "shippingState",
            "state": "state",
        },
    )
    class CustomerProfileAttributesProperty:
        def __init__(
            self,
            *,
            account_number: typing.Optional[builtins.str] = None,
            additional_information: typing.Optional[builtins.str] = None,
            address1: typing.Optional[builtins.str] = None,
            address2: typing.Optional[builtins.str] = None,
            address3: typing.Optional[builtins.str] = None,
            address4: typing.Optional[builtins.str] = None,
            billing_address1: typing.Optional[builtins.str] = None,
            billing_address2: typing.Optional[builtins.str] = None,
            billing_address3: typing.Optional[builtins.str] = None,
            billing_address4: typing.Optional[builtins.str] = None,
            billing_city: typing.Optional[builtins.str] = None,
            billing_country: typing.Optional[builtins.str] = None,
            billing_county: typing.Optional[builtins.str] = None,
            billing_postal_code: typing.Optional[builtins.str] = None,
            billing_province: typing.Optional[builtins.str] = None,
            billing_state: typing.Optional[builtins.str] = None,
            birth_date: typing.Optional[builtins.str] = None,
            business_email_address: typing.Optional[builtins.str] = None,
            business_name: typing.Optional[builtins.str] = None,
            business_phone_number: typing.Optional[builtins.str] = None,
            city: typing.Optional[builtins.str] = None,
            country: typing.Optional[builtins.str] = None,
            county: typing.Optional[builtins.str] = None,
            custom: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            email_address: typing.Optional[builtins.str] = None,
            first_name: typing.Optional[builtins.str] = None,
            gender: typing.Optional[builtins.str] = None,
            home_phone_number: typing.Optional[builtins.str] = None,
            last_name: typing.Optional[builtins.str] = None,
            mailing_address1: typing.Optional[builtins.str] = None,
            mailing_address2: typing.Optional[builtins.str] = None,
            mailing_address3: typing.Optional[builtins.str] = None,
            mailing_address4: typing.Optional[builtins.str] = None,
            mailing_city: typing.Optional[builtins.str] = None,
            mailing_country: typing.Optional[builtins.str] = None,
            mailing_county: typing.Optional[builtins.str] = None,
            mailing_postal_code: typing.Optional[builtins.str] = None,
            mailing_province: typing.Optional[builtins.str] = None,
            mailing_state: typing.Optional[builtins.str] = None,
            middle_name: typing.Optional[builtins.str] = None,
            mobile_phone_number: typing.Optional[builtins.str] = None,
            party_type: typing.Optional[builtins.str] = None,
            phone_number: typing.Optional[builtins.str] = None,
            postal_code: typing.Optional[builtins.str] = None,
            profile_arn: typing.Optional[builtins.str] = None,
            profile_id: typing.Optional[builtins.str] = None,
            province: typing.Optional[builtins.str] = None,
            shipping_address1: typing.Optional[builtins.str] = None,
            shipping_address2: typing.Optional[builtins.str] = None,
            shipping_address3: typing.Optional[builtins.str] = None,
            shipping_address4: typing.Optional[builtins.str] = None,
            shipping_city: typing.Optional[builtins.str] = None,
            shipping_country: typing.Optional[builtins.str] = None,
            shipping_county: typing.Optional[builtins.str] = None,
            shipping_postal_code: typing.Optional[builtins.str] = None,
            shipping_province: typing.Optional[builtins.str] = None,
            shipping_state: typing.Optional[builtins.str] = None,
            state: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The customer profile attributes that are used with the message template.

            :param account_number: A unique account number that you have given to the customer.
            :param additional_information: Any additional information relevant to the customer's profile.
            :param address1: The first line of a customer address.
            :param address2: The second line of a customer address.
            :param address3: The third line of a customer address.
            :param address4: The fourth line of a customer address.
            :param billing_address1: The first line of a customer’s billing address.
            :param billing_address2: The second line of a customer’s billing address.
            :param billing_address3: The third line of a customer’s billing address.
            :param billing_address4: The fourth line of a customer’s billing address.
            :param billing_city: The city of a customer’s billing address.
            :param billing_country: The country of a customer’s billing address.
            :param billing_county: The county of a customer’s billing address.
            :param billing_postal_code: The postal code of a customer’s billing address.
            :param billing_province: The province of a customer’s billing address.
            :param billing_state: The state of a customer’s billing address.
            :param birth_date: The customer's birth date.
            :param business_email_address: The customer's business email address.
            :param business_name: The name of the customer's business.
            :param business_phone_number: The customer's business phone number.
            :param city: The city in which a customer lives.
            :param country: The country in which a customer lives.
            :param county: The county in which a customer lives.
            :param custom: The custom attributes in customer profile attributes.
            :param email_address: The customer's email address, which has not been specified as a personal or business address.
            :param first_name: The customer's first name.
            :param gender: The customer's gender.
            :param home_phone_number: The customer's mobile phone number.
            :param last_name: The customer's last name.
            :param mailing_address1: The first line of a customer’s mailing address.
            :param mailing_address2: The second line of a customer’s mailing address.
            :param mailing_address3: The third line of a customer’s mailing address.
            :param mailing_address4: The fourth line of a customer’s mailing address.
            :param mailing_city: The city of a customer’s mailing address.
            :param mailing_country: The country of a customer’s mailing address.
            :param mailing_county: The county of a customer’s mailing address.
            :param mailing_postal_code: The postal code of a customer’s mailing address.
            :param mailing_province: The province of a customer’s mailing address.
            :param mailing_state: The state of a customer’s mailing address.
            :param middle_name: The customer's middle name.
            :param mobile_phone_number: The customer's mobile phone number.
            :param party_type: The customer's party type.
            :param phone_number: The customer's phone number, which has not been specified as a mobile, home, or business number.
            :param postal_code: The postal code of a customer address.
            :param profile_arn: The ARN of a customer profile.
            :param profile_id: The unique identifier of a customer profile.
            :param province: The province in which a customer lives.
            :param shipping_address1: The first line of a customer’s shipping address.
            :param shipping_address2: The second line of a customer’s shipping address.
            :param shipping_address3: The third line of a customer’s shipping address.
            :param shipping_address4: The fourth line of a customer’s shipping address.
            :param shipping_city: The city of a customer’s shipping address.
            :param shipping_country: The country of a customer’s shipping address.
            :param shipping_county: The county of a customer’s shipping address.
            :param shipping_postal_code: The postal code of a customer’s shipping address.
            :param shipping_province: The province of a customer’s shipping address.
            :param shipping_state: The state of a customer’s shipping address.
            :param state: The state in which a customer lives.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                customer_profile_attributes_property = wisdom.CfnMessageTemplate.CustomerProfileAttributesProperty(
                    account_number="accountNumber",
                    additional_information="additionalInformation",
                    address1="address1",
                    address2="address2",
                    address3="address3",
                    address4="address4",
                    billing_address1="billingAddress1",
                    billing_address2="billingAddress2",
                    billing_address3="billingAddress3",
                    billing_address4="billingAddress4",
                    billing_city="billingCity",
                    billing_country="billingCountry",
                    billing_county="billingCounty",
                    billing_postal_code="billingPostalCode",
                    billing_province="billingProvince",
                    billing_state="billingState",
                    birth_date="birthDate",
                    business_email_address="businessEmailAddress",
                    business_name="businessName",
                    business_phone_number="businessPhoneNumber",
                    city="city",
                    country="country",
                    county="county",
                    custom={
                        "custom_key": "custom"
                    },
                    email_address="emailAddress",
                    first_name="firstName",
                    gender="gender",
                    home_phone_number="homePhoneNumber",
                    last_name="lastName",
                    mailing_address1="mailingAddress1",
                    mailing_address2="mailingAddress2",
                    mailing_address3="mailingAddress3",
                    mailing_address4="mailingAddress4",
                    mailing_city="mailingCity",
                    mailing_country="mailingCountry",
                    mailing_county="mailingCounty",
                    mailing_postal_code="mailingPostalCode",
                    mailing_province="mailingProvince",
                    mailing_state="mailingState",
                    middle_name="middleName",
                    mobile_phone_number="mobilePhoneNumber",
                    party_type="partyType",
                    phone_number="phoneNumber",
                    postal_code="postalCode",
                    profile_arn="profileArn",
                    profile_id="profileId",
                    province="province",
                    shipping_address1="shippingAddress1",
                    shipping_address2="shippingAddress2",
                    shipping_address3="shippingAddress3",
                    shipping_address4="shippingAddress4",
                    shipping_city="shippingCity",
                    shipping_country="shippingCountry",
                    shipping_county="shippingCounty",
                    shipping_postal_code="shippingPostalCode",
                    shipping_province="shippingProvince",
                    shipping_state="shippingState",
                    state="state"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__31a9d5f6219c52f900443be7cd1a4f580db25aaf647c7876e4062d152500f342)
                check_type(argname="argument account_number", value=account_number, expected_type=type_hints["account_number"])
                check_type(argname="argument additional_information", value=additional_information, expected_type=type_hints["additional_information"])
                check_type(argname="argument address1", value=address1, expected_type=type_hints["address1"])
                check_type(argname="argument address2", value=address2, expected_type=type_hints["address2"])
                check_type(argname="argument address3", value=address3, expected_type=type_hints["address3"])
                check_type(argname="argument address4", value=address4, expected_type=type_hints["address4"])
                check_type(argname="argument billing_address1", value=billing_address1, expected_type=type_hints["billing_address1"])
                check_type(argname="argument billing_address2", value=billing_address2, expected_type=type_hints["billing_address2"])
                check_type(argname="argument billing_address3", value=billing_address3, expected_type=type_hints["billing_address3"])
                check_type(argname="argument billing_address4", value=billing_address4, expected_type=type_hints["billing_address4"])
                check_type(argname="argument billing_city", value=billing_city, expected_type=type_hints["billing_city"])
                check_type(argname="argument billing_country", value=billing_country, expected_type=type_hints["billing_country"])
                check_type(argname="argument billing_county", value=billing_county, expected_type=type_hints["billing_county"])
                check_type(argname="argument billing_postal_code", value=billing_postal_code, expected_type=type_hints["billing_postal_code"])
                check_type(argname="argument billing_province", value=billing_province, expected_type=type_hints["billing_province"])
                check_type(argname="argument billing_state", value=billing_state, expected_type=type_hints["billing_state"])
                check_type(argname="argument birth_date", value=birth_date, expected_type=type_hints["birth_date"])
                check_type(argname="argument business_email_address", value=business_email_address, expected_type=type_hints["business_email_address"])
                check_type(argname="argument business_name", value=business_name, expected_type=type_hints["business_name"])
                check_type(argname="argument business_phone_number", value=business_phone_number, expected_type=type_hints["business_phone_number"])
                check_type(argname="argument city", value=city, expected_type=type_hints["city"])
                check_type(argname="argument country", value=country, expected_type=type_hints["country"])
                check_type(argname="argument county", value=county, expected_type=type_hints["county"])
                check_type(argname="argument custom", value=custom, expected_type=type_hints["custom"])
                check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
                check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
                check_type(argname="argument gender", value=gender, expected_type=type_hints["gender"])
                check_type(argname="argument home_phone_number", value=home_phone_number, expected_type=type_hints["home_phone_number"])
                check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
                check_type(argname="argument mailing_address1", value=mailing_address1, expected_type=type_hints["mailing_address1"])
                check_type(argname="argument mailing_address2", value=mailing_address2, expected_type=type_hints["mailing_address2"])
                check_type(argname="argument mailing_address3", value=mailing_address3, expected_type=type_hints["mailing_address3"])
                check_type(argname="argument mailing_address4", value=mailing_address4, expected_type=type_hints["mailing_address4"])
                check_type(argname="argument mailing_city", value=mailing_city, expected_type=type_hints["mailing_city"])
                check_type(argname="argument mailing_country", value=mailing_country, expected_type=type_hints["mailing_country"])
                check_type(argname="argument mailing_county", value=mailing_county, expected_type=type_hints["mailing_county"])
                check_type(argname="argument mailing_postal_code", value=mailing_postal_code, expected_type=type_hints["mailing_postal_code"])
                check_type(argname="argument mailing_province", value=mailing_province, expected_type=type_hints["mailing_province"])
                check_type(argname="argument mailing_state", value=mailing_state, expected_type=type_hints["mailing_state"])
                check_type(argname="argument middle_name", value=middle_name, expected_type=type_hints["middle_name"])
                check_type(argname="argument mobile_phone_number", value=mobile_phone_number, expected_type=type_hints["mobile_phone_number"])
                check_type(argname="argument party_type", value=party_type, expected_type=type_hints["party_type"])
                check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
                check_type(argname="argument postal_code", value=postal_code, expected_type=type_hints["postal_code"])
                check_type(argname="argument profile_arn", value=profile_arn, expected_type=type_hints["profile_arn"])
                check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
                check_type(argname="argument province", value=province, expected_type=type_hints["province"])
                check_type(argname="argument shipping_address1", value=shipping_address1, expected_type=type_hints["shipping_address1"])
                check_type(argname="argument shipping_address2", value=shipping_address2, expected_type=type_hints["shipping_address2"])
                check_type(argname="argument shipping_address3", value=shipping_address3, expected_type=type_hints["shipping_address3"])
                check_type(argname="argument shipping_address4", value=shipping_address4, expected_type=type_hints["shipping_address4"])
                check_type(argname="argument shipping_city", value=shipping_city, expected_type=type_hints["shipping_city"])
                check_type(argname="argument shipping_country", value=shipping_country, expected_type=type_hints["shipping_country"])
                check_type(argname="argument shipping_county", value=shipping_county, expected_type=type_hints["shipping_county"])
                check_type(argname="argument shipping_postal_code", value=shipping_postal_code, expected_type=type_hints["shipping_postal_code"])
                check_type(argname="argument shipping_province", value=shipping_province, expected_type=type_hints["shipping_province"])
                check_type(argname="argument shipping_state", value=shipping_state, expected_type=type_hints["shipping_state"])
                check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if account_number is not None:
                self._values["account_number"] = account_number
            if additional_information is not None:
                self._values["additional_information"] = additional_information
            if address1 is not None:
                self._values["address1"] = address1
            if address2 is not None:
                self._values["address2"] = address2
            if address3 is not None:
                self._values["address3"] = address3
            if address4 is not None:
                self._values["address4"] = address4
            if billing_address1 is not None:
                self._values["billing_address1"] = billing_address1
            if billing_address2 is not None:
                self._values["billing_address2"] = billing_address2
            if billing_address3 is not None:
                self._values["billing_address3"] = billing_address3
            if billing_address4 is not None:
                self._values["billing_address4"] = billing_address4
            if billing_city is not None:
                self._values["billing_city"] = billing_city
            if billing_country is not None:
                self._values["billing_country"] = billing_country
            if billing_county is not None:
                self._values["billing_county"] = billing_county
            if billing_postal_code is not None:
                self._values["billing_postal_code"] = billing_postal_code
            if billing_province is not None:
                self._values["billing_province"] = billing_province
            if billing_state is not None:
                self._values["billing_state"] = billing_state
            if birth_date is not None:
                self._values["birth_date"] = birth_date
            if business_email_address is not None:
                self._values["business_email_address"] = business_email_address
            if business_name is not None:
                self._values["business_name"] = business_name
            if business_phone_number is not None:
                self._values["business_phone_number"] = business_phone_number
            if city is not None:
                self._values["city"] = city
            if country is not None:
                self._values["country"] = country
            if county is not None:
                self._values["county"] = county
            if custom is not None:
                self._values["custom"] = custom
            if email_address is not None:
                self._values["email_address"] = email_address
            if first_name is not None:
                self._values["first_name"] = first_name
            if gender is not None:
                self._values["gender"] = gender
            if home_phone_number is not None:
                self._values["home_phone_number"] = home_phone_number
            if last_name is not None:
                self._values["last_name"] = last_name
            if mailing_address1 is not None:
                self._values["mailing_address1"] = mailing_address1
            if mailing_address2 is not None:
                self._values["mailing_address2"] = mailing_address2
            if mailing_address3 is not None:
                self._values["mailing_address3"] = mailing_address3
            if mailing_address4 is not None:
                self._values["mailing_address4"] = mailing_address4
            if mailing_city is not None:
                self._values["mailing_city"] = mailing_city
            if mailing_country is not None:
                self._values["mailing_country"] = mailing_country
            if mailing_county is not None:
                self._values["mailing_county"] = mailing_county
            if mailing_postal_code is not None:
                self._values["mailing_postal_code"] = mailing_postal_code
            if mailing_province is not None:
                self._values["mailing_province"] = mailing_province
            if mailing_state is not None:
                self._values["mailing_state"] = mailing_state
            if middle_name is not None:
                self._values["middle_name"] = middle_name
            if mobile_phone_number is not None:
                self._values["mobile_phone_number"] = mobile_phone_number
            if party_type is not None:
                self._values["party_type"] = party_type
            if phone_number is not None:
                self._values["phone_number"] = phone_number
            if postal_code is not None:
                self._values["postal_code"] = postal_code
            if profile_arn is not None:
                self._values["profile_arn"] = profile_arn
            if profile_id is not None:
                self._values["profile_id"] = profile_id
            if province is not None:
                self._values["province"] = province
            if shipping_address1 is not None:
                self._values["shipping_address1"] = shipping_address1
            if shipping_address2 is not None:
                self._values["shipping_address2"] = shipping_address2
            if shipping_address3 is not None:
                self._values["shipping_address3"] = shipping_address3
            if shipping_address4 is not None:
                self._values["shipping_address4"] = shipping_address4
            if shipping_city is not None:
                self._values["shipping_city"] = shipping_city
            if shipping_country is not None:
                self._values["shipping_country"] = shipping_country
            if shipping_county is not None:
                self._values["shipping_county"] = shipping_county
            if shipping_postal_code is not None:
                self._values["shipping_postal_code"] = shipping_postal_code
            if shipping_province is not None:
                self._values["shipping_province"] = shipping_province
            if shipping_state is not None:
                self._values["shipping_state"] = shipping_state
            if state is not None:
                self._values["state"] = state

        @builtins.property
        def account_number(self) -> typing.Optional[builtins.str]:
            '''A unique account number that you have given to the customer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-accountnumber
            '''
            result = self._values.get("account_number")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def additional_information(self) -> typing.Optional[builtins.str]:
            '''Any additional information relevant to the customer's profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-additionalinformation
            '''
            result = self._values.get("additional_information")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def address1(self) -> typing.Optional[builtins.str]:
            '''The first line of a customer address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-address1
            '''
            result = self._values.get("address1")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def address2(self) -> typing.Optional[builtins.str]:
            '''The second line of a customer address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-address2
            '''
            result = self._values.get("address2")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def address3(self) -> typing.Optional[builtins.str]:
            '''The third line of a customer address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-address3
            '''
            result = self._values.get("address3")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def address4(self) -> typing.Optional[builtins.str]:
            '''The fourth line of a customer address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-address4
            '''
            result = self._values.get("address4")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def billing_address1(self) -> typing.Optional[builtins.str]:
            '''The first line of a customer’s billing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress1
            '''
            result = self._values.get("billing_address1")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def billing_address2(self) -> typing.Optional[builtins.str]:
            '''The second line of a customer’s billing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress2
            '''
            result = self._values.get("billing_address2")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def billing_address3(self) -> typing.Optional[builtins.str]:
            '''The third line of a customer’s billing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress3
            '''
            result = self._values.get("billing_address3")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def billing_address4(self) -> typing.Optional[builtins.str]:
            '''The fourth line of a customer’s billing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-billingaddress4
            '''
            result = self._values.get("billing_address4")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def billing_city(self) -> typing.Optional[builtins.str]:
            '''The city of a customer’s billing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-billingcity
            '''
            result = self._values.get("billing_city")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def billing_country(self) -> typing.Optional[builtins.str]:
            '''The country of a customer’s billing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-billingcountry
            '''
            result = self._values.get("billing_country")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def billing_county(self) -> typing.Optional[builtins.str]:
            '''The county of a customer’s billing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-billingcounty
            '''
            result = self._values.get("billing_county")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def billing_postal_code(self) -> typing.Optional[builtins.str]:
            '''The postal code of a customer’s billing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-billingpostalcode
            '''
            result = self._values.get("billing_postal_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def billing_province(self) -> typing.Optional[builtins.str]:
            '''The province of a customer’s billing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-billingprovince
            '''
            result = self._values.get("billing_province")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def billing_state(self) -> typing.Optional[builtins.str]:
            '''The state of a customer’s billing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-billingstate
            '''
            result = self._values.get("billing_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def birth_date(self) -> typing.Optional[builtins.str]:
            '''The customer's birth date.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-birthdate
            '''
            result = self._values.get("birth_date")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def business_email_address(self) -> typing.Optional[builtins.str]:
            '''The customer's business email address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-businessemailaddress
            '''
            result = self._values.get("business_email_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def business_name(self) -> typing.Optional[builtins.str]:
            '''The name of the customer's business.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-businessname
            '''
            result = self._values.get("business_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def business_phone_number(self) -> typing.Optional[builtins.str]:
            '''The customer's business phone number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-businessphonenumber
            '''
            result = self._values.get("business_phone_number")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def city(self) -> typing.Optional[builtins.str]:
            '''The city in which a customer lives.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-city
            '''
            result = self._values.get("city")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def country(self) -> typing.Optional[builtins.str]:
            '''The country in which a customer lives.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-country
            '''
            result = self._values.get("country")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def county(self) -> typing.Optional[builtins.str]:
            '''The county in which a customer lives.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-county
            '''
            result = self._values.get("county")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The custom attributes in customer profile attributes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-custom
            '''
            result = self._values.get("custom")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def email_address(self) -> typing.Optional[builtins.str]:
            '''The customer's email address, which has not been specified as a personal or business address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-emailaddress
            '''
            result = self._values.get("email_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def first_name(self) -> typing.Optional[builtins.str]:
            '''The customer's first name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-firstname
            '''
            result = self._values.get("first_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def gender(self) -> typing.Optional[builtins.str]:
            '''The customer's gender.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-gender
            '''
            result = self._values.get("gender")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def home_phone_number(self) -> typing.Optional[builtins.str]:
            '''The customer's mobile phone number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-homephonenumber
            '''
            result = self._values.get("home_phone_number")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def last_name(self) -> typing.Optional[builtins.str]:
            '''The customer's last name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-lastname
            '''
            result = self._values.get("last_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mailing_address1(self) -> typing.Optional[builtins.str]:
            '''The first line of a customer’s mailing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress1
            '''
            result = self._values.get("mailing_address1")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mailing_address2(self) -> typing.Optional[builtins.str]:
            '''The second line of a customer’s mailing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress2
            '''
            result = self._values.get("mailing_address2")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mailing_address3(self) -> typing.Optional[builtins.str]:
            '''The third line of a customer’s mailing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress3
            '''
            result = self._values.get("mailing_address3")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mailing_address4(self) -> typing.Optional[builtins.str]:
            '''The fourth line of a customer’s mailing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-mailingaddress4
            '''
            result = self._values.get("mailing_address4")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mailing_city(self) -> typing.Optional[builtins.str]:
            '''The city of a customer’s mailing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-mailingcity
            '''
            result = self._values.get("mailing_city")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mailing_country(self) -> typing.Optional[builtins.str]:
            '''The country of a customer’s mailing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-mailingcountry
            '''
            result = self._values.get("mailing_country")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mailing_county(self) -> typing.Optional[builtins.str]:
            '''The county of a customer’s mailing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-mailingcounty
            '''
            result = self._values.get("mailing_county")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mailing_postal_code(self) -> typing.Optional[builtins.str]:
            '''The postal code of a customer’s mailing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-mailingpostalcode
            '''
            result = self._values.get("mailing_postal_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mailing_province(self) -> typing.Optional[builtins.str]:
            '''The province of a customer’s mailing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-mailingprovince
            '''
            result = self._values.get("mailing_province")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mailing_state(self) -> typing.Optional[builtins.str]:
            '''The state of a customer’s mailing address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-mailingstate
            '''
            result = self._values.get("mailing_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def middle_name(self) -> typing.Optional[builtins.str]:
            '''The customer's middle name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-middlename
            '''
            result = self._values.get("middle_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mobile_phone_number(self) -> typing.Optional[builtins.str]:
            '''The customer's mobile phone number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-mobilephonenumber
            '''
            result = self._values.get("mobile_phone_number")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def party_type(self) -> typing.Optional[builtins.str]:
            '''The customer's party type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-partytype
            '''
            result = self._values.get("party_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def phone_number(self) -> typing.Optional[builtins.str]:
            '''The customer's phone number, which has not been specified as a mobile, home, or business number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-phonenumber
            '''
            result = self._values.get("phone_number")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def postal_code(self) -> typing.Optional[builtins.str]:
            '''The postal code of a customer address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-postalcode
            '''
            result = self._values.get("postal_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def profile_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of a customer profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-profilearn
            '''
            result = self._values.get("profile_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def profile_id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of a customer profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-profileid
            '''
            result = self._values.get("profile_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def province(self) -> typing.Optional[builtins.str]:
            '''The province in which a customer lives.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-province
            '''
            result = self._values.get("province")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def shipping_address1(self) -> typing.Optional[builtins.str]:
            '''The first line of a customer’s shipping address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress1
            '''
            result = self._values.get("shipping_address1")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def shipping_address2(self) -> typing.Optional[builtins.str]:
            '''The second line of a customer’s shipping address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress2
            '''
            result = self._values.get("shipping_address2")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def shipping_address3(self) -> typing.Optional[builtins.str]:
            '''The third line of a customer’s shipping address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress3
            '''
            result = self._values.get("shipping_address3")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def shipping_address4(self) -> typing.Optional[builtins.str]:
            '''The fourth line of a customer’s shipping address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-shippingaddress4
            '''
            result = self._values.get("shipping_address4")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def shipping_city(self) -> typing.Optional[builtins.str]:
            '''The city of a customer’s shipping address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-shippingcity
            '''
            result = self._values.get("shipping_city")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def shipping_country(self) -> typing.Optional[builtins.str]:
            '''The country of a customer’s shipping address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-shippingcountry
            '''
            result = self._values.get("shipping_country")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def shipping_county(self) -> typing.Optional[builtins.str]:
            '''The county of a customer’s shipping address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-shippingcounty
            '''
            result = self._values.get("shipping_county")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def shipping_postal_code(self) -> typing.Optional[builtins.str]:
            '''The postal code of a customer’s shipping address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-shippingpostalcode
            '''
            result = self._values.get("shipping_postal_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def shipping_province(self) -> typing.Optional[builtins.str]:
            '''The province of a customer’s shipping address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-shippingprovince
            '''
            result = self._values.get("shipping_province")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def shipping_state(self) -> typing.Optional[builtins.str]:
            '''The state of a customer’s shipping address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-shippingstate
            '''
            result = self._values.get("shipping_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''The state in which a customer lives.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-customerprofileattributes.html#cfn-wisdom-messagetemplate-customerprofileattributes-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomerProfileAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplate.EmailMessageTemplateContentBodyProperty",
        jsii_struct_bases=[],
        name_mapping={"html": "html", "plain_text": "plainText"},
    )
    class EmailMessageTemplateContentBodyProperty:
        def __init__(
            self,
            *,
            html: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.MessageTemplateBodyContentProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            plain_text: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.MessageTemplateBodyContentProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The body to use in email messages.

            :param html: The message body, in HTML format, to use in email messages that are based on the message template. We recommend using HTML format for email clients that render HTML content. You can include links, formatted text, and more in an HTML message.
            :param plain_text: The message body, in plain text format, to use in email messages that are based on the message template. We recommend using plain text format for email clients that don't render HTML content and clients that are connected to high-latency networks, such as mobile devices.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-emailmessagetemplatecontentbody.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                email_message_template_content_body_property = wisdom.CfnMessageTemplate.EmailMessageTemplateContentBodyProperty(
                    html=wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                        content="content"
                    ),
                    plain_text=wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                        content="content"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__594c1bc5995ee95767b5cc83468d73e0803b33cd404adbe242bdf2932351cf22)
                check_type(argname="argument html", value=html, expected_type=type_hints["html"])
                check_type(argname="argument plain_text", value=plain_text, expected_type=type_hints["plain_text"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if html is not None:
                self._values["html"] = html
            if plain_text is not None:
                self._values["plain_text"] = plain_text

        @builtins.property
        def html(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.MessageTemplateBodyContentProviderProperty"]]:
            '''The message body, in HTML format, to use in email messages that are based on the message template.

            We recommend using HTML format for email clients that render HTML content. You can include links, formatted text, and more in an HTML message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-emailmessagetemplatecontentbody.html#cfn-wisdom-messagetemplate-emailmessagetemplatecontentbody-html
            '''
            result = self._values.get("html")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.MessageTemplateBodyContentProviderProperty"]], result)

        @builtins.property
        def plain_text(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.MessageTemplateBodyContentProviderProperty"]]:
            '''The message body, in plain text format, to use in email messages that are based on the message template.

            We recommend using plain text format for email clients that don't render HTML content and clients that are connected to high-latency networks, such as mobile devices.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-emailmessagetemplatecontentbody.html#cfn-wisdom-messagetemplate-emailmessagetemplatecontentbody-plaintext
            '''
            result = self._values.get("plain_text")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.MessageTemplateBodyContentProviderProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmailMessageTemplateContentBodyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplate.EmailMessageTemplateContentProperty",
        jsii_struct_bases=[],
        name_mapping={"body": "body", "headers": "headers", "subject": "subject"},
    )
    class EmailMessageTemplateContentProperty:
        def __init__(
            self,
            *,
            body: typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.EmailMessageTemplateContentBodyProperty", typing.Dict[builtins.str, typing.Any]]],
            headers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.EmailMessageTemplateHeaderProperty", typing.Dict[builtins.str, typing.Any]]]]],
            subject: builtins.str,
        ) -> None:
            '''The content of the message template that applies to the email channel subtype.

            :param body: The body to use in email messages.
            :param headers: The email headers to include in email messages.
            :param subject: The subject line, or title, to use in email messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-emailmessagetemplatecontent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                email_message_template_content_property = wisdom.CfnMessageTemplate.EmailMessageTemplateContentProperty(
                    body=wisdom.CfnMessageTemplate.EmailMessageTemplateContentBodyProperty(
                        html=wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                            content="content"
                        ),
                        plain_text=wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                            content="content"
                        )
                    ),
                    headers=[wisdom.CfnMessageTemplate.EmailMessageTemplateHeaderProperty(
                        name="name",
                        value="value"
                    )],
                    subject="subject"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a7215403540c347569227a7338deac451582c85e88a78a4272e4cd57567766c7)
                check_type(argname="argument body", value=body, expected_type=type_hints["body"])
                check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
                check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "body": body,
                "headers": headers,
                "subject": subject,
            }

        @builtins.property
        def body(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.EmailMessageTemplateContentBodyProperty"]:
            '''The body to use in email messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-emailmessagetemplatecontent.html#cfn-wisdom-messagetemplate-emailmessagetemplatecontent-body
            '''
            result = self._values.get("body")
            assert result is not None, "Required property 'body' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.EmailMessageTemplateContentBodyProperty"], result)

        @builtins.property
        def headers(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.EmailMessageTemplateHeaderProperty"]]]:
            '''The email headers to include in email messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-emailmessagetemplatecontent.html#cfn-wisdom-messagetemplate-emailmessagetemplatecontent-headers
            '''
            result = self._values.get("headers")
            assert result is not None, "Required property 'headers' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.EmailMessageTemplateHeaderProperty"]]], result)

        @builtins.property
        def subject(self) -> builtins.str:
            '''The subject line, or title, to use in email messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-emailmessagetemplatecontent.html#cfn-wisdom-messagetemplate-emailmessagetemplatecontent-subject
            '''
            result = self._values.get("subject")
            assert result is not None, "Required property 'subject' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmailMessageTemplateContentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplate.EmailMessageTemplateHeaderProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class EmailMessageTemplateHeaderProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The email headers to include in email messages.

            :param name: The name of the email header.
            :param value: The value of the email header.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-emailmessagetemplateheader.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                email_message_template_header_property = wisdom.CfnMessageTemplate.EmailMessageTemplateHeaderProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__13ed2a2205dc124617ee1edcae036a820325172941596023510196fe54baf556)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the email header.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-emailmessagetemplateheader.html#cfn-wisdom-messagetemplate-emailmessagetemplateheader-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the email header.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-emailmessagetemplateheader.html#cfn-wisdom-messagetemplate-emailmessagetemplateheader-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmailMessageTemplateHeaderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplate.GroupingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"criteria": "criteria", "values": "values"},
    )
    class GroupingConfigurationProperty:
        def __init__(
            self,
            *,
            criteria: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''The configuration information of the grouping of Amazon Q in Connect users.

            :param criteria: The criteria used for grouping Amazon Q in Connect users. The following is the list of supported criteria values. - ``RoutingProfileArn`` : Grouping the users by their `Amazon Connect routing profile ARN <https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html>`_ . User should have `SearchRoutingProfile <https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchRoutingProfiles.html>`_ and `DescribeRoutingProfile <https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRoutingProfile.html>`_ permissions when setting criteria to this value.
            :param values: The list of values that define different groups of Amazon Q in Connect users. - When setting ``criteria`` to ``RoutingProfileArn`` , you need to provide a list of ARNs of `Amazon Connect routing profiles <https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html>`_ as values of this parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-groupingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                grouping_configuration_property = wisdom.CfnMessageTemplate.GroupingConfigurationProperty(
                    criteria="criteria",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fe8ac046ae2df337296b1f5a22706eb034910def9d9a88cab8bf76dbc739dd08)
                check_type(argname="argument criteria", value=criteria, expected_type=type_hints["criteria"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "criteria": criteria,
                "values": values,
            }

        @builtins.property
        def criteria(self) -> builtins.str:
            '''The criteria used for grouping Amazon Q in Connect users.

            The following is the list of supported criteria values.

            - ``RoutingProfileArn`` : Grouping the users by their `Amazon Connect routing profile ARN <https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html>`_ . User should have `SearchRoutingProfile <https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchRoutingProfiles.html>`_ and `DescribeRoutingProfile <https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRoutingProfile.html>`_ permissions when setting criteria to this value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-groupingconfiguration.html#cfn-wisdom-messagetemplate-groupingconfiguration-criteria
            '''
            result = self._values.get("criteria")
            assert result is not None, "Required property 'criteria' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''The list of values that define different groups of Amazon Q in Connect users.

            - When setting ``criteria`` to ``RoutingProfileArn`` , you need to provide a list of ARNs of `Amazon Connect routing profiles <https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html>`_ as values of this parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-groupingconfiguration.html#cfn-wisdom-messagetemplate-groupingconfiguration-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GroupingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplate.MessageTemplateAttachmentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attachment_name": "attachmentName",
            "s3_presigned_url": "s3PresignedUrl",
            "attachment_id": "attachmentId",
        },
    )
    class MessageTemplateAttachmentProperty:
        def __init__(
            self,
            *,
            attachment_name: builtins.str,
            s3_presigned_url: builtins.str,
            attachment_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the message template attachment.

            :param attachment_name: The name of the attachment file being uploaded. The name should include the file extension.
            :param s3_presigned_url: The S3 Presigned URL for the attachment file. When generating the PreSignedUrl, please ensure that the expires-in time is set to 30 minutes. The URL can be generated through the AWS Console or through the AWS CLI. For more information, see `Sharing objects with presigned URLs <https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html>`_ .
            :param attachment_id: The identifier of the attachment file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-messagetemplateattachment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                message_template_attachment_property = wisdom.CfnMessageTemplate.MessageTemplateAttachmentProperty(
                    attachment_name="attachmentName",
                    s3_presigned_url="s3PresignedUrl",
                
                    # the properties below are optional
                    attachment_id="attachmentId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__733b704f810bd9a3eb9d75f4f3b82b249fd0f3b3c3429da2875584133affc320)
                check_type(argname="argument attachment_name", value=attachment_name, expected_type=type_hints["attachment_name"])
                check_type(argname="argument s3_presigned_url", value=s3_presigned_url, expected_type=type_hints["s3_presigned_url"])
                check_type(argname="argument attachment_id", value=attachment_id, expected_type=type_hints["attachment_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attachment_name": attachment_name,
                "s3_presigned_url": s3_presigned_url,
            }
            if attachment_id is not None:
                self._values["attachment_id"] = attachment_id

        @builtins.property
        def attachment_name(self) -> builtins.str:
            '''The name of the attachment file being uploaded.

            The name should include the file extension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-messagetemplateattachment.html#cfn-wisdom-messagetemplate-messagetemplateattachment-attachmentname
            '''
            result = self._values.get("attachment_name")
            assert result is not None, "Required property 'attachment_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_presigned_url(self) -> builtins.str:
            '''The S3 Presigned URL for the attachment file.

            When generating the PreSignedUrl, please ensure that the expires-in time is set to 30 minutes. The URL can be generated through the AWS Console or through the AWS CLI. For more information, see `Sharing objects with presigned URLs <https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-messagetemplateattachment.html#cfn-wisdom-messagetemplate-messagetemplateattachment-s3presignedurl
            '''
            result = self._values.get("s3_presigned_url")
            assert result is not None, "Required property 's3_presigned_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attachment_id(self) -> typing.Optional[builtins.str]:
            '''The identifier of the attachment file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-messagetemplateattachment.html#cfn-wisdom-messagetemplate-messagetemplateattachment-attachmentid
            '''
            result = self._values.get("attachment_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MessageTemplateAttachmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplate.MessageTemplateAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "agent_attributes": "agentAttributes",
            "custom_attributes": "customAttributes",
            "customer_profile_attributes": "customerProfileAttributes",
            "system_attributes": "systemAttributes",
        },
    )
    class MessageTemplateAttributesProperty:
        def __init__(
            self,
            *,
            agent_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.AgentAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            custom_attributes: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            customer_profile_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.CustomerProfileAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            system_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.SystemAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The attributes that are used with the message template.

            :param agent_attributes: The agent attributes that are used with the message template.
            :param custom_attributes: The custom attributes that are used with the message template.
            :param customer_profile_attributes: The customer profile attributes that are used with the message template.
            :param system_attributes: The system attributes that are used with the message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-messagetemplateattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                message_template_attributes_property = wisdom.CfnMessageTemplate.MessageTemplateAttributesProperty(
                    agent_attributes=wisdom.CfnMessageTemplate.AgentAttributesProperty(
                        first_name="firstName",
                        last_name="lastName"
                    ),
                    custom_attributes={
                        "custom_attributes_key": "customAttributes"
                    },
                    customer_profile_attributes=wisdom.CfnMessageTemplate.CustomerProfileAttributesProperty(
                        account_number="accountNumber",
                        additional_information="additionalInformation",
                        address1="address1",
                        address2="address2",
                        address3="address3",
                        address4="address4",
                        billing_address1="billingAddress1",
                        billing_address2="billingAddress2",
                        billing_address3="billingAddress3",
                        billing_address4="billingAddress4",
                        billing_city="billingCity",
                        billing_country="billingCountry",
                        billing_county="billingCounty",
                        billing_postal_code="billingPostalCode",
                        billing_province="billingProvince",
                        billing_state="billingState",
                        birth_date="birthDate",
                        business_email_address="businessEmailAddress",
                        business_name="businessName",
                        business_phone_number="businessPhoneNumber",
                        city="city",
                        country="country",
                        county="county",
                        custom={
                            "custom_key": "custom"
                        },
                        email_address="emailAddress",
                        first_name="firstName",
                        gender="gender",
                        home_phone_number="homePhoneNumber",
                        last_name="lastName",
                        mailing_address1="mailingAddress1",
                        mailing_address2="mailingAddress2",
                        mailing_address3="mailingAddress3",
                        mailing_address4="mailingAddress4",
                        mailing_city="mailingCity",
                        mailing_country="mailingCountry",
                        mailing_county="mailingCounty",
                        mailing_postal_code="mailingPostalCode",
                        mailing_province="mailingProvince",
                        mailing_state="mailingState",
                        middle_name="middleName",
                        mobile_phone_number="mobilePhoneNumber",
                        party_type="partyType",
                        phone_number="phoneNumber",
                        postal_code="postalCode",
                        profile_arn="profileArn",
                        profile_id="profileId",
                        province="province",
                        shipping_address1="shippingAddress1",
                        shipping_address2="shippingAddress2",
                        shipping_address3="shippingAddress3",
                        shipping_address4="shippingAddress4",
                        shipping_city="shippingCity",
                        shipping_country="shippingCountry",
                        shipping_county="shippingCounty",
                        shipping_postal_code="shippingPostalCode",
                        shipping_province="shippingProvince",
                        shipping_state="shippingState",
                        state="state"
                    ),
                    system_attributes=wisdom.CfnMessageTemplate.SystemAttributesProperty(
                        customer_endpoint=wisdom.CfnMessageTemplate.SystemEndpointAttributesProperty(
                            address="address"
                        ),
                        name="name",
                        system_endpoint=wisdom.CfnMessageTemplate.SystemEndpointAttributesProperty(
                            address="address"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__94be2b3e247d65fdf9ede2a9ef720965133047f24bfea2e9cda8dddc0b98feb1)
                check_type(argname="argument agent_attributes", value=agent_attributes, expected_type=type_hints["agent_attributes"])
                check_type(argname="argument custom_attributes", value=custom_attributes, expected_type=type_hints["custom_attributes"])
                check_type(argname="argument customer_profile_attributes", value=customer_profile_attributes, expected_type=type_hints["customer_profile_attributes"])
                check_type(argname="argument system_attributes", value=system_attributes, expected_type=type_hints["system_attributes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if agent_attributes is not None:
                self._values["agent_attributes"] = agent_attributes
            if custom_attributes is not None:
                self._values["custom_attributes"] = custom_attributes
            if customer_profile_attributes is not None:
                self._values["customer_profile_attributes"] = customer_profile_attributes
            if system_attributes is not None:
                self._values["system_attributes"] = system_attributes

        @builtins.property
        def agent_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.AgentAttributesProperty"]]:
            '''The agent attributes that are used with the message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-messagetemplateattributes.html#cfn-wisdom-messagetemplate-messagetemplateattributes-agentattributes
            '''
            result = self._values.get("agent_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.AgentAttributesProperty"]], result)

        @builtins.property
        def custom_attributes(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The custom attributes that are used with the message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-messagetemplateattributes.html#cfn-wisdom-messagetemplate-messagetemplateattributes-customattributes
            '''
            result = self._values.get("custom_attributes")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def customer_profile_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.CustomerProfileAttributesProperty"]]:
            '''The customer profile attributes that are used with the message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-messagetemplateattributes.html#cfn-wisdom-messagetemplate-messagetemplateattributes-customerprofileattributes
            '''
            result = self._values.get("customer_profile_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.CustomerProfileAttributesProperty"]], result)

        @builtins.property
        def system_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.SystemAttributesProperty"]]:
            '''The system attributes that are used with the message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-messagetemplateattributes.html#cfn-wisdom-messagetemplate-messagetemplateattributes-systemattributes
            '''
            result = self._values.get("system_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.SystemAttributesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MessageTemplateAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty",
        jsii_struct_bases=[],
        name_mapping={"content": "content"},
    )
    class MessageTemplateBodyContentProviderProperty:
        def __init__(self, *, content: typing.Optional[builtins.str] = None) -> None:
            '''The container of the message template body.

            :param content: The content of the message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-messagetemplatebodycontentprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                message_template_body_content_provider_property = wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                    content="content"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__91e161e5190bc28f3ba5b1a8df2e1101ff4f45bfe209c74195160cd328f28814)
                check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if content is not None:
                self._values["content"] = content

        @builtins.property
        def content(self) -> typing.Optional[builtins.str]:
            '''The content of the message template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-messagetemplatebodycontentprovider.html#cfn-wisdom-messagetemplate-messagetemplatebodycontentprovider-content
            '''
            result = self._values.get("content")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MessageTemplateBodyContentProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplate.SmsMessageTemplateContentBodyProperty",
        jsii_struct_bases=[],
        name_mapping={"plain_text": "plainText"},
    )
    class SmsMessageTemplateContentBodyProperty:
        def __init__(
            self,
            *,
            plain_text: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.MessageTemplateBodyContentProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The body to use in SMS messages.

            :param plain_text: The message body to use in SMS messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-smsmessagetemplatecontentbody.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                sms_message_template_content_body_property = wisdom.CfnMessageTemplate.SmsMessageTemplateContentBodyProperty(
                    plain_text=wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                        content="content"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b9ffc2cd4d7675f6b77015f221bf2163943c73ed8bc184e5c43f47d33dc83715)
                check_type(argname="argument plain_text", value=plain_text, expected_type=type_hints["plain_text"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if plain_text is not None:
                self._values["plain_text"] = plain_text

        @builtins.property
        def plain_text(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.MessageTemplateBodyContentProviderProperty"]]:
            '''The message body to use in SMS messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-smsmessagetemplatecontentbody.html#cfn-wisdom-messagetemplate-smsmessagetemplatecontentbody-plaintext
            '''
            result = self._values.get("plain_text")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.MessageTemplateBodyContentProviderProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SmsMessageTemplateContentBodyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplate.SmsMessageTemplateContentProperty",
        jsii_struct_bases=[],
        name_mapping={"body": "body"},
    )
    class SmsMessageTemplateContentProperty:
        def __init__(
            self,
            *,
            body: typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.SmsMessageTemplateContentBodyProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The content of the message template that applies to the SMS channel subtype.

            :param body: The body to use in SMS messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-smsmessagetemplatecontent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                sms_message_template_content_property = wisdom.CfnMessageTemplate.SmsMessageTemplateContentProperty(
                    body=wisdom.CfnMessageTemplate.SmsMessageTemplateContentBodyProperty(
                        plain_text=wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                            content="content"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5996259411eb96bb9d7a8aaecb5f716307ce93390a851bca361b510ec852f0e3)
                check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "body": body,
            }

        @builtins.property
        def body(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.SmsMessageTemplateContentBodyProperty"]:
            '''The body to use in SMS messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-smsmessagetemplatecontent.html#cfn-wisdom-messagetemplate-smsmessagetemplatecontent-body
            '''
            result = self._values.get("body")
            assert result is not None, "Required property 'body' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.SmsMessageTemplateContentBodyProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SmsMessageTemplateContentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplate.SystemAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "customer_endpoint": "customerEndpoint",
            "name": "name",
            "system_endpoint": "systemEndpoint",
        },
    )
    class SystemAttributesProperty:
        def __init__(
            self,
            *,
            customer_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.SystemEndpointAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            name: typing.Optional[builtins.str] = None,
            system_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMessageTemplate.SystemEndpointAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The system attributes that are used with the message template.

            :param customer_endpoint: The CustomerEndpoint attribute.
            :param name: The name of the task.
            :param system_endpoint: The SystemEndpoint attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-systemattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                system_attributes_property = wisdom.CfnMessageTemplate.SystemAttributesProperty(
                    customer_endpoint=wisdom.CfnMessageTemplate.SystemEndpointAttributesProperty(
                        address="address"
                    ),
                    name="name",
                    system_endpoint=wisdom.CfnMessageTemplate.SystemEndpointAttributesProperty(
                        address="address"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bd590492f1b15737eb4d99b87e845ae5b578516dd6a202c1c00f10d883c4606f)
                check_type(argname="argument customer_endpoint", value=customer_endpoint, expected_type=type_hints["customer_endpoint"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument system_endpoint", value=system_endpoint, expected_type=type_hints["system_endpoint"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if customer_endpoint is not None:
                self._values["customer_endpoint"] = customer_endpoint
            if name is not None:
                self._values["name"] = name
            if system_endpoint is not None:
                self._values["system_endpoint"] = system_endpoint

        @builtins.property
        def customer_endpoint(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.SystemEndpointAttributesProperty"]]:
            '''The CustomerEndpoint attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-systemattributes.html#cfn-wisdom-messagetemplate-systemattributes-customerendpoint
            '''
            result = self._values.get("customer_endpoint")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.SystemEndpointAttributesProperty"]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-systemattributes.html#cfn-wisdom-messagetemplate-systemattributes-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def system_endpoint(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.SystemEndpointAttributesProperty"]]:
            '''The SystemEndpoint attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-systemattributes.html#cfn-wisdom-messagetemplate-systemattributes-systemendpoint
            '''
            result = self._values.get("system_endpoint")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMessageTemplate.SystemEndpointAttributesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SystemAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplate.SystemEndpointAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"address": "address"},
    )
    class SystemEndpointAttributesProperty:
        def __init__(self, *, address: typing.Optional[builtins.str] = None) -> None:
            '''The system endpoint attributes that are used with the message template.

            :param address: The customer's phone number if used with ``customerEndpoint`` , or the number the customer dialed to call your contact center if used with ``systemEndpoint`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-systemendpointattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                system_endpoint_attributes_property = wisdom.CfnMessageTemplate.SystemEndpointAttributesProperty(
                    address="address"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a331097c8b523e827ded8e1b2307d25adea67abd59cd8f02120521fb1bcec13e)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address

        @builtins.property
        def address(self) -> typing.Optional[builtins.str]:
            '''The customer's phone number if used with ``customerEndpoint`` , or the number the customer dialed to call your contact center if used with ``systemEndpoint`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-messagetemplate-systemendpointattributes.html#cfn-wisdom-messagetemplate-systemendpointattributes-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SystemEndpointAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_subtype": "channelSubtype",
        "content": "content",
        "knowledge_base_arn": "knowledgeBaseArn",
        "name": "name",
        "default_attributes": "defaultAttributes",
        "description": "description",
        "grouping_configuration": "groupingConfiguration",
        "language": "language",
        "message_template_attachments": "messageTemplateAttachments",
        "tags": "tags",
    },
)
class CfnMessageTemplateProps:
    def __init__(
        self,
        *,
        channel_subtype: builtins.str,
        content: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.ContentProperty, typing.Dict[builtins.str, typing.Any]]],
        knowledge_base_arn: builtins.str,
        name: builtins.str,
        default_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.MessageTemplateAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        grouping_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.GroupingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        language: typing.Optional[builtins.str] = None,
        message_template_attachments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.MessageTemplateAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMessageTemplate``.

        :param channel_subtype: The channel subtype this message template applies to.
        :param content: The content of the message template.
        :param knowledge_base_arn: The Amazon Resource Name (ARN) of the knowledge base.
        :param name: The name of the message template.
        :param default_attributes: An object that specifies the default values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.
        :param description: The description of the message template.
        :param grouping_configuration: The configuration information of the external data source.
        :param language: The language code value for the language in which the quick response is written. The supported language codes include ``de_DE`` , ``en_US`` , ``es_ES`` , ``fr_FR`` , ``id_ID`` , ``it_IT`` , ``ja_JP`` , ``ko_KR`` , ``pt_BR`` , ``zh_CN`` , ``zh_TW``
        :param message_template_attachments: List of message template attachments.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_message_template_props = wisdom.CfnMessageTemplateProps(
                channel_subtype="channelSubtype",
                content=wisdom.CfnMessageTemplate.ContentProperty(
                    email_message_template_content=wisdom.CfnMessageTemplate.EmailMessageTemplateContentProperty(
                        body=wisdom.CfnMessageTemplate.EmailMessageTemplateContentBodyProperty(
                            html=wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                                content="content"
                            ),
                            plain_text=wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                                content="content"
                            )
                        ),
                        headers=[wisdom.CfnMessageTemplate.EmailMessageTemplateHeaderProperty(
                            name="name",
                            value="value"
                        )],
                        subject="subject"
                    ),
                    sms_message_template_content=wisdom.CfnMessageTemplate.SmsMessageTemplateContentProperty(
                        body=wisdom.CfnMessageTemplate.SmsMessageTemplateContentBodyProperty(
                            plain_text=wisdom.CfnMessageTemplate.MessageTemplateBodyContentProviderProperty(
                                content="content"
                            )
                        )
                    )
                ),
                knowledge_base_arn="knowledgeBaseArn",
                name="name",
            
                # the properties below are optional
                default_attributes=wisdom.CfnMessageTemplate.MessageTemplateAttributesProperty(
                    agent_attributes=wisdom.CfnMessageTemplate.AgentAttributesProperty(
                        first_name="firstName",
                        last_name="lastName"
                    ),
                    custom_attributes={
                        "custom_attributes_key": "customAttributes"
                    },
                    customer_profile_attributes=wisdom.CfnMessageTemplate.CustomerProfileAttributesProperty(
                        account_number="accountNumber",
                        additional_information="additionalInformation",
                        address1="address1",
                        address2="address2",
                        address3="address3",
                        address4="address4",
                        billing_address1="billingAddress1",
                        billing_address2="billingAddress2",
                        billing_address3="billingAddress3",
                        billing_address4="billingAddress4",
                        billing_city="billingCity",
                        billing_country="billingCountry",
                        billing_county="billingCounty",
                        billing_postal_code="billingPostalCode",
                        billing_province="billingProvince",
                        billing_state="billingState",
                        birth_date="birthDate",
                        business_email_address="businessEmailAddress",
                        business_name="businessName",
                        business_phone_number="businessPhoneNumber",
                        city="city",
                        country="country",
                        county="county",
                        custom={
                            "custom_key": "custom"
                        },
                        email_address="emailAddress",
                        first_name="firstName",
                        gender="gender",
                        home_phone_number="homePhoneNumber",
                        last_name="lastName",
                        mailing_address1="mailingAddress1",
                        mailing_address2="mailingAddress2",
                        mailing_address3="mailingAddress3",
                        mailing_address4="mailingAddress4",
                        mailing_city="mailingCity",
                        mailing_country="mailingCountry",
                        mailing_county="mailingCounty",
                        mailing_postal_code="mailingPostalCode",
                        mailing_province="mailingProvince",
                        mailing_state="mailingState",
                        middle_name="middleName",
                        mobile_phone_number="mobilePhoneNumber",
                        party_type="partyType",
                        phone_number="phoneNumber",
                        postal_code="postalCode",
                        profile_arn="profileArn",
                        profile_id="profileId",
                        province="province",
                        shipping_address1="shippingAddress1",
                        shipping_address2="shippingAddress2",
                        shipping_address3="shippingAddress3",
                        shipping_address4="shippingAddress4",
                        shipping_city="shippingCity",
                        shipping_country="shippingCountry",
                        shipping_county="shippingCounty",
                        shipping_postal_code="shippingPostalCode",
                        shipping_province="shippingProvince",
                        shipping_state="shippingState",
                        state="state"
                    ),
                    system_attributes=wisdom.CfnMessageTemplate.SystemAttributesProperty(
                        customer_endpoint=wisdom.CfnMessageTemplate.SystemEndpointAttributesProperty(
                            address="address"
                        ),
                        name="name",
                        system_endpoint=wisdom.CfnMessageTemplate.SystemEndpointAttributesProperty(
                            address="address"
                        )
                    )
                ),
                description="description",
                grouping_configuration=wisdom.CfnMessageTemplate.GroupingConfigurationProperty(
                    criteria="criteria",
                    values=["values"]
                ),
                language="language",
                message_template_attachments=[wisdom.CfnMessageTemplate.MessageTemplateAttachmentProperty(
                    attachment_name="attachmentName",
                    s3_presigned_url="s3PresignedUrl",
            
                    # the properties below are optional
                    attachment_id="attachmentId"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec25e0f87d8fdbd9dfa333317dee4b1a02318078d19b7a6a2b5abe02825ec475)
            check_type(argname="argument channel_subtype", value=channel_subtype, expected_type=type_hints["channel_subtype"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument knowledge_base_arn", value=knowledge_base_arn, expected_type=type_hints["knowledge_base_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument default_attributes", value=default_attributes, expected_type=type_hints["default_attributes"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument grouping_configuration", value=grouping_configuration, expected_type=type_hints["grouping_configuration"])
            check_type(argname="argument language", value=language, expected_type=type_hints["language"])
            check_type(argname="argument message_template_attachments", value=message_template_attachments, expected_type=type_hints["message_template_attachments"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_subtype": channel_subtype,
            "content": content,
            "knowledge_base_arn": knowledge_base_arn,
            "name": name,
        }
        if default_attributes is not None:
            self._values["default_attributes"] = default_attributes
        if description is not None:
            self._values["description"] = description
        if grouping_configuration is not None:
            self._values["grouping_configuration"] = grouping_configuration
        if language is not None:
            self._values["language"] = language
        if message_template_attachments is not None:
            self._values["message_template_attachments"] = message_template_attachments
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def channel_subtype(self) -> builtins.str:
        '''The channel subtype this message template applies to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplate.html#cfn-wisdom-messagetemplate-channelsubtype
        '''
        result = self._values.get("channel_subtype")
        assert result is not None, "Required property 'channel_subtype' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnMessageTemplate.ContentProperty]:
        '''The content of the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplate.html#cfn-wisdom-messagetemplate-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnMessageTemplate.ContentProperty], result)

    @builtins.property
    def knowledge_base_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the knowledge base.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplate.html#cfn-wisdom-messagetemplate-knowledgebasearn
        '''
        result = self._values.get("knowledge_base_arn")
        assert result is not None, "Required property 'knowledge_base_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplate.html#cfn-wisdom-messagetemplate-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMessageTemplate.MessageTemplateAttributesProperty]]:
        '''An object that specifies the default values to use for variables in the message template.

        This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplate.html#cfn-wisdom-messagetemplate-defaultattributes
        '''
        result = self._values.get("default_attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMessageTemplate.MessageTemplateAttributesProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplate.html#cfn-wisdom-messagetemplate-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grouping_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMessageTemplate.GroupingConfigurationProperty]]:
        '''The configuration information of the external data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplate.html#cfn-wisdom-messagetemplate-groupingconfiguration
        '''
        result = self._values.get("grouping_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMessageTemplate.GroupingConfigurationProperty]], result)

    @builtins.property
    def language(self) -> typing.Optional[builtins.str]:
        '''The language code value for the language in which the quick response is written.

        The supported language codes include ``de_DE`` , ``en_US`` , ``es_ES`` , ``fr_FR`` , ``id_ID`` , ``it_IT`` , ``ja_JP`` , ``ko_KR`` , ``pt_BR`` , ``zh_CN`` , ``zh_TW``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplate.html#cfn-wisdom-messagetemplate-language
        '''
        result = self._values.get("language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message_template_attachments(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMessageTemplate.MessageTemplateAttachmentProperty]]]]:
        '''List of message template attachments.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplate.html#cfn-wisdom-messagetemplate-messagetemplateattachments
        '''
        result = self._values.get("message_template_attachments")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMessageTemplate.MessageTemplateAttachmentProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplate.html#cfn-wisdom-messagetemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMessageTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnMessageTemplateVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplateVersion",
):
    '''Creates a new Amazon Q in Connect message template version from the current content and configuration of a message template.

    Versions are immutable and monotonically increasing. Once a version is created, you can reference a specific version of the message template by passing in ``<messageTemplateArn>:<versionNumber>`` as the message template identifier. An error is displayed if the supplied ``messageTemplateContentSha256`` is different from the ``messageTemplateContentSha256`` of the message template with ``$LATEST`` qualifier. If multiple ``CreateMessageTemplateVersion`` requests are made while the message template remains the same, only the first invocation creates a new version and the succeeding requests will return the same response as the first invocation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplateversion.html
    :cloudformationResource: AWS::Wisdom::MessageTemplateVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_message_template_version = wisdom.CfnMessageTemplateVersion(self, "MyCfnMessageTemplateVersion",
            message_template_arn="messageTemplateArn",
        
            # the properties below are optional
            message_template_content_sha256="messageTemplateContentSha256"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        message_template_arn: builtins.str,
        message_template_content_sha256: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param message_template_arn: The Amazon Resource Name (ARN) of the message template.
        :param message_template_content_sha256: The content SHA256 of the message template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74fb30e95cf0983e689b729ce7c37f315a3a89ee72eba30c0076157947593055)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMessageTemplateVersionProps(
            message_template_arn=message_template_arn,
            message_template_content_sha256=message_template_content_sha256,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fdcf0b0fc316f9964e2a8f50d95ef92efe9e07b4a9d5ef74b7c3ca6257dc206)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ac027a7bca9f313df16a3ac8bc0b9a8b1f796ce03d79d5eb49d64dd963e9c8c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrMessageTemplateVersionArn")
    def attr_message_template_version_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Message Template Version.

        :cloudformationAttribute: MessageTemplateVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMessageTemplateVersionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrMessageTemplateVersionNumber")
    def attr_message_template_version_number(self) -> _IResolvable_da3f097b:
        '''The version number for this Message Template Version.

        :cloudformationAttribute: MessageTemplateVersionNumber
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrMessageTemplateVersionNumber"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="messageTemplateArn")
    def message_template_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the message template.'''
        return typing.cast(builtins.str, jsii.get(self, "messageTemplateArn"))

    @message_template_arn.setter
    def message_template_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08418dbc91726be614a7891204fe619271f6618bccf8511f3e62a4f02edd6fb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageTemplateArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="messageTemplateContentSha256")
    def message_template_content_sha256(self) -> typing.Optional[builtins.str]:
        '''The content SHA256 of the message template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageTemplateContentSha256"))

    @message_template_content_sha256.setter
    def message_template_content_sha256(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2add34eec806e4ffcc1182689dc4344729a80e6faab1ee1e72aafe25168cddeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageTemplateContentSha256", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnMessageTemplateVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "message_template_arn": "messageTemplateArn",
        "message_template_content_sha256": "messageTemplateContentSha256",
    },
)
class CfnMessageTemplateVersionProps:
    def __init__(
        self,
        *,
        message_template_arn: builtins.str,
        message_template_content_sha256: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMessageTemplateVersion``.

        :param message_template_arn: The Amazon Resource Name (ARN) of the message template.
        :param message_template_content_sha256: The content SHA256 of the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplateversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_message_template_version_props = wisdom.CfnMessageTemplateVersionProps(
                message_template_arn="messageTemplateArn",
            
                # the properties below are optional
                message_template_content_sha256="messageTemplateContentSha256"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0b2a184adf6bc572d2575c7f11c4caa1ebc990936a7af469c6f91288d5f2908)
            check_type(argname="argument message_template_arn", value=message_template_arn, expected_type=type_hints["message_template_arn"])
            check_type(argname="argument message_template_content_sha256", value=message_template_content_sha256, expected_type=type_hints["message_template_content_sha256"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "message_template_arn": message_template_arn,
        }
        if message_template_content_sha256 is not None:
            self._values["message_template_content_sha256"] = message_template_content_sha256

    @builtins.property
    def message_template_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplateversion.html#cfn-wisdom-messagetemplateversion-messagetemplatearn
        '''
        result = self._values.get("message_template_arn")
        assert result is not None, "Required property 'message_template_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def message_template_content_sha256(self) -> typing.Optional[builtins.str]:
        '''The content SHA256 of the message template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplateversion.html#cfn-wisdom-messagetemplateversion-messagetemplatecontentsha256
        '''
        result = self._values.get("message_template_content_sha256")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMessageTemplateVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnQuickResponse(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnQuickResponse",
):
    '''Creates an Amazon Q in Connect quick response.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-quickresponse.html
    :cloudformationResource: AWS::Wisdom::QuickResponse
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_quick_response = wisdom.CfnQuickResponse(self, "MyCfnQuickResponse",
            content=wisdom.CfnQuickResponse.QuickResponseContentProviderProperty(
                content="content"
            ),
            knowledge_base_arn="knowledgeBaseArn",
            name="name",
        
            # the properties below are optional
            channels=["channels"],
            content_type="contentType",
            description="description",
            grouping_configuration=wisdom.CfnQuickResponse.GroupingConfigurationProperty(
                criteria="criteria",
                values=["values"]
            ),
            is_active=False,
            language="language",
            shortcut_key="shortcutKey",
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
        content: typing.Union[_IResolvable_da3f097b, typing.Union["CfnQuickResponse.QuickResponseContentProviderProperty", typing.Dict[builtins.str, typing.Any]]],
        knowledge_base_arn: builtins.str,
        name: builtins.str,
        channels: typing.Optional[typing.Sequence[builtins.str]] = None,
        content_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        grouping_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnQuickResponse.GroupingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        is_active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        language: typing.Optional[builtins.str] = None,
        shortcut_key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param content: The content of the quick response.
        :param knowledge_base_arn: The Amazon Resource Name (ARN) of the knowledge base.
        :param name: The name of the quick response.
        :param channels: The Amazon Connect contact channels this quick response applies to. The supported contact channel types include ``Chat`` .
        :param content_type: The media type of the quick response content. - Use ``application/x.quickresponse;format=plain`` for quick response written in plain text. - Use ``application/x.quickresponse;format=markdown`` for quick response written in richtext.
        :param description: The description of the quick response.
        :param grouping_configuration: The configuration information of the user groups that the quick response is accessible to.
        :param is_active: Whether the quick response is active.
        :param language: The language code value for the language in which the quick response is written. The supported language codes include ``de_DE`` , ``en_US`` , ``es_ES`` , ``fr_FR`` , ``id_ID`` , ``it_IT`` , ``ja_JP`` , ``ko_KR`` , ``pt_BR`` , ``zh_CN`` , ``zh_TW``
        :param shortcut_key: The shortcut key of the quick response. The value should be unique across the knowledge base.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ea732c0aa1c75214dd603b6887da6352fe66fd3d98e2168fdc3654ffd9d1629)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnQuickResponseProps(
            content=content,
            knowledge_base_arn=knowledge_base_arn,
            name=name,
            channels=channels,
            content_type=content_type,
            description=description,
            grouping_configuration=grouping_configuration,
            is_active=is_active,
            language=language,
            shortcut_key=shortcut_key,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d749875d4fcc7d4242bef84ff9a9085b8827dd339b292a8c0429c8dd8b8f394a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__55603fa5b935508baa2dfab5656797245339ea337e135b1dc21a3a68319e401a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrContents")
    def attr_contents(self) -> _IResolvable_da3f097b:
        '''The content of the quick response stored in different media types.

        :cloudformationAttribute: Contents
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrContents"))

    @builtins.property
    @jsii.member(jsii_name="attrQuickResponseArn")
    def attr_quick_response_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the quick response.

        :cloudformationAttribute: QuickResponseArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQuickResponseArn"))

    @builtins.property
    @jsii.member(jsii_name="attrQuickResponseId")
    def attr_quick_response_id(self) -> builtins.str:
        '''The identifier of the quick response.

        :cloudformationAttribute: QuickResponseId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQuickResponseId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the quick response data.

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
    @jsii.member(jsii_name="content")
    def content(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnQuickResponse.QuickResponseContentProviderProperty"]:
        '''The content of the quick response.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnQuickResponse.QuickResponseContentProviderProperty"], jsii.get(self, "content"))

    @content.setter
    def content(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnQuickResponse.QuickResponseContentProviderProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9dfed0b86363ddee2b73b59a4f8b9559cdd5914e6289f92f15feac8409c416b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="knowledgeBaseArn")
    def knowledge_base_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the knowledge base.'''
        return typing.cast(builtins.str, jsii.get(self, "knowledgeBaseArn"))

    @knowledge_base_arn.setter
    def knowledge_base_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2144e7491ad5d7946aab6f020cc3753c00cd404c7ff07340ab3cd7d070d37993)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "knowledgeBaseArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the quick response.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5165c48c2f03231e6cd852d113854e793302bd6e08d080e9cccd919f79e3565e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="channels")
    def channels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Connect contact channels this quick response applies to.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "channels"))

    @channels.setter
    def channels(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e83f69c01eda758c5d6ec662eb36e57ab3b0b525a49f25b680b666ab899f00be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channels", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> typing.Optional[builtins.str]:
        '''The media type of the quick response content.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6492a4d7ba49b236142344d0d0c57fc6ca8829e7d6ecf3259503a67f78948deb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the quick response.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7acfcd0f2c542ee39a59469bc0ea12f5507951f336da00fcd37146edb79dc73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="groupingConfiguration")
    def grouping_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQuickResponse.GroupingConfigurationProperty"]]:
        '''The configuration information of the user groups that the quick response is accessible to.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQuickResponse.GroupingConfigurationProperty"]], jsii.get(self, "groupingConfiguration"))

    @grouping_configuration.setter
    def grouping_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQuickResponse.GroupingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ec3f31a69e16fce2ffc00474e1f2852bd0e753c6a3e973b7255a9d4d7f64a45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupingConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="isActive")
    def is_active(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the quick response is active.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "isActive"))

    @is_active.setter
    def is_active(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d8198e1c8f2c5b8c3703976122f2d1b18fe79607316aa0a9b449b4cd01026e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isActive", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="language")
    def language(self) -> typing.Optional[builtins.str]:
        '''The language code value for the language in which the quick response is written.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "language"))

    @language.setter
    def language(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6278f29e4c31c723a6c5cf2bf58f08721883768d361fa4186d576bffdeb71902)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "language", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="shortcutKey")
    def shortcut_key(self) -> typing.Optional[builtins.str]:
        '''The shortcut key of the quick response.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortcutKey"))

    @shortcut_key.setter
    def shortcut_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a0dc9541d897c6f038624fe355ba3d2374e8c28f367a9049dd7553a8b466138)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shortcutKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2727d6beae8f791672bb80625961e3def8262f5b47864ede2817419f60527d6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnQuickResponse.GroupingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"criteria": "criteria", "values": "values"},
    )
    class GroupingConfigurationProperty:
        def __init__(
            self,
            *,
            criteria: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''The configuration information of the grouping of Amazon Q in Connect users.

            :param criteria: The criteria used for grouping Amazon Q in Connect users. The following is the list of supported criteria values. - ``RoutingProfileArn`` : Grouping the users by their `Amazon Connect routing profile ARN <https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html>`_ . User should have `SearchRoutingProfile <https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchRoutingProfiles.html>`_ and `DescribeRoutingProfile <https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRoutingProfile.html>`_ permissions when setting criteria to this value.
            :param values: The list of values that define different groups of Amazon Q in Connect users. - When setting ``criteria`` to ``RoutingProfileArn`` , you need to provide a list of ARNs of `Amazon Connect routing profiles <https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html>`_ as values of this parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-quickresponse-groupingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                grouping_configuration_property = wisdom.CfnQuickResponse.GroupingConfigurationProperty(
                    criteria="criteria",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__29ad467bcbf64a9ce7a7056818b168b5e373d2ea25459103334981acb63580bc)
                check_type(argname="argument criteria", value=criteria, expected_type=type_hints["criteria"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "criteria": criteria,
                "values": values,
            }

        @builtins.property
        def criteria(self) -> builtins.str:
            '''The criteria used for grouping Amazon Q in Connect users.

            The following is the list of supported criteria values.

            - ``RoutingProfileArn`` : Grouping the users by their `Amazon Connect routing profile ARN <https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html>`_ . User should have `SearchRoutingProfile <https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchRoutingProfiles.html>`_ and `DescribeRoutingProfile <https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRoutingProfile.html>`_ permissions when setting criteria to this value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-quickresponse-groupingconfiguration.html#cfn-wisdom-quickresponse-groupingconfiguration-criteria
            '''
            result = self._values.get("criteria")
            assert result is not None, "Required property 'criteria' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''The list of values that define different groups of Amazon Q in Connect users.

            - When setting ``criteria`` to ``RoutingProfileArn`` , you need to provide a list of ARNs of `Amazon Connect routing profiles <https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html>`_ as values of this parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-quickresponse-groupingconfiguration.html#cfn-wisdom-quickresponse-groupingconfiguration-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GroupingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnQuickResponse.QuickResponseContentProviderProperty",
        jsii_struct_bases=[],
        name_mapping={"content": "content"},
    )
    class QuickResponseContentProviderProperty:
        def __init__(self, *, content: typing.Optional[builtins.str] = None) -> None:
            '''The container quick response content.

            :param content: The content of the quick response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-quickresponse-quickresponsecontentprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                quick_response_content_provider_property = wisdom.CfnQuickResponse.QuickResponseContentProviderProperty(
                    content="content"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bbc837db2935bb8ba68a94a7b51c5172ece37235c44ca2b1dfad732a04eb1154)
                check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if content is not None:
                self._values["content"] = content

        @builtins.property
        def content(self) -> typing.Optional[builtins.str]:
            '''The content of the quick response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-quickresponse-quickresponsecontentprovider.html#cfn-wisdom-quickresponse-quickresponsecontentprovider-content
            '''
            result = self._values.get("content")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QuickResponseContentProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnQuickResponse.QuickResponseContentsProperty",
        jsii_struct_bases=[],
        name_mapping={"markdown": "markdown", "plain_text": "plainText"},
    )
    class QuickResponseContentsProperty:
        def __init__(
            self,
            *,
            markdown: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnQuickResponse.QuickResponseContentProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            plain_text: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnQuickResponse.QuickResponseContentProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The content of the quick response stored in different media types.

            :param markdown: The quick response content in markdown format.
            :param plain_text: The quick response content in plaintext format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-quickresponse-quickresponsecontents.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                quick_response_contents_property = wisdom.CfnQuickResponse.QuickResponseContentsProperty(
                    markdown=wisdom.CfnQuickResponse.QuickResponseContentProviderProperty(
                        content="content"
                    ),
                    plain_text=wisdom.CfnQuickResponse.QuickResponseContentProviderProperty(
                        content="content"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__41295c77edcd7270c3f3a36764ea805915fa2a44214fd58b6530df7e0fac5f07)
                check_type(argname="argument markdown", value=markdown, expected_type=type_hints["markdown"])
                check_type(argname="argument plain_text", value=plain_text, expected_type=type_hints["plain_text"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if markdown is not None:
                self._values["markdown"] = markdown
            if plain_text is not None:
                self._values["plain_text"] = plain_text

        @builtins.property
        def markdown(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQuickResponse.QuickResponseContentProviderProperty"]]:
            '''The quick response content in markdown format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-quickresponse-quickresponsecontents.html#cfn-wisdom-quickresponse-quickresponsecontents-markdown
            '''
            result = self._values.get("markdown")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQuickResponse.QuickResponseContentProviderProperty"]], result)

        @builtins.property
        def plain_text(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQuickResponse.QuickResponseContentProviderProperty"]]:
            '''The quick response content in plaintext format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-quickresponse-quickresponsecontents.html#cfn-wisdom-quickresponse-quickresponsecontents-plaintext
            '''
            result = self._values.get("plain_text")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQuickResponse.QuickResponseContentProviderProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QuickResponseContentsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnQuickResponseProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "knowledge_base_arn": "knowledgeBaseArn",
        "name": "name",
        "channels": "channels",
        "content_type": "contentType",
        "description": "description",
        "grouping_configuration": "groupingConfiguration",
        "is_active": "isActive",
        "language": "language",
        "shortcut_key": "shortcutKey",
        "tags": "tags",
    },
)
class CfnQuickResponseProps:
    def __init__(
        self,
        *,
        content: typing.Union[_IResolvable_da3f097b, typing.Union[CfnQuickResponse.QuickResponseContentProviderProperty, typing.Dict[builtins.str, typing.Any]]],
        knowledge_base_arn: builtins.str,
        name: builtins.str,
        channels: typing.Optional[typing.Sequence[builtins.str]] = None,
        content_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        grouping_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQuickResponse.GroupingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        is_active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        language: typing.Optional[builtins.str] = None,
        shortcut_key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnQuickResponse``.

        :param content: The content of the quick response.
        :param knowledge_base_arn: The Amazon Resource Name (ARN) of the knowledge base.
        :param name: The name of the quick response.
        :param channels: The Amazon Connect contact channels this quick response applies to. The supported contact channel types include ``Chat`` .
        :param content_type: The media type of the quick response content. - Use ``application/x.quickresponse;format=plain`` for quick response written in plain text. - Use ``application/x.quickresponse;format=markdown`` for quick response written in richtext.
        :param description: The description of the quick response.
        :param grouping_configuration: The configuration information of the user groups that the quick response is accessible to.
        :param is_active: Whether the quick response is active.
        :param language: The language code value for the language in which the quick response is written. The supported language codes include ``de_DE`` , ``en_US`` , ``es_ES`` , ``fr_FR`` , ``id_ID`` , ``it_IT`` , ``ja_JP`` , ``ko_KR`` , ``pt_BR`` , ``zh_CN`` , ``zh_TW``
        :param shortcut_key: The shortcut key of the quick response. The value should be unique across the knowledge base.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-quickresponse.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_quick_response_props = wisdom.CfnQuickResponseProps(
                content=wisdom.CfnQuickResponse.QuickResponseContentProviderProperty(
                    content="content"
                ),
                knowledge_base_arn="knowledgeBaseArn",
                name="name",
            
                # the properties below are optional
                channels=["channels"],
                content_type="contentType",
                description="description",
                grouping_configuration=wisdom.CfnQuickResponse.GroupingConfigurationProperty(
                    criteria="criteria",
                    values=["values"]
                ),
                is_active=False,
                language="language",
                shortcut_key="shortcutKey",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__067c5855940164369fb121429e1673fedfb78768ee6ca862e7facdd01b2c15ac)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument knowledge_base_arn", value=knowledge_base_arn, expected_type=type_hints["knowledge_base_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument channels", value=channels, expected_type=type_hints["channels"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument grouping_configuration", value=grouping_configuration, expected_type=type_hints["grouping_configuration"])
            check_type(argname="argument is_active", value=is_active, expected_type=type_hints["is_active"])
            check_type(argname="argument language", value=language, expected_type=type_hints["language"])
            check_type(argname="argument shortcut_key", value=shortcut_key, expected_type=type_hints["shortcut_key"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content": content,
            "knowledge_base_arn": knowledge_base_arn,
            "name": name,
        }
        if channels is not None:
            self._values["channels"] = channels
        if content_type is not None:
            self._values["content_type"] = content_type
        if description is not None:
            self._values["description"] = description
        if grouping_configuration is not None:
            self._values["grouping_configuration"] = grouping_configuration
        if is_active is not None:
            self._values["is_active"] = is_active
        if language is not None:
            self._values["language"] = language
        if shortcut_key is not None:
            self._values["shortcut_key"] = shortcut_key
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def content(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnQuickResponse.QuickResponseContentProviderProperty]:
        '''The content of the quick response.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-quickresponse.html#cfn-wisdom-quickresponse-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnQuickResponse.QuickResponseContentProviderProperty], result)

    @builtins.property
    def knowledge_base_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the knowledge base.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-quickresponse.html#cfn-wisdom-quickresponse-knowledgebasearn
        '''
        result = self._values.get("knowledge_base_arn")
        assert result is not None, "Required property 'knowledge_base_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the quick response.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-quickresponse.html#cfn-wisdom-quickresponse-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Connect contact channels this quick response applies to.

        The supported contact channel types include ``Chat`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-quickresponse.html#cfn-wisdom-quickresponse-channels
        '''
        result = self._values.get("channels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''The media type of the quick response content.

        - Use ``application/x.quickresponse;format=plain`` for quick response written in plain text.
        - Use ``application/x.quickresponse;format=markdown`` for quick response written in richtext.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-quickresponse.html#cfn-wisdom-quickresponse-contenttype
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the quick response.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-quickresponse.html#cfn-wisdom-quickresponse-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grouping_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnQuickResponse.GroupingConfigurationProperty]]:
        '''The configuration information of the user groups that the quick response is accessible to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-quickresponse.html#cfn-wisdom-quickresponse-groupingconfiguration
        '''
        result = self._values.get("grouping_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnQuickResponse.GroupingConfigurationProperty]], result)

    @builtins.property
    def is_active(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether the quick response is active.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-quickresponse.html#cfn-wisdom-quickresponse-isactive
        '''
        result = self._values.get("is_active")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def language(self) -> typing.Optional[builtins.str]:
        '''The language code value for the language in which the quick response is written.

        The supported language codes include ``de_DE`` , ``en_US`` , ``es_ES`` , ``fr_FR`` , ``id_ID`` , ``it_IT`` , ``ja_JP`` , ``ko_KR`` , ``pt_BR`` , ``zh_CN`` , ``zh_TW``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-quickresponse.html#cfn-wisdom-quickresponse-language
        '''
        result = self._values.get("language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shortcut_key(self) -> typing.Optional[builtins.str]:
        '''The shortcut key of the quick response.

        The value should be unique across the knowledge base.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-quickresponse.html#cfn-wisdom-quickresponse-shortcutkey
        '''
        result = self._values.get("shortcut_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-quickresponse.html#cfn-wisdom-quickresponse-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickResponseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAIAgent",
    "CfnAIAgentProps",
    "CfnAIAgentVersion",
    "CfnAIAgentVersionProps",
    "CfnAIGuardrail",
    "CfnAIGuardrailProps",
    "CfnAIGuardrailVersion",
    "CfnAIGuardrailVersionProps",
    "CfnAIPrompt",
    "CfnAIPromptProps",
    "CfnAIPromptVersion",
    "CfnAIPromptVersionProps",
    "CfnAssistant",
    "CfnAssistantAssociation",
    "CfnAssistantAssociationProps",
    "CfnAssistantProps",
    "CfnKnowledgeBase",
    "CfnKnowledgeBaseProps",
    "CfnMessageTemplate",
    "CfnMessageTemplateProps",
    "CfnMessageTemplateVersion",
    "CfnMessageTemplateVersionProps",
    "CfnQuickResponse",
    "CfnQuickResponseProps",
]

publication.publish()

def _typecheckingstub__e4d43de9ccaeb31eba5b0b613ecac25531a87bb9137652388e6196070f4622ab(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    assistant_id: builtins.str,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.AIAgentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daf9bd162ab4eaa6b11972bcaf8372498a47b4ad8cf111130cabfae3f675d2b4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__569f9e85834b9b380045c7e9789b3ac0684022e3b37642b34e232ba9b451ade6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3d8fd38839efd97edc463e08adcbeb6d1b964aa278b19d07017fb40c806bb19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d07c289ddb2abe8b14c5f581386f3377fb7266b5b099c89c1b142b4bbd9d769(
    value: typing.Union[_IResolvable_da3f097b, CfnAIAgent.AIAgentConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b90fdd18e60e92e1589e2bf61b55c6cd7758b9da5e26d00525cb08a2ad13830(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6380f3badbada0c208691bd5242dfabe1122f10b446d77f1ae5ad0c9da456ae8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__982490f39ff188d23898421a1623ad1489db32be592625d58e01c368c7568247(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e3ed01afbf4aa2c01303d467dcbf5c5cd3fb267902b917f3c4f5fdd0d83ccdc(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cb84ad0dc27ffdae65e4e739c98ea6a4e7c36340f15c21ae83a2225ff763ba3(
    *,
    answer_recommendation_ai_agent_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.AnswerRecommendationAIAgentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    manual_search_ai_agent_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.ManualSearchAIAgentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    self_service_ai_agent_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.SelfServiceAIAgentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6847cf788b7def362d576a512b579b2a08c25837003298b7c57254d1dfb45112(
    *,
    answer_generation_ai_guardrail_id: typing.Optional[builtins.str] = None,
    answer_generation_ai_prompt_id: typing.Optional[builtins.str] = None,
    association_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.AssociationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    intent_labeling_generation_ai_prompt_id: typing.Optional[builtins.str] = None,
    locale: typing.Optional[builtins.str] = None,
    query_reformulation_ai_prompt_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c351d3e3386a19a82d6920c115ac6f8c911a12da4a117a9c0676a8ff0038fd41(
    *,
    knowledge_base_association_configuration_data: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.KnowledgeBaseAssociationConfigurationDataProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2df56062b7b8c55a883d0469e63c3aad05d8079bf21171f13f4e68d2f26fea44(
    *,
    association_configuration_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.AssociationConfigurationDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    association_id: typing.Optional[builtins.str] = None,
    association_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af25ecdf7592033a618b9a411d145fb2bd7b10ae3e9b0a04a4502e0dee139e27(
    *,
    content_tag_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.TagFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_results: typing.Optional[jsii.Number] = None,
    override_knowledge_base_search_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3346eba3a05ad4b31350bf2c54edbb6063a18cfea8a25ebbab80c402438f039a(
    *,
    answer_generation_ai_guardrail_id: typing.Optional[builtins.str] = None,
    answer_generation_ai_prompt_id: typing.Optional[builtins.str] = None,
    association_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.AssociationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    locale: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf2bbad68aea63c5546563872782e30b131382ddae5fbabf04602b928494d4d4(
    *,
    and_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.TagConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tag_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.TagConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0833e248a2b0215b05dd66ce2879efe35c5180b459e725cf02acb524808c7ec(
    *,
    association_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.AssociationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    self_service_ai_guardrail_id: typing.Optional[builtins.str] = None,
    self_service_answer_generation_ai_prompt_id: typing.Optional[builtins.str] = None,
    self_service_pre_processing_ai_prompt_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76535774a57202e416fb208d73c095c91408f65fd8a1b99f6b568fd994b915e9(
    *,
    key: builtins.str,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47961a691b994d09a0537dc7d655a0aab653585a5e8bd78b30c4bc84ec243c19(
    *,
    and_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.TagConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    or_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.OrConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tag_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.TagConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1cda9a6282ec07c28c0ef49efdf8da8f079052d26edd32bbe15324644982756(
    *,
    assistant_id: builtins.str,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIAgent.AIAgentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa5a166c3d658d9410f80c3ff44a4aee88b29cb4def5f6c7d811c5b47f5ffb68(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ai_agent_id: builtins.str,
    assistant_id: builtins.str,
    modified_time_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eec3c0a8aee757b615051ab77f3708fef64acd48758d58f7b8801c7073f3ea55(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eec2d46406b6deb09ae2fc5f30e9bb5223c8f293091f02f7d13f928906953a1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df356486e6fdad853cdc4c3aa5d62a5febffd1441d8e82f3a672bf4aef6e809d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c00eedc618755e116ec4cf13129b9ecab51c03e0aa3285aa6c4eca0e7c9311(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cbb04d6951221f1cfd98bc4ebed42ba72b9f79a3ef0707bfcea622572f06cd2(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ce55b0c69b9bc58cfcaeadaff04d7986170a5f73af9f6157ba1fe19c79b250e(
    *,
    ai_agent_id: builtins.str,
    assistant_id: builtins.str,
    modified_time_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76ea8e26c58eaed3d156b1860dd33693ef608e81ac9c96aa849d3236df58330b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    assistant_id: builtins.str,
    blocked_input_messaging: builtins.str,
    blocked_outputs_messaging: builtins.str,
    content_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.AIGuardrailContentPolicyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    contextual_grounding_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.AIGuardrailContextualGroundingPolicyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    sensitive_information_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.AIGuardrailSensitiveInformationPolicyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    topic_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.AIGuardrailTopicPolicyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    word_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.AIGuardrailWordPolicyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fbdc5de28d3c991f79f98e3c345ade75e45ce50bdb72f64634f0031d019b3e0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71dcd22a9ef76aa3a7c280a922b91cc6f9cd7b114a93623bb44dbc112e60ec54(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24f61192b3941f9e6c1d63e119a6d1f1ac8e4e31bfb9beda991736af85ba7edc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a3f10e3678233e9583c04468dd2fa9082d1099e59298bafe2cbef0c5d3a0a58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab881749cd994050fdfe9190c2ad83d2d5995d553667532d5b3046c5784f3a46(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af0b681055aef2365d977a2adefd9d9d8538dd4e7497bed81a040c4d3e6d1013(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAIGuardrail.AIGuardrailContentPolicyConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6f963ab8c2eace9b626eca75747edc1eef5302cb2ca185e3c17ef190404aa68(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAIGuardrail.AIGuardrailContextualGroundingPolicyConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13bc08d099c391203a59ca71c4b7738f433a55e9dce1b3ec45bc792ea35be252(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5074d801992ea9ab774216aab1356ca4243d514bdf42abc16be1a957239bdca(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e94179fb829e66c40130c72071c91ec85dbd64f5e3e9cbe35c4966a40c3fefda(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAIGuardrail.AIGuardrailSensitiveInformationPolicyConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c295406d2cf871f486448002b556c3b63d9432e2114674011371326c1ba7c1b(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8bb338f6da5f73bdb4820c73ee887f612953bf85b2d8bd54e7541ea081f4f53(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAIGuardrail.AIGuardrailTopicPolicyConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f41825c818a79784ab378059125875eeee0524136b34267aa4caca170457da14(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAIGuardrail.AIGuardrailWordPolicyConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3b7764340b5366a000b7609f9e6c1b7857f2afd9dca723fd492a1e331b82b32(
    *,
    filters_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.GuardrailContentFilterConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8b3e67068f407c2f3042d1380119651fa9edd8b97c312dbce41168ba5036ce3(
    *,
    filters_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.GuardrailContextualGroundingFilterConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1019f2767cdb75a66ac9e6dbb808d33ced4e1d098b227029ca4e8aaace98331(
    *,
    pii_entities_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.GuardrailPiiEntityConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    regexes_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.GuardrailRegexConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9fd7602104f512891874b785e4236b2dd9131ea684d5c3e16792b3e5f9a3767(
    *,
    topics_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.GuardrailTopicConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddb251dfe6c0ff4b7a273bddeb253f5fc859e92197286c2d46566bdebdb6837d(
    *,
    managed_word_lists_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.GuardrailManagedWordsConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    words_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.GuardrailWordConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e47d1e764075659f79a8e65f93d2613f269a815edddfaa5255b97587dc9f2a91(
    *,
    input_strength: builtins.str,
    output_strength: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57e4e4233989e39271f6f5b1254ba49184eaf97a79f1df28337cd59a6a5ce09f(
    *,
    threshold: jsii.Number,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfc19deb6dd371180a4bb8d9f0990f6132afb22d46b71ae1e32e4ffdbe4ef567(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c764d4acc62cb140dda0e1c7dbd2f6738df34c8fb43ef4cf0d9a9941f03af4c1(
    *,
    action: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a28c8495c26410e3b614188ff183453c712c882484a101d2d68ce3d2a925385(
    *,
    action: builtins.str,
    name: builtins.str,
    pattern: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__925705bff59beafe6b6eee70065213b10cb0a6047a45adbdaf25fa9a8b0ee5cf(
    *,
    definition: builtins.str,
    name: builtins.str,
    type: builtins.str,
    examples: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__606553234f4510e4e970f7df37efccc44b1516de671a981777f6102615e8243d(
    *,
    text: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__272934bdd57f29fc5c93ba393c351f7b04e959a7a6be0e13591e187bd90df3aa(
    *,
    assistant_id: builtins.str,
    blocked_input_messaging: builtins.str,
    blocked_outputs_messaging: builtins.str,
    content_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.AIGuardrailContentPolicyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    contextual_grounding_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.AIGuardrailContextualGroundingPolicyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    sensitive_information_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.AIGuardrailSensitiveInformationPolicyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    topic_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.AIGuardrailTopicPolicyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    word_policy_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIGuardrail.AIGuardrailWordPolicyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a9a92a95cf92d95c08e9a7abc4202740081918bf2082c415b59e8a388ed1ceb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ai_guardrail_id: builtins.str,
    assistant_id: builtins.str,
    modified_time_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce87f6cc038ae50940e8317ea6eb15fb4755952543358f516cfb8178eb844887(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb4398a8c6a20907582fa6297d25cfd57e7cd74c3d99a7d32fa8f1476c4ba7f4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a553f580b0f104a026581e9450d365d429441d11d53e610beb7a35a5229aedf5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad42f08834e2762e6f546d5167e6c7dccf9f639bbf36d9596aa7a154f6898e41(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94c07d3aa9bfd5fbb498b3a8c9f38b60219be42b9521625f0f8d680e6206d6ee(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a99128fc6202c08bbbe787b73cc8f6fe79376afb6a408a1c3b9f1d86295794b(
    *,
    ai_guardrail_id: builtins.str,
    assistant_id: builtins.str,
    modified_time_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48a265f7ec519ced4028dd8e69d5a1fe8ef89d36b11d693c968f74c8be6bb9df(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_format: builtins.str,
    model_id: builtins.str,
    template_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIPrompt.AIPromptTemplateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    template_type: builtins.str,
    type: builtins.str,
    assistant_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7567e2bb6113fabf7ae624801bcdbbfa2507650c0fcedb4572ac328601553fcc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c65608208361b5449f96e9e897202e481d956b960bbccf8366c60dac3e4bd70(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6643cec138a765effc7d182e3db5b09b1ddb19205b800c1f517cbed5e73488b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be2ea2c4f381a43b0574cf9f6fdcace2ba70655e5f3ebd78fd5e8c4541b05982(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5419aa0c5422844ff34f9fc9a194021532fa6ada449722bb2aa4b846530445ba(
    value: typing.Union[_IResolvable_da3f097b, CfnAIPrompt.AIPromptTemplateConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e4b3aeb8d77c711927acf1f94798cc7b4e483f8fc8bc95ae0b322f2c18a51f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3f45400801eabea6672075f9e78a389daf48244d79b0b5601339aad9840939b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5634dda4bc6094fc31dbde0ffceab32283f49a381e6e026ed12c76738e89fe5e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aab971aeb8e18c48f506a9f2350fb427745d11ff1d792a38763843c7c52200b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c8237463d9724c409122f49c9b69b5a1e0f429714ecc37326da2fb2d24ac916(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebc135e5b323c7d3a33dd614d94d6bb8425982f46dc4aafee23df90fac59a460(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5c009da191a8948caab2f589b801cb2b5b6bd6f17d15c830bfcc3eac735974e(
    *,
    text_full_ai_prompt_edit_template_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIPrompt.TextFullAIPromptEditTemplateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aab519c6a13d7d17f031944b9ddc67f7d24074f5ba48e4816f1ba2dfd7883ffc(
    *,
    text: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a55de2153828f44950073a28af3416601dc1f09105d3fa9d8f1ec243b3822d3(
    *,
    api_format: builtins.str,
    model_id: builtins.str,
    template_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAIPrompt.AIPromptTemplateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    template_type: builtins.str,
    type: builtins.str,
    assistant_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__729db38c828e5e73ae0386aea45298b479e1a069777600fadadd338035a13e5d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ai_prompt_id: builtins.str,
    assistant_id: builtins.str,
    modified_time_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb551060d0407b951291352d04af15e21651dd34a52774e39a2d2da6e4df3220(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b234db791908c37519c8ae3284494dc43affe3bad0ab4eadab6407ef7ccc7627(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad29e2ee6fad75de44645890c2c623b9ccb35a02f6e75d7ed98fa3b7337272ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b6982f0f13d49bf234e47082e4a9783bc461e6dc18d68737a370a3682f93b48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1f64ffa51639af07e9712d95780a238db8bd368a440a159ead5f0364951dcd4(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39068faf047cdd2f1dce0d86adaff6f71058bba08c161da563b36647959f2add(
    *,
    ai_prompt_id: builtins.str,
    assistant_id: builtins.str,
    modified_time_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8078b7e28a17a68ab6f3d362e7de3af6b6867207690b2b344e35797cd6569746(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistant.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67a0860b53a1867e3124a155db57aa1ab8bbb2d50c48a1553f8766101996d0b8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a17095196842a083c7a71c961443f89f6d1dd766154e06248d10cdee66b0113(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ded25c09bd072cbcb02cdfdf40580d154663664980378f96c5210edc137dd8c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c131b16ef6a21690f65d4e643bc0f04ea3e1fa9afd2bbf0e89a9bd4b96032657(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17115c2ceb35036c54e25dfa13fd4465303e5a759aae943761c84163427b74ed(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb8470e364668ea9060baa4a3306507e0ded02773f75cc435d33474d30577d1b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAssistant.ServerSideEncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a82c89946835215b7304a7033eacc23c202ee6ae8e17e73d0ba34f1dbaf1416(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa78e1cc313485ba353b8f1dc8b01c69bcdd1c5bcecd204b9778596de1e4a07d(
    *,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17f6f8491bb7be7dab63c57bf64b65f643c4fece381b02f49002f796c7a8f0f9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    assistant_id: builtins.str,
    association: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistantAssociation.AssociationDataProperty, typing.Dict[builtins.str, typing.Any]]],
    association_type: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a96af34ce4ed10cd5d626bf5df7799b86ca3023d4f6b302c0cdb51a0bdd1274(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e84fe37792368fc9821204b49ed0d6e13642f35bcdc7bb2676de0ee949767075(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c72c215a467df1527e01f95d41dc85287728a80fa94729b3ff14b2b1312fb30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e46eeb6364ccf0b8f92618927437f56df6248417cb401c056b83fe5692feb0f8(
    value: typing.Union[_IResolvable_da3f097b, CfnAssistantAssociation.AssociationDataProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48fcb269f8dde8b147d1a0d7681e40817cb35b599f00a24aff263a84df4cea90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea3d3cb4fe1048c256fc8719ac3d18f47cb21ef29730dd9d1f53a9304ccd4030(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6ecf0cfb2eb97624a8ec4ab51e16f75cfa1a5397890274252a2621ff5ad378d(
    *,
    knowledge_base_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__419e70156a249f4fa2bea77a71d532fe9a351e3d150b5939dc8455b174375514(
    *,
    assistant_id: builtins.str,
    association: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistantAssociation.AssociationDataProperty, typing.Dict[builtins.str, typing.Any]]],
    association_type: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2f6978729a0bccb7cc077df26ee5d379812791b9fe7ec0622251ed958562e07(
    *,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistant.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99512a2eb8a3e47802b889aac668fc94bdc0534ee683313dac712b20006ea6ed(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    knowledge_base_type: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    rendering_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.RenderingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vector_ingestion_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.VectorIngestionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e12fde615d3c7854b4e97326fea29e89d837485efe274039378606ee08a4be76(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__198b767f5d7e7dce9b330a5c5c43441fed236182c59b06b0be2da034b14ce256(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93bc0b75027c2aaed7afea32df7bbe9ea25daf054d032e869d4b65d3c73427e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06da4251d33a92a96fd91655710caf394cf4fa6fe728e86b20be47c80f50c450(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8e87e39918fdfb349935e6c5b5b76307ecd838c21583fab217f7d88ca3ea67c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dbfe6a279891a574d7128da28db41ca74ec109e76fb61b5b9db27b1ee815fba(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.RenderingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__221e4b62cf601d8c0e6300aceb9f7a7bfe38ac19093345137be6abb3f22756d8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ab7292e64b294c529dec00a33cfb2da96ff80581b3e1376c67027a944849691(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.SourceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b654968450798e9434ae157e80b0efdde965d3d9cf517c41c4fcdcfa66e910f8(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__841ed99c710bd0f2748a34efe9978e0d2cadafde4697b94a4cfbf0d401c23ee2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.VectorIngestionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb5af4edc537ecd6b5dab081c90708156852ccef10f7a6228ff445f6dc0e509c(
    *,
    app_integration_arn: builtins.str,
    object_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3357d1d4f3808129b0987d8a651abe6fce2d6e99ac83ee764b51bcb69af90bfa(
    *,
    model_arn: builtins.str,
    parsing_prompt: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.ParsingPromptProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d95119d30e49d5bd11aadde5636c2dcecbffe3cd3f2559414b0a1fc6d4a6af3(
    *,
    chunking_strategy: builtins.str,
    fixed_size_chunking_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.FixedSizeChunkingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hierarchical_chunking_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.HierarchicalChunkingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    semantic_chunking_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.SemanticChunkingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e3c61c31746c21216c5087b3b9c0ff8b6a3720c51cb749cc9b8ac907b6269dc(
    *,
    rate_limit: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e64775237b79e7f336be4b1d76a0ab710432dde63badb3a5752cee09b6d6fcae(
    *,
    max_tokens: jsii.Number,
    overlap_percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2e75b2aebff3c68af11b908941d1e187a79a951b58f0a33b152f1ab00053e49(
    *,
    level_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.HierarchicalChunkingLevelConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    overlap_tokens: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b80446f3a787de6c7b48fad975fa7ee10b8ee51af79a599756b923e9991e203f(
    *,
    max_tokens: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01b279dc3cda96328b8095cb5a3f31cb31404d26a7e228390580d93bf073de89(
    *,
    web_crawler_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.WebCrawlerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc6bf4b7f99a7762951f3f88a8d67827d0e4117b574284c21f89ea4ed59edb2f(
    *,
    parsing_strategy: builtins.str,
    bedrock_foundation_model_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.BedrockFoundationModelConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05d68dd54deb469c741ebfe8562286929c13c3a79aeac89ec4266aac6399b98e(
    *,
    parsing_prompt_text: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc0b3350c030b63153dd14a7ab6b7c686549027289e97b41678c46c5c9bce0d1(
    *,
    template_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f5d22aa2f115decf996bdbc44327658efeadecefcf31ed94de1f632c99c4226(
    *,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37473100b67c3634da11f7c1327c6358310e63403f4bba0df82c4eabeeae71df(
    *,
    breakpoint_percentile_threshold: jsii.Number,
    buffer_size: jsii.Number,
    max_tokens: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0cd7e6721b8c282e7e8effcea12ef5d59096c2d9eb9611a2269ac2deff0e697(
    *,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__169c34939e73e3c8ce81d921898915b159d4e29ad0c3757e50950775728d0aa0(
    *,
    app_integrations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.AppIntegrationsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    managed_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.ManagedSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71e0a652750aa86f6181cd7e7b6bae1e590e2b69e5632dac0497da6c702900f9(
    *,
    seed_urls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.SeedUrlProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8cf77ffdab289f4029f153e2fd852680c5cf76c8d875df505957acb18dd433b(
    *,
    chunking_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.ChunkingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parsing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.ParsingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b62d94eb7bc7c732098a29bd2a5de83daa71f6616ea1433becc1240c16c3e6a(
    *,
    url_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.UrlConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    crawler_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.CrawlerLimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    exclusion_filters: typing.Optional[typing.Sequence[builtins.str]] = None,
    inclusion_filters: typing.Optional[typing.Sequence[builtins.str]] = None,
    scope: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b2c89f78d66a3c10ed4851c5bc420028f69cc91ddabbe2ac038dd7332ea1edd(
    *,
    knowledge_base_type: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    rendering_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.RenderingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vector_ingestion_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.VectorIngestionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d99067595817364fbb03fa017437b616b3c32bdfb38c386a909328ac78d1053(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel_subtype: builtins.str,
    content: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.ContentProperty, typing.Dict[builtins.str, typing.Any]]],
    knowledge_base_arn: builtins.str,
    name: builtins.str,
    default_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.MessageTemplateAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    grouping_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.GroupingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    language: typing.Optional[builtins.str] = None,
    message_template_attachments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.MessageTemplateAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bd3a69fd8e8039386e9bb281e08fdde1b7575eb0f4584620df31d2602466d2b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51e5807f3469c5509115f0174d0a4a4e94bf8231cc93e8f0094c9c6a9a4b8671(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9a491239929796de387804b5ffabbcc9d2d80c46187061bad6dbd69cb644824(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ee7a5f3ae13619e783db2bde4848cd5e3d84a6c38e5cf0e040a3d6810a2b619(
    value: typing.Union[_IResolvable_da3f097b, CfnMessageTemplate.ContentProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1089af8f7f43591721a256e0bcbb3a3e75172ab965d8e37a20d563d96fea6c7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d2ebd98b6a5c07a0bfd2e4c013c178b5a1cdc3388149770a1a36251b5b6e6e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c90c4e95d1b7bc695fb4935b1c99d447bbd24e9da4bc0367c93bcfe1269fbe2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMessageTemplate.MessageTemplateAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f18337bd9aa5b9f46e3c5167353a0544735c7f2633460e6e48392e441c4c1ba(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a293700b704f958a326ada96bec14e09605f0a2af76a1972e28306ecd1c0bea9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMessageTemplate.GroupingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4bfbbc60d2eb951b3081015f23b57de459d734cb6ca7e17db3b5ea28887251d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99e58f577d070d3c392b7519e6ec169337ff707d8d0fbec1d5b147b3eb27b11a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMessageTemplate.MessageTemplateAttachmentProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a8749d4385c7e2fd758f8b86ee5b36af0b25c3e531a4c7936791aa080a35421(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19e932a438b8adf98a2f01a0c01e6402cbbcee9d65521d2cf7fd141793378561(
    *,
    first_name: typing.Optional[builtins.str] = None,
    last_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d47d957dda4da1971b35706dec828b7fec81d445218ea14dbd7300f581ac052(
    *,
    email_message_template_content: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.EmailMessageTemplateContentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sms_message_template_content: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.SmsMessageTemplateContentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31a9d5f6219c52f900443be7cd1a4f580db25aaf647c7876e4062d152500f342(
    *,
    account_number: typing.Optional[builtins.str] = None,
    additional_information: typing.Optional[builtins.str] = None,
    address1: typing.Optional[builtins.str] = None,
    address2: typing.Optional[builtins.str] = None,
    address3: typing.Optional[builtins.str] = None,
    address4: typing.Optional[builtins.str] = None,
    billing_address1: typing.Optional[builtins.str] = None,
    billing_address2: typing.Optional[builtins.str] = None,
    billing_address3: typing.Optional[builtins.str] = None,
    billing_address4: typing.Optional[builtins.str] = None,
    billing_city: typing.Optional[builtins.str] = None,
    billing_country: typing.Optional[builtins.str] = None,
    billing_county: typing.Optional[builtins.str] = None,
    billing_postal_code: typing.Optional[builtins.str] = None,
    billing_province: typing.Optional[builtins.str] = None,
    billing_state: typing.Optional[builtins.str] = None,
    birth_date: typing.Optional[builtins.str] = None,
    business_email_address: typing.Optional[builtins.str] = None,
    business_name: typing.Optional[builtins.str] = None,
    business_phone_number: typing.Optional[builtins.str] = None,
    city: typing.Optional[builtins.str] = None,
    country: typing.Optional[builtins.str] = None,
    county: typing.Optional[builtins.str] = None,
    custom: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    email_address: typing.Optional[builtins.str] = None,
    first_name: typing.Optional[builtins.str] = None,
    gender: typing.Optional[builtins.str] = None,
    home_phone_number: typing.Optional[builtins.str] = None,
    last_name: typing.Optional[builtins.str] = None,
    mailing_address1: typing.Optional[builtins.str] = None,
    mailing_address2: typing.Optional[builtins.str] = None,
    mailing_address3: typing.Optional[builtins.str] = None,
    mailing_address4: typing.Optional[builtins.str] = None,
    mailing_city: typing.Optional[builtins.str] = None,
    mailing_country: typing.Optional[builtins.str] = None,
    mailing_county: typing.Optional[builtins.str] = None,
    mailing_postal_code: typing.Optional[builtins.str] = None,
    mailing_province: typing.Optional[builtins.str] = None,
    mailing_state: typing.Optional[builtins.str] = None,
    middle_name: typing.Optional[builtins.str] = None,
    mobile_phone_number: typing.Optional[builtins.str] = None,
    party_type: typing.Optional[builtins.str] = None,
    phone_number: typing.Optional[builtins.str] = None,
    postal_code: typing.Optional[builtins.str] = None,
    profile_arn: typing.Optional[builtins.str] = None,
    profile_id: typing.Optional[builtins.str] = None,
    province: typing.Optional[builtins.str] = None,
    shipping_address1: typing.Optional[builtins.str] = None,
    shipping_address2: typing.Optional[builtins.str] = None,
    shipping_address3: typing.Optional[builtins.str] = None,
    shipping_address4: typing.Optional[builtins.str] = None,
    shipping_city: typing.Optional[builtins.str] = None,
    shipping_country: typing.Optional[builtins.str] = None,
    shipping_county: typing.Optional[builtins.str] = None,
    shipping_postal_code: typing.Optional[builtins.str] = None,
    shipping_province: typing.Optional[builtins.str] = None,
    shipping_state: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__594c1bc5995ee95767b5cc83468d73e0803b33cd404adbe242bdf2932351cf22(
    *,
    html: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.MessageTemplateBodyContentProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    plain_text: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.MessageTemplateBodyContentProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7215403540c347569227a7338deac451582c85e88a78a4272e4cd57567766c7(
    *,
    body: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.EmailMessageTemplateContentBodyProperty, typing.Dict[builtins.str, typing.Any]]],
    headers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.EmailMessageTemplateHeaderProperty, typing.Dict[builtins.str, typing.Any]]]]],
    subject: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13ed2a2205dc124617ee1edcae036a820325172941596023510196fe54baf556(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe8ac046ae2df337296b1f5a22706eb034910def9d9a88cab8bf76dbc739dd08(
    *,
    criteria: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__733b704f810bd9a3eb9d75f4f3b82b249fd0f3b3c3429da2875584133affc320(
    *,
    attachment_name: builtins.str,
    s3_presigned_url: builtins.str,
    attachment_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94be2b3e247d65fdf9ede2a9ef720965133047f24bfea2e9cda8dddc0b98feb1(
    *,
    agent_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.AgentAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_attributes: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    customer_profile_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.CustomerProfileAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    system_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.SystemAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91e161e5190bc28f3ba5b1a8df2e1101ff4f45bfe209c74195160cd328f28814(
    *,
    content: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9ffc2cd4d7675f6b77015f221bf2163943c73ed8bc184e5c43f47d33dc83715(
    *,
    plain_text: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.MessageTemplateBodyContentProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5996259411eb96bb9d7a8aaecb5f716307ce93390a851bca361b510ec852f0e3(
    *,
    body: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.SmsMessageTemplateContentBodyProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd590492f1b15737eb4d99b87e845ae5b578516dd6a202c1c00f10d883c4606f(
    *,
    customer_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.SystemEndpointAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    system_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.SystemEndpointAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a331097c8b523e827ded8e1b2307d25adea67abd59cd8f02120521fb1bcec13e(
    *,
    address: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec25e0f87d8fdbd9dfa333317dee4b1a02318078d19b7a6a2b5abe02825ec475(
    *,
    channel_subtype: builtins.str,
    content: typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.ContentProperty, typing.Dict[builtins.str, typing.Any]]],
    knowledge_base_arn: builtins.str,
    name: builtins.str,
    default_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.MessageTemplateAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    grouping_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.GroupingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    language: typing.Optional[builtins.str] = None,
    message_template_attachments: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMessageTemplate.MessageTemplateAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74fb30e95cf0983e689b729ce7c37f315a3a89ee72eba30c0076157947593055(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    message_template_arn: builtins.str,
    message_template_content_sha256: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fdcf0b0fc316f9964e2a8f50d95ef92efe9e07b4a9d5ef74b7c3ca6257dc206(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ac027a7bca9f313df16a3ac8bc0b9a8b1f796ce03d79d5eb49d64dd963e9c8c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08418dbc91726be614a7891204fe619271f6618bccf8511f3e62a4f02edd6fb9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2add34eec806e4ffcc1182689dc4344729a80e6faab1ee1e72aafe25168cddeb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0b2a184adf6bc572d2575c7f11c4caa1ebc990936a7af469c6f91288d5f2908(
    *,
    message_template_arn: builtins.str,
    message_template_content_sha256: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ea732c0aa1c75214dd603b6887da6352fe66fd3d98e2168fdc3654ffd9d1629(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    content: typing.Union[_IResolvable_da3f097b, typing.Union[CfnQuickResponse.QuickResponseContentProviderProperty, typing.Dict[builtins.str, typing.Any]]],
    knowledge_base_arn: builtins.str,
    name: builtins.str,
    channels: typing.Optional[typing.Sequence[builtins.str]] = None,
    content_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    grouping_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQuickResponse.GroupingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    is_active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    language: typing.Optional[builtins.str] = None,
    shortcut_key: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d749875d4fcc7d4242bef84ff9a9085b8827dd339b292a8c0429c8dd8b8f394a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55603fa5b935508baa2dfab5656797245339ea337e135b1dc21a3a68319e401a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9dfed0b86363ddee2b73b59a4f8b9559cdd5914e6289f92f15feac8409c416b(
    value: typing.Union[_IResolvable_da3f097b, CfnQuickResponse.QuickResponseContentProviderProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2144e7491ad5d7946aab6f020cc3753c00cd404c7ff07340ab3cd7d070d37993(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5165c48c2f03231e6cd852d113854e793302bd6e08d080e9cccd919f79e3565e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e83f69c01eda758c5d6ec662eb36e57ab3b0b525a49f25b680b666ab899f00be(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6492a4d7ba49b236142344d0d0c57fc6ca8829e7d6ecf3259503a67f78948deb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7acfcd0f2c542ee39a59469bc0ea12f5507951f336da00fcd37146edb79dc73(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ec3f31a69e16fce2ffc00474e1f2852bd0e753c6a3e973b7255a9d4d7f64a45(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnQuickResponse.GroupingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d8198e1c8f2c5b8c3703976122f2d1b18fe79607316aa0a9b449b4cd01026e9(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6278f29e4c31c723a6c5cf2bf58f08721883768d361fa4186d576bffdeb71902(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a0dc9541d897c6f038624fe355ba3d2374e8c28f367a9049dd7553a8b466138(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2727d6beae8f791672bb80625961e3def8262f5b47864ede2817419f60527d6a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29ad467bcbf64a9ce7a7056818b168b5e373d2ea25459103334981acb63580bc(
    *,
    criteria: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbc837db2935bb8ba68a94a7b51c5172ece37235c44ca2b1dfad732a04eb1154(
    *,
    content: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41295c77edcd7270c3f3a36764ea805915fa2a44214fd58b6530df7e0fac5f07(
    *,
    markdown: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQuickResponse.QuickResponseContentProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    plain_text: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQuickResponse.QuickResponseContentProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__067c5855940164369fb121429e1673fedfb78768ee6ca862e7facdd01b2c15ac(
    *,
    content: typing.Union[_IResolvable_da3f097b, typing.Union[CfnQuickResponse.QuickResponseContentProviderProperty, typing.Dict[builtins.str, typing.Any]]],
    knowledge_base_arn: builtins.str,
    name: builtins.str,
    channels: typing.Optional[typing.Sequence[builtins.str]] = None,
    content_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    grouping_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQuickResponse.GroupingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    is_active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    language: typing.Optional[builtins.str] = None,
    shortcut_key: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
